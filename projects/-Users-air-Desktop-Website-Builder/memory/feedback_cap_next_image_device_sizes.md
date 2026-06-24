---
name: Cap Next.js image deviceSizes/imageSizes in config, never ship defaults
description: Default Next.js `images.deviceSizes` includes 2048 and 3840, so every <Image> gets a 3840px fallback src even for 200px-displayed thumbnails. Always set a capped deviceSizes/imageSizes in next.config for image-heavy sites.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
Every `<Image>` in Next.js defaults to a `src` fallback at the largest entry in `images.deviceSizes` (default max = 3840). For thumbnail grids displayed at 200px, this means the browser can fetch a 3840px version as the fallback, tens of times larger than needed.

**Why:** On otto-cristofoli (2026-04-22), mentor photos on `/music-system-italy` were loading slowly. The `<Image>` markup looked correct with `sizes="(max-width: 640px) 50vw, (max-width: 1024px) 25vw, 200px"`, but grepping the deployed HTML revealed every `src` attribute was `w=3840&q=75`. Adding `images.deviceSizes: [360, 640, 828, 1080, 1440, 1920]` + `imageSizes: [64, 96, 128, 200, 256, 384]` capped the srcset to sane thumbnail sizes. Cesari photo on wire dropped from hundreds of KB to 7.7KB (AVIF at w=200).

**How to apply:**
- For any Next.js site with image-heavy pages, add to `next.config.ts`:
  ```ts
  images: {
    formats: ["image/avif", "image/webp"],
    deviceSizes: [360, 640, 828, 1080, 1440, 1920],
    imageSizes: [64, 96, 128, 200, 256, 384],
    minimumCacheTTL: 60 * 60 * 24 * 30,
  }
  ```
- Verify by `curl`ing deployed HTML and grepping `srcSet=` and `src=` on actual image tags. Do NOT trust source code `<Image sizes=...>` alone. The fallback `src` attribute is what matters for legacy browsers AND what appears in page-weight audits.
- Same pattern applies to large hero videos: check actual `content-length` over CDN, not source file size. Source may be 18MB but gets served as-is if no compression pipeline.
