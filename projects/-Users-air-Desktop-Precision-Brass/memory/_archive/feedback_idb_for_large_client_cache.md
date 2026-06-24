---
name: Use IndexedDB for client caches with multiple large entries
description: localStorage's per-origin quota (~5MB on Safari, less under ITP) silently drops entries when many large objects are written. Use IndexedDB instead for any cache holding >5 entries averaging >50KB.
type: feedback
originSessionId: 377101fb-e5ce-4244-8b3a-adf8f5f91240
---
When the dashboard needs to cache 10+ data blobs (e.g., 30 prefetched HYROS combos), localStorage is the wrong store. Safari's per-origin quota plus aggressive eviction means most writes silently fail. Eviction-on-quota loops cannot recover because each new write triggers another quota error.

**Symptom:** user opens the page, sees a "Loading..." spinner every time, even after the data has been "cached" client-side. Dev inspection shows localStorage has only a few small entries; the big ones (the ones that matter) are gone.

**Root cause:** localStorage QuotaExceededError fires when total serialized size exceeds the quota. The catch block reads cache, evicts, retries, but each retry serializes the entire cache. Large entries (75KB+) keep triggering the same error. Net effect: only the smallest entries survive.

**Fix:** use IndexedDB. Quota is 50MB+ (browser-managed, often 1GB+). Per-key writes don't serialize the whole store. Async API but easy to wrap with a sync-readable hot copy.

**Pattern:**
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
_hydrate();  // start hydration immediately on script load

function read(key) { return _hot[key] || null; }
async function write(key, value) {
  _hot[key] = value;  // sync-readable IMMEDIATELY
  try {
    const db = await _open();
    await new Promise((resolve, reject) => {
      const tx = db.transaction(STORE, 'readwrite');
      tx.objectStore(STORE).put(value, key);
      tx.oncomplete = resolve;
      tx.onerror = () => reject(tx.error);
    });
  } catch (_) { /* swallow; hot copy still has it for this session */ }
}

// In loadAll, AWAIT readiness before checking cache:
async function loadAll() {
  if (!_ready) await _readyPromise;  // ~10-30ms first load, instant after
  const cached = read(key);
  if (cached) return render(cached);
  // cold path
}
```

**Why this fix works:**
- IDB quota is large enough for 30+ entries of any realistic size.
- Per-key writes don't rewrite the whole store, so one bad entry doesn't poison others.
- Hot copy provides sync read, matching the localStorage API surface.
- Hydration finishes before first loadAll awaits, so first cache-hit is still instant after IDB is warm.

**Caught 2026-05-06** when the user kept seeing the loading spinner on every page reload. localStorage cache had only 5 of 30 prefetched combos. Switching to IDB fixed it: all 35 entries persist, every page load is instant from cache, no spinner unless ↻ is pressed.

**When to apply:** any client-side cache holding multiple data blobs >50KB each, or 10+ entries total. Especially if you see "QuotaExceededError" in the console or entries silently disappearing.
