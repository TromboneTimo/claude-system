---
name: pb-film-card
description: Adds a filming-brief card to Harrisson's "Ready to Film" pile on the Precision Brass dashboard (dashboard/scripts.html). Takes a Loom walkthrough link plus a shot list / instructions and inserts a card into the Supabase `scripts` table with status='approved' so it shows in the Ready To Film column next to the other Loom briefs. Optionally attaches reference-video link cards. Use whenever Timo says "add a film card", "add this to the ready to film pile", "new filming brief", "queue this for Harrisson to film", "add a loom brief", "make a card for the film pile", or "/pb-film-card". This is for lightweight Loom/shot-list briefs, NOT full written scripts (those come from pb-script-write).
---

# pb-film-card. Add a Loom-brief card to the Ready to Film pile.

## OPERATING PRINCIPLE: Ship right, never ship fast. Put it in the column Timo means.

The recurring failure here (2026-06-05) was putting the card in the wrong column and writing to the wrong record. Read [[project_scripts_pipeline_loom_cards]] and [[feedback_map_named_list_and_reproduce_view]] before acting.

- "Ready to Film" / "the film pile" / "to be filmed" = `scripts.status = 'approved'`. This is the default for this skill.
- "Filmed" / Done column = `scripts.status = 'filmed'`. Only use if Timo explicitly says the card is already shot.
- The card is a row in the `scripts` table. The Ready-to-Film modal renders that row's `body`, NOT any idea's notes.

## What this does

Inserts one card into `scripts` (status `approved`) so it appears in the **Ready To Film** column of `Precision-Brass/dashboard/scripts.html`, styled like the sibling Loom briefs (a clickable Loom card + a shot list, with the "Loom brief" tag).

## When to fire

Timo says: "add a film card", "add this to the ready to film pile", "new filming brief", "queue this for Harrisson", "add a loom brief", "/pb-film-card". Fire when he gives a Loom link and/or a list of things to shoot.

## Inputs to gather from Timo's message

- **Loom URL** (the walkthrough). Required if he mentions one.
- **Shot list / instructions**: the bullet list of what Harrisson should shoot or do. Required.
- **Title** (optional): if absent, derive a short one in the sibling "New X: ..." style (e.g. "New B-roll: ...", "New Talk: ...", "New Ad: ..."). Keep it concrete.
- **Reference videos** (optional): YouTube/IG links to attach as link cards.
- **Status** (optional): default `approved`. Only `filmed` if Timo says it is already shot.

If the shot list is missing or ambiguous, ASK. Do not invent shots.

## Content gate (do not skip)

This card is on Harrisson's client-facing board. Do NOT publish crude/sexual/troll text (Timo sometimes drops a junk "the instructions say: ..." line as a test). Do the real task; if he wants a real instructions note, ask for the actual wording. Keep shots faithful to what Timo said, in his phrasing.

## Build the card

Reuse the page's own classes (`.script-link`, `.script-link-loom`) so it matches what shipped. `body` is an array of sections `{kicker, time, heading, copy, visual}`; `copy` is injected as raw HTML by `renderScriptDetail`, so links/lists render. Build with Python (safe quoting), POST with curl.

```bash
source ~/.claude/secrets/precision-brass.env   # SUPABASE_URL + SUPABASE_SECRET_KEY (bypasses RLS)
python3 - <<'PY'
import json
# ---- fill these in ----
LOOM   = "https://www.loom.com/share/XXXXXXXX"
TITLE  = "New B-roll: <concise label>"
SLUG   = "broll-concise-label"            # used in the id
STATUS = "approved"                        # 'approved' = Ready to Film (default)
SHOTS  = [
  "shot 1, in Timo's phrasing",
  "shot 2",
]
REFS   = []   # optional: [{"label": "...", "url": "https://..."}]
# -----------------------
arrow='<svg class="sl-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
loom = (f'<a href="{LOOM}" target="_blank" rel="noopener" class="script-link script-link-loom">'
 '<span class="sl-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M10 9l5 3-5 3z" fill="currentColor" stroke="none"/></svg></span>'
 '<span class="sl-body"><span class="sl-title">Watch the Loom walkthrough</span><span class="sl-sub">Timo&#39;s brief</span></span>'
 f'{arrow}</a>') if LOOM else ''
refs = ('<div class="script-links-group"><div class="meta-label" style="margin-bottom:2px">Reference videos</div>'
 + ''.join(f'<a href="{r["url"]}" target="_blank" rel="noopener" class="script-link"><span class="sl-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="3"/><path d="M10 9l5 3-5 3z" fill="currentColor" stroke="none"/></svg></span><span class="sl-body"><span class="sl-title">{r["label"]}</span></span>'+arrow+'</a>' for r in REFS)
 + '</div>') if REFS else ''
ol = '<ol style="margin:0;padding-left:22px;line-height:1.7;color:var(--text);font-size:14px">' + ''.join(f'<li style="margin-bottom:10px">{s}</li>' for s in SHOTS) + '</ol>'
body=[]
if loom: body.append({"kicker":"WATCH FIRST","time":"","heading":"Loom walkthrough","copy":loom,"visual":""})
if refs: body.append({"kicker":"REFERENCE","time":"","heading":"Reference videos","copy":refs,"visual":""})
body.append({"kicker":"SHOT LIST","time":f"{len(SHOTS)} shots","heading":"What Harrisson shoots","copy":ol,"visual":""})
row={"id":"s_REPLACEDATE_"+SLUG,"idea_id":None,"title":TITLE,"length":"Loom brief","status":STATUS,
     "body":body,"history":[{"who":"Timo","text":"<b>Added</b> filming brief via pb-film-card","time":"REPLACEDATE","type":"delivered"}]}
json.dump(row, open("/tmp/film-card.json","w")); print("built", row["id"])
PY
# set the id date + history date to today (YYYY-MM-DD), then POST
TODAY=$(date +%Y%m%d); DSTAMP=$(date +%Y-%m-%d)
sed -i '' "s/REPLACEDATE_/${TODAY}_/; s/\"REPLACEDATE\"/\"${DSTAMP}\"/" /tmp/film-card.json
curl -s -X POST "${SUPABASE_URL}/rest/v1/scripts" \
  -H "apikey: ${SUPABASE_SECRET_KEY}" -H "Authorization: Bearer ${SUPABASE_SECRET_KEY}" \
  -H "Content-Type: application/json" -H "Prefer: resolution=merge-duplicates,return=representation" \
  --data-binary @/tmp/film-card.json | python3 -c "import sys,json;d=json.load(sys.stdin);print('OK',d[0]['id'],'| status',d[0]['status']) if isinstance(d,list) else print('ERR',d)"
```

## Dedup

Before POST, GET `scripts?select=id,title` and skip if the id collides or the title closely matches an existing card (3+ overlapping non-stopword tokens). Per Timo's standing rule, skip duplicates silently and note it; do not ask per-dup.

## Verify (do not skip)

Confirm the card landed in the column Timo expects by reading that exact filter, not just "the row exists":

```bash
source ~/.claude/secrets/precision-brass.env
curl -s "${SUPABASE_URL}/rest/v1/scripts?status=eq.approved&select=id,title,length&order=updated_at.desc" \
  -H "apikey: ${SUPABASE_SECRET_KEY}" -H "Authorization: Bearer ${SUPABASE_SECRET_KEY}" \
  | python3 -c "import sys,json;d=json.load(sys.stdin);print('Ready to Film count:',len(d));[print(' ',r['title'][:55]) for r in d]"
```

Report the count and the new card's position. If Timo says "I don't see it," the board defaults to the Ideas Pending column and only refetches every 30s (paused while a modal is open): tell him to hard-reload and click the **Ready To Film** tile.

## Confirm

> "Added '<title>' to Ready to Film (now N cards). Hard-reload scripts.html and click Ready To Film. Want me to open it?"

## What this skill does NOT do

- Does not write full scripts (that is `pb-script-write`, which produces an `html_full` body + PDF).
- Does not touch the `ideas` table or content_items tiles.
- Does not auto-deploy code. It is pure data; no git push needed unless scripts.html itself changed.
