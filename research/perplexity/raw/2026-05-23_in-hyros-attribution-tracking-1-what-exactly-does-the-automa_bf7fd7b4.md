---
query: "In HYROS attribution tracking: (1) What exactly does the \"automatic\" traffic source mean on a lead or sale - does it mean the pixel fired but no source tag was present? (2) Complete list of reasons a click/lead/sale ends up unattributed or \"automatic\" in HYROS: missing sl/htrafficsource params, missing universal pixel on landing page, cross-domain hops dropping query params, redirects stripping params, cookie/ITP loss, email links not auto-detected. (3) Does HYROS use sl= and htrafficsource= URL params for source naming, and is el= meaningful in HYROS? (4) For an email link to a multi-step funnel (email -> precisionbrass.info masterclass -> third-party webinar host -> Calendly booking), what must be true for HYROS to attribute the booking to the email click - must sl/htrafficsource persist across every domain hop, or does the pixel + lead email-match handle it? (5) first-touch vs last-touch: if a subscriber first arrived via a Facebook ad, will a later tracked email click ever show as the source?"
query_hash: "bf7fd7b4fa437706"
slug: "in-hyros-attribution-tracking-1-what-exactly-does-the-automa"
model: "sonar-pro"
date: "2026-05-23"
workspaces: []
category: "APIs / Integrations General"
tags:
  - hyros
  - attribution
  - tracking
  - automatic
  - cross-domain
  - pixel
  - email
  - first-touch
  - funnel
keywords:
  - hyros
  - source
  - email
  - automatic
  - click
  - lead
  - params
  - pixel
  - htrafficsource
  - attribution
  - missing
  - sale
  - calendly
  - complete
  - facebook
citations_count: 9
synthesized_in_notebooklm: false
stale_after: "2026-11-19"
---

# In HYROS attribution tracking: (1) What exactly does the "automatic" traffic source mean on a lead or sale - does it mean the pixel fired but no source tag was present? (2) Complete list of reasons a click/lead/sale ends up unattributed or "automatic" in HYROS: missing sl/htrafficsource params, missing universal pixel on landing page, cross-domain hops dropping query params, redirects stripping params, cookie/ITP loss, email links not auto-detected. (3) Does HYROS use sl= and htrafficsource= URL params for source naming, and is el= meaningful in HYROS? (4) For an email link to a multi-step funnel (email -> precisionbrass.info masterclass -> third-party webinar host -> Calendly booking), what must be true for HYROS to attribute the booking to the email click - must sl/htrafficsource persist across every domain hop, or does the pixel + lead email-match handle it? (5) first-touch vs last-touch: if a subscriber first arrived via a Facebook ad, will a later tracked email click ever show as the source?

## Key findings

Here’s what’s going on in HYROS, point‑by‑point, with some “HYROS‑specific” nuance plus general attribution logic. HYROS’s own docs are sparse on these exact edge cases, so parts of this are based on how first‑party attribution platforms typically work combined with what’s publicly known about HYROS. I’ll flag anything that’s necessarily an inference.

---

## 1. What does “Automatic” traffic source actually mean?

In HYROS, “Automatic” on a lead/sale generally means:

- HYROS **tracked the event** (pixel fired, or server/API event received),
- but it could **not confidently tie it to a known traffic source / campaign** based on its normal attribution rules.

In practice this usually means one of:

- A click/visit occurred **without valid HYROS tracking parameters** (sl, htrafficSource, etc.), **and**  
- HYROS either:
  - couldn’t match the visitor to any previously tagged session (no cookied history or history was lost), or
  - only had ambiguous history, so it falls back to a generic “automatic” / “direct” style label.

So yes: “automatic” is *consistent* with “the pixel fired but no usable attribution info was present or recoverable.” It’s not *only* that the tag was missing; it’s also that HYROS had no older tagged session to fall back to.

---

## 2. Common reasons a click/lead/sale ends up **unattributed** or “Automatic” in HYROS

These are the main real‑world causes:

1. **Missing HYROS URL parameters on the first tracked entry visit**
   - No `sl=` (source link) or `htrafficSource=` (traffic source / channel) in the URL  
   - No other HYROS‑recognizable parameters (`hclid` from Google, `fbc_id` etc.)  
   - Result: HYROS sees the visit, but doesn’t know where it came from → later lead/sale = “Automatic” or “Direct”.

2. **Universal pixel not installed or not firing**
   - Pixel missing from:
     - Initial landing page
     - Key funnel steps
     - Final conversion page (e.g., order confirmation, booking confirmation)
   - Pixel present but:
     - JS errors prevent it firing
     - Loaded in a way that blocks it (e.g., via tag manager trigger not firing)
   - Result: HYROS sees a sale/lead only via API/Ecomm integration *without the prior web journey*, or doesn’t see part of the journey. This can cause unattributed events or “Automatic”.

3. **Cross‑domain hops dropping query params**
   - Funnel path: `ad → domain A → domain B → domain C (checkout)`  
   - If any redirect / link in that path:
     - strips query parameters, or
     - uses post/redirect without passing them through,
   - then the `sl`/`htrafficSource` and/or click IDs are lost mid‑funnel.
   - If HYROS can’t match the visitor using cookies / stored identifiers from the initial domain, the later lead/sale can become unattributed.

4. **Redirects that strip parameters or use intermediate “naked” URLs**
   - Link shorteners, cloakers, affiliate redirect scripts, or custom redirect pages can:
     - drop all query params,
     - selectively drop unknown params like `sl` / `htrafficSource`.
   - Result: visitor arrives on the real landing page without tracking params, HYROS only has a bare visit with no origin.

5. **Cookie / ITP / privacy loss**
   - Safari / iOS with strict ITP
   - Users clearing cookies
   - Private browsing / incognito
   - Browser settings or extensions blocking certain storage
   - Result: user arrives on the final conversion step as a “new” visitor (from HYROS’s point of view), with no params and no stored profile → event = automatic/unattributed.

6. **Email links not being correctly tagged or detected**
   - Link in email:
     - lacks HYROS parameters (`sl`, `htrafficsource`, or specific email‑tag params), and
     - isn’t rewritten by HYROS or your ESP integration correctly.
   - The click comes in as “direct” when the page loads.
   - HYROS may still associate the user with an existing profile if email identity is known and pixel fires, but the **source of the session** may show as automatic rather than “Email – Campaign X”.

7. **Inconsistent or missing HYROS code on third‑party tools**
   - Third‑party webinar platforms, scheduling tools, checkout carts, etc. without HYROS script (or with mis‑configured script).
   - HYROS sees traffic on your site, but not the final conversion event (or vice versa).
   - Result: events imported from the 3rd party system without a matching tracked session → “Automatic” or unattributed.

8. **Mobile apps / in‑app browsers / native app flows**
   - A user goes from an in‑app browser to the native browser (or vice versa), losing cookies and sometimes query params.
   - HYROS treats it as a new session with no prior tag.

9. **API‑only / backend events with no linked click**
   - Sales pushed via API or integration (e.g., from Stripe / payment processor) where:
     - the customer record doesn’t include a HYROS ID/click ID/email that HYROS recognizes, and
     - HYROS can’t confidently match to an existing profile.
   - Result: unattributed; often appears under “Automatic” or similar.

10. **Manual wrong tagging / malformed params**
    - Typo in parameter name (`htrafficsource` vs `htrafficSource`, missing `=` or `&`),
    - Inconsistent naming across campaigns so HYROS can’t group properly.
    - HYROS sees “something” but not in the format it expects, so default fallback.

Your list (missing params, missing pixel, cross‑domain/redirects, cookie loss, email links not auto-detected) captures the core causes. The above just rounds out a few less obvious ones.

---

## 3. What do `sl=`, `htrafficsource=` and `el=` mean in HYROS?

### `sl=` and `htrafficsource=` (or `htrafficSource=`)

HYROS does indeed use URL parameters for naming traffic sources / links. The names are commonly seen as:

- `sl=` – “source link” (or similar). Typically used to uniquely identify the *specific* ad or link. Think of it like a HYROS‑style UTM content / ad ID.
- `htrafficSource=` (sometimes written with case variations such as `htrafficSource` / `htrafficsource`) – used to store the high‑level traffic source type (e.g., “facebook”, “google”, “email”, “organic”, etc.), or medium.

Public HYROS guides don’t always spell out the exact parameter names, but implementers and agencies commonly use these, and they align with how HYROS organizes reporting by source/link. So:

- Yes: HYROS uses parameters of this nature to **name and categorize** the source.
- When those are present and recognized, they drive what you see as the traffic source, campaign, and link in attribution reports.

### `el=` in HYROS

HYROS docs don’t officially standardize an `el=` parameter in public materials. In many tracking setups:

- `el=` is often used informally as “email link” / “event label” / “email list” or similar.

In HYROS specifically:

- There is no widely documented, core HYROS feature that depends on `el=` in the same way it does on source/link parameters and click IDs.
- If you’re seeing `el=` in your HYROS URLs, it’s likely:
  - A **custom parameter you or your implementer added** for internal naming, or
  - A param used by your ESP that HYROS may simply pass through or optionally capture as metadata.

So, unless you have a specific internal script or HYROS custom field mapped to `el`, it’s **not inherently meaningful** to HYROS’s default attribution logic in the way `sl` / `htrafficSource` / click IDs are.

---

## 4. Email → multi‑step funnel: what has to be true for HYROS to attribute the final booking to the **email click**?

Scenario:  
Email → `precisionbrass.info` masterclass page → third‑party webinar host → Calendly booking.

Desired: booking attributed to the email campaign / click, not just “automatic.”

HYROS can attribute cross‑domain so long as:

1. **HYROS script is installed and firing on every key step** where you care about tracking:
   - `precisionbrass.info` masterclass page
   - Webinar host pages (if possible)
   - Calendly booking confirmation (or at least the final confirmation page)

2. **The initial email click is properly tagged or identifiable as “email”**  
   You have two main paths:

   ### Path A – URL parameters survive (strongest / cleanest)

   - The email link includes HYROS parameters, e.g.:
     - `?sl=email_masterclass_may&htrafficSource=email`
   - When the user:
     - clicks email,
     - lands on `precisionbrass.info`,
   - those parameters are present, and HYROS creates/updates the user profile with:
     - Source: email
     - Specific link: email_masterclass_may
   - If your redirects between domains **preserve those params**, HYROS can attribute subsequent steps robustly.

   However, **HYROS does not require** `sl/htrafficSource` to persist across *every* hop so long as:

   - It can reliably identify the same user on later pages via:
     - HYROS cookies / localStorage,
     - HYROS user ID embedded in the URL or stored in session,
     - and (for logged‑in or known users) email/other identifiers.

   Once the initial visit is tagged, HYROS uses first‑party identifiers to tie later actions — even on other domains — back to that original email click, **if**:
   - Those other domains have the HYROS script,
   - and share enough information (via the HYROS script / configuration) to connect the dots.

   ### Path B – Pixel + email identity matching (when params are lost mid‑funnel)

   Even if `sl/htrafficSource` don’t survive every hop, HYROS can often still attribute if:

   - The initial email click is tracked on the first domain with HYROS script;
   - HYROS associates that browser + email address (via form submit, login, or email link with embedded HYROS ID);
   - Later, when the user hits Calendly or another domain with HYROS script:
     - HYROS recognizes the same browser/user ID (cookie / localStorage / HYROS ID in URL),
     - or the same email is submitted again (e.g., in Calendly), and HYROS matches it back to the existing profile.

   In this case:
   - The **original source** remains “email”.
   - The booking event is tied to the profile that originated from that email click, even though `sl` parameters don’t appear on Calendly.

**Conclusion for this scenario**

For the booking to be attributed to the *email*:

- **Required in practice:**
  1. HYROS pixel present and working on:
     - `precisionbrass.info` (entry from email)
     - the final booking confirmation page (Calendly or your own thank‑you, depending on integration)
  2. Either:
     - The initial email link is tagged (`sl` + `htrafficSource=email`), *and* HYROS can maintain the user identity across steps, **or**
     - HYROS can reliably identify the same user later via its cookie/ID/email match.

- **Not strictly required:**
  - `sl/htrafficSource` do **not** need to physically persist as query params on every domain hop, as long as HYROS’s user ID / cookie continuity and/or email identity matching works across those domains.

But: if cookies/IDs are broken (e.g., different browsers, ITP, no common HYROS script), then **losing the parameters on the first hop will make attribution much more likely to fall back to “automatic.”**

---

## 5. First‑touch vs last‑touch: can a later email click ever show as the source if the user originally came from Facebook?

HYROS is a **multi‑touch attribution** system; it keeps the whole journey and can show:

- **First touch (original source)** – e.g., “Facebook – Campaign A – Ad X”
- **Last touch (most recent touch before conversion)** – e.g., “Email – Sequence B – Link Y”
- **Assisted touches** – all the steps in between

How this looks in reports:

- The **user profile** will usually show the **original acquisition source** as “Facebook” if that’s how they first arrived and were tagged.
- For a specific **sale or event**, the **credited source** depends on:
  - The attribution model/view you choose (first click, last click, multi‑touch, etc.),
  - The specific HYROS report (some views default more “first touch,” others show last touch or both).

So, answering your question directly:

> If a subscriber first arrived via a Facebook ad, will a later tracked email click ever show as the source?

- **Yes**, a later email click *can* show as the source of a given conversion **under last‑touch or multi‑touch views**:
  - For that **specific sale or booking**, HYROS may list:
    - First touch: Facebook
    - Last touch: Email (Campaign X)
  - In an “Email Attribution” or “Last‑touch” oriented report, that conversion can be credited to email.

- **No**, the original **acquisition source** for that user will remain Facebook:
  - In “First Touch” / LTV by original source reports, the customer is counted under Facebook.
  - Email is then shown as a **nurturing / reactivation touch**, not the acquisition source.

So you should expect:

- LTV by original source → dominated by the first ever touch (Facebook)
- Per‑campaign or per‑email reports → email can absolutely be shown as the driving source for subsequent conversions by that same user.

---

### Summary in plain terms

1. **“Automatic”** = HYROS saw the event but couldn’t tie it to a clear tagged source or identifiable prior session.
2. Common causes: missing params, missing pixel, cross‑domain/redirect param loss, cookie/ITP issues, mis‑tagged emails, and API‑only events without a match.
3. HYROS uses URL params like `sl` and `htrafficSource` for source/link naming. `el` is not a core HYROS parameter unless you or your stack explicitly use it.
4. For your email → multi‑domain funnel, HYROS needs (a) scripts on the key pages and (b) either tagged initial email links or stable user identification across domains. `sl/htrafficSource` don’t need to survive every hop if HYROS can maintain identity via its own IDs/cookies/email.
5. A user acquired via Facebook will still be a “Facebook customer” in first‑touch views, but later conversions can absolutely be attributed to email in last‑touch / multi‑touch reporting.

## Citations:
[1] What Is Hyros? Everything You Need to Know About Hyros Tracking - https://clientaccelerators.com/what-is-hyros/
[2] Hyros Tutorial: Set Up AI-Powered Ad Tracking to Boost ROI (Step ... - https://www.youtube.com/watch?v=P7EuR4klVcE
[3] A Complete Guide To How Ad Tracking Works - HYROS - https://hyros.com/updates/how-does-ad-tracking-work/
[4] Hyros: The Best Ad Tracking & Attribution Software - https://hyros.com
[5] SaaS Attribution & Ad Tracking Software - Hyros - https://hyros.com/saas
[6] Best Hyros Alternative Attribution Tool: 2026 Guide - Cometly - https://www.cometly.com/post/hyros-alternative-attribution-tool
[7] Ultimate Hyros AI Remarketing Guide: Hyros AIR Review 2025 - https://mediabuyer.com/hyros-air
[8] Hyros Implementation - LGG Media - https://www.lgg.media/hyros/
[9] Call Attribution Tracking For Your Funnels & Ads - Hyros - https://hyros.com/call-tracking

## Sources

- https://clientaccelerators.com/what-is-hyros/
- https://www.youtube.com/watch?v=P7EuR4klVcE
- https://hyros.com/updates/how-does-ad-tracking-work/
- https://hyros.com
- https://hyros.com/saas
- https://www.cometly.com/post/hyros-alternative-attribution-tool
- https://mediabuyer.com/hyros-air
- https://www.lgg.media/hyros/
- https://hyros.com/call-tracking