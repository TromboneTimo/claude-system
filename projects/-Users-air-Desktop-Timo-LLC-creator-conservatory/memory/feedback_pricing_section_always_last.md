---
name: Pricing Rules. Section Order, Line Items, Never In Header
description: Canonical rules for pricing in every Timo LLC proposal. Position, format, and what's banned everywhere else in the document.
type: feedback
originSessionId: 3860a3a8-590f-4199-8724-16d7b6a081e5
---
Three rules govern pricing in every Timo LLC proposal. All three are non-negotiable.

## Rule 1. Section order

The pricing section appears AFTER the value-build sections and BEFORE Next Steps. Protections/Ownership/Handover come LAST in the document, after Next Steps, as the legal/safety-net layer.

Canonical order:

1. What Was Requested
2. Proposed Systems
3. Delivery Timeline
4. **Engagement Structure & Pricing** (after value-build, before Next Steps)
5. Next Steps
6. Protections & Terms (Ownership, Handover, Client Protections, Dispute Resolution, Governing Law). LAST in document.
7. Signature

**Why:** Pricing as the climax of the value-build means by the time the client reaches the number, every preceding section has been justifying it. Next Steps closes the persuasion arc with action. Protections live at the back like a contract appendix because they're the legal layer, not the persuasion layer.

## Rule 2. Line-item pricing per deliverable. Never lump-sum.

Every component / system / deliverable in the proposal gets its own price line. Never collapse multiple components into a single line like "$1,750 = Components 1, 2, 4, 5." That hides what the client is buying and triggers "what am I actually paying for?" friction.

Pricing table format: one row per component. Subtotal + total at the bottom. Each row maps directly to a component header in Section 2.

**Why:** Timo flagged 2026-04-25 that I lumped 4 components into a single $1,750 line. Hides the value, looks lazy, makes the client question what's in the bucket. Line-item every deliverable so the client can see the math and feel the depth.

## Rule 3. Price NEVER appears outside the pricing section.

Price, dollar amounts, "$X flat," or any pricing language must NOT appear in:
- The header / title / subtitle of the document
- Section 1 (What Was Requested)
- Section 2 (Proposed Systems). Components describe scope only, no per-component price callouts.
- Delivery Timeline
- Sub-headers anywhere outside Section 4
- The signature intro line

The first time the client encounters a number is in Section 4 (Engagement Structure & Pricing). Period.

**Why:** Timo flagged 2026-04-25 that "$2,500 Flat" in the document subtitle leaked the price before the value-build. Anchoring on price kills the persuasion arc. The reader should absorb the scope, the systems, and the timeline before encountering cost. The header sells the engagement, not the number.

## Rule 4. When 40/60 (or any phased) payment is in play, the FIRST dollar amount in the pricing section must be the upfront/Phase-1 number. Never lead with totals.

If the deal has a phased payment (40/60 build-and-prove, 50/50, milestone-based), the reader's first dollar number in Section 4 must be the upfront/kickoff amount. Never the total. Never the system-fee total. Never any line that sums everything up. Lead with what the client pays on signature, then later phases, then total at the END as a sanity-check sum.

**Why:** Timo flagged 2026-04-28 that I had restructured the Payment subsection to lead with day-1 ($3,550) but left a "One-time fees" table at the TOP of Section 4 that led with the $6,250 total. The Payment subsection was correct; the section-level structure was not. Reader's first dollar number was the total, which is the exact anchor we don't want.

**How to apply:** Before declaring done, READ Section 4 top-to-bottom and identify the FIRST dollar number a reader encounters. If it's the total or any sum-line, restructure. The first number must be the upfront/kickoff. If you restructured one subsection, audit the WHOLE section, not just the part you touched. Scoped fixes leak.

## How to apply

Before declaring any proposal draft done, run this check:
1. **Section order check.** Pricing is Section 4 of 6 (or 5 of 7 with replacement-of-prior-agreement block). Protections is the last section before signature.
2. **Line-item check.** The pricing table has one row per component. No row covers more than one component.
3. **Price-leak grep.** `grep -E '\$[0-9]|flat|free|included' draft.html` should return matches ONLY inside the pricing section (Section 4) and the signature intro. Any hit in the header, subtitle, scope section, or systems section = FAIL. Fix before showing draft.
4. **Phased-payment order check.** If the deal has a 40/60 (or similar) split, READ Section 4 top-to-bottom. The FIRST dollar number must be the upfront/kickoff amount, NOT the total. If you fixed one subsection, audit the entire section for the rule.

This rule supersedes any conflict with the canonical reference (Harrisson, Artifact). The reference's structure is a starting point. These four rules win.
