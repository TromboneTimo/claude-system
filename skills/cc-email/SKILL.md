# /cc-email -- Creator Conservatory Email System

## Description
Generates emails for Tim Maines' Creator Conservatory coaching business. Tim's voice: direct, irreverent, proof-heavy, anti-guru. Musicians who want to grow online.

## ANTI-HALLUCINATION PROTOCOL (MANDATORY - added 2026-04-12 after Precision Brass audit)

Lessons from the Precision Brass failure apply here. See full audit: `~/Desktop/Timo LLC/creator-conservatory/research/precision-brass-email-system-redesign-2026-04-12.md`

### Rule 1: Auto-transcripts MANGLE proper names
Fathom, Otter, Loom auto-transcriptions produce errors like "Willie Mario" (real: Willie Murillo), "Matt Jodville" (real: Mat Jodrell). **Before using any proper name from a transcript, verify against a press kit, LinkedIn, or Tim's direct confirmation.**

### Rule 2: Prospects are NOT students
Separate discovery-call transcripts (people who HAD sales calls) from testimonials (people who PAID and GOT RESULTS). Harrison is Tim's flagship student case study. Everyone else: verify status before implying transformation.
- Prospect quotes = HOOK material (they represent the reader)
- Student quotes = PROOF material (they represent the outcome)
- NEVER claim a prospect became a student unless verified.

### Rule 3: Tim's own drafts are drafts, not fact
If Tim's draft email contains a credential ("Featured in X", "worked with Y"), ASK before propagating to multiple emails. See Precision Brass: "Featured in Forbes" was in Harrison's own draft — we shipped it in 7 emails before it was flagged as fake.

### Rule 4: Review checklist addition
Every email must pass: "Every named person is labeled prospect or student. Every outcome claim cites a verified testimonial. No unverified credentials in sign-off."

## Activation
User says: `/cc-email`, or any request about Creator Conservatory emails

## Project Location
`~/Desktop/Timo LLC/creator-conservatory/`

## CRITICAL: Context Load Order

First read `knowledge-index.md` at project root. It maps everything and tells you what to load when.

### Priority 1: VOICE (always first)
1. `email-system/voice-spec.md` - Hard numbers, forbidden words, quality gate.
2. `email-system/annotated-reference-emails.md` - 5 annotated examples.

### Priority 2: STRATEGY (second)
3. `email-system/strategy/strategy-memo.md` - Current direction.
4. `email-system/strategy/angle-scores.md` - What to write about.
5. `email-system/strategy/creative-ledger.md` - What's been sent.

### Priority 3: BRAND (third)
6. `context/brand.md` - Tim's story, credentials, positioning.
7. `context/offers.md` - Conservatory, Hook Book, services.
8. `context/audience.md` - ICP: musicians who want to grow online.
9. `context/competitors.md` - BookLivePro, byaustere, etc.

### Priority 4: KNOWLEDGE BASES (on-demand, per knowledge-index.md)
10. `references/jason-batch*.md` - Hormozi frameworks (load specific batch based on task)
11. `transcripts/analyzed/` - Call transcript analysis (load when mining for stories)
12. `references/high-ticket-email-research.md` - Email sequence frameworks (load when designing sequences)

## Sub-Commands

| Command | What It Does |
|---------|-------------|
| `/cc-email generate` | Write one email. Full flow with quality gate. |
| `/cc-email sequence [type]` | Build sequence: welcome, nurture, launch, win-back |
| `/cc-email angle-status` | Show angle scores and cooldowns |

## /cc-email generate -- Flow

1. Load Priority 1 (voice-spec + annotated examples)
2. Load Priority 2 (strategy + angles + ledger)
3. Select angle (filter cooldowns, rank by score)
4. Select framework based on angle category
5. Load Priority 3 (brand + offers + audience)
6. Write email following voice-spec structure
7. Run Quality Gate:
   - Sounds like Tim, not a marketing department?
   - Opens with specific event/result, not abstract advice?
   - Body is value, sell in PS only?
   - At least 1 specific number or client result?
   - Zero em dashes, zero "on this journey," zero "leverage"?
   - Under 450 words? Subject under 50 chars?
   - Would Tim actually say this out loud?
   - **ANY failure = regenerate**
8. Save to `email-system/output/emails/`
9. Log to creative ledger

## Negative Examples

### GENERIC COACH EMAIL (never):
```
Are you a musician struggling to grow your online presence? 
I help artists like you build sustainable businesses through 
strategic content creation. Let me show you how.
```
**Why garbage:** "Struggling to grow your online presence" is a cliche. "Artists like you" is vague. "Strategic content creation" means nothing. "Let me show you how" is passive.

### TIM'S WAY:
```
Harrison was invisible online. Good trumpet player. Great teacher. 
Zero digital footprint.

Now he makes $50K/mo. All from YouTube.
```
**Why this works:** Specific person. Specific before ("invisible," "zero footprint"). Specific after ($50K/mo). No jargon. No "let me show you."


---

## VISUAL SELF-QA (MANDATORY before reporting done)

**After generating any HTML, PDF, slide, chart, or image output, you MUST render it and READ the result with your vision tool BEFORE reporting done.** Never ask the user to verify what you can verify yourself. Running `open` to launch Preview is NOT verification.

**Commands:**

```bash
# HTML -> PNG (no visible browser)
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --headless --disable-gpu \
  --screenshot="/tmp/verify.png" --window-size=1440,1800 \
  "file:///absolute/path/to/file.html"

# PDF -> PNG, multi-page, 150 DPI (optimal for AI vision)
pdftoppm -r 150 -png input.pdf page
# produces page-1.png, page-2.png, page-3.png, ...
```

Then use the `Read` tool on each PNG. Check for: page-break splits (cards cut in half), text overflow, misaligned elements, missing images, color/contrast issues, wrong fonts, responsive regressions. If any issue found: fix source, re-render, re-verify. Only report done when rendered output is correct.

**Full protocol:** `~/.claude/knowledge/visual-self-qa-protocol.md`
**Rule origin:** 2026-04-12 PDF proposal card split across page break, caught by user. Never again.


---

## CONTENT VERIFICATION GATE (ASK, DONT INVENT)

**When writing copy that references a real person (client, prospect, endorser, testimonial subject) — NEVER invent behavioral claims to make a pitch smoother. ASK the user instead.**

Trigger phrases that require verification:
- "You already X" / "Since you X" / "Given your weekly/monthly Y"
- "As part of your regular Z" / "Like the [interviews/videos/posts] you do"
- "Your existing [habit/practice/content]"

Before shipping any draft:

```bash
# grep the draft for fabrication-risk phrases
grep -iE "already|existing|since you|your weekly|your monthly|like you do|given your|as part of your" draft.md
```

For each hit: verify evidence (transcript, memory, prior confirmed conversation). If not verified: **ASK the user before writing it**. Do not invent a plausible-sounding version. Narrative convenience is the #1 source of fabrication.

Separate two claim types:
- **What they HAVE** (access, network, skills, audience) — safe if backed
- **What they DO** (behaviors, habits, routines) — requires verification

Full rule: `~/.claude/projects/-Users-air-Desktop-Timo-LLC-creator-conservatory/memory/feedback_fabricated_behavior.md`
Rule origin: 2026-04-12 Otto proposal fabrication ("you already do those conversations weekly" — false, caught by user).
