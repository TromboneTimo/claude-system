---
name: Proposal Render Gate. MD-Only Iteration Until Sign-Off
description: PDF rendering on every micro-edit is the biggest token sink in the proposal-writer skill. Render only when Timo says "approve / render / ship / send / final".
type: feedback
originSessionId: 3860a3a8-590f-4199-8724-16d7b6a081e5
---
PDF rendering for proposals is a SIGN-OFF action, not an iteration action. During the entire draft + correction loop, the workflow is MD-only.

## Hard rules

**During iteration:**
- Write the first draft to `output/proposals/{client-slug}/{client-slug}-proposal-{YYYY-MM-DD}.md` as the SINGLE source of truth (one Write call)
- All corrections happen via Edit on the `.md` file (one targeted Edit per change, never a full Write rewrite)
- Show changed sections as text in chat for review (zero file-touch is cheapest)
- DO NOT run Chrome headless
- DO NOT run pdftoppm
- DO NOT Read PNG pages
- DO NOT regenerate the HTML
- DO NOT touch the PDF in either location

**At the render gate (when Timo says one of the trigger words):**
- Generate HTML from MD using the canonical CSS template
- Render PDF via Chrome headless
- Dual-save (Downloads + project folder) per `feedback_proposal_pdf_dual_save.md`
- Convert key pages (cover, pricing, signature) to PNG and Read for visual QA
- Open the PDF in Preview

**Render-gate trigger words (and only these):** "approve" / "render" / "render this" / "render final" / "ship" / "ship it" / "send" / "send to client" / "ready" / "ready for DocuSign" / "looks good, render" / "go ahead and render" / "finalize". Anything else = stay in MD-only iteration mode.

**After render, if Timo gives more corrections:** return to MD-only iteration. Do NOT re-render after every micro-edit. Wait for the next trigger word before re-rendering.

## Why

Each render-and-screenshot cycle costs roughly 50-100K input tokens (PNG Reads alone) plus Chrome wall time plus full-file regeneration tokens. A 6-iteration session that renders on every edit burns roughly 6x what an MD-only iteration with one final render would cost.

**Canonical incident:** 2026-04-27 Robinson's Remedies session. 6 PDF renders, 6 visual QAs, 6 full HTML rewrites for a single proposal. Research (Perplexity + NotebookLM, NotebookLM ID `40bc178b-5ee4-4f1f-98aa-7432d9abae03`) confirmed this is the highest-leverage workflow change. Every legal-tech platform (PandaDoc, Juro, Conga, DocuSign Gen) follows the same pattern: drafts and reviews in lightweight form; PDF assembly only at the e-sign stage.

## How to apply

Bake into proposal-writer SKILL.md as Layer 0 of the post-draft enforcement gate. The render-gate trigger words list is the contract: any input that doesn't match a trigger word means stay in MD-only mode.

For ANY future skill that involves a "draft + iterate + render to expensive format" pattern (slide decks, PDFs, HTML pages, images), apply the same gate: cheap iteration mode → explicit sign-off → expensive render. Never render after every edit.
