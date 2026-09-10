---
type: decision
case: "37"
status: current
targets:
  - {kind: create, category: rules, slug: rule-harness}
  - {kind: create, category: estimates, slug: estimate-harness-pipeline, ref: rule-harness}
  - {kind: update, category: rules, slug: rule-render-harness}
  - {kind: update, category: rules, slug: rule-hook-registry}
  - {kind: update, category: rules, slug: rule-lint}
  - {kind: update, category: rules, slug: rule-index}
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow, render, hooks]
---

## Context

Четыре правила не принадлежат фазе: renderer, реестр хуков, lint, индексы.

## Now

Три страницы несут `parent: rule-documentation`, lint даёт три `ref`-находки. `rule-hook-registry` — под `rule-session-start`, временно.
**＋** §6: дети Rule MOC упорядочены. Правило Method: make target.

## Problem

Где им жить.

## Then

Кто-то запускает `make test-harness`. Кто-то запускает `make lint`.

`make test-harness` прогоняет тесты renderer'а, lint и индексов одним pipeline. Зелёные.
**＋** `make lint` идёт в порядке детей: `render --check`, `index --check`, `guppi lint`. Первые два exit 0.
**＋** Четыре страницы несут `parent: rule-harness`. Три `ref`-находки ушли.
**－** `guppi lint` может быть красным на известном ложном.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
