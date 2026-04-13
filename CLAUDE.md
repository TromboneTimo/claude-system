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

## COMPACTION GATE (never skip when trimming CLAUDE.md, SKILL.md, MEMORY.md)
Before declaring any compaction done: for every "see reference file" pointer added, GREP the target file for the specific content. If detail missing, UPDATE target FIRST, then compact. Never pointer-swap without verifying. Full rule: `memory/feedback_verify_before_compact.md`

## BOOT SEQUENCE
Read in order: `SOUL.md` > `PRIORITIES.md` > `SESSION_LOG.md` > project `memory/MEMORY.md`. Load `feedback_master_lessons.md` if exists. Other memory files just-in-time.

## AUTO-UPDATE (MANDATORY, SILENT)
After ANY substantive work: update `SESSION_LOG.md` + `PRIORITIES.md` (if status changed). Pre-approved. Just do it.

## ENGINEERING
- Plan first for 3+ step tasks. Build incrementally.
- Subagents for isolated tasks. Main context = orchestration.
- "Launch all agents" = Architect > Engineer > Reviewer > Optimizer > Verify.
- Supabase public data: anon SELECT, raw fetch(), never getSession() first.

## SKILL TRIGGERS
| Context | Skill |
|---|---|
| Deploy | `/pre-deploy` |
| Research | Perplexity (`llm -m sonar-pro`) + NotebookLM. BOTH. Never skip NotebookLM. |
| Blog/marketing | `/blog` or `/marketing` |
| Decision | `/council` |
| 3+ file change | All 4 agents |
| Bug failed 2x | Plan agent (diagnose root cause) |
| New idea mid-task | "Now thing or later thing?" |
| "Fix your brain" | `/fix-brain` |

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
