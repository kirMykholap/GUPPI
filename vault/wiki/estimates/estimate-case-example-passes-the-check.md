---
type: estimate
kind: QA
status: passed
target: "[[rule-case-example]]"
purpose: Whether the example Case of case-example.md, in the chat form case-guppi writes, passes the check the SubagentStop hook runs over the file of a Case, so the form it shows stays a form the scripts accept
method: uv run pytest tests/test_case_schema.py, passed and not skipped; at the Retro of the session that creates it, the new Renders of rule-case-example and rule-case-protocol in the Spec read against the Criterion
origin: raw/2026-10-07/1804/ledger.md#case-717.1
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness]
---

## Criterion

When:
`tests/test_case_schema.py` runs under `uv run pytest`. It reads the block tagged `case` in `vault/wiki/case-example.md`, rendered from `rule-case-example`, and runs over it the function of `guppi/casecheck.py` that the `SubagentStop` hook of `rule-case-check` runs over the Cases of a file, in a temporary project that holds the schema files of the vault and the pages the example updates.

Then:
`vault/wiki/case-example.md` holds one block tagged `case`, one Case with sub-cases in the chat form that `case-guppi` writes into its file, and after it one block tagged `then`.
**＋** The example holds a `create` and an `update` with their sub-points, a `replace` pair whose values hold a backtick in spans padded by one space, a `set` in a fenced block, an `update` of an Estimate whose Criterion it replaces, a read line for each Estimate it creates or replaces, and its ledger lines in a quoted fence under `ratification`.
**＋** The example's `context` says what the sentence around the match of its `replace` pair names.
**＋** The paragraph before the block says that the example passes the check of the `SubagentStop` hook of `rule-case-check`, and that the check, not the paragraph, is the source of the limits; it lists no limit.
**＋** `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, holds no example block and names `vault/wiki/case-example.md` where it sets the chat form and the `then` block.
**＋** The check gives the example no finding and no note, and the test passes; a change of the check that gives the example a finding or a note fails the test, which prints it.
**＋** The test reads the example from the file and the checks from `guppi/casecheck.py`, and holds no copy of either.
**－** While `vault/wiki/case-example.md` does not stand, the test reads the block tagged `case` of `vault/wiki/case-schema.md`; a Case of a later session removes that path.
**－** While the file the test reads holds no block tagged `case`, both tests of `tests/test_case_schema.py` fail with a message that names the file; no test of the file is skipped.

## Result

2026-10-07, uv run pytest tests/test_case_schema.py: 2 passed, none skipped, reading case-schema.md since case-example.md is rendered only at the librarian's run; Retro, by hand: the new Renders of rule-case-example and rule-case-protocol in the Spec read against the Criterion — case-example.md holds one block tagged case, a Case with sub-cases holding a create, an update, a replace pair in padded spans, a fenced set, a replaced Criterion, read lines and a quoted ratification, then one block tagged then; its paragraph names the check and lists no limit; case-schema.md keeps no example block and names case-example.md for the chat form and the then block

## History

- 2026-10-07 created · [[decision-case-717.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/1804/ledger.md#L24
