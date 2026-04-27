# Objection Lenses

Used by Agent 3 (Objection Dissolver). Each lens is a specific objection that stopped a prospect from buying. The agent's job: propose a video that pre-empts the objection BEFORE the sales call, so the prospect arrives already past it.

## The 8 objection lenses

Sourced from coaching-db's `mine-angles.md` and Precision Brass's `voc/personas/objection-library.md`.

| ID | Lens | What the prospect actually says | What's underneath |
|---|---|---|---|
| OBJ1 | mouthpiece-objections | "I've tried 50 mouthpieces" | Equipment-blame as identity protection (it's the gear, not me) |
| OBJ2 | financial-doubt | "Is this worth $X?" | Fear of being a sucker after past failed coaching |
| OBJ3 | time-doubt | "I don't have time to practice" | Fear of NOT being able to fix it even with time |
| OBJ4 | skeptical-of-coaches | "I've worked with 3 coaches before" | Loss-of-trust trauma; needs proof of difference |
| OBJ5 | technical-confusion | "I don't even know what's wrong" | Decision paralysis; can't commit to a fix without a diagnosis |
| OBJ6 | plateau-frustration | "Work hard, go nowhere" | Belief that effort is uncorrelated with outcome (learned helplessness) |
| OBJ7 | embarrassment | "I haven't played for anyone in years" | Shame as gatekeeper of action |
| OBJ8 | age-frame | "I'm too old / it's too late" | Pre-emptive permission to fail |

## Picking the lens

The agent rotates from this pool, picking the lens least-recently-used per `voices_used_log.jsonl` (`lenses` field). Same algorithm as fresh-lens picker.

## Pre-emption pattern

The proven move (verified in YouTube winners): name the objection in the first 30 seconds, validate it ("you're not wrong to think this"), then dismantle it with a specific reframe + demonstration.

### Pattern template

```
HOOK (first 15s): "If you've tried [X] for [Y years] and still can't [Z], I want to tell you why..."
VALIDATION (15-30s): "And before I say a word, I want to be clear: [the objection] is a completely reasonable thing to think. Most people in your position think it. I thought it too."
DISMANTLE (30-60s): "But here's what nobody told you: [the reframe]. Watch this."
DEMONSTRATION (60-180s): Visual proof on Harrison or a student.
RESOLUTION (180-end): "Now you know why [Y years] of [X] didn't work. The next move is [single CTA]."
```

## Required output (Agent 3)

1. Pick 1 objection lens (OBJ1 to OBJ8).
2. Find 3+ verbatim quotes from `voc/raw/sales-calls/` (sales call moments where the prospect raised the objection) AND 2+ quotes from `voc/personas/lost-deals-voice-bank.md`.
3. Propose 1 video idea using the pre-emption pattern.
4. Show the dismantle line (the specific reframe that flips the objection).

## Hard rules

- The video must address ONE objection, not three. Multi-objection videos dilute the conversion punch.
- Cite the exact sales-call moment where the objection appeared. File path + speaker name + paraphrased context.
- If the objection was already directly addressed in a YouTube winner, pick a different lens. (Cross-check `youtube-database/index.json` topic_tags.)
- The dismantle line MUST be falsifiable on camera (Harrison can DEMONSTRATE the reframe, not just claim it).
