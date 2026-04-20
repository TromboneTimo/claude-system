# Engraving Error Taxonomy (Positive Checklist, v2)

This is the complete error vocabulary the score-corrector flags. It is written as a POSITIVE checklist because negative instructions ("don't flag X") bias vision models against related visual issues. For every staff on every page, walk this checklist. Anything that matches a bullet is a real finding.

## 1. Collision

Two or more notation elements physically overlap or crowd each other into illegibility.

Flag these:
- **Dynamic-on-dynamic stacking.** `sfz` sitting directly on top of `mf` (or any two dynamics) with no vertical breathing room.
- **Dynamic + hairpin overlap.** `mf ff` written inline with a crescendo hairpin where the hairpin's tip or end collides with the letter glyphs.
- **Articulation + dynamic collision.** Accent (>), staccato (.), tenuto, or marcato glyphs crammed into the same vertical space as a dynamic letter or hairpin.
- **Trill + accent + dynamic pile-up.** Three or more ornament / articulation / dynamic elements crushed into the same tight vertical band.
- **Text label collision.** Instrument labels like "Tamb.Sn. Dr." (missing space) or rehearsal-letter text overlapping with time signature or tempo marking.
- **Tempo + rehearsal mark proximity.** Rehearsal box and tempo glyph touching or crushing the top staff line.
- **Accidental + notehead collision.** Sharp / flat / natural glyph physically touching the note it modifies.

## 2. Spacing

Elements don't overlap but the layout reads as cramped, uneven, or the defect is caused by too-tight spacing.

Flag these:
- **Staff spacing too tight.** Not enough vertical gap between two staves in the same system.
- **Uneven system spacing.** One system has 2x the vertical gap of the next for no musical reason.
- **Measure width inconsistency.** A dense 16th-note measure given the same horizontal space as a whole-rest measure.
- **No breathing room around hairpins.** Hairpin butts directly against barline or next dynamic.

## 3. Layout / Structural

How the score is organized, not how individual marks sit.

Flag these:
- **Inline staff sharing.** Two different instruments (e.g., Tamb. and Sn. Dr.) written on one staff with text labels switching between them mid-bar.
- **Disappearing staff.** A staff listed in the first-page instrumentation vanishes from subsequent pages with no "tacet" instruction.
- **System break mid-phrase.** Musical phrase split across a system break where the break interrupts the musical logic.
- **Page turn in busy passage.** Page turn falls on a measure where the player cannot physically turn the page.
- **Rehearsal mark floating.** Rehearsal letter placed far from the barline it's supposed to mark.

## 4. Consistency

Same musical idea notated differently in different places.

Flag these:
- **Dynamic placement flip-flop.** Dynamics written above the staff in one system and below the staff in the next, no musical reason.
- **Articulation inconsistency across like passages.** Same rhythmic figure marked with accents in one bar and unmarked in a parallel bar later.
- **Abbreviation inconsistency.** `Tamb.` in one bar, `Tambourine` in another, `Tam.` in a third.
- **Slur / tie style inconsistency.** Slur drawn as a shallow arc here and as a sharp peak there for the same melodic figure.
- **Beam grouping inconsistency.** 8th-notes beamed in groups of 3 in one bar and groups of 2 in an adjacent bar of the same meter.

## 5. Missing / truncated / malformed

Something that should be present but isn't, or something that IS present but is malformed or truncated. This category catches the "hole in the score" errors that vision models usually miss.

Flag these:
- **Missing tempo at section change.** New section (rehearsal mark, new meter, new feel) with no tempo marking.
- **Missing dynamic after long rest.** Player returns from a multi-bar rest with no dynamic for their re-entry.
- **Missing breath marks.** Wind or vocal line with no breath indication at a natural phrase end.
- **Missing cue.** Instrument tacet for many bars re-enters with no cue from another part printed above.
- **Missing key signature on new system.** New page or system doesn't repeat the key signature.
- **Missing courtesy accidental.** Chromatic note in a new bar where a courtesy accidental would prevent confusion.
- **Truncated rest figure.** A rest (whole, half, quarter, or multi-bar) that appears cut off, malformed, or trailing off into empty space instead of sitting cleanly on its rest line.
- **Truncated tie / slur.** Tie or slur that starts but has no terminus visible, or that curves into a staff edge.
- **Malformed multi-bar rest.** Multi-bar rest that doesn't show the count number, or shows a count that doesn't match the actual bar span.
- **Empty measure with no rest.** A measure with no notes and no rest glyph at all (should always have at least a whole rest).

## 6. Percussion-specific

Percussion staves use non-standard noteheads and conventions. These errors are the ones Tim sees instantly but general prompts miss.

Flag these:
- **Ghost notes not in parentheses or brackets.** Ghost notes should be visually distinct (parens, smaller heads, or bracketed) from normal notes. Flag when they are indistinguishable.
- **Ghost note misalignment.** Ghost notes not sitting cleanly on the same rhythm grid as the surrounding notes.
- **Grace notes crammed against primary notes.** Grace notes should have a small but clear horizontal gap before the primary note, not butted against the notehead.
- **Slash notation inconsistency.** Rhythm slashes in one measure and conventional noteheads in an adjacent measure for the same pattern.
- **X-noteheads vs filled noteheads mixed.** Same instrument using x-noteheads for one rhythm and filled noteheads for the next without a clear reason.
- **Mid-line meter change inside a measure.** A time signature glyph appearing partway through a measure rather than at a barline.
- **Rimshot / cross-stick notation missing its glyph.** "rim." or cross-stick x-notehead expected but absent.
- **Percussion staff-line count wrong.** Single-line percussion staff accidentally rendered with 5 lines, or vice versa.

## Severity levels

- **BLOCKER.** Will cause a reading error in rehearsal. Player will play wrong, miss entrance, or fail page turn.
- **HIGH.** Noticeable defect that will be criticized by conductor or section leader.
- **MEDIUM.** Clarity improvement.
- **LOW.** Stylistic polish.

## Structured verification protocol

For each staff on each page, DO NOT just "scan for problems." Instead, walk this checklist in order:

1. **Per-staff presence check.** Is this staff present? If absent, is there a tacet marker?
2. **Per-measure rest check.** Does every "empty" measure have a rest glyph? Is the glyph well-formed (no truncation)?
3. **Per-measure meter check.** Does the time signature appear ONLY at barlines? Any mid-measure meter glyphs?
4. **Per-note articulation check.** Are articulations clear of adjacent elements?
5. **Per-note dynamic check.** Are dynamics clear of hairpins, beams, and adjacent dynamics?
6. **Per-rehearsal-mark clearance check.** Does each rehearsal box have padding from staff lines and ledger notes?
7. **Per-percussion-staff special check.** If percussion, walk the percussion-specific checklist in section 6.
8. **Per-system margin check.** Does the system have at least one staff-space of vertical padding above and below?
9. **Per-page crossings check.** Do 8va brackets, pedal lines, and slurs cross into adjacent staves?

Structured verification produces significantly higher recall than open-ended scanning.

## What the subagent returns

Instead of pixel coordinates (which vision models return unreliably on dense music), return SEMANTIC anchors:

- `page` (int)
- `measure` (string, e.g., "10-12" or "rehearsal E")
- `staff` (string, the instrument name as it appears on the page)
- `staff_position` (one of: "top", "upper-middle", "middle", "lower-middle", "bottom") to help place a margin marker
- `category` (collision / spacing / layout / consistency / missing / percussion)
- `severity` (BLOCKER / HIGH / MEDIUM / LOW)
- `description` (what is wrong)
- `fix` (what to do)

No bounding box. No pixel coordinates. The annotator will use staff_position to place a small margin dot at the correct vertical level, and the errata PDF will list the full details.
