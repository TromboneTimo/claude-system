"""
fb-vault ad processor.

Builds the structured fb-vault folder for one Facebook ad. Unlike yt-vault,
this is fully manual ingestion. Pass everything the skill knows about the ad
on the command line, and the script writes the metadata, performance, and
copy files. Then Claude writes analysis.md by hand using the references.

Usage:

  python3 process_ad.py \\
    --ad-id manual-001 \\
    --slug pain-hook-comeback \\
    --status winner \\
    --sales 4 \\
    --launch-date 2026-04-10 \\
    --primary-text "$(cat /tmp/copy.txt)" \\
    --headline "Stop fighting for high notes" \\
    --description "" \\
    --cta "Learn More" \\
    --destination-url "https://precisionbrass.info/webinar-registration..." \\
    --audience-name "Comeback Players 50+" \\
    --placement "Facebook Feed" \\
    --campaign-objective "Conversions" \\
    --creative-path /tmp/fb-staging/ad.mp4 \\
    --spend 412.50 \\
    --impressions 18230 \\
    --clicks 287 \\
    --ctr 1.57 \\
    --cpa 103.13 \\
    --roas 2.4 \\
    --conversions 4 \\
    --out-root /Users/air/Desktop/Precision-Brass/facebook-ads-database

Required: --ad-id, --slug, --status, --out-root
Everything else is optional; whatever is missing gets stored as null and
flagged in metadata.json so the analysis can call it out.

Updates index.json (appends or updates the row for this ad_id).
Does NOT write analysis.md. Claude writes that by hand.
"""
import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


def f_or_none(x):
    if x is None or x == "":
        return None
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def i_or_none(x):
    if x is None or x == "":
        return None
    try:
        return int(x)
    except (TypeError, ValueError):
        return None


def process_ad(args):
    today = datetime.now().strftime("%Y-%m-%d")
    launch = args.launch_date or today
    yyyymm = launch[:7] if len(launch) >= 7 else today[:7]
    folder_name = f"{yyyymm}_{args.slug}_{args.ad_id}"

    out_root = Path(args.out_root)
    out_dir = out_root / folder_name
    creative_dir = out_dir / "creative"
    out_dir.mkdir(parents=True, exist_ok=True)
    creative_dir.mkdir(parents=True, exist_ok=True)

    # ---- copy.md -------------------------------------------------------------
    copy_lines = [f"# Ad Copy. {args.slug}", ""]
    if args.primary_text:
        copy_lines += ["## Primary text (body)", "", args.primary_text.strip(), ""]
    if args.headline:
        copy_lines += ["## Headline", "", args.headline.strip(), ""]
    if args.description:
        copy_lines += ["## Description", "", args.description.strip(), ""]
    if args.cta:
        copy_lines += ["## CTA button", "", args.cta.strip(), ""]
    if args.destination_url:
        copy_lines += ["## Destination URL", "", args.destination_url.strip(), ""]
    (creative_dir / "copy.md").write_text("\n".join(copy_lines))

    # ---- creative file copy --------------------------------------------------
    creative_filename = None
    if args.creative_path:
        src = Path(args.creative_path)
        if src.exists():
            ext = src.suffix.lower() or ".bin"
            dest = creative_dir / f"ad{ext}"
            shutil.copy2(src, dest)
            creative_filename = dest.name
        else:
            creative_filename = f"MISSING ({args.creative_path})"

    # ---- metadata.json -------------------------------------------------------
    existing_meta_path = out_dir / "metadata.json"
    sales_history = []
    if existing_meta_path.exists():
        try:
            existing = json.loads(existing_meta_path.read_text())
            sales_history = existing.get("sales_history") or []
        except Exception:
            sales_history = []

    sales_count = i_or_none(args.sales) or 0
    sales_history.append({
        "date": today,
        "sales": sales_count,
        "note": args.note or ("manual update" if sales_history else "initial entry, manual"),
    })

    metadata = {
        "ad_id": args.ad_id,
        "slug": args.slug,
        "fb_ad_library_url": args.fb_library_url or None,
        "launch_date": launch,
        "end_date": args.end_date or None,
        "status": args.status,
        "sales_attributed": sales_count,
        "sales_history": sales_history,

        # Ad context
        "campaign_name": args.campaign_name or None,
        "adset_name": args.adset_name or None,
        "campaign_objective": args.campaign_objective or None,
        "audience_name": args.audience_name or None,
        "audience_notes": args.audience_notes or None,
        "placement": args.placement or None,
        "creative_type": args.creative_type or None,
        "creative_filename": creative_filename,

        # Ingestion provenance
        "ingestion_source": args.ingestion_source or "manual",
        "metrics_snapshot_date": today,
        "last_updated": today,
    }
    (out_dir / "metadata.json").write_text(json.dumps(metadata, indent=2))

    # ---- performance.json ----------------------------------------------------
    performance = {
        "spend_usd": f_or_none(args.spend),
        "impressions": i_or_none(args.impressions),
        "reach": i_or_none(args.reach),
        "clicks": i_or_none(args.clicks),
        "ctr_pct": f_or_none(args.ctr),
        "cpa_usd": f_or_none(args.cpa),
        "cpc_usd": f_or_none(args.cpc),
        "cpm_usd": f_or_none(args.cpm),
        "roas": f_or_none(args.roas),
        "conversions": i_or_none(args.conversions),
        "video_hook_rate_pct": f_or_none(args.hook_rate),
        "video_hold_rate_pct": f_or_none(args.hold_rate),
        "snapshot_date": today,
        "date_range": args.date_range or None,
    }
    (out_dir / "performance.json").write_text(json.dumps(performance, indent=2))

    # ---- index.json ----------------------------------------------------------
    index_path = out_root / "index.json"
    if index_path.exists():
        index = json.loads(index_path.read_text())
    else:
        index = {"schema_version": 1, "last_updated": today, "total_ads": 0, "ads": []}

    new_row = {
        "folder": folder_name,
        "ad_id": args.ad_id,
        "slug": args.slug,
        "launch_date": launch,
        "status": args.status,
        "sales_attributed": sales_count,
        "spend_usd": performance["spend_usd"],
        "roas": performance["roas"],
        "ctr_pct": performance["ctr_pct"],
        "cpa_usd": performance["cpa_usd"],
        "audience_name": metadata["audience_name"],
        "creative_type": metadata["creative_type"],
        "fb_ad_library_url": metadata["fb_ad_library_url"],
        "last_updated": today,
    }

    existing_idx = next(
        (i for i, a in enumerate(index["ads"]) if a.get("ad_id") == args.ad_id), None
    )
    if existing_idx is not None:
        index["ads"][existing_idx] = new_row
    else:
        index["ads"].append(new_row)

    index["ads"].sort(key=lambda a: a.get("launch_date") or "", reverse=True)
    index["total_ads"] = len(index["ads"])
    index["last_updated"] = today
    index_path.write_text(json.dumps(index, indent=2))

    # ---- summary -------------------------------------------------------------
    print(f"OK  folder: {out_dir}")
    print(f"OK  metadata.json, performance.json, creative/copy.md")
    if creative_filename and "MISSING" not in (creative_filename or ""):
        print(f"OK  creative file copied: creative/{creative_filename}")
    elif creative_filename:
        print(f"WARN creative file: {creative_filename}")
    else:
        print(f"WARN no creative file provided")
    print(f"OK  index.json updated ({index['total_ads']} ads total)")
    print(f"NEXT: write {out_dir}/analysis.md citing context/prospect-psychology.md + voc/personas/")


def main():
    p = argparse.ArgumentParser()

    # Required
    p.add_argument("--ad-id", required=True, help="Meta ad ID, or manual-NNN if not from Meta")
    p.add_argument("--slug", required=True, help="2-4 word lowercase hyphenated descriptor")
    p.add_argument("--status", required=True, choices=["winner", "flop", "unrated"])
    p.add_argument("--out-root", required=True)

    # Sales + dates
    p.add_argument("--sales", default="0")
    p.add_argument("--launch-date", default="", help="YYYY-MM-DD")
    p.add_argument("--end-date", default="")
    p.add_argument("--date-range", default="", help="Free text e.g. 'Apr 10 to Apr 24, 2026'")
    p.add_argument("--note", default="")

    # Creative + copy
    p.add_argument("--creative-path", default="")
    p.add_argument("--creative-type", default="", help="video | image | carousel")
    p.add_argument("--primary-text", default="")
    p.add_argument("--headline", default="")
    p.add_argument("--description", default="")
    p.add_argument("--cta", default="")
    p.add_argument("--destination-url", default="")

    # Ad context
    p.add_argument("--campaign-name", default="")
    p.add_argument("--adset-name", default="")
    p.add_argument("--campaign-objective", default="")
    p.add_argument("--audience-name", default="")
    p.add_argument("--audience-notes", default="")
    p.add_argument("--placement", default="")
    p.add_argument("--fb-library-url", default="")
    p.add_argument("--ingestion-source", default="manual")

    # Performance
    p.add_argument("--spend", default="")
    p.add_argument("--impressions", default="")
    p.add_argument("--reach", default="")
    p.add_argument("--clicks", default="")
    p.add_argument("--ctr", default="")
    p.add_argument("--cpa", default="")
    p.add_argument("--cpc", default="")
    p.add_argument("--cpm", default="")
    p.add_argument("--roas", default="")
    p.add_argument("--conversions", default="")
    p.add_argument("--hook-rate", default="")
    p.add_argument("--hold-rate", default="")

    args = p.parse_args()
    process_ad(args)


if __name__ == "__main__":
    main()
