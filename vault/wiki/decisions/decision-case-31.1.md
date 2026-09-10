---
type: decision
case: "31.1"
status: current
targets:
  - {kind: update, category: file, slug: decisions-schema, path: vault/wiki/decisions/schema.md}
  - {kind: update, category: file, slug: decisions-schema-yaml, path: vault/wiki/decisions/schema.yaml}
  - {kind: update, category: rules, slug: rule-ask}
origin: raw/2026-09-10/ledger.md#case-31.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Context

Первый шаг Documentation. Скрипт собирает `raw/<date>/materialize.yaml` из ledger и Spec. Librarian читает yaml вместо ledger и Spec (§10).

## Now

Схема decisions: одна страница на строку. Case 11 дал бы восемь одинаковых страниц.
**＋** Render `ask-guppi` не запрещает Grep по `wiki/`.
**－** Индексов decisions нет и не будет.

## Problem

Форма yaml, грамматика строк, ledger со Spec старше конвенции, имена Decision-страниц.

## Then

`guppi generate` пишет Decision-страницу. `ask-guppi` ищет.

Одна страница на Case, slug `decision-case-<N>`, строки Case — список `targets`.
**＋** `ask-guppi` не открывает и не grep'ит `wiki/decisions/`, если вопрос не «почему так решили».
**－** Ничего не архивируется.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-31.1
