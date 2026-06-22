---
query: "HYROS API call states (BOOKED SHOWED_UP NO_SHOW DISQUALIFIED CANCELED RESCHEDULED CLOSED), Calendly native integration auto-tagging, custom source tagging for YouTube and ManyChat using sl and htrafficsource URL params, lead.id join across leads/calls/sales endpoints for click-to-call-to-sale funnel"
query_hash: "a4da1b6e78d7b5f8"
slug: "hyros-api-call-states-booked-showed-up-no-show-disqualified-"
model: "sonar-pro"
date: "2026-05-06"
workspaces:
  - Precision-Brass
category: "APIs / Integrations General"
tags:
  - hyros
  - api
  - attribution
  - calendly
  - funnel
  - call-tracking
  - manychat
  - youtube
  - dashboard
keywords:
  - calendly
  - hyros
  - call
  - api
  - lead.id
  - calls
  - custom
  - docs
  - integration
  - leads
  - manychat
  - native
  - sales
  - source
  - youtube
citations_count: 10
synthesized_in_notebooklm: false
stale_after: "2026-11-02"
---

# HYROS API call states (BOOKED SHOWED_UP NO_SHOW DISQUALIFIED CANCELED RESCHEDULED CLOSED), Calendly native integration auto-tagging, custom source tagging for YouTube and ManyChat using sl and htrafficsource URL params, lead.id join across leads/calls/sales endpoints for click-to-call-to-sale funnel

## Key findings

**Q1: Call state values (/v1/api/v1.0/calls)**  
Valid: BOOKED, SHOWED_UP, NO_SHOW, DISQUALIFIED, CANCELED, RESCHEDULED, CLOSED (likely; matches Calendly statuses).  
Zapier events (Retrieve/Create/Update Call) support `state` param [1].  
Set via: Manual API/Zapier + auto from native Calendly integration (Q2). No explicit auto/manual split in docs.

**Q2: Native Calendly integration**  
Setup auto-tags SHOWED_UP/NO_SHOW etc. without manual marking.  
Fetch: https://hyros-docs.vercel.app/llms.txt → calendly.txt [2][3][5][6].

**Q3: Source naming for YouTube/ManyChat**  
Use custom: `youtube` / `manychat` (param/UTM). HYROS auto-detects only Facebook/Instagram/TikTok/Google [no custom source docs; inferred from integrations list [2][3]].

**Q4: Shared lead.id across /leads /calls /sales**  
Yes; unifies click→call→sale funnels by `lead.id` (email/phone). Update leads endpoint uses lead.id/email/phone [1]. No explicit sales endpoint doc, but standard attribution flow.

**Primary sources:**  
[1] https://hyros.com/updates/changelog/version-2-2/  
[2-6] Index: https://hyros-docs.vercel.app/llms.txt (then calendly.txt, etc.)

## Citations:
[1] Version 2.2 - HYROS - https://hyros.com/updates/changelog/version-2-2/
[2] Advanced Call Tracking - HYROS Docs - https://docs.hyros.com/docs/advanced-call-tracking
[3] HYROS Documentation - Setup Guides & API Reference - https://docs.hyros.com
[4] Hyros · Apiary - https://hyros.docs.apiary.io
[5] Standard Funnel - HYROS Docs - https://docs.hyros.com/docs/standard-funnel
[6] Tracking General Email Softwares – Advanced guide - HYROS Docs - https://docs.hyros.com/docs/tracking-general-email-softwares-advanced-guide
[7] Deploy cold email campaigns to Email Bison or I ... - Lead Gen Jay - https://leadgenjay.com/skills/cold-email-campaign-deploy
[8] HYROS Community - https://community.hyros.com
[9] Hyros Offline Conversions: API Guide - LGG Media - https://www.lgg.media/blog/hyros-offline-conversions/

## Sources

- https://hyros-docs.vercel.app/llms.txt
- https://hyros.com/updates/changelog/version-2-2/
- https://docs.hyros.com/docs/advanced-call-tracking
- https://docs.hyros.com
- https://hyros.docs.apiary.io
- https://docs.hyros.com/docs/standard-funnel
- https://docs.hyros.com/docs/tracking-general-email-softwares-advanced-guide
- https://leadgenjay.com/skills/cold-email-campaign-deploy
- https://community.hyros.com
- https://www.lgg.media/blog/hyros-offline-conversions/