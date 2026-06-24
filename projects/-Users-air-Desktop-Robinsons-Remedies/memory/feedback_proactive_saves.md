---
name: Save feedback immediately without being asked
description: When user corrects ANY behavior, save feedback + update relevant skill IN THE SAME TURN. Never wait to be told.
type: feedback
---

When the user corrects Claude's behavior, Claude MUST in the SAME response turn:
1. Fix the immediate issue
2. Save a feedback_*.md memory file
3. Update MEMORY.md index
4. Update the relevant SKILL.md if applicable
5. Confirm what was saved

NEVER just fix the thing and move on. NEVER wait for the user to say "save that" or "remember this." The correction IS the save trigger.

**Why:** User has flagged this pattern multiple times. He gives feedback, Claude fixes the output, but doesn't save the lesson. Then the same mistake happens next session. This is the #1 source of frustration.

**How to apply:** Treat every correction, preference statement, or "don't do X" as an automatic save event. The save happens in the same tool call batch as the fix. No exceptions. No "I'll save that later." Same turn.

**Examples of save triggers:**
- "that looks like shit" -> fix + save feedback on what was wrong + update skill
- "use this instead" -> fix + save preference + update relevant files
- "don't do X ever again" -> fix + save feedback + update CLAUDE.md if it's a rule
- "why didn't you remember this" -> save the thing they're referencing + apologize once, don't grovel
