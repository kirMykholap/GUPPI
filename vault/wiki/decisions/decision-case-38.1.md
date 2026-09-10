---
type: decision
case: "38.1"
status: superseded
targets:
  - {kind: create, category: rules, slug: rule-retro, ref: rule-end-of-work}
  - {kind: create, category: estimates, slug: estimate-retro-loads, ref: rule-retro}
superseded_by: [decision-case-40]
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Context

Конец работы: Retro, коммит, handoff с вызовом librarian'а. Сейчас всё по памяти.

## Now

Retro смотрит на эту сессию. Правка кода допустима, если заканчивает работу из сегодняшнего ledger.
**＋** Баг — `lesson[error]`. Красные тесты — `lesson[error]` с причиной «почему дошли до Retro с регрессией».
**－** Skill'а нет.

## Problem

Retro без рамки. Коммит — инструкция, которую можно пропустить. Handoff без формы.

## Then

Человек вызывает `/retro`.

В контексте до первого хода: `make test`, `make style`, сегодняшний ledger. Без read-вызовов.
**＋** В `event_log.md` строка `retro`.
**＋** Агент обсуждает только эту сессию. Правит только то, что ведёт к строке сегодняшнего ledger.
**＋** Баг — `lesson[error]`. Отложенный — `defer`.
**＋** Ответ заканчивается списком ратификаций, сделанного и несделанного. Когда человек одобрил — коммит, потом `/handoff` (Case 40).
**－** `make lint` в Retro не запускается. Skill вызывает только человек.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 superseded by decision-case-40 · raw/2026-09-10/ledger.md#case-40
