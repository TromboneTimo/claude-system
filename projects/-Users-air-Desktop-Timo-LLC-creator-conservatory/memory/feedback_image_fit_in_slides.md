---
name: Image Must Fit The Slide Or Get Cut
description: Never drop an image into a slide without verifying it fits the layout, aspect ratio, and viewport. If the image fights the type, kill the image.
type: feedback
originSessionId: f48c716d-c5d0-4b99-bba5-c74c4f22aed9
---
Before placing any image in a slide, verify three things: (1) source dimensions and aspect ratio, (2) how it will render at the target viewport (1440x900 for desktop deck, 9:16 for mobile), (3) whether the image earns its slot or fights the headline.

**Why:** 2026-04-13 leaking-business deck — slide 10 had a 1376x768 AI workflow image dropped into a flex column with the headline. The image was sized 80vw max but at desktop viewport competed with the headline, broke the typographic hierarchy, and looked like stock-art filler. Timo: "see how youre not optmiizing imamges you make to fit well into the slide?" Fix: kill the image, run on type alone — the slide reads stronger.

**How to apply:**
- Before inserting an image: `sips -g pixelWidth -g pixelHeight image.png` to know the source.
- Match aspect ratio to slide intent: full-bleed background = 16:9 landscape, inline diagram = use as-is with object-fit:contain.
- If image is going behind text, use `object-fit:cover` AND a darken overlay AND verify text contrast.
- If image is competing with headline for focal weight, EITHER demote the image (smaller, lower opacity, side-positioned) OR cut the image entirely.
- Default: when in doubt, cut the image. Type-only slides land harder than slides with weak art.
- Slide 10 lesson: "you're a one-person team fighting a four-person agency" doesn't need a workflow diagram. The line IS the visual.
