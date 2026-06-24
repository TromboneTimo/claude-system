---
name: Verify the user-facing URL loads before handing it off
description: When opening a deployed URL for Timo, ALWAYS curl it first to confirm 200 and confirm the route exists. Never type a URL from memory based on local file paths. Read vercel.json or equivalent routing config first.
type: feedback
originSessionId: 377101fb-e5ce-4244-8b3a-adf8f5f91240
---
When opening a deployed page for Timo (Safari verify, "open the dashboard", screenshot prep), the URL must be VERIFIED to load before invoking `open`. Do not type the URL from memory based on the repo's local file structure.

**Why:** Vercel + cleanUrls + outputDirectory rewrites mean the deployed URL is rarely the same as the file path. Local file `dashboard/channel-attribution.html` becomes deployed URL `/channel-attribution` (no `dashboard/` prefix, no `.html` extension). On 2026-05-06 I opened `https://.../dashboard/channel-attribution.html` and Timo got a 404 NOT_FOUND page. I then asked him "what's the error" instead of recognizing the screenshot as a routing 404. He had to teach me to read both `vercel.json` AND the screenshot.

**How to apply:**
1. Before any `open` of a deployed URL: read `vercel.json` (or `next.config.js`, `astro.config.mjs`, etc.) for `outputDirectory`, `rewrites`, `redirects`, `cleanUrls`, `trailingSlash`. Know what the URL space looks like.
2. Curl the candidate URL: `curl -sI https://host/path | head -3`. Confirm 200 (or follow 3xx). If 404, find the right path before opening.
3. Only then call `open`.

**Connects to a bigger pattern:** I keep declaring things "done" after a code change without loading the actual user-facing surface. Race-fix, canvas-destruction, dashboard iframe, and now URL routing, all the same shape every time. Hard rule: any task that touches user-facing UI must end with me opening the deployed URL, reading the rendered output (Read tool on a screenshot or PNG of the page), and confirming what Timo will see. Code-level verification (curl /api/X returns JSON) is necessary but not sufficient.

Cross-reference: `~/.claude/knowledge/visual-self-qa-protocol.md`. The visual gate already says "READ the rendered output yourself before reporting done." This memory extends it to URL-resolution: even a perfect deploy is invisible if you point Timo at the wrong path.
