# System Maintenance Meta-Rules

**Canonical meta-rules governing how Claude maintains the skill/memory/gate system itself.**

These apply across ALL workspaces (creator-conservatory, robinsons-remedies, precision-brass, any future). Loaded from global CLAUDE.md so they fire regardless of which workspace is active. Workspace-specific origin stories and examples live in each workspace's `memory/feedback_*.md` files.

## Four Rules

### 1. Verify Before Declaring Done
Before saying "done" or "complete," test the specific claim with a concrete command. The claim you are 80% sure about is where the bug hides, not the claim you are 50% sure about. Do not wait for pushback to trigger verification. If you said "X is tracked in git," run `git status X`. If you said "all 14 files fixed," enumerate all 14. If you said "the rule was preserved," grep the canonical file for the rule.

**Failure this prevents:** Declared-done differs from actually-done. Motivated reasoning at task boundaries makes self-review unreliable.

### 2. Match Rule To Enforcement Layer
Rules without enforcement mechanisms are aspirations. Pick the layer that matches the rule's nature:

- **Mechanical patterns** (em dashes, banned phrases, regex-detectable content): hook in `~/.claude/hooks/`
- **Pre-action checks** (before generating, before compacting, before declaring done): gate in `~/.claude/CLAUDE.md`
- **Post-action review** (was anything silently deleted, does output match claim): subagent with protocol file
- **Skill-specific domain rules** (n8n syntax, blog SEO): inline in that SKILL.md
- **Cross-cutting rules** (2+ skills reference): canonical in `~/.claude/knowledge/`, referenced in 1-2 lines

Start with prose. If the rule keeps failing, escalate to a gate. If the gate keeps failing, escalate to a hook. Do not engineer prematurely, but do not hide behind prose when the pattern is clearly mechanical.

**Failure this prevents:** Writing a rule in prose feels like progress but is a note-to-self the note-writer will ignore.

### 3. YAGNI For New Agents And Skills
Before building a new subagent, skill, or orchestrator, grep existing tooling. `/fix-brain` is the system orchestrator. `/self-improve` is the per-skill loop. `/weekly-review` is cross-workspace. general-purpose handles most research. Build new entities only after 5+ instances of sustained friction the existing tools cannot address. "Canonical librarian," "memory gardener," "skill creator" are theater unless there is a concrete incident log showing the need.

**Failure this prevents:** Over-engineering temptation. Every new artifact is forever-maintenance.

### 4. Audit State Before Prescribing Action
Before proposing a fix or remediation workflow for a reported problem, audit the actual state. Test the assumption that defines the problem: for leaked credentials, curl the API; for "feature does not exist," fetch docs AND check available tools/skills; for "broken X," run X and read the actual error. Check alternative success paths (parallel auth, fallbacks, caches). Present findings first, solution second. Companion to verify-before-done: that rule covers output-side verification, this covers input-side.

**Failure this prevents:** Leaping from "problem reported" to "here is the fix workflow" creates busywork when the problem has already resolved (auto-revoked credential, parallel auth path working silently) or exists in a different shape than assumed.

### 5. Gates Come From Fuckups, Not Architecture
Every gate in CLAUDE.md, every canonical rule in `knowledge/`, and every feedback file traces to a specific incident. Do not invent gates from abstract reasoning. Do not delete gates because they seem redundant. The burden of proof for deletion is on the deleter: name the incident the gate prevents recurrence of. If you cannot find the incident, the gate is still probably load-bearing.

Corollary: Timo's pushback is diagnostic, not resistance. "What about X?" either surfaces a new incident (which produces the next gate) or confirms an existing gate covered it.

**Failure this prevents:** Treating the rule system as architecture to be optimized for elegance. It is a scar log, not architecture.

## Scope

These meta-rules govern:
- Writing any new feedback_*.md
- Adding or removing gates in CLAUDE.md
- Promoting rules to `~/.claude/knowledge/`
- Creating new skills, subagents, scripts, or hooks
- Running /fix-brain, /self-improve, /weekly-review
- End-of-task "done" declarations

## Workspace Origin Files

Each rule has a workspace feedback file with specific incident context:
- Rule 1: `feedback_verify_before_done.md`
- Rule 2: `feedback_enforcement_mechanism_choice.md`
- Rule 3: `feedback_yagni_new_agents.md`
- Rule 4: `feedback_gates_come_from_fuckups.md`

Currently in creator-conservatory workspace memory. The canonical version here is the cross-workspace reference.

## The Meta-Principle

The goal is not "all possible failures prevented." The goal is "no failure happens twice." Each incident produces one gate. Each gate prevents one specific recurrence. The system ratchets forward, it does not arrive.
