---
type: decision
case: "33"
status: current
targets:
  - {kind: create, category: rules, slug: rule-cleanup, ref: rule-documentation}
  - {kind: create, category: estimates, slug: estimate-cleanup-moves, ref: rule-cleanup}
  - {kind: update, category: file, slug: index, path: vault/wiki/index.md}
  - {kind: update, category: file, slug: glossary, path: vault/wiki/glossary.md}
origin: raw/2026-09-10/ledger.md#case-33
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Context

Страница со `status: archived` должна уйти из живого vault. Скрипта нет.

## Now

`wiki/archive/` пуст. `index.md` §1 и glossary называют `wiki/archive/`, lint читает его.
**＋** `vault/archive/` занят старым архивом, 505 файлов, до Slice 5.
**＋** Каждый `origin` указывает в `raw/<date>/`.
**－** Черновик велит переносить `raw/`. Это сломает origin.

## Problem

Куда переносить. Кто правит ссылки. Что с `raw/`.

## Then

Librarian запускает `uv run guppi cleanup`.

Каждая живая страница со `status: archived` лежит в `vault/archived/<sprint>/<date>/<category>/<slug>.md`.
**＋** У неё строка History `archived · cleanup`. В `log.md` такая же.
**＋** Её slug убран из `children` и `estimates` живых страниц. Секции пересобраны. У них строка History.
**＋** Индексы пересобраны без неё.
**＋** Страница в архиве со статусом не `archived` вернулась в `wiki/<category>/`. History `restored · cleanup`.
**－** `children` у Insight не меняются. `[[slug]]` в тексте не меняются.
**－** Живая страница, чей `parent` или `target` ушёл в архив, остаётся. Флаг в stderr.
**－** Повторный запуск ничего не переносит. Exit 0.
**－** Файл, который нельзя перенести, или занятое имя — stderr, exit 1. Остальные переносятся.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-33
