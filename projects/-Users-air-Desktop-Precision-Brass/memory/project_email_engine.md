---
name: Precision Brass Email Engine
description: pb-email + pb-email-push skills, dashboard pages, schema, and AC/HYROS Phase 2 plan for Harrison's email proposal and analytics flow.
type: project
originSessionId: 7f540398-3cb8-4b73-9023-2f87ee04eec4
---
The email side of Harrison's content engine, built 2026-04-28. Mirrors the YouTube content engine (pb-script + pb-ideas-push + pb-script-write) but compressed: pb-email returns COMPLETE drafts (not just ideas), so there is no separate writer phase.

## The 2 skills

- `~/.claude/skills/pb-email/` (Phase 1+2 fused). 6 parallel mining agents + 1 sequential auditor. Returns 5-draft menu where each draft is a complete email body + reasoning + VOC quotes. Reads `voc/emails/extracts/harrison-email-voice.md` (302-line voice catalog), 3 FINAL emails in `output/`, and emails 1-7 of the webinar sequence (NEVER 8-12). Voice rotation log at `voc/email_voices_used_log.jsonl` prevents recycling the same voices.
- `~/.claude/skills/pb-email-push/` (Phase 1.5). Pushes Timo-approved drafts to the dashboard via curl POST to Supabase email_proposals table. Same zero-drop preflight + silent-dedup contract as pb-ideas-push.

## The 2 dashboard pages

- `dashboard/emails.html`. Email Proposal Queue. Mirrors scripts.html structurally (3-pane pipeline: Harrison's review / Timo's plate / Done). Status flow: proposal_pending -> approved -> changes -> rejected -> scheduled -> sent. Action buttons: Approve, Request Changes, Reject, Schedule, "Send to ActiveCampaign" (disabled, Phase 2).
- `dashboard/email-analytics.html` (renamed from `email.html` on 2026-04-28). Reads from Supabase email_sends table. 5 tabs (sales / assisted / replies / ctr / youtube views). "Log a Send" form on the page for manual entry until AC + HYROS sync ships. `/email` path redirects via vercel.json.

## Schema (in dashboard/setup/schema.sql)

- `email_proposals`. Drafts awaiting Harrison review. Columns: id, subject, subject_alts, preheader, body, ps_text, ps_type, hook_angle, pain_point, audience (broadcast / reengagement / webinar-push / discovery-followup), cta_type, cta_url, rationale, voc_quotes, source_tags, status, notes, history, scheduled_for, ac_campaign_id, timestamps.
- `email_sends`. Sent emails with AC + HYROS metrics. Columns: id, proposal_id (FK), subject, sent_at, list_size, opens, clicks, replies, unsubscribes, booked_calls, closed_deals, direct_revenue, assisted_revenue, youtube_views, hyros_synced_at, ac_synced_at, timestamps.

## AC + HYROS sync (Phase 2, NOT BUILT YET)

User has the API keys and confirmed wiring is desired. Built path:
1. Schema, dashboard pages, and manual entry form are LIVE now.
2. `scripts/sync-email-stats.mjs` (Node CLI) is the future entry point.
3. Env vars already documented in `dashboard/setup/.env.example` (ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY, HYROS_API_KEY, SUPABASE_SERVICE_ROLE_KEY).
4. AC publish step (Send to ActiveCampaign button on emails.html) is also Phase 2.
See `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/project_future_todos.md` items 6 and 7 for the buildout plan.

## Why this exists

Timo asked for an email system that mirrors the script system. Two pages:
1. Proposals page (like scripts.html) where Harrison reviews drafts produced by agents that mined his VOC corpus.
2. Analytics page that ranks every send by CTR, replies, booked calls, revenue.

He wanted Harrison to NOT copy-paste between systems. Long-term goal: agents push to AC directly. For now, manual entry on analytics is fine and the proposal flow works end-to-end without AC integration.

## How to apply

When Timo says "email ideas" / "draft emails" / "what should we send":
- Spawn `/pb-email` (the skill triggers automatically on those phrases).

When Timo says "push these emails" / "send to harrison":
- Spawn `/pb-email-push` after Timo picks from the menu.

When asked to open the email pages:
- Proposals: `open -a Safari /Users/air/Desktop/Precision-Brass/dashboard/emails.html`
- Analytics: `open -a Safari /Users/air/Desktop/Precision-Brass/dashboard/email-analytics.html`

If the schema has not been applied to Supabase yet, paste `dashboard/setup/schema.sql` into the Supabase SQL editor. The new tables are additive and idempotent.
