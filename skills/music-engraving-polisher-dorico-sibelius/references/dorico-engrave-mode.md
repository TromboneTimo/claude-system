# Dorico Engrave-Mode Quick Reference

When the polisher emits `dorico-instructions.md`, this file is the template the generator pulls from. Use this as a field guide when answering user questions about Dorico-specific fixes.

## Where the rules live in Dorico

- **Library > Engraving Options** (all score-level rules)
- **Library > Paragraph Styles** (text styles like rehearsal marks, tempo, dynamics)
- **Engrave mode > Graphic Editing tool** (per-object nudges)

## Most common adjustments

### Vertical spacing
- Library > Engraving Options > Vertical Spacing
- **Ideal gap between adjacent staves**: 7-8sp (moderate-strict)
- **Ideal gap between systems**: 9-10sp
- **Minimum gap from top of frame to first staff**: 5sp
- **Minimum gap from last staff to bottom of frame**: 5sp

### Dynamics
- Library > Engraving Options > Dynamics
- **Minimum gap between staff and dynamic**: 1sp
- **Default distance below bottom staff**: 3.5sp
- **Gap between dynamic and hairpin**: 0.5sp

### Rehearsal marks
- Library > Engraving Options > Rehearsal Marks
- **Default vertical position**: above top staff
- **Gap above top staff**: 3.5-4.5sp
- **Padding inside border**: 0.5-0.75sp

### Beams
- Library > Engraving Options > Beams
- **Beam slope limits**: preserve default (Dorico uses Gould-style already)

## Re-import workflow

If user wants to accept the polisher output wholesale:

1. File > Import > MusicXML, select `polished.musicxml`
2. Dorico creates a new flow. Your Engrave-mode tweaks from the original are NOT preserved.
3. Save as a new project or flow to keep the original as backup.

## Preserving Dorico overrides

If user has hand-placed dynamics, tweaked slurs, etc. in Engrave mode, those overrides ARE preserved on MusicXML export IF:
- User exports via File > Export > MusicXML (not just Share > PDF)
- User checks "Include Engrave mode overrides" in the MusicXML export dialog

Warn user to check that box before exporting to the polisher.