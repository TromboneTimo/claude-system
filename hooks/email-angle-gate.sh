#!/usr/bin/env bash
# UserPromptSubmit hook. When Timo asks for ANY Precision Brass email work
# (draft / rework / schedule / pb-email), this auto-runs the angle ledger and
# injects the live saturation report + the anti-self-copy rule into context,
# BEFORE Claude writes a word. Makes the freshness check physically inescapable
# instead of memory-dependent.
#
# Origin: 2026-06-04. Timo: "make a system so it actually fires your memory,
# so every time you fix it you check you're not copying yourself." The memory
# files (feedback_email_batch_trope_diversity, feedback_email_short_paragraphs)
# kept getting bypassed because nothing forced me to read them at draft time.

set -u

LEDGER="/Users/air/Desktop/Precision-Brass/scripts/email-angle-ledger.py"

INPUT=$(cat)

PROMPT=$(echo "$INPUT" | /usr/bin/python3 -c "import json,sys
try: print((json.load(sys.stdin).get('prompt') or '').replace(chr(10),' '))
except Exception: pass" 2>/dev/null)
CWD=$(echo "$INPUT" | /usr/bin/python3 -c "import json,sys
try: print(json.load(sys.stdin).get('cwd',''))
except Exception: pass" 2>/dev/null)

# Only fire in the Precision Brass workspace and only if the ledger exists.
case "$CWD" in *Precision-Brass*) : ;; *) exit 0 ;; esac
[[ -f "$LEDGER" ]] || exit 0

# Only fire on email-drafting intent. Keep this specific so it doesn't run on
# every prompt.
if ! echo "$PROMPT" | grep -qiE '\bemail\b|pb-email|broadcast|email_proposals|swipe|subject line|draft.*(send|trombonetimo)|rework.*(email|draft)|schedul.*(email|draft|send)'; then
  exit 0
fi

REPORT=$(/usr/bin/python3 "$LEDGER" 2>/dev/null | head -60)
[[ -z "$REPORT" ]] && exit 0

export ANGLE_REPORT="$REPORT"
/usr/bin/python3 <<'PY'
import json, os
report = os.environ.get("ANGLE_REPORT", "")
msg = (
  "EMAIL ANGLE GATE (auto-fired: you are about to do Precision Brass email work).\n"
  "Read this BEFORE drafting. This is the LIVE saturation report from "
  "email_proposals. Per feedback_email_batch_trope_diversity + "
  "feedback_email_short_paragraphs:\n"
  "1. Any mechanism flagged HEAVY is OVERUSED. Do NOT reach for it again unless "
  "you cite the prior email and Timo approves. Pick a FRESH/UNUSED angle instead.\n"
  "2. Vary the OPENER, the MYTH, and the PROOF STUDENT across the batch (cap each "
  "reflex trope at once: use-more-air, it-was-never-you, nobody-ever-told-you, "
  "for-years, the-wall, Quick-rant). Rotate Brad/Mike/Kay/Heather/Yens/Rachel.\n"
  "3. Paragraph rhythm = grouped 2-3 sentence thought-units, one-liners only as a "
  "punch. BOTH walls AND one-sentence-per-line lists are banned. Do not mechanically "
  "reflow; eyeball against voc/emails/swipe-file/raw/dimitri-fantini-drums/.\n"
  "4. Teach one real, masterclass-sourced mechanism so the reader is smarter. "
  "Invent nothing.\n"
  "BANNED PHRASES (delete on sight, do NOT type them in any draft, chat or skill): "
  "the 'nobody tells you' family ('here's what nobody tells you', 'the truth nobody "
  "told you', 'the secret no one tells you', any variant) and 'Featured in Forbes'. "
  "These are gated at push (email-link-gate.sh + email-lint.js marker-opener) but "
  "the gate fires AFTER drafting; do not write them in the first place.\n"
  "5. Do NOT oscillate to the opposite extreme of a recent correction; synthesize "
  "toward the middle.\n\n"
  "--- LIVE LEDGER ---\n" + report
)

# LINK LAW block (added 2026-06-11 after 5 broadcasts shipped to the email
# CAPTURE page despite the rule existing in memory). Just-in-time injection:
# the canonical URL is read FROM the executable registry (email-lint.js) at
# fire time, so this block can never drift from the enforced truth. Research:
# decision-time rule injection + machine gates >> static memory files
# (cache 2026-06-11_llm-agents-ignoring-written-rules 1ccd6f6f).
import re as _re
try:
    _lint = open('/Users/air/Desktop/Precision-Brass/dashboard/lib/email-lint.js').read()
    _m = _re.search(r"CANONICAL_MASTERCLASS_URL = '([^']+)'", _lint)
    _canon = _m.group(1) if _m else 'REGISTRY READ FAILED - read dashboard/lib/email-lint.js yourself'
except Exception:
    _canon = 'REGISTRY READ FAILED - read dashboard/lib/email-lint.js yourself'
msg += (
    "\n\n=== LINK LAW (machine-enforced: lint + PreToolUse hook block violations; DB trigger pending Timo approval) ===\n"
    "Master class CTA, copy VERBATIM, never retype, never copy from an old email:\n"
    "  " + _canon + "\n"
    "BANNED in broadcasts: webinar-registration-pb (email CAPTURE page -- the list is already captured), "
    "any added el= param, any URL not in the registry or voc/testimonials/raw/. "
    "YOUTUBE POLICY (Timo 2026-06-13): a YouTube link is ALLOWED only when Timo explicitly asks for it. "
    "NEVER add a YouTube link or channel link on your own initiative. When Timo directs one, push with the YT_OK=1 token. "
    "Wrong-destination shipped 5 times before 2026-06-11; the gates below you will reject it anyway -- "
    "do not waste a turn finding out."
)
print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": msg}}))
PY
exit 0
