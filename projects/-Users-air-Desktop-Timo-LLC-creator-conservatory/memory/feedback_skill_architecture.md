---
name: Skill Architecture (Cross-Cutting Rules Belong in /knowledge/, Not Inline)
description: CRITICAL. Before writing any rule into a SKILL.md, ask "does this apply to 2+ skills?" If YES, write it ONCE in ~/.claude/knowledge/ and reference. If NO, inline. SKILL.md target ~60 lines, max 500. Pre-flight check on every skill write.
type: feedback
originSessionId: cd22fabf-ac2e-4ec0-80c0-a1f41342ea1a
---
# Skill Architecture, Apply DRY To Documentation

**Rule:** When writing or updating a SKILL.md, before adding any rule/checklist/protocol, ask: "Will this apply to 2+ skills?" If yes, the rule belongs in `~/.claude/knowledge/<rule>.md`, and the SKILL.md references it in 1-2 lines. If no, inline it. SKILL.md target is ~60 lines; max 500. Anything beyond gets extracted to `references/` subfolders.

**Why:** On 2026-04-13/14, /fix-brain found Visual QA block duplicated in 14 skills (308 wasted lines), Content Verification Gate duplicated in 9 skills (216 wasted lines), and the canonical files at `~/.claude/knowledge/` were MORE complete than any of the copies. Same disease as code copy-paste. Per Perplexity research 2026-04-14 (8 sources): Claude Code best practice is shared "constraint skill" or canonical knowledge folder, NOT inline duplication. Reference implementation: github.com/affaan-m/everything-claude-code/skills/rules-distill/SKILL.md.

**How to apply (mandatory before any SKILL.md write):**

1. **Pre-flight cross-cutting check.** Before adding any block to SKILL.md, grep `~/.claude/skills/*/SKILL.md` for similar text. If 2+ matches, the rule already exists or is being duplicated. Promote to `~/.claude/knowledge/`.

2. **SKILL.md size gate.** If SKILL.md exceeds 200 lines, before adding more: identify what can move to `references/<topic>.md` (commands, workflows, examples).

3. **Reference format** (1-2 lines, not the bloat block):
   ```
   ## RULE NAME (when it fires)
   One-sentence summary of what to do.
   **Full protocol:** `~/.claude/knowledge/<rule>.md`
   ```

4. **Refinement direction.** When a cross-cutting rule needs improvement: edit the canonical file in `~/.claude/knowledge/`, NOT the SKILL.md references. The SKILL.md references should never need updating because they're just pointers.

5. **The 3-part promotion test.** Promote a rule to canonical when:
   - It appears in 2+ skills
   - It has an "actionable behavior change" form ("do X" or "don't do Y")
   - It's not already covered by an existing canonical rule

**Where this applies:**
- Every SKILL.md write or update (mandatory pre-flight)
- /self-improve runs (must check before adding assertions)
- /fix-brain runs (must audit for duplication)
- Any new skill creation (start lean, push to references/)

**The deeper failure pattern this prevents:**
Treating documentation as monolithic. Each SKILL.md being "self-contained" became license to copy-paste cross-cutting rules. Result: every refinement became a 14-place edit (and only ever happened in 1-2 places, leading to drift).

**Architecture diagram:**
```
~/.claude/CLAUDE.md (60 lines, gate triggers + universal rules)
~/.claude/knowledge/<rule>.md (canonical cross-cutting rules, loaded on demand)
~/.claude/skills/<name>/SKILL.md (60 lines target, max 500, references > inlines)
~/.claude/skills/<name>/references/ (per-skill detail, loaded on demand)
```

**Full canonical:** `~/.claude/knowledge/skill-architecture.md`

**Related memories:**
- feedback_verify_before_compact.md (verify references contain claimed content)
- feedback_audit_scope_must_match_usage.md (enumerate full inventory)
- feedback_negative_rules_first.md (NEVER do X beats positive rules)
