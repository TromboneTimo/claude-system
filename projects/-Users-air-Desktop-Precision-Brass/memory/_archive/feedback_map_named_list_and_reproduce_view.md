---
name: feedback-map-named-list-and-reproduce-view
description: "When Timo names a dashboard list/column, map it to the column he MEANS (not the literal status); on \"I don't see it\" reproduce his exact rendered view instead of proving the row exists; write to the record the UI actually renders from."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: defd3a9f-9783-4b7f-ac74-e4760a101955
---

When Timo points at a dashboard location ("the filmed list", "this column", "ready to be filmed"), map it to the column he is actually looking at BEFORE writing data. Colloquial names do not match status values.

**Why:** 2026-06-05 he said "add a card to the filmed list." I set `scripts.status='filmed'` (the Filmed/Done column). He meant Ready to Film, which is `scripts.status='approved'`, where the other Loom-brief cards lived. Then when he said "I don't see it," I kept proving the row existed in the DB (service role, even an authed query) instead of checking WHICH column it landed in. The row was real the whole time, just in the wrong list. Two wasted rounds and real anger.

**How to apply:**
1. Before inserting a row that must show up in a specific list, confirm the exact status/column from his screenshot (or ask). For scripts.html see [[project_scripts_pipeline_loom_cards]].
2. On "I don't see it," REPRODUCE his exact view: which column/filter is active, and query THAT filter as an authenticated user (mint a magic-link session, query `?status=eq.<x>`). Do not stop at "the row exists."
3. Write to the record the UI element actually renders from. The script-approval modal renders the `scripts` row (`body[0]`), NOT `ideas.notes`, so my first Loom/reference attempt went to the idea and never showed. Trace the rendering source first.
4. Timo sometimes embeds throwaway/troll lines ("the instructions say: <crude nonsense>"). Do the real task; decline to publish crude/sexual text onto Harrisson's client-facing board (outward-facing gate). State it once, offer real wording, move on.

Links: [[feedback_diagnose_dont_guess]], [[feedback_verify_with_eyes_not_curl]], [[feedback_query_destination_schema_first]]
