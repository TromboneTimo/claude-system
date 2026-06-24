---
name: project_daily_email_queue_cancelled_20260601
description: "2026-06-01 cancelled the entire scheduled Daily Email broadcast queue; old format abandoned, new formats coming. Plus the unexplained AC send-time stop incident."
metadata: 
  node_type: memory
  type: project
  originSessionId: 25cd0445-216c-44ea-993d-1bfdbf782ae2
---

2026-06-01: Timo cancelled ALL scheduled Daily Email broadcasts (AC campaigns 619-625, the June 1-7 queue). Deleted in ActiveCampaign + their email_send_ledger rows cleared. Reason: he's abandoning the old daily-email format (too soft/weak) and moving to NEW email formats. **Do NOT auto-reschedule the old daily-email batch.** Automations/funnel drips (campaigns like "Quick Question?", "Last Chance") were left running, separate from the broadcast queue.

Incident + fix: the May 29/30/31 daily broadcasts (616/617/618) were STOPPED by ActiveCampaign at send time with 0 recipients (status=4, send_amt=0) even though the account was sending automations fine, list 13 had 4,188 active subs, sender + config were byte-identical to sends that worked, and our dashboard code never stops campaigns. Root cause is NOT visible via the AC v3 API; only the AC campaign **report UI** shows the stop reason (likely a send-time content/deliverability auto-halt or a manual stop). **Before relaunching new formats, check campaign 618's report in AC UI**; if it's an account deliverability flag, new formats stop too.

PIPELINE PROVEN HEALTHY 2026-06-01: a real scheduled send to list 20 (trombonetimo@gmail.com) fired on time and delivered (campaign 626). So the send/schedule/dedup pipeline works; the stops were AC-side on those specific campaigns.

WATCHDOG ADDED 2026-06-01 (api/ac.js reconcileScheduled, commit 49b7efc): the */30 pg_cron reconcile now flips any past-due scheduled proposal that AC did NOT ship to status='send_failed' and fires a loud Slack alert (notifySlackSendFailed) to the Harrison + Timo channels. 15-min grace before flagging a non-stopped campaign. Alerts ONCE (status flip prevents re-alert). New proposal status value: 'send_failed' (terminal; dashboard emails.html has no column for it yet, optional follow-up). This closes the silent-failure gap that hid the original incident. See [[project_email_engine]], [[project_email_deliverability_from_address]], [[feedback_dup_send_db_gate]].
