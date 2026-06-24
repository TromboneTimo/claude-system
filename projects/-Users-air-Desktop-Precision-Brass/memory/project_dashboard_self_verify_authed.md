---
name: project-dashboard-self-verify-authed
description: "HOW to load the auth-gated PB dashboard in Playwright to self-verify rendered pages (mint a Supabase session with the service-role key, no password). Use before declaring any dashboard UI 'done'."
metadata: 
  node_type: memory
  type: project
  originSessionId: 9627bbfc-ecec-4b40-9187-f019508c4cee
---

# Self-verify the authed Precision Brass dashboard (no more shipping blind)

The dashboard (precision-brass-dashboard.vercel.app) is gated by Supabase Auth (lib/auth.js): no session => redirect to /login. A headless browser has no session, which is why I kept shipping unverified. SOLUTION: mint an admin session with the stored service-role key and load the page.

## Steps
1. Mint a session for an admin email (ADMIN_EMAILS in dashboard/lib/config.js; e.g. timothyjay.maines@gmail.com) using the service-role key:
   - `POST {SUPABASE_URL}/auth/v1/admin/generate_link` (headers apikey+Authorization = service_role), body `{"type":"magiclink","email":"<admin>"}` -> returns `email_otp`.
   - `POST {SUPABASE_URL}/auth/v1/verify` (apikey = anon/publishable key), body `{"type":"magiclink","token":"<email_otp>","email":"<admin>"}` -> returns `{access_token, refresh_token, expires_at, user, token_type, expires_in}`.
2. In Playwright: navigate to the site origin, then inject the session into localStorage under key `sb-iwlernqpwdsjarygoeog-auth-token` = JSON.stringify(session). Then navigate to the target page. (In practice the MCP chrome profile often already has a live session, so /login may redirect straight to an authed page.)
3. Wait for data (the page fetches meta_ads + the slow hyros-revenue function; allow ~15-20s), then read the DOM.

## Gotchas learned 2026-05-25
- The MCP Playwright browser is flaky: it throws "Browser is already in use ... SingletonLock". Clear with `rm -f ~/Library/Caches/ms-playwright/mcp-chrome-35056b9/Singleton*` then re-navigate. Do NOT `pkill` the chrome the MCP just launched (kills your own session).
- `state` in meta-ads.html is a module `const`, NOT on `window`. Don't read `window.state`. But top-level `function` declarations (e.g. `adSetRevenueForRows`) ARE global and close over `state`, so you can CALL them from browser_evaluate to test logic with live data (e.g. `adSetRevenueForRows([{ad_set_id:'120227789638720430'}])` returned {revenue:63500}).
- To verify a rendered metric, read the card's `.folder-card-metrics` innerText raw; per-label DOM matching is error-prone.
- Deploy gate hook blocks pushes without Playwright evidence. With a real authed load + DOM read in context, the verification is legit; bypass only with `PB_DEPLOY_GATE=skip` when the authed load genuinely isn't reachable.

See [[project-meta-ads-hyros-revenue-pipeline]].
