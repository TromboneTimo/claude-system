#!/usr/bin/env bash
# PreToolUse hook on the ActiveCampaign send tool. PHYSICALLY BLOCKS a send whose
# HTML body fails the wall-of-text rhythm check. This is the enforcement Timo asked
# for on 2026-06-04 after I shipped walls THREE times in one session despite the
# memory rules: take my own judgment out of the loop. A send literally cannot fire
# on a wall now.
#
# Blocks: mcp__precision-brass-ac__send_draft_through_campaign and duplicate_campaign
# Checker: scripts/email-rhythm-check.py (gates on chars/visual height).

set -u
CHECK="/Users/air/Desktop/Precision-Brass/scripts/email-rhythm-check.py"
[[ -f "$CHECK" ]] || exit 0

INPUT=$(cat)

TOOL=$(echo "$INPUT" | /usr/bin/python3 -c "import json,sys
try: print(json.load(sys.stdin).get('tool_name',''))
except Exception: pass" 2>/dev/null)

case "$TOOL" in
  *send_draft_through_campaign*|*duplicate_campaign*) : ;;
  *) exit 0 ;;
esac

# REAL-LIST GUARD (added 2026-06-11 per audit B1). Claude-initiated sends go to
# list 20 (Test - Timo Solo) ONLY -- feedback_never_test_send_to_real_list.
# Real-list sends happen from the dashboard (env-gated, human-clicked), never
# from this tool path. Hard block, no bypass token: there is no legitimate
# Claude-side reason to MCP-send to a real list.
LIST_ID=$(echo "$INPUT" | /usr/bin/python3 -c "import json,sys
try:
  d=json.load(sys.stdin).get('tool_input',{})
  print(d.get('list_id') or d.get('list') or d.get('p') or '')
except Exception: pass" 2>/dev/null)
if [[ -n "$LIST_ID" && "$LIST_ID" != "20" ]]; then
  echo "BLOCKED: Claude-initiated AC sends are allowed to list 20 (Test - Timo Solo) ONLY. Got list=$LIST_ID." >&2
  echo "Real-list sends are scheduled by a human in the dashboard (env-gated). canon_email_shipping.md. No bypass." >&2
  exit 2
fi

# LINK LAW parity (added 2026-06-11 per audit B2): the Bash link gate cannot see
# MCP tool calls, so the same banned-link scan runs here on html_body.
LINT="/Users/air/Desktop/Precision-Brass/dashboard/lib/email-lint.js"
CANON=$(grep -o "CANONICAL_MASTERCLASS_URL = '[^']*'" "$LINT" 2>/dev/null | cut -d"'" -f2)
BODYSCAN=$(echo "$INPUT" | /usr/bin/python3 -c "import json,sys
try: print(json.load(sys.stdin).get('tool_input',{}).get('html_body',''))
except Exception: pass" 2>/dev/null)
if [[ -n "$BODYSCAN" ]]; then
  if echo "$BODYSCAN" | grep -q "webinar-registration-pb"; then
    echo "BLOCKED: html_body links webinar-registration-pb (the email CAPTURE page). Canonical master class URL: ${CANON}" >&2
    exit 2
  fi
  if echo "$BODYSCAN" | grep -qiE "https?://(www\.)?(youtube\.com|youtu\.be)/"; then
    # YouTube policy (Timo 2026-06-24): warn-only everywhere, never a hard block.
    # The push gate (email-link-gate.sh) also warns-and-allows. At send time this
    # is a non-blocking note only (feedback_never_hard_block_user_send).
    echo "NOTE: html_body contains a YouTube link. Allowed per Timo; ensure this send was Timo-directed, not auto-added." >&2
  fi
  if echo "$BODYSCAN" | grep -q "training-room1729899474908" && [[ -n "$CANON" ]]; then
    BAD=$(echo "$BODYSCAN" | grep -oE 'https?://[^"\ <>]*training-room1729899474908[^"\ <>]*' | grep -vF "$CANON" | head -1 || true)
    if [[ -n "$BAD" ]]; then
      echo "BLOCKED: training-room URL in html_body does not match the canonical registry entry. Got: $BAD" >&2
      echo "Canonical (copy verbatim): $CANON" >&2
      exit 2
    fi
  fi
  if echo "$BODYSCAN" | grep -qE "(REPLACE_TOKEN|hirose\.example|TODO_LINK|youtube\.example|example\.com/|MASTERCLASS_URL|\bPLACEHOLDER\b)"; then
    echo "BLOCKED: html_body contains a placeholder URL token. canon_email_shipping.md." >&2
    exit 2
  fi
fi

# Extract html_body, write to a temp file, run the checker.
BODY=$(echo "$INPUT" | /usr/bin/python3 -c "import json,sys
try:
  d=json.load(sys.stdin); print(d.get('tool_input',{}).get('html_body',''))
except Exception: pass" 2>/dev/null)

[[ -z "$BODY" ]] && exit 0

TMP=$(mktemp /tmp/email-rhythm-XXXX.html)
printf '%s' "$BODY" > "$TMP"
RESULT=$(/usr/bin/python3 "$CHECK" "$TMP" 2>&1)
RC=$?
rm -f "$TMP"

if [[ $RC -ne 0 ]]; then
  echo "BLOCKED: this email body fails the wall-of-text rhythm gate. Do NOT send it." >&2
  echo "" >&2
  echo "$RESULT" >&2
  echo "" >&2
  echo "FIX: re-break the flagged paragraphs to <=2 sentences / <=170 chars (Dimitri rhythm, mostly 1-2 sentences, varied, occasional one-line punch). Re-run scripts/email-rhythm-check.py until it PASSES, then resend. Do not bypass this." >&2
  exit 2
fi
exit 0
