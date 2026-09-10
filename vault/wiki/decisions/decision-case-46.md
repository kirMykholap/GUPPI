---
type: decision
case: "46"
status: current
targets:
  - {kind: update, category: file, slug: migration-plan, path: docs/migration/migration-plan.md}
origin: raw/2026-09-10/ledger.md#case-46
sprint: migration
created: 2026-09-10
tags: []
---

## Context

Несколько сессий в день. Строки ledger после коммита библиотекаря и `origin` как путь в `raw/` держат весь `raw/` навсегда, а хвост сессии виден только через разницу с yaml.

## Now

`migration-plan.md` — Rule-class (`migration-plan` в `RULE_CLASS` у `materialize`), правится руками в Work Mode. `sprint.md` не страница и не Rule-class: ledger-строке на него нет категории; он зеркалит план и правится руками под этим Case.
**＋** `origin` сегодня на 166 страницах путём `raw/<date>/ledger.md#case-N` или `#L<n>`; глоссарий определяет его как «the Decision that created or deleted the page» и grep-цель lint. `decided_by` в vault не встречается.
**＋** `guppi cleanup` уже переносит `archived` страницы в `vault/archived/<sprint>/<date>/<category>/`; `raw/` не трогает. `event_log.md` в gitignore.
**＋** Definition of done п. 1 требует `origin` у каждой страницы; с переименованием формулировка должна допускать `decided_by`.
**－** Case 45 отложен до этого slice; `old-harness` (Frontier п. 6) блокирует архивацию 2026-09-09 и решается до него или в нём.
**－** Что именно меняется в `generate`, `lint`, схемах и семи Rule-страницах — Cases того Plan Mode, здесь только контракт slice.

## Problem

`origin` смешивает два смысла: «какое решение породило страницу» и «где строка в ledger». Пока страницы указывают путём в `raw/`, `raw/` нельзя очищать, и хвост после библиотекаря приходится вычислять. Модель обсуждена в чате; без записи в план она живёт только там.

## Then

Кто-то читает `migration-plan.md` или `sprint.md`; Plan Mode Slice 3c открывается.

Phase 1 плана перечисляет archive script с контрактом: `decided_by`/`origin`, архив `raw/<date>/` по штампу прогона для полностью применённых дат, переписывание путей, свежий ledger как хвост, `/hi` печатает `raw/*/ledger.md`, lint на оба поля, миграция страниц скриптом.
**＋** Definition of done п. 1: «`decided_by` or `origin`, as its schema says».
**＋** `sprint.md` перечисляет Slice 3c между 3b и 4 с той же формулой в одну строку и правит п. 1.
**－** Порядок 3b и 3c не фиксируется: оба до Slice 4.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-46
