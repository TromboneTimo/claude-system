---
name: Harrison future build items
description: Ads system and Fathom integration planned for after current workspace is tested and validated
type: project
originSessionId: 2f4ef775-0ad8-47f0-b205-f0de8c56f7ca
---
## Future Build Items (NOT NOW)

1. **Fathom call analyzer** - n8n workflow that pulls Harrison's new sales call transcripts, extracts pain points/objections/closing language, and feeds them into the content system automatically. Prerequisite for the email system.

2. **Email sequence builder** - Klaviyo integration. Fathom data feeds a "strategy brain" that rotates email angles from real sales conversations. Plain text heavy (75/25). Tracks opens, clicks, calls booked, deals closed.

3. **Ad creation from Fathom data** - System auto-generates Facebook ad copy variations from new prospect pain points as they come in from calls. Currently using static prospect-psychology.md data (19 prospects).

4. **Facebook DM setter system** - Captures missed organic leads from the 3,000+ unanswered comments. Automated first response + human handoff.

5. **Meta Ad Library API hookup for fb-vault** [added 2026-04-25] - Currently `fb-vault` ingests Facebook ads manually (Timo pastes copy + drops creative file + types performance numbers). When Timo is ready, wire up the Meta Marketing API to auto-pull Harrison's own ad creative, copy, audience, and performance numbers via ad_id. For competitor ads, wire up the Ad Library API. Process_ad.py already has an `--ingestion-source` flag that should flip to `api` once wired up. Needs Meta App ID + secret + ads_read access token. Footnoted in `Precision-Brass/voc/meta-ads/README.md` and the `fb-vault` SKILL.md "Future work" section.

6. **AC + HYROS sync for email-analytics.html** [added 2026-04-28] - Currently the analytics page reads from Supabase `email_sends` table populated by the "Log a Send" manual entry form on the page. Phase 2: build `scripts/sync-email-stats.mjs` (Node.js CLI) that pulls AC campaign metrics (opens, clicks, replies, unsubscribes, list size) via `/api/3/campaigns?orders[sdate]=DESC&limit=50` and HYROS attribution per UTM (`utm_campaign=<ac_campaign_id>`) for booked_calls, closed_deals, direct_revenue, assisted_revenue. Upsert to `email_sends` keyed on `id = ac_campaign_id`. Cadence: manual at first via `node scripts/sync-email-stats.mjs`. Later: cron via `/routines`. Env vars already set in `dashboard/setup/.env.example` (ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY, HYROS_API_KEY, SUPABASE_SERVICE_ROLE_KEY). Timo has the API keys ready; this is a "wire it up" task, not a "design it" task. Reference: `~/.claude/plans/i-need-to-create-serene-truffle.md` and `dashboard/setup/schema.sql` (email_sends table).

7. **AC publish step from Harrison's approved drafts** [added 2026-04-28] - When Harrison approves an email proposal in dashboard/emails.html, the "Send to ActiveCampaign" button is currently disabled (Phase 2). Build the AC campaign-create API call so an approved + scheduled `email_proposals` row fires a real AC campaign with the body, subject, preheader, and audience tag mapped to AC list segments. After send, populate `email_proposals.ac_campaign_id`. Combined with #6 above, this gives a closed loop: pb-email -> Harrison approves -> AC sends -> stats sync back -> analytics updates.

**Why:** These all depend on the Fathom analyzer being built first. The analyzer extracts the psychological data that feeds everything else. Build order: Fathom analyzer -> email sequences -> ad automation -> DM system. The Meta Library hookup is independent and can be done any time the manual fb-vault ingestion gets too painful.

**When:** After Hook Book ships and the current Precision-Brass workspace is tested and validated with real content.
