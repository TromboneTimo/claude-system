# Reviewer Pass Protocol: Catch Silent Semantic Losses

**Canonical procedure for verifying any compaction, dedup, or self-improve iteration didn't silently delete important content.**

Companion to COMPACTION GATE (which verifies pointer targets exist) and SKILL ARCHITECTURE GATE (which prevents duplication). This rule catches what binary assertions and pointer checks are blind to: removed content that no eval tests for and no pointer preserves.

## The Core Problem

Binary-assertion-driven self-improvement loops (Karpathy pattern) only detect regressions they know to test for. If a SKILL.md contains rule X but no assertion exercises rule X, the loop can delete rule X without any test turning red. Compaction pointer-checks verify the canonical FILE exists, not that the canonical file contains the specific rule being removed. Result: silent rule deletion with no failing signal.

## When To Run

Mandatory after any of:
- `/self-improve` iteration that modifies a SKILL.md
- `/fix-brain` compaction or dedup step
- Any manual SKILL.md / CLAUDE.md / MEMORY.md trim
- Cross-cutting rule promotion (moving content from SKILL.md to `~/.claude/knowledge/`)

## The Procedure

### Step 1: Capture BEFORE
Before making changes, save the current state:
- If git-tracked: note the commit hash
- If not: copy file to `/tmp/<filename>.before.md`

### Step 2: Make the change
Proceed with the planned edit (dedup, compaction, rule addition, assertion fix).

### Step 3: Capture AFTER
Same file state, post-edit. Note any pointer references added (to `~/.claude/knowledge/*.md` or `feedback_*.md`).

### Step 4: Spawn reviewer subagent
Use the general-purpose Agent with this exact prompt structure:

```
You are a semantic-diff reviewer. Compare BEFORE and AFTER versions of a
skill/memory file. Your job is to catch silent semantic losses.

BEFORE:
<paste full BEFORE content>

AFTER:
<paste full AFTER content>

POINTERS ADDED (for reachability check):
<list any "see file X" references added in AFTER>

For each rule, instruction, checklist item, example, or behavioral guidance
present in BEFORE, classify:
1. PRESERVED: still in AFTER verbatim or near-verbatim
2. MOVED: content migrated to a pointed-to file. Verify by reading the
   pointer target and confirming the rule appears there. Cite line numbers.
3. CONSOLIDATED: merged with existing canonical rule. Verify canonical
   contains equivalent content.
4. LOST: removed from AFTER AND not reachable through any pointer AND not
   present in any canonical rule. FLAG IN RED.

Output format:

## Reviewer Pass Report for <filename>
- PRESERVED: <count>
- MOVED: <count, each with source to target line number>
- CONSOLIDATED: <count, each with canonical file cited>
- LOST: <count, each with verbatim quote of lost content>

Verdict: PASS (0 losses) or FAIL (N losses, list them)

Under 400 words total.
```

### Step 5: Act on verdict
- **PASS**: Proceed with declaring the iteration done.
- **FAIL**: Do NOT declare done. For each LOST item:
  - If it belongs in canonical: add it there FIRST, then re-run reviewer pass.
  - If it was rightly removed: confirm with user before finalizing.
  - If uncertain: restore to SKILL.md pending user review.

## Why Use A Subagent, Not Self-Review

Self-review at end of a loop suffers from motivated reasoning: the loop "wants" to declare done. A fresh subagent with no stake in the iteration reads the diff with cold eyes. Cost: ~30-60s per review. Benefit: catches the silent-deletion failure class that binary evals cannot cover.

## What This Does NOT Replace

- COMPACTION GATE (pointer target verification) is still required. Reviewer pass assumes targets exist and checks content reachability through them.
- SCOPE GATE (full inventory enumeration) is still required. Reviewer pass operates per-file, doesn't catch "you only fixed 3 of 14 files."
- Binary assertions / eval.json are still primary signal for regressions.

Reviewer pass is the THIRD line of defense for the specific failure mode of silent semantic deletion during compaction/dedup/self-improve.

## Failure Mode This Prevents

2026-04-13: /fix-brain compaction almost weakened 8-item slide pre-check by pointer-swapping to a canonical file that didn't yet contain the content. COMPACTION GATE caught it (verified target was empty).

2026-04-14: /fix-brain dedup removed Visual QA blocks from 3 SKILL.md files, left 11 with originals. SCOPE GATE was needed (and now exists).

Next class of failure (prevented by this protocol): a /self-improve iteration passes all binary assertions while removing a rule that happened to be under-tested. Eval score goes UP (fewer rules means fewer things to violate). Behavior silently degrades. No gate catches it without a semantic review.

## Cost Estimate

- Typical SKILL.md: ~100-300 lines. Reviewer pass: 30-45s per file.
- Typical compaction iteration touches 1-3 files. ~2-3 min added per iteration.
- /fix-brain full run (~10 files): ~5-8 min added.

Worth it. A silent rule deletion that ships into Timo's daily workflow costs far more than a few minutes per audit.
