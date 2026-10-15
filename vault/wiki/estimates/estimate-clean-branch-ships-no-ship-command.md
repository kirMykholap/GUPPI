---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether the clean version holds the module of the judgment of a pointer and no module of the command ship, so that guppi there lists no command ship, while guppi ship of this repository judges by that module
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k ship_command
checked: 2026-10-15
origin: raw/2026-10-15/0553/ledger.md#case-820.5
sprint: plugin
created: 2026-10-15
tags: [plugin, ci]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` builds the clean version of this repository into an empty folder, as `rule-clean-branch` sets it.
**＋** Then `guppi` runs from the code of that folder, with no argument and with the argument `ship`.

Then:
The clean version holds `.guppi/guppi/pointers.py` and no `.guppi/guppi/ship.py`.
**＋** Run from the code of the clean version, `guppi` lists no command `ship`, and `guppi ship` prints that the command is unknown and exits 2.
**＋** `guppi ship` removes and refuses a pointer by the functions of `.guppi/guppi/pointers.py`, and holds no copy of them.
**－** `guppi ship --check` does not judge `.guppi/guppi/ship.py`, which the clean version does not hold.
**－** In this repository, `guppi` lists the command `ship`, and `guppi ship` runs as `rule-clean-branch` sets it.

## Result

2026-10-15, uv run --project .guppi pytest .guppi/tests/test_ship.py -k ship_command: 4 passed, exit 0

## History

- 2026-10-15 created · [[decision-case-820.5]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L2
