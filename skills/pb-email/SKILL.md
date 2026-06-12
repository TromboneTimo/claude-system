---
name: pb-email
description: Email proposal engine for Harrison Ball's Precision Brass business. Mirrors pb-script architecture but produces ready-to-send DRAFT emails (not video scripts). 7 parallel mining agents read sales calls, testimonials, winning emails and ads, best-practices research + live AC perf data, and Harrison's existing email sequence to surface 5 fresh email drafts. Each draft includes subject line + 2 alternates, preheader, full body in Harrison's voice (with the recurring tagline verbatim), P.S. matching one of 5 proven types, CTA from Section 5 templates, audience tag (broadcast / re-engagement / webinar-push / discovery-followup), hook angle, pain point, rationale, and VOC quote evidence. A sequential voice & diversity auditor (run inline by the orchestrator) enforces voice fidelity, freshness across runs, and 1+ testimonial + 1+ sales-call quote per draft. Use when Timo says "email ideas", "email proposals", "draft emails", "what email should we send", "/pb-email", or after AC sends are logged and we need fresh angles. Stops at the 5-draft menu and waits for Timo to pick. Do NOT auto-push to dashboard; pb-email-push handles that.
---

# pb-email. Email proposal engine.

## OPERATING PRINCIPLE: Ship right, never ship fast.

Speed is never the priority for this skill. Voice fidelity is. Harrison's email list is small, focused, and high-signal. One off-voice email kills trust faster than ten on-voice ones build it. If a draft does not sound like Harrison wrote it, throw it away and start over. Do not push borderline drafts and "iterate later".

This principle is also stored in `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/canon_working_process.md`.

## What this does

Mirrors the pb-script architecture compressed into a single phase: 7 parallel specialist subagents (files in `agents/01` through `agents/07`) mine Harrison's VOC corpus, the swipe-file research corpus, and live AC performance data through different lenses, each returns a complete DRAFT email (not just an idea), then a sequential voice & diversity auditor (run inline by the orchestrator; it has no agent file) selects 5 final drafts enforcing voice and source diversity. The menu item IS the draft. Timo picks; pb-email-push lands them in `dashboard/emails.html` for Harrison's review.

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

Optional Step 0b: `Precision-Brass/brain/wiki/index.md` may be consulted FIRST to locate evidence (students, techniques, objections, winning patterns) before corpus sweeps; follow its [[wikilinks]] to the exact voc/ source instead of bulk-reading corpora.

Before spawning ANY drafting agent, read these files in this exact order. Pass them into each agent prompt as load-once context:

1. `voc/emails/extracts/harrison-email-voice.md` (the 302-line voice catalog)
2. `output/email-PP01-dental-trigger-FINAL.txt`
3. `output/email-PP03-failed-lessons-FINAL.txt`
4. `output/email-PP05-isolation-FINAL.txt`
5. `voc/emails/raw/sequences/2026-04-21_email-sequence_webinar-optin-to-strategy-session.md` (emails 1-7 ONLY)
6. `~/.claude/skills/pb-email-write/references/reader-facing-playbook.md` (THE method, proven 2026-06-09). Every draft: write TO the reader in their scene, never ABOUT a third party they watch; cite a SPECIFIC named Harrison technique from his videos so the reader feels smart; edge over soft-cock energy; P.S. inside the body. Section 9 = VARY THE REFRAME TRANSITION across the 5-draft batch (no two emails reuse the same pivot; never repeat "Here's the truth nobody told you").
7. `references/email-beat-cloning-method.md` (the drafting law: clone a real swipe-file skeleton, fill from Harrison's own material, carry one verified proof point)
8. `references/email-data-driven-patterns.md` (empirical findings from 416 Harrison broadcasts; the composite open x CTR score and subject-pattern data every draft must respect)

NEVER load emails 8-12 of the webinar sequence. They are signed by Paul The Trombonist and target music educators. Per `voc/emails/extracts/harrison-email-voice.md` Section 10, they are template leakage and will pollute Harrison's voice.

The recurring tagline must appear verbatim in every draft:

> "We help trumpet players unlock their full potential by aligning sound, body, and technique into one effortless system."

Do not paraphrase. Do not "improve". Verbatim.

## Subagent architecture

Spawn agents 1-7 IN PARALLEL in a single message after audience confirmation. After all 7 return, run the sequential voice & diversity auditor.

Read each agent's prompt from `references/email-output-template.md` and the agent prompt files in `agents/` (7 files, `01` through `07`).

| # | Agent | Corpus / lens | Returns |
|---|---|---|---|
| 1 | Sales-call anchor | One rotating sales call from `voc/sales-calls/raw/` | 1 draft naming the unnamed wound from that call |
| 2 | Testimonial proof | One rotating testimonial from `voc/testimonials/raw/` | 1 draft built around 1 student's transformation, Joinville/Enrique/Mike pattern |
| 3 | Objection preempt | Least-recently-used OBJ lens from pb-script `references/objection-lenses.md` | 1 draft that dismantles the objection |
| 4 | Winning-pattern | `voc/emails/raw/winning-emails/` (18 ranked winners) + `voc/emails/performance/ranking.json` + `voc/meta-ads/` winners + `voc/synthesis/ad-winning-verbiage.jsonl` | 1 draft mirroring proven hook/structure |
| 5 | P.S. trigger | One of 5 P.S. types (scarcity / timing / urgency / social-pressure / risk-reversal) as the seed | 1 draft engineered around a strategic P.S. |
| 6 | Discovery-followup OR fresh lens | If `discovery-followup` audience selected, mines no-show/no-close calls. Otherwise rotating fresh lens (dental-trigger, isolation, age-anxiety, comeback-arc, failed-method-grief) + `voc/synthesis/fresh-ad-pain-points.md` | 1 draft |
| 7 | Best-practices | Email-marketing research cache + live AC perf brief + swipe-file (`voc/emails/swipe-file/`: STRATEGY.md, analysis/, 311 modeled emails) | 1 draft engineered against documented best practices, every move cited |

Each parallel agent returns a candidate draft pack (subject + alts, preheader, body, P.S., CTA, audience, hook angle, pain point, rationale, voc_quotes, source_tags).

| Agent | Type | Purpose |
|---|---|---|
| Voice & diversity auditor (run inline by the orchestrator; no agent file) | Sequential | Selects final 5. Enforces: |

Auditor enforces (all must pass):

1. **5 distinct primary voices.** Reject candidates whose primary voice has been used in the last 2 runs (read `voc/email_voices_used_log.jsonl`). Allow exceptions if the agent provides a `freshness_override` justification.
2. **1+ testimonial-anchored draft AND 1+ sales-call-anchored draft.** Per `canon_working_process.md`.
3. **Recurring tagline verbatim in every draft.** Grep each body. If missing or paraphrased, send back.
4. **No template leakage.** Reject drafts containing "Paul The Trombonist", "music educators", "mastermind" (unless explicitly justified), or sequence email 8-12 phrasings.
5. **No fabricated authority claims.** Reject drafts asserting "Featured in Forbes" or "9,500 trumpet players have watched this training" without source verification, per `canon_working_process.md`.
6. **Plain-English rationale.** No "the corpus", "the converter", "the voice bank", "the database", "BOFU floor", or similar dev-speak. Per `canon_working_process.md`.
7. **Real student names only.** Every name proof in a draft must trace to a file in `voc/testimonials/raw/`.
8. **EMAIL DRAFT GATE.** Run `~/.claude/knowledge/email-draft-gate.md` on every final draft (swipe-file pacing read THIS session, Q/A grammar flow, named-technique specificity, no pendulum) and print its 1-line `GATE:` proof block above each draft shown in chat.

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

### Step 0 (MANDATORY). Run /pb-email-perf and read its brief before any drafting

Nothing is auto-loaded. Run all three, in this order, before any drafting:

1. `/pb-email-perf` (endpoint live at `api/ac-perf.js`): top 10 by open rate / CTR / reply rate, bottom 5 anti-patterns, destination mix, subject-pattern aggregates.
2. `python3 scripts/email-perf-quadrant.py` (added 2026-06-11): median-splits every mature send into CLONE WHOLE / CLONE SUBJECT / CLONE BODY / AVOID, plus UNSUB-HOT and BOUNCE hygiene flags. High-open and high-click are separate skills; each draft must state which quadrant its subject pattern and its body shape are borrowed from. MATURING sends (<48h) are excluded; never cite them.
3. `get_recent_replies` (precision-brass-ac MCP): read the last 2 weeks of real subscriber replies. A reply is the strongest VOC signal there is; reply themes feed hook angles directly (the too-old angle pulls 2-5x the replies of any other -- found 2026-06-11).

Pass all three (or their /tmp paths) into every drafting agent. Do not spawn any agent before these exist.

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
2. `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/canon_working_process.md`
3. `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/canon_email_writing.md`
4. `voc/emails/extracts/harrison-email-voice.md`
5. `voc/email_voices_used_log.jsonl` (last 3 runs to know which voices to avoid)
6. `references/email-beat-cloning-method.md` + `references/email-data-driven-patterns.md` (mandatory drafting law + empirical patterns; pass both into every drafting agent)
7. `voc/emails/raw/losing-emails/ANTI-PATTERNS.md` (9 click-killing patterns mined from the 13 bottom-ranked real sends, 2026-06-11; the AUDITOR CHECKLIST section is a kill-list the voice & diversity auditor enforces on every final draft)
8. `voc/lessons/extracts/fresh-mechanisms.md` (18 under-used named mechanisms + 77 verbatim lesson quotes mined 2026-06-11 from the 97-session lessons corpus; the FIRST place to look when the angle ledger flags saturation. Lead candidates: Four Points of Contact (0 prior uses, 26 lesson files), Comfort Slide, Hot Water Bottle/compression lineage. Auto-transcript rule applies: verify unusual proper names before shipping.)

LINK RULE (standing order, Timo 2026-06-11): NO YouTube links in any draft -- no videos, no channel. Every master class CTA points at the VSL training-room URL copied VERBATIM from `CANONICAL_MASTERCLASS_URL` in dashboard/lib/email-lint.js (NEVER webinar-registration-pb -- that is the capture page; NEVER with el= added; never copied from an old email). cta_type youtube-watch is retired. Full rules: pb-email-push LINK RULES.

### Step 3. Pick rotation slots (Bash, before spawning agents)

For each audience selected:
- Pick a sales call from `voc/sales-calls/raw/` not used in the last 2 runs.
- Pick a testimonial from `voc/testimonials/raw/` not used in the last 2 runs.
- Pick the least-recently-used OBJ lens from pb-script's `references/objection-lenses.md`.
- Pick the least-recently-used fresh lens (or set Agent 6 to discovery-followup mode).

Print these slot picks in chat so Timo can see what's in play this run.

### Step 4. Spawn agents 1-7 in parallel

Single message, 7 Agent tool calls. Each gets:
- The voice catalog and the 3 FINAL emails as load-once context
- The 7-email sequence (emails 1-7 only) as a voice exemplar
- The beat-cloning law + data-driven patterns references and the Step 0 perf brief
- Their specific corpus/lens slot
- The audience tag(s) to honor
- Off-limits names (from voc/email_voices_used_log.jsonl last 2 runs)
- Output schema (subject + alts + preheader + body + P.S. + CTA + rationale + voc_quotes + source_tags)

Each agent reads its slot, drafts, and returns the draft pack as JSON-shaped chat output.

### Step 5. Run the voice & diversity auditor sequentially

Pass it all 7 candidates plus the off-limits voices list. It runs the 8 enforcement checks above and returns the final 5.

### Step 6. Render menu in chat

Format per `references/email-output-template.md`. Include the "pick which to push" prompt at the bottom.

### Step 7. Wait

Do NOT auto-fire pb-email-push. Wait for Timo to say "push N" or similar. The push skill has its own zero-drop preflight.

### Step 8. Append to voices_used_log

After Timo picks, append the selected draft voices to `voc/email_voices_used_log.jsonl` regardless of whether he then pushes or not. (Voice freshness rotation should advance even if Timo bins all 5 and asks for a fresh menu.)

## What this skill does NOT do

- Does NOT push to the dashboard. That's `pb-email-push`.
- Does NOT send emails to ActiveCampaign. AC publish is Phase 2.
- Does NOT modify `voc/emails/extracts/harrison-email-voice.md`. The catalog is the source of truth.
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
7. **Spectator voice ("soft-cock energy").** Reject any draft that tells a third party's story and comments on it instead of putting the READER in the scene. Talk to the person reading it. Per `reader-facing-playbook.md`.
8. **Vague mechanism.** Reject "a system nobody taught you" with no named, specific Harrison technique. The reader must feel smart from a real move cited from his videos. Per `reader-facing-playbook.md`.
9. **Repeated reframe transition.** Across the 5-draft batch, no two emails may use the same pivot into the reframe. Reject duplicates. Never "Here's the truth nobody told you". Per `reader-facing-playbook.md` Section 9.
