---
query: "Multi-tier cache testing methodology Vercel serverless Node.js 2026: 3-tier (in-memory Map, Supabase persistent, upstream API), test matrix structure, curl smoke tests, X-Cache header verification"
query_hash: "ca1515be4c48d73c"
slug: "multi-tier-cache-testing-methodology-vercel-serverless-node-"
model: "sonar"
date: "2026-05-07"
workspaces:
  - Precision-Brass
category: "Next.js / Supabase / Tech Stack"
tags:
  - vercel
  - caching
  - testing
  - three-tier
  - api
  - supabase
  - 2026
  - test-matrix
keywords:
  - cache
  - tier
  - curl
  - map
  - supabase
  - x-cache
  - vercel
  - verification
  - key
  - multi-tier
  - test1
  - api
  - compute
  - fluid
  - full
citations_count: 13
synthesized_in_notebooklm: true
stale_after: "2026-11-03"
---

# Multi-tier cache testing methodology Vercel serverless Node.js 2026: 3-tier (in-memory Map, Supabase persistent, upstream API), test matrix structure, curl smoke tests, X-Cache header verification

## Key findings

## Multi-Tier Cache Testing Methodology

### Architecture
```
Tier 1: In-process Map (Fluid Compute shared state) → X-Cache: HIT-T1
Tier 2: Supabase table (TTL 5min)                → X-Cache: HIT-T2/MISS→T2
Tier 3: Upstream API (rate-limited)              → X-Cache: MISS
```

### Test Matrix Structure
```yaml
test_matrix:
  concurrency: [1, 10, 100]  # Fluid Compute realism [1]
  cache_state: ["cold", "warm", "stale"]
  tiers: ["T1-only", "T1+T2", "full"]
  regions: ["iad1", "sfo1", "fra1"]  # Multi-region [2]
  repeat: 50  # Statistical significance
```

### Curl Smoke Tests
```bash
#!/bin/bash
# cache-smoke.sh - Multi-tier verification

BASE_URL="https://your-app.vercel.app/api/cache-test"
SUPABASE_KEY="your_supabase_key"

# Headers for cache verification
HEADERS="X-Cache: HIT-T1,HIT-T2,MISS | Cache-Control: max-age=300"

# 1. Cold start (Tier 3 only)
curl -w "T3: %{time_total}s\n" \
  -H "Cache-Control: no-cache" \
  "$BASE_URL?key=test1"

# 2. Tier 1 hit (Fluid Compute in-memory Map)
for i in {1..10}; do
  curl -w "T1: %{time_total}s %{http_code} %{response_header_X-Cache}\n" \
    "$BASE_URL?key=test1" &
done; wait

# 3. Tier 2 population (Supabase)
curl -X POST "$BASE_URL/cache" \
  -H "Authorization: Bearer $SUPABASE_KEY" \
  -d '{"key":"test1","data":"cached","ttl":300}'

# 4. Full tier verification
curl -w "Full: %{time_total}s → %{response_header_X-Cache}\n" \
  -H "X-Verify-Tiers: true" \
  "$BASE_URL?key=test1"

# 5. Stale invalidation
curl -X POST "$BASE_URL/invalidate?key=test1"
```

### Node.js Function Implementation
```js
// api/cache-test.js - Fluid Compute (2026) [1]
const cacheT1 = new Map(); // Shared across concurrent requests
const SUPABASE_URL = `https://your-project.supabase.co/rest/v1/cache`;
const UPSTREAM_API = 'https://slow-api.example.com/data';

export default async function handler(req, res) {
  const { key } = req.nextUrl.searchParams;
  const tiers = req.headers.get('X-Verify-Tiers') ? 'full' : 'fast';
  
  // Tier 1: In-process Map (persists across requests in Fluid instance) [1]
  if (cacheT1.has(key)) {
    res.setHeader('X-Cache', 'HIT-T1');
    return respond(res, cacheT1.get(key));
  }
  
  // Tier 2: Supabase (persistent, TTL-aware)
  const supabaseData = await fetchSupabase(key);
  if (supabaseData) {
    cacheT1.set(key, supabaseData); // Warm T1
    res.setHeader('X-Cache', `HIT-T2,T1-WARMED`);
    return respond(res, supabaseData);
  }
  
  // Tier 3: Upstream API
  if (tiers === 'full') {
    const upstreamData = await fetch(upstreamAPI + `?key=${key}`).then(r => r.json());
    await storeSupabase(key, upstreamData, 300); // 5min TTL
    cacheT1.set(key, upstreamData);
    res.setHeader('X-Cache', 'MISS→T2,T1-WARMED');
    return respond(res, upstreamData);
  }
  
  res.setHeader('X-Cache', 'MISS');
  res.status(404).json({ error: 'Cold miss, tiers=fast' });
}

async function fetchSupabase(key) {
  const res = await fetch(`${SUPABASE_URL}?key=eq.${key}&select=*`, {
    headers: { apikey: process.env.SUPABASE_KEY }
  });
  return res.ok ? res.json()?.[0] : null;
}
```

### State Coverage Matrix
```markdown
| Scenario | Expected X-Cache | Latency | Fluid Impact |
|----------|------------------|---------|--------------|
| Cold start | MISS | 1500ms+ | New instance [1] |
| T1 hit (10 concurrent) | HIT-T1 | <50ms | Shared Map [1] |
| T2 hit | HIT-T2,T1-WARMED | <100ms | DB roundtrip |
| Stale T2 → T3 | MISS→T2 | 800ms | ISR-like [2] |
| Multi-region | HIT-T1 (region-local) | Varies | Region cache [2] |
```

### Verification Assertions
```bash
# assert-cache.sh - Fail on invalid cache states
assert() {
  local actual=$(curl -s -w "%{response_header_X-Cache}" "$1" | tail -1)
  [[ "$actual" == "$2" ]] || { echo "FAIL: $1 expected $2 got $actual"; exit 1; }
}

assert "$BASE_URL?key=test1" "HIT-T1"  # After warm
assert "$BASE_URL?key=cold" "MISS"     # Fresh key
```

**Sources**: Vercel Fluid Compute concurrency [1], Multi-layer caching [2], Render 2026 limits [3]. Matches Stripe's cache debugging patterns (X-Cache headers) and Cloudflare Workers state testing [5].


## Citations

- https://getautonoma.com/blog/vercel-fluid-compute
- https://vercel.com/docs/caching
- https://render.com/articles/deploy-nodejs-production-2026
- https://www.luckymedia.dev/insights/vercel
- https://www.digitalapplied.com/blog/serverless-functions-vercel-cloudflare-guide
- https://github.com/vercel/next.js/discussions/87842
- https://vercel.com/docs/functions/runtimes
- https://community.vercel.com/t/news-cache-2026-03-09/35595
- https://www.clarifai.com/blog/vercel-vs-netlify
- https://community.vercel.com/t/news-cache-2026-03-02/34687.md

## Sources

- https://your-app.vercel.app/api/cache-test
- https://your-project.supabase.co/rest/v1/cache`
- https://slow-api.example.com/data
- https://getautonoma.com/blog/vercel-fluid-compute
- https://vercel.com/docs/caching
- https://render.com/articles/deploy-nodejs-production-2026
- https://www.luckymedia.dev/insights/vercel
- https://www.digitalapplied.com/blog/serverless-functions-vercel-cloudflare-guide
- https://github.com/vercel/next.js/discussions/87842
- https://vercel.com/docs/functions/runtimes
- https://community.vercel.com/t/news-cache-2026-03-09/35595
- https://www.clarifai.com/blog/vercel-vs-netlify
- https://community.vercel.com/t/news-cache-2026-03-02/34687.md