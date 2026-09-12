---
type: decision
case: "45"
status: superseded
defer: [rule-ledger-tail]
superseded_by: [decision-case-63]
origin: raw/2026-09-10/ledger.md#case-45
sprint: migration
created: 2026-09-10
tags: []
---

## Context

Чтения и уроки фазы End of Work пишутся после коммита библиотекаря. Бриф написан раньше них, `/hi` читает только бриф. Хвост сессии F (15 строк, два `failed`) дошёл до этого Frontier только через ручную приписку владельца и память агента.

## Problem

Факт, рождённый после коммита библиотекаря, попадает во Frontier через две сессии: следующий библиотекарь материализует его в страницы, и только бриф после него его назовёт. Упавшее чтение и урок ждут сессию лишнюю.

## Given

Ask-guppi: ни одна страница не покрывает нематериализованный хвост, слепое пятно брифа или чтение ledger из `/hi`; `rule-ledger-tail` и `estimate-tail-lists-unmaterialized` свободны; теги `session`, `harness`, `ledger` зарегистрированы.
**＋** `rule-skill-hi` (`built`, `render_mode: full`) держит свою строку `Recorded: !`uv run guppi event hi`` в собственном Render, без ребёнка; новая строка ложится так же. Скрипт `guppi event` живёт своей страницей `rule-event-log` под `rule-session-start`; `rule-ledger-tail` ложится туда же (Atomicity: рендер и скрипт падают порознь, две страницы).
**＋** `materialize.yaml` держит `line` у каждой записи, `folded` у create со свёрнутым чтением, `unparsed` со своими `line`; `guppi/ledger.py` даёт `body`, `guppi/materialize.py` — `parse_line`, `dates_with`, `load_yaml`. Скрипт складывается из них.
**＋** `estimate-hi-no-read-calls` `passed`; критерий меняется → `pending`, `rule-skill-hi` вернётся в `draft` до чтения следующим `/hi` (lesson-estimates-criterion-stale-after-contract-change).
**＋** Глоссарий, строка `/hi`, Frontier, перечисляет источники Frontier; хвост добавляется туда. Rule-class `update`, руками в Work Mode.
**－** `rule-brief`, `rule-materialize` не меняются: бриф по-прежнему знает только yaml, обход дат уже подбирает хвост в страницы.
**－** `hi` не пишется в ledger, только в event_log; строки без грамматики записи скрипт не печатает.
**－** Дата с `ledger.md` без yaml печатает все свои записи: так виден и ledger сессии, у которой библиотекарь не бежал вовсе.

## When

`uv run guppi tail` запускается; `/hi` вызывает его строкой рендера.

## Note

The `then` of the Case, as ratified:

Для каждой `vault/raw/<date>/ledger.md` по возрастанию даты скрипт печатает каждую строку-запись, номера которой нет ни в `line` записей, ни в `folded`, ни в `unparsed` `materialize.yaml` этой даты, как `<date> L<n>: <строка как в ledger>`.
**＋** Дата без yaml печатает все свои строки-записи.
**＋** Дата, у которой всё материализовано, не печатает ничего; при пустом хвосте вывод пуст.
**＋** Выход 0 всегда; ошибка чтения одной даты печатается на stderr, обход идёт дальше.
**＋** После `/hi` контекст держит вывод `guppi tail` без read-tool вызова; Frontier называет упавшее чтение и урок из хвоста пунктами.
**－** Строка, не разобранная грамматикой ledger, не печатается: она либо уже `unparsed` в yaml, либо не запись.
**－** Decision-строка хвоста — не пункт Frontier: её страницу пишет следующий библиотекарь.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-45
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
- 2026-09-12 superseded by decision-case-63 · [[decision-case-63]]
