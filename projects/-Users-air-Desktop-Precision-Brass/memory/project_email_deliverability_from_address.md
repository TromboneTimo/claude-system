---
name: project_email_deliverability_from_address
description: "Harrisson's AC daily broadcasts send FROM harrissonball@precisionbrass.info (his OWN domain). Optional polish = add AC SPF/DKIM at IONOS for full alignment. DMARC is p=none. Do NOT raise any alternate/old from-address; it is off the table by Timo's standing order."
metadata: 
  node_type: memory
  type: project
  originSessionId: b1137a51-e4a3-44d3-9329-692d856cbb63
---

STANDING ORDER (2026-05-28, Timo, emphatic): The send-from address is `harrissonball@precisionbrass.info`. Never bring up any other/legacy from-address again. Do not investigate it, propose migrating it, or mention it. The topic is closed.

**Verified send-from:** Harrisson's AC daily broadcasts send FROM `Harrisson Ball <harrissonball@precisionbrass.info>`, his OWN domain. Campaign names embed it literally: `Daily Email 1 [by harrissonball@precisionbrass.info]`.

**Current DNS for precisionbrass.info (IONOS-hosted, verified 2026-05-28):**
- SPF: `v=spf1 include:_spf.perfora.net include:_spf.kundenserver.de include:_spf-us.ionos.com ~all`, covers IONOS, does NOT list ActiveCampaign.
- DMARC: `v=DMARC1;p=none;` (monitor only, nothing rejected).
- No AC DKIM found at common selectors (dk/dkim/am1/acdkim/activecampaign). CAVEAT: AC can use a non-standard selector not probed, so DKIM absence is not 100% confirmed.
- `precisionbrass.com` has no SPF/DMARC; not the active domain.

**Optional polish (NOT a crisis):** for full SPF+DKIM/DMARC alignment on AC-sent mail, add ActiveCampaign's SPF include + DKIM records at IONOS (values from AC's "verify a domain" screen). With DMARC at p=none nothing is currently rejected, so this is deliverability optimization, not an emergency.

LESSON: don't declare a from-address (or any classifier-style fact) from a single API row. Sample the distribution. See [[feedback_classifier_verification_must_use_ground_truth.md]]. UNRELATED to [[feedback_dup_send_db_gate.md]].
