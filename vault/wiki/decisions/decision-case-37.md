---
type: decision
case: "37"
status: current
create: ["[[rule-harness]]", "[[estimate-harness-pipeline]]"]
update: ["[[rule-render-harness]]", "[[rule-hook-registry]]", "[[rule-lint]]", "[[rule-index]]"]
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow, render, hooks]
---

## Context

Четыре правила не принадлежат фазе: renderer, реестр хуков, lint, индексы.

## Problem

Где им жить.

## Given

Три страницы несут `parent: rule-documentation`, lint даёт три `ref`-находки. `rule-hook-registry` — под `rule-session-start`, временно.
**＋** §6: дети Rule MOC упорядочены. Правило Method: make target.

## When

Кто-то запускает `make test-harness`. Кто-то запускает `make lint`.

## Note

The `then` of the Case, as ratified:

`make test-harness` прогоняет тесты renderer'а, lint и индексов одним pipeline. Зелёные.
**＋** `make lint` идёт в порядке детей: `render --check`, `index --check`, `guppi lint`. Первые два exit 0.
**＋** Четыре страницы несут `parent: rule-harness`. Три `ref`-находки ушли.
**－** `guppi lint` может быть красным на известном ложном.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
