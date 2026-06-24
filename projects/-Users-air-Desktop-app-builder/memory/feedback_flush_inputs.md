---
name: feedback_flush_inputs
description: Tag/badge inputs must flush pending text before form save. User typed a tag but it wasn't committed because they clicked Save instead of Enter.
type: feedback
---

When building forms with tag/badge/chip inputs that require Enter or "+" to commit, ALWAYS flush pending input text before saving the form.

**Why:** User added a tag by typing it, then clicked Save without pressing Enter. The tag was lost because the pending text was never committed to state. Deletions worked because they fire onChange immediately.

**How to apply:** Use forwardRef + useImperativeHandle on tag/badge input components to expose a `flush()` method. The parent form calls `flush()` on all input refs before reading form state and saving.
