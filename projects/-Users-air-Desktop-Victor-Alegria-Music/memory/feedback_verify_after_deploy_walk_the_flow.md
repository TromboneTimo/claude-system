---
name: verify-after-deploy-walk-the-flow
description: "After deploying any user-facing flow change, walk the actual click path before saying \"ready to test\". 200 + 0 console errors is not proof the flow works. If I can't walk it (auth-gated), say so explicitly and ASK Timo to test before declaring done."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2e60061b-e9d8-4829-a2d9-34e0c95fb455
---

After deploying any user-facing change (new page, new button, new redirect, new form), before saying "ready" or "live":

1. Walk the actual click path from the entry point to the destination.
2. If Playwright lands on a different URL than the one I navigated to, that's a FAILURE signal, not a pass. Read the `Page URL:` field in the Playwright result. If it changed, ask why before moving on.
3. If the flow is auth-gated and I can't walk it, say so EXPLICITLY ("I cannot verify the authed view; Timo needs to test before I call this done") and STOP. Do not flip to him with "ready to drive" hoping it works.

**Why:** 2026-05-13. Built a new /scheduled page + multi-select on /emails. Verified by curl (200), Playwright unauthed (got redirected to /scripts), and `0 console errors`. Declared "live, ready for you to drive." Timo clicked Schedule N selected, got bounced to /scripts immediately because of an auth allowlist miss. The Playwright output had literally said `Page URL: https://...vercel.app/scripts` when I navigated to /scheduled. I had the ground truth in front of me and read past it because I wanted the deploy to be done. His exact words: "Can you please test it and make sure it's actually working? Fuck you." Fair.

The pattern is the same shape as `feedback_classifier_verification_must_use_ground_truth.md`: verifying internal consistency (curl returns 200, JS parses, no errors thrown) instead of ground truth (does the actual user flow reach the destination?). Two implementations of the same wrong rule will agree. The only test that matters is "did the user end up where they were supposed to?"

**How to apply:**

- Before saying "live" / "ready" / "deployed": list the entry point, list the destination URL, confirm the destination loaded the right page (not a redirect).
- If Playwright redirects to a different page than I asked for, DO NOT shrug it off as "auth gate working." Investigate why. Specifically: when navigating to a NEW route I just created, a redirect to /scripts means the route isn't in the allowlist. See [[new-route-check-auth-allowlist]].
- "0 console errors on a redirected page" proves nothing. The page I was supposed to test wasn't loaded.
- "I can't verify because of auth" is a valid reason to NOT declare done. It is NOT a reason to declare done anyway and hope.

This is also a recurrence of `feedback_ship_right_not_fast.md` and `feedback_verify_with_eyes_not_curl.md`. The lesson keeps being the same and I keep being the one to learn it the hard way. Save the lesson, apply it, stop shipping unverified flows to Timo.
