---
query: "Vercel serverless function caching for slow third-party API proxy. Authorization header blocks edge cache. In-memory module-scope Map vs Vercel Runtime Cache vs sessionStorage. SWR pattern. TTL recommendations for auth-gated marketing dashboards."
query_hash: "82908fc13010a7ed"
slug: "vercel-serverless-function-caching-for-slow-third-party-api-"
model: "vercel-docs-webfetch"
date: "2026-05-06"
workspaces:
  - Precision-Brass
category: "Next.js / Supabase / Tech Stack"
tags:
  - vercel
  - caching
  - api
  - performance
  - dashboard
  - hyros
  - swr
  - authorization
keywords:
  - vercel
  - authorization
  - cache
  - caching
  - header
  - cache-control
  - edge
  - map
  - cdn
  - function
  - api
  - auth
  - auth-gated
  - browser
  - cdns
citations_count: 0
synthesized_in_notebooklm: false
stale_after: "2026-11-02"
---

# Vercel serverless function caching for slow third-party API proxy. Authorization header blocks edge cache. In-memory module-scope Map vs Vercel Runtime Cache vs sessionStorage. SWR pattern. TTL recommendations for auth-gated marketing dashboards.

## Key findings

# Vercel serverless function caching for slow third-party API proxy

Source: vercel.com/docs/caching/cdn-cache (last_updated 2026-03-17) and vercel.com/docs/caching/runtime-cache (last_updated 2026-03-05).

## The killer constraint: Authorization header disables edge caching

From vercel.com/docs/caching/cdn-cache, "Cacheable response criteria":

> Request doesn't contain `Authorization` header.

If the request has `Authorization: Bearer <token>`, Vercel Edge Network will NOT cache the response no matter what `Cache-Control`, `CDN-Cache-Control`, or `Vercel-CDN-Cache-Control` you set. The headers are silently ignored. This is the #1 trap for auth-gated dashboards on Vercel.

Implication: a private dashboard that sends a JWT in the Authorization header for auth gating has only two options for caching:
1. Move auth out of the Authorization header (cookie-based, query param, etc.), accepting a security/UX trade-off.
2. Cache server-side INSIDE the function (in-memory module-scope OR Vercel Runtime Cache), keeping auth gating intact.

## Three Cache-Control header layers (when caching is allowed)

- `Cache-Control`: browser plus downstream CDNs plus Vercel CDN.
- `CDN-Cache-Control`: downstream CDNs plus Vercel CDN. NOT browser. Overrides Cache-Control for CDN.
- `Vercel-CDN-Cache-Control`: Vercel CDN only. NOT downstream CDNs, NOT browser. Most targeted.

Function-level Cache-Control headers OVERRIDE vercel.json route-level headers.

## Required directives for Edge caching

Any of:
- `s-maxage=N`
- `s-maxage=N, stale-while-revalidate=Z`
- `s-maxage=N, stale-while-revalidate=Z, stale-if-error=Z` (NOTE: stale-if-error not currently supported on Vercel)

`proxy-revalidate` is not supported.

## Other criteria for Edge cache

- GET or HEAD only.
- No Range header.
- Status 200, 404, 410, 301, 302, 307, or 308.
- Response under 10MB (non-streaming) or under 20MB (streaming).
- No set-cookie header on response.
- No `private`, `no-cache`, or `no-store` in response Cache-Control.
- No `Vary: *` (treated as `private`).

## Server-side cache options inside the function

### Option A: Module-scope in-memory Map

```js
const _cache = new Map(); // top-level

export default async function handler(req, res) {
  const key = `${req.query.days}|${req.query.platform}`;
  const hit = _cache.get(key);
  if (hit && hit.expires > Date.now()) {
    return res.status(200).json(hit.data);
  }
  const fresh = await fetchUpstream();
  _cache.set(key, { data: fresh, expires: Date.now() + 300_000 });
  return res.status(200).json(fresh);
}
```

Trade-offs:
- Free, zero new dependencies.
- Per-instance cache. Multiple Vercel instances do not share. For low-traffic dashboards (1-10 active users) this is fine. For high traffic you'll see cache misses across instances.
- Ephemeral. Cleared on instance shutdown. No control over when shutdown happens.
- Per Vercel docs (Runtime Cache page): "use cache is in-memory by default. This means that it is ephemeral, and disappears when the instance that served the request is shut down."

### Option B: Vercel Runtime Cache via `@vercel/functions` getCache()

```js
import { getCache } from '@vercel/functions';

export default async function handler(req, res) {
  const cache = getCache();
  const key = `hyros:${req.query.days}:${req.query.platform}`;
  const hit = await cache.get(key);
  if (hit) return res.status(200).json(hit);
  const fresh = await fetchUpstream();
  await cache.set(key, fresh, { ttl: 300, tags: ['hyros'] });
  return res.status(200).json(fresh);
}
```

Trade-offs:
- Regional cache shared across Vercel function instances.
- Persistent across deployments.
- LRU eviction at project storage limit.
- 2MB item size cap.
- 64 tags per item, 256 byte tag length.
- REQUIRES "Runtime Cache" permission enabled.
- BILLABLE per use.
- Requires `@vercel/functions` package.

## Stale-while-revalidate pattern in code

For a slow upstream where you want first-user-pays-once and everyone else gets fast loads:

```js
const _cache = new Map();
const _inflight = new Map(); // de-dupe concurrent refreshes

async function getCached(key, fetcher, ttlMs, staleMs) {
  const now = Date.now();
  const entry = _cache.get(key);

  if (entry && entry.expires > now) return entry.data; // fresh

  if (entry && entry.expires + staleMs > now) {
    // Stale but usable. Kick off background refresh, return stale.
    if (!_inflight.has(key)) {
      _inflight.set(key, fetcher().then(d => {
        _cache.set(key, { data: d, expires: Date.now() + ttlMs });
        _inflight.delete(key);
      }).catch(() => _inflight.delete(key)));
    }
    return entry.data;
  }

  // Cold: must wait.
  if (!_inflight.has(key)) {
    _inflight.set(key, fetcher().then(d => {
      _cache.set(key, { data: d, expires: Date.now() + ttlMs });
      _inflight.delete(key);
      return d;
    }));
  }
  return _inflight.get(key);
}
```

## Recommended TTLs for marketing dashboards

For attribution data updated daily upstream where freshness within minutes is acceptable:
- Fresh window: 5 minutes (`ttl: 300`)
- Stale-but-serve window: 30 minutes (still serves while background refresh runs)
- Total max staleness before forced wait: 30 min after last good fetch

## Client-side: sessionStorage for tab/range toggle UX

Once the server-side cache makes a fresh fetch sub-2s, client-side sessionStorage with a 60-300s TTL eliminates ALL re-fetches within a single user session for the same `{days, platform}` combo. Range button clicks become instant.

```js
const CACHE_KEY = 'hyros_cache_v1';
const TTL_MS = 5 * 60 * 1000;

function getClientCache(days, platform) {
  try {
    const all = JSON.parse(sessionStorage.getItem(CACHE_KEY) || '{}');
    const k = `${days}|${platform}`;
    const e = all[k];
    if (e && e.expires > Date.now()) return e.data;
  } catch {}
  return null;
}

function setClientCache(days, platform, data) {
  try {
    const all = JSON.parse(sessionStorage.getItem(CACHE_KEY) || '{}');
    all[`${days}|${platform}`] = { data, expires: Date.now() + TTL_MS };
    sessionStorage.setItem(CACHE_KEY, JSON.stringify(all));
  } catch {}
}
```

## Architecture for Precision Brass HYROS dashboard

Given:
- Auth-gated (Authorization header is required)
- 3-5 concurrent users max
- Upstream HYROS API 15-30s slow
- 500KB JSON payload
- Daily-updated upstream data

Optimal stack:
1. SERVER: module-scope in-memory Map cache with SWR pattern. TTL 5 min, stale 30 min.
2. SERVER: in-flight de-duplication (avoid 2 concurrent slow fetches for same key).
3. CLIENT: sessionStorage cache, 5 min TTL.
4. CLIENT: skeleton UI replacing "Loading..." spinner so structure paints in under 100ms.
5. SKIP: Vercel Runtime Cache (overkill, billable, 3-5 user scale doesn't justify).
6. SKIP: Vercel KV (same reason).
7. SKIP: Edge Cache (blocked by Authorization header anyway).
