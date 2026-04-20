#!/usr/bin/env python3
"""
VTT/SRT to clean markdown converter with YAML frontmatter.

Usage:
  python3 vtt-to-markdown.py --input <vtt-or-dir> --output-dir <voc-raw-subdir> --source-type <type> [--host <name>] [--speaker-type-default <prospect|customer|commenter>]

Examples:
  # Single file
  python3 vtt-to-markdown.py --input /tmp/call.vtt --output-dir voc/raw/sales-calls/ --source-type sales-call --host "Harrison Ball"

  # Folder of VTTs (sales calls)
  python3 vtt-to-markdown.py --input "/Users/air/Desktop/Precision-Brass/sort this/" --output-dir voc/raw/sales-calls/ --source-type sales-call --host "Harrison Ball"

Handles two VTT variants:
  1. YouTube auto-captions with rolling duplicate lines and <c> tags (processed with de-dup).
  2. Zoom/Meet-style simple CUE#\\nTIMESTAMP\\nTEXT blocks.

Writes one .md file per input .vtt with YAML frontmatter and clean paragraphs.
"""
import argparse
import json
import re
from datetime import datetime
from pathlib import Path

TAG_RE = re.compile(r"<[^>]+>")

NAME_PATTERNS = [
    re.compile(r"\b(?:Hey|Hi|Hello),?\s+([A-Z][a-z]{2,15})\b"),
    re.compile(r"\bMy name is ([A-Z][a-z]{2,15})\b"),
    re.compile(r"\bthis is ([A-Z][a-z]{2,15})\b"),
]
EXCLUDE_NAMES = {"There", "Good", "Hello", "Yes", "Well", "Okay", "Right", "Sorry",
                 "Thank", "Thanks", "Oh", "Yeah", "Looks", "Sure", "Great", "Nice",
                 "Actually", "Perfect", "Cool", "Fine", "Awesome"}


def parse_vtt(path: Path):
    """Return list of (HH:MM:SS, text) pairs with rolling-caption de-dup."""
    lines = path.read_text().splitlines()
    out = []
    current_ts = None
    seen_text = set()
    for line in lines:
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line:
            current_ts = line.split(" --> ")[0].split(".")[0]
            continue
        if not line.strip():
            continue
        cleaned = TAG_RE.sub("", line).strip()
        if not cleaned:
            continue
        if out and out[-1][1] == cleaned:
            continue
        if cleaned in seen_text:
            continue
        seen_text.add(cleaned)
        out.append((current_ts or "00:00:00", cleaned))
    return out


def paragraphs(segments, bucket_secs=45):
    def to_secs(ts):
        h, m, s = ts.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
    if not segments:
        return []
    result = []
    bucket_start_ts = segments[0][0]
    bucket_start_sec = to_secs(bucket_start_ts)
    buffer = []
    for ts, text in segments:
        if to_secs(ts) - bucket_start_sec >= bucket_secs and buffer:
            result.append((bucket_start_ts, " ".join(buffer)))
            buffer = []
            bucket_start_ts = ts
            bucket_start_sec = to_secs(ts)
        buffer.append(text)
    if buffer:
        result.append((bucket_start_ts, " ".join(buffer)))
    return result


def infer_speaker(segments, host=None):
    """Pick the most likely non-host first name from the first 60 segments."""
    candidates = {}
    for _, text in segments[:60]:
        for pat in NAME_PATTERNS:
            for m in pat.finditer(text):
                name = m.group(1)
                if name in EXCLUDE_NAMES:
                    continue
                if host and name == host.split()[0]:
                    continue
                candidates[name] = candidates.get(name, 0) + 1
    if not candidates:
        return "unknown"
    return max(candidates.items(), key=lambda x: x[1])[0]


def slug(s, maxlen=30):
    s = re.sub(r"[^\w-]", "-", s.lower())
    return re.sub(r"-+", "-", s).strip("-")[:maxlen]


def find_info_json(vtt_path: Path):
    """If there's a matching .info.json (yt-dlp pattern), return metadata."""
    candidates = [
        vtt_path.with_suffix(".info.json"),
        vtt_path.parent / f"{vtt_path.stem.replace('.en', '').replace('.en-orig', '')}.info.json",
    ]
    for c in candidates:
        if c.exists():
            try:
                return json.loads(c.read_text())
            except Exception:
                pass
    return None


def process(vtt_path: Path, output_dir: Path, source_type: str, host: str, speaker_type_default: str):
    segments = parse_vtt(vtt_path)
    if not segments:
        return None

    info = find_info_json(vtt_path)
    paras = paragraphs(segments)
    duration = segments[-1][0] if segments else "00:00:00"

    if info:
        title = info.get("title", "").strip()
        uploader = info.get("uploader", "").strip()
        upload_date_raw = info.get("upload_date", "")
        upload_date = f"{upload_date_raw[:4]}-{upload_date_raw[4:6]}-{upload_date_raw[6:8]}" if upload_date_raw else ""
        vid_id = info.get("id", "")
        source_url = f"https://www.youtube.com/watch?v={vid_id}" if vid_id else ""
        description = (info.get("description") or "").strip()
        speaker = infer_speaker(segments, host=uploader)
        ingest_source = "youtube-auto-captions"
    else:
        title = vtt_path.stem
        uploader = ""
        mtime = datetime.fromtimestamp(vtt_path.stat().st_mtime)
        upload_date = mtime.strftime("%Y-%m-%d")
        vid_id = ""
        source_url = ""
        description = ""
        speaker = infer_speaker(segments, host=host)
        ingest_source = "zoom-or-meet-auto-captions"

    if not upload_date:
        upload_date = datetime.now().strftime("%Y-%m-%d")

    idx_match = re.search(r"-(\d+)(?:\.en)?\.vtt$", vtt_path.name)
    idx = idx_match.group(1) if idx_match else ""
    slug_part = slug(title or speaker)
    suffix = f"_{idx}" if idx else ""
    out_name = f"{upload_date}_{source_type}_{slug(speaker)}_{slug_part}{suffix}.md"
    out_path = output_dir / out_name

    body = []
    body.append("---")
    body.append(f"source_type: {source_type}")
    body.append(f"original_filename: {vtt_path.name}")
    if source_url:
        body.append(f"source_url: {source_url}")
    if vid_id:
        body.append(f"video_id: {vid_id}")
    if title:
        body.append(f"title: {json.dumps(title)}")
    if uploader:
        body.append(f"uploader: {json.dumps(uploader)}")
    body.append(f"date: {upload_date}")
    body.append(f"host: {json.dumps(host) if host else '""'}")
    body.append(f"speaker_type: {speaker_type_default}")
    body.append(f"speaker_name_inferred: {speaker}")
    body.append(f"duration_estimate: {duration}")
    body.append(f"segments_count: {len(segments)}")
    body.append(f"transcript_confidence: medium")
    body.append(f"transcript_source: {ingest_source}")
    body.append(f"ingested: {datetime.now().strftime('%Y-%m-%d')}")
    body.append(f"ingested_via: coaching-db-skill")
    body.append("---")
    body.append("")
    body.append(f"# {source_type.replace('-', ' ').title()}: {speaker}" + (f" ({title})" if title and title != vtt_path.stem else ""))
    body.append("")
    body.append(f"**Speaker (inferred):** {speaker}  ")
    if host:
        body.append(f"**Host:** {host}  ")
    body.append(f"**Original file:** `{vtt_path.name}`  ")
    body.append(f"**Duration:** {duration}  ")
    body.append(f"**Segments:** {len(segments)}")
    body.append("")
    if description:
        body.append("## Description")
        body.append("")
        body.append(description)
        body.append("")
    body.append("## Transcript")
    body.append("")
    body.append("> Note: auto-captions. May contain errors. Verify before quoting verbatim.")
    body.append("")
    for ts, text in paras:
        body.append(f"**[{ts}]** {text}")
        body.append("")

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(body))
    return (out_name, len(paras), len(segments), speaker)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="VTT file OR directory containing VTTs")
    parser.add_argument("--output-dir", required=True, help="Target folder under voc/raw/")
    parser.add_argument("--source-type", required=True, help="e.g. sales-call, testimonial, youtube-transcript")
    parser.add_argument("--host", default="", help="Host name (for speaker-inference exclusion)")
    parser.add_argument("--speaker-type-default", default="prospect",
                        choices=["prospect", "customer", "commenter"])
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)

    vtts = []
    if input_path.is_dir():
        vtts = sorted(input_path.glob("*.vtt"))
    elif input_path.suffix == ".vtt":
        vtts = [input_path]
    else:
        print(f"Error: --input must be a .vtt file or directory of .vtt files")
        return 1

    if not vtts:
        print(f"No .vtt files found at {input_path}")
        return 1

    print(f"Processing {len(vtts)} VTT file(s)")
    print(f"Source type: {args.source_type}")
    print(f"Output dir:  {output_dir}")
    print(f"Default speaker_type: {args.speaker_type_default}")
    print()

    for vtt in vtts:
        result = process(vtt, output_dir, args.source_type, args.host, args.speaker_type_default)
        if result:
            name, paras_n, segs_n, speaker = result
            print(f"  WROTE {name} ({paras_n} paragraphs, {segs_n} segments, speaker={speaker})")
        else:
            print(f"  SKIP {vtt.name}: empty or unparseable")

    print()
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
