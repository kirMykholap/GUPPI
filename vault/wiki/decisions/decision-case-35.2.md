---
type: decision
case: "35.2"
status: current
create: [rule-synthesis, estimate-synthesis-clusters]
update: [index, insights-schema]
origin: raw/2026-09-10/ledger.md#case-35.2
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Context

Между скриптами librarian сверяет новые страницы с индексами, собирает Insight, пишет brief. Каждая — partial render в файл агента.

## Problem

Границы каждого шага.

## Given

§8: Insight рождается на втором уроке с общей причиной. `actioned` не конечный.
**＋** Урок уходит в архив только когда его Insight стал `actioned`; Insight остаётся живым, его `pattern` в `insights-index.md`.
**－** §8 и `insights/schema.md` велят искать в архиве. Это дорого и ничего не добавляет.

## When

В `materialize.yaml` есть запись `lesson`.

## Note

The `then` of the Case, as ratified:

Librarian сравнивает `root_cause` со строками `lessons-index.md` и `insights-index.md`.
**＋** Второй живой урок, Insight нет: `create` в `insights` и `update` обоим урокам.
**＋** Insight с тем же `pattern`: `update` Insight (`children` плюс урок, `status: open` если был `actioned`) и `update` уроку.
**＋** Записи помечены `librarian: synthesis`. Генератор ставит Insight `origin: <date> · librarian`.
**＋** §8 и `insights/schema.md`: архив не читается.
**－** Он не читает архив, не пишет страницы сам. Один урок остаётся `new`. `Proposal` — предложение.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.2
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
