---
type: decision
case: "44"
status: current
targets:
  - {kind: update, category: rules, slug: rule-documentation}
  - {kind: update, category: rules, slug: rule-index-check}
  - {kind: update, category: rules, slug: rule-synthesis}
  - {kind: update, category: estimates, slug: estimate-synthesis-clusters}
  - {kind: update, category: estimates, slug: estimate-documentation-completes}
origin: raw/2026-09-10/ledger.md#case-44
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian, render]
---

## Context

Два чтения Slice 3 упали на чтениях библиотекаря: страница урока перед синтезом, `guppi/generate.py` трижды до любой ошибки, потом правка yaml через sed после краха `generate`.

## Now

`rule-documentation` (`draft`, MOC, `render_mode: full`) строки 42–46: «Read four things and nothing else … Open a page only when a script reports a problem, or an index line is not enough to judge». `rule-index-check` (`draft`) повторяет разрешение. `rule-synthesis` (`draft`): «Do not read the archive and do not write pages yourself», о страницах уроков молчит. `estimate-synthesis-clusters` (`pending`): «no archive file and no lesson page was read». Ask-guppi: приоритет Render родителя над критерием ребёнка нигде не задан.
**＋** Обе оценки стоят `failed` в ledger-хвосте (11:57:07), ещё не в yaml. Следующий `generate` применит `failed`, затем правки этого Case; `passed` ляжет после следующего прогона библиотекаря. Slice 3 закрывается тогда.
**＋** `lesson-librarian-reads-beyond-the-four-inputs` (knowledge, в хвосте) получит Research-оценку `pending`; утверждение проверено по страницам сейчас, строка `passed` в ответе Case.
**＋** `guppi/generate.py` не читает `near`, `librarian`, `merged`; `rule-brief` их отчитывает. Описание меток — факт.
**＋** Все slug заняты, только `update`. Теги без изменений.
**－** Insight остаётся продуктом библиотекаря, статус `open`, бриф его называет; ратификация приходит Case'ом, который на нём действует. Глоссарий и `insights/schema.md` не меняются.
**－** Правка yaml после краха 11:51: с Case 46 запись падает одна; рамка называет отвергнутую запись флагом.
**－** `render` файла агента после правки — шаг 1 Work Mode этой сессии.

## Problem

Рамка говорит «четыре входа и ничего больше», а два её суждения иногда требуют страницы: строка индекса не различает «то же» и «рядом», а Insight нельзя написать по одной строке старого урока. Критерий `estimate-synthesis-clusters` запрещает то, что рамка разрешает. Метки yaml не описаны нигде, и за ними пошли в код. Правка yaml сверх меток не запрещена, и её сделали.

## Then

Библиотекарь запускается по файлу агента, отрендеренному из `rule-documentation`, и после его прогона снимаются чтения `estimate-documentation-completes` и `estimate-synthesis-clusters`.

Библиотекарь читает четыре входа прогона.
**＋** Страницу `wiki/` он открывает в трёх случаях: строка индекса не решает «то же или рядом»; он пишет Insight и ему нужны Trigger и Root cause его уроков; скрипт назвал страницу в ошибке и он объясняет причину. Каждую открытую страницу он называет в отчёте с причиной.
**＋** Он не читает `ledger.md`, `spec.md`, `plan.md`, `wiki/decisions/`, `vault/archived/`, файлы под `guppi/` и `tests/`; рамка говорит, что значит каждая метка yaml.
**＋** Yaml он правит только метками и записями index check и синтеза; запись, отвергнутая скриптом, остаётся как есть и становится флагом.
**＋** `estimate-synthesis-clusters` проходит, когда архив не читан, а каждая прочитанная страница урока названа в отчёте как ребёнок написанного Insight.
**＋** `estimate-documentation-completes` проходит, когда каждое чтение сверх четырёх входов названо с одной из трёх причин, сырьё сессии и код не читаны, yaml не правлен сверх меток и записей.
**－** Что содержит Insight, кто его создаёт и его статусы — без изменений.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-44
