---
name: QA at REAL Safari Viewport, Not 1920x1080
description: NEVER declare a slide viewport-safe based on a headless 1920x1080 render. Safari's tab bar + URL bar + bookmarks eat 100-200px from the window. Render at 1440x680 to 1440x760 to simulate what users actually see.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
NEVER declare a slide viewport-safe by checking a headless 1920x1080 render. Safari's chrome (tab bar + URL bar + bookmarks toolbar + optional address bar) eats 100-200px from the top of every window. A slide that fits at 1080px tall will CUT OFF in real Safari at 720-900px tall.

**The exact failure pattern (2026-04-13):**
After the previous viewport-overflow fix on slide 7, I audited slide 4 at 1920x1080 and called it clean. Timo opened it in Safari and the eyebrow "HERE'S WHY →" was clipped off the top of the viewport. Flexbox centering (`align-items: center; justify-content: center`) pushed content outward equally when the slide's total height exceeded the actual Safari viewport — the overflow hit BOTH top and bottom, hiding the eyebrow.

Timo: "still a fucking issue see how the text cuts off, why is this happening still"

My 1080px render didn't simulate Safari's real viewport. Slide 4 had:
- Eyebrow (~30px)
- Big headline (3 lines at 54px clamp = ~180px)
- Bullseye image (200px)- Paragraph (3 lines at 24px clamp = ~110px)
- Complication card (~100px)
- Total: ~620px of content + margins ~180px = ~800px

Fit at 1080 (fine, 280px slack). Overflow at 760 (40px too tall). Overflow at 680 (120px too tall).

**The pipeline that actually catches Safari overflow:**

1. Build the slide.
2. Render at MULTIPLE realistic Safari heights:
   ```bash
   for H in 680 760 820; do
     /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --screenshot=/tmp/slide-h${H}.png --window-size=1440,${H} --hide-scrollbars --virtual-time-budget=2500 "file:///path/to/slide.html"
   done
   ```
3. Read each screenshot and verify:
   - Top element fully visible with ≥20px margin above
   - Bottom element fully visible with ≥20px margin below
   - No flexbox "push outward" overflow
4. If overflow at 680, shrink content. If overflow at 760 but fits at 820, borderline — still shrink. Only 680-clean counts as passing.

**Safari chrome heights to budget for:**
- Minimum Safari window (no bookmarks, tabs hidden): ~80px chrome, usable ~1000px from 1080 window
- Standard Safari (1 tab row + URL bar): ~120px chrome, usable ~960px from 1080 window
- Safari with bookmarks bar: ~160px chrome, usable ~920px from 1080 window
- Small Safari window (common for demos/presentations): often 800-900px window → usable ~680-780px
- **Default target: design for 680px usable height.** If content fits there, it fits everywhere.

**Content budgets at 680px usable height (after 6vh*2 padding = ~80px):**
- Total content ~600px
- Hero headline at clamp(22px, 3vw, 44px): max 2-3 lines
- Secondary text at clamp(14px, 1.55vw, 20px): max 3-4 lines
- No decorative icons larger than 120px unless they REPLACE a text block
- Callout cards: max 2 lines, ~14px padding

**Specific cuts that bought me 200+ px on slide 4:**
- Removed bullseye image (saved ~220px)
- Shrunk headline clamp from (26-54) to (22-44) (saved ~20-40px)
- Shrunk paragraph clamp from (16-24) to (14-20) (saved ~10-20px)
- Shrunk complication card font from (18-30) to (15-24) (saved ~15-25px)
- Shrunk complication padding from 20px/32px to 14px/24px (saved ~12px)

**Why I kept missing this:**
1. Headless Chrome defaults feel authoritative. "1920x1080, looks clean" sounds like "this is how it renders everywhere."
2. I never checked what Safari's actual chrome height is. I assumed 100vh = 1080px of usable space.
3. My viewport-overflow memory (`feedback_viewport_overflow_check.md`) prescribed checking at 1920x1080 — which is the WRONG target. Updating it implicitly here.

**How to apply:**
- For every slide, render at **1440x680** minimum. If passes there, also check 1920x1080.
- For hero-heavy slides or image-heavy slides, render at THREE heights: 680, 760, 820. All three must fit.
- Never ship a slide based solely on a 1920x1080 render. That's a false-pass.
- When user reports overflow, the fix is usually: shrink headline clamp, remove decorative image, tighten margins — in that order.
