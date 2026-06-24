---
name: narrate-long-generations
description: Always send a heads-up message BEFORE starting any tool call that will take >20s of silent token generation (big Write, long Bash, big Edit). Silence reads as stalling.
type: feedback
originSessionId: 6bffca3c-789c-4c2a-9d3b-f957e123208e
---
Before any tool call that will produce >20 seconds of silent output (large Write files, long-running Bash, big Edit replace-all), send a one-sentence status message first: what you're doing and roughly how long. Never start a 500+ line Write with zero narration.

**Why:** Spent 2+ minutes silently generating a ~700-line HTML file. Timo stared at a blank screen, sent "hello?", "what are you doing", and "what the fuck is taking so long" in that order. The work was progressing but invisible to him. Silence reads as a stall or a hang, regardless of whether it's actually broken.

**How to apply:**
- Before big Write (>300 lines): "Writing the full file now (~700 lines, ~90s)."
- Before long Bash (build, install, long test): say what's running and that it may take a minute.
- Before batched Edits across many files: "Applying X edits across Y files."
- Rule of thumb: if a single tool call will take longer than ~20s, narrate first. If you can break it into smaller visible chunks, prefer that.
