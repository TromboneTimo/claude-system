# Phases 6-8: Preview deploy, approval gate, production + verify

## Phase 6: Vercel env vars + PREVIEW deploy
Set the env vars the api functions read (login itself needs none of these; it works off
config.js, but set them so functions do not crash):
```bash
cd "/Users/air/Desktop/<Client Name>"
add_env(){ printf '%s' "$2" | vercel env add "$1" production; }
add_env SUPABASE_URL "https://<new_ref>.supabase.co"
add_env SUPABASE_PROJECT_REF "<new_ref>"
add_env SUPABASE_SERVICE_ROLE_KEY "<new_service_role_jwt>"
add_env SUPABASE_ANON_KEY "<new_publishable_key>"
# AC / HYROS / secrets: leave unset unless the client provided them; note them as TODO.
vercel link --yes --project <slug>     # slug must be lowercase, no spaces, no '---'
vercel --yes                            # PREVIEW deploy (NOT --prod)
```
Grab the preview URL from the output.

Sanity-check the preview is public and serving the app (not a Vercel SSO wall):
```bash
curl -sS -m 20 -I "<preview_url>/login" | grep -iE "HTTP/|x-vercel"
curl -sS -m 20 "<preview_url>/login" | grep -oiE "<Client Name>|Sign in|Authentication Required" | sort -u
```
If you see an SSO/"Authentication Required" wall, deployment protection is on; turn it off for
this project in Vercel settings (or note it for Timo) before calling it done.

## Phase 7: STOP for approval (mandatory)
Present a tight summary and WAIT for an explicit yes:
- preview URL
- Supabase project ref + region
- pages included
- accounts: client email (their password) + admin emails (password = "same as Precision Brass")
Do not run `--prod` until Timo approves.

## Phase 8: Production + per-role verification
```bash
vercel --prod --yes
```
Then verify in a REAL browser (Playwright), per role. Curl proves reachability, not auth.

CLIENT (restricted):
1. login at `<prod>/login` with the client email+password -> lands on their first page.
2. snapshot the sidebar: it shows ONLY their client-facing pages. No admin section/links.
3. navigate directly to an admin URL (e.g. `<prod>/hooks`) -> redirected back out.
4. console errors = 0 (empty-state zeros are fine, they are not errors).

ADMIN (Timo):
1. login with an admin email + the PB password -> lands fine.
2. admin nav section is visible; open EACH selected page -> all load, 0 console errors.
   (Empty Content Hub pages should show empty state, NOT "could not load X" -- that would mean a
   table is still missing; go back to phase 3.)

CONTENT PARITY + VISUAL (do this, it is where the clone silently fails):
- For every shared library you copied (e.g. `hooks`), confirm the new project's row count equals
  PB's. An empty page throws zero console errors, so "0 errors" does NOT mean populated.
- Actually LOOK at a populated page. Take a full screenshot and read it yourself. Images
  (thumbnails, logos, avatars) load with no "No thumbnail"/broken-image placeholders. A broken
  `<img>` 404s silently with no console error, so component-exists and console-clean both miss it.
  Spot-check the referenced files over HTTP too: `curl -I <prod>/thumbnails/<id>.jpg` -> 200.
- The bar for "done" is: the client's page renders the way PB's does. Not "the table exists",
  not "it loaded without errors". Compare to the source with your own eyes before handoff.

Report PASS/FAIL with the specific evidence (which roles, which pages, console counts, row-count
parity, screenshot read). A login that lands fine but has a bouncing nav link, an empty library,
or broken thumbnails is a FAIL.

Playwright note: the MCP browser profile can hold a stale lock from a prior run. If navigate/
snapshot errors with "Browser is already in use", `pkill -f mcp-chrome` and remove the profile's
`SingletonLock`/`SingletonSocket`, then retry. Sign out between roles via
`window.PB_SUPABASE.auth.signOut()` (browser_evaluate) since login.html auto-redirects an existing
session back into the app.
