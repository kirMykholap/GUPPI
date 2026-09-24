---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: An item of the plan carries one promise per Case, names a page that exists or is created, and no file
method: uv run pytest tests/test_prespec.py
checked: 2026-09-24
origin: raw/2026-09-24/1916/ledger.md#case-399.5
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

Then:
A Case whose `then` block holds two or more Estimate items — a `create`, or an `update` with `set: {status: pending}` — without a written `sections: Criterion` is the finding `case N: two promises in one Case — split it`.
**＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
**＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
**＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.

## Result

2026-09-24, `uv run pytest tests/test_prespec.py`: 108 passed

## History

- 2026-09-25 created · [[decision-case-399.5]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L41
