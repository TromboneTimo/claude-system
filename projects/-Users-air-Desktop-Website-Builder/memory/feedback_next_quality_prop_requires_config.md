---
name: Custom quality prop on <Image> requires images.qualities in next.config, or Vercel returns 400
description: Setting `quality={78}` or any value not in `images.qualities` config causes Vercel's image optimizer to return HTTP 400 INVALID_IMAGE_OPTIMIZE_REQUEST. Default q=75 works. Other values silently break images in production.
type: feedback
originSessionId: 5857f0fd-4e7a-4b74-b5bd-f23376b6f5e7
---
Next.js `<Image>` accepts a `quality` prop (0-100), but Vercel's production image optimizer only serves widths/qualities declared in `next.config.ts`. Passing `quality={78}` without whitelisting 78 in `images.qualities` returns HTTP 400, image never loads, and there is no visible error in browser DevTools other than a broken image.

**Why:** On otto-cristofoli (2026-04-22), I added `quality={78}` and `quality={80}` to Image tags thinking "78 is tighter than default 75 will be better." In local dev it worked. On Vercel production it returned 400 for every such request. User saw empty tiles on the mentor grid. The HTML srcset still used q=75 because Next.js' image builder caught this and didn't include the bad quality in srcset, but the fallback `src` attribute and any eager-loaded variants failed.

**How to apply:**
- Default Next.js/Vercel quality is 75. Leave it alone unless you have a reason.
- If you MUST set a custom quality, add it to config:
  ```ts
  images: {
    qualities: [60, 75, 85],   // only these values will be accepted at runtime
  }
  ```
- The same rule applies to `deviceSizes` and `imageSizes`: any width or quality passed at runtime that is not in the config gets a 400 in production.
- Verify in production by grepping the deployed HTML for `q=\d+` values. If any q values appear that aren't in config, test them with `curl -I` against `/_next/image?...` before shipping.
