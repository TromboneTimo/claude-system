---
name: project-comments-intelligence-20260517
description: "Comments tab on channel-attribution.html ships 2026-05-17. Scrapes FB Page + Instagram comments via Meta Graph API. Pattern analysis (theme clustering, top questions) is the next phase, runs INSIDE the Claude session on demand (zero LLM API cost)."
metadata: 
  node_type: memory
  type: project
  originSessionId: 467afc37-9455-4e76-8762-b666eca3bdcb
---

# Comments Intelligence. Foundation Shipped 2026-05-17

**Why:** Per Timo 2026-05-17. He wants a tab on channel-attribution that scrapes comments and DMs across FB / IG / YouTube and surfaces question patterns. Foundation built this session; intelligence layer is the next session's work.

**How to apply (this session, shipped):**

1. **Endpoint:** `/api/ac?action=meta-comments`. Inlined into ac.js to stay under Vercel Hobby plan's 12-function cap. Pulls FB Page posts + IG media via Meta Graph v22.0, then comments per post. Authed via Supabase JWT (dashboard users) or x-perf-secret (perf warmer).
   - Query params: `platform=facebook|instagram|all`, `days=N` (default 90), `post_limit=N` (default 25), `comments_per_post=N` (default 50).
   - Response: `{ counts: {facebook, instagram, total, questions}, window_days, errors, page_id, ig_id, comments: [...] }`.
   - Each comment: `platform, post_id, post_message, post_url, comment_id, author, body, like_count, reply_count, created_at, is_question`.
   - Heuristic question detection: ends in `?` OR starts with how/what/why/when/where/which/who/can/does/do/is/are/am/will/would/should/could/may/might.

2. **UI:** View switcher on channel-attribution.html toggles between "Attribution" (default, existing revenue view) and "Comments" (new). Comments view = filter dropdowns (platform + question-only) + summary bar + scrollable comment list. State persisted to `pb_ca_view` localStorage.

3. **Live data:** First fetch returned 772 comments (168 FB + 604 IG, 33 flagged as questions) across 90-day window. Page ID 1018199588043827 (Precision Brass), IG business ID 17841400206268158.

4. **Token:** `META_USER_TOKEN` in Vercel env. Long-lived user token. Server exchanges for page token on each call (cached 30 min in memory). Scopes: `pages_read_user_content, pages_read_engagement, instagram_basic, instagram_manage_comments, ...`. Stored at `~/.claude/credentials/MASTER.md` under "Precision Brass / Meta Graph API". Token expires 2026-07-16; re-extend at developers.facebook.com/tools/debug/accesstoken.

## Next-session work (intelligence layer)

When Timo says "show me comment patterns" or "what are people asking", the agent should:

1. Fetch comments via `/api/ac?action=meta-comments&days=180&platform=all&post_limit=50&comments_per_post=100` (wider window for pattern analysis).
2. Run analysis INSIDE the Claude session (no LLM API cost, since the session is already running):
   - Cluster comments by theme using semantic similarity
   - Extract top 10 questions by frequency
   - Surface unanswered questions (Harrison didn't reply)
   - Flag comments mentioning specific pain (range, embouchure, mouthpiece, age, pressure)
   - Identify content gaps (questions Harrison hasn't addressed in videos)
3. Output a structured report in chat (top questions, themes, content recommendations).

Could also fold the analysis into pb-script's mining agents. Make YouTube/FB/IG comments a first-class corpus alongside sales calls and testimonials. Probably the right home for the long term.

## DMs (deferred)

Current Meta token does NOT have these scopes:
- `pages_messaging` (FB Messenger DMs)
- `instagram_manage_messages` (IG DMs)

To add DMs: Timo re-extends the token at developers.facebook.com with the additional permissions. Once added, mirror the comments endpoint pattern with `/me/conversations` and `/{conversation_id}/messages`.

## YouTube comments

Not yet wired into the dashboard endpoint, but the data exists locally at `youtube-database/{video_folder}/comments.json` (top 200 per video for 4 videos = ~800 comments). Easy add: extend `action=meta-comments` (or rename it `action=comments`) to also bundle YouTube comments by reading the static asset paths via the Vercel deployment's bundled files.

## Cron auto-refresh (deferred)

Manual refresh button only this session. Adding a Vercel cron (every 6h) that stores recent comments to a Supabase `comments` table would enable:
- Trending analysis over time
- "New comments since last visit" badge
- Faster page load (read from Supabase vs Meta API each time)

## File map

- `api/ac.js` (action=meta-comments). The endpoint.
- `dashboard/channel-attribution.html` (Comments view + Attribution view switcher). The UI.
- `~/.claude/credentials/MASTER.md` (Precision Brass / Meta Graph API section). The token.
- Cross-reference: [[project-8-agent-restructure-20260515]] for the broader VOC mining architecture.
