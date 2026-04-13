---
name: fix-brain
description: "Full system self-improvement run. Tests all skills with evals, cross-pollinates feedback across workspaces, checks file bloat, updates PRIORITIES.md staleness, and reports what improved. Triggers on 'fix your brain', 'improve yourself', 'self-improve all', or 'optimize system'."
user_invocable: true
---

# Fix Your Brain - Full System Self-Improvement

When triggered, run the complete self-improvement pipeline across all workspaces and skills.

## Steps (run in order)

### 1. Audit File Health
Check line counts on all always-on files:
- ~/.claude/CLAUDE.md (target: under 65)
- ~/.claude/SOUL.md (target: under 50)
- ~/.claude/PRIORITIES.md (target: under 50)
- ~/.claude/SESSION_LOG.md (prune entries older than 14 days)
- All project CLAUDE.md files (target: under 60 each)
- All MEMORY.md files (target: under 20 each, technical details in reference files)

If any file exceeds its target, flag it and propose a trim.

**COMPACTION GATE (MANDATORY for every trim):**
Before declaring ANY file compaction done:
1. Identify every new "see reference file" pointer added (grep the compacted file for `feedback_`, `knowledge/`, `references/`, `see .*\.md`).
2. For each pointer, GREP the target file for the specific content you claimed is there. Use specific keywords, not vague ones.
3. If the target is missing detail: STOP. Update target file FIRST with full content, THEN compact the source.
4. Never pointer-swap without verifying the target. A reference to a file that doesn't have the rule = null reference = silently weakened rule.

This gate exists because on 2026-04-13 a fix-brain run almost weakened Timo's 8-item slide pre-check by compacting to a reference file that only had 4 items. Caught only because the user asked. Full rule: `creator-conservatory/memory/feedback_verify_before_compact.md`.

### 2. Run Self-Improve on All Skills with Evals
Find all skills that have an eval/ directory:
```bash
find ~/.claude/skills/ -name "eval.json" -exec dirname {} \;
```
For each skill found, run the Karpathy loop:
- Test against binary assertions
- Make ONE change if any fail
- Retest, keep or revert
- Log results to eval/improvement-log.md

### 3. Run Weekly Review
Execute the weekly-review skill:
- Read all feedback_*.md files across all workspaces
- Identify universal rules to propagate to CLAUDE.md
- Check PRIORITIES.md for stale projects (7+ days)
- Update "Last Touched" dates
- Report WIP limit compliance

### 4. Check for Unlogged Feedback
Scan recent conversation for any corrections that weren't saved:
- Did the user correct something that doesn't have a feedback_*.md yet?
- Did any SKILL.md get updated without adding a corresponding eval assertion?

### 5. Report
Output a summary:
```
## Brain Fix Report - [date]

### File Health
[line counts, any over-limit flagged]

### Skills Improved
[which skills were tested, scores before/after, changes made]

### Cross-Workspace Lessons
[rules propagated, conflicts found]

### Priority Status  
[stale projects, WIP compliance]

### Gaps Found
[missing feedback files, missing eval assertions, bloated files]
```

## Autonomy
Once started, run all 5 steps without asking permission. Report at the end.
