---
name: Pre-size source images before deploy so the image optimizer has less cold-cache work
description: Next.js/Vercel image optimizer cold-request time is proportional to source size. A 780KB source takes ~1-2s to optimize cold. A 150KB source takes <0.3s. Pre-size every source to max 2x the biggest display width.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
Next.js image optimization on Vercel is fast after cache warmup but slow on the first request per unique (url, width, quality) triple. First-request time scales with source image size because the optimizer has to: download source → decode → resize → encode AVIF/WebP. Heavy sources = slow cold paints.

**Why:** On otto-cristofoli (2026-04-22), mentor photos displayed at 200px were stored at 1024-2000px, 476-780KB per JPG. First-visit cold optimization was ~1-2s per image. User reported grids loaded with a visible lag. After `sips -Z 800` on all mentor sources (down to 50-165KB), cold optimization dropped under 500ms.

**How to apply:**
- For any gallery/grid/carousel where images are displayed at X pixels, resize sources to max 2x X, quality 80-85.
- Batch command (macOS): `for f in src/*.jpg; do sips -Z 800 "$f" --out "$f"; done`
- Back up originals first: `mkdir -p _backup && cp src/* _backup/`
- Measure after deploy: `curl -o /dev/null -w "%{time_total}s\n" -H "Accept: image/avif" "<url>/_next/image?url=...&w=200&q=75"`. Cold should be <500ms on sensible sources.
- Do NOT rely on Next.js image optimizer alone as a substitute for resizing. It is a CDN layer, not a magic shrinker. The source file still ships to Vercel on deploy and is still the input to every resize operation.
