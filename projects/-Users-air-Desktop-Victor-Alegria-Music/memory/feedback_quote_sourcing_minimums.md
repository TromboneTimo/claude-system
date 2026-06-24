---
name: Voice-of-customer quote sourcing minimums for dashboard proposals
description: Every proposal pushed to dashboard MUST include at least one testimonial quote AND one sales call quote. Harrison-quotes need conversion-lens framing.
type: feedback
originSessionId: 96d24bc4-360e-4d3e-b566-fcab2c713a01
---
Standing rule for `pb-ideas-push` and any future proposal-building skill (2026-04-26).

## Minimum sourcing per proposal

Every voc_quotes array MUST include at least:
1. **One quote from a testimonial** (someone who has worked with Harrison and recorded a video testimonial). Sources live in `voc/testimonials/raw/`.
2. **One quote from a sales call** (someone Harrison did a discovery call with, whether or not they signed up). Sources live in `voc/sales-calls/raw/`.
3. Other quotes from YouTube comments, Facebook comments, DMs, and similar are encouraged but supplementary, not required.

If a proposal lacks a testimonial OR sales call quote, do not push it. Pull a real quote from the corpus first.

## Harrison-quote conversion-lens rule

If a proposal includes a quote where Harrison himself is the speaker (his own ad copy, his own video transcript, his own DM), the source attribution MUST do two things:
1. State the source (which ad, which video, which post).
2. Explain WHY that language is causing people to convert. What's the mechanism? What's the audience reaction it triggers? What's the permission it grants? What's the reframe it lands?

Without the conversion lens, a Harrison quote is just self-citation and adds no signal to the proposal. With the lens, it shows the proposal-writer understands what makes the language work.

**Bad example:** "Harrison Ball's own Facebook ad copy. Hook line of currently-performing ads."

**Good example:** "Harrison Ball's own Facebook ad copy. The reason this exact framing converts on cold traffic: it gives comeback players permission to stop blaming their own body for damage a teacher caused. That permission is the prerequisite for being open to a new program."

## Why this matters

Proposals without testimonial quotes lack proof of the after-state (what life looks like once Harrison fixes the problem). Proposals without sales-call quotes lack proof that this wound shows up in actual buying conversations. Harrison-quotes without conversion lens look like padding. All three failure modes weaken Harrison's trust in the proposal.

## How to apply

When building voc_quotes for a new idea:
1. Identify the wound the video addresses.
2. Search testimonials for someone who experienced that exact wound and recovered. Pull their before/after language.
3. Search sales calls for someone who described that wound on a call (signed up or not).
4. Add 1-3 supplementary quotes from comments / DMs / ads as relevant.
5. If using any Harrison quote, add the conversion-lens explanation to the source field.

Verify minimum sourcing BEFORE the curl POST. Do not push if the testimonial OR sales-call quote is missing.
