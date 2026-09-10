---
type: decision
case: "47"
status: current
targets:
  - {kind: update, category: rules, slug: rule-page-generation}
  - {kind: update, category: file, slug: case-schema, path: vault/wiki/case-schema.md}
  - {kind: create, category: estimates, slug: estimate-generate-rejects-shape-alone, ref: rule-page-generation}
  - {kind: create, category: estimates, slug: estimate-generate-logs-per-entry, ref: rule-page-generation}
  - {kind: create, category: estimates, slug: estimate-generate-dates-history-by-run, ref: rule-page-generation}
origin: raw/2026-09-10/ledger.md#case-47
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Первый прогон библиотекаря оставил три урока об `generate`: `replace` в форме mapping уронил весь прогон; `log.md` пишется один раз в конце, и крах потерял девять строк ленты; при обходе дат History и log получили дату yaml, а не прогона.

## Now

`rule-page-generation` (`draft`, `check`, `guppi/generate.py`) строки 31–33: падение записи — collision, `ref` без страницы, `replace` без текста; строка 37: «`created` is the yaml's date»; строка 46: «`log.md` gets the same line». `case-schema.md` строка 60: «`replace` (`old` → `new` inside the body)», форма не задана.
**＋** `estimate-generate-writes` `passed` с Result: вторую строку не примет, потому новые Estimates. Slugs `estimate-generate-rejects-shape-alone`, `estimate-generate-logs-per-entry`, `estimate-generate-dates-history-by-run` свободны (estimates-index). Теги страницы: `harness`, `workflow`, `ledger`.
**＋** `generate.py`: `Vault.date` — дата yaml, используется и для `created`, и для History (строка 221), и для log (225); `write_log` вызывается один раз в конце `apply` (649); `replace` итерируется как список (395).
**＋** `log.md` — рабочий файл, не страница (case-schema «Not schema-governed»); девять строк известны из History страниц entries 78–82 и брифа.
**＋** Уроки `lesson-generate-replace-mapping-crashes`, `lesson-generate-log-written-last`, `lesson-generate-walk-history-dated-by-yaml` в хвосте; их Estimate `passed` от рождения (error). Insight поверх них — дело библиотекаря.
**－** Yaml 2026-09-10 уже в списочной форме (правка библиотекаря); переписывать его не нужно.
**－** `old-harness` не в этом Case.

## Problem

Контракт `rule-page-generation` называет три причины падения записи и обещает, что остальные применяются; неожиданная форма поля к ним не относится и роняет всё. Лента и страницы расходятся после любого исключения. Дата в History лжёт при обходе. Форма `replace` не закреплена в `case-schema.md`, и Spec Case 43 написал её иначе, чем читает скрипт.

## Then

`uv run guppi generate` применяет yaml, в том числе при обходе дат; кто-то пишет блок `then` с `replace`.

Запись, чьё поле имеет форму, которую скрипт не ждёт, или в которой поднялось любое исключение, отмечается `failed`, печатается на stderr и пропускается; остальные записи применяются; выход 1.
**＋** После каждой применённой записи её строки дописаны в `log.md`; прогон, остановившийся на записи N, оставил в ленте строки записей до N.
**＋** History-строки и строки `log.md` несут дату прогона; `created` страницы — дату yaml.
**＋** `case-schema.md`: `replace` — список пар `{old, new}`; одна пара тоже список из одного элемента.
**＋** Девять строк entries 78–82 дописаны в `log.md` руками под этим Case.
**－** `materialize` не меняется: форму `replace` он поднимает как написано; неверную форму отвергает `generate`, одной записью.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-47
