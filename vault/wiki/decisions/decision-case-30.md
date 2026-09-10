---
type: decision
case: "30"
status: superseded
targets:
  - {kind: update, category: file, slug: case-schema, path: vault/wiki/case-schema.md}
  - {kind: update, category: rules, slug: rule-case-protocol}
superseded_by: [decision-case-34]
origin: raw/2026-09-10/ledger.md#case-30
sprint: migration
created: 2026-09-10
tags: [session, workflow, ledger]
---

## Then

Ратифицирован, затем перекрыт Case 34: блок `then` живёт в Spec, не в чате. Форма блока —
как в шапке этого документа. Записи ниже дают только строку History; содержание несёт Case 34.

```then
update:
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "then carries a YAML block tagged then, read by guppi materialize (superseded by case 34 on where the block lives)"
  - slug: rule-case-protocol
    change: "the Render names the then block (superseded by case 34)"
```

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-30
- 2026-09-10 superseded by decision-case-34 · raw/2026-09-10/ledger.md#case-34
