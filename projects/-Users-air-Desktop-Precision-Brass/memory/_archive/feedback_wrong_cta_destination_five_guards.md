---
name: wrong-cta-destination-five-guards
description: "5 broadcasts linked the email-capture page instead of the masterclass VSL; 5 mechanical guards now prevent wrong-destination links. Registry > recent artifacts, ALWAYS."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

2026-06-11: Timo, furious, after 5 sent broadcasts (incl. quick_question, beware, hollywood-bowl) linked `webinar-registration-pb` (the email CAPTURE page) instead of the masterclass VSL: "I told you this multiple times... It needs to go straight to [training-room], not the registration link."

**Why it happened:** two sources of truth disagreed. [[project-canonical-links]] (canon) said training-room for email CTAs; the email-lint rule (stale, 2026-05-13) and the most recent sent emails said webinar-registration-pb. I anchored on the recent artifacts and the lint instead of the canonical memory, then BUILT MORE SYSTEM (per-email el tags) on top of the wrong link. A wrong convention, once shipped, self-propagates: every "copy the latest email's format" step spreads it.

**The 5 guards (all implemented 2026-06-11):**
1. **One executable registry.** `CANONICAL_MASTERCLASS_URL` in dashboard/lib/email-lint.js, mirrored in [[project-canonical-links]]; changed together or not at all. URLs are COPIED from it, never typed, never taken from a past email.
2. **Wrong-destination lint BLOCKS.** `wrong-destination-registration-page` (any webinar-registration-pb in a broadcast body) and `masterclass-url-not-canonical` (any training-room variant not byte-identical to canon, incl. stray el= or stale webinar_ext). Both autoFix to canonical. Fires at draft, push, and dashboard pre-send.
3. **Push preflight href diff.** pb-email-push LINK RULES: every body href must be the registry URL or a verified testimonial link; any other URL = STOP and ask.
4. **Canon beats artifacts.** When memory canon and a recent email/lint rule disagree, the canon wins and the discrepancy is surfaced to Timo immediately; never silently resolve toward "what the last email did."
5. **Verify the assembled message.** Before confirming any schedule/send, grep the actual AC campaign HTML (campaignMessages->messages) for the canonical URL; wrong or missing = surface, don't proceed.

**Bonus correction:** per-email `el=` tagging is REDUNDANT, not just banned: the HYROS<->AC integration auto-injects per-campaign el tags (source names like @quick-question already appear on HYROS sales). Per-send revenue attribution already exists natively. Never re-propose manual tagging.
