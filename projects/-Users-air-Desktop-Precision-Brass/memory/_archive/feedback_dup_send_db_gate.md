---
name: feedback_dup_send_db_gate
description: "Any endpoint that CREATES an outbound artifact (AC campaign, email send, charge, post) needs a DB-enforced unique claim BEFORE creating, never check-then-create. Caught after a double-send blasted ~4,150 subscribers twice."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ddcf6d58-a0fb-418d-80a9-23364d0dd89a
---

On 2026-05-22 Harrison's "Daily Email 1" broadcast went out TWICE to ~4,150 subscribers on list 13, two days running (05-21 and 05-22). Timo found it because his Gmail thread showed "Harrison Ball 2" (two identical messages).

Root cause: the dashboard "Schedule all" button (`scheduleAll()` in dashboard/scheduled.html) looped the approved queue and, per item, (1) POSTed to `/api/ac-send` which created an AC campaign, then (2) flipped the proposal to status=scheduled. The endpoint had ZERO idempotency: every call created a campaign. A double-fired / overlapping "Schedule all" run created a second campaign for the first 3 queue days before the status flip dropped them from the queue. AC does not dedupe across separate campaigns, so each campaign delivered to the full list.

**Why:** check-then-create always has a TOCTOU race. A client button-disable does not survive double-clicks across tabs, retries, or overlapping runs. The only race-proof prevention is a database constraint.

**How to apply:** for ANY endpoint that creates an outbound, hard-to-reverse artifact (email campaign, send, charge, social post), use **claim-then-create** against a DB UNIQUE constraint:
1. INSERT a "claiming" row keyed by the natural send identity (here: `email_send_ledger` UNIQUE(target_list_id, scheduled_for)).
2. If the insert wins, create the external artifact, then stamp the row with its id + status='created'.
3. If the insert hits the unique violation (Postgres 23505 / PostgREST 409): look up the existing row. If it has the artifact id, return it (idempotent success). If not, another claim is in flight, return 409.
4. On any creation failure after claiming, DELETE the claim row so a retry is clean.
5. FAIL-CLOSED: if the gate can't run (e.g. service key missing), refuse the send rather than risk a duplicate.

Stack independent backstops: a client re-entrancy flag + skip-already-scheduled filter, an AC-level same-day-same-list pre-create check, and a reconciler sweep that scans for two scheduled campaigns on the same list+day and Slack-alerts (detection, not auto-delete, because auto-picking which to kill is itself risky).

Implementation lives in `dashboard/setup/schema.sql` (email_send_ledger), `api/ac-send.js` (claimSlot/confirmSlot/releaseSlot), `api/ac.js` (detectDuplicateScheduled/notifySlackDuplicate), `dashboard/scheduled.html` + `dashboard/broadcast.html` (client guards). See [[feedback_vercel_kills_fire_and_forget]] for the related await-side-effects rule and [[feedback_2026_05_13_session_lessons]] for the AC third-party send-read-back discipline.
