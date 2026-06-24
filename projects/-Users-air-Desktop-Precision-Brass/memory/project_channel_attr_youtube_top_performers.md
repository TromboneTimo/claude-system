---
name: project-channel-attr-youtube-top-performers
description: "channel-attribution YouTube tab swaps the Sales Funnel sub-tab for a 'Top Performers' table; how the per-platform sub-tab override works."
metadata: 
  node_type: memory
  type: project
  originSessionId: 6a16b3f6-b8fd-429a-acff-d79a73c1345e
---

2026-05-28, deployed to main (commit 0c9e4c1). On `dashboard/channel-attribution.html`:

**YouTube platform tab only:** the "Sales Funnel" sub-tab is relabeled "Top Performers" and renders the Top Content table (heading "Best Performing Videos and Ads") instead of the funnel strip. The now-redundant "Top Content" sub-tab is HIDDEN on YouTube so there are not two identical tabs. Every other platform tab (All / Email / Meta Ads / Meta Organic) keeps Top Content + Sales Funnel unchanged.

**Mechanism (no new panes, reuses existing content viewpane):**
- `applyPlatformViewConfig()` runs on every platform-tab click and in init: when `activePlatform==='youtube'` it hides `.viewtab[data-view="content"]` and sets `.viewtab[data-view="funnel"]` text to "Top Performers" (else restores "Sales Funnel" + shows content btn), then re-resolves the active view.
- `setActiveView(view)` has a `ytSwap` branch: on YouTube when view==='funnel' it activates the `content` viewpane (paneView) while keeping the funnel button highlighted.

This shipped alongside the long-unmerged `channel-attribution-meta-organic` branch work that had never reached main: Meta Organic merge (FB+IG organic combined, TikTok parked), cross-tab Top Content leak fix, and the BMW + Youtubetimo el-tag mappings in `dashboard/lib/hyros-source-map.js` (bmwtestamonial -> Mike "BMW" testimonial video; youtubetimo -> channel page). Those mappings turned the old "Bmwtestamonial * VERIFY" placeholder into a proper titled row with thumbnail.

**Thumbnails (added 2026-05-28, commit 8b675cb):** rows with no real image no longer show an empty dashed box. `contentCell()` else-branch now renders a platform-BRANDED tile (glyph + label, colored by `c.platform`: YouTube ▶ / Meta Ads ◈ / Facebook f / Instagram ◉ / Email ✉ / Direct ↗). Still never fabricates a content thumbnail; VERIFY badge stays when the specific content is unconfirmed. Also mapped the one confirmed unmapped YouTube el-tag `youtuberelaxationroutine` -> video VOpkBLJ2YCM in hyros-source-map.js. The other ~6 YouTube placeholder el-tags (youtubebuzzing, youtubecomments, ytcomments, youtubebootcamp, youtube37routine, generic youtube) are NOT in voc/youtube/index.json so cannot be mapped without guessing. Most remaining branded-tile rows are Meta ad creatives the token cannot read + email/direct (no image exists).

**meta-ads.html (same commit):** Top Performers + Warnings boards now show ONLY live ads via `adIsActive(r)` (= bucket!=='paused' && !archived; archived = spend 0 + revenue >0). New third tab `💤 Paused / Archived` (key `inactive`) holds every paused/archived ad with data, sorted by revenue. Verified on prod: Top 2 / Warn 52 all active, Paused-Archived 94 all inactive, 0 leak.

Landed via worktree (other meta-ads worker confirmed done first). See [[feedback_concurrent_repo_use_worktree]].

**meta-ads LOAD architecture (commit 94d856c, 2026-05-28):** meta-ads.html had NO client cache and the card grid was gated on a heavy 365-day `hyros-revenue` edge function with NO timeout, so slow/cold loads showed a blank grid (sometimes forever). Fixed in `fetchAll(forceRefresh)`:
- IndexedDB SWR cache `pb_meta_ads_v1` (store `cache`, key `meta_ads_365`) caches {rows, hyrosByAd, hyrosByAdSet, coverage}. Repeat loads paint instantly then refresh.
- `fetchT(url,opts,ms)` = fetch + AbortController timeout (meta_ads 20s, hyros-revenue 45s). hyros degrades to null on timeout.
- Ads paint as soon as meta_ads returns via `buildRows(metaRows, null)`; revenue + bucketing fill in when hyros lands; if hyros null, retry once in background + self-heal. Never blank.
- `buildRows()` extracted as pure builder. Refresh button calls `fetchAll(true)`.
- MEASURED bottleneck (prod resource-timing): auth is FAST (~1.2s); the cost is data fetches. meta_ads ~2.8s, hyros-revenue 3.6s warm but up to ~10s COLD START. Do NOT blame auth.js.

**hyros-revenue server-side cache (deployed 2026-05-28):** the gitignored edge function `supabase/functions/hyros-revenue/index.ts` now wraps its compute in a read-through stale-while-revalidate cache in the `api_cache` table (key `hyros-revenue:<days>`, TTL 30 min, `?force=1` bypass). fresh -> instant; stale -> serve stale instantly + recompute via `EdgeRuntime.waitUntil`; cold/force -> compute then store. Uses SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY (auto-injected env). Result: hyros-revenue dropped from 3.6s to ~1.07s on prod, no more 10s cold spikes. Deploy: `SUPABASE_ACCESS_TOKEN=<sbp_ PAT from MASTER.md> supabase functions deploy hyros-revenue --project-ref iwlernqpwdsjarygoeog` (verify_jwt=true preserved via config.toml). The function source is GITIGNORED (lives only in the main working dir, never committed; deploy via CLI only). `deno check` it before deploy.

**meta-ads card placeholder:** ads whose creative the Meta token can't read (dead account) now show a clean Meta-blue image-frame icon + "No creative" tile (not a bare infinity glyph). Real creatives are still fetched + cached per ad via `/api/ac?action=meta-thumbnails` (negative-caches the unreadable ones). On prod every card has a real thumbnail or the tile, 0 empty.
