---
query: "ActiveCampaign API replies field on /api/3/campaigns always 0, reply tracking off by default per campaign, must enable per campaign via Tracking and Automations Reply Tracking checkbox, no replies count exposed via API, alternative is webhooks type=reply"
query_hash: "b66bcd4ecc8dcfb6"
slug: "activecampaign-api-replies-field-on-api-3-campaigns-always-0"
model: "sonar-pro"
date: "2026-05-06"
workspaces:
  - Precision-Brass
category: "APIs / Integrations General"
tags:
  - activecampaign
  - api
  - email
  - replies
  - webhooks
  - tracking
keywords:
  - tracking
  - api
  - reply
  - replies
  - campaign
  - activecampaign
  - per
  - automations
  - campaigns
  - via
  - webhooks
  - field
  - automations-reply
  - checkbox
  - count
citations_count: 8
synthesized_in_notebooklm: false
stale_after: "2026-11-02"
---

# ActiveCampaign API replies field on /api/3/campaigns always 0, reply tracking off by default per campaign, must enable per campaign via Tracking and Automations Reply Tracking checkbox, no replies count exposed via API, alternative is webhooks type=reply

## Key findings

**Reply tracking is off by default per campaign (not per account), must be enabled manually for replies to be tracked.** [2]

**API /campaigns endpoint `replies` field always 0 because it doesn't exist or isn't populated via API—use webhooks (`type: reply`) for reply events instead.** [2,5]

- No `replies` count field in `/api/3/campaigns` docs; view counts in UI Reports > Campaign > Replies. [2]
- **Alternates**: `/api/3/webhooks` for reply data (incl. `contact[email]`, `message`, `result` like 'forward'). No `/api/3/conversations` or `/api/3/messageStatus` for replies. [5]
- Enable: Campaign Settings > "Tracking and Automations" > Reply Tracking checkbox. [2]

## Citations:
[1] Scores set to 0 by automations are being reset by static scoring rules - https://help.activecampaign.com/hc/en-us/articles/4404523793948-Scores-set-to-0-by-automations-are-being-reset-by-static-scoring-rules
[2] Use Reply Tracking with your campaigns - https://help.activecampaign.com/hc/en-us/articles/115000013844-Use-Reply-Tracking-with-your-campaigns
[3] 8 ActiveCampaign User Scenarios and Ways to Optimize Them - https://clearout.io/blog/activecampaign-user-scenarios-optimization/
[4] 3 QUICK SOLUTIONS for ActiveCampaign Automations Not Working - https://www.youtube.com/watch?v=THcpCZDZV6k
[5] Webhooks - ActiveCampaign API documentation - https://developers.activecampaign.com/page/webhooks
[6] Contact Scoring in ActiveCampaign - https://help.activecampaign.com/hc/en-us/articles/221293927-Contact-Scoring-in-ActiveCampaign
[7] Basic troubleshooting steps for your ActiveCampaign account - https://help.activecampaign.com/hc/en-us/articles/360021730040-Basic-troubleshooting-steps-for-your-ActiveCampaign-account
[8] Contact_edit and contact_add api gives no response about format of ... - https://community.activecampaign.com/t/contact-edit-and-contact-add-api-gives-no-response-about-format-of-data-posted-error/2258

## Sources

- https://help.activecampaign.com/hc/en-us/articles/4404523793948-Scores-set-to-0-by-automations-are-being-reset-by-static-scoring-rules
- https://help.activecampaign.com/hc/en-us/articles/115000013844-Use-Reply-Tracking-with-your-campaigns
- https://clearout.io/blog/activecampaign-user-scenarios-optimization/
- https://www.youtube.com/watch?v=THcpCZDZV6k
- https://developers.activecampaign.com/page/webhooks
- https://help.activecampaign.com/hc/en-us/articles/221293927-Contact-Scoring-in-ActiveCampaign
- https://help.activecampaign.com/hc/en-us/articles/360021730040-Basic-troubleshooting-steps-for-your-ActiveCampaign-account
- https://community.activecampaign.com/t/contact-edit-and-contact-add-api-gives-no-response-about-format-of-data-posted-error/2258