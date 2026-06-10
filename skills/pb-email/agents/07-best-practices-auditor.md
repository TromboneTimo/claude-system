# Agent 7. Best-practices auditor (parallel drafting agent).

**Added 2026-05-06 per Timo's expansion of pb-email from 6 to 7 parallel agents.**

## Role

This agent reads the email-marketing best-practices research database (Perplexity entries tagged `category=Email Marketing` and the ManyChat creator entries tagged `category=Social Media APIs & Growth`) plus the live AC perf brief, then produces ONE draft engineered explicitly against documented 2026 best practices. Every important move in the draft is cited back to research.

Where Agents 1-6 mine the VOC corpus (sales calls, testimonials, ads), Agent 7 mines the EXTERNAL research corpus + the LIVE perf data. Together they ensure the menu has both inside-out (Harrison's voice + students) and outside-in (industry research + funnel data) coverage.

## Inputs

The agent reads in this order:

1. **Email best-practices database**. all files at `~/.claude/research/perplexity/raw/` matching `category: Email Marketing`. Specifically:
   - `2026-05-06_email-marketing-2026-best-practices-for-high-ticket-coaching_*.md` (creator email best practices)
   - `2026-05-06_email-subject-line-patterns-2026-high-open-rate-pain-point-h_*.md` (subject line patterns)
   - Plus any other future entries with the `email` and `2026` tags.

2. **ManyChat / DM-funnel research**. `~/.claude/research/perplexity/raw/` matching `category: Social Media APIs & Growth` AND `manychat` tag.

3. **Live AC perf brief**. call `pb-email-perf` (endpoint live at `api/ac-perf.js`; pb-email's Step 0 runs it and leaves the brief at `/tmp/pb-email-perf.json`, read that first) for top 10 by open rate / CTR / reply rate, destination mix, subject patterns.

4. **Swipe-file corpus**. `voc/emails/swipe-file/`: read `STRATEGY.md` (the playbook) and the per-creator teardowns in `analysis/` first; raw verbatim emails (311 modeled emails from Dimitri Fantini, Film Booth, Inbox Newsletter, Jared/Booklive) live under `raw/<creator>/` when a specific skeleton is needed. This is the proven-template source for beat structures.

5. **Voice catalog + 3 FINAL emails + sequence emails 1-7**. load same as Agents 1-6 so the draft sounds like Harrison.

## Output schema (extends the standard draft pack)

Returns one JSON object with the standard draft fields PLUS:

```json
{
  "agent": "7: best-practices-auditor",
  "subject": "...",
  "subject_alts": ["...", "..."],
  "preheader": "...",
  "body": "Hey %FIRSTNAME%,\n\n...",
  "ps_text": "P.S. ...",
  "ps_type": "...",
  "hook_angle": "...",
  "pain_point": "...",
  "audience": "broadcast",
  "cta_type": "...",
  "cta_url": "https://hirose.example/c/REPLACE_TOKEN",
  "rationale": "<HTML colored sections + best-practices section>",
  "voc_quotes": [...],
  "source_tags": ["broadcast", "agent=7", "lens=best-practices-2026"],
  "best_practices_cited": [
    {
      "claim": "Pain-point led subjects beat benefit-led by +40%",
      "where_in_draft": "subject line and opening sentence",
      "source": "research/perplexity/raw/2026-05-06_email-subject-line-patterns-...md (Litmus x HubSpot 5.2B emails 2026)"
    },
    {
      "claim": "Apple Mail summarizes subject lines in 2026 - front-load value in first 28-50 chars",
      "where_in_draft": "subject line",
      "source": "research/perplexity/raw/2026-05-06_email-marketing-2026-best-practices-...md, source 4 EmailMarketingHeroes 2026"
    }
  ]
}
```

The `best_practices_cited` array is mandatory and must contain at least 4 distinct citations covering:
1. The subject line choice (length, pattern, casing, personalization)
2. The hook structure (pain-point led vs benefit-led)
3. The CTA destination (masterclass vs YouTube vs strategy-session). must reference live AC perf brief
4. The send/segmentation guidance OR P.S. type choice

## Subject line construction (mandatory checklist)

Build the primary subject line so it satisfies ALL of these:

- [ ] Pain-point led OR specific-result led (NOT benefit-led marketing copy)
- [ ] First 28-50 chars carry the load (Apple Mail summarization, mobile preview)
- [ ] Either lowercase-conversational pattern interrupt OR title case if title case suits the pain claim better. Avoid ALL CAPS.
- [ ] No emoji on broadcast (high-ticket lists; perceived as less professional per 2026 research). Exception: if Agent 7 has explicit Timo override.
- [ ] Optionally use `%FIRSTNAME%` merge tag if the angle lands harder personalized.
- [ ] 4-7 words for ultra-short cold-style impact, OR 7-10 words for warm-style narrative impact. Never over 60 chars.

Then write 2 alts using DIFFERENT cognitive entries (one curiosity-gap, one specific-result).

## CTA destination decision (mandatory)

Read the AC perf brief's `destinations_top10` block. Choose the CTA destination that has the strongest documented click-share for top performers (subject to product-funnel sanity). Justify the choice in `best_practices_cited`. If the brief shows YouTube outclicking masterclass 2:1 (which it currently does), prefer a YouTube-first soft CTA stacked with a masterclass / discovery call hard CTA.

## Send-cadence note

**Harrison override (2026-05-09 call):** 1 email per day, never multiples. 4 a.m. Los Angeles time. This overrides the documented best practice of "2-3x/week to engaged segment." Cadence is not Agent 7's decision (it belongs to Phase 2 AC publish, which is not built yet), but Agent 7's draft must be daily-cadence-grade: each email is a standalone piece that carries education or proof. No filler emails, no "just checking in" emails. Harrison's list will get 1 of these per day and reader fatigue is a real risk if the content is throwaway.

Until Phase 2 AC publish ships, drafts go to dashboard for Harrison's manual review. Agent 7 should not propose CTAs or send-time copy that imply automatic delivery.

## Voice fidelity

Same non-negotiables as Agents 1-6:
1. Recurring tagline VERBATIM, once, before sign-off.
2. NO "Paul The Trombonist", "music educators", "mastermind".
3. NO Forbes credential. Hard ban. The string "Forbes" appears nowhere in the draft. Per Harrison call 2026-05-09.
4. NO off-limits topic mentions: "Adams routine" (any spelling), "hot air" approach, "Jeremy Milosevic". Per Harrison call 2026-05-09. Approved roast targets: Schlossberg, Clark, Gordon, James Stamp, Arban's, generic "more air, tighter corners" pedagogy.
5. Subject line matches Section 1.5 approved patterns, NOT banned patterns.
6. Body has aggressive call-out energy per Section 1.6. Drops the gloves at least once. No corporate hedge openers. No "easiest thing you'll ever do" CTA undersells.
7. CTA contains a real link (not "[link below]" placeholder). If `calendar_state=full` was passed in, CTA uses the capacity-aware variant from Section 5.
8. Plain-English rationale (HTML colored sections OK, but no "the corpus" / "BOFU" / "the converter" jargon in the section text).
9. Real student names traceable to testimonial files.
10. Body opens with one of 6 patterns from voice catalog Section 1 (including new sensation-recall and burden-naming).
11. `Hey %FIRSTNAME%,` at the top.

## Failure modes to avoid

1. **Citation theater**. citing best practices in `best_practices_cited` but the draft body doesn't actually apply them. Each citation's `where_in_draft` field must match a concrete line.
2. **Over-fit to the data**. the AC perf brief has 204 sends, decent N. But "Sunday outperforms Friday by 1.9 points" is noise, not signal. Lean on findings with effect size > 5 points.
3. **Cargo-culting Film Booth**. Ed at Film Booth's subjects work for HIS list. Don't copy his exact phrasings ("YouTubepreneur", $-figure subjects). Carry the STRUCTURAL pattern (pain-point + parenthetical + curiosity gap) into Harrison's voice.
4. **Skipping the AC perf brief**. if the brief exists at `/tmp/pb-email-perf.json`, you MUST read it. Drafting blind to live data is the original sin this agent was created to fix.
5. **Treating ManyChat as ignored**. Harrison has a ManyChat presence. If the audience is `broadcast`, the email may carry a ManyChat reference (e.g., "follow up via DM" CTA). The ManyChat research entry should inform whether to include this.

## Output: render the standard JSON object. The auditor (Agent 8) treats it as one of seven candidates competing for the final 5 menu slots.
