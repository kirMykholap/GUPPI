---
type: decision
case: "36.1"
status: current
targets:
  - {kind: create, category: rules, slug: rule-close, ref: rule-documentation}
  - {kind: create, category: estimates, slug: estimate-close-commits, ref: rule-close}
origin: raw/2026-09-10/ledger.md#case-36.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, git, librarian]
---

## Context

Семь детей фазы ратифицированы. Нужен MOC, который держит порядок и рамку файла агента.

## Now

Коммит librarian'а должен быть отдельным от коммита Retro.
**＋** Главный агент видит из запуска только отчёт.

## Problem

Рамка агента и порядок шагов. Три ребёнка — скрипты без Render. Нет шага «коммит».

## Then

Librarian закончил brief.

Он запускает `make lint` и держит вывод.
**＋** Один коммит только путей `vault/`: `docs(vault): librarian, <date>`.
**＋** Отчёт до двадцати строк.
**－** Без `--amend`. Ничего вне `vault/`.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.1
