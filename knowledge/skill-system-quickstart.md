# Skill System Quickstart: How To Actually Use What Got Built

**Audience:** You, when you forget how this works. Written dummy-style because that's useful.

## The 30-Second Mental Model

You have 5 always-on gates that fire automatically during any skill/memory work:

| Gate | Fires when | Stops you from |
|------|-----------|----------------|
| VISUAL GATE | Generating HTML/PDF/slide/chart/image | Shipping rendering bugs unseen |
| CONTENT VERIFICATION GATE | Writing copy about real people | Fabricating behavioral claims |
| COMPACTION GATE | Trimming any SKILL.md/CLAUDE.md/MEMORY.md | Pointer-swap without verifying target has content |
| SCOPE GATE | Any multi-file audit/cleanup | Satisficing on agent-named subset |
| SKILL ARCHITECTURE GATE | Writing any rule into a SKILL.md | Copy-pasting cross-cutting rules into 14 places |

Plus the Reviewer Pass (third line of defense) that catches silent deletions the other gates miss.

## What You Should Notice Working (Positive Signs)

### Across all workspaces

1. **SKILL.md files getting SHORTER over time, not longer.** Target: ~60 lines. Max: 500. If a skill crosses 200 lines, next `/fix-brain` should flag it.

2. **New rules appearing in `~/.claude/knowledge/` instead of duplicating.** When Claude says "I promoted this rule to canonical," that's the system working. Old pattern: same rule copy-pasted in 14 skills. New pattern: 1 canonical file, 14 one-line references.

3. **`feedback_*.md` entries getting linked in MEMORY.md indexes.** Every workspace's `memory/MEMORY.md` should have an index entry for each feedback file. Check by: open `memory/MEMORY.md` in any workspace, see if the list matches `ls memory/feedback_*.md`.

4. **Reviewer Pass Reports with "Verdict: PASS" after `/fix-brain` compactions.** If you see FAIL, something real was about to be lost. Good catch.

5. **Auto-sync commits showing NET DELETIONS in SKILL.md files BUT additions in knowledge/.** That's dedup happening correctly (content moved, not lost).

### Red flags to watch for

1. **SKILL.md files growing past 500 lines.** Means SKILL ARCHITECTURE GATE failed or wasn't checked. Action: `/fix-brain` or ask Claude to extract content to `references/`.

2. **Pointer to a canonical file that doesn't contain what it claims.** Action: `grep -r "see.*knowledge" ~/.claude/skills/ | head` then manually grep target for the specific content.

3. **Rules you remember existing that now aren't anywhere.** Action: `cd ~/.claude && git log -p --all -S "distinctive phrase from the rule"` to find when it got deleted and restore.

4. **Canonical files (`~/.claude/knowledge/*.md`) getting SMALLER.** Canonical files should grow as cross-cutting rules get promoted. Shrinkage means something was removed. Check `git log -p knowledge/<file>.md`.

## How To Actually Use The Reviewer Pass

### Pattern A: You're about to edit a skill file manually

```bash
~/.claude/scripts/reviewer-pass.sh capture ~/.claude/skills/my-skill/SKILL.md
# (make your edits via Claude or hand)
~/.claude/scripts/reviewer-pass.sh diff ~/.claude/skills/my-skill/SKILL.md
```

Then tell Claude: *"run the skill-reviewer subagent on the diff we just captured."*

### Pattern B: Claude's `/fix-brain` or `/self-improve` runs

Automatic. The REVIEWER PASS GATE in [fix-brain/SKILL.md](~/.claude/skills/fix-brain/SKILL.md) and [self-improve/SKILL.md](~/.claude/skills/self-improve/SKILL.md) Step 4.5 invoke the reviewer pass before declaring any compaction done. You'll see the Reviewer Pass Report in the run output.

### Pattern C: Retrospective audit (did a past commit silently delete something?)

```bash
~/.claude/scripts/reviewer-pass.sh from-git skills/blog-rewrite/SKILL.md abc1234 def5678
```

Then ask Claude: *"run skill-reviewer on blog-rewrite between those two commits."*

## Cross-Workspace Checklist

Run through this monthly (or when something feels off):

### ~/.claude (global)

```bash
cd ~/.claude && git log --oneline -20       # recent activity
wc -l CLAUDE.md SOUL.md PRIORITIES.md       # target: under 65/50/50
find skills -name "SKILL.md" -exec wc -l {} + | sort -rn | head -10
# flag any SKILL.md over 500 lines
find knowledge -name "*.md" -exec wc -l {} +
# canonical files should be 80-200 lines typically
```

### Per workspace (creator-conservatory, robinsons-remedies, precision-brass, etc.)

```bash
cd <workspace> && wc -l CLAUDE.md memory/MEMORY.md
# target: CLAUDE.md under 60, MEMORY.md under 200 (index only)
grep -c "^- \[" memory/MEMORY.md            # count of index entries
ls memory/feedback_*.md | wc -l             # count of feedback files
# these two numbers should be close (every feedback file indexed)
```

### System health

```bash
find ~/.claude/skills -name "eval.json" | wc -l
ls ~/.claude/skills | wc -l
# these should be equal or close (every skill has an eval)
```

## When To Run What

| Situation | Command |
|-----------|---------|
| Something feels wrong, don't know what | `/fix-brain` |
| One skill produces bad output | `/self-improve <skill-name>` |
| Suspect a rule was lost | Pattern C above, then ask Claude to run skill-reviewer |
| Just finished major work | Auto-updates fire (SESSION_LOG, PRIORITIES). No action |
| Weekly hygiene | `/weekly-review` |

## Signs The System Is Healthy (You Don't Need To Do Anything)

- Auto-sync commits happening every session close
- `~/.claude/knowledge/` folder tracked in git (committed 2026-04-14)
- New canonical files appearing in `~/.claude/knowledge/` over time
- SKILL.md files trending shorter
- `feedback_*.md` index entries in MEMORY.md files
- /fix-brain runs ending with "Verdict: PASS"

## Signs It's Degrading (Action Required)

- Same rule written identically in 3+ SKILL.md files (SKILL ARCHITECTURE GATE failed)
- Canonical file referenced but doesn't contain the rule (COMPACTION GATE failed)
- A rule you remember being there is now gone everywhere (run Pattern C)
- `/fix-brain` runs reporting LOST items (act on each one)
- CLAUDE.md growing past 70 lines (needs compaction, but use gates)

## The Tools You Have

- `/fix-brain`: full system audit, runs all gates, auto-pollinates lessons
- `/self-improve <skill>`: Karpathy loop on one skill with reviewer pass
- `/weekly-review`: cross-workspace intelligence review
- `~/.claude/scripts/reviewer-pass.sh`: manual BEFORE/AFTER capture
- `~/.claude/agents/skill-reviewer.md`: dedicated subagent for semantic diff
- `~/.claude/knowledge/`: canonical cross-cutting rules (now git-tracked)
- Git recovery: `git log -p --all -S "phrase"` to find deleted content

## The One Rule You Need To Remember

**When in doubt, run `/fix-brain`.** It triggers all 5 gates, runs evals on every skill, pollinates cross-workspace lessons, catches stale priorities, and reports a punch list. It's the big red button.

For everyday skill work: let the gates fire automatically. They're wired into CLAUDE.md and every relevant SKILL.md. You don't need to think about them.

## If You Want Proof It's Working

```bash
cd ~/.claude && git log --oneline --all | head -20
cat ~/.claude/CLAUDE.md | grep "^## .*GATE"  # should show 5 gates
ls ~/.claude/knowledge/*.md                   # should show 5+ canonical files
ls ~/.claude/agents/*.md                      # should include skill-reviewer.md
```

If all 4 commands return the expected output, the system is wired correctly.
