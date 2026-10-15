---
type: estimate
kind: QA
status: passed
target: "[[rule-backlog]]"
purpose: guppi backlog --check names backlog.md when it differs from the render of its sources, exit 1, and writes nothing
method: uv run --project .guppi pytest .guppi/tests/test_backlog.py, plus uv run --project .guppi guppi check after the librarian's run — no backlog line
checked: 2026-09-27
origin: raw/2026-09-27/1255/ledger.md#case-451.5
sprint: migration
created: 2026-09-27
tags: [harness, sprint]
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi backlog --check`, by hand or through `uv run --project .guppi guppi check`.

Then:
When `vault/wiki/backlog.md` differs from the render of its sources, the check prints one line on stdout that names the file and exits 1. When it is the same, the check is silent and exits 0. The file is written in neither case.
**＋** `uv run --project .guppi guppi check` runs it after `sprint --check` and before `glossary --check`.
**－** `uv run --project .guppi guppi check` writes nothing to the tree.

## Result

2026-09-27, uv run pytest tests/test_backlog.py on the working tree of session 1819 (uncommitted guppi/ changes, vault/wiki unchanged): 16 passed; uv run guppi backlog --check: no output, exit 0; make lint after the librarian run of e229e99: no backlog finding, its only backlog lines are unread lines of Estimates

## History

- 2026-09-27 created · [[decision-case-451.5]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L23
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
