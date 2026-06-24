#!/usr/bin/env bash
# PreToolUse(Bash) hook: EMAIL LINK GATE.
#
# Origin 2026-06-11. Five broadcasts shipped linking webinar-registration-pb
# (the email CAPTURE page) instead of the master class VSL, even though the
# rule existed in memory/project_canonical_links.md. Timo: "There has to be
# an undeniable way." Research (cache 1ccd6f6f): agent-readable docs are
# advisory; only machine-enforced gates at the tool boundary are mandatory.
#
# This gate intercepts WRITE operations that ship email content (Supabase
# email_proposals POST/PATCH, ActiveCampaign message PUT/POST, ac-send) and
# blocks if the command or any referenced payload file contains:
#   1. webinar-registration-pb            (banned capture page)
#   2. a training-room URL that is NOT byte-identical to the canonical
#      registry entry in dashboard/lib/email-lint.js  (stale params, el=)
#   3. a YouTube link                     (standing order 2026-06-11)
# Read-only commands (grep/SELECT) are not touched.
#
# Bypass (requires Timo's explicit say-so): PB_LINK_GATE=skip
set -u

INPUT=$(cat)
[[ "${PB_LINK_GATE:-}" == "skip" ]] && exit 0

CMD=$(echo "$INPUT" | /usr/bin/python3 -c "import json,sys
try: print(json.load(sys.stdin).get('tool_input',{}).get('command',''))
except Exception: pass" 2>/dev/null)
[[ -z "$CMD" ]] && exit 0

# Inline bypass: hooks run before the command, so an exported env var inside
# the command never reaches this process. Match the deploy-gate convention of
# honoring the literal token in the command text. Auditable in transcripts.
echo "$CMD" | grep -q "PB_LINK_GATE=skip" && exit 0

# REAL-LIST GUARD, Bash transport (added 2026-06-11 per audit B1: "the direct
# AC API path from Claude is pure prose"). Any campaign create/send against the
# AC API (api-us1.com or /api/3/campaigns) that targets a list other than 20
# (Test - Timo Solo) blocks hard. Real-list sends are human-clicked in the
# dashboard. p[20]=20 is AC's list-targeting param shape.
if echo "$CMD" | grep -qiE "api-us1\.com|/api/3/campaigns"; then
  if echo "$CMD" | grep -qiE "(-X *(POST|PUT)|--data|--data-binary|--json|campaign_send|action=send)"; then
    SENDSCAN="$CMD"
    for f in $(echo "$CMD" | grep -oE '@[^" ]+' | sed 's/^@//'); do
      [[ -f "$f" ]] && SENDSCAN="$SENDSCAN
$(cat "$f")"
    done
    if echo "$SENDSCAN" | grep -qE 'p\[[0-9]+\]' && ! echo "$SENDSCAN" | grep -qE 'p\[20\]'; then
      echo "EMAIL LINK GATE: AC campaign call targets a list other than 20 (Test - Timo Solo). Claude-initiated sends are list-20 ONLY; real-list sends are human-clicked in the dashboard (canon_email_shipping.md). No bypass." >&2
      exit 2
    fi
  fi
  # DELETE guard (audit B5, feedback_verify_send_not_ack: a campaign was once
  # deleted while its send was in flight). Requires the explicit ack token
  # AC_DELETE_OK= in the command text -- forces a deliberate, verified turn.
  if echo "$CMD" | grep -qiE "\-X *DELETE" && ! echo "$CMD" | grep -q "AC_DELETE_OK="; then
    echo "EMAIL LINK GATE: deleting an AC campaign requires verifying send state FIRST (send_amt, status) and then including the literal token AC_DELETE_OK= in the command. canon_email_shipping.md." >&2
    exit 2
  fi
fi

# Only fire the LINK LAW scan on commands that WRITE to an email shipping surface.
echo "$CMD" | grep -qiE "email_proposals|/api/3/(messages|campaigns)|ac-send|campaignMessages" || exit 0
echo "$CMD" | grep -qiE "(-X *(POST|PATCH|PUT)|--data|--data-binary|--json)" || exit 0

# Collect text to scan: the command + every payload file it references.
SCAN="$CMD"
for f in $(echo "$CMD" | grep -oE '@[^" ]+' | sed 's/^@//'); do
  [[ -f "$f" ]] && SCAN="$SCAN
$(cat "$f")"
done

LINT="/Users/air/Desktop/Precision-Brass/dashboard/lib/email-lint.js"
CANON=$(grep -o "CANONICAL_MASTERCLASS_URL = '[^']*'" "$LINT" 2>/dev/null | cut -d"'" -f2)

fail() {
  echo "EMAIL LINK GATE: $1" >&2
  echo "Canonical master class URL (copy verbatim): ${CANON:-read dashboard/lib/email-lint.js}" >&2
  echo "Set by Timo 2026-06-11 after 5 broadcasts shipped to the capture page. Fix the payload; do not bypass without Timo's explicit say-so (PB_LINK_GATE=skip)." >&2
  exit 2
}

if echo "$SCAN" | grep -q "webinar-registration-pb"; then
  fail "payload links webinar-registration-pb -- that is the email CAPTURE page; the list is already captured. Broadcasts link the training-room VSL."
fi

if echo "$SCAN" | grep -q "training-room1729899474908" && [[ -n "$CANON" ]]; then
  # Every training-room occurrence must be the canonical string exactly.
  BAD=$(echo "$SCAN" | grep -oE 'https?://[^"\\ <>]*training-room1729899474908[^"\\ <>]*' | grep -vF "$CANON" | head -1 || true)
  # Tolerate JSON-escaped slashes in payloads.
  if [[ -n "$BAD" ]]; then
    UNESC=$(echo "$BAD" | sed 's|\\/|/|g')
    [[ "$UNESC" == "$CANON" ]] || fail "training-room URL does not match the canonical registry entry (got: $BAD)."
  fi
fi

if echo "$SCAN" | grep -qiE "https?:(\\\\?/){2}(www\.)?(youtube\.com|youtu\.be)"; then
  fail "payload contains a YouTube link -- banned in broadcasts (standing order 2026-06-11)."
fi

if echo "$SCAN" | grep -qE "(REPLACE_TOKEN|hirose\.example|TODO_LINK|youtube\.example|example\.com/|MASTERCLASS_URL|\bPLACEHOLDER\b)"; then
  fail "payload contains a placeholder URL token (canon_email_shipping.md)."
fi

# Banned marketer openers (the "nobody tells you" family). Doc-only rule since
# 2026-06-09; Timo caught one in a chat draft 2026-06-13 ("why does it keep
# happening"), so it is now gated at the write boundary like the link rules.
# Mirrors the 'marketer-opener' rule in dashboard/lib/email-lint.js.
if echo "$SCAN" | grep -qiE "(nobody|no one|no-one) +(ever +)?(tell|tells|told|telling) +you"; then
  echo "EMAIL CONTENT GATE: payload contains a banned marketer opener (the 'nobody tells you' family). Tell-tale guru voice, banned by the email doctrine 2026-06-09. Cut it and start on the real claim. Bypass with Timo's say-so (PB_LINK_GATE=skip)." >&2
  exit 2
fi

exit 0
