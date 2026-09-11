---
type: decision
case: "53.1"
status: current
kind: [update, update, update, update, update, update, update, update, delete, delete, delete, delete, delete, delete, delete, delete, delete, delete, delete, delete, delete, delete, delete, delete, delete]
target_slug: [estimates-schema-yaml, estimates-schema, lessons-schema-yaml, lessons-schema, index, glossary, rule-page-generation, rule-lint, estimate-agents-at-import-not-expanded, estimate-agents-loaded-at-session-start, estimate-agents-visible-in-session, estimate-estimates-criterion-stale-after-contract-change, estimate-generate-log-written-last, estimate-generate-replace-mapping-crashes, estimate-generate-walk-history-dated-by-yaml, estimate-hooks-exitplanmode-payload, estimate-hooks-messagedisplay-cannot-block, estimate-hooks-sessionstart-cannot-block, estimate-hooks-stop-payload, estimate-hooks-windows-stdin-encoding, estimate-ledger-hook-misses-a-reply-ending-in-a-tool-call, estimate-librarian-reads-beyond-the-four-inputs, estimate-materialize-assumes-every-entry-has-a-line, estimate-readings-after-librarian-invisible-to-next-hi, estimate-tests-cli-date-pinned]
origin: raw/2026-09-11/ledger.md#case-53.1
sprint: migration
created: 2026-09-11
tags: [harness, workflow, ledger, hooks, librarian]
---

## Context

53 Estimate-страниц на 33 правила: 17 парных к урокам с шаблонной фразой, четыре новых у `rule-page-generation` вместо правки одной, шесть с `criterion` полем без секции. Estimate — проверка контракта: критерий, метод, результат, статус; от неё считается `built`. Существует только у страницы с `when` + `then`.

## Problem

Снять пары у уроков; изменение контракта — `update` существующей Estimate; ask доходит до Estimate через цель; два дефекта хвоста; нужен ли `estimates-index.md`.

## When

`guppi generate` применяет `lesson`; lint проверяет урок и Estimate; библиотекарь пишет Insight.

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#case-53.1
