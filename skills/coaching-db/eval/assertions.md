# Coaching DB Skill. Binary Assertions

Run these after any change to the skill. All must pass.

## Structural

- [ ] `~/.claude/skills/coaching-db/SKILL.md` exists
- [ ] `SKILL.md` has frontmatter with `name: coaching-db` and `user-invocable: true`
- [ ] `references/` contains `voc-methodology.md`, `funnel-taxonomy.md`, `use-case-tags.md`, `mine-angles.md`, `anti-hallucination.md`
- [ ] `templates/` contains `quote-entry.md` and `voice-bank.md`
- [ ] `scripts/` contains `vtt-to-markdown.py`, `build-voice-bank.py`, `fetch-youtube-transcript.sh`
- [ ] All Python scripts have a `main()` and argparse-based CLI
- [ ] Shell script is executable (`chmod +x`)

## Behavioral. `/coaching-db init`

- [ ] Creates `voc/raw/{sales-calls,testimonials,youtube-transcripts,youtube-comments,facebook-comments,dms}/` in cwd
- [ ] Creates `voc/quotes/` and `voc/personas/`
- [ ] Writes `voc/config.yaml` with client name and funnel stages
- [ ] Does not overwrite existing `voc/` data

## Behavioral. `/coaching-db ingest`

- [ ] YouTube URL input produces a `raw/testimonials/*.md` or `raw/youtube-transcripts/*.md` file
- [ ] Folder of VTTs input produces one `.md` per VTT
- [ ] Each raw file has frontmatter with `source_type`, `speaker_type`, `transcript_source`, `transcript_confidence`
- [ ] Existing raw files are never overwritten on re-run

## Behavioral. `/coaching-db extract`

- [ ] Spawns parallel Agents, batch size max 6
- [ ] Output JSONL entries have all required fields (quote, speaker_type, speaker_name, source_file, source_timestamp, pain_point, emotional_trigger, funnel_stage, use_for, mining_angle, confidence)
- [ ] No entry has `confidence: high` if the source is auto-captioned
- [ ] De-dup by (quote, source_file) works on re-run
- [ ] Already-extracted files are not re-extracted

## Behavioral. `/coaching-db mine <angle>`

- [ ] Reads ALL raw files (not just the delta)
- [ ] Tags every new quote with `mining_angle: <angle>`
- [ ] De-duplicates against existing JSONL
- [ ] Does not touch already-extracted quotes

## Behavioral. `/coaching-db synthesize`

- [ ] Regenerates `voc/personas/voice-bank.md` from scratch each run
- [ ] Voice bank has sections: Before state, Pain points, Failed methods, Transformation, Identity, Why Coach, Recommendations, Surprising angles, Funnel indexed, Use-case indexed, Gaps
- [ ] Attribution format is `*Name, YYYY-MM*`
- [ ] Gaps section auto-flags thin stages/use-cases
- [ ] No em dashes anywhere in output

## Behavioral. `/coaching-db status`

- [ ] Reports raw file counts per source type
- [ ] Reports quote counts by funnel stage, pain point, use_for, speaker_type
- [ ] Flags gaps (zero-counts, thin stages)

## Anti-hallucination gates

- [ ] Every extracted quote matches an exact substring in its `source_file`
- [ ] `speaker_type` matches raw file frontmatter default unless explicit override
- [ ] No quote tagged `high` confidence from an auto-caption source
- [ ] Unknown speakers tagged `unknown`, not guessed
- [ ] Extraction agent reports honest low-yield, does not fill quota
