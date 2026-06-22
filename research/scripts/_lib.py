"""Shared helpers: keyword extraction, slugify, hash, stale calc."""
import hashlib
import re
import string
from datetime import datetime, timedelta

STOPWORDS = set("""
a about above after again against all am an and any are aren't as at be because been before being
below between both but by can can't cannot could couldn't did didn't do does doesn't doing don't down
during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here
here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself
let's me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves
out over own same shan't she she'd she'll she's should shouldn't so some such than that that's the
their theirs them themselves then there there's these they they'd they'll they're they've this those
through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when
when's where where's which while who who's whom why why's with won't would wouldn't you you'd you'll
you're you've your yours yourself yourselves
also use using used uses one two three four five six seven eight nine ten get gets getting got
just like make makes making made may might must need needs needed see seen take taken want wants wanted
will would shall should good bad new old big small much many lot lots way ways thing things etc
yes no maybe whether something anything nothing everything someone anyone everyone nobody anywhere
everywhere somewhere actually really probably possibly definitely certainly clearly obviously even
ever never always often sometimes usually generally specifically essentially basically simply
""".split())

STALE_MONTHS = {
    'Shopify/E-commerce APIs': 6,
    'Amazon Seller Central APIs': 6,
    'Attribution & Tracking': 6,
    'Social Media Tools & Scheduling': 3,
    'Social Media APIs & Growth': 3,
    'AI Image Generation': 3,
    'AI Agents & Self-Improvement': 3,
    'Next.js / Supabase / Tech Stack': 6,
    'n8n Workflows': 6,
    'Knowledge Base / AI Context': 6,
    'APIs / Integrations General': 6,
    'Claude Code Architecture': 3,
}
DEFAULT_STALE_MONTHS = 24

def slugify(s, maxlen=60):
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:maxlen]

def hash_query(q):
    norm = re.sub(r'\s+', ' ', q.lower()).strip()
    return hashlib.sha256(norm.encode()).hexdigest()[:16]

def extract_sources(text):
    urls = re.findall(r'https?://[^\s\)\]\}\>\"\']+', text)
    seen = []
    for u in urls:
        u = u.rstrip('.,;:)')
        if u not in seen:
            seen.append(u)
    return seen[:20]

def extract_keywords(query, result_text, n=15):
    """Extract top-N salient keywords from query + first 1500 chars of result.
    Boosts terms in query, hyphenated/compound terms, capitalized proper nouns.
    """
    blob_query = (query or '').lower()
    blob_result = (result_text or '')[:1500].lower()
    # Strip URLs
    blob_result = re.sub(r'https?://\S+', ' ', blob_result)
    # Tokenize: words 3+ chars, allow hyphens and dots
    tokens_query = re.findall(r"\b[a-z][a-z0-9\-\.]{2,}\b", blob_query)
    tokens_result = re.findall(r"\b[a-z][a-z0-9\-\.]{2,}\b", blob_result)
    # Count, with query terms doubled
    counts = {}
    for t in tokens_query:
        if t in STOPWORDS or t.endswith('.') or t.startswith('.'):
            continue
        counts[t] = counts.get(t, 0) + 2
    for t in tokens_result:
        if t in STOPWORDS or t.endswith('.') or t.startswith('.'):
            continue
        counts[t] = counts.get(t, 0) + 1
    # Also pull capitalized proper nouns from query (Schwartz, Anthropic, etc.)
    proper = re.findall(r"\b[A-Z][a-z]{2,}(?:\s+[A-Z][a-z]+)?\b", query or '')
    for p in proper:
        key = p.lower().replace(' ', '-')
        counts[key] = counts.get(key, 0) + 3
    ranked = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    seen = []
    for term, _ in ranked:
        # Prefer hyphenated compound terms (more specific)
        if term not in seen:
            seen.append(term)
        if len(seen) >= n:
            break
    return seen

def calc_stale_after(date_str, category):
    months = STALE_MONTHS.get(category, DEFAULT_STALE_MONTHS)
    try:
        d = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        d = datetime.now()
    return (d + timedelta(days=months * 30)).strftime('%Y-%m-%d')

def write_frontmatter(fm):
    lines = ['---']
    for k, v in fm.items():
        if isinstance(v, list):
            if v:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{k}: []")
        elif isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, int):
            lines.append(f"{k}: {v}")
        else:
            esc = str(v).replace('"', '\\"')
            lines.append(f'{k}: "{esc}"')
    lines.append('---')
    return '\n'.join(lines)
