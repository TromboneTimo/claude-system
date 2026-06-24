---
name: Timo LLC Address Is Pflugerville Not Austin
description: Timo LLC is registered at 900 East Pecan Street, Ste 300, Pflugerville, TX 78660. Never write "Austin, Texas" on any contract, proposal, footer, or signature block.
type: reference
originSessionId: 44a98549-51b8-4912-8651-9ce2b92f8852
---
The canonical Timo LLC address on every contract, proposal footer, signature block, and legal document:

**Timo LLC**
**900 East Pecan Street, Ste 300**
**Pflugerville, TX 78660, USA**

NOT Austin, TX. Pflugerville is the registered LLC home jurisdiction.

**Canonical business contact email:** `timo@trombonetimollc.com`. Use this on legal pages, contact lines, proposal footers, and signature blocks. Confirmed by Timo 2026-06-07 (Creator Conservatory FB funnel privacy policy + terms of service). Do NOT use his personal gmail on public-facing documents.

**Why this rule exists.** 2026-05-09 ISO proposal: I propagated "Austin, Texas, USA" from a stale source MD into the rendered HTML footer + signature block without cross-checking against the canonical Harrisson Ball reference (which has the correct Pflugerville address embedded in the signature block). Timo caught it post-render. Address mismatches on signed contracts are jurisdictionally meaningful (governing-law clause references Texas; venue clause references Travis County). Never write a city without confirming.

**How to apply.**
1. When drafting any signed legal document, the Timo LLC address line is `900 East Pecan Street, Ste 300, Pflugerville, TX 78660, USA`.
2. The signature block in the Harrisson Ball canonical reference is the source of truth. Cross-check before any footer / signature insertion.
3. If a source MD has "Austin, Texas" in it, that's a stale value. Fix at the MD layer, do not propagate.
4. Every render-gate run includes a grep for `Austin` against the final HTML and PDF. Zero hits required before declaring done.

**Generalization.** This is an instance of the broader rule: cross-check entity / address / credential data against canonical references before propagating from any single source. Mirrors the "verify before propagate" pattern in `feedback_master_lessons.md`.
