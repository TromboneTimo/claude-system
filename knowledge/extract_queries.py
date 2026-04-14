import json, os, re
from pathlib import Path

files = open('/tmp/perplexity_files.txt').read().strip().split('\n')
queries = []
tool_results = {}  # tool_use_id -> content

def get_workspace(fp):
    """Extract workspace from path like /Users/air/.claude/projects/-Users-air-Desktop-Foo/xxx.jsonl"""
    parts = fp.split('/')
    # find the 'projects' segment
    for i, p in enumerate(parts):
        if p == 'projects' and i+1 < len(parts):
            raw = parts[i+1]
            # -Users-air-Desktop-Foo  -> Foo
            m = re.sub(r'^-Users-air-Desktop-', '', raw)
            return m
    return 'unknown'

# First pass: collect queries and tool results
for fp in files:
    if not fp or not os.path.exists(fp):
        continue
    workspace = get_workspace(fp)
    try:
        with open(fp) as f:
            for line in f:
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                msg = obj.get('message', {})
                content = msg.get('content', [])
                if not isinstance(content, list):
                    continue
                for item in content:
                    if not isinstance(item, dict):
                        continue
                    t = item.get('type')
                    if t == 'tool_use':
                        inp = item.get('input', {})
                        cmd = inp.get('command', '')
                        if cmd and ('sonar' in cmd.lower()) and 'llm' in cmd.lower():
                            # Only capture actual llm -m sonar... invocations
                            m = re.search(r'llm\s+-m\s+sonar[\w-]*\s+["\']([^"\']+)["\']', cmd)
                            if not m:
                                # Multi-line or no quotes
                                m = re.search(r'llm\s+-m\s+sonar[\w-]*\s+(.+)', cmd, re.DOTALL)
                            if not m:
                                continue
                            query = m.group(1).strip().strip('"\'').replace('\\n',' ')[:500]
                            queries.append({
                                'workspace': workspace,
                                'file': fp,
                                'tool_use_id': item.get('id'),
                                'cmd': cmd[:1000],
                                'query': query,
                                'timestamp': obj.get('timestamp', '')
                            })
                    elif t == 'tool_result':
                        tid = item.get('tool_use_id')
                        c = item.get('content', '')
                        if isinstance(c, list):
                            c = ''.join(x.get('text','') if isinstance(x, dict) else str(x) for x in c)
                        if tid:
                            tool_results[tid] = str(c)[:8000]
    except Exception:
        continue

# Attach results
for q in queries:
    q['result'] = tool_results.get(q['tool_use_id'], '')

print(f"Total queries: {len(queries)}")
print(f"With results: {sum(1 for q in queries if q['result'])}")

from collections import Counter
ws = Counter(q['workspace'] for q in queries)
print("\nBy workspace:")
for w, c in ws.most_common():
    print(f"  {c}: {w}")

with open('/tmp/perplexity_full.json', 'w') as f:
    json.dump(queries, f, indent=2)

print("\nSample 3 queries with results:")
for q in queries[:3]:
    print(f"\n[{q['timestamp'][:10]}][{q['workspace']}]")
    print(f"Q: {q['query'][:200]}")
    print(f"R: {q['result'][:300]}")
