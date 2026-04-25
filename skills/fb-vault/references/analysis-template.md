# Analysis Template (fb-vault)

Use this structure when writing `analysis.md` for a Facebook ad. Every claim cites a source. Sources to draw from:

- `context/prospect-psychology.md` (the 19-prospect deep psych dive, the central reference)
- `voc/personas/voice-bank.md` (general voice patterns)
- `voc/personas/won-deals-voice-bank.md` (sales-call quotes from buyers)
- `voc/personas/lost-deals-voice-bank.md` (quotes from prospects who didn't buy, especially for flops)
- `voc/personas/objection-library.md` (mapped objections by class)
- `voc/personas/comments-voice-bank.md` (commenter language from YouTube and Facebook)
- `voc/personas/harrison-email-voice.md` (Harrison's voice fingerprint)
- `voc/quotes/*.jsonl` (raw verbatim quotes if you need to grep)

## Required structure

### 1. Header block

```
# Analysis. <slug>

**Status:** WINNER | FLOP | UNRATED
**Sales attributed:** N (manual until DB sync)
**Spend:** $X | **Impressions:** N | **CTR:** X% | **CPA:** $X | **ROAS:** X
**Date range:** YYYY-MM-DD to YYYY-MM-DD
**Audience:** <named audience>
**Source files cited:** (list the .md files used)
```

### 2. TL;DR

3-5 numbered bullets. Each bullet ties one ad element to one psych principle. No fluff. If a bullet doesn't tie to a move + a principle, cut it.

### 3. Audience match (does it hit the ICP?)

Reference `context/prospect-psychology.md` lines 6-11 (ICP profile: 40-65, US, comeback). Did the audience targeting match the ICP? If the ad targeted "musicians 18-65" globally, that's a likely flop signal even if the creative was great. The wrong audience is the most common reason a good creative fails.

### 4. The 6-move ad framework

For each move, write:

> **Move name** (location in ad. e.g., "first 3 seconds," "headline," "body copy line 2")
>
> > "verbatim ad copy or screen description"
>
> - **What it tries to do:** the strategic intent
> - **Psych principle:** name the principle from `prospect-psychology.md` and cite the line number
> - **Validation:** quote a commenter, won-deal, or lost-deal that proves the move landed (or didn't)

The 6 moves to score against:

1. **Hook (first 3 sec for video, headline for static).** Does it stop the scroll? Does it name the universal pain in <15 words? Does it pattern-interrupt the feed?

2. **Promise / Big Idea.** What transformation is being promised? Range? Endurance? Effortlessness? Identity?

3. **Mechanism (the proprietary "how").** Does the ad name a system the viewer can't get elsewhere? VAS, Sim/Pa, Vertical Alignment, the Embouchure Truth, etc. Generic mechanism = no differentiation = no conversion.

4. **Proof.** What evidence supports the promise? Demonstration on camera (refrigerator effect), numbers, testimonials, lineage name-drops (Maynard, Dizzy, Donald Reinhardt), credentials.

5. **CTA + frictionless next step.** What action? "Learn more" vs "Watch free training" vs "Book strategy call". Does the destination URL match the ad's promise?

6. **Audience-named.** Does the ad address the prospect by their identity ("If you're a comeback player over 50...")? Per the psych dive, naming the prospect is one of the highest-converting moves because it answers "is this for me?" before they ask.

For winners, score how strongly each move was executed (weak / solid / strong). For flops, look for which moves are MISSING or BROKEN. The most common flop pattern is a strong hook + weak mechanism + vague CTA, which generates clicks but no conversions.

### 5. Comments map (if comments are available)

2-column table mapping commenter pain language to won-deals pain language from `voc/personas/won-deals-voice-bank.md`. If commenters complained, log it under "objection signals" so we can pre-empt next time.

### 6. Performance read

Three short paragraphs:

- **What the numbers say.** CTR vs platform average (~0.9% for FB feed, ~1.3% for video on this kind of audience), CPA vs Harrison's target, ROAS vs breakeven (1.0). Is the ad making money or burning it?
- **What the numbers DON'T say.** ROAS is lagging. A 7-day window may not capture a 30-day funnel. Note attribution windows.
- **Specific failure mode (for flops).** Was it: low CTR (hook problem), high CTR low conversion (promise/landing-page mismatch), low ROAS despite conversions (LTV problem, not creative problem)? Each has a different fix.

### 7. Reproducible pattern checklist

Markdown checklist. For winners, what to replicate in the next ad. For flops, what to fix. Format:

- [ ] **<thing>** (specific, actionable)

### 8. What we don't know yet

Honest list. Examples:
- Attribution beyond 7-day click window
- Whether sales came from THIS ad or the broader funnel exposure
- Audience overlap with other adsets running in parallel
- Whether the landing page was the bottleneck, not the ad

### 9. How to use this analysis

One paragraph explaining how the next ad creator (Claude or Timo or Harrison) should consume this file. The whole point is that the analysis becomes operational, not a postmortem.

---

## Quality bar

- Every claim has a source citation OR is flagged "we don't know yet"
- No vague descriptors ("strong hook," "weak CTA"). Always cite the specific copy line + psych principle.
- Verbatim ad copy in `> "..."` blockquote format. Verbatim customer quotes the same way.
- For flops: name which of the 6 moves are missing or broken. Be specific. "The mechanism is generic" is not enough. Quote the line and explain what would have made it specific.
- Always note ingestion confidence: "manual entry from Timo's notes" vs "Meta API export."

## Common ad-specific failure patterns to look for

- **The ICP mismatch.** Ad copy is great but audience is "musicians 18+ worldwide". CTR is OK, CPA is brutal.
- **The vague mechanism.** "Discover the secret to high notes" with no proprietary term. Sounds like every other trumpet ad.
- **The promise/landing-page break.** Ad promises "free 5-minute lesson," landing page asks for full webinar registration. Drop-off cliff.
- **The hookless hook.** First 3 seconds is Harrison saying "Hi, my name is Harrison Ball." Scroll past in 1.2 seconds.
- **The wrong CTA for the funnel stage.** Cold-audience ad asking for a strategy call (BOFU CTA) when the audience is TOFU. Or vice versa: warm retargeting ad with a soft "learn more" when they should be asking for the booking.
- **No identity callout.** Generic "trumpet players" instead of "comeback players over 50". Filters wrong.
