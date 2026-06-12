# Email Data-Driven Patterns

Empirical findings from **416 Harrison broadcasts** spanning Oct 2024 to May 2026, pulled live from ActiveCampaign on 2026-05-17. Optimization target per Timo: **open rate x CTR (composite score)**. Both opens and click-throughs matter; opens without clicks are vanity, clicks without opens means the audience never showed up to be persuaded.

This file is the authoritative source for what actually drives engagement in production. It supersedes "I think this kind of subject works" intuition. Loaded by every drafting agent.

## How the composite score works

`score = open_pct x ctr_pct`

- Median across all 416 broadcasts: **25.0**
- Top: 237.8 ("Quick Video on Lip Puckering", Apr 13)
- Big-broadcast top (delivered 4K+): 89.1 ("Masterclass Replay GONE IN 5 DAYS")

When a draft is in tension between a high-open subject and a high-click subject, optimize the product. A 45% open with 0.9% CTR (score = 40) loses to a 28% open with 2.0% CTR (score = 56).

## Audience size is the most powerful variable

| Tier (delivered) | n | Median Open | Median CTR | p75 CTR |
|---|---|---|---|---|
| S (<1.5K, segmented) | 210 | 30.8% | **1.40%** | 2.40% |
| M (1.5-3.5K) | 160 | 26.8% | 0.70% | 1.50% |
| L (3.5K+, full list) | 46 | 28.2% | 0.70% | 1.30% |

**Implication:** segmented sends to engaged subscribers convert at 2x the CTR of full-list blasts. When tagging an audience, prefer narrower segments (engaged-in-last-30-days, opened-last-3, etc) over `broadcast` unless the content explicitly needs reach (masterclass announcement, ITG-type news).

## The single most reproducible winning subject (use this pattern by default)

**"New Video on [Specific Technique] / Your Questions Answered!"**

- Sent 6 times across months
- Avg CTR **4.83%**
- Total 325 clicks
- The Jaw Placement variant alone hit 5.2% / 5.7% / 5.6% / 2.8% / 3.0% / 2.8% across 6 sends

This is a manual A/B test that already happened, and the result is "send this again with a new technique." When Harrison films a new technique-focused video, the subject line should default to this pattern. The technique slot is the only thing that changes.

Reusable variants in the same family (all verified winners):

- `"Quick Video on [Technique]"`. Lip Puckering variant: 7.5% CTR, 106 clicks, 1406 delivered
- `"How [technique] affects your trumpet playing"`. 5 sends, 1.54% avg CTR, range 1.5% to 4.1%
- `"Unlock Effortless High Notes with This Secret"`. 8 sends, 3.55% avg CTR

## High-confidence subject-line rules (n >= 18, real lift)

These are statistically defensible across the 290 broadcasts with delivered >= 1000:

| Feature | Lift on score | n with | Notes |
|---|---|---|---|
| **`%FIRSTNAME%` in subject** | **+46%** | 18 | Personalization signal. Use freely, especially on re-engagement and discovery-followup audiences. |
| **Short subject (<35 chars)** | **+81%** | 60 | Brevity wins. "Quick Video on Lip Puckering" = 28 chars. |
| **1-5 word subjects** | **+65%** | 63 | Same principle. "Did you forget this, %FIRSTNAME%?" = 5 words, 4.8% CTR. |
| **Multi-exclaim (!!)** | **+19%** | 14 | Surprising but real. The webinar-day "Webinar Today!!" pattern. Single `!` actually hurts (-19%). |

## High-confidence ANTI-patterns (subjects that drag score DOWN)

| Feature | Drag | n with | Replace with |
|---|---|---|---|
| Quote marks | -32% | 1 | Rare in this corpus; only one example pulled the score down. Avoid as a stylistic choice. |
| Ellipsis (`...` or `unicode-ellipsis`) | -23% | 20 | "...." reads like hesitation or trailing off. Replace with a punchier full stop or a colon. |
| Single exclamation (`!`) | -19% | 85 | The single `!` is the marketing-newsletter cliche. Either drop it (most subjects don't need any) or commit to `!!` (the urgency variant). |
| Question mark (`?`) | -10% | 48 | Mixed; some questions work ("Did you forget this, %FIRSTNAME%?"). Defaulting to questions is weak. Use only when the question is genuinely uncomfortable. |

## Structural openers (first word of subject), median score

Top 10 most-reused openers, ranked by median composite score:

| Opener | n | Median score | Use case |
|---|---|---|---|
| `"New ..."` | 7 | **82.8** | Utility-named-video pattern (default winner) |
| `"Masterclass ..."` | 3 | 78.1 | Big-list urgency announcement |
| `"Build ..."` | 5 | 68.2 | Result/outcome promise ("Build trumpet endurance without overplaying") |
| `"Did ..."` | 4 | 65.4 | Soft accusation ("Did you forget this, %FIRSTNAME%?") |
| `"Friday ..."` | 3 | 64.9 | Day-of-week event reminder |
| `"Private ..."` | 4 | 64.4 | Scarcity framing ("Private Invite! Read This Letter ASAP") |
| `"We ..."` | 4 | 49.2 | Plural / community |
| `"Unlock ..."` | 7 | 44.0 | Curiosity / payoff (works but oversaturated) |
| `"Stop ..."` | 13 | **27.7** | Underperformer. "Stop waiting" / "Stop relying on outdated methods" both bombed. |
| `"Hey ..."` | 8 | **25.8** | Underperformer. The `"Hey %FIRSTNAME%,"` opener doesn't beat baseline. |
| `"Tired ..."` | 3 | 25.4 | Underperformer. "Tired of working harder..." pulled 2.7. |

**Defaults:** prefer `New`, `Did`, `Build`, `Private`, `Masterclass`, `Friday`. Avoid `Stop`, `Hey`, `Tired`, `What`, `Missed` unless you have a specific reason.

## Big-broadcast (4K+) winning archetypes

When delivering to the full daily list, only these three archetypes have crossed 1.5% CTR in the past 12 months:

1. **Masterclass urgency / deadline on free thing.** "Masterclass Replay GONE IN 5 DAYS" (3.0%, 184 clicks), "Live Master Class and Replay and Gifts" (2.6%), "Watch This Incredible Masterclass Before It's Gone!" (3.1%)
2. **Testimonial with specific outcome number.** "The routine that built my range" (2.5%, 103 clicks), "My sound got 20% bigger from this" (1.5%), "What Happened When Brian Joined Precision Brass" (1.5%)
3. **Failure-framed story.** "He spent $20,000 on trumpet lessons... and got worse" (1.6%, 73 clicks), "They didn't have to do this, but you have to hear it" (1.3%), "Every teacher avoids this" (1.3%)

Anything else for a 4K+ broadcast should be challenged before drafting. Pure identity emails ("I used to play trumpet...", 44.5% open / 0.9% CTR) get opened but rarely clicked at big-list scale.

## Big-broadcast (4K+) anti-patterns (high unsub bleed)

These showed real CTR but ALSO high unsubscribe damage. The 12-month unsub median is 0.20%. Anything above 0.75% is bleeding the list:

| Subject | CTR | Unsubs | Unsub rate |
|---|---|---|---|
| ITG interview blast (Mar 25) | 2.2% | **55** | 0.92% |
| Client Onboarding Specialist (Feb 5) | 0.6% | 45 | 0.93% |
| "5 free spots this week!!" (Jan 14) | 0.6% | 50 | 1.06% |
| "Did You Quit on Your Trumpet Goals?" (Nov 23) | 3.1% | 3 | 1.15% |
| "Stop Relying on Outdated Methods" (Nov 29) | 1.5% | 4 | 1.23% |

**Rule:** non-product content (hiring, press, identity shaming, repeated "5 free spots" blasts) should be segmented to engaged subscribers only, never sent to the full daily list.

## Open-rate vs CTR divergence, the open-trap pattern

Three subjects to study before drafting a vague-identity hook:

| Subject | Open | CTR | What went wrong |
|---|---|---|---|
| "I used to play trumpet....." (Apr 8) | **44.5%** | 0.9% | Nostalgia opens, no actionable next step |
| "the 'I'm too old' lie costing trumpet players a decade" (May 16) | 24.4% | 0.7% | Identity hook + emotional close, no offer in body |
| "Quick Life Lesson" (Nov 16) | 53.5% | 4.9% | Curiosity opens, body delivered an actual lesson + click. This is the model |

**Rule:** if the subject leans identity/curiosity, the body MUST have a concrete payoff (a video, a 1:1 spot, a free resource) within 6 lines. Identity opens without payoff = vanity opens. Score column on the dashboard tells the real story.

## Subject-line drafting checklist (auditor enforces)

Every subject + alt drafted by a specialist agent must pass:

1. **Length sanity.** Target <=35 chars OR <=5 words. Long-form (70+ char) subjects only when there's a structural reason (full subject as the hook).
2. **No ellipsis (`...` / unicode-ellipsis).** Replace with a period or colon.
3. **Single `!` -> 0 or `!!`.** No lone exclamation marks.
4. **Opener is in the top-6 winning list** (`New`, `Did`, `Build`, `Private`, `Masterclass`, `Friday`), OR has a specific aggression-driven reason to deviate per Section 1.5.
5. **If `%FIRSTNAME%` would fit the angle, use it.** +46% lift.
6. **For technique-named-video drafts: use the `New Video on [Technique] / Your Questions Answered!` pattern verbatim** as the primary subject. Reuse is proven; reinvention loses.
7. **For 4K+ broadcasts: subject must map to one of the three winning archetypes** (masterclass-urgency, testimonial-with-number, failure-framed-story). If not, route to a smaller segment instead.

## Repeated-subject discipline

Subjects sent multiple times split into two groups:

**Winners reused 5+ times with stable performance:**
- "New Video on Jaw Placement / Your Questions Answered!" (6x at 4.83% avg)
- "Unlock Effortless High Notes with This Secret" (8x at 3.55% avg)
- "The top 5 Things That will absolutely Kill Your Endurance on the trumpet" (5x at 2.50% avg)

**Losers reused 5+ times with declining CTR (fatigue):**
- "Last chance to register for the free class happening tomorrow!" (8x at 0.46% avg)
- "5 free spots this week, then I close the calendar" (11x at 0.49% avg)
- "Reminder: Precision Brass FREE TRUMPET CLASS!" (7x at 0.56% avg)

**Rule:** the masterclass funnel needs subject-line rotation discipline. Don't send the same "Last chance" subject 8 times. Force 2-3 alternates per cycle. The agents drafting `webinar-push` audience emails must check the most recent 3 sends to that audience and reject any subject already used.

## Anti-recycling against the live broadcast log

When drafting, the auditor reads the last 30 days of broadcasts (queried from `email_proposals` joined with the AC perf cache, or from the dashboard's broadcast table data dump) and rejects any subject that:

- Matches an existing subject within Levenshtein-3
- Reuses a winning pattern within the same 14-day window (don't burn "New Video on Jaw Placement" twice in a fortnight)
- Reuses a losing pattern at all in the next 30 days (don't send "Last chance" again until at least one cycle of subject rotation has happened)

## How to use this file

Every drafting agent (1-8) receives this reference as load-once context alongside the voice catalog and the always-on masterclass corpus.

When drafting a subject:
1. Decide the archetype (technique-named-video / testimonial-with-numbers / failure-framed / masterclass-urgency / identity-call-out / utility-curiosity)
2. Pick the appropriate winning pattern from this file
3. Verify the opener, length, and punctuation against the checklist
4. If the draft is for a 4K+ broadcast, verify it maps to one of the three winning archetypes; otherwise downgrade audience or rewrite
5. Pass to Agent 9 for the auditor check, which now includes the rules above

## Provenance

Generated 2026-05-17 from `/api/ac?days=3650` (no list filter, all broadcasts) yielding 416 rows. Filter: send_amt > 50, not list-20-only, automation field empty (type_bucket='broadcast'). Composite score computed per row. Median, percentile, and lift figures from Python analysis on the full set. Update this file whenever the rolling 12-month dataset shifts materially (re-run the analysis quarterly, or after any A/B test that disconfirms a rule here).

## 2026-06-11 broadcast-efficiency upgrades (research-applied)

Sources: research cache `2026-05-31_daily-email-vs-weekly_5116e9a0` (Clearout, MailerLite, CodeCrew, Litmus), `2026-05-06_email-marketing-2026-best-practices_23fd6ecc` (SMTP2GO, Email Marketing Heroes, Vertical Response), `2026-05-23_hyros-attribution_bf7fd7b4`. Tooling: `scripts/email-perf-quadrant.py` + `voc/emails/raw/losing-emails/ANTI-PATTERNS.md`.

1. **Every email has a commercial job.** Daily email converts when every send bridges to ONE offer with ONE explicit CTA; value-only dailies train consumption, not buying, and produce high-open/low-click "invisible churn" (the open-trap pattern above is exactly this). One idea, one CTA, always a sell -- soft or hard.
2. **Quadrants over whole-email cloning.** Subject skill (opens) and body skill (CTR-of-opens) are independent. Borrow each from its own quadrant: CLONE SUBJECT donors for hooks, CLONE BODY donors for structure. Never borrow anything from AVOID (cross-check ANTI-PATTERNS.md).
3. **Hygiene thresholds (deliverability research):** unsubs > 0.5%/send = UNSUB-HOT (hollywood-bowl hit 0.68%); hard bounces > 1% = BOUNCE; Gmail/Yahoo throttle senders above ~0.3% complaint rate. The quadrant script flags these; a flagged email's pattern is NOT a clean donor even from CLONE WHOLE.
4. **Front-load the subject's scannable claim.** Apple Mail now AI-summarizes subject lines in preview; the first 4-6 words must carry the hook on their own.
5. **Engagement segmentation beats frequency.** Research default: full daily cadence to engaged openers (30d), reduced to moderates, win-back-then-suppress past 90d. 5-7 behavioral segments outperform demographic ones. (AC segment build = ops decision, Timo's call -- see SESSION_LOG 2026-06-11.)
6. **Per-email attribution: SUSPENDED (2026-06-11 evening).** The el=email-<slug> scheme assumed the registration-page link; Timo corrected the destination to the training-room VSL, which carries NO added params (first-touch protection). Until Timo adds a tagged variant to the registry, winner ranking stays clicks-based. The api/hyros.js email-prefix classifier rule stays (it correctly buckets legacy timoemail + any future tagged sends).
7. **Canonical link registry.** Master class CTA = `CANONICAL_MASTERCLASS_URL` in dashboard/lib/email-lint.js, byte-for-byte. The registration page (webinar-registration-pb) is BANNED in broadcasts (capture page; list is already captured). Lint blocks both wrong-destination and any non-canonical training-room variant.
