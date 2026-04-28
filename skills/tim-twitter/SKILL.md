---
name: tim-twitter
description: Tim Maines Twitter/X agent. Drafts/schedules/publishes tweets and threads to Tim's X via Zernio. Triggered by /tim-social twitter ... or /tim-social x ... Do not invoke directly without orchestrator unless user explicitly says "tim twitter" or "tim x".
user_invocable: false
---

# Tim Maines Twitter/X agent

## Identity gate
- Posts to **Tim Maines** X account (account id `69f02d7f985e734bf3c76f9e`, username `TromboneTim0`).
- **CAVEAT**: The connected handle `TromboneTim0` is the entertainment-side handle, not a Tim-Maines-authority handle. Two paths:
  1. If Timo wants `TromboneTim0` to BECOME the Tim Maines authority handle, post in personal-brand voice here.
  2. If Timo wants a separate `@timmaines` handle for authority, this skill should refuse and prompt to OAuth a new handle in Zernio.
  Confirm with Timo on first run before posting anything.

## Inputs
- `mode`: `draft` | `publish` | `schedule`
- `kind`: `single` | `thread`
- `content` (single) OR `tweets[]` (thread, 8-12 tweets per best-practices.md)
- `media`: optional image/video
- `scheduled_for`: ISO 8601 if mode=schedule

## Workflow
1. Load voice spec / methodology fallback. Refuse if missing.
2. Load `tim-maines/twitter/best-practices.md` (mandatory). Apply: bookmarks as top signal, threads 8-12 tweets, X Premium 2-4x reach multiplier (verify Premium status), link suppression (use in-app or text-only), SimClusters topic clustering (stay on-niche).
3. Load accounts JSON, confirm `twitter` exists. Confirm handle identity per Identity Gate above.
4. Generate hook tweet (curiosity gap / contrarian / list-promise). For threads: 8-12 tweets, hook + payload + payoff structure. Confirm before publish.
5. Call `zernio_post.py --platform twitter --account-id 69f02d7f985e734bf3c76f9e --content "<text>" --mode <mode>`. For threads, the tweet array passes through Zernio's threadItems.
6. Log to `tim-maines/twitter/posts/YYYY-MM-DD-<slug>.md`.

## Twitter/X request body shape
```json
{
  "content": "<hook tweet (280 chars max, or 25000 if X Premium long-form)>",
  "platforms": [{"platform": "twitter", "accountId": "69f02d7f985e734bf3c76f9e"}],
  "publishNow": true,                 // for publish
  "scheduledFor": "<iso>",            // for schedule
  "twitterSettings": {
    "amplifyVideo": false,            // true requires X Premium + allowlisting; up to 10min video
    "threadItems": []                 // for threads, array of follow-up tweets
  }
}
```

## Limits and caveats
- Free tier: 280 chars per tweet. X Premium: 25000 chars. Verify Premium status before generating long-form.
- External links cut reach 50-90%. Drop links in a reply tweet AFTER the main thread, OR text-only.
- First-hour engagement determines 50%+ of total reach; encourage early replies.
- "Not interested" signals from off-topic posts confuse SimClusters and tank distribution. Stay on niche.
- Bad ratios (high follower-to-following imbalance, dormant first 30 mins) suppress. Don't post multiples rapidly.

## Anti-hallucination
Universal rules: load `~/.claude/knowledge/tim-maines-anti-hallucination.md`.
Platform-specific additions:
- No rage bait or muted-keyword games. Grok ranking specifically penalizes.
- Drop external links in a REPLY tweet, not the main thread (50-90% reach cut on links).
- Don't post multiples rapidly. Velocity loss + first-30-min-dormant = SimClusters tank.
