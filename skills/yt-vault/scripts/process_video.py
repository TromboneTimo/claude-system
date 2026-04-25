"""
yt-vault video processor.

Converts raw yt-dlp output into the structured yt-vault files for one video.

Usage:
  python3 process_video.py \\
    --info-json /tmp/yt-vault-staging/<ID>.info.json \\
    --srt /tmp/yt-vault-staging/<ID>.en.srt \\
    --status winner \\
    --sales 3 \\
    --slug embouchure-truth \\
    --out-root /Users/air/Desktop/Precision-Brass/youtube-database \\
    [--note "manual entry"]

Writes:
  <out-root>/<YYYY-MM>_<slug>_<videoID>/metadata.json
  <out-root>/<YYYY-MM>_<slug>_<videoID>/transcript.md
  <out-root>/<YYYY-MM>_<slug>_<videoID>/comments.json
  <out-root>/<YYYY-MM>_<slug>_<videoID>/comments-top.md

Updates:
  <out-root>/index.json (appends or updates the row for this video_id)

Does NOT write analysis.md. That is written by Claude (or the user) by reading
the transcript and citing context/prospect-psychology.md + voc/personas/.
See references/analysis-template.md.
"""
import argparse
import json
import re
from datetime import datetime
from pathlib import Path


def srt_to_text(srt_path: Path) -> str:
    """YouTube auto-captions emit rolling, overlapping segments. Stitch them
    into a single deduped stream by finding the longest suffix of running
    text that is a prefix of the new segment, and keeping only the new tail."""
    raw_srt = srt_path.read_text()
    blocks = re.split(r"\n\n+", raw_srt.strip())

    segments = []
    for b in blocks:
        parts = b.split("\n")
        if len(parts) < 3:
            continue
        m = re.match(r"(\d\d):(\d\d):(\d\d)", parts[1])
        ts_min = int(m.group(1)) * 60 + int(m.group(2)) if m else None
        ts_sec = int(m.group(3)) if m else None
        text = " ".join(parts[2:]).strip()
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            segments.append((ts_min, ts_sec, text))

    running = ""
    output = []
    for ts_min, ts_sec, text in segments:
        if not running:
            running = text
            output.append((ts_min, ts_sec, text))
            continue
        max_check = min(len(text), len(running), 250)
        overlap = 0
        for k in range(max_check, 0, -1):
            if running[-k:] == text[:k]:
                overlap = k
                break
        new_part = text[overlap:].strip()
        if new_part:
            running = (running + " " + new_part).strip()
            output.append((ts_min, ts_sec, new_part))

    body_words = []
    last_marker_total = -999
    for ts_min, ts_sec, chunk in output:
        total = (ts_min or 0) * 60 + (ts_sec or 0)
        if ts_min is not None and total - last_marker_total >= 30:
            body_words.append(f"\n\n**[{ts_min:02d}:{ts_sec:02d}]**\n")
            last_marker_total = total
        body_words.append(chunk)

    body = " ".join(w for w in body_words if w).strip()
    body = re.sub(r" +", " ", body)
    body = re.sub(r"\n +", "\n", body)
    body = re.sub(r"([.!?])\s+(?=[A-Z])", r"\1\n\n", body)
    return body


def slugify(title: str, fallback: str) -> str:
    if not title:
        return fallback
    s = title.lower()
    s = re.sub(r"[^a-z0-9 ]+", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    parts = s.split("-")
    keep = [p for p in parts if p not in {"the", "a", "an", "to", "and", "of", "for", "by", "is", "on"}]
    return "-".join(keep[:3]) or fallback


def process_video(args):
    info = json.loads(Path(args.info_json).read_text())

    video_id = info["id"]
    title = info.get("title") or video_id
    upload_date_raw = info.get("upload_date") or ""
    upload_iso = (
        f"{upload_date_raw[:4]}-{upload_date_raw[4:6]}-{upload_date_raw[6:]}"
        if upload_date_raw and len(upload_date_raw) == 8
        else None
    )
    today = datetime.now().strftime("%Y-%m-%d")
    yyyymm = upload_iso[:7] if upload_iso else today[:7]
    slug = args.slug or slugify(title, video_id)
    folder_name = f"{yyyymm}_{slug}_{video_id}"

    out_root = Path(args.out_root)
    out_dir = out_root / folder_name
    out_dir.mkdir(parents=True, exist_ok=True)

    # ---- metadata.json -------------------------------------------------------
    duration = info.get("duration") or 0
    duration_human = f"{duration // 60}:{duration % 60:02d}" if duration else None

    # Preserve sales_history if file already exists (re-store of same video)
    existing_meta_path = out_dir / "metadata.json"
    sales_history = []
    if existing_meta_path.exists():
        try:
            existing = json.loads(existing_meta_path.read_text())
            sales_history = existing.get("sales_history") or []
        except Exception:
            sales_history = []

    sales_history.append({
        "date": today,
        "sales": args.sales,
        "note": args.note or ("manual update" if sales_history else "initial entry, manual"),
    })

    metadata = {
        "video_id": video_id,
        "url": info.get("webpage_url"),
        "title": title,
        "channel": info.get("channel"),
        "channel_url": info.get("channel_url"),
        "uploader_handle": info.get("uploader_id"),
        "upload_date": upload_iso,
        "duration_seconds": duration,
        "duration_human": duration_human,
        "view_count": info.get("view_count"),
        "like_count": info.get("like_count"),
        "comment_count": info.get("comment_count"),
        "tags": info.get("tags", []),
        "categories": info.get("categories", []),

        "status": args.status,
        "sales_converted": args.sales,
        "sales_history": sales_history,
        "metrics_snapshot_date": today,
        "last_updated": today,
    }
    (out_dir / "metadata.json").write_text(json.dumps(metadata, indent=2))

    # ---- comments.json + comments-top.md -------------------------------------
    raw_comments = info.get("comments") or []
    top_level = [c for c in raw_comments if c.get("parent") == "root"]
    replies = [c for c in raw_comments if c.get("parent") != "root"]
    top_level.sort(key=lambda c: c.get("like_count") or 0, reverse=True)

    clean_comments = []
    for c in top_level:
        clean = {
            "comment_id": c.get("id"),
            "author": c.get("author"),
            "author_handle": c.get("author_id"),
            "text": c.get("text"),
            "like_count": c.get("like_count") or 0,
            "is_pinned": c.get("is_pinned") or False,
            "is_uploader_reply": False,
            "timestamp": c.get("timestamp"),
            "replies": [],
        }
        children = sorted(
            [r for r in replies if r.get("parent") == c.get("id")],
            key=lambda r: r.get("like_count") or 0,
            reverse=True,
        )
        for r in children:
            clean["replies"].append({
                "comment_id": r.get("id"),
                "author": r.get("author"),
                "author_handle": r.get("author_id"),
                "text": r.get("text"),
                "like_count": r.get("like_count") or 0,
                "is_uploader_reply": r.get("author_is_uploader") or False,
                "timestamp": r.get("timestamp"),
            })
        clean_comments.append(clean)

    (out_dir / "comments.json").write_text(
        json.dumps(clean_comments, indent=2, ensure_ascii=False)
    )

    md_lines = [
        f"# Top Comments. {title}",
        "",
        f"Total top-level comments: {len(top_level)} | Total comments incl. replies: {len(raw_comments)}",
        "Sorted by like count (descending). For full set with replies see `comments.json`.",
        "",
        "---",
        "",
    ]
    for i, c in enumerate(clean_comments[:50], 1):
        pin = " (pinned)" if c["is_pinned"] else ""
        md_lines += [
            f"### {i}. {c['author']}{pin}. likes {c['like_count']}",
            "",
            "> " + (c["text"] or "").replace("\n", "\n> "),
            "",
        ]
        for r in c["replies"][:3]:
            marker = " (Harrison reply)" if r["is_uploader_reply"] else ""
            md_lines += [
                f"  - **{r['author']}**{marker}. likes {r['like_count']}",
                "",
                "  > " + (r["text"] or "").replace("\n", "\n  > "),
                "",
            ]
    (out_dir / "comments-top.md").write_text("\n".join(md_lines))

    # ---- transcript.md -------------------------------------------------------
    if args.srt:
        srt_path = Path(args.srt)
        if srt_path.exists():
            body = srt_to_text(srt_path)
            transcript_md = (
                f"# Transcript. {title}\n\n"
                f"**Video:** {info.get('webpage_url')}\n"
                f"**Duration:** {duration_human}\n"
                f"**Source:** YouTube auto-captions (medium confidence, verify exact "
                f"wording before quoting in production copy)\n"
                f"**Pulled:** {today}\n\n---\n\n{body}\n"
            )
            (out_dir / "transcript.md").write_text(transcript_md)
        else:
            (out_dir / "transcript.md").write_text(
                f"# Transcript. {title}\n\n_No SRT found at {srt_path}. "
                "Re-run yt-dlp with --write-auto-subs --sub-lang en --convert-subs srt._\n"
            )

    # ---- index.json ----------------------------------------------------------
    index_path = out_root / "index.json"
    if index_path.exists():
        index = json.loads(index_path.read_text())
    else:
        index = {"schema_version": 1, "last_updated": today, "total_videos": 0, "videos": []}

    new_row = {
        "folder": folder_name,
        "video_id": video_id,
        "url": metadata["url"],
        "title": title,
        "channel": metadata["channel"],
        "upload_date": upload_iso,
        "duration_seconds": duration,
        "view_count": metadata["view_count"],
        "like_count": metadata["like_count"],
        "comment_count": metadata["comment_count"],
        "status": args.status,
        "sales_converted": args.sales,
        "topic_tags": [t for t in (info.get("tags") or [])][:8],
        "last_updated": today,
    }

    existing_idx = next(
        (i for i, v in enumerate(index["videos"]) if v.get("video_id") == video_id), None
    )
    if existing_idx is not None:
        index["videos"][existing_idx] = new_row
    else:
        index["videos"].append(new_row)

    index["videos"].sort(key=lambda v: v.get("upload_date") or "", reverse=True)
    index["total_videos"] = len(index["videos"])
    index["last_updated"] = today
    index_path.write_text(json.dumps(index, indent=2))

    print(f"OK  folder: {out_dir}")
    print(f"OK  metadata.json, comments.json, comments-top.md, transcript.md")
    print(f"OK  index.json updated ({index['total_videos']} videos total)")
    print(f"NEXT: write {out_dir}/analysis.md citing context/prospect-psychology.md + voc/personas/")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--info-json", required=True)
    p.add_argument("--srt", required=False, default="")
    p.add_argument("--status", required=True, choices=["winner", "flop", "unrated"])
    p.add_argument("--sales", type=int, required=True)
    p.add_argument("--slug", required=False, default="")
    p.add_argument("--out-root", required=True)
    p.add_argument("--note", required=False, default="")
    args = p.parse_args()
    process_video(args)


if __name__ == "__main__":
    main()
