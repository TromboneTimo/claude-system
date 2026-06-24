---
name: project-clone-status
description: "What was cloned from Precision Brass into Victor Alegria Music, what is still placeholder, and the remaining fill-in list."
metadata: 
  node_type: memory
  type: project
  originSessionId: 535cfadc-a09e-499b-91b5-baab3f146810
---

# Victor Alegria Music: clone status (2026-05-25)

Victor is a **music coach / educator**. Infrastructure cloned from Precision Brass, **minus all paid Meta ads**.

## DONE (Phase 1 + 2)
- Workspace skeleton at `~/Desktop/Victor Alegria Music/`: context/, references/, voc/ (channel-first, no meta-ads), dashboard/ (16 pages, no meta-ads.html), api/ (no meta-ads-ingest), scripts/, output/.
- `CLAUDE.md` rewritten for Victor coaching model (ICP + voice are PLACEHOLDERS).
- `voc/config.yaml` + `voc/STRUCTURE.md` re-anchored to Victor; ICP fields = TBD.
- Safe branding re-point in dashboard HTML (Precision Brass -> Victor Alegria Music, Harrison -> Victor).
- `DEFERRED-PHASE4.md` lists the backend re-point that MUST happen before deploy (live Supabase ref, env vars, table prefixes, Harrison logic in api/lib).
- Memory: 35 universal lessons + Timo profile copied. SOUL/PRIORITIES/SESSION_LOG are global.

## STILL PLACEHOLDER (need Victor's real intake - Phase 0)
- ICP: age, segment, geography, pain themes (in CLAUDE.md + voc/config.yaml)
- Victor's voice / named teaching techniques
- Offer, price points, funnel specifics
- Domain + webinar/registration URL (PB's precisionbrass.info still in code)
- Email platform (assumed ActiveCampaign; confirm)
- Credentials: Supabase, Vercel, email platform

## REMAINING PHASES
- Phase 3: clone 8 pb-* skills to va-* and re-anchor to Victor voice + VOC paths.
- Phase 4: new Supabase + Vercel + .env.local + (optional) MCP server. Execute DEFERRED-PHASE4.md.
- Phase 5: ingest Victor's real material via /coaching-db, run first va-script + va-email, verify dashboard.

## Decisions locked
- Skill prefix: `va-`
- No paid Meta ads (excluded throughout)
- Channels carried: youtube + email core; facebook/instagram organic tabs present, prune if unused
- Email platform: assume ActiveCampaign until told otherwise
- Supabase/Vercel: new dedicated projects
