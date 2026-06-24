---
name: feedback-verify-lean-not-browser-loop
description: Don't verify every small dashboard change by restarting a local server + re-minting a Supabase token + re-injecting a session in Playwright. That loop bugs out (dead server, expired token, blank page) and wastes the session. Verify lean.
metadata:
  type: feedback
---

**From 2026-06-04 (Timo, frustrated):** "the way you're trying to do things is causing
you to bug out and do the same thing over and over." The pattern that fails: per-step
Playwright verification that needs (a) a local python http.server that keeps dying on
shell resets, (b) an hourly-expiring Supabase token re-minted every time, (c) a session
re-injected via evaluate that gets wiped on every navigate. It loops.

**Verify lean instead, matched to risk:**
- Trivial additive UI (a button, label, copy handler that mirrors an existing one):
  `node --check` the extracted inline script + deploy + `curl | grep` the live bundle
  for the new symbol. No browser.
- New server endpoint: `curl` the live endpoint with a real Bearer token and inspect the
  JSON. No browser.
- Genuinely NEW rendering: exactly ONE prod screenshot, read it, done. No loops.
- If the auth/session injection fails once, fall back to grep/curl and report honestly.
  Never restart-server / re-mint-token more than once for the same check.

Mint at most ONE token per verification and reuse it across curl + a single browser shot.
See also [[project_dashboard_self_verify_authed]] (the how) but cap the browser use.
