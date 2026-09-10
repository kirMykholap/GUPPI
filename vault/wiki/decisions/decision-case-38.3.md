---
type: decision
case: "38.3"
status: current
targets:
  - {kind: create, category: rules, slug: rule-handoff, ref: rule-end-of-work}
  - {kind: create, category: estimates, slug: estimate-handoff-dispatches, ref: rule-handoff}
origin: raw/2026-09-10/ledger.md#case-38.3
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Context

Конец работы: Retro, коммит, handoff с вызовом librarian'а. Сейчас всё по памяти.

## Now

`handoff.md` несёт три раздела. Главный агент не перечитывает артефакты для него.
**＋** Librarian — агент, его вызывает главный агент.
**－** Skill'а нет.

## Problem

Retro без рамки. Коммит — инструкция, которую можно пропустить. Handoff без формы.

## Then

Агент вызывает `/handoff`.

В контексте `git status --porcelain`. Не пуст — агент останавливается: «commit first».
**＋** В `event_log.md` строка `handoff`.
**＋** Агент дописывает `raw/<date>/handoff.md` из памяти: три раздела.
**＋** Агент вызывает `librarian-guppi` одной строкой. Ждёт отчёт. Показывает его.
**－** После этого не коммитит. Skill вызывает агент.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.3
