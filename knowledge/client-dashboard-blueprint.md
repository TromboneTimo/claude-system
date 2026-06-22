# Client Dashboard Blueprint

What I learned building the Precision Brass email + attribution dashboard, hardened into a reusable playbook for future clients. Two layers: **Section 1** is the universal pattern (visual + data layer rules that apply to ANY client dashboard); **Section 2** is the AC-specific implementation (use when the client runs ActiveCampaign).

Locked 2026-05-15 from the Precision Brass build.

---

## Section 1: Universal dashboard rules

These apply regardless of CRM/email tool. Codified after burning four rounds of UI rebuilds because I defaulted to "show everything."

### 1.1 Three-question intake (MANDATORY before writing any code)

Before any "build me a dashboard view" request, ask exactly these three:

1. **What's the ONE thing you want at-a-glance?** Forces specificity. If they say "I want to see everything," push back: "Pick one number or one row that's the most important. Everything else is supporting."
2. **What data feeds it?** Forces me to query the destination schema BEFORE building. Get the API endpoint, the table name, the field shape. (Per `~/.claude/projects/-Users-air-Desktop-Precision-Brass/memory/feedback_query_destination_schema_first.md`.)
3. **What's explicitly OUT of scope?** Forces me to NOT hedge with extra tabs/views. If they say "just X," do X. Do not build "All Sends" + "By Funnel" + "By List" + "By Whatever" tabs because "they might want it later." They won't.

If I skip these three questions, I will build the wrong dashboard and waste 3-5 rounds of iteration.

### 1.2 Hero card on top, sortable table below

Every dashboard view should have:

- **Hero card at the top.** The single most-important data point with full-context stats around it (5-tile grid is the right shape: primary metric + 4 supporting). Eyebrow label includes a relative timestamp ("X HOURS AGO") so the user knows recency at a glance.
- **Sortable table below.** Default sort = newest first (sent_at desc, created_at desc, etc). NEVER default to "best performing" because that buries today's data under historical winners.
- **NO tabs unless the user explicitly asks for multi-view navigation.** Tabs add cognitive load and break sort/filter state. One focused page beats six clever tabs.

### 1.3 Show "scheduled" vs "sent" vs "draft" visually

Future-dated rows should be visually distinct:

- 50-60% opacity on the row
- Yellow/orange "SCHEDULED" badge in the type column
- Dot placeholders for stat cells (so 0% open rate doesn't look like a failed send)
- Filter the hero card to `sent_at <= now` so future-scheduled rows don't displace the actual most-recent send

### 1.4 Real subject lines, not internal labels

Every email tool stores TWO names per campaign:
- The **internal label** ("Daily Email 1 [by user@gmail.com] -- 2026-05-15 11:00:00")
- The **inbox subject** that recipients actually see ("Mike added 3 notes to his range in one day")

These live in DIFFERENT places in the API. The campaign endpoint returns the label; the message/template endpoint returns the real subject. **Always show the real subject.** If you can't get it, show the label with an orange "PENDING SUBJECT" badge so the user knows it's a stopgap.

### 1.5 Default to all-time, not 30 days

For "what did I send" dashboards, default to all-time (or 1 year). 30-day defaults silently hide historical sends. If the user has 22 sends in the last 30 days but 200 sends in the last year, defaulting to 30d shows them 22 and they assume that's everything. Migration logic should auto-bump cached old defaults.

### 1.6 Audit at the URL/destination level, not the prose level

When deduplicating links, comparing entries, or filtering by name: compare the destination URL or canonical ID, NOT the visible text. Different anchor text can point to the same URL. Different display names can refer to the same database record. Always normalize and compare at the destination layer.

### 1.7 Cache-layer awareness

Modern dashboards have ~5 cache layers stacked. When a user reports stale data, debug them in this order:

1. **Browser localStorage** (date range, sort preference, filter state). Check via DevTools or just clear it.
2. **Browser HTTP cache** (HTML/JS/CSS). Hard-refresh (Cmd+Shift+R) or version your asset URLs (`?v=N`).
3. **Lambda warm cache** (in-process Map on serverless function). Restart by redeploying.
4. **Persistent cache** (Supabase api_cache table, Redis, etc.). Purge directly via SQL/HTTP.
5. **Upstream API** (the CRM, HYROS, etc.). Check rate limits + freshness windows.

If you can't tell which layer is lying, hit each one in order. Don't assume your code is wrong until you've ruled out all five.

### 1.8 Asterisk + VERIFY badge for unconfirmed data

Anything you've inferred or guessed (e.g., name-to-record mapping, attribution, classification) should render with an asterisk and an orange "VERIFY" badge until the user confirms. Don't fake-render confidence you don't have. If a HYROS source name doesn't match an entry in your database, render it with `*` + tooltip explaining what to fill in to confirm.

### 1.9 Lock the view to ONE focus per user request

If the user only cares about one list (one segment, one funnel, one product), hardcode that filter at the data layer. Don't expose a dropdown that lets them pick "all lists." The dropdown adds noise; the user already knows what they want.

### 1.10 Don't ship UI without clicking it

Before declaring a feature "done": load the page, click every interactive element, verify state changes. The All Sends button race condition that bit me for two rounds would have been caught in 5 seconds of manual click-testing. Per `canon_deploy_verification.md` (project memory).

---

## Section 2: ActiveCampaign-specific implementation

Use this when the client runs ActiveCampaign. Skip if they use ConvertKit / Mailchimp / Klaviyo / etc. (the patterns translate but the field names differ).

### 2.1 The data model

AC's API splits campaign metadata across multiple endpoints. You need ALL of them to render a useful dashboard row.

| Field | Endpoint | Notes |
|---|---|---|
| Campaign internal label | `/api/3/campaigns?orders[sdate]=DESC` (`c.name`) | Looks like "Daily Email 1 [by user@email] -- date". NOT the inbox subject. |
| **Inbox subject** | `/api/3/messages/{c.message_id}` (`m.subject`) | The line recipients actually see. Required for any UI that shows a "what was this email about." |
| **From name** | `/api/3/messages/{c.message_id}` (`m.fromname`) | "Harrison Ball" |
| **From email** | `/api/3/messages/{c.message_id}` (`m.fromemail`) | "harrissonball@precisionbrass.info" (note: client may have a typo in their actual sender domain, do NOT correct it client-side) |
| List name | `/api/3/campaigns/{id}/campaignLists` (`cl.campaignLists[0].name`) | "Daily Email 1". Required to filter by list. |
| Status | `c.status` | `5` = sent, `4` = scheduled, `1` = draft, etc. |
| Send time | `c.sdate` | ISO with offset. Future = scheduled, past = sent. |
| Total sent | `c.send_amt` (or `c.total_amt`) | Recipients delivered |
| Unique opens | `c.uniqueopens` | NOT `total_unique_opens` (don't invent field names) |
| Unique link clicks | `c.uniquelinkclicks` | NOT `total_unique_clicks` |
| Open tracking enabled | `c.trackreads` | `1` = on. Old campaigns may have `0` and show 0% open rate forever. |
| Link tracking enabled | `c.tracklinksanalytics` | `1` = on |
| Replies | NOT in AC API | AC's `/api/3/campaigns` does NOT expose reply counts. Either install AC's reply webhook (`/api/ac-reply-webhook` pattern) and store counts in your own DB, or accept "0" with a tooltip explaining. |

### 2.2 Broadcasts vs automation-driven sends

AC returns `c.type='single'` for EVERY campaign in most accounts (verified against hballmusic.api-us1.com 2026-05-06). The `c.type` field is useless for distinguishing broadcasts from automation sends.

**The actual signal:** `c.automation`. Numeric automation ID = automation-driven; null/0/empty = true broadcast.

```js
const isAutomationDriven = c.automation != null && String(c.automation) !== '0' && String(c.automation) !== '';
const type_bucket = isAutomationDriven ? 'automation' : 'broadcast';
```

### 2.3 Required enrichment passes (parallel)

After the initial campaigns fetch, run TWO parallel enrichment loops over ALL sends (not top-N, historical rows need enrichment too, otherwise they get filtered out by null-list-name rules):

```js
// Pass 1: list_id + list_name from /api/3/campaigns/{id}/campaignLists
await Promise.all(sends.map(async (s) => {
  const cl = await acGet(`/api/3/campaigns/${s.id}/campaignLists`);
  const first = (cl.campaignLists || [])[0];
  if (first) { s.list_id = String(first.listid || first.list); s.list_name = first.name; }
}));

// Pass 2: real subject + from info from /api/3/messages/{message_id}
await Promise.all(sends.map(async (s) => {
  if (!s.message_id) return;
  const mj = await acGet(`/api/3/messages/${s.message_id}`);
  const m = mj.message || mj;
  if (m.subject) s.subject = m.subject;
  if (m.fromname) s.fromname = m.fromname;
  if (m.fromemail) s.fromemail = m.fromemail;
}));
```

Both calls are per-campaign so they're N requests. AC's rate limit is generous (5 req/sec sustained per account); 200 campaigns = ~40s wall-clock with concurrency=200, much less in practice. Cap concurrency at 500 if needed.

### 2.4 Cross-channel attribution caps (when paired with HYROS)

If you join AC sends with HYROS attribution data (sales/clicks per source), the per-channel `sales / calls` ratio can exceed 100%. This is NOT a bug. HYROS attributes sales and calls independently by first-touch source. A sale can be attributed to YouTube without ever going through a YouTube-attributed call (cross-channel attribution).

**Display rule:** cap display at 100%, expose `raw_call_to_sale_rate` so UI can render `100%*` with a tooltip explaining the cross-channel cause. Same pattern as `call_close_rate` cap. Per project memory `canon_attribution_analytics.md` for related ground-truth rules.

### 2.5 Reply tracking requires a webhook

AC's API does not return reply counts. To track replies you need to:

1. Set up an AC webhook that fires on inbound reply events
2. Receive at `/api/ac-reply-webhook` (or equivalent)
3. Insert into a Supabase table like `email_replies(campaign_id, replied_at, lead_email)`
4. Aggregate in your dashboard query

The AC webhook UI is at `Settings, Developer, Webhooks, Add, Reply event`. Documentation: https://help.activecampaign.com/hc/en-us/articles/115000013844

### 2.6 Sender info is on the campaign source, NOT hardcoded

Per `canon_email_shipping.md` (project memory): when sending via the dashboard, `fromname` and `fromemail` come from the AC source campaign the user picks at send time. NEVER hardcode the sender display in the inbox preview. The dashboard updates the avatar initial + sender chip on dropdown change.

### 2.7 Lambda cache + Supabase api_cache pattern

For any server-side proxy to AC (or HYROS), implement a 3-tier cache:

```
Tier 1: in-process Map (lambda lifetime)
Tier 2: Supabase api_cache table (survives deploys)
Tier 3: AC upstream
```

Cache entries can be kept indefinitely if the data doesn't change often, OR you can add a TTL. For a daily-email dashboard, indefinite + manual `?force=1` button is fine. Just remember to PURGE the Supabase cache when you change the response shape (e.g., when you add a new enriched field), or users will see stale payloads with missing fields.

### 2.8 Common AC dashboard mistakes to avoid

- **Filtering by `c.type='broadcast'`** = wrong, every campaign is `type='single'`. Use `c.automation` instead.
- **Showing `c.name` as the subject** = wrong, that's the internal label. Use `/messages/{message_id}.subject`.
- **Sorting by `sent_at` without filtering future** = wrong, scheduled drafts displace today's actual send.
- **Defaulting the date range to 30 days** = wrong, hides historical sends.
- **Top-N enrichment slice** = wrong, historical rows get null fields and get silently filtered.
- **0 opens after a real send** = check `c.trackreads`. If 0, open tracking was disabled on that campaign. Not a bug, just no data.
- **Reply count = 0** = check whether the AC reply webhook is wired up. If not, AC returns 0 by default for everything.

---

## Section 3: When the client doesn't use ActiveCampaign

Mimic the visual layout from Section 1 (hero + sortable table, scheduled badges, real subject, all-time default, etc.) but adapt the field names + endpoints for the client's CRM:

| If client uses... | Subject lives at... | List/segment lives at... | Reply tracking... |
|---|---|---|---|
| ConvertKit | `/v3/broadcasts/{id}` (`subject`) | `/v3/broadcasts/{id}` (`thumbnail_url` + custom segments) | Not natively, use webhook |
| Mailchimp | `/3.0/campaigns/{id}` (`settings.subject_line`) | `/3.0/campaigns/{id}` (`recipients.list_id`) | Not natively, use webhook |
| Klaviyo | `/api/campaigns/{id}` (`attributes.name` + `attributes.subject`) | `/api/segments/{id}` | Not natively, use webhook |

The **patterns transfer** (hero, sort newest first, real subject, scheduled badge, etc). Only the field names + endpoints change.

---

Related project memory:
- `feedback_query_destination_schema_first.md` (PB project)
- `feedback_audit_links_at_url_level.md` (PB project)
- `canon_email_writing.md` (PB project)
- `feedback_use_lightweight_youtube_fetch.md` (PB project)
- `canon_deploy_verification.md` (PB project)

Reference dashboard implementation: https://github.com/TromboneTimo/precision-brass-dashboard
