---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: An update of an Estimate changes the part it names alone, or replaces the Criterion whole
method: uv run pytest tests/test_materialize.py
checked: 2026-09-24
origin: raw/2026-09-24/1916/ledger.md#case-397.3
sprint: migration
created: 2026-09-24
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run guppi materialize` lifts the `update` item of an Estimate.

Then:
An item that names no part of the page — `change` alone — or carries `set.status` gets `sections.Criterion`, the text written under `sections: Criterion` or else the Criterion lifted from its Case, and `set: {status: pending}` unless the item set a status itself.
**＋** An item that names a part — `set` without `status`, a `replace` pair, a section other than `Criterion` — and writes no Criterion carries that part alone: nothing is lifted and no status is set.
**＋** A written `sections.Criterion` beside any other part stands and sets `pending`.

## Result

2026-09-24, `uv run pytest tests/test_materialize.py`: 75 passed

## History

- 2026-09-25 created · [[decision-case-397.3]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L29
