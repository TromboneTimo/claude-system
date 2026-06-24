---
name: interrupts-preempt-big-writes
description: When user sends a quick ask mid-task (logo swap, rename, path fix), pause the in-flight big work and handle the interrupt first. Never queue fast asks behind slow writes.
type: feedback
originSessionId: 6bffca3c-789c-4c2a-9d3b-f957e123208e
---
If the user sends a new request while you are mid-generation on a big tool call (long Write, large Edit), and the new ask is quick (<20s work), pause and do the quick ask first. Do not queue it behind the big work.

**Why:** Was mid-generation on a ~700-line HTML file when Timo said "also replace the samurai brass logo." I mentally queued it to run after the big Write finished. That meant the logo swap sat behind another 60+s of silent work, plus a Write failure and retry. The right move was to abandon or pause the Write, do the 2-second logo swap, then resume. Big writes are rarely atomic anyway, since they can fail on read-before-write and need to be restarted.

**How to apply:**
- New ask arrives mid-tool-call. If the new ask is small (single file rename, single variable change, path swap, image replace), do it FIRST.
- Only continue the original big task if the new ask is genuinely "add this at the end" / "also add X" in the same file.
- If the two tasks conflict (new ask changes something the big Write is also changing), abandon the in-flight Write entirely and restart with both requirements merged.
