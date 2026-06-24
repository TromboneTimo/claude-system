---
name: feedback-warn-dont-block-when-timo-oversees
description: "When Timo is manually reviewing/directing an action, gates must WARN loudly, never silently hard-block. YouTube email links are now warn-only."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 17134246-d29e-4c59-8135-eb0885ece65e
---

When Timo is in the loop, looking over the work and manually setting/approving it, a gate must **warn loudly and let it through**, never silently hard-block. A block he didn't expect, gated on an obscure token buried in a hook, is the worst outcome.

**Why:** 2026-06-24. The Martin testimonial email had a Timo-directed YouTube CTA. Publishing kept getting hard-blocked by `email-link-gate.sh`, which required a `YT_OK=1` token that was buried and undocumented. Timo: "it shouldn't just block just because it has a YouTube link... I should just be warned... Under no circumstance should you block rules if I'm looking over it and I'm manually setting it. It was buried deep somewhere and I had to double-check to see that it wasn't set. This is absolutely atrocious."

**The fix shipped (warn-only, tested):**
- `~/.claude/hooks/email-link-gate.sh`: YouTube link -> prints `EMAIL LINK GATE [WARNING -- NOT blocking]` to stderr and `exit 0`. No token needed. Removed the `YT_OK=1` block.
- `dashboard/lib/email-lint.js` rule `no-youtube-links`: already `severity: 'warn'` (blockCount unaffected). Comment updated.
- `email-angle-gate.sh` injected LINK LAW text + `email-send-rhythm-gate.sh` comment: updated to "YouTube = warn-only, never blocked."
- STILL hard-block (genuinely-always-wrong, money-critical, all overridable with `PB_LINK_GATE=skip`): `webinar-registration-pb` capture page, non-canonical `training-room` URL, placeholder tokens, marketer-opener "nobody tells you" family. These are mistakes Timo would never set on purpose, so they don't violate the principle.

**How to apply:**
- Distinguish "legit thing Timo sometimes wants" (warn) from "always a mistake" (block, but bypassable). Never gate the former behind a hidden token.
- When an action WILL trip a hard gate, warn Timo IN CHAT proactively, before he hits the wall. The visible warning he reads is the one from me, not buried hook stderr.
- After editing any shared hook, test ALL branches (shared hooks break everything): confirm the softened case passes AND the guards still fire. Done here via piped JSON simulation.
- Related: [[feedback_testimonial_not_in_db_just_add_it]], [[canon_email_shipping.md]] (never-hard-block-owner), [[feedback_push_is_one_insert]].
