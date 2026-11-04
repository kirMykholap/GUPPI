---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether, after an Edit, Write or MultiEdit of a file under .guppi/ in the repository of GUPPI, the hook guppi codewrite names to the agent each pointer outside its bracket and each bare case number of that file by the judgment of the live code test, and gives no line on a clean file, on a file outside .guppi/ or on a call of another tool
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k code_write_names
origin: raw/2026-11-04/0358/ledger.md#case-1028.1
sprint: plugin
created: 2026-11-04
tags: [ci, hooks, plugin]
---

## Criterion

When:
An Edit, Write or MultiEdit call writes a file under `.guppi/` in the repository of GUPPI, and the `PostToolUse` hook `uv run --project .guppi guppi codewrite` of `.guppi/guppi/codewrite.py` runs; or `.guppi/tests/test_ship.py` runs that hook over a payload of such a call in a temporary project.

Then:
The hook reads the file as written and runs over it `live_code` of `.guppi/guppi/ship.py`, the judgment that the live code test of `.guppi/tests/test_ship.py` runs too.
**＋** For each pointer outside a bracket of its own and each bare case number in a comment or a docstring of the file, it gives the agent a line with the file, the line and what it found, in `hookSpecificOutput.additionalContext` beside the result of the tool.
**＋** With those lines it gives one line on the fix: a bracket of its own at the end of the sentence, or the sample `case N`.
**＋** `live_code` leaves out each file of `LEFT_OUT` and `NOT_CLEANED` of `.guppi/guppi/ship.py` and each file outside `.guppi/`, and the live code test of `.guppi/tests/test_ship.py` takes its lines from it.
**－** A file with no such line, a file outside `.guppi/` and a call of another tool get no line.
**－** The hook refuses no call and exits 0; a payload or a file it cannot read gives one line on stderr.

## Result

2026-11-04, Retro of session 0358, uv run --project .guppi pytest .guppi/tests/test_ship.py -k code_write_names at 43401067: 6 passed

## History

- 2026-11-04 created · [[decision-case-1028.1]]
- 2026-11-04 status: pending → passed · raw/2026-11-04/0358/ledger.md#L31
