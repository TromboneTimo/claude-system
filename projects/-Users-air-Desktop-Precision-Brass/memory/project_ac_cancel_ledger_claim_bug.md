---
name: project_ac_cancel_ledger_claim_bug
description: "Cancelling a scheduled email deletes the AC campaign but does NOT release its email_send_ledger slot claim, so re-scheduling silently reuses the dead campaign id (phantom schedule). Release the ledger row when cancelling."
metadata: 
  node_type: memory
  type: project
  originSessionId: 01124e67-071c-4f2b-b966-013999b596bd
---

The email scheduling pipeline claims a (target_list_id, scheduled_for) slot in `email_send_ledger` BEFORE creating the AC campaign (the duplicate-send gate in `api/ac-send.js` -> `claimSlot`). The gate is what makes double-sends impossible.

BUG (hit 2026-06-08, Hannah "How many years" email): `api/ac-cancel.js` deletes the AC campaign and flips the proposal back to approved, but it never deletes/releases the matching `email_send_ledger` row. So after a cancel, the slot stays claimed by the now-deleted campaign id. The next time someone clicks Schedule for that slot, `claimSlot` sees the stale claim and returns `{owned:false, existingCampaignId:<dead id>}` -> `/api/ac-send` takes the "duplicate_prevented" idempotent-success path and returns the DEAD campaign id WITHOUT creating a new campaign. The dashboard then shows status=scheduled (phantom) while ActiveCampaign has nothing scheduled. Nothing sends.

Symptom: dashboard Scheduled tab shows the email scheduled, but `GET /api/3/campaigns/{id}` 404s and there is no status=1 campaign for that date.

Manual fix that worked: `DELETE email_send_ledger?id=eq.<row>&ac_campaign_id=eq.<deadid>` to free the slot, then call prod `/api/ac-send` (authed, from the Playwright prod session) with target_list_id=13 ("Daily Email 1"), the proposal body, scheduled_for_iso, proposal_id -> creates a REAL campaign. Then PATCH the proposal's ac_campaign_id to the new id. Verify: campaign status=1, sdate correct, send_amt=0, exactly ONE campaign for that date, ledger row points to the new id.

PERMANENT FIX (applied + deployed 2026-06-08), defense in depth:
1. `api/ac-cancel.js` now DELETEs the `email_send_ledger` rows for the cancelled `ac_campaign_id` (releases the slot) and returns `ledger_released` count. So cancel + reschedule always creates a real campaign.
2. `api/ac.js` `flagPhantomSchedules()` (wired into `?action=reconcile-scheduled`, runs every reconcile tick) checks FUTURE `status=scheduled` proposals: if the `ac_campaign_id` has no live AC campaign with `status=1` (404/stopped/none), it flips the proposal to `send_failed` + Slack-alerts, BEFORE the send time. Fail-safe: non-404 AC errors (429/5xx) are skipped, never false-flagged.
3. `dashboard/scheduled.html` renders that as a red "WON'T SEND" badge with a tooltip that covers both "AC dropped it" and "phantom / no live campaign".
Meta-lesson: a status field / badge / API ack is NEVER proof of the real-world effect. Verify the real object (the AC campaign: status=1, future sdate, send_amt). Relates to [[feedback_verify_send_not_ack]], [[feedback_fix_the_shipping_artifact_not_the_proxy]], [[project_reconcile_supabase_pgcron]]. The daily broadcast list is AC list 13 "Daily Email 1".
