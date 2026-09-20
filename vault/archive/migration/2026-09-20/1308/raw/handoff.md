# Handoff — 2026-09-20, session 1308: the tick on a reading, the schema as a Render, reword

## Notes from memory

- The person hesitated twice on the same question: who ticks the `read` line of a
  Spec, and how a script can judge a reading it did not take. The answer that held:
  the script judges nothing — the agent's `estimate[...]` line is the judgment, and
  `generate` only ticks the line when it applies that judgment (270.1). The person
  then asked why the librarian did not tick before; the answer was the contract of
  226.1, not a defect.
- The person chose, against my first recommendation, to move the Case schema out of
  `CLAUDE.md` and load it at `/hi` (273): compaction is not used, subagents do not get
  `CLAUDE.md`, and the person will watch whether the agent's behaviour changes. If it
  does, that is an `error` lesson and a Case, not a repair.
- `replace` inside an Estimate's Criterion (C3) was rejected after a long exchange:
  the script cannot tell a rename from a change of meaning. What was ratified instead
  is `reword` on the owner rule (274.1) with a regulated procedure — the agent greps,
  puts every place and its meaning in `context`, the person signs the pairs. Its first
  use, 274.2, was itself wrong (the word `pre-task` meant the vault query in most
  places) and pre-spec caught it; 277.4 supersedes 274.2 and does the sweep by
  `replace` per page, by meaning. So no `reword` is applied in this session:
  `estimate-generate-rewords` stays `pending` until the first real one, and
  `rule-page-generation` therefore stays `draft` after your run.
- Three amendments to already-signed text were ratified at pre-spec as a block (the
  scope of `reword` in 274.1, "a child of a `full` page" in 273.1, `set.purpose` on
  the recuts of 272.1 and 273.2); the same decision lines stand, the Spec text changed.
- The reading of `estimate-case-protocol-case-form` (277.5) was taken at Retro on this
  session's Cases, `passed`, with two departures named in the line.
- The person's decision at the end of Work Mode: keep the late decision line of 277.3
  on `decisions-schema` — the grep found a sixth Rule-class file, I edited it and
  backfilled the line; a lesson was written for the behaviour, the content stands.

## Direct instructions to the librarian

- Order matters on three pages, and the ledger order gives it: `estimate-case-protocol-loaded`
  is updated by 270.2 then 273.1 (the second carries the final Criterion, `given` + `when` +
  `then` of 273.1); `estimate-claude-md-rendered` by 272.1 then 273.3 (the second final);
  `rule-claude-md` by 272.1 then 273.3 — the `replace` pairs of 273.3 assume 272.1 landed
  (the marker lines, the How it works sentences). `rule-case-protocol` by 270.2 (a `replace`
  in the old Render) then 273.1 (`sections: Render` whole, `governs`, `render_mode`,
  `parent`). `rule-page-generation` by 270.1 then 274.1. `rule-materialize` by 274.3 then
  277.1 (its `replace` of "and `rename` when the item carries it (case 258.2)" assumes
  274.3 did not touch that sentence — it did not; 274.3 inserted a sentence after
  "(case 204)").
- `rule-case-protocol` changes `governs` to `vault/wiki/case-schema.md` and `parent` to
  `rule-plan-mode`; 273.1 sets `children` of `rule-plan-mode` and 273.3 sets `children`
  of `rule-claude-md` to `[rule-language, rule-agent-writing]` — the two creates of 272
  append to that list first, then the set replaces it. If `render` complains that a child
  governs another file, the parent change of `rule-case-protocol` did not apply; report,
  do not repair.
- `render` will write `vault/wiki/case-schema.md` for the first time from a Rule page
  (273.1). I dry-ran the Render text against the hand-written file: the differences are
  the header, five new sections (Plan Mode and the Frontier, The vault before a `create`,
  the ledger paragraph in What a Case produces, The acknowledging reply, The harness),
  the tick sentence of 270.2, the Language pointer, `pre-spec` in two lines — 118 → 136
  lines. Your render's diff line for it is expected; every other stderr line is a flag.
  Also expected: `CLAUDE.md` (three changes: the memory sentence, two markers in place
  of Language and Style, the protocol marker and the schema import gone),
  `.claude/skills/hi/SKILL.md` (one `@` line), `.claude/skills/retro/SKILL.md`,
  `.claude/agents/librarian-guppi.md`.
- The `read` lines: 270.1 is live in your run for the first time. `generate` should tick
  `- [ ] read …` lines for the estimate entries of this yaml — lines 308, 488, 544 of
  `raw/2026-09-20/0958/spec.md` (W1–W3, the readings of `documentation-completes`,
  `brief-written`, `hi-writes-frontier`), and lines 56 and 829 of
  `raw/2026-09-20/1308/spec.md` (`generate-ticks-the-spec`, `materialize-assembles`),
  and line 1060 (`case-protocol-case-form`, read at Retro). If any of those stays
  `[ ]` after your run, that is a flag for the brief — the mechanism failed live.
- `reword` is not in this yaml: 274.2 is superseded by 277.4 (`{supersedes:case 274.2}`
  on the `rule-ask` line). Its four entries should carry `superseded_by`; if materialize
  marks them otherwise, report.
- Two `file` items name `case-schema.md`: 270.2 (by hand, done in Work Mode) — mark as
  applied by hand as usual. After 273.1 lands the file is governed; do not edit it.
- Index check: `rule-language` and `rule-agent-writing` are new rules whose text was a
  section of `rule-claude-md`'s Render until now — not duplicates, the text moves.
  `estimate-language-followed`, `estimate-agent-writing-followed`,
  `estimate-generate-rewords` are new Estimates; the last has no reading.
- Synthesis: two new lessons —
  `lesson-work-mode-check-widened-the-list-and-the-agent-acted` (a `tasks` check widened
  the ratified list and the agent acted instead of returning) and
  `lesson-reword-pairs-signed-before-the-places-were-read`. Compare the first with
  `lesson-agent-memory-is-not-the-product` (the agent acting where a Case was due) and
  with any lesson on a subagent's or agent's fork returning as a Case; the second with
  `lesson-spec-change-text-quotes-a-wikilink-bare` (the agent checking one place and
  not the others) — a candidate root cause "the agent verifies the place the Case is
  about and not the other places the change reaches". Judge; do not force a cluster.
- Readings due after your run, all for the next session: `estimate-case-protocol-loaded`
  (the first turn after `/hi`), `estimate-retro-loads` (the first `/retro` after the render),
  `estimate-documentation-completes` (your run, read in the next), `estimate-claude-md-rendered`
  (`render --check` and the session start), `estimate-language-followed`,
  `estimate-agent-writing-followed`, `estimate-internal-context-loaded` (the `/hi`),
  `estimate-case-protocol-ledger-line-form` (`case-schema.md` and `index.md` §4),
  `estimate-generate-rewords` (the first `reword`, no date). The Spec 1308 has two `read`
  lines for `estimate-case-protocol-loaded` (98, 577) and for `estimate-claude-md-rendered`
  (259, 693): one reading each, the second line closes by hand at the next Retro.

## What actually got done

- Closed: 270.1–270.3, 271, 272.1–272.3, 273.1–273.3, 274.1, 274.3, 275, 277.1–277.6;
  274.2 superseded by 277.4; 276 the defer of Slice 3b (`rule-work-mode`,
  `rule-subagent-guppi`, the twelfth).
- Code, commit `10baf3d` on `migration`: `guppi/generate.py` — `READ_LINE`, `tick_read`,
  `raw_specs`, `Vault.tick` on estimate entries and folded creates (270.1);
  `REWORD_CATEGORIES`, `REWORD_FIELDS`, `Vault.owner_text`, `reword_text`,
  `reword_pairs`, `reword` among the update keys (274.1); the docstring.
  `guppi/materialize.py` — `reword` carried as a list of pairs, `incomplete: [reword]`
  otherwise (274.3). Tests: `tests/test_generate.py` +6 (reading ticks) +5 (reword),
  `tests/test_materialize.py` +1, `tests/test_render.py` +1 (a `full` page into
  `vault/wiki/case-schema.md`, passes without a code change). 455 green, style clean.
- By hand: `vault/wiki/index.md` (8 places: §1 and §2 on the schema, §10 the librarian's
  ban with its exception, §5 the Rule-class map, §3 three `pre-task` → the vault query,
  two `pre-task` → `pre-spec` on the slug guard), `glossary.md` (rows 70, 86, 88),
  `rules/schema.md` (lines 19, 64, 157), `entities/schema.md` (2), `estimates/schema.md`
  (1), `decisions/schema.md` (1, the sixth file), `case-schema.md` (the tick sentence of
  270.2 and two `pre-spec`; the render overwrites it with the same words).
- W5: the boxes of 0958 lines 191, 249, 432 and 0740 line 172 ticked by hand.
- Readings `passed` this session: `estimate-documentation-completes`,
  `estimate-brief-written`, `estimate-hi-writes-frontier` (W1–W3),
  `estimate-generate-ticks-the-spec`, `estimate-materialize-assembles` (pytest, the live
  part your run), `estimate-case-protocol-case-form` (Retro).
- Not done: the pages, the renders and `guppi sprint` — yours; the readings listed
  above — the next session; `estimate-generate-rewords` — the first `reword`; the
  `grep` checks after your run (Spec lines 783, 863, 1028) and the diff of the first
  rendered `case-schema.md` (575) — the next session; Slice 3b — defer 276.
