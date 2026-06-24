---
name: project-meta-thumbnails-durable-storage
description: "Meta-ads creative thumbnails are now downloaded ONCE into the public Supabase Storage bucket 'meta-thumbs' and served via permanent URLs, instead of short-lived signed fbcdn links that 403'd after ~1.5-4.5 days. api/ac.js action=meta-thumbnails handles store-on-first-sight. Supersedes the old fbcdn-URL caching."
metadata: 
  node_type: memory
  type: project
  originSessionId: f84aeb30-40f8-4688-89fd-7320b07676a1
---

**The 403/blank-creative bug (fixed 2026-06-03):** Graph `creative.thumbnail_url` and the video `/thumbnails` edge return signed `*.fbcdn.net` URLs whose `oe=` expiry is only ~1.5-4.5 days (NOT ~10 as an old code comment claimed). The api/ac.js `action=meta-thumbnails` cache TTL was 6 days, so the dashboard kept serving links fbcdn had already killed -> 403s, blank ad cards. Proven by decoding the `oe=` of all 133 cached rows (every one expired) and confirming a live `force=1` re-fetch returns a fresh URL that loads 200.

**The durable fix (what Timo wanted: "store thumbnails, only update for brand-new ads"):** `action=meta-thumbnails` now downloads each ad's best creative image ONCE and uploads it to the **public Supabase Storage bucket `meta-thumbs`** (`<ad_id>.jpg`), then hands the browser the permanent public URL `${SUPABASE_URL}/storage/v1/object/public/meta-thumbs/<ad_id>.jpg`. api_cache `meta_thumb:<ad_id>` payload now stores that stable storage URL (permanent, never re-fetched) or `{url:null}` for ads the token can't read (negative cache, NEG_TTL re-check 7 days). Graph is only hit for a brand-new ad (not yet stored) or `force=1`. Legacy fbcdn-cached rows auto-detect as not-stored (url doesn't start with the storage prefix) and re-store on next request. MAX_NEW=50 cap per request + `more:true` flag guards the Vercel timeout; api/ac.js maxDuration raised to 60 in vercel.json.

**Gotchas:**
- CSP `img-src` in vercel.json must include `https://*.supabase.co` (added 2026-06-03) alongside the existing `*.fbcdn.net`.
- The bucket `meta-thumbs` is public (created via Storage API `POST /storage/v1/bucket {public:true}`).
- Bulk backfill (133 ads at once, force=1) rate-limited Meta on the 2nd Graph call (the video `/thumbnails` edge), so ~28 ads stored as the 64px `thumbnail_url` fallback. Re-storing them slowly did NOT upgrade them -> those 28 ads genuinely only expose a 64px image to this token (105/133 are full-res 1080px). Acceptable; it's the best Meta returns for them.
- Backfill pattern: call the deployed endpoint with `force=1&ids=<batch>` in batches of ~20 (curl, not python-urllib which hits SSL cert errors on this mac). Token = mint a user JWT (see [[reference-view-authed-dashboard]]); endpoint requires Bearer auth.
- Same endpoint feeds meta-ads.html AND channel-attribution Meta board, so the fix covers both.

Related: [[project-meta-thumbnails-and-csp]] (the older fbcdn-era doc, now superseded), [[feedback-vercel-kills-fire-and-forget]] (why the upload is awaited, not fire-and-forget).
