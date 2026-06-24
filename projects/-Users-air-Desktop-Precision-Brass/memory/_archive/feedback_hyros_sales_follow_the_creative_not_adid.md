---
name: feedback-hyros-sales-follow-the-creative-not-adid
description: meta-ads -- HYROS attributes a sale to the EXACT ad_id that earned it, but Meta gives a re-uploaded ad ("... - Copy N") a brand-new ad_id, so a proven creative re-launched as a fresh copy looks like 0 sales. Roll sales up to the creative (strip "- Copy N") before deciding anything; never flag a proven creative TURN OFF.
metadata:
  type: feedback
---

**From 2026-06-03 (Timo, angry):** the dashboard labeled an ACTIVE ad "TURN OFF"
($763 spent, 0 sales) that was actually a proven $6.8K winner. Root cause: HYROS
attributes each sale to the exact Meta `ad_id` that earned it, but when you duplicate
an ad in Meta the copy gets a NEW ad_id and is named "<base> - Copy N". The sale stayed
with the original copy's ad_id; the active re-launch (a different ad_id) read 0 sales.

**Rule:** before any per-ad sales/kill decision in meta-ads.html, roll HYROS sales up to
the CREATIVE across its copies. `normalizeCreative(name)` strips trailing "- Copy N"
suffix(es); `state.creativeSales[key]` sums sales/revenue per creative (built at the top
of buildAdSets from state.hyrosByAd). A creative that sold under ANY copy is "proven" and
is NEVER a problem ad / never flagged TURN OFF; the drill-in shows "creative sold N / $X
(another copy)" + a green Proven chip. See [[project-meta-ads-adset-level-redesign]].

**Caveats / open:** matching is by full name minus the copy suffix, so it does NOT unify
inconsistent prefixes ("PB 011" vs "P-B 011") or treat different ad numbers (008 vs 011)
as the same creative -- that's Timo's naming convention to define if he wants it. Always
VERIFY a kill flag against HYROS ground truth (query /functions/v1/hyros-revenue, match
the normalized creative) before trusting it -- a difference is not a cause until checked
against the real data. This is the [[feedback_classifier_verification_must_use_ground_truth]]
lesson again: I shipped the kill flag without checking HYROS first.
