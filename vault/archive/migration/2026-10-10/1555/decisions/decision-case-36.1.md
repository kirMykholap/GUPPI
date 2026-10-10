---
type: decision
case: "36.1"
status: archived
create: ["[[rule-close]]", "[[estimate-close-commits]]"]
origin: raw/2026-09-10/ledger.md#case-36.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, git, librarian]
---

## Context

Семь детей фазы ратифицированы. Нужен MOC, который держит порядок и рамку файла агента.

## Problem

Рамка агента и порядок шагов. Три ребёнка — скрипты без Render. Нет шага «коммит».

## Given

Коммит librarian'а должен быть отдельным от коммита Retro.
**＋** Главный агент видит из запуска только отчёт.

## When

Librarian закончил brief.

## Note

The `then` of the Case, as ratified:

Он запускает `make lint` и держит вывод.
**＋** Один коммит только путей `vault/`: `docs(vault): librarian, <date>`.
**＋** Отчёт до двадцати строк.
**－** Без `--amend`. Ничего вне `vault/`.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.1
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
