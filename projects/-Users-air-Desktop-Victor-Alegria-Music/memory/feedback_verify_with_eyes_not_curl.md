---
name: Verify user-facing fixes by loading the user's view, not by curling APIs
description: Stop saying "fixed" after curl returns 200, after vercel logs show 200, after the diff looks correct. The only signal that counts is loading the deployed page in a browser (Playwright, Safari) and seeing with my own eyes that the bug is gone. Code-level signals are necessary but never sufficient.
type: feedback
originSessionId: 377101fb-e5ce-4244-8b3a-adf8f5f91240
---
The pattern that has cost Timo hours, repeatedly: I edit code, the diff looks right, I push, I curl an API endpoint, the response comes back 200, I declare "fixed." Then Timo opens the page, the bug is still there, and I have to come back to it.

**The rule: every "I fixed X" must end with a Playwright (or osascript+Safari) screenshot or DOM read of the actual deployed page, with my own eyes confirming the bug is gone. Not the API response. Not the diff. The page.**

Specific verification flow for any user-facing fix:
1. Edit + commit + push + deploy (vercel deploy --prod).
2. Wait for Aliased URL.
3. `mcp__playwright__browser_navigate` to the affected page on the deployed URL.
4. `mcp__playwright__browser_console_messages level=error` → confirm zero errors (or only known-extension noise).
5. `mcp__playwright__browser_snapshot` or `browser_take_screenshot` → READ the result.
6. ONLY THEN say "fixed." Quote the specific evidence in the response.

If Playwright isn't available, use osascript to drive Safari and `screencapture` + `Read` the PNG.

**When the user sends a screenshot:** the screenshot IS the answer. Do not ask "what does it say." Read the image yourself. Recognize Vercel error pages, browser dev tools, error toasts, etc. on sight.

**When the user says "still seeing X":** before patching anything, distinguish LIVE vs STALE. A "still seeing" complaint about console errors usually means stale console entries (Chrome doesn't auto-clear them). Verify with a fresh-browser load (Playwright) BEFORE assuming the underlying bug isn't fixed.

**Caught 2026-05-09 (and every previous session)** when Timo went through 5+ rounds of "you said it was fixed but it isn't." Each round was caused by me trusting curl over screenshots.
