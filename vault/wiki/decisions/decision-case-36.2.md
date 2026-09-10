---
type: decision
case: "36.2"
status: current
targets:
  - {kind: update, category: rules, slug: rule-render-harness}
  - {kind: update, category: estimates, slug: estimate-render-harness-reproduces}
origin: raw/2026-09-10/ledger.md#case-36.2
sprint: migration
created: 2026-09-10
tags: [harness, render]
---

## Context

Семь детей фазы ратифицированы. Нужен MOC, который держит порядок и рамку файла агента.

## Now

`render_full` требует маркер для каждого ребёнка и ошибается на ребёнке без Render.
**－** У `rule-documentation` три ребёнка — скрипты.

## Problem

Рамка агента и порядок шагов. Три ребёнка — скрипты без Render. Нет шага «коммит».

## Then

`guppi render` рендерит full-страницу с ребёнком без `enforcement: render`.

Такой ребёнок ничего не вносит. Маркер не нужен.
**＋** Критерий `estimate-render-harness-reproduces` дополнен. Тест добавлен.
**－** Маркер для такого ребёнка — ошибка, ничего не записано.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.2
