---
name: YouTube URL From Timo Means Go Straight To yt-dlp
description: CRITICAL. When Timo provides a YouTube URL for ANY reason (not just quote verification), the FIRST tool is yt-dlp for the transcript. Not WebFetch. Not WebSearch. Not asking clarifying questions. yt-dlp first, always.
type: feedback
originSessionId: 2026-04-14T23:49:08Z
---
# YouTube URL From Timo = yt-dlp Immediately

**Rule:** When Timo gives me a YouTube URL, the FIRST tool I reach for is `yt-dlp` to pull the auto-transcript. Not WebFetch (YouTube renders nothing useful to scrapers). Not WebSearch (adds latency and drift). Not clarifying questions. Download the transcript first, read it, then answer. This applies regardless of context: quote verification, product research, competitive intel, tutorial watching, news. YouTube URL means transcript via yt-dlp as step one.

**Why:** On 2026-04-14, Timo sent a YouTube URL asking if I had a new feature (Claude Routines). I went to WebFetch first (got YouTube's empty footer HTML), then tried WebSearch, THEN went to yt-dlp after he snapped at me. I had `feedback_verify_quotes_via_transcript.md` in memory but scoped the rule too narrowly ("for quote verification") and missed that the same pipeline applies to any YouTube URL. The user's exact words: "motherfucker get the transcript you dumbass, i gave you the skill why did you do that right away?"

**How to apply (zero-thought pipeline):**

1. **See a YouTube URL in Timo's message.** Immediate action.
2. **Run yt-dlp in one command:**
   ```bash
   yt-dlp --skip-download --write-auto-sub --sub-lang en --sub-format vtt \
          --output "/tmp/video.%(ext)s" "<URL>" 2>&1 | tail -5
   ```
3. **Clean + search:**
   ```bash
   sed 's/<[^>]*>//g' /tmp/video.en.vtt | awk '!seen[$0]++' | \
     grep -v "^$\|-->" | head -200
   ```
4. **THEN answer the user's question.**

**Do NOT:**
- Start with WebFetch on a YouTube URL (YouTube doesn't render descriptions/transcripts to scrapers)
- Start with WebSearch to see "what the video is about" (yt-dlp gives you the actual content)
- Ask clarifying questions before pulling the transcript ("what do you want to know about it?")
- Assume the rule only applies to quote verification (it applies to ANY YouTube URL)

**Where this applies:**
- Any Timo message containing `youtube.com/watch` or `youtu.be/`
- Any request to "check this video" / "see what he says about X" / "confirm the feature in this video"
- Any YouTube-sourced research request
- Any time Timo asks what's in a video

**The deeper failure pattern this prevents:**
Scoping a rule too narrowly to its original triggering context. The yt-dlp rule was written for quote verification (2026-04-13 Hormozi incident) and I applied it only there. Same disease as: treating the agent's named scope as the work scope (audit_scope_must_match_usage.md). When a rule has a workflow, the workflow is general; the incident that produced it is specific. Apply the workflow, do not limit to the original incident.

**Related memories:**
- feedback_verify_quotes_via_transcript.md (parent rule, quote-verification specific)
- feedback_audit_scope_must_match_usage.md (same pattern: scoping too narrow)
- feedback_verify_before_done.md (would have caught "I got the info" when I hadn't)
- feedback_easy_path_default.md (yt-dlp is the easy path, go straight there)

**Meta:**
This rule was written BECAUSE I violated the parent rule's spirit while technically complying with its letter. Generalized scope: "for ANY YouTube URL, yt-dlp first." Not "for YouTube quotes, yt-dlp first."
