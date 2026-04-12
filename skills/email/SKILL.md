# /email -- Precision Brass Email System

## Description
Generates emails for Harrisson Ball's (DOUBLE S) Precision Brass coaching business that sound like Harrison wrote them, not like AI.

## ANTI-HALLUCINATION PROTOCOL (MANDATORY - added 2026-04-12 after audit)

**Hard-won lessons from past failures. Ignore at your peril.**

### Rule 1: Every name is guilty until verified
Auto-transcribed files (Loom, Otter, Fathom) MANGLE proper names. The 2026-04-05 masterclass transcript had these errors baked into brand.md:
- "Willie Mario" → actually **Willie Murillo** (Harrison's mentor, per letter of rec)
- "Matt Jodville" → actually **Mat Jodrell**
- "Vanessa Perka" → actually **Vanessa Perica**
- Unverified auto-transcript names: Yens Lenderman, Nadia Nordhouse, Rosco James Owen, Bones Malone, Larry (CTS)

**Before using ANY proper name in an email, verify against:** `Press Kit.` folder, LinkedIn, or direct confirmation from Timo. If not verifiable, DO NOT USE.

### Rule 2: Prospects ≠ Students. NEVER blend them.
`context/voice-bank.md` has two sections. They have different email roles:
- **SECTION A — SALES CALL PROSPECTS** (Michelle, Karen, Joe, Tom, Walter, Richard, Ron, Barry, Robert, David, Toby, Jason, Joel, Will, Dave, Sam, Ted, Robbie, Johannes, Kent, Michael, John-Denver, John-IN, John). Use quotes for **HOOKS**. NEVER claim they "became students," "got results," or "Harrison worked with them." They were on discovery calls. Many never enrolled.
- **SECTION B — STUDENT TESTIMONIALS** (Benny, Hannah, Mike BMW, Sharon, Trevor/Joville, Tony, John-testimonial, Mike-4mo, Unnamed-female; plus masterclass students Brad, Rachel, Yens-masterclass, Lee, Brandon, Philip). Use quotes for **PROOF**. These are verified paying students with documented outcomes.

**Language patterns:**
- Diagnosing on a sales call? Say: "On our first call, I showed [prospect] that..." — accurate.
- Claiming transformation? Only for SECTION B names with verified results.
- NEVER: "We worked together and [prospect] improved." If you didn't witness it in their testimonial, don't write it.

### Rule 3: Client drafts are drafts, not source of truth
If Harrison's own email says "Featured in Forbes" and it can't be verified externally, ASK before propagating. "Featured in Forbes" was in Harrison's Email 1 — we copied it into 7+ emails before Timo confirmed it's not real. Lost credibility fast.

**Always ask on first use:** "Is [specific claim] something we can verify, or a placeholder?"

### Rule 4: "Unusual → Verify" filter
Before writing: scan brand.md for any claim that would make you go "huh?" on a cold read. Unusual teacher names, obscure credentials, specific publications, numerical stats. Flag them. Ask Timo. Better to pause than to ship fiction.

### Rule 5: Label every person inline during draft
In v1 of any email, annotate: "Karen (prospect)" or "Mike BMW (student)." Strip the labels before shipping. But write with them so the reviewer can audit attribution.

### Rule 6: SOURCE FIDELITY — Students + Solutions

**6a. Student names come from the TESTIMONIAL DATABASE only.**
Verified student roster:
- YouTube testimonials: Benny, Hannah, Mike BMW, Sharon, Trevor/Joville, Tony (trumpet teacher), John (jazz comeback), Mike (4-month), unnamed female student
- Masterclass documented: Brad, Rachel, Yens (masterclass student — NOT the unverified Yens Lenderman), Lee (trombone), Brandon, Philip (87-year-old)

If the name isn't in this list, treat as prospect. Do not attribute student-level outcomes.

**6b. Solutions use Harrison's proven converting language.**
When an email describes HOW a problem gets solved, the language must come from:
- YouTube educational videos (e.g. "sim" setup from embouchure video, Gravity Breath technique, upstream/downstream explainer)
- Sales call breakthrough moments where the prospect shifted (e.g. "right method, wrong type of player" reframe that triggered Karen's "no one has ever said that")

Source files for this:
- `transcripts/raw/masterclass-webinar-2026.md` — the Three Core Methods section
- YouTube video transcripts (paste when Timo provides)
- Sales call breakthrough moments in `voice-bank.md` → Breakthrough Moments section

Before writing any solution paragraph, ASK: "Where in Harrison's content has he taught this specific fix? What exact phrase did he use?" If I can't cite the source, pull the phrase or cut the section.

Do NOT use:
- Generic coaching language ("rebuild your foundation," "unlock your potential")
- My own synthesis of Harrison's method
- Paraphrases that drop specificity

---

## Description (continued)

## Activation
User says: `/email`, or any request involving Harrison's email system

## Project Location
`~/Desktop/precision-brass-emails/`

## CRITICAL: Context Load Order (Priority Matters)

Load these files IN THIS EXACT ORDER. Earlier files take priority over later ones. If there's a conflict, the higher-priority file wins.

### Priority 0: HARRISON'S REAL VOICE (load FIRST, before anything)
0. `references/harrison-real-voice.md` -- Extracted from Harrison's actual 12-email sequence. THIS OVERRIDES voice-spec.md wherever they conflict. This is how Harrison actually writes.

### Priority 1: VOICE (load second)
1. `context/voice-spec.md` -- Ed Lawrence-adapted voice rules. SECONDARY to harrison-real-voice.md. Use for patterns that are compatible with Harrison's real voice, ignore rules that contradict it.
2. `references/annotated-reference-emails.md` -- 5 annotated example emails. Quality benchmarks, but TONE must match harrison-real-voice.md.

### Priority 2: STRATEGY (load second)
3. `strategy/strategy-memo.md` -- What's working right now. Priority angles. Segment focus.
4. `strategy/angle-scores.md` + `strategy/creative-ledger.md` -- Which angle to pick. What's in cooldown.

### Priority 3: DATA (load third, for content)
5. `context/voice-bank.md` -- Verbatim prospect phrases. Pull subject lines and hooks from here.
6. `context/brand.md` -- Harrison's story, methods, credentials. For factual accuracy.
7. `context/audience.md` -- Who we're writing to. For empathy and relevance.
8. `context/offers.md` -- Program details. Harrison sells in body AND PS. NEVER mention price.

### Priority 4: STYLE REFERENCE (load if output feels generic)
9. `references/email-style-database.md` -- Ed Lawrence pattern analysis. The gold standard.
10. `references/email-frameworks.md` -- Brunson, Chaperon, Kern frameworks.

### DO NOT LOAD unless specifically needed:
- Transcript batch files (too long, dilutes context)
- SOP files (these are for humans, not for email generation)
- Performance tracking files (for reporting, not writing)

## Sub-Commands

| Command | What It Does |
|---------|-------------|
| `/email generate` | Write one email. Full flow below. |
| `/email sequence [type]` | Build complete sequence (welcome/nurture/re-engagement/pre-call) |
| `/email analyze-transcript [path]` | Process a Fathom transcript into synthesis files |
| `/email update-strategy` | Generate new strategy memo from performance data |
| `/email performance-report` | Score recent emails, update angle scores |
| `/email compliance-check [path]` | Validate a draft against voice-spec rules |
| `/email angle-status` | Show angle scores, cooldowns, availability |
| `/email queue` | Show upcoming sends |

## /email generate -- The Exact Flow

### Step 1: Load Priority 1 files
Read `voice-spec.md` and `annotated-reference-emails.md`. Internalize the voice rules and study the examples. These define HOW you write.

### Step 2: Load Priority 2 files
Read `strategy-memo.md`, `angle-scores.md`, `creative-ledger.md`. These define WHAT you write about.

### Step 3: Select angle
- Filter by cooldown (14 days same angle, 4 days same category)
- Rank by score
- Weight by segment (new = pain points x1.3, warm = credibility x1.3)
- Enforce diversity (not 3+ same category in a row)

### Step 4: Select framework
Based on angle category + what was used in last 3 sends:
- Pain Point -> PAS, Before-After-Bridge
- Credibility -> Hook-Story-Offer
- Value -> Educational Hook
- CTA -> AIDA

### Step 5: Load Priority 3 files
Read `voice-bank.md` for verbatim quotes to use as hooks and dialogue.
Read `brand.md` for factual details about Harrison's methods.
Read `audience.md` to check empathy alignment.

### Step 6: Write the email
Follow the structure from `voice-spec.md`:
```
Subject: [hook or story -- under 50 chars]

[First name],

[HOOK: specific person + specific event, 1-2 sentences]

[STORY: 3-5 short paragraphs with dialogue from voice-bank]

[INSIGHT: one idea, 2-3 paragraphs]

Harrison

PS -- [casual sell, 1-3 sentences]
```

### Step 7: Run Quality Gate
From `voice-spec.md`, check ALL of these:
1. Does this sound like Harrison talking to a friend, or like a marketing email? -> If marketing, REGENERATE.
2. Opens with a specific person/event, not an abstract statement?
3. Body is 100% value, ZERO selling? (sell in PS only)
4. Used dialogue from real transcripts?
5. Sentences averaging 14-16 words? None over 25?
6. Zero "we" or "our"?
7. Under 500 words body?
8. Subject under 50 chars?
9. Zero em dashes, zero emoji, max 1 exclamation mark?
10. Does it match the TONE of the annotated reference emails?
11. **Every named person is correctly labeled in voice-bank Section A (prospect) or Section B (student)?**
12. **Every outcome/result claim is tied to a Section B name with verified testimonial?**
13. **No "Featured in Forbes" or other unverified credentials in sign-off?**
14. **Every unusual proper name (teacher, collaborator) cross-checked against press kit?**
15. **Every SOLUTION description traces back to a YouTube video or sales-call breakthrough moment (not my own synthesis)?**
16. **Every STUDENT name is in the verified testimonial database (not a prospect reframed as a student)?**

**If ANY check fails: regenerate without outputting.**

### Step 8: Save and log
- Save to `output/emails/[YYYY-MM-DD]-[type]-[angle-id].md`
- Log to `strategy/creative-ledger.md` with cooldown date
- Add to `strategy/send-calendar.md` as Draft

## Negative Examples (What NOT to Write)

### GENERIC COACHING EMAIL (never do this):
```
Are you struggling with your trumpet playing? Many musicians face 
challenges with range and endurance. I understand how frustrating 
that can be. That's why I developed a unique system that has helped 
hundreds of students improve their playing. If you're ready to take 
your trumpet playing to the next level, I'd love to help.
```
**Why this is garbage:** No specific person. No story. No dialogue. "Many musicians" is vague. "Unique system" is empty. "Take your trumpet playing to the next level" is a cliche. "I'd love to help" is passive. Zero personality. Could be written by any coach in any niche.

### OVER-EXPLAINED TEACHING EMAIL (never do this):
```
Today I want to talk about breathing. Breathing is one of the most 
important aspects of trumpet playing. In this email, I'll cover 
three key principles that will help you improve your breathing 
technique. First, let's discuss the role of the diaphragm...
```
**Why this is garbage:** "Today I want to talk about" = throat clearing. "One of the most important aspects" = filler. "In this email I'll cover" = literally telling them the agenda instead of hooking them. "Let's discuss" = academic, not conversational. No story. No person. No tension.

### THE CORRECT VERSION:
```
"Push from your diaphragm."

You've heard it. I've heard it. Every trumpet teacher in history 
has said it.

It's wrong.
```
**Why this works:** Opens with a recognizable quote. Reader nods. Then contradicts it in two words. Record-scratch. Now they're reading.
