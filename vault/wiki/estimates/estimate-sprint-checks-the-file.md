---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: sprint --check names sprint.md when it differs from the render of the sprint page, exit 1, and writes nothing
method: pytest tests/test_sprint.py, plus make lint after the librarian's run — no sprint line
checked: 2026-09-29
origin: raw/2026-09-17/1119/ledger.md#case-227
sprint: migration
created: 2026-09-17
tags: [harness, sprint]
---

## Criterion

When:
Someone runs `uv run guppi sprint --check`, by hand or through the target `lint` of the `Makefile`, and it renders the file from the sprint page in memory.

Then:
When `vault/wiki/sprint.md` differs from the render of the page, stdout holds one line `sprint: <file> differs from entity-sprint-<id>`, the file named by its path from the project root, and the check exits 1. When the file equals the render, the check exits 0 with no output. The file is written in neither case.
**＋** The target `lint` of the `Makefile` runs it after `render --check` and before `guppi lint`.
**－** A render error, such as no sprint page, two sprint pages or a slug with no page, is one line on stderr and exit 1, as with `guppi sprint`.

## Result

2026-09-29, uv run pytest tests/test_sprint.py: 20 passed; uv run guppi sprint --check exit 0, no output

## History

- 2026-09-18 created · [[decision-case-227]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L14
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the bounds lines out (case 491.2) · [[decision-case-491.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L64
