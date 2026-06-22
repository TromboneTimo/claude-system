---
query: "Meta Marketing API: view-only role token generation, ads_read vs ads_management, System User token path, 2025-2026 permission changes"
query_hash: "b3fcb2b8c54d1486"
slug: "meta-marketing-api-view-only-role-token-generation-ads-read-"
model: "sonar-pro"
date: "2026-05-13"
workspaces:
  - Precision-Brass
category: "APIs / Integrations General"
tags:
  - meta
  - api
  - facebook-ads
  - access-token
  - marketing-api
keywords:
  - token
  - source
  - access
  - api
  - tokens
  - generation
  - results
  - meta
  - role
  - scopes
  - search
  - view-only
  - long-lived
  - marketing
  - mentions
citations_count: 11
synthesized_in_notebooklm: false
stale_after: "2026-11-09"
---

# Meta Marketing API: view-only role token generation, ads_read vs ads_management, System User token path, 2025-2026 permission changes

## Key findings

# Meta Marketing API: Access Token Generation with View-Only/Analyst Role

Based on the search results provided, I can address some aspects of your query, though the results have significant gaps for a complete answer. Here's what the documentation shows and where clarity is needed:

## What the Search Results Confirm

**1. Long-Lived Access Tokens Are Available**
- Source [2] and [3] confirm you can generate long-lived Page/User access tokens via server-side API calls
- Source [3] specifically mentions generating "a single, long-lived Page token to continuously fetch data without worrying about it expiring"
- These tokens persist longer than short-lived tokens (which expire in 1-2 hours per Source [1])

**2. Access Token Generation Locations**
- Source [4] states: "Access tokens can be generated through the Meta developer portal. Navigate to Tools and select Access..."
- Source [7] references the Graph API Explorer tool

**3. Scopes and Permissions**
- Source [1] mentions scopes are "permissions added in the Graph API Explorer"
- Source [6] discusses specific permission scopes (example: `attribution_read`), indicating granular permissions exist

---

## Critical Gaps in Search Results

The search results **do not directly address**:

1. ❌ Whether **View-Only or Analyst roles** can generate tokens (only mentions they exist)
2. ❌ Specific difference between **`ads_read` vs `ads_management` scopes**
3. ❌ Whether role restrictions block token generation or only write actions
4. ❌ **System User token creation path** in Business Settings (not covered)
5. ❌ **Personal access token vs System User token** distinction
6. ❌ 2025-2026 changes to the Meta permission model

---

## What Official Documentation Likely Covers (Inference)

Based on typical Meta API patterns and the partial results:

- **`ads_read` scope** is likely the correct scope for read-only Ad Insights (spend, impressions, clicks, CTR, CPA, ROAS)
- **`ads_management` scope** probably grants write permissions (campaign creation/editing)
- **View-Only/Analyst roles likely permit token generation** but may restrict certain scopes
- **System Users** (created in Business Settings) are the recommended approach for server-to-server integration (vs personal tokens)

---

## Recommendation

To get definitive answers to your specific questions, you need to consult:

1. **[Meta Marketing API Scopes Reference](https://developers.facebook.com/docs/marketing-api/authorization/permissions-reference)** — for `ads_read` vs `ads_management` details
2. **[Ad Account Roles & Permissions](https://www.facebook.com/business/help/)** — for role-based access control specifics
3. **[System User Setup Guide](https://www.facebook.com/business/help/908499776457049)** — for Business Settings path to create System Users
4. **[2026 Breaking Changes](https://developers.facebook.com/docs/apis/marketing-api/breaking-changes)** — for recent permission model updates

The search results provided are incomplete for a comprehensive answer to this technical question.

## Citations:
[1] Authentication - Meta for Developers - Facebook - https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authentication
[2] Access Tokens for Meta Technologies - Meta for Developers - https://developers.facebook.com/documentation/facebook-login/guides/access-tokens
[3] Retrieving Leads - Meta for Developers - Facebook - https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/retrieving
[4] Frequently Asked Questions - Meta for Developers - Facebook - https://developers.facebook.com/documentation/ads-commerce/marketing-api/using-the-api/faq
[5] Long-Lived Access Tokens - Meta for Developers - https://developers.facebook.com/documentation/facebook-login/guides/access-tokens/get-long-lived
[6] Permissions Reference - App Development with Meta - Documentation - https://developers.facebook.com/docs/permissions/
[7] Meta for Business (formerly Facebook for Business) - https://developers.facebook.com/tools/explorer/

## Sources

- https://developers.facebook.com/docs/marketing-api/authorization/permissions-reference
- https://www.facebook.com/business/help/
- https://www.facebook.com/business/help/908499776457049
- https://developers.facebook.com/docs/apis/marketing-api/breaking-changes
- https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authentication
- https://developers.facebook.com/documentation/facebook-login/guides/access-tokens
- https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/lead-ads/retrieving
- https://developers.facebook.com/documentation/ads-commerce/marketing-api/using-the-api/faq
- https://developers.facebook.com/documentation/facebook-login/guides/access-tokens/get-long-lived
- https://developers.facebook.com/docs/permissions/
- https://developers.facebook.com/tools/explorer/