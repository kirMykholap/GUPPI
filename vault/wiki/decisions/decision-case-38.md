---
type: decision
case: "38"
status: current
targets:
  - {kind: create, category: rules, slug: rule-end-of-work}
  - {kind: create, category: estimates, slug: estimate-end-of-work-order, ref: rule-end-of-work}
origin: raw/2026-09-10/ledger.md#case-38
sprint: migration
created: 2026-09-10
tags: [session, workflow]
---

## Context

Конец работы: Retro, коммит, handoff с вызовом librarian'а. Сейчас всё по памяти.

## Now

`/hi` показал образец skill'а. `rule-pretask-hook` — образец `PreToolUse`-отказа.
**＋** Команда человека не проходит через `Skill`. `guppi event tool` читает поле `skill`.
**－** `gh` не авторизован.

## Problem

Retro без рамки. Коммит — инструкция, которую можно пропустить. Handoff без формы.

## Then

Человек вызывает `/retro`. Агент вызывает `/handoff`. Librarian возвращает отчёт.

Порядок держится: Retro, коммит, handoff, librarian. Handoff не начинается без коммита. Librarian — без `handoff.md`.
**＋** `make test-end-of-work` зелёный.
**－** После handoff главный агент не коммитит.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
