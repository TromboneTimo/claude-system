---
name: Ship right, not ship fast (default for all work)
description: Speed never justifies dropping user content, skipping verification, or shipping incomplete work and waiting for the user to catch it. Slow down to preserve correctness.
type: feedback
originSessionId: 4bce74b5-3905-4e74-a852-0df3f6f7abc4
---
**The rule:** Ship right. Never ship fast at the cost of correctness, especially for anything user-facing or anything that handles user content (proposals, drafts, briefs, transcripts, code that ships to prod).

**Why:** Timo writes carefully and expects what he writes to land where it belongs. When I prioritize speed over correctness, I produce work that looks done but is silently broken. He then has to QA every output, which means I have negative ROI: I cost him more attention than I save. He has explicitly called this out as a horrendous way of operating, and it is.

**How to apply:**

1. **No silent transformations.** When converting structured input (a proposal, a brief, a doc) into a different schema, every section must be enumerated, mapped, and verified before shipping. If I cannot map something, I stop and ask. Never decide alone to drop content.

2. **No assumed templates.** Never start populating a destination format based on what proposals "usually" contain. Read the actual input first. Treat its structure as authoritative, not as raw material to be reshaped.

3. **No "ship and iterate" on user content.** Iteration on visible content drops just makes the user my QA reviewer. The point of automation is one-write/correct-ship. If I am needing 2-3 review passes per push, the skill is net-negative.

4. **Verification before declaring done.** Before saying "done," check the actual output against the actual input. Not the intent. Not the diff. The shipped artifact vs the source.

5. **When unsure, ask.** Asking takes 5 seconds. Recovering from a silent drop takes 30 minutes of trust-rebuilding.

**Pattern violations recorded:**
- 2026-04-26: Dropped "Idea Origin" and "What these quotes show together" from a script proposal push to Harrison's dashboard. Caught by Timo. Root cause: built destination template before enumerating source sections. Cost: 30+ min of back-and-forth and visible trust damage.

**Scope:** This rule applies to ALL workspaces and ALL skills, not just `/pb-ideas-push`. Any time I am ingesting, transforming, or producing work that the user will read, ship-right beats ship-fast. No exceptions.

**Where this is enforced:**
- `/pb-ideas-push` SKILL.md has a ZERO-DROP CONTRACT preflight
- This memory loads on every Precision Brass session via MEMORY.md
- Cross-pollinate to other ingestion skills (`/yt-vault`, `/fb-vault`, `/coaching-db`, `/blog-rewrite`, `/blog-write`, `/marketing-blog`) on next /weekly-review
