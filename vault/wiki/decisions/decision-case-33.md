---
type: decision
case: "33"
status: current
create: ["[[rule-cleanup]]", "[[estimate-cleanup-moves]]"]
update: [index, glossary]
origin: raw/2026-09-10/ledger.md#case-33
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Context

Страница со `status: archived` должна уйти из живого vault. Скрипта нет.

## Problem

Куда переносить. Кто правит ссылки. Что с `raw/`.

## Given

`wiki/archive/` пуст. `index.md` §1 и glossary называют `wiki/archive/`, lint читает его.
**＋** `vault/archive/` занят старым архивом, 505 файлов, до Slice 5.
**＋** Каждый `origin` указывает в `raw/<date>/`.
**－** Черновик велит переносить `raw/`. Это сломает origin.

## When

Librarian запускает `uv run guppi cleanup`.

## Note

The `then` of the Case, as ratified:

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
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
