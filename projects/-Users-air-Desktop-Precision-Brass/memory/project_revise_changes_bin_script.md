---
name: project-revise-changes-bin-script
description: Local script that processes the email_proposals changes bin. Replaces the unobservable cloud routine for testing and iteration.
metadata: 
  node_type: memory
  type: project
  originSessionId: f2a78e7a-6ab5-4d9b-a1c5-a0b5f465643c
---

# Email Revision: Local Script (Not Cloud Routine)

`scripts/revise-changes-bin.sh` is the canonical way to process `email_proposals` rows in `status=changes`.

Built 2026-05-15 after the cloud routine (`trig_017DDvYoyv5m6josQptPkNrr`, "Precision Brass Email Revision") proved untestable. `RemoteTrigger action=run` returned 200 with no run ID, no log link, and no visible execution. After 4 minutes of polling Supabase the row had not flipped. The cloud routine may still work on its 14:13 UTC cron, but you cannot iterate on it.

## How it works

1. Queries `email_proposals?status=eq.changes` via Supabase REST.
2. Per row: reads the last entry in `history[]`.
   - If `who == "Routine-PB-Revise"` -> SKIP (anti-loop).
   - If `type != "changes"` -> SKIP (no actionable feedback).
   - Else -> build a revision prompt embedding `voc/emails/extracts/harrison-email-voice.md` + `dashboard/lib/email-lint.js` + the current row + Harrison's feedback verbatim.
3. Calls `claude -p --model claude-sonnet-4-6` for the LLM step (~60-90s per row).
4. Parses the JSON response, PATCHes Supabase with the revised fields + `status=proposal_pending`, appends a `Routine-PB-Revise` history entry quoting the feedback verbatim.

## Usage

```bash
export SUPABASE_SERVICE_ROLE_KEY=<service-role>  # from memory/project_credentials.md
./scripts/revise-changes-bin.sh            # live
./scripts/revise-changes-bin.sh --dry-run  # generate, log, do not patch
```

End-to-end time: ~60-90s per row (dominated by the Claude API call). Anti-loop run on a row already revised: <1s.

## Why: Verified 2026-05-15

- Run #1 (fresh Harrison feedback): 92s, subject softened, opener replaced per Harrison's example, third paragraph cut, testimonial + CTA preserved, all lint rules pass (tagline, masterclass URL, banned-phrase checks).
- Run #2 (re-run after v2 in place): correctly SKIPPED via anti-loop.
- Run #3 (new Harrison feedback after v2): 58s, body cut to roughly half length, warm opener preserved.

## When to use the cloud routine instead

If you ever need this to fire unattended at 14:13 UTC daily, the cloud routine exists. But for any change to the revision prompt or rule set, edit and test this script locally. Promote to cloud only after the local run is right.

Related:
- `pb-email-write` skill writes v1 drafts.
- `dashboard/lib/email-lint.js` is the lint source of truth (loaded into the prompt).
- `voc/emails/extracts/harrison-email-voice.md` is the voice source of truth (loaded into the prompt).
- [[feedback-email-html-links-and-cta]] locks tagline + master class URL rules the script must respect.
