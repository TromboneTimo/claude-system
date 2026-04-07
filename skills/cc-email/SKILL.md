# /cc-email -- Creator Conservatory Email System

## Description
Generates emails for Tim Maines' Creator Conservatory coaching business. Tim's voice: direct, irreverent, proof-heavy, anti-guru. Musicians who want to grow online.

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
