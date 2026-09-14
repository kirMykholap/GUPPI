---
type: decision
case: "35.3"
status: current
create: ["[[rule-brief]]", "[[estimate-brief-written]]"]
origin: raw/2026-09-10/ledger.md#case-35.3
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Context

Между скриптами librarian сверяет новые страницы с индексами, собирает Insight, пишет brief. Каждая — partial render в файл агента.

## Problem

Границы каждого шага.

## Given

`brief.md` и `sprint.md` — рабочие файлы без схемы; их пишет librarian.
**＋** Отложенное — не больше 7, ранг по severity, потом по числу переносов. Флаги без лимита.
**＋** Librarian знает о сессии из `handoff.md` и yaml.
**－** Никто не считает переносы.

## When

`guppi generate` и `guppi cleanup` отработали. Librarian запустил `make lint`.

## Note

The `then` of the Case, as ratified:

`brief.md` переписан целиком: где стоим; что делать первым; отложенное до 7; флаги без лимита; чтения на закрытие.
**＋** Пункт отложенного несёт число переносов: прошлое плюс один.
**＋** `sprint.md` меняется только по указанию из `handoff.md`.
**－** Ни решений, ни оценок. Только факты и флаги из yaml, handoff и lint.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.3
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
