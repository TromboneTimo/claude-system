---
name: feedback-sourceless-lead-dig
description: "When a lead or sale shows no acquisition source (HYROS firstSource NONE, an \"email lead\" with no real origin, or the dashboard \"doesn't say where they came from\"), do NOT accept it at face value. Actively dig across HYROS + ActiveCampaign and identity-stitch likely-same-person records before concluding it is sourceless."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: defd3a9f-9783-4b7f-ac74-e4760a101955
---

A "sourceless" lead/sale is a prompt to investigate, never a finished fact. A plain HYROS API refresh only reports `firstSource: NONE`; the true source usually lives elsewhere (a tagged click on a different email/device, an AC tag, a Calendly booking). Cross-reference before concluding, and dig every time.

**Why:** 2026-06-17, Benjamin Piela. The dashboard showed his $6,800 sale as sourceless. HYROS `firstSource` was NONE on the buying email (`pielabenjaminj`, tags `!calendly` + `$stripe-6800`). But a SECOND email (`benjaminpiela666`), same name, same evening, same Grand Rapids 616 area, had `firstSource = YouTube` (`@youtubebreathetimo`). One human, a YouTube-driven $6,800 sale, but HYROS treated the two emails as separate leads and never stitched them, so the money looked sourceless. Accepting "no source" would have credited a real YouTube sale to nothing. Timo: "when I see a lead without a source, then definitely do some tracking."

**How to apply (run this dig whenever a lead/sale has no source):**
1. HYROS leads API by email -> check `firstSource`, `lastSource`, `tags`. Real first-touch tags look like `@youtubebreathetimo`, `@meta...`, or per-email `@live-...-masterclass-...-email` tags.
2. If `firstSource: NONE` -> pull the AC contact (list_contacts search by name, or get_contact_by_email): tags, automations, list, cdate, `last_open_date`/`last_click_date`, IP (`2130706433` = `127.0.0.1` = API/integration-added, e.g. Calendly), trackingLogs.
3. Look for IDENTITY FRAGMENTATION: the same person on multiple emails. Search by exact phone, name + same day, email local-part root, area code / city. The source frequently sits on a different email's record than the purchase.
4. Stitch probable twins (name + phone/area + same-evening + home-wifi-vs-mobile IP pattern) and credit the sourced twin's channel. Surface as a confidence-rated suggestion; never silently merge (classifier gate, [[canon_attribution_analytics]]).
5. State confidence honestly. HYROS never auto-merges different emails/devices. Cases with different email AND phone AND device AND IP (like Benjamin) are unsolvable deterministically: only a probabilistic flag. A source never captured (no tagged click ever) is unrecoverable, only inferable.

Root cause of sourcelessness: (a) the entry link was not HYROS-tagged (Calendly/booking links), (b) cross-device means a different cookie, (c) a different email means no merge key. Planned systemic fix: a sourceless-sale watchdog (Slack alert + auto-stitch candidates -> dashboard panel for human confirm) + instrument every entry point with HYROS tracking + capture phone as a stitch key. Most acquisition is Meta ads (~60%) + YouTube (~14%); "email" is the follow-up channel, almost never the true source. See [[canon_attribution_analytics]].
