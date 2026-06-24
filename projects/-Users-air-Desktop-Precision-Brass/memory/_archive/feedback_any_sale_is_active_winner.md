---
name: feedback-any-sale-is-active-winner
description: "REVERSED 2026-06-03 by Harrison. meta-ads now reports at the AD SET level and a paused/archived ad set is NEVER shown as an active winner, even with past sales. The old per-ad \"any sale = winner shown Active\" rule was the bug Harrison caught."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: af1dedbd-b693-4fcb-9923-a4abb532695b
---

**REVERSED 2026-06-03 (Harrison feedback, via WhatsApp audio).** The earlier rule
"ANY ad with a sale = WINNER shown Active even if ADSET_PAUSED/archived" was WRONG
and is the bug Harrison caught: the dashboard was labeling ad sets that are OFF as
active winners, and the Warnings tab listed ad sets that aren't even running.

**Current model (meta-ads.html):** report at the AD SET level. A set's status is its
REAL delivery (running = >=1 ad actually delivering). A paused/archived ad set reads
**Paused** and lives in the **Past Performers** tab, regardless of past sales -- never
an active winner. Running Winners / Warnings / Pending only ever contain currently-
running ad sets. See [[project-meta-ads-adset-level-redesign]].

**Why:** Harrison won't act on a snapshot. He keeps a running set with a high
cost-per-contact ($211) because it still produces sales on a long cycle (~every 2
months) -- that's a Running Winner (it has HYROS sales in the 365-day window), not a
warning. And an OFF ad set is just history, not something to scale or kill now.

**REFINED 2026-06-07 (Timo, "you're not flagging enough").** Two more holes closed in
meta-ads.html (classify / classifyAdSet / tabConfig / adVerdict / rowAlerts):
1. **Winner = real REVENUE, not sale-count.** A HYROS "sale" worth $0 was promoting a
   running set with ~$1,225 spend / $0 back into Running Winners. Winner test everywhere
   is now `hyros_revenue > 0`. A $0-revenue sale no longer shields a money-loser.
2. **Set-level kill line ($500).** Per-ad kill line still applies, PLUS a running set is
   a bleeder if `unprovenSpend` (sum of active spend on creatives that never earned real
   revenue under any copy) >= $500. Catches a set bleeding $500+ across several sub-$500
   ads (the per-ad-only rule from 2026-06-03 missed these). Proven creatives stay carved
   out so a re-launched winner copy never drags a set down. `adVerdict` now grades a set
   on unprovenSpend so the verdict matches the flag.
**STRICTER PASS, same session (Timo: "flag bad/non-converting ads harder, into the
morning pile sooner").** Shipped + verified live:
3. **Creative-level burn rollup.** `state.creativeBurn[normalizeCreative]` sums spend
   across ALL copies; `creativeIsLosing(name)` = cumulative spend >= KILL_LINE with $0
   revenue. `isProblemAd` now flags any active copy of a losing creative even if that
   copy is < $500 (verified: a $66 "P-B 003 - Copy" got flagged because its creative
   burned >$500 across copies). Proven creatives (revenue>0) still exempt.
4. **Morning pile sooner.** Warnings-tab entry dropped from unprovenSpend >= $500 to
   >= $250 (KILL_LINE/2); Pending is now only < $250 + no problem ad. DISCONTINUE
   verdict still fires at >= $500, WATCH at $250-500. So the two pure-Timo running sets
   ($475-480) now sit in Warnings as WATCH ("approaching the $500 kill line").
KILL_LINE const stayed 500 (the DISCONTINUE/loser line, = Harrison's "sale by $500"
target). To go even harder, lower KILL_LINE. Hero + turn-off list + card/modal copy all
updated from "over $500 / 0 sales" to "not converting / $0 revenue". Verified: Warnings
2->4, turn-off list 8 ads, 0 console errors, screenshots read.

## Detail (moved from index 2026-06-10)
Origin of the old (now-reversed) rule, 2026-05-28: a ~$6.8K-revenue Timo ad was buried as paused, so classify() was changed to keep the sale-check ABOVE the paused check and show any ad with a sale as a WINNER displayed Active with full ROI. That per-ad rule is exactly what Harrison reversed on 2026-06-03 (see above).
