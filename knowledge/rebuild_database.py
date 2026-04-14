import json, re
from collections import defaultdict

with open('/tmp/perplexity_full.json') as f:
    queries = json.load(f)

# Filter out error-only queries but keep them for counting
valid = [q for q in queries if q['result'] and 'Exit code 1' not in q['result'][:50] and 'Unknown model' not in q['result'][:100]]
print(f"Valid entries: {len(valid)} / {len(queries)}")

# Categorization rules (ordered - first match wins)
CATEGORIES = [
    ('Marketing Frameworks', ['laurel portie', 'portie', 'marketing framework', 'copy framework', 'hook framework', 'offer framework', 'godin', 'brunson', 'halbert', 'ogilvy', 'sop to a client']),
    ('Dashboard/Analytics Architecture', ['dashboard', 'analytics architecture', 'metrics dashboard', 'bi tool', 'looker', 'datastudio', 'superset', 'grafana', 'metabase', 'data pipeline']),
    ('Shopify/E-commerce APIs', ['shopify', 'woocommerce', 'bigcommerce', 'ecommerce api', 'storefront api', 'admin api', 'dtc lip', 'dtc marketing']),
    ('Amazon Seller Central APIs', ['amazon sp', 'amazon seller', 'selling partner', 'sp-api', 'amazon mws', 'amazon api']),
    ('Attribution & Tracking', ['hyros', 'attribution', 'utm', 'tracking pixel', 'conversion tracking', 'triple whale', 'northbeam', 'ga4 attribution', 'first-party tracking', 'server-side tracking']),
    ('Social Media Tools & Scheduling', ['buffer', 'hootsuite', 'later', 'metricool', 'socialbee', 'contentstudio', 'sprout social', 'loomly', 'planoly', 'publer', 'typefully', 'mixpost', 'postiz', 'blotato', 'pallyy', 'vista social', 'social media scheduling', 'scheduling tool']),
    ('Social Media APIs & Growth', ['instagram api', 'tiktok api', 'youtube api', 'twitter api', 'x api', 'meta graph', 'social growth', 'follower growth', 'algorithm', 'reels algorithm', 'shorts algorithm', 'instagram carousel', 'carousel generator', 'ai carousel', 'postnitro', 'instacarousel', 'aicarousels', 'contentdrips', 'taplio', 'predis.ai', 'draft ai', 'mirra', 'krumzi', 'empler']),
    ('Presentation Design Best Practices', ['presentation design', 'slide design', 'pitch deck', 'keynote', 'pptx', 'slides layout', 'powerpoint', 'reveal.js']),
    ('Chart/Data Visualization Best Practices', ['chart', 'visualization', 'data viz', 'bar chart', 'line chart', 'sparkline', 'd3', 'recharts', 'chart.js', 'plotly', 'svg chart']),
    ('AI Image Generation', ['nanobanana', 'nano banana', 'gemini image', 'midjourney', 'stable diffusion', 'flux ', 'dalle', 'dall-e', 'image generation', 'imagen', 'replicate image']),
    ('Email Marketing', ['email marketing', 'klaviyo', 'mailchimp', 'convertkit', 'kit.com', 'beehiiv', 'substack', 'cold email', 'email deliverability', 'spf dkim', 'sendgrid', 'postmark', 'resend']),
    ('Content Strategy & SEO', ['seo', 'serp', 'google ranking', 'keyword research', 'backlink', 'schema markup', 'e-e-a-t', 'content strategy', 'topical authority', 'ai overview', 'perplexity citation', 'geo optimization']),
    ('Web Design & Typography', ['fonts for', 'typography', 'color palette', 'color psychology', 'hex color', 'cta button', 'landing page', 'website design', 'portfolio website', 'google fonts', 'web fonts']),
    ('AI Agents & Self-Improvement', ['ai agent', 'self-improving ai', 'agent systems', 'autonomous agent', 'agent framework', 'karpathy', 'feedback loop', 'multi-agent']),
    ('Next.js / Supabase / Tech Stack', ['next.js', 'nextjs', 'supabase', 'vercel', 'postgres', 'react server', 'app router', 'server component', 'tailwind', 'shadcn', 'prisma', 'drizzle', 'puppeteer', 'html-to-image']),
    ('n8n Workflows', ['n8n', 'workflow automation', 'zapier', 'make.com', 'integromat']),
    ('Music Industry / Musicians', ['trumpet', 'trombone', 'musician', 'music industry', 'band', 'orchestra', 'brass', 'skool', 'booklivepro', 'byaustere', 'music coaching', 'music education', 'music creator']),
    ('Sales & Psychology', ['sales call', 'prospect', 'psychological', 'psychology', 'high-ticket', 'coaching sales', 'objection', 'closing', 'discovery call']),
    ('Knowledge Base / AI Context', ['knowledge base', 'claude project', 'context window', 'rag ', 'retrieval', 'vector db', 'embedding', 'document chunking']),
    ('APIs / Integrations General', ['oauth', 'webhook', 'rest api', 'graphql', 'service account', 'google workspace', 'google sheets', 'apps script', 'claude code scheduled', 'mcp server']),
    ('Blog & Content Ops', ['blog post', 'blog cms', 'ghost cms', 'wordpress', 'contentful', 'sanity cms', 'headless cms']),
]

def categorize(q_text, result_text):
    blob = (q_text + ' ' + result_text[:500]).lower()
    for cat, keywords in CATEGORIES:
        for kw in keywords:
            if kw in blob:
                return cat
    return 'Miscellaneous'

# Generate tags from query
def gen_tags(query, cat):
    q = query.lower()
    tags = set()
    tokens = re.findall(r'\b[a-z][a-z0-9\-\.]{2,}\b', q)
    # Common tech/topic words
    interesting = {'api','sdk','oauth','webhook','dashboard','analytics','tracking','attribution','email','seo','blog','skool','shopify','amazon','youtube','tiktok','instagram','meta','gemini','claude','nanobanana','hyros','n8n','supabase','next.js','nextjs','vercel','postgres','react','tailwind','klaviyo','beehiiv','airtable','google','slack','discord','stripe','paypal','zapier','svg','chart','d3','rag','embedding','vector','presentation','slide','funnel','cta','cro','landing','image','video','transcript','whisper','gpt','llm','anthropic','openai','perplexity','notebooklm','framework','prospect','sales','coaching','conservatory','musician','music','brass','trumpet','trombone'}
    for t in tokens:
        if t in interesting:
            tags.add(t)
    return sorted(tags)[:8]

# Generate key findings summary
def summarize(result, max_chars=1200):
    # Strip code fences? No, keep structure.
    text = result.strip()
    # Remove leading "# " title if huge
    # Truncate at sentence boundary near max_chars
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    # try to cut at a paragraph break
    lastp = cut.rfind('\n\n')
    if lastp > max_chars * 0.6:
        return cut[:lastp].strip() + '\n\n[...truncated...]'
    return cut.strip() + ' [...truncated...]'

def extract_sources(result):
    urls = re.findall(r'https?://[^\s\)\]\}\>\"\']+', result)
    # Dedupe keep order
    seen = []
    for u in urls:
        u = u.rstrip('.,;:)')
        if u not in seen:
            seen.append(u)
    return seen[:10]

# Group/dedupe near-duplicates by first 80 chars of query (case-insensitive)
by_key = defaultdict(list)
for q in valid:
    key = re.sub(r'\s+',' ', q['query'].lower())[:100]
    by_key[key].append(q)

# Build consolidated entries
entries = []
for key, group in by_key.items():
    # Most recent first
    group.sort(key=lambda x: x['timestamp'], reverse=True)
    primary = group[0]
    cat = categorize(primary['query'], primary['result'])
    dates = sorted(set(q['timestamp'][:10] for q in group if q['timestamp']))
    workspaces = sorted(set(q['workspace'] for q in group))
    entries.append({
        'category': cat,
        'query': primary['query'],
        'most_recent_date': dates[-1] if dates else 'unknown',
        'all_dates': dates,
        'workspaces': workspaces,
        'result': primary['result'],
        'sources': extract_sources(primary['result']),
        'tags': gen_tags(primary['query'], cat),
        'query_count': len(group)
    })

# Group by category
by_cat = defaultdict(list)
for e in entries:
    by_cat[e['category']].append(e)

# Sort categories by canonical order
CANON_ORDER = [
    'Marketing Frameworks',
    'Dashboard/Analytics Architecture',
    'Shopify/E-commerce APIs',
    'Amazon Seller Central APIs',
    'Attribution & Tracking',
    'Social Media Tools & Scheduling',
    'Social Media APIs & Growth',
    'Presentation Design Best Practices',
    'Chart/Data Visualization Best Practices',
    'AI Image Generation',
    'Email Marketing',
    'Content Strategy & SEO',
    'Web Design & Typography',
    'AI Agents & Self-Improvement',
    'Next.js / Supabase / Tech Stack',
    'n8n Workflows',
    'Music Industry / Musicians',
    'Sales & Psychology',
    'Knowledge Base / AI Context',
    'APIs / Integrations General',
    'Blog & Content Ops',
    'Miscellaneous',
]

print("\nCategory distribution:")
for c in CANON_ORDER:
    if by_cat.get(c):
        print(f"  {len(by_cat[c])}: {c}")

# Build markdown
lines = []
lines.append("# Perplexity Research Database")
lines.append("")
lines.append(f"**Auto-generated from Claude Code session logs.** Total unique research entries: **{len(entries)}** (consolidated from {len(valid)} raw Perplexity queries across {len(set(q['workspace'] for q in valid))} workspaces).")
lines.append("")
lines.append("**Purpose:** Before running any new `llm -m sonar-pro` query, grep this file. If the topic exists, use the cached findings instead of burning tokens.")
lines.append("")
lines.append("**Last updated:** auto from session logs")
lines.append("")
lines.append("## Table of Contents")
lines.append("")
for c in CANON_ORDER:
    if by_cat.get(c):
        anchor = c.lower().replace(' ','-').replace('/','').replace('&','').replace('--','-')
        lines.append(f"- [{c}](#{anchor}) ({len(by_cat[c])})")
lines.append("")
lines.append("---")
lines.append("")

for c in CANON_ORDER:
    bucket = by_cat.get(c, [])
    if not bucket:
        continue
    bucket.sort(key=lambda x: x['most_recent_date'], reverse=True)
    lines.append(f"## {c}")
    lines.append("")
    for e in bucket:
        lines.append(f"### {e['query'][:180]}")
        lines.append("")
        lines.append(f"- **Date:** {e['most_recent_date']}" + (f" (also: {', '.join(e['all_dates'][:-1])})" if len(e['all_dates']) > 1 else ""))
        lines.append(f"- **Workspace(s):** {', '.join(e['workspaces'])}")
        lines.append(f"- **Query count:** {e['query_count']}")
        lines.append(f"- **Tags:** {', '.join(e['tags']) if e['tags'] else 'n/a'}")
        lines.append("")
        lines.append("**Key findings:**")
        lines.append("")
        lines.append(summarize(e['result'], 1500))
        lines.append("")
        if e['sources']:
            lines.append("**Sources cited:**")
            lines.append("")
            for s in e['sources']:
                lines.append(f"- {s}")
            lines.append("")
        lines.append("---")
        lines.append("")

with open('/Users/air/.claude/knowledge/perplexity_research_database.md', 'w') as f:
    f.write('\n'.join(lines))

print(f"\nWrote database: {sum(len(l) for l in lines)} chars, {len(lines)} lines")

# Top 5 most researched
ranked = sorted(entries, key=lambda x: x['query_count'], reverse=True)[:5]
print("\nTop 5 most-researched topics:")
for e in ranked:
    print(f"  [{e['query_count']}x] {e['category']}: {e['query'][:100]}")

# Also write summary stats
with open('/tmp/db_stats.json','w') as f:
    json.dump({
        'total_raw': len(queries),
        'total_valid': len(valid),
        'unique_entries': len(entries),
        'categories': {c: len(by_cat[c]) for c in CANON_ORDER if by_cat.get(c)},
        'top5': [{'count': e['query_count'], 'cat': e['category'], 'query': e['query'][:120]} for e in ranked],
    }, f, indent=2)
