---
name: feedback_never_hard_block_user_send
description: "Timo (the owner) must never be HARD-BLOCKED from sending his own email. Content lint warns, never prevents. The list-allowlist safety gate is the ONLY thing allowed to stop a send."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7f59b606-524f-4bf6-8cec-391e67c8d3f7
---

Standing rule, set by Timo 2026-06-07: "In general, I should never be blocked from sending something. I should just be warned."

**Why:** the dashboard email-lint kept HARD-BLOCKING him from broadcasting his own approved email (the backwards "Harrisson" spell-rule, plus Forbes/placeholder/etc bans all severity:'block'). He's the owner; the tool should advise, not prevent.

**How to apply:**
- Dashboard content lint is now WARN-ONLY. `dashboard/emails.html` (the `goto_broadcast` gate + banner) and `dashboard/broadcast.html` (`lintBlocked`/`blocked`) no longer disable Send/Schedule on `blockCount>0`. They show a heads-up toast + banner and proceed. The rule severities in `dashboard/lib/email-lint.js` still compute block/warn (so the warning text stays informative), but nothing in the human's send path keys off them to PREVENT sending.
- The ONE gate that stays hard: the **list allowlist** (`is_send_allowed` / `AC_SEND_ALLOWED_LIST_IDS`). That is a different, real safety gate (prevents firing a non-allowlisted real list), not a content-quality gate. Never neutralize it. See [[never-test-send-to-real-list]].
- Same principle for MY gates: warn the user, don't hard-block THEM. (My own deploy/quality gates that gate ME are fine.)
- Tradeoff to flag: warn-only means the human CAN send with a real problem still present (e.g. a placeholder apply link the lint doesn't catch). So surface those loudly in chat, since the dashboard no longer stops them.
