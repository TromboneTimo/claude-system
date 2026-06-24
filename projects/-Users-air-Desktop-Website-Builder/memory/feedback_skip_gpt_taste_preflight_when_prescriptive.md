---
name: skip-gpt-taste-preflight-when-brief-is-prescriptive
description: The gpt-tasteskill preflight ritual (Python RNG sim, design_plan, AIDA verification) adds latency without value when the user brief is already highly prescriptive. Skip it and execute.
type: feedback
originSessionId: 6bffca3c-789c-4c2a-9d3b-f957e123208e
---
When `/gpt-taste` is invoked with a fully prescriptive brief (explicit typography stack, explicit layout rules, explicit animation behavior, explicit banned patterns), skip the skill's Python RNG simulation and design_plan preflight block. Go straight to building.

**Why:** The gpt-tasteskill loads a long system prompt demanding a `<design_plan>` block with simulated Python `random.choice()` output, AIDA check, hero math verification, etc. BEFORE writing any code. When the user has already specified Noto Serif JP + Cormorant + Manrope, exact section architecture, exact animation timings, and named anti-patterns, the preflight produces zero additional signal. It just adds latency before the first useful output. Timo got angry watching this theater play out before any file was written.

**How to apply:**
- If the brief has 5+ specific design decisions already made (fonts named, layout architecture specified, animation timings given), skip the preflight entirely.
- Still honor the skill's substantive rules: no 6-line hero wraps, no gapless-grid defaults, no meta-labels, real motion, massive spacing, 2-3 line H1 limit.
- Only run the full preflight ritual when the brief is genuinely open ("build a SaaS landing page") and you need to invent the architecture.
- Skills are tools, not scripts. When they add latency without value for a specific request, the right move is to skip the ceremony and execute.
