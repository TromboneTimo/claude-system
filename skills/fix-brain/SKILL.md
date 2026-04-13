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

Origin: 2026-04-13 fix-brain run almost weakened Timo's 8-item slide pre-check. Full rule: `creator-conservatory/memory/feedback_verify_before_compact.md`.

**SCOPE GATE (MANDATORY at start AND end of multi-file work):**
Before STARTING any cleanup/dedup/refactor: ENUMERATE the full file inventory affected. If an audit subagent flags "X duplicated in 14 files," your scope is 14 files, NOT the 3 the agent named in its summary. Run an exhaustive grep BEFORE deciding what to fix.

Before DECLARING DONE: list every file in the original inventory. For each file NOT addressed, justify why (irrelevant, false positive, deferred with reason). Subset completion is not completion.

Origin: 2026-04-14 fix-brain run deduped 3 of 14 skills with same Visual QA bloat, called it done, ignored slide/marketing skills Timo uses daily. Full rule: `creator-conservatory/memory/feedback_audit_scope_must_match_usage.md`.

**SKILL ARCHITECTURE AUDIT (MANDATORY in step 2):**
For each skill examined, check:
1. **Size targets:** SKILL.md ideal ~60 lines, max 500. Anything beyond gets extracted to `references/` subfolders.
2. **Cross-cutting duplication:** Grep for blocks that appear in 2+ SKILL.md files. Promote to `~/.claude/knowledge/<rule>.md`, replace with 1-2 line references in each consumer.
3. **Reference verification:** For any "see reference" pointer, GREP target to confirm content present (Compaction Gate).

The 3-part promotion test for a cross-cutting rule (from rules-distill reference impl):
- Appears in 2+ skills
- Actionable behavior change ("do X" or "don't do Y")
- Not already covered by an existing canonical rule

Full architecture: `~/.claude/knowledge/skill-architecture.md`. Failure mode: 2026-04-14 fix-brain found 14 skills with duplicated Visual QA block (308 wasted lines). Architecture rule prevents recurrence.

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
