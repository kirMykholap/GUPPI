---
type: decision
case: "55.2"
status: current
kind: [update, update]
target_slug: [rule-ledger-write, estimate-ledger-write-lifts]
origin: raw/2026-09-11/ledger.md#case-55.2
sprint: migration
created: 2026-09-11
tags: [session, hooks, harness, ledger]
---

## Context

Хук ledger дважды терял ратифицированные строки. Вчера: реплики Cases 48 и 49 кончались `/pre-task` и `ExitPlanMode`, `Stop` не сработал (Case 51, отложен). Сегодня: сессия перешла полночь, хук искал `session-start` и `hi` в сегодняшнем логе; 44 строки Case 53 ушли только после resume.

## Problem

Окно `hi` привязано к файлу одного дня; хук привязан к одному событию, которого у части реплик нет.

## When

Хук `Stop` срабатывает.

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#case-55.2
