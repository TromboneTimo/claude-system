---
name: Always skip duplicates silently when pushing to dashboard
description: When pb-ideas-push finds a dup, skip it silently and continue with the rest. Do not ask Timo per dup. Standing rule.
type: feedback
originSessionId: 96d24bc4-360e-4d3e-b566-fcab2c713a01
---
When `pb-ideas-push` (or any push-to-dashboard skill) detects a duplicate idea by id collision or title similarity, **silently skip it and proceed with the non-duplicates**. Do not ask Timo "skip / replace / push as v2." That question wastes his time.

Standing rule from 2026-04-26: "skip, always skip the duplicates always dont ask me remember that."

**How to apply:**
- In the preflight summary, note: "Skipping N duplicate(s): [titles]"
- Push the rest without further confirmation
- Do not pause for per-dup decisions

**Override condition:** only ask about dups if Timo has explicitly said earlier in the same session "ask me about dups this time."

**Why:** every Timo-paste of proposals from chat will collide with prior pushes if titles repeat across sessions. Silent skip is the right default. Replacement and v2 versions are rare edge cases that Timo can call out when he wants them.
