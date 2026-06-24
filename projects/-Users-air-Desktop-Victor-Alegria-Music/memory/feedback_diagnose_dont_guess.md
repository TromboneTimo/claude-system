---
name: Diagnose runtime state, don't guess from config
description: When a UI/auth/permissions bug is reported with screenshots, add a runtime diagnostic on move 2, not move 8. Config on disk is not runtime state.
type: feedback
originSessionId: 043e5bf9-932a-42e7-95ed-17f896f45464
---
When user reports a UI/auth/permissions bug and provides a screenshot, the FIRST move after reading the relevant file is to surface the actual runtime state. What email the session has, what role resolved, what nav items the page emitted. Do NOT propose remediation steps (clear cache, sign in fresh, private window) before reading what the running page actually thinks is true.

**Why:** 2026-05-06 dashboard incident. Timo asked to open the email/analytics dashboard. His screenshots clearly showed scripts.html with one nav item. I kept reopening standalone.html, telling him to sign in again, suggesting private windows, blaming stale cookies. Took 8+ prompts and a profanity-laden "do not talk to me until this is fixed" before I added a debug badge that would have revealed the actual issue in 30 seconds. The config (`ADMIN_EMAILS` includes timothyjay.maines@gmail.com) was correct on disk. The runtime check was failing for a reason I never bothered to inspect because I trusted the config file.

**How to apply:**
- UI/auth/permissions bug + screenshot = first action is `console.log` or visible badge of runtime state. Logged-in email, resolved role, computed nav allowlist. Not "try X and see."
- Config on disk is necessary but not sufficient. Always verify runtime values match config values.
- "Sign in again, clear cache, private window" is a guess, not a diagnosis. If you're suggesting it before you've read runtime state, you're stalling.
- Read the user's screenshot literally. If sidebar shows ONE nav item but source has FOUR, that's the gating filter firing, not the wrong page. Match visible state to file source before proposing anything.
- The AUDIT GATE in global CLAUDE.md governs this. Test the assumption that defines the problem before prescribing.
