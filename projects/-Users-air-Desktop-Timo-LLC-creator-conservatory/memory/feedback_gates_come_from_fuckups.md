---
name: Gates Come From Fuckups, Not Architecture
description: META RULE. Every gate/rule/canonical file in the system traces to a specific incident where Claude failed Timo. Do not invent gates from abstract principles. Do not delete gates because they seem redundant. Each gate is a scar from a real failure and deletion risks recurrence.
type: feedback
originSessionId: cd22fabf-ac2e-4ec0-80c0-a1f41342ea1a
---
# Gates Come From Fuckups, Not Architecture

**Rule:** Every gate in CLAUDE.md, every canonical rule in `~/.claude/knowledge/`, and every feedback_*.md file traces to a specific incident where Claude failed Timo. Do not invent new gates from abstract reasoning. Do not delete gates because they feel redundant or overlap with another gate. Each rule is a scar from a real failure and deletion risks recurrence of that exact failure mode.

**Why:** On 2026-04-14, in reflection: every gate Timo and I built this session or previously traces to a specific fuckup.
- VISUAL GATE: 2026-04-12 PDF proposal card split across page break
- CONTENT VERIFICATION GATE: 2026-04-12 Otto proposal fabrication "you already do those conversations weekly"
- COMPACTION GATE: 2026-04-13 /fix-brain near-miss weakening 8-item slide pre-check
- SCOPE GATE: 2026-04-14 /fix-brain deduped 3 of 14 skills with same bloat
- SKILL ARCHITECTURE GATE: 2026-04-14 Perplexity research + 14-skill dedup event
- Reviewer Pass: 2026-04-14 Timo's question "without deleting important information"

None of these were invented from first principles. All came from a specific moment where I failed. The gates work because they encode the specific failure pattern, not abstract quality standards.

**How to apply:**

1. **When tempted to add a new gate from reasoning ("we should have a gate for X"), stop.** Ask: what incident is this gate preventing recurrence of? If there is no incident, there is no gate. File the idea as a watch item, not a gate.

2. **When tempted to delete a gate because it seems redundant, stop.** Ask: which incident would this gate's deletion permit to recur? If you can name the incident, the gate stays. If you cannot find it in the feedback files or git log, the gate is still probably load-bearing. The burden of proof is on deletion.

3. **When adding a gate, cite the incident.** In the "Why" section of the feedback file and in the gate's line in CLAUDE.md, name the date and the failure. "Origin: 2026-04-14 fix-brain deduped 3 of 14..." This is load-bearing documentation. Future-Claude needs to know why the gate exists or future-Claude will delete it.

4. **Expect the next gate is coming from the next fuckup.** The system is not done. It is not designed for completeness. It is designed to ratchet: each incident produces a gate, each gate prevents one specific recurrence. The goal is not "all possible failures prevented" but "no failure happens twice."

**Where this applies:**
- Adding or removing gates in CLAUDE.md
- Promoting rules to canonical in `~/.claude/knowledge/`
- Auditing feedback files during /fix-brain
- Evaluating proposals for new subagents, skills, or hooks
- Any moment of "we could simplify by removing X"

**The deeper failure pattern this prevents:**
Treating the rule system as architecture to be optimized for elegance. The system is a scar log, not an architecture. Elegance is the wrong metric. The right metric is: does every past incident have a corresponding gate, and does every gate have a traceable incident?

**The corollary:**
Because gates trace to incidents, Timo's pushback is load-bearing. When he says "what about Y?" the question itself is diagnostic: either it surfaces a new incident (which produces the next gate) or it confirms an existing gate covered it. I should welcome pushback, not resist it.

**Related memories:**
- feedback_verify_before_done.md (verify claims before declaring done)
- feedback_enforcement_mechanism_choice.md (pick the right enforcement layer)
- feedback_audit_scope_must_match_usage.md (scope gate origin)
- feedback_reviewer_pass.md (reviewer pass origin)
- feedback_skill_architecture.md (skill architecture gate origin)
- feedback_master_lessons.md (master lessons aggregate)
