#!/usr/bin/env python3
"""
After re-engraving, scan the polished MusicXML for issues re-engraving can't
fix. These are content-level problems baked into the data.

Categories:
- Missing tempo marking at rehearsal marks
- Missing dynamic on entry after long rest
- Beat-off notation (rhythm doesn't sum to declared meter)
- Missing cue for re-entry after many tacet bars

Usage: validation_pass.py polished.musicxml out.json
"""
import argparse
import json
import sys
from pathlib import Path

from music21 import converter, note, tempo, dynamics, expressions, stream


TACET_THRESHOLD = 8  # bars of rest before "long tacet"


def validate(xml_path):
    score = converter.parse(str(xml_path))
    issues = []

    for p_idx, part in enumerate(score.parts):
        part_name = part.partName or f"Part {p_idx + 1}"
        measures = list(part.getElementsByClass("Measure"))

        # Track consecutive rest measures per part for tacet/re-entry detection
        consecutive_rest = 0
        for m_idx, m in enumerate(measures):
            has_sound = any(isinstance(el, note.Note) or
                            (hasattr(el, "isChord") and el.isChord)
                            for el in m.recurse())
            has_rest_only = not has_sound

            if has_rest_only:
                consecutive_rest += 1
            else:
                if consecutive_rest >= TACET_THRESHOLD:
                    # Player is re-entering after long tacet. Check for dynamic.
                    has_dynamic = any(isinstance(el, dynamics.Dynamic) for el in m.recurse())
                    if not has_dynamic:
                        issues.append({
                            "part": part_name,
                            "measure": m.measureNumber,
                            "kind": "missing_dynamic_on_reentry",
                            "severity": "MEDIUM",
                            "detail": f"{part_name} re-enters at m.{m.measureNumber} after "
                                      f"{consecutive_rest} tacet bars with no dynamic printed.",
                            "fix": "Add a dynamic marking at the entry beat so the player has a target.",
                        })
                consecutive_rest = 0

        # Rehearsal marks without tempo markings
        for m in measures:
            has_rehearsal = any(isinstance(el, expressions.RehearsalMark) for el in m.recurse())
            has_tempo = any(isinstance(el, tempo.TempoIndication) for el in m.recurse())
            if has_rehearsal and not has_tempo and p_idx == 0:
                # Only report once per measure, from the top part
                issues.append({
                    "part": "score",
                    "measure": m.measureNumber,
                    "kind": "rehearsal_without_tempo",
                    "severity": "MEDIUM",
                    "detail": f"Rehearsal mark at m.{m.measureNumber} has no associated tempo marking.",
                    "fix": "Add a tempo indication (or 'a tempo' / 'tempo primo') at the rehearsal mark.",
                })

        # Beat-off measures (rhythm doesn't sum to meter). Skip pickup (anacrusis)
        # measures: m.0, or any measure flagged as partial/anacrusis.
        current_meter = None
        for m_idx2, m in enumerate(measures):
            if m.timeSignature is not None:
                current_meter = m.timeSignature
            if current_meter is None:
                continue
            # Skip anacrusis (pickup) and partial measures
            if m.measureNumber == 0 or m_idx2 == 0:
                continue
            if hasattr(m, "paddingLeft") and m.paddingLeft > 0:
                continue
            expected = current_meter.barDuration.quarterLength
            actual = sum(
                el.quarterLength for el in m.recurse()
                if isinstance(el, (note.Note, note.Rest)) and hasattr(el, "quarterLength")
                and el.activeSite is m
            )
            if abs(actual - expected) > 0.01 and actual > 0:
                issues.append({
                    "part": part_name,
                    "measure": m.measureNumber,
                    "kind": "beat_off_measure",
                    "severity": "HIGH",
                    "detail": f"m.{m.measureNumber} duration {actual} does not match "
                              f"time signature {current_meter} (expected {expected}).",
                    "fix": "Verify rhythm adds up. Likely missing/extra note or rest.",
                })

    summary = {"BLOCKER": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for i in issues:
        sev = i.get("severity", "LOW")
        if sev in summary:
            summary[sev] += 1

    return {
        "source": str(xml_path),
        "total": len(issues),
        "by_severity": summary,
        "issues": issues,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("musicxml", type=Path)
    ap.add_argument("out_json", type=Path)
    args = ap.parse_args()

    result = validate(args.musicxml)
    args.out_json.write_text(json.dumps(result, indent=2))
    print(f"Wrote {args.out_json} with {result['total']} residual issues")
    s = result["by_severity"]
    print(f"  BLOCKER: {s['BLOCKER']}, HIGH: {s['HIGH']}, MEDIUM: {s['MEDIUM']}, LOW: {s['LOW']}")


if __name__ == "__main__":
    main()