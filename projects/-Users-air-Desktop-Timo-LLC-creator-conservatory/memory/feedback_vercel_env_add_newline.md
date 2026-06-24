---
name: Vercel env add - never echo, use printf
description: Piping values to `vercel env add` with `echo` appends a trailing newline that gets stored literally and breaks API calls.
type: feedback
originSessionId: 51f2c306-fba9-4509-8219-75955722ae14
---
When adding env vars via `vercel env add` from a pipe, use `printf '%s' "$VAL" | vercel env add NAME production`, NOT `echo "$VAL" | vercel env add`.

**Why:** `echo` adds `\n`. `vercel env add` reads the full stdin including the newline and stores it literally as part of the value. Pulling the env back shows `VAR="actual-value\n"`. Google Sheets API (and most others) reject IDs with newlines with an opaque 500, not a parse error.

**How to apply:** Any time I'm scripting `vercel env add` from a pipe, use `printf '%s'`. Also applies to piping secrets/tokens to any CLI that reads from stdin (gh auth login, gcloud auth, etc.). When in doubt: `vercel env pull .env.check` and grep the value for literal `\n` before trusting it.

**Symptom to recognize:** API call returns 500 "Something went wrong" generic error on a handler that worked on another project with the same env var names. First check: `vercel env pull` and inspect the raw value for trailing characters.

2026-04-15: bit me on video-downloader-plugin deploy. Landing page API returned 500 for ~10 minutes until I pulled the env and saw `SPREADSHEET_ID="1x-mlfNS...\n"`.
