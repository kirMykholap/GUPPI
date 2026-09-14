---
type: decision
case: "49"
status: current
update: ["[[estimate-index-check-merges]]", "[[rule-materialize]]", index]
origin: raw/2026-09-10/ledger.md#case-49
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian, ledger]
---

## Context

`/pre-task` над Cases 44–48 нашёл три места, где vault останется в расхождении с ратифицированным, и одно, где формулировка Case 48 неточна.

## Problem

`estimate-index-check-merges` не требует называть открытую страницу, так что отчётная часть Case 44 у index check не проверяется ничем. `rule-materialize` перечисляет метки yaml без `failed` и `folded`, которые скрипты уже пишут и которые рамка Case 44 описывает. Таблица маршрутов §5 `index.md` не знает `delete` вне vault, который Case 48 вводит. Case 48 говорил «без префикса категории», а `materialize` без префикса даёт и Rule-class файлы.

## Given

`estimate-index-check-merges` (`pending`): «no page was read when its index line sufficed». `rule-materialize` строка 41: «`exists` (a create whose page is on disk), `applied` (set by `guppi generate`)». §5 `index.md`: строки таблицы для `delete` только с target.
**＋** Остальные находки pre-task уже известны: `estimate-generate-writes` («log.md gains one line per write», «a replace … fails that entry alone») верна и после Case 47; «exactly one occurrence» в `rule-page-generation` согласуется со списком пар; расхождения Case 46 с §1, §3, §4, глоссарием, схемами, `rule-ask`, `rule-cleanup`, `rule-documentation`, `rule-skill-hi` — работа Plan Mode Slice 3c, Case 46 так и говорит.
**－** Новых страниц нет.

## When

Библиотекарь читает отчёт index check; кто-то читает `rule-materialize` или §5.

## Note

The `then` of the Case, as ratified:

`estimate-index-check-merges` проходит, когда каждая открытая при index check страница названа в отчёте со строкой индекса, которая не решила «то же или рядом».
**＋** `rule-materialize` перечисляет `folded`, `applied` и `failed` среди полей записи.
**＋** §5 держит строку: `delete` без target и без категории — вне vault, Decision-страница фиксирует, `generate` отмечает applied.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-49
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
