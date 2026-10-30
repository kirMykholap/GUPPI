---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether guppi test judges the code and the tests under .guppi/ for a pointer outside its bracket and a bare case number, with no read of the vault, so that a stray one goes red before the librarian's run
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k live_code, and uv run --project .guppi guppi test, read against the Criterion at Retro
origin: raw/2026-10-30/0304/ledger.md#case-919.2
sprint: plugin
created: 2026-10-30
tags: [plugin, tests]
---

## Criterion

When:
`uv run --project .guppi guppi test` runs the tests of `.guppi/tests/` in the repository of GUPPI.

Then:
A test of `.guppi/tests/test_ship.py` walks the code and the tests under `.guppi/` by `tree_files`, leaves out `LEFT_OUT` and `NOT_CLEANED`, and runs `judged` of `.guppi/guppi/ship.py` over each file, the same judgment as the step of the clean version, and passes when `judged` returns nothing for every file.
**＋** Where a comment or a docstring under `.guppi/` holds a pointer outside a bracket of its own or a bare case number, the test fails and shows the file and the line of each.
**＋** The test carries no mark `live` and reads no page of the vault, so `uv run --project .guppi guppi test` runs it.
**＋** A second test runs the same walk over a temporary folder whose test file has a docstring that opens with `Case 5:`, and finds that line.
**－** It judges no file of the harness, no file at the root of the project and no marker line of a page without `core: true`; those stay with the step `--check` of `.guppi/guppi/ship.py`.

## Result

2026-10-30, Retro of session 0304, uv run --project .guppi pytest .guppi/tests/test_ship.py -k live_code and guppi test, read against the Criterion of case 919.2: 2 passed; live_code_lines walks ship.tree_files(root, ".guppi"), skips ship.LEFT_OUT and ship.NOT_CLEANED and returns the lines of ship.judged with empty sets of known and loose slugs, so it reads no page and judges no harness file; neither test carries the mark live, and guppi test ran them among 1803 passed; the second test finds "ship: .guppi/tests/test_z.py:2: a reference to a case: Case 5" in a temporary root

## History

- 2026-10-30 created · [[decision-case-919.2]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/0304/ledger.md#L34
