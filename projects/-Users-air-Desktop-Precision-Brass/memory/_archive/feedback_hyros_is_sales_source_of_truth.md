---
name: feedback_hyros_is_sales_source_of_truth
description: "HYROS is the ultimate source of truth for sales/revenue. Don't hedge ad flags with attribution-gap caveats or build manual sale overrides. $0 HYROS = $0."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: af1dedbd-b693-4fcb-9923-a4abb532695b
---

HYROS is the **ultimate source of truth for sales/revenue.** If HYROS shows $0 revenue / 0 sales for an ad, the ad made $0, and it gets flagged like any non-converter. Period.

**Why:** Timo, 2026-06-07, when I flagged the "Coke can" ad set DISCONTINUE (HYROS 0 sales / $0 revenue over 730 days) and then hedged that "HYROS only attributes ~26% per-ad, so maybe it sold and HYROS missed it" and offered to build a manual "converted" override. He rejected that hard.

**How to apply:**
- Do NOT soften or second-guess a HYROS-driven flag with "attribution gap" caveats. The meta-ads board already treats HYROS revenue as truth (winner = `hyros_revenue > 0`); keep it that way.
- Do NOT build manual sale-override UI. No "mark as converted" by hand. HYROS decides.
- The ~26% attribution caveat in the code applies to BOOKED CALLS (already dropped from grading 2026-05-29), NOT to sales/revenue. Don't conflate them.
- When asked "didn't X get a sale?": check HYROS, report what HYROS says, and stand on it. See [[feedback_any_sale_is_active_winner]] and [[project_meta_ads_revenue]].
