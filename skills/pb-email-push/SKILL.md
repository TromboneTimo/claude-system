---
name: pb-email-push
description: Phase 1.5 of Harrison Ball's Precision Brass email engine. Pushes Timo-approved email drafts from the pb-email chat conversation into the Supabase-backed dashboard so Harrison can review them at dashboard/emails.html. Takes the drafts Timo greenlit (e.g. "push 2 and 4 to the dashboard", "send these to harrison", "upload the dental-trigger one") and inserts them into the email_proposals table with status=proposal_pending. Each proposal includes subject + 2 alts, preheader, full body, P.S. text and type, hook angle, audience, CTA, rationale, VOC quotes, and source tags. After Harrison approves on the dashboard, the email is ready to send via ActiveCampaign (publish to AC is Phase 2). Use this skill any time Timo says "push to dashboard", "send to harrison", "upload these emails", "queue these for harrison", "/pb-email-push", or after a pb-email run when Timo picks 1+ drafts to send for review.
---

# pb-email-push. Phase 1.5: Push email drafts to Harrison's dashboard.

## OPERATING PRINCIPLE: Ship right, never ship fast.

This skill mirrors `pb-ideas-push` exactly. Timo's draft proposals are the source of truth. Every labeled section MUST appear on the dashboard. Silent omission is the highest-severity failure mode for this skill.

If tempted to "just push and we will iterate", STOP. Run the preflight enumeration. Asking Timo a clarifying question takes 5 seconds. Recovering from a silent drop takes 30 minutes of trust damage.

Stored in `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_ship_right_not_fast.md`.

## What this does

Bridges `pb-email` (5-draft menu in chat) and the dashboard at `dashboard/emails.html`. Pushes Timo-approved drafts into the Supabase `email_proposals` table with status `proposal_pending`.

Harrison approves on the dashboard. Email moves to `approved`. Then Timo (or the future AC publish step) sends it via ActiveCampaign.

## When to fire

Trigger when Timo says (after a `/pb-email` run):
- "push draft 2 to the dashboard"
- "send drafts 1 and 3 to harrison"
- "upload these emails"
- "queue these for harrison's review"
- "/pb-email-push"
- "ship the dental-trigger one"

Do NOT fire if Timo has not yet seen drafts in chat. Run `/pb-email` first.

## Schema mapping

The `email_proposals` table columns:

| Field | Source | Required |
|---|---|---|
| id | `e_{YYYYMMDD}_{slug}` from subject | yes |
| subject | The picked subject line | yes |
| subject_alts | Array of the 2 alts | yes |
| preheader | Preheader text | yes |
| body | Full email body | yes |
| ps_text | The actual P.S. line | yes |
| ps_type | scarcity / timing / urgency / social-pressure / risk-reversal | yes |
| hook_angle | identity / failed-method / specific-result / curiosity / money | yes |
| pain_point | 1 line | yes |
| audience | broadcast / reengagement / webinar-push / discovery-followup | yes |
| cta_type | discovery-call / strategy-session / training-rewatch / youtube-watch | yes |
| cta_url | HiRose tracking URL placeholder | yes |
| rationale | HTML or plain text rationale (3 sentences plain English) | yes |
| voc_quotes | Array of `{text, source}`. 1+ testimonial AND 1+ sales call MINIMUM | yes |
| source_tags | Array of lowercase tags. First tag is the audience | yes |
| status | proposal_pending (default) | auto |
| history | `[{type:"delivered",who:"Timo",text:"<b>Pushed</b> from pb-email",time:"<now>"}]` | auto |

If any required field is missing in the chat draft, ASK Timo before pushing. Never invent.

## ZERO-DROP CONTRACT

Every labeled section in the chat draft MUST land on the dashboard. The `pb-email` output template defines 14 required fields. Run preflight enumeration:

1. **Dedup check FIRST.** GET the current email_proposals table:
   ```bash
   source ~/.claude/secrets/precision-brass.env
   curl -s "${SUPABASE_URL}/rest/v1/email_proposals?select=id,subject" \
     -H "apikey: ${SUPABASE_PUBLISHABLE_KEY}" \
     -H "Authorization: Bearer ${SUPABASE_PUBLISHABLE_KEY}"
   ```
   For each draft to push, check id collision OR subject similarity (3+ overlapping non-stopword tokens). DEFAULT: silently skip duplicates per `feedback_skip_dups_silently.md` (standing rule from 2026-04-26). Note skips in preflight summary, then proceed.

2. **Enumerate**. List every labeled section in the draft from chat. Should be: Subject + alts, Preheader, Body, P.S. (with type), CTA (with URL), Audience, Hook angle, Pain point, Rationale, VOC quotes, Source tags.

3. **Map**. For each section, name its destination column.

4. **Account for every word**. If the draft has a section with no destination (e.g. an extra "production notes" block Timo added), STOP and ask. Do not push.

5. **Show Timo the map**. Display the dedup result + enumeration as a numbered checklist. Wait for explicit "go" before curling.

### Example preflight (output in chat)

```
Pushing 3 drafts. Preflight:

Dedup: 0 collisions. All 3 are new.

Sections found in each draft (verified across all 3):
1. Subject + alts                        -> subject + subject_alts
2. Preheader                             -> preheader
3. Body                                  -> body
4. P.S. (type-tagged)                    -> ps_text + ps_type
5. CTA (type + URL)                      -> cta_type + cta_url
6. Audience                              -> audience
7. Hook angle                            -> hook_angle
8. Pain point                            -> pain_point
9. Rationale (3 sentences plain English) -> rationale
10. VOC quotes (testimonial + sales call) -> voc_quotes
11. Source tags                          -> source_tags

Every section accounted for. Push? (y to proceed)
```

If Timo says yes, curl. Otherwise ask what to fix.

## VOC quote sourcing minimums (per `feedback_quote_sourcing_minimums.md`)

Every `voc_quotes` array MUST include at least:
1. **One quote from a testimonial** (someone who worked with Harrison and recorded a video testimonial). Source: `voc/raw/testimonials/`.
2. **One quote from a sales call** (someone Harrison did a discovery call with). Source: `voc/raw/sales-calls/`.

If either is missing in the draft, STOP. Tell Timo which is missing. Do not push.

## Workflow

### Step 1. Confirm what to push

If Timo says "push 2 and 4", read back the subjects:

> "Pushing these 2 drafts to Harrison's dashboard:
> 1. {subject 1}
> 2. {subject 2}
> Confirm? (y to push, or tell me what to change)"

Only proceed on explicit "y" or "go".

### Step 2. Load Supabase config

Read `/Users/air/Desktop/Precision-Brass/dashboard/lib/config.js`. If the file does not exist or contains placeholder `YOUR-PROJECT-REF`, STOP and tell Timo to run `dashboard/setup/SUPABASE_SETUP.md` first.

### Step 3. Build proposal IDs

Format: `e_{YYYYMMDD}_{slug}`. Slug = first 3-4 words of subject, lowercased, hyphenated, with non-alphanumeric characters stripped.

Example: subject "Karen has a master's from Northwestern" -> id `e_20260428_karen_has_a_masters`.

If id collides with an existing row, append `_v2`, `_v3`, etc.

### Step 4. POST to Supabase

For each greenlit draft, run a Bash curl POST to the email_proposals endpoint:

```bash
SUPABASE_URL="$(grep SUPABASE_URL /Users/air/Desktop/Precision-Brass/dashboard/lib/config.js | cut -d\' -f2)"
SUPABASE_KEY="$(grep SUPABASE_ANON_KEY /Users/air/Desktop/Precision-Brass/dashboard/lib/config.js | cut -d\' -f2)"

# Build payloads with python3 to avoid shell-escape issues with quotes
python3 build_email_payloads.py  # writes /tmp/pb-emails/{0,1,2}.json

for f in /tmp/pb-emails/*.json; do
  curl -s -X POST "${SUPABASE_URL}/rest/v1/email_proposals" \
    -H "apikey: ${SUPABASE_KEY}" \
    -H "Authorization: Bearer ${SUPABASE_KEY}" \
    -H "Content-Type: application/json" \
    -H "Prefer: return=representation" \
    --data-binary "@${f}"
done
```

DO NOT use Python's urllib or requests for the POST. macOS system Python lacks linked CA certs and fails with `SSL: CERTIFICATE_VERIFY_FAILED`. Always POST via curl (which uses the system keychain). Same constraint as pb-ideas-push.

### Step 5. Confirm + open dashboard

After all POSTs return 201:

> "Pushed N drafts to the dashboard.
> Harrison can review them at: dashboard/emails.html (Pending Review column).
> Want me to open it?"

If Timo says yes, run `open -a Safari /Users/air/Desktop/Precision-Brass/dashboard/emails.html`.

### Step 6. Append to voices_used_log

After successful push, append a line to `voc/email_voices_used_log.jsonl` capturing the voices in the pushed drafts. This advances rotation for the next pb-email run.

### Step 7. Log to SESSION_LOG (silent)

Add a one-liner:
> "Pushed N email drafts to Harrison dashboard: [subjects]. Awaiting approval."

## Failure modes to avoid

1. **Inventing VOC quotes.** Every quote must trace to a real file in `voc/raw/sales-calls/` or `voc/raw/testimonials/`. If you don't have it, ask. Never paraphrase a quote and pass it as verbatim.
2. **Pushing drafts Timo did not pick.** Only push the ones Timo explicitly named. If Timo says "push the good ones", ASK which numbers.
3. **Silent failures.** If curl returns 4xx/5xx, surface the full error to Timo. Don't pretend it worked.
4. **Skipping the approval wait.** Do NOT auto-fire any AC publish step after pushing. Harrison has to approve first on the dashboard.
5. **Tagline missing.** Before pushing, grep each body for the recurring tagline. If absent, send back to Timo for repair.

## What this skill does NOT do

- Does not generate drafts (that's `pb-email`).
- Does not publish emails to ActiveCampaign (Phase 2).
- Does not approve drafts on Harrison's behalf (Harrison clicks the button).
- Does not push without Timo's explicit confirmation.
