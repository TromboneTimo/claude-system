---
name: Audit static asset sizes before every deploy, not after user complains
description: Before any `vercel --prod` on a site with videos/images, run `ls -lah public/videos public/images` and flag anything >2MB. A single 18MB hero video will kill page load regardless of how clever the code is.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
Never ship a static asset without knowing its size. Code-level perf optimizations (React.memo, willChange, IntersectionObserver) are invisible next to a 18MB MP4 in the hero.

**Why:** On otto-cristofoli (2026-04-22), Timo said "smooth out the site" and I shipped a set of component optimizations without ever looking at `public/videos/`. User reported slowness. The actual cause was `music-system-italy-hero.mp4` at 18MB (170 seconds at 900kbps, trimmed to 20s = 1.9MB, 9.5x reduction). All the React polish was insignificant compared to this.

**How to apply:**
- Before any `vercel --prod` or `npm run build` on a content-heavy site, run:
  ```bash
  find public -type f -size +1M -exec ls -lah {} \; | sort -k5 -h -r
  ```
- Anything >2MB = flag it. Videos should be <3MB compressed (CRF 26, `-movflags +faststart`). Hero loops trim to 15-25s.
- Images: any source >500KB at 1024px+ resolution gets flagged for pre-compression or rely on Next.js image optimizer (verify via grep of deployed HTML).
- After deploy, `curl -I` each heavy asset on the CDN and check `content-length`. Don't assume Vercel compresses videos (it doesn't).
- Add this check to the pre-deploy gate: build > asset audit > QA > API > browser verify.
