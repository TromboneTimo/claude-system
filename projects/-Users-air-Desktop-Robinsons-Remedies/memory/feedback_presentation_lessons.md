---
name: Presentation creation lessons
description: Hard-learned rules from building RR strategy presentations. NEVER repeat these mistakes.
type: feedback
---

## Presentation Creation Rules (from multiple rounds of corrections)

1. **NEVER use the same layout twice in a row.** Vary between: stat slides, image-dominant, centered text, card grids, full-bleed image. If two consecutive slides look the same, redesign one.

2. **MAX 2-3 sentences per slide.** If you need more, split into another slide. Walls of text = presentation is useless.

3. **Every slide needs an image.** Not just product shots. Use images RELEVANT to what's being discussed. Facebook strategy = Facebook screenshot. Dashboard = analytics image. Livestream = livestream image.

4. **Use REAL product images and logos, not placeholders.** Pull from robinsonsremedies.com Shopify CDN or local image files. Verify every URL returns 200 before shipping.

5. **Never cram multiple concepts into one slide.** The 4-tier awareness funnel = 4 slides, one per level. Not 2 slides with 2 levels crammed in each. Each concept gets its own slide.

6. **Attribution matters.** If Timo built it, don't say "we built." Say what the thing IS, not who built it.

7. **Include brand logos when referencing tools.** ChatGPT slide = ChatGPT logo. Claude Code slide = Claude logo. Facebook ads slide = Facebook image.

8. **Text overlay on dark images is unprofessional** unless done perfectly. Prefer side-by-side layouts (text left, image right) over text overlaying a dimmed background image.

9. **Explain WHY to non-technical people.** Richard and Kenny are 60+ year old business owners. Every slide must answer "why does this matter to Robinson's Remedies" in plain English.

10. **Organize the ending.** Don't dump random slides at the end. Structure: System Overview > Roadmap > Compensation > Close. Clear sequence.

11. **Images for awareness levels should match the PAGE TYPE, not generic stock photos.** Advertorial = Kenny's story photo. Listicle = wax demo. Landing page = product photo. Product page = endorser social proof.

12. **Never fabricate quotes.** If Kenny didn't say it, don't put it in quotes. Use narrative description instead.

13. **VERIFY EVERY IMAGE URL BEFORE SHIPPING.** After generating any presentation, run an automated audit: grep all src/url attributes, curl each remote URL (must return 200), ls each local path (must exist). Fix ALL failures before declaring done. This is mandatory, not optional.

14. **Never use Wikipedia/Wikimedia image URLs.** They rate-limit aggressively and return 429. Use Shopify CDN, Unsplash, or styled text instead.

15. **If an external image might fail, replace with styled text.** Text never breaks. A bold "ChatGPT" in Clash Display at stat-size looks better than a broken image icon.

16. **Every image must match the text on its slide.** Don't use a generic stock photo to fill space. If the slide talks about email marketing, the image should be about email, not a random desk photo.

17. **Open the presentation in Safari and verify EVERY SLIDE visually before declaring done.** This is the final gate. No exceptions.

**How to apply:** Read this before building ANY presentation. After building, run the image audit (grep + curl + ls). Then open in Safari. Only then is it done.
