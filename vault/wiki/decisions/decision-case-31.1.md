---
type: decision
case: "31.1"
status: current
kind: [update, update, update]
target_slug: [decisions-schema, decisions-schema-yaml, rule-ask]
origin: raw/2026-09-10/ledger.md#case-31.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Context

Первый шаг Documentation. Скрипт собирает `raw/<date>/materialize.yaml` из ledger и Spec. Librarian читает yaml вместо ledger и Spec (§10).

## Problem

Форма yaml, грамматика строк, ledger со Spec старше конвенции, имена Decision-страниц.

## Given

Схема decisions: одна страница на строку. Case 11 дал бы восемь одинаковых страниц.
**＋** Render `ask-guppi` не запрещает Grep по `wiki/`.
**－** Индексов decisions нет и не будет.

## When

`guppi generate` пишет Decision-страницу. `ask-guppi` ищет.

## Note

The `then` of the Case, as ratified:

Одна страница на Case, slug `decision-case-<N>`, строки Case — список `targets`.
**＋** `ask-guppi` не открывает и не grep'ит `wiki/decisions/`, если вопрос не «почему так решили».
**－** Ничего не архивируется.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-31.1
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
