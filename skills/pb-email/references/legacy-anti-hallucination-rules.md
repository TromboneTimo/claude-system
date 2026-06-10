# Legacy Anti-Hallucination Rules (ported from the deprecated /email skill)

> **Provenance:** Ported 2026-06-10 from `~/.claude/skills/email/SKILL.md` (the original "/email Precision Brass Email System", deprecated the same day). That skill's data files (`context/voice-bank.md`, `context/voice-spec.md`, `references/harrison-real-voice.md`, the whole `~/Desktop/precision-brass-emails/` project) are DELETED and exist nowhere on disk. This file preserves the rules and name lists that lived only there.
>
> **Dead-path map (read before following any old citation below):**
> - `references/harrison-real-voice.md` and `context/voice-spec.md`: GONE. The modern voice canon is `voc/emails/extracts/harrison-email-voice.md` (Precision-Brass repo) plus pb-email's `references/email-voice-protocol.md`. NOTE: the project memory `feedback_harrison_voice.md` still points at the deleted harrison-real-voice.md / voice-spec.md files; treat its load-order instruction as superseded by the modern load order in pb-email SKILL.md.
> - `context/voice-bank.md`: GONE. Its prospect/student name rosters are preserved in this file (below).
> - `transcripts/raw/masterclass-webinar-2026.md`: GONE at that path. The masterclass corpus now lives at `voc/masterclass/raw/` (see memory `project_masterclass_corpus.md`).
> - Original /email SKILL.md is recoverable from `~/.claude` git history.

These rules were added 2026-04-12 after a fabrication audit, plus field-test lessons from the Richard email. They remain TRUE and apply to every pb-email / pb-email-write run.

---

## Rule 1: Every name is guilty until verified

Auto-transcribed files (Loom, Otter, Fathom) MANGLE proper names. The 2026-04-05 masterclass transcript had these errors baked into brand.md:

- "Willie Mario" → actually **Willie Murillo** (Harrison's mentor, per letter of rec)
- "Matt Jodville" → actually **Mat Jodrell**
- "Vanessa Perka" → actually **Vanessa Perica**
- Unverified auto-transcript names (never confirmed): Yens Lenderman, Nadia Nordhouse, Rosco James Owen, Bones Malone, Larry (CTS)

Before using ANY proper name in an email, verify against the Press Kit folder, LinkedIn, or direct confirmation from Timo. If not verifiable, DO NOT USE.

## Rule 2: Prospects ≠ Students. NEVER blend them.

The old voice-bank had two sections with different email roles. The rosters (preserved here because voice-bank.md is deleted):

- **SECTION A - SALES CALL PROSPECTS:** Michelle, Karen, Joe, Tom, Walter, Richard, Ron, Barry, Robert, David, Toby, Jason, Joel, Will, Dave, Sam, Ted, Robbie, Johannes, Kent, Michael, John-Denver, John-IN, John. Use their quotes for **HOOKS**. NEVER claim they "became students," "got results," or "Harrison worked with them." They were on discovery calls. Many never enrolled.
- **SECTION B - STUDENT TESTIMONIALS:** Benny, Hannah, Mike BMW, Sharon, Trevor/Joville, Tony, John-testimonial, Mike-4mo, Unnamed-female; plus masterclass students Brad, Rachel, Yens-masterclass, Lee, Brandon, Philip. Use their quotes for **PROOF**. These are verified paying students with documented outcomes.

Language patterns:
- Diagnosing on a sales call? Say: "On our first call, I showed [prospect] that..." Accurate.
- Claiming transformation? Only for SECTION B names with verified results.
- NEVER: "We worked together and [prospect] improved." If you didn't witness it in their testimonial, don't write it.

(Modern enforcement: pb-email's voice protocol requires every cited student name to trace to `voc/testimonials/raw/`. This roster is the legacy ground-truth list.)

## Rule 3: Client drafts are drafts, not source of truth

If Harrison's own email says "Featured in Forbes" and it can't be verified externally, ASK before propagating. "Featured in Forbes" was in Harrison's Email 1; it was copied into 7+ emails before Timo confirmed it's not real. Lost credibility fast.

Always ask on first use: "Is [specific claim] something we can verify, or a placeholder?"

(Note: per the 2026-05-09 Harrison call, the Forbes credential is HARD-BANNED. See memory `feedback_harrison_email_call_20260509.md`.)

## Rule 4: "Unusual → Verify" filter

Before writing: scan source material for any claim that would make you go "huh?" on a cold read. Unusual teacher names, obscure credentials, specific publications, numerical stats. Flag them. Ask Timo. Better to pause than to ship fiction.

## Rule 5: Label every person inline during draft

In v1 of any email, annotate: "Karen (prospect)" or "Mike BMW (student)." Strip the labels before shipping. But write with them so the reviewer can audit attribution.

## Rule 6: SOURCE FIDELITY - Students + Solutions

**6a. Student names come from the TESTIMONIAL DATABASE only.**
Verified student roster (as of the 2026-04-12 audit):
- YouTube testimonials: Benny, Hannah, Mike BMW, Sharon, Trevor/Joville, Tony (trumpet teacher), John (jazz comeback), Mike (4-month), unnamed female student
- Masterclass documented: Brad, Rachel, Yens (masterclass student, NOT the unverified "Yens Lenderman"), Lee (trombone), Brandon, Philip (87-year-old)

If the name isn't in this list (or in `voc/testimonials/raw/` today), treat as prospect. Do not attribute student-level outcomes.

**6b. Solutions use Harrison's proven converting language.**
When an email describes HOW a problem gets solved, the language must come from:
- YouTube educational videos (e.g. the "sim" setup from the embouchure video, Gravity Breath technique, upstream/downstream explainer)
- Sales call breakthrough moments where the prospect shifted (e.g. the "right method, wrong type of player" reframe that triggered Karen's "no one has ever said that")

Modern source locations: `voc/masterclass/raw/` (Three Core Methods section), `references/converting-video-embouchure-transcript.md`, sales call raws under `voc/` per `voc/config.yaml`.

Before writing any solution paragraph, ASK: "Where in Harrison's content has he taught this specific fix? What exact phrase did he use?" If you can't cite the source, pull the phrase or cut the section.

Do NOT use:
- Generic coaching language ("rebuild your foundation," "unlock your potential")
- Your own synthesis of Harrison's method
- Paraphrases that drop specificity

---

## Rule 7: CONVERSION PRINCIPLES (field test: the Richard email, 2026-04-12)

The Richard email (identity-loss story, "He turned down every band that called" subject) got high engagement (opens, reads, replies) and ZERO conversions to booked calls. Harrison reported this directly. That data reveals 7 specific rules about converting vs engaging.

### 7a. Engagement is NOT success. Conversion is.
An email that gets read and felt but doesn't drive a strategy call booking is a failure with a silver lining. Don't celebrate opens. Don't celebrate replies. Count booked calls. If engagement is high but conversions are zero, the HOOK works but the CLOSE is broken.

### 7b. Never describe the solution in your own words. Link to Harrison's video.
The Richard email said "he's a downstream player, nobody checked": abstract, tells-don't-shows. A reader can't evaluate whether Harrison's fix is real from abstract description. Instead: tease the problem, then link to Harrison's own YouTube video demonstrating the diagnosis/fix.

**Rule:** Every solution section in a pain-point email must EITHER link to a Harrison YouTube video that shows the fix, OR cite a verified student case with documented result. Never just describe the method.

### 7c. The CTA must match the emotional register of the body.
Richard email body = heart-level (wife passed, identity loss, isolation). Richard email PS = technical (Brad fixed high C in 11 minutes). That's a tonal whiplash. The reader in the grief-zone gets yanked to a chops conversation and bounces.

**Rule:** Emotional body needs an emotional bridge before the CTA. "If you've been saying no to things you used to say yes to, let's figure out what's actually going on" matches Richard's register. "Book a 45-min call to fix your chops" doesn't.

### 7d. Proof stack must match the story arc.
Richard's arc: identity-loss, nobody-checked, turning down gigs. Brad (PS) had a range problem, a different arc. Trevor's arc (self-taught church player who "never thought improvement was possible" → hit high E live) matches Richard. Mismatch between body pain and proof outcome dilutes belief.

**Rule:** The student you cite in the PS/proof must have had the SAME TYPE of pain as the prospect in the hook. Not just any success story: a matching success story.

### 7e. Close with momentum, not reflection.
Richard email ends with "It might be that nobody ever checked." That's a diagnosis; it holds the reader in the wound. A conversion close pulls them toward the exit: "Here's how to find out for YOU" + link.

**Rule:** The last line before sign-off must face forward. Name the next action. Don't leave the reader in the feeling.

### 7f. Two-step CTA for emotional emails.
Forcing every reader to the same commitment level (strategy call) loses the ones who aren't ready. A two-step CTA respects where the reader actually is:
- **Step 1 (low friction, high fit for just-engaged reader):** Watch the video
- **Step 2 (high friction, high fit for ready-to-decide):** Book the call

The video also serves as qualification; readers who watch it show up to the call warmer.

### 7g. Bridge paragraph required between pain and CTA.
Don't jump from "here's Richard's pain" to "watch this video." Insert a bridge that explicitly says: "here's why this is solvable for YOU specifically." Example: "Richard isn't unusual. Most players I work with have been taught the wrong physiology for their body. And here's the thing: once you know which type you are, the fix is fast. [video link]"

---

## Post-Richard review checklist additions

Run on every draft (numbering kept from the legacy skill):

17. Does the email link to a Harrison YouTube video that demonstrates the fix (not just describes it)?
18. Does the PS/proof feature a student whose arc MATCHES the prospect's arc in the hook?
19. Does the CTA match the emotional register of the body?
20. Does the last line before sign-off create forward momentum (not reflection)?
21. Is there a two-step CTA (video + call), not just one?
22. Is there a bridge paragraph between the pain story and the CTA?

And the legacy anti-hallucination checks:

11. Every named person is correctly labeled prospect (Section A) or student (Section B)?
12. Every outcome/result claim is tied to a Section B name with verified testimonial?
13. No "Featured in Forbes" or other unverified credentials in sign-off?
14. Every unusual proper name (teacher, collaborator) cross-checked against press kit?
15. Every SOLUTION description traces back to a YouTube video or sales-call breakthrough moment (not your own synthesis)?
16. Every STUDENT name is in the verified testimonial database (not a prospect reframed as a student)?

---

## Legacy negative examples (what NOT to write)

Still-true teaching examples preserved from the old skill.

### GENERIC COACHING EMAIL (never do this):
```
Are you struggling with your trumpet playing? Many musicians face
challenges with range and endurance. I understand how frustrating
that can be. That's why I developed a unique system that has helped
hundreds of students improve their playing. If you're ready to take
your trumpet playing to the next level, I'd love to help.
```
Why this is garbage: No specific person. No story. No dialogue. "Many musicians" is vague. "Unique system" is empty. "Take your trumpet playing to the next level" is a cliche. "I'd love to help" is passive. Zero personality. Could be written by any coach in any niche.

### OVER-EXPLAINED TEACHING EMAIL (never do this):
```
Today I want to talk about breathing. Breathing is one of the most
important aspects of trumpet playing. In this email, I'll cover
three key principles that will help you improve your breathing
technique. First, let's discuss the role of the diaphragm...
```
Why this is garbage: "Today I want to talk about" = throat clearing. "One of the most important aspects" = filler. "In this email I'll cover" = literally telling them the agenda instead of hooking them. "Let's discuss" = academic, not conversational. No story. No person. No tension.

### THE CORRECT VERSION:
```
"Push from your diaphragm."

You've heard it. I've heard it. Every trumpet teacher in history
has said it.

It's wrong.
```
Why this works: Opens with a recognizable quote. Reader nods. Then contradicts it in two words. Record-scratch. Now they're reading.
