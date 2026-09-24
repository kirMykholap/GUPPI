---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A key of a create or a defer that the category's schema.yaml does not name never reaches the page
method: uv run pytest tests/test_materialize.py
checked: 2026-09-24
origin: raw/2026-09-24/1916/ledger.md#case-397.2
sprint: migration
created: 2026-09-24
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run guppi materialize` lifts a `create` or `defer` item whose category has its `vault/wiki/<category>/schema.yaml` on disk, in a unit that neither creates nor updates `rule-<category>-schema`.

Then:
Only the keys the category's `schema.yaml` names as fields reach `fields` of the entry; `ref` goes to the entry, `sections` to its own key.
**＋** A key that is no field of the schema and none of the item's own keys — `slug`, `ref`, `sections`, `file`, `estimate`, `parent_create`, `parent_tags`, and on the `create` of a rule or an entity `method`, `contract`, `estimate_slug`, `estimate_kind` — is named under `unknown` on the entry, printed by `--show`, never written to the page, and the entry applies.
**＋** The `type` and `purpose` of a `defer` are its own keys and reach `fields` whatever the category of its target; a `defer` without `purpose` is `incomplete: [purpose]`.

## Result

2026-09-24, `uv run pytest tests/test_materialize.py`: 75 passed

## History

- 2026-09-25 created · [[decision-case-397.2]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L28
