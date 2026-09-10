---
type: decision
case: "43"
status: current
targets:
  - {kind: update, category: rules, slug: rule-materialize}
  - {kind: create, category: estimates, slug: estimate-materialize-walks-dates, ref: rule-materialize}
  - {kind: update, category: rules, slug: rule-page-generation}
  - {kind: create, category: estimates, slug: estimate-generate-walks-dates, ref: rule-page-generation}
  - {kind: update, category: rules, slug: rule-documentation}
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger, session, librarian, render]
---

## Context

Чтения handoff-фазы пишутся после коммита библиотекаря, в ledger своей даты. Следующая сессия обычно на другой дате.

## Now

`rule-materialize` и `rule-page-generation` `built`, обе фиксируют одну `raw/<date>/`. Ни одна страница не покрывает остаток за границей даты (ask-guppi).
**＋** Yaml дополняется, `applied` делает повтор идемпотентным (Case 41). Обход по датам ничего не переписывает.
**＋** `rule-documentation` `render_mode: full`: правка текста перерендеривает `.claude/agents/librarian-guppi.md`.
**＋** Slugs `estimate-materialize-walks-dates`, `estimate-generate-walks-dates` свободны. Теги: `harness`, `workflow`, `ledger`.
**－** Yaml 2026-09-09 держит упавший `old-harness`; при обходе `generate` флагует его каждый запуск и выходит 1. Известный долг, свой Case из брифа.
**－** `rule-handoff` не меняется: `Materialize <date>.` называет дату сессии, остаток подбирает скрипт.
**－** Страница `passed` с Result вторую строку не принимает; поэтому новые Estimates, не `update` старых.

## Problem

`materialize` и `generate` читают одну `raw/<date>/`, по умолчанию сегодня. Строки после коммита библиотекаря никто не материализует, если следующая сессия не на той же дате. Хвост сессии E спасён только совпадением дат.

## Then

`uv run guppi materialize` и `uv run guppi generate` без `--date`.

`materialize` обходит каждую `vault/raw/<date>/` с `ledger.md` по возрастанию даты, дополняет или пишет её yaml, печатает одну строку на дату.
**＋** `generate` обходит каждую `vault/raw/<date>/` с `materialize.yaml` по возрастанию даты, применяет непримененные записи.
**＋** Дата без новых строк и без непримененных записей ничего не меняет.
**＋** `--date` ограничивает обход одной датой, поведение прежнее.
**＋** Библиотекарь читает каждый yaml, названный на stdout, для index check и синтеза.
**－** Ошибка одной даты: `materialize` печатает её и выходит 1, не идя дальше; `generate` продолжает, выходит 1 в конце.
**－** `cleanup` не меняется.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
