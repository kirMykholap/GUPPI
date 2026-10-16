---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether guppi ship writes the tests but those of the command ship, cleans and judges only their comments and docstrings, keeps their other strings as samples, and whether the tests pass in the clean version
method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k tests; by hand, after a tag prod-x.y.z stands in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder of its own, then uv run --project .guppi pytest .guppi/tests in that folder, read against the Criterion"
checked: 2026-10-16
origin: raw/2026-10-15/0553/ledger.md#case-822.2
sprint: plugin
created: 2026-10-15
tags: [plugin, tests]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
**＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.
**＋** Then `uv run --project .guppi pytest .guppi/tests` runs in that folder.

Then:
It writes each file under `.guppi/tests/` but `.guppi/tests/test_ship.py`.
**＋** In a Python file under `.guppi/tests/`, it removes a bracket that holds a pointer only from the comments and the docstrings, and it judges only them for a pointer outside a bracket and for a bare case number.
**＋** Each other string of such a file is a sample: a case id there, such as `[case 10]` or `(case 320)` in the data of a test, is neither removed nor judged.
**＋** `--check` judges each file under `.guppi/tests/` in place, in the same way.
**＋** In the clean version, `uv run --project .guppi pytest .guppi/tests` passes, and a test that needs a file or a module that the clean version does not hold is skipped.
**－** The Python environment `.guppi/.venv/` stays out of the copy.
**－** In a Python file outside `.guppi/tests/`, it judges the whole text as before.

## Result

2026-10-16, /hi of session 0342, tag prod-0.2.0 in the history of HEAD: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k tests` 50 passed, 1 deselected; `uv run --project .guppi guppi ship --allow-draft` into the empty folder scratchpad/ship-0342, which held no `.guppi/.venv/` and no `.guppi/tests/test_ship.py`, then `uv run --project .guppi pytest .guppi/tests` there: 1656 passed, 15 skipped, 0 failed

## History

- 2026-10-15 created · [[decision-case-822.2]]
- 2026-10-16 updated: the method waits for a tag prod-x.y.z in the history of HEAD, which guppi ship needs; the Criterion stands · [[decision-case-844]]
- 2026-10-16 status: pending → failed · raw/2026-10-16/0104/ledger.md#L17
- 2026-10-16 status: failed → passed · raw/2026-10-16/0342/ledger.md#L14
