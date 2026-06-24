---
name: Slide Typography Hierarchy (Real Ratios)
description: Supporting text must be 20-25% of hero text size, not 60-70%. One focal point per slide. Breathing room mandatory.
type: feedback
originSessionId: 8a1f3cb4-64a7-4d88-bcea-b99ce6f13880
---
# Slide Hierarchy Rule -- Real Ratios

**Rule:** On any slide with a hero headline, every supporting element must be sized at 20-25% of the hero size. Not 60-70%. Hierarchy means one focal point dominates and everything else supports quietly.

**Why:** On 2026-04-13, Timo called out multiple slides where "it feels way too heavy on text" and "text almost doesn't fit the screen." Root cause: I sized supporting captions, eyebrows, and sub-headlines at clamp(18px, 2vw, 28px) or clamp(24px, 3.5vw, 56px) when the hero was at clamp(60px, 12vw, 200px). The supporting elements were 30-50% of hero size, causing them to compete visually. Nothing dominated. Everything screamed. Text overflowed viewports because stacked competing elements couldn't fit.

## The Fixed Ratios

| Element | Size Relative to Hero | Example clamp |
|---------|----------------------|----------------|
| Hero headline (1 per slide MAX) | 100% | `clamp(44px, 8vw, 120px)` |
| Eyebrow label (uppercase, letterspaced) | 12-15% | `clamp(12px, 1.2vw, 16px)` |
| Sub-headline / promise line | 20-25% | `clamp(14px, 1.5vw, 20px)` |
| Body / caption text | 18-22% | `clamp(14px, 1.6vw, 22px)` |
| Small proof text | 15-18% | `clamp(12px, 1.4vw, 18px)` |

## Hard Rules

1. **ONE hero element per slide.** Not two. Not "hook + equally-sized sub-hook." One thing dominates.
2. **Eyebrow labels use letter-spacing 0.15-0.25em and uppercase.** This makes them read as "label" not "headline."
3. **Supporting text opacity 0.7-0.85 on busy slides.** Makes it visually recede behind the hero.
4. **Breathing room: minimum 24-36px gap between elements.** Text cannot touch.
5. **Mentally render at 3 viewport widths** before shipping: mobile (375px), laptop (1440px), large (1920px). If hero text wraps awkwardly or supporting text is unreadable at any of these, fix it.
6. **Test max clamp values.** At 20vw on a 1440px screen = 288px. Count the characters. If hero text is "100,000,000" that's 11 characters * 180px letter width = 1980px, overflowing. Always math the overflow before shipping.

## Common Failures I Keep Making

- Using the CSS `.cta-target` class (clamp 60-200px) for a CTA keyword WHILE also having a bullseye graphic AND tagline AND subtext on the same slide. All at large sizes. Everything collides.
- Sub-headlines at `clamp(24px, 3.5vw, 56px)` directly under heroes at `clamp(30px, 5.2vw, 88px)`. That's a 63% ratio. They compete.
- Not reducing CTA type size when the slide also includes an image and tagline. The CTA alone can be huge. The CTA PLUS image PLUS eyebrow cannot.

## Related
- feedback_visual_qa.md (Safari-render after edits, check overflow)
- feedback_pregeneration_checklist.md (mentally render before shipping)
- feedback_presentations.md (presentation design rules)
