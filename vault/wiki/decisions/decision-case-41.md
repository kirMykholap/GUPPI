---
type: decision
case: "41"
status: current
targets:
  - {kind: update, category: rules, slug: rule-materialize}
  - {kind: update, category: estimates, slug: estimate-materialize-assembles}
supersedes: [decision-case-31]
origin: raw/2026-09-10/ledger.md#case-41
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Один ledger материализуется в два приёма.

## Now

Case 31: «yaml уже есть — exit 1».
**＋** Каждая запись несёт `line`. `generate` помечает `applied`.
**－** В этой сессии скрипты бегут по сегодняшнему ledger дважды.

## Problem

Отказ теряет поздние строки и ломает второй запуск.

## Then

`uv run guppi materialize` при существующем `materialize.yaml`.

Записи с известным `line` остаются как были.
**＋** Новые строки ledger — новые записи в конце.
**＋** Текст по номеру не совпал — флаг, запись не трогается.
**＋** Поздний `supersedes` дописывает ранней записи `superseded_by`. Больше ничего.
**＋** `estimate`-строка для `create` с `applied` — своя запись `estimate`.
**＋** Stdout: сколько добавлено. Exit 0.
**－** Критерий `estimate-materialize-assembles` меняется в этой части.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-41
