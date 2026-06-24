---
name: YAGNI For New Agents And Skills
description: CRITICAL. Before building a new subagent, skill, or orchestrator, ask if an existing one already covers the use case. /fix-brain is already the orchestrator. Build new agents only after 5+ instances of sustained friction, not based on imagined future need.
type: feedback
originSessionId: cd22fabf-ac2e-4ec0-80c0-a1f41342ea1a
---
# YAGNI For New Agents And Skills

**Rule:** Before spawning a new subagent, skill, or meta-skill, grep for whether existing tooling already covers the use case. /fix-brain is the system orchestrator. /self-improve is the per-skill improvement loop. /weekly-review is cross-workspace. general-purpose subagent handles most research. Do not build canonical-librarian, memory-gardener, skill-creator, or similar "nice to have" agents until there are 5+ real instances of sustained friction that the existing tools cannot address.

**Why:** On 2026-04-14, while answering Timo's "what agents would make this more efficient," I listed canonical-librarian, memory-gardener, skill-creator as options. Then caught myself: those would be theater. /fix-brain step 1 already audits canonical files. /weekly-review already reviews cross-workspace memory. Creating new agents would add maintenance burden without incremental benefit. The only agent worth building was skill-reviewer, because it addressed a real gap (silent deletion not caught by binary evals). Every other proposed agent was YAGNI.

**How to apply (checklist before building anything new):**

1. **Grep existing tools.** `ls ~/.claude/skills/ ~/.claude/agents/` and read the descriptions. If something 70%-covers the use case, extend it rather than creating a new one.

2. **Count real incidents.** Has this friction come up 5+ times? Or am I imagining it will come up? Build for past pain, not future possibility.

3. **Ask what it replaces.** If a new agent does not reduce load on an existing agent or eliminate manual work, it is additive complexity.

4. **Prefer extension over creation.** Add a step to /fix-brain. Add a reference to an existing canonical. Add a hook. New top-level entities (skills, agents, scripts) carry maintenance cost forever.

5. **Orchestrator ban.** Do not build an "agent that coordinates other agents" unless /fix-brain actually fails at orchestration. It does not. It works.

**Where this applies:**
- "Should I build a new skill for X?" (usually no)
- "Should I build a new subagent?" (usually no, general-purpose is fine)
- "Should we add a meta-orchestrator?" (no, /fix-brain is it)
- New rules that feel like they need "a whole thing" (they usually need a file, not a thing)

**The deeper failure pattern this prevents:**
Over-engineering temptation. Building new scaffolding feels productive. It creates artifacts that look like progress. The actual signal of progress is reduced friction on real tasks, not number of agents/skills/scripts created. Every new artifact is forever-maintenance.

**When a new agent IS justified:**
- Existing tool has been tried 5+ times and repeatedly fails the same way
- The gap is structural (cannot be fixed by editing the existing tool)
- The new agent replaces rather than adds
- There is a specific incident log showing the need

**Example of justified creation:** skill-reviewer subagent (2026-04-14). Addressed the silent-deletion gap in binary-assertion eval loops. Not preventable by extending /self-improve because the need for fresh-eyes review is structurally different from within-loop testing. Tested immediately against 4 historical commits to prove value.

**Related memories:**
- feedback_easy_path_default.md (reach for simplest working option first)
- feedback_skill_architecture.md (cross-cutting rules to canonical, not new skills)
- feedback_gates_come_from_fuckups.md (new rules trace to incidents, not architecture)
