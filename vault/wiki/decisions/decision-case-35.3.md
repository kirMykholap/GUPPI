---
type: decision
case: "35.3"
status: current
targets:
  - {kind: create, category: rules, slug: rule-brief, ref: rule-documentation}
  - {kind: create, category: estimates, slug: estimate-brief-written, ref: rule-brief}
origin: raw/2026-09-10/ledger.md#case-35.3
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Context

Между скриптами librarian сверяет новые страницы с индексами, собирает Insight, пишет brief. Каждая — partial render в файл агента.

## Now

`brief.md` и `sprint.md` — рабочие файлы без схемы; их пишет librarian.
**＋** Отложенное — не больше 7, ранг по severity, потом по числу переносов. Флаги без лимита.
**＋** Librarian знает о сессии из `handoff.md` и yaml.
**－** Никто не считает переносы.

## Problem

Границы каждого шага.

## Then

`guppi generate` и `guppi cleanup` отработали. Librarian запустил `make lint`.

`brief.md` переписан целиком: где стоим; что делать первым; отложенное до 7; флаги без лимита; чтения на закрытие.
**＋** Пункт отложенного несёт число переносов: прошлое плюс один.
**＋** `sprint.md` меняется только по указанию из `handoff.md`.
**－** Ни решений, ни оценок. Только факты и флаги из yaml, handoff и lint.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.3
