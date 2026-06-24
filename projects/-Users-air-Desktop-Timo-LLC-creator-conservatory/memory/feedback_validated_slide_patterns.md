---
name: Validated Slide Patterns (What Timo Loves)
description: Specific slide patterns Timo has explicitly approved with strong positive feedback. Repeat these defaults across all decks.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
When building slides for Timo, default to these patterns. Each was validated with explicit "I LOVE this" or equivalent strong positive feedback.

**Pattern 1: Hero portrait + before/after with REAL generated visuals.**
Layout: large stylized portrait of the public figure on the left, brand logo + biz desc top right, BEFORE | → | AFTER mockups using actual generated images of the specific visual that changed, THE CHANGE text callout below the mockups, big result number + caption inline, source citation at bottom.
Validated on: Obama 2008 case study slide, 2026-04-13. Timo: "I LOVE THE CHANGES YOU JUST MADE THOUGH YES!! BEAUTIFUL! PLEASE NOTE THAT I REALLY LIKE MORE LIKE THIS"

**Pattern 2: Split-screen comparison (old way vs new way).**
Layout: full-bleed two-column slide with 0 padding on the .slide. Left column dim-tinted with red accents, "OLD WAY" eyebrow, headline ("Hire a designer."), 5 dashed-bullet downsides. Right column accent-tinted with green/positive accents, "NEW WAY" eyebrow, headline ("One AI-empowered marketer."), 5 checkmark-bullet upsides. Center eyebrow positioned absolute at top.
Validated on: slide 6 designer-vs-marketer deck, 2026-04-13.

**Pattern 3: THE CHANGE callout block.**
Use whenever showing a specific case study change. Style: `background:rgba(255,255,255,.04); border-left:3px solid var(--accent); padding:.7rem 1.4rem; border-radius:0 6px 6px 0`. Inside: small accent-colored "THE CHANGE" label (uppercase, letter-spacing:.3em, font-weight:800), then a single sentence describing what changed in plain words. Position: between the visual mockup and the result number.

**Pattern 4: Color swatch chip with hex code.**
When the case study is about a color/design value change, include color swatch chips visible AT THUMBNAIL SIZE. Format: `[28x28 colored square] LINK COLOR / #HEXCODE`. Make the BEFORE swatch dim/desaturated, the AFTER swatch vibrant with an accent ring around it. This makes the proof visible even when the in-mockup color difference is subtle.
Validated context: Bing slide blue-shade test fix, 2026-04-13.

**The default stack for any "external case study" slide:**
1. Eyebrow (numbered + section name)
2. Brand logo + 1-line business context (centered top)
3. BEFORE | → | AFTER mockups (with real generated visuals when applicable)
4. THE CHANGE callout (between visuals and result)
5. Big result number + short caption (inline, side-by-side, NOT stacked vertically — saves space, prevents source line collisions)
6. Source citation at very bottom (small caps, muted, position:absolute with bottom:.85-1.4rem)

**Why these patterns work for Timo specifically:**
- He's a video creator — he thinks visually. Real images > placeholders. Specific > generic.
- He's anti-BS — actual case study visuals build credibility; generic mockups look like filler.
- He's an audience whisperer — split-screen comparisons land harder than single-column "X vs Y" headlines because the audience SEES both sides.
- He's iterating fast — these patterns compose well. Once built, they're easy to swap content into.

**How to apply:** When starting any new slide deck for Timo, scan this file first. Use these patterns as the defaults instead of inventing new layouts each time.
