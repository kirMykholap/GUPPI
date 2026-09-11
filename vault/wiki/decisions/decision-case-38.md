---
type: decision
case: "38"
status: current
kind: [create, create]
target_slug: [rule-end-of-work, estimate-end-of-work-order]
origin: raw/2026-09-10/ledger.md#case-38
sprint: migration
created: 2026-09-10
tags: [session, workflow]
---

## Context

Конец работы: Retro, коммит, handoff с вызовом librarian'а. Сейчас всё по памяти.

## Problem

Retro без рамки. Коммит — инструкция, которую можно пропустить. Handoff без формы.

## Given

`/hi` показал образец skill'а. `rule-pretask-hook` — образец `PreToolUse`-отказа.
**＋** Команда человека не проходит через `Skill`. `guppi event tool` читает поле `skill`.
**－** `gh` не авторизован.

## When

Человек вызывает `/retro`. Агент вызывает `/handoff`. Librarian возвращает отчёт.

## Note

The `then` of the Case, as ratified:

Порядок держится: Retro, коммит, handoff, librarian. Handoff не начинается без коммита. Librarian — без `handoff.md`.
**＋** `make test-end-of-work` зелёный.
**－** После handoff главный агент не коммитит.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
