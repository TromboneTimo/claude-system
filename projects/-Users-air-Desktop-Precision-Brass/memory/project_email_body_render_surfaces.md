---
name: project_email_body_render_surfaces
description: "The dashboard renders an email body on THREE surfaces, each with its own DOMPurify allowlist; broadcast.html is deprecated. Fix the surface the user actually sees."
metadata: 
  node_type: memory
  type: project
  originSessionId: 01124e67-071c-4f2b-b966-013999b596bd
---

The Precision Brass dashboard renders an email proposal body in three places, each with a SEPARATE DOMPurify allowlist. A too-narrow allowlist strips the video-thumbnail embed (`<table>` wrapping an `<img>` + play-button spans) and inline styles, so the preview looks nothing like the real inbox.

1. **emails.html** `.email-body` (`renderEmailBody` + `PB_BODY_TAGS`/`PB_BODY_ATTR`, ~line 1262). This is the REVIEW surface Timo/Harrison actually look at. Its CSS was cream `#FAF7F2` + Georgia serif; changed to white + Arial 2026-06-07 to mirror the inbox.
2. **scheduled.html** `.preview-body` (`PREVIEW_TAGS`/`PREVIEW_ATTR`, ~line 496). This is the actual BROADCAST/SCHEDULE surface (white/Arial already). The send flow is emails.html review -> `/scheduled?ids=` -> pick a day -> schedule.
3. **broadcast.html** (`renderInboxBody` + `ALLOWED_TAGS`/`ALLOWED_ATTR`). DEPRECATED. `gotoBroadcast()` in emails.html routes to `/scheduled`, not here. Editing this alone does NOTHING for what Timo sees.

All three allowlists must include `img`, `table/thead/tbody/tr/td/th`, `div`, and the `style/src/width/height/alt/align/...` attrs for the video embed to render. Fixed all three 2026-06-07.

**Lesson (ties to [[feedback_map_named_list_and_reproduce_view]]):** when Timo says "I still don't see it," REPRODUCE his exact view before fixing. The cream-bg + serif-font fingerprint pointed straight at emails.html `.email-body`; I wasted a deploy on broadcast.html first. Identify the surface by its CSS fingerprint, don't assume.

**Authed verify method that worked here:** serve a `/tmp` COPY of dashboard/ (NOT the deploy root, a session token there gets blocked), mint a magic-link session ([[reference_view_authed_dashboard]]), fetch the proposal body in-page with the token, render it through the page's own `window.DOMPurify` with the deployed allowlist into a `.email-body` div, screenshot. Vercel preview URLs are behind Vercel SSO so Playwright cannot reach them; the prod alias is the only authed-reachable deploy.
