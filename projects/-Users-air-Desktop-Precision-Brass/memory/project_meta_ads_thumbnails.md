---
name: project-meta-ads-thumbnails
description: "meta-ads.html is now a two-board layout (Top Performers + Warnings) with creative thumbnails. Thumbnails come from /api/ac?action=meta-thumbnails (api_cache, 6-day TTL). The top-performer ads live in an ad account the Meta token CANNOT read, so they show placeholders until Timo grants access."
metadata: 
  node_type: memory
  type: project
  originSessionId: 1406ccde-9bdf-4b95-ad6a-39b05517b2d4
---

2026-05-28: Rebuilt `dashboard/meta-ads.html` (per Timo) from the dense tab-switched table into TWO stacked boards, mirroring the channel-attribution "Best Performing Ads" design:
- Top Performers: ads with a HYROS sale, ranked by revenue. Cols: Ad, Cost, Clicks, Sales, Revenue, Profit, ROAS, Warn.
- Warnings: active zero-sale ads ranked by spend burned. Cols: Ad, Cost, Leads, Calls, Freq, Verdict (DISCONTINUE/WATCH/PROVING), Warn.
- Ad cell is thumbnail-first because the Meta `ad_name` is unreliable (Timo's recurring complaint). Name is secondary text. Row click still opens the detail modal (reuses `openDetail`).

Thumbnails = `/api/ac?action=meta-thumbnails` (Graph `creative{thumbnail_url}`). Now CACHED per-ad in `api_cache` (key `meta_thumb:<ad_id>`, 6-day TTL, positive + negative cache). Before caching, one Graph call per ad per load tripped Meta rate limit (code 17) and thumbnails flickered. After: a warm cache serves all ids with 0 live Graph calls. Signed CDN URLs (`*.fbcdn.net`, allowed in CSP img-src) expire about 10 days, so TTL stays under that.

HARD CONSTRAINT, top performers show NO thumbnail. 16 of 17 revenue-driving ads have ad_ids ending `...0430` (a different ad account). The current Meta token (act_2443232582800725 "Precision Brass 1", `...0598` ads) returns `"missing permissions"` for `...0430` creatives, so they negative-cache and render the infinity placeholder. Only `...0598` ads (mostly test/new = the Warnings board) get real thumbnails. To give the top performers thumbnails, Timo must grant the Meta token access to the `...0430` ad account (Meta Business settings). Not fixable in code. Ties to the account split in [[project-meta-ads-hyros-revenue-pipeline]] (revenue acct 8388204844642603 not token-accessible).

Deploy note: prod drifted to old code once because CLI `vercel --prod` deploys the working tree, and a later deploy from a tree WITHOUT the (then-uncommitted) changes reverted it. Always COMMIT meta-ads/api changes so any deploy carries them. Verified live on precision-brass-dashboard.vercel.app/meta-ads: two boards, 0 console errors, 57/83 thumbnails, cache 83/83 hit.
