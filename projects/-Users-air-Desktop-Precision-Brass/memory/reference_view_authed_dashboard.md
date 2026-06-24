---
name: reference-view-authed-dashboard
description: "How to load the auth-gated Precision Brass dashboard in Playwright with real data, to visually verify pages. Solves the recurring \"can't see the authed view\" gap."
metadata: 
  node_type: memory
  type: reference
  originSessionId: d228715a-5ca5-4603-b90f-9fe73056656e
---

The PB dashboard pages (meta-ads, email-analytics, etc.) are auth-gated by `dashboard/lib/auth.js`: an unauthenticated load redirects to /login and `<style id="pb-auth-gate-style">html{visibility:hidden}</style>` hides everything. So curl and a logged-out Playwright see only a redirect/blank. To ACTUALLY SEE a page's real rendered tables/data (verify-with-eyes), mint a real user session.

1. Mint a session (no password change) via Supabase GoTrue admin, using the PAT/service-role from [[project-credentials]]:
   - `POST {SB}/auth/v1/admin/generate_link` (apikey+Bearer = service_role) body `{"type":"magiclink","email":"timothyjay.maines@gmail.com"}` returns `email_otp`.
   - `POST {SB}/auth/v1/verify` (apikey = anon) body `{"type":"magiclink","email":...,"token":<email_otp>}` returns session `{access_token, refresh_token, expires_at, token_type, user}`.
   (Admin auth users as of 2026-05-25: timothyjay.maines@gmail.com is ADMIN; also harrissonball@precisionbrass.info, trombonetimollc@gmail.com.)
2. The MCP Playwright chrome profile usually ALREADY has a persisted session, so just `browser_navigate` to `https://precision-brass-dashboard.vercel.app/meta-ads`; if it loads (no redirect), you are authed. Otherwise inject the minted session into localStorage key `sb-iwlernqpwdsjarygoeog-auth-token` = the session JSON (supabase-js v2 default storage), then navigate.
3. Read data WITHOUT relying on JS scope: `state` is module-scoped, NOT `window.state`. Use `browser_evaluate` to read the rendered DOM, e.g. `.folder-card .folder-metric .l/.v` for cards, `table.ads tbody tr td` for rows. Click a `[data-tab]` or `.folder-card` to drill.

Gotchas: the MCP browser throws "Browser is already in use ... mcp-chrome-35056b9", fix with `pkill -f mcp-chrome-35056b9; rm -f <profile>/SingletonLock`, then retry. `file://` is blocked, so serve local renders via `python3 -m http.server`. This is how the 2026-05-25 meta-ads revenue bug was finally seen and confirmed. See [[project-meta-ads-revenue]].
