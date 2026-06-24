---
name: project-meta-ads-audience-breakdown
description: meta-ads.html 'Audience' button opens a panel of LEADS by age/gender/country/placement (last 30d) from a new api/ac.js 'meta-breakdowns' action. Meta sees leads (custom registration event), NEVER the $ sale (HYROS, off-platform), so there is no revenue/ROAS by demographic.
metadata:
  type: project
---

**Built 2026-06-04** (Feature from the Evelyn Weiss "Claude Meta MCP" video; Timo's ask).
A header **Audience** button in meta-ads.html opens `openAudiencePanel()` -> a modal with 4
tables (age / gender / country / placement) showing spend + leads + cost-per-lead for the
last 30 days, sorted by leads, thin (spend<$100 or leads<5) segments dimmed. Cached once
per session client-side (`_audienceCache`).

**Server:** `api/ac.js` action `meta-breakdowns` (NOT a new function file -- folded in to
respect the Hobby 12-function cap). Calls Graph `/{act}/insights` with breakdowns=age |
gender | country | publisher_platform,platform_position, time_range last N days, in
parallel. Env: `META_USER_TOKEN` (already set), `META_AD_ACCOUNT` (defaults to
act_2443232582800725), `META_LEAD_ACTION` (defaults to the custom conversion
`offsite_conversion.custom.1628048068427083`).

**HONEST LIMIT (load-bearing):** Harrisson's account fires NO Meta purchase event -- the
only conversion Meta tracks is that custom registration (the "lead"). Real $ sales live in
HYROS, attributed per-ad, and CANNOT be split by demographic. So this view is leads / CPL /
spend ONLY, never revenue or ROAS by age/country. It's an ICP-validation tool ("who gives
the cheapest leads"), not a profit-by-segment view. The UI states this explicitly. Real
data 30d: 65+ cheapest ($12/lead, biggest volume), male 3x cheaper than female, US/CA only,
facebook/feed + IG cheap, facebook/reels expensive. Related: [[project_meta_ads_adset_level_redesign]].
