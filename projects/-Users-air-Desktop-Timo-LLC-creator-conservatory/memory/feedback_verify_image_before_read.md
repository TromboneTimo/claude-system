---
name: Verify Image Files Before Reading
description: Run `file` on any fetched image asset before passing it to the Read tool. Tiny image files are usually error pages, not images, and crash the API.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
After `curl`-ing an image asset, ALWAYS check it's a real image before calling Read on it. If the file is suspiciously small (under ~3KB for a logo, under ~10KB for a photo) it is almost certainly an HTML error page with a `.png` extension, and the Read tool will hit `API Error: 400 "Could not process image"` repeatedly until the loop crashes.

**Why:** 2026-04-13 fetched a comScore logo from Wikipedia that returned a 1956-byte HTML error page named `comscore-logo.png`. Read failed 3x in a row with `invalid_request_error`, halted the slide-edit work mid-task, Timo lost confidence ("you glitched out, fuck you"). The user's IDE then opened the auto-research-marketing hook file because of the cascading errors. Total trust hit, completely avoidable.

**How to apply:**
1. After every `curl -o file.png` (or any image fetch), run `file path.png` and `ls -la path.png` BEFORE Read.
2. If `file` reports `HTML document text` instead of `PNG image data`, the fetch failed. Don't Read it. Try a different source or skip and build the visual inline (CSS/SVG mockup).
3. Sanity threshold: a real logo PNG is usually 5-100KB. A real photo is 100KB+. Anything under 3KB labeled `.png` is suspect.
4. If 2 image sources fail in a row, STOP fetching and build the visual inline with HTML/CSS/SVG. Don't loop on broken URLs while the user waits.
5. DNS or network failures often cascade silently — `curl: (6) Could not resolve host` means switch immediately to inline visuals, no retries.
