# Mock Data Quarantine

Canonical rule: mock data is for VISUAL DESIGN. The numbers in it are fake-by-construction. Once a mock value escapes the file it was written in and gets quoted to the user as if it were real, the lie is mine.

Loaded from `CLAUDE.md > MOCK DATA GATE`. Referenced from `dashboard-dev` and any skill that builds preview/scaffold HTML. Aligns with the existing `canon_attribution_analytics.md` (same family of bug: trusting your own derivation instead of ground truth).

---

## The rule

**Before typing any specific number that affects the user's decisions, the number must come from a live query result in the CURRENT conversation, not from memory and not from a mock.**

Numbers that fall under this:
- Subscriber counts, recipient counts, send_amt, total contacts
- Send times, schedule times, fire times, response times
- IDs (campaign id, contact id, list id, proposal id)
- Status codes, error codes, counts of any kind
- Money amounts (revenue, ad spend, CPA)
- Any benchmark / threshold / measured value the user is making a decision against

Numbers EXEMPT (still write them, no extra check):
- Constants from the codebase the user can read themselves (e.g., port 8767)
- Times from `date` shell calls inside the same response
- Computed math the user can verify (e.g., "1 + 1 = 2")

---

## How to apply

1. **If I am about to type a specific number**, ask: "did I run a query in THIS turn that returned this number?"
   - If YES → fine. Cite it.
   - If NO → re-query before typing it. Even if I "remember" the number from earlier in the session, re-query.

2. **Mock data in any file I write must be marked obvious-mock**:
   - `<option value="20">Test - Timo Solo . 1 sub</option>` (real)
   - `<option value="6">Email Subscribers . [MOCK] 9999 active subs</option>` (mock; the brackets + 9999 ensure I never quote it later thinking it's real)
   - OR delete the mock value entirely and use `???` so I am physically incapable of citing it.

3. **When user contradicts my number**: assume they are right. Re-query immediately. Do not argue. Do not anchor on my prior claim.

4. **End-of-session memory**: if I wrote any mock data file during the session, delete it before commit, AND if any of the mock values made it into my conversation responses, correct them on the way out.

---

## Why this exists

Origin: 2026-05-13. Built a local `dashboard/broadcast-preview.html` to mock up the new schedule UI. Put `<option value="6">Email Subscribers . 3,142 active subs</option>` in there because I needed dropdown content to demo the layout. Through the rest of the session I cited "3,142" or "~3,142" repeatedly as if it were the real subscriber count of Harrison's broadcast list. Across many turns, including in formal punch-list and rollout summaries.

Timo then noticed the dashboard showed 4,105 (the real `active_subscribers` value AC reports). He asked: "why does the dashboard say 4,100 but you're saying 3,100?" That is when I queried AC for the real count and discovered MY OWN MOCK had been the source of "3,142" the entire time.

The damage potential: if Timo had been planning Harrison's email cadence based on "~3,000 subs", and the real number was 4,100, every per-subscriber calculation he made (open rate, CTR, revenue per send) would have been off by ~25%. Bad enough that this is the kind of mistake that can land a wrong number in a board deck.

His exact words: "What did you learn from that math mistake from using mock data over the actual real data? Is there anything you could do to fix your brain?"

---

## Related rules

- `canon_attribution_analytics.md` (don't verify your code with your own re-implementation)
- `feedback_verify_after_deploy_walk_the_flow.md` (don't verify the deploy with curl alone)
- `feedback_ship_polish_not_skeleton.md` (don't ship skeletons + wait for the user to find the gaps)

All variants of the same root: **prefer ground truth over your own derivation. Always.**
