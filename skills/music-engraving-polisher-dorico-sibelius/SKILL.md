---
name: music-engraving-polisher-dorico-sibelius
description: Automatically polishes and re-engraves sheet music scores from Dorico or Sibelius. Prioritizes MusicXML re-engraving with strict professional rules (MuseScore CLI + engraving style presets) for cleaner results than visual detection alone. Falls back to Audiveris OMR when only PDF/image is available. Outputs clean MusicXML, publication-ready PDF, before/after diff report, side-by-side comparison PDF, and Dorico/Sibelius Engrave-mode step-by-step instructions. Use this skill whenever the user uploads a score (MusicXML, MXL, PDF, or image), mentions engraving errors, collisions, polishing, proofreading, publisher-ready output, or says "clean up this score," "make this score publisher-ready," "re-engrave this," "fix the engraving," or "polish this score." Also use when the user exports from Dorico or Sibelius and wants their score to look professional.
---

# Music Engraving Polisher (Dorico / Sibelius)

Takes a messy Dorico or Sibelius export and produces a publisher-grade version by re-engraving through MuseScore with strict Behind-Bars-style rules. This is fundamentally different from visual proofreading: instead of finding defects, the polisher ELIMINATES them by letting a clean engraving engine re-flow the entire score.

## When to use this skill (non-exhaustive triggers)

The user hands you a MusicXML, MXL, or PDF and asks any of:
- "polish this score" / "make this publisher-ready" / "clean up the engraving"
- "re-engrave this" / "re-flow this"
- "fix the collisions / spacing / dynamics / rehearsal marks"
- "I exported from Dorico, it looks rough"
- "Sibelius gave me an ugly layout, can you fix it"
- "proofread this score" (the polisher handles ~90% of what proofreading would catch, just by eliminating the defects instead of reporting them)

## What this skill DOES

1. Loads the user's MusicXML (or extracts one from PDF via Audiveris OMR, auto-installing if needed)
2. Renders the original PDF for before/after comparison baseline
3. Re-engraves the score through MuseScore CLI with a strict style (`moderate`, `strict`, or `conservative` preset)
4. Emits clean polished MusicXML + publication-ready PDF
5. Diffs before/after at the content level (should be near-zero if re-engrave is pure layout)
6. Runs a validation pass for issues re-engraving can't fix (missing tempos, missing re-entry dynamics, beat-off measures)
7. Renders a side-by-side comparison PDF
8. Generates step-by-step Engrave-mode instructions for both Dorico and Sibelius so the user can replicate the polish settings in their own project

## What this skill DOES NOT do

- Invent missing content (wrong notes, missing tempos, missing cues stay missing until the composer adds them)
- Modify the composer's musical intent (articulations, voice assignments, specific dynamic values are preserved)
- Guarantee OMR accuracy on PDF-only inputs (Audiveris is 90-99% accurate; the skill warns in output)

## Workflow

### Primary path (MusicXML in)

```bash
python3 ~/.claude/skills/music-engraving-polisher-dorico-sibelius/scripts/polish.py \
    <input.musicxml> <out_dir/> [--style moderate|strict|conservative]
```

The `polish.py` orchestrator runs all 8 steps above. Default style is `moderate`.

### Fallback path (PDF in)

Same command, same CLI. `polish.py` detects PDF input, runs `pdf_to_musicxml.sh` which will auto-install Audiveris from GitHub Releases on first use (~100MB, one-time download). Then the workflow continues as primary.

If Audiveris install fails, the skill tells the user to export MusicXML directly from Dorico or Sibelius and rerun.

## Output files

Written to the user-specified `out_dir/`:

- `polished.musicxml` - clean MusicXML, ready to re-import into Dorico or Sibelius
- `polished.pdf` - publication-ready PDF
- `original.pdf` - baseline rendering of the input for comparison
- `before-after.pdf` - landscape, original on left and polished on right, page-by-page
- `changes.json` - music21 content-level diff of before vs after (should be small for style-only polish)
- `residual_issues.json` - list of issues re-engraving could not fix, severity-tagged
- `dorico-instructions.md` - how to apply equivalent settings in Dorico Engrave mode
- `sibelius-instructions.md` - same for Sibelius

## Style presets

- `moderate` (DEFAULT): Dorico-ish defaults with tightened spacing. Safest choice. Good for 95% of scores.
- `strict`: Elaine Gould's Behind Bars / publisher-grade. Generous spacing, aggressive re-flow, stricter minimums. Use for final publisher-bound output.
- `conservative`: Minimal changes. Preserves composer's explicit formatting as much as possible. Use when the user has spent hours tweaking layout manually and just wants collision floors enforced.

## Dependencies (auto-check at first run)

- MuseScore 4 (install at `/Applications/MuseScore 4.app` via musescore.org if missing)
- Python packages: `music21`, `pypdf`, `reportlab`, `Pillow` (install via `pip3`)
- Audiveris (auto-installed on first PDF input)

## Relationship to score-corrector

The old `score-corrector` skill (vision-based proofreader) has been retired. The polisher handles ~90% of what score-corrector was catching, because it eliminates defects rather than reporting them. The remaining ~10% (missing tempos, missing re-entry dynamics, beat-off measures) is caught by the validation pass inside polish.py.

## Persona

Act as a world-class professional music engraver with 20+ years at Dorico / Sibelius level. Hyper-critical but constructive. When explaining outputs to the user, always say WHY a change was made, not just what changed. Token-efficient: do not pre-render preview images or chatter through the workflow. One-shot the orchestrator and explain the outputs.

## References (just-in-time loading)

- `references/engraving-rules.md` - Gould's Behind Bars rules with rationale
- `references/dorico-engrave-mode.md` - Dorico-specific fix instructions
- `references/sibelius-engrave-mode.md` - Sibelius-specific fix instructions
- `references/fallback-workflow.md` - what to do if MusicXML isn't available
- `references/style-preset-comparison.md` - when to pick each preset