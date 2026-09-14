---
type: decision
case: "53.4"
status: current
update: [index, "[[rule-index]]", "[[rule-index-check]]", "[[rule-lint]]", "[[estimate-index-lists]]"]
origin: raw/2026-09-11/ledger.md#case-53.4
sprint: migration
created: 2026-09-11
tags: [harness, workflow, librarian]
---

## Context

53 Estimate-страниц на 33 правила: 17 парных к урокам с шаблонной фразой, четыре новых у `rule-page-generation` вместо правки одной, шесть с `criterion` полем без секции. Estimate — проверка контракта: критерий, метод, результат, статус; от неё считается `built`. Существует только у страницы с `when` + `then`.

## Problem

Снять пары у уроков; изменение контракта — `update` существующей Estimate; ask доходит до Estimate через цель; два дефекта хвоста; нужен ли `estimates-index.md`.

## Given

`lessons/schema.md` строка 18: `estimates` required, `error` born `passed`, `knowledge` Research «before an Insight». §8 то же; глоссарий повторяет. `insight-harness-agent-visibility` стоит на уроке с Research `pending`.
**＋** `generate.estimate()` 439: same status with a Result → skipped. `lesson_estimate()` 343 пишет пару по шаблону.
**＋** `materialize` 326–330: sections only for the nested estimate; `apply()` never clears `failed`.
**＋** §3 «Estimates count too»; `ask-guppi` читает `estimates-index.md`; index check сравнивает estimate creates; `estimate-index-lists` требует строку estimate.
**＋** На 17 парных Estimate ссылаются только их уроки. `estimate-librarian-reads-beyond-the-four-inputs` прошла живым чтением 13:10:37; чтение остаётся в ledger.
**－** Estimate как секция на Leaf — не здесь. `rule-index-check` сравнение остальных категорий не меняется.

## When

`guppi index` пишет индексы; библиотекарь делает index check; `make lint` идёт.

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#case-53.4
- 2026-09-12 Given inherited from the parent Case · [[decision-case-60]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
