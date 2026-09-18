---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: sprint --check names sprint.md when it differs from the render of the sprint page, exit 1, and writes nothing
method: pytest tests/test_sprint.py, plus make lint after the librarian's run — no sprint line
checked: 2026-09-18
origin: raw/2026-09-17/1119/ledger.md#case-227
sprint: migration
created: 2026-09-17
tags: [harness, sprint]
---

## Criterion

Given:
`guppi sprint` renders the file from the sprint page; `render --check` is the model: compare in memory, name the file, exit 1, write nothing.
**＋** `tests/test_sprint.py` fixes the behaviour on a temp vault.
**－** `make lint` writes nothing to the tree (case 147.7).

When:
Someone runs `uv run guppi sprint --check`, by hand or through `make lint`.

Then:
When `vault/wiki/sprint.md` differs from the render of the page, one line on stdout — `sprint: vault/wiki/sprint.md differs from entity-sprint-<id>` — and exit 1; when it is the same, silence and exit 0; the file is written in neither case.
**＋** `make lint` calls it after `render --check`, before `guppi lint`.
**－** A render error — no page, two, a slug without a page — as with `guppi sprint`: stderr and exit 1.
**－** Nothing is added at `SessionStart` or in `/hi`.

## Result

2026-09-18, uv run pytest tests/test_sprint.py and make lint in session 1252: the sprint tests green; make lint printed no sprint: line and no render: line before the guppi lint findings — sprint.md is the render of entity-sprint-migration after the run of 1119, the file not written

## History

- 2026-09-18 created · [[decision-case-227]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L14
