---
name: query-destination-schema-first
description: "When pushing data into ANY destination table (Supabase, AC, dashboard rows), query a complete known-good row with select=* BEFORE building the payload. Don't build from the source-side schema (chat template, MCP output, skill spec). The destination's column set + rendering logic is the authority. Mismatch is silent because the row inserts fine. Caught 2026-05-15 when I shipped 7 email_proposals with a plain-text rationale and no concept/wound/why/icp/synthesis/origin/channel sections, because I built from the pb-email output schema instead of querying email_proposals directly."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0b9fa848-7b9a-4dda-b396-5cc296f16876
---

# Query destination schema first. Source schema is a lie.

**Rule:** Before pushing data into ANY destination table for the first time in a session (or after suspected schema changes), run `select=*` on a known-good existing row. Diff the returned column set against your planned payload. Every column either gets a real value or an explicit null. Any column you can't account for means STOP and ask.

**Why:** 2026-05-15. I pushed 7 `email_proposals` rows with a 3-sentence plain-text `rationale` field. The dashboard at `/emails` parses rationale as HTML with named `r-section` blocks (concept, wound, why, icp, synthesis, origin, channel). On Harrison's view, the new drafts showed a wall of plain text where the old drafts had 7 styled cards. Timo: "you did not include any of this information when you published the emails, which is fucking stupid because it's in the other emails that you proposed."

**Root cause:** I built the payload from the pb-email skill's output template (12 fields). The destination table doesn't define rendering rules in the column type system. They're encoded in HTML class names inside the string column. The skill's "rationale: 3 sentences plain English" was technically valid SQL but invalid product. The destination's actual rendering is the authority; the source-side schema is a hint, not a contract.

**How to apply:**
1. Before the first POST/INSERT/upsert in a session on a new (or recently-changed) table, run:
   ```bash
   curl -s "${SUPABASE_URL}/rest/v1/{table}?select=*&limit=1" -H "apikey: ${KEY}" -H "Authorization: Bearer ${KEY}" | python3 -m json.tool
   ```
2. For every string field longer than ~200 chars on the existing row, inspect the structure (HTML class names, JSON sub-keys, markdown sections, ANSI codes). The string is probably a structured document, not a paragraph.
3. If your planned payload doesn't match that structure, STOP. Either rebuild the payload to match, or ask the user if the new pattern is a deliberate departure.
4. The `pb-email-push` skill's "Step 2. Load Supabase config" step should be updated to add this query as a mandatory prelude.

**Generalization:** This applies to ANY destination, not just Supabase. AC v3 fields, ScriptKit metadata, dashboard config JSON, Slack message attachments, NotebookLM source metadata. The destination's actual rendering logic is the truth. The skill's output spec is a guide.

**Cross-reference:** Built-in compliment to [[zero-drop-ingestion]] but inverted. That rule says "every section in Timo's input must land somewhere"; this rule says "every column the destination renders must be populated correctly."

Related: [[audit-links-at-url-level]], [[link-count-variation]].
