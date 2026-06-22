# Tim Maines anti-hallucination rules (universal)

Every skill in the `tim-*` family loads this. Rules apply to all 8 platforms (LinkedIn, YouTube, TikTok, Instagram, Facebook, Twitter/X, Reddit, Substack). Platform-specific additions live in each skill's own SKILL.md.

## Universal bans

1. **No fabricated engagement numbers.** Likes, views, impressions, opens, comments, follower counts. Pull live via Zernio API or leave as `null` in frontmatter. Never invent.
2. **No fake credentials beyond TIMO_PROFILE.md.** TED talk was INVITED, not delivered. Four Tops was NOT performed with. Anything not in TIMO_PROFILE is off-limits unless Timo confirms in this turn.
3. **No naming specific clients in public Tim Maines posts** (per `memory/feedback_client_claims.md`). Describe situationally ("Australian trumpet coach", "brand I work with") not by name.
4. **No em dashes** (per `~/.claude/CLAUDE.md` and the block-em-dashes hook). Replace with periods, commas, slashes, or colons.
5. **No guru language**: leverage, synergy, bandwidth, unlock, supercharge, 10x, game-changing, paradigm shift, ecosystem.
6. **No hedging**: "might help", "could potentially", "may be able to", "in many cases". Tim is direct. State the claim or kill it.
7. **No engagement bait** that triggers algorithm penalties: "Like if you agree", "Tag a friend", "Comment YES below", "Share if this hit home". These get throttled on Instagram (Mosseri 2024+), Facebook (engagement-bait penalty), Twitter (rage-bait suppression), and LinkedIn (360Brew spam pattern flag).

## Identity rules

- **Tim Maines** = personal brand authority play. Founders, creators, musicians wanting positioning + business takes.
- **Trombone Timo** = entertainment channel. 1M+ followers. Fun, meme-energy, music nerd. NOT this skill family.
- **Creator Conservatory** = musician coaching. $500/mo. Direct, anti-guru, proof-heavy. NOT this skill family.
- Cross-contamination is the #1 failure mode. Identity gate at the top of every platform skill enforces this.

## Verification (before any behavioral claim about a real person)

Per `memory/feedback_fabricated_behavior.md`: never write "you already X" / "since you Y" / "given your Z" about a real person without evidence. Grep draft for `already|existing|since you|your weekly|your monthly|like you do|given your`. For each hit: verify or DELETE/REWRITE/ASK.

## Numerical claims

Per `memory/feedback_fabricated_content_numbers.md`: every number in a Tim Maines post traces to TIMO_PROFILE.md, the Zernio analytics endpoint, or is explicitly hypothetical. No "I helped 100 creators" unless 100 is in the database.

## Quote attribution

Per `memory/feedback_verify_quotes_via_transcript.md`: never ship a verbatim quote attributed to a real person without verifying the transcript. Perplexity fabricates URLs and conflates speakers.

## Chat review before any Zernio push (universal, all 8 platforms)

**NEVER call `zernio_post.py` or hit any Zernio post endpoint without first showing the full draft in chat and getting Timo's explicit go-ahead.** This applies to ALL modes: `draft`, `schedule`, `publish`. There is no mode where a Zernio call is allowed without prior chat approval.

Wrong: "I'll push these as Zernio drafts so you can review them in the dashboard." Reviewing happens HERE first, then Zernio second.

Right flow per turn:
1. Generate draft inline in the chat (with frontmatter logged to `tim-maines/<platform>/posts/`).
2. Wait for Timo's edit pass or "go" / "push it" / "ship it".
3. Then call Zernio with the approved draft.

If a per-skill SKILL.md says "draft and schedule skip confirm" or anything similar, IGNORE it. The canonical rule in this file overrides. Origin: 2026-04-28 Timo correction after the $1k-website-Claude-Code drafts.

## Required media attachments per platform

Text posts on **LinkedIn** and **Facebook** must ship with media. Text-only posts get crushed in 2026:

- **LinkedIn**: text post needs an image attached, or (preferred) a PDF document carousel. Document/PDF carousels are the highest-engagement format on LinkedIn 2026 (~6.6% engagement vs ~2% for text-only). If a video is the media, fine. NEVER ship LinkedIn text-only.
- **Facebook**: text post needs an image attached, or pair with a native video / Reel (Reels get 5-10x feed reach). NEVER ship Facebook text-only.
- **Twitter/X**: image or video lifts dwell but is not strictly required for threads. Threads >> single posts.
- **Instagram, TikTok, YouTube, Reddit, Substack**: media requirements are platform-native (covered in each SKILL.md).

When generating a LinkedIn or FB draft, the chat reply must propose a specific image/carousel/video plan alongside the copy, not after-the-fact. If no media exists, propose generating one (Gemini, Pixabay, screenshot from source video, or PDF carousel built from the post's bullet structure).

**ASK before uploading. Timo provides the files.** For any LinkedIn or Facebook push, ASK Timo for the actual asset BEFORE calling Zernio. Do NOT auto-generate. Do NOT offer generation as the default option. Wait for him to drop a file path or URL.

Per Timo 2026-04-28 spec:
- **LinkedIn**: image, PDF, or hero image. Timo provides.
- **Facebook**: single image. Timo provides.
- **X / Twitter**: NO picture. Do not attach media unless Timo explicitly provides one and says to attach it.

The chat sequence is: (1) draft copy inline, (2) ASK Timo for the file (LinkedIn / FB only), (3) wait for file path, (4) push to Zernio with attached asset. Only if Timo says "I don't have one" should you offer to generate. Origin: 2026-04-28 Timo corrections.
