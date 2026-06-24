---
name: NEVER seed demo or fake data into the dashboard
description: Standing rule from 2026-04-28. Empty-state is the correct first-run state for any user-facing dashboard table. No INSERT...VALUES seed blocks in schema.sql, no fake demo rows for "showing what the column looks like with content," no test uploads left behind in production tables.
type: feedback
originSessionId: 7f540398-3cb8-4b73-9023-2f87ee04eec4
---
## The rule

**Zero seed data. Zero demo rows. Zero placeholder content. Ever.**

Applies to all Supabase tables that feed any user-facing dashboard at `Precision-Brass/dashboard/`:
- `ideas`
- `scripts`
- `harrison_suggestions`
- `email_proposals`
- `email_sends`
- any future tables added

Empty state is the correct first-run state. The page should render its empty placeholder ("Nothing here. This column is clear.") on day one. Real content only enters via the production paths:
- `/pb-script` then `/pb-ideas-push` (ideas)
- `/pb-script-write` (scripts)
- `/pb-email` then `/pb-email-push` (email_proposals)
- "Log a Send" form on email-analytics.html (email_sends)
- the dashboard's own Submit button (harrison_suggestions)

## Why

Timo lost trust in the script approval pipeline on 2026-04-28 because the original schema.sql contained 4 seeded scripts ("The mouthpiece question...", "Why your range stopped growing at 52...", "The 6 minute embouchure reset...", "The 30 minute practice...") inserted with `on conflict (id) do nothing`. They were intended as demo content showing what each pipeline column looks like with rows in it. Two of them carried fake `notes` text ("Section 3 feels rushed. Add a demo of the slur exercise...") and one was seeded with status='approved' which made it appear that Harrison had approved a script that he had never seen. Timo thought the approval flow was broken when in fact it was correct, and the seed data had skipped the entire flow.

Also deleted same day: 2 "(Demo)" PDF flow test scripts left in the table from skill testing. Production tables should never carry test artifacts past a session.

## How to apply

1. **Schema files:** `dashboard/setup/schema.sql` and any future schema files contain ONLY `create table`, triggers, and RLS policies. Zero `insert into ... values` blocks.
2. **Skills:** `pb-ideas-push`, `pb-script-write`, `pb-email-push`, `fb-vault`, `yt-vault`, etc., must never insert "test" or "demo" rows for verifying their wiring. If they need to test, use a temporary id prefix like `test_` and DELETE before the session ends.
3. **Test uploads:** if a skill is being verified end-to-end against the live Supabase, the test row gets deleted in the same session it was created. No exceptions.
4. **Visual QA / screenshots:** if the empty state needs to be visually demoed, mock it with a separate file (a `*-preview.html` outside the deploy path, or a screenshot in the plan), never with a real INSERT into a production table.
5. **If you find seed data already in the db:** delete it immediately when surfaced. Then strip the seed block from whatever file generated it. Then save a memory entry like this one if it represents a new pattern.

## Severity

This is a high-severity trust failure. Same tier as fabricating VOC quotes or shipping unverified behavioral claims. A single fake row that looks real undermines the whole "ship right, never ship fast" principle stored in `feedback_ship_right_not_fast.md`. If in doubt, delete the row and ask Timo before re-adding anything.

## Also applies to: hardcoded UI numbers

Same rule applies to KPI cards, chart axes, leaderboard rows, sample data in JS objects (`VIEWS`, etc.), or any other UI element that shows a number. Until the data source is properly hooked up:

- KPI cards: show `$0` / `0` / "No data yet" until the live query returns real rows.
- Charts: empty state ("No data in this window") until real data flows.
- Tables: empty state ("No sends logged...") until rows exist.
- Date-comparison deltas like "+214% vs last month": NEVER hardcode. Compute from live data or omit entirely.

Example violation caught 2026-04-28: the `email-analytics.html` KPI cards were hardcoded with `$16,800 +214%` / `3,840 +12.2%` / `299 +38%` / `24 +71%` from the original mockup HTML. Even though the JS was wired to overwrite them on load, the user saw the fake numbers on first paint and lost trust. Fix: replace HTML defaults with `$0` / `0` / "No data yet" so even if JS fails the page is honest.

The principle: a Precision Brass dashboard should never display a number the underlying database cannot back. Zeros and empty states are the truthful default. Real data populates from real sources only.
