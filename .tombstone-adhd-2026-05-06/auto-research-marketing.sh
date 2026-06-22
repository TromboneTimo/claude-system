#!/bin/bash
# UserPromptSubmit hook. Fires on every user prompt.
# Responsibilities (2026-04-18 rewrite):
#   1. Session-scoped prompt counter
#   2. JST time awareness
#   3. Active-engagement time (GA4 5-min gap model)
#   4. Daily Reset vs Mid-Day discrimination
#   5. TARGETED banner from tasks.json (first prompt + 30-min-idle refire only)
#   6. Anchor capture + debounced drift detection (not keyword-only)
#   7. (removed) active-time threshold injections
#   8. Robinson's Remedies orchestrator routing
#
# What was REMOVED 2026-04-18:
#   - Every-prompt HEADER strip (PROMPT COUNT | ACTIVE | JST). Banner noise.
#   - Every-prompt BOOT_BANNER. Mid-day banner repeated same message each turn.
#   - Keyword-surface research-pipeline reminder. Fired on "how do" / "what are".
#   - Topic-shift starter-word detector (now/next/also/let's). False-positive-heavy.
#
# Replaced with:
#   - First-prompt anchor capture + 30-min-idle-refire banner
#   - Semantic-ish drift detector: Jaccard keyword overlap vs session anchor,
#     debounced by 10 min before firing completion-check injection

INPUT=$(cat)
PROMPT_RAW=$(echo "$INPUT" | jq -r '.prompt // ""')
PROMPT=$(echo "$PROMPT_RAW" | tr '[:upper:]' '[:lower:]')
CWD=$(echo "$INPUT" | jq -r '.cwd // ""')

# ============================================================
# SESSION-SCOPED PROMPT COUNTER
# ============================================================
SESSION_META="$HOME/.claude/.session_meta"
SESSION_START=$(sed -n '2p' "$SESSION_META" 2>/dev/null || echo "unknown")
SESSION_KEY=$(echo "$SESSION_START" | tr -c '[:alnum:]' '_')
COUNT_FILE="$HOME/.claude/.session_count_${SESSION_KEY}"

if [ ! -f "$COUNT_FILE" ]; then
  echo "1" > "$COUNT_FILE"
else
  CUR=$(cat "$COUNT_FILE")
  echo "$((CUR + 1))" > "$COUNT_FILE"
fi
CURRENT_COUNT=$(cat "$COUNT_FILE")

find "$HOME/.claude" -maxdepth 1 -name ".session_count_*" -mtime +1 -delete 2>/dev/null

# ============================================================
# JST TIME
# ============================================================
TODAY_JST=$(TZ='Asia/Tokyo' date +%Y-%m-%d)
NOW_JST=$(TZ='Asia/Tokyo' date +%H:%M)
DOW_JST=$(TZ='Asia/Tokyo' date +%A)
NOW_EPOCH=$(date -u +%s)

# ============================================================
# ACTIVE-ENGAGEMENT TIME (GA4 5-min gap)
# ============================================================
ENGAGEMENT_STATE="$HOME/.claude/.engagement_state"
GAP_THRESHOLD=300

LAST_ENGAGEMENT_DATE_FILE="$HOME/.claude/.engagement_state_date"
LAST_ENGAGEMENT_DATE=$(cat "$LAST_ENGAGEMENT_DATE_FILE" 2>/dev/null || echo "")
PREV_TS=0
if [ "$LAST_ENGAGEMENT_DATE" != "$TODAY_JST" ]; then
  printf "%s\n0\n" "$NOW_EPOCH" > "$ENGAGEMENT_STATE"
  echo "$TODAY_JST" > "$LAST_ENGAGEMENT_DATE_FILE"
  CUM_SECONDS=0
else
  if [ ! -f "$ENGAGEMENT_STATE" ]; then
    printf "%s\n0\n" "$NOW_EPOCH" > "$ENGAGEMENT_STATE"
    CUM_SECONDS=0
  else
    PREV_TS=$(sed -n '1p' "$ENGAGEMENT_STATE")
    CUM_SECONDS=$(sed -n '2p' "$ENGAGEMENT_STATE")
    GAP=$((NOW_EPOCH - PREV_TS))
    if [ "$GAP" -le "$GAP_THRESHOLD" ]; then
      CUM_SECONDS=$((CUM_SECONDS + GAP))
    fi
    printf "%s\n%s\n" "$NOW_EPOCH" "$CUM_SECONDS" > "$ENGAGEMENT_STATE"
  fi
fi
ACTIVE_MIN=$((CUM_SECONDS / 60))

# Detect idle gap since previous prompt (for banner refire decision)
IDLE_SINCE_LAST=0
if [ "$PREV_TS" -gt 0 ]; then
  IDLE_SINCE_LAST=$((NOW_EPOCH - PREV_TS))
fi

# ============================================================
# DAILY RESET vs MID-DAY
# ============================================================
DAILY_RESET_FILE="$HOME/.claude/.daily_reset_jst"
LAST_RESET_DATE=$(cat "$DAILY_RESET_FILE" 2>/dev/null || echo "")
IS_FIRST_TODAY=""
if [ "$LAST_RESET_DATE" != "$TODAY_JST" ]; then
  IS_FIRST_TODAY="1"
fi

# ============================================================
# ANCHOR: capture first prompt of session as the session's intent anchor
# Stored on line 3 of .session_meta (lines 1+2 already hold workspace + start-ts)
# ============================================================
ANCHOR_PROMPT=$(sed -n '3p' "$SESSION_META" 2>/dev/null || echo "")
if [ -z "$ANCHOR_PROMPT" ] && [ -n "$PROMPT_RAW" ]; then
  # First prompt of session. Capture first 280 chars as anchor.
  printf '%s\n' "${PROMPT_RAW:0:280}" >> "$SESSION_META"
  ANCHOR_PROMPT="${PROMPT_RAW:0:280}"
fi

# ============================================================
# TARGETED BANNER from tasks.json
# Fires only on:
#   (a) prompt 1 of session, OR
#   (b) idle gap > 1800s since previous prompt (user came back from break)
# ============================================================
TARGETED_BANNER=""
BANNER_STAMP="$HOME/.claude/.banner_shown"
LAST_BANNER_TS=$(cat "$BANNER_STAMP" 2>/dev/null || echo 0)
BANNER_GAP=$((NOW_EPOCH - LAST_BANNER_TS))

SHOULD_FIRE_BANNER=""
if [ "$CURRENT_COUNT" = "1" ]; then
  SHOULD_FIRE_BANNER="1"
elif [ "$BANNER_GAP" -gt 1800 ] && [ "$IDLE_SINCE_LAST" -gt 1800 ]; then
  SHOULD_FIRE_BANNER="1"
fi

if [ -n "$SHOULD_FIRE_BANNER" ] && [ -f "$HOME/.claude/state/tasks.json" ]; then
  BANNER_TEXT=$(python3 - <<'PY' 2>/dev/null
import json, sys
from pathlib import Path
try:
    d = json.load(open(Path.home() / ".claude/state/tasks.json"))
except Exception:
    sys.exit(0)
b = d.get("buckets", {})
today = b.get("today") or []
dl = b.get("deadlines_72h") or []
blocked = b.get("blocked") or []
shipped = b.get("shipped_today") or []
cal_path = Path.home() / ".claude/state/calendar-today.json"
cal = []
if cal_path.exists():
    try:
        cal = json.load(open(cal_path)).get("events", [])
    except Exception:
        cal = []
lines = []
lines.append(f"Today: {d.get('today_jst','?')} JST")
if today:
    lines.append("Timeboxed today:")
    for t in today[:5]:
        sh = f"@{t['start_hour']:02d}:00 " if t.get("start_hour") is not None else ""
        lines.append(f"  - {sh}{t.get('title','')[:70]}")
if dl:
    lines.append("Deadlines under 72h:")
    for t in dl[:5]:
        lines.append(f"  - {t.get('deadline_jst')}: {t.get('title','')[:70]}")
if cal:
    lines.append("Calendar today:")
    for e in cal[:6]:
        lines.append(f"  - {e.get('start','?')} {e.get('title','')[:60]}")
if blocked:
    lines.append("Blocked & waiting:")
    for t in blocked[:3]:
        lines.append(f"  - {t.get('title','')[:50]} (on: {t.get('blocked_on','?')[:40]})")
if shipped:
    lines.append(f"Already shipped today: {len(shipped)}")
lines.append("")
lines.append("Dashboard: open ~/.claude/dashboard/index.html")
lines.append("Mutate via /task add|done|park|block|start (see /task skill)")
print("\n".join(lines))
PY
)
  if [ -n "$BANNER_TEXT" ]; then
    if [ -n "$IS_FIRST_TODAY" ]; then
      HEADER_LINE="DAILY RESET (first session of the JST day, ${TODAY_JST} ${DOW_JST}, ${NOW_JST}). Run: echo '${TODAY_JST}' > ~/.claude/.daily_reset_jst once oriented."
    elif [ "$CURRENT_COUNT" = "1" ]; then
      HEADER_LINE="NEW SESSION (${TODAY_JST} ${DOW_JST}, ${NOW_JST}). Task state below. Ask Timo what he is working on to set the session anchor."
    else
      HEADER_LINE="BACK FROM BREAK (idle $((IDLE_SINCE_LAST/60))m). Refreshed task state:"
    fi
    TARGETED_BANNER="<system-reminder>${HEADER_LINE}

${BANNER_TEXT}</system-reminder>"
    echo "$NOW_EPOCH" > "$BANNER_STAMP"
  fi
fi

# ============================================================
# DRIFT DETECTION: Jaccard keyword overlap vs anchor, debounced 10 min.
# Only scores substantive prompts (>= 6 words). Skips tool-ack-style short prompts.
# ============================================================
DRIFT_ALERT=""
DRIFT_STATE="$HOME/.claude/.drift_state_${SESSION_KEY}"
# File format: line1 = first_drift_ts (epoch), line2 = fired_flag (0|1)
if [ -n "$ANCHOR_PROMPT" ] && [ "$CURRENT_COUNT" -ge 3 ] && ! echo "$PROMPT" | grep -qE '^/(task|blog|email|marketing|council|loop|schedule|fix-brain|routines|perplexity)'; then
  PROMPT_WORDS=$(echo "$PROMPT" | wc -w | tr -d ' ')
  if [ "$PROMPT_WORDS" -ge 6 ]; then
    OVERLAP=$(ANCHOR="$ANCHOR_PROMPT" CUR="$PROMPT" python3 - <<'PY' 2>/dev/null
import os, re
STOP = set("the a an and or but if of in on at to for with by from as is are was were be been being have has had do does did can could would should will this that these those we you i it they me my your our their not no yes its ok now just really also still very too get got give take make made do done".split())
def toks(s):
    return {w for w in re.findall(r"[a-z]{3,}", (s or "").lower()) if w not in STOP}
a = toks(os.environ.get("ANCHOR",""))
p = toks(os.environ.get("CUR",""))
if not a or not p:
    print("1.0")
else:
    inter = len(a & p)
    union = len(a | p)
    print(f"{inter/union:.3f}" if union else "1.0")
PY
)
    OVERLAP_NUM=$(echo "$OVERLAP" | awk '{print int($1*1000)}')
    FIRST_DRIFT_TS=0
    FIRED=0
    if [ -f "$DRIFT_STATE" ]; then
      FIRST_DRIFT_TS=$(sed -n '1p' "$DRIFT_STATE" 2>/dev/null || echo 0)
      FIRED=$(sed -n '2p' "$DRIFT_STATE" 2>/dev/null || echo 0)
    fi

    # Drift if Jaccard < 0.2 (OVERLAP_NUM < 200).
    if [ "${OVERLAP_NUM:-1000}" -lt 200 ]; then
      if [ "$FIRST_DRIFT_TS" = "0" ]; then
        printf "%s\n0\n" "$NOW_EPOCH" > "$DRIFT_STATE"
      else
        DRIFT_AGE=$((NOW_EPOCH - FIRST_DRIFT_TS))
        if [ "$DRIFT_AGE" -ge 600 ] && [ "$FIRED" = "0" ]; then
          ANCHOR_SNIPPET=$(echo "$ANCHOR_PROMPT" | head -c 80 | tr '\n' ' ')
          DRIFT_ALERT="<system-reminder>DRIFT DETECTED (anchor: \"${ANCHOR_SNIPPET}...\", ${DRIFT_AGE}s off-topic, overlap ${OVERLAP}). BEFORE engaging with the new topic, ask Timo: 'Did you finish [anchor task]? Mark it done before we pivot?' Use /task done or /task park if he confirms. Do not silently drop the prior task.</system-reminder>"
          printf "%s\n1\n" "$FIRST_DRIFT_TS" > "$DRIFT_STATE"
        fi
      fi
    else
      # Back on anchor. Clear drift state.
      rm -f "$DRIFT_STATE" 2>/dev/null
    fi
  fi
fi

# ============================================================
# ACTIVE-TIME THRESHOLD ALERTS: REMOVED 2026-05-06 per Timo request
# (deleted ADHD alerts and ADHD systems)
# ============================================================
TIME_ALERT=""

# ============================================================
# OUTPUT: RR orchestrator or default
# ============================================================
if echo "$CWD" | grep -qi "robinsons"; then
  BODY="${TARGETED_BANNER}

ORCHESTRATOR ACTIVE (Robinson's Remedies). Before task execution:
1. Load brand.md / brand-guidelines.md if not loaded
2. Load products.md if task references a product
3. Load audience.md to match tone
4. Load references/top-content/best-performing-posts.md for any social content
5. Route: Research -> marketing-researcher, Content -> marketing-social/blog, Creative -> marketing-creative, Data -> marketing-data
6. Log deliverables to /feedback/deliverables-log.md
7. NEVER use em dashes
8. Every CTA must include 'Available on Amazon Prime'

${DRIFT_ALERT}
${TIME_ALERT}"
else
  BODY="${TARGETED_BANNER}
${DRIFT_ALERT}
${TIME_ALERT}"
fi

cat <<ENDJSON
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": $(printf '%s' "$BODY" | jq -Rs .)
  }
}
ENDJSON
exit 0
