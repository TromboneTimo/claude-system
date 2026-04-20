#!/usr/bin/env python3
"""
Regenerate voc/personas/voice-bank.md from voc/quotes/all-quotes.jsonl.

Organizes quotes by theme with attribution. Never hand-edit the output; re-run
this script after adding quotes.

Usage:
  python3 build-voice-bank.py --jsonl voc/quotes/all-quotes.jsonl --output voc/personas/voice-bank.md [--client-name "Precision Brass"] [--coach-name "Harrison"]
"""
import argparse
import json
from pathlib import Path
from collections import Counter


def load_quotes(path):
    quotes = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            quotes.append(json.loads(line))
        except Exception as e:
            print(f"Skipping malformed line: {e}")
    return quotes


def attribution(q):
    name = q.get("speaker_name", "unknown")
    src = q.get("source_file", "")
    date = ""
    if "/" in src:
        fname = src.rsplit("/", 1)[-1]
        if len(fname) >= 7 and fname[4] == "-" and fname[7] == "_":
            date = fname[:7]
    return f"*{name}" + (f", {date}" if date else "") + "*"


def render_block(quotes_list, limit=None):
    if limit:
        quotes_list = quotes_list[:limit]
    lines = []
    for q in quotes_list:
        text = q.get("quote", "").strip()
        if not text:
            continue
        lines.append(f'> "{text}"')
        lines.append(f'> {attribution(q)}')
        lines.append("")
    return "\n".join(lines) if lines else "*(no quotes yet)*\n"


def by_angle(quotes, angle):
    return [q for q in quotes if q.get("mining_angle") == angle]


def by_pain(quotes, pain):
    return [q for q in quotes if pain in (q.get("pain_point") or [])]


def by_funnel(quotes, stage):
    return [q for q in quotes if q.get("funnel_stage") == stage]


def by_speaker_type(quotes, stype):
    return [q for q in quotes if q.get("speaker_type") == stype]


def by_use(quotes, use):
    return [q for q in quotes if use in (q.get("use_for") or [])]


def build(quotes, client_name, coach_name):
    total = len(quotes)
    speakers = sorted({q.get("speaker_name", "unknown") for q in quotes})
    speaker_types = Counter(q.get("speaker_type") for q in quotes)
    source_types = Counter()
    for q in quotes:
        src = q.get("source_file", "")
        if "/" in src:
            parts = src.split("/")
            if len(parts) >= 2:
                source_types[parts[1]] += 1

    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")

    md = []
    md.append(f"# {client_name} Voice Bank")
    md.append("")
    md.append(f"Verbatim customer and prospect language extracted from {total} raw entries across {len(source_types)} source types. Use these quotes directly in ad copy, email subject lines, YouTube hooks, and content. Every quote is traceable to its source via `voc/quotes/all-quotes.jsonl`.")
    md.append("")
    md.append(f"**Source breakdown:** " + ", ".join(f"{k}={v}" for k, v in source_types.most_common()))
    md.append(f"**Speaker type breakdown:** " + ", ".join(f"{k}={v}" for k, v in speaker_types.most_common()))
    md.append(f"**Unique speakers:** {len(speakers)}")
    md.append(f"**Extracted:** {today}")
    md.append(f"**Total quotes:** {total}")
    md.append("")
    md.append(f"**How to use:** scan by section heading. Copy quote directly into the asset. Attribution format is *Name, YYYY-MM*. For full context, open the source transcript in `voc/raw/`.")
    md.append("")
    md.append("**Transcript confidence:** medium (most sources are auto-captions). Verify exact wording against original source before using in production copy.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Table of contents")
    md.append("")
    md.append("1. [Before state](#before-state)")
    md.append("2. [Pain points](#pain-points)")
    md.append("3. [Failed methods](#failed-methods)")
    md.append("4. [Transformation](#transformation)")
    md.append("5. [Identity](#identity)")
    md.append(f"6. [Why {coach_name}](#why-{coach_name.lower()})")
    md.append("7. [Recommendations](#recommendations)")
    md.append("8. [Surprising angles](#surprising-angles)")
    md.append("9. [Prospect vs customer voice](#prospect-vs-customer)")
    md.append("10. [Funnel indexed](#funnel-indexed)")
    md.append("11. [Use-case indexed](#use-case-indexed)")
    md.append("12. [Gaps](#gaps)")
    md.append("")
    md.append("---")
    md.append("")

    md.append("## Before state")
    md.append("")
    md.append("Use for: TOFU hooks, ad headlines that name the problem.")
    md.append("")
    md.append(render_block(by_angle(quotes, "before-state"), limit=30))

    md.append("## Pain points")
    md.append("")
    md.append("Use for: ad copy, email subject lines, YouTube titles that target a specific pain.")
    md.append("")
    for pain in ["range", "endurance", "consistency", "embouchure", "mouthpiece", "tone",
                 "practice-habits", "accountability", "breathing", "fundamentals",
                 "comeback", "age-regression", "identity-loss", "plateau", "confidence"]:
        pain_quotes = by_pain(quotes, pain)
        if not pain_quotes:
            continue
        md.append(f"### {pain.replace('-', ' ').title()} ({len(pain_quotes)} quotes)")
        md.append("")
        md.append(render_block(pain_quotes, limit=8))

    md.append("## Failed methods")
    md.append("")
    md.append("Use for: 'if you've tried X and it didn't work' ad angles.")
    md.append("")
    md.append(render_block(by_angle(quotes, "what-they-tried") + by_angle(quotes, "failed-methods"), limit=20))

    md.append("## Transformation")
    md.append("")
    md.append("Use for: proof-driven ad copy, specific outcome headlines, BOFU emails.")
    md.append("")
    md.append(render_block(
        by_angle(quotes, "transformation") + by_angle(quotes, "specific-result")
        + by_angle(quotes, "before-after") + by_angle(quotes, "desired-outcome"),
        limit=25))

    md.append("## Identity")
    md.append("")
    md.append("Use for: identity-based hooks. Who they became, not what they achieved.")
    md.append("")
    md.append(render_block(
        by_angle(quotes, "identity") + by_angle(quotes, "identity-loss") + by_angle(quotes, "age-comeback"),
        limit=20))

    md.append(f"## Why {coach_name}")
    md.append("")
    md.append(f"Use for: positioning copy. What differentiates {coach_name} from alternatives.")
    md.append("")
    md.append(render_block(
        by_angle(quotes, "why-harrison") + by_angle(quotes, f"why-{coach_name.lower()}")
        + by_angle(quotes, "what-worked") + by_angle(quotes, "accountability")
        + by_angle(quotes, "community"),
        limit=20))

    md.append("## Recommendations")
    md.append("")
    md.append("Use for: testimonial carousels, social proof blocks.")
    md.append("")
    md.append(render_block(
        by_angle(quotes, "recommendation") + by_angle(quotes, "social-proof"),
        limit=15))

    md.append("## Surprising angles")
    md.append("")
    md.append("Unexpected quotes that could power a whole piece of content on their own.")
    md.append("")
    md.append(render_block(
        by_angle(quotes, "surprising-angle") + by_angle(quotes, "objection-handler"),
        limit=15))

    md.append("## Prospect vs customer")
    md.append("")
    md.append("Keep these separated. Prospect voice powers TOFU/MOFU. Customer voice powers BOFU.")
    md.append("")
    md.append("### Prospect voice (sales-call extracts)")
    md.append("")
    md.append(render_block(by_speaker_type(quotes, "prospect"), limit=20))
    md.append("### Customer voice (testimonial extracts)")
    md.append("")
    md.append(render_block(by_speaker_type(quotes, "customer"), limit=20))

    md.append("## Funnel indexed")
    md.append("")
    md.append("Top 10 per stage for quick scanning.")
    md.append("")
    for stage in ["TOFU", "MOFU", "BOFU"]:
        md.append(f"### {stage}")
        md.append("")
        md.append(render_block(by_funnel(quotes, stage), limit=10))

    md.append("## Use-case indexed")
    md.append("")
    md.append("Best-in-class quotes per use-case. Top 6 each.")
    md.append("")
    for use in ["hook", "ad-copy", "email-subject", "email-conversion", "content-idea", "testimonial"]:
        use_quotes = by_use(quotes, use)
        md.append(f"### {use} ({len(use_quotes)} tagged)")
        md.append("")
        md.append(render_block(use_quotes, limit=6))

    md.append("## Gaps")
    md.append("")
    md.append("Flagged for future ingestion. Fill by running `/coaching-db ingest` or `/coaching-db mine <angle>`.")
    md.append("")

    # Auto-detect gaps
    funnel = Counter(q.get("funnel_stage") for q in quotes)
    if funnel.get("TOFU", 0) < 10:
        md.append(f"- **TOFU is thin** ({funnel.get('TOFU', 0)} quotes). Ingest more sales calls or comment data to surface pre-aware pain language.")
    if funnel.get("MOFU", 0) < 10:
        md.append(f"- **MOFU is thin** ({funnel.get('MOFU', 0)} quotes). Mine for `what-they-tried` and objection language.")
    if funnel.get("BOFU", 0) < 10:
        md.append(f"- **BOFU is thin** ({funnel.get('BOFU', 0)} quotes). Ingest more testimonials or late-stage sales calls.")

    use_counts = Counter()
    for q in quotes:
        for u in q.get("use_for") or []:
            use_counts[u] += 1
    for use in ["hook", "ad-copy", "email-subject", "email-conversion", "content-idea", "testimonial"]:
        if use_counts.get(use, 0) < 5:
            md.append(f"- **`{use}` is thin** ({use_counts.get(use, 0)} tagged). Re-mine or ingest more sources.")

    if speaker_types.get("prospect", 0) == 0:
        md.append("- **No prospect voice captured.** Ingest sales calls for pre-purchase language.")
    if speaker_types.get("customer", 0) == 0:
        md.append("- **No customer voice captured.** Ingest testimonials.")
    if speaker_types.get("commenter", 0) == 0:
        md.append("- **No commenter voice captured.** Ingest YouTube/Facebook comments.")

    # Low-confidence ratio
    confs = Counter(q.get("confidence") for q in quotes)
    if confs.get("low", 0) > total * 0.2:
        md.append(f"- **High low-confidence rate** ({confs.get('low', 0)}/{total}). Consider human review of transcripts.")

    md.append("")
    md.append("---")
    md.append("")
    md.append(f"*Generated {today} from {total} quotes. Re-run `/coaching-db synthesize` (or `python3 scripts/build-voice-bank.py`) to regenerate after changes.*")

    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jsonl", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--client-name", default="Voice of Customer")
    parser.add_argument("--coach-name", default="Coach")
    args = parser.parse_args()

    quotes = load_quotes(Path(args.jsonl))
    content = build(quotes, args.client_name, args.coach_name)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(content)
    print(f"Wrote {args.output} ({len(content.splitlines())} lines, from {len(quotes)} quotes)")


if __name__ == "__main__":
    main()
