---
type: lesson
kind: error
root_cause: the cleaning of ship removes a bracket that holds a pointer and leaves the `#` of a comment that held only that bracket and the space before a bracket at the end of a line, and no test runs the style commands or the tests over the copy
status: new
origin: raw/2026-11-04/0358/ledger.md#L34
sprint: plugin
created: 2026-11-04
tags: [plugin, ci]
---

## Trigger

2026-11-04, the three trial installs of session 0358 from the copy of guppi ship --allow-draft at 28c69232: `ruff check .` found 51 PLR2044 "Line with empty comment", such as `.guppi/guppi/casecheck.py:1019` (`... (store or {}).get(case))  #`), ruff format would reformat 5 files, and `pytest .guppi/tests` failed test_lint.py::test_cli_dispatches_to_lint and test_sprint.py::test_hi_setup_pending_prints_the_setup_line_before_the_sprint_line, the second on a space left at the end of a line

## Root cause

the cleaning of ship removes a bracket that holds a pointer and leaves the `#` of a comment that held only that bracket and the space before a bracket at the end of a line, and no test runs the style commands or the tests over the copy

## History

- 2026-11-04 created · raw/2026-11-04/0358/ledger.md#L34
