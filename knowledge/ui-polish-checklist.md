# UI Polish Checklist

Canonical reference for the "did I ship the polished thing, or just the skeleton" check.

Run this checklist BEFORE saying "ready", "live", "done", or "deployed" on any UI work.

The point: a memory note that I "should infer polish" is not enforcement. This is the durable rule list to walk before declaring a UI feature complete. Loaded from `CLAUDE.md > UI POLISH GATE`. Referenced from `dashboard-dev` and any other UI-touching skill. Also printed by `~/.claude/hooks/dashboard-deploy-gate.sh` at deploy time so I cannot miss it.

---

## The 7 questions, no skipping

Before declaring done on any UI feature:

**1. Orphan UI?**
Is there a button, link, label, or icon that doesn't do something useful? Delete it. Examples that have shipped to Timo as bugs: a "Today" button on a calendar that the user already starts on, a "Save" button next to an autosaving field, decorative arrows on read-only labels.

**2. Consistent flows?**
Does the new flow look and behave like the related flow next to it? Single-item action and multi-item action should not have two different UIs. Caught 2026-05-13: single-email schedule had its own broadcast.html with Send-Now + Schedule split, while multi-select had a clean queue+calendar layout. One had to be retrofitted to match the other.

**3. Obvious affordance?**
Does every interactive element LOOK clickable? Default `<select>`, default `<input type="date">`, plain text spans, hover-only-reveals all fail this. Caught 2026-05-13: native dropdown looked like an unclickable static label. Custom button with stripe + label + chevron + raised shadow passes.

**4. Diagnosability?**
If something is wrong, can the user click to see why? Read-only labels that hide the underlying data are traps. Caught 2026-05-13: scheduled-email pills on the calendar couldn't be clicked to see body, ship time, or target list, so the user had no way to verify what they had scheduled.

**5. Warning prominence**
Does the warning actually warn? Red banner at the bottom while the action button is at the top fails. Caught 2026-05-13: conflict warning lived below the calendar while the Schedule button was above it. User assigned 2 emails to the same day and saw nothing.

**6. Label consistency**
Does the sidebar say the same thing the page title says? Does the page title match across all pages that reference this feature? Caught 2026-05-13: sidebar said "Schedule" on one page while everywhere else and the user expectation said "Scheduled emails".

**7. Route allowlist (auth-gated apps)**
If I added a new route, did I update the auth allowlist? On Precision Brass that means `dashboard/lib/config.js > LOCKED_ROLE.allow_pages`. Caught 2026-05-13: new `/scheduled` page silently redirected to `/scripts` because the allowlist wasn't updated. The whole multi-select flow was unreachable.

**8. Contrast on data text**
Never use the muted/secondary text color for actual data the user needs to read. Muted greys (`#8a96b0`, `var(--text-muted)`, etc.) are ONLY for labels, hints, captions, instructions, dim-state badges. Anything containing a NUMBER, NAME, DATE, TIME, ID, STATUS VALUE, or any user-facing data point gets:
- Full-contrast text (`var(--text)` `#e8eaf0` at minimum), or a labeled chip/pill with bordered background.
- Font size 12px+. Diagnostic data at 11px on muted grey is unreadable on dark mode.
- If the text contains 4+ data points (e.g., "BROADCAST . Ships at X . To: Y . AC 123"), render each as a separate chip with a category-distinct color and a border. One-liner blob with separators is a fail.

Caught 2026-05-13: scheduled-email modal meta line "BROADCAST . Ships at Wed, May 13, 2026, 4:30 AM PST . To: Test - Timo Solo . AC campaign 591" at 11px in `#8a96b0` blended into the modal background. The diagnostic info Timo specifically wanted to read was invisible. Rebuilt as 4 colored chips.

This is a recurring complaint. Timo's words: "I keep telling you that text like this doesn't really work." Audit every block of data-bearing text in any UI I touch and apply this rule before shipping.

---

## Proactive offers

After running the checklist, if any item is "no", I should:

1. Fix it before declaring done.
2. If I notice an adjacent thing that's broken or rough but is technically out of scope, mention it as a proactive offer: "While I was in here I also noticed X. Want me to fix that?" Do NOT silently leave it.

The cost of asking is one sentence. The cost of waiting to be told is the user's confidence in me.

---

## Why this exists

Origin: 2026-05-13. Across one session building the scheduled-emails calendar for Precision Brass, Timo had to manually correct EVERY item above. His words: "I feel like there are a lot of features that you weren't inclined to include, and I had to really guide you through. It's like I'm talking to a child." He asked me to make the lesson durable, not just a memory note that gets ignored.

The meta-pattern: I default to "ship the literal minimum that satisfies the request" and wait to be corrected. The actual bar is "would the user use this without rolling their eyes." Functional is necessary, not sufficient.

---

## Workspaces this applies to

All. Precision Brass, Robinson's Remedies, Tim Maines, blog work, anywhere I touch a frontend. The polish checklist is workspace-agnostic.

---

## Related

- `~/.claude/skills/dashboard-dev/SKILL.md` (dashboard-specific gates + verification)
- `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_ship_polish_not_skeleton.md` (Precision Brass session that produced this)
- `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_verify_after_deploy_walk_the_flow.md` (walk-the-flow rule)
- `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_new_route_check_auth_allowlist.md` (route allowlist rule)
- `~/.claude/hooks/dashboard-deploy-gate.sh` (enforcement at deploy time)
