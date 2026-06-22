#!/usr/bin/env python3
"""
Cache check: search the research DB for entries matching a topic.
Multi-axis ranked match: tags > keywords > category > query text > workspace.

Usage:
  check.py "topic keywords"
  check.py --json "topic"             # JSON output
  check.py --stale                    # list stale entries only
  check.py --tag tag-name             # filter by exact tag
  check.py --category "Marketing Frameworks"
"""
import argparse
import json
import pathlib
import re
import sys
from datetime import datetime

ROOT = pathlib.Path('/Users/air/.claude/research/perplexity')
INDEX = ROOT / 'index' / '_all.jsonl'

def load_index():
    if not INDEX.exists():
        return []
    out = []
    for line in INDEX.read_text().splitlines():
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out

def tokenize(s):
    return [t.lower() for t in re.findall(r"\b[a-z][a-z0-9\-\.]{2,}\b", (s or '').lower())]

def score(entry, query_tokens, query_str):
    """Multi-axis weighted score. Higher = better match."""
    s = 0
    qstr_low = query_str.lower()
    # Exact phrase in query (strong)
    if qstr_low in entry.get('query', '').lower():
        s += 50
    # Per-token matches
    for t in query_tokens:
        # Tag match (strongest per-token signal)
        if t in [tag.lower() for tag in entry.get('tags', [])]:
            s += 20
        # Keyword match
        if t in [kw.lower() for kw in entry.get('keywords', [])]:
            s += 10
        # Category match
        if t in entry.get('category', '').lower():
            s += 5
        # Query text match
        if t in entry.get('query', '').lower():
            s += 3
        # Slug match
        if t in entry.get('slug', '').lower():
            s += 3
        # Workspace match (lower weight, mostly informational)
        if any(t in ws.lower() for ws in entry.get('workspaces', [])):
            s += 1
    return s

def is_stale(entry):
    sa = entry.get('stale_after')
    if not sa:
        return False
    try:
        return datetime.strptime(sa, '%Y-%m-%d') < datetime.now()
    except ValueError:
        return False

def main():
    p = argparse.ArgumentParser()
    p.add_argument('topic', nargs='?', default='')
    p.add_argument('--json', action='store_true', dest='as_json')
    p.add_argument('--stale', action='store_true')
    p.add_argument('--tag')
    p.add_argument('--category')
    p.add_argument('--limit', type=int, default=10)
    args = p.parse_args()
    entries = load_index()
    if not entries:
        print("Empty index. Run migrate.py first.", file=sys.stderr)
        sys.exit(2)
    # Stale-only mode
    if args.stale:
        stale = [e for e in entries if is_stale(e)]
        if args.as_json:
            print(json.dumps(stale, indent=2))
        else:
            print(f"{len(stale)} stale entries (out of {len(entries)}):\n")
            for e in stale[:args.limit]:
                print(f"  [{e['date']} STALE {e['stale_after']}] {e['query'][:120]}")
                print(f"    {ROOT / e['file']}")
        return
    # Tag filter
    if args.tag:
        matches = [e for e in entries if args.tag.lower() in [t.lower() for t in e.get('tags', [])]]
    elif args.category:
        matches = [e for e in entries if args.category.lower() in e.get('category', '').lower()]
    elif args.topic:
        tokens = tokenize(args.topic)
        scored = [(score(e, tokens, args.topic), e) for e in entries]
        scored = [(s, e) for s, e in scored if s > 0]
        scored.sort(key=lambda x: -x[0])
        matches = [e for _, e in scored]
    else:
        print("Provide a topic, --tag, --category, or --stale", file=sys.stderr)
        sys.exit(1)
    matches = matches[:args.limit]
    if args.as_json:
        print(json.dumps(matches, indent=2))
        return
    if not matches:
        print(f"NO CACHE for: {args.topic}")
        print(f"  Run /research query to populate. Total entries in DB: {len(entries)}")
        sys.exit(3)
    print(f"CACHE HITS for '{args.topic}' ({len(matches)} of {len(entries)} entries):\n")
    for i, e in enumerate(matches, 1):
        stale_flag = ' [STALE]' if is_stale(e) else ''
        print(f"{i}. {e['query'][:140]}{stale_flag}")
        print(f"   Date: {e['date']} | Category: {e['category']}")
        if e.get('tags'):
            print(f"   Tags: {', '.join(e['tags'][:8])}")
        print(f"   File: {ROOT / e['file']}")
        print()

if __name__ == '__main__':
    main()