---
query: "HYROS Calendly integration auto vs manual call state tracking, what HYROS auto-captures from Calendly bookings vs what requires manual marking, alternative to manual via webhooks, htrafficsource URL params for YouTube ManyChat"
query_hash: "0cdaea405e17f9a5"
slug: "hyros-calendly-integration-auto-vs-manual-call-state-trackin"
model: "sonar-pro"
date: "2026-05-06"
workspaces:
  - Precision-Brass
category: "APIs / Integrations General"
tags:
  - hyros
  - calendly
  - api
  - attribution
  - funnel
  - call-tracking
  - manychat
  - youtube
  - webhooks
keywords:
  - hyros
  - calendly
  - manual
  - call
  - integration
  - marking
  - state
  - tracking
  - manychat
  - rate
  - youtube
  - api
  - auto
  - bookings
  - docs
citations_count: 1
synthesized_in_notebooklm: false
stale_after: "2026-11-02"
---

# HYROS Calendly integration auto vs manual call state tracking, what HYROS auto-captures from Calendly bookings vs what requires manual marking, alternative to manual via webhooks, htrafficsource URL params for YouTube ManyChat

## Key findings

# HYROS Calendly Integration - Auto vs Manual Tracking

## Definitive answer (from HYROS official docs at hyros-docs.vercel.app/docs/install/v1/calendly.txt)

HYROS native Calendly integration tracks BOOKINGS automatically (when someone books, HYROS gets the lead + call event). It does NOT auto-track:
- Show-up vs No-show
- Disposition (DQ, completed, canceled by who)

Quote from docs: "Manual Tracking Required: HYROS does not auto-capture Calendly attendance status — users must manually mark call outcomes."

## How call states actually get populated in HYROS

1. Manual marking in HYROS dashboard (per-call dropdown)
2. Zapier / n8n: Calendly webhook (invitee.no_show, invitee.canceled with canceled_by=organizer for pre-DQ) → HTTP POST to HYROS calls API to update state
3. Direct Calendly API → HYROS API integration (custom Vercel function)

## Implication for Precision Brass dashboard

If Harrison is not manually marking call states in HYROS, the call.state field will be EMPTY or just "BOOKED" for everything. Show-up rate / no-show rate / DQ rate will all under-report unless either (a) Harrison starts manually marking, or (b) we wire Calendly webhooks → HYROS state updates ourselves.

Workaround for "paid" rate without state tracking: join HYROS sales to HYROS calls on lead.id directly. A booking that later has a sale event = closed. This works today.

## Custom source naming for YouTube and ManyChat

HYROS auto-detects Facebook, Instagram, TikTok, Google. For YouTube/ManyChat/Email/Other, every tracking link must include:
?sl=<unique-source-name>&htrafficsource=<Platform>

Example: https://precisionbrass.info/?sl=yt_embouchure_video&htrafficsource=YouTube

When set, HYROS exposes trafficSource.name = "YouTube" on the source object. Filter by trafficSource.name (not by source.name keyword matching) for accurate channel attribution.

## Lead.id join for full funnel

HYROS /leads, /calls, /sales all carry lead.id. Click-to-call-to-sale funnel = three filtered counts of distinct lead.id, joined on the same lead.id across endpoints.

## Sources

- https://precisionbrass.info/?sl=yt_embouchure_video&htrafficsource=YouTube