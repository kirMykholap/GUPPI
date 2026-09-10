---
type: decision
case: "29"
status: current
targets:
  - {kind: defer, category: rules, slug: rule-work-mode}
  - {kind: defer, category: rules, slug: rule-subagent-guppi}
origin: raw/2026-09-10/ledger.md#case-29
sprint: migration
created: 2026-09-10
tags: []
---

## Context

`sprint.md` называет Slice 3: materialize, generate, librarian, retro, handoff. Карта Slice 0 шире: ещё Work Mode и `subagent-guppi`.

## Now

Черновики `rule-documentation` и `rule-end-of-work` лежат в `docs/migration/`.
**＋** Агент, отрендеренный в сессии, виден только со следующей. Хуки проекта внутри субагента не работают.
**－** Phase 1 миграции не требует Work Mode.

## Problem

Граница слайса и порядок Cases.

## Then

Следующая сессия открывает Frontier.

`rule-work-mode` и `rule-subagent-guppi` стоят в `rules-index.md` как `draft` placeholder.
**＋** `sprint.md` называет Slice 3b после Slice 3.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-29
