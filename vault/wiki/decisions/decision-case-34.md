---
type: decision
case: "34"
status: current
targets:
  - {kind: update, category: file, slug: case-schema, path: vault/wiki/case-schema.md}
  - {kind: update, category: rules, slug: rule-case-protocol}
  - {kind: update, category: file, slug: index, path: vault/wiki/index.md}
  - {kind: update, category: file, slug: glossary, path: vault/wiki/glossary.md}
supersedes: [decision-case-30]
origin: raw/2026-09-10/ledger.md#case-34
sprint: migration
created: 2026-09-10
tags: [session, workflow, ledger]
---

## Context

Case стал тяжёлым. Новый формат должен лечь в `case-schema.md`, Render `rule-case-protocol` и грамматику ledger.

## Now

`case-schema.md`: шесть секций, `then` несёт страницу целиком.
**＋** `index.md` §4: грамматика без тегов.
**－** Про операнды и простой язык не говорит ни один файл.

## Problem

Формат живёт только в чате.

## Then

Агент пишет Case. Хук `Stop` читает ответ. `guppi materialize` читает Spec.

Case состоит из семи цитат. Имя блока с двоеточием.
**＋** Строки given, when, then после первой начинаются с **＋** или **－**.
**＋** Превью ledger-строк — в `ratification`, fence без тега.
**＋** Строка `create` несёт `{tags:a,b}`. Категория из префикса slug.
**＋** В Spec под каждым Case стоит блок `then`.
**－** В чате блока нет. Правило LEDGER не меняется.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-34
