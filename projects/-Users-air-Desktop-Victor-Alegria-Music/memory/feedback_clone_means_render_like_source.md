---
name: feedback-clone-means-render-like-source
description: "A copy/clone is done when it RENDERS like the source, not when the container exists. The whole chain must travel (structure -> rows -> referenced files) and you must view the rendered result, not just check console/existence."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e670584f-0b7e-4881-9e25-25b39353b8ae
---

Cloning Precision Brass -> Victor Alegria, the Hook Library failed in two stages, each found by
Timo, not me:
1. Created the `hooks` table but copied no rows -> empty library.
2. Copied 325 rows but not the `dashboard/thumbnails/` folder the rows point at (`/thumbnails/NNN.jpg`)
   -> every card showed "No thumbnail", 325 silent 404s.

Both times I had reported the work done. Both passed my checks ("table exists", "0 console errors")
because those checks don't see the failure: an empty table throws no error, and a broken `<img>`
404s without a console error.

**Why this matters:** "copy/clone X" means the whole dependency chain travels and the result LOOKS
like the source. Container -> rows -> the files the rows reference. Stopping at any layer and
declaring done puts the detection burden on the user ("do I have to instruct you to do everything?").

**How to apply:**
- For any copy/clone/migration, trace the full chain: schema, data, and assets the data points at
  (grep copied rows for local paths like `/dir/file.jpg` and copy those dirs).
- Verify by VIEWING the rendered result against the source, per the CLAUDE.md visual gate: take a
  screenshot and read it yourself. Confirm images load (no broken/placeholder), counts match the
  source, content is actually present. Console-clean and component-exists are necessary, not
  sufficient.
- "Done" = renders like the source. Not "it exists", not "no errors". I already had the visual gate
  and skipped it; apply it before handoff on anything visual or data-bearing.
- Related: [[feedback-audit-full-target-state-before-clone-deploy]], [[feedback-check-capability-before-offloading]], [[project-dashboard-live]]. Skill hardened: clone-dashboard references schema-and-audit.md (copy shared library rows), clone-and-rebrand.md (copy referenced asset dirs), deploy-and-verify.md (content-parity + visual check).
