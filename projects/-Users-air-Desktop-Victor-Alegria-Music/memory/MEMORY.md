# Victor Alegria Music - Memory Index

> Cloned from Precision Brass on 2026-05-25. SOUL.md / PRIORITIES.md / SESSION_LOG.md are GLOBAL (`~/.claude/`) and apply automatically. This index covers per-project memory only.

- [user_timo_profile.md](user_timo_profile.md) - Full Timo profile. READ FIRST. (Same person across all workspaces.)
- [project_clone_status.md](project_clone_status.md) - What was cloned from PB, what is still PLACEHOLDER, and the Phase 0/3/4 fill-in list. READ to know the build state.
- [project_dashboard_live.md](project_dashboard_live.md) - Dashboard LIVE at victor-alegria-music.vercel.app, own Supabase (ref agbldmgbxzrrxznwbxar), PB-style login working.
- [project_one_super_system_multitenant.md](project_one_super_system_multitenant.md) - ONE multi-tenant app for ALL coaching clients (content_clients/content_items + admin switcher). Do NOT clone separate per-client deploys. Victor+Sohee+Tzu all tenants.
- [project_voc_database.md](project_voc_database.md) - VOC DB from 29 call transcripts. 138 quotes, voice bank, confirmed trombone/audition-prep ICP. Verify names+pricing+claims.

## Universal lessons (copied verbatim from PB - apply to all client work)

### Dashboard / deploy bug-class
- [feedback_canvas_destroy_on_empty_state.md](feedback_canvas_destroy_on_empty_state.md) - Never innerHTML= a Chart.js canvas parent on empty state.
- [feedback_idb_for_large_client_cache.md](feedback_idb_for_large_client_cache.md) - IndexedDB for 10+ entries or >50KB; localStorage thrashes on Safari.
- [feedback_vercel_kills_fire_and_forget.md](feedback_vercel_kills_fire_and_forget.md) - Await side-effect writes; Vercel kills lambdas on response.
- [feedback_html_no_store_for_safari_cache.md](feedback_html_no_store_for_safari_cache.md) - no-store headers for HTML or Safari serves stale.
- [feedback_dashboard_iframe_needs_full_html.md](feedback_dashboard_iframe_needs_full_html.md) - iframe srcdoc needs full HTML doc, not body innerHTML.
- [feedback_new_route_check_auth_allowlist.md](feedback_new_route_check_auth_allowlist.md) - New route = update lib/config.js allow_pages.
- [feedback_verify_user_facing_url_before_handoff.md](feedback_verify_user_facing_url_before_handoff.md) - Read vercel.json + curl 200 before sharing a URL.
- [feedback_verify_after_deploy_walk_the_flow.md](feedback_verify_after_deploy_walk_the_flow.md) - Walk the click path after deploy; redirect = FAIL.
- [feedback_verify_with_eyes_not_curl.md](feedback_verify_with_eyes_not_curl.md) - Confirm fixes with Playwright/Safari + own eyes, not curl alone.
- [feedback_ui_bug_diagnostic_protocol.md](feedback_ui_bug_diagnostic_protocol.md) - UI bug diagnostic protocol.

### Process / correctness
- [feedback_check_capability_before_offloading.md](feedback_check_capability_before_offloading.md) - Check what I already have / can do BEFORE asking the user. "I can't" is a conclusion, not a reflex.
- [feedback_audit_full_target_state_before_clone_deploy.md](feedback_audit_full_target_state_before_clone_deploy.md) - Clone/deploy = diff the FULL target state (DB, tables, RLS, auth, per-role nav) up front, not reactively.
- [feedback_clone_means_render_like_source.md](feedback_clone_means_render_like_source.md) - A clone is done when it RENDERS like the source (structure->rows->referenced files), verified by viewing it, not by "table exists"/"0 errors".
- [feedback_diagnose_dont_guess.md](feedback_diagnose_dont_guess.md) - Runtime diagnostic on move 2, not move 8.
- [feedback_root_cause_before_patch.md](feedback_root_cause_before_patch.md) - Trace full flow before patch #2.
- [feedback_no_seed_data.md](feedback_no_seed_data.md) - Never seed demo/fake rows. Empty state is correct first-run.
- [feedback_query_destination_schema_first.md](feedback_query_destination_schema_first.md) - select=* a known row and diff before first push.
- [feedback_chat_draft_before_render.md](feedback_chat_draft_before_render.md) - Show full draft in chat before any Write/render.
- [feedback_save_credentials_immediately.md](feedback_save_credentials_immediately.md) - Save pasted keys before next tool call.
- [feedback_ship_right_not_fast.md](feedback_ship_right_not_fast.md) - TOP RULE. Ship right, never fast at cost of correctness.
- [feedback_ship_polish_not_skeleton.md](feedback_ship_polish_not_skeleton.md) - 7-point UI polish checklist before declaring done.
- [feedback_zero_drop_ingestion.md](feedback_zero_drop_ingestion.md) - Preserve every labeled section when ingesting structured content.
- [feedback_dont_silently_skip.md](feedback_dont_silently_skip.md) - When named source != reality, ASK.
- [feedback_classifier_verification_must_use_ground_truth.md](feedback_classifier_verification_must_use_ground_truth.md) - Verify classifiers against human ground truth, not a re-implementation.
- [feedback_dedup_all_active_statuses.md](feedback_dedup_all_active_statuses.md) - Dedup queue tables across all active statuses.
- [feedback_audit_links_at_url_level.md](feedback_audit_links_at_url_level.md) - Dedup links by destination URL, not anchor text.
- [feedback_cite_primitives_never_fabricate.md](feedback_cite_primitives_never_fabricate.md) - Cite real sources; never fabricate.
- [feedback_never_ship_placeholder_urls.md](feedback_never_ship_placeholder_urls.md) - Never ship placeholder URLs to production.
- [feedback_master_lessons.md](feedback_master_lessons.md) - 4 core rules: auto-transcripts lie, client drafts != fact, prospects != customers, unusual = verify.

### Email / content engine (universal mechanics)
- [feedback_never_test_send_to_real_list.md](feedback_never_test_send_to_real_list.md) - ADAPT: PB uses AC list 20. Set Victor's safe test list before any test send.
- [feedback_dup_send_db_gate.md](feedback_dup_send_db_gate.md) - DB gate against duplicate sends.
- [feedback_skip_dups_silently.md](feedback_skip_dups_silently.md) - Silently skip dashboard-push duplicates.
- [feedback_no_internal_jargon_in_rationale.md](feedback_no_internal_jargon_in_rationale.md) - Plain English in dashboard rationale.
- [feedback_subjects_speak_to_reader.md](feedback_subjects_speak_to_reader.md) - Subject lines speak to the reader.
- [feedback_quote_sourcing_minimums.md](feedback_quote_sourcing_minimums.md) - ADAPT: each proposal needs testimonial + sales-call quote (re-anchor to Victor's VOC).
- [feedback_use_lightweight_youtube_fetch.md](feedback_use_lightweight_youtube_fetch.md) - Use curl+oEmbed for YouTube metadata, not Playwright.
- [feedback_pdfs_to_downloads.md](feedback_pdfs_to_downloads.md) / [feedback_pdf_only_to_downloads.md](feedback_pdf_only_to_downloads.md) - PDF deliverables to ~/Downloads.

## NOT cloned (PB-specific - to be rebuilt for Victor in Phase 3/5)
Harrison voice/age/spelling/email-call, the converter template, masterclass/winning-emails/lessons corpora, hook-structure, lead-with-technique, bullet-anchors, email-voice-load-order, pb-script-write lessons, the 8-agent restructure notes. These encode Harrison's voice + PB content state and must be re-derived from Victor's own material.
