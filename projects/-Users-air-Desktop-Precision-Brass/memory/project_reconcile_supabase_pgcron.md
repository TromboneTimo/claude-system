---
name: project-reconcile-supabase-pgcron
description: "The scheduled->sent email reconcile runs in Supabase pg_cron (every 30 min), NOT a Vercel cron. Where to find/edit it."
metadata: 
  node_type: memory
  type: project
  originSessionId: d228715a-5ca5-4603-b90f-9fe73056656e
---

As of 2026-05-25, the email `scheduled -> sent` reconcile is owned by **Supabase pg_cron**, not a Vercel cron.

**Why moved:** the old Vercel cron ran `0 10 * * *` (10:00 UTC) but daily emails send at 11:00 UTC, so it checked an hour too early and never caught same-day sends. The dashboard's sent-state only updated via the on-page-load `triggerReconcile()` in `dashboard/scheduled.html`. Vercel Hobby also caps crons at once-per-day, so we couldn't poll more often there. This caused the 2026-05-24 "did the email even fire?" scare (the email DID fire via AC's native scheduler; the DASHBOARD just hadn't reconciled). NOTE: AC's own scheduler sends the emails. No cron of ours is in the send path. The reconcile is reporting-sync only.

**Where it lives now:** Supabase project `iwlernqpwdsjarygoeog`, `pg_cron` job `reconcile-scheduled-emails`, schedule `*/30 * * * *`. It uses `pg_net` (`net.http_post`) to call the EXISTING endpoint `https://precision-brass-dashboard.vercel.app/api/ac?action=reconcile-scheduled` with header `x-perf-secret: <EMAIL_PERF_SECRET>`. The reconcile LOGIC still lives in `api/ac.js` `reconcileScheduled()` (unchanged, it was correct). Extensions `pg_cron` + `pg_net` are enabled.

**To inspect/edit the job** (via Management API + PAT, see [[project-credentials]]):
```
select jobid, schedule, jobname, active, command from cron.job where jobname='reconcile-scheduled-emails';
-- responses land in net._http_response (status_code, content)
select id, status_code, left(content,160) from net._http_response order by id desc limit 5;
```
Reschedule with `cron.schedule('reconcile-scheduled-emails', '<cron>', $job$ ... $job$)`; unschedule with `select cron.unschedule(jobid) from cron.job where jobname=...`.

**Backstop:** `triggerReconcile()` on `/scheduled` page load still runs the same endpoint. The Vercel `reconcile-scheduled` cron was REMOVED from `vercel.json` (commit 7a9b9bb) so there is a single owner; only the `meta-ads-ingest` daily cron remains on Vercel.

Verified end-to-end 2026-05-25: a manual `net.http_post` returned `status_code 200` with the reconcile JSON. See [[project-email-engine]].
