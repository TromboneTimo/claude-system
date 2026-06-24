---
name: age-aligned-comparisons
description: "Any \"vs typical/benchmark\" metric MUST compare at equal age/maturity. Never compare a partial cumulative value against final totals. Caught by Timo on vs-Typical v1 (2026-06-11)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 691f9e3a-bc3b-40f4-b4d6-3643fe24482f
---

2026-06-11: shipped a "vs Typical" email tracker that compared a 4-hour-old send's cumulative clicks against the FINAL totals of matured sends. It passed every gate (syntax, deploy, screenshot, zero console errors) because the gates verify rendering, not semantics. Timo rejected it from one screenshot: "this is just god awful."

**Why:** "Renders correctly" is not "measures correctly." A comparison metric has a definition, and the definition can be wrong while every pixel is right. YouTube's typical band = the last ~10 comparable items AT THE SAME AGE since publish, interpolated from per-item time series.

**How to apply:**
1. Before building any benchmark/comparison feature, write the comparison rule in one sentence and check it against how the reference product actually defines it. If the rule compares values captured at different maturities, it is wrong.
2. Hunt the CLASS, not the instance: the same flaw lived in the CTR tier chips (WEAK assigned to an hours-old send). Sends under 48h get MATURING, no tier.
3. The fix pattern used here: per-entity time series snapshots (api_cache key email_snap:<cid>, zero DDL), a 30-min GitHub Actions heartbeat ([[project-reply-capture-pipeline]] style secret), linear interpolation at the current item's age, "N of 10 priors have data at this age" honesty label, building-history note instead of a misleading bar when coverage < 4 priors, final-vs-final only when BOTH sides are matured (>7d).
