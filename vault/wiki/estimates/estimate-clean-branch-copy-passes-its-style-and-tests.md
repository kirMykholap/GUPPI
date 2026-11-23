---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether guppi ship leaves no empty comment and no line of spaces where it removed a bracket, formats the Python files of the clean version, and whether the style commands and the tests of the project pass over it
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k own_style; uv run --project .guppi pytest .guppi/tests/test_ship.py -m live -k own_tests
checked: 2026-11-23
origin: raw/2026-11-04/0807/ledger.md#case-1030.1
sprint: plugin
created: 2026-11-04
tags: [plugin, ci, tests]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` of `.guppi/guppi/ship.py`, as `rule-clean-branch` sets it, builds the clean version from the working tree into an empty folder.
**＋** Then `.guppi/tests/test_ship.py` runs over that folder the commands of the keys `style` and `test` of `guppi.toml`.

Then:
In a Python file it writes, it removes each comment that the removal of a bracket left empty, with the spaces before it, and the whole line where that comment stood alone.
**＋** In each text file it writes, a bracket that holds a pointer and stands alone on its line goes with that line.
**＋** As its last step it runs `ruff format` over `.guppi/` of the folder.
**＋** The commands of the key `style` exit 0 over the folder, in a test that `uv run --project .guppi guppi test` runs.
**＋** The commands of the key `test` exit 0 over the folder, in a test marked `live`, and a test that needs a file or a module that the clean version does not hold is skipped.
**－** Where `ruff format` does not start or does not exit 0, it prints one `ship:` line and exits 1.
**－** That run keeps its cache in a temporary folder outside the folder, so the clean version holds no `.ruff_cache/`.
**－** `--check` runs no `ruff format`.

## Result

2026-11-23, Retro of session 1353, on the Criterion of Case 1042.2: uv run --project .guppi pytest .guppi/tests/test_ship.py -k own_style 4 passed; uv run --project .guppi pytest .guppi/tests/test_ship.py -m live -k own_tests 1 passed (66.8 s), on Windows

## History

- 2026-11-20 created · [[decision-case-1030.1]]
- 2026-11-20 status: pending → passed · raw/2026-11-04/0807/ledger.md#L46
- 2026-11-23 updated: the Criterion replaced whole — the line that prod.yml runs neither command is gone, since the workflow now runs both · [[decision-case-1042.2]]
- 2026-11-23 status: pending → passed · raw/2026-11-20/1353/ledger.md#L21
