---
name: Vercel kills fire-and-forget promises after function returns
description: Vercel serverless functions terminate the runtime as soon as the response is sent. Any unawaited fetch().catch() is aborted mid-flight. Always await side-effect writes to external systems (Supabase, Discord, etc.) before returning.
type: feedback
---

Pattern that LOOKS correct but silently fails on Vercel:

```js
async function handler(req, res) {
  const data = await doExpensiveThing();
  // Fire-and-forget side effect:
  fetch(supabaseUrl, { ... }).catch(() => {});  // BROKEN
  return res.json(data);
}
```

Vercel lambdas shut down immediately after the response is flushed. The .catch() doesn't preserve the promise; the underlying TCP socket is closed mid-handshake. The Supabase write never happens.

**Symptom:** persistent caches that should be growing stay empty. Background-write code looks fine in code review. Logs show 200 OK on the function side. The destination DB has zero new rows. Cold restarts always rebuild from scratch.

**Fix:** await the side-effect write before returning. Adds 50-200ms to the function response but ensures the write actually lands.

```js
async function handler(req, res) {
  const data = await doExpensiveThing();
  try {
    await fetch(supabaseUrl, { ... });  // AWAITED
  } catch (_) { /* best-effort, but at least we tried */ }
  return res.json(data);
}
```

If you genuinely need fire-and-forget on Vercel, use `context.waitUntil(promise)` (Edge runtime) or the `@vercel/functions` `waitUntil` helper. Don't trust naked `fetch().catch()`.

**Caught 2026-05-07** when the Precision Brass dashboard kept showing loading spinners despite a "fully populated" Tier 2 Supabase cache. Direct queries showed Tier 2 had ZERO hyros: rows. The Tier 2 write had been fire-and-forget for months. Every cold lambda was a fresh HYROS fetch.
