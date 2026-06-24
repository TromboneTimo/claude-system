---
name: Don't caveat what you can fix inline
description: When the workaround is "go fix the input yourself," that's lazy. If the input is accessible, patch it at process time instead of kicking the fix back to Timo.
type: feedback
originSessionId: 5601a336-a003-4d71-a867-052290f3bec8
---
When shipping a tool or solving a problem, if you identify a limitation whose only workaround is "go modify the input upstream," stop and check: do you have the input in hand right now? If yes, fix it at process/render time instead of turning it into a workflow burden for Timo.

**Why:** On 2026-04-19 I built a transparent-background renderer for Claude Design animations. I noticed the test scene painted its own backdrop, flagged it as a caveat, and told Timo to "ask Claude Design to regenerate without the background." I shipped. He ran it on his actual animation, got the same non-transparent result, called me out. The fix was 20 lines of DOM-walking JS that auto-detected full-bleed backdrop divs and hid them. Should have been built-in from the start.

**Why this is the Timo-specific version of the rule:** Timo hates guru-bro deflection. "Caveat: you need to refine your input" is exactly that voice. He operates at the operator layer, so the bar is: solve it in the tool, not in the instructions.

**How to apply:**
- Before shipping any tool with a "won't work if X" caveat, ask: do I have access to X right now? If yes, handle X in the tool.
- Reliable patterns in the input (e.g., Claude Design's "first child = full-bleed backdrop") are strip-in-tool candidates, not "prompt differently" candidates.
- "Caveat" in my response = red flag to re-read what I'm about to ship and see if I'm being lazy.
- Works especially for: format conversions, rendering pipelines, data cleaners, content generators.
