---
name: subjects-speak-to-reader
description: "Email subject lines must address the reader directly. Never name a third-party student (Tom, Karen, Joe, Phil, Heather, Michelle, Toby, etc) in a subject line."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d0c10100-009e-4416-b9c9-ee766cc9fe29
---

Email subject lines must address the READER directly. Never name a third-party student in a subject line. Use "you / your / I'm" framing, not "Karen this, Tom that."

**Why:** Caught 2026-05-17 when I drafted subject rewrites that named specific students (Tom, Karen, Joe, Phil, Heather, Michelle, Toby) in the subject. Timo's correction verbatim: "I think you need to lean off of citing specific names and talk directly to the reader. I needed to go through all the titles again and redo them all because you keep saying, 'Karen, this, this.' You need to make it about the viewer themselves. Don't try to name a name."

The mechanism: a subject that names another person reads as a spectator pitch ("come watch what happened to Karen"). A subject that uses "you" reads as a stakes pitch ("this is about you"). Spectator pitches get opened out of curiosity. Stakes pitches get opened AND clicked. Per the data-driven patterns file, click-through is what matters, not vanity opens.

This also matches Harrison's voice protocol Section 1.5 underlying principle: "Less like, you're more like, kind of, indirectly calling out their playing." Naming Karen calls out Karen. Indirect call-out of the reader requires speaking TO the reader, not ABOUT a student.

**How to apply:**
- Subject lines: NO third-party first names. Use "you / your / I'm" (reader-voice or reader's internal monologue).
- The Harrison-approved patterns (Section 1.5) all use second-person or first-person, never a third party. Honor that.
- Bodies CAN name students because the body has space to set up the testimonial. The subject does not have that space.
- If a draft's source is a specific student (Tom's quote, Karen's session), translate the wound into a "you" subject. Save the name for the first line of the body.
- Preheaders: also default to direct-to-reader. Naming the student in the preheader is a softer offense than the subject, but still weaker than addressing the reader.

**Examples of the fix:**
- Bad: "Did Tom waste 40 years?" -> Good: "Did 40 years of practice betray you?"
- Bad: "Heather: 5 years gone in 3 days" -> Good: "5 years of struggle. Gone in 3 days."
- Bad: "Did Indiana fail Karen?" -> Good: "Did your teachers train you wrong?"
- Bad: "Phil thought it was over" -> Good: "This is why you blame your age"
- Bad: "Did one teacher cost Joe 40 years?" -> Good: "Did one teacher cost you 40 years?"

Auditor enforcement: agent 9 should grep each subject + each alt against a regex for known student names from `voc/testimonials/raw/` and `voc/sales-calls/raw/`. Any hit auto-rejects. Names are fine in the body, never in the subject.
