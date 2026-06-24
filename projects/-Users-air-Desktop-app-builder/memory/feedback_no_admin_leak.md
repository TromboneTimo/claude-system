---
name: feedback_no_admin_leak
description: Never show admin UI elements (links, buttons, edit controls) in client/public views. Role-based UI must be strict.
type: feedback
---

When building apps with admin vs client views, NEVER leak admin UI into the client view. No admin links, no edit buttons, no management navigation — nothing that reveals admin functionality exists.

**Why:** User was frustrated that the client view showed an "Admin" link in the header, breaking the separation between admin and client experiences. This is a basic role-based UI mistake.

**How to apply:** When `isAdmin` is false (or user role is client), the entire admin navigation block must not render at all — don't just hide individual buttons, wrap the entire admin nav section in the role check. Test both views before shipping.
