---
name: feedback-audit-full-target-state-before-clone-deploy
description: "When deploying a \"clone\" or \"make it work like X\", diff the full target state (DB project, tables, functions, RLS, auth accounts, admin config, per-role nav) UP FRONT, not reactively after deploy."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e670584f-0b7e-4881-9e25-25b39353b8ae
---

"Publish this, it works just like Precision Brass" is a backend-clone request, not a static-file deploy. On the Victor Alegria dashboard (2026-06-04) I treated it as the latter and discovered every missing dependency reactively, in the worst order, over many round-trips:
- config.js still pointed at Precision Brass's Supabase (data-bleed risk; caught pre-deploy by luck)
- 4 tables (content_admins, content_clients, content_items, hooks) + is_content_admin() fn that the pages query did not exist in the new DB
- Hook Library nav link bounced restricted users (found only because Timo clicked it)

**Why:** each gap became a separate user-visible failure and a separate fix cycle. A single up-front structural diff against the source (PB) would have surfaced all of it at once. Timo: "this was way more work than it should have been."

**How to apply:** before deploying any clone / "make it work like X", enumerate and diff the FULL runtime contract against the source:
1. Which backend project does config point at? (must be the NEW client's, never the source's)
2. Every table/function/RLS policy the front-end queries (grep `from('...')`, `.rpc('...')` in all pages) -> confirm each exists in the target DB. Pull exact DDL from the source's live DB if missing.
3. Auth accounts + admin allowlist (config + any admins table) match intent.
4. Per-ROLE walkthrough: for each role, every nav item / page actually loads or is correctly gated. Test the interactions a real user does, not just the landing page. A login that lands fine but has a link that bounces is NOT verified.
Do this BEFORE the first deploy. Related: [[feedback-check-capability-before-offloading]], SCOPE GATE + AUDIT GATE in CLAUDE.md, [[project-dashboard-live]].
