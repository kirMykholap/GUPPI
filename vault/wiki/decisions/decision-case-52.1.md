---
type: decision
case: "52.1"
status: current
update: [decisions-schema-yaml, decisions-schema, rule-page-generation, rule-lint]
origin: raw/2026-09-10/ledger.md#case-52.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Decision-страница сегодня — журнал по Case: `targets` списком объектов, тело из четырёх секций старой формы Case, пустое у defer с Retro. Цель defer не знает, что по ней что-то отложено; её History указывает на строку ledger, не на решение.

## Problem

Форма полей Decision и тела; откуда у Retro-Case берётся текст; поле `deferred_by` на цели и его путь через индекс в ask; History и порядок записи.

## Given

`decisions/schema.yaml`: required `targets`, body `## Context`, `## Now`, `## Problem`, `## Then`, `## History`.
**＋** `generate.py`: entries applied (line 629) before decision pages (line 662). History `<action> · <origin>`.
**＋** `materialize.py`: `case_text` from `## Case N` in `spec.md`; Retro Cases never reach the Spec; Cases 50, 51 `incomplete`.
**＋** `rules/schema.yaml`, `entities/schema.yaml`: no `deferred_by`; `built` computed by the cascade.
**＋** `rule-index`: `slug: purpose`. `ask-guppi` never opens `decisions/` unless asked why.
**＋** `materialize` marks `superseded_by` on `{supersedes:case N}`.
**－** `origin` stays a ledger path until Slice 3c.

## When

`guppi generate` writes a Decision page; lint checks it; someone reads `decisions/schema.md`.

## History

- 2026-09-11 created · raw/2026-09-10/ledger.md#case-52.1
- 2026-09-12 Given inherited from the parent Case · [[decision-case-60]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
