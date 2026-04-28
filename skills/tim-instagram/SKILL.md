---
name: tim-instagram
description: Tim Maines Instagram agent. Drafts/schedules/publishes Reels, carousels, single images to Tim's IG via Zernio. Triggered by /tim-social instagram ... Do not invoke directly without orchestrator unless user explicitly says "tim instagram".
user_invocable: false
---

# Tim Maines Instagram agent

## Identity gate
- Posts to **Tim Maines** Instagram (account id `69f02da5985e734bf3c77032`, username `timo.maines`).
- Account must be Business or Creator (verify via Zernio dashboard if posting fails). Personal accounts cannot post via API.

## Inputs
- `mode`: `draft` | `publish` | `schedule`
- `kind`: `reel` | `carousel` | `single-image` | `story`
- `media`: video for reel, 2-10 images for carousel, single image, or story media
- `caption`, `cover_frame` (reel), `aspect_ratio`
- `scheduled_for`: ISO 8601 if mode=schedule

## Workflow
1. Load voice spec / methodology fallback. Refuse if missing.
2. Load `tim-maines/instagram/best-practices.md` (mandatory). Apply: original-content boost, swipe-back signal for carousels (7-10 slides), 3-5 niche hashtags max, hook in first 1-3 seconds for Reels.
3. Load accounts JSON, confirm `instagram` exists.
4. Generate caption (hook before "see more" cutoff at ~125 chars, no engagement bait). For carousel, generate cover slide + content slides. Confirm before publish.
5. Call `zernio_post.py --platform instagram --account-id 69f02da5985e734bf3c77032 --content "<caption>" --mode <mode> --media-url <url> --media-type <image|video>`.
6. Log to `tim-maines/instagram/posts/YYYY-MM-DD-<slug>.md`.

## Instagram request body shape
```json
{
  "content": "<caption with hook before 125 chars>",
  "platforms": [{"platform": "instagram", "accountId": "69f02da5985e734bf3c77032"}],
  "publishNow": true,                    // for publish
  "scheduledFor": "<iso>",               // for schedule (Zernio internal scheduling)
  "mediaItems": [{"type": "video|image", "url": "..."}],
  "instagramSettings": {
    "mediaType": "REELS | CAROUSEL_ALBUM | IMAGE | STORY",
    "coverUrl": "<reel cover frame>",     // optional
    "shareToFeed": true                   // for reels
  }
}
```

## Limits and caveats
- IG drafts via Zernio are INTERNAL Zernio drafts (not native IG drafts). To "post manually from mobile" Timo uses the Zernio mobile app to release the draft.
- Hashtags have been explicitly de-emphasized by Mosseri 2024-2025; use 3-5 niche, prioritize keyword-stuffed alt text and location tags instead.
- Carousels: 7-10 slides, square (1:1) or 4:5; swipe-back signal counts double in feed ranking.
- Reels: vertical 9:16, hook in 1-3 seconds, original audio preferred over trending (per Mosseri 2025 original-content boost).
- Watermarks from other platforms (TikTok logo) suppress reach.

## Anti-hallucination
Universal rules: load `~/.claude/knowledge/tim-maines-anti-hallucination.md`.
Platform-specific additions:
- No watermarks from other platforms (TikTok logo) on Reels. Original-content boost penalizes detected reposts per Mosseri 2025.
- DM-share is the new gold signal. Engineer the post for "would I send this to a friend?" not "would I like this?"
- Carousel cover slide: bold visuals, minimal text. Over-text covers tank swipe-through.
