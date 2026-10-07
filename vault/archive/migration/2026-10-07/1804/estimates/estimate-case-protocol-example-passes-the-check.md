---
type: estimate
kind: QA
status: archived
target: "[[rule-case-protocol]]"
purpose: Whether the example Case of case-schema.md, in the chat form case-guppi writes, passes the check the SubagentStop hook runs over the file of a Case, so the form it shows stays a form the scripts accept
method: uv run pytest tests/test_case_schema.py, passed and not skipped
checked: 2026-10-05
origin: raw/2026-10-05/0311/ledger.md#case-646
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Criterion

When:
`tests/test_case_schema.py` runs under `uv run pytest`. It reads the block tagged `case` in `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, and runs over it the function of `guppi/casecheck.py` that the `SubagentStop` hook of `rule-case-check` runs over the Cases of a file. It runs in a temporary project that holds the schema files of the vault and the pages the example updates.

Then:
`vault/wiki/case-schema.md` holds, under its own heading after its `## Language` section, one block tagged `case`: one Case with sub-cases, in the chat form that `case-guppi` writes into its file.
**＋** The example holds a `create` and an `update` with their sub-points, a `replace` pair whose values hold a backtick in spans padded by one space, a `set` in a fenced block, an `update` of an Estimate whose Criterion it replaces, a read line for each Estimate it creates or replaces, and its ledger lines in a quoted fence under `ratification`.
**＋** The example's `context` says what the sentence around the match of its `replace` pair names.
**＋** The paragraph before the block says that the example passes the check of the `SubagentStop` hook of `rule-case-check`, and that the check, not the paragraph, is the source of the limits; it lists no limit.
**＋** The check gives the example no finding and no note, and the test passes.
**＋** A change of the check that gives the example a finding or a note fails the test, which prints it.
**＋** The test reads the example from `vault/wiki/case-schema.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
**－** While `vault/wiki/case-schema.md` holds no block tagged `case`, both tests of `tests/test_case_schema.py` fail with a message that names the file; no test of the file is skipped.
**－** The Spec example and the limits that the prose of `vault/wiki/case-schema.md` already states stay as they are.

## Result

2026-10-05, at the /hi of session 1616: uv run pytest -q -rs tests/test_case_schema.py 2 passed, none skipped

## History

- 2026-10-05 created · [[decision-case-646]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L8
- 2026-10-05 updated: the Criterion replaced whole — the test fails, not skips, when case-schema.md holds no block tagged case (case 652) · [[decision-case-652]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1616/ledger.md#L3
- 2026-10-07 deleted · [[decision-case-717.1]]
- 2026-10-07 archived · cleanup
