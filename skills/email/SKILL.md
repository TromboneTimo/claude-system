# /email -- Precision Brass Email System

## Description
Generates emails for Harrison Ball's Precision Brass coaching business that sound like Harrison wrote them, not like AI.

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
