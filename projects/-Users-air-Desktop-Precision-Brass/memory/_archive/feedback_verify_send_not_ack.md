---
name: feedback_verify_send_not_ack
description: "An API/tool \"success\" ack is NOT proof of delivery. Verify the real side-effect (send_amt/row count/rendered result) before saying done, and never take an irreversible action right after a fire-and-forget op. Cross-workspace."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7f59b606-524f-4bf6-8cec-391e67c8d3f7
---

Two linked failures from 2026-06-07 (Precision Brass test send), both violations of rules I already had.

1. **An optimistic acknowledgment is not delivery.** ActiveCampaign's `campaign_send` returned `"Message sent"` and I told Timo it was delivered. It was not. The only proof was `send_amt` incrementing to 1 (and `status=5`). I claimed done off a string ack, twice. This is the same theater verification as "curl returned 200" or "the API didn't error."

2. **Never take an irreversible action right after a fire-and-forget operation.** I fired a queued send, then DELETED the campaign seconds later to "tidy up", which killed the in-flight message. Nothing arrived. The user got nothing, then later got two (because I then double-fired test + broadcast as belt-and-suspenders).

**Why:** I had standing rules for both ([[feedback_verify_with_eyes_not_curl]], [[feedback_ship_right_not_fast]], lead-with-caveats) and broke them under pressure when the user was angry and rushing me. Advisory memory is the weakest enforcement; speed pressure overrides it.

**How to apply (every send/deploy/destructive op, all workspaces):**
- Before saying "sent / delivered / done": read the REAL post-state (send_amt, the inserted row, the rendered pixels, the 200 from the user-facing URL), not the trigger's return value. Quote the number.
- Do destructive/irreversible steps (delete, overwrite, reset) LAST, and only after the side-effect you care about is confirmed complete. A queued op is not a completed op.
- One verified mechanism beats two unverified ones. Double-firing to "make sure" creates duplicates and confusion.
- Lead the report with the real state and any caveat, not the hopeful state.
- Know the actual delivery path before operating it (PB real sends ship via the scheduler on `status=1 + sdate`, not the flaky `campaign_send`). See [[project_ac_test_send_mechanism]].
