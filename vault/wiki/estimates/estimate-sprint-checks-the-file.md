---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: sprint --check names sprint.md when it differs from the render of the live sprint page, or from the closed form when no live sprint page stands, exit 1, and writes nothing
method: uv run --project .guppi pytest .guppi/tests/test_sprint.py
checked: 2026-10-09
origin: raw/2026-09-17/1119/ledger.md#case-227
sprint: migration
created: 2026-09-17
tags: [harness, sprint]
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi sprint --check`, by hand or through the target `lint` of the `Makefile`, and it renders the file from the sprint page in memory.

Then:
When `vault/wiki/sprint.md` differs from the render of the page, stdout holds one line `sprint: <file> differs from entity-sprint-<id>`, the file named by its path from the project root, and the check exits 1. When the file equals the render, the check exits 0 with no output. The file is written in neither case.
**＋** The target `lint` of the `Makefile` runs it after `render --check` and before `guppi lint`.
**＋** With no live sprint page, the check compares the file with the closed form that `estimate-sprint-marks-a-closed-sprint` sets, and the line on stdout reads `sprint: <file> differs from the closed form of <id>`.
**－** A render error, such as two sprint pages, a slug with no page, or no sprint page and no file, is one line on stderr and exit 1, as with `guppi sprint`.

## Result

2026-10-09, uv run pytest tests/test_sprint.py; 29 passed, the closed file silent with exit 0 and a differing one named as the closed form of migration with exit 1

## History

- 2026-09-18 created · [[decision-case-227]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L14
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the bounds lines out (case 491.2) · [[decision-case-491.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L64
- 2026-10-09 updated: the Criterion replaced whole — with no live sprint page the check compares the closed form; the purpose covers both; the method a test of the session (case 743.9) · [[decision-case-743.9]]
- 2026-10-09 status: pending → passed · raw/2026-10-08/2352/ledger.md#L34
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
