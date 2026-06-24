---
name: Proposal Default Pattern. Harrisson, Not Artifact
description: For any client proposal going forward, use the Harrisson Ball 6-section lean signable-contract pattern as the default. The 11-section Artifact AI enterprise-pitch pattern is opt-in only.
type: feedback
originSessionId: bb11f5ff-044e-47bd-9a9d-ecc9b0a26bf5
---
Timo's canonical proposal structure as of 2026-04-21 is the Harrisson Ball lean contract (6 sections), not the Artifact AI enterprise pitch (11 sections).

**Why:** Timo's actual clients are known individuals and small businesses. They sign contracts, they don't need 15-page pitch decks with Competitive Context and Performance Snapshot framing sections. The extra depth reads as agency bloat to clients who already know why they're hiring him. The Harrisson pattern was built iteratively over a long session, and Timo explicitly locked it in at the end as the template for all future proposals.

**How to apply:** When the user says "draft a proposal" or "write a contract for X," default to the `references/harrisson-ball-reference.md` pattern:

1. What Was Requested
2. Proposed Systems (with inline mockup images + Mermaid diagrams)
3. Delivery Timeline
4. Engagement Structure & Pricing (consolidated chart at END of the doc)
5. Protections & Terms (plain-English summary at top, then legal subsections: ownership/handover, dispute resolution, governing law/venue/severability)
6. Next Steps

Plus: Replacement-of-prior-agreement block (if applicable) + Signature block with sender address embedded (not fillable).

**Patterns to replicate:**
- Hybrid pricing (commission % + flat fee) when the engagement has both build and performance components.
- 40/60 build-and-prove payment structure (40% upfront, 60% gated on client sign-off that it's working).
- 90-day performance guarantee with pro-rated refund of Phase 1.
- Commission term + tail (Timo-default: 6-month term + 180-day tail).
- California-specific legal language (Cal. Labor Code section 2870 carve-out, CCPA service-provider terms) when client is in CA.
- AAA Commercial Arbitration seated in Los Angeles County for CA clients.
- Ownership / handover clause: work-for-hire + explicit assignment, third-party accounts in client's name from day one, exit deliverables within 30 days, paid transition at stated hourly rate.
- Plain-English summary block at top of Protections section written at 5th-grade reading level.

**Upgrade path to the Artifact pattern:** Only when the user explicitly says "enterprise pitch deck," "full discovery proposal," or the client has not yet committed and needs framing depth. Otherwise Harrisson pattern wins.

**Hard bans that carry over from earlier feedback:**
- No "At a glance" / exec summary box at the top (readability canon violation).
- No "In short:" TL;DR leaders per section.
- No "Before you sign" block (readability canon violation).
- No fabricated taglines, references, or dollar figures.
- No em dashes anywhere (hook-enforced).
- **Pricing never surfaces before the Engagement Structure & Pricing section. ZERO dollar figures in earlier sections. Applies to ROI blocks, system descriptions, testimonials, everything. 2026-04-21 violation: I put "$5,000 investment" in a System 2 ROI block in Section 2. Banned.**
- **ROI blocks never mention commission math, commission rates, or any pricing number. Frame ROI purely in terms of time saved, output multiplied, feedback loop speed, and qualitative sales-velocity benefits. The reader already knows the value of their own time; do not calculate commission offsets for them. 2026-04-21 violation: I wrote "one additional $6,800 sale per month nets Harrisson $5,780 after 15% commission" in a System 1 ROI block. Banned.**
- **Visible deductions stay visible. Discounts, credits, and rollovers favorable to the client must appear as their own line item in the pricing table, not collapsed into a notes column or summary line. The client's eye should land on the deduction the same way it lands on the subtotal. 2026-04-22 violation: I collapsed the $1,500 coaching credit into a Notes column. Timo lost his shit. Restored as a visible row.**

**Validator script already enforces these structural bans.** Run `python3 .claude/skills/proposal-writer/scripts/validate_structure.py <path>` on every draft before showing the user.
