---
name: dashboard-dev
description: Consolidated reference for building auth-gated dashboards on Vercel + Supabase. Covers the verification protocol (Playwright + curl), Vercel cache traps, multi-tier cache architecture, client-side IndexedDB pattern, and the bug-class checklist (canvas destroy, fire-and-forget upserts, race conditions, CSP, URL routing, classifier verification). Use BEFORE editing files under any project's dashboard/, api/, or vercel.json. Triggers on phrases "dashboard work", "fix the dashboard", "deploy the dashboard", "/dashboard-dev", or any edit to dashboard/api files. Replaces the scattered feedback_*.md memory files with one canonical reference.
---

# /dashboard-dev. Consolidated dashboard development reference

This skill consolidates 8+ painful lessons from real production debugging. Read the relevant section BEFORE making the edit, not after.

## Client dashboard blueprint (CROSS-WORKSPACE)

When building a dashboard for ANY client (especially one running ActiveCampaign), read `~/.claude/knowledge/client-dashboard-blueprint.md` FIRST. It encodes:

- The 3-question intake protocol (ONE focus, what data, what's out of scope)
- Hero card + sortable table + scheduled-vs-sent visual rules
- Real-subject-from-message-endpoint pattern
- All-time default + asterisk-when-uncertain
- AC-specific data model (subject lives on `/messages/{message_id}`, NOT campaign)
- HYROS cross-channel attribution caps
- Cache-layer debugging order (5 tiers stacked)

If the client doesn't use AC, the blueprint maps the equivalent endpoints for ConvertKit / Mailchimp / Klaviyo. Built 2026-05-15 from the Precision Brass dashboard build (4 rounds of UI iteration before this got encoded).

---

## UI Polish Gate (MANDATORY before declaring "ready" / "live" / "done")

Before saying done on any UI feature, walk all 8 checks in `~/.claude/knowledge/ui-polish-checklist.md`:
orphan UI removed; new flow consistent with adjacent flows; every interactive element looks clickable;
user can click to diagnose; warnings prominent AT the point of action; labels match across pages;
new route added to auth allowlist if applicable; data text uses full-contrast color + 12px+ size
(never muted grey for numbers/names/dates/IDs; 4+ facts = colored chips, not separator blob).
Proactively offer adjacent fixes you notice in passing.

Function = code runs. Done = user wouldn't roll their eyes. The dashboard-deploy-gate hook prints
the checklist at deploy time so it cannot be skipped silently.

---

## Verification protocol (MANDATORY before declaring "fixed")

> Backed by `canon_deploy_verification.md` plus cached research [2026-05-07_multi-tier-cache-testing-methodology] (X-Cache header verification is industry-standard, not optional).

For ANY user-facing dashboard fix:

1. Edit + commit + push + `vercel deploy --prod --yes --no-clipboard`
2. Wait for "Aliased: <url>" line
3. `mcp__playwright__browser_navigate` to the affected page on the deployed URL
4. `mcp__playwright__browser_console_messages level=error` to confirm zero errors (or only known-extension noise)
5. `mcp__playwright__browser_snapshot` or `browser_take_screenshot`, then READ the result image with the Read tool
6. ONLY THEN say "fixed", and QUOTE the specific evidence in the response

If Playwright is unavailable: drive Safari via `osascript`, `screencapture` the window, `Read` the PNG.

**Failure modes that look like success but aren't:**
- Curl returns 200. (The function ran. Doesn't mean the user sees data.)
- Vercel logs show 200. (Same.)
- The diff looks correct. (Doesn't mean it deploys correctly.)
- The local file has the change. (Doesn't mean Vercel served it.)

**When the user sends a screenshot:** the screenshot IS the answer. Read it. Recognize Vercel error pages, browser dev tools, error toasts, etc. on sight. Do not ask "what does it say."

**When the user says "still seeing X":** before patching anything, distinguish LIVE vs STALE. Console errors don't auto-clear in Chrome devtools. A "still seeing" complaint may mean the display isn't refreshing, not that the underlying issue is unfixed. Verify with a fresh-browser load (Playwright with no extensions) BEFORE assuming the bug isn't fixed.

---

## Root-cause-before-second-patch rule

> Backed by `canon_working_process.md`.

If the FIRST fix doesn't resolve the bug, STOP patching. Trace the entire data flow end-to-end before patch #2.

```
Origin (upstream API) -> Server function -> Server cache -> Transport (headers/CSP) ->
   -> Client receive -> Client storage -> Client render
```

Stop at the first link that doesn't match expectations. THAT is the bug. The real cause is almost always 1-2 layers DEEPER than where the symptom appears.

**The fire-and-forget bug took 6 deploys** because each one patched a symptom (canvas destroy, eviction logic, IDB swap, classifier, prefetch list). One curl on the Supabase api_cache table on hour 1 would have shown 0 hyros rows and pointed at the writeback. Always go one layer deeper before patching.

---

## Vercel cache traps (the killer ones)

> Backed by cached research [2026-05-06_vercel-serverless-function-caching-for-slow-third-party-api-_82908fc1.md], confirmed against Vercel docs.

### Trap 1: Authorization header disables edge cache

**`Authorization: Bearer <token>` makes Vercel edge cache silently skip caching, ignoring all `Cache-Control` headers.**

If your dashboard sends a JWT for auth-gating, you have two choices:
- Move auth out of Authorization header (cookie-based, query param). UX/security trade-off.
- Cache server-side INSIDE the function (in-memory Map OR Vercel Runtime Cache OR Supabase). Keeps auth gating, doesn't rely on edge.

### Trap 2: Fire-and-forget side effects get killed

**Vercel terminates the lambda the moment the function returns.** Any unawaited `fetch(...).catch(() => {})` is aborted mid-handshake. The Supabase write never lands.

```js
// BROKEN (2026-05-06 spinner bug, 6 deploys to find)
async function handler(req, res) {
  const data = await doExpensiveThing();
  fetch(supabaseUrl, { ... }).catch(() => {});  // KILLED on return
  return res.json(data);
}

// CORRECT
async function handler(req, res) {
  const data = await doExpensiveThing();
  try { await fetch(supabaseUrl, { ... }); } catch (_) {}
  return res.json(data);
}
```

If you genuinely need fire-and-forget on Vercel, use `context.waitUntil(promise)` (Edge runtime) or `@vercel/functions` `waitUntil`. Don't trust naked `fetch().catch()`.

### Trap 3: Deployment Protection blocks /api/* on preview URLs

`https://*-trombonetimo-9261s-projects.vercel.app/api/*` returns "Authentication Required" (HTML) instead of JSON. Always test against the production alias `https://<project>.vercel.app`, not raw deployment URLs.

### Trap 4: cleanUrls + outputDirectory rewrite the URL space

`vercel.json` `outputDirectory: "dashboard"` plus `cleanUrls: true` means local file `dashboard/channel-attribution.html` deploys as `/channel-attribution` (no `dashboard/` prefix, no `.html`). **Always read `vercel.json` before typing a URL from memory.**

---

## Multi-tier cache architecture (the standard pattern)

> Backed by cached research [2026-05-07_multi-tier-cache-testing-methodology + NotebookLM synthesis].

```
Tier 1: In-process Map (Fluid Compute shared)  -> X-Cache: HIT-T1     (<10ms)
Tier 2: Supabase persistent (TTL-aware)         -> X-Cache: HIT-T2     (~100ms)
Tier 3: Upstream API (rate-limited)             -> X-Cache: MISS       (15-30s)
```

### Reference implementation

```js
const _cache = new Map();
const _inflight = new Map();  // de-dupe concurrent identical requests

async function getOrFetch(key, fetcher, opts) {
  const force = !!(opts && opts.force);
  const now = Date.now();

  if (!force) {
    const t1 = _cache.get(key);
    if (t1) return { data: t1.data, source: 'memory', age_ms: now - t1.created };

    const sb = await fetch(`${SUPABASE_URL}/rest/v1/api_cache?cache_key=eq.${encodeURIComponent(key)}&select=payload,created_at`, {
      headers: { 'apikey': serviceKey, 'Authorization': `Bearer ${serviceKey}` }
    });
    if (sb.ok) {
      const rows = await sb.json();
      if (rows && rows.length > 0) {
        const cachedAt = new Date(rows[0].created_at).getTime();
        _cache.set(key, { data: rows[0].payload, created: cachedAt });
        return { data: rows[0].payload, source: 'supabase', age_ms: now - cachedAt };
      }
    }
  }

  if (!_inflight.has(key)) {
    const p = fetcher().then(async d => {
      const fetchedAt = Date.now();
      _cache.set(key, { data: d, created: fetchedAt });
      // CRITICAL: AWAIT the upsert. Fire-and-forget gets killed.
      try {
        await fetch(`${SUPABASE_URL}/rest/v1/api_cache`, {
          method: 'POST',
          headers: { 'apikey': serviceKey, 'Authorization': `Bearer ${serviceKey}`, 'Content-Type': 'application/json', 'Prefer': 'resolution=merge-duplicates' },
          body: JSON.stringify({ cache_key: key, payload: d, created_at: new Date(fetchedAt).toISOString() })
        });
      } catch (_) {}
      _inflight.delete(key);
      return d;
    }).catch(e => { _inflight.delete(key); throw e; });
    _inflight.set(key, p);
  }
  const data = await _inflight.get(key);
  return { data, source: 'cold', age_ms: 0 };
}
```

### Required Supabase table

```sql
create table if not exists api_cache (
  cache_key text primary key,
  payload jsonb not null,
  created_at timestamptz default now()
);
```

`cache_key` MUST be a primary key for `Prefer: resolution=merge-duplicates` upserts to work.

### Verification tests for the cache (run after every cache change)

```bash
# 1. Cold start: confirm Tier 3 is hit
curl -w "%{time_total}\n" $URL/api/endpoint?key=test1
# Expect 15-30s (HYROS upstream)

# 2. T2 persistence: simulate lambda death by waiting + confirm Supabase served
sleep 60
curl -w "%{time_total}\n" -o /dev/null $URL/api/endpoint?key=test1
# Expect ~500ms (Supabase round-trip)

# 3. Concurrency dedup: 50 parallel cold-cache requests = 1 upstream call
ROWS_BEFORE=$(curl -s "$SUPABASE_URL/rest/v1/upstream_logs?select=count" | jq '.[0].count')
for i in {1..50}; do curl -s "$URL/api/endpoint?key=newkey" > /dev/null & done
wait
ROWS_AFTER=$(curl -s "$SUPABASE_URL/rest/v1/upstream_logs?select=count" | jq '.[0].count')
echo "Upstream calls: $((ROWS_AFTER - ROWS_BEFORE))"  # MUST be 1

# 4. Direct Supabase verification: confirm rows actually persist
curl -s "$SUPABASE_URL/rest/v1/api_cache?select=cache_key" | python3 -c "import json,sys; print(len(json.load(sys.stdin)))"
```

If test 4 returns 0 rows after the Vercel function "wrote" them, you have the fire-and-forget bug.

---

## Client-side cache: use IndexedDB for >5 entries or >50KB

> Backed by `canon_dashboard_engineering.md`.

localStorage is the wrong store for caching multiple large objects. Safari's per-origin quota plus aggressive eviction means most writes silently fail. Eviction-on-quota loops cannot recover because each new write triggers another quota error.

**Symptom:** spinner every page load even though the cache "should be filled". Inspect localStorage and find only the smallest entries survived.

**Fix:** IndexedDB. 50MB+ quota. Per-key writes. Hot in-memory mirror for sync reads.

```js
const DB_NAME = 'pb_xxx_v1';
const STORE = 'cache';
let _hot = {};
let _ready = false;
let _readyResolve;
const _readyPromise = new Promise(r => { _readyResolve = r; });

function _open() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_NAME, 1);
    req.onupgradeneeded = () => req.result.createObjectStore(STORE);
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

async function _hydrate() {
  try {
    const db = await _open();
    const req = db.transaction(STORE, 'readonly').objectStore(STORE).openCursor();
    return new Promise(resolve => {
      req.onsuccess = (e) => {
        const c = e.target.result;
        if (c) { _hot[c.key] = c.value; c.continue(); }
        else { _ready = true; _readyResolve(); resolve(); }
      };
      req.onerror = () => { _ready = true; _readyResolve(); resolve(); };
    });
  } catch (_) {
    _ready = true; _readyResolve();
  }
}
_hydrate();

function read(key) { return _hot[key] || null; }
async function write(key, value) {
  _hot[key] = value;
  try {
    const db = await _open();
    await new Promise((resolve, reject) => {
      const tx = db.transaction(STORE, 'readwrite');
      tx.objectStore(STORE).put(value, key);
      tx.oncomplete = resolve;
      tx.onerror = () => reject(tx.error);
    });
  } catch (_) {}
}

async function loadAll() {
  if (!_ready) await _readyPromise;  // 10-30ms first call, instant after
  const cached = read(key);
  if (cached) return render(cached);
  // cold path
}
```

---

## Common bug-class checklist (audit BEFORE writing render code)

> Each backed by a memory file. Run through this list when touching dashboard/render code.

| Class | Symptom | Audit | Fix pattern |
|---|---|---|---|
| Canvas destroy | Empty state shows on tab A, then tab B's chart never renders | grep `parentElement.innerHTML` near `canvas` | Use show/hide overlay div pattern. Never overwrite parentElement of a canvas. |
| Fire-and-forget upsert | Cache "should be there" but Supabase has 0 rows | `curl $SUPABASE_URL/rest/v1/api_cache?cache_key=like.X*` | `await` the upsert, never `.catch(() => {})` |
| Race on rapid clicks | Wrong-tab data renders, cache slot poisoned | Look for `await` after capturing `activeFoo` global | Snapshot vars + token gate. Discard responses where token doesn't match |
| iframe-srcdoc missing CSS | Modal renders unstyled HTML | Look for body innerHTML extraction sent to srcdoc | Send the FULL HTML doc (head + style + body), not just body innerHTML |
| URL routing 404 | `open` lands on Vercel 404 page | Read vercel.json before typing URL | cleanUrls strips .html, outputDirectory remaps prefix |
| CSP font/connect violations | Console floods with "violates Content-Security-Policy" | Check vercel.json CSP header against what page loads | Add cdn.jsdelivr.net to connect-src for sourcemaps. Use `font-src 'self' data: https:` for permissive font loading. |
| Classifier silently wrong | Tab shows zero but data exists | Sample raw rows + ask user "does this label match reality" | Direct upstream curl + verify per-bucket assignments against ground truth |
| Stale console errors | User sees "still 228 errors" after fix deployed | Open page in fresh Playwright (no extensions, no cache) | Clear console + hard-refresh. Errors don't auto-clear when fix deploys. |
| Empty state for Chart.js | "No data drove clicks" persists across tab switches | grep `section-empty` in canvas render functions | setEmptyOverlay/clearEmptyOverlay helpers (canvas-preserving) |

---

## Pre-flight checklist before saying "fixed"

```
[ ] Edited the right file (not just the local copy of a stale repo)
[ ] Committed + pushed
[ ] vercel deploy --prod --yes (or auto-deploy waited for)
[ ] Aliased URL line confirmed in deploy output
[ ] Loaded the deployed URL in Playwright (or osascript Safari)
[ ] Read mcp__playwright__browser_console_messages level=error to confirm 0 errors (or extension-only)
[ ] Read screenshot/snapshot myself
[ ] If cache-related: curl Supabase api_cache directly and confirmed rows persist
[ ] If user reports "still broken": fresh Playwright load to distinguish stale vs live
[ ] Quote specific evidence in the "fixed" message
```

If any box is unchecked, you have not fixed it. You have shipped a hopeful patch.

---

## Reference files (memory cross-references)

Auto-loaded on session boot via MEMORY.md. Listed here so this skill is the canonical entry point:

- `canon_deploy_verification.md`. Verify by loading the actual page, not by curl
- `canon_working_process.md`. Trace full flow before patch #2
- `canon_dashboard_engineering.md`. Await side-effect writes
- `canon_dashboard_engineering.md`. Never innerHTML a canvas parent
- `canon_dashboard_engineering.md`. IndexedDB for >5 entries or >50KB
- `canon_dashboard_engineering.md`. Full HTML doc to iframe srcdoc
- `canon_deploy_verification.md`. Read vercel.json before opening
- `canon_attribution_analytics.md`. Verify classifiers against real samples
- `canon_dashboard_engineering.md`. Runtime diagnostic on move 2

## Cached research (auto-loaded)

- `~/.claude/research/perplexity/raw/2026-05-06_vercel-serverless-function-caching*`. Auth-header trap + cache options
- `~/.claude/research/perplexity/raw/2026-05-07_multi-tier-cache-testing-methodology*`. Test matrix + X-Cache headers
- `~/.claude/research/notebooklm/raw/2026-05-07_pb-cache-testing-synthesis.md`. NotebookLM synthesis
- `~/.claude/research/perplexity/raw/2026-04-09_best-practices-for-building-a-small-business-marketing-dashb*`. Architecture
- `~/.claude/research/perplexity/raw/2026-04-14_claude-code-skill-files-skill-md-best-practices-2026*`. Consolidation pattern (validates this skill's existence)

## When NOT to use this skill

- Pure backend work that doesn't touch a deployed UI surface
- Local-only scripts that never deploy
- Doc/text edits that don't run code
