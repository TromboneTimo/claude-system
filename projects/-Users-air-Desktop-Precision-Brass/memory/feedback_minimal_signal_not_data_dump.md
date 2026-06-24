---
name: feedback-minimal-signal-not-data-dump
description: "For Timo's dashboards/analytics, ship the minimum that answers the question (the signal/pattern), not comprehensive data. Strip cards/rosters/totals/paragraphs he didn't ask for. Build EXACTLY what's asked; never bolt on extras or pitch new scope."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: defd3a9f-9783-4b7f-ac74-e4760a101955
---

Timo wants the SIGNAL, not a data dump. Default every view to the smallest thing that answers his question. He will ask for more if he wants it; he should never have to ask you to REMOVE things.

**Why:** 2026-06-20/21 "Converters" build. Over many rounds he kept saying "too much information," "way too overwhelming," "remove all that," "I have to spend all this time telling you to dumb shit down." Each round I had shipped extras he never asked for: summary count cards, a per-person roster, revenue totals, a multi-line "estimates" paragraph. He stripped every one. Then I pitched wiring an opt-in age field; he called it "a stupid idea." The pattern: my additions were friction he had to delete, not value.

**How to apply:**
1. Build EXACTLY what he asked. No bonus cards/tables/totals/paragraphs "to be helpful." Extras are friction, not value.
2. Lead with the answer/pattern. A breakdown chart ("where buyers are") beats a roster of every buyer. Cap long tails to top N; never dump the full list.
3. Helper text = one short line max. No inline caveat paragraphs.
4. Do NOT propose new scope/features/ideas unless asked. Do the task, stop, let him ask. (opt-in field = rejected.)
5. Analytics = coverage-first. When data reads mostly "Unknown", fix the SOURCE, do not just render sparse data prettily. IP geolocation beat phone-only and cut location-unknown ~50% -> 13%. Be honest where a signal plateaus (name->age caps ~55%).
6. Match his words to the real artifact and reproduce his exact view: see [[feedback_map_named_list_and_reproduce_view]] ("filmed list" = Ready to Film; the "Clicks" column already WAS leads, mislabeled).
7. Engineering: bump BOTH server and client cache-version keys whenever the payload SHAPE changes, or the new field renders blank from stale cache. See [[canon_dashboard_engineering]].
8. Never let a sub-view silently inherit a PARENT filter. The Converters sub-tab was being filtered by BOTH the global platform selector (YouTube/Meta/etc) AND its own Organic-vs-Meta camp toggle - two filters stacked, invisible. Timo: "you can't really see where the data is being filtered." Each view should own its filter scope explicitly; if a sub-view has its own toggle, decouple it from the parent filter entirely. When something can be filtered, the active filter must be VISIBLE on that view (date-range chip, camp toggle counts).
9. A truncated list ("+N more") must be EXPANDABLE to the full list on click. Timo: "I should be able to see all states and all cities... it's fucking retarded if it's not." Cap for density, never to hide data.

Links: [[feedback_map_named_list_and_reproduce_view]], [[canon_dashboard_engineering]], [[canon_working_process]]
