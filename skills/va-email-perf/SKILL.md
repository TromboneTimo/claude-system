---
name: va-email-perf
description: Email performance analyzer for Victor Alegria / Victor Alegria Music. ALWAYS auto-loaded by pb-email at preflight (Step 0 in pb-email's load order). Calls the live /api/ac-perf endpoint to read past ActiveCampaign send performance, body content, and per-link click destinations. Returns a structured brief covering top 10 performers by open rate / CTR / reply rate, bottom 5 (anti-patterns), destination-mix breakdown (masterclass vs YouTube vs strategy-session vs Drive resource vs Zoom live), subject-pattern aggregates (length, question marks, numbers, day-of-week), and plain-English recommendations. The brief is consumed by pb-email so each new draft batch is informed by what actually worked, not just what feels right. Use when Timo says "/va-email-perf", "what's been performing", "email performance brief", "what's working on emails", "show me the perf data", or as the first step of any pb-email run.
---

> **CLONE NOTE (2026-05-25):** Cloned from Precision Brass. The orchestration logic and infra paths are re-pointed to Victor Alegria Music. BUT the VOICE, ICP, example scripts, conversion-trigger taxonomy, lens names, and locked-line templates in `references/` and `agents/` STILL CONTAIN PRECISION BRASS / HARRISON CONTENT. They must be re-derived from Victor's own VOC before this skill is run to produce real Victor content (Phase 5). This build excludes paid Meta ads.


# pb-email-perf. Email performance brief.

## When to fire

- **Auto, every pb-email run.** Step 0 of pb-email's voice load order calls this skill. The brief is read INTO the load-once context for every drafting agent. Without it, agents draft on intuition; with it, they draft against actual evidence.
- Manual: Timo says "/va-email-perf", "what's working on emails", "email perf brief", "show me what performs".

## What this does

Calls `https://precision-brass-dashboard.vercel.app/api/ac-perf?lookback_days=N` (default N=365) with the shared secret, gets back a structured brief covering 12+ months of ActiveCampaign sends. Then surfaces the brief as plain markdown the next agent (or Timo) can read.

The brief includes:

1. **Window**. how many sends in the analyzed window.
2. **Top 10 by open rate / CTR / reply rate**. subject + open % + ctr % + sent_at.
3. **Bottom 5 by open rate (anti-patterns)**. what NOT to imitate, send-volume normalized.
4. **Destinations across top-10 performers**. clicks by bucket: `youtube`, `masterclass`, `strategy-session`, `resource` (Google Drive), `zoom_live`, `social`, `other`. Tells you where engagement actually flows.
5. **Subject patterns**. average open rate by subject length (short/medium/long), question-mark presence, number presence, day-of-week.
6. **Top performer bodies**. first 8000 chars of body text from each top-10 performer, plus extracted P.S. block + inferred P.S. type.
7. **Recommendations**. plain-English bullets the next pb-email run should absorb.

The endpoint caches 1h fresh + 23h stale-while-revalidate, so repeated pb-email runs in the same day don't re-hit AC's API.

## How to fire

The skill is a thin wrapper. Steps:

1. Read `~/.claude/credentials/MASTER.md` to get the perf secret. Look for the `EMAIL_PERF_SECRET=` line under "Email perf analyzer".
2. Bash-curl the endpoint:
   ```bash
   SECRET=$(grep "^EMAIL_PERF_SECRET=" ~/.claude/credentials/MASTER.md | cut -d'=' -f2-)
   curl -sS -H "x-perf-secret: $SECRET" \
     "https://precision-brass-dashboard.vercel.app/api/ac-perf?lookback_days=365" \
     > /tmp/va-email-perf.json
   ```
3. Read `/tmp/va-email-perf.json` and pretty-print the brief in chat using the format below.
4. If pb-email called this, return the brief content as its function return value (it becomes preflight context for all 6 drafting agents).

## Output format

Return the brief as plain markdown matching this skeleton. Order matters: recommendations come last so the reader (human or agent) finishes with the action.

```markdown
# Email performance brief
**Window**: {sent_count} sends, {from_date} to {to_date}.
**Cache**: {fresh|stale|cold} per X-AcPerf-Cache header.

## Top 5 by CTR (skip outlier opens > 60%)
| CTR | Open | Date | Subject |
|---|---|---|---|
| 4.8% | 26.9% | 2025-08-18 | Did you forget this, %FIRSTNAME%? |
...

## Top 5 by open rate
| Open | CTR | Date | Subject |
...

## Anti-patterns (bottom 5 by open rate, sends >= 50)
| Open | Date | Subject |
...

## Where clicks actually go (top 10 performers)
| Destination | Clicks | % share |
|---|---|---|
| youtube | 135 | 35.5% |
| resource | 103 | 27.1% |
| strategy-session | 77 | 20.3% |
| masterclass | 61 | 16.1% |
...

## Subject patterns
- Short (under 36 chars): X% avg open
- Medium (36-55): Y%
- Long (over 55): Z%
- Has question mark: A% (yes) vs B% (no)
- Has number: C% (yes) vs D% (no)
- Best send day: {day} ({avg}%)
- Worst send day: {day} ({avg}%)

## Top performer bodies (digest)
For each of top 10 by open rate, show subject + first 200 chars of body + P.S. (if extracted) + per-destination click split.

## Recommendations for next pb-email run
- {plain-english bullet}
- {plain-english bullet}
- ...
```

## Failure modes

1. **Secret missing or wrong**. endpoint returns 401. Check MASTER.md and Vercel env.
2. **AC API down**. endpoint returns 502. The brief is unavailable; tell Timo "perf brief unavailable, drafting on instinct" and proceed.
3. **Stale data**. `X-AcPerf-Cache: stale` header means the cached entry is past 1h fresh but within 23h stale window. Acceptable; flag in output but proceed.
4. **Empty top performer bodies**. AC permissions or message-fetch failed. Brief still has stats; bodies degrade gracefully.

## What this skill is NOT

- Not a place to write new emails. That's pb-email.
- Not a place to push to dashboard. That's pb-email-push.
- Not a long-term storage layer. The brief lives in /tmp and is regenerated on demand.
- Not a substitute for reading the voice catalog or the FINAL emails. Performance data tells you WHAT worked, not HOW Victor's voice works. Both are required for pb-email.

## Maintenance

- The endpoint code is at `api/ac-perf.js` in the project repo.
- The URL classifier (in ac-perf.js, `classifyUrl()`) needs updating whenever Victor adds a new destination type. Currently buckets: youtube, masterclass, strategy-session, resource, zoom_live, social, hirose, reply, other.
- The shared secret rotates if needed: `vercel env rm EMAIL_PERF_SECRET production` then `vercel env add EMAIL_PERF_SECRET production` then update MASTER.md.
