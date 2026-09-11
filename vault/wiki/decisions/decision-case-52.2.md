---
type: decision
case: "52.2"
status: current
kind: [update, update]
target_slug: [rule-retro, case-schema]
origin: raw/2026-09-10/ledger.md#case-52.2
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Context

Decision-страница сегодня — журнал по Case: `targets` списком объектов, тело из четырёх секций старой формы Case, пустое у defer с Retro. Цель defer не знает, что по ней что-то отложено; её History указывает на строку ledger, не на решение.

## Problem

Форма полей Decision и тела; откуда у Retro-Case берётся текст; поле `deferred_by` на цели и его путь через индекс в ask; History и порядок записи.

## When

At Retro a Case is ratified or deferred; the agent writes the `LEDGER` block.

## History

- 2026-09-11 created · raw/2026-09-10/ledger.md#case-52.2
