---
name: push-lean-and-proposals-rls
description: "Push an approved draft = lean silent gates, no judge-agent ceremony; email_proposals SELECT needs service-role key (anon returns empty [])"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

2026-06-10, after pushing e_20260610_quick_question Timo said: "why did you do so much fucking hell, i mostly just wanted you to push."

**Why:** The draft was already approved in chat. The deliverable was assembly + POST + one read-back. I narrated every gate, spawned an independent judge agent, and burned 3 detours on a key problem. Gates exist to catch errors, not to perform diligence.

**How to apply:**
- When Timo says "push" on a chat-approved draft: run dedup + quote-source check + rhythm gate + render in ONE batched pass, report one summary line, POST. No judge agent unless the draft is NEW this turn (the judge gate in [[feedback_email_quality_gate_pipeline]] is a DRAFT-time gate, not a push-time gate).
- `email_proposals` SELECT with the anon key returns `[]` (RLS), NOT an error. Dedup/PATCH must use the service-role key.
- MASTER.md contains the `SUPABASE_SERVICE_ROLE_KEY=` line MORE THAN ONCE: always `grep -m1 | head -1` or you concatenate two JWTs and get a 401 "Invalid API key".
- Verify an edit to a pushed proposal by reading the stored row back and listing hrefs/markers. No browser loop for field edits ([[feedback_verify_lean_not_browser_loop]]).
- Link-count data point: Timo stripped the body YouTube link and kept ONE masterclass anchor in the P.S. (P.S.-carries-offer). Lean single-link when in doubt ([[feedback_link_count_variation]]).
