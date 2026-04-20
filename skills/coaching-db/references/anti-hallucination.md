# Anti-Hallucination Gates

The four failure patterns (from Timo's global CLAUDE.md) applied to VOC work. Every extraction run must pass these gates or reject the output.

## Gate 1: Verbatim only

**The rule:** every quote must be copy-paste traceable back to a specific `source_file` at a specific `source_timestamp`.

**Why:** paraphrased quotes feel plausible but do not exist in the raw. They can't be defended if questioned. They undermine the copy they power.

**How to apply:**
- Extract the exact span of text from the raw transcript.
- If you rephrase, stop. Re-extract the actual words.
- Punctuation cleanup and sentence-boundary adjustment are permitted. Word substitution is not.
- If the speaker stumbled ("I was, I mean, I couldn't"), keep the stumble if it is vivid. Clean only if it obscures meaning.

## Gate 2: Prospects are not customers

**The rule:** `speaker_type` defaults match source type, not vibes.

| Source type | Default speaker_type |
|---|---|
| Sales call | prospect |
| Testimonial video | customer |
| YouTube comment | commenter |
| DM | commenter (unless known customer) |

**Why:** Timo's master lesson. Writing ads with customer language when the speaker is actually a prospect misrepresents the copy. It also pollutes the BOFU pool with TOFU voice.

**How to apply:**
- On extraction, use the raw file's frontmatter `speaker_type` as the default.
- If the transcript reveals the speaker is already a paying customer (they reference starting the program, past lessons, specific results), override to `customer` with a note.
- Do not promote `prospect` to `customer` based on enthusiasm alone. A motivated prospect is still a prospect.

## Gate 3: Auto-transcripts lie

**The rule:** confidence cap at `medium` for any transcript sourced from YouTube auto-captions, Zoom auto-captions, or any unverified machine transcription.

**Why:** global failure pattern #4. Auto-transcripts miss words, substitute words, mis-punctuate in ways that reverse meaning. A quote extracted at `high` confidence from an auto-caption will fail manual QA.

**How to apply:**
- Check `transcript_source` in the raw file's frontmatter.
- If `youtube-auto-captions`, `zoom-auto-captions`, or equivalent: cap extracted quote confidence at `medium`.
- Reserve `high` confidence only for human-reviewed or speaker-verified transcripts.
- `low` confidence is for quotes where the transcript is clearly garbled but you think you have the gist.

## Gate 4: Unusual = verify

**The rule:** if a proper name, technical term, or credential appears in an extracted quote and the raw transcript is machine-generated, flag the quote for manual review.

**Why:** auto-captions mangle proper names. "Schlossberg" becomes "Schlashberg." "Stamp" becomes "Stump." Extracting these verbatim propagates the error. Worse: extracting them confidently makes them look correct in downstream copy.

**How to apply:**
- If a quote contains a proper name (teacher, method, piece, composer) and the transcript is auto-captioned: set `confidence: low` OR add a flag comment in the JSONL entry.
- The downstream content generator must check flagged quotes before using them in production copy.
- When possible, cross-reference proper names against known trumpet-world terms (Clarke, Stamp, Schlossberg, Caruso, Arban, Maggio, etc.).

## Gate 5: Empty extraction is valid

**The rule:** if a raw file yields fewer than 3 high-impact quotes, report that honestly. Do not manufacture quotes to fill quota.

**Why:** quota-filling pushes paraphrases and low-value generic quotes into the JSONL. Those pollute the voice bank and make the downstream content generator sound generic.

**How to apply:**
- Target 8-15 quotes per file. But respect the ceiling: if a 20-minute transcript only has 2 gold quotes, report 2.
- In the extraction agent's report, flag files with unusually low yield for possible re-mining under a different angle.

## Verification checklist (run after every extraction)

Before merging per-batch JSONLs into `voc/quotes/all-quotes.jsonl`:

1. Spot-check 5 random quotes. Grep the raw file for the exact quote string. If any miss, reject the batch and re-run extraction with stricter verbatim instructions.
2. Confirm every entry has `source_file` and `source_timestamp`. Reject entries missing either.
3. Confirm `speaker_type` matches raw file frontmatter default unless explicitly overridden with justification.
4. Confirm no `high` confidence on auto-captioned sources.
5. Confirm all `use_for` tags are from the approved list (hook, content-idea, ad-copy, email-subject, email-conversion, testimonial).
