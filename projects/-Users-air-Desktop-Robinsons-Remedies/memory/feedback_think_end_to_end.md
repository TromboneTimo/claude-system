---
name: Think end-to-end before declaring something done
description: Always verify the FULL chain works before telling the user it's done. Don't just build one piece and assume the rest connects.
type: feedback
---

Before telling Timo something is "done" or "set up," mentally walk through the ENTIRE chain from input to output and verify every link works.

**Why:** Multiple times Claude built systems that looked complete but had critical broken links: scheduled agents that couldn't reach local files, ADHD guardrails that were instructions but not automated, SESSION_LOG hooks that spammed instead of logging, research pipelines that skipped steps. Timo catches these gaps and it erodes trust.

**How to apply:**
1. After building anything, ask: "If Timo walks away right now, does this actually work without him?" If no, it's not done.
2. For automation: trace the full path. Trigger fires -> data flows -> action happens -> result is visible. If any link is broken, fix it BEFORE declaring done.
3. For scheduled/remote agents: verify they can ACCESS the files they need to read/write. Local files != remote access.
4. For hooks: test that they actually fire in the right context, not just that the script exists.
5. Don't present the ideal state as the current state. If there's a caveat, lead with it. "This is set up BUT the scheduled agent can't reach local files yet. Here's how to fix that."
6. Default to the MOST RELIABLE implementation, not the fastest. If there are two ways to do something and one has a caveat, pick the one that just works.
