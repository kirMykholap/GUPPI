---
type: estimate
kind: QA
status: pending
target: "[[rule-backlog]]"
purpose: guppi backlog --check names backlog.md when it differs from the render of its sources, exit 1, and writes nothing
method: uv run pytest tests/test_backlog.py, plus make lint after the librarian's run — no backlog line
origin: raw/2026-09-27/1255/ledger.md#case-451.5
sprint: migration
created: 2026-09-27
tags: [harness, sprint]
---

## Criterion

When:
Someone runs `uv run guppi backlog --check`, by hand or through `make lint`.

Then:
When `vault/wiki/backlog.md` differs from the render of its sources, the check prints one line on stdout that names the file and exits 1. When it is the same, the check is silent and exits 0. The file is written in neither case.
**＋** `make lint` runs it after `sprint --check` and before `glossary --check`.
**－** `make lint` writes nothing to the tree.

## History

- 2026-09-27 created · [[decision-case-451.5]]
