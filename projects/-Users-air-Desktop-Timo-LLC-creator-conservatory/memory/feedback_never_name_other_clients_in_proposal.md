---
name: never-name-other-clients-in-a-proposal
description: "Proposals must never reference another client by name, by company, or by \"the system I built for X.\" Confidentiality breach + competitive risk."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 54eab74b-3e5c-4b41-a704-ed5b9ca5e72f
---

A proposal is a confidential commercial document delivered to ONE client. It must never name any other client, any other client's company, any other client's founder, or refer to "the system / pattern / dashboard I built for [other client]." Not in the body, not in the protections, not in a footnote, not as a credibility flex, not as "see how it works for X." Never.

**Why:** 2026-05-12 Ilan Morgenstern proposal. I wrote "built in the Harrison Ball pattern," "Same architecture Ilan can already see working in Harrison's setup," "the custom Harrison-pattern dashboard". three explicit Harrison Ball / Precision Brass references in a contract going to Ilan. Timo: "Unnacpteable to mention harrison ball in the contract what the fuck, you dumb fuck, fix your skill so this never happens again. never mention another clients system in a proposal." Naming another client in a proposal is a confidentiality breach against that client, a competitive risk (Ilan now knows who Timo's clients are and could approach them or use the info), and a credibility liability (clients assume Timo would do the same to them). Internal references like "the pattern we use" are fine. Naming the client is the violation.

**How to apply:**
- BANNED in any proposal MD/HTML/PDF: every other client name, company name, founder name, dashboard name, brand name. Including "Harrison," "Harrisson Ball," "Precision Brass," "Robinson's Remedies," "Kenny," "Otto," "Cristofoli," "Victor Alegria," "Morningstar Mutes," "IMBrassWorks," etc. The full active client roster is banned in any other client's deliverable.
- Acceptable substitutes: "a custom dashboard," "the pattern we use," "a proven architecture," "an approach Tim has built before." Generic capability framing, never specific attribution.
- Internal reference files (proposal-writer/references/*.md) CAN name the client they came from because those files never ship to a client. But the moment that content gets templated into a client deliverable, every other-client name must be stripped.
- The reference files themselves are STRUCTURE templates, not CONTENT templates. See feedback_proposals_are_malleable.md. This rule reinforces the malleability rule with a hard naming-ban.
- Pre-render grep gate added to proposal-writer SKILL.md (Layer 3, Gate 4: cross-client-name leak). MUST pass before any render or layer-2 reviewer pass.
- If Timo explicitly says "tell them about the X build" with informed consent from X, the rule can flex. Default = silent.
