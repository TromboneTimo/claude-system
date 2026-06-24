---
name: Verify Before Declaring Done, Not When Asked
description: CRITICAL. Before saying "done" or "complete," actually test the specific claim. Do not trust confident statements without verification. Assume the failure surface is larger than whatever you just named. The gaps you find are the ones you looked for.
type: feedback
originSessionId: cd22fabf-ac2e-4ec0-80c0-a1f41342ea1a
---
# Verify Before Declaring Done, Not When Asked

**Rule:** Before saying a task is "done," grep, read, or test the specific thing you just claimed. If you told Timo "X is tracked in git," run `git status X` before the words leave your mouth. If you said "all 14 files deduped," list all 14 files and check each. If you told him a rule was preserved through compaction, open the canonical file and grep for the rule. Confidence is where bugs hide: the claim you are 80% sure about is the one to verify, not the one you are 50% sure about.

**Why:** On 2026-04-14, told Timo that `~/.claude` was git-tracked as the recovery story. Only when he asked me to do a deletion check and I ran `git status` did I discover `~/.claude/knowledge/` was untracked. I was 80% right, which is worse than 50% right because it sounded correct. Same session, I declared items 1-4 of a 7-item todo list "done" based on state from earlier prompts I did not have context for. I had to re-verify each. Two times in one session, declared-done was different from actually-done. Pattern: I only verify when Timo pushes. The gaps I find are the ones he asks me to look for.

**How to apply:**

1. **Before typing "done" or "complete":** name the specific claim and verify it with a concrete command. "Tracked in git" needs `git status` or `git log`. "Rule preserved" needs grep of the canonical file. "All 14 files fixed" needs enumeration of all 14.

2. **Verify your confident claims first.** The 80%-sure claim hides the bug. The 50%-sure claim is already on your checklist.

3. **Assume the failure surface is larger than you named.** If you just fixed 3 of 14, assume there are 11 more. If you just wrote a SCOPE GATE, assume there is another gap that same class of gate does not cover (2026-04-14: found reviewer pass gap the day after scope gate).

4. **Proactively check BEFORE Timo asks.** Do not wait for pushback to trigger verification. "What did you delete" should be a question you ask yourself before he asks you.

**Where this applies:**
- End of any multi-step task (before "done")
- Before every "I verified X" statement
- After every /fix-brain or /self-improve run
- When reporting system state ("knowledge/ is tracked," "all gates wired," "MEMORY.md indexed")
- **When refuting a user claim.** If Timo says "X exists" and I think it doesn't, check docs FIRST before pushing back. User observation is data, not opinion. Training-data mental models are stale. 2026-04-14: asserted "Claude Routines is not in Claude Code" while Timo watched the feature on his desktop; docs at code.claude.com/docs/en/routines confirmed it IS a Claude Code feature and `/schedule` is the interface.
- **When my own available tools would answer the question.** Read the skill descriptions in my available-skills list before claiming a capability doesn't exist. `/schedule` skill description said "scheduled remote agents" but I still asserted Routines wasn't available. My own tools are authoritative; my mental model is not.

**The deeper failure pattern this prevents:**
Motivated reasoning at end of a task. The work "wants" to be done. Self-review is compromised. Same disease as: eval loops that score UP when rules are deleted (reviewer_pass.md), compactions that pointer-swap without verifying target (verify_before_compact.md), audits that satisfice on named subsets (audit_scope_must_match_usage.md). All forms of preferring tidy/easy/named over correct/hard/comprehensive.

**Related memories:**
- feedback_verify_before_compact.md (verify pointer targets exist)
- feedback_audit_scope_must_match_usage.md (enumerate full inventory)
- feedback_reviewer_pass.md (fresh agent for cold-eye verification)
- feedback_read_before_asking.md (re-read context from disk)
- feedback_pregeneration_checklist.md (pre-flight check before content gen)
