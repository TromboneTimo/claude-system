# /rr-email -- Robinson's Remedies Email System

## Description
Generates on-brand emails for Robinson's Remedies e-commerce. Kenny Robinson's voice. Wax-free science. Anti-drugstore positioning. Every CTA includes "Available on Amazon Prime."

## ANTI-HALLUCINATION PROTOCOL (MANDATORY - added 2026-04-12 after Precision Brass audit)

See full audit: `~/Desktop/Timo LLC/creator-conservatory/research/precision-brass-email-system-redesign-2026-04-12.md`

### Rule 1: Verify all proper names and credentials
Customer reviews, podcast quotes, influencer mentions — any proper name pulled from a transcript must be cross-referenced against an authoritative source before use.

### Rule 2: Customers ≠ Prospects ≠ Reviewers
- Amazon reviewers (real customers with verified purchases) = PROOF material
- Survey respondents / quiz takers (prospects) = HOOK material
- NEVER conflate them. Don't claim a reviewer was a survey taker or vice versa.

### Rule 3: Kenny's drafts are drafts
Any credential in Kenny's copy ("Featured in X", "MD-approved") needs verification. Precision Brass precedent: "Featured in Forbes" was in the founder's own draft and shipped in 7 emails before flagged as fake.

### Rule 4: Medical/health claims need citation
FDA/FTC watch e-commerce health copy. Unverified efficacy claims are legal risk, not just hallucination risk. Cite or cut.

## Activation
User says: `/rr-email`, or any request about Robinson's Remedies email marketing

## Project Location
`~/Desktop/Robinsons Remedies/`

## CRITICAL: Context Load Order (Priority Matters)

### Priority 1: VOICE (load first, always)
1. `email-system/voice-spec.md` -- Hard numbers, forbidden words, quality gate. THE LAW.
2. `email-system/annotated-reference-emails.md` -- 5 annotated examples. Study before writing.

### Priority 2: STRATEGY (load second)
3. `email-system/strategy/strategy-memo.md` -- What's working right now.
4. `email-system/strategy/angle-scores.md` -- Which angle to pick. Cooldowns.
5. `email-system/strategy/creative-ledger.md` -- What's been sent recently.

### Priority 3: BRAND DATA (load third)
6. `context/brand.md` -- Kenny's story, mission, key people.
7. `context/products.md` -- All 5 products with ingredients and mechanisms.
8. `context/audience.md` -- Musicians, cold sore sufferers, general consumers.
9. `context/competitors.md` -- Abreva, Herpecin-L, ChapStick positioning.

### Priority 4: PROOF POINTS (load for social proof emails)
10. `references/content-examples.md` -- Dye test, burn test, endorsers, headline patterns.

### DO NOT LOAD for email generation:
- Blog SOP, social SOP, creative SOP (wrong context)
- Landing page HTML files (too heavy)
- Research reports (reference only, not generation context)

## Sub-Commands

| Command | What It Does |
|---------|-------------|
| `/rr-email generate` | Write one email. Full flow below. |
| `/rr-email sequence [type]` | Build sequence: welcome, nurture, cart-abandon, win-back, launch |
| `/rr-email product [name]` | Generate product-specific email for: lightning-stick, endurance-cream, recovery-stick, lip-quench, skin-repair |
| `/rr-email angle-status` | Show angle scores, cooldowns, availability |

## /rr-email generate -- Flow

### Step 1: Load Priority 1
Read voice-spec.md. Read annotated-reference-emails.md. Internalize the voice. Study the examples.

### Step 2: Load Priority 2
Read strategy memo. Read angle scores + creative ledger. Determine WHAT to write about.

### Step 3: Select angle + framework
- Filter by cooldown (14 days same angle, 4 days same product, 3 days same category)
- Rank by score
- Select framework:
  - Product angle -> Product Email template
  - Educational angle -> Educational Email template
  - Founder story -> Founder Story template
  - Social proof -> Social Proof template

### Step 4: Load Priority 3
Read brand.md for Kenny's story. Read products.md for ingredient specifics. Read audience.md for segment matching.

### Step 5: Write
Follow the structure from voice-spec.md. Use the matching template from the annotated examples.

### Step 6: Quality Gate
1. Sounds like Kenny, not a marketing department?
2. Opens with story/problem, not product pitch?
3. Names at least 1 ingredient + mechanism?
4. CTA followed by "Available on Amazon Prime"?
5. Zero em dashes, zero emoji?
6. No "may help" hedging?
7. No red in body text?
8. Under 500 words?
9. Subject under 50 chars?

**ANY failure = regenerate.**

### Step 7: Save
- Save to `email-system/output/emails/[YYYY-MM-DD]-[product]-[angle].md`
- Log to `email-system/strategy/creative-ledger.md`

## Negative Examples

### GENERIC E-COMMERCE (never do this):
```
Hey there! Ready to upgrade your lip care routine? Our all-natural, 
wax-free formula is specially designed to give you the moisture your 
lips deserve. Shop now and experience the difference!
```
**Why garbage:** "Hey there" = no name. "Upgrade your lip care routine" = cliche. "Specially designed" = empty. "Experience the difference" = means nothing. No story. No ingredient. No Kenny.

### THE RR WAY:
```
Last week a trumpet player told me he puts ChapStick on before every 
gig. Then wipes it off before he plays.

That cycle is the whole problem with wax-based lip balm.
```
**Why this works:** Specific person. Specific action. Relatable. The reader sees themselves. No product name until the solution paragraph.

## Email Types for E-commerce

| Type | % of Sends | Goal | CTA |
|------|-----------|------|-----|
| Product | 40% | Drive purchase | SHOP [PRODUCT] + Amazon Prime |
| Educational | 30% | Build trust, demonstrate expertise | Soft (blog link or YouTube) |
| Founder Story | 15% | Emotional connection, brand loyalty | PS only (product link) |
| Social Proof | 15% | Credibility, overcome skepticism | SHOP + Amazon Prime |

## Segment-Specific Rules

| Segment | Tone Shift | Product Focus | Angles to Prioritize |
|---------|-----------|---------------|---------------------|
| Musicians | Peer-to-peer. Use: chops, embouchure, gig, mouthpiece. | Endurance Cream + Recovery Stick | EC-01, EC-02, RS-01, ED-06 |
| Cold Sore | Empathetic. They've been let down. Earn trust with science. | Lightning Stick | LS-01, LS-02, ED-02, ED-03 |
| General | Accessible. No jargon. Focus on the dependency cycle. | Lip Quench | LQ-01, LQ-02, ED-05, ED-01 |


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
