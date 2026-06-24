---
name: feedback_complete_nav
description: Always build complete navigation between all views. Every view needs buttons to reach every other relevant view.
type: feedback
---

When building multi-view apps, EVERY view must have clear navigation to reach every other view the user needs. Don't assume users will type URLs manually.

**Why:** User was frustrated that admin view had no button to reach client view, and client view had no dashboard button. Missing navigation is a critical UX failure.

**How to apply:** Before shipping any multi-view/multi-role app, list all views and verify each one has navigation links to all other views that role should access. Draw the nav map mentally: can every role reach every page they need from any starting point?
