---
name: project_email_swipe_file_and_beat_cloning
description: "The email swipe-file database (Dimitri/Ed Lawrence/Inbox Newsletter) + the beat-cloning drafting law now wired into pb-email. How Harrison's emails must be written."
metadata: 
  node_type: memory
  type: project
  originSessionId: 2e4ca898-2a60-4653-91b1-c90554d4165b
---

Built 2026-05-31. Harrison's daily emails were soft (teach-and-stop, no CTA, no proof). Timo had me scrape 3 high-performing lists from trombonetimo@gmail.com and build a swipe-file DB + a drafting method, then wire it into pb-email.

**The database:** `voc/emails/swipe-file/` (registered in voc/config.yaml + STRUCTURE.md).
- `raw/<creator>/` = 275 verbatim emails: dimitri-fantini-drums (143, the closest analog, 3.8/wk), film-booth / Ed Lawrence (39, 1.6/wk), inbox-newsletter / Max (93, 4.3/wk).
- `analysis/<creator>.md` = per-creator teardown. `STRATEGY.md` = synthesis + template. `index.json` = measured cadence.

**The drafting law** (canonical: `~/.claude/skills/pb-email/references/email-beat-cloning-method.md`, enforced in pb-email + pb-email-write). Every email MUST:
1. **Clone a real swipe-file template skeleton** (extract a stored email's beat map, write Harrison onto identical beats). Do NOT freelance or blend voices. Blending 3 sources = "soft cock energy" (Timo's words). Copy ONE hard.
2. **Source the story from Harrison's OWN content** (`voc/masterclass/raw/transcript.md` + `voc/youtube/raw/<vid>/transcript.md`), in his words. NEVER invent a story.
3. **Carry one verified proof point** (specific number or real named testimonial result). His #1 email ever is "I could almost cry" (pure proof). No proof = reject.

**The lessons Timo drilled (do not repeat these mistakes):**
- **Stop defaulting to student stories.** Only 1 of Harrison's top 8 sent emails is a student story; only 15/143 of Dimitri's. Student-story is capped ~1 in 8. Rotate 7 archetypes (myth-bust, age-lie, delay-cost, not-talent, curiosity-secret, confession, result-video).
- **USE EVERYTHING.** Mine his masterclass + 6 YouTube transcripts + testimonials + sales calls + his own `voc/emails/performance/ranking.json`, not just sales calls + testimonials.
- **Cadence is NOT the problem.** [[feedback_*]] Research (cached) + Ed's 1.6/wk winning prove content/routing is the lever, not frequency. Keep daily; make every email end on ONE ask. Soft-sell daily, hard-sell launch only.
- **Length by job:** 120-220w daily teaching send (Dimitri median 134), 600-900w launch/replay only.
- **Randomize 5 dims/run:** archetype, clone_template, story_source, cta_rung, length_band. Logged to `voc/email_voices_used_log.jsonl`.

His proven top-8 subjects (mimic these patterns): "I could almost cry", "Use more air and other useless advice", "What another year of this costs you", "it's not talent", "I'm not 24 anymore", "the I'm too old lie". His real system names: Vertical Alignment, gravity breath, embouchure swing, dynamic repetition, upstream/downstream, studied with James Morrison.

Phase 2 still open: `email_swipefiles` Supabase table + browse tab in dashboard/emails.html (Timo wanted "both"). Older ~30 Dimitri emails (pre-Sept 2025) not scraped; 143 recent is plenty.
