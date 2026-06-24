---
name: feedback_email_ps_must_be_in_body
description: "When pushing an email to email_proposals, the P.S. + CTA MUST live INSIDE the `body` field. The dashboard broadcast sends `body` only and silently drops `ps_text`. Verify the ASSEMBLED AC message, not proposal fields."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7f59b606-524f-4bf6-8cec-391e67c8d3f7
---

Near-miss 2026-06-07: the Hannah email was scheduled to the real 4,105-sub list (list 13) for 4am with NO P.S. and NO call-to-action. The whole conversion path was gone. Caught by Timo noticing the broadcast preview, NOT by my verification.

**Root cause:** I pushed the proposal with the P.S. + "Apply and book your chat here" CTA in the separate `ps_text` column. `dashboard/broadcast.html` loads ONLY `p.body` into the send editor (`bcBody`) and sends that; **`ps_text` is never included.** So the P.S. silently vanished from the actual send. The convention was already documented ([[feedback_email_html_links_and_cta]]: "P.S. lives inside the body, not ps_text") and I violated it.

**How to apply:**
- When pushing ANY email to `email_proposals` (pb-email-push or manual), put the **P.S. and every CTA INSIDE the `body` HTML**. Leave `ps_text` empty (it's display-legacy; the broadcast does not send it).
- Before declaring an email ready for a real send, **pull the assembled artifact that actually ships** (the AC message HTML via `campaigns/{id}/campaignMessages` -> `messages/{id}`) and confirm it contains the body, the P.S., the CTA link, the video, correct spelling, and the right list. Do NOT trust a render of the standalone draft or the proposal fields in isolation, that is a proxy, not the shipped thing.
- This is the recurring lesson: **verify the exact thing that ships, end-to-end.** See [[feedback_verify_send_not_ack]].
- TODO: harden pb-email-push so P.S. always goes into `body`, and ideally make `dashboard/broadcast.html` warn if `ps_text` is non-empty (silent-drop footgun).
