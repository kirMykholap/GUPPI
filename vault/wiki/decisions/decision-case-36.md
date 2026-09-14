---
type: decision
case: "36"
status: current
create: ["[[rule-documentation]]", "[[estimate-documentation-completes]]"]
origin: raw/2026-09-10/ledger.md#case-36
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian, render]
---

## Context

Семь детей фазы ратифицированы. Нужен MOC, который держит порядок и рамку файла агента.

## Problem

Рамка агента и порядок шагов. Три ребёнка — скрипты без Render. Нет шага «коммит».

## Given

Renderer требует Render у каждого ребёнка full-страницы.
**＋** Правило Method: Estimate MOC называет make target.
**＋** Агент виден со следующей сессии. Хуки проекта внутри субагента не работают.
**－** Черновик кладёт index-check до generate, synthesis после — два прохода. Один проход лучше.

## When

Главный агент вызывает агента `librarian-guppi` после `/handoff`.

## Note

The `then` of the Case, as ratified:

Агент идёт по шагам: materialize, index-check, synthesis, generate, cleanup, brief, close.
**＋** Читает только `handoff.md`, `materialize.yaml`, пять индексов, `tags.md`.
**＋** Каждая его команда — строка в `event_log.md` через его хук.
**＋** После запуска у каждой decision-строки есть Decision-страница и страница цели. Нет страницы без решения.
**＋** Его коммит отдельный. `make test-documentation` зелёный.
**－** Не останавливается спросить. Ошибка materialize останавливает его с отчётом.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
