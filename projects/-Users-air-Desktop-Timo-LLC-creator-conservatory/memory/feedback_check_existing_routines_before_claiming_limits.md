---
name: Check Existing Routines Before Claiming MCP Limits
description: Before telling Timo an MCP can't do X, check his existing working routines. Locally exposed tool lists are a subset, not the full capability.
type: feedback
originSessionId: 2e2e7f2e-fde0-45d8-b4d6-c479ee7921fb
---
The local claude.ai Gmail MCP tool list showed only read/search/draft tools (no send). I told Timo the routine couldn't send the digest to his inbox and proposed Resend as a workaround. He called me out: his Daily Morning Briefing routine (trig_01LSUbvtYdKwPFroa3eC3qta) sends email successfully every day via "Gmail MCP tools to send".

**Why:** The Gmail MCP in the remote routine environment exposes more tools than the locally-viewable subset. My local tool list is not authoritative for what runs in the cloud routine environment.

**How to apply:** Before claiming any MCP or connector has a capability limit (especially around sending, creating, or modifying):
1. List existing routines via `RemoteTrigger list`
2. Read their prompts for precedent: is there a working routine that already does what I'm claiming is impossible?
3. **Precedent in a prompt is not proof the routine works.** A prompt saying "Use Gmail MCP to send" does not mean sending works. Verify the routine's recent runs actually delivered the output (check the session transcript, or in the case of email, ask Timo if he actually receives the emails reliably or has been pulling them from Drafts).
4. Only after BOTH prompt precedent AND delivery proof may you assume the capability exists. Otherwise still test in a dry run before proposing workarounds.

**2026-04-15 incident (full arc):**
- Timo asked for a routine to email him a triage digest.
- My local tool list showed no `gmail_send_*` tool. I proposed Resend as a workaround.
- Timo pushed back: "you were able to give me daily updates to my email before." I found the Morning Briefing routine's prompt saying "Use Gmail MCP tools to send." I pivoted and assumed the MCP could send in the cloud env.
- After creating Email Triage and firing it, the routine's own ToolSearch confirmed: no `gmail_send_mail` or `gmail_send_draft` tool exists. The digest was drafted, not sent. Morning Briefing has likely been drafting too without Timo noticing.
- Lesson: a prompt's instruction is not evidence of capability. The Morning Briefing may have been silently broken for weeks.

Related: this is a specific case of the general "verify before declaring done" rule. Do not assume a limit from an incomplete view, AND do not assume a capability from an unverified prompt.
