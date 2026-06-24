---
name: Rules Without Enforcement Mechanisms Are Aspirations
description: CRITICAL. When saving a rule, pick the right enforcement mechanism. Mechanical rules (em dashes, formatting) belong in hooks. Pre-action checks belong in gates (CLAUDE.md). Post-action reviews belong in agents. Prose in a skill file is the weakest option: it hopes you will remember.
type: feedback
originSessionId: cd22fabf-ac2e-4ec0-80c0-a1f41342ea1a
---
# Rules Without Enforcement Mechanisms Are Aspirations

**Rule:** When documenting a new rule, choose the enforcement layer that matches the rule's nature, not the layer that is easiest to write. Hooks for mechanical patterns you will never internalize. Gates for pre-action checks (before generating, before compacting, before declaring done). Subagents for post-action review (fresh cold eyes). Prose in a SKILL.md or CLAUDE.md is the weakest option: it hopes you will read it at the right moment and remember the rule.

**Why:** On 2026-04-14, the em-dash block hook caught me twice in one session, despite "never use em dashes" being in CLAUDE.md for weeks. Prose-level rules do not override the habit. Only the PreToolUse hook fires reliably. Same session: the SKILL ARCHITECTURE principle had existed in past feedback files before I wired it to a gate. It existed as a note, not a rule. The difference between "wrote it down" and "enforced it" is the difference between 0% and 95% compliance.

**How to apply (decision tree):**

1. **Is the rule mechanical / pattern-based?** (Em dashes, banned phrases, forbidden filenames, specific regexes.)
   Use a **hook** in `~/.claude/hooks/`. PreToolUse blocks bad content. UserPromptSubmit injects context.

2. **Does the rule need to fire BEFORE an action?** (Pre-flight check, verification before compaction, scope enumeration before cleanup.)
   Use a **gate** in `~/.claude/CLAUDE.md`. Gates are always-on, load every conversation.

3. **Does the rule need fresh cold eyes AFTER an action?** (Was anything silently deleted? Does the output match the claim?)
   Use a **subagent** with a dedicated protocol file. Invoked by the skill or /fix-brain. Fresh context, no motivated reasoning.

4. **Is the rule specific to one skill's domain?** (n8n expression syntax, blog SEO tags.)
   Inline in that SKILL.md. Still prose, but scoped.

5. **Does the rule apply to 2+ skills?** (Visual QA, content verification, compaction checks.)
   Canonical in `~/.claude/knowledge/`, referenced in 1-2 lines from each consumer.

**The escalation pattern:**
Prose -> gate -> hook. Start with prose. If the rule keeps failing, escalate to a gate. If the gate keeps failing, escalate to a hook. Do not start at the top and engineer prematurely, but do not hide behind prose when the pattern is clearly mechanical.

**Where this applies:**
- Writing any new feedback_*.md (ask: is prose enough?)
- Adding any rule to CLAUDE.md (ask: should this be a gate or a hook?)
- Any /fix-brain iteration adding a new rule
- Any time Claude says "I will remember not to X" (that is the weakest commitment possible)

**The deeper failure pattern this prevents:**
Treating documentation as enforcement. Writing a rule in prose feels like progress. It is not. It is a note-to-self that the note-writer will ignore. Enforcement is the thing that makes future-Claude different from past-Claude.

**Related memories:**
- feedback_adhd_enforcement.md (only forced UserPromptSubmit hook injection works)
- feedback_skill_architecture.md (cross-cutting rules belong in canonical)
- feedback_reviewer_pass.md (post-action subagent review)
- feedback_negative_rules_first.md (NEVER-do-X wording fires more reliably)
