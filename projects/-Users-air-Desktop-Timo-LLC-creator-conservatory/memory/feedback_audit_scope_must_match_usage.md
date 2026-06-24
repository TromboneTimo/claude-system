---
name: Audit Scope Must Match Actual Usage, Not Agent's Flagged List
description: CRITICAL. When an audit agent reports problems across N skills, filter the list through "which skills does Timo actually use daily" BEFORE deciding what to fix. Don't blindly execute the agent's named scope. The agent flags by line count, not by usage frequency.
type: feedback
originSessionId: cd22fabf-ac2e-4ec0-80c0-a1f41342ea1a
---
# NEVER Treat An Audit Agent's Named Scope As The Work Scope

**Rule:** When a /fix-brain or audit agent reports issues across multiple files/skills, the agent's specific list is WHERE PROBLEMS EXIST, not WHAT TO FIX FIRST. Filter through "what does Timo actually use this week" before picking what to ship. Audit agents see line counts. They don't see workflow.

**Why:** On 2026-04-14, /fix-brain audit agent reported Visual QA block duplicated in 14 skill files. I deduped 3 (blog, cc-email, rr-email) because those were the skills the agent specifically named in its summary. I IGNORED 11 others including frontend-slides, marketing-present, marketing-creative, marketing-data, manipulate-image, blog-image, blog-chart, email, blog-write, blog-rewrite, marketing-blog, clone-website. Timo had been using the slide/presentation skills daily for two weeks. He caught it: "what about all the presentation skills and shit we were using from slide shit god damnit." Same near-miss pattern as my "I trimmed line counts without verifying content" fuckup yesterday: I prioritized the easy/named work over the actually-impactful work.

**How to apply (mandatory before any audit-driven cleanup):**

1. **Read the audit agent's full file list, not just the summary.** Agents truncate. The summary names 3 skills. The actual problem hits 14. Look at the underlying grep results.

2. **Cross-reference against recent SESSION_LOG.md entries.** Which skills/files has Timo touched in the last 7 days? Those are the ones where bloat hurts MOST. Fixing a skill he doesn't use is theater.

3. **Specifically scan for slide/presentation/marketing skills.** Timo runs decks daily. frontend-slides, marketing-present, marketing-creative, marketing-data, blog-chart, blog-image, manipulate-image. These are his hot path. Audit-flagged bloat in these = highest priority.

4. **Do NOT let the agent's named subset become your scope.** If audit says "X is duplicated in 14 files" and lists 3 by name, your job is the 14, not the 3.

**Where this applies:**
- /fix-brain runs (always)
- Any audit subagent reporting cross-file issues
- /weekly-review cross-pollination work
- Any "find all X" scan

**The deeper failure pattern this prevents:**
Letting the agent's report become a satisficing scope. "I did what the agent named" feels like completion. It's not. Same family as: prioritizing line-count metrics over content preservation (`feedback_verify_before_compact.md`), prioritizing narrative convenience over factual accuracy (`feedback_fabricated_behavior.md`). All three are forms of preferring tidy/easy/named over correct/hard/comprehensive.

**Related memories:**
- feedback_verify_before_compact.md (verify references survive compaction)
- feedback_fabricated_behavior.md (parent: ASK don't invent)
- feedback_read_before_asking.md (re-read context, don't infer)
