---
name: pb-email-write
description: Phase 2 of Harrison Ball's Precision Brass email engine. Takes ONE approved email idea (status=idea_approved in `email_ideas` table) and expands it into a full ready-to-send draft, then INSERTS it as a proposal in `email_proposals` for Harrison's final review. Mirrors pb-script-write's role in the script flow. The idea contains the angle, audience, hook, pain point, rationale, and VOC quotes; this skill writes the actual subject (plus 2 alts), preheader, full Harrison-voice body (tagline verbatim), proven P.S. type, CTA, and final rationale. Use when Timo says "/pb-email-write <id>", "write the email for idea N", "draft the email Harrison approved", "expand idea X into a proposal", or names a specific approved idea title and asks for the full draft. Hard precondition the source idea must already be `idea_approved` on the dashboard. ALWAYS load the existing pb-email reference files (`email-voice-protocol.md`, `email-output-template.md`, `email-audience-guide.md`, `email-rotation-protocol.md`) and the project memory `feedback_email_voice_load_order.md` before drafting. Show the full draft in chat as plain markdown FIRST and wait for Timo's approval before inserting into Supabase. The chat-draft-before-render rule applies (per `feedback_chat_draft_before_render.md`).
---

# pb-email-write. Phase 2: Approved-idea to full draft.

## OPERATING PRINCIPLE

Ship right, never ship fast. Voice fidelity over speed. One off-voice email kills trust faster than ten on-voice ones build it. If the draft doesn't sound like Harrison wrote it, throw it away and rewrite. Do NOT push borderline drafts to the dashboard. (Per `feedback_ship_right_not_fast.md`.)

## What this does

Takes ONE approved email idea by ID. Reads the idea's angle, hook, pain point, audience, CTA hint, rationale, and VOC quotes from Supabase. Expands into a full draft email matching Harrison's voice. Inserts the draft as a row in `email_proposals` with `status=proposal_pending`, `idea_id=<source idea>`. Updates the source `email_ideas` row to `status=drafted` and stamps `proposal_id`.

Difference vs `pb-email`:
- `pb-email` generates 5 fresh angles AND drafts in one batch (idea + body fused, no approval gate).
- `pb-email-write` writes the deep draft AFTER Harrison has approved a single angle on the dashboard. Mirrors how `pb-script-write` writes a full script for ONE approved idea picked from `pb-script`'s menu.

## When to fire

Trigger when Timo says:
- `/pb-email-write <id>`
- `/pb-email-write` followed by a subject line or shorthand naming an approved idea
- "write the email for idea N"
- "draft the email Harrison approved"
- "expand idea ei_2026XXXX_XXX into a proposal"
- "now draft it" (immediately after Timo confirms an idea is approved on the dashboard)
- "phase 2 of email"

Do NOT fire on:
- A pending idea (status=idea_pending). Tell Timo to get Harrison to approve first.
- A rejected idea. Tell Timo and stop.
- A request that contains no ID and no recent context for which idea is meant. Ask which idea.

## Hard preconditions (do not skip)

Before drafting a single line, READ all of these in this exact order:

1. `~/.claude/skills/pb-email/references/email-voice-protocol.md`. Harrison's voice fingerprint, tagline rule, banned words, contraction rules.
2. `~/.claude/skills/pb-email/references/email-output-template.md`. The draft format. Subject + 2 alts + preheader + body + P.S. + CTA structure.
3. `~/.claude/skills/pb-email/references/email-audience-guide.md`. Tone differences across broadcast / reengagement / webinar-push / discovery-followup.
4. `~/.claude/skills/pb-email/references/email-rotation-protocol.md`. Avoid repeating the same hook angle / P.S. type used in the last 2 sends.
5. `/Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_email_voice_load_order.md`. The non-negotiable load order. Voice catalog + 3 FINAL emails + sequence emails 1-7. NEVER load emails 8-12 (Paul template leakage).
6. `/Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_ship_right_not_fast.md`. Shipping bar.
7. `/Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_chat_draft_before_render.md`. Show full draft in chat first; never auto-push to Supabase.
8. `/Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_zero_drop_ingestion.md`. Every section the idea provides MUST flow into the draft. No silent drops.
9. `/Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_no_internal_jargon_in_rationale.md`. Plain English rationale only.
10. `/Users/air/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_quote_sourcing_minimums.md`. Minimum 1 testimonial quote AND 1 sales call quote in the rationale evidence.

Skipping the load order = repeating the Paul-template-leakage failure of 2026-04-28. The list above is the same enforced load order as `pb-email`, plus the chat-draft and zero-drop rules specific to this Phase 2 skill.

## Pulling the approved idea

The skill reads from Supabase. Two paths:

1. **Preferred**: Use the existing dashboard. Timo says `/pb-email-write ei_20260506_XXX`. The skill fetches that idea row from Supabase via the REST API using the project's `SUPABASE_URL` and the user's session JWT (or service_role key if running locally with `.env`).
2. **Fallback**: Timo pastes the idea fields directly into chat (subject, hook_angle, audience, pain_point, rationale, voc_quotes). Skill drafts from the pasted blob. Still INSERTs into Supabase if connected.

If the idea status is anything other than `idea_approved`, refuse and explain. The script flow has the same gate.

## Drafting protocol

For the picked idea:

1. **Subject + 2 alts**. Three subjects targeting the same hook angle but with different cognitive entries (curiosity / specific-result / pattern-interrupt). Keep under 60 chars.
2. **Preheader**. One short sentence amplifying or counter-balancing the subject.
3. **Body**. Full Harrison-voice email. Open with the hook angle from the idea. Lead with pain point. Build with VOC evidence (paraphrased, not pasted verbatim into body unless flagged as a quotable testimonial). Close with the recurring tagline VERBATIM:
   > We help trumpet players unlock their full potential by aligning sound, body, and technique into one effortless system.
4. **P.S.**. ONE of the 5 proven types: scarcity, timing, urgency, social-pressure, risk-reversal. Pick the one that matches the idea's audience and CTA. Honor `email-rotation-protocol.md`: avoid the P.S. type used in the most recent send for this audience.
5. **CTA**. Match `cta_type` from the idea (discovery-call / strategy-session / training-rewatch / youtube-watch). HiRose tracking URL placeholder `https://hirose.example/c/REPLACE_TOKEN` until Timo provides the actual link.
6. **Rationale**. HTML using the same colored-section pattern as `dashboard/scripts.html` (`r-section.concept`, `r-section.wound`, `r-section.why`, `r-section.icp`, `r-section.synthesis`). 5-7 sections. Plain English (no "the corpus", "the voice bank", "the converter"). Per `feedback_no_internal_jargon_in_rationale.md`.
7. **VOC quotes**. Carry forward the ones from the idea row. Add at most 1 more if it tightens the rationale. Minimum: 1 testimonial + 1 sales call quote (per `feedback_quote_sourcing_minimums.md`).
8. **Source tags**. Carry forward from the idea. Add `phase=write` so we can filter Phase 1 vs Phase 2 origin in analytics.

## Chat draft gate (NON-NEGOTIABLE)

Before any DB write or Chrome render or file touch:

1. Render the FULL draft in chat as plain markdown. Subject + 2 alts + preheader + body + P.S. + CTA + rationale (HTML rendered as plain markdown sections) + VOC quotes.
2. Stop. Wait for Timo's explicit approval ("ship it", "push it", "looks good", "approved", "yes proposal it").
3. Only after explicit approval, INSERT into `email_proposals` and update the source idea.

This is enforced by `feedback_chat_draft_before_render.md`. Two checkpoints: render approval, upload approval.

## Supabase insert (after Timo approves)

Generate a new proposal ID: `e_YYYYMMDD_<short_slug>` (e.g. `e_20260506_dental_trigger`). Insert with:

```js
{
  id: 'e_YYYYMMDD_<slug>',
  idea_id: '<source email_ideas.id>',
  subject: '<final subject>',
  subject_alts: ['<alt1>', '<alt2>'],
  preheader: '<preheader>',
  body: '<full body, %FIRSTNAME% merge tags>',
  ps_text: '<actual P.S. line>',
  ps_type: '<scarcity|timing|urgency|social-pressure|risk-reversal>',
  hook_angle: '<carry forward from idea>',
  pain_point: '<carry forward from idea>',
  audience: '<carry forward from idea>',
  cta_type: '<carry forward from idea>',
  cta_url: '<HiRose tracking URL>',
  rationale: '<HTML rationale>',
  voc_quotes: [{ text, source }, ...],
  source_tags: [...idea.source_tags, 'phase=write'],
  status: 'proposal_pending',
  notes: '',
  history: [{ type: 'delivered', who: 'Timo', text: '<b>Drafted</b> from idea ' + idea_id, time: '<now>' }]
}
```

Then update the source `email_ideas` row: `status='drafted'`, `proposal_id='<new proposal id>'`, append history entry `{ type: 'delivered', who: 'Timo', text: '<b>Drafted</b> as ' + proposal_id }`.

Both writes go through the same `lib/db.js` API the dashboard uses (or direct Supabase REST with the user's JWT). Use the same anon key + bearer pattern; do NOT embed service_role keys in code.

## Confirm to Timo after insert

Tell Timo:
- Proposal ID created
- Where it landed: dashboard/emails.html, "Drafts Pending" column
- Source idea is now marked drafted with link to the new proposal
- No emails are sent. Harrison still reviews on the dashboard.

## Failure modes (read before drafting)

1. Drafting from an idea that wasn't approved. Always check status.
2. Loading the wrong reference set (emails 8-12 = Paul template leakage). Per `feedback_email_voice_load_order.md`, only load voice catalog + 3 FINAL + sequence 1-7.
3. Auto-pushing to Supabase without showing the draft in chat first. Always two-checkpoint.
4. Using "the corpus", "the voice bank", "the converter" in rationale text. Plain English only.
5. Dropping a section the idea provides (e.g., the idea has 4 VOC quotes, draft proposal has only 2). Zero-drop ingestion.
6. Inventing behavioral claims about Harrison's audience that aren't in the idea or VOC corpus. ASK, don't invent.
7. Using a P.S. type or hook angle that was used in the most recent send. Honor rotation protocol.

## Output

The skill ends with the proposal ID, dashboard link, and a 1-line summary. No PDF. No HTML file. The DRAFT lives in Supabase, viewable on `dashboard/emails.html`. If Timo wants a printable version, that's a downstream skill.
