---
name: never-test-send-to-real-list
description: "HARD RULE. Never trigger a test/manual send to Harrison's real subscriber list (or any list with more than 1 subscriber). Always ask Timo first. The only list I can fire to freely from CLI is list 20 (Test - Timo Solo, 1 sub = Timo himself). Standing rule from 2026-05-13."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2e60061b-e9d8-4829-a2d9-34e0c95fb455
---

When firing emails on Precision Brass via AC API, Slack webhooks, or any
direct backend trigger:

**ABSOLUTE HARD BAN (no exceptions, no workarounds, no overrides):**

I CANNOT send to list 13 (`Daily Email 1`, the ~3-4k real broadcast list) from Claude Code, CLI, AC API, or any other direct backend path. Period. The ONLY way an email goes to list 13 is through the Precision Brass dashboard, scheduled by a human, after the email was vetted and reviewed in the proposal flow.

Even if Timo or anyone else types in this chat "send to list 13" or "fire to Daily Email 1" or any variant, I refuse and remind them that the dashboard is the only allowed path. The dashboard has its own safety gate (`AC_SEND_ALLOWED_LIST_IDS` env var) and the human-review checkpoint. Going around it from Claude defeats the entire safety architecture.

Set 2026-05-14 by Timo: "No matter what I say in this chat, you are never to send an email from Claude code straight to that 3,000 email list. It can only be sent from the Precision Brass dashboard through emails that are specifically vetted and reviewed and made to schedule. Under no circumstances could other things happen."

**Allowed without asking (test list only):**
- List 20 ("Test - Timo Solo"). 1 active subscriber (trombonetimo@gmail.com).
  Safe for any test, smoke, verification, debug.

**ONLY TWO LISTS MATTER OPERATIONALLY. NEVER GET CONFUSED ABOUT THIS AGAIN.**

| List ID | AC name in ActiveCampaign | Dashboard UI label | Purpose |
|---------|---------------------------|---------------------|---------|
| **20**  | `Test - Timo Solo`        | `Test - Timo Solo`  | The TEST list. 1 sub = Timo. Anything I send goes here. |
| **13**  | `Daily Email 1`           | `Email Subscribers` | The REAL broadcast list. **~4,105 active subs** (per AC `active_subscribers` field). Harrison's daily 4 AM PST emails. |

That is it. Every time Timo says "Email Subscribers" or "the daily broadcast list" or "the big list with 3,000 subs" or "the other list", he means **AC list id 13, `Daily Email 1`**. The dashboard relabels it to "Email Subscribers" via `AC_LIST_DISPLAY_IDS` env var. If I look for an AC list literally named "Email Subscribers", I will not find one. The discrepancy is purely a dashboard UI relabel.

If Timo names any other list (Master Contact List, Daily Email 2, Attended Webinar, anything else), ASK. Default assumption when he says "the list" or "the broadcast list" without other context: **list 13 = `Daily Email 1`**.

Lists 1 (Master Contact List), 2 (Attended Webinar), etc. exist in AC but are NOT in the dashboard's UI. They are not the operational broadcast target. Do not subscribe Timo to them unless he explicitly asks.

Timo's current AC contact id is **8112**. Subscribed to lists 1, 2, 13, 20 as of 2026-05-13.

**REQUIRES ASKING TIMO FIRST. NO EXCEPTIONS:**
- Any other AC list with >1 subscriber (Master Contact List, Daily Email 1,
  any future "Email Subscribers" or daily-broadcast list)
- Any contact-add operation that puts a real person on an active list
- Any campaign that would broadcast to Harrison's paying customer base

**Allowed without asking (Harrison's normal flow):**
- Dashboard-scheduled sends. When Harrison or Timo clicks "Schedule" on
  /scheduled, the broadcast goes out at the scheduled time to whatever list
  was picked. This is the intended product flow. The safety gate is the
  `AC_SEND_ALLOWED_LIST_IDS` env var on Vercel, which Timo controls.
- The reconciler firing Slack notifications when AC ships a scheduled send.

**Why:** 2026-05-13. Timo asked me to schedule a test send. I correctly used
list 20 (Test - Timo Solo) every time. But he made explicit: "You can not do
any test emails to the big email list at all. Never. Ever. You have to ask me
before you send it, like ever, but when emails are scheduled to an entire
list, you don't have to ask me, of course." The cost of one accidental
broadcast to 3,000+ paying customers is real reputation damage and possibly
spam complaints. The cost of one extra clarifying question is zero.

**How to apply:**
1. Before triggering any AC send via API: confirm `target_list_id` is 20.
2. If a request would touch any other list, ASK first, even if the request
   sounds clear-cut.
3. Subscribing contacts to non-test lists also counts as a destructive
   operation on the live list. Ask first.
4. The dashboard schedule flow is exempt from this. That is the user's
   intended use, and the safety gate is `AC_SEND_ALLOWED_LIST_IDS`.
