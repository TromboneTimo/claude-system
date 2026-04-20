# Engraving Error Taxonomy

This is the complete error vocabulary the score-corrector flags. Each error detected by a vision subagent must map to one of these `category` values. If something doesn't fit, propose a new category in the subagent's response. Don't silently bucket it under something wrong.

## 1. Collision (most common, highest-priority)

When two notation elements physically overlap or crowd each other into illegibility.

Flag any of these:
- **Dynamic-on-dynamic stacking:** `sfz` sitting directly on top of `mf` (or any two dynamics) with no vertical breathing room. Two simultaneous dynamics for the same note should be one combined marking, not stacked.
- **Dynamic + hairpin overlap:** `mf ff` written inline with a crescendo hairpin such that the hairpin's tip or end collides with the letter glyphs. Hairpin should terminate clearly before or after the dynamic.
- **Articulation + dynamic collision:** Accent `>`, staccato `.`, tenuto, or marcato glyphs crammed into the same vertical space as a dynamic letter or hairpin.
- **Trill + accent + dynamic pile-up:** Three or more ornament / articulation / dynamic elements crushed into the same tight vertical band above or below a note. The classic "everything on one note" collision.
- **Text label collision:** Instrument labels like `Tamb.Sn. Dr.` (missing space) or rehearsal-letter text overlapping with time signature or tempo marking.
- **Tempo + rehearsal mark proximity:** A rehearsal box like `D` and a tempo glyph like `♩. = 120` touching or crushing the top staff line.
- **Noteheads + articulations running into adjacent noteheads:** Usually happens at dense 16th-note passages where accent marks from one note visually enter the next note's space.

## 2. Spacing

Elements don't overlap but the layout reads as cramped or uneven.

Flag any of these:
- **Staff spacing too tight:** Not enough vertical gap between two staves in the same system, causing articulations from the top staff and dynamics from the bottom staff to nearly touch.
- **Uneven system spacing:** One system has 2x the vertical gap of the next for no musical reason.
- **Measure width inconsistency:** A dense 16th-note measure given the same horizontal space as a whole-rest measure, causing unreadable note compression.
- **No breathing room around hairpins:** Hairpin butts directly against barline or next dynamic.
- **Accidental too close to notehead:** Sharp / flat / natural glyph touching the note it modifies.

## 3. Layout / Structural

How the score is organized, not how individual marks sit.

Flag any of these:
- **Inline staff sharing:** Two different instruments (e.g., Tamb. and Sn. Dr.) written on one staff with text labels switching between them mid-bar. Each instrument needs its own staff, or the labels must be unambiguous and spaced.
- **Disappearing staff:** A staff listed in the first-page instrumentation vanishes from subsequent pages with no "tacet" instruction, no re-entry cue, and no indication whether it was intentionally auto-hidden.
- **System break mid-phrase:** A musical phrase split across a system break where the break interrupts the musical logic (e.g., split between upbeat and downbeat, or mid-slur).
- **Page turn in busy passage:** Page turn falls on a measure where the player cannot physically turn the page (continuous 16ths across the turn with no rests).
- **Rehearsal mark floating:** Rehearsal letter placed far from the barline it's supposed to mark.

## 4. Consistency

Same musical idea notated differently in different places.

Flag any of these:
- **Dynamic placement flip-flop:** Dynamics written above the staff in one system and below the staff in the next, with no musical reason.
- **Articulation inconsistency across like passages:** Same rhythmic figure marked with accents in one bar and unmarked in a parallel bar later.
- **Abbreviation inconsistency:** `Tamb.` in one bar, `Tambourine` in another, `Tam.` in a third.
- **Slur / tie style inconsistency:** Slur drawn as a shallow arc here and as a sharp peak there for the same melodic figure.
- **Beam grouping inconsistency:** 8th-notes beamed in groups of 3 in one bar and groups of 2 in an adjacent bar of the same meter, without a musical reason.

## 5. Missing elements

Something that should be present but isn't.

Flag any of these:
- **Missing tempo at section change:** New section starts (new rehearsal mark, new meter, new tempo feel) with no tempo marking.
- **Missing dynamic after long rest:** Player returns from a multi-bar rest with no dynamic indicated for their re-entry.
- **Missing breath marks:** Wind or vocal line with no breath indication at a natural phrase end.
- **Missing cue:** An instrument that's been tacet for many bars re-enters with no cue from another part printed above.
- **Missing key signature on new system:** New page or new system doesn't repeat the key signature.
- **Missing courtesy accidental:** Same chromatic note appears in a new bar where a courtesy accidental would prevent confusion.

## Severity levels

Use these exactly. The annotation script colors boxes by severity.

- **BLOCKER:** Will cause a reading error in rehearsal. A player will play the wrong note, miss an entrance, or fail to turn the page. Fix before distributing parts.
- **HIGH:** Noticeable engraving defect that will be criticized by the conductor or section leader but won't stop the rehearsal.
- **MEDIUM:** Clarity improvement. Not broken, just not polished.
- **LOW:** Stylistic polish. Fix if time allows.

## What NOT to flag

- Pitch / rhythm / harmonic content (that's a v2 MusicXML-path job)
- Stylistic engraver preferences (curly vs flat slurs, etc.) unless inconsistent
- Any element you can't see clearly at 1024px resolution. Mark that page as `needs_higher_res: true` in your response instead of inventing an error.
