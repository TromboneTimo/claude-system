# Memory Index

## Critical (anti-hallucination, content verification)
- [Master Lessons](feedback_master_lessons.md) - 4-rule anti-hallucination protocol. Auto-transcripts lie, drafts are not facts, prospects are not customers, unusual=verify.
- [Verify Before Compact](feedback_verify_before_compact.md) - NEVER compact a file by pointer-swap without verifying target file has the content. 2026-04-13 /fix-brain near-miss.
- [Audit Scope Must Match Usage](feedback_audit_scope_must_match_usage.md) - NEVER execute on agent-named subset when full inventory is larger. Enumerate full file list first. 2026-04-14 fix-brain near-miss (3 of 14 skills deduped, ignored slide skills).
- [ASK Don't Invent](feedback_fabricated_behavior.md) - Never write "you already X" about a real person without evidence.
- [Never Fabricate Business Numbers](feedback_fabricated_content_numbers.md) - Every number traces to Timo's real database or is explicitly hypothetical.
- [Read The Database Before Asking](feedback_read_before_asking.md) - RE-READ relevant context file from disk before responding or asking clarification.
- [Search Content Before Concluding Missing](feedback_search_content_before_concluding_missing.md) - When Timo says a newer version exists, grep distinctive CONTENT disk-wide (incl. _cleanup-backup-* folders) before saying it doesn't. Trust content over mtime. 2026-06-07 cleanup clobbered the landing page with client videos.
- [Pre-Generation Checklist](feedback_pregeneration_checklist.md) - 4-item check BEFORE any content generation.
- [Verify Quotes Via Transcripts](feedback_verify_quotes_via_transcript.md) - Download YouTube transcript via yt-dlp. Perplexity fabricates URLs/attribution.
- [YouTube URL = yt-dlp Immediately](feedback_youtube_url_go_to_transcript.md) - ANY YouTube URL from Timo triggers yt-dlp FIRST. Not WebFetch, not WebSearch, not clarifying questions. Generalizes the quote-verification rule to all YouTube URLs.

## Meta Rules
- [Negative Rules First](feedback_negative_rules_first.md) - Prefer "NEVER do X" over "always do Y". Exclusionary rules fire more reliably.
- [Confirm Scope Before Building](feedback_confirm_scope.md) - Restate ICP + scope + thesis in ONE sentence before committing.
- [Skill Architecture](feedback_skill_architecture.md) - Cross-cutting rules belong in ~/.claude/knowledge/, not inline in every SKILL.md. Pre-flight check before every skill write. Canonical: ~/.claude/knowledge/skill-architecture.md.
- [Reviewer Pass](feedback_reviewer_pass.md) - After any compaction/dedup/self-improve iteration, spawn fresh Agent to diff BEFORE vs AFTER and flag LOST content. Binary evals miss silent deletions. Canonical: ~/.claude/knowledge/reviewer-pass-protocol.md.
- [Verify Before Declaring Done](feedback_verify_before_done.md) - Before saying "done," test the specific claim. Confident claims hide bugs (80% sure is worse than 50% sure). Do not wait for Timo to ask "what about X."
- [Check Existing Routines Before Claiming MCP Limits](feedback_check_existing_routines_before_claiming_limits.md) - Local tool lists are a subset. Before saying an MCP can't do X, check existing working routines for precedent.
- [Enforcement Mechanism Choice](feedback_enforcement_mechanism_choice.md) - Match rule to layer: hooks for mechanical patterns, gates for pre-action checks, subagents for post-action review, prose is weakest. Escalate when the layer below keeps failing.
- [YAGNI For New Agents](feedback_yagni_new_agents.md) - /fix-brain is the orchestrator. Do not build canonical-librarian, memory-gardener, or similar without 5+ real incidents. Extend existing tools before creating new ones.
- [Gates Come From Fuckups](feedback_gates_come_from_fuckups.md) - Every gate traces to a specific incident. Do not invent from reasoning. Do not delete for elegance. Burden of proof is on deletion. Timo's pushback is diagnostic, not resistance.
- [Subagent Output Is Advisory](feedback_subagent_output_advisory.md) - Diagnosis = trust. Prescription = QC. "Do everything" is permission to act, not a waiver of filtering. 2026-04-22 hidden-deduction incident.
- [Chat Review Before Zernio Push, Ask For LinkedIn/FB Media](feedback_chat_review_before_push.md) - Never push to Zernio without chat approval (any mode). For LinkedIn/FB, ASK Timo for image or PDF carousel before upload. 2026-04-28 $1k-website-Claude-Code correction.
- [Show Full Proposal In Chat Before Render](feedback_proposal_show_full_in_chat.md) - Paste FULL proposal MD into chat after every draft / meaningful edit. Never describe + ask "ready to render?" without showing content. 2026-05-09 MSJ proposal incident.
- [Proposal Value Communication](feedback_proposal_value_communication.md) - 7 rules for outcome-first proposal writing. Lead with outcomes not systems. Find the specific pain hook. Consulting BEFORE pricing always. Don't price-anchor consulting. Order systems by client value not technical dependency. Name goal-driven deliverables. Use credibility markers. Banned jargon list + 7-point verdict gate. 2026-05-10 Victor Alegria session, 5 rewrites required.
- [Never Fabricate Week-by-Week Schedules](feedback_never_fabricate_timelines.md) - Do NOT invent specific weekly deliverables in Delivery Timeline. Use only the sequence Timo has stated. Coarse phases beat fake weekly rows. Phase 2 trigger language must match Timo's exact words. 2026-05-09 Otto, 2026-05-11 Victor.
- [Down Payment Before Total](feedback_down_payment_before_total.md) - In pricing sections, the down payment dollar amount MUST appear in the document BEFORE the engagement total. Payment phases table first, line items second (framed as "what that $X covers"). Reader's first big dollar number is always the kickoff, never the total. 2026-05-11 Victor (repeat violation; Timo: "I told you this before, and yet you still do it over and over and over and over again").
- [Show Plan In Chat Before ExitPlanMode](feedback_show_plan_in_chat_before_exit.md) - Paste full plan content into chat as text BEFORE calling ExitPlanMode. Plan file is invisible to Timo until approval. 2026-05-09 Ilan Morgenstern proposal correction.
- [Audit State Before Prescribing](feedback_audit_state_before_prescribing.md) - Before proposing a fix workflow, audit the state. Test the assumption that defines the problem. 2026-04-15 GitHub token rotation was busywork because I never tested if token was still live (dead) or if gh CLI was handling auth (it was). Canonical: ~/.claude/knowledge/audit-state-before-prescribing.md.
- [Don't Caveat What You Can Fix](feedback_dont_caveat_what_you_can_fix.md) - If the workaround is "go fix the input yourself" and the input is accessible, patch it at process time. Shipping with a caveat = laziness. 2026-04-19 transparent render backdrop strip.
- [Read Inputs Not Conventions](feedback_read_inputs_not_conventions.md) - When Timo attaches specifically-named files (e.g., "Endorsers Carousel.html" + carousel.jsx), use those. Never fall back to tool default entry points. 2026-04-19 rendered sheet music when he wanted the carousel.
- [Find Files Before Spawning Agents](feedback_find_files_before_spawning.md) - When Timo says a file is "in Downloads" or "in [X] workspace", run ls FIRST, pass absolute paths to subagents. Subagents do NOT see the parent's attached PDFs. 2026-04-23 RR Apr 8 transcript incident.
- [Match Referenced Structure Exactly](feedback_match_reference_exactly.md) - When Timo provides a reference and says "do not deviate," replicate literally. No exec summaries, no TL;DRs, no readability additions. 2026-04-20 proposal-writer iteration 3 broke this three ways. Price placement is strategic; never move it earlier than the reference places it.
- [Pricing Rules. Section Order, Line Items, Never In Header](feedback_pricing_section_always_last.md) - 3 rules. (1) Order: Requested → Systems → Timeline → PRICING → Next Steps → PROTECTIONS (last). (2) Line-item per component, never lump-sum. (3) Price NEVER appears outside the pricing section. No $ in header/subtitle/scope. 2026-04-25 Robinson's iteration 3.
- [Proposals Are Malleable. Never Copy Reference Assumptions](feedback_proposals_are_malleable.md) - Each new client requires re-interrogating jurisdiction, term, pricing model, compliance clauses, component count. The reference is STRUCTURE, not CONTENT. Default to Texas (Timo LLC home) for unknown jurisdictions, FLAG the default. 2026-04-25 Robinson's. I copy-pasted CA legal language from Harrisson without checking.
- [Proposal Default Pattern. Harrisson, Not Artifact](feedback_proposal_default_pattern.md) - Default to Harrisson 6-section lean signable contract. Artifact 11-section enterprise pitch is opt-in only. Commission + flat fee hybrid, 40/60 build-and-prove, 90-day guarantee, AAA arbitration, full handover clause. Jurisdiction/legal language is per-client (see Proposals Are Malleable).
- [Contract Signature Block Format](feedback_contract_signature_format.md) - Every contract gets a parallel 2-column signature block with 5 labeled fields per side (Business Name, Full Name, Email, Signature, Date Signed). Timo's address as subtitle, Business Name + Full Name + Email pre-filled. NO AcroForm widgets (DocuSign overlays its own).
- [Proposal PDF Dual-Save Rule](feedback_proposal_pdf_dual_save.md) - Every proposal PDF goes to BOTH ~/Downloads/ AND output/proposals/{client-slug}/ in the project. Never just one. Cp on the same turn as the Chrome render. 2026-04-27 Robinson's correction.
- [Proposal Render Gate. MD-Only Iteration Until Sign-Off](feedback_proposal_render_gate.md) - Iterate proposals in MD only via targeted Edits. NO Chrome, pdftoppm, PNG Reads, or HTML during iteration. Render PDF + visual QA ONLY when Timo says "approve / render / ship / send / final". 2026-04-27 Perplexity+NotebookLM research after 6-render Robinson's session.
- [Proposal Drafts Must Appear In Chat](feedback_proposal_show_full_draft_in_chat.md) - Paste full draft into chat as markdown after every Write/Edit. Pointing at the .md path is not review. 2026-05-09 IPO proposal. Timo had to ask to see the content.
- [Don't Label Client Deliverables As AI-Generated](feedback_dont_label_deliverables_as_ai.md) - Never write "AI-generated summary," "Fireflies AI agent," etc. in a proposal. Just "written summary" / "recording." 2026-05-09 IPO.
- [Never Downplay Production Quality](feedback_never_downplay_production_quality.md) - Banned: "no promises of premium," "expect functional not exceptional," "basic," "sufficient." Differentiate scope tiers by deliverable shape, never by quality apology. 2026-05-13 Ilan System 5.
- [Never Name Other Clients In A Proposal](feedback_never_name_other_clients_in_proposal.md) - Banned in every client-facing proposal: every other active client's name, company, founder, brand. Use generic substitutes ("a custom dashboard," "the pattern we use"). Enforced via hook ~/.claude/hooks/proposal-cross-client-leak-gate.sh + registry ~/.claude/banned-cross-client-names.txt + SKILL Gate 4 + Layer 2 reviewer. 2026-05-12 Ilan proposal had "Harrison Ball pattern" 3x.
- [Robinson's Proposal Process. 100 Lessons + Repetition Patterns](feedback_robinsons_proposal_lessons.md) - 100 themed lessons from the 12-iteration Robinson's Remedies proposal arc (2026-04-25 to 2026-04-28). Diagnostic of repetition patterns (where Timo had to repeat himself), top 5 actionable rules for next proposal, scoped-fix-leak failure modes. Read before any new proposal session.

## Content Voice / Strategy
- [Content Angle Evaluation](feedback_content_angles.md) - Audit the frame before ranking options. Every angle needs an enemy.
- [ICP Segmentation Default](feedback_icp_segmentation.md) - When Timo says "5 ideas" default to 5 ICPs not 5 angles.
- [Content Generation Craft](feedback_content_generation_craft.md) - 5 patterns that move Power Content scores up.
- [Don't Wait For The Punchline](feedback_dont_wait_for_punchline.md) - Write the behavioral diagnosis in Timo's voice, don't just name the category.
- [Six-Point Content Hook Gate](feedback_six_point_content_hook.md) - Every deck/VSL/social must pass 6-point check.
- [Public Client Claims Rules](feedback_client_claims.md) - Never name specific clients or dollar amounts in public content.
- [CTA Language: Chat with Tim](feedback_cta_language.md) - Never write "strategy call", "coaching call", "free consultation". Default: "Book a chat with Tim". Anti-guru.
- [Web Build Principles](feedback_web_build_principles.md) - 11 overarching rules for ANY website build. RULE 0: ask 4-6 sharp forced-choice questions FIRST (accent / type voice / CTA / reference / assets / anti-patterns). Then: reference > convention > design-kit. Interrogate marketing defaults. Copy voice matches visual voice. Smaller type, more spacing. Elegant placeholders. Volume > polish on proof. Literal spatial directives. Anti-guru everywhere. Color-coded dark-surface elevation. Pre-build plan.
- [Red Highlight Is Hero-Reserved](feedback_highlight_reserved_for_hero.md) - The red .hi pill treatment belongs on the hero headline + 1 climactic statement. Never on section H2s, CTA headings, FAQs. Max 2 per page. 2026-04-20 landing-playstation-v2 caught "My Music Business Journey" dupe.

## Slide / Deck Craft
- [Slide Typography Hierarchy](feedback_slide_hierarchy.md) - Supporting text 20-25% of hero, not 60-70%.
- [Viewport Overflow Check](feedback_viewport_overflow_check.md) - Verify LAST CHARACTER within frame + 80px breathing room.
- [QA at Safari Real Viewport](feedback_qa_at_safari_real_viewport.md) - Render at 1440x680 min. Safari chrome eats 100-200px.
- [Image Fit Or Cut](feedback_image_fit_in_slides.md) - If image fights headline, kill it.
- [Never Parallel For Causal](feedback_never_parallel_for_causal.md) - Never use 3-column triptych for causal/sequential items.
- [One Beat Per Slide](feedback_one_beat_per_slide.md) - Never stack 3 instances of same pattern.
- [Accent Slides Stay Minimal](feedback_accent_slides_stay_minimal.md) - NEVER add body paragraphs to hook/warning/pivot/transition slides. Headline IS the slide. Accent slides are rhythm slides, not evidence slides. If slide has `<p>` with 10+ words and isn't content/evidence/closer, delete it. Timo corrected this 3x in one session on views-that-matter.
- [Evidence vs Atmosphere](feedback_evidence_vs_atmosphere.md) - Sales deck images must literally show the claim.
- [Deck Sweep Gates](feedback_deck_sweep_gates.md) - 3 gates before declaring multi-slide deck done.
- [Deck Flow QA](feedback_deck_flow_qa.md) - Read top-to-bottom as continuous script after any edit.
- [Slides Connect Idea-To-Idea](feedback_idea_connection.md) - Every slide needs antecedent in prior slide.
- [Serve Thesis Not Slot](feedback_serve_thesis_not_slot.md) - Empty placeholders beat off-thesis filler.
- [Generate Don't Placeholder](feedback_generate_dont_placeholder.md) - Specific real-world visuals = generate via Gemini, not CSS icons.
- [Gates Are Guidance Not Prescription](feedback_gates_are_guidance_not_prescription.md) - Never apply content gates mechanically to hook slide.
- [List Elements Before Rebuilding](feedback_audit_before_rebuild.md) - ADD does not mean REPLACE.
- [Case Study Slide Pattern](feedback_case_study_slide_pattern.md) - Citing brand A/B tests needs logo + context + mockup + result + source.
- [Warning Slide Pattern](feedback_warning_slide_pattern.md) - Canonical gold warning triangle icon, not just text badge.
- [Validated Slide Patterns](feedback_validated_slide_patterns.md) - Specific layouts Timo explicitly approved.
- [Presentation Design Rules](feedback_presentations.md) - No reused images, show prompts not code, full-screen.
- [Presentation Draft Mode](feedback_presentation_draft_mode.md) - Draft slide-by-slide first, invoke frontend-slides only after approval.
- [Placeholder Images](feedback_placeholder_images.md) - Styled CSS boxes, not AI portraits of Timo.
- [Screenshot Source Quality](feedback_screenshot_source_quality.md) - Pull from live URL at 2x, not IDE thumbnails.
- [Visual QA Before Done](feedback_visual_qa.md) - Open in Safari, check every changed slide for overflow.
- [Mobile QA Use Playwright Viewport](feedback_mobile_qa_use_playwright_viewport.md) - Headless Chrome --window-size=390 --force-device-scale-factor=2 renders at 195 CSS px (HALF a phone) = FALSE clipping. Verify overflow numerically (scrollWidth vs clientWidth) at true 390px via Playwright before "fixing" a responsive bug. 2026-06-07 fb-funnel phantom-overflow incident.

## Workflow Rules
- [Proactive Task Management](feedback_proactive_tasks.md) - Ask about task completion, don't wait to be told.
- [Do It Yourself](feedback_do_it_yourself.md) - Never delegate setup to Timo. Install, create, script.
- [Test Locally First](feedback_test_locally_first.md) - Test serverless before deploying. Base64 encode private keys.
- [Perplexity DB Protocol](feedback_perplexity_db_protocol.md) - ALWAYS grep perplexity_research_database.md before sonar-pro query.
- [Gemini API Direct](feedback_gemini_api_direct.md) - Call Gemini via curl, never MCP servers.
- [Google Sheets Integration](feedback_google_sheets_integration.md) - Vercel serverless + service account pattern.
- [Vercel env add: no echo](feedback_vercel_env_add_newline.md) - Use `printf '%s'`, not `echo`, when piping secrets to `vercel env add`. Echo's newline gets stored literally and breaks API calls with opaque 500s.
- [No Parallel Chrome Screenshots](feedback_no_parallel_chrome_screenshots.md) - Run sequentially or in batches of 3-4 max.
- [Verify Image Files Before Reading](feedback_verify_image_before_read.md) - Run `file` after curl. Tiny PNGs are HTML errors.
- [ADHD Enforcement Requires Hooks](feedback_adhd_enforcement.md) - Only forced UserPromptSubmit hook injection works.
- [Session Clock Is Not Engagement](feedback_session_clock.md) - Elapsed timer counts from session start, not active use.
- [Content Follows Video Order](feedback_content_order.md) - Mirror video's sequence when updating pages from transcripts.
- [Easy Path Default](feedback_easy_path_default.md) - Reach for the simplest working option first.
- [Priorities Display](feedback_priorities_display.md) - How priorities surface in morning email.

## References
- [Content Suggestions Upload](reference_content_suggestions_upload.md) - How to push IG/TikTok tiles to a client dashboard's Content Suggestions. Shared Supabase agbldmgbxzrrxznwbxar, client_ids, og:image + TikTok oembed thumbnail download, deploy via vercel CLI.
- [API Keys Location](reference_api_keys.md) - API keys live in ~/.zshrc. Grep there FIRST. Includes FIREFLIES_API_KEY + Fireflies GraphQL quick ref.
- [Snapshots Folder Location](reference_snapshots_folder.md) - Screenshots pasted into chat live at ~/Desktop/Snapshotsss/ (THREE s's). Sort by mtime, use glob pattern (not quoted name) to cp. Do NOT say "paste didn't save."
- [Timo Headshot Canonical](reference_timo_headshot_canonical.md) - Master portrait path. NEVER AI-generate Timo.
- [Timo LLC Address Pflugerville](feedback_timo_llc_address_pflugerville.md) - Timo LLC is at 900 East Pecan Street, Ste 300, Pflugerville, TX 78660. NEVER "Austin, Texas" on contracts. 2026-05-09 ISO proposal incident.
- [Steve Parker Case Facts](feedback_steve_parker_facts.md) - Under-1-min video, 800K views, KUT News, several revisions, hook borrowed from piano-tuning niche. Stale numbers in brand.md / TIMO_PROFILE / email-system. Re-read before drafting.
- [Shared Image Library](reference_shared_image_library.md) - Gemini-generated assets inventory.
- [Conservatory Page vs FB Ads Funnel (DO NOT CONFUSE)](reference_conservatory_landing_page.md) - TWO separate properties: (1) Creator Conservatory page = output/landing-playstation/index.html ("Book A Chat With Tim"); (2) FB ads funnel = output/fb-funnel/ (email capture to VSL to booked.html). Do NOT bolt funnel parts onto the Conservatory page. 2026-06-06 conflation incident.
- [Gemini Image API](reference_gemini_image_api.md) - Working curl call, model `gemini-2.5-flash-image`.
- [Ottaviano Cristofoli (Otto)](reference_ottaviano_cristofoli.md) - Principal trumpet Japan Phil, full profile.
- [Claude Routines (Claude Code feature)](reference_claude_routines.md) - Routines ARE in Claude Code. `/schedule` CLI creates them; sync across CLI/Desktop/web. Cloud-run, schedule/API/GitHub triggers. Docs: https://code.claude.com/docs/en/routines
- [Hook Library Client Access](reference_hook_library_client_access.md) - hooks.html is client-visible READ-ONLY on all 4 dashboards (2026-06-10). Access gated in FOUR layers: RLS + boot guard + allow_pages + nav reveal. Check the DB first when un-gating any page.

## Projects
- [Skool Scraper Setup](project_skool_scraper.md) - Apify engagement analyzer, blocked on usage reset.
