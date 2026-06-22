---
name: pb-hook-design
description: Phase 1.6 of Harrisson Ball's Precision Brass YouTube content engine. Sits between Harrisson approving an idea on the dashboard (status=idea_approved) and pb-script-write expanding it into a full script. Takes an approved idea, fans out 4 parallel agents to rank a 40-video corpus of Antoine Morales (top YouTube violin teacher, ~25K subs, same adult-learner ICP) by hook quality on a 6-criterion rubric, semantically matches the best Antoine hook pattern + body structure to THIS specific idea, drafts the hook in Antoine's exact cadence translated to trumpet, presents top 3 hook options in chat for Timo's pick, then writes a locked hook + 6-beat structure brief to voc/scripts/in-progress/<idea_id>/hook-brief.md that pb-script-write consumes as its Step 0. Required step before pb-script-write. Use whenever Timo says "design the hook for idea N", "harrisson approved [X], let's design the structure", "prep the hook for [X]", "match an antoine pattern for [idea]", "/pb-hook-design", or any variant that signals an approved idea needs a hook before scripting. NEVER skip in favor of going straight to pb-script-write. NEVER invent hook copy from scratch when an Antoine pattern can be cloned. The corpus, rubric, and patterns are pre-built; the skill orchestrates the matching and drafting.
---

# pb-hook-design. Phase 1.6: Hook + Structure Brief

## When to fire

- Explicit: `/pb-hook-design <idea_id>` or `/pb-hook-design` (defaults to latest idea_approved without a brief).
- Natural language: "design the hook for idea N", "let's prep the structure for [X]", "match an antoine pattern for [X]", "harrisson approved [X], next step", "hook design".
- ALSO fires whenever someone tries to run pb-script-write on an idea that has no brief on disk. pb-script-write itself stops and tells Timo to run this skill first.

## Hard preconditions

1. **Antoine corpus exists** at `/Users/air/Desktop/Precision-Brass/voc/inspiration/antoine-morales-violin/raw/_all40.json` with view counts, comment depth signals, and verbatim first-30s per video. If missing, stop and tell Timo to re-run the corpus build.
2. **Idea exists in Supabase** with `status=idea_approved`. If status is `idea_pending`, tell Timo Harrisson hasn't approved it yet. If no row, tell Timo to run pb-script + pb-ideas-push.
3. **References loaded** before any agent spawn:
   - `references/hook-rubric.md`. The 6-criterion scoring spec (curiosity, specificity, authority, pacing, engagement, semantic-match).
   - `references/hook-patterns.md`. The 4 opener patterns (stat-shock, story cold-open, empathy disarm, Good morning) and when to pick which based on the idea's emotional register.
   - `references/structure-templates.md`. The 6-beat body shapes from the top 3 Antoine winners (PcsnUkruHks, J0OdaOyrS1c, KBT0roUguhc).

## Workflow

### Step 0. Resolve the idea

If Timo named an idea by id or title, load that row. Otherwise query the `ideas` table for the most recent `status=idea_approved` row that does NOT already have a brief at `voc/scripts/in-progress/<id>/hook-brief.md`. If multiple candidates, list them in chat and ask Timo to pick. If zero candidates, stop and tell Timo there's nothing to design.

Echo back the idea details (title, hook angle, pain point, named techniques in the rationale) for confirmation in one tight paragraph.

### Step 1. Fan out 4 parallel ranking agents (single message, four Agent calls)

Split the 40-video corpus round-robin into 4 batches of 10 and write to `/tmp/antoine_batch_1.json` through `_4.json`. Each agent is general-purpose, reads its batch file, and scores every video on the 6 criteria in `references/hook-rubric.md`. Each returns RAW JSON: per-video scores + the agent's top 3 picks from its batch with a 2-sentence justification grounded in verbatim first-30s phrasing and specific comment metrics.

The 6th criterion (semantic-match) injects THIS idea's pain + named techniques into each agent's prompt so they can judge transferability, not just hook quality in the abstract.

### Step 2. Merge + propose top 3 hooks in chat

Aggregate scores across all 4 batches. Take the top 3 by total. For EACH of the 3:

- Antoine video id, title, score breakdown
- Verbatim Antoine first 30s (quoted)
- Drafted Harrisson hook: clones the Antoine cadence beat-for-beat, swaps in Harrisson's named techniques (amisha, vertical alignment, dynamic repetition, gravity breath, 4 points of contact, upstream/downstream, place-breathe-play, wedge breath. See `[[feedback-lead-with-technique-not-diagnosis]]`)
- Word count match (Antoine 30s = ~80 words; the Harrisson draft must be within ~10% or it's bloated)
- 1-line reason this pattern fits THIS specific idea

Show all 3 in chat as plain markdown. **Chat-draft-before-render.** Nothing gets written to disk yet.

### Step 3. Wait for Timo to pick or iterate

Timo picks one ("go with #2"), asks for a revision ("redraft #1 with X tweak"), or rejects all 3 ("try again, none of these land"). Keep iterating until Timo approves a specific hook draft. Do NOT proceed to Step 4 without an explicit approval.

### Step 4. Draft the 6-beat body structure

Once the hook is locked, draft the body structure using the chosen Antoine reference's body shape (per `references/structure-templates.md`). Each beat gets:

- Timestamp range
- Beat purpose (in 1 line)
- Named technique anchored in this beat (from the idea's rationale)
- Visual plan in 1 line (what Harrisson demonstrates, what the viewer sees)
- 1-2 VOC quotes from the idea that ground this beat

Show in chat for Timo's approval before writing the brief.

### Step 5. Write the brief

Save to `/Users/air/Desktop/Precision-Brass/voc/scripts/in-progress/<idea_id>/hook-brief.md` with frontmatter and these sections:

```
---
idea_id: <id>
title: <title>
antoine_ref: <video_id>
antoine_score: <total>/60
designed_at: <ISO date>
status: ready_for_script
---

# Hook brief: <title>

## Antoine reference
- Video: <title> (<id>)
- Score: <total>/60 (curiosity X, specificity X, authority X, pacing X, engagement X, semantic-match X)
- Why this pattern fits: <2 sentences>
- Antoine verbatim first 30s: <quote>

## Locked hook (verbatim, ready for pb-script-write)
<the approved hook copy>

## 6-beat body structure
1. <Hook> ...
2. ...
6. <CTA>

## Named techniques per beat
- Beat 3: <technique>
- ...

## VOC quote evidence (from the idea row)
- ...
```

Create the directory if it doesn't exist.

### Step 6. Hand off

Tell Timo:

> "Hook brief ready at `voc/scripts/in-progress/<idea_id>/hook-brief.md`. Run `/pb-script-write <idea_id>` to expand into the full filming script."

## What this skill does NOT do

- Write the full script. That is pb-script-write's job.
- Push anything to the dashboard. The brief is file-only by design (see Timo decision 2026-06-01).
- Refresh the Antoine corpus. That is a separate manual operation. The skill uses whatever snapshot is at `_all40.json` right now.
- Invent hook copy without an Antoine pattern anchor. Every hook draft MUST clone an Antoine pattern from the corpus.

## Failure modes (NON-NEGOTIABLE, caught across sessions)

These rules were each Timo-corrected during iterative drafting sessions. Repeating them costs trust.

### Hook construction (pb-hook-design)

1. **Hard word budget: 80-90 words for 30 seconds.** Anything over is bloat. Cut to the bone before showing in chat.

2. **Lead order is fixed.** Stat-shock (false belief) → CONSEQUENCE BEAT (3 specific stacked pains) → authority anchor → system tease → gatekeeping. The consequence beat is mandatory between stat-shock and authority. Without it the pain is abstract.

3. **NEVER name the proprietary system in the hook.** Use "a system" or "the secret method". The naming reveal happens in the body, not the opening 30 seconds. Naming the system in the hook kills curiosity.

4. **NEVER describe the system mechanics in the hook either** if the name is non-obvious (like Vertical Alignment System). Just say "a system". Describing the parts in the hook is the same mistake as naming it.

5. **Authority anchor adjustment for under-30 creators.** Drop "X years playing." Use "After teaching hundreds of [specific subgroup]" instead. Student count, not tenure.

6. **Dream outcome stack belongs in the authority slot, not separate.** Pattern: "I built a system that gives my students [outcome 1], [outcome 2], and [outcome 3]." Three stacked outcomes, one sentence.

See ~/.claude/skills/pb-script-write/SKILL.md for the Script structure rules that apply during pb-script-write.
