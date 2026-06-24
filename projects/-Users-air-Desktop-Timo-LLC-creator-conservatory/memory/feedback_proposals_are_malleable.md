---
name: Proposals Are Malleable. Never Copy Reference Assumptions
description: Every proposal is custom to the client. Never carry forward the previous client's jurisdiction, pricing model, term length, component count, or industry-specific clauses without confirming.
type: feedback
originSessionId: 3860a3a8-590f-4199-8724-16d7b6a081e5
---
The canonical reference (Harrisson, Artifact, etc.) is a STRUCTURE template, not a content template. Each new client requires explicit re-interrogation of every assumption the reference encodes.

**Identify the contracting parties correctly.** Contracts are between LEGAL ENTITIES, not individuals. If the client is a business (LLC, Inc., DBA), the party is the BUSINESS NAME, not the founder's personal name. The founder signs as authorized representative inside the signature block, but the document refers to the business throughout (header, plain-English summary, protection clauses). Personal names stay only in CONTENT references (e.g., "Kenny's stories," "Kenny is the face of the brand"). 2026-04-25 Robinson's Remedies correction: I addressed Kenny as the contracting party throughout. The contract is Timo LLC ↔ Robinson's Remedies. Kenny just signs for Robinson's.

**Things that MUST NOT be copy-pasted from the reference:**
- **Governing law / jurisdiction.** Harrisson's contract uses California law because that's where Harrisson is based, NOT because Timo is California. Default to Texas (Timo LLC's home state, Pflugerville/Travis County) unless the client's location dictates otherwise. Confirm with Timo before using any state.
- **Pricing structure.** Commission vs flat fee vs hybrid vs per-unit varies completely per engagement. Never assume Harrisson's commission model fits.
- **Term length.** Harrisson is 6-month commission term. Robinson's was 30-day pilot. Each client's term is bespoke.
- **Compliance clauses.** CCPA references make sense only if California consumer data is involved. Drop or replace based on client jurisdiction (e.g., Texas Data Privacy and Security Act for TX-based clients, or generalize the clause).
- **Cal Labor Code § 2870.** California-specific. Drop entirely for non-CA contracts. Not needed for contractor work in most states anyway.
- **Component count.** Harrisson had 2 systems. Robinson's had 5 components. Match the actual scope, not the reference's count.
- **Replacement-of-prior-agreement block.** Only include if there's a real prior signed agreement to supersede.
- **Per-video / per-unit prices.** Don't assume $250/video transfers. Confirm pricing per client.

**Why:** Timo flagged 2026-04-25 that I assumed California legal language for Robinson's because I copied Harrisson's contract structure verbatim. Each client is malleable. The reference gives the SHAPE; the client gives the SUBSTANCE. Mixing them ships hallucinated assumptions.

**How to apply:** Before drafting, list every reference-encoded assumption (jurisdiction, term, pricing model, compliance) and either confirm it applies OR ask Timo. The pre-draft confirmation gate already covers pricing and durations. Add: jurisdiction, applicable law, compliance frameworks. If Timo doesn't answer a jurisdictional question, default to Texas (Timo LLC's home) and FLAG it explicitly in the response so he can override in two seconds.

**Mental model.** Each new proposal is a blank document with a known structure. Fill the structure with this client's data, not the previous client's data.
