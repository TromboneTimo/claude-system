---
name: project_ac_test_send_mechanism
description: "HOW to reliably test-send a Precision Brass email to Timo (list 20) via the AC API, and the two traps that waste time. Read before any AC test send from CLI/MCP."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7f59b606-524f-4bf6-8cec-391e67c8d3f7
---

Goal: get a test email into trombonetimo@gmail.com (the ONLY sub on AC list 20 = "Test - Timo Solo"). Safe per [[never-test-send-to-real-list]]. Never list 13.

## The reliable path (verified working 2026-06-06)
1. Create the campaign on list 20 (MCP `send_draft_through_campaign` with a list-20 source, OR raw legacy `message_add` + `campaign_create` with `p[20]=20`). Confirmed **list-20-only source campaigns: 626, 596, 586** ("Source Template - Timo Test").
2. The campaign lands `status=1` but parked ~5h in the FUTURE (legacy `sdate` timezone quirk) so the scheduler won't ship it.
3. FIX: v3 PUT `campaigns/{id}` with `{"campaign":{"sdate":"<Chicago wall-clock>-05:00"}}` set to NOW (use UTC-5, a couple min in the past). AC's scheduler then ships within ~3 min. Poll `send_amt` until it hits 1 and `status` flips to 5. That is THE proof of delivery (this is how the 4am daily emails actually ship too).

## Two traps that cost a whole session
1. **`campaign_send action=send` (instant broadcast trigger) consistently fails on this account: `result_code 0, "Message not sent"`.** Do NOT rely on it. The scheduler (sdate=now + status=1) is the real delivery mechanism. `action=test` with `email=...` returns "Message sent" and works for a single address.
2. **NEVER delete the campaign right after firing.** A test/send is queued; deleting the campaign seconds later kills the in-flight message and nothing arrives. Leave the campaign in place, verify `send_amt`/`ldate` FIRST.

Sender that authenticates / lands: `harrissonball@precisionbrass.info` (the daily-email domain), fromname "Harrison Ball". AC creds in `~/.claude/secrets/precision-brass.env` (`ACTIVECAMPAIGN_URL`, `ACTIVECAMPAIGN_API_KEY`). Legacy API = POST `{url}/admin/api.php` form `api_key,api_action,api_output=json,...`.

Verify the whole HTML render to PNG (headless Chrome, file:// is blocked in Playwright so serve via `python3 -m http.server`) and READ it before sending. Video embeds in email = centered clickable thumbnail (`i.ytimg.com/vi/<id>/hqdefault.jpg`) linking to the watch URL, with a CSS play-button overlay; real iframes don't render in inboxes.
