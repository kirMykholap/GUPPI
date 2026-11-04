---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether the clean version holds no .guppi/guppi/codewrite.py and no registration of guppi codewrite in .claude/settings.json or in the Render of rule-hook-registry, lists no command codewrite, passes guppi render --check, and whether the build exits 1 where a text still names guppi codewrite after the removal of the exact entry
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k no_code_write_hook
origin: raw/2026-11-04/0358/ledger.md#case-1028.2
sprint: plugin
created: 2026-11-04
tags: [ci, hooks, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` of `.guppi/guppi/ship.py` builds the clean version of the repository of GUPPI into an empty folder; or `.guppi/tests/test_ship.py` runs the build over a temporary project.

Then:
The clean version holds no `.guppi/guppi/codewrite.py`.
**＋** Its `.claude/settings.json` and the Render of `rule-hook-registry` hold no registration of `guppi codewrite`, and every other line stays as the working tree holds it.
**＋** `guppi render --check` over the clean version names no file that differs.
**＋** Run from the code of the clean version, `guppi` lists no command `codewrite`.
**＋** Where a text still names `guppi codewrite` after the removal of the exact entry, the build prints a line that names the file and exits 1.
**－** A text that never names `guppi codewrite` passes as it is.
**－** `guppi ship --check` does not judge `.guppi/guppi/codewrite.py`, which the clean version does not hold.

## Result

2026-11-04, Retro of session 0358, uv run --project .guppi pytest .guppi/tests/test_ship.py -k no_code_write_hook at 43401067: 4 passed

## History

- 2026-11-04 created · [[decision-case-1028.2]]
- 2026-11-04 status: pending → passed · raw/2026-11-04/0358/ledger.md#L32
