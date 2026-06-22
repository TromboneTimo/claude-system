---
name: verify-dashboard
description: Automated verification protocol for any deployed dashboard page. Loads the URL via Playwright, captures console errors (filtering known browser-extension noise), takes a screenshot, reads it, and returns a PASS/FAIL verdict with specific evidence. Replaces the manual 6-step verification flow in dashboard-dev. Use BEFORE saying "fixed" on any dashboard work, OR when the dashboard-deploy-gate hook blocks a deploy. Triggers on phrases "verify dashboard", "verify the deploy", "/verify-dashboard <url>", or auto-fires when a dashboard-dev fix is about to ship.
---

# /verify-dashboard. Mechanical verification of a deployed dashboard page

This skill is the answer to "how do I prove the fix actually works on the deployed page" without having to remember 6 steps every time.

## Inputs

- A deployed URL (e.g. `https://precision-brass-dashboard.vercel.app/channel-attribution`)
- Optional: a list of known-OK extension prefixes to filter from errors (default: `Migaku`, `Eternl`, `eternl`, `migaku`, `chrome-extension`, `moz-extension`)
- Optional: an expected text snippet that should be on the rendered page (e.g. `"$11,567"` for a revenue dashboard)

## Protocol (run all steps, fail fast)

1. **Close any open Playwright browser** to ensure a fresh session
   ```
   mcp__playwright__browser_close  (ignore error if none open)
   ```

2. **Navigate** to the URL
   ```
   mcp__playwright__browser_navigate url=<url>
   ```

3. **Wait** for primary content to settle (3 seconds max)
   ```
   mcp__playwright__browser_wait_for time=3
   ```

4. **Capture console errors**
   ```
   mcp__playwright__browser_console_messages level=error
   ```
   Filter: drop entries whose URL or message contains any extension prefix. Drop `favicon.ico` 404 (cosmetic).
   PASS if remaining count is 0. FAIL otherwise. Report the specific error messages.

5. **Capture console warnings** (informational, doesn't fail)
   ```
   mcp__playwright__browser_console_messages level=warning
   ```
   Filter same. Report count + first 3 messages.

6. **Take a snapshot** for content verification
   ```
   mcp__playwright__browser_snapshot
   ```
   If `expected_text` was provided: assert the snapshot text contains it. PASS or FAIL accordingly.

7. **Take a screenshot** for visual record
   ```
   mcp__playwright__browser_take_screenshot filename=/tmp/verify-dashboard-<timestamp>.png
   ```
   Read the PNG with the Read tool. Acknowledge what's visible (KPIs populated, charts rendered, or empty states).

8. **Print the verdict** in this exact format so the dashboard-deploy-gate hook can detect it:

```
=== VERIFY-DASHBOARD VERDICT ===
URL: <url>
Console errors (after extension filter): <count>
Console warnings (after extension filter): <count>
Snapshot text contains expected: <YES|NO|N/A>
Screenshot read: <path>
VERDICT: <PASS|FAIL>
Evidence:
  - <one line per item, e.g. "0 errors after filtering Migaku/Eternl">
  - <e.g. "$11,567 revenue visible on screen">
================================
```

9. If VERDICT=PASS: dashboard work is cleared to claim "fixed". Quote the evidence in the user-facing message.
10. If VERDICT=FAIL: do NOT claim "fixed". Report exact errors. Re-investigate before next iteration.

## Default extension filters

Filter out console messages containing any of these substrings:
- `Migaku`, `migaku`, `player-store-` (Japanese learning extension)
- `Eternl`, `eternl`, `initEternlDomAPI`, `dom.js?token=` (crypto wallet)
- `chrome-extension://`, `moz-extension://`, `safari-extension://`
- `favicon.ico` 404 (cosmetic only)

Add new patterns to this list as encountered.

## When to invoke

- **Manually:** `/verify-dashboard https://precision-brass-dashboard.vercel.app/channel-attribution`
- **Auto:** when about to claim "fixed" / "shipped" / "deployed" on dashboard-dev work
- **By hook recovery:** when dashboard-deploy-gate.sh blocks a deploy with no evidence, run this skill, then retry the deploy

## Failure-mode handling

- **Playwright browser already locked:** delete `/Users/air/Library/Caches/ms-playwright/mcp-chrome-*/Singleton*` files
- **Page redirects to /login:** still PASS if the login page renders without errors. The auth flow is separate; verify that with a logged-in test user via service-role.
- **404 on the URL:** check `vercel.json` (cleanUrls + outputDirectory rewrite the URL space). The local file path `dashboard/foo.html` deploys as `/foo`.
- **Stale Vercel cache:** add `?v=$(date +%s)` to the URL to force a fresh response.

## Reference

- `~/.claude/skills/dashboard-dev/SKILL.md` for the full verification rationale
- `~/.claude/hooks/dashboard-deploy-gate.sh` (the hook that gates deploys without verification)

## What this skill is NOT

- Not a load test. Use a separate matrix script (`dashboard/dashboard-test-matrix.sh` in each project) for that.
- Not a replacement for running unit tests or build steps. Those happen earlier in the deploy pipeline.
- Not a security audit. CSP / auth / RLS checks belong in `/security-review`.
