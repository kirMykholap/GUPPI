---
type: decision
case: "32"
status: current
targets:
  - {kind: create, category: rules, slug: rule-page-generation, ref: rule-documentation}
  - {kind: create, category: estimates, slug: estimate-generate-writes, ref: rule-page-generation}
  - {kind: update, category: file, slug: lessons-schema, path: vault/wiki/lessons/schema.md}
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Единственный писатель в `wiki/`. Пишет страницы, обратные ссылки, History, `log.md`, теги, считает `built`.

## Now

Черновик: коллизия — ошибка; страница создаётся всегда; `origin`, `status`, `parent`, `children`, backlinks — производные.
**＋** У Estimate нет статуса `archived`, хотя схема уроков велит архивировать Estimate error-урока. Статуса `deleted` нет ни в одной `schema.yaml`.
**＋** `sprint` — первый заголовок `## <id>` в `sprint.md`.
**－** Все 34 страницы и `log.md` написаны руками.

## Problem

Что скрипт выводит механически, какими шаблонами, как ведёт себя при ошибке и повторе.

## Then

Librarian или главный агент запускает `uv run guppi generate`.

`create` даёт страницу с полями записи и производными: начальный статус по категории, `origin`, `sprint`, `created`, `parent` из `ref`, `target` из `ref`. Секции в порядке схемы. Первая строка History.
**＋** Родитель получает `children += slug` в конец, цель Estimate — `estimates += slug`; их секции пересобраны, у них строка History.
**＋** `update`: `set`, `sections`, `replace` (сравнение со схлопнутыми пробелами, ровно одно вхождение), History `updated: <change>`.
**＋** `estimate`: `status`, `## Result` целиком, History `status: a → b`. Страница уже в этом статусе с Result — пропуск.
**＋** `delete`: `status: archived`, History `deleted`. `defer`: History `deferred` или placeholder `draft` из полей Case.
**＋** `lesson`: страница урока и парный Estimate по шаблону. Decision-страница на Case; `supersedes` ставит ранней `superseded`.
**＋** Каскад: все Estimates `passed` → `built`; `built` с не-`passed` → `draft`. `severity` Insight пересчитан.
**＋** Объявленный новый тег — в `tags.md`; необъявленный — сообщён. `log.md`: строка на запись.
**－** Коллизия, `ref` без страницы, `replace` не найден — запись пропущена, stderr, exit 1.
**－** Повторный запуск ничего не пишет.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-32
