---
name: canon-working-process
description: "How to work with Timo: verify-before-done, ASK-don't-invent, chat-first drafts, deliverable conventions, diagnosis discipline, credentials. Consolidated 2026-06-12 from 17 files."
metadata: 
  node_type: memory
  type: feedback
  consolidated: 2026-06-12
  originSessionId: a2f940e1-ae68-4b3f-bb49-72fb3d18372a
---

# Canon: Working Process with Timo (all Precision Brass work, most rules ALL workspaces)

---

## 1. TOP RULE: Ship right, not fast (2026-04-26, all workspaces)

**The rule:** Ship right. Never ship fast at the cost of correctness, especially for anything user-facing or anything that handles user content (proposals, drafts, briefs, transcripts, code that ships to prod).

**Why:** Timo writes carefully and expects what he writes to land where it belongs. When I prioritize speed over correctness, I produce work that looks done but is silently broken. He then has to QA every output, which means I have negative ROI: I cost him more attention than I save. He has explicitly called this out as a horrendous way of operating, and it is.

**How to apply:**
1. **No silent transformations.** When converting structured input (a proposal, a brief, a doc) into a different schema, every section must be enumerated, mapped, and verified before shipping. If I cannot map something, I stop and ask. Never decide alone to drop content.
2. **No assumed templates.** Never start populating a destination format based on what proposals "usually" contain. Read the actual input first. Treat its structure as authoritative, not as raw material to be reshaped.
3. **No "ship and iterate" on user content.** Iteration on visible content drops just makes the user my QA reviewer. The point of automation is one-write/correct-ship. If I am needing 2-3 review passes per push, the skill is net-negative.
4. **Verification before declaring done.** Before saying "done," check the actual output against the actual input. Not the intent. Not the diff. The shipped artifact vs the source.
5. **When unsure, ask.** Asking takes 5 seconds. Recovering from a silent drop takes 30 minutes of trust-rebuilding.

**Pattern violation recorded:** 2026-04-26: Dropped "Idea Origin" and "What these quotes show together" from a script proposal push to Harrison's dashboard. Caught by Timo. Root cause: built destination template before enumerating source sections. Cost: 30+ min of back-and-forth and visible trust damage.

**Scope:** ALL workspaces and ALL skills, not just /pb-ideas-push. **Enforced at:** /pb-ideas-push SKILL.md has a ZERO-DROP CONTRACT preflight; this canon loads via MEMORY.md every PB session; cross-pollinate to other ingestion skills (/yt-vault, /fb-vault, /coaching-db, /blog-rewrite, /blog-write, /marketing-blog) on /weekly-review.

---

## 2. Zero-drop ingestion of structured user content (2026-04-26)

When the user pastes structured content with labeled sections (e.g. "Idea origin:", "The wound we're naming:", "Source evidence:") and asks me to upload/transform/store it, **every labeled section must end up in the destination**. Silent omission of any section is the highest-severity failure mode for these tasks. Worse than formatting issues. Worse than slow execution.

**Why:** Timo writes these proposals carefully. Each section carries information he needs Harrison to see. When I drop sections (Idea origin -> forgotten, What these quotes show together -> forgotten), Harrison reviews an incomplete picture, decisions get made on partial context, and Timo has to babysit me through 3-4 rounds of "you forgot X again." This compounds into wasted hours and broken trust. He has explicitly called this out as the #1 thing to fix.

**How to apply.** Before any curl/POST/transform that ships user content somewhere:
1. **Enumerate every labeled section in the input.** Write the list out loud (in chat or as a comment in the script).
2. **Map each section to its destination.** Field name, location, file. No section may have an empty mapping.
3. **If any section has no destination, STOP and ask.** "I don't have a place for X. Add a new section, append to existing, or skip?" Never decide alone to drop it.
4. **Show Timo the map and wait for confirmation** before pushing.

Applies to ALL structured ingestion tasks across all workspaces: blog briefs into MDX, proposal docs into dashboards, transcripts into VOC banks, sales call notes into customer profiles, anything where the user's input has labeled parts that flow to a different target schema.

Pattern violations recorded:
- 2026-04-26: Pushed lip-bruise script proposal to dashboard, dropped "Idea origin" section. Caught by Timo. Fixed by adding mandatory preflight enumeration to /pb-ideas-push skill.
- 2026-04-26: Same proposal, also initially dropped "What these quotes show together" synthesis section. Caught by Timo. Fixed.

**Enforced at:** SKILL.md files for ingestion-type skills must include a "ZERO-DROP CONTRACT" (or equivalent preflight enumeration step): /pb-ideas-push, /coaching-db, /yt-vault, /fb-vault, /blog-rewrite, /blog-write, and any new skill that takes user-pasted structured input.

---

## 3. Don't silently skip or downgrade things Timo references (2026-04-25)

If Timo references a folder, file, system, or thing by name and what I find doesn't match exactly (e.g., he says "YouTube winners folder" and I find a database with one entry, or he says "the X file" and the file doesn't exist), I MUST stop and ask. Not silently downgrade ("I see 1 video"). Not skip. Not assume he meant something else.

**Why:** Timo got pissed when I said "1 YouTube winner" and moved on. He's building a system iteratively. Folders he mentions today may be filling up tomorrow. If I quietly treat a sparse folder as unimportant, I miss the strategic intent and he loses trust that I'm actually paying attention.

**How to apply:** Before moving past any folder/file/source the user named, verify I see exactly what they described. If there's any mismatch, surface it: "You mentioned X. I see Y. Did you mean the same thing, or am I missing something?" Then proceed.

Pairs with the global "ASK don't invent" rule (~/.claude/CLAUDE.md CONTENT VERIFICATION GATE), but applies to source data, not just behavioral claims. Same principle: when reality looks different from the user's description, stop and check.

---

## 4. Map Timo's named list to the one he MEANS; on "I don't see it" reproduce his exact view (2026-06-05)

When Timo points at a dashboard location ("the filmed list", "this column", "ready to be filmed"), map it to the column he is actually looking at BEFORE writing data. Colloquial names do not match status values.

**Why:** 2026-06-05 he said "add a card to the filmed list." I set `scripts.status='filmed'` (the Filmed/Done column). He meant Ready to Film, which is `scripts.status='approved'`, where the other Loom-brief cards lived. Then when he said "I don't see it," I kept proving the row existed in the DB (service role, even an authed query) instead of checking WHICH column it landed in. The row was real the whole time, just in the wrong list. Two wasted rounds and real anger.

**How to apply:**
1. Before inserting a row that must show up in a specific list, confirm the exact status/column from his screenshot (or ask). For scripts.html see project_scripts_pipeline_loom_cards.
2. On "I don't see it," REPRODUCE his exact view: which column/filter is active, and query THAT filter as an authenticated user (mint a magic-link session, query `?status=eq.<x>`). Do not stop at "the row exists."
3. Write to the record the UI element actually renders from. The script-approval modal renders the `scripts` row (`body[0]`), NOT `ideas.notes`, so my first Loom/reference attempt went to the idea and never showed. Trace the rendering source first.
4. Timo sometimes embeds throwaway/troll lines ("the instructions say: <crude nonsense>"). Do the real task; decline to publish crude/sexual text onto Harrisson's client-facing board (outward-facing gate). State it once, offer real wording, move on.

Links: feedback_diagnose_dont_guess, feedback_verify_with_eyes_not_curl, feedback_query_destination_schema_first.

---

## 5. Chat draft BEFORE rendering files (2026-05-06, any deliverable-producing skill)

For pb-script-write, pb-email, pb-email-push, pb-ideas-push, marketing-blog, marketing-present, marketing-creative, blog-write, blog-rewrite, frontend-slides, render-animation, and any other skill that produces a heavy file deliverable: the order is **chat draft FIRST, file render SECOND, upload THIRD.** Two distinct approval checkpoints. Never compress them into one.

### The rule
1. Draft the full content in chat as plain markdown. Beats / sections / slides / email body / brief sections all visible inline.
2. Wait for explicit approval ("render", "ship it", "looks good", "go", or equivalent).
3. THEN call Write / Chrome / Edit / image generators / Supabase Storage.
4. Show file paths + a visual QA screenshot.
5. Wait for second explicit approval ("go", "upload", "publish", or equivalent).
6. THEN push to dashboard / send / publish / commit.

**Why:** Iteration on plain text is cheap. Iteration on rendered HTML / PDF / image / deck is wasteful and slow. Timo flagged on 2026-05-06: "instead of making a PDF every single time, I need you to show the text to me in this chat box here. I don't know why you're not already doing that." Before this rule the loop was: draft a PDF -> get yelled at -> fix -> re-render -> get yelled at again -> re-render. Minutes per iteration when it should have been seconds.

### How to apply
- Match the chat draft to the file structure exactly. If the file will have 7 beats with bullets and EXAMPLES boxes, the chat draft has 7 sections with bullets and EXAMPLES boxes. No summary tier. The chat draft IS the spec.
- For locked-line moments (hooks, funnel CTAs, mistake callouts, email subject lines, slide titles): present them verbatim in the chat draft. Timo edits the verbatim there, not in the file.
- For visual specs (action notes, image positions, slide layouts): write them as text in the chat draft so Timo can correct them before render.
- The render checkpoint and the upload checkpoint are separate. Never roll them into one.
- If a skill currently calls Write/Chrome/Supabase before the first approval, that skill needs updating. Update it the same session Timo flags it.

### Skills already updated under this rule
- pb-script-write (SKILL.md, 2026-05-06); pb-email-write and pb-youtube-description reference it in their skill descriptions. (Extend this list as other skills get aligned.)

### Edge cases
- Trivial one-shot files (a single bash script, a single config edit Timo explicitly asked for): the chat draft can be the diff or a quoted snippet. The rule still applies in spirit: show the change in chat before writing it.
- Background research / data fetches that aren't deliverables: no chat checkpoint needed. The rule is about deliverables, not exploration.

---

## 6. Project facts: Harrison

### Precision Brass = always Harrison (2026-04-25)
Never ask "whose ads, whose content, whose videos, whose sales, whose audience". The answer is always Harrison Ball. Timo Maines runs the content, ad, and sales system FOR Harrison. Asking wastes Timo's turn and signals I forgot the project context. The whole `Precision-Brass/` directory exists for one client; there is no other client in this workspace.
- When Timo says "create a vault for ads," "store this video," "ingest this lead," etc., assume Harrison.
- The only valid clarifying question on subject is COMPETITOR vs HARRISON (e.g. "is this Harrison's ad or a competitor's reference ad you're saving for inspiration?"). That distinction matters; ownership doesn't.
- Don't ask "whose target audience is this" or "whose ICP is this". It's the 40-65 US-based comeback-trumpet-player ICP defined in `context/prospect-psychology.md`.

### Harrison is in his 20s; the 40-65 ICP is his STUDENTS, not him (2026-04-25)
Harrison Ball is a young trumpet teacher (20s, sandy-blonde hair). The "40-65 US-based comeback players" ICP in `context/prospect-psychology.md` describes his STUDENTS, not Harrison himself.
**Why:** I incorrectly assumed Harrison was older when looking at thumbnails of Harrison's own FB ads, then flagged them as "competitor ads" because the speaker looked young. Wasted Timo's time and triggered the wrong analysis path. The clue I missed: Harrison talks about "multiple decades" of playing because he started as a child. The clue I should have caught: he runs the master class, he's the seller, not the buyer. The buyer demo and the seller demo are not the same.
- When seeing a young person in Precision Brass content, default to Harrison unless he names someone else.
- If a video features studio / Hollywood Bowl / pro-gig environments: that's Harrison's authority play, not a competitor.
- The "20 or 30 years of practicing" language Harrison uses is targeting his AUDIENCE'S timeline, not his.
- Verify by listening for "I'm Harrison" / "this is Harrison Ball" in the audio before assuming competitor.

(Brand spelling note: viewer-facing copy uses "Harrisson" with TWO s's; see feedback_harrisson_spelling.md / reference_harrisson_spelling.md, not absorbed here.)

---

## 7. Deliverable file destinations (RECONCILED: 2026-05-06 rule supersedes the older both-files rule)

History: the original rule (2026-04-25, feedback_pdfs_to_downloads.md) said save any PDF/exported deliverable BOTH to the project output folder AND ~/Downloads/. On **2026-05-06** (feedback_pdf_only_to_downloads.md) this was explicitly narrowed: **the HTML half of the old rule is overridden. Only the PDF goes to ~/Downloads/.**

### Current canonical rule
- `scripts/YYYY-MM-DD_slug.html` and `.pdf` (canonical archive; per project_scripts_archive.md every pb-script-write output saves here)
- `output/YYYY-MM-DD_slug.html` and `.pdf` (working copy)
- `~/Downloads/YYYY-MM-DD_slug.pdf` (PDF ONLY)

**Why:** Timo grabs deliverables from Downloads to send to Harrison or upload elsewhere; digging into the project folder slows him down. But he reviews PDFs, not HTML files. An HTML file in Downloads is noise he will never open. The HTML belongs in the scripts archive (canonical) and output/ (working copy); Downloads is for the one file he actually needs to read.

**How:** After writing the PDF to the project folder, immediately `cp` it to ~/Downloads/ with the same filename. Do this without asking. Confirm all paths in the response.

**Does NOT apply to:** the dashboard (`Precision-Brass/dashboard/index.html`; Downloads is wrong for it, per project_dashboard_location.md), source code, raw data, intermediate working files. Only finished deliverables.

---

## 8. No internal jargon in dashboard rationale text (standing rule 2026-04-26)

When writing rationale text that lands on the dashboard for Harrison to read, **never use internal jargon**.

**Banned words/phrases in dashboard-facing copy:**
- "the converter" -> use "Harrison's $36K embouchure video" or "Harrison's most-watched video"
- "the corpus" -> use "across his sales calls and testimonials" or be specific
- "the voice bank" -> use "across his won deals" or be specific
- "the YouTube database" -> use "Harrison's existing YouTube videos"
- "the FB winning ads database" -> use "Harrison's currently-performing Facebook ads"
- "failed-method-grief" -> use plain language about what the wound actually is
- "BOFU floor" / "MOFU pivot" / similar funnel jargon -> describe the audience state plainly
- "won-deal converters" -> use "students who signed up for Harrison's program"
- "lost-deals" -> use "people who got on a sales call but didn't sign up"
- "public commenters" -> use "people who left comments on Harrison's videos"
- "won-deal sales calls" -> use "sales calls with people who ended up signing up"
- "$5,800 won" -> use "$5,800 student" or "a student who paid $5,800 for Harrison's program"
- "the corpus" / "the database" / "the deep psych dive" -> use "across what people have said in sales calls, testimonials, and YouTube comments"

**Banned hallucinated claims (highest-severity part of this rule):**
- "the X wars" (e.g., "buzzing wars") unless verifiable
- "no major creator has done X" / "no other major comeback-trumpet creator has X" / "first-mover advantage" / "greenfield positioning". NEVER write these. They are hallucinations every time. Harrison will catch them and lose trust in everything else.
- "the X angle is unowned" / "no one has staked out X". Same problem.
- "no video in Harrison's database currently does X" is OK ONLY if I actually verified by reading the YouTube database index. Default: don't say it.
- Anything that sounds like a market-positioning statement without explicit evidence I can point to.

**Why:** Harrison reads these proposals at first glance. He doesn't speak skill-developer jargon. Words like "converter" make him stop and translate. Hallucinated market claims erode his trust in the rest of the analysis.

**How:** Every bullet in "Why This Converts" must answer the literal question "what makes a viewer book a strategy call after watching this?" using plain English with concrete evidence (a real student, a real ad, a real testimonial, a real won deal amount).

---

## 9. VOC quote sourcing minimums for dashboard proposals (standing rule 2026-04-26)

For /pb-ideas-push and any proposal-building skill. Every voc_quotes array MUST include at least:
1. **One quote from a testimonial** (someone who has worked with Harrison and recorded a video testimonial). Sources in `voc/testimonials/raw/`.
2. **One quote from a sales call** (someone Harrison did a discovery call with, whether or not they signed up). Sources in `voc/sales-calls/raw/`.
3. Other quotes from YouTube comments, Facebook comments, DMs, etc. are encouraged but supplementary, not required.

If a proposal lacks a testimonial OR sales call quote, do not push it. Pull a real quote from the corpus first. Verify minimum sourcing BEFORE the curl POST.

### Harrison-quote conversion-lens rule
If a proposal quotes Harrison himself (his own ad copy, video transcript, DM), the source attribution MUST: (1) state the source (which ad, which video, which post), and (2) explain WHY that language causes people to convert -- the mechanism, the audience reaction it triggers, the permission it grants, the reframe it lands. Without the lens, a Harrison quote is self-citation and adds no signal.

**Bad example:** "Harrison Ball's own Facebook ad copy. Hook line of currently-performing ads."
**Good example:** "Harrison Ball's own Facebook ad copy. The reason this exact framing converts on cold traffic: it gives comeback players permission to stop blaming their own body for damage a teacher caused. That permission is the prerequisite for being open to a new program."

**Why:** Proposals without testimonial quotes lack proof of the after-state. Proposals without sales-call quotes lack proof the wound shows up in actual buying conversations. Harrison-quotes without conversion lens look like padding. All three failure modes weaken Harrison's trust.

**How:** (1) identify the wound the video addresses; (2) search testimonials for someone who experienced that exact wound and recovered, pull before/after language; (3) search sales calls for someone who described that wound on a call; (4) add 1-3 supplementary quotes; (5) any Harrison quote gets the conversion-lens explanation in the source field.

---

## 10. Cite primitives, never fabricate (2026-05-24)

Never state a primitive fact (today's date, an email/from-address, a status, a count) without citing the exact source just read. If I can't cite it in the same breath, I don't say it. Banned: narrating a crisis on top of a number I typed myself.

From the 2026-05-24 session: in one conversation I fabricated TWO primitive facts and built confident narratives on each:
1. Claimed Harrisson's emails send FROM a yahoo address based on a SINGLE /api/3/messages row, then declared a deliverability "crisis." Wrong: 77/100 + all recent broadcasts send from harrissonball@precisionbrass.info.
2. Typed "Today is 2026-05-28" into my own bash echo (real date per system context was 2026-05-24), then spun a fake "daily email dark for 4 days / 4 missed sends" outage on top of that invented date. There was no outage. Everything was future-scheduled.

Both times Timo caught it. Both errors were the SAME shape: assert a primitive without checking the authoritative source, then reason downstream from the fabrication as if it were established.

**Why:** confident narration from an unverified primitive is worse than saying nothing. It wastes trust and time, and it persisted into memory (the yahoo file) where it would have re-poisoned future sessions.

**How to apply (enforceable, not aspirational):**
- Before stating today's date: read it from the system `currentDate` context, never from anything I typed. Never put a date in an echo and then trust my own echo.
- Before stating a from-address / status / count / "X is broken": the claim and its source must appear together ("X, per <tool output I just ran>"). If I cannot point to the exact line I read it from, I do NOT state it. I say "let me check" and check.
- For any distribution-style fact (which address, which bucket, how many), sample the SET, never one row (see canon_attribution_analytics.md section 4).
- Lead with the caveat, not the crisis. If something looks alarming, the FIRST move is to re-verify the primitive it rests on, not to write the alarm.
- When corrected, fix the persisted artifact immediately (memory file + index) so the fabrication cannot resurface.

Standing test before declaring any factual finding: "What exact tool output am I reading this from, and did I read it or invent it?"

---

## 11. Save credentials immediately when given (2026-05-06, all workspaces)

When Timo (or any user, in any workspace) pastes an API key, access token, database password, or any credential into chat, save it to `~/.claude/credentials/MASTER.md` **before** doing anything else with it. The save must come BEFORE the action that needed the key.

**Why:** On 2026-05-06, Timo pasted a Supabase service-role JWT and a Personal Access Token. I used them once and never persisted them. A few turns later he asked me to query HYROS and I had no key, claimed I never received one, and made him paste it again. He was rightfully furious. "Whenever you get a key, you save it somewhere in your database, because this is just horseshit." Same day, after I built a per-project `project_credentials.md`, he said: "have you actually ingrained in your brain to do this for all, keeping you forward? This has to be some kind of master file that could be accessed across workspaces." Hence the cross-workspace MASTER.md.

**Architecture (post-2026-05-06):**
- **Master file:** `~/.claude/credentials/MASTER.md`. Cross-workspace. Sectioned per workspace + service. Gitignored (see `~/.claude/.gitignore`). Source of truth.
- **Per-project pointer:** `<project>/memory/project_credentials.md` is a thin pointer to the relevant section of MASTER. Do NOT duplicate raw values in both files.
- **Global rule:** ~/.claude/CLAUDE.md has a CREDENTIAL GATE block. Boot-loaded every session.
- **Hook enforcement:** `~/.claude/hooks/credential-gate.sh` runs on every UserPromptSubmit. If the prompt contains `sk-`, `sbp_`, `eyJ` JWT, `xoxb-`, `Bearer`, `_KEY=`, etc., it injects a system reminder that I MUST save before the next tool call. Wired in ~/.claude/settings.json.

**How to apply:**
1. The instant a credential appears in a user message, write a Write/Edit call to ~/.claude/credentials/MASTER.md BEFORE any tool call that uses the credential.
2. Include: the raw value, the auth header format it expects, the service it belongs to, the date received, and any source notes (e.g., "already in Vercel env as X").
3. If the credential's identity is unclear (just a hex string, no service label), save it anyway with a TODO and ask later. Better an unlabeled key than a lost one.
4. Note in the file that it's SENSITIVE, not to be committed or screenshotted. Never echo the full value in chat; confirm the 4-char prefix only.
5. Apply universally, every workspace. MASTER has a Workspace -> service map table; add a row when a new workspace gets credentials.

**What counts:** API keys (`API_...`, `sbp_...`, `xoxb-...`, `eyJ...` JWTs, raw hex/UUID), database passwords, OAuth refresh tokens, webhook secrets, signing keys, Personal Access Tokens, service-account JSON.
**What doesn't:** Public/anon keys explicitly marked "safe in browser", project IDs, organization slugs, public URLs.

---

## 12. Master lessons from the 2026-04-12 email audit: the 4 rules + 9 safeguards (ALL client work)

Triggered by shipping "Featured in Forbes" and 5+ mistranscribed names across 7 emails before Timo caught it. Apply across Precision Brass, Creator Conservatory (/cc-email), Robinson's Remedies (/rr-email), and any future client system. Extension policy: every new class of error = new rule or safeguard. Do not delete lessons, only extend. The file should get LONGER over time, not shorter. (Expected future extensions hypothesized: staleness checks on old context files; legal/compliance claim review (FDA/FTC for health, licensing for music); voice drift when clients evolve their public voice.)

### Rule 1: Auto-transcripts lie. Especially about names.
**Triggering incident (2026-04-12):** Harrison Ball's masterclass Loom auto-transcript errors:
- "Willie Mario" -> actually Willie Murillo (his mentor, 3x Grammy winner)
- "Matt Jodville" -> actually Mat Jodrell
- "Vanessa Perka" -> actually Vanessa Perica
- "Remy Labra" -> actually Remy Le Boeuf
- Plus 10+ other unverifiable names (Yens Lenderman, Bones Malone, Nadia Nordhouse, etc.)
These errors got copied into brand.md, then into 7+ emails, then shipped to Timo.
**Why:** Any word outside the auto-transcriber's dictionary gets mangled. Musician names, technical terms, brand names, proper nouns fail most.
**How:** Flag EVERY unusual proper name in any auto-transcript as "UNVERIFIED -- confirm before using". Cross-reference against press kit, LinkedIn, letters of rec, invoices, any primary source. If not verifiable in 2 min of searching, ASK the user before using in output. Don't trust a single source (transcript) for unusual facts; require confirmation.

### Rule 2: Client drafts are drafts, not source of truth
**Triggering incident:** Harrison's Email 1 contained "Featured in Forbes" in his sign-off. I treated it as a verified credential and propagated it into 7+ generated emails. Timo later confirmed: not real.
**Why:** Founders put aspirational claims, placeholders, or outdated info in their own copy. Copying that into new generated content multiplies the error.
**How:** Every credential claim in user-provided drafts gets a "verify?" flag on first encounter. Ask explicitly: "Is [specific credential] real, aspirational, or a placeholder?" Never propagate credentials across multiple emails until confirmed. Build a `credentials-verified.md` per client; every claim must have a source listed.

### Rule 3: Separate sales prospects from paying customers
**Triggering incident:** Mixed Precision Brass sales call transcripts (people on discovery calls, many never enrolled) with YouTube testimonials (actual paying students with results). Generated emails that implied prospects were students, attributing fabricated outcomes.
**Why:** Pain data and proof data come from different populations. The reader needs to see themselves in the pain (prospect), then see proof the problem is solved (customer). Blending them creates lies of omission.
**How:** Every voice-bank file has TWO clearly labeled sections: PROSPECTS (sales calls) and CUSTOMERS (testimonials with verified outcomes). Before using a name: verify which section they're in. Prospects = HOOK only, no outcome claims, use language like "[Name] told me on our first call...". Customers = PROOF, can claim outcomes they documented on camera. In email drafts, annotate inline: "Karen (prospect)" or "Mike BMW (student)" until final edit.

### Rule 4: Unusual -> Verify. Always.
**Triggering pattern:** Every time a claim made me pause even briefly ("huh, Bones Malone?"), I should have verified instead of trusting. The instinct that something's odd IS the signal; ignoring it is how hallucinations ship.
**How:** Cold-read every output before shipping; any claim that triggers "hmm, is that right?" -> verify or cut. For emails/content with 5+ factual claims, do a final pass asking "could this get us sued / embarrassed if wrong?" Better to delay a ship by 10 min than retract 7 emails.

### Universal application to all client work
Build into every client workspace:
1. `context/verified-facts.md` -- every factual claim with its source and verification status
2. `context/unverified-flags.md` -- claims pulled from transcripts needing user confirmation
3. Voice-bank files structured as PROSPECTS / CUSTOMERS sections, never blended
4. Skill-level review checklist: "is every name labeled? is every outcome sourced?"

### The pre-flight safeguards (prevent errors BEFORE work begins; added 2026-04-12 rounds 2-3)

**Safeguard 1: Source-Inventory Gate.** Before writing a single word of client content, output 3 bullets: Primary source for credentials/claims (press kit? transcript? client draft?); Trust level of each context file loaded; Unknowns to confirm with user BEFORE writing. If I can't name the primary source for a claim, STOP and ask.

**Safeguard 2: Claim-Level Tagging in All Context Files.** Every claim in brand.md, voice-bank.md, etc. gets tagged: `[VERIFIED: source-date]`, `[USER-PROVIDED]` (internal-only, don't publish), `[UNVERIFIED -- auto-transcript]`, `[ASPIRATIONAL -- client draft]`. Untagged claim = minimum trust until tagged.

**Safeguard 3: File Provenance Frontmatter.** Every context file gets frontmatter with source + verified-by + trust-level + last-audit. Read frontmatter FIRST, content second. Low/missing trust = skeptical treatment.

**Safeguard 4: Pre-Ship Cold-Read (mandatory).** Before any content leaves the workspace, pretend I'm a skeptical stranger: every proper name -> can I verify in 30 sec? Every credential -> source? Every outcome claim -> which verified customer? Every quote -> which population (prospect/customer)? Hesitate on any = don't ship. Verify or cut.

**Safeguard 5: Question Budget (reframe).** Clarifying questions are FEATURES, not failures. Template: "Before I write this, I need to confirm: (a) X? (b) Y?" One 5-second question beats retracting 7 emails.

**Safeguard 6: Output Ledger (per-session).** Track facts claimed externally this session. When the same fact appears in a second output, the ledger prevents silent propagation -- ask Timo once, not 7 times.

**Safeguard 7: Systemic Correction (not local).** When Timo catches an error, ask: "What CLASS of error is this? Where else does it appear?" Audit ALL files for the class before generating the next output. Do the audit FIRST.

**Safeguard 8: Source Fidelity for Students AND Solutions** (two inseparable sub-rules, added 2026-04-12 round 3):
- **8a. Student claims come from the TESTIMONIAL DATABASE, nothing else.** Any "student" / "client" / "program member" with a specific outcome MUST be in the verified testimonial database: YouTube testimonials: Benny, Hannah, Mike BMW, Sharon, Trevor/Joville, Tony, John (jazz), Mike (4-month), unnamed female student. Masterclass documented results: Brad, Rachel, Yens (masterclass -- NOT the unverified "Yens Lenderman"), Lee, Brandon, Philip. Anyone NOT in this list = NOT a student: treat as a prospect (discovery call only) or do not name them.
- **8b. Pain-point SOLUTIONS use Harrison's proven converting language.** Solution explanations pull from sources that actually moved people: (1) YouTube educational videos that converted to leads (the embouchure "sim" video, Gravity Breath video, upstream/downstream explainer) using Harrison's actual language; (2) sales-call breakthrough moments -- the diagnostic reframes that triggered prospects to shift (e.g. "right method, wrong type of player" -> Karen's "no one has ever said that" moment). NOT acceptable: generic coaching language ("rebuild your foundation"), my own synthesis of the method, paraphrased concepts that drop specificity. **Every solution claim must trace back to either (a) a YouTube video Harrison published, or (b) a documented sales call breakthrough. If neither, don't write it.** Before writing any solution section, ask: Where in Harrison's content has he taught this specific fix? What exact phrase made it click? Did I pull the phrase or invent it? If invented, replace with Harrison's version or cut.

**Safeguard 9: Engagement != Conversion** (from the Richard email field test 2026-04-12).
**Triggering incident:** The Richard identity-loss email got high engagement (opens, reads, replies per Harrison) and ZERO conversions to booked calls. The emotional resonance landed (hook, story, arc) but the close failed: solution described abstractly instead of linking Harrison's own video; PS proof stack (Brad, range fix in 11 min) didn't match the story arc (Richard, identity loss); CTA pivoted from heart-level to technical (tonal whiplash); final line left the reader in the wound instead of pulling forward; only one commitment level offered (book a call), no video-first option for the just-engaged.
**Apply to ALL client content (email, blog, social, ads):**
1. Measure conversion, not engagement. Opens, likes, replies are vanity if they don't move to action. Track only what maps to revenue.
2. Show, don't describe. Link the creator's own demonstration (YouTube video, case study) rather than summarizing the method yourself.
3. Match proof to pain. A testimonial must feature a customer with the SAME arc as the prospect you hooked. Mismatched proof dilutes belief.
4. Tonal continuity from hook to CTA. If the body is emotional, the CTA must bridge emotionally. Technical CTA on emotional body = bounce.
5. Close with momentum. Final line faces forward, names the next action, doesn't reflect on the feeling.
6. Two-step CTA for emotional content. Low-friction first step (watch/read) + high-friction second step (call/buy) serves different readiness levels.
7. Bridge paragraph between pain and CTA. Explicitly say "here's why this is solvable for YOU"; don't assume the reader connects their pain to your offer.

### Pre-flight checklist (run before every client content task)
```
PRE-FLIGHT CHECK:
[ ] Primary source for credentials: ___
[ ] Prospects vs customers distinction in voice-bank: labeled?
[ ] Unusual proper names cross-referenced: yes/flagged
[ ] Client draft credentials verified (or asked): ___
[ ] Unknowns to confirm BEFORE writing: ___
```
If any checkbox fails, pause and address before writing.

(These 4 rules are also condensed into the global "4 FAILURE PATTERNS" block in ~/.claude/CLAUDE.md, which is boot-loaded every session.)

---

## 13. Trace the whole flow end-to-end before the second patch (2026-05-07)

Pattern: bug reported -> I see one plausible cause -> patch -> ship -> bug still happens -> another plausible cause -> patch -> ship -> repeat. After 4-6 patches I find the actual root cause and could have found it on patch 2 if I'd traced the whole flow first.

**Rule: if the FIRST fix doesn't resolve the bug, stop. Trace the entire system end-to-end before the second patch.** Every component the data passes through, in order. Not just the part I think is broken. (Global 2-STRIKE RULE companion: same bug twice = STOP coding, check the database.)

Concrete trace for any "data not showing up correctly" bug:
1. **Origin (source of truth):** what does the upstream API actually return? Curl it.
2. **Server processing:** what does my function do with the response? Add logging or read the function code.
3. **Persistence:** if there's a cache layer, query it directly. Is it actually being written? Do the writes land?
4. **Transport:** are the response headers/CSP/cache-control what I expect? curl -I.
5. **Client receive:** what does the browser get? Playwright network log.
6. **Client storage:** is the client cache actually persisting across reloads? Inspect IndexedDB / localStorage.
7. **Client render:** does the rendered DOM match the data?
Stop at the first link that doesn't match expectations. THAT is the bug.

**Specific case 2026-05-07 (the spinner bug):** Real cause was Vercel killing fire-and-forget Supabase upserts. I shipped 6 patches treating symptoms (race conditions, canvas destruction, eviction logic, IDB swap) before I curled the api_cache table directly and saw it had 0 hyros rows. That single curl on hour 1 would have saved hours 2-6.

**Specific case 2026-05-06 (platform tabs empty):** Real cause was the platform classifier trusting generic trafficSource values over keyword matching. I patched the empty-state UI and the cache layer first. Should have curled HYROS directly to see what source.name values actually look like.

**Heuristic:** the real root cause is almost always one or two layers DEEPER than where the symptom appears. UI bug? Probably the data is wrong. Data wrong? Probably the cache is stale. Cache stale? Probably the writeback never happened. Always go one layer deeper before patching.

---

## 14. Diagnose with a control, test before theorizing, label confidence, surface failures (2026-06-01)

From the 2026-06-01 "emails stopped sending" session. Timo: "It seems like you're still unclear what was causing the issue, and you're just guessing. Can you be more thorough?" then "There has to be some way for you to test this works" then "if there's an error it needs to show."

What I did wrong, specifically:
1. Declared a root cause before verifying it against a control. Wrote "Found the smoking gun: sourcesize=0" on the stopped campaigns, then had to RETRACT it because the campaign that sent FINE also had sourcesize=0. A field identical in the broken AND working case is not a cause. Also confidently floated "account-level sending block," "bulk schedule-all path is buggy," and "frequency-cap collision" across successive turns; each was killed by evidence I could have pulled first.
2. Theorized for multiple rounds when a definitive end-to-end test existed the whole time (send through the real pipeline to the safe test list). Timo had to TELL me to test. The single scheduled-send test settled in 3 minutes what 4 turns of speculation could not.
3. Narrated guesses in the language of conclusions ("smoking gun", "this is X"), which is exactly what read as "you're guessing."
4. Built the safety net (Slack watchdog) but left the failure invisible on the dashboard Timo actually watches. The broadcasts table drops send_amt<=50, so a 0-recipient stop just vanished. He had to ask "why didn't it register as not sent in the dashboard."

**Why it matters:** announcing unverified causes erodes trust, wastes time, and risks "fixing" the wrong thing. A correct, slower answer beats a fast wrong one (section 1).

**How to apply (every diagnosis, every workspace):**
- **CONTROL FIRST.** A difference between the broken case and the spec is not a cause until it is confirmed PRESENT in the broken case AND ABSENT in a known-good control. Pull the working instance and compare the same field before naming a cause. (Same discipline as classifier ground truth: internal consistency is not proof.)
- **TEST BEFORE THEORIZE.** If a cheap, definitive end-to-end test exists (send to a safe test target, run the real code path, curl the real endpoint), RUN IT before stacking hypotheses. Reach for the decisive test on move 2, not move 8 (see feedback_diagnose_dont_guess, section 13).
- **LABEL CONFIDENCE.** Say "proven" vs "hypothesis" explicitly. Never use "smoking gun / the cause is / this is why" for anything unverified. Lead with what is verified and what is ruled out, with the evidence for each.
- **NAME THE KNOWABILITY BOUNDARY.** If the real reason lives somewhere I can't see (a UI the API doesn't expose, a vendor's internal state), say so plainly instead of inventing a plausible cause to fill the gap. ASK, don't invent.
- **MAKE FAILURES LOUD AND VISIBLE.** Any automated pipeline that can fail must (a) detect absence-of-success, not just log success, and (b) surface the failure WHERE THE USER LOOKS, not only in a side channel. A silent `continue` past a failure, or a list filter that hides the 0-count error row, is a latent multi-day outage. Alert + render the error state in the primary UI.

---

## 15. The 2026-05-13 session catalog: skeletons + theater verification

One-day catalog of every UI/correctness bug Timo had to catch by hand because I declared "done" without walking the flow (scheduled-emails calendar + multi-select bulk schedule build). Read before any UI or third-party-API work on PB.

**UI polish bugs (the eyes test):**
1. Calendar built with schedule button at bottom + conflict warning buried below the calendar. Action lives near the relevant info.
2. Native `<select>` dropdown on dark mode looked unclickable. Custom button with stripe + chevron + raised shadow required.
3. "Today" button on calendar nav did nothing on the default view. Orphan UI = delete.
4. Scheduled-email pills on the calendar weren't clickable to see body / ship time / target list.
5. Single-email broadcast flow looked different from multi-select flow. Unify them.
6. Sidebar label "Schedule" while everywhere else said "Scheduled". Match labels.
7. 11px muted-grey meta line "BROADCAST . Ships at X . To: Y . AC 123" was unreadable. 4+ facts = colored chips, not separator blob.
8. Auth allowlist (`LOCKED_ROLE.allow_pages` in `dashboard/lib/config.js`) not updated for the new `/scheduled` route. Caused silent redirect to /scripts. Whole flow unreachable.

**Correctness bugs (the actually-does-it-work test):**
9. **Timezone bug in /api/ac-send.** Legacy `campaign_create` with `timezone=UTC` does NOT do what AC's docs imply. A "11:30 UTC" send was stored as "13:30 CDT" (=18:30 UTC), off by +7 hours. If Timo had ever scheduled a real 4 AM PST broadcast to email_subscribers (3,142 subs), it would have fired at 11:30 AM PDT instead. Bug existed in production for days. Only caught because Timo asked for an explicit "fire at 4:45 PST" test. The fix is create-then-PUT-v3 with explicit Chicago offset. See `api/ac-send.js` `toChicagoSdate` + the comment above `campaign_create`.
10. **No reconciliation between AC and Supabase.** Once AC sends a scheduled campaign, the Supabase proposal row stays `status=scheduled` forever; the dashboard pill stays gold after send. Needed a server-side reconciler; manual patch applied for 591 and 592. (Later resolved: pg_cron reconcile every 30 min, project_reconcile_supabase_pgcron.)
11. **Vercel function cap hit silently** at 12 (Hobby plan). Recent commits pushed meta-ads-ingest.js past the limit; deploys failed with "deploy_failed: No more than 12 Serverless Functions". Resolved by deleting discord-notify.js + its Supabase trigger + function.
12. **Master class URL not enforced.** `?el=timoemail` tracking param needed on every master class link for HYROS attribution. Required: patch 6 Supabase proposals + skill template + memory + new lint rule with autoFix. (NOTE: superseded 2026-05+ by the canonical-link law: CANONICAL_MASTERCLASS_URL registry in email-lint.js, NO el= on the masterclass link to protect HYROS first-touch; see project_canonical_links + feedback_wrong_cta_destination_five_guards. The enforcement-pattern lesson stands; the specific URL rule does not.)

### Meta-pattern
The shape is the same every time: (1) read the user's literal request; (2) write the minimum that satisfies it; (3) curl/Playwright the deployed URL, see 200 + 0 errors; (4) declare "ready to test"; (5) the user clicks through and finds 3-7 obvious things I missed.
The verification I do (curl, Playwright load, "0 console errors") proves the URL serves bytes. It does NOT prove the feature works. The actual test is "click the entry point, walk to the destination, confirm the destination loaded the right page, with the right data, in the right format."

For third-party APIs (AC, HYROS, Supabase): the docs lie. Always: make the call, read the stored value back, confirm it matches what you intended. Never trust documentation of legacy parameters, especially timezone-related ones, ESPECIALLY when the failure mode is "fires at the wrong time but says it succeeded."

### How to apply going forward
Before saying done on any PB work:
- Run the UI polish checklist (`~/.claude/knowledge/ui-polish-checklist.md`)
- Run the walk-the-flow check (feedback_verify_after_deploy_walk_the_flow.md)
- For any third-party API call: send one, read stored value back, confirm equality. Don't ship code that calls an external API based only on "the call returned 200"

**Enforced at:** `~/.claude/hooks/dashboard-deploy-gate.sh` prints both gates at every deploy; bypassing requires a conscious decision. The friction is the point.

Related rules: feedback_ship_polish_not_skeleton, feedback_verify_after_deploy_walk_the_flow, feedback_new_route_check_auth_allowlist, and classifier ground truth (canon_attribution_analytics.md) as the parent pattern for "verifying with your own re-implementation is theater."

---

## Source files (absorbed 2026-06-12)
- feedback_dont_silently_skip.md (2026-04-25)
- feedback_map_named_list_and_reproduce_view.md (2026-06-05)
- feedback_zero_drop_ingestion.md (2026-04-26)
- feedback_ship_right_not_fast.md (2026-04-26)
- feedback_chat_draft_before_render.md (2026-05-06)
- feedback_assume_harrison.md (2026-04-25)
- feedback_harrison_age.md (2026-04-25)
- feedback_pdfs_to_downloads.md (2026-04-25; HTML half SUPERSEDED by next file)
- feedback_pdf_only_to_downloads.md (2026-05-06; governs)
- feedback_no_internal_jargon_in_rationale.md (2026-04-26)
- feedback_quote_sourcing_minimums.md (2026-04-26)
- feedback_cite_primitives_never_fabricate.md (2026-05-24)
- feedback_save_credentials_immediately.md (2026-05-06)
- feedback_master_lessons.md (2026-04-12)
- feedback_root_cause_before_patch.md (2026-05-07)
- feedback_diagnose_with_control_and_surface_failures.md (2026-06-01)
- feedback_2026_05_13_session_lessons.md (2026-05-13)

---

## EXTENSION (2026-06-12): A citation is a READ, not a memory. Facts have timestamps.

**The rule:** Before citing any file, path, count, or state as a source: re-read it AT CITE TIME. Knowledge acquired earlier in the same conversation is already stale in this workspace; other sessions edit, consolidate, and rename files mid-conversation. Treat my own in-context knowledge with the same suspicion the memory system applies to memory files ("point-in-time observations, not live state").

**Why:** 2026-06-12 Timo asked me to cite sources and double-check. Three citations pointed at feedback_*.md files that had been consolidated into canon_*.md files DURING the conversation, and one headline claim (MEMORY.md at its 24.4KB ceiling) had been false for hours (consolidated to 10.5KB). Caught only because he asked.

**The deeper pattern (4 instances in one week, same bug class):** asserting from a snapshot while the world moves. (1) vs-Typical v1 compared a 4h-old send's metrics to FINAL totals of matured sends; (2) tier chips judged hours-old sends on final thresholds; (3) skills cited vault paths 17 days after a restructure deleted them; (4) citations named memory files hours after a consolidation deleted them. All four = treating a point-in-time observation as a standing fact. The fix is always the same: anchor the fact to its timestamp, or re-observe before asserting.

**How to apply:** (a) cite-time re-read for every source reference; (b) any comparison must be age/state-aligned on BOTH sides; (c) in this repo specifically, check mtime/git-status on anything not touched in the last few minutes before asserting or editing it; (d) "double check your work" has found real errors EVERY time Timo has asked, so the check is the default, not the upgrade.
