# V2: MusicXML Path for Pitch and Rhythm Proofreading

This is the planned v2 architecture for catching music-content errors (wrong notes, bad rhythms, missing accidentals) that vision alone misses. Not built yet. Build when the user actually asks for pitch/rhythm proofreading against a reference.

## Why v2 is not just "OMR and diff the text"

A naive v1 of this would be: run Audiveris on both files, run `xmldiff`, done. That fails because:
- MusicXML is a permissive W3C standard. Voice ordering, time-slot representation, and note attribute ordering vary between exporters (Dorico vs Sibelius vs Finale vs Audiveris all emit slightly different MusicXML for identical music).
- `xmldiff` and other structural diffs flag these cosmetic differences as errors and drown the real catches.
- OMR accuracy plateaus around 90-99% on clean printed scores. Audiveris devs themselves concede "a 100% recognition ratio is simply out of reach." So even the reference file has OMR errors in it.

## The correct v2 architecture (crop-and-escalate)

```
1. Audiveris converts BOTH reference.pdf and engraver.pdf to MusicXML.
   (Ships as .dmg on macOS since 5.5, bundled JRE, no Java setup.)

2. music21 parses both files and walks a canonical key:
   (part_id, measure_number, voice, beat)

3. Semantic diff: for each matched key, compare tuples:
   (step, octave, alter, duration, stem_direction, articulations, dynamics, ties, slurs)
   Normalize enharmonic equivalents, voice ordering, and exporter-specific quirks
   BEFORE flagging a difference.

4. For each flagged measure, CROP the exact measure bbox from BOTH PDFs
   (the orchestrator calculates the bbox from MusicXML layout hints or
   falls back to dividing the page by system+measure count).

5. Spawn a vision subagent per flagged measure with a SPECIFIC prompt:
   "Here are two images of the same measure from two versions of a score
   and the MusicXML snippet from each. Does the music21 diff reflect a
   real musical difference, or is it an OMR artifact? Answer: real / artifact /
   ambiguous + one-sentence explanation."

6. Orchestrator merges verdicts into a proofread report, listing only REAL
   differences with page/measure/staff/description.
```

## Why this wins on cost

| Score size | Pure image approach | Hybrid v2 approach | Savings |
|-----------|---------------------|---------------------|---------|
| 100 pages | ~$0.47             | ~$0.06             | 8x      |
| 500 pages | ~$2.35             | ~$0.30             | 8x      |
| 1000 pages| ~$4.70             | ~$0.60             | 8x      |

Assumes 10-15% of measures get flagged by the music21 diff and escalated to vision.

## Required install

```bash
# Audiveris (.dmg from github.com/Audiveris/audiveris/releases, drag to /Applications)

# Python deps
pip3 install music21 lxml

# macOS helper for cropping measure regions
brew install poppler  # already installed typically; provides pdftoppm + pdftocairo
```

## Known gotchas (so future-us doesn't rediscover them)

1. **xmldiff breaks.** Use music21's walk-and-compare, not any structural XML differ.
2. **OMR is not deterministic.** Run Audiveris twice on the same file and you may get slightly different MusicXML. Deduplicate before diffing.
3. **Enharmonic equivalents are common false positives.** C# and Db are the same pitch. Normalize before comparing.
4. **Voice ordering varies.** Dorico puts voices in a different order than Audiveris. Sort voices by their first-note pitch before matching.
5. **Grace notes and cues are special.** They don't take beats. Handle their beat assignment explicitly.
6. **Audiveris CLI flags are not in Perplexity's or NotebookLM's source sets.** Pull directly from audiveris.github.io/audiveris before shipping. Likely format: `audiveris -batch -export -output OUTDIR input.pdf`. Verify.
7. **Haiku for cropped-measure comparison.** Per NotebookLM: workers on Haiku, orchestrator on Opus. Each crop is a small image (single measure, ~300px wide) so vision cost per escalation is pennies.

## When to build v2

Build this when:
- A real user request names pitch/rhythm/accidental errors as the thing they want caught
- The user has a reference score to compare against (v2 is not autonomous; needs a reference)
- Budget for ~1 day to wire Audiveris CLI + music21 diff + crop extraction + vision escalation prompt

Do NOT build v2:
- For visual engraving errors (v1 already does this well)
- For scores without a reference (semantic diff needs two files)
- As a pre-emptive optimization

## References

- NotebookLM synthesis: notebook `d08c042e-5b00-4d33-8857-5cad2af00434`
- Audiveris: https://audiveris.github.io/audiveris/
- music21: https://web.mit.edu/music21/
- MusicXML 4.0 spec: https://www.w3.org/2021/06/musicxml40/
