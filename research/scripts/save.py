#!/usr/bin/env python3
"""
Save a Perplexity query result to the research DB. Cache-aware.

Usage:
  save.py --query "..." --result-file /path/result.txt [--category "..."] [--tags a,b] [--workspace ws]
  save.py --bulk /path/queries.json
"""
import argparse
import json
import pathlib
import sys
from datetime import datetime

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _lib import (slugify, hash_query, extract_sources, extract_keywords,
                  calc_stale_after, write_frontmatter)

ROOT = pathlib.Path('/Users/air/.claude/research/perplexity')
RAW = ROOT / 'raw'
INDEX = ROOT / 'index' / '_all.jsonl'
RAW.mkdir(parents=True, exist_ok=True)
INDEX.parent.mkdir(parents=True, exist_ok=True)

def is_cached(qhash):
    if not INDEX.exists():
        return None
    with INDEX.open() as f:
        for line in f:
            try:
                rec = json.loads(line)
                if rec.get('hash') == qhash:
                    return rec
            except json.JSONDecodeError:
                continue
    return None

def save_one(query, result, model='sonar-pro', category='Miscellaneous',
             tags=None, workspaces=None, date=None, synthesized=False):
    tags = tags or []
    workspaces = workspaces or []
    date = date or datetime.now().strftime('%Y-%m-%d')
    qhash = hash_query(query)
    cached = is_cached(qhash)
    if cached:
        print(f"  CACHE HIT: {cached['file']}")
        return cached['file'], False
    slug = slugify(query)
    fname = f"{date}_{slug}_{qhash[:8]}.md"
    fpath = RAW / fname
    sources = extract_sources(result)
    keywords = extract_keywords(query, result, n=15)
    fm = {
        'query': query, 'query_hash': qhash, 'slug': slug, 'model': model,
        'date': date, 'workspaces': workspaces, 'category': category, 'tags': tags,
        'keywords': keywords,
        'citations_count': len(sources), 'synthesized_in_notebooklm': synthesized,
        'stale_after': calc_stale_after(date, category),
    }
    body = [write_frontmatter(fm), '', f"# {query}", '', '## Key findings', '',
            result.strip(), '']
    if sources:
        body += ['## Sources', '']
        body += [f'- {url}' for url in sources]
    fpath.write_text('\n'.join(body))
    rec = {
        'hash': qhash, 'slug': slug, 'date': date, 'category': category,
        'tags': tags, 'keywords': keywords, 'workspaces': workspaces,
        'file': str(fpath.relative_to(ROOT)), 'stale_after': fm['stale_after'],
        'query': query,
    }
    with INDEX.open('a') as f:
        f.write(json.dumps(rec) + '\n')
    print(f"  SAVED: {fname}")
    return str(fpath), True

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--query'); p.add_argument('--result-file'); p.add_argument('--result')
    p.add_argument('--model', default='sonar-pro'); p.add_argument('--category', default='Miscellaneous')
    p.add_argument('--tags', default=''); p.add_argument('--workspace', default='')
    p.add_argument('--date'); p.add_argument('--bulk')
    args = p.parse_args()
    if args.bulk:
        items = json.load(open(args.bulk))
        for item in items:
            result = item.get('result')
            if not result and 'result_file' in item:
                result = pathlib.Path(item['result_file']).read_text()
            save_one(
                item['query'], result,
                model=item.get('model', 'sonar-pro'),
                category=item.get('category', 'Miscellaneous'),
                tags=item.get('tags', []),
                workspaces=item.get('workspaces', []),
                date=item.get('date'),
            )
    else:
        if not args.query:
            print('--query required (or use --bulk)', file=sys.stderr); sys.exit(1)
        if args.result_file:
            result = pathlib.Path(args.result_file).read_text()
        elif args.result:
            result = args.result
        else:
            result = sys.stdin.read()
        tags = [t.strip() for t in args.tags.split(',') if t.strip()]
        workspaces = [w.strip() for w in args.workspace.split(',') if w.strip()]
        save_one(args.query, result, args.model, args.category, tags, workspaces, args.date)

if __name__ == '__main__':
    main()