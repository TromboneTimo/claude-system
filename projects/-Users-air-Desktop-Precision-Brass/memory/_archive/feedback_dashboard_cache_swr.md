---
name: feedback-dashboard-cache-swr
description: Every dashboard client cache MUST be stale-while-revalidate (render cached + ALWAYS background-refresh + swap if changed). The recurring stale-data bug = caches that render and return without revalidating. Audited + fixed 2026-05-26.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9627bbfc-ecec-4b40-9187-f019508c4cee
---

# Dashboard client caches must self-heal (stale-while-revalidate)

**Why:** The dashboard kept showing stale data (e.g. email-analytics stuck on "Daily Email 1 (subject loading)", meta-ads stale columns). Root cause class: client caches (IndexedDB/localStorage) that on load **render the cached copy and `return` without ever re-fetching** (readCache hardcoded `fresh:true`; loadAll commented "cached = always current, only ↻ refreshes"). So after any deploy or data change, the cache served old data until a MANUAL version bump. Bumping the version each time is a band-aid, not a fix.

**How to apply (the standard for ANY cached dashboard page):**
Stale-while-revalidate. On load: render cached instantly (speed), then ALWAYS fire a background network re-fetch, write the cache, and re-render ONLY if the fresh payload differs (token-guarded so switching range/filter mid-flight can't clobber). Pattern:
```
const cached = readCache(key);
if (cached) { render(cached.data); revalidateInBackground(token, key, cached.data); return; }
// cold path: fetch + writeCache + render
async function revalidateInBackground(token, key, prev){ try{ const d=await fetchNetwork(); writeCache(key,d); if(isStale(token,key))return; if(JSON.stringify(d)!==JSON.stringify(prev)){ render(d); } }catch(_){} }
```
The network fn must hit the network (not another cache layer). Verify on the LIVE authed page that a cached load fires exactly 1 background API call (patch window.fetch + count).

## Cache audit of all dashboard pages (2026-05-26)
- **email-analytics.html** (IDB `pb_ea_v*`): had the flaw. FIXED (SWR) + v7->v8 bump to clear the one existing stale cache.
- **channel-attribution.html** (IDB `CLIENT_DB_NAME`): had the flaw. FIXED (SWR).
- **scheduled.html** (localStorage): ALREADY did SWR. Fine.
- **meta-ads.html**: NO data cache, fetches meta_ads + hyros-revenue fresh every load. Fine (its stale issues were stale browser BUNDLES, not data cache; /meta-ads sends no-store).
- All other pages (scripts, emails, ideas, broadcast, revenue, youtube, instagram, facebook, book-meeting, index): no client API cache found.

If a NEW cached page is added, it MUST use the SWR pattern above. See [[project_dashboard_self_verify_authed]] for how to verify on the live authed page.
