---
name: tim-reddit
description: Tim Maines Reddit agent. Drafts/schedules/publishes posts to subreddits via Zernio. Triggered by /tim-social reddit ... Do not invoke directly without orchestrator unless user explicitly says "tim reddit".
user_invocable: false
---

# Tim Maines Reddit agent

## Identity gate
- Reddit account is **NOT YET CONNECTED** to Zernio. Before this skill can post, Timo must OAuth Reddit at zernio.com and run `python3 ~/.claude/skills/tim-social/scripts/zernio_refresh.py` to lock in the account ID.
- Reddit personal brand requires authenticity. Mods detect promotional accounts fast. The 9-1 rule (9 value-adding contributions per 1 self-promo) is canonical.

## Inputs
- `mode`: `draft` | `publish` | `schedule`
- `kind`: `text` | `link` | `native-video`
- `subreddit`: target sub (without "r/" prefix)
- `title` (max 300 chars)
- `body` (text post)
- `url` (link post)
- `media` (native video)
- `flairId` (some subs require)
- `scheduled_for`: ISO 8601 if mode=schedule

## Workflow
1. Load voice spec / methodology fallback. Refuse if missing.
2. Load `tim-maines/reddit/best-practices.md` (mandatory). Apply: 9-1 rule, AMA prep checklist, per-subreddit format conventions, hot/top/best/controversial sort signals, AI-spam moderation triggers.
3. Load accounts JSON, confirm `reddit` exists. If not, refuse and prompt OAuth.
4. Pre-flight: validate subreddit exists via `GET /v1/tools/validate/subreddit?subreddit=<name>&accountId=<id>`. Check if it requires flair via `GET /v1/accounts/{id}/reddit-flairs?subreddit=<name>`.
5. Generate post per format conventions (title 60-80 chars question-style; body = problem -> personal experience with numbers/steps/mistakes -> options including ours neutrally -> open question; TLDR top or bottom). Confirm with user before publish.
6. Call `zernio_post.py --platform reddit --account-id <id> --content "<body>" --mode <mode>` plus subreddit + title in `redditSettings`.
7. Log to `tim-maines/reddit/posts/YYYY-MM-DD-r-<sub>-<slug>.md`. Include the subreddit in slug for searchability.

## Reddit request body shape
```json
{
  "content": "<body text>",
  "platforms": [{"platform": "reddit", "accountId": "<reddit_account_id>"}],
  "publishNow": true,                  // for publish
  "scheduledFor": "<iso>",             // for schedule
  "redditSettings": {
    "subreddit": "Entrepreneur",        // without r/
    "title": "<title up to 300 chars>",
    "url": "<for link posts>",
    "flairId": "<if required by sub>",
    "forceSelf": false,                 // true forces text post even if URL provided
    "nativeVideo": true                 // for video posts via Reddit CDN
  }
}
```

## Limits and caveats
- Title max 300 chars.
- Mods auto-remove undisclosed affiliates in business subs (r/Entrepreneur, r/SaaS). Disclose: "I work for [X], here's what we learned."
- AI content detection in 2026 flags repetitive phrasing, low-effort posts, bot-like patterns. Write personally.
- Karma decay penalizes older low-engagement posts. New accounts have less reach until they build karma.
- Subreddit-specific automod rules vary. Pre-validate via `GET /v1/tools/validate/subreddit` before posting.
- Engagement bait ("Upvote if agree!") gets flagged as karma farming. Use "What's your take?" or "Similar experience?" instead.

## Recommended subreddits for personal-brand authority
Per `best-practices.md`: r/Entrepreneur, r/SmallBusiness, r/marketing, r/SaaS, r/digitalnomad, r/PersonalFinance, r/indiehackers (niche-specific). Niche subs (smaller, focused) reward specificity (numbers, steps, mistakes). Larger subs (r/marketing) lean on volume.

## Anti-hallucination
Universal rules: load `~/.claude/knowledge/tim-maines-anti-hallucination.md`.
Platform-specific additions:
- ALWAYS disclose affiliation: "I work for/own [X], here's what we learned." Mods auto-remove undisclosed affiliates in r/Entrepreneur, r/SaaS, r/marketing.
- AI-spam moderation in 2026 detects repetitive phrasing, low-effort posts, bot-like patterns. Write personally, share specific numbers/steps/mistakes.
- 9-1 rule: 9 value-adding contributions per 1 self-promo. Track this across the account, not per subreddit.
