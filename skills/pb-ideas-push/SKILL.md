---
name: pb-ideas-push
description: Phase 1.5 of Harrison Ball's Precision Brass YouTube content engine. Pushes Timo-approved video ideas from the pb-script chat conversation into the Supabase-backed dashboard so Harrison can review them at dashboard/scripts.html. Takes the ideas Timo greenlit (e.g. "push idea 2 and 4 to the dashboard", "send these to harrison", "upload the chops idea") and inserts them into the ideas table with status=idea_pending. Each idea includes title, pain point, hook angle, 1-paragraph rationale, VOC quote evidence, and source tags. After Harrison greenlights an idea on the dashboard, Timo runs pb-script-write on the approved idea ID. Use this skill any time Timo says "push to dashboard", "send to harrison", "upload these ideas", "queue these for harrison", "/pb-ideas-push", or after a pb-script run when Timo picks 1+ ideas to send for review.
---

# pb-ideas-push. Phase 1.5: Push Ideas to Harrison's Dashboard

## What this does

Bridges `pb-script` (Phase 1, brainstorm in chat) and `pb-script-write` (Phase 2, full filming script). Pushes Timo-approved ideas into the Supabase `ideas` table so Harrison sees them on `Precision-Brass/dashboard/scripts.html` in the "Ideas Pending" column.

Harrison greenlights → idea moves to "Ideas Approved" → Timo runs `pb-script-write` → full script lands in "Script Pending".

## When to fire

Trigger when Timo says (after a `pb-script` run):
- "push idea 2 to the dashboard"
- "send ideas 1 and 3 to harrison"
- "upload these"
- "queue these for harrison's review"
- "/pb-ideas-push"
- "ship the chops one to the dashboard"

Do NOT fire if Timo has not yet seen ideas in chat. Run `pb-script` first.

## Inputs

From the conversation context (the prior `pb-script` output), pull for each greenlit idea:

| Field        | Source                                          | Required |
|--------------|-------------------------------------------------|----------|
| title        | The idea title from the menu                    | yes      |
| pain_point   | The pain/identity tension named in the idea     | yes      |
| hook_angle   | identity / failed-method / specific-result / curiosity / money | yes |
| rationale    | 1 paragraph: why this video, what VOC backs it  | yes      |
| voc_quotes   | array of `{text, source}` from the idea's evidence | yes  |
| source_tags  | which corpus the idea came from                 | yes      |

If any required field is missing from the chat output, ask Timo to fill it in before pushing. Never invent VOC quotes (4 failure patterns: prospects ≠ customers, auto-transcripts lie).

## Workflow

### Step 1. Confirm what to push

If Timo says "push 2 and 4", read back the titles and confirm:
> "Pushing these 2 ideas to Harrison's dashboard:
> 1. {title 1}
> 2. {title 2}
> Confirm? (y to push, or tell me what to change)"

Only proceed on explicit confirmation.

### Step 2. Load Supabase config

Read `/Users/air/Desktop/Precision-Brass/dashboard/lib/config.js`. If the file does not exist or still contains the placeholder `YOUR-PROJECT-REF`, STOP and tell Timo:
> "Supabase isn't configured yet. Open dashboard/setup/README.md and run the 3-step setup (~5 min), then come back."

### Step 3. Build idea IDs

Generate stable IDs in the format: `i_{YYYYMMDD}_{slug}` where slug = first 3-4 words of the title, lowercased, hyphenated. Example: `i_20260426_chops_recovery_protocol`.

If an idea with that ID already exists in the table, append `_v2`, `_v3`, etc.

### Step 4. POST to Supabase

For each greenlit idea, run a Bash curl POST to the Supabase REST API:

```bash
SUPABASE_URL="$(grep SUPABASE_URL /Users/air/Desktop/Precision-Brass/dashboard/lib/config.js | cut -d\' -f2)"
SUPABASE_KEY="$(grep SUPABASE_ANON_KEY /Users/air/Desktop/Precision-Brass/dashboard/lib/config.js | cut -d\' -f2)"

curl -X POST "${SUPABASE_URL}/rest/v1/ideas" \
  -H "apikey: ${SUPABASE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_KEY}" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=representation" \
  -d '{
    "id": "i_20260426_chops_recovery",
    "title": "The 7-day chops recovery protocol",
    "pain_point": "Comeback players over 50 with damaged embouchure",
    "hook_angle": "specific-result",
    "rationale": "VOC repeatedly cites...",
    "voc_quotes": [{"text":"I lost 9 months...", "source":"Fathom call 2026-03-12"}],
    "source_tags": ["fb-winners","fathom","lost-deals"],
    "status": "idea_pending",
    "history": [{"type":"delivered","who":"Timo","text":"<b>Pushed</b> from pb-script","time":"2026-04-26 20:30"}]
  }'
```

Use heredoc-style JSON, never shell-escape complex strings. Use `python3 -c` to JSON-encode if quotes get hairy.

### Step 5. Confirm + open dashboard

After all POSTs return 201:
> "✓ Pushed N ideas to the dashboard.
> Harrison can review them at: dashboard/scripts.html (Ideas Pending column).
> Want me to open it?"

If Timo says yes, run `open -a Safari /Users/air/Desktop/Precision-Brass/dashboard/scripts.html`.

### Step 6. Log to PRIORITIES.md (silent)

Add a one-liner to `~/.claude/projects/-Users-air-Desktop-Precision-Brass/SESSION_LOG.md`:
> "Pushed N ideas to Harrison dashboard: [titles]. Awaiting greenlight."

## Failure modes to avoid

1. **Inventing VOC quotes.** Every quote must trace back to a real file in `voc/` or a Fathom transcript Timo shared in chat. If you don't have it, ask. Never paraphrase a quote and pass it as verbatim.
2. **Pushing ideas Timo didn't pick.** Only push the ones Timo explicitly named. If Timo says "push the good ones", ASK which numbers.
3. **Silent failures.** If curl returns 4xx/5xx, surface the full error to Timo. Don't pretend it worked.
4. **Skipping the greenlight wait.** Do NOT auto-run `pb-script-write` after pushing. Harrison has to greenlight first on the dashboard.

## What this skill does NOT do

- Does not generate ideas (that's `pb-script`)
- Does not write the full filming script (that's `pb-script-write`)
- Does not approve ideas on Harrison's behalf (Harrison clicks the button)
- Does not push without Timo's explicit confirmation
