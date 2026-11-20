---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether guppi ship writes the tests but those of the command ship, cleans and judges only their comments and docstrings, and keeps their other strings as samples
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k tests
checked: 2026-11-20
origin: raw/2026-10-15/0553/ledger.md#case-822.2
sprint: plugin
created: 2026-10-15
tags: [plugin, tests]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
**＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.

Then:
It writes each file under `.guppi/tests/` but `.guppi/tests/test_ship.py`.
**＋** In a Python file under `.guppi/tests/`, it removes a bracket that holds a pointer only from the comments and the docstrings, and it judges only them for a pointer outside a bracket and for a bare case number.
**＋** Each other string of such a file is a sample: a case id there, such as `[case 10]` or `(case 320)` in the data of a test, is neither removed nor judged.
**＋** `--check` judges each file under `.guppi/tests/` in place, in the same way.
**－** The Python environment `.guppi/.venv/` stays out of the copy.
**－** In a Python file outside `.guppi/tests/`, it judges the whole text as before.

## Result

2026-11-20, uv run --project .guppi pytest .guppi/tests/test_ship.py -k tests; 79 passed, 2 deselected

## History

- 2026-10-15 created · [[decision-case-822.2]]
- 2026-10-16 updated: the method waits for a tag prod-x.y.z in the history of HEAD, which guppi ship needs; the Criterion stands · [[decision-case-844]]
- 2026-10-16 status: pending → failed · raw/2026-10-16/0104/ledger.md#L17
- 2026-10-16 status: failed → passed · raw/2026-10-16/0342/ledger.md#L14
- 2026-11-20 updated: the promise that the tests pass in the clean version moves to estimate-clean-branch-copy-passes-its-style-and-tests · [[decision-case-1030.2]]
- 2026-11-20 status: pending → passed · raw/2026-11-04/0807/ledger.md#L47
