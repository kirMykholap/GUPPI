---
type: decision
case: "38.1"
status: archived
create: [rule-retro, estimate-retro-loads]
superseded_by: [decision-case-40]
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Context

Конец работы: Retro, коммит, handoff с вызовом librarian'а. Сейчас всё по памяти.

## Problem

Retro без рамки. Коммит — инструкция, которую можно пропустить. Handoff без формы.

## Given

Retro смотрит на эту сессию. Правка кода допустима, если заканчивает работу из сегодняшнего ledger.
**＋** Баг — `lesson[error]`. Красные тесты — `lesson[error]` с причиной «почему дошли до Retro с регрессией».
**－** Skill'а нет.

## When

Человек вызывает `/retro`.

## Note

The `then` of the Case, as ratified:

В контексте до первого хода: `make test`, `make style`, сегодняшний ledger. Без read-вызовов.
**＋** В `event_log.md` строка `retro`.
**＋** Агент обсуждает только эту сессию. Правит только то, что ведёт к строке сегодняшнего ledger.
**＋** Баг — `lesson[error]`. Отложенный — `defer`.
**＋** Ответ заканчивается списком ратификаций, сделанного и несделанного. Когда человек одобрил — коммит, потом `/handoff` (Case 40).
**－** `make lint` в Retro не запускается. Skill вызывает только человек.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 superseded by decision-case-40 · raw/2026-09-10/ledger.md#case-40
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
- 2026-09-13 archived · superseded
- 2026-09-13 archived · cleanup
