---
name: feedback-check-capability-before-offloading
description: "Before asking the user to do anything, exhaustively check what credentials/access I already have and whether the capability actually exists. \"I can't\" is a conclusion, not a reflex."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e670584f-0b7e-4881-9e25-25b39353b8ae
---

When a task seems to need the user to provide a credential, run a command, or supply a secret, STOP and check what I already have and what I can actually do BEFORE asking. Two failures in one session (Victor Alegria dashboard deploy, 2026-06-04) both came from offloading work I was already equipped to do:

1. Asked Timo to `supabase login` / paste a token. His Supabase personal access token (`sbp_...`) was already in `~/.claude/credentials/MASTER.md`. He pushed back: "why do I need to do anything?"
2. Told him I couldn't make Victor's admin password match Precision Brass. I could copy the bcrypt `encrypted_password` hash between two Supabase projects I admin (read PB's auth.users, write Victor's). He pushed back: "yes you can, just go to the other database and do it." He was right.

**Why:** every offloaded step is a round-trip that breaks his flow and reads as me being lazy or incapable. Both times he had to correct me; the actual work was minutes. The CREDENTIAL/BOOT gates already say read MASTER.md first. I didn't apply it before asking.

**How to apply:**
- Before any "can you provide / run / paste X" ask: grep MASTER.md + ~/.claude/secrets + env + existing `.vercel`/CLI auth for X. Verify it's truly absent.
- Reframe "I can't do X" as "have I confirmed I can't?" If I have admin/service access to the systems involved, assume the data can be moved/copied/derived until proven otherwise. Passwords can't be read, but hashes can be copied between DBs I control.
- Only ask the user for something that genuinely exists ONLY in their head or an account I have zero access to.
- Related: [[feedback-audit-full-target-state-before-clone-deploy]], [[feedback-save-credentials-immediately]], [[project-dashboard-live]].
