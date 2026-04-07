# Master Eval Runner

This prompt is used by /schedule to run evals across all skills every 4 days.

## What This Does
1. Reads all feedback files from every workspace
2. Loads eval.json for each skill
3. Runs /self-improve on each skill (batched, top priority skills first)
4. Logs results to /Users/air/.claude/eval-logs/

## Skill Priority Order (run these first)
1. cc-email (Creator Conservatory emails)
2. email (Precision Brass emails)
3. rr-email (Robinson's Remedies emails)
4. blog-write (blog content)
5. blog-rewrite (blog optimization)
6. marketing-social (social media content)
7. marketing-blog (RR blog)
8. marketing-present (presentations)
9. marketing-creative (creative briefs)
10. marketing-research (market research)

## Remaining skills (run if time permits)
All other skills in /Users/air/.claude/skills/

## Process
For each skill:
1. Load its eval/eval.json
2. Run the skill 3 times against assertions
3. If score < 80%, make ONE improvement to SKILL.md
4. Re-test
5. Keep change if score improved, revert if not
6. Log result to eval-logs/YYYY-MM-DD.md

## Reporting (MANDATORY)
After all evals complete, write a summary to /Users/air/.claude/eval-logs/latest-report.md containing:
1. Date and which batch of skills was run
2. For each skill: name, score before, score after, what was changed (if anything)
3. Any skills flagged as NEEDS ATTENTION (below 60%)
4. Top 3 most common failure patterns across all skills
5. What feedback assertions were newly added from feedback files
6. Total skills improved vs total skills tested

This report should be readable in 2 minutes. No fluff.

## Token Budget
Max 50K tokens per skill. Skip to next skill if budget exceeded.
Total session budget: 500K tokens (covers ~10 skills per run, rotates through all over multiple runs).
