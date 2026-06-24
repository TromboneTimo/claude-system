---
name: Contract Signature Block Format
description: Canonical signature/fillable-form layout for all Timo LLC contracts and proposals. Applies to every new contract unless Timo says otherwise.
type: feedback
originSessionId: 6c984749-81c4-487c-99e7-abd3bbf0b11e
---
Every Timo LLC contract's signature block uses a parallel two-column layout with 5 labeled fields per side. Labels go ABOVE the field, not below. No "Business Address" or "Printed Name / Legal Business" labels.

**Client block (all 5 fields blank):**
1. Business Name
2. Full Name
3. Email Address
4. Signature
5. Date Signed

**Timo LLC block (address as subtitle, 3 fields pre-filled, 2 blank):**
- Subtitle: `900 East Pecan Street, Ste 300, Pflugerville, TX 78660`
- Business Name: `Timo LLC`
- Full Name: `Timothy Maines`
- Email Address: `TromboneTimoLLC@gmail.com`
- Signature: blank
- Date Signed: blank

**No AcroForm injection. No interactive PDF fields.** Timo signs and routes contracts through DocuSign, which overlays its own fillable fields on top of the static PDF. Adding AcroForm widgets via reportlab/pypdf is dead work and creates a conflicting interactive layer underneath DocuSign's. Render the PDF as a clean static document with visible labeled underlines. That's the deliverable. The legacy `scripts/add_acroform_fields.py` was deleted on 2026-04-23.

**HTML rules.** Use `<input type="text">` for the visible field rows so each field renders as a labeled blank line in the printed PDF. Do NOT use `type="email"` (Chrome renders a thicker bottom border for email inputs, which breaks visual parity). Do NOT set `placeholder` attributes (placeholder text bakes into the PDF and reads as filled-in content to the client).

**Why:** Two corrections from Timo on 2026-04-23. (1) Original v1 of the Harrisson proposal shipped with mismatched field labels and an inconsistent email-input border. (2) The first fix added AcroForm widgets, which Timo did not ask for and does not need because his signature flow is DocuSign. Same turn, he flagged that the client side has no place to enter their business name (Timo's "Timo LLC" is in the block heading; the client has no parallel slot).

**How to apply:** Bake into every future contract from the start. This is now the default for the proposal-writer skill (codified in `references/harrisson-ball-reference.md`). When drafting a new contract: produce HTML with the parallel 5-field structure, render to PDF via Chrome `--print-to-pdf`. Stop there. Do not run any AcroForm overlay step. Hand the static PDF to Timo for DocuSign upload.
