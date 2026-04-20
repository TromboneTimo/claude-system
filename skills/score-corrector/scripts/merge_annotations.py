#!/usr/bin/env python3
"""
Merge per-batch JSON outputs from vision subagents into a single annotations.json
that annotate_pdf.py can consume.

Input: directory containing batch-*.json files, each with this shape:
  {
    "batch_pages": [1, 2, 3, 4, 5],
    "errors": [ { "page": 1, ... }, ... ],
    "pages_needing_higher_res": []
  }

Output: single annotations.json with errors renumbered globally, sorted by page,
plus a summary of which pages need higher-res rerun.

Usage:
  python merge_annotations.py batches_dir/ out_annotations.json \
      --title "Score Title" --arranger "Arranger Name" --total-pages 100
"""
import argparse
import json
import sys
from pathlib import Path


SEVERITY_RANK = {"BLOCKER": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batches_dir", type=Path)
    ap.add_argument("out_path", type=Path)
    ap.add_argument("--title", default="Untitled score")
    ap.add_argument("--arranger", default="")
    ap.add_argument("--total-pages", type=int, required=True)
    args = ap.parse_args()

    batches = sorted(args.batches_dir.glob("batch-*.json"))
    if not batches:
        print(f"No batch-*.json files in {args.batches_dir}", file=sys.stderr)
        sys.exit(1)

    all_errors = []
    higher_res_pages = set()

    for batch_file in batches:
        try:
            data = json.loads(batch_file.read_text())
        except json.JSONDecodeError as e:
            print(f"WARNING: could not parse {batch_file}: {e}", file=sys.stderr)
            continue
        all_errors.extend(data.get("errors", []))
        higher_res_pages.update(data.get("pages_needing_higher_res", []))

    # Sort: by page number, then by severity (BLOCKER first), then by y position
    def sort_key(e):
        page = e.get("page", 0)
        if isinstance(page, str):
            page = 9999  # string pages like "throughout" go last
        sev = SEVERITY_RANK.get(e.get("severity", "LOW"), 99)
        y = e.get("region", {}).get("y_pct", 0)
        return (page, sev, y)

    all_errors.sort(key=sort_key)

    # Renumber globally
    for i, err in enumerate(all_errors, start=1):
        err["id"] = i

    # Severity counts for summary
    counts = {"BLOCKER": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for err in all_errors:
        sev = err.get("severity", "LOW")
        if sev in counts:
            counts[sev] += 1

    out = {
        "score_title": args.title,
        "arranger": args.arranger,
        "analyzed_by": "score-corrector (vision batch pipeline)",
        "total_pages": args.total_pages,
        "severity_legend": {
            "BLOCKER": "Must fix before sending to players. Will cause reading errors.",
            "HIGH": "Should fix. Noticeable engraving defect.",
            "MEDIUM": "Recommended fix. Improves clarity.",
            "LOW": "Stylistic consistency. Fix if time allows.",
        },
        "severity_counts": counts,
        "pages_needing_higher_res": sorted(higher_res_pages),
        "errors": all_errors,
    }

    args.out_path.write_text(json.dumps(out, indent=2))
    print(f"Wrote {args.out_path} with {len(all_errors)} errors "
          f"(BLOCKER: {counts['BLOCKER']}, HIGH: {counts['HIGH']}, "
          f"MEDIUM: {counts['MEDIUM']}, LOW: {counts['LOW']})")
    if higher_res_pages:
        print(f"  {len(higher_res_pages)} pages flagged for higher-res rerun: "
              f"{sorted(higher_res_pages)}")


if __name__ == "__main__":
    main()
