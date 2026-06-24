---
name: html-no-store-for-safari-cache
description: "When a UI bug reappears after a deploy that should have fixed it, suspect Safari's WebKit disk cache before suspecting the code. Default cache headers on .html let Safari serve stale bytes for hours. Solved permanently by Cache-Control no-store on HTML routes in vercel.json."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f99ddcb6-ecd6-45dc-b8b2-e7b0c18f5374
---

When a user reports the same UI bug after a deploy that *should* have fixed it, and Playwright + curl + visual inspection all confirm the deployed bytes are correct, the next move is not "diagnose the CSS again." It is: check whether the user's browser is serving stale HTML from disk cache.

**Why:** 2026-05-19. Timo reported the meta-ads column misalignment for the 10th time after I had just shipped commit 3e6f99f (`table-layout: fixed` + scroll wrapper) the day before. I ran the full ui-bug-diagnostic-protocol with Playwright WebKit (literal Safari engine) + Chromium across 5 viewports + 5 zoom levels = 300+ cells per run = zero misalignments anywhere. The deployed CSS was correct. The bug existed only in Timo's Safari disk cache, which was serving the pre-3e6f99f bytes with `width: 100%; table-layout: auto`. Safari's WebKit cache ignores `must-revalidate` on first-party `.html` under ITP, holding the disk copy for hours.

**The fix that stops it forever:** in `vercel.json`, add a headers rule that targets every route EXCEPT `/api/*` and recognized static asset extensions, with `Cache-Control: no-store, no-cache, must-revalidate, max-age=0`. Clean URLs (`/meta-ads`, `/scripts`) match the negative lookahead and get the no-store header. Assets (`.js`, `.css`, fonts, images) keep their regular cache. API routes set their own headers in code and are not overridden.

```json
{
  "source": "/((?!api/|.*\\.(?:js|css|json|png|jpg|jpeg|gif|svg|ico|webp|avif|woff|woff2|ttf|eot|map|mp4|webm|pdf|txt|xml)$).*)",
  "headers": [
    { "key": "Cache-Control", "value": "no-store, no-cache, must-revalidate, max-age=0" }
  ]
}
```

**How to apply:** Any Vercel-hosted dashboard or app where the user might see a recurring UI bug after a deploy. Add this rule on Day 1, not on Day 10. The cost (one extra HTML request per page load, no CDN edge cache for HTML) is trivial compared to the cost of "I told you a million times" debugging cycles. Static assets are unaffected, so initial load + repeat performance is barely changed.

**Diagnostic shortcut:** Before deep-diving into "the bug is back," do `curl -sI <prod_url>` and look at the `age:` header. `age: 44210` (12.3h) on a `.html` route with `cache-control: public, max-age=0, must-revalidate` is the smell. Vercel's CDN AND the user's browser may both be holding stale HTML.

**Linked:** [[feedback_ui_bug_diagnostic_protocol]] (full Step-1 coordinate-dump protocol), [[feedback_verify_with_eyes_not_curl]] (always verify with Playwright before saying fixed).
