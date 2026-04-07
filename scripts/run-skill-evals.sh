#!/bin/bash
# Master Skill Eval Runner
# Runs every 4 days at 10am JST via local crontab
# Launches Claude Code CLI to self-improve all skills

DATE=$(date +%Y-%m-%d)
LOG_DIR="/Users/air/.claude/eval-logs"
mkdir -p "$LOG_DIR"

# Launch Claude Code with the eval prompt
/usr/local/bin/claude --print --dangerously-skip-permissions "
Read /Users/air/.claude/scripts/eval-all-skills.md for context.

Run /self-improve on skills in this priority order. Do 10 skills per session, rotate through all 48 over multiple runs. Track which batch you're on in /Users/air/.claude/eval-logs/.last-batch.

Priority skills (always run first):
1. cc-email
2. email
3. rr-email
4. blog-write
5. blog-rewrite
6. marketing-social
7. marketing-blog
8. marketing-present
9. marketing-creative
10. marketing-research

Before running evals, read ALL feedback files:
find /Users/air/.claude/projects/*/memory/feedback_*.md
If any new feedback exists since last run, update the relevant skill's eval/eval.json with new assertions.

For each skill:
1. Load eval/eval.json
2. Run 3 test iterations
3. If score < 80%, make ONE change to SKILL.md
4. Re-test. Keep if improved, revert if not.
5. Log to /Users/air/.claude/eval-logs/$DATE.md

Flag any skill scoring below 60% as NEEDS ATTENTION.
" >> "$LOG_DIR/$DATE.log" 2>&1
