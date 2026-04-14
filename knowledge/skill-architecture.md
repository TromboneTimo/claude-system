# Skill Architecture: How to Maintain Skills Without Bloat

**Canonical source for skill design rules across all of Timo's skills.**

Based on Perplexity research 2026-04-14 (8 sources synthesized) + concrete reference implementation at github.com/affaan-m/everything-claude-code/skills/rules-distill/SKILL.md. See `~/.claude/knowledge/perplexity_research_database.md` for full citations.

## The Core Problem

Skills bloat geometrically when cross-cutting rules (visual QA, content verification, deploy gates, em-dash bans, etc.) get COPY-PASTED into every SKILL.md that needs them. Result: 14+ identical 22-line blocks across skills, drift between copies, refinements made in the wrong file. This is documentation DRY-violation. Same disease as code copy-paste.

## The Architecture

```
~/.claude/
├── CLAUDE.md                          (always-on, ~60 lines, gate triggers + universal rules)
├── knowledge/                         (canonical cross-cutting rules)
│   ├── visual-self-qa-protocol.md     (cited by 14+ skills)
│   ├── skill-architecture.md          (this file)
│   ├── perplexity_research_database.md (research log)
│   └── ...
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md                   (target ~60 lines, max 500)
│       ├── references/                (per-skill corpora, loaded on demand)
│       │   ├── commands.md
│       │   ├── workflows.md
│       │   └── examples.md
│       ├── scripts/                   (executable helpers)
│       └── eval/                      (binary assertions for /self-improve)
└── projects/<workspace>/memory/
    └── feedback_*.md                  (workspace-specific lessons)
```

## Hard Rules

### Rule 1: SKILL.md Length Targets
- **Ideal:** ~60 lines (per CLAUDE.md research)
- **Max:** 500 lines
- **Anything beyond:** extract to `references/` subfolder

### Rule 2: Cross-Cutting Rule Test
Before writing ANY rule into a SKILL.md, ask: **"Will this rule apply to 2+ skills?"**
- YES → write it ONCE in `~/.claude/knowledge/<rule>.md`. SKILL.md references it in 1-2 lines.
- NO → write it inline in SKILL.md.

### Rule 3: Reference Format
When SKILL.md references a canonical rule, use this format (1-2 lines max):

```markdown
## VISUAL SELF-QA (MANDATORY before reporting done)

After generating ANY HTML/PDF/slide/chart/image: render to PNG, READ with vision tool, fix issues, re-verify. Never outsource to user.

**Full protocol:** `~/.claude/knowledge/visual-self-qa-protocol.md`
```

NOT this (the bloat pattern):
```markdown
## VISUAL SELF-QA

[22 lines of detailed commands, examples, origin story, what to check, ...]
```

### Rule 4: Refinement Rule
When fixing/improving a cross-cutting rule: edit the canonical file, NOT the consumer references. If you find yourself editing the same paragraph in 3 SKILL.md files, STOP. The paragraph belongs in `~/.claude/knowledge/`.

### Rule 5: Progressive Disclosure
SKILL.md should contain:
- Triggers (when to activate)
- Role framing (1-2 sentences)
- Skill-specific instructions (what THIS skill does)
- Quick command examples (most-used)
- References to detailed workflows/commands in `references/`

SKILL.md should NOT contain:
- Long command tables (→ `references/commands.md`)
- Multiple workflow examples with code (→ `references/workflows.md`)
- Cross-cutting rules that apply to other skills (→ `~/.claude/knowledge/`)
- Verbose origin stories (→ link to feedback_*.md instead)

## The 3-Phase Audit Pattern (from rules-distill reference impl)

When auditing skills for cross-cutting bloat:

**Phase 1 (Inventory):** Deterministically scan all skill files. Don't filter yet.

**Phase 2 (LLM Judgment):** Group skills into thematic clusters. For each candidate rule, apply 3-part filter:
- Appears in 2+ skills
- Actionable behavior change ("do X" or "don't do Y")
- Not already in canonical rules

**Phase 3 (User Review):** Present table with verdicts (Append, Revise, New File, Already Covered, Too Specific). User approves before changes apply.

## Enforcement

- `/fix-brain` audits SKILL.md sizes + cross-cutting duplication every run
- `/self-improve` checks "is this cross-cutting?" before adding any rule
- `feedback_skill_architecture.md` (workspace memory) reminds Timo's working sessions
- Global CLAUDE.md `SKILL ARCHITECTURE GATE` fires on every conversation

## When To Promote A Rule To Canonical

Rule belongs in `~/.claude/knowledge/` if ANY of:
- It's referenced by 2+ skills currently
- It has a date origin like "Rule origin: 2026-XX-XX..." (signals reusable lesson)
- It includes commands or examples that 2+ skills would copy
- Its content is workflow-agnostic (about HOW to verify, not WHAT to do for this skill)

## When To Keep A Rule Local

Rule belongs IN SKILL.md if:
- It's specific to this skill's domain (e.g., n8n syntax rules in n8n-* skills)
- It's a triggering condition (when to activate THIS skill)
- It's a one-off example showing this skill's capability

## Failure Mode This Prevents

2026-04-13/14 fix-brain run discovered:
- Visual QA block duplicated in 14 SKILL.md files (22 lines each = 308 wasted lines)
- Content Verification Gate duplicated in 9 SKILL.md files (24 lines each = 216 wasted lines)
- Canonical files at `~/.claude/knowledge/` were MORE complete than any of the copies
- Total: ~580 lines of skill bloat eliminated by enforcing this architecture