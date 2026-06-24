---
name: canon-email-writing
description: "ALL email DRAFTING rules: voice, structure, rhythm, subjects, names, bans. Consolidated 2026-06-12 from 17 files."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

# Canon: Email Writing (Precision Brass / Harrisson Ball)

Every rule below survived a real failure. Origin date + incident + enforcement noted per rule. Read this BEFORE drafting any Precision Brass email (pb-email, pb-email-write, or ad-hoc in chat).

## Voice & load order

Why the 3 FINAL emails in `output/` are in the load order: they are the closest thing to verified production-quality Harrisson voice (restored 2026-06-12 after reviewer pass).

**Load order is non-negotiable** (origin 2026-04, `feedback_email_voice_load_order`). Before drafting ANY email for Harrisson Ball / Precision Brass, load these files in this exact order, then write:
1. `voc/emails/extracts/harrison-email-voice.md` (302-line voice catalog, the source of truth, built 2026-04-21 from 7 known-Harrison emails)
2. `output/email-PP01-dental-trigger-FINAL.txt`
3. `output/email-PP03-failed-lessons-FINAL.txt`
4. `output/email-PP05-isolation-FINAL.txt`
5. `voc/emails/raw/sequences/2026-04-21_email-sequence_webinar-optin-to-strategy-session.md` (emails 1-7 ONLY, NEVER 8-12)

**Hard exclusions (Paul-template leakage):** Emails 8-12 of the webinar sequence are signed by Paul The Trombonist and target music educators; per voice catalog Section 10 they are template leakage. Never load them. Banned phrasings: "Mastermind" terminology (Email 3 leak), "music educators", "profitable, flexible online teaching business". Off-voice email > no email. Enforced by `~/.claude/skills/pb-email/references/email-voice-protocol.md`; drafting agents receive these files as load-once context; the auditor rejects any draft lacking the tagline or containing forbidden phrases. The same load order applies OUTSIDE the skill too (one-off "write a quick email to the list about X" requests).

**The recurring tagline must appear verbatim in every draft.** No paraphrase, no reorder, no "improve":
> "We help trumpet players unlock their full potential by aligning sound, body, and technique into one effortless system."

**Voice history (SUPERSEDED rule, lesson stands)** (origin 2026-04-07, superseded 2026-06-10, `feedback_harrison_voice`): voice-spec.md was built from Ed Lawrence's style adapted for Harrison. Harrison reviewed the AI emails and said they were "total shit." His real voice (12-email welcome sequence): longer emails (400-800 words), "we/our", ALL CAPS emphasis, exclamations, emoji, hype ("massive success"), urgency/scarcity, selling in the body not just the P.S. The fix at the time was loading harrison-real-voice.md over voice-spec.md. STATUS 2026-06-10: harrison-real-voice.md and voice-spec.md are DELETED with the deprecated legacy /email skill (stub points to /pb-email). Do not go looking for them. Living voice canon = `voc/emails/extracts/harrison-email-voice.md` + `~/.claude/skills/pb-email-write/references/reader-facing-playbook.md` (+ email-doctrine.md). The lesson stands: never write Harrison in a borrowed Ed Lawrence voice; a client's real voice beats any borrowed template; templates leak (same lesson as the Paul-template ban).

**Spine, not tone** (origin 2026-06-01, `feedback_email_voice_spine_not_tone`). After weeks of tuning TONE (friendly vs naggy vs whimsical), drafts still felt "soft-cocked." Diagnosis (backed by cached research `~/.claude/research/perplexity/raw/2026-05-31_daily-email-vs-weekly-email...`): the problem was never tone, it was SPINE. Value-only/story-only drafts with a limp CTA ("come hang out and I'll walk you through it") train readers to consume, not buy, give no trackable buying pathway, and cause invisible engagement churn. Friendly delivery and selling are NOT a trade-off; every master named in the research (Ben Settle, Ian Stanley, Andre Chaperon, Justin Goff) plus Ed Lawrence and Dimitri do BOTH: entertaining story-driven delivery on top, one clear commercial pivot underneath. The locked spec for every broadcast/daily draft:
1. Cold open straight into a scene. No windup ("over the last 10 years..."). Open mid-event, like Dimitri or the Dave Richards email: "A couple years back I played some gigs with Dave Richards." (Real verified facts only, see Names & stories.)
2. One story, one idea, one emotional angle. Not three lessons. Over-talking IS the bug. Match the swipe-source economy, not just its skeleton (depth still holds for teaching, but depth does not mean word-count bloat).
3. The story is the VEHICLE to the offer, not decoration. Tight pivot, the way Dimitri pivots "he joined, I spotted it in 10 seconds" straight into "the camp is built for that."
4. Every email has ONE explicit, named ask. Soft-sell is fine. NO-sell is banned. Replace limp "come hang out" with a specific reason to act NOW. Soft-sell still bridges to a commercial next step.
5. Rotate the ask across the batch (Timo's call 2026-06-01): some free masterclass (training-room URL), some reply-to-me (engagement + warm-lead surfacing, very Ed Lawrence), some book-a-call / application. Pick the ask the story naturally sets up; always exactly ONE ask per email.
6. Whimsy/personality lives in delivery + P.S.; spine lives in structure. Keep Harrisson likable (self-deprecating, real stories, contractions, direct 2nd-person address) AND make every send move the reader toward buying.
Meta-lesson: when Timo says "soft," soft = no spine = add a real ask, do NOT add more friendliness. And run `/research check` before drafting a voice spec; the answer was already cached from the day before.

**Friend-to-friend depth, no thin husks** (origin 2026-05-31, `feedback_email_friend_to_friend_depth`). Timo gut-checked drafts against the actual swipe-file source emails (Dimitri Fantini, Ed Lawrence/Film Booth) and was furious: thin 130-word skeletons that "borrowed the bones and threw away everything that makes the skeleton work." A beat-clone that copies structure but strips texture, teaching, and warmth is worse than not cloning at all; the source emails earn the CTA by being worth reading on their own. Timo confirmed the rewritten deep version is "hands down a better upgrade" and it is now the DEFAULT way to make every email (restored 2026-06-12 after reviewer pass). The bar for EVERY draft:
1. Teach ONE real, usable thing for free. The reader can try something tonight and feel a difference (whistle/air-speed reframe, 3-step pre-play breath, "practice less / stop at strain"). Plain steps like Ed Lawrence. The free value IS the email; the CTA is almost an afterthought.
2. Physical, specific mechanism, never vague diagnosis. Not "an embouchure issue" but "a fulcrum issue he'd been compensating for since day one." Not "use better air" but "same air, moving faster, like whistling up." Mine the named mechanisms from his masterclass + YouTube transcripts (air speed, place-breathe-play, gravity breath, 4 points of contact, vertical alignment, embouchure swing, upstream/downstream). Verify named-technique specifics against the masterclass before send.
3. Confession / vulnerability up front. Harrisson (or a real student) got it wrong first ("The advice that wrecked my range for years," "Don't make my dumb mistake," "Why I told my best student to practice less"). A friend telling you what HE screwed up, not a guru lecturing.
4. Texture in the struggle. Staccato "he tried everything" beats before the turn ("He practiced every single day. Ran through rudiments. Watched tutorials. Put in the hours."). Make the reader FEEL the years before the gut-punch.
5. Friend-to-friend warmth, not marketing voice. "Can I tell you the thing that kept me stuck longest?" "Be honest with me for a sec." Direct address, contractions, rhetorical questions. Harrisson's voice fingerprint (second person, "Now,", "right?").
6. Full length that earns attention: about 350 to 500 words. NOT 130. The husk is the bug. Match the depth of the source swipe email, not just its skeleton.
7. CTA earned, not begged: the body already paid the reader, so the CTA reads as "here is where there is more," not "please click." Make the CTA a person/experience where possible ("come hang out and I'll walk you through it"), not a button. (The spine rule above refines this: the ask must still be explicit, named, and give a reason to act now.)
Three reference drafts that set the bar (2026-05-31): (a) "the advice that wrecked my range for years" (Dimitri-clone, whistle/air-speed teach); (b) "the 10 seconds before you play that fix everything" (Ed-$240k-clone, 3-step breath teach); (c) "why I told my best student to practice less" (Ed-88%-clone, counterintuitive confession). WARNING: these three are ALL confession + myth-bust + teach; cloning them faithfully mass-produces sameness (see Batch diversity).

**Cite a SPECIFIC named Harrison technique; vary the reframe transition** (origin 2026-06-09, `feedback_email_cite_specific_technique_and_vary_transition`). Timo on a draft: "I don't feel smart after reading it... I don't think we're really citing Harrison's voice." A "system nobody taught you" with no concrete move is empty; the reader must finish the email knowing a real thing they didn't before. Pull the actual move from Harrison's videos and NAME it: tongue-arch (say "tar" not "tee", Bobby Shew "overdrive", from YouTube dsi1bM46abE), vertical alignment, amisha, 4 points of contact, upstream/downstream, place-breathe-play, gravity breath, wedge breath, dynamic repetition. The named technique IS what makes the reader feel smart and makes the email sound like Harrison. AND vary the reframe transition (Section 9 of the playbook, locked 2026-06-09). Timo: "you keep saying 'Here's the truth nobody told you'... Can you find some other way? It's kind of ridiculous. Remember to mix it up." Across a batch, no two emails may pivot into the reframe the same way; rotate the MOVE itself (a question, a confession, a reframe of the cause, a cost line, naming the invisible problem), never reuse one stock sentence. Banned: "Here's the truth nobody told you / nobody tells you." Also reinforced: lead with EDGE, not "soft-cock energy" (Timo's words); study/mimic Ed Lawrence, Jared Judge (booklive), Dimitri; short question hook, "that was me" confession, P.S. carries the offer and lives INSIDE the body; never overstate/misattribute a testimonial (verify the actual transcript). Why: off-voice, vague, or template-y emails kill trust on a small high-signal list; specificity + variety = the difference between a spectator pitch and an email that feels written for the one person reading it. THE canonical method = `~/.claude/skills/pb-email-write/references/reader-facing-playbook.md` (9 sections), a hard precondition load in both pb-email and pb-email-write with matching failure-mode/auditor checks. Read it before drafting any email.

**Revision lessons from the Hannah rebuild** (origin 2026-06-07, the "Hannah / How many years" email, ~10 rounds of Timo corrections, `feedback_email_revision_lessons`). Each lesson cost a round: drafted before fully reading the source, softballed the transformation, overstated a testimonial past the witness's words, kept answering near-versions of Timo's exact asks. Canonical detail + the centered-video HTML + the metrics script live in `~/.claude/skills/pb-email-write/references/ed-style-and-revision-lessons.md` (loaded by pb-email-write). Highlights:
- Read the FULL transcript/testimonial before writing one word about a student. Hannah's real wins (lead playing, improv, music school) were in the part not yet read. Never draft off a truncated pull.
- Stay inside the witness's exact words. "Confidence to go after lead" is not "is gigging lead." Write "going after," not the harder fact, unless Timo confirms it from outside the video. Overstating a testimonial blocks the ship.
- The link is the source of truth for who the student is (Joinville template: the link was Mike, then Hannah). Resolve via oEmbed first. Unusual name = verify (master lessons).
- Default structure = Ed Lawrence: short question hook -> "That was me" confession -> woven reframe -> proof student with quote-alone-at-the-pivot -> centered video -> P.S. carries the offer. Timo loves the question open and the natural P.S.-as-offer.
- Answer the literal ask. "Show full emails" = full, not quotes. "Reform the question" = questions, not statements.
- Run the metrics pass EARLY (word count vs corpus, readability, I:you ratio, paragraph walls) to settle taste with data instead of five rounds of vibes.
- Calibrate harder / more emotionally specific for Harrison's list; my safe default repeatedly read as "soft" to Timo. Synthesize toward the middle, don't swing to choppy.

## Rhythm & paragraphs

(origin 2026-06-02, corrected 2026-06-02 with hard data and again 2026-06-04, `feedback_email_short_paragraphs`) Timo sent screenshots comparing my dense 6-8 sentence paragraph walls against a real Dimitri Fantini email (every paragraph 1-2 short sentences with air between them); he was angry I shipped walls and did not notice when the reference emails are visibly airy. Readability is part of the deliverable, not an afterthought; a wall kills the friend-to-friend feel and tanks read-through even when the words are good. The swipe-file teardowns call Dimitri "plain, short-paragraph, white-space-as-rhythm." Measured data from all three swipe creators' real emails (after Timo pushed back on "1-2 short sentences" as too rigid):
- Ed Lawrence / Film Booth (1057 paras): 85% ONE sentence, 14% two, 1% three. Sentence words p25=6, median=12, p75=18, MAX=57.
- Max / Inbox (3922 paras): 82% one sentence. Sentence words 6/10/15/55.
- Dimitri (1506 paras): 59% one sentence, 24% two, 10% three (the only one who clusters for staccato runs). Sentence words 5/10/15/52.

The rule for EVERY email body (pb-email, pb-email-write, ad-hoc):
1. One THOUGHT per `<p>` block, usually one sentence. Two sentences only when tightly linked; three is rare (Dimitri-style staccato only). White space comes from one-thought-per-line.
2. VARY sentence length deliberately; do NOT force everything short (that reads choppy and monotone). Mix 5-6 word punches with 15-20+ word flowing lines (Ed goes up to 57 words on one line). Median ~10-12 words. The alternation between short and long IS the rhythm.
3. A long sentence is fine on its own line. What is banned is CRAMMING multiple sentences into one block (the 6-8 sentence walls). Never break a single sentence mid-way into its own paragraph (lowercase fragments read broken).
4. Numbered-lever lines (`<strong>1. ...</strong>`), the CTA anchor, the sign-off, the P.S., and the tagline each stay their own block.
5. Model paragraphing AND short/long rhythm on the actual swipe emails in `voc/emails/swipe-file/raw/film-booth/` and `dimitri-fantini-drums/`, not on a blog post.

**BOTH extremes are banned** (2026-06-04 correction): 6-8 sentence walls AND every-sentence-on-its-own-line lists (Timo: "soft," "reads like a list," not friend-to-friend prose). The mechanical reflow pass (split every sentence) produced the list failure. The real target is Dimitri's RENDERED rhythm: group a narrative/descriptive beat into 2-3 linked sentences in ONE block; a one-liner stands alone ONLY when it lands as a punch (the turn, the gut-shot, the reveal). The 85%-single-sentence stat is measured per sentence, NOT a license to isolate every sentence; Ed/Dimitri still read as grouped because long flowing sentences fill a line and related thoughts sit together. Do NOT mechanically reflow; group by thought-unit with editorial judgment, eyeballing against `dimitri-fantini-drums/` rendered. This walls<->list ping-pong is the oscillation failure (see Batch diversity meta-rule).

**The precise char-gated paragraph rule (no more oscillation)** (2026-06-04, `feedback_email_quality_gate_pipeline`): Dimitri rhythm = mostly 1-2 sentences per paragraph, max ~170 chars per `<p>` (~2 phone lines; the visual-height wall signal), VARIED, with deliberate one-line punches ("That's backwards." / "A major third. In an afternoon."). The char count is the wall signal, not raw sentence count (sentence count alone never fails; short punches are fine).

**Tooling:** `/tmp/reflow.py` pattern (rebuild if gone) mechanically splits dense `<p>` blocks at sentence boundaries and re-patches email_proposals rows, keeping structural blocks (links, em, strong, br, P.S.) intact and lint-guarding tagline/link counts; used 2026-06-02 to fix all 19 scheduled+proposal emails (paragraph counts roughly doubled). BUT per the 2026-06-04 correction, never apply it blindly (it creates the list failure); final grouping is editorial. Self-check before declaring any email done: look at the body as the reader will see it; any paragraph more than ~3 lines tall gets split. Part of the ship-polish gate.

## Batch diversity (trope caps + angle ledger)

**Batch trope diversity** (origin 2026-06-04, `feedback_email_batch_trope_diversity`). Timo asked if my "fresh" email rewrite "sounds exactly like other emails we've drafted"; checking all 16 scheduled bodies (June 5-20) proved him right: the whole queue leaned on the same handful of moves, so every email read same-y even when individually fine. Root cause: the three bar-setting friend-to-friend reference drafts are ALL confession + myth-bust + teach; cloning them faithfully mass-produces sameness. Diversity must be a BATCH-level gate, not per-email.

Reflex tropes, each capped at ONCE per batch (counts from the 2026-06-04 queue audit):
- "use more air" myth-bust (was in 3 of 16 + the new draft)
- "it was never you / the problem was never you" reframe (5 of 16)
- "Here is something nobody in your section/world ever told you" opener (4 of 16)
- "for years..." (6+ of 16)
- "the wall you keep hitting" (4 of 16)
- "Quick rant." opener (3 of 16, two near-identical mouthpiece-drawer rants back to back)

Rotate IN the under-used winner shapes: the proven winning-emails corpus (`voc/emails/raw/winning-emails/`) does NOT use the myth/Rachel/"never you" machinery at all. It wins with concrete one-day result micro-stories ("Mike added 3 notes in one day", "my sound got 20% bigger"), a specific named drill taught start-to-finish ("the routine that built my range"), real backstage stories with a turn (Dimitri's "the grip that changed everything"), and genuine usable nuggets lists (Ed Lawrence's 100 nuggets). Pull from these, not just the confession formula.

Rotate the proof student: Brad, Mike, Kay, Heather, Yens, Rachel (masterclass transcript + testimonials). Default-to-Rachel is the known failure. Spread them; never reuse the same student twice in one batch.

Mechanical pre-draft check (run BEFORE writing, not after Timo catches it):
1. Pull the live scheduled queue bodies: `email_proposals?status=eq.scheduled&select=subject,body,hook_angle,pain_point`. Grep openers, reframes, myths, and proof students already in flight.
2. Pick an opener archetype + proof student + myth (if any) NOT already used in the batch.
3. After drafting, grep the new body against the trope list above. Any trope already at its cap in the queue = rewrite.
4. Aim for a distinct ENTRY MODE per email: result-story / named-drill / backstage-story / nuggets-list / myth-bust / confession / direct-challenge. No two adjacent emails share an entry mode.

**Angle ledger is MANDATORY before drafting** (origin 2026-06-01, `feedback_run_angle_ledger_before_drafting`). Timo, furious (rightly), caught variation after variation of the same email: the "use more air" angle alone appeared 12 times across email_proposals and was already a subject line TWICE. Drafting from memory without looking at what already shipped = grabbing the same 3-4 mechanisms forever. He called it "clown town" and demanded a SYSTEM. The fix: `scripts/email-angle-ledger.py` (Precision-Brass repo) reads every email_proposals row and prints hook_angles used, teaching MECHANISMS/THEMES by frequency (flagging `<-- OVERUSED` at >=4), the UNUSED/fresh mechanisms, and every subject line already written. Zero tokens, ~2 seconds. HARD RULE (refined by Timo 2026-06-01): REPETITION IS ALLOWED; the sin is repeating SILENTLY. Catch it, cite it, ask:
1. Before drafting ANY email (pb-email, pb-email-write, or ad-hoc in chat), RUN `python3 scripts/email-angle-ledger.py` FIRST. No exceptions. (Email sibling of the pb-script voice-diversity log.)
2. If the angle/mechanism is marked HEAVY or a subject is close to an existing one: do NOT silently avoid AND do NOT silently ship. Surface to Timo with a citation: "This repeats the [angle] from [exact prior subject(s) + status], e.g. sent 'X' and scheduled 'Y'. Want me to run it again or go fresh?" Then wait for his call. The ledger prints up to 3 example subjects per heavy theme precisely for citing the last time.
3. Fresh, never-used angles are always available if he wants new: mine `voc/youtube/raw/*/transcript.md`. As of 2026-06-01 the never-used ones were tongue arch (taro vs "ti") and four points of contact / pressure distribution (Donald Reinhardt, the "tank over an egg vs hovercraft over eggs" metaphor, bruised vibrating surface = thin sound). The transcripts hold dozens more (overdrive, embouchure swing, aperture/efficiency car metaphor, "muscle memory does not exist", Bernoulli/cone, open resonant breath, type-1/type-2 air direction).
4. Generalization: before producing any recurring deliverable, enumerate what already exists and diff against it; on overlap, cite the prior instance and ask rather than silently repeat or silently dodge. The meta: generating feels faster than checking, so the check gets skipped; but the check is 2 seconds and the repetition costs Timo's trust every time. Checking past work is step zero of the task, not optional overhead.
Auto-enforcement: UserPromptSubmit hook `~/.claude/hooks/email-angle-gate.sh` injects the live saturation report into context on any email-intent prompt.

**STOP OSCILLATING (meta, applies beyond email)** (2026-06-04): when Timo corrects something, BEFORE swinging, grep memory for the prior correction on the SAME axis and synthesize toward the middle. The walls -> one-sentence-per-line -> caught-again ping-pong happened because the paragraph-axis correction from 48h earlier was never checked. Over-correcting to the opposite extreme is its own failure mode.

## Subjects

(origin 2026-05-17, `feedback_subjects_speak_to_reader`) Subject lines must address the READER directly. Never name a third-party student (Tom, Karen, Joe, Phil, Heather, Michelle, Toby, etc.) in a subject line. Use "you / your / I'm" framing, not "Karen this, Tom that." Timo's correction verbatim: "I think you need to lean off of citing specific names and talk directly to the reader. I needed to go through all the titles again and redo them all because you keep saying, 'Karen, this, this.' You need to make it about the viewer themselves. Don't try to name a name."

Mechanism: a subject that names another person reads as a spectator pitch ("come watch what happened to Karen") and gets opened out of curiosity; a "you" subject reads as a stakes pitch ("this is about you") and gets opened AND clicked. Per the data-driven patterns file, click-through is what matters, not vanity opens. Matches Harrison's voice protocol Section 1.5 underlying principle: "Less like, you're more like, kind of, indirectly calling out their playing." Naming Karen calls out Karen; indirect call-out of the reader requires speaking TO the reader. How to apply:
- Subjects: NO third-party first names. Reader-voice or reader's internal monologue. The Harrison-approved Section 1.5 patterns all use second- or first-person, never a third party.
- Bodies CAN name students because the body has space to set up the testimonial; the subject does not. If a draft's source is a specific student (Tom's quote, Karen's session), translate the wound into a "you" subject and save the name for the first line of the body.
- Preheaders: also default to direct-to-reader. Naming the student in the preheader is a softer offense than the subject, but still weaker than addressing the reader.
- Examples of the fix: "Did Tom waste 40 years?" -> "Did 40 years of practice betray you?"; "Heather: 5 years gone in 3 days" -> "5 years of struggle. Gone in 3 days."; "Did Indiana fail Karen?" -> "Did your teachers train you wrong?"; "Phil thought it was over" -> "This is why you blame your age"; "Did one teacher cost Joe 40 years?" -> "Did one teacher cost you 40 years?"
- Auditor enforcement: agent 9 greps each subject + each alt against a regex of known student names from `voc/testimonials/raw/` and `voc/sales-calls/raw/`. Any hit auto-rejects. Names are fine in the body, never in the subject.

(See Hard bans section for Harrison's approved/banned subject PATTERNS from the 2026-05-09 call.)

## Names & stories

**No stranger names as the body's protagonist** (origin 2026-05-31, `feedback_no_stranger_names_in_email_body`). Timo, angry, after drafts kept opening "Mike had been stuck at a double G...", "Kay had been fighting since 2020...", "Heather said something...". Standing correction: STOP centering email bodies on a named third-party student the reader has never heard of. Leading with a stranger's name makes the reader a spectator watching someone else's win instead of feeling the email is about THEM; this extends the subject-line rule to the BODY. (The Dimitri swipe email is built around "Darren" only because it pitches a physical camp Darren will literally attend; Harrisson's daily broadcasts are not that. The transformation belongs to the reader, not to a named someone else.) How to apply:
- Write the body in second person: "You've been stuck at the top of the staff for years," not "Mike had been stuck."
- If a real result is needed for proof, fold it in WITHOUT making a named person the protagonist: "a student of mine," "one of the players in the program," or drop the name entirely and quote the result. Keep the proof; lose the name-as-hero framing.
- A verbatim student QUOTE can still appear as evidence (it's proof), but it is not the spine of the email and the reader is still the subject. Do not open on it.
- Harrisson's own first-person story is fine (he's the sender). The ban is on third-party stranger names as the email's main character.
- Still respects: only the ~11 students with public testimonial URLs earn a "watch" link (never-ship-placeholder-urls); P.S. student stories locked to a REAL verified student or kept deliberately vague, never fabricated.

**Zero invented story details** (origin 2026-06-01, `feedback_no_invented_story_details`). Timo caught embellishment of Harrisson's real Dave Richards / Tower of Power backstage story (his rank-9 winning email "My sound got 20% bigger from this"). The CORE was real and verified, but invented flourishes shipped: "stirring a cup of tea," "bored almost," "enough coffee," "planets lined up," "top shelf with my fingertips," a "Dave was working less not harder" spin he never said, and a P.S. about throwing a trumpet (also tonally bad). Timo: "are you sure this is based in reality or are you hallucinating facts about him?" This is the auto-transcripts-lie / ASK-don't-invent rule applied to email storytelling: even when the story IS real, dressing it with invented specifics is fabrication. The whimsical friend voice does not require invented details; Harrisson's own real phrasing is already warm and good. Rules:
1. Before writing any Harrisson personal story into an email, GREP/READ the source (winning-emails/, masterclass/raw/, youtube/raw/) and pull the actual facts and his actual phrasing.
2. Keep his real wording where it's vivid ("like it was nothing", "reaching instead of owning it", "if you don't know them, you should probably get hip"). Lift, don't paraphrase into something fancier.
3. The ONLY additions are connective tissue and warmth. NO new facts, no invented metaphors presented as what happened, no invented quotes, no invented motivations ("Dave was working less").
4. If a story beat would make the email better but isn't in the source: leave it out or ASK Timo if it's true. Never fill the gap with a plausible-sounding invention.
5. P.S. lines follow the same rule and stay on-brand (no violence/aggression jokes like throwing a trumpet).
Voice note Timo confirmed 2026-06-01: he LIKES the Ed-Lawrence-style whimsical, friend-sharing-a-story voice that makes Harrisson likable as a person. He DISLIKES the naggy/lecturing tutorial voice with numbered steps. Lead with Harrisson's own real stories, told warmly.

**Spelling: Harrisson, TWO s's** (origin 2026-05-17, `feedback_harrisson_spelling`). His first name is spelled **Harrisson**, not "Harrison." Timo verbatim: "you need to know how to spell Harrison. Harrisson Ball fucker." Authoritative sources: YouTube channel `@harrissonball`, channel display name "Harrisson Ball," the voc/synthesis voice protocol, and his email signatures all use Harrisson. Why it slips: the single-s misspelling dominates this workspace (including CLAUDE.md itself), so reading more context makes it worse, not better. Apply:
- Every email draft signed off by him uses "Harrisson Ball." Every chat message, summary, analysis, or output addressing or quoting him uses "Harrisson." Subject lines, ad copy, hooks, video titles all spell "Harrisson."
- Internal references in skill files and memory pointers can keep the dominant "Harrison" form (e.g. `feedback_harrison_voice.md`, `harrison-email-voice.md` are internal filenames Timo himself created); don't rename files, just fix outputs.
- Catch yourself typing "Harrison" in a deliverable = fix before sending. The audience knows his name; getting it wrong is a credibility hit.

## Hard bans from Harrison's 2026-05-09 call

(origin 2026-05-09, `feedback_harrison_email_call_20260509`: first time Harrison personally reviewed pb-email output, line-by-line on a live call with Timo. Audio `~/Downloads/transcribethis.m4a`, transcript `/tmp/transcribethis.txt`, Harrison portion ~line 510, after the violin teacher Wilhelm leaves the call. ENFORCEMENT: the hard bans below are encoded as RegExp rules in `Precision-Brass/dashboard/lib/email-lint.js`; the browser dashboard banners on hits at modal-open + broadcast-load and offers Auto-fix; pb-email-push runs the same lint via Node before any POST (Step 3a in `~/.claude/skills/pb-email-push/SKILL.md`). When a rule here is added or relaxed, ALSO update the RULES array in that file. Note 2026-06-07 standing rule: content lint WARNS, never hard-blocks Timo's own send; only the list-allowlist gate stays hard.)

**1. Forbes credential is BANNED, no exceptions.** Harrison verbatim: "I'm not in Forbes, bro… where did Paul get Forbes from?" The credential was hallucinated off Paul The Trombonist's bio; the pb-email skill contradictorily both REQUIRED it (voice protocol Section 2 + output template) AND told the auditor to reject it, so Forbes shipped to Harrison's eyes. The string "Forbes" appears nowhere in any draft, ever; auditor greps and rejects on hit. Files fixed 2026-05-09: `~/.claude/skills/pb-email/references/email-voice-protocol.md` (Section 3 + self-check), `~/.claude/skills/pb-email/references/email-output-template.md` (body template), `~/.claude/skills/pb-email/SKILL.md` (auditor check 5, failure mode 4), `~/.claude/skills/pb-email/agents/07-best-practices-auditor.md` (voice fidelity 3), `Precision-Brass/voc/emails/extracts/harrison-email-voice.md` (Sections 2, 6, 10).

**2. Subject line patterns, approved verbatim (Harrison wrote these on the call):**
- "This is why you {verb} {emotional outcome}" e.g. "This is why you quit trumpet playing three times"
- "The real reason why you'll never {verb}" e.g. "The real reason why you'll never succeed at coming back"
- "The reason why you {emotional outcome}" e.g. "The reason why you live in regret from your trumpet playing"
- "What's a {identity} without {thing}? {Pejorative}?" e.g. "What's a lead trumpet player without their upper register? Useless?"
- "I'm too {age}" (states the prospect's internal monologue) e.g. "I'm too old"

**Subject patterns BANNED (Harrison rejected verbatim):**
- "Why {identity} {polite verb}" (Harrison: "no, that's lame")
- "{Identity} quietly lose {thing}" (Harrison: "too direct, on-the-nose")
- "Pick up the horn after X years..." (Harrison: "soft cock")
- "{Number} year old isn't coming back. Here's what to do" (Harrison: "lame as fuck")
Why: Harrison wants emotional weight that stops the read. Indirect call-out beats direct accusation. Cannot read like marketing copy or trip spam filters. Section 1.5 of email-voice-protocol.md; auditor enforcement check 7 in SKILL.md.

**3. Body voice = aggressive call-out energy ("dude this sucks").** Harrison verbatim: "You're just like, dude, this sucks. It's like the emotional tie to it, 'cause it's like, it needs to be like, stop people." He reviewed competing creators' emails on the call and called the weak ones "limp dink" and "soft cock." A bold subject followed by a polite, hedging body is the worst combo: the reader opens expecting a punch, gets a hug, and immediately distrusts the sender. Harrison talks like a frustrated coach who's tired of watching the reader get sucker-punched by other methods; the aggression earns the right to deliver the solution. Body must drop the gloves at least once per email (one sentence that would feel uncomfortable to read aloud to a stranger). Banned hedge openers: "I just wanted to say...", "Maybe you've felt...", "If it's okay with you...", "Just checking in...", "No worries if...". Banned corporate hedges: "we believe", "many of our students", "in our experience". Section 1.6; auditor check 8.

**4. Topic guardrails, HARD ban.** Harrison verbatim: "Let's stay away from shitting on the Adams routine too much… It's gonna piss Jeremy Milosevic off, and him and I have a mutual understanding." Timo follow-up 2026-05-09: hard ban, no "a little bit" exceptions. Avoid ALL talk of the Adams routine; focus on other popular methods like Arban's, Schlossberg, general etudes.
- BANNED (any spelling, case-insensitive): "Adams routine" / "Adam's routine" / "Adams approach"; "hot air" approach; "Milosevic" / "Jeremy M".
- APPROVED roast targets: Schlossberg / Sloshberg; Clark studies (Claude Gordon Systematic Approach); Gordon (any Gordon-named method); James Stamp warmups; Arban's method drills (also Arbans, Arben); generic "more air, tighter corners" pedagogy; etudes generally.
Why: Harrison maintains a personal non-aggression pact with Jeremy Milosevic; the LA trumpet scene reads his emails; one slip burns a peer relationship. Section 12; auditor check 6.

**5. CTA hard rules.** Harrison flagged a draft whose CTA said "watch the training, link below" with no actual link, and roasted a competing creator's "this will be the easiest thing you'll ever do" CTA as "limp dink." Rules: every CTA must contain a real link or clearly-marked HiRose `?el=` placeholder (no "[link below]" placeholder text); no undersold CTAs ("easiest thing you'll ever do", "just hit reply, no big deal", "if you have a second"); CTA names the asset (training, strategy session, discovery call) plus an adjective (free, complimentary, no-cost). Approved verbatim 2026-05-09: "Click the link to watch the training and book your complimentary strategy session". Section 5; auditor check 9.

**6. Calendar-state preflight.** Harrison's last broadcast got 44% engagement and $0 in conversions because his calendar was full at send time; replies came back "no times available." Rule: pb-email asks Timo before every run: "Is Harrison's calendar currently open or full?" If full, drafts use the capacity-aware CTA variant ("we're at capacity, here's the waitlist") instead of "book a call"; P.S. type changes from `scarcity` to `social-pressure` or `risk-reversal`; never `urgency` when calendar is full. Step 1b in SKILL.md; Section 5 calendar-full variant in email-voice-protocol.md.

**7. Send cadence.** Harrison verbatim: "Every day, 4 a.m., nothing else. One a day, 4 a.m., not multiples." + "4 a.m. Los Angeles time." Phase 2 (AC publish) must honor 1/day at 4am LA. AC segment exclusions: exclude `booked-call` tag, require `40-day automation completed` tag. SKILL.md "Harrison's hard send rules"; Agent 7 send-cadence note overrides the 2-3x/week best practice. (Note 2026-06-01: the daily-email queue was cancelled pending a new format; see project_daily_email_queue_cancelled_20260601.)

**8. AUTO-SEND IS NOT BUILT (loud reminder).** Phase 2 AC publish does not exist; drafts go to dashboard for Harrison's manual review and manual AC send. Never write copy or status messages that imply auto-send. Top-of-file warning in SKILL.md; failure mode 10; Agent 7 send-cadence note.

**Win captured:** a subject line generated by pb-email beat Harrison's hand-written subject in a production A/B test "by far" (script proposal lens). Confirms the system is in the right ballpark when fed Harrison's voice catalog.

## Draft-time & send-time gates

**Draft-time gate (4 checks + visible GATE proof line)** (origin 2026-06-10, `feedback_email_draft_gate`). Quiz-email session; Timo: "clearly you're not learning and applying your learnings... I keep having to remind you." Four rules that ALREADY existed (specific named technique, swipe-file pacing, no oscillation, batch diversity) were injected into context by the angle-ledger hook and STILL broken at draft time. Knowledge in context does not equal execution at draft time. Send-time gates (send-rhythm-gate hook, angle-ledger) already existed and were NOT enough: the rules broke at DRAFT time, before any send gate could fire; that is why this gate runs at draft time, before pasting any draft in chat. Before pasting ANY email draft in chat:
1. READ 2-3 dimitri swipe-file emails THIS session; never draft from a remembered rhythm description.
2. Check every question's grammar matches its answers (action question, action answers).
3. The mechanism must be a do-able named Harrison technique verbatim from a transcript; a diagnosis is soft cock.
4. Synthesize corrections toward the middle; never flip extremes.
Then print the 1-line `GATE:` proof block above the draft so Timo can SEE the gate ran. No proof line = not paste-able. Canonical gate: `~/.claude/knowledge/email-draft-gate.md`. Wired into pb-email (auditor rule 8) and pb-email-write (chat draft gate step 0).

**Quality-gate pipeline (self-judgment removed from the loop)** (origin 2026-06-04, `feedback_email_quality_gate_pipeline`). Shipped a wall of text, over-corrected to one-sentence-per-line, over-corrected again into 4-5 sentence blocks (walls again), THREE times in one session, each time declaring it fixed off my own read. Timo: "you just keep missing it... there has to be a solution that makes you do this right without me ever having to ask again." Root cause was NOT the rule; it was self-certification on my own judgment, which is unreliable on rendered density. Three independent gates, ALL must pass before any email send or "done":
1. **Mechanical char-gate (BLOCKS the send).** `scripts/email-rhythm-check.py` flags any `<p>` over ~170 chars (the visual-height wall signal). Wired as PreToolUse hook `~/.claude/hooks/email-send-rhythm-gate.sh` on `send_draft_through_campaign`/`duplicate_campaign`: if the html_body fails, the send is BLOCKED (exit 2). Physically cannot send a wall.
2. **Auto-fired repetition gate.** `scripts/email-angle-ledger.py` + UserPromptSubmit hook `~/.claude/hooks/email-angle-gate.sh` inject the live saturation report into context on any email-intent prompt, so overused tropes are visible before drafting.
3. **Independent visual review (no self-certification).** Spawn a FRESH agent that renders each email to a screenshot at phone width, READS the pixels, and returns WALL/LIST/GOOD-RHYTHM + re-verifies every student quote against source + checks tropes. Do NOT declare done on my own read; ALSO read the screenshot myself (never outsource visual QA, per global VISUAL GATE), but the independent agent is the tiebreaker because my own read is the thing that kept failing.
Operating sequence for any email work going forward: draft -> run `email-rhythm-check.py` until PASS -> run `email-angle-ledger.py`, confirm no HEAVY trope reused -> spawn independent review agent (render + judge + verify quotes) -> read the screenshot myself -> only then send/schedule. The send hook is the backstop if step 1 is skipped.

## Link count

(origin 2026-05-15, `feedback_link_count_variation`) Across a batch of broadcast emails (or any cadence), the link count per email must VARY. Some drafts get 1 unique link (the body CTA; P.S. is text-only). Others get 2 unique links (body primary + P.S. secondary pointing to a DIFFERENT destination). The choice per email is based on what serves the close, not a fixed template. Incident: after fixing the "no duplicate URL" violation, the 7-draft batch ended up with exactly 2 unique links per email. Timo: "There doesn't always have to be two links. By the way, I would experiment sometimes having one link or having two, but not fucking both in the same place. I think having always two links per email might be a little too template-y for people." Per-draft decision tree:
1. **1-link drafts** when: the body CTA IS the close (no funnel laddering needed); the P.S. works as a text-only risk-reversal or reply-as-CTA closer; the email's energy is single-CTA discipline (best-practices research backs this for high-conversion sends). Examples from the 2026-05-15 batch: masterclass-anchored drafts where the masterclass IS the CTA, video-anchored drafts where the video is the close, drafts where the P.S. invites a reply rather than a click.
2. **2-link drafts** when: the body has a primary CTA AND a secondary destination genuinely adds value (e.g. testimonial proof after framework, or framework after testimonial). The 2nd link must be a DIFFERENT URL (no same-URL duplicates; block-severity; audit duplicates by destination URL, not anchor text).
3. **Across a 7-draft broadcast batch:** aim for roughly 50/50 split. Final 2026-05-15 mix was 4 with 2 links + 3 with 1 link. Don't make it exactly half; variance is the goal.
4. **NEVER** all drafts in a batch with the same link count (all 1-link OR all 2-link). That's the template-y failure mode.
Auditor enforcement (pb-email Agent 9): across the final 5 (or 7) drafts, count the unique-link distribution; if all drafts have the same count, flag for re-roll on at least 2 drafts to introduce variance. Per-draft, ban same-URL duplicates (block-severity).
Generalization: applies to any cadence content (broadcasts, sequences, social posts). Repeating the same structural pattern across a batch turns voice into formula and people unsubscribe. Variance per item, intention per choice.

## Source files (absorbed 2026-06-12)

1. feedback_email_batch_trope_diversity.md
2. feedback_email_short_paragraphs.md
3. feedback_email_draft_gate.md
4. feedback_email_friend_to_friend_depth.md
5. feedback_email_cite_specific_technique_and_vary_transition.md
6. feedback_email_voice_load_order.md
7. feedback_email_voice_spine_not_tone.md
8. feedback_email_revision_lessons.md
9. feedback_no_stranger_names_in_email_body.md
10. feedback_no_invented_story_details.md
11. feedback_subjects_speak_to_reader.md
12. feedback_link_count_variation.md
13. feedback_harrisson_spelling.md
14. feedback_harrison_email_call_20260509.md
15. feedback_run_angle_ledger_before_drafting.md
16. feedback_email_quality_gate_pipeline.md
17. feedback_harrison_voice.md (SUPERSEDED 2026-06-10; historical lesson + pointer to living canon preserved; dead files harrison-real-voice.md / voice-spec.md noted as deleted, not resurrected)
