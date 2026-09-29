# Handoff — 2026-09-29, migration: glossary rows, the comment guard, the repeat tick

## Notes from memory

- The person agreed with every recommendation of every round and asked for plain explanations twice: what a repeat is against a superseded Case (C11), and the two points of the first pre-spec pass that needed a decision.
- Case 520 went through two pre-spec passes: the rule "a meaning says only what its `where` page says" meets terms that several schema pages define (`deferred_by`, `origin`). The last text opens `deferred_by` with no category and `origin` with "On a page a Case created"; the next reading of the table judges it.
- Case 524 grew a sub-case 524.3 at pre-spec, because the showing rule belongs in `case-schema.md`, not in the grill-me skill. Its context was rebuilt once more to drop Cyrillic.
- Case 523 changes only the `method` of `estimate-case-protocol-defers-in-one-reply`; its Criterion and its `failed` status stand by design.
- The session passed 400 000 tokens at the Retro; the person was told.

## Direct instructions to the librarian

- Case 520 was ratified four times, 521 and 524 three times, 522 and 523 twice: the ledger holds each decision line once (the hook skips a line it holds), but check that no entry is a repeat, and that each Case's then block in `spec.md` is its last text.
- Three Cases update `rule-case-protocol` (521.4 a pair in the short-form paragraph, 523 only a `change` with `{supersedes:case 518}`, 524.3 a pair in the showing paragraph); pre-spec found each anchor once, before and after the others.
- 521.3 carries `{supersedes:case 519}` and 523 `{supersedes:case 518}`: `decision-case-519` and `decision-case-518` should go `superseded`, and their `deferred_by` leave `rule-estimates-schema` and `rule-case-protocol`. Case 525 carries `{supersedes:case 517}` on a defer of `rule-documentation`, so `deferred_by` there swaps 517 for 525.
- `estimate-materialize-marks-a-comment` is the one `create`; its slug was free at pre-spec.
- `make lint` stopped at the backlog check before the work, and `guppi backlog` in the run rewrites the file.

## What actually got done

Ratified: 520, 521.1, 521.2, 521.3, 521.4, 522, 523, 524.1, 524.2, 524.3, 525.

What got done: commits dd08a1b (code of 521.1, 521.2, 522) and 3520653 (the session folder); `guppi/materialize.py`, `guppi/ratified.py`, `guppi/generate.py`, `tests/test_materialize.py`, `tests/test_ratified.py`, `tests/test_generate.py`; make test 923 passed, 2 skipped; make style clean; readings L1–L4, L23, L24; the Retro readings of `estimate-retro-red-in-the-baseline-is-not-charged` (passed) and `estimate-retro-report-holds-each-fact-once` (failed: a reading named in two parts of the report).

What is not done:
- The read line of `estimate-glossary-terms-defined` under Case 520: its reading L4 stands before the first decision line of Case 520, so `generate` skips that section and the line stays open; its reading waits for a session after this run renders the table.
- `make lint` red before the work: `backlog: vault/wiki/backlog.md differs from its sources`, the Frontier of this session changing the defer counts.
- Eight more values cut at ` #` stand in archived Specs of 2026-09-12 to 2026-09-21 (`change` and `purpose` holding `## …` unquoted), the cause of case 519; `materialize` reads no archive, so nothing is affected now.
- PyYAML does not cut a value at a tab before `#`: it refuses the block. The context of Case 521 says it cuts; the mark and the refusal hold either way.
- `insight-materialize-estimate-update-lifts-the-criterion-whole` describes behaviour gone since case 378.4 (`names_a_part` in `lift_criterion`); the next Plan Mode can reject it.
- The Case 524 context took the person's relayed words untranslated at a rebuild: lesson `lesson-case-build-rebuild-quotes-the-relayed-words`.
- Two pre-spec passes on the glossary rows of cross-category terms: lesson `lesson-glossary-one-where-for-a-term-many-schemas-define`.
- Work readings W1 and W6 skipped though their moment had come: reading `estimate-work-mode-takes-the-work-readings`, failed.
- The defer of Case 525 closed the last Cases line and ended on the `/pre-spec` question, the branch `estimate-case-protocol-defers-in-one-reply` reads; this session updates that Estimate, so it is no reading.
- The live reading of `estimate-context-size-warns-past-the-limit`: the `UserPromptSubmit` warning came at 408 159 tokens and `uv run pytest tests/test_context.py -k limit` gave 3 passed; the `Stop` line was not read, so the reading waits.

23 boxes wait for the librarian.
Read in a later session: `estimate-spec-write-writes-a-defer`, `estimate-materialize-marks-a-comment`, `estimate-generate-ticks-the-spec`, `estimate-case-protocol-defers-in-one-reply`, `estimate-skill-grill-me-asks-in-rounds`, `estimate-case-build-writes-a-plain-round`, `estimate-case-protocol-shows-the-built-case`.
