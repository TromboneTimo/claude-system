---
name: tim-social
description: Tim Maines social media orchestrator. Routes posting, scheduling, drafting, analytics, and content ideation across LinkedIn, YouTube, TikTok, Instagram, Facebook via Zernio. Also extends /blog for transcript-to-blog. Triggers on "/tim-social", "tim social", "post on linkedin as tim", "schedule a tiktok for tim", "draft an instagram", "log my post", "what's working on tim maines", "tim ideate", or any explicit reference to the Tim Maines channel + a posting/analytics action.
user_invocable: true
---

# Tim Maines social orchestrator

## Load order (Priority 1, every run)
1. `references/voice-spec.md` (THE LAW for Tim Maines voice, evolved from `voice-methodology-research.md`). If voice-spec is missing, fall back to discovery interview from voice-methodology Phase A before generating.
2. `references/voice-methodology-research.md` (NotebookLM-synthesized cold-start + iteration framework with cited sources).
3. **Platform best-practices** for whichever platform is being targeted: `tim-maines/<platform>/best-practices.md` (deep Perplexity research, 2026-04-28). Mandatory load when generating for that platform.
4. `references/zernio-cheatsheet.md` (env loading, auth, IDs, posting flow).
5. `~/.claude/CLAUDE.md` rules (no em dashes, no guru language, no hedging).
6. `/Users/air/Desktop/Timo LLC/creator-conservatory/CLAUDE.md` (this is Creator Conservatory workspace, NOT Trombone Timo; Tim Maines is its own personal-brand identity).

## Commands

| Command | What it does |
|---|---|
| `/tim-social refresh` | Run `scripts/zernio_refresh.py`. Pulls profiles + accounts. Always run after OAuth changes. |
| `/tim-social <platform> draft "<topic>"` | Generate draft via per-platform skill, push to Zernio as draft, save markdown to `tim-maines/<platform>/posts/`. |
| `/tim-social <platform> publish "<topic>"` | Same as draft but `publishNow: true`. Confirm with user FIRST. |
| `/tim-social <platform> schedule "<topic>" <ISO-time>` | Same as draft but with `scheduledFor`. |
| `/tim-social log <post-path>` | Pull latest metrics for that post via Zernio analytics endpoints, update frontmatter. |
| `/tim-social analyze [platform]` | Read all posts in database. Compute top decile per platform. Write `tim-maines/insights/what-is-working.md`. |
| `/tim-social ideate` | Read top performers + comment archives. Produce 5 next-round content ideas with quote evidence. |
| `/blog from-transcript <path>` | Phase 5: turn a video transcript + optional comment file into a blog post via existing /blog skill. |

## Routing (which sub-skill handles what)
- `linkedin` -> `tim-linkedin`
- `youtube` -> `tim-youtube`
- `tiktok` -> `tim-tiktok`
- `instagram` -> `tim-instagram`
- `facebook` -> `tim-facebook`
- `twitter` | `x` -> `tim-twitter`
- `reddit` -> `tim-reddit`
- `substack` -> `tim-substack` (manual-only: Zernio does NOT support Substack; skill produces a draft markdown saved to `tim-maines/substack/posts/` for user to paste into Substack web UI)

## Database
- Skill assets: `~/.claude/skills/tim-social/`
- Project database: `/Users/air/Desktop/Timo LLC/creator-conservatory/tim-maines/`
  - `<platform>/posts/YYYY-MM-DD-slug.md` (frontmatter from `templates/post.md`)
  - `<platform>/comments/<post-id>.md`
  - `<platform>/best-performing.md` (refreshed weekly by `/tim-social analyze`)
  - `insights/what-is-working.md`, `insights/content-ideas.md`
  - `config/zernio-{profiles,accounts}.json`

## Anti-hallucination rules
- Never fabricate post-engagement numbers. Always pull live via Zernio.
- Never use claimed credentials beyond TIMO_PROFILE.md (no Four Tops, no TED-talk-as-delivered).
- Never name specific clients in public Tim Maines posts (per `feedback_client_claims.md`).
- Never confuse Tim Maines (personal brand authority) with Trombone Timo (entertainment) or Creator Conservatory (musician coaching).

## Current connection status (2026-04-28)
Run `/tim-social refresh` to update.
- Connected via Zernio: Facebook (Tim Maines Page), LinkedIn, YouTube (timmaines), Instagram (timo.maines), TikTok (timo.maines), Twitter/X (TromboneTim0)
- Pending OAuth: Reddit (when Timo connects)
- Manual-only (Zernio doesn't support): Substack

## Failure modes
- 401 on Zernio: env var loading bug, OR token rotated. Re-extract key from `~/.zshrc` per cheatsheet.
- Connection reset: retry with backoff (refresh script handles this). If persistent, check `https://zernio.com/api/health`.
- Post returns "platform not connected": run `/tim-social refresh` and re-check `config/zernio-accounts.json`.
