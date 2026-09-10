---
type: decision
case: "27"
status: current
targets:
  - {kind: update, category: rules, slug: rule-index}
  - {kind: update, category: file, slug: index, path: vault/wiki/index.md}
  - {kind: update, category: rules, slug: rule-ask}
supersedes: [decision-case-22]
origin: raw/2026-09-09/ledger.md#case-27
sprint: migration
created: 2026-09-09
tags: [harness, workflow, session]
---

## Then

Учтено выше: файлы `wiki/<category>-index.md`; `index.md` §1, §10, §11; `rule-ask`
читает `rules-index.md`. Индекса decisions нет.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-27
