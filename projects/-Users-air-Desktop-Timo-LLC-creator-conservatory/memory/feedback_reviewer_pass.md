---
name: Reviewer Pass After Any Skill/Memory Compaction
description: CRITICAL. After any /self-improve iteration, /fix-brain compaction, or SKILL.md edit, spawn a fresh reviewer subagent to diff BEFORE vs AFTER and flag silent semantic losses. Binary assertions can't catch rules that no test exercises.
type: feedback
originSessionId: cd22fabf-ac2e-4ec0-80c0-a1f41342ea1a
---
# Reviewer Pass, Third Line Of Defense Against Silent Deletion

**Rule:** After any compaction, dedup, or /self-improve iteration that modifies a SKILL.md, CLAUDE.md, MEMORY.md, or canonical rule file, spawn a fresh general-purpose subagent to diff BEFORE and AFTER versions and flag any rule/instruction/guidance present in BEFORE but missing in AFTER AND not reachable through any pointer. If reviewer reports LOST items, do NOT declare the iteration done. Restore or promote to canonical, re-verify.

**Why:** On 2026-04-14, Timo asked "is there a way you can teach yourself to improve skills better without deleting important information that you probably deleted?" The /self-improve Karpathy loop is binary-assertion driven: if no assertion tests for rule X, the loop can delete rule X and score UP (fewer rules = fewer violations). The COMPACTION GATE verifies pointer TARGETS exist, but not that target CONTENT matches the claim. The SCOPE GATE enumerates full file inventory, but doesn't verify per-file semantic preservation. Gap: silent per-file deletion with no failing signal. Reviewer pass closes it.

**How to apply (mandatory after any of these operations):**

1. **Identify the trigger event.** Any of:
   - /self-improve iteration modifying SKILL.md
   - /fix-brain compaction or dedup step
   - Manual trim of SKILL.md / CLAUDE.md / MEMORY.md / canonical knowledge file
   - Cross-cutting rule promotion (SKILL.md → knowledge/)

2. **Capture BEFORE** via git commit hash OR `/tmp/<filename>.before.md`.

3. **Make the change.**

4. **Capture AFTER** and list any pointer references added.

5. **Spawn general-purpose Agent** with the reviewer prompt from `~/.claude/knowledge/reviewer-pass-protocol.md`. Agent classifies each BEFORE rule as PRESERVED / MOVED / CONSOLIDATED / LOST.

6. **Act on verdict:**
   - PASS (0 losses) → proceed.
   - FAIL → for each LOST, either add to canonical FIRST or restore to SKILL.md. Re-run reviewer.

**Where this applies:**
- /self-improve runs (every iteration, not just final)
- /fix-brain runs (every compaction/dedup step)
- Manual edits to always-on files (CLAUDE.md, MEMORY.md, SOUL.md, PRIORITIES.md)
- Cross-cutting rule promotions

**The deeper failure pattern this prevents:**
Motivated reasoning at end of a loop. The loop "wants" to declare done. Self-review at the end is compromised. A fresh subagent with no stake in the iteration reads the diff with cold eyes. Same family as: verify quotes via transcript (outsource verification to a source that doesn't want the quote to be true), verify before compact (outsource target-check to a grep that doesn't want the compaction to succeed).

**Cost vs benefit:**
- Cost: ~30-60s per file reviewed, ~2-3 min per iteration, ~5-8 min per full /fix-brain run.
- Benefit: catches silent deletions that binary evals and pointer checks miss. One prevented rule-loss that would have shipped into daily workflow pays for weeks of reviewer passes.

**Full canonical:** `~/.claude/knowledge/reviewer-pass-protocol.md`

**Related memories:**
- feedback_verify_before_compact.md (verify pointer targets have content)
- feedback_audit_scope_must_match_usage.md (enumerate full inventory)
- feedback_skill_architecture.md (promote cross-cutting rules to canonical)
- feedback_verify_quotes_via_transcript.md (same pattern: outsource verification)
