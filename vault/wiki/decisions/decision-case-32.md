---
type: decision
case: "32"
status: current
kind: [create, create, update]
target_slug: [rule-page-generation, estimate-generate-writes, lessons-schema]
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Единственный писатель в `wiki/`. Пишет страницы, обратные ссылки, History, `log.md`, теги, считает `built`.

## Problem

Что скрипт выводит механически, какими шаблонами, как ведёт себя при ошибке и повторе.

## Given

Черновик: коллизия — ошибка; страница создаётся всегда; `origin`, `status`, `parent`, `children`, backlinks — производные.
**＋** У Estimate нет статуса `archived`, хотя схема уроков велит архивировать Estimate error-урока. Статуса `deleted` нет ни в одной `schema.yaml`.
**＋** `sprint` — первый заголовок `## <id>` в `sprint.md`.
**－** Все 34 страницы и `log.md` написаны руками.

## When

Librarian или главный агент запускает `uv run guppi generate`.

## Note

The `then` of the Case, as ratified:

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
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
