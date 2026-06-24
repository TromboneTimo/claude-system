---
name: canon-deploy-verification
description: "ALL deploy + verification rules: alias markers, click-path walks, eyes-not-curl, lean verify, Safari cache. Consolidated 2026-06-12 from 6 files."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

# Canon: Deploy + Verification (Precision Brass)

Enforcement layer: `~/.claude/hooks/dashboard-deploy-gate.sh` (PreToolUse on Bash) blocks `git push` / `vercel deploy|--prod` of dashboard/api changes when no Playwright/curl verification evidence exists in recent transcript context (origin: 2026-05-09, 5+ "done" declarations after curl-only verification; bypass `PB_DEPLOY_GATE=skip`). Helper: `scripts/verify-deploy.sh <alias-url> <unique-marker> [path]` polls the alias with cache-busting, 10 tries x 5s, exits 0 only when the marker is live (built 2026-06-11, audit item B8).

## 1. Alias-published gate: grep a unique marker of THIS change on the prod alias

After `vercel --prod`, do NOT declare "deployed" until you curl the production alias (`https://precision-brass-dashboard.vercel.app/<page>?cb=<ts>`) and `grep` for a UNIQUE string that only exists in the change you just made (e.g. a new label, var name, or width). The alias can keep serving the previous bundle while the new deploy is still "Building", so a too-early verification (or one that only checks part of the page) passes on stale code.

**Why:** 2026-05-26, the meta-ads per-ad/metrics change. The first `vercel --prod` reported success and the table looked updated, but the CARD code had NOT published to the alias yet. Timo saw only one ad set with the new stats ("you only updated one, apply to all idiot"). The local file + git HEAD had all the changes; the alias was just serving an older bundle. A redeploy + immediate `grep` of the alias for `Conv Rate`/`cpaDisplay`/`1472px` confirmed it published the second time. This bit twice on 2026-05-26: the first "verified" pass ran against the stale bundle still on the alias, and only the redeploy + alias grep confirmed the real publish.

**How to apply:** deploy -> wait ~8s -> `curl -sL "<alias>/<page>?cb=$(date +%s%N)" | grep -c "<unique-marker>"` -> only when >0, load the authed page and verify visually. Canonical automation: `scripts/verify-deploy.sh https://precision-brass-dashboard.vercel.app "<marker>" /<path>` (e.g. `"no-youtube-links" /lib/email-lint.js`). Combine with [[reference-view-authed-dashboard]] for the visual step. This is the spirit of the dashboard-deploy-gate hook; honor it rather than bypassing blind.

## 2. Walk the actual click path after deploying any user-facing flow

After deploying any user-facing change (new page, new button, new redirect, new form), before saying "ready" or "live":

1. Walk the actual click path from the entry point to the destination.
2. If Playwright lands on a different URL than the one navigated to, that's a FAILURE signal, not a pass. Read the `Page URL:` field in the Playwright result. If it changed, ask why before moving on.
3. If the flow is auth-gated and I can't walk it, say so EXPLICITLY ("I cannot verify the authed view; Timo needs to test before I call this done") and STOP. Do not flip to him with "ready to drive" hoping it works.

**Why:** 2026-05-13. Built a new /scheduled page + multi-select on /emails. Verified by curl (200), Playwright unauthed (got redirected to /scripts), and `0 console errors`. Declared "live, ready for you to drive." Timo clicked Schedule N selected, got bounced to /scripts immediately because of an auth allowlist miss. The Playwright output had literally said `Page URL: https://...vercel.app/scripts` when navigating to /scheduled. I had the ground truth in front of me and read past it because I wanted the deploy to be done. His exact words: "Can you please test it and make sure it's actually working? Fuck you." Fair.

Same shape as `feedback_classifier_verification_must_use_ground_truth.md`: verifying internal consistency (curl returns 200, JS parses, no errors thrown) instead of ground truth (does the actual user flow reach the destination?). Two implementations of the same wrong rule will agree. The only test that matters is "did the user end up where they were supposed to?"

**How to apply:**
- Before saying "live" / "ready" / "deployed": list the entry point, list the destination URL, confirm the destination loaded the right page (not a redirect).
- If Playwright redirects to a different page than asked for, DO NOT shrug it off as "auth gate working." Investigate why. Specifically: when navigating to a NEW route I just created, a redirect to /scripts means the route isn't in the allowlist (see `canon_dashboard_engineering.md` section 5).
- "0 console errors on a redirected page" proves nothing. The page I was supposed to test wasn't loaded.
- "I can't verify because of auth" is a valid reason to NOT declare done. It is NOT a reason to declare done anyway and hope.

Recurs with `feedback_ship_right_not_fast.md` and the eyes-not-curl rule below.

## 3. Verify the user-facing URL loads before handing it off

When opening a deployed page for Timo (Safari verify, "open the dashboard", screenshot prep), the URL must be VERIFIED to load before invoking `open`. Do not type the URL from memory based on the repo's local file structure.

**Why:** Vercel + cleanUrls + outputDirectory rewrites mean the deployed URL is rarely the same as the file path. Local file `dashboard/channel-attribution.html` becomes deployed URL `/channel-attribution` (no `dashboard/` prefix, no `.html` extension). On 2026-05-06 I opened `https://.../dashboard/channel-attribution.html` and Timo got a 404 NOT_FOUND page. I then asked him "what's the error" instead of recognizing the screenshot as a routing 404. He had to teach me to read both `vercel.json` AND the screenshot. (The cleanUrls/outputDirectory mechanics are also documented in the dashboard-dev skill as "Trap 4: cleanUrls + outputDirectory rewrite the URL space"; verified present 2026-06-12.)

**How to apply:**
1. Before any `open` of a deployed URL: read `vercel.json` (or `next.config.js`, `astro.config.mjs`, etc.) for `outputDirectory`, `rewrites`, `redirects`, `cleanUrls`, `trailingSlash`. Know what the URL space looks like.
2. Curl the candidate URL: `curl -sI https://host/path | head -3`. Confirm 200 (or follow 3xx). If 404, find the right path before opening.
3. Only then call `open`.

**Bigger pattern:** any task that touches user-facing UI must end with opening the deployed URL, reading the rendered output (Read tool on a screenshot/PNG), and confirming what Timo will see. Code-level verification (curl /api/X returns JSON) is necessary but not sufficient. Race-fix, canvas-destruction, dashboard iframe, and URL routing were all this same shape. Cross-reference: `~/.claude/knowledge/visual-self-qa-protocol.md` (the visual gate); this extends it to URL-resolution: even a perfect deploy is invisible if you point Timo at the wrong path.

## 4. Eyes not curl: every "I fixed X" ends with loading the user's view

**The rule: every "I fixed X" must end with a Playwright (or osascript+Safari) screenshot or DOM read of the actual deployed page, with my own eyes confirming the bug is gone. Not the API response. Not the diff. The page.**

The full 6-step verification flow (deploy -> Aliased URL -> `browser_navigate` -> `browser_console_messages level=error` -> screenshot/snapshot + READ it -> only then say "fixed", quoting specific evidence), the osascript+Safari fallback, "the user's screenshot IS the answer, read it yourself", and the "still seeing X = distinguish LIVE vs STALE console with a fresh Playwright load" rule are all fully documented in the dashboard-dev skill, section "Verification protocol (MANDATORY before declaring fixed)" (verified present 2026-06-12). The dashboard-deploy-gate hook enforces it at push time; /verify-dashboard automates it.

**Why (incident detail not in the skill):** caught 2026-05-09 (and every previous session) when Timo went through 5+ rounds of "you said it was fixed but it isn't." Each round was caused by trusting curl over screenshots. The recurring pattern that cost Timo hours: edit code, diff looks right, push, curl an API endpoint, 200, declare "fixed", Timo opens the page, bug still there.

## 5. Verify LEAN: match verification cost to risk, no browser loops

**From 2026-06-04 (Timo, frustrated):** "the way you're trying to do things is causing you to bug out and do the same thing over and over." The pattern that fails: per-step Playwright verification that needs (a) a local python http.server that keeps dying on shell resets, (b) an hourly-expiring Supabase token re-minted every time, (c) a session re-injected via evaluate that gets wiped on every navigate. It loops.

**Verify lean instead, matched to risk:**
- Trivial additive UI (a button, label, copy handler that mirrors an existing one): `node --check` the extracted inline script + deploy + `curl | grep` the live bundle for the new symbol. No browser.
- New server endpoint: `curl` the live endpoint with a real Bearer token and inspect the JSON. No browser.
- Genuinely NEW rendering: exactly ONE prod screenshot, read it, done. No loops.
- If the auth/session injection fails once, fall back to grep/curl and report honestly. Never restart-server / re-mint-token more than once for the same check.

Mint at most ONE token per verification and reuse it across curl + a single browser shot. See [[project_dashboard_self_verify_authed]] (the how) but cap the browser use.

## 6. Safari WebKit disk cache: HTML routes need Cache-Control no-store

When a user reports the same UI bug after a deploy that *should* have fixed it, and Playwright + curl + visual inspection all confirm the deployed bytes are correct, the next move is not "diagnose the CSS again." It is: check whether the user's browser is serving stale HTML from disk cache.

**Why:** 2026-05-19. Timo reported the meta-ads column misalignment for the 10th time after commit 3e6f99f (`table-layout: fixed` + scroll wrapper) shipped the day before. The full ui-bug-diagnostic-protocol with Playwright WebKit (literal Safari engine) + Chromium across 5 viewports + 5 zoom levels = 300+ cells per run = zero misalignments anywhere. The deployed CSS was correct. The bug existed only in Timo's Safari disk cache, which was serving the pre-3e6f99f bytes with `width: 100%; table-layout: auto`. Safari's WebKit cache ignores `must-revalidate` on first-party `.html` under ITP, holding the disk copy for hours.

**The fix that stops it forever:** in `vercel.json`, add a headers rule that targets every route EXCEPT `/api/*` and recognized static asset extensions, with `Cache-Control: no-store, no-cache, must-revalidate, max-age=0`. Clean URLs (`/meta-ads`, `/scripts`) match the negative lookahead and get the no-store header. Assets (`.js`, `.css`, fonts, images) keep their regular cache. API routes set their own headers in code and are not overridden.

```json
{
  "source": "/((?!api/|.*\\.(?:js|css|json|png|jpg|jpeg|gif|svg|ico|webp|avif|woff|woff2|ttf|eot|map|mp4|webm|pdf|txt|xml)$).*)",
  "headers": [
    { "key": "Cache-Control", "value": "no-store, no-cache, must-revalidate, max-age=0" }
  ]
}
```

**How to apply:** any Vercel-hosted dashboard or app where the user might see a recurring UI bug after a deploy. Add this rule on Day 1, not on Day 10. The cost (one extra HTML request per page load, no CDN edge cache for HTML) is trivial compared to "I told you a million times" debugging cycles. Static assets are unaffected, so initial load + repeat performance is barely changed.

**Diagnostic shortcut:** before deep-diving into "the bug is back," do `curl -sI <prod_url>` and look at the `age:` header. `age: 44210` (12.3h) on a `.html` route with `cache-control: public, max-age=0, must-revalidate` is the smell. Vercel's CDN AND the user's browser may both be holding stale HTML.

Linked: the 7-step UI diagnostic in `canon_dashboard_engineering.md` (full Step-1 coordinate-dump protocol) and section 4 above (always verify with Playwright before saying fixed).

## Source files (absorbed 2026-06-12)
- feedback_verify_deploy_alias_published.md
- feedback_verify_after_deploy_walk_the_flow.md
- feedback_verify_user_facing_url_before_handoff.md
- feedback_verify_with_eyes_not_curl.md
- feedback_verify_lean_not_browser_loop.md
- feedback_html_no_store_for_safari_cache.md


## Concurrent-deployer regression (2026-06-13)

A verified-deployed UI fix VANISHED from production hours later: the daily scrape bot's session deployed `vercel --prod` from its own checkout, which only had origin -- and the fix commits were LOCAL-ONLY (never pushed). Timo saw the old page and thought he was losing his mind. Two rules, both mechanical:

1. **Push after every dashboard deploy.** A deploy whose commits are not on origin/main WILL be regressed by the next deployer. The deploy isn't done until `git push origin main` succeeds (rebase onto origin first if the scrape bot landed).
2. **Deploys only from the canonical checkout** (`/Users/air/Desktop/Precision-Brass`). Enforced: dashboard-deploy-gate.sh blocks `vercel --prod` from any other Precision-Brass path (added 2026-06-13, tested: worktree path exit 2, canonical falls through to the evidence gate).

Diagnosis shortcut for "my fix disappeared": curl the alias for the fix's marker FIRST (verify-deploy.sh). Marker present = browser cache; marker absent = someone deployed stale code -- check `vercel ls` ages against your last deploy.
