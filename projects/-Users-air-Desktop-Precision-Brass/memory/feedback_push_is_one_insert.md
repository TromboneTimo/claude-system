---
name: feedback_push_is_one_insert
description: "When Timo says \"push to dashboard\", do ONLY the insert. No quote-hunting, no schema spelunking, no extra metadata gathering."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b68e1ad7-380c-446e-804f-d718d37adf2f
---

When Timo has already approved an email draft in chat and says "push it to the dashboard," the push is **one database insert**. Build the `email_proposals` row from what is ALREADY in the chat draft, clear the machine link gate, POST once. Done.

Do NOT, at push time:
- grep `voc/sales-calls/raw/` to satisfy the skill's "1 testimonial + 1 sales-call quote" metadata minimum. That field is review-panel metadata, not a prerequisite for getting the email onto the dashboard. The Martin testimonial precedent row shipped with testimonial-only quotes. Use whatever quotes are already in the chat draft.
- inspect existing rows to "learn the schema convention" (it is known: body = full HTML incl. P.S./P.P.S. inline, ps_text="", anchors as `<a href>`).
- write elaborate rationale prose or chase extra source_tags.

**Why:** 2026-06-24, Sharon testimonial push. Timo gave me the video AND the transcript, approved the draft in chat, said "push it." I then ran drafting-grade gates at push time (hunted a sales-call quote, inspected rows) and burned many tool calls and tokens on a one-insert task. Timo: "I really just wanted the email pushed to the dashboard. It's just one simple process, then you can do the other shit." The only unavoidable friction was the link-gate hook (`email-link-gate.sh`) hard-blocking the YouTube testimonial link, which forced a re-POST with `PB_LINK_GATE=skip` (legit because Timo explicitly directed that testimonial link).

**How to apply:** "Push" in LEAN MODE means lean. Required at push: correct already-approved content, link gate, insert, read-back verify. Everything else (sales-call evidence, rotation log to `voc/email_voices_used_log.jsonl`, richer tags) is a SEPARATE step Timo asks for explicitly. If a required metadata field is genuinely empty, fill it from the chat draft or ask in one line. Never go mining. See [[canon_email_shipping]] (LEAN MODE) and [[feedback_minimal_signal_not_data_dump]].

**Testimonial-link fast path:** if the email links a testimonial video not yet in `voc/testimonials/raw/`, the link gate hard-blocks. With Timo's explicit approval of that link, POST with `PB_LINK_GATE=skip` on the FIRST POST when the only flagged link is the owner-approved testimonial, to avoid the retry.
