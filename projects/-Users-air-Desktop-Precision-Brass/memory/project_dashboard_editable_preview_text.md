---
name: project_dashboard_editable_preview_text
description: "Email preview text (preheader) is now editable on BOTH the review (emails.html) and send (broadcast.html) pages, and injected as a hidden preheader at send time. Blank = no inbox preview. Built + verified live 2026-06-09."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7f59b606-524f-4bf6-8cec-391e67c8d3f7
---

2026-06-09. The dashboard broadcast sends ONLY `email_proposals.body`; `preheader` (and `ps_text`) were always silently dropped, so `preheader` was cosmetic, shown in the UI but never in the actual email. Preview text strongly moves open rates, so this was a real gap. Built an editable preview-text feature and verified it live (commit 9258182).

**What ships now:**
- **emails.html (review):** editable "Preview text" input under the subject (`#emPreheaderEdit`), `onchange` -> `savePreheaderEdit()` -> `PB_DB.email_proposals.update(id,{preheader})`. Blank input clears it.
- **broadcast.html (send):** `#bcPreheader` input with a live "Inbox preview" snippet (`#bcMailSnippet`) that shows "(no preview text...)" when blank. At send time BOTH payloads (test path + real-send path) prepend `buildPreheaderHtml(preheader) + bcBody.value` as `html_body`.
- **`buildPreheaderHtml(text)`** returns a hidden `<div style="display:none;max-height:0;...">` containing (text + `&nbsp;`) then ~40x the invisible-filler string `&#847;&zwnj;&nbsp;&#8199;&shy;`. Empty text => spacer-only div => the inbox preview is BLANK (the filler stops body text bleeding into the preview). Per Timo: blank-when-empty is the desired behavior (e.g. the "beware" email ships with no preview).

**Verified live (authed Playwright):** field renders under the subject on emails.html, save round-trips to Supabase (typed -> persisted -> cleared -> `preheader=""`), 0 console errors on both pages, `buildPreheaderHtml('')` is invisible and `buildPreheaderHtml('text')` carries the text.

**Why it matters for future emails:** to set/clear an email's inbox preview, edit the Preview text field on the dashboard (review or send page). Do NOT rely on the `preheader` column alone reaching the inbox via the old path; the send injects it from the field. Related: [[feedback_email_ps_must_be_in_body]] (same root cause: broadcast sends body only), [[feedback_email_html_links_and_cta]].
