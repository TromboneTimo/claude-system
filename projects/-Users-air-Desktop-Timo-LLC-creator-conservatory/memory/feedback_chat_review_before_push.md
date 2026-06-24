---
name: Chat Review Before Any Zernio Push, Plus Ask For LinkedIn/FB Media
description: For all 8 tim-* platform skills, NEVER call zernio_post.py or hit any Zernio endpoint without first showing the full draft in chat and getting Timo's explicit go-ahead. For LinkedIn and Facebook specifically, ASK Timo for the image or PDF carousel asset BEFORE the push.
type: feedback
originSessionId: 5da82800-5bbe-480d-b683-65a7fcba012d
---
For all 8 tim-* platform skills (linkedin, facebook, twitter, instagram, tiktok, youtube, reddit, substack), NEVER call `zernio_post.py` or hit any Zernio post endpoint without first showing the full draft in chat and getting Timo's explicit go-ahead.

There is NO mode where a Zernio push is allowed without prior chat approval. Not `draft`, not `schedule`, not `publish`. "Pushing as a Zernio draft so you can review in the dashboard" is wrong. Review happens in chat first, Zernio second.

Per-platform media spec (Timo 2026-04-28 correction):
- **LinkedIn**: image, PDF, or hero image. Timo PROVIDES the file. Do not auto-generate. Do not offer generation by default.
- **Facebook**: single image. Timo PROVIDES the file. Do not auto-generate.
- **X / Twitter**: NO picture. Do not attach media unless Timo explicitly drops a file and says to attach.

ASK FIRST. Wait for Timo to drop the file path or URL. Only ask about generation if he says he has nothing. The chat sequence is:
1. Generate draft copy inline in chat with frontmatter logged to `tim-maines/<platform>/posts/`.
2. Propose specific media options (e.g., "PDF carousel: 8 slides covering hook + 5 steps + caveat + closer" or "image: Gemini hero of Claude Code editor with $1,000 crossed out").
3. ASK Timo: "What asset do you want attached? Do you have a file path, or want me to generate one?"
4. Wait for Timo to either provide a file path/URL or confirm generation.
5. ONLY THEN call Zernio with the confirmed asset attached via --media-url.

**Why:** 2026-04-28 Timo correction after the $1k-website-Claude-Code drafts. Two distinct corrections in the same turn:
1. "in general i want to review the post here before you push straight to zernio"
2. "you need to ask me for a picture or pdf before uploading to fb or linkedin"

The LinkedIn/FB SKILL.md files had explicit "draft and schedule skip confirm" language that contradicted his actual preference. He also flagged that text-only posts on those two platforms are unacceptable in 2026, and that the Claude should ask for the asset rather than just propose a plan.

**How to apply:**
- Triggers on any tim-* platform skill invocation that produces post content.
- Block any `zernio_post.py` call until Timo confirms in chat.
- For LinkedIn/FB drafts, the chat reply MUST: (a) include copy, (b) propose 2-3 specific media options, (c) END with an explicit ASK for the asset.
- If Timo does not respond with an asset by the next turn, do NOT proceed to push. Re-ASK.
- Canonical: `~/.claude/knowledge/tim-maines-anti-hallucination.md` (Chat review section + Required media section + ASK before uploading paragraph).
- Per-skill SKILL.md updated 2026-04-28: `tim-linkedin/SKILL.md` step 5 + 5a + 6, `tim-facebook/SKILL.md` step 4 + 4a + 5. Both now require chat approval AND explicit asset request before any Zernio call regardless of mode.
