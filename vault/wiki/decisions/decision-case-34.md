---
type: decision
case: "34"
status: current
kind: [update, update, update, update]
target_slug: [case-schema, rule-case-protocol, index, glossary]
supersedes: [decision-case-30]
origin: raw/2026-09-10/ledger.md#case-34
sprint: migration
created: 2026-09-10
tags: [session, workflow, ledger]
---

## Context

Case стал тяжёлым. Новый формат должен лечь в `case-schema.md`, Render `rule-case-protocol` и грамматику ledger.

## Problem

Формат живёт только в чате.

## Given

`case-schema.md`: шесть секций, `then` несёт страницу целиком.
**＋** `index.md` §4: грамматика без тегов.
**－** Про операнды и простой язык не говорит ни один файл.

## When

Агент пишет Case. Хук `Stop` читает ответ. `guppi materialize` читает Spec.

## Note

The `then` of the Case, as ratified:

Case состоит из семи цитат. Имя блока с двоеточием.
**＋** Строки given, when, then после первой начинаются с **＋** или **－**.
**＋** Превью ledger-строк — в `ratification`, fence без тега.
**＋** Строка `create` несёт `{tags:a,b}`. Категория из префикса slug.
**＋** В Spec под каждым Case стоит блок `then`.
**－** В чате блока нет. Правило LEDGER не меняется.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-34
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
