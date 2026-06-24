---
name: canon-dashboard-engineering
description: "ALL dashboard/eng bug-class rules: SWR, canvas, IDB, fire-and-forget, allowlists, CSP, worktrees, seed data. Consolidated 2026-06-12 from 14 files."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

# Canon: Dashboard Engineering bug classes (Precision Brass)

Canonical engineering reference = `~/.claude/skills/dashboard-dev/SKILL.md` (verification protocol, Vercel cache traps, multi-tier cache, IDB pattern, bug-class checklist). Where a rule below says "documented in dashboard-dev skill" that coverage was grep-verified 2026-06-12 before pointer-swapping. Everything else here is NOT in the skill and this file is its only home.

## 1. Dashboard client caches must self-heal (stale-while-revalidate)

Every dashboard client cache MUST be stale-while-revalidate: render cached + ALWAYS background-refresh + swap if changed. NOT in dashboard-dev skill; this is the canonical statement.

**Why:** the dashboard kept showing stale data (e.g. email-analytics stuck on "Daily Email 1 (subject loading)", meta-ads stale columns). Root cause class: client caches (IndexedDB/localStorage) that on load **render the cached copy and `return` without ever re-fetching** (readCache hardcoded `fresh:true`; loadAll commented "cached = always current, only the refresh button refreshes"). So after any deploy or data change, the cache served old data until a MANUAL version bump. Bumping the version each time is a band-aid, not a fix. Audited + fixed 2026-05-26.

**How to apply (the standard for ANY cached dashboard page):** on load, render cached instantly (speed), then ALWAYS fire a background network re-fetch, write the cache, and re-render ONLY if the fresh payload differs (token-guarded so switching range/filter mid-flight can't clobber). Pattern:

```
const cached = readCache(key);
if (cached) { render(cached.data); revalidateInBackground(token, key, cached.data); return; }
// cold path: fetch + writeCache + render
async function revalidateInBackground(token, key, prev){ try{ const d=await fetchNetwork(); writeCache(key,d); if(isStale(token,key))return; if(JSON.stringify(d)!==JSON.stringify(prev)){ render(d); } }catch(_){} }
```

The network fn must hit the network (not another cache layer). Verify on the LIVE authed page that a cached load fires exactly 1 background API call (patch window.fetch + count).

**Cache audit of all dashboard pages (2026-05-26):**
- email-analytics.html (IDB `pb_ea_v*`): had the flaw. FIXED (SWR) + v7->v8 bump to clear the one existing stale cache.
- channel-attribution.html (IDB `CLIENT_DB_NAME`): had the flaw. FIXED (SWR).
- scheduled.html (localStorage): ALREADY did SWR. Fine.
- meta-ads.html: NO data cache, fetches meta_ads + hyros-revenue fresh every load. Fine (its stale issues were stale browser BUNDLES, not data cache; /meta-ads sends no-store).
- All other pages (scripts, emails, ideas, broadcast, revenue, youtube, instagram, facebook, book-meeting, index): no client API cache found.

If a NEW cached page is added, it MUST use the SWR pattern above. See [[project_dashboard_self_verify_authed]] for verifying on the live authed page.

## 2. Never overwrite a Chart.js canvas's parentElement.innerHTML on empty state

When a Chart.js canvas has no data, the wrong fix is `ctx.parentElement.innerHTML = '<div>No data</div>'`. That obliterates the canvas element. The next `getElementById(canvasId)` (when the user clicks a tab that DOES have data) returns null and the chart can never re-render.

**Symptom:** click YouTube tab (no content data) -> see "No content drove clicks in this window" empty state -> click Meta Ads tab (which has data) -> still see empty state, even though the data is in the cache. Charts permanently dead until full page reload. The data WAS cached correctly; the empty-state code on a prior tab destroyed the canvas DOM nodes, so the next tab's renderHorizontalBar hit `ctx === null` and either crashed silently or kept the dead empty-state in place.

**Fix pattern (use everywhere a Chart.js canvas might be empty):**

```js
function setEmptyOverlay(ctx, message) {
  if (!ctx) return;
  const parent = ctx.parentElement;
  if (!parent) return;
  let overlay = parent.querySelector('.section-empty');
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.className = 'section-empty';
    parent.appendChild(overlay);
  }
  overlay.innerHTML = `<div class="section-empty-title">${message}</div>`;
  ctx.style.display = 'none';
  overlay.style.display = '';
}
function clearEmptyOverlay(ctx) {
  if (!ctx) return;
  const parent = ctx.parentElement;
  if (!parent) return;
  const overlay = parent.querySelector('.section-empty');
  if (overlay) overlay.style.display = 'none';
  ctx.style.display = '';
}
```

Always call `clearEmptyOverlay(ctx)` BEFORE `new Chart(ctx, ...)` and `setEmptyOverlay(ctx, msg)` for empty cases.

**Where this bit:** `dashboard/channel-attribution.html` lines 566 (trend chart), 618 (donut), 658 (horizontal bars). Caught 2026-05-06 after the user reported the bug at least 3 times across the session before the actual root cause was diagnosed.

**Audit prompt:** before declaring a Chart.js dashboard done, grep the file for `parentElement.innerHTML`. Any match is a canvas-destruction bug. (The dashboard-dev skill bug-class checklist names this class + the grep; the helper code above lives only here.)

## 3. IndexedDB for client caches with multiple large entries

Use IndexedDB, NOT localStorage, for any client cache holding multiple data blobs >50KB each, or 10+ entries total (skill threshold phrasing: >5 entries or >50KB). localStorage's per-origin quota (~5MB on Safari, less under ITP) plus aggressive eviction means most writes silently fail; eviction-on-quota loops cannot recover because each retry re-serializes the entire cache, so large entries (75KB+) keep re-triggering QuotaExceededError and only the smallest entries survive.

**Symptom:** "Loading..." spinner on every page load even though the data was "cached"; dev inspection shows localStorage has only a few small entries, the big ones gone. Watch for QuotaExceededError in console or entries silently disappearing.

**Why IDB works:** 50MB+ quota (browser-managed, often 1GB+); per-key writes don't serialize the whole store, so one bad entry doesn't poison others; async API wraps easily with a sync-readable hot in-memory copy; hydration (~10-30ms) finishes before first loadAll awaits, so first cache-hit is still instant once warm.

**The full reference implementation** (`_open`/`_hydrate`/hot-copy `read`/`write`/`loadAll` awaiting `_readyPromise`) is documented verbatim in the dashboard-dev skill, section "Client-side cache: use IndexedDB for >5 entries or >50KB" (verified present 2026-06-12).

**Incident:** caught 2026-05-06 when the user kept seeing the loading spinner on every reload. localStorage cache had only 5 of 30 prefetched HYROS combos. Switching to IDB fixed it: all 35 entries persist, every page load instant from cache, no spinner unless the refresh button is pressed. Combine with rule 1: IDB caches must STILL be stale-while-revalidate.

## 4. Vercel kills fire-and-forget promises after the function returns

Vercel lambdas shut down the moment the response is flushed. Any unawaited `fetch(supabaseUrl,{...}).catch(() => {})` is aborted mid-handshake (the .catch() doesn't preserve the promise; the TCP socket closes). The Supabase write never happens. Always `await` side-effect writes to external systems (Supabase, Discord, etc.) before returning; adds 50-200ms but the write lands. If you genuinely need fire-and-forget on Vercel, use `context.waitUntil(promise)` (Edge runtime) or the `@vercel/functions` `waitUntil` helper. Never trust naked `fetch().catch()`.

**Symptom:** persistent caches that should be growing stay empty; background-write code looks fine in review; function logs show 200 OK; destination DB has zero new rows; cold restarts always rebuild from scratch.

Broken-vs-correct code is documented in the dashboard-dev skill as "Trap 2: Fire-and-forget side effects get killed" plus the multi-tier cache reference impl ("CRITICAL: AWAIT the upsert") (verified present 2026-06-12).

**Incident:** caught 2026-05-07 when the Precision Brass dashboard kept showing loading spinners despite a "fully populated" Tier 2 Supabase cache. Direct queries showed Tier 2 had ZERO hyros: rows. The Tier 2 write had been fire-and-forget for months; every cold lambda was a fresh HYROS fetch. (The skill notes it took 6 deploys to find; one curl on api_cache in hour 1 would have shown 0 rows.)

## 5. New dashboard route = update LOCKED_ROLE.allow_pages BEFORE deploy

When creating or routing to a NEW page under `dashboard/` on Precision Brass, before deploy:

1. Open `dashboard/lib/config.js`
2. Add the new `pagename.html` to `LOCKED_ROLE.allow_pages`
3. Otherwise `enforcePageAllowlist()` in `lib/auth.js` redirects to `allow_pages[0]` (currently `scripts.html`)

**Why:** 2026-05-13. Built a new `/scheduled` calendar page and deployed it. Timo clicked the new "Schedule selected" multi-select flow on /emails; the button navigated to `/scheduled?ids=...` which IMMEDIATELY redirected to `/scripts` because `scheduled.html` was missing from `LOCKED_ROLE.allow_pages`. He'd been told the flow was ready, hit a dead end, and was rightfully pissed. The fix was one line of config.

The admin-only `ADMIN_EMAILS = '*'` bypass exists, but Timo's session apparently resolves as restricted-role for reasons not yet traced. Don't rely on the admin bypass to dodge updating the allowlist. The allowlist is the source of truth.

**How to apply:** any time a new HTML file is created under `dashboard/`, or any page adds a `window.location.href = '/newpage'` jump, grep `lib/config.js` for `allow_pages` and confirm the destination is in the list. If it isn't, add it BEFORE saying "deployed" or "ready to test". See `canon_deploy_verification.md` section 2 (walk the flow); also enforced as item 7 of the UI polish checklist (`~/.claude/knowledge/ui-polish-checklist.md`).

## 6. Ad blockers cosmetically hide ad-keyword CSS classes

**Symptom:** a dashboard section renders for me (Chromium/Playwright) and in the user's INCOGNITO window, but is BLANK in their normal browser profile (tabs/header show, content grid empty, no console error).

**Cause:** an ad blocker extension (uBlock, AdBlock, etc.). Incognito disables extensions by default, which is the tell. Ad blockers apply EasyList-style COSMETIC filters injecting `display:none !important` on any element whose class matches `ad-`, `ads`, `banner`, `sponsor`, `promo`, `doubleclick`, or attribute `[data-ad]`. The Precision Brass meta-ads cards were class `ad-card` / `ad-card-grid` / `ad-thumb` / `table.ads` / `ad-cell` -> all silently hidden. (2026-05-28)

**Proven, not guessed:** reproduce by injecting `[class^="ad-"]{display:none !important}` on the live page -> the cards vanish while tabs stay = the exact symptom. After renaming, inject an aggressive `ad-/ads/banner/sponsor/promo/[data-ad]` filter and confirm cards STAY visible.

**Fix:** rename every ad-keyword CSS class/attr to a NEUTRAL name with no `ad`/`ads` substring. meta-ads now uses `creative-card`, `creative-grid`, `creative-thumb`, `creative-cell/flex/text`, `table.creatives`, `data-cid`. Inner `ac-*` classes were already safe (no `ad` substring). Data fields (`meta_ads`, `ad_id`, `ad_set_id`) are NOT classes, leave them.

**Prevent:**
1. Never name viewer-facing UI with `ad`, `ads`, `advert`, `banner`, `sponsor`, `promo`, `doubleclick` in a class/id. For an ads dashboard use `creative-*`, `campaign-*`, `unit-*`, or a `pb-` prefix.
2. "Works in incognito, blank in normal browser" -> suspect ad blocker FIRST. Ties to global failure pattern #3 (verify in the real browser + its extensions, not Chromium/curl).
3. Related: Safari no-store cache (canon_deploy_verification.md section 6, the other "stale/blank after deploy" cause), worktree rule below.

## 7. Dashboard iframe (html_full) needs the FULL HTML doc, not body innerHTML

The dashboard renders rich content (`type: 'html_full'`) inside an iframe via `srcdoc=` (see `dashboard/scripts.html` line ~875). The iframe is a sandboxed standalone document and does NOT inherit the dashboard's CSS. Uploading only body innerHTML (class names, no `<style>` block) means Harrison sees a wall of unstyled plain text instead of the color-coded beat layout.

**Why:** the prior pb-script-write said "extract body innerHTML for upload." Wrong. Caught 2026-05-06 when Timo opened the famous-method-killing-embouchure script in the dashboard and saw plain text instead of the PDF's colored layout.

**How to apply** for any dashboard upload using `type: 'html_full'`:

```python
with open(html_path) as f:
    full_html = f.read()  # READ THE WHOLE FILE
body = [{'type': 'html_full', 'content': full_html, 'pdf_url': pdf_url}]
```

Do NOT split on `<body>`. Do NOT extract innerHTML. Upload the entire file including `<!DOCTYPE>`, `<html>`, `<head><style>...</style></head>`, and `<body>`.

The iframe's `sandbox="allow-same-origin"` lets the embedded `<style>` apply but blocks scripts, so fonts via `<link href="https://fonts.googleapis.com/...">` may or may not load. Inline-define system font fallbacks just in case.

Applies to: pb-script-write (scripts table), pb-email-write (email_proposals) if emails ever use html_full, and any future html_full upload. Note 2026-06: email bodies now have 3 render surfaces with their own DOMPurify allowlists (see project_email_body_render_surfaces.md).

## 8. Ship polish, not skeleton (the 7-point + route/flow checklist)

Do NOT ship the literal minimum. Before declaring any UI feature "ready" / "live" / "done", run this checklist (canonical expanded copy: `~/.claude/knowledge/ui-polish-checklist.md`, printed by the dashboard-deploy-gate hook at deploy time; summarized as the "UI Polish Gate" in the dashboard-dev skill, both verified present 2026-06-12):

1. **Orphan UI?** Any button or element that doesn't do something useful? Delete it. (Caught: Today button on calendar nav that did nothing because the user was already on today's month.)
2. **Consistent flows?** Does the new flow look and behave like related flows in the same app? Single-email vs multi-email schedule should not have different UIs. (Caught: broadcast.html had its own Send Now + Schedule split that didn't match the new /scheduled?ids= queue+calendar layout.)
3. **Obvious affordance?** Does every interactive element LOOK clickable? Default `<select>` on dark mode = ugly + unclickable-looking. Custom button with stripe, label, big chevron, raised shadow = obviously a button. (Caught: native dropdown that looked unclickable.)
4. **Diagnosability?** If something is wrong, can the user click to see why? Read-only labels that hide the underlying data are a trap. (Caught: scheduled email pills on the calendar that you couldn't click to see body/time/list.)
5. **Warning prominence.** Does the warning actually warn? Red banner at the BOTTOM of the page when the action button is at the TOP fails. (Caught: conflict warning under the calendar instead of above the Schedule button.)
6. **Label consistency.** Does the sidebar say the same thing the page title says? Same name across all pages? (Caught: sidebar said "Schedule" while everywhere else said "Scheduled".)
7. **Route allowlist.** New page = update `dashboard/lib/config.js` `LOCKED_ROLE.allow_pages` (rule 5 above).
8. **Walk the flow.** Click entry point > destination, actually arrive there, see the UI you expect. Not "0 console errors on a redirect to /scripts" (canon_deploy_verification.md section 2). (The knowledge-file version adds a 8th/contrast check: full-contrast color + 12px+ for data text, chips for 4+ facts.)

**Why:** 2026-05-13. Built /scheduled calendar + multi-select bulk schedule. Timo had to manually correct EVERY item above in one session. His words: "I feel like there are a lot of features that you weren't inclined to include, and I had to really guide you through." I was shipping the literal minimum and waiting to be told what was missing, instead of inferring what polish a reasonable designer would add. Specific catches: ugly native select, dead Today button, single-email flow not unified with multi, scheduled pills not clickable, conflict warning buried, "Schedule" vs "Scheduled emails" mismatch.

**Meta-pattern:** "does the code run" is not the done bar. The done bar is "would Timo use this without rolling his eyes." Functional is necessary, not sufficient. Before saying done: walk the flow once end to end, identify every clickable thing and label; for each ask "what would a polished version look like?"; match new elements to the analogous nearby thing (label, layout, affordance); proactively say "while I was in here I also noticed X, want me to fix that?" Applies workspace-agnostic: Robinson's Remedies, Tim Maines, Precision Brass, blog work, any UI.

## 9. Content Suggestions hub: TWO independent admin gates

The Content Suggestions / Content Hub (dashboard/suggestions.html, tables `content_items` + `content_clients` + `content_admins`) gates admin access in TWO independent places. Granting someone admin requires updating BOTH or the UI lies:

1. **Frontend**: `dashboard/lib/config.js` `ADMIN_EMAILS`. Controls whether `PB_ROLE.role === 'admin'` -> shows the "Suggesting for" client picker + admin UI. If only this is set, the picker appears but shows "No clients yet" and 0 items because the DB blocks the reads.
2. **Database**: `content_admins` table (email rows). `is_content_admin()` (SECURITY DEFINER, checks `lower(email)` against `auth.jwt()->>'email'`) backs the RLS policies `content_clients admin all` and `content_items admin all`. Without a row here, RLS returns nothing for other clients.

Items are per-client: `content_items.client_id` = the client's **auth.users.id**, and `content_clients.id` is ALSO that same auth uid (NOT a random uuid). Client RLS = `content_items.client_id = auth.uid()`. A non-admin only ever sees rows stamped to their own login; a client sees nothing if items are stamped to a DIFFERENT account.

**Why (2026-06-02):** Timo reported "I uploaded 6 IG links, Content Suggestions shows Nothing here yet." The 6 rows WERE uploaded and correctly stamped to Harrisson (harrissonball@precisionbrass.info). Timo saw nothing because he was logged in as `trombonetimollc@gmail.com` (his 2nd account), neither admin nor Harrisson, so the per-client filter returned his own empty list. Fix: added trombonetimollc@gmail.com to BOTH config.js ADMIN_EMAILS (commit on origin/main) AND content_admins table. The DB half was caught ONLY by testing end-to-end as that exact account (frontend showed admin picker but "No clients yet" until the content_admins row existed).

**How to apply:** grant content-hub admin = add email to config.js ADMIN_EMAILS AND insert into content_admins. Verify a client can see their items by minting THAT client's session and loading the page ([[reference-view-authed-dashboard]]); do NOT just check the DB. Two admin gates, verify as the real account.

## 10. The 7-step UI bug diagnostic protocol

When the user reports a UI / CSS / layout / visual bug, follow this protocol. Don't deviate. NOT in the dashboard-dev skill (only the narrower root-cause-before-patch rule is); this is the canonical copy.

**Why this exists:** caught 2026-05-17 when the meta-ads dashboard column-misalignment bug took multiple sessions and angry user feedback before finally running `getBoundingClientRect()` on the live page and finding the real cause (missing `table-layout: fixed`). User verbatim: "I've told you this a million times, but every time you say 'Oh, I get it,' but then you don't fucking do shit." Every prior attempt patched a visible symptom instead of diagnosing the structural cause.

### Step 1. Replay the user's exact complaint, with their words
If they said "the SPEND column shows 1 and LEADS shows $7.39," the diagnostic is about those specific column labels and those specific data values. Do not translate to "the columns look weird." Don't lose the specifics in paraphrase.

### Step 2. Get measurable evidence from the live page
For layout bugs: Playwright `browser_evaluate` extracting `getBoundingClientRect()` for every relevant element (headers, data cells, etc). Compare positions numerically.

```js
const tbl = document.querySelector('table.X');
const ths = [...tbl.querySelectorAll('thead th')];
const tds = [...tbl.querySelectorAll('tbody tr:first-child td')];
const pos = el => ({ left: el.getBoundingClientRect().left, right: el.getBoundingClientRect().right });
// Assert: for each i, ths[i] position == tds[i] position
```

For content bugs: screenshot + Read + assert the specific text the user named is present at the specific location. For state bugs: log the relevant variables at the point of failure, not at the point of mount. **Eyeballing a screenshot is NEVER enough.** Anti-aliasing, device pixel ratio, font rendering, and pattern-matching bias all distort what you think you see. Use coordinates.

### Step 3. State your hypothesis BEFORE the fix attempt
Write it as a falsifiable claim, e.g. "I believe the SPEND header is at x=673 but the SPEND data value is at x=775 because the table uses table-layout: auto which treats col width as hints, allowing column widths to vary per row based on content." If you can't write the hypothesis with element selectors and CSS property names, you haven't diagnosed the bug. Back to Step 2.

### Step 4. Fix the root cause, not the symptom
A symptom-fix tweaks a visible value (column width, padding, font size). A root-cause fix changes the underlying mechanism (table-layout, box-sizing, flex-direction). Symptom fixes work in one configuration and break in another. If two symptom fixes have already failed, the third attempt is FORBIDDEN until the root cause is identified and written down.

### Step 5. Verify with the same coordinates check that diagnosed the bug
After deploy, re-run the Step 2 `getBoundingClientRect()` check. Confirm header.left == data.left for every column. The verification protocol must be the SAME as the diagnostic protocol, otherwise you're checking a different thing than the user's complaint.

### Step 6. Add a code comment explaining why the fix exists
Any non-obvious CSS rule that prevents a specific bug class gets a comment pointing at the bug it prevents. Without it, the next session sees a "weird rule" and removes it as cleanup.

### Step 7. Save the lesson to memory if the bug took more than one attempt
Name: the bug class, the diagnostic technique that finally worked, the fix, a short prevention rule.

### Forbidden behaviors
- **"I see the problem" without coordinates.** Either say "I have N hypotheses, let me verify which" or stay silent until coordinates are pulled.
- **Bypassing `dashboard-deploy-gate` for a UI bug.** The gate forces Playwright verification; that friction is the point.
- **Iterating after 2 failed fixes.** Stop, enumerate prior attempts and why each failed, propose a fresh diagnostic plan.
- **Going faster when the user is angry.** Slow down. One slow-but-correct response costs far less than three fast-but-wrong ones.
- **Eyeballing a thumbnail as "visual verification."** Visual verification requires extracted measurable properties.

### Specific to layout / CSS bugs
- Look up the actual W3C / MDN spec behavior of the elements involved (col, sticky positioning, border-collapse, flexbox container queries). These are knowable. Don't guess.
- The default value of every CSS property matters. `table-layout: auto` is default and treats col width as hints. `box-sizing: content-box` is default and excludes padding. `position: static` is default and ignores left/top. Verify what default you're working against.
- When you change one CSS property, document what other properties it now depends on. `table-layout: fixed` only works if col widths are set. `position: sticky` only works inside a scrolling container. Constraints compose.

### Specific to recurring bugs
If the user says "I've told you this multiple times," the next action is NOT another fix attempt. It's: (1) a written enumeration of every prior fix attempt with timestamps if visible in git history, (2) why each failed (symptom addressed vs root cause missed), (3) a fresh diagnostic plan starting from Step 1. THEN a fix. Skipping the enumeration is what makes the count keep climbing.

## 11. Diagnose runtime state, don't guess from config

When a user reports a UI/auth/permissions bug WITH a screenshot, the FIRST move after reading the relevant file is to surface the actual runtime state: what email the session has, what role resolved, what nav items the page emitted. Do NOT propose remediation (clear cache, sign in fresh, private window) before reading what the running page actually thinks is true.

**Why:** 2026-05-06 dashboard incident. Timo asked to open the email/analytics dashboard. His screenshots clearly showed scripts.html with one nav item. I kept reopening standalone.html, telling him to sign in again, suggesting private windows, blaming stale cookies. Took 8+ prompts and a profanity-laden "do not talk to me until this is fixed" before adding a debug badge that would have revealed the actual issue in 30 seconds. The config (`ADMIN_EMAILS` includes timothyjay.maines@gmail.com) was correct on disk. The runtime check was failing for a reason never inspected because the config file was trusted.

**How to apply:**
- UI/auth/permissions bug + screenshot = first action is `console.log` or visible badge of runtime state (logged-in email, resolved role, computed nav allowlist), on move 2, not move 8. Not "try X and see."
- Config on disk is necessary but not sufficient. Always verify runtime values match config values.
- "Sign in again, clear cache, private window" is a guess, not a diagnosis. Suggesting it before reading runtime state = stalling.
- Read the user's screenshot literally. Sidebar shows ONE nav item but source has FOUR = the gating filter firing, not the wrong page. Match visible state to file source before proposing anything.
- The AUDIT GATE in global CLAUDE.md governs this: test the assumption that defines the problem before prescribing.

## 12. NEVER seed demo or fake data into the dashboard

**Zero seed data. Zero demo rows. Zero placeholder content. Ever.** Standing rule from 2026-04-28. HIGH SEVERITY trust failure, same tier as fabricating VOC quotes or shipping unverified behavioral claims.

Applies to all Supabase tables feeding any user-facing dashboard at `Precision-Brass/dashboard/`: `ideas`, `scripts`, `harrison_suggestions`, `email_proposals`, `email_sends`, and any future tables. Empty state is the correct first-run state; the page renders its empty placeholder ("Nothing here. This column is clear.") on day one. Real content enters only via production paths: `/pb-script` then `/pb-ideas-push` (ideas), `/pb-script-write` (scripts), `/pb-email` then `/pb-email-push` (email_proposals), "Log a Send" form on email-analytics.html (email_sends), the dashboard's own Submit button (harrison_suggestions).

**Why:** Timo lost trust in the script approval pipeline on 2026-04-28 because the original schema.sql contained 4 seeded scripts ("The mouthpiece question...", "Why your range stopped growing at 52...", "The 6 minute embouchure reset...", "The 30 minute practice...") inserted with `on conflict (id) do nothing`, intended as demo content. Two carried fake `notes` text ("Section 3 feels rushed. Add a demo of the slur exercise...") and one was seeded with status='approved', making it appear Harrison had approved a script he had never seen. Timo thought the approval flow was broken when it was correct; the seed data had skipped the entire flow. Also deleted same day: 2 "(Demo)" PDF flow test scripts left in the table from skill testing.

**How to apply:**
1. **Schema files:** `dashboard/setup/schema.sql` and any future schema files contain ONLY `create table`, triggers, and RLS policies. Zero `insert into ... values` blocks.
2. **Skills:** pb-ideas-push, pb-script-write, pb-email-push, fb-vault, yt-vault, etc. must never insert "test"/"demo" rows to verify wiring. If a test is needed, use a temporary id prefix like `test_` and DELETE before the session ends.
3. **Test uploads:** any end-to-end test row against live Supabase gets deleted in the same session it was created. No exceptions.
4. **Visual QA / screenshots:** mock with a separate file (a `*-preview.html` outside the deploy path, or a screenshot in the plan), never a real INSERT into a production table.
5. **Found seed data already in the db:** delete immediately when surfaced, strip the seed block from whatever file generated it, save a memory entry if it's a new pattern.

**Also applies to hardcoded UI numbers:** KPI cards, chart axes, leaderboard rows, sample data in JS objects (`VIEWS`, etc.). Until the data source is hooked up: KPI cards show `$0` / `0` / "No data yet"; charts show empty state ("No data in this window"); tables show empty state ("No sends logged..."); date-comparison deltas like "+214% vs last month" are NEVER hardcoded, compute from live data or omit. Violation caught 2026-04-28: email-analytics.html KPI cards hardcoded `$16,800 +214%` / `3,840 +12.2%` / `299 +38%` / `24 +71%` from the mockup; even with JS wired to overwrite on load, the user saw fake numbers on first paint and lost trust. Fix: HTML defaults of `$0` / `0` / "No data yet" so the page is honest even if JS fails. Principle: a Precision Brass dashboard never displays a number the underlying database cannot back. If in doubt, delete the row and ask Timo before re-adding.

## 13. Lightweight YouTube fetch: the lightest tool that returns the data

For YouTube metadata (title, author, thumbnails, description, tracked-link extraction), use the lightweight stack; reserve Playwright for actual rendered-page screenshots:

1. **Thumbnails** are predictable URLs, no API call: `https://i.ytimg.com/vi/{VIDEO_ID}/mqdefault.jpg` (also `default.jpg`, `hqdefault.jpg`, `maxresdefault.jpg`).
2. **Title + author + provider** via oEmbed (no auth, JSON): `curl -s "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VIDEO_ID&format=json"`.
3. **Full description** via curl + regex on the watch page HTML: extract `"shortDescription":"..."` from `ytInitialPlayerResponse`.
4. **Convenience helper:** `dashboard/scripts/yt-fetch.sh VIDEO_ID` prints all of the above as one JSON blob, including tracked-link extraction. (Also referenced as `scripts/yt-fetch.sh`.)
5. **Full metadata + transcript + comments:** `yt-dlp` if installed (canonical for ingestion). Browse `youtube-database/index.json` for what's already stored.

**Why:** 2026-05-15. Used `mcp__playwright__browser_navigate` + `browser_evaluate` to read YouTube descriptions: spawns headless Chromium, navigates, waits for hydration, runs JS, closes. About 100x more expensive than curl + python3 regex. Timo: "Why aren't you using YouTube fetch to just get the thumbnail and description and stuff? It's just kind of fucking annoying the way you're doing this. You're doing this in a really inefficient way."

**Generalization:** browsers are for rendering verification; HTML is for parsing; APIs are for structured pulls. If the data is in `<meta>` tags or a JSON blob in page source, never launch a browser. Playwright IS correct for screenshots of rendered pages (channel banner, video player UI, dashboard verification). Related: [[query-destination-schema-first]] (same "right primitive, not heaviest tool" family).

## 14. Concurrent repo use = git worktree; durability = push to origin/main

When a second Claude session (or any process, e.g. the meta-ads/scrape bots) is actively committing in the SAME git repo, the shared working directory is unsafe: the other process's `git checkout` / `git reset` silently clobbers your uncommitted (or even feature-branch-committed) work.

**What happened (2026-05-28):** while staging channel-attribution.html + hyros-source-map.js on a new branch off main, a concurrent meta-ads worker committed onto MY branch, then ran `checkout main` + `reset --hard origin/main`, wiping the staged changes. Reflog showed the whole hijack. git's working dir + HEAD are shared state across one checkout; two agents in it = the 4-failure-pattern "shared state breaks everything."

**How to apply:**
1. `git worktree add -b <branch> ../<repo>-wt-<task> <base>` gives a separate working dir + separate HEAD, immune to the other process's branch switches.
2. Do all edits, commits, and verification in the worktree.
3. Land WITHOUT touching the shared dir: `git push origin <branch>:main` (fast-forward). If rejected, `git fetch && git rebase origin/main` in the worktree and retry. Confirm your files are disjoint from the other agent's first; the disjoint-files check is what makes the fast-forward land clean (meta-ads worker touched only meta-ads.html; I touched only channel-attribution.html + hyros-source-map.js).
4. `git worktree remove --force` + `git worktree prune` when done.

**ADDENDUM (2026-06-05): the shared working tree can be BEHIND origin/main, so `vercel --prod` from it REGRESSES prod.** The scrape/meta-ads bots had advanced origin/main 37 commits while the local working dir sat on an old HEAD (96ca06a) with a pile of uncommitted changes. `vercel --prod` from that dir shipped my features but DROPPED 9 `dashboard/thumbnails/*.jpg` that existed in origin/main but not locally, so suggestion tiles 404'd on prod. Before ANY `vercel --prod`: run `git fetch origin main` then `git diff --diff-filter=D --name-only origin/main -- dashboard/ api/`. If that lists ANY deployed file, your tree is stale and you WILL regress prod. Safest pattern: never deploy the shared working tree. Land features to origin/main first (worktree at origin/main, `git apply` a `git diff origin/main -- <files>` patch, push), THEN deploy from a clean origin/main checkout. Recover a stale-tree regression: `git checkout origin/main -- <missing paths>` then redeploy.

**CRITICAL ADDENDUM (2026-05-29): a local commit + `vercel --prod` is NOT durable. You MUST push to origin/main.** This repo has a "Daily PB scrape" bot that pushes to origin/main on its own schedule, and Vercel auto-deploys from origin/main. A change only committed locally (or only deployed via `vercel --prod` from the working dir) gets REVERTED the next time the scrape bot pushes, because Vercel rebuilds from origin/main which lacks your commits. This silently reverted the "any sale = winner" classify fix overnight: the commit lived only on local main, never on origin, so the scrape push + git auto-deploy served the pre-fix bundle. **Always finish dashboard/api work with `git push origin main`** (rebase onto origin/main first; the scrape bot only touches `voc/emails/performance/*`, so it never conflicts with dashboard/api files). Verify the prod alias still serves your marker AFTER the git-triggered build settles, not just after your local `vercel --prod` (see canon_deploy_verification.md section 1 / scripts/verify-deploy.sh).

## Source files (absorbed 2026-06-12)
- feedback_dashboard_cache_swr.md
- feedback_canvas_destroy_on_empty_state.md
- feedback_idb_for_large_client_cache.md
- feedback_vercel_kills_fire_and_forget.md
- feedback_new_route_check_auth_allowlist.md
- feedback_adblocker_hides_ad_classes.md
- feedback_dashboard_iframe_needs_full_html.md
- feedback_ship_polish_not_skeleton.md
- feedback_content_hub_two_admin_gates.md
- feedback_ui_bug_diagnostic_protocol.md
- feedback_diagnose_dont_guess.md
- feedback_no_seed_data.md
- feedback_use_lightweight_youtube_fetch.md
- feedback_concurrent_repo_use_worktree.md
