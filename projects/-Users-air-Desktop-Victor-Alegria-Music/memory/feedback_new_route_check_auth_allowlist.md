---
name: new-route-check-auth-allowlist
description: "When adding a new dashboard route to Precision Brass, ALWAYS update LOCKED_ROLE.allow_pages in dashboard/lib/config.js before declaring done. Skipping this caused /scheduled to silently redirect to /scripts on 2026-05-13."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2e60061b-e9d8-4829-a2d9-34e0c95fb455
---

When creating or routing to a NEW page under `dashboard/` on Precision Brass, before deploy:

1. Open `dashboard/lib/config.js`
2. Add the new `pagename.html` to `LOCKED_ROLE.allow_pages`
3. Otherwise `enforcePageAllowlist()` in `lib/auth.js` redirects to `allow_pages[0]` (currently `scripts.html`)

**Why:** 2026-05-13. Built a new `/scheduled` calendar page and deployed it. Timo clicked through the new "Schedule selected" multi-select flow on /emails. The button navigated to `/scheduled?ids=...` which IMMEDIATELY redirected to `/scripts` because `scheduled.html` was missing from `LOCKED_ROLE.allow_pages`. He'd been told the flow was ready, hit a dead end, and was rightfully pissed. The fix was one line of config.

The admin-only `ADMIN_EMAILS = '*'` bypass exists, but Timo's session apparently resolves as restricted-role for reasons I haven't traced. Don't rely on the admin bypass to dodge updating the allowlist. The allowlist is the source of truth.

**How to apply:** Any time I create a new HTML file under `dashboard/`, or any time `emails.html` / another page adds a `window.location.href = '/newpage'` jump, grep `lib/config.js` for `allow_pages` and confirm the destination is in the list. If it isn't, add it. Do this BEFORE saying "deployed" or "ready to test", not after.

See also: [[verify-after-deploy-walk-the-flow]]. The deeper rule that I should have walked the user flow end-to-end, not just curl'd for a 200.
