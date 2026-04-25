# Analysis Template (yt-vault)

Use this structure when writing `analysis.md` for a new video. Every section must cite at least one source file. Sources to draw from:

- `context/prospect-psychology.md` (the 19-prospect deep psych dive, the central reference)
- `voc/personas/comments-voice-bank.md` (commenter quotes, often video-specific)
- `voc/personas/won-deals-voice-bank.md` (sales-call quotes from buyers)
- `voc/personas/lost-deals-voice-bank.md` (quotes from prospects who didn't buy)
- `voc/personas/objection-library.md` (mapped objections by class)
- `voc/personas/harrison-email-voice.md` (Harrison's voice fingerprint)
- `voc/quotes/*.jsonl` (raw verbatim quotes if you need to grep)
- `references/converting-video-embouchure-transcript.md` (the proven-converter template, 12 moves)

## Required structure

### 1. Header block

```
# Analysis. <title>

**Status:** WINNER | FLOP | UNRATED
**Sales attributed:** N (placeholder until DB sync)
**Views:** N | **Likes:** N (X% rate) | **Comments:** N
**Upload date:** YYYY-MM-DD | **Duration:** MM:SS
**Source files cited:** (list the .md files you use)
```

### 2. TL;DR

3-5 numbered bullets. Each bullet is one reason the video performed (or flopped). No fluff. If a bullet doesn't tie to a structural move OR a psych-dive principle, cut it.

### 3. Audience match (does it hit the ICP?)

Reference `context/prospect-psychology.md` lines 6-11 (ICP profile). Find at least one verbatim commenter quote that proves the ICP showed up. If the ICP didn't show up, that's a flop signal. Say so.

### 4. Structural moves

For each move, write:

> **Move name** (timestamp `[mm:ss]`)
>
> > "verbatim quote from the transcript"
>
> - **Psych principle:** name the principle from `prospect-psychology.md` and cite the line number
> - **Validation:** verbatim commenter or won-deals quote that proves the move landed (or didn't)

Aim for 8-12 moves on a winner. Aim for 3-5 missing-or-broken moves on a flop.

For winners, the canonical 12 moves to look for (from the embouchure converter):

1. Cold open with universal pain (<15 sec)
2. Collapses many problems into ONE root cause (<60 sec)
3. Credibility without bragging
4. Anti-conventional wisdom hook ("99% of teachers say... but in reality...")
5. Proprietary terminology (VAS, Sim/Pa, Type 1/2, Unfurling)
6. Lineage name-drops (3+ legends or teachers)
7. Demonstrates as he talks (refrigerator effect, effortless playing on camera)
8. Identity layer ("the way we play is the way we live")
9. Specific consequences of NOT fixing it (TMJ, swelling, etc)
10. Cliffhanger CTA to next video
11. Step-list recap at the end (chantable)
12. Comments section as the funnel (Harrison reply + webinar link drop)

### 5. What the comments confirm

A 2-column table mapping commenter pain language to won-deals pain language. Use this to prove that the video's pain framing matches paying customers' pain framing. If the table is sparse, the video drew the wrong audience.

### 6. Reproducible pattern checklist

Markdown checklist. Each row is one thing the next long-form must do to replicate this video's success. Format:

- [ ] **<thing>** (specific, actionable, scriptable)

### 7. What we don't know yet

Honest list of unknowns. Examples:
- Sales attribution mechanism (description link vs comment-CTA vs bio link)
- Retention curve (need YouTube Studio data)
- Whether view count is normal for this channel (need baseline)
- Click-through on the tracking link

### 8. How to use this analysis

One paragraph explaining how a future scriptwriter (Claude or Timo) should consume this file. The whole point is that the analysis becomes operational, not a postmortem on a shelf.

---

## Quality bar

- Every claim has a source citation OR is flagged as "we don't know yet"
- No vague descriptors ("great hook," "strong open"). Always cite the specific timestamp + transcript line + psych principle.
- For flops: actively look for which of the 12 canonical moves are MISSING or BROKEN. That's the lesson.
- Verbatim quotes always appear in `> "..."` blockquote format. Never paraphrase a customer.
- Always note transcript confidence: "auto-caption, medium confidence, verify exact wording before using in production."
