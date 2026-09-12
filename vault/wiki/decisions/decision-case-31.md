---
type: decision
case: "31"
status: superseded
create: [rule-materialize, estimate-materialize-assembles]
superseded_by: [decision-case-41]
origin: raw/2026-09-10/ledger.md#case-31
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Первый шаг Documentation. Скрипт собирает `raw/<date>/materialize.yaml` из ledger и Spec. Librarian читает yaml вместо ledger и Spec (§10).

## Problem

Форма yaml, грамматика строк, ledger со Spec старше конвенции, имена Decision-страниц.

## Given

`index.md` §4: `decision` → действие, содержание из Spec; `estimate` → статус и результат; `lesson` → `create` из строки; `supersedes` — цепочка.
**＋** `guppi/ledger.py` разбирает строки: переиспользуется.
**＋** Ledger 2026-09-09: 85 строк, HTML-комментарии, строки без времени, `{ref}`, `{source}`, `{supersedes}`. Его Spec без блоков `then`. Страницы уже существуют.
**－** Decision-страниц нет ни одной.

## When

Librarian или главный агент запускает `uv run guppi materialize`.

## Note

The `then` of the Case, as ratified:

В `raw/<date>/materialize.yaml` есть запись на каждую строку-запись ledger, в порядке ledger: `case`, `kind`, `category`, `slug`, `ref`, `source`, `supersedes`, `origin`, `line`, `text`, `decision`, `fields`, `sections`, `replace`, `change`, `incomplete`, `exists`.
**＋** `category` — из префикса slug; Rule-class файл — `file` с путём.
**＋** Вложенный `estimate` из блока `create` — своя запись `create`.
**＋** `estimate`-строка для страницы этого ledger сложена в её запись; для ранней страницы — запись `estimate`.
**＋** `lesson`-строка — запись `create` в `lessons` с `root_cause`, `Trigger`, `Root cause`; `origin` `#L<n>`.
**＋** Запись, перекрытая `supersedes`, несёт `superseded_by`.
**＋** Блока `then` под Case нет — `incomplete: then`. Страница `create` уже на диске — `exists: true`.
**＋** Одна Decision-запись на Case: `decision: decision-case-<N>`, `case_text` из семи цитат, `targets` из всех строк Case.
**－** Строка, которую грамматика не разобрала, — в `unparsed`; скрипт продолжает.
**－** Существующий yaml не переписывается: см. Case 41.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-31
- 2026-09-10 superseded by decision-case-41 · raw/2026-09-10/ledger.md#case-41
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
