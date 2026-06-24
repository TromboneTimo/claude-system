---
name: canon-script-writing
description: ALL pb-script-write + hook design lessons. Consolidated 2026-06-12 from 7 files.
metadata: 
  node_type: memory
  type: feedback
  consolidated: 2026-06-12
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

# Canon: Script Writing (pb-script ideas, pb-script-write, pb-hook-design)

Read this file BEFORE any pb-script-write or pb-hook-design run, and before ANY script-related work in this project, even outside the skills. Rules are ordered oldest to newest; where rules conflict, the LATER-dated rule governs (reconciliations are flagged inline).

---

## 1. The 2026-04-25 mouthpieces-script failure modes (12 don'ts + 8 dos)

(Indexed historically as "the 14 failure modes"; the source file actually held 12 NOT-to-do items + 8 TO-do items. All 20 preserved here.) Learned the hard way during the "Stop Buying Mouthpieces" iteration: that session went through 12+ iterations on a single script because of regressions on these patterns. Future script work should hit the bar in 1-2 iterations, not 12.

### What NOT to do
1. **Don't write paragraphs of explanation.** Bullet director's notes only. Timo said "too much text", "be efficient", "lower text by half" multiple times.
2. **Don't summarize his locked phrasing.** Preserve verbatim. He had to repaste his own draft when I edited.
3. **Don't drop visual specs.** "Harrison sitting in front of all his mouthpieces" was specific and mandatory. Preserve all visual detail.
4. **Don't stack mistakes/tests as separate beats after trap topics.** Weave them inside the same beat. He flagged this twice.
5. **Don't fabricate stats or social proof.** Knowledge gaps OK, made-up "every single one of them stopped buying" claims NOT.
6. **Don't put meta-instructions inside the deliverable.** No "Send to Timo for review" footer in the page Harrison reads while filming.
7. **Don't write in clinical third-person register.** Harrison talks second-person, conversational ("Now,", "right?", repetitions, mid-sentence metaphors).
8. **Don't fragment every sentence into its own shot.** Beats can hold many sentences that flow together.
9. **Don't regress.** Once a fix lands, it stays. He repeatedly said "we fixed this before."
10. **Don't manhandle Harrison.** Locked lines for critical moments, riff topics for the rest. Trust him to improvise.
11. **Don't let PDF paragraphs split across pages.** CSS: `break-inside: avoid` on script paragraphs.
12. **Don't design over readability.** No yellow speech bubbles, no italic body, no chat-bubble metaphor. Script readability is sacred.

### What TO do
1. **7-beat interleaved structure.** Cold Open -> Demo -> Apparatus Reveal -> Mistake 1 (trap+mistake+test) -> Mistake 2 (same) -> Mistake 3 (same) -> Funnel. (LATER REFINEMENT 2026-06-01: this 7-beat Trap/Mistake/Test template is for "mistakes" videos ONLY; "system" videos use the 6-beat Antoine pattern. See section 5.)
2. **Each beat = one cycle.** Trap topic + named mistake + test demo all in one color-coded beat.
3. **Cold open visual gag.** Curiosity in 0-5s before any dialogue (e.g., Mission Impossible mouthpiece swap).
4. **Voice fingerprint:** "Now,", "right?", second person, repeats key terms 3-5x, names wrong way before right way, metaphors mid-sentence.
5. **Funnel pattern:** callback to tests + NEW knowledge gap question + "Hint: it's not what you think" + point to embouchure video card.
6. **Locked lines for hook, apparatus reveal, mistake callouts, funnel CTA.** Riff topics for everything else. (LATER REFINEMENT 2026-06-01: verbatim locked lines now apply to the HOOK only; beat bodies get topic anchors, never quoted sentences. See section 5.)
7. **Save deliverables to BOTH** project output AND `~/Downloads/`. (REFINED 2026-05-06: only the PDF goes to ~/Downloads/; HTML stays in scripts/ and output/. Full rule in canon_working_process.md.)
8. **PDF aesthetic:** warm off-white #FAF7F2 bg, near-black 22px Inter, 7-color vibrant accent palette per beat, no boxes around script, generous whitespace, max-width 760px single column.

### CRITICAL: applies even outside the pb-script-write skill
These rules apply to ANY script-related work in this project, not just inside the `pb-script-write` skill. If Timo pastes a draft with locked phrasing in a free-form conversation, preserve it character-for-character. Regression on this happened immediately after the rules were written. Verify before drafting: "did Timo write the cold open already? If yes, preserve it verbatim, no improvising."

### Reference files (read when generating a new script)
- `~/.claude/skills/pb-script/references/example-mouthpieces-script.md` (the proven structural template)
- `~/.claude/skills/pb-script/references/script-writing-protocol.md` (full ruleset)
- `/Users/air/Desktop/Precision-Brass/references/converting-video-embouchure-transcript.md` (voice source)

---

## 2. The 7 master lessons (2026-05-06, famous-method-killing-embouchure script, 15-iteration session)

Each cost multiple iterations to learn. Apply ALL OF THEM by default. Do not make Timo re-teach any of these.

### Lesson 1: VOC mining IS the first step, not an optional afterthought
**The single biggest lesson of the session.** I drafted the script entirely from Timo's pasted instructions and pedagogy guesses. He had to explicitly call me out and ask if I was even using the database. When I finally ran the 6 mining agents, the script transformed. Real prospect quotes (Karen, Ted, Barry, Tom, Richard, Johannes, Bruce) carried more weight than any director's note I could write.
**Why:** the database exists for a reason. Inventing prospect objections from general pedagogy is fabrication. Real verbatim language is the conversion edge.
**How:** spawn 6 parallel mining agents against the FULL vault (not just sales calls) BEFORE drafting any beats. Sales calls + testimonials + YouTube comments + FB ads + voice banks + objection library + youtube-database + voc/meta-ads. ALL of it. Different lens per agent. (Note: project_8_agent_restructure_20260515 later expanded the roster to 8 parallel specialists + 1 sequential auditor.)

### Lesson 2: Bullet anchors are 1-line director's intent, NOT prose Harrison reads
Bullets that wrap to 2-3 lines kill Harrison's voice. He needs short labels he can riff off. Locked one-liners are the only exception.
**Why:** Long bullets read like a Teleprompter draft. Harrison improvises better than any pre-written sentence.
**How:** if a bullet is more than 1 line on the page, cut it. Use a verb + object. "Drop the marathon metaphor" beats "Talk about how the marathon metaphor is like running with a weight."

### Lesson 3: When you reference a metaphor by short label, define it inline the FIRST time
Harrison doesn't have my context. He cannot expand a label he hasn't seen the full version of. The first beat that uses a metaphor must spell out what the metaphor is. Later beats can use the short label.

### Lesson 4: Each step gets its OWN shape. No rigid template across all steps.
Don't force every step into the same bullet structure. Step 4 might be a brief intro. Step 5 might lead with VOC quotes. Step 6 might pre-empt a denial. Step 7 might tease unknown info. Each step's shape serves the content of THAT step, not a copy-paste format.

### Lesson 5: Curiosity loops are spent currency. Use them only where attention must be re-bought.
Ed Lawrence does NOT loop every section. He uses loops at 4-5 specific moments per video. Forcing a loop into every step reads like copy-paste and kills the ones that earn their place. When you DO use loops, cycle through 5 distinct types: pre-empt objection, pose-the-next-question, reveal-contradiction, tease-new-info, bait-why-question. Never repeat the same loop shape twice in one script.

### Lesson 6: Bridges connect on CONTENT, are direction notes (not Harrison's lines)
Bridges name what just happened + what comes next, on substance. NOT filler like "get Step 4 right and you're set up for Step 5." Also NOT pre-written words Harrison would say. Direction note format: "Pivot to the demo. Cut back to camera." Harrison fills in the actual words.

### Lesson 7: Instructions are DIRECTIVE to Harrison, not abstract third-person
"Cut to camera." not "Harrison transitions to camera." Every "Harrison X" line in the doc is a code smell. Trim to a verb the reader can act on.

### Process meta-lesson
Don't render to PDF before Timo has approved a plain-markdown chat draft. Two checkpoints: (1) chat draft approval, (2) render approval. Iterating on plain text is cheap. Iterating on rendered files wastes everyone's time. PDF only goes to ~/Downloads/. HTML stays in scripts/ and output/. (Full chat-draft-before-render rule in canon_working_process.md.)

---

## 3. The 10 v2 lessons (2026-05-13, mouthpiece-buzzing + daily-inconsistency scripts)

Origin: two scripts in one session, `i_20260426_mouthpiece_buzzing` (published 2026-05-06) and `i_20260426_daily_inconsistency` (in progress 2026-05-13). Timo had to redirect on the same kinds of failures across both. These layer ON TOP of the 7 master lessons above; read both before any new pb-script-write run.

### Sourcing

**Lesson 1: Mine the masterclass FIRST. Verbatim teaching trumps composition.**
The converter transcript (`references/converting-video-embouchure-transcript.md`) is Harrison's most polished public teaching. Real lines like:
- *"Muscle memory does not exist. Neurological memory exists."*
- *"Everything comes down to not the trumpet, not the gear, but the way you set yourself up for success."*
- *"The same setup every single time is consistent."*
- *"That is the real reason that people have inefficiencies, they have terrible endurance, and they blame it on some other reason."*
These convert because they're his actual voice. Composing locked lines IN his fingerprint is weaker than LIFTING his lines verbatim.
**Rule:** Spawn a 7th mining agent in the VOC sweep, scoped to the masterclass transcript only. Pull every Harrison-teaching line relevant to the script's beats. Use those as locked-line candidates BEFORE composing anything.
**Confirmed 2026-05-13** on the inconsistency script. Timo: "Please look through the webinar that you have in your database to pull out key moments of Harrison's teaching." The "webinar" he meant was the converter masterclass. I should have known.

**Lesson 2: Locked lines should be VERBATIM Harrison, not composed in his voice.**
Default preference order for locked-line content:
1. Verbatim Harrison quote from the converter masterclass (cite source).
2. Verbatim Harrison teaching from a sales call (cite call and timestamp).
3. Verbatim Harrison line from a testimonial moment (Harrison coaching mid-testimonial).
4. Composed line modeled on his voice fingerprint (last resort; tag as `[COMPOSED. confirm with Harrison]`).
Tag every locked line with its source. Harrison should be able to look at any locked line and see whether it's his real phrasing or a composition he can override.
(RECONCILE with 2026-06-01 rule in section 5: locked verbatim lines now live in the HOOK only. Inside beats, masterclass verbatim still informs WHAT he teaches, but is presented as topic anchors, not quoted sentences for him to read.)

### Listening to Timo

**Lesson 3: Preserve Timo's exact wording. No silent substitution.**
When Timo writes specific phrasing in chat, it goes into the script VERBATIM. No paraphrase. No "cleaning up." No substitution.
Failures from this session:
- "Air compression tube thing he did in a short video recently that went viral" got rewritten as "lead pipe." Wrong. Should have kept his phrasing.
- "Two-sentence skit" became a paragraph with stage + jacket + dim lighting. Wrong.
- "Buzzing routine like he did in his previous long-form buzzing video" got sourced from a sales call instead. Should have asked which video.
**Rule:** If a substitution feels necessary, ASK before writing. Tag `[Timo's wording locked]` next to phrases you must preserve verbatim.

**Lesson 4: Reshape around Timo's suggestions. Don't garnish.**
When Timo proposes a structural element (include the buzz chain as the hook, make the practice-wrong-way the centerpiece), the next draft RESTRUCTURES around that suggestion. It doesn't tuck the suggestion in as an addition to the existing structure.
Test: after revising, ask "if Timo's idea disappeared, would the script's logic still work?" If yes, his idea was garnish. If no (the script's spine depends on his idea), the reshape was correct.
Confirmed 2026-05-13: I kept treating his ideas as additions across two scripts. He told me directly: "I suggested very specific content ideas, and I don't see you putting them in anywhere or you heavily rewarding it."

**Lesson 5: Lengths Timo specifies are HARD limits.**
"Two sentences" = two sentences. Not a paragraph with stage design. "30 seconds" = 30 seconds of actual content, not a structural template. "Short rep" = short. Not 3 reps + variations. If a length feels too tight, ask. Don't expand silently.

### Defaults (what every MOFU script should have)

**Lesson 6: Hook ALWAYS includes a roadmap promise.**
YouTube educational best-practice that converts. Default Hook template includes:
> "In this video, I'm going to show you the [N] things that are actually [causing X / fixing Y / etc.], and what you can do to fix every single one of them, even if you've been [doing X for Y years]."
The "even if you've been doing X for Y years" clause is the conversion lever. It pre-empts the "I've tried everything" objection.

**Lesson 7: MOFU default beat. The practice trap.**
Most comeback players have been practicing daily for decades with no progress. The conversion question isn't "why isn't trumpet working" but "why isn't MY PRACTICE working." Name this directly:
- People are practicing the wrong way (drilling skill on top of an unlocked apparatus).
- More reps don't help because each rep teaches the nervous system a different setup.
- Harrison's masterclass line lands here: *"Muscle memory does not exist. Neurological memory exists."*
Default: include a "practice trap" beat in every MOFU script unless the topic genuinely doesn't intersect with practice.

**Lesson 8: Strip verbose shot prescriptions.**
DO NOT write: "Camera tight on face for stage 1, pulls back for stages 2 and 3" / "Wide shot. 30 to 60 sec demo. Camera back to wide." / "Side-profile shot. Show the jaw position closed vs open."
DO write: "Shoot like Reference [letter]." (with YouTube URL), or a 1-line description of the SHOT'S PURPOSE, not its mechanics ("Show the wrong placement then the right placement.").
Timo flagged 2026-05-13: "I really fucking hate the way you describe certain shots." Harrison and his videographer don't need shot mechanics. They need intent.

**Lesson 9: Whiteboard = one moment, maximum.**
If a whiteboard is in the script, it appears ONCE, at the system-explanation beat (typically the anchor/VAS beat). Used to draw the diagram, then put away. Don't return to it. One whiteboard moment becomes a memorable visual hook; three dilute it and slow the script.

**Lesson 10: Ask for reference videos upfront.**
In the FIRST response after fetching the idea (before drafting), ask:
> "Do you have YouTube videos you want Harrison to model specific beats on? Especially the demo, any prop moments, or the system-explanation beat?"
If Timo sends URLs, bake them into a "Watch Before Filming" card at the top of the doc and reference them per beat ("Shoot like Reference A"). This pattern worked on the mouthpiece-buzzing script (3 URLs Timo sent).

**Cross-reference:** `project_harrison_lessons_database_incoming.md` (when the student-lessons database lands, it becomes the #1 source for verbatim teaching, ahead of the masterclass). `feedback_classifier_verification_must_use_ground_truth` / canon_attribution_analytics.md (same meta-pattern: don't compose / verify against your own work; use the human + the real corpus).

---

## 4. Proven 3-bullet hook structure: Problem -> Cause -> Promise (Timo-approved 2026-05-06)

Default hook for every Phase 2 long-form script (approved after multiple iterations on the famous-method-killing-embouchure script).

### The structure
1. **Call out the problem.** Name the surface-level frustration in language the viewer recognizes. Use specific symptoms (years of the same warmup, sound/range/effort haven't moved, etc.). This is the "you" sentence. Hooks the comeback player.
2. **Name the cause.** Diagnose the invisible problem underneath the symptom. Frame it as something the viewer couldn't have known without Harrison telling them. The apparatus isn't set, the order is wrong, the placement is wrong, etc. This is the "here's what's actually happening" sentence.
3. **Promise the payoff.** Stack two things: (a) the system that fixes it, AND (b) what NOT to do while running it so it actually sticks. The "AND what not to do" half is non-negotiable per Timo's 2026-05-06 standing instruction. Without it the promise feels generic.

### Format rules
- Bullet anchors, NOT verbatim sentences. Each bullet is a topic prompt Harrison rides. Two short clauses max per bullet. No locked prose.
- Hook is the journey roadmap for the rest of the video. Each bullet should map to a section of the script.
- Hook bullets are NEVER long paragraphs. If a bullet runs over two lines on screen, cut it.

### Why this works (Timo's reasoning)
> "It's very clear, like the flow of logic there, and I love the amount of information you gave, which is perfect there." (2026-05-06)
The Problem -> Cause -> Promise arc is mini-story compression. Viewer feels seen (problem), gets the aha (cause), commits to staying (promise). Three beats is the smallest viable narrative.

### Apply this
- Default to this hook structure in pb-script-write for every new long-form. If the script needs a different hook shape (rare), explicitly justify why before drafting.
- NOTE/RECONCILE: when running the dedicated **pb-hook-design** skill (or a "system"-video hook), the 2026-06-01 spec in section 5 governs (80-90 word verbatim hook, fixed lead order). Problem->Cause->Promise remains the default 3-bullet anchor pattern for ordinary pb-script-write long-forms; the two coexist (anchor-bullets default vs designed-verbatim hook).

### Reference example (the 2026-05-06 Timo-approved hook)
- Call out the problem: years of the same daily warmup, same range exercises, same lip slurs, sound and range and effort haven't moved.
- Name the cause: the apparatus isn't set for you, so every famous method (including the ones you teach) makes it worse, not better.
- Promise the payoff: today you'll learn the system that fixes this AND exactly what NOT to do while running it, so it actually sticks.

---

## 5. Hook design + bullet density rules (2026-06-01 Vertical Alignment System session)

NON-NEGOTIABLE; each was Timo-corrected during a single iterative drafting session. Repeating them costs trust. Apply to all future pb-hook-design and pb-script-write runs.

### Hook construction (pb-hook-design)
1. **Hard word budget: 80-90 words for 30 seconds.** Anything over is bloat. Cut to the bone before showing in chat.
2. **Lead order is fixed.** Stat-shock (false belief) -> CONSEQUENCE BEAT (3 specific stacked pains) -> authority anchor -> system tease -> gatekeeping. The consequence beat is mandatory between stat-shock and authority. Without it the pain is abstract.
3. **NEVER name the proprietary system in the hook.** Use "a system" or "the secret method". The naming reveal happens in the body, not the opening 30 seconds. Naming the system in the hook kills curiosity.
4. **NEVER describe the system mechanics in the hook either** if the name is non-obvious (like Vertical Alignment System). Just say "a system". Describing the parts in the hook is the same mistake as naming it.
5. **Authority anchor adjustment for under-30 creators.** Drop "X years playing." Use "After teaching hundreds of [specific subgroup]" instead. Student count, not tenure.
6. **Dream outcome stack belongs in the authority slot, not separate.** Pattern: "I built a system that gives my students [outcome 1], [outcome 2], and [outcome 3]." Three stacked outcomes, one sentence.

### Script structure (pb-script-write)
1. **1-2 bullets MAXIMUM per beat. Period.** No exceptions for narrative complexity. More than 2 bullets per beat overwhelms Harrisson and shows in his on-camera energy.
2. **NO section labels.** Eliminate "Locked X", "Purpose:", "Riff:", "ACTION:", "VOC pull-quote:" sub-headers entirely. Per beat: heading line + 1 short paragraph of what happens visually + 1-2 bullet topics. Nothing else.
3. **DO NOT tell Harrisson what to say in quotes.** Don't write verbatim sentences for him. Explain WHAT he explains as topic, list sub-topics he covers. Harrisson improvises better than any draft can.
4. **Insert specific repertoire suggestions, not abstractions.** Name actual pieces (Beethoven Ode to Joy in Bb, Haydn Trumpet Concerto opening, Carnival of Venice main theme, When the Saints Go Marching In) and exercises (Clarke Technical Studies #1, Carmine Caruso 6 Notes, lip slurs from low C to G). Antoine pattern: name real repertoire, never abstract "an exercise".
5. **Demo pacing matches topic class.** Mechanical/positioning videos (placement, alignment, embouchure, fingerings) get 2-3 short demos per beat, roughly 1 every 60 seconds. This matches Antoine's "This One Fix" (13 demos in 12 min, the highest-density technical video). Story/persuasion videos get 0-1 demo per beat (sLpOh6wpQZs has 0 demos in 14 min).
6. **Structure adaptation by Antoine reference.** Default to 6-beat Antoine pattern for "the system" videos: Hook + 3-4 named element beats + Apply on a real piece + CTA. The 7-beat Trap/Mistake/Test mouthpieces template is for "mistakes" videos only, not "system" videos. Match the body shape to the hook archetype.
7. **NO mid-roll System Reveal beat.** The system is named in the hook OR in the first bridge sentence after Beat 1, not as a separate beat. Antoine doesn't waste a beat on "the system is..." reveals; he just teaches.

### What stays the same (explicitly re-affirmed 2026-06-01)
- The chat-draft-before-render rule. Full draft in plain markdown FIRST. Render only on explicit approval.
- The two-checkpoint flow (chat draft approval, then render approval, then upload).
- The locked-line format for the hook verbatim (the hook stays italic-quoted because every word matters).
- The funnel pattern with the embouchure converter video card.
- The visual plan per beat (what the viewer sees).

---

## 6. Bullet anchors are intent, not text Harrison reads (2026-05-06)

For Harrison long-form scripts (pb-script-write), bullet anchors are DIRECTOR'S INTENT, not draft copy. Each bullet = one short line describing the *purpose* of that beat: what Harrison is trying to land, why it's there, what it connects to. Never write the actual sentences Harrison would say. He fills in his own words on camera.

**Why:** Harrison's voice gets killed when bullets become paragraphs of pre-written prose. Long bullets read like a Teleprompter draft and pull him out of his natural register. Timo flagged this twice in the 2026-05-06 famous-method-killing-embouchure iteration: first on Step 3 (too many bullets), again on Step 3 (still too long). The third pass nailed it: 1-line intent bullets, no quoted prose. Locked one-liners stay verbatim, but everything else is short anchors.

**How to apply:**
- Default bullet length: ~1 line. If it wraps to 2-3 lines on screen, it's already too much. (And per 2026-06-01: 1-2 bullets MAX per beat.)
- Each bullet says WHAT this beat does and WHY (the connection to the previous beat or the payoff for the next one).
- Locked one-liners (verbatim quotes Harrison must say word-for-word) stay long if needed. Those are the exception. (Per 2026-06-01: in practice this exception is now the HOOK.)
- Metaphors and reframes get a short label, not the full speech. ("Drop the marathon-with-a-weight metaphor", not the whole metaphor written out.)
- When in doubt, cut. Harrison improvises better than any draft can write for him.

Layered on the protocol: locked lines verbatim, riff topics as bullets, but RIFF BULLETS = short intent labels, not pre-written paragraphs.

---

## 7. Lead with Harrison's named techniques, not with diagnosis (2026-05-15)

**Rule:** When generating video ideas for Harrison (pb-script, pb-script-write, pb-email, anywhere Harrison's content is being framed), default to the POSITIVE technique-reveal frame, not the diagnostic mistake-shaming frame.

**Why:** Caught 2026-05-15. I generated 5 video ideas where every title was diagnostic ("Mouthpiece Pressure Test", "Russian Roulette With Your Embouchure", "Why You Crunch The High Note", "Your Practice Routine Is The Problem", "Noodle Around"). Timo pushed back: Harrison's actual methodology has named techniques he teaches (amisha, vertical alignment, dynamic repetition, gravity breath, 4 points of contact, upstream/downstream, place-breathe-play, wedge breath, circular energy). Harrison himself uses the word "secret" 14 times in the masterclass. That's the on-brand frame for his channel. Diagnostic-only framing reads as identity-attacking and misses the actual conversion lever, which is "here is a thing I teach that you have never heard of."

**How to apply:**

1. **Title patterns to default to:**
   - "[Technique Name]: [Promise of unlock]" e.g. "Dynamic Repetition: Why This Replaces Long Tones"
   - "The [Named Move] [Pros/Harrison/Upstream Players] Use To [Outcome]"
   - "How To [Outcome] Using [Named Technique]"
   - "The Secret [Technique]" e.g. "The Vertical Alignment Secret That Doubles Your Range"
   - "[Named Concept]: [Hidden Insight]"

2. **Harrison's actual named techniques to surface** (from `voc/masterclass/extracts/masterclass-voice-bank.md`):
   - **Amisha / amisher** (22x in masterclass). Harrison's word for the embouchure formation.
   - **Vertical Alignment System / Vertical Alignment** (6x). The proprietary system name.
   - **Upstream / Downstream** (18x). Player taxonomy.
   - **Dynamic Repetition** (13x). Practice methodology, replaces long tones.
   - **Gravity Breath** (5x). Specific breathing technique.
   - **Wedge Breath** (4x). Specific breathing technique.
   - **Place. Breathe. Play.** The 3-step (or 6-step expanded) setup sequence.
   - **4 Points Of Contact.** Donald Reinhart concept Harrison uses.
   - **The Apparatus.** Harrison's collective term for lips/teeth/corners/air.
   - **Circular Energy.** Concept for air return.
   - **The Doubt Fairies** (locked metaphor). The inner critic when notes feel uncertain.

3. **The diagnostic frame is still valid but as the SECOND beat, not the title.** Structure: hook with the secret technique, then validate with the pain it solves. Not: hook with the pain, then promise to fix it. Order matters because the search-term match and click-through trigger off the title.

4. **Verbatim quote evidence stays the same.** VOC mining still anchors every idea in real prospect/customer pain. The reframe is at the TITLE + HOOK + IDENTITY OUTCOME level, not the underlying research.

5. **When in doubt:** "What technique would Harrison name if he had to teach this in one sentence?" If you cannot name a Harrison-specific move, the idea is too generic and should be rewritten or dropped.

**Banned title patterns** (diagnostic-only, no technique):
- "Why You [Mistake]" / "The [Mistake] Problem"
- "Stop [Doing Wrong Thing]"
- "The [Trap/Lie/Myth] [Subject Matter]"
- Any title that names ONLY a problem and offers no technique by name

**Half-OK patterns** (mistake + technique-promise, OK but not preferred):
- "Why [Mistake] Hasn't Worked (And The [Named Technique] That Does)"
- "Stop [Wrong Thing]. Use [Named Technique] Instead."
These are acceptable when the mistake is genuinely the dominant scroll-stopper for the target audience. But the title MUST name the Harrison technique that replaces it. Pure-mistake titles are out.

**Cross-reference:** project_masterclass_corpus (masterclass voice bank holding all named techniques), project_8_agent_restructure_20260515 (the 8-agent roster defaults to this framing).

---

## Source files (absorbed 2026-06-12)
- feedback_script_writing_lessons.md (2026-04-25 mouthpieces failure modes)
- feedback_pb_script_write_master_lessons.md (7 master lessons, 2026-05-06)
- feedback_pb_script_write_v2_lessons.md (10 v2 lessons, 2026-05-13)
- feedback_pb_hook_design_revision_lessons.md (2026-06-01 VAS session)
- feedback_hook_structure_proven.md (Problem->Cause->Promise, 2026-05-06)
- feedback_bullet_anchors_are_intent_not_text.md (2026-05-06)
- feedback_lead_with_technique_not_diagnosis.md (2026-05-15)
