# Priorities

**Last updated:** 2026-04-17 (JST)

## Tiers
- **T1 ENGINE:** Trombone Timo (~$8.5K/mo, 15hrs/wk, daily posting) / Creator Conservatory ($1.5K/mo, 3 clients)
- **T2 INFRA:** Hook Book (deep focus), n8n automations, Claude system
- **T3 SATELLITE:** Robinson's Remedies (~$500/mo, 5hr/wk cap, comp renegotiation in progress)

**WIP rule:** Max 3 active + 1 deep focus. T3 only after T1 obligations met.

## RR Key Context
- Revenue target: $124,800 to $260,000 in 12 months (+$11,300/mo)
- Bottleneck: Image library from Betty/Richard (blocks content scaling)
- Next meeting: April 22, 7 PM ET with Richard

---

## This Week (2026-04-13 onward)

### HIGH PRIORITY (time-ordered)
- **RR Comp Proposal** (DUE 4/22, 5 DAYS) -- project-based + performance-tiered draft to Richard. NOT STARTED. Biggest time risk.
- **Harrison pilot launch** -- dashboard + data pipeline built 4/17. NEXT: get YouTube API key + channel ID, test pipeline, send pitch (keep $500 base, $750/sale at $30K milestone, testimonial as deliverable)
- **Hook Book VSL** -- record (still blocking entire funnel)
- **Trombone Timo** -- daily shorts + long-form (always-on)
- **Otto / Music System Japan** -- content creation proposal for festival
- **RR Dashboard/Data Access** -- scope data requirements doc for Richard (blocks dashboard build)
- **RR Image Library** -- request consolidated folder from Betty/Richard (unblocks everything)
- **Creator Conservatory other clients** -- Sohee (AI content system), Wilhelm (check-in before May 16 wedding)

### MEDIUM PRIORITY
- RR blog content system (Betty publishing workflow)
- RR video content + live stream planning with Kenny
- RR carousel templates (blocked on Betty's design direction)
- Tim Maines consulting brand (Porkbun, FB automation)

## Next Week (2026-04-20+)
- RR email audit (abandoned cart, post-purchase, segmentation)
- RR Claude training video for Richard
- RR ad testing strategy ($5-50/day)
- Training content suite (DaVinci, Adobe Podcast, thumbnails, scripting)

**Detailed checklists:** `~/.claude/BACKLOG.md`

## Not Active Yet
- Skool as email capture / top-of-funnel
- Portie's 62-67 day buying cycle

## Backlog (promote when slot opens)
Script Bot / Claude Hook Agent for Artists / Transcript Quote Finder / ICP-Content Mismatch Analyzer / Script Comparison Bot / Email Sequence Builder / Artist Profile Quiz / Email/DM Performance Scanner / PDF/Report Generator

**Promote:** slot open + T1/T2 + clear outcome. **Demote:** stalled 2+ weeks OR T3 stealing from T1.

---

## Session 2026-04-17 (JST)

### Shipped
- Built Precision Brass dashboard prototype: 6 HTML pages (index, email, youtube, instagram, facebook, revenue), sidebar nav, dark theme + brass accent, Chart.js visuals, per-page tracking explainers
- Built YouTube data pipeline: fetch_youtube.py, mine_comments.py (AI classifier: gold/wound/friction), run_daily.sh orchestration, full setup README, Claude routine prompt
- Established Harrison pilot terms: $500/mo base stays, $750 per attributed closed sale at month 4 after $30K HYROS milestone hit in 60 days, video testimonial required

### Decisions made (not yet executed)
- Architecture: YouTube-only phase 1 (no Harrison data access needed), email/HYROS phase 2 when he grants access
- Dashboard hosting: local `python3 -m http.server` or Vercel free tier (TBD)
- Pitch to send Harrison: message drafted in `/Users/air/.claude/plans/enchanted-sleeping-reddy.md`, NOT YET SENT

### Blocked on
- Harrison pitch not sent yet (Timo to review + send)
- YouTube API key + channel ID (Timo to get from Google Cloud + Harrison)
- RR comp proposal 5 days out and not started

### ONE thing before closing session
Pick: Harrison pilot live (YT API + test pipeline + send pitch) OR RR comp draft. Cannot do both well in remaining time today.