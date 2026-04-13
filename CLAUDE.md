# Global Claude Code Guidelines

<!-- CRITICAL AT TOP — "lost in middle" fix -->

## 4 FAILURE PATTERNS (NEVER TRIM)
1. Shared hooks break everything. After modifying shared state: test ALL features.
2. Same bug 3x = check the DATABASE (RLS, policies), not the code.
3. Verify in Safari, not curl. Stale tokens fool curl. Use raw fetch() for smoke tests.
4. Auto-transcripts lie. Client drafts aren't facts. Prospects aren't customers. Verify every unusual proper name against press kit/LinkedIn. Every credential from a client draft = ASK before propagating. Voice banks must separate PROSPECTS from CUSTOMERS.

## 2-STRIKE RULE
Same bug twice = STOP coding. Check the database. Don't iterate on code fixes.

## DEPLOY GATE (NEVER SKIP)
Build > QA Agent > API curl > Safari browser verify. All 4. Every time.

## VISUAL GATE (HTML/PDF/slide/chart/image)
Render to PNG and READ it yourself before reporting done. Never outsource visual QA. "Open for me" is NOT verification. Full protocol: `~/.claude/knowledge/visual-self-qa-protocol.md`

## CONTENT VERIFICATION GATE (proposals, emails, pitches about real people)
Before ANY behavioral claim ships, verify. Grep draft for: `already|existing|since you|your weekly|your monthly|like you do|given your`. For each hit: verify evidence or DELETE/REWRITE/ASK. ASK, don't invent. Full rule: `memory/feedback_fabricated_behavior.md`

## COMPACTION GATE (trimming CLAUDE.md, SKILL.md, MEMORY.md)
Before declaring compaction done: for every "see reference file" pointer added, GREP target file for the content. If missing, UPDATE target FIRST. Never pointer-swap unverified. Full: `memory/feedback_verify_before_compact.md`

## SCOPE GATE (any multi-file audit/cleanup/refactor/dedup)
Before starting AND before declaring done: ENUMERATE the full file inventory. If audit reports "X duplicated in 14 files" do NOT execute on the 3 it names. Execute on all 14. Before saying "done": list every file in the original problem set. For each NOT addressed: justify why. NO satisficing on the agent's named subset. Full: `memory/feedback_audit_scope_must_match_usage.md`

## SKILL ARCHITECTURE GATE (any SKILL.md write or update)
Before adding any block to SKILL.md: ask "does this apply to 2+ skills?" If YES, write once in `~/.claude/knowledge/<rule>.md` and reference in 1-2 lines. If NO, inline. SKILL.md target ~60 lines, max 500. Refine canonical, never the references. Full: `~/.claude/knowledge/skill-architecture.md`

## BOOT SEQUENCE
Read in order: `SOUL.md` > `PRIORITIES.md` > `SESSION_LOG.md` > project `memory/MEMORY.md`. Load `feedback_master_lessons.md` if exists. Other memory files just-in-time.

## AUTO-UPDATE (MANDATORY, SILENT)
After ANY substantive work: update `SESSION_LOG.md` + `PRIORITIES.md` (if status changed). Pre-approved. Just do it.

## ENGINEERING
- Plan first for 3+ step tasks. Build incrementally. Subagents for isolated tasks.
- "Launch all agents" = Architect > Engineer > Reviewer > Optimizer > Verify.
- Supabase public: anon SELECT, raw fetch(), never getSession() first.

## SKILL TRIGGERS
- Deploy = `/pre-deploy` | Research = Perplexity + NotebookLM (BOTH always)
- Blog/marketing = `/blog` or `/marketing` | Decision = `/council` | Brain = `/fix-brain`
- 3+ file change = all 4 agents | Bug failed 2x = Plan agent | New idea mid-task = "Now or later?"

## SELF-IMPROVEMENT
- After corrections: save `feedback_*.md` AND update relevant SKILL.md.
- Corrections apply to ALL workspaces.
- Use plain text file references, NOT @imports (@imports embed the whole file every run).

## UNIVERSAL RULES
- ALWAYS Safari. Memory-first (read before writing code).
- Never use em dashes (enforced via hook).
- Research = Perplexity THEN NotebookLM. No exceptions.

<!-- COMPACTION STANDING ORDERS -->
## WHEN COMPACTING
Preserve: modified files, user corrections this session, current task status, architectural decisions.

<!-- CRITICAL REPEATED AT END -->
## REMEMBER
- 4 failure patterns above are NON-NEGOTIABLE.
- Never skip deploy gate, visual gate, or NotebookLM. No em dashes.
- ASK, don't invent. Behavioral claims need evidence.
- Update SESSION_LOG + PRIORITIES silently after every task.
- THINK END-TO-END before declaring done. Lead with caveats, not ideal state.
