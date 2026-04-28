---
name: pb-email
description: Email proposal engine for Harrison Ball's Precision Brass business. Mirrors pb-script architecture but produces ready-to-send DRAFT emails (not video scripts). 6 parallel mining agents read sales calls, testimonials, winning ads, and Harrison's existing email sequence to surface 5 fresh email drafts. Each draft includes subject line + 2 alternates, preheader, full body in Harrison's voice (with the recurring tagline verbatim), P.S. matching one of 5 proven types, CTA from Section 5 templates, audience tag (broadcast / re-engagement / webinar-push / discovery-followup), hook angle, pain point, rationale, and VOC quote evidence. A 7th sequential auditor enforces voice fidelity, freshness across runs, and 1+ testimonial + 1+ sales-call quote per draft. Use when Timo says "email ideas", "email proposals", "draft emails", "what email should we send", "/pb-email", or after AC sends are logged and we need fresh angles. Stops at the 5-draft menu and waits for Timo to pick. Do NOT auto-push to dashboard; pb-email-push handles that.
---

# pb-email. Email proposal engine.

## OPERATING PRINCIPLE: Ship right, never ship fast.

Speed is never the priority for this skill. Voice fidelity is. Harrison's email list is small, focused, and high-signal. One off-voice email kills trust faster than ten on-voice ones build it. If a draft does not sound like Harrison wrote it, throw it away and start over. Do not push borderline drafts and "iterate later".

This principle is also stored in `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_ship_right_not_fast.md`.

## What this does

Mirrors the pb-script architecture compressed into a single phase: 6 parallel specialist subagents mine Harrison's VOC corpus through different lenses, each returns a complete DRAFT email (not just an idea), then a sequential auditor selects 5 final drafts enforcing voice and source diversity. The menu item IS the draft. Timo picks; pb-email-push lands them in `dashboard/emails.html` for Harrison's review.

Runs the same 4-failure-pattern + 4-master-lesson guard rails as pb-script.

## When to fire

Trigger when Timo says:
- "give me email ideas"
- "draft some emails"
- "what should we send to the list"
- "email proposals"
- "fresh email angles"
- "/pb-email"
- "email ideas for harrison"
- "we need a re-engagement email" (audience hint)
- "webinar push email" (audience hint)

Do NOT fire on YouTube/script context. That is `pb-script`.

## Audience selection (REQUIRED before spawning agents)

Ask Timo which audience(s) the menu should serve. Multiple OK.

| Audience | Targets | Used for |
|---|---|---|
| `broadcast` | Whole AC list | Newsletter, announcement, content drop |
| `reengagement` | Subscribers cold 30/60/90 days | Win-back angles |
| `webinar-push` | Cold list driving to free training opt-in | Mirrors emails 1-2 of existing sequence |
| `discovery-followup` | Booked-but-no-show or showed-but-no-close | Re-warm prospects post-call |

If Timo doesn't specify, default to `broadcast` and ask if he wants other audiences too.

## Voice load order (NON-NEGOTIABLE)

Before spawning ANY drafting agent, read these files in this exact order. Pass them into each agent prompt as load-once context:

1. `voc/personas/harrison-email-voice.md` (the 302-line voice catalog)
2. `output/email-PP01-dental-trigger-FINAL.txt`
3. `output/email-PP03-failed-lessons-FINAL.txt`
4. `output/email-PP05-isolation-FINAL.txt`
5. `voc/raw/email-sequences/2026-04-21_email-sequence_webinar-optin-to-strategy-session.md` (emails 1-7 ONLY)

NEVER load emails 8-12 of the webinar sequence. They are signed by Paul The Trombonist and target music educators. Per `voc/personas/harrison-email-voice.md` Section 10, they are template leakage and will pollute Harrison's voice.

The recurring tagline must appear verbatim in every draft:

> "We help trumpet players unlock their full potential by aligning sound, body, and technique into one effortless system."

Do not paraphrase. Do not "improve". Verbatim.

## Subagent architecture

Spawn agents 1-6 IN PARALLEL in a single message after audience confirmation. After all 6 return, run agent 7 sequentially.

Read each agent's prompt from `references/email-output-template.md` and the agent prompt files in `agents/`.

| # | Agent | Corpus / lens | Returns |
|---|---|---|---|
| 1 | Sales-call anchor | One rotating sales call from `voc/raw/sales-calls/` | 1 draft naming the unnamed wound from that call |
| 2 | Testimonial proof | One rotating testimonial from `voc/raw/testimonials/` | 1 draft built around 1 student's transformation, Joinville/Enrique/Mike pattern |
| 3 | Objection preempt | Least-recently-used OBJ lens from pb-script `references/objection-lenses.md` | 1 draft that dismantles the objection |
| 4 | Winning-pattern | `voc/raw/winning-emails/` (currently empty) and `facebook-ads-database/*` winners | 1 draft mirroring proven hook/structure |
| 5 | P.S. trigger | One of 5 P.S. types (scarcity / timing / urgency / social-pressure / risk-reversal) as the seed | 1 draft engineered around a strategic P.S. |
| 6 | Discovery-followup OR fresh lens | If `discovery-followup` audience selected, mines no-show/no-close calls. Otherwise rotating fresh lens (dental-trigger, isolation, age-anxiety, comeback-arc, failed-method-grief) | 1 draft |

Each parallel agent returns a candidate draft pack (subject + alts, preheader, body, P.S., CTA, audience, hook angle, pain point, rationale, voc_quotes, source_tags).

| # | Agent | Type | Purpose |
|---|---|---|---|
| 7 | Voice & diversity auditor | Sequential | Selects final 5. Enforces: |

Auditor enforces (all must pass):

1. **5 distinct primary voices.** Reject candidates whose primary voice has been used in the last 2 runs (read `voc/email_voices_used_log.jsonl`). Allow exceptions if the agent provides a `freshness_override` justification.
2. **1+ testimonial-anchored draft AND 1+ sales-call-anchored draft.** Per `feedback_quote_sourcing_minimums.md`.
3. **Recurring tagline verbatim in every draft.** Grep each body. If missing or paraphrased, send back.
4. **No template leakage.** Reject drafts containing "Paul The Trombonist", "music educators", "mastermind" (unless explicitly justified), or sequence email 8-12 phrasings.
5. **No fabricated authority claims.** Reject drafts asserting "Featured in Forbes" or "9,500 trumpet players have watched this training" without source verification, per `feedback_master_lessons.md`.
6. **Plain-English rationale.** No "the corpus", "the converter", "the voice bank", "the database", "BOFU floor", or similar dev-speak. Per `feedback_no_internal_jargon_in_rationale.md`.
7. **Real student names only.** Every name proof in a draft must trace to a file in `voc/raw/testimonials/`.

After selection, append to `voc/email_voices_used_log.jsonl`:

```jsonl
{"run_at": "2026-04-28T15:30:00Z", "audience": ["broadcast"], "voices": ["Karen", "Joe", "Joinville", "Mike", "fresh-lens-isolation"], "draft_subjects": [...]}
```

## Output format

Return the 5-draft menu in chat using the format in `references/email-output-template.md`. Each draft block contains:

- Number (1-5)
- Subject line + 2 alts
- Audience badge
- Hook angle + pain point
- Preheader
- Full body (Harrison voice, %FIRSTNAME% merge tag, recurring tagline verbatim)
- P.S. (one of 5 types) + a one-word P.S. type label
- CTA type + placeholder URL (HiRose `?el=` format)
- Rationale (3-sentence plain English)
- VOC quotes (1+ testimonial + 1+ sales-call)
- Source tags

Then end with:

> Pick which to push to Harrison's dashboard. Reply "push 1, 3, 5" or "push 2" or "all of them". I'll run pb-email-push.

## Workflow

### Step 1. Confirm audience(s)

If Timo didn't specify, ask:
> "Which audience(s) should this menu serve?
> - broadcast (whole list)
> - reengagement (cold subscribers)
> - webinar-push (free training opt-in)
> - discovery-followup (no-shows or no-closes)
>
> Pick 1+ or say 'broadcast' to default."

Wait for confirmation.

### Step 2. Pre-flight reads

Read in order (do NOT skip):
1. `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/MEMORY.md`
2. `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_master_lessons.md`
3. `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_harrison_voice.md`
4. `voc/personas/harrison-email-voice.md`
5. `voc/email_voices_used_log.jsonl` (last 3 runs to know which voices to avoid)

### Step 3. Pick rotation slots (Bash, before spawning agents)

For each audience selected:
- Pick a sales call from `voc/raw/sales-calls/` not used in the last 2 runs.
- Pick a testimonial from `voc/raw/testimonials/` not used in the last 2 runs.
- Pick the least-recently-used OBJ lens from pb-script's `references/objection-lenses.md`.
- Pick the least-recently-used fresh lens (or set Agent 6 to discovery-followup mode).

Print these slot picks in chat so Timo can see what's in play this run.

### Step 4. Spawn agents 1-6 in parallel

Single message, 6 Agent tool calls. Each gets:
- The voice catalog and the 3 FINAL emails as load-once context
- The 7-email sequence (emails 1-7 only) as a voice exemplar
- Their specific corpus/lens slot
- The audience tag(s) to honor
- Off-limits names (from voc/email_voices_used_log.jsonl last 2 runs)
- Output schema (subject + alts + preheader + body + P.S. + CTA + rationale + voc_quotes + source_tags)

Each agent reads its slot, drafts, and returns the draft pack as JSON-shaped chat output.

### Step 5. Spawn agent 7 (voice auditor) sequentially

Pass it all 6 candidates plus the off-limits voices list. It runs the 7 enforcement checks above and returns the final 5.

### Step 6. Render menu in chat

Format per `references/email-output-template.md`. Include the "pick which to push" prompt at the bottom.

### Step 7. Wait

Do NOT auto-fire pb-email-push. Wait for Timo to say "push N" or similar. The push skill has its own zero-drop preflight.

### Step 8. Append to voices_used_log

After Timo picks, append the selected draft voices to `voc/email_voices_used_log.jsonl` regardless of whether he then pushes or not. (Voice freshness rotation should advance even if Timo bins all 5 and asks for a fresh menu.)

## What this skill does NOT do

- Does NOT push to the dashboard. That's `pb-email-push`.
- Does NOT send emails to ActiveCampaign. AC publish is Phase 2.
- Does NOT modify `voc/personas/harrison-email-voice.md`. The catalog is the source of truth.
- Does NOT touch pb-script tables (ideas, scripts). Separate workflow.
- Does NOT create short-form social copy (that's manual extraction post-send).
- Does NOT generate subject lines without bodies. Every menu item is a complete draft.

## Failure modes to avoid

1. **Off-voice drafts.** If you can't find real voice in Harrison's corpus, don't fabricate it. Pull a different sales call or testimonial.
2. **Recycling Robbie/Mike/Heather/Phil.** The corpus has 28 sales calls and 11 testimonials. Use the freshness log.
3. **Paul-template leakage.** Reject any draft containing "Paul The Trombonist", "music educators", "mastermind".
4. **Fabricated credibility.** "Featured in Forbes" stays out unless verified per failure-pattern #4.
5. **Tagline drift.** The recurring tagline is verbatim. Grep before returning the menu.
6. **Auto-pushing.** Do not call pb-email-push without explicit Timo say-so.
