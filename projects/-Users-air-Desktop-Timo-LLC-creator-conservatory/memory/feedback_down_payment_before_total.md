---
name: Down Payment Number Appears Before Total
description: In any pricing section showing a phased payment, the down payment dollar amount must appear in the document BEFORE the engagement total. Reader sees the manageable kickoff number first, then the completion payment, THEN the total as the sum. The line-item breakdown of what the total covers comes AFTER the payment phases, framed as "what that $X covers." Reader never hits the total as the first big number.
type: feedback
originSessionId: fd3dfc9f-1ccb-45e7-a4ff-3b98709a9069
---
# Down Payment Number Appears Before Total

In any pricing section that includes a phased payment (40/60, 50/50, etc.), the **down payment dollar amount must appear in the document BEFORE the engagement total**. The reader's first big number is the manageable down payment, then the completion payment, then the total as the sanity-check sum.

## The order

1. **Down payment (40%)**: $X due on signature.
2. **Phase 2 / completion payment (60%)**: $Y due when [trigger].
3. **Engagement total**: $X + $Y.
4. **What that total covers**: line items breakdown (comes AFTER the payment phases, framed as "what the total covers" or "what that $Z covers", not as the leading pricing table).

## Why

Sales psychology. The reader needs to evaluate "can I commit to this engagement?" The first decision is "can I afford the down payment?" not "can I afford the total?" Leading with the total reframes the entire engagement as a one-shot purchase decision. Leading with the down payment frames it as a manageable first step into a build-and-prove arrangement.

This is the canonical pricing rule already documented in `feedback_pricing_section_always_last.md` under "Phased-payment order: When 40/60 (or any phased) split applies, the FIRST dollar number in Section 4 must be the upfront/Phase-1 amount. Never lead with the total." This memory exists because that rule has been violated repeatedly across proposals.

## Failure pattern I keep repeating

The line-item breakdown table ("What Victor pays: High-Ticket Funnel $1,000, Email Engine $2,500, ...") comes first because it looks like the natural "here's the pricing" section. The engagement total ($5,275) appears at the bottom of that table. Then the Payment Structure table appears below with Phase 1 / Phase 2 / Total.

This means the reader hits the engagement total ($5,275) BEFORE seeing the down payment ($2,110). Wrong order.

## The fix

Put the payment phases table FIRST in Section 4:

```
### What Victor pays
| | Amount | When |
| Down payment (40%) | $2,110 | On signature. |
| Phase 2, when completed | $3,165 | When [trigger]. |
| Engagement total | $5,275 |

### What that $5,275 covers
[line items here]
```

The line items still exist. They just live below the payment phases, framed as "what that $X covers" rather than "what Victor pays." The reader's first big dollar number is $2,110, not $5,275.

## How to apply

Before writing any pricing section, ask: "What dollar amount does the reader see first?" If the answer is the engagement total or the largest line item, restructure. The first dollar amount must be the down payment.

This is a hard rule. Caught 2026-05-09 (Robinson's), 2026-05-11 (Victor), and many other proposals. Timo's exact words on this iteration of Victor: "before showing the total number, first show the down payment number of 40%, then show, once everything is completed, this will be owed, and then show the total. For right now, you're showing the total first. It pisses me off. I told you this before, and yet you still do it over and over and over and over again."

## Pre-paste gate

Add to the 7-point verdict gate in proposal-writer SKILL.md: "Does the pricing section lead with the down payment number, not the engagement total or line item table? If the first big dollar amount the reader sees is anything other than the down payment, FAIL."
