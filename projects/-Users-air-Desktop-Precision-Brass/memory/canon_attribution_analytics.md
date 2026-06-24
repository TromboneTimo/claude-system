---
name: canon-attribution-analytics
description: "HYROS truth, creative rollup, ad-set winners, classifier ground truth, age-aligned comparisons. Consolidated 2026-06-12 from 5 files."
metadata: 
  node_type: memory
  type: feedback
  consolidated: 2026-06-12
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

# Canon: Attribution & Analytics (HYROS, meta-ads board, classifiers, benchmarks)

Read before touching meta-ads.html, api/hyros.js, any classifier, or any "vs benchmark" metric.

---

## 1. HYROS is the ultimate source of truth for sales/revenue (2026-06-07)

If HYROS shows $0 revenue / 0 sales for an ad, the ad made $0, and it gets flagged like any non-converter. Period.

**Why:** Timo, 2026-06-07, when I flagged the "Coke can" ad set DISCONTINUE (HYROS 0 sales / $0 revenue over 730 days) and then hedged that "HYROS only attributes ~26% per-ad, so maybe it sold and HYROS missed it" and offered to build a manual "converted" override. He rejected that hard.

**How to apply:**
- Do NOT soften or second-guess a HYROS-driven flag with "attribution gap" caveats. The meta-ads board already treats HYROS revenue as truth (winner = `hyros_revenue > 0`); keep it that way.
- Do NOT build manual sale-override UI. No "mark as converted" by hand. HYROS decides.
- The ~26% attribution caveat in the code applies to BOOKED CALLS (already dropped from grading 2026-05-29), NOT to sales/revenue. Don't conflate them.
- When asked "didn't X get a sale?": check HYROS, report what HYROS says, and stand on it.

(Also a project rule in MEMORY index: $0 = $0; flag it. No attribution-gap hedging. The 26% caveat = CALLS.)

---

## 2. Roll HYROS sales up to the CREATIVE, not the ad_id (2026-06-03)

**From 2026-06-03 (Timo, angry):** the dashboard labeled an ACTIVE ad "TURN OFF" ($763 spent, 0 sales) that was actually a proven $6.8K winner. Root cause: HYROS attributes each sale to the exact Meta `ad_id` that earned it, but when you duplicate an ad in Meta the copy gets a NEW ad_id and is named "<base> - Copy N". The sale stayed with the original copy's ad_id; the active re-launch (a different ad_id) read 0 sales.

**Rule:** before any per-ad sales/kill decision in meta-ads.html, roll HYROS sales up to the CREATIVE across its copies. `normalizeCreative(name)` strips trailing "- Copy N" suffix(es); `state.creativeSales[key]` sums sales/revenue per creative (built at the top of buildAdSets from state.hyrosByAd). A creative that sold under ANY copy is "proven" and is NEVER a problem ad / never flagged TURN OFF; the drill-in shows "creative sold N / $X (another copy)" + a green Proven chip. See project_meta_ads_adset_level_redesign.

**Caveats / open:** matching is by full name minus the copy suffix, so it does NOT unify inconsistent prefixes ("PB 011" vs "P-B 011") or treat different ad numbers (008 vs 011) as the same creative -- that's Timo's naming convention to define if he wants it. Always VERIFY a kill flag against HYROS ground truth (query /functions/v1/hyros-revenue, match the normalized creative) before trusting it -- a difference is not a cause until checked against the real data. Same lesson as section 4 below: I shipped the kill flag without checking HYROS first.

---

## 3. Ad-set-level winners; paused sets are NEVER active winners (REVERSED 2026-06-03, refined 2026-06-07)

### Reversal history (preserve this)
- **Original rule (2026-05-28, now REVERSED):** a ~$6.8K-revenue Timo ad was buried as paused, so classify() was changed to keep the sale-check ABOVE the paused check and show ANY ad with a sale as a WINNER displayed Active with full ROI ("any sale = Active winner", per-ad level).
- **REVERSED 2026-06-03 (Harrison feedback, via WhatsApp audio).** That per-ad rule WAS the bug Harrison caught: the dashboard was labeling ad sets that are OFF as active winners, and the Warnings tab listed ad sets that aren't even running.

### Current model (meta-ads.html)
Report at the AD SET level. A set's status is its REAL delivery (running = >=1 ad actually delivering). A paused/archived ad set reads **Paused** and lives in the **Past Performers** tab, regardless of past sales -- never an active winner. Running Winners / Warnings / Pending only ever contain currently-running ad sets. See project_meta_ads_adset_level_redesign.

**Why:** Harrison won't act on a snapshot. He keeps a running set with a high cost-per-contact ($211) because it still produces sales on a long cycle (~every 2 months) -- that's a Running Winner (it has HYROS sales in the 365-day window), not a warning. And an OFF ad set is just history, not something to scale or kill now.

### REFINED 2026-06-07 (Timo: "you're not flagging enough")
Two holes closed in meta-ads.html (classify / classifyAdSet / tabConfig / adVerdict / rowAlerts):
1. **Winner = real REVENUE, not sale-count.** A HYROS "sale" worth $0 was promoting a running set with ~$1,225 spend / $0 back into Running Winners. Winner test everywhere is now `hyros_revenue > 0`. A $0-revenue sale no longer shields a money-loser.
2. **Set-level kill line ($500).** Per-ad kill line still applies, PLUS a running set is a bleeder if `unprovenSpend` (sum of active spend on creatives that never earned real revenue under any copy) >= $500. Catches a set bleeding $500+ across several sub-$500 ads (the per-ad-only rule from 2026-06-03 missed these). Proven creatives stay carved out so a re-launched winner copy never drags a set down. `adVerdict` now grades a set on unprovenSpend so the verdict matches the flag.

### STRICTER PASS, same session (Timo: "flag bad/non-converting ads harder, into the morning pile sooner"). Shipped + verified live:
3. **Creative-level burn rollup.** `state.creativeBurn[normalizeCreative]` sums spend across ALL copies; `creativeIsLosing(name)` = cumulative spend >= KILL_LINE with $0 revenue. `isProblemAd` now flags any active copy of a losing creative even if that copy is < $500 (verified: a $66 "P-B 003 - Copy" got flagged because its creative burned >$500 across copies). Proven creatives (revenue>0) still exempt.
4. **Morning pile sooner.** Warnings-tab entry dropped from unprovenSpend >= $500 to >= $250 (KILL_LINE/2); Pending is now only < $250 + no problem ad. DISCONTINUE verdict still fires at >= $500, WATCH at $250-500. So the two pure-Timo running sets ($475-480) now sit in Warnings as WATCH ("approaching the $500 kill line").

KILL_LINE const stayed 500 (the DISCONTINUE/loser line, = Harrison's "sale by $500" target). To go even harder, lower KILL_LINE. Hero + turn-off list + card/modal copy all updated from "over $500 / 0 sales" to "not converting / $0 revenue". Verified: Warnings 2->4, turn-off list 8 ads, 0 console errors, screenshots read.

---

## 4. Classifier verification must use GROUND TRUTH, not internal consistency (2026-05-06)

When checking a classifier (HYROS platform inference, email categorization, ad-vs-organic detection, anything that buckets data), do NOT settle for "no leakage between buckets" or "my Python mirror agrees with the JS". Self-consistency proves nothing about correctness. Two implementations of the same wrong rule will happily agree.

The rule that DOES catch errors:
1. Sample 5 to 10 rows from EACH bucket.
2. Show the user the source data (name, tag, traffic source, any meta fields) plus the assigned label.
3. Ask: "Is each row in the right bucket?"
4. Only after the human confirms is the classifier verified.

**Why:** On 2026-05-06, I "verified" Precision Brass HYROS classification by mirroring `inferPlatform` in Python and reporting "PASS: no leakage detected" against 365 days of real sales. I had `adSource.adAccountId` and `adSource.platform=FACEBOOK` in the raw API payload (literally printed it earlier in the same conversation) and ignored it. Result: 89 sales / $261,392 of paid Meta ads were sitting in the "Facebook organic" bucket. Timo had to point at the screen: "you're saying Facebook has made almost $20,000, but it was really mostly Facebook ads I got it to that place. I don't know how you're missing." A **$269,558 attribution error** went undetected. (The global CLASSIFIER GATE in ~/.claude/CLAUDE.md now enforces this, citing the same incident: "$269K of paid Meta ads sat in a Facebook organic bucket for 90 minutes after I called the classifier verified.")

**Specific failure modes that produced the miss:**
- **Self-consistency theater:** Python mirror of the JS rule on real data, called the cross-platform-leakage check "PASS." The Python had the same bug as the JS, so of course they agreed. Internal agreement is worthless.
- **Trusted code comments over data.** inferPlatform had a comment "CONSERVATIVE rule. Trusting adSourceId swept organic FB/IG sources into Meta Ads." I assumed the rule was correct instead of testing whether "CONSERVATIVE" was right for THIS account's data.
- **Looked for technical leakage, not semantic correctness.** Checked "does a tag with 'youtube' end up in the facebook bucket?" (contamination detection). The actual question: "does the row in the facebook bucket match what a human would call a Facebook organic click?" Never asked it.
- **Did not use available signals.** The HYROS API returns `adSource.adAccountId` and `adSource.platform`. Both are definitive paid-ad markers. I dumped a sample sale earlier in the conversation that included these fields. Did not connect them to classification.
- **Did not ask the domain expert.** Timo runs Harrison's ads. He knows the naming convention ("we date them, audience name, MF, musical instruments"). The naming convention is in his head, not in the data.

**How to apply going forward:**
1. Before declaring a classifier correct, dump samples per bucket and ask the user. "Here are 5 rows currently labeled facebook organic. Are these actually organic? If not, tell me what's different about them so I can fix the rule."
2. List all the signals available in the source data BEFORE writing the classifier. For HYROS: trafficSource, source.name, source.tag, adSource.adAccountId, adSource.platform, lead.tags, sourceLinkAd.adSourceId. Decide which are decisive vs heuristic. Use the decisive ones first.
3. For platform/category detection on customer accounts, ask for the customer's naming convention up front. "What naming pattern do your paid ads vs organic posts follow in HYROS?" 30 seconds of input prevents days of bad attribution data.
4. A passing self-test is not a passing test. "My Python matches the JS" / "linting clean" / "no exceptions thrown" is not verification of business correctness.
5. When the user reports a numbers-look-wrong issue, the FIRST move is to dump the contested bucket and ask them to spot-check. Not patch the rule and re-test against itself.

**Generalizable rule:** any time I am about to write "PASS" / "verified" / "no issues found" about a categorization, I must be able to point at a human confirmation. Until that exists, the categorizer is unverified, regardless of how many internal checks pass. Applies to ALL workspaces, all classifiers (blog templates, content categories, audience personas, sales funnel stages, anything).

Related code rule: api/hyros.js imports lib/hyros-source-map.js so YouTube el= tags without 'youtube'/'yt' bucket correctly; mirror new video tags into the map (project_youtube_attribution_classifier_fix).

---

## 5. Age-aligned comparisons: never compare partial cumulative values against final totals (2026-06-11)

2026-06-11: shipped a "vs Typical" email tracker that compared a 4-hour-old send's cumulative clicks against the FINAL totals of matured sends. It passed every gate (syntax, deploy, screenshot, zero console errors) because the gates verify rendering, not semantics. Timo rejected it from one screenshot: "this is just god awful."

**Why:** "Renders correctly" is not "measures correctly." A comparison metric has a definition, and the definition can be wrong while every pixel is right. YouTube's typical band = the last ~10 comparable items AT THE SAME AGE since publish, interpolated from per-item time series.

**How to apply:**
1. Before building any benchmark/comparison feature, write the comparison rule in one sentence and check it against how the reference product actually defines it. If the rule compares values captured at different maturities, it is wrong.
2. Hunt the CLASS, not the instance: the same flaw lived in the CTR tier chips (WEAK assigned to an hours-old send). Sends under 48h get MATURING, no tier.
3. The fix pattern used here: per-entity time series snapshots (api_cache key `email_snap:<cid>`, zero DDL), a 30-min GitHub Actions heartbeat (project_reply_capture_pipeline-style secret), linear interpolation at the current item's age, "N of 10 priors have data at this age" honesty label, building-history note instead of a misleading bar when coverage < 4 priors, final-vs-final only when BOTH sides are matured (>7d).

---

## Source files (absorbed 2026-06-12)
- feedback_hyros_is_sales_source_of_truth.md (2026-06-07)
- feedback_hyros_sales_follow_the_creative_not_adid.md (2026-06-03)
- feedback_any_sale_is_active_winner.md (2026-05-28 origin, REVERSED 2026-06-03, refined 2026-06-07; reversal history preserved above)
- feedback_classifier_verification_must_use_ground_truth.md (2026-05-06)
- feedback_age_aligned_comparisons.md (2026-06-11)
