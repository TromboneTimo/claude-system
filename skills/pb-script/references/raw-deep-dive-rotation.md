# Raw Deep-Dive Rotation Pool

The Raw Deep-Dive agent (Agent 1) reads ONE raw corpus end-to-end per run. Rotation breaks the loudest-voice concentration problem caused by always reading summary files.

## The 8 corpora in the rotation pool

| ID | Corpus | Path | Size |
|---|---|---|---|
| `sales-A` | Sales calls batch A (1-9) | `voc/raw/sales-calls/*.md` (alphabetical first 9) | ~500KB |
| `sales-B` | Sales calls batch B (10-18) | same dir, middle 9 | ~500KB |
| `sales-C` | Sales calls batch C (19-28) | same dir, last 10 | ~500KB |
| `testimonials` | All 11 testimonials | `voc/raw/testimonials/*.md` | 51KB |
| `yt-comments` | YouTube comments JSON | `youtube-database/2026-04_embouchure-truth_O4a-q93ENAg/comments.json` | 32KB |
| `unsorted-vtt` | 28 unsorted .vtt files | `sort this/*.vtt` | 500KB |
| `fb-ads` | Facebook ad creative + performance | `facebook-ads-database/*/` | 55KB |
| `email-seq` | Webinar opt-in to strategy session sequence | `voc/raw/email-sequences/2026-04-21_email-sequence_webinar-optin-to-strategy-session.md` | 34KB |

## Picking algorithm (run in Bash before spawning Agent 1)

```bash
# 1. Read voices_used_log.jsonl, extract `corpus_picked` from last 3 runs
# 2. Subtract those from the 8-corpus pool
# 3. Pick uniformly at random from the remainder
# 4. If voices_used_log empty, pick uniformly from all 8

python3 - <<'PY'
import json, os, random, pathlib
log_path = pathlib.Path('/Users/air/Desktop/Precision-Brass/voc/voices_used_log.jsonl')
all_corpora = ['sales-A','sales-B','sales-C','testimonials','yt-comments','unsorted-vtt','fb-ads','email-seq']
recent = []
if log_path.exists():
    lines = log_path.read_text().splitlines()[-3:]
    for line in lines:
        try:
            recent.append(json.loads(line).get('corpus_picked'))
        except json.JSONDecodeError:
            continue
remaining = [c for c in all_corpora if c not in recent] or all_corpora
print(random.choice(remaining))
PY
```

Inject the chosen corpus_id into Agent 1's prompt.

## Per-corpus reading instructions

The agent must read its assigned corpus **end-to-end**, not skim. For batched sales calls, that means all 9 or 10 files. For .jsonl, parse and read every entry. For VTT, parse out the dialogue lines and treat as transcripts.

### sales-A / sales-B / sales-C
- Glob the directory, sort alphabetically, take the assigned slice.
- Read each .md file completely.
- Extract speaker names, pain quotes, hesitations, conversion moments, hidden subtext.
- Note which speakers haven't appeared in voices_used_log recently.

### testimonials
- Read all 11 files.
- Note: testimonials are CUSTOMERS who completed the program, not prospects. Per `feedback_master_lessons.md` rule 3, do NOT mix prospect language with customer language.
- Extract: identity-restoration moments, before/after framings, conversion triggers explicitly named.

### yt-comments
- Parse the JSON. Read every comment.
- Extract: emotional resonance signals, language register, pain points named publicly (different from sales-call pain points which are private).
- Public commentary surfaces social-permission objections.

### unsorted-vtt
- Triage first: open each .vtt, identify what it is (sales call? webinar? testimonial? something else?). Auto-categorize.
- Then deep-read 3-5 of the most promising files.
- These are likely high-signal because they haven't been mined yet.
- Recommend a destination folder for each file in the agent's report (e.g., "vtt-3.vtt looks like a sales call from 2026-02, suggest moving to voc/raw/sales-calls/").

### fb-ads
- Read every campaign folder (`hollywood-bowl-authority`, `studio-authority-comeback`, `they-told-me-vas-origin`, plus any new ones).
- For each: metadata.json (audience), performance.json (CTR/ROAS/CPA), copy.md (creative), analysis.md.
- Extract: ad copy that converted vs flopped, audience reactions, hooks that worked.

### email-seq
- Read end-to-end.
- Extract: subject lines, hook patterns, transition language, CTAs that perform, identity framings used in funnel-warming copy.
- Particularly valuable for surfacing language Harrison already uses successfully but hasn't repurposed for video hooks.

## Output requirement

Agent 1 returns:
1. The corpus_id picked.
2. 5 to 10 verbatim quotes from voices NOT in last 3 runs (per voices_used_log).
3. 2 candidate ideas, each anchored in a fresh voice + a specific pain or identity arc surfaced from this raw read.
4. A "voices surfaced" list (named speakers found, with file paths).

The diversity auditor uses the "voices surfaced" list to populate voices_used_log after the run.