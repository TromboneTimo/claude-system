---
name: Viewport Overflow — Check Pixel Fit, Not "Renders Cleanly"
description: NEVER declare a text-heavy slide done by checking "does it render." Slides using .split / two-column layouts must be checked for overflow at exactly 1920x1080. Text that exceeds the viewport height disappears below the fold and the user has to tell me.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
NEVER run visual QA on a text-heavy slide by checking "does it render cleanly." That criterion is too weak. The real check: "does every pixel of content fit inside the 1920x1080 viewport, including the bottom-most characters?"

**The exact failure pattern (2026-04-13):**
Slide 7 of views-that-matter (Problem 02 — Distribution) had its closing kicker line cut off at the viewport bottom. I had rendered the slide earlier, read the screenshot, and said "looks good." What I actually checked: that text was visible, the layout wasn't broken, the image rendered. What I FAILED to check: that the LAST line of the kicker was fully visible within 1080px. It wasn't — Timo's feedback screenshot showed text flowing off the bottom.

**Why "looks clean" is not sufficient:**
- Screenshots at --window-size=1920,1080 show what fits. Text that overflows disappears below the frame. I don't SEE the cut-off because it's not in the screenshot.
- My pattern-match for "looks clean" rewards presentation, not completeness. A text block that's been truncated by overflow LOOKS clean in the screenshot — the remaining lines are well-formatted.
- The only reliable check is character-by-character verification that the LAST line of source text is visible in the rendered frame.

**The pre-ship check for text-heavy slides:**
1. Note the LAST sentence of the source text (the final kicker or closing line).
2. Look at the 1920x1080 screenshot.
3. Confirm that sentence's FINAL CHARACTER is visible with space below it. Not just the start of the sentence. Not just 3 lines of it. The FINAL period must be within the frame with margin.
4. If not visible: shorten the text, reduce font-size clamp, or split to a second slide.

**Content density rules of thumb for `.split` layouts at 1920x1080:**
- Headline (28-48px): max 1-2 lines.
- Body paragraph (14-20px): max 3-4 sentences or ~220 characters.
- Kicker (14-22px, emphasized): max 1 line, or 2 very short lines.
- Total vertical space for text column: ~720px after padding.

**Font size reductions that help without visible degradation:**
- Body: clamp(16px, 1.8vw, 24px) → clamp(14px, 1.5vw, 20px).
- Kicker: clamp(18px, 2vw, 28px) → clamp(14px, 1.55vw, 22px).

**How to apply:**
- For every split/two-column text slide with more than 2 sentences in the body, run the "last character visible" check.
- When adding new items to a bullet list or paragraph (like I did with "DMs, platform tracking, competitor analysis"), RE-RUN the overflow check. Adding content never shrinks existing content automatically.
- If visual QA shows content near the bottom edge (within ~50px of frame bottom), that's a fail. Ship with at least 80-100px of breathing room.

**Why I missed this initially:**
I rendered the slide after the content addition. I read the screenshot. Content looked present. But I didn't specifically verify the LAST sentence's last character was within the frame. That's a distinct check, and I skipped it because "looks good" felt sufficient.
