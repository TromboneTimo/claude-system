# Engraving Rules Reference (Gould's Behind Bars + house style)

These are the rules encoded in the three `.mss` style presets. Rationale comes from Elaine Gould's *Behind Bars: The Definitive Guide to Music Notation* and common publisher practice (Bärenreiter, Henle, Boosey).

## Spacing

- **Notehead to accidental**: min 0.22sp (moderate) / 0.25sp (strict)
- **Accidental column within beat**: min 0.3sp (moderate) / 0.35sp (strict) between stacked accidentals
- **Note to barline**: min 1.2sp (moderate) / 1.3sp (strict)
- **Minimum note distance**: 1.2sp (moderate) / 1.4sp (strict)

## Staff and system

- **Staff distance** (within a system): 7sp (moderate) / 8sp (strict)
- **Grand-staff / bracket distance**: 6.5sp (moderate) / 7sp (strict)
- **Min system distance**: 9sp (moderate) / 10sp (strict)
- **Upper / lower staff border**: 7sp (moderate) / 8sp (strict)

## Dynamics and hairpins

- **Dynamics to staff clearance**: min 1sp (strict) / 0.5sp (moderate)
- **Hairpin default height**: 1.2sp
- **Hairpin to dynamic separation**: 0.5sp horizontal minimum

## Articulations

- **Articulation to neighbor**: min 0.75sp (strict) / 0.5sp (moderate)
- Anchor default: above staff for stem-down notes, below for stem-up

## Rehearsal marks

- **Frame padding**: 0.5sp (moderate) / 0.75sp (strict)
- **Gap above top staff**: 3.5sp (moderate) / 4.5sp (strict)

## Tempo

- **Gap above top staff**: 4sp (moderate) / 5sp (strict)
- Always placed above rehearsal mark if both are present

## Beaming

- Respect meter grouping (6/8 = two groups of 3, 4/4 = groups of 2 or 4)
- Never beam across beats without explicit markup
- Beam angle: prefer flat to gentle slope; never extreme

## Rests

- **Multi-measure rests**: only consolidate when 2+ empty bars
- Minimum MM-rest width: 4sp (moderate) / 5sp (strict)

## Casting-off

- **Minimum measure width**: 5sp (moderate) / 6sp (strict)
- Respect explicit system / page break instructions
- Otherwise allow MuseScore to re-flow

## Slurs and ties

- **Default slur height**: 1.2sp
- **Asymmetric curve** for slurs longer than 4 beats
- **Tie min length**: 1sp (moderate) / 1.2sp (strict)
- Never cross staff lines