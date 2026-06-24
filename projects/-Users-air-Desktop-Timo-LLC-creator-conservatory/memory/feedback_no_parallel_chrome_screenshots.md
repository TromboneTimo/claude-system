---
name: Never Fire 18 Parallel Chrome Headless Instances
description: Visual QA via Chrome headless must run sequentially or in batches of 3-4 max. Spawning a parallel process per slide hangs the bash tool.
type: feedback
originSessionId: f48c716d-c5d0-4b99-bba5-c74c4f22aed9
---
When doing visual QA on a multi-slide deck via Chrome headless screenshots, NEVER spawn one chrome instance per slide in parallel using `&`. Chrome headless on macOS leaks zombie processes, eats RAM, and the bash tool's parent shell hangs waiting on `wait`.

**Why:** 2026-04-13 leaking-business deck — I tried to screenshot all 18 slides at once with `for n in 1..18; do chrome --headless ... & done; wait`. Bash tool stalled out completely. Timo had to interrupt: "you knd of stalled out." That was the second time I burned trust in the same session.

**How to apply:**
- Default: render slides ONE AT A TIME with a single chrome invocation per slide. `for n in 1..18; do chrome --headless ... ; done` (no `&`).
- If parallelization is needed, batch in groups of 3-4 max with `wait` between groups.
- Better: render ONE representative slide per layout type (hook, headline, quote, stat, CTA), not every slide. The CSS is shared, so rendering one validates the type system.
- For URL fragment navigation (`file://path.html#5`), Chrome headless doesn't always honor it — verify the screenshot is actually slide N before trusting it. The deck's JS uses keyboard events to navigate, so fragments may not trigger slide changes.
- If visual QA needs to be exhaustive, write a shell loop that opens one slide, screenshots, kills chrome, then iterates. NOT parallel spawn.
