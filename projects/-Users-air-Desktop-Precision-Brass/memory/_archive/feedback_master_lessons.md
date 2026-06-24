---
name: Master lessons from Precision Brass email audit (2026-04-12)
description: The four hard-won rules to prevent factual hallucinations across ALL client email/content work. Triggered by shipping "Featured in Forbes" and 5+ mistranscribed names across 7 emails before Timo caught it.
type: feedback
originSessionId: 22f224ca-c858-4442-9136-a3ca2b38f0cf
---
# The 4 Rules (apply to ALL client work — Precision Brass, Creator Conservatory, Robinson's Remedies, any future)

## Rule 1: Auto-transcripts lie. Especially about names.

**Triggering incident:** 2026-04-12. Harrison Ball's masterclass Loom was auto-transcribed with these errors:
- "Willie Mario" → actually Willie Murillo (his mentor, 3x Grammy winner)
- "Matt Jodville" → actually Mat Jodrell
- "Vanessa Perka" → actually Vanessa Perica
- "Remy Labra" → actually Remy Le Boeuf
- Plus 10+ other unverifiable names (Yens Lenderman, Bones Malone, Nadia Nordhouse, etc.)

These errors got copied into brand.md, then into 7+ emails, then shipped to Timo.

**Why:** Any word outside the auto-transcriber's dictionary gets mangled. Musician names, technical terms, brand names, proper nouns are the most likely to fail.

**How to apply:**
- Flag EVERY unusual proper name in any auto-transcript file as "UNVERIFIED — confirm before using"
- Cross-reference against: press kit, LinkedIn, letters of rec, invoices, any primary source
- If not verifiable in 2 min of searching, ASK the user before using in output
- Don't trust a single source (transcript) for unusual facts. Require confirmation.

## Rule 2: Client drafts are drafts, not source of truth

**Triggering incident:** Harrison's Email 1 contained the line "Featured in Forbes" in his sign-off. I treated this as a verified credential and propagated it into 7+ generated emails. Timo later confirmed: not real.

**Why:** Founders often put aspirational claims, placeholders, or outdated info in their own copy. Copying that into new generated content multiplies the error.

**How to apply:**
- Every credential claim in user-provided drafts gets a "verify?" flag on first encounter
- Ask explicitly: "Is [specific credential] real, aspirational, or a placeholder?"
- Never propagate credentials across multiple emails until confirmed
- Build a `credentials-verified.md` for each client. Every claim must have a source listed.

## Rule 3: Separate sales prospects from paying customers

**Triggering incident:** Mixed Precision Brass sales call transcripts (people on discovery calls, many never enrolled) with YouTube testimonials (actual paying students with results). Generated emails that implied prospects were students, attributing fabricated outcomes.

**Why:** Pain data and proof data come from different populations. The reader needs to see themselves in the pain (prospect), then see proof the problem is solved (customer). Blending them creates lies of omission.

**How to apply:**
- Every voice-bank file must have TWO clearly labeled sections: PROSPECTS (sales calls) and CUSTOMERS (testimonials with verified outcomes)
- Before using a name in an email: verify which section they're in
- Prospects = HOOK only. No outcome claims. Use language like "[Name] told me on our first call..."
- Customers = PROOF. Can claim outcomes they documented on camera.
- In email drafts, annotate inline: "Karen (prospect)" or "Mike BMW (student)" until final edit

## Rule 4: Unusual → Verify. Always.

**Triggering pattern:** Every time a claim made me pause even briefly ("huh, Bones Malone?"), I should have verified instead of trusting.

**Why:** The instinct that something's odd IS the signal. Ignoring it is how hallucinations ship.

**How to apply:**
- Cold-read every output before shipping. Any claim that triggers "hmm, is that right?" → verify or cut
- For emails/content with 5+ factual claims, do a final pass that asks "could this get us sued / embarrassed if wrong?"
- Better to delay a ship by 10 min than retract 7 emails

---

# UNIVERSAL APPLICATION TO ALL CLIENT WORK

Apply across: Precision Brass (/email), Creator Conservatory (/cc-email), Robinson's Remedies (/rr-email), any future client system.

Build into every client workspace:
1. `context/verified-facts.md` — every factual claim with its source and verification status
2. `context/unverified-flags.md` — claims pulled from transcripts that need user confirmation
3. Voice-bank files structured as PROSPECTS / CUSTOMERS sections, never blended
4. Skill-level review checklist that asks "is every name labeled? is every outcome sourced?"

---

# THE 7 PRE-FLIGHT SAFEGUARDS (prevent errors before they start — added 2026-04-12 round 2)

The 4 rules above catch errors DURING work. These 7 safeguards prevent errors BEFORE work begins.

## Safeguard 1: Source-Inventory Gate
Before writing a single word of client content, output 3 bullets:
- **Primary source** for credentials/claims (press kit? transcript? client draft?)
- **Trust level** of each context file loaded
- **Unknowns** to confirm with user BEFORE writing

If I can't name the primary source for a claim, STOP and ask.

## Safeguard 2: Claim-Level Tagging in All Context Files
Every claim in `brand.md`, `voice-bank.md`, etc. gets tagged:
- `[VERIFIED: source-date]`
- `[USER-PROVIDED]` (internal-only, don't publish)
- `[UNVERIFIED — auto-transcript]`
- `[ASPIRATIONAL — client draft]`

Untagged claim = minimum trust until tagged.

## Safeguard 3: File Provenance Frontmatter
Every context file gets frontmatter with source + verified-by + trust-level + last-audit. Read frontmatter FIRST, content second. Low/missing trust = skeptical treatment.

## Safeguard 4: Pre-Ship Cold-Read (mandatory)
Before any content leaves the workspace, pretend I'm a skeptical stranger:
- Every proper name → can I verify in 30 sec?
- Every credential → source?
- Every outcome claim → which verified customer?
- Every quote → which population (prospect/customer)?

Hesitate on any = don't ship. Verify or cut.

## Safeguard 5: Question Budget (reframe)
Clarifying questions are FEATURES, not failures. Template: "Before I write this, I need to confirm: (a) X? (b) Y?" One 5-second question beats retracting 7 emails.

## Safeguard 6: Output Ledger (per-session)
Track facts claimed externally this session. When the same fact appears in second output, the ledger prevents silent propagation — ask Timo once, not 7 times.

## Safeguard 7: Systemic Correction (not local)
When Timo catches an error, ask: "What CLASS of error is this? Where else does it appear?" Audit ALL files for the class before generating next output. Do the audit FIRST.

## Safeguard 9: Engagement ≠ Conversion (from Richard email field test 2026-04-12)

**Triggering incident:** Richard identity-loss email got high engagement (opens, reads, replies per Harrison) and ZERO conversions to booked calls.

**Why it happened:** Emotional resonance was strong (hook, story, arc all landed) but the close failed:
- Solution was described abstractly instead of linking to Harrison's own video
- PS proof stack (Brad, range fix in 11 min) didn't match the story arc (Richard, identity loss)
- CTA pivoted from heart-level to technical — tonal whiplash
- Final line left reader in the wound instead of pulling forward
- Only one commitment level offered (book a call) — no video-first option for the just-engaged

**Apply to ALL client content (email, blog, social, ads):**

1. **Measure conversion, not engagement.** Opens, likes, replies are vanity if they don't move to action. Track only what maps to revenue.
2. **Show, don't describe.** When possible, link to the creator's own demonstration (YouTube video, case study) rather than summarizing the method yourself.
3. **Match proof to pain.** A testimonial must feature a customer with the SAME arc as the prospect you hooked. Mismatched proof dilutes belief.
4. **Tonal continuity from hook to CTA.** If the body is emotional, the CTA must bridge emotionally. Technical CTA on emotional body = bounce.
5. **Close with momentum.** Final line faces forward, names the next action, doesn't reflect on the feeling.
6. **Two-step CTA for emotional content.** Low-friction first step (watch/read) + high-friction second step (call/buy) serves different readiness levels.
7. **Bridge paragraph between pain and CTA.** Explicitly say "here's why this is solvable for YOU" — don't assume the reader connects their pain to your offer.

---

## Safeguard 8: Source Fidelity for Students AND Solutions

**Two inseparable sub-rules added 2026-04-12 round 3:**

### 8a. Student claims come from the TESTIMONIAL DATABASE, nothing else.
If an email, ad, or any content references a "student," "client," "program member" with a specific outcome, that person MUST be in the verified testimonial database:
- YouTube testimonials: Benny, Hannah, Mike BMW, Sharon, Trevor/Joville, Tony, John (jazz), Mike (4-month), unnamed female student
- Masterclass documented results: Brad, Rachel, Yens (masterclass — NOT the unverified "Yens Lenderman"), Lee, Brandon, Philip

Anyone NOT in this list = NOT a student. Treat them as a prospect (discovery call only) or do not name them.

### 8b. Pain-point SOLUTIONS use Harrison's proven converting language.
When describing how a problem is solved, the explanation must pull from sources that have actually moved people:

1. **YouTube educational videos** that converted to leads — e.g. the embouchure "sim" video, Gravity Breath video, upstream/downstream explainer. Use Harrison's actual language from those videos.
2. **Sales call breakthrough moments** — specifically the diagnostic reframes Harrison made that triggered prospects to shift (e.g. "right method, wrong type of player" → Karen's "no one has ever said that" moment). Use the REFRAME that worked.

Not acceptable for solution descriptions:
- Generic coaching language ("rebuild your foundation")
- My own synthesis of the method
- Paraphrased concepts that drop specificity

**Every solution claim in an email must trace back to either (a) a YouTube video Harrison published, or (b) a documented sales call breakthrough. If neither, don't write it.**

**Practical application:** Before writing any solution section, ask:
- Where in Harrison's content has he taught this specific fix?
- What exact phrase did he use that made it click?
- Did I pull the phrase or did I invent it?

If I invented it, replace with Harrison's version or cut.

---

# PRE-FLIGHT CHECKLIST (run before every client content task)

Copy-paste at the start of every content generation:

```
PRE-FLIGHT CHECK:
□ Primary source for credentials: ___
□ Prospects vs customers distinction in voice-bank: labeled?
□ Unusual proper names cross-referenced: yes/flagged
□ Client draft credentials verified (or asked): ___
□ Unknowns to confirm BEFORE writing: ___
```

If any checkbox fails, pause and address before writing.

---

# WHEN TO EXTEND THIS FILE

Every new class of error = new rule or safeguard. Do not delete lessons, only extend. Track growth: the file should get LONGER over time, not shorter.

Expected future extensions (hypotheses):
- Staleness checks on old context files
- Legal/compliance claim review (FDA/FTC for health, licensing for music)
- Voice drift when clients evolve their public voice
