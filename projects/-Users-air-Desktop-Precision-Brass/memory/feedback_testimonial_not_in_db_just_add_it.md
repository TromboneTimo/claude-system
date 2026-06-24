---
name: feedback-testimonial-not-in-db-just-add-it
description: "When given a testimonial not yet in voc/testimonials/raw/, just add it and move on. Don't make it complicated."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 17134246-d29e-4c59-8135-eb0885ece65e
---

When Timo hands me a testimonial (usually a YouTube URL) that isn't in the database, the move is simple: check the RIGHT place (`voc/testimonials/raw/`), and if it's not there, pull the transcript, write the file in the existing naming/frontmatter format, say one line ("Not in the database, adding it"), and keep going.

**Why:** 2026-06-24, on the Martin testimonial email, I repeatedly flagged "Martin isn't in the corpus" as a blocker-ish caveat and offered it as a separate follow-up instead of just doing it. Timo: "just don't make this so complicated." Adding a testimonial to the DB is a 30-second mechanical task I'm fully equipped to do, not a decision to escalate.

**How to apply:**
- Right place = `voc/testimonials/raw/`. Filename: `YYYY-MM-DD_youtube_<name>_<title-slug>.md`, date = video upload_date (`yt-dlp --print "%(upload_date)s"`).
- Match the existing frontmatter block (source_url, video_id, uploader, speaker_name_inferred, transcript_confidence, etc.) + transcript + key quotes + themes.
- Don't pile on caveats, don't offer it as optional future work, don't ask permission for the obvious. Add it, say one line, continue.
- Same spirit for the whole task: when something is in-scope and I can just do it, do it. See [[canon_working_process.md]].
