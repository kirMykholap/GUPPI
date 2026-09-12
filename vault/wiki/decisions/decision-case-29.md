---
type: decision
case: "29"
status: superseded
defer: [rule-work-mode, rule-subagent-guppi]
superseded_by: [decision-case-64]
origin: raw/2026-09-10/ledger.md#case-29
sprint: migration
created: 2026-09-10
tags: []
---

## Context

`sprint.md` называет Slice 3: materialize, generate, librarian, retro, handoff. Карта Slice 0 шире: ещё Work Mode и `subagent-guppi`.

## Problem

Граница слайса и порядок Cases.

## Given

Черновики `rule-documentation` и `rule-end-of-work` лежат в `docs/migration/`.
**＋** Агент, отрендеренный в сессии, виден только со следующей. Хуки проекта внутри субагента не работают.
**－** Phase 1 миграции не требует Work Mode.

## When

Следующая сессия открывает Frontier.

## Note

The `then` of the Case, as ratified:

`rule-work-mode` и `rule-subagent-guppi` стоят в `rules-index.md` как `draft` placeholder.
**＋** `sprint.md` называет Slice 3b после Slice 3.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-29
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
- 2026-09-12 superseded by decision-case-64 · [[decision-case-64]]
