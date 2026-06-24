---
name: Generate Real Visuals, Don't Placeholder
description: When a slide's job is to show a specific real-world visual (a campaign photo, a product screenshot, a UI before/after), generate the actual visual via Gemini. Generic icon placeholders defeat the slide's purpose.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
When building a slide that compares specific real-world visuals (Obama campaign video → family photo, old Bing search results → new Bing search results, short Highrise page → long Highrise page), GENERATE the actual visuals via Gemini. Do not use generic placeholders (play-button rectangles, silhouette boxes, fake search result text).

**The exact failure pattern (2026-04-13):**
- Built slide 3 case study showing Obama 2008 A/B test
- BEFORE mockup: generic black rectangle with a play-button triangle and "VIDEO" label
- AFTER mockup: warm gradient with three black silhouette shapes labeled "PHOTO"
- Both were CSS placeholder boxes when I had a working Gemini image generator (had already used it for the Obama portrait on the same slide)
- Timo: "why didnt you also render the fucking family hero video and family photo, you just did generic bullshit"
- Generated the real visuals immediately afterward — slide instantly became 10x more credible because the proof IS the visual

**Why this happens:** I default to "build mockups in HTML/CSS" mode when working on slides. That mode is correct for browser frames, buttons, layouts. It's WRONG when the slide's whole point is "look at the specific visual that changed." Generic icon placeholders communicate "this is a placeholder for a video" — but the slide doesn't need a video placeholder, it needs THE video frame.

**The decision rule:**
Before placeholder-mocking any visual content on a slide, ask: "Is this a generic UI element (button, modal, browser chrome) OR is this specific real-world content (a particular photo, a specific product screen, a brand's actual page)?"
- Generic UI → CSS mockup is fine.
- Specific real-world content → GENERATE the actual visual via Gemini.

**The deeper rule:**
When I have an image generator AND the slide's purpose is to show a specific visual difference, defaulting to placeholder is a failure mode, not a minimalism choice. The image generator exists. Use it.

**How to apply:**
- For any case study slide showing X-was-replaced-by-Y, generate X and Y as real images.
- For brand mockups (e.g., showing what a famous landing page looked like), generate the actual page screenshot stylization.
- For product UI before/after, generate the actual UI states.
- Use the working Gemini API call shape (see `reference_gemini_image_api.md`).
- Specify "editorial illustration style, slightly painterly, NOT photorealistic" for any real public figure to avoid uncanny photo issues and stay within content policy.
- Generate the BEFORE and AFTER as a matched pair — same prompt structure, same aesthetic, so they read as a comparison.

**Why this is high leverage:** Every "show what changed" slide in every deck I'll ever build benefits from generated specifics over generic placeholders. The 30-second delta between asking for a placeholder vs asking for a generation is the difference between "this slide is filler" and "this slide is the proof."
