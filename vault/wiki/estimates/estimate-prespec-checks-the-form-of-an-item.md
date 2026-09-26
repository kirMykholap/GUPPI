---
type: estimate
kind: QA
status: pending
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
**＋** A key of an item of any kind that `item_keys` of `guppi/materialize.py` does not give its kind and category — `slug` a key of every kind — is the finding `case N: <kind> <slug>: key <key> is not a key of this item`.
**－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session creates or updates, is not judged by its keys (case 308.2).

## Result

2026-09-24, `uv run pytest tests/test_prespec.py`: 108 passed

## History

- 2026-09-25 created · [[decision-case-399.5]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L41
- 2026-09-26 updated: the Criterion replaced whole — a key of an item outside the keys item_keys gives it is a finding (case 436.2) · [[decision-case-436.2]]
