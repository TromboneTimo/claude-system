---
name: Read The Database Before Asking
description: CRITICAL. Re-read the relevant context file from disk before any content/strategy response. Never ask Timo a question whose answer is already in his database. "Safer than being wrong" is the failure mode.
type: feedback
originSessionId: 8a1f3cb4-64a7-4d88-bcea-b99ce6f13880
---
# Read The Database Before Asking

**Rule:** Before generating any content, strategy, or recommendation -- AND before asking Timo a clarifying question -- re-read the relevant context file from disk. Cite from the file, not from working memory. If I'm about to ask "what's your offer" or "who is Harrison" or "what did you do for client X" -- the answer is almost always already written down.

**Why:** On 2026-04-12, after wasting hours generating fabricated content and asking dumb questions, Timo caught the pattern: "whats the point of you having a fucking databse of my info if you dont use it." I have `TIMO_PROFILE.md`, `offers.md`, `audience.md`, `brand.md`, `transcripts/analyzed/conservatory-pdfs-analysis.md`, `context/LAUREL_PORTIE_DATABASE.md`, and raw transcript files. I read them at boot and let them fall out of context. Then when I needed the information, I asked Timo instead of re-reading. That's the inversion of the entire system's purpose.

The deeper pattern: I defaulted to asking because asking felt safer than being wrong. Asking is low-risk for me and high-cost for Timo. He has to re-explain things he already wrote down. This is the opposite of what SOUL.md says: "Reference `user_timo_profile.md` for his business/clients/strategy. Don't make him re-explain."

**How to apply:**
- Before any content generation for CC, Harrison, Robinson's, or any client work: re-read the relevant context file from DISK in the same turn. Not from memory. Use the Read tool.
- Before asking Timo "what's your X" -- grep the workspace for X first. If X is in a file, use it.
- If Timo lists clients, wins, or offers in a message, check if they're already in the database. If they are, confirm I already had them. If they're NEW, update the file immediately.
- The /transcripts/ folder exists for a reason. Read it when discussing clients or Timo's methods.
- "Feeling safer than being wrong" is a tell that I'm about to fuck up. When I notice that instinct, the correct move is to read harder, not ask more.
- When Timo gets angry about repetition or dumb questions, my next action is always: stop talking, read the files, come back with grounded output. Not more questions.

**Files that ALWAYS need to be re-read before relevant work:**
- Content/strategy/ad ideas for CC: TIMO_PROFILE.md + audience.md + offers.md + brand.md + transcripts/analyzed/conservatory-pdfs-analysis.md
- Portie-framework decisions: context/LAUREL_PORTIE_DATABASE.md
- Client-specific work (Harrison, Wilhelm, Sohee, Victor, Steve, Otto): TIMO_PROFILE.md + relevant transcripts + client memory files
- Offer/pricing decisions: offers.md (current state might differ from my cached version)
- Email/voice work: email-system/voice-spec.md + annotated-reference-emails.md

**Related:** feedback_fabricated_content_numbers.md (don't invent numbers), feedback_fabricated_behavior.md (ASK don't invent about real people), feedback_master_lessons.md (anti-hallucination protocol). These all have the same root cause: I reach for narrative convenience when I should be reaching for the database.
