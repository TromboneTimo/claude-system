# Session Log

Rolling log of sessions. Keeps the last 14 days. Older entries archived to `~/.claude/session-archive/`.

---

## 2026-04-28

### Session: Precision Brass email engine built end-to-end
**What happened:** Shipped Harrison's email proposal + analytics system, parallel to the existing pb-script video pipeline. Two new skills (`pb-email`, `pb-email-push`), two dashboard pages (`emails.html` proposal queue, `email-analytics.html` performance tracking, renamed from `email.html`), 2 new Supabase tables (`email_proposals`, `email_sends`), updated sidebar nav across 6 dashboard pages, `/email` redirect in vercel.json for backwards compat, 2 new memory entries.

**Architecture:** pb-email mirrors pb-script's 6-parallel-agent + 1-sequential-auditor design but compressed: each menu item is a complete DRAFT (subject + body + reasoning + VOC quotes), not just an idea. 4 audience modes: broadcast, reengagement, webinar-push, discovery-followup. Voice fidelity enforced via `voc/personas/harrison-email-voice.md` (recurring tagline verbatim, P.S. matches one of 5 types, real student names only, no Paul-template leakage from emails 8-12).

**Phase 2 deferred:** AC + HYROS sync via `scripts/sync-email-stats.mjs` (CLI), AC publish-from-approved-draft step. Documented in `project_future_todos.md` items 6 and 7. Env vars set in `dashboard/setup/.env.example`.

**Verification:** Visual QA passed via headless Chrome. Both pages render with full sidebar, brass styling, empty states, 5 analytics tabs (sales/assisted/replies/ctr/youtube), Log a Send form, action buttons. Schema not yet applied to Supabase. Action: paste `dashboard/setup/schema.sql` into Supabase SQL editor.

**Plan file:** `~/.claude/plans/i-need-to-create-serene-truffle.md`

---

## 2026-04-02

### Session 1 (System Setup)
**What happened:**
- Condensed global CLAUDE.md from 418 → 126 lines (removed duplication, collapsed 10 engineering modes to 5-row table)
- Updated user_timo_profile.md with data from "For David" PDF: new clients (Victor Alegria, Steve Parker, Big Wy's Brass Band, Norfolk Chamber, Third Coast, Brass Witch), expanded ICP framework, 9 tool ideas, high ticket barriers, competitor references
- Updated Trombone Timo stats: billion views, $40k from one video, NBC mention, TED talk invite
- Designed and built Kuro-adapted life operating system: SOUL.md, PRIORITIES.md, RHYTHM.md, SESSION_LOG.md, /ops skill

**Decisions saved:**
- Priority tiers defined: Engine (Trombone Timo, Conservatory), Infrastructure (Hook Book, automations), Satellite (Robinson's)
- WIP limits set: max 3 active, 1 deep focus (currently Hook Book)
- 9 tool ideas logged to backlog with recommended priority order
- Robinson's capped at 5 hr/week until renegotiated

**Open threads:**
- Test boot sequence in a fresh session to confirm it fires automatically
- Obsidian vault opened and working

### Session 2 (Landing Page + Offer + Funnel Strategy)
**What happened:**
- Built irresistible offer worksheet (GOH framework adapted for Timo)
- Built landing page v1 (too complex), v2 (Andrews Bodega cream style, still too much text), v3 (VSL + book a call — minimal, research-backed)
- Fixed dream outcome: "I help musicians with businesses and music coaches massively increase sales through organic social media and systems — without wasting time on strategies that don't work"
- Cut $5 ads from offer — no proof yet, future upsell after Robinson's data
- Decided: AI = "how" shown on calls, not the headline. Say "systems" not "AI" on VSL.
- VSL structure outlined: hook → pain → story → insight → what I do → CTA (under 10 min)

**Decisions saved:**
- Dream outcome updated in offer worksheet
- Landing page is VSL-first (video + CTA + minimal results below)
- Priorities updated: deep focus = Hook Book + Conservatory funnel
- Consulting content channels: Facebook, Instagram, YouTube (Tim Maines brand, separate from Trombone Timo)

**Open threads:**
- Record the VSL (bottleneck — unlocks the whole funnel)
- Get Calendly link set up and plugged into landing page
- Move domains to Porkbun
- Update landing page + offer worksheet to remove all $5 ads references
- Write full VSL script

## 2026-04-03

### Session 1 (Hook Book Content + Bug Fixes)
**What happened:**
- Added 37 new entries to Hook Book (now 325 total): 15 Dimitri Fantini (drums, 150K+), 14 Andrea Scaffardi (clarinet, 2K+ likes), 2 guptaviolin, 1 sophiereidfit (412K likes), 1 jettfranzen, 1 cafeandy, 1 garyvee, 1 Tony Polecastro, 1 magbakk carousel
- Fixed sorting: "Most views" → "Most popular" (uses views for YT, likes for IG). Date sort uses ID tiebreaker.
- Fixed "videos" → "posts", "Watch Original" → "See Original"
- Fixed admin assignment bug: auto-retry after 1.5s + error UI with Retry button
- Added creator search: dedicated `activeCreator` filter with pill UI, not just text search
- Fixed 2 broken carousel thumbnails (Nahre Sol, wiam_architect)
- Reclassified all Victor Alegria entries from Trumpet → Trombone
- Logged all client commitments from coaching call to memory

**Decisions saved:**
- Priorities updated with client deliverables: AI systems, training content, Hook Book expansion
- Deep focus after Hook Book ships = Client AI Systems

**Open threads:**
- Record VSL (still the bottleneck)
- Expand Hook Book to 100+ carousels (currently ~35 carousels)
- Build AI content creation systems for Harrison + Sohee
- DaVinci Resolve tutorial suite
- Fathom call analyzer for Harrison

## 2026-04-04

### Session 1 (Robinson's Remedies + System Optimization)
**What happened:**
- Built 3 landing pages (Lightning Stick, Recovery Stick, Endurance Cream) with Blueprint-style design
- Wired real product images into landing pages and carousel
- Installed Perplexity MCP server + perplexity-web-research skill
- Built self-improving system: /self-improve skill (Karpathy loop), eval.json for 3 skills, /weekly-review skill
- Created feedback/deliverables-log.md for deliverable tracking
- Researched and applied CLAUDE.md best practices via Perplexity -> NotebookLM pipeline
- Optimized all global MD files: CLAUDE.md (132->65), SOUL.md (129->44), PRIORITIES.md (95->43)
- Fixed notify.sh SESSION_LOG spam

- Built ADHD prompt counter (fires at 15/25/35/40+ prompts, all workspaces)
- Copied user profile to all 5 workspaces
- Built Harrison's Precision-Brass Claude Code workspace with full content system
- Saved 19-prospect Deep Psychological Dive as context file
- Saved Harrison's full personal profile (strengths, weaknesses, communication style)
- Saved 7-section content creation SOP
- Created eval.json for 8 skills total (was 3)
- Initialized git repo in ~/.claude/ for scheduled agent access

**Decisions saved:**
- Research pipeline: ALWAYS Perplexity then NotebookLM. No exceptions.
- CLAUDE.md best practice: under 60 lines, critical rules at top AND bottom, compaction orders
- Harrison workspace: long-form ONLY enforced, ICP checklist mandatory, visual plan required
- Future Harrison builds (Fathom, email, ads, DM) saved to memory as TODOs, not now
- CLAUDE.md instructions only 70-80% followed - use hooks for 100% enforcement rules

**Open threads:**
- Optimize Digital Product Creator MEMORY.md (139 lines, bloated)
- Run /self-improve on marketing-social to test the Karpathy loop
- Set up /schedule for weekly-review cron job
- Record VSL (still the bottleneck for Hook Book)

### Session 2 (RR Blog + Harrison Email System)
**What happened:**
- Built SEO blog system for RR Shopify (NotebookLM research, 2 sample posts, PAA keyword research for all products)
- Built Harrison Precision Brass email system at ~/Desktop/precision-brass-emails/ (43 files: CLAUDE.md, 6 context files, 6 SOPs, 5 strategy brain files, 10 templates, 4 references, 4 feedback trackers, 4 transcript synthesis structures)
- Architecture: strategy memo + angle scoring + cooldowns + self-improving feedback loop
- NotebookLM research on coach email best practices running in background

**Decisions saved:**
- Blog: 750-1250 words, listicle format, never direct comparison ads
- Harrison: Klaviyo over ConvertKit, 75/25 plain text/HTML, 14-day angle cooldown
- Client commitments from 2026-04-03 call logged to memory

**Open threads:**
- Harrison: Install /email skills as Claude Code SKILL.md files
- Harrison: Process 19 transcripts through analysis pipeline (Phase 2)
- RR: Keyword methodology for blog SOP, 3 more blog posts
- RR presentation due Tuesday 2026-04-07

## 2026-04-07

### Session 1 (System Fix + Daily Briefing)
**What happened:**
- RR Presentation marked complete, WIP slot freed
- Created private GitHub repo (TromboneTimo/claude-system) for remote agent access
- Pushed full ~/.claude system to GitHub (skills, priorities, session log, soul, agents)
- Upgraded morning-briefing remote agent: reads live repo, checks calendar, emails trombonetimo@gmail.com, includes "my take" direction
- Fixed ADHD counter: now shows prompt count on EVERY prompt in ALL workspaces (was only visible at thresholds in non-RR workspaces)
- Added auto-push hook (session-sync.sh): commits and pushes ~/.claude to GitHub on every session end
- Fixed Daily Brain Fix remote agent: added repo source, fixed broken local paths
- Fixed Weekly Deep Review remote agent: added repo source, fixed broken local paths
- Added proactive task management to SOUL.md: surface open threads, ask about completion, track with TodoWrite

**Decisions saved:**
- GitHub repo for remote agents: TromboneTimo/claude-system (private, classic PAT)
- Auto-sync on session end is now default behavior
- Timo wants proactive task check-ins: ask if things are done, don't wait to be told
- All 3 remote agents now read from live GitHub repo instead of hardcoded/local paths

**Open threads:**
- Record VSL (still the bottleneck for Hook Book)
- Verify session-sync hook fires correctly on next session end

## 2026-04-09

### Session 1 (Fix Automation System)
**What happened:**
- Diagnosed why ADHD tracker/daily briefings weren't working: both remote triggers were DISABLED
- Re-enabled Daily Morning Briefing + Daily Brain Fix remote triggers
- Built n8n workflow (Daily Morning Briefing) that reads GitHub repo, formats briefing, sends ACTUAL email via Gmail
- Workflow is ACTIVE on timotrombone.app.n8n.cloud, fires daily at 8am JST
- Flow: Schedule Trigger > Fetch PRIORITIES.md + SESSION_LOG.md from GitHub > Code node formats briefing > Gmail sends to trombonetimo@gmail.com

**Decisions saved:**
- n8n is the email delivery layer (Gmail MCP can only draft, not send)
- Remote triggers stay enabled for Claude-side analysis; n8n handles email delivery
- Two systems complement each other: Claude agents for smart analysis, n8n for reliable email

**Open threads:**
- Record VSL (bottleneck since Apr 2)
- Verify n8n briefing email arrives tomorrow at 8am JST
- Consider: should the Claude remote agent also push to a Google Sheet so n8n can pull richer data?

## 2026-04-08

### Session 1 (RR Meeting Action Items)
**What happened:**
- Added full RR to-do list from Fireflies meeting transcript to PRIORITIES.md (HIGH/MEDIUM/LOWER tiers)
- Saved meeting decisions to memory: comp proposal, $260K revenue target, April 22 follow-up, image bottleneck
- Flagged: RR scope expanding well beyond 5hr/wk T3 cap. Comp proposal is the gating item.

**Decisions saved:**
- RR revenue target: $124,800 -> $260,000 in 12 months (+$11,300/mo)
- Next RR meeting: April 22, 7 PM ET
- Key bottleneck: image library from Betty/Richard
- Comp proposal: project-based + performance-based (sales milestones)
- Content goal: 80% time reduction via AI, still needs human review/approval

**Open threads:**
- Comp proposal (due before 4/22)
- Send presentation slides to Richard
- Amazon/Shopify data access doc for Richard
- Image library request to Betty/Richard
- Blog publishing workflow with Betty
- Kenny live stream coordination (NABA conference this weekend)

### Session 2 (Full System Build + Cross-Session Sync)
**What happened:**
- Fixed repo visibility (private > public) so remote agents can clone
- Built cross-workspace session tracking (cross-workspace-log.jsonl)
- Added git pull to session-boot.sh -- every new session pulls latest from GitHub
- Added git pull to session-sync.sh -- session end pulls before pushing
- Cross-workspace activity summary injected into every session boot context
- Upgraded morning briefing: cross-workspace stats, dynamic Top 3, dynamic My Take
- Built Fireflies > Action Items n8n workflow (3 iterations to fix: string parsing, email independence, webhook POST)
- Tested Fireflies pipeline end-to-end: execution 783 SUCCESS with real RR meeting data
- Fixed RemoteTrigger run bug workaround (tool is broken, documented)

**Decisions saved:**
- Repo made public (no secrets, just priorities/skills/session log)
- Cross-session sync via git pull/push on boot/end is the standard
- n8n is the reliable email layer, Claude remote triggers are the maintenance layer
- Fireflies webhook URL: https://timotrombone.app.n8n.cloud/webhook/fireflies-meeting

**Open threads:**
- Register Fireflies webhook URL in Fireflies settings (Timo action)
- Record VSL (bottleneck since Apr 2)
- Verify morning briefing email arrives tomorrow 8am JST
- Verify Brain Fix remote trigger ran successfully (check claude.ai/code/scheduled)

## 2026-04-05

### Meeting: Studio Class (AM) (0min)
**Summary:** - **Content Strategy:** Focus on merging music performance with personal storytelling for better audience engagement and loyalty.

- **Audience Growth Goal:** Aim for 10,000 followers by New Year’s Eve, targeting 2-3 quality posts weekly.

- **Batch Production:** Plan to record multiple videos in one session to ensure consistent content without burnout.

- **Personal Branding:** Share emotional an

**Action Items (from meeting):**
- [FCANGI] Begin writing and producing a long-form video about the Ambusher trumpet journey, including mental and physical challenges (00:00)
- [FCANGI] Experiment with layering songs starting from the last layer to build viewer anticipation (04:15)
- [FCANGI] Incorporate more spoken segments in videos to enrich content despite English shyness (04:45)
- [FCANGI] Batch create videos, recording and editing multiple at once to ensure weekly consistency (05:30)
- [FCANGI] Continue creating playful and lifestyle content such as playing in various parts of the garden, including watering plants (09:10)
- [FCANGI] Send video drafts to Timothy for feedback but proceed with posting proactively (10:40)
- [Timothy Maines] Provide ongoing feedback on FCANGI’s video drafts and content experimentation (10:40)
- [Timothy Maines] Encourage consistency and weekly check-ins to support FCANGI’s follower growth goals (10:00)

## 2026-04-07

### Meeting: trombonetimollc@gmail.com - Wed, 08 Apr 2026 08:04:24 JST - Untitled (2min)
**Summary:** - **Sales Target:** Aim to double sales to **$260,000**; current revenue is **$124,800**, 48% of the target.  
- **Traffic Challenge:** High conversion rates show demand; focus on increasing traffic to Amazon and the website.  
- **Product Launch:** Lip Quench **4-pack** launching by end of April at **$21.59**, with a **10% discount** planned.  
- **Content Strategy:** Use AI for rapid, SEO-optimi

**Action Items (from meeting):**
- [Richard Mukamal] Work with Tim to analyze and provide access to Amazon and Shopify sales data for AI integration dashboard
- [Richard Mukamal] Support compensation discussion by reviewing Tim's forthcoming proposal and coordinate internal discussion with Betty and Kenny
- [Richard Mukamal] Schedule and send calendar invite for follow-up meeting on April 22
- [Bette Evans] Finalize Lip Quench 4-pack order details with Max and coordinate packaging/artwork timeline (12:32)
- [Bette Evans] Provide and organize high-quality images for marketing content and assist Tim with carousel template creation
- [Bette Evans] Work with Kenny and Tim to categorize endorser list and update the website endorser section accordingly
- [Bette Evans] Address website mobile UX issues such as translation button overlay and continue improvement on image carousel (18:28)
- [Bette Evans] Coordinate with Tim on blog publishing format and integration into Shopify
- [Timothy Maines] Develop a detailed compensation proposal including project-based and performance-based pay within two weeks
- [Timothy Maines] Organize and request AI-compatible images and create carousel templates using Photoshop or similar
- [Timothy Maines] Set up access and integration to collect Shopify and Amazon sales data for dashboard monitoring with Richard’s assistance
- [Timothy Maines] Lead implementation of blog content system for SEO-focused, story-driven marketing and coordinate small ad testing
- [Timothy Maines] Initiate and manage test live stream recording and promotion, enabling Kenny to start live video marketing
- [Timothy Maines] Prepare and share presentation materials and help coordinate collaborative content review process
- [Kenneth Robinson] Continue producing and uploading video content to Dropbox with proper organization (44:02)
- [Kenneth Robinson] Provide and update endorser information and assist Betty in website endorser section refinement
- [Kenneth Robinson] Schedule and participate in recordings/interviews with endorsers at upcoming events (e.g., ITG conference)
- [Kenneth Robinson] Perform initial test live stream as directed by Tim to leverage video marketing

## 2026-04-07

### Meeting: trombonetimollc@gmail.com - Wed, 08 Apr 2026 08:04:24 JST - Untitled (2min)
**Summary:** - **Sales Target:** Aim to double sales to **$260,000**; current revenue is **$124,800**, 48% of the target.  
- **Traffic Challenge:** High conversion rates show demand; focus on increasing traffic to Amazon and the website.  
- **Product Launch:** Lip Quench **4-pack** launching by end of April at **$21.59**, with a **10% discount** planned.  
- **Content Strategy:** Use AI for rapid, SEO-optimi

**Action Items (from meeting):**
- [Richard Mukamal] Work with Tim to analyze and provide access to Amazon and Shopify sales data for AI integration dashboard
- [Richard Mukamal] Support compensation discussion by reviewing Tim's forthcoming proposal and coordinate internal discussion with Betty and Kenny
- [Richard Mukamal] Schedule and send calendar invite for follow-up meeting on April 22
- [Bette Evans] Finalize Lip Quench 4-pack order details with Max and coordinate packaging/artwork timeline (12:32)
- [Bette Evans] Provide and organize high-quality images for marketing content and assist Tim with carousel template creation
- [Bette Evans] Work with Kenny and Tim to categorize endorser list and update the website endorser section accordingly
- [Bette Evans] Address website mobile UX issues such as translation button overlay and continue improvement on image carousel (18:28)
- [Bette Evans] Coordinate with Tim on blog publishing format and integration into Shopify
- [Timothy Maines] Develop a detailed compensation proposal including project-based and performance-based pay within two weeks
- [Timothy Maines] Organize and request AI-compatible images and create carousel templates using Photoshop or similar
- [Timothy Maines] Set up access and integration to collect Shopify and Amazon sales data for dashboard monitoring with Richard’s assistance
- [Timothy Maines] Lead implementation of blog content system for SEO-focused, story-driven marketing and coordinate small ad testing
- [Timothy Maines] Initiate and manage test live stream recording and promotion, enabling Kenny to start live video marketing
- [Timothy Maines] Prepare and share presentation materials and help coordinate collaborative content review process
- [Kenneth Robinson] Continue producing and uploading video content to Dropbox with proper organization (44:02)
- [Kenneth Robinson] Provide and update endorser information and assist Betty in website endorser section refinement
- [Kenneth Robinson] Schedule and participate in recordings/interviews with endorsers at upcoming events (e.g., ITG conference)
- [Kenneth Robinson] Perform initial test live stream as directed by Tim to leverage video marketing

## 2026-06-07 — Hannah email CTA-less send rescued
- Campaign 665 / message 680 (Daily Email 1, 4,105 list, 4am 06-08) was scheduled with NO P.S./CTA: P.S.+booking link had been parked in proposal ps_text, which broadcast.html never sends (body only).
- FIX (verified): backed up msg 680, re-PUT /api/3/messages/680 appending P.S. + real CTA https://www.precisionbrass.info/precision-brass-application-page (the application page from all 18 winning emails; my earlier /apply was a bogus placeholder). Confirmed P.S.+CTA in html AND text, video intact, greeting still %FIRSTNAME%, campaign still status=1, same sdate, send_amt=0. Editing the message in place = the reschedule.
- Synced Supabase proposal body link to match.
- ROOT CAUSE hardening (local, NOT deployed): broadcast.html composeBody() folds stray ps_text into body on load.
- Lesson saved: feedback_fix_the_shipping_artifact_not_the_proxy.md. I had already-written knowledge (feedback_email_wall_of_text_propagation) and narrated a plan instead of executing it.

## 2026-06-07 — broadcast.html preview fidelity + deploy
- Bug: broadcast Inbox preview stripped the video embed (DOMPurify allowlist had no img/table/style); cream/serif dashboard CSS also leaked in. Real Gmail showed the embed, preview did not.
- Fix: expanded ALLOWED_TAGS/ATTR (img,table,tr,td,style,src,width,alt...) + render body in an isolated about:blank iframe via document.write (NOT srcdoc, which the default-src 'self' CSP with no frame-src would block on the live site). img-src already allows i.ytimg.com.
- Deployed to prod (precision-brass-dashboard.vercel.app). Live bundle confirmed (bc-mail-frame, doc.write, composeBody, expanded allowlist all present; HTTP 200). Verified the exact iframe code path renders the video embed under a production-matching CSP via headless Chrome screenshot. Could NOT load the authed live page in-browser (Playwright instance locked by another process).
- Also live now: composeBody() ps_text fold (root-cause net from the CTA-less send earlier today).

## 2026-06-07 — Found the RIGHT surface: emails.html .email-body (video embed)
- Earlier broadcast.html fix was the WRONG surface (deprecated; gotoBroadcast routes to /scheduled). Timo still saw cream/serif + no video = emails.html .email-body fingerprint.
- Real cause: emails.html PB_BODY_TAGS and scheduled.html PREVIEW_TAGS allowlists lacked img/table/style -> video embed stripped. Fixed both; flipped .email-body cream/Georgia -> white/Arial to mirror the inbox.
- Verified on the ACTUAL emails.html page, authed (magic-link session, /tmp dashboard copy), real proposal data through the page's own DOMPurify: video thumbnail + play button renders, white/Arial, 0 console errors. Read screenshot myself.
- Deployed prod (gate passed with live evidence). /emails + /scheduled confirmed live (HTTP 200, expanded allowlist, white .email-body).
- Saved project_email_body_render_surfaces.md.

## 2026-06-08 — Why the email-body fix wasn't live: CONCURRENT DEPLOY CLOBBER
- Root cause Timo's incognito still showed cream/serif: my earlier prod deploys (broadcast c1o15l73o, emails f6iwgsij6) were CLOBBERED. A concurrent process deployed rkvkzn7zv + 59sp2u1uw AFTER mine and re-aliased prod to a bundle WITHOUT my (uncommitted) changes. Cache-busted curl proved live origin = old (FAF7F2, no allowlist).
- Fix: COMMITTED the 3 dashboard files to main (a533d79, rebased over concurrent 3649a58 -> confirms active concurrent committer), pushed origin/main, then vercel --prod --force.
- Verified live: cache-busted curl .email-body = #ffffff/Arial, FAF7F2 gone, allowlist present, age:0; browser computed .email-body = rgb(255,255,255)/Arial; real proposal body via page DOMPurify renders video; 0 console errors.
- LESSON (reinforces feedback_concurrent_repo_use_worktree): uncommitted dashboard fixes get reverted by the concurrent deployer. COMMIT to main for durability, don't rely on a CLI --prod deploy alone.

## 2026-06-08 — Phantom schedule fixed + queue cleared
- Deleted 15 approved email_proposals (queue fresh; Hannah scheduled row kept).
- BUG: api/ac-cancel.js deletes the AC campaign + flips proposal but never releases the email_send_ledger claim. After I cancelled 665, ledger row 51 still claimed list13+2026-06-08T11:00 for dead 665. Dashboard Schedule -> claimSlot saw the stale claim -> "duplicate_prevented", returned dead 665, created NO real campaign. Dashboard showed "scheduled" (phantom); AC had nothing for tomorrow.
- FIX: deleted stale ledger row 51, called prod /api/ac-send (authed, list 13, 2026-06-08T11:00Z, Hannah body) -> created REAL campaign 666 (msg 683). Verified status=1, sdate tomorrow 4am, send_amt=0, list 13, ONLY campaign for tomorrow, 665 stays 404. Pointed proposal at 666; ledger row 53 = real claim.
- OPEN: ac-cancel.js should release the ledger claim on cancel (offered to fix). Without it, every cancel->reschedule reuses the dead campaign id.

## 2026-06-08 — Schedule-integrity system fixes shipped (commit a5ddfa4)
Built + deployed + verified the 3 safeguards so the phantom-schedule class can't recur:
1. api/ac-cancel.js: cancel now DELETEs the email_send_ledger claim by ac_campaign_id (returns ledger_released). Root-cause prevention.
2. api/ac.js flagPhantomSchedules(): wired into ?action=reconcile-scheduled; flips any FUTURE status=scheduled proposal with no live AC status=1 campaign to send_failed + Slack BEFORE its send time. Fail-safe on non-404 AC errors.
3. dashboard/scheduled.html: red badge now 'WON'T SEND' + tooltip covering AC-dropped and phantom cases.
VERIFIED LIVE: reconcile-scheduled returns phantom_watchdog {future_checked:1, phantom_count:0} -> did NOT false-flag real campaign 666; Hannah stays status=scheduled cid=666; scheduled.html marker live; ac.js new code live (phantom_watchdog only exists in new code). NOT live-tested (to avoid side effects): a positive phantom flip (would Slack-spam) and a real cancel (would delete 666). Logic syntax-checked; ledger DELETE is the same query proven manually on row 51.
Brain: memory updated (project_ac_cancel_ledger_claim_bug = fix applied; meta-lesson "verify the real object, never the proxy").

## 2026-06-09 — Editable email preview text + reader-facing method institutionalized
- BUILT editable Preview text (preheader) on BOTH dashboard pages (commit 9258182, deployed + verified live authed):
  - emails.html (review): #emPreheaderEdit input under subject -> savePreheaderEdit() -> PB_DB.update(preheader). Verified DB round-trip (type -> persist -> clear -> "").
  - broadcast.html (send): #bcPreheader + live inbox snippet; buildPreheaderHtml() injects a hidden preheader at top of body in BOTH send payloads (test path L558 + real-send L805). Blank field = invisible spacer = blank inbox preview.
  - Root cause it fixes: broadcast sends body only; preheader was cosmetic/never reached inbox.
- beware email (e_20260609_beware): CTA -> masterclass webinar (?el=timoemail); removed redundant in-body spacer (body 3266->1935) so the preview field is single source of truth; status=approved (NOT sent; Timo sends from dashboard).
- REMEMBERED: reader-facing-playbook.md is now a hard-load precondition in pb-email + pb-email-write (+ matching failure-mode/auditor checks). New rules: cite a SPECIFIC named Harrison technique (reader feels smart), vary the reframe transition across a batch, edge over soft-cock.
- Memory: feedback_email_cite_specific_technique_and_vary_transition.md + project_dashboard_editable_preview_text.md (both indexed in project MEMORY.md).
- Note: deploy hit a concurrent meta-ads-refresh sync collision; my commit landed clean on origin/main, left the other process's working-tree state untouched (should've used a worktree).

## 2026-06-13 (pt3) - GATED the "nobody tells you" phrase (Timo: "why didn't you do that the first time")
- Root cause verified by grep: the ban existed in 6 DOC files since 2026-06-09 but had ZERO enforcement; and I drafted in chat (skill files never loaded). The one live signal (angle-gate hook) listed "nobody-ever-told-you" only as a soft "cap this trope," not a ban. Classic docs-advise-but-no-gate, same failure class as stale citations / vs-typical.
- FIX (3 layers): (1) email-lint.js marketer-opener block rule; (2) email-link-gate.sh banned-phrase check at the email_proposals write chokepoint (blocks push/send, chat-drafted or not); (3) email-angle-gate.sh injection rewritten to a loud BANNED-phrases line. Pattern anchored on (nobody|no one) [ever] (tell|told) you to catch "here is what/the truth nobody told you" variants.
- Testing CAUGHT a real hole mid-build: first pattern only matched the contraction "here's" not "here is" and missed bare forms; broadened + retested 4/4 bad blocked, 4/4 clean pass, youtube/forbes rules unaffected, the already-pushed email clean (0 hits). Honest admission logged: I took the lazy doc path when first corrected instead of building the gate.
