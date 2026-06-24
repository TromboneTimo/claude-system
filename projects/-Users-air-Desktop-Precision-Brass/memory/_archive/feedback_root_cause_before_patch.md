---
name: Trace the whole flow end-to-end before the second patch
description: When a bug survives one fix attempt, STOP patching and trace the full data flow before the next change. Symptom-patches stack and obscure the real root cause for hours.
type: feedback
originSessionId: 377101fb-e5ce-4244-8b3a-adf8f5f91240
---
Pattern: bug reported → I see one plausible cause → patch → ship → bug still happens → I see another plausible cause → patch → ship → repeat. After 4-6 patches I find the actual root cause and could have found it on patch 2 if I'd traced the whole flow first.

**Rule: if the FIRST fix doesn't resolve the bug, stop. Trace the entire system end-to-end before the second patch.** Every component the data passes through, in order. Not just the part I think is broken.

Concrete trace for any "data not showing up correctly" bug:
1. **Origin (the source of truth):** what does the upstream API actually return? Curl it.
2. **Server processing:** what does my function do with the response? Add logging or read the function code.
3. **Persistence:** if there's a cache layer, query it directly. Is it actually being written? When you fetch later, do the writes land?
4. **Transport:** are the response headers/CSP/cache-control what I expect? curl -I.
5. **Client receive:** what does the browser get? Use Playwright network log.
6. **Client storage:** is the client cache actually persisting across reloads? Inspect IndexedDB / localStorage.
7. **Client render:** does the rendered DOM match the data?

Stop at the first link that doesn't match expectations. THAT is the bug.

**Specific case 2026-05-07 (the spinner bug):** Real cause was Vercel killing fire-and-forget Supabase upserts. I shipped 6 patches treating symptoms (race conditions, canvas destruction, eviction logic, IDB swap) before I curled the api_cache table directly and saw it had 0 hyros rows. That single curl on hour 1 would have saved hours 2-6.

**Specific case 2026-05-06 (platform tabs empty):** Real cause was the platform classifier trusting generic trafficSource values over keyword matching. I patched the empty-state UI and the cache layer first. Should have curled HYROS directly to see what source.name values actually look like.

**Heuristic:** the real root cause is almost always one or two layers DEEPER than where the symptom appears. UI bug? Probably the data is wrong. Data wrong? Probably the cache is stale. Cache stale? Probably the writeback never happened. Always go one layer deeper before patching.
