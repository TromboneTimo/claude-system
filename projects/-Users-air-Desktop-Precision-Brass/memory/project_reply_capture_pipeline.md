---
name: project_reply_capture_pipeline
description: "How email reply capture works (AC webhook to Supabase email_replies to read via MCP). Runs OPEN, no dashboard tab by Timo's choice. The 401 gotcha."
metadata: 
  node_type: memory
  type: project
  originSessionId: af1dedbd-b693-4fcb-9923-a4abb532695b
---

Email REPLY capture for Precision Brass, fixed/verified 2026-06-06.

**Flow:** AC webhook "PB Dashboard reply receiver" (id 8, event=`reply` only, state active, sources public/admin/api/system) POSTs to `api/ac-reply-webhook.js`, which stores into Supabase `email_replies` (body_clean strips quoted chains, plus body_raw/body_html/subject/raw_payload). Read it via the precision-brass-ac MCP: `get_recent_replies`, `search_replies`, `reply_stats`. Also `api/ac-replies.js` (authed) returns the feed.

**THE GOTCHA (why 0 replies for weeks):** endpoint required a secret via `X-Webhook-Secret` header or `?secret=` query param, but AC's webhook UI CANNOT send custom headers and its "Send sample data" DROPS query strings, so every event silently 401'd and nothing stored. Fix: removed `WEBHOOK_SECRET` from Vercel prod, redeployed. Endpoint now runs OPEN (URL-obscurity only). **Do NOT re-add WEBHOOK_SECRET** unless you confirm AC actually delivers it, or you break reply capture again.

**Reply tracking** must be on per-campaign or AC never fires `reply` (MCP `send_draft_through_campaign` sets trackreplies=1 automatically; manual AC-UI sends need the box ticked).

**No dashboard reply tab by design.** Per Timo 2026-06-06 he just wants Claude to read replies via MCP. The old emails.html feed was removed 2026-05-09. Don't rebuild a UI unless asked.

AC API key already lives in `~/.claude/credentials/MASTER.md` line 97 (`ACTIVECAMPAIGN_API_KEY`, url `https://hballmusic.api-us1.com`, auth `Api-Token:`). It is NOT needed for reply capture. See [[project_credentials]].
