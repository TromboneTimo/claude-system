# Global Claude Code Guidelines

<!-- CRITICAL RULES AT TOP — "lost in the middle" fix: Claude pays most attention to START and END -->

## 3 FAILURE PATTERNS — HARD-WON, NEVER TRIM
1. Shared hooks break everything. After modifying shared state: test ALL features, not just the one changed.
2. Same bug 3x = check the DATABASE (RLS, policies), not the code. (14 failed code fixes, 1 RLS policy fixed it.)
3. Verify in BROWSER (Safari), not curl. Stale tokens fool curl. Use raw fetch() for smoke tests.

## 2-STRIKE RULE
Same bug twice = STOP coding. Check the database. Don't iterate on code fixes.

## DEPLOY GATE (NEVER SKIP)
Build > QA Agent > API curl > Safari browser verify. All 4 steps. Every time.

## BOOT SEQUENCE
Read in order: `SOUL.md` > `PRIORITIES.md` > `SESSION_LOG.md` > project `memory/MEMORY.md`. Load `feedback_master_lessons.md` if it exists. Other memory files just-in-time only.

## AUTO-UPDATE (MANDATORY, SILENT, NEVER ASK)
After ANY substantive work, update `SESSION_LOG.md` (bullets + decisions) and `PRIORITIES.md` (if status changed). Pre-approved in settings.json. Just do it.

## ENGINEERING
- Plan first for 3+ step tasks. Build incrementally (scaffold > run > add > run).
- Subagents for isolated tasks. Main context = orchestration only.
- "Launch all agents" = ALL 4: Architect > Engineer > Reviewer > Optimizer > Verify.

## SUPABASE
- Public data: anon SELECT. Expired JWTs override anon.
- NEVER getSession() before public data. Use raw fetch().

## SKILL TRIGGERS
| Context | Skill |
|---|---|
| Deploy | `/pre-deploy` |
| Research | Perplexity (`llm -m sonar-pro`) > NotebookLM. ALWAYS both. Never skip NotebookLM. |
| Blog/marketing | `/blog` or `/marketing` |
| Decision | `/council` |
| 3+ file change | All 4 agents |
| Bug failed 2x | Plan agent (stop, diagnose root cause) |
| New idea mid-task | "Now thing or later thing?" |
| "Fix your brain" | Run `/self-improve` on all skills with evals + `/weekly-review` + optimize any bloated files |

## SELF-IMPROVEMENT
- After corrections: save `feedback_*.md` AND update relevant SKILL.md.
- Corrections apply to ALL workspaces, not just current one.
- `/self-improve [skill]` runs Karpathy eval loop. `/weekly-review` cross-pollinates.
- When loading context, use plain text references ("first read docs/file.md") not @imports. @imports embed the entire file on every run.

## UNIVERSAL RULES
- ALWAYS Safari. Memory-first (read before writing code).
- Never use em dashes in any output (enforced via hook for 100% compliance).
- Research pipeline = Perplexity THEN NotebookLM. No exceptions. No "seems clear enough."

<!-- COMPACTION STANDING ORDERS — preserves critical info when context auto-compacts -->
## WHEN COMPACTING
When auto-compaction occurs, ALWAYS preserve:
- The full list of modified files in this session
- All user corrections and feedback given this session
- Current task status and next steps
- Any decisions made that affect architecture or priorities

<!-- CRITICAL RULES REPEATED AT END — "lost in the middle" fix -->
## REMEMBER
- 3 failure patterns above are NON-NEGOTIABLE. They came from real production bugs.
- Never skip the deploy gate. Never skip NotebookLM in research. Never use em dashes.
- Update SESSION_LOG.md and PRIORITIES.md silently after every task.
- THINK END-TO-END before declaring anything done. Trace the full chain. If any link is broken, fix it first. Don't present ideal state as current state. Lead with caveats.
