---
type: decision
case: "35.1"
status: current
targets:
  - {kind: create, category: rules, slug: rule-index-check, ref: rule-documentation}
  - {kind: create, category: estimates, slug: estimate-index-check-merges, ref: rule-index-check}
origin: raw/2026-09-10/ledger.md#case-35.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Context

Между скриптами librarian сверяет новые страницы с индексами, собирает Insight, пишет brief. Каждая — partial render в файл агента.

## Now

§10: единственное суждение — `create` → `update` при дубликате. Остальное — флаг.
**＋** Индексы: одна строка на живую страницу. Сравнение не идёт между категориями.
**＋** `handoff.md` несёт прямые указания.

## Problem

Границы каждого шага.

## Then

Librarian прочитал `materialize.yaml` и `handoff.md`.

Он выполняет указания из `handoff.md` первыми.
**＋** Для каждой записи `create` сравнивает `purpose` (`criterion`, `root_cause`) со строками индекса той же категории по смыслу.
**＋** Дубликат: запись становится `update` найденной страницы, `change: merged by librarian: <why>`, пометка `librarian: merged`.
**＋** Похожая страница: флаг `near: <slug>`.
**－** Он не читает страницы без нужды. Не меняет содержание. Не сравнивает между категориями.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.1
