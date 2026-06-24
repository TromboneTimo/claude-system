---
name: project-meta-ads-adset-level-redesign
description: meta-ads.html reports at the AD SET level (Harrison 2026-06-03). buildAdSets() rolls ads into sets; classifyAdSet() uses real running status (paused set = Past Performers, never an active winner). Tabs Running Winners/Warnings/Pending = running only; Past Performers = paused/archived. Click a set -> drill into its ads.
metadata:
  type: project
---

**meta-ads.html data model (2026-06-03 redesign, Harrison's feedback):**
- `buildAdSets(rows)` aggregates per-ad `state.rows` into `state.adsets` (one object per
  ad_set_id): sums amount_spent/impressions/reach/link_clicks/leads/video_thruplays;
  hyros_sales/hyros_revenue summed from the per-ad HYROS attribution; `running` = any ad
  with ad_delivery 'active'/'ACTIVE'; thumbnail = highest-spend ad in the set; ad_id =
  that thumb ad (for the creative), card_id = ad_set_id (for click-to-open).
- `classifyAdSet(s)`: NOT running -> 'paused' (Past Performers), ALWAYS, regardless of
  sales. Running + sales -> 'winners'; running + spend>=KILL_LINE($500) + 0 sales ->
  'bleeders'; etc.
- render()/paintTabs/paintHero/tabConfig all operate on `state.adsets`. Tabs: top='Running
  Winners', warn='Warnings', pending='Pending' (all `s.running` only), inactive='Past
  Performers' (`!s.running` + has data). `adIsActive(s)=!!s.running`.
- `buildAdCard` reused as-is (ad-set objects carry row-compatible fields: ad_name=ad_set_name,
  amount_spent, hyros_*, roas, cpl, frequency, bucket). Card data-cid = card_id.
- `openDetail(set)`: ad-set summary grid + a "N ads in this set" list (each ad's
  Running/Off + spend + sales). Detects an ad set via `Array.isArray(r.ads)`; skips the
  per-ad day-over-day trend for sets.
- Legacy drill funcs (aggregate/groupBy/cardHtml/renderAdSetCards/renderCampaignCards/
  inScope/bucketCounts/paintBreadcrumb) are DEAD (no call sites) -- ignore.

As of redesign: 48 ad sets, ~10 running (2 winners / 6 warnings / 2 pending), 29 Past
Performers. The big historical winners (Oct 27 $11K, Warm audiences $9.5K, Jan 11 $6.8K,
26 March $7K ADSET_PAUSED) all correctly sit in Past Performers now, not faked as Active.
Supersedes [[feedback-any-sale-is-active-winner]]. Related: [[project-meta-thumbnails-durable-storage]].


**UPDATE 2026-06-03 (pt11) -- per-AD kill line + per-ad drill-in:** The $500 kill line
is PER INDIVIDUAL AD, not the ad-set total (Timo: "it's only a problem when one ad itself
spends over 500"). buildAdSets() now computes per set: `s.problemAds` (running ads with
spend>=$500 AND 0 own-sales), `s.problemSpend` (their summed spend), `s.worstAdSpend`.
- Warnings tab match = running set, 0 set-sales, problemAds.length>0. Pending = running,
  0 sales, NO problem ad. A set whose spend is spread across many sub-$500 ads is Pending,
  not a warning.
- A WINNING set (has sales) that hides a problem ad STAYS in Running Winners (Timo's call)
  and shows a red 'N ads over $500, 0 sales' badge (.ac-killbadge) on the card. Hero shows
  total 'N ads over $500 to turn off ($X spent, 0 sales)' across ALL running sets.
- openDetail(): for a set, the per-ad list renders FIRST (above the set-total metrics grid),
  sorted by spend desc, each ad with its OWN thumbnail (metaThumbs[a.ad_id], 20 unique URLs
  verified on prod), status, spend, sales/ROAS, and a red 'Turn off' flag on problem ads.
- BUG FIXED: render() had its own stale inline copy of the bucket filters (set-aggregate
  spend) while paintTabs() counted via tabConfig.match -> count/cards disagreed. render()
  now filters via `tabConfig.find(t=>t.key===k).match` so the two can never diverge. When
  changing bucket logic, edit tabConfig.match (source of truth) -- paintHero + classifyAdSet
  still hold separate copies, keep them in sync.


**UPDATE 2026-06-04 (pt17) -- SINGLE-COUNT revenue attribution (replaces the double-counting rollup):**
A set's revenue/sales = each creative's HYROS earnings assigned to exactly ONE home set, so
everything reconciles. Home = the running copy with the highest spend; if no running copy, the
copy where it sold the most (tiebreak highest spend). buildAdSets builds `state.creativeHome`
(creativeKey -> sid) + `state.homeTotals` (sid -> {sales,revenue}); `s.hyros_sales/revenue` =
homeTotals[sid]. A creative with no synced copy stays unattributed = the unsynced gap.
Reconciles: total $319,554 = $288,221 attributed to 16 sets + $31,333 unsynced; 110 sales = 96
attributed + 14 unsynced. The HYROS banner now shows total = attributed + gap. Modal rows show a
creative's earnings on its HOME set only ("credited to its active set" elsewhere) so rows sum to
the set total. `hyros_*_direct` keeps the raw exact-ad-id figure for the revenue tooltip. The brief
high-risk creative-lifetime rollup (which double-counted across sets) was WRONG and is gone.
