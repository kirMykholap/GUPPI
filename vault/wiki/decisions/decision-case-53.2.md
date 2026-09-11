---
type: decision
case: "53.2"
status: current
kind: [update, update, update, update, update, update, delete, delete, delete, delete]
target_slug: [index, case-schema, rule-page-generation, rule-ask, rule-pretask, estimate-generate-writes, estimate-generate-rejects-shape-alone, estimate-generate-logs-per-entry, estimate-generate-dates-history-by-run, estimate-generate-passes-delete-outside-vault]
origin: raw/2026-09-11/ledger.md#case-53.2
sprint: migration
created: 2026-09-11
tags: [harness, workflow, ledger, session]
---

## Context

53 Estimate-страниц на 33 правила: 17 парных к урокам с шаблонной фразой, четыре новых у `rule-page-generation` вместо правки одной, шесть с `criterion` полем без секции. Estimate — проверка контракта: критерий, метод, результат, статус; от неё считается `built`. Существует только у страницы с `when` + `then`.

## Problem

Снять пары у уроков; изменение контракта — `update` существующей Estimate; ask доходит до Estimate через цель; два дефекта хвоста; нужен ли `estimates-index.md`.

## When

Case меняет контракт Leaf; `guppi generate` применяет строку чтения; `ask-guppi` отвечает про проверку.

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#case-53.2
