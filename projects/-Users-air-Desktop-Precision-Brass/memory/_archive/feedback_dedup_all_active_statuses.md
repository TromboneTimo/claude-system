---
name: dedup-all-active-statuses
description: When pushing revised drafts to a queue with status lifecycle, dedup must cover ALL active statuses, not just the "incoming" status. Pushing v2 to proposal_pending without superseding the v1 in changes leaves both visible. Caught 2026-05-09 when Harrison saw 6 email entries when there should have been 3.
type: feedback
originSessionId: e058534c-234c-434c-872f-b6cbfc8ff00d
---
# Dedup must cover all active statuses, not just the entry status

**Rule:** Any skill that writes into a queue with a status lifecycle (e.g. `email_proposals`: `proposal_pending` → `changes` → `approved` → `sent`) must dedup against ALL active statuses, not just the entry one. When a v2 revision matches an existing entry in a non-entry status (like `changes`), AUTO-SUPERSEDE the old entry as part of the push.

**Why:** On 2026-05-09 I pushed 3 v2 emails to `proposal_pending` after Harrison asked for changes on the v1 versions. The pb-email-push skill only checked `status=proposal_pending` for dedup. The 3 v1 entries lived in `status=changes`. Net effect: 6 entries on Harrison's dashboard (3 in Needs Changes tab + 3 in Pending Review tab) when there should have been 3. Timo was rightfully pissed.

**How to apply:**
- Dedup query: `?status=in.(proposal_pending,changes,approved,approved-pending-send)`
- For each match found:
  - `status=proposal_pending` + match: silently skip per existing dup-skip rule
  - `status=changes` + match: AUTO-SUPERSEDE the old (PATCH `status=superseded`, append history entry pointing at new id), then push the new
  - `status=approved` or `approved-pending-send` + match: STOP and surface to Timo. May be already scheduled in AC; silent supersede could break a campaign mid-flight
- Always run a post-push verification step that re-queries and confirms the expected end-state (count delta, no orphaned old rows in `changes`, all new rows in `proposal_pending`)

**Files updated 2026-05-09:**
- `~/.claude/skills/pb-email-push/SKILL.md` (dedup section, supersede flow in Step 4, new Step 4b verification, failure modes 6-8)

**Generalizes to:**
- Any queue-style table with multi-stage lifecycle (ideas, scripts, tasks, leads, proposals)
- Any push/insert skill that targets one status but should respect the broader pipeline

**Related rule:** `feedback_skip_dups_silently.md` (silent skip for true within-status dups). The status=changes case is NOT a dup, it's a revision, so the silent-skip rule doesn't apply.
