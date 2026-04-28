# Email rotation protocol

Mirrors pb-script's `voice-diversity-protocol.md`. Prevents the corpus from sounding like Robbie's diary instead of Voice of Customer evidence.

## Why rotation matters

Harrison's corpus has 28 sales calls and 11 testimonials. If every email cites the same 4 names (Robbie, Mike, Heather, Phil), the email engine produces drafts that feel repetitive and flatten Harrison's authority. Rotation forces fresh voices into every menu.

## State file

`voc/email_voices_used_log.jsonl` (one JSON object per line, append-only).

Each line records one pb-email run:

```jsonl
{"run_at":"2026-04-28T15:30:00Z","audience":["broadcast"],"voices":["Karen","Joe","Joinville","Mike","fresh-lens-isolation"],"draft_subjects":["..."],"sales_calls_used":["voc/raw/sales-calls/2026-03-12_karen.md"],"testimonials_used":["voc/raw/testimonials/joe-isolation.md"]}
```

If the file does not exist, create it empty (zero bytes, no header) before the first run.

## Rotation algorithm (run BEFORE spawning drafting agents)

1. Read the last 3 entries of `voc/email_voices_used_log.jsonl`.
2. Build the off-limits set: union of all `voices` from those entries.
3. Build the off-limits sales-call set: union of all `sales_calls_used`.
4. Build the off-limits testimonial set: union of all `testimonials_used`.
5. List all available files:
   - Sales calls: `ls voc/raw/sales-calls/*.md`
   - Testimonials: `ls voc/raw/testimonials/*.md`
6. Pick fresh slots:
   - Sales-call anchor (Agent 1): random pick from `available_sales - off_limits_sales_calls`. If empty, fall back to least-recently-used (oldest entry in log).
   - Testimonial proof (Agent 2): random pick from `available_testimonials - off_limits_testimonials`. Same fallback.
   - Objection lens (Agent 3): least-recently-used from `pb-script/references/objection-lenses.md` OBJ1 to OBJ8 list.
   - Fresh lens (Agent 6): least-recently-used from the fresh lens list (below).

Print the rotation picks in chat before spawning agents. This is the "showing the work" step that lets Timo redirect if a slot picks something that does not fit the audience.

## Fresh lens list (12 lenses, rotate)

For Agent 6 when not in discovery-followup mode:

1. dental-trigger (specific physical event triggered comeback)
2. isolation (player who hides their playing from peers)
3. age-anxiety (over-50 fear they are out of time)
4. comeback-arc (player returning after years away)
5. failed-method-grief (anger at past teachers)
6. equipment-confusion (mouthpiece-and-horn paralysis)
7. plateau-frustration (range or endurance ceiling)
8. perfectionism-paralysis (won't play in front of anyone)
9. legacy-anxiety (wants to play before it is too late)
10. orchestral-aspiration (gigs they want back)
11. teaching-shame (private teacher who can't play what they teach)
12. recovery-after-injury (medical or dental incident knocked them out)

## Voices_used_log append (after every run)

After Timo picks (or rejects all 5), append a new line to `voc/email_voices_used_log.jsonl`:

```jsonl
{"run_at":"<ISO timestamp>","audience":["<tags>"],"voices":["<primary voice per draft, in menu order>"],"draft_subjects":["<subject 1>","<subject 2>",...],"sales_calls_used":["<path>"],"testimonials_used":["<path>"]}
```

This advances rotation even if Timo bins all 5 drafts and asks for a fresh menu. The next run sees these voices as off-limits and forces fresh slots.

## When rotation fails to pick fresh

If all sales calls or all testimonials have been used in the last 3 runs (rare, but possible after 9 weekly menus), surface this to Timo:

> "Heads up: every sales call has been used in the last 3 runs. Reusing the oldest one (Robbie 2026-02-14) for Agent 1. We are due for new corpus ingestion."

Do NOT silently reuse without flagging.

## Voice freshness override

If a drafting agent insists a recently-used voice is the right anchor for this audience (e.g. the testimonial perfectly matches a re-engagement angle that no fresh voice can match), it can include `freshness_override` in its return:

```json
{
  "voice": "Robbie",
  "freshness_override": "Robbie's recovery arc is the only testimonial that names the dental-trigger pain point head on, and the audience is reengagement of subscribers who churned post-injury. No fresh voice covers this exact arc."
}
```

The auditor (agent 7) reviews the override. If it accepts, the draft stays in the menu and the override is logged in `voc/email_voices_used_log.jsonl` so future runs can see why a recent voice was reused.
