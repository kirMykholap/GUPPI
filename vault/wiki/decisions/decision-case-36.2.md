---
type: decision
case: "36.2"
status: current
update: ["[[rule-render-harness]]", "[[estimate-render-harness-reproduces]]"]
origin: raw/2026-09-10/ledger.md#case-36.2
sprint: migration
created: 2026-09-10
tags: [harness, render]
---

## Context

Семь детей фазы ратифицированы. Нужен MOC, который держит порядок и рамку файла агента.

## Problem

Рамка агента и порядок шагов. Три ребёнка — скрипты без Render. Нет шага «коммит».

## Given

`render_full` требует маркер для каждого ребёнка и ошибается на ребёнке без Render.
**－** У `rule-documentation` три ребёнка — скрипты.

## When

`guppi render` рендерит full-страницу с ребёнком без `enforcement: render`.

## Note

The `then` of the Case, as ratified:

Такой ребёнок ничего не вносит. Маркер не нужен.
**＋** Критерий `estimate-render-harness-reproduces` дополнен. Тест добавлен.
**－** Маркер для такого ребёнка — ошибка, ничего не записано.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.2
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
