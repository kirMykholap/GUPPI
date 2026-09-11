---
type: decision
case: "52.3"
status: current
kind: [update, update, update, update, update, update, update, update, update, update]
target_slug: [rules-schema-yaml, rules-schema, entities-schema-yaml, entities-schema, rule-page-generation, rule-index, rule-ask, rule-lint, index, glossary]
origin: raw/2026-09-10/ledger.md#case-52.3
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger, session]
---

## Context

Decision-страница сегодня — журнал по Case: `targets` списком объектов, тело из четырёх секций старой формы Case, пустое у defer с Retro. Цель defer не знает, что по ней что-то отложено; её History указывает на строку ledger, не на решение.

## Problem

Форма полей Decision и тела; откуда у Retro-Case берётся текст; поле `deferred_by` на цели и его путь через индекс в ask; History и порядок записи.

## When

`guppi generate` applies a `defer`; `guppi index` builds the index; `ask-guppi` answers about a page carrying the field.

## History

- 2026-09-11 created · raw/2026-09-10/ledger.md#case-52.3
