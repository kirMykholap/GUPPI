# GUPPI — миграция на модель ратификации. План-карта и Slice 0

## Контекст

Репозиторий `C:\PROJECTS\GUPPI` — это harness вокруг сессий Claude Code и Obsidian-vault,
отделённые 2026-09-07 от продукта job-hunt-ai. Старая модель (ритуал retro → handoff → ingest,
librarian как единственный писатель, 14 хуков, 18 скриптов, 7 skills) описана в
`job_hunt_ai_vault/harness-map.md`. Новая модель описана в `docs/migration/` (17 файлов):
Decision, ратифицированный человеком, как атомарная единица; шесть категорий страниц
(decision, entity, rule, estimate, lesson, insight); Rule со `enforcement: render` *является*
harness'ом; librarian с чистым контекстом читает только `materialize.yaml` и индексы.

Задача: перевести репозиторий со старой модели на новую, сохранив то, что стоит сохранить.
Владелец не может заранее сказать, что оставить, поэтому каждый механизм получает вердикт в
Case, а исполнение идёт слайсами, каждый со своим Plan Mode.

Ритуал старого harness'а игнорируется по разрешению владельца; всю работу делает главный агент,
subagents не диспатчатся (кроме read-only справок по документации платформы).

## Решения, ратифицированные 2026-09-09 (владелец выбрал из вариантов)

| # | Вопрос | Решение |
|---|---|---|
| D1 | Гранулярность ратификации | Phase 1: один Case на механизм harness'а. Phase 2: страницы группами по вердикту, одна ратификация на группу с таблицей внутри |
| D2 | lessons (31) и proposals (52) | Lessons конвертировать в новую схему; proposals запарковать, возвращать по запросу |
| D3 | Старые скрипты | Писать заново на Python через uv, без новых зависимостей (pyyaml уже есть). Старый код — справка, не источник |
| D4 | Мелкие противоречия в docs/migration | Сессия закрывает сама, список ниже; владелец вычёркивает несогласное |
| D5 | Папка vault | `git mv job_hunt_ai_vault vault`; раскладка по `index.md` §1 |
| D6 | Запрет 2026-09-07 на правку CLAUDE.md и хуков | Снят на ветке `migration`: старые хуки, skills, агенты и CLAUDE.md заменяются, каждый с вердиктом keep/remove/rework |
| D7 | Старые rules/ (35) | Архив по умолчанию; исключения аргументируются в Case |
| D8 | Нарезка | Слайсами, каждый слайс — свой Plan Mode и своё одобрение |

Эти восемь строк становятся первыми `- decision[...]` линиями в `raw/2026-09-09/ledger.md`,
написанными вручную (ledger-хука ещё нет — так велит `migration-plan.md` Phase 1 п. 4).

## Противоречия в docs/migration, закрытые сессией (D4)

Правило выбора: схема категории и `index.md` старше glossary; более поздняя и подробная
формулировка побеждает.

| # | Где | Принято |
|---|---|---|
| C1 | glossary даёт две модели статусов Lesson | `new / clustered / archived` (lesson-schema). `reviewed`, `actioned` для Lesson не существуют |
| C2 | glossary даёт две модели статусов Insight | `open / actioned / archived` |
| C3 | «Restoring is an update back to `current`» vs «back to `draft`/`built`» | Для Entity/Rule — `draft`/`built` (index §3). `current` — статус только Decision |
| C4 | Librarian «читает ledger, spec, plan» и тут же «только handoff, materialize.yaml, indexes» | Только `handoff.md`, `materialize.yaml`, индексы категорий (index §10). Raw-артефакты открываются лишь когда скрипт сообщил о проблеме |
| C5 | `hook_ref` (glossary) vs `implementation_ref` (rule-schema) | `implementation_ref` |
| C6 | README ссылается на `index.md`, `glossary.md`, `moc/`, `superseded/` | Файлы переименовываются при переносе в vault: `index-5.md` → `wiki/index.md`, `glossary-2.md` → `wiki/glossary.md`. Черновики `rule-*.md` остаются в `docs/migration/` до превращения в страницы. `superseded/` нет и не создаётся |
| C7 | `rule-ledger-write` «слушает вывод агента и блокирует» | Хук на событии `Stop`, а не `MessageDisplay`. `Stop` получает транскрипт и последнее сообщение, может блокировать с причиной, которую видит модель. `MessageDisplay` не может ни говорить, ни блокировать — измерено 2026-08-29, lesson в старом vault |
| C8 | Кто пишет «был ли `/hi`» в event log | Сам skill `/hi` через `!`-подстановку (`uv run guppi event hi`). Пользовательский вызов `/hi` не проходит через `Skill`-tool, хук его не увидит |
| C9 | Spec = одобрение плана, но файл плана лежит вне репозитория | Одобренный план копируется в `raw/<date>/spec.md`. В Slice 0–1 вручную, позже — хуком `rule-branch-commit` (PostToolUse ExitPlanMode) |
| C10 | `origin: raw/…/ledger.md#case-N` — в markdown нет такого якоря | Соглашение: `#case-N` означает строку ledger с `[case N]`. Ищется grep'ом; lint проверяет существование строки |
| C11 | `sprint` — какой id у миграции | `sprint: migration` на всех страницах, созданных до закрытия миграции |
| C12 | Старые rule-страницы с инструментом (например, no-quantity в заголовке) | Становятся Rule со `enforcement: check`, `implementation_ref` → lint-проверка. Без инструмента — архив (D7) |
| C13 | Schema — `schema.yaml` (index §1) или prose-документ `*-schema.md` (migration-plan «permanent set») | Оба: `wiki/<cat>/schema.yaml` — машинная часть (поля, required, values, секции body), читается lint'ом; `wiki/<cat>/schema.md` — проза с примерами. Lint сверяет таблицу полей в `.md` с `.yaml`, чтобы два источника не расходились |
| C14 | `decisions/` возвращается как папка после того, как 218 решений запарковали за стоимость чтения | Возвращается. Без `decisions.index`, ничем не сканируется, читается только по `origin`. Это не противоречит парковке: парковали чтение в `/pre-task`, а не существование |

## Раскладка после Slice 0

```
vault/
  raw/
    2026-09-09/            ledger.md, spec.md (копия одобренного плана), handoff.md
    notes/                 две заметки владельца от 2026-08-13 — как были
    handoffs/ plans/ specs/   пустые, удаляются (.gitkeep) — новая модель их не знает
  wiki/
    index.md  glossary.md  case-schema.md   ← из docs/migration, с правками C1–C14
    brief.md  sprint.md  tags.md  log.md    ← новые, короткие
    decisions/ schema.yaml schema.md
    entities/  schema.yaml schema.md
    rules/     schema.yaml schema.md
    estimates/ schema.yaml schema.md
    lessons/   schema.yaml schema.md
    insights/  schema.yaml schema.md
    archive/                               пусто
  parked/
    2026-09-07/  decisions/ concepts/ entities/ rules/   ← сегодняшний parked/, переименован
    2026-09-09/  entities/ rules/ lessons/ proposals/    ← четыре живые папки старого wiki/
                 registers/  index.md tags.md authority.md log.md sprint.md brief.md
                             CLAUDE.md pages.base
  archive/                                 старый архив, 505 файлов — не трогаем (длинные пути)
docs/
  harness-map-2026-09-07.md                ← из vault/harness-map.md
  migration/  README.md migration-plan.md rule-*.md (7)   ← остаются до конца миграции
  superpowers/ HANDOFF.md и прочее          ← не трогаем в Slice 0
guppi/                                     Python-пакет, появляется в Slice 1
```

Индексы `wiki/<cat>.index` появляются в Slice 2 вместе с lint'ом.

## Дорожная карта слайсов

Каждый слайс — отдельный Plan Mode, отдельное одобрение, отдельный `raw/<date>/spec.md`.
Ledger пишется вручную до Slice 1, далее хуком.

| Слайс | Что строится | Rule-страницы, которые его описывают |
|---|---|---|
| **0** | Ветка, раскладка, схемы, index/glossary/case-schema в vault, CLAUDE.md bootstrap, settings.json без старых хуков, удаление старого harness'а, ledger вручную, brief | нет — это подготовка |
| **1** | Пакет `guppi/` (CLI `uv run guppi …`): `event` (event_log), `ledger` (Stop-хук), `/hi` skill, CLAUDE.md с `@import` glossary и case-schema | `rule-session-start` MOC: `rule-skill-hi` (+3 детей), `rule-event-log`, `rule-ledger-write`; `rule-case-protocol` |
| **2** | `guppi render` (renderer full/partial), `guppi lint` (refs, schema, orphans, cascade `built`, slug collisions, no-quantity), `guppi index`, `/ask` skill, `pre-task` skill + хук | `rule-plan-mode` MOC: `rule-ask`, `rule-pretask-hook`, `rule-pretask`; `rule-renderer` |
| **3** | `guppi materialize`, `guppi generate`, `guppi cleanup`, агент `librarian-guppi`, `/retro`, `/handoff`, хуки retro-commit и harness-tests, `to-executable-plan`, `subagent-guppi` | `rule-work-mode`, `rule-end-of-work`, `rule-documentation`, `rule-subagent-guppi` |
| **4** | Phase 2: конверсия старых страниц группами — entities (44), rules (35, архив по умолчанию), lessons (31 → новая схема). Proposals остаются в parked | по группам, Case на группу |
| **5** | Phase 3 и закрытие: судьба `parked/` и старого `archive/`, удаление `docs/migration/`, merge `migration` → `main` | — |

Порядок 1 → 2 → 3 диктуется зависимостями: renderer нужен, чтобы rule-страницы Slice 1
перестали жить в двух копиях; librarian нужен только когда есть что материализовать.
Rule-страницы Slice 1 пишутся руками в Slice 1 и перерендериваются в Slice 2 — это единственное
место, где две копии живут одну сессию.

## Вердикты по старому harness'у (D6, одна таблица — одна ратификация)

| Старый механизм | Вердикт | Куда уходит |
|---|---|---|
| `session-brief.ps1` | rework | `/hi` skill + `rule-event-log` (Slice 1) |
| `catch-the-feedback.ps1` (MessageDisplay) | rework | `rule-ledger-write` на `Stop` (Slice 1); идея «хук снимает fenced-блоки из ответа» сохраняется |
| `pre-task-ledger.tsv`, `pre-task-state.ps1`, `record-the-dispatch.ps1`, `record-the-smoke.ps1` | rework | `event_log.md` (Slice 1) |
| `check-the-plan.ps1` | rework | `rule-pretask-hook`, advisory (Slice 2) |
| `pre-task` agent, `/vault-ask`, `vault-catalogue.sh`, `vault-authority.sh` | rework | `/ask` над индексами + `pre-task` skill (Slice 2) |
| `vault-inject.sh` | rework | `guppi render` (Slice 2) |
| `vault-check.sh` + selftest | rework | `guppi lint` + pytest (Slice 2) |
| `vault-archive.sh` | rework | `guppi cleanup` (Slice 3) |
| `vault-librarian`, `/ingest`, `vault-units.sh`, `vault-coverage.sh` | rework | `librarian-guppi` + `materialize`/`generate` (Slice 3) |
| `/retro`, `/handoff`, `gate-the-handoff.ps1`, `remind-the-smoke.ps1`, шаблоны | rework | `rule-retro`, `rule-handoff`, `rule-retro-commit`, `rule-harness-tests` (Slice 3) |
| `session-dialogue.py` + selftest | remove | Retro новой модели не читает транскрипт |
| `serve-the-rule.ps1`, `ask-the-vault.ps1`, `remind-the-feedback.ps1`, `lock-the-librarian.ps1`, `check-the-journal.ps1`, `vault-path.ps1` | remove | нет аналога в модели; `authority`, VAULT-FEEDBACK и smoke-gate уходят вместе с ними |
| `/sprint`, `/vault-lint`, `decisions-agent`, `lessons-agent`, `lessons-queue.py`, `build-families-*.py`, `vault-measure.py` + selftest, `hook-selftest.ps1` | remove | sprint пишет librarian; lint — скрипт; lessons кластеризует librarian |
| `/grill-me` | keep | не в модели, но живой и безвредный; решение о нём — позже |
| `Makefile` | rework | `help`, `style`, `lint` (Slice 2), `test` (Slice 2) |
| `CLAUDE.md` (корень), `job_hunt_ai_vault/CLAUDE.md` | rework / remove | корень — bootstrap в Slice 0, render из `rule-case-protocol` в Slice 2; vault'овский уходит в parked |
| `docs/vault-cleanup-*.md`, `docs/who-reads-the-vault.md`, `docs/2026-08-3*.md`, `docs/HANDOFF.md`, `docs/superpowers/` | оставить как есть | история; судьба решается в Slice 5 |

## Slice 0 — исполняемые шаги

Все шаги на ветке `migration`, один коммит на шаг или на группу шагов. `main` и тег
`vault-v1` не трогаются.

1. **Ветка.** `git checkout -b migration`.

2. **Переименование vault.** `git mv job_hunt_ai_vault vault`. Проверить, что `.obsidian/` в
   gitignore (есть) — Obsidian нужно открыть заново как `vault/`.

3. **Парковка старого содержимого.**
   - `git mv vault/parked vault/parked-tmp && mkdir vault/parked && git mv vault/parked-tmp vault/parked/2026-09-07`
   - `mkdir vault/parked/2026-09-09`; `git mv vault/wiki/{entities,rules,lessons,proposals} vault/parked/2026-09-09/`
   - `mkdir vault/parked/2026-09-09/registers`; `git mv` туда `index.md tags.md authority.md log.md sprint.md brief.md CLAUDE.md pages.base` из `vault/`
   - `git mv vault/harness-map.md docs/harness-map-2026-09-07.md`
   - `git rm vault/raw/{handoffs,plans,specs}/.gitkeep`
   - `vault/archive/` не трогать (пути до 258 символов; `core.longpaths` уже `true`, но лишние 18 символов не нужны).

4. **Новый wiki/.** Создать папки `decisions entities rules estimates lessons insights archive`.
   `git mv docs/migration/index-5.md vault/wiki/index.md`, `glossary-2.md → glossary.md`,
   `case-schema.md → case-schema.md`. Внести правки C1–C14 в эти три файла (только там, где
   текст противоречит; не переписывать стиль). `git mv docs/migration/<cat>-schema.md vault/wiki/<cat>/schema.md`.

5. **`schema.yaml` × 6.** Формат:
   ```yaml
   type: entity
   properties:
     required: [type, kind, purpose, status, estimates, origin, sprint, created, tags]
     optional: [parent, children, code_ref]
     values:
       kind: [MOC, Leaf]
       status: [draft, built, archived]
   body:
     required: ["## Purpose", "## Estimates", "## History"]
     optional: ["## How it works", "## Children", "## Parent", "## Code"]
   ```
   Поля и значения — из таблиц `schema.md`, один в один. Rule получает `enforcement`,
   `implementation_ref`, `governs`, `render_mode`; Estimate — `target`; Lesson — `root_cause`,
   `source`, `insight`; Insight — `pattern`, `children`, `severity`, `addressed_by`; Decision —
   `target_category`, `target_slug`, `ref`, `source`, `supersedes`, `superseded_by`. Условные
   требования (например, `governs` только при `render`) — в `conditional:` блоке, который lint
   в Slice 2 научится читать.

6. **Регистры.** `wiki/tags.md` — заголовок и пустая таблица `tag | meaning | aliases (ru)`;
   `wiki/log.md` — заголовок; `wiki/sprint.md` — sprint `migration`, цель «репозиторий работает
   по модели index.md, Phase 1 и 2 закрыты», критерии — семь пунктов из «Definition of done»
   `migration-plan.md`; `wiki/brief.md` — написан вручную: что сделано в Slice 0, что следующий
   слайс строит, что deferred.

7. **`raw/2026-09-09/`.** `ledger.md` — восемь строк D1–D8 в формате
   `- decision[case N][kind][slug]{ref}` (kind: `update` для D4–D8 над Rule-class файлами,
   `delete` для старого harness'а, `create` для ветки/раскладки — по одной строке на решение;
   точные slug'и пишутся при исполнении и попадают в коммит). `spec.md` — копия этого плана.
   `handoff.md` — три раздела по модели: notes, instructions to the librarian, what got done.

8. **Старый harness — удаление.** `git rm -r .claude/hooks .claude/agents .claude/templates
   scripts .superpowers`, skills `retro handoff ingest sprint vault-lint vault-ask`. Оставить
   `.claude/skills/grill-me`. `.claude/settings.json` → `{"permissions": {"defaultMode": "plan"}}`.
   `Makefile` → только `help` и `style` (`uv run ruff check guppi tests` — папки появятся в
   Slice 1; до того `style` проходит на пустом наборе). `pyproject.toml`: `name = "guppi"`,
   описание, `[project.scripts] guppi = "guppi.cli:main"` добавляется в Slice 1.

9. **`CLAUDE.md` bootstrap** (корень, ~40 строк, английский): что такое GUPPI; vault в
   `vault/`, карта в `vault/wiki/index.md`, `@vault/wiki/glossary.md`,
   `@vault/wiki/case-schema.md`; правило §0 index'а (ничего не меняется без ратифицированного
   Decision); язык (английский в репозитории, русский с владельцем, план для владельца —
   русский); статус миграции: ритуал старой модели не действует, ledger пишется вручную до
   Slice 1, следующий слайс — по `vault/wiki/brief.md`; `docs/migration/README.md` как порядок
   чтения.

10. **Коммиты.** Шаги 1–3 одним коммитом (перенос), 4–7 вторым (новый vault), 8–9 третьим
    (harness). Сообщения на английском, с трейлером Co-Authored-By.

### Что Slice 0 не делает

- Не пишет Python. Ни одного хука, ни одного скрипта.
- Не создаёт ни одной страницы в `wiki/<cat>/` — первые страницы (Rule-страницы Slice 1 и
  Decision-страницы D1–D8) появляются, когда есть чем их проверить.
- Не трогает `vault/archive/`, `docs/superpowers/`, старые заметки в `raw/notes/`.

## Проверка Slice 0

- `git status` чист после трёх коммитов; `git log --oneline main..migration` показывает три.
- `find vault/wiki -type f | sort` даёт ровно: 3 верхних файла + 4 регистра + 6×2 схем = 19.
- `find vault/wiki -name '*.md' | xargs grep -l 'hook_ref\|reviewed\|superseded/'` — пусто.
- `ls .claude/hooks` — папки нет; `.claude/settings.json` не содержит `hooks`.
- `uv run ruff check .` — чисто (нет Python).
- Следующая сессия открывается без вывода старых хуков; `CLAUDE.md` раскрывает `@import`
  glossary и case-schema (видно по системному промпту: термины «Case», «Ledger» на месте без
  чтения файлов).
- Obsidian открывает `vault/` и видит `wiki/`, `parked/`, `archive/`, `raw/`.

## Что deferred из этого плана (попадает в brief.md)

- Судьба `/grill-me` — keep без страницы; решить при Slice 3 (retro) или Slice 5.
- Рендер `.claude/settings.json` из Rule-страницы (`rule-hook-registry`, `render: full`) —
  кандидат, решить в Slice 2, когда есть renderer.
- Верификация payload'а `Stop`-хука (поле `last_assistant_message` vs чтение транскрипта) —
  пробой в Slice 1, как учит старый lesson о probe-хуках.
- Проверка, что `PostToolUse ExitPlanMode` получает текст плана (нужно для C9 хуком) — Slice 2.
