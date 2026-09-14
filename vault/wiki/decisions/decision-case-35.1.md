---
type: decision
case: "35.1"
status: current
create: ["[[rule-index-check]]", "[[estimate-index-check-merges]]"]
origin: raw/2026-09-10/ledger.md#case-35.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Context

Между скриптами librarian сверяет новые страницы с индексами, собирает Insight, пишет brief. Каждая — partial render в файл агента.

## Problem

Границы каждого шага.

## Given

§10: единственное суждение — `create` → `update` при дубликате. Остальное — флаг.
**＋** Индексы: одна строка на живую страницу. Сравнение не идёт между категориями.
**＋** `handoff.md` несёт прямые указания.

## When

Librarian прочитал `materialize.yaml` и `handoff.md`.

## Note

The `then` of the Case, as ratified:

Он выполняет указания из `handoff.md` первыми.
**＋** Для каждой записи `create` сравнивает `purpose` (`criterion`, `root_cause`) со строками индекса той же категории по смыслу.
**＋** Дубликат: запись становится `update` найденной страницы, `change: merged by librarian: <why>`, пометка `librarian: merged`.
**＋** Похожая страница: флаг `near: <slug>`.
**－** Он не читает страницы без нужды. Не меняет содержание. Не сравнивает между категориями.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.1
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
