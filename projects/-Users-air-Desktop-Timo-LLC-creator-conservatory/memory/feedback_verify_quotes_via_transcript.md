---
name: Verify Quotes Against Actual Transcripts, Not Perplexity Output
description: NEVER trust Perplexity's verbatim quote output. ALWAYS verify against the original source via yt-dlp transcript, WebFetch, or actual page read. Perplexity confabulates both quote text AND source URLs.
type: feedback
originSessionId: e765d7f8-f494-4a6b-8d42-9b0e63cc684b
---
NEVER ship a quote attributed to a real person based on Perplexity's output alone. Perplexity fabricates:
- Quote wording (paraphrases presented as verbatim)
- Source URLs (invented blog posts that 404)
- Attribution (conflates "someone discussing Hormozi" with "Hormozi himself")

**The exact failure pattern (2026-04-13):**
Timo asked for a verbatim quote about testing organic before paid. First attempt: I used training-data recall (failed — Ogilvy/Wanamaker were tangential). Second attempt: I asked Perplexity, got 12 candidate quotes with sources. Verification:
- Seth Godin blog URL: 404 (fabricated by Perplexity)
- Marketing Week URL: 403 paywall (unverifiable)
- Alex Hormozi podcast URL: video EXISTED but was on "6 Figure Creative" channel, NOT Hormozi's channel. Perplexity conflated a podcast DISCUSSING Hormozi's frameworks with Hormozi speaking directly.

Only after downloading the actual YouTube transcript via `yt-dlp` did I find a REAL Alex Hormozi quote with verified exact wording.

**The pipeline that actually works (use this every time for quote verification):**

1. **Perplexity pass 1** — get candidates with source URLs. Don't trust these.
2. **Source URL check** — `curl https://www.youtube.com/oembed?url=<URL>&format=json` verifies video exists AND returns the real channel name. Compare channel to the claimed speaker.
3. **Transcript download** — `~/Library/Python/3.10/bin/yt-dlp --write-auto-sub --skip-download --sub-format "vtt" --sub-lang en "<URL>" -o "video.%(ext)s"` pulls the YouTube auto-transcript.
4. **Transcript clean** — dedupe and strip VTT timestamps: `awk '/^[0-9]+:[0-9]+:[0-9]+\.[0-9]+/ {next} /^$/ {next} /WEBVTT/ {next} /<[0-9]/ {next} /-->/ {next} {print}' video.en.vtt | awk '!seen[$0]++'`
5. **Find the passage** — grep for the claimed quote keywords in the cleaned transcript.
6. **Extract VERBATIM** — use only the exact words from the transcript. If the transcript says "stitch on 5 seconds of a CTA" then the quote must say "stitch on 5 seconds of a CTA" — not "add a 5-second CTA" or any paraphrase.

**Non-YouTube sources:**
- Books: require page number + edition. Cannot verify without the book. Skip unless user owns it.
- Tweets/X posts: fetching requires auth. Use nitter.net mirror or skip.
- Podcasts without video: Apple Podcasts/Spotify transcripts often locked. Prefer YouTube mirror if available.
- Blog posts: WebFetch the URL. 404 = fabricated.

**Decision rule when verification fails:**
- 2 failed source verifications in a row → STOP using that quote candidate. Do not salvage with paraphrase + attribution.
- Zero verified quotes after 3 attempts → cut the quote slide entirely. Write the principle in Timo's own voice (no attribution). Per `feedback_serve_thesis_not_slot.md`.

**Why this matters:** Per `feedback_fabricated_behavior.md` and `feedback_master_lessons.md` — attributing invented verbatim to a real person is a lie, even when the person has said similar things. The fact that Hormozi has TALKED about this principle many times does not give me license to invent his exact words. Only transcripts give license to exact words.

**How to apply:**
- Before shipping ANY quote attributed to a real person: run the 6-step verification pipeline above.
- If Perplexity gives a URL, verify it returns 200 AND the content matches before using the quote.
- If a user asks for a quote 2+ times and each attempt fails: switch to transcript-based verification (yt-dlp) on the second attempt, not the fifth.
