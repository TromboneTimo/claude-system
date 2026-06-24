---
name: When padding trimmed images, pad with the exact container bg color from the data file
description: Trimmed non-square images that get padded to square must use the SAME color as the downstream container background, read from the data file. Never pad with black or a guess.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
When trimming an image leaves a non-square result and you need to pad it to square for a fixed-aspect container, the padding color MUST match the container background EXACTLY. If different items have different backgrounds (e.g., per-album bg colors), read the data file and pad per-item.

**Why:** On Samurai Brass (2026-04-22), I padded all 9 cropped album covers with `#0a0a0a` black, assuming it matched the slide bg. Each album actually had its own `bgSideA` in `albums.ts` (`#2a1a05`, `#7a1a05`, `#162a16`, etc.). The result was visible letterbox bands between the cover and the slide. Fixed by reading each album's `bgSideA` from the data file and padding per-image.

**How to apply:**
- Before padding any trimmed image, grep the relevant data/config file for the container's background color. If it's per-item, build a filename -> color map.
- Parse hex (`#RRGGBB`) to `(r,g,b)` and pass to `Image.new("RGB", size, rgb)`.
- Alternative when feasible: change the container aspect ratio to match the trimmed image, avoiding padding entirely. (Not always possible if the container hosts layered siblings like a vinyl disc that must stay square.)
- If the container bg is defined in CSS, not data, either extract it from CSS or switch to a PNG with transparent padding + set the container bg in markup.
