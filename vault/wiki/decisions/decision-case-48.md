---
type: decision
case: "48"
status: current
targets:
  - {kind: update, category: rules, slug: rule-page-generation}
  - {kind: create, category: estimates, slug: estimate-generate-passes-delete-outside-vault, ref: rule-page-generation}
origin: raw/2026-09-10/ledger.md#case-48
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Строка 8 ledger 2026-09-09, `decision[case 6][delete][old-harness]{source:docs/harness-map-2026-09-07.md}`: удаление старого harness'а, файлов, а не страницы. Записана рукой при backfill. Каждый прогон `generate` роняет её: `old-harness: no page to delete`, exit 1.

## Now

Запись yaml 2026-09-09 строка 78–90: `category: unknown`, `incomplete: [category, then]`, `failed`. `decision-case-6` написана и `applied` (строка 1168). Case 6 Spec'а не имеет блока `then`.
**＋** `rule-page-generation` строка 52: «A `delete` sets `status: archived` with History `deleted`»; про slug без категории молчит. `materialize` даёт `category: unknown` такому slug.
**＋** Slug `estimate-generate-passes-delete-outside-vault` свободен. Теги страницы.
**－** `guppi materialize` не меняется: `unknown` — честная категория для вещи вне vault.
**－** Строка ledger не переписывается и не superseded: решение верное, исполнитель не умел его прочесть.

## Problem

Грамматика ledger позволяет `delete` вещи вне vault, и `source` для того и нужен; `generate` знает только удаление страницы. Запись без категории и без страницы падает вечно, обход дат несёт её в каждый прогон, exit 1 маскирует настоящие падения. Правка yaml рукой запрещена (Case 44); Slice 3c не архивирует дату с непримененной записью.

## Then

`uv run guppi generate` встречает `delete`, чей slug не несёт префикса категории.

Запись печатается на stdout как удаление вне vault, без страницы к архивации, и отмечается `applied`; страниц не пишется, History нет.
**＋** Следующий прогон обхода над 2026-09-09 ничего не печатает на stderr и выходит 0.
**－** `delete` с категорией и без страницы падает как прежде.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-48
