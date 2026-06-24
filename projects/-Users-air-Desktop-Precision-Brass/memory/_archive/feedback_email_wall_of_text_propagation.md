---
name: feedback-email-wall-of-text-propagation
description: Editing an email's body row in Supabase does NOT update a campaign already created in ActiveCampaign. Scheduled AC campaigns hold their own copy of the HTML. To fix a scheduled email's formatting you must re-PUT the AC message, not just fix the DB row.
metadata:
  type: feedback
---

**From 2026-06-04 (Timo, furious):** scheduled emails rendered as a wall of block text.
Root cause was NOT generation -- the stored email_proposals bodies are short, one-thought
`<p>` paragraphs. The problem: the 8 imminent AC campaigns (629-636, June 4-11) were
created BEFORE the bodies were reformatted, so their AC message HTML still held the old
MERGED paragraphs (8-16 `<p>`, paragraphs 350-730 chars). Reformatting the Supabase row
never reached the already-created AC campaign. The fix didn't PROPAGATE to in-flight sends,
and nothing enforced it.

**Rules:**
1. A scheduled AC campaign carries its OWN copy of the HTML (in /api/3/messages/{id}). To
   fix its formatting, fetch the campaign's message id (`/campaigns/{cid}/campaignMessages`),
   re-style the clean Supabase body, and `PUT /api/3/messages/{id}` with {message:{html,text}}.
   Editing email_proposals alone does nothing to an already-scheduled campaign.
2. `applyHarrisonStyling` (api/ac-send.js) now gives every `<p>` an explicit
   `margin:0 0 16px` so short paragraphs always render with gaps in EVERY client (some
   inboxes strip the default `<p>` margin and fuse paragraphs into a block).
3. email-lint.js has a `wall-of-text` rule (warn) flagging any `<p>` over ~280 chars.
   Clean Harrison emails top out ~270; walls were 350+. Catches a merged block before
   scheduling. See [[feedback_email_html_links_and_cta]].
4. To audit: pull each scheduled campaign's AC html and check the LONGEST paragraph, not
   just the `<p>` count. The merged walls had few `<p>` with huge inner text.
