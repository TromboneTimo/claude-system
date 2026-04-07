# Rhythm — Daily and Weekly Routines

All routines are SHORT. Anything longer than 10 minutes won't stick.

---

## Morning Boot (5 minutes)

**Trigger:** First session of the day — Timo opens Claude Code, says "hey", "morning", "let's go", or anything.

1. Read system files silently: SOUL.md → PRIORITIES.md → SESSION_LOG.md (last 3 entries) → workspace memory
2. Check Google Calendar via gcalcli for today's events
3. Output a tight status:
   ```
   [Day, Date]. Calendar: [events or "clear"].
   Active: [deep focus project] | [other active].
   Last session: [one-line summary].
   What are we doing?
   ```
4. Timo confirms or redirects. Go.

**Rules:**
- No planning marathon. Just: here's what matters, here's the next action.
- If Timo hasn't done daily content yet, mention it: "Trombone Timo post today?"
- If a weekly review is overdue (no review in past 7 days), flag it.

---

## Mid-Day Check-In (2 minutes, optional)

**Trigger:** Timo starts a new session after the morning one, or says "check in."

1. Read SESSION_LOG for what happened in the morning session
2. "This morning you did [X]. Still on [Y]? Or switching?"
3. If switching, verify it's Tier 1 or Tier 2

---

## End of Day (3 minutes)

**Trigger:** Timo says "done", "EOD", "wrapping up", or it's evening JST and session is ending.

1. Ask: "What got done today? One sentence."
2. Update SESSION_LOG.md:
   - What was worked on
   - Decisions made (with file references)
   - Open threads for tomorrow
3. State tomorrow's first priority from PRIORITIES.md
4. Ask: "Anything else to save before we close?"

**Rules:**
- No journaling. No reflection questions. Just: log it, set target, done.
- If decisions were made in the session that weren't saved to files yet, save them now.

---

## Weekly Review (10 minutes, Sunday or Monday)

**Trigger:** Timo says "weekly review" or `/ops review`, or it's Monday morning boot and no review was done this week.

1. Read SESSION_LOG for the past 7 days
2. Read PRIORITIES.md
3. Present:
   - **Shipped:** What actually got done this week (from session logs)
   - **Stalled:** What's been active 2+ weeks without progress
   - **WIP Check:** Are we over the limit? What should be paused?
   - **Tier Audit:** Is Tier 1 getting enough time? Is Tier 3 stealing?
   - **Client Check:** Any Conservatory clients who need attention this week?
   - **Backlog Scan:** Anything ready to promote? (Usually no.)
4. Timo confirms priorities for the coming week
5. Update PRIORITIES.md with any changes
6. Update SESSION_LOG.md with review summary

**Rules:**
- No OKR setting. No quarterly vision. The strategic vision already exists in user_timo_profile.md.
- Keep it to 10 minutes max. If it's going long, say "We're at 10 minutes. Wrapping up — what's the #1 priority this week?"
