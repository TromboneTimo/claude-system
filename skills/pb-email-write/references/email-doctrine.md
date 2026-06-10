# Email Doctrine: Strategy + CTA Economics (canonized 2026-06-10)

Synthesized from the 18-winner corpus (AC list 13, ranked by unique clicks), the 314-email swipe file (Ed Lawrence + Dimitri Fantini), and 14 dated Timo/Harrison feedback corrections.

## PRECEDENCE (read first)

- **This file governs strategy and CTA economics (the WHAT).**
- **`reader-facing-playbook.md` governs voice and POV (the HOW)** and wins on any voice question.
- **`ed-style-and-revision-lessons.md` is the default structure model.**
- **`email-beat-cloning-method.md` is the archetype library** (lives at `~/.claude/skills/pb-email/references/email-beat-cloning-method.md`).
- On conflict: most recent dated Timo/Harrison feedback wins, then this doctrine for strategy, then the playbook for voice.

## CORE EVIDENCE (why this doctrine exists)

Across the 18 winning broadcasts, open rates are flat (22-33%) while click rates vary 6x. Subject lines are NOT the lever. **The lever is what is behind the click.**

- Top 5 of 7 winners = a **deadline-bound free asset** (replay gone in N days; best performer 3.0% CTR). [EVIDENCE: 18-winner corpus, 2026-06-10 synthesis]
- Bottom 5 = **commitment-first CTAs** (book a call ~0.6% CTR, apply 0.45%). [EVIDENCE: same corpus]
- The one reader-facing-style email ranked 15/18 on clicks. **Voice rules are approved but click-unproven; asset/cycle economics is the proven WHAT.** Voice serves the click engine, it does not replace it.

---

## PHASE 0: PREFLIGHT (checkable, in order)

- [ ] **0.1 Load order** per `feedback_email_voice_load_order.md`: harrison-email-voice.md, the 3 FINAL emails, sequence emails 1-7 ONLY, reader-facing-playbook.md. NEVER load sequence emails 8-12 (Paul template leakage).
- [ ] **0.2 Angle ledger** runs against the LIVE queue (`python3 scripts/email-angle-ledger.py`). Pick an entry mode, mechanism, proof student, and transition that are NOT at cap.
- [ ] **0.3 Ask calendar state AND what dated asset exists this week** (live class, replay window, new routine drop). If none exists, FLAG IT: a deadline asset is the proven click engine [EVIDENCE: top 5/7 winners], and the batch is fighting with one hand tied.

## PHASE 1: ANGLE (one of each, decided before drafting)

- [ ] **1.1 One idea, one pain, one belief, one named technique, one ask.** No stacking.
- [ ] **1.2 Rotate the angle source** across: the 16-objection library, psych-dive hidden problems (`context/prospect-psychology.md`), fresh-ad pain points (`voc/synthesis/fresh-ad-pain-points.md`), proven ad-verbiage beats (`voc/synthesis/ad-winning-verbiage.jsonl`). Not just the 5 reflex tropes.
- [ ] **1.3 Decide the CTA rung BEFORE drafting** (the ask ladder, evidence-ranked):
  1. **Asset-with-deadline** on cycle weeks (replay gone in N days). [EVIDENCE: 3.0% CTR best, top 5/7 winners]
  2. **Masterclass** is the default rung.
  3. **Reply-to-me** about 1x/week.
  4. **Strategy-session / book-a-call** ONLY with true scarcity attached. [EVIDENCE: ~0.6% CTR naked, 0.45% apply; bottom 5 of corpus]

## PHASE 2: SUBJECT (open rates are flat; subjects buy attention, not clicks)

- [ ] **2.1 Speaks to the READER. Never names a student-hero.** [per reader-facing-playbook Section 4]
- [ ] **2.2 Rotate subject modes** across the batch: asset+deadline, two-fragment gut-punch, fear question, number+timeframe, belief-attack, lowercase DM-style for nudges.
- [ ] **2.3 Harrison's approved molds stay canon. The banned list stays banned** (per `feedback_harrison_email_call_20260509.md`: no Forbes, Adams routine, hot air, Milosevic).
- [ ] **2.4 Casing split is deliberate**: lowercase = intimate/nudge; Title Case = asset/value.
- [ ] **2.5 Preheader EXTENDS the open loop, never repeats the subject.**

## PHASE 3: BODY (voice rules per playbook; structure per ed-style)

- [ ] **3.1 Open with a punch at the reader within 3 lines**: cold scene, accusation, mind-read quote, or fear question.
- [ ] **3.2 POV ratios**: reader ("you") is grammatical subject 50-65% of sentences; Harrison "I" 25-40% confession-only; named student max 15%, 2-4 lines, snaps back to "you" within one line.
- [ ] **3.3 Kill ONE named false belief** with a VARIED transition ("the truth nobody told you" is banned as a crutch, per Timo 2026-06-09) and replace it with **ONE specific named Harrison technique** taught well enough the reader can try it tonight (amisha, vertical alignment, tongue arch tar-not-tee, 4 points of contact, wedge breath, place-breathe-play, upstream/downstream, dynamic repetition). [per feedback_email_cite_specific_technique_and_vary_transition]
- [ ] **3.4 One verbatim Harrisson charged line per email** (two-s spelling in all client copy).
- [ ] **3.5 Edge in diagnosis, warm in rescue.** The exoneration unit ("You're not lazy. You've done the work. It's not your fault.") is the proven $60K hinge. Blame the METHOD, never the reader. [EVIDENCE: winner corpus + converter video]
- [ ] **3.6 Rhythm**: paragraphs under ~170 chars, 1-2 sentences, varied; one-line punches at the turn. 350-500 words for teaching emails. **~90-word asset emails and 2-line nudges are legitimate separate formats**, not violations.
- [ ] **3.7 Proof**: verbatim student quote ALONE on its own line at the pivot. Rotate students. Never overstate past the witness's exact words. [per ed-style READ-FULL-SOURCE gate]
- [ ] **3.8 Run the metrics pass EARLY** (words, FRE, I:you, walls), not after five revision rounds.

## PHASE 4: CLOSE (CTA economics, the load-bearing phase)

- [ ] **4.1 One bridge sentence, then ONE conditional imperative hyperlinked-anchor CTA.** Canonical masterclass wording verbatim ("Come watch the free master class where I talk about this in detail" -> precisionbrass.info/webinar-registration-pb) plus `?el=timoemail` when that rung. No raw URLs ever.
- [ ] **4.2 Asset CTAs may add the proven secondary book-call link BELOW** the primary. This is the ONLY sanctioned 2-destination shape. The bridge sentence "if what you hear resonates..." is proven verbatim in winners 1/5/6. [EVIDENCE: winner corpus]
- [ ] **4.3 P.S. lives INSIDE body** (the dashboard drops ps_text at send, per `feedback_email_ps_must_be_in_body.md`), written fresh each time, a second HARDER sell.
- [ ] **4.4 Tagline verbatim where the format carries it** (teaching emails yes; 2-line nudges may skip).

## PHASE 5: BATCH + SHIP

Batch diversity (all checkable against the ledger):
- [ ] **5.1** No two adjacent emails share an entry mode.
- [ ] **5.2** Each reflex trope max 1x per batch (use-more-air, it-was-never-you, nobody-ever-told-you, for-years, the-wall, Quick-rant).
- [ ] **5.3** Reframe transitions all different.
- [ ] **5.4** Proof students spread (rotate Brad/Mike/Kay/Heather/Yens/Rachel/Hannah).
- [ ] **5.5** ASK RUNG ROTATED across the batch (the ledger now prints the CTA-rung distribution; check it).
- [ ] **5.6** Link count ~50/50 one-vs-two unique destinations across the batch. [per feedback_link_count_variation]
- [ ] **5.7** P.S. structures all different (no shared template).

Ship gates:
- [ ] **5.8** rhythm-check PASS (`scripts/email-rhythm-check.py`).
- [ ] **5.9** angle-ledger clean (no uncited HEAVY reuse).
- [ ] **5.10** Independent render + judge (agent renders the email and judges it; my self-judgment is out of the loop).
- [ ] **5.11** Verify the ASSEMBLED AC message (campaignMessages -> messages), not proposal fields. [per feedback_email_ps_must_be_in_body]
- [ ] **5.12** WARN the human, never hard-block. The list-allowlist gate is the ONLY hard gate. [per feedback_never_hard_block_user_send]
- [ ] **5.13** Hard bans always: Forbes credential, Adams routine, "hot air", Jeremy Milosevic, placeholders, raw URLs, stranger-name openers, invented results/quotes/scarcity.

---

## STRUCTURAL PLAYS TO ROTATE IN (evidence-tagged)

1. **Monthly live-class launch cycle with replay-deadline emails.** The proven click core. [EVIDENCE: top 5/7 winners, 3.0% CTR best] Status: pending Harrison cadence buy-in; flag it every preflight where no dated asset exists.
2. **Weekly 2-line DM-style nudge.** [EVIDENCE: dimitri Format C, swipe file]
3. **Freed-slot "re:" play**, ONLY when a slot truly freed (invented scarcity is a hard ban).
4. **Audio-version experiment** (offer the email as audio; untested, low cost).
5. **Recurring named segment** (a branded weekly slot readers learn to expect).
6. **Identity-UP labeling and future-pacing** ("you're the player who...", sell identity not technique). [EVIDENCE: psych dive Section 7]
7. **Teacher-loyalty and relational-shame angles** from the psych dive (the embouchure built for your teacher; the section noticing).
