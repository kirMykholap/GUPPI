---
type: decision
case: "38.3"
status: archived
create: ["[[rule-handoff]]", "[[estimate-handoff-dispatches]]"]
origin: raw/2026-09-10/ledger.md#case-38.3
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Context

Конец работы: Retro, коммит, handoff с вызовом librarian'а. Сейчас всё по памяти.

## Problem

Retro без рамки. Коммит — инструкция, которую можно пропустить. Handoff без формы.

## Given

`handoff.md` несёт три раздела. Главный агент не перечитывает артефакты для него.
**＋** Librarian — агент, его вызывает главный агент.
**－** Skill'а нет.

## When

Агент вызывает `/handoff`.

## Note

The `then` of the Case, as ratified:

В контексте `git status --porcelain`. Не пуст — агент останавливается: «commit first».
**＋** В `event_log.md` строка `handoff`.
**＋** Агент дописывает `raw/<date>/handoff.md` из памяти: три раздела.
**＋** Агент вызывает `librarian-guppi` одной строкой. Ждёт отчёт. Показывает его.
**－** После этого не коммитит. Skill вызывает агент.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.3
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
