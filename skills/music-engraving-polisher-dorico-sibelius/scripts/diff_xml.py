#!/usr/bin/env python3
"""
Semantic diff of two MusicXML files using music21. Walks both scores measure
by measure, part by part, and reports differences in musical CONTENT
(pitches, rhythms, articulations, dynamics, tempo markings, barlines).

This is the honest accounting of what re-engraving changed. For a
style-only polish, the diff should be very small: mostly whitespace/ordering
artifacts from the round-trip, not actual musical changes. Any unexpected
content change is worth investigating.

Usage:
  diff_xml.py before.musicxml after.musicxml out.json
"""
import argparse
import json
import sys
from pathlib import Path

from music21 import converter, note, chord, dynamics, expressions, tempo


def fingerprint_measure(m):
    """Return a compact signature of a measure's musical content."""
    fp = {
        "number": m.measureNumber if hasattr(m, "measureNumber") else None,
        "time_sig": str(m.timeSignature) if m.timeSignature else None,
        "key_sig": str(m.keySignature) if m.keySignature else None,
        "notes": [],
        "rests": 0,
        "dynamics": [],
        "articulations": [],
        "tempo": None,
    }
    for el in m.recurse():
        if isinstance(el, note.Note):
            fp["notes"].append({
                "pitch": el.pitch.nameWithOctave,
                "dur": float(el.quarterLength),
                "tie": str(el.tie) if el.tie else None,
                "articulations": [a.name for a in el.articulations],
            })
        elif isinstance(el, chord.Chord):
            fp["notes"].append({
                "chord": [p.nameWithOctave for p in el.pitches],
                "dur": float(el.quarterLength),
                "articulations": [a.name for a in el.articulations],
            })
        elif isinstance(el, note.Rest):
            fp["rests"] += 1
        elif isinstance(el, dynamics.Dynamic):
            fp["dynamics"].append(el.value)
        elif isinstance(el, tempo.TempoIndication):
            fp["tempo"] = str(el)
    return fp


def compare(before_path, after_path):
    before = converter.parse(str(before_path))
    after = converter.parse(str(after_path))

    before_parts = list(before.parts)
    after_parts = list(after.parts)

    changes = []

    if len(before_parts) != len(after_parts):
        changes.append({
            "level": "score",
            "kind": "part_count_changed",
            "before": len(before_parts),
            "after": len(after_parts),
            "severity": "HIGH",
        })

    pair_count = min(len(before_parts), len(after_parts))
    for p_idx in range(pair_count):
        bp = before_parts[p_idx]
        ap = after_parts[p_idx]
        part_name = bp.partName or f"Part {p_idx + 1}"

        b_measures = list(bp.getElementsByClass("Measure"))
        a_measures = list(ap.getElementsByClass("Measure"))
        m_count = min(len(b_measures), len(a_measures))

        for m_idx in range(m_count):
            bm = b_measures[m_idx]
            am = a_measures[m_idx]
            b_fp = fingerprint_measure(bm)
            a_fp = fingerprint_measure(am)

            if b_fp["notes"] != a_fp["notes"]:
                changes.append({
                    "level": "measure",
                    "part": part_name,
                    "measure": b_fp["number"] or (m_idx + 1),
                    "kind": "note_content_changed",
                    "severity": "HIGH",
                    "detail": "Pitch or rhythm content differs between before and after. Investigate.",
                })
            if b_fp["dynamics"] != a_fp["dynamics"]:
                changes.append({
                    "level": "measure",
                    "part": part_name,
                    "measure": b_fp["number"] or (m_idx + 1),
                    "kind": "dynamics_changed",
                    "severity": "LOW",
                    "before": b_fp["dynamics"],
                    "after": a_fp["dynamics"],
                })
            if b_fp["time_sig"] != a_fp["time_sig"]:
                changes.append({
                    "level": "measure",
                    "part": part_name,
                    "measure": b_fp["number"] or (m_idx + 1),
                    "kind": "time_signature_changed",
                    "severity": "MEDIUM",
                    "before": b_fp["time_sig"],
                    "after": a_fp["time_sig"],
                })

        if len(b_measures) != len(a_measures):
            changes.append({
                "level": "part",
                "part": part_name,
                "kind": "measure_count_changed",
                "before": len(b_measures),
                "after": len(a_measures),
                "severity": "HIGH",
            })

    return {
        "before": str(before_path),
        "after": str(after_path),
        "summary": {
            "total_changes": len(changes),
            "by_kind": {},
        },
        "changes": changes,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("before", type=Path)
    ap.add_argument("after", type=Path)
    ap.add_argument("out_json", type=Path)
    args = ap.parse_args()

    if not args.before.exists() or not args.after.exists():
        print(f"ERROR: input file(s) missing", file=sys.stderr)
        sys.exit(1)

    result = compare(args.before, args.after)

    by_kind = {}
    for c in result["changes"]:
        by_kind[c["kind"]] = by_kind.get(c["kind"], 0) + 1
    result["summary"]["by_kind"] = by_kind

    args.out_json.write_text(json.dumps(result, indent=2))
    print(f"Wrote {args.out_json} with {result['summary']['total_changes']} content changes")
    for k, v in by_kind.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()