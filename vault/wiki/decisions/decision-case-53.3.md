---
type: decision
case: "53.3"
status: current
kind: [update, update, update, update]
target_slug: [rule-materialize, rule-page-generation, estimate-materialize-assembles, estimate-generate-writes]
origin: raw/2026-09-11/ledger.md#case-53.3
sprint: migration
created: 2026-09-11
tags: [harness, workflow, ledger]
---

## Context

53 Estimate-страниц на 33 правила: 17 парных к урокам с шаблонной фразой, четыре новых у `rule-page-generation` вместо правки одной, шесть с `criterion` полем без секции. Estimate — проверка контракта: критерий, метод, результат, статус; от неё считается `built`. Существует только у страницы с `when` + `then`.

## Problem

Снять пары у уроков; изменение контракта — `update` существующей Estimate; ask доходит до Estimate через цель; два дефекта хвоста; нужен ли `estimates-index.md`.

## When

`guppi materialize` читает standalone `create` Estimate с `ref`; `guppi generate` применяет запись с `failed` прошлого прогона.

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#case-53.3
