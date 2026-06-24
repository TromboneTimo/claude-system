---
name: content-hub-two-admin-gates
description: "Content Suggestions hub has TWO independent admin gates - frontend config.js ADMIN_EMAILS and the database content_admins table (via is_content_admin() RLS). Granting admin requires BOTH. Per-client items are keyed to the client's auth.uid, so non-admins only see their own."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f84aeb30-40f8-4688-89fd-7320b07676a1
---

The Content Suggestions / Content Hub (dashboard/suggestions.html, tables `content_items` + `content_clients` + `content_admins`) gates admin access in TWO independent places. Granting someone admin requires updating BOTH or the UI lies:

1. **Frontend**: `dashboard/lib/config.js` `ADMIN_EMAILS`. Controls whether `PB_ROLE.role === 'admin'` -> shows the "Suggesting for" client picker + admin UI. If only this is set, the picker appears but shows "No clients yet" and 0 items because the DB blocks the reads.
2. **Database**: `content_admins` table (email rows). `is_content_admin()` (SECURITY DEFINER, checks `lower(email)` against `auth.jwt()->>'email'`) backs the RLS policies `content_clients admin all` and `content_items admin all`. Without a row here, RLS returns nothing for other clients.

Items are per-client: `content_items.client_id` = the client's **auth.users.id**, and `content_clients.id` is ALSO that same auth uid (NOT a random uuid). Client RLS = `content_items.client_id = auth.uid()`. So a non-admin only ever sees rows stamped to their own login. A client sees nothing if items are stamped to a DIFFERENT account.

**Why this matters (2026-06-02):** Timo reported "I uploaded 6 IG links, Content Suggestions shows Nothing here yet." The 6 rows WERE uploaded and correctly stamped to Harrisson (harrissonball@precisionbrass.info). Timo saw nothing because he was logged in as `trombonetimollc@gmail.com` (his 2nd account), which was neither admin nor Harrisson, so the per-client filter returned his own empty list. Fix: added trombonetimollc@gmail.com to BOTH config.js ADMIN_EMAILS (commit on origin/main) AND content_admins table. The DB half was caught ONLY by testing end-to-end as that exact account (frontend showed admin picker but "No clients yet" until the content_admins row existed).

**How to apply:** To grant content-hub admin, add the email to config.js ADMIN_EMAILS AND insert into content_admins. To verify a client can see their items, mint that client's session and load the page (see [[reference-view-authed-dashboard]]) - do NOT just check the DB. Two admin gates, verify as the real account. Related: [[feedback-new-route-check-auth-allowlist]], [[feedback-diagnose-with-control-and-surface-failures]].
