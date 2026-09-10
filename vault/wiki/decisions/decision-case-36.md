---
type: decision
case: "36"
status: current
targets:
  - {kind: create, category: rules, slug: rule-documentation}
  - {kind: create, category: estimates, slug: estimate-documentation-completes, ref: rule-documentation}
origin: raw/2026-09-10/ledger.md#case-36
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian, render]
---

## Context

Семь детей фазы ратифицированы. Нужен MOC, который держит порядок и рамку файла агента.

## Now

Renderer требует Render у каждого ребёнка full-страницы.
**＋** Правило Method: Estimate MOC называет make target.
**＋** Агент виден со следующей сессии. Хуки проекта внутри субагента не работают.
**－** Черновик кладёт index-check до generate, synthesis после — два прохода. Один проход лучше.

## Problem

Рамка агента и порядок шагов. Три ребёнка — скрипты без Render. Нет шага «коммит».

## Then

Главный агент вызывает агента `librarian-guppi` после `/handoff`.

Агент идёт по шагам: materialize, index-check, synthesis, generate, cleanup, brief, close.
**＋** Читает только `handoff.md`, `materialize.yaml`, пять индексов, `tags.md`.
**＋** Каждая его команда — строка в `event_log.md` через его хук.
**＋** После запуска у каждой decision-строки есть Decision-страница и страница цели. Нет страницы без решения.
**＋** Его коммит отдельный. `make test-documentation` зелёный.
**－** Не останавливается спросить. Ошибка materialize останавливает его с отчётом.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36
