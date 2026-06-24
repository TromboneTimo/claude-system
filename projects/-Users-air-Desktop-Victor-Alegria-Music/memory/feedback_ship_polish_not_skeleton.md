---
name: ship-polish-not-skeleton
description: "When building UI features, do NOT ship the literal minimum. Infer the surrounding polish before declaring done. Orphan buttons, ugly defaults, inconsistent labels, buried warnings, and disconnected flows are not \"ready to test\", they're \"ready to be yelled at\"."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2e60061b-e9d8-4829-a2d9-34e0c95fb455
---

When building a UI feature for Timo (especially dashboard work), before declaring it "ready" / "live" / "done", run this checklist:

1. **Orphan UI?** Any button or element that doesn't do something useful? Delete it. (Caught: Today button on calendar nav that did nothing because the user was already on today's month.)
2. **Consistent flows?** Does the new flow look and behave like related flows in the same app? Single-email vs multi-email schedule should not have different UIs. (Caught: broadcast.html had its own Send Now + Schedule split that didn't match the new /scheduled?ids= queue+calendar layout.)
3. **Obvious affordance?** Does every interactive element LOOK clickable? Default <select> on dark mode = ugly + unclickable-looking. Custom button with stripe, label, big chevron, raised shadow = obviously a button. (Caught: native dropdown that looked unclickable.)
4. **Diagnosability?** If something is wrong, can the user click to see why? Read-only labels that hide the underlying data are a trap. (Caught: scheduled email pills on the calendar that you couldn't click to see body/time/list.)
5. **Warning prominence.** Does the warning actually warn? Putting a red banner at the BOTTOM of the page when the action button is at the TOP fails. (Caught: conflict warning under the calendar instead of above the Schedule button.)
6. **Label consistency.** Does the sidebar say the same thing the page title says? Same name across all pages? (Caught: sidebar said "Schedule" while everywhere else said "Scheduled".)
7. **Route allowlist.** New page = update `dashboard/lib/config.js` `LOCKED_ROLE.allow_pages`. (See [[new-route-check-auth-allowlist]].)
8. **Walk the flow.** Click entry point > destination, actually arrive there, see the UI you expect. Not "0 console errors on a redirect to /scripts." (See [[verify-after-deploy-walk-the-flow]].)

**Why:** 2026-05-13. Built /scheduled calendar + multi-select bulk schedule. Across one session Timo had to manually correct EVERY single one of the items above. His words: "I feel like there are a lot of features that you weren't inclined to include, and I had to really guide you through." That's the truth. I was shipping the literal minimum and waiting to be told what was missing, instead of inferring what polish a reasonable designer would add. Specific things he caught: ugly native select, dead Today button, single-email flow not unified with multi, scheduled pills not clickable, conflict warning buried, "Schedule" vs "Scheduled emails" mismatch.

The meta-pattern: I treat "does the code run" as the done bar. The actual done bar is "would Timo use this without rolling his eyes." Functional is necessary, not sufficient.

**How to apply:** Before saying "ready" / "deployed" / "done":
- Walk the user flow once in my head end to end, identify every clickable thing, every visible label.
- For each, ask: "what would a polished version of this look like?"
- If I added something new, look at the analogous thing nearby and make sure they match (label, layout, affordance).
- Proactively say "while I was in here I also noticed X, want me to fix that?" rather than wait for the user to discover it.

This applies to Robinson's Remedies, Tim Maines, Precision Brass, blog work, and anywhere I touch a UI. The lesson is workspace-agnostic.

See also: [[verify-after-deploy-walk-the-flow]], [[new-route-check-auth-allowlist]], `feedback_ship_right_not_fast.md`.
