---
type: decision
case: "56"
status: current
update: ["[[rule-retro]]", case-schema, decisions-schema-yaml, decisions-schema, "[[rule-materialize]]", "[[estimate-retro-loads]]"]
supersedes: ["[[decision-case-50]]"]
origin: raw/2026-09-11/ledger.md#case-56
sprint: migration
created: 2026-09-11
tags: [session, workflow, harness, render, ledger]
---

## Context

Case 50 отложил переосмысление Retro без текста; восстановлено из handoff G (строки 104–107) и дополнения владельца: Retro открывается фронтиром работ, замечания агента и человека, исход каждого — строка, решения только `defer` в короткой форме.

## Problem

`rule-retro` читается как малый Plan Mode. Нет открывающего фронтира, нет шага чтений, нет пути «откатить и отложить». Полная форма Case для defer избыточна; Decision-страница по 52.1 требует Given и When, которых у отсрочки нет.

## Given

`rule-retro` Render: контекст загружает `make test`, `make style`, ledger дня; «Discuss … in the Case form»; правки в счёт ratified; остальное defer; красные тесты — урок; три списка, коммит, `/handoff`.
**＋** 52.1: Decision body Given, When required. 52.2: Retro Case — семь секций. `materialize` метит отсутствующие секции `incomplete`.
**＋** `estimate-retro-loads` `passed`; по 53.2 дополняется, `pending`. `rule-retro-commit` требует чистое дерево.
**－** Три списка, коммит, `/handoff`, загрузка контекста — без изменений.

## When

Человек вызывает `/retro`; в Retro возникает замечание; красные тесты; Estimates этой сессии в `pending` с законченной работой.

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#case-56
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
