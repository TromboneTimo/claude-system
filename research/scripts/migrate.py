#!/usr/bin/env python3
"""
One-time migration: parse legacy perplexity_research_database.md monolith
into per-entry files under ~/.claude/research/perplexity/raw/ with rich
keyword indexing in _all.jsonl.
"""
import re
import json
import pathlib
import shutil
import sys
from datetime import datetime

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _lib import (slugify, hash_query, extract_sources, extract_keywords,
                  calc_stale_after, write_frontmatter)

LEGACY = pathlib.Path('/Users/air/.claude/knowledge/perplexity_research_database.md')
ROOT = pathlib.Path('/Users/air/.claude/research/perplexity')
RAW = ROOT / 'raw'
INDEX = ROOT / 'index' / '_all.jsonl'
LEGACY_DEST = ROOT / 'legacy' / 'perplexity_research_database.md'
BY_CAT = ROOT / 'index' / 'by-category'
BY_TAG = ROOT / 'index' / 'by-tag'

for d in [RAW, INDEX.parent, LEGACY_DEST.parent, BY_CAT, BY_TAG]:
    d.mkdir(parents=True, exist_ok=True)

CANONICAL_CATEGORIES = {
    'Marketing Frameworks', 'Dashboard/Analytics Architecture',
    'Shopify/E-commerce APIs', 'Amazon Seller Central APIs',
    'Attribution & Tracking', 'Social Media Tools & Scheduling',
    'Social Media APIs & Growth', 'Presentation Design Best Practices',
    'Chart/Data Visualization Best Practices', 'AI Image Generation',
    'Email Marketing', 'Content Strategy & SEO', 'Web Design & Typography',
    'AI Agents & Self-Improvement', 'Next.js / Supabase / Tech Stack',
    'n8n Workflows', 'Music Industry / Musicians', 'Sales & Psychology',
    'Knowledge Base / AI Context', 'APIs / Integrations General',
    'Blog & Content Ops', 'Claude Code Architecture', 'Miscellaneous',
}

def parse_legacy():
    """Walk the legacy DB top-down. Track current category from canonical H2s only.
    Sub-section H2s within entries (Citations:, Configuration, etc) are treated as
    entry body, not new categories.
    """
    if not LEGACY.exists():
        print(f"Legacy file not found: {LEGACY}")
        return []
    lines = LEGACY.read_text().splitlines()
    entries = []
    current_cat = 'Miscellaneous'
    current_entry = None
    in_toc = False
    for line in lines:
        if line.startswith('## Table of Contents'):
            in_toc = True
            continue
        if in_toc and line.startswith('## ') and not line.startswith('## Table'):
            in_toc = False
        if in_toc:
            continue
        # Canonical H2 = new category
        if line.startswith('## ') and not line.startswith('### '):
            cand = line[3:].strip()
            if cand in CANONICAL_CATEGORIES:
                if current_entry:
                    entries.append(current_entry)
                    current_entry = None
                current_cat = cand
                continue
            # Non-canonical H2 inside an entry: treat as body content
            if current_entry is not None:
                current_entry['body'] += '\n' + line
            continue
        # H3 = new entry under current category
        if line.startswith('### '):
            if current_entry:
                entries.append(current_entry)
            current_entry = {
                'category': current_cat,
                'query': line[4:].strip(),
                'body': '',
            }
            continue
        # Body line
        if current_entry is not None and line.strip() != '---':
            current_entry['body'] += '\n' + line
    if current_entry:
        entries.append(current_entry)
    return entries

def parse_entry_metadata(body):
    meta = {
        'date': '2026-04-01',
        'workspaces': [],
        'tags': [],
        'query_count': 1,
        'findings': '',
        'sources': [],
    }
    m = re.search(r'\*\*Date:\*\*\s*(\d{4}-\d{2}-\d{2})', body)
    if m:
        meta['date'] = m.group(1)
    m = re.search(r'\*\*Workspace\(s\):\*\*\s*(.+)', body)
    if m:
        meta['workspaces'] = [w.strip() for w in m.group(1).split(',') if w.strip()]
    m = re.search(r'\*\*Query count:\*\*\s*(\d+)', body)
    if m:
        meta['query_count'] = int(m.group(1))
    m = re.search(r'\*\*Tags:\*\*\s*(.+)', body)
    if m and 'n/a' not in m.group(1).lower():
        meta['tags'] = [t.strip() for t in m.group(1).split(',') if t.strip()]
    m = re.search(r'\*\*Key findings:\*\*\s*\n+(.+?)(?:\n\*\*Sources cited:|$)', body, re.DOTALL)
    if m:
        meta['findings'] = m.group(1).strip()
    sources_block = re.search(r'\*\*Sources cited:\*\*\s*\n+(.+)', body, re.DOTALL)
    if sources_block:
        for line in sources_block.group(1).split('\n'):
            line = line.strip()
            if line.startswith('- ') and 'http' in line:
                meta['sources'].append(line[2:].strip())
    return meta

def write_entry(entry, meta):
    qhash = hash_query(entry['query'])
    slug = slugify(entry['query'])
    date = meta['date']
    fname = f"{date}_{slug}_{qhash[:8]}.md"
    fpath = RAW / fname
    keywords = extract_keywords(entry['query'], meta['findings'], n=15)
    sources = meta['sources'] or extract_sources(meta['findings'])
    fm = {
        'query': entry['query'],
        'query_hash': qhash,
        'slug': slug,
        'model': 'sonar-pro',
        'date': date,
        'workspaces': meta['workspaces'],
        'category': entry['category'],
        'tags': meta['tags'],
        'keywords': keywords,
        'citations_count': len(sources),
        'synthesized_in_notebooklm': False,
        'stale_after': calc_stale_after(date, entry['category']),
    }
    body = [write_frontmatter(fm), '', f"# {entry['query']}", '', '## Key findings', '',
            meta['findings'] or '_(no findings extracted)_', '']
    if sources:
        body += ['## Sources', '']
        body += [f'- {url}' for url in sources]
    fpath.write_text('\n'.join(body))
    return fpath, fm

def index_record(fm, fpath):
    return {
        'hash': fm['query_hash'],
        'slug': fm['slug'],
        'date': fm['date'],
        'category': fm['category'],
        'tags': fm['tags'],
        'keywords': fm['keywords'],
        'workspaces': fm['workspaces'],
        'file': str(fpath.relative_to(ROOT)),
        'stale_after': fm['stale_after'],
        'query': fm['query'],
    }

def build_views(records):
    cats, tags = {}, {}
    for r in records:
        cats.setdefault(r['category'], []).append(r)
        for t in r['tags']:
            tags.setdefault(t, []).append(r)
    for cat, recs in cats.items():
        path = BY_CAT / (slugify(cat) + '.md')
        recs.sort(key=lambda r: r['date'], reverse=True)
        out = [f"# {cat}", '', f"{len(recs)} cached entries.", '']
        for r in recs:
            out += [f"### {r['query'][:200]}", '',
                    f"- Date: {r['date']} | Stale after: {r['stale_after']}",
                    f"- Tags: {', '.join(r['tags']) if r['tags'] else 'n/a'}",
                    f"- Keywords: {', '.join(r['keywords'][:10])}",
                    f"- File: `{r['file']}`", '']
        path.write_text('\n'.join(out))
    for tag, recs in tags.items():
        path = BY_TAG / (slugify(tag) + '.md')
        recs.sort(key=lambda r: r['date'], reverse=True)
        out = [f"# Tag: {tag}", '', f"{len(recs)} entries.", '']
        for r in recs:
            out += [f"### {r['query'][:180]}", '',
                    f"- Date: {r['date']} | Category: {r['category']}",
                    f"- File: `{r['file']}`", '']
        path.write_text('\n'.join(out))
    print(f"Built {len(cats)} category views, {len(tags)} tag views")

def main():
    print(f"Reading legacy: {LEGACY}")
    entries = parse_legacy()
    print(f"Parsed {len(entries)} entries")
    INDEX.write_text('')
    written = 0
    skipped = 0
    seen = set()
    records = []
    with INDEX.open('a') as idx:
        for entry in entries:
            qhash = hash_query(entry['query'])
            if qhash in seen:
                skipped += 1
                continue
            seen.add(qhash)
            meta = parse_entry_metadata(entry['body'])
            try:
                fpath, fm = write_entry(entry, meta)
                rec = index_record(fm, fpath)
                idx.write(json.dumps(rec) + '\n')
                records.append(rec)
                written += 1
            except (OSError, ValueError) as e:
                print(f"  skip {entry['query'][:60]}: {e}")
                skipped += 1
    print(f"Wrote {written} raw files, skipped {skipped}")
    if LEGACY.exists() and not LEGACY_DEST.exists():
        shutil.copy2(LEGACY, LEGACY_DEST)
        print(f"Copied legacy to {LEGACY_DEST}")
    build_views(records)

if __name__ == '__main__':
    main()