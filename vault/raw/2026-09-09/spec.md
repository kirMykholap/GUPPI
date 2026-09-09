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


---

# GUPPI — Slice 1: ledger, event log, `/hi`

Spec слайса. Собирается из ратифицированных Case по одному; после одобрения копируется
в `vault/raw/2026-09-09/spec.md` (второй документ в том же файле — Slice 0 прошёл тем же
днём, папка одна, нумерация case продолжается с 9).

## Frontier (2026-09-09, вторая сессия дня)

Источники: `brief.md`, `sprint.md`, `docs/migration/rule-session-start.md`, roadmap в
`raw/2026-09-09/spec.md`. Ветка `migration`, дерево чистое, `main..migration` — три коммита.

**Задачи слайса** (brief, п. 1–6), по одному Case на механизм (D1):

| Case | Механизм | Страницы в `then` |
|---|---|---|
| 9 | пакет `guppi/` + `guppi event` (event log) | `rule-event-log` + Estimate |
| 10 | `guppi ledger` — `Stop`-хук, с пробой payload'а | `rule-ledger-write` + Estimate |
| 11 | skill `/hi` | `rule-skill-hi` (MOC) + 3 детей + 4 Estimate |
| 12 | MOC фазы | `rule-session-start` + Estimate |
| 13 | секция Case protocol в `CLAUDE.md` | `rule-case-protocol` + Estimate |

**Проблемы, найденные при подготовке** (решаются в Case 11, если владелец не вынесет
отдельно):

- `origin` этого репозитория — `c:/PROJECTS/job hunt ai`, репозиторий продукта, от которого
  vault отделили 2026-09-07. У ветки `migration` нет upstream. `git pull` внутри `/hi`
  либо упадёт («no tracking information»), либо, если upstream поставить, потянет продукт.
- `gh` не залогинен (`gh auth status` → not logged in). `gh issue list` в `/hi` упадёт.

**Отложенное, перенесено из brief** (не для этого слайса, кроме первого пункта):

- Проверка `PostToolUse ExitPlanMode` (несёт ли текст плана, C9) — brief относит к Slice 2,
  но проба `Stop` в Case 10 уже регистрирует throwaway-хук; регистрация второго стоит одну
  строку. Предлагаю снять оба показания в одной пробе.
- `/grill-me` без страницы — Slice 3 или 5.
- Рендер `settings.json` из `rule-hook-registry` — Slice 2.
- Судьба `parked/`, `archive/`, `docs/superpowers/`, `docs/HANDOFF.md` — Slice 5.

**Известное ложное, остаётся:** `docs/migration/rule-*.md` с `TBD` в полях — черновики;
`rule-case-protocol` получит `parent: rule-plan-mode`, страницы которого до Slice 2 нет.

---

## Case 9 — `rule-event-log`: пакет `guppi/` и `guppi event`

**context.** Event log — шумная запись сессии: старты, вызовы инструментов, диспатчи,
коммиты, прогоны тестов. Пишется хуками, не инструкциями, поэтому фиксирует и отклонения
агента. Не коммитится. Это первый механизм слайса, и вместе с ним рождается пакет `guppi/`,
в котором живут все хуки и скрипты модели (D3).

**now.** Python в репозитории нет. `pyproject.toml` объявляет пакет `guppi`, зависимость
`pyyaml`, dev-группу с `ruff`; `[project.scripts]` не задан (Slice 0 отложил на Slice 1).
`.claude/settings.json` — только `defaultMode: plan`, хуков нет. `.gitignore` не знает
`event_log.md`. Старый аналог — `pre-task-ledger.tsv` и четыре хука на PowerShell —
удалён в Slice 0 с вердиктом rework. Два урока старого vault держат: хук всегда получает
payload на stdin, и мерить его надо через pipe; процесс, читающий stdin, вешается при
фоновом запуске — каждый вызов в Makefile закрывает stdin. `tags.md` пуст: любой тег
здесь — новый. `wiki/` не содержит страниц, pre-task по индексам невозможен (индексов
нет); проверено чтением `wiki/` и `parked/` — дубликатов нет.

**problem.** Три решения: (а) форма пакета и тестов — в частности pytest как новая
dev-зависимость; (б) контракт event log — путь, формат строки, какие события; (в) как
скилл `/hi` оставляет свою отметку без session id, и как `Stop`-хук потом её находит.

**recommend.**

(а) `guppi/` — пакет на stdlib + pyyaml: `guppi/cli.py` (`main`, argparse, субкоманды),
`guppi/event.py`, позже `ledger.py`. `[project.scripts] guppi = "guppi.cli:main"`, вызов
всюду `uv run guppi …`. Тесты в `tests/` на **pytest**: roadmap в spec.md уже называет
«`guppi lint` + pytest», brief — «the pytest suite beside it»; это одна dev-зависимость
рядом с `ruff`, runtime-зависимостей не прибавляется. `Makefile` получает `test`
(`uv run pytest -q < /dev/null`); `style` остаётся `ruff check .`.

(б) `guppi event <name> [detail]`. Читает JSON хука со stdin, если он есть (не tty, не
пуст): берёт `session_id`, `hook_event_name`, `tool_name`, для `Bash` — первые 80 символов
`command`, для `Agent`/`Skill` — тип агента или имя скилла. Дописывает одну строку в
`vault/raw/<сегодня>/event_log.md`, создавая папку и файл:

```
- 15:02:11 a1b2c3d4 session-start startup
- 15:02:40 -------- hi
- 15:03:05 a1b2c3d4 tool Bash: git status --short
- 15:04:12 a1b2c3d4 tool Agent: Explore
```

Формат: `- HH:MM:SS <8 знаков session_id | -------- > <event> <detail>`. Никогда не
роняет сессию: любая ошибка — в stderr, exit 0. Регистрация в `settings.json`:
`SessionStart` → `uv run guppi event session-start`; `PostToolUse` без matcher'а →
`uv run guppi event tool`. Пишутся все вызовы инструментов, не только Bash/Agent: это
запись для отладки, и фильтр — лишнее решение, которое потом придётся менять.
`.gitignore` получает `vault/raw/*/event_log.md`.

(в) `/hi` пишет `hi` через `!`-подстановку `uv run guppi event hi` — там нет payload'а,
session id неизвестен, в строке `--------`. `Stop`-хук (Case 10) считает сессию рабочей,
если в сегодняшнем `event_log.md` после **последней** строки `session-start` с его
session_id есть строка `hi`, и между ними нет `session-start` другой сессии. Две
одновременные сессии в одном репозитории этот способ не различает — фиксируется в
`How it works` как известное ограничение. Проба Case 10 заодно проверит, доступна ли
`$CLAUDE_SESSION_ID` внутри `!`-подстановки; если да, `hi` получит настоящий id и
ограничение снимается.

**then.**

```
slug: rule-event-log
type: rule
kind: Leaf
purpose: Prevents the ledger from being written into a session nothing recorded
enforcement: hook
implementation_ref: [guppi/event.py, guppi/cli.py, .claude/settings.json]
parent: rule-session-start
sprint: migration
tags: [session, hooks, harness]        # все три — новые, tags.md пуст
estimate:
  slug: estimate-event-log-records
  kind: QA
  criterion: >
    After a session starts and one tool call completes, raw/<date>/event_log.md carries a
    `session-start` line with this session's id and a `tool` line after it; after `/hi`
    it carries a `hi` line; `git check-ignore` reports the file ignored; and a hook
    invocation with piped stdin exits 0 and finishes under 2 s.
  method: >
    pytest in tests/test_event.py drives guppi.event with piped JSON payloads against a
    temp vault; the git-ignore and timing readings are taken once by hand, through a pipe,
    and written into the estimate line.
```

Код: `guppi/__init__.py`, `guppi/cli.py`, `guppi/event.py`, `tests/test_event.py`,
правки `pyproject.toml` (scripts, pytest в dev), `Makefile` (`test`), `.gitignore`,
`.claude/settings.json` (два хука).

Ledger:
```
- decision[case 9][create][rule-event-log]{ref:rule-session-start}
- decision[case 9][create][estimate-event-log-records]{ref:rule-event-log}
```

**ratification.** Ратифицирован владельцем 2026-09-09, как предложено.

---

## Case 10 — `rule-ledger-write`: `guppi ledger`, хук на `Stop`

**context.** Хук, который снимает `- decision[...]`, `- estimate[...]` и `- lesson[...]`
строки из только что законченного ответа и дописывает их в `raw/<date>/ledger.md`
дословно, ничего не интерпретируя. Отказывает с причиной, если сессия не рабочая
(Case 9, пункт в). Это механизм, ради которого «ledger пишется вручную до Slice 1».

**now.** Хука нет; ledger сегодняшнего дня — девять строк руками (Slice 0). Старый
`catch-the-feedback.ps1` на `MessageDisplay` снимал fenced-блоки из ответа — удалён с
вердиктом rework, идея «хук снимает строки из ответа» сохранена. Урок 2026-08-29:
`MessageDisplay` не может ни говорить, ни блокировать; C7 переносит хук на `Stop`.
Документация (справка read-only агента по docs) говорит, что `Stop` получает
`session_id`, `hook_event_name`, `last_assistant_message`, `permission_mode`, блокирует
через exit 2 + stderr; видит ли модель причину, и есть ли `stop_hook_active` — не
задокументировано. Brief велит не верить, а пробовать. Формат строк — index §4 и
case-schema.

**problem.** (а) откуда брать текст ответа; (б) какие строки считаются — в частности,
строки внутри fenced-блока: Case показывает будущие ledger-строки в `then` **до**
ратификации, и хук, снявший их с этого же ответа, записал бы нератифицированное;
(в) что делать без `/hi`; (г) повторный запуск хука на том же ответе; (д) первая проба.

**recommend.**

(д) сначала — **проба**, первый шаг Work Mode: throwaway-команда `guppi probe`,
зарегистрированная на `Stop` и на `PostToolUse` с matcher `ExitPlanMode`, пишет сырой
stdin в `vault/raw/2026-09-09/probe-<event>-<n>.json`; в тело `/hi`-заглушки временно
кладётся `!`-подстановка `echo $CLAUDE_SESSION_ID`. Снимается за одну новую сессию (хуки
читаются при старте — тоже показание пробы). Показания идут в ledger как
`- lesson[knowledge][lesson-hooks-stop-payload] trigger: … root_cause: …` (и второй
lesson для `ExitPlanMode`), проба и её файлы удаляются в том же коммите. Ветка кода,
которую проба не подтвердила, не пишется.

(а) текст — `last_assistant_message`; если проба покажет только `transcript_path`,
читается последняя assistant-запись транскрипта. Пишется одна ветка, не обе.

(б) считается строка, которая начинается с `- decision[`, `- estimate[` или
`- lesson[` в нулевой колонке **и не лежит внутри fenced-блока**. Правило для агента,
войдёт в `rule-case-protocol` (Case 13): в fence — предпросмотр, голой строкой — запись;
голую строку агент пишет только в ответе, который признаёт ратификацию.

(в) строки есть, `/hi` не записан → exit 2, stderr:
`ledger: 2 line(s) not written — no /hi recorded for session a1b2c3d4. Tell the person; run /hi, then repeat the lines.`
Строк нет → exit 0, ledger не трогается (создаётся лениво, при первой строке).

(г) `stop_hook_active: true` (повторный Stop после блокировки) → exit 0, ничего не
пишет и не блокирует, чтобы не зациклиться. Дополнительно строка, дословно уже
присутствующая в сегодняшнем ledger, не дописывается второй раз — это покрывает и
повтор хука, и агента, повторившего строку в следующем ответе.

Папка — `raw/<сегодня>/`, та же, что у event log. Регистрация: `Stop` →
`uv run guppi ledger`, timeout 30 с. Строки Case 9–13 этой сессии пишутся руками при
ратификации (хука ещё нет); всё, что родится в Work Mode после запуска хука — строки
`estimate[...]` с результатами и `lesson[...]` пробы — пишет хук. Это репетиция пункта 5
Definition of done.

**then.**

```
slug: rule-ledger-write
type: rule
kind: Leaf
purpose: Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened
enforcement: hook
implementation_ref: [guppi/ledger.py, .claude/settings.json]
parent: rule-session-start
sprint: migration
tags: [session, hooks, harness, ledger]        # ledger — новый тег
estimate:
  slug: estimate-ledger-write-lifts
  kind: QA
  criterion: >
    Given a Stop payload whose reply carries one bare decision line, the same line inside a
    fence, and one bare estimate line, with a `hi` recorded for the session: the ledger
    gains exactly the two bare lines, verbatim, once, even when the hook runs twice on the
    same payload. Without `hi` the hook exits 2 with a reason naming the count and the
    session, and the ledger is untouched. With `stop_hook_active` true it exits 0 and
    writes nothing. In a live session, the last lines of this slice reach
    raw/2026-09-09/ledger.md written by the hook, not by hand.
  method: >
    pytest in tests/test_ledger.py with piped payloads against a temp vault; the live
    reading is taken once by hand and written into the estimate line.
```

Код: `guppi/ledger.py`, `guppi/probe.py` (временно), `tests/test_ledger.py`,
`.claude/settings.json` (хук `Stop`).

Ledger:
```
- decision[case 10][create][rule-ledger-write]{ref:rule-session-start}
- decision[case 10][create][estimate-ledger-write-lifts]{ref:rule-ledger-write}
```

**ratification.** Ратифицирован владельцем 2026-09-09, как предложено.

---

## Case 11 — `rule-skill-hi`: skill `/hi` и три его секции

**context.** `/hi` открывает рабочую сессию. Bash-подстановки в теле скилла исполняются
до первого хода агента, поэтому sprint, brief, git-состояние и issues просто присутствуют
в контексте — нет шага, который агент мог бы забыть. Скилл сам оставляет отметку `hi` в
event log (C8). Без `/hi` сессия обычная: ничего не загружено, ledger не пишется.

**now.** Скилла нет; `.claude/skills/` содержит только `grill-me`. Старый
`session-brief.ps1` (SessionStart, печатал brief) удалён с вердиктом rework. Черновик
`docs/migration/rule-session-start.md` задаёт структуру: MOC `rule-skill-hi`
(`render: full`) и три Leaf с `render: partial` — internal context, git context, github
issues; разбиение обосновано там же (четыре `@`-импорта падают одинаково — один Leaf;
`git pull` и `gh issue list` падают по-разному — отдельные). До Slice 2 renderer'а нет:
файл скилла и страницы правил — две копии на одну сессию, brief это принимает.
Два факта среды, которых черновик не знал: `origin` → `c:/PROJECTS/job hunt ai`
(репозиторий продукта), у `migration` нет upstream; `gh` не залогинен.

**problem.** (а) текст скилла — он же тело четырёх страниц; (б) `git pull` в `/hi` при
таком `origin`; (в) `gh issue list` без авторизации; (г) Estimates на каждую страницу.

**recommend.**

(а) Файл `.claude/skills/hi/SKILL.md`, frontmatter `name: hi`,
`disable-model-invocation: true` (вызывает только человек — иначе агент мог бы «открыть»
сессию сам). Тело — рендер MOC с маркерами трёх детей:

```markdown
---
name: hi
description: Open a working session — sprint, brief, git state, open issues, then the Frontier.
disable-model-invocation: true
---
<!-- rule-skill-hi -->
Recorded: !`uv run guppi event hi --session "${CLAUDE_SESSION_ID:-}"`

<!-- rule-internal-context -->
@vault/wiki/sprint.md
@vault/wiki/brief.md
<!-- /rule-internal-context -->

<!-- rule-git-context -->
Pull: !`git pull --ff-only 2>&1 || true`
Branch: !`git branch --show-current`
Status: !`git status --short`
<!-- /rule-git-context -->

<!-- rule-github-issues -->
Open issues: !`gh issue list --limit 5 2>&1 || true`
<!-- /rule-github-issues -->

Assemble the Frontier from the above and present it as a list: tasks, problems, debt
carried over, where the sprint stands; on a plan branch the unfinished plan comes first.
A failed pull or an unavailable `gh` is an item on that list, not a reason to stop. Wait
for the human to pick the order or defer items. Before any `create`, ask the vault first
(§3 of `vault/wiki/index.md`).
<!-- /rule-skill-hi -->
```

`${CLAUDE_SESSION_ID:-}` — если проба Case 10 покажет переменную, `hi` получит настоящий
id; если нет — пустая строка, `--------`, текст скилла не меняется.

(б) `git pull --ff-only` остаётся в скилле: правило «pull здесь и только здесь» — про
место, не про сегодняшний remote. Падение печатается в контекст и становится пунктом
Frontier. Сам `origin` — вопрос владельцу (11.1): оставить как есть до Slice 5 (merge в
`main`), или снять/переназначить сейчас. Рекомендую оставить: репозиторий сейчас
локальный, а `git pull` с `|| true` безвреден.

(в) `gh issue list` остаётся; без авторизации в контекст попадает `gh`'s own message.
Вопрос владельцу (11.2): логиниться ли в `gh` для этого репозитория (нужен GitHub-remote,
которого нет). Рекомендую: не сейчас; правило страницы — «список или названная причина
его отсутствия».

(г) Четыре Estimate, все QA, метод — ручное показание при старте сессии, записанное в
строку `estimate[...]`; автоматической проверки у markdown-скилла нет до Slice 2.

**then.**

```
slug: rule-skill-hi
type: rule
kind: MOC
purpose: Prevents a session from being loaded piecemeal by read-tool calls
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: full
parent: rule-session-start
children: [rule-internal-context, rule-git-context, rule-github-issues]   # порядок — содержание
sprint: migration
tags: [session, harness]
estimate:
  slug: estimate-hi-no-read-calls
  kind: QA
  criterion: >
    After /hi the context holds sprint.md, brief.md, the current branch, git status and the
    issue list (or gh's message) with no read-tool call having occurred, and
    raw/<date>/event_log.md carries a `hi` line.
  method: one reading at a session start, by hand, recorded in the estimate line

slug: rule-internal-context
type: rule
kind: Leaf
purpose: Prevents work starting without the current sprint and the previous session's handover
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: rule-skill-hi
sprint: migration
tags: [session, harness]
estimate:
  slug: estimate-internal-context-loaded
  kind: QA
  criterion: the text of sprint.md and brief.md is present in the first turn's context
  method: one reading at a session start, by hand

slug: rule-git-context
type: rule
kind: Leaf
purpose: Prevents a session from starting on a branch it does not know, or pulling mid-session
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: rule-skill-hi
sprint: migration
tags: [session, harness, git]          # git — новый тег
estimate:
  slug: estimate-git-context-current
  kind: QA
  criterion: >
    branch and short status are in context; a failing pull shows its message there and the
    skill still completes; no pull happens later in the session
  method: one reading at a session start, by hand, on the current remote

slug: rule-github-issues
type: rule
kind: Leaf
purpose: Prevents deferred bugs, tracked outside the vault, from being forgotten at session start
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: rule-skill-hi
sprint: migration
tags: [session, harness, github]       # github — новый тег
estimate:
  slug: estimate-github-issues-listed
  kind: QA
  criterion: >
    the open-issue list, or gh's own message naming why there is none, is in context and
    the skill completes either way
  method: one reading at a session start, by hand, in the current gh state
```

Код: `.claude/skills/hi/SKILL.md`; страницы `vault/wiki/rules/rule-skill-hi.md`,
`rule-internal-context.md`, `rule-git-context.md`, `rule-github-issues.md`; четыре
страницы в `vault/wiki/estimates/`.

Ledger:
```
- decision[case 11][create][rule-skill-hi]{ref:rule-session-start}
- decision[case 11][create][estimate-hi-no-read-calls]{ref:rule-skill-hi}
- decision[case 11][create][rule-internal-context]{ref:rule-skill-hi}
- decision[case 11][create][estimate-internal-context-loaded]{ref:rule-internal-context}
- decision[case 11][create][rule-git-context]{ref:rule-skill-hi}
- decision[case 11][create][estimate-git-context-current]{ref:rule-git-context}
- decision[case 11][create][rule-github-issues]{ref:rule-skill-hi}
- decision[case 11][create][estimate-github-issues-listed]{ref:rule-github-issues}
```

**ratification.** Ратифицирован владельцем 2026-09-09, как предложено. 11.1: `origin`
остаётся как есть до Slice 5. 11.2: в `gh` не логинимся; Estimate снимается по ветке
«причина названа».

---

## Case 12 — `rule-session-start`: MOC фазы Session Start

**context.** Родитель трёх механизмов, ратифицированных в Case 9–11. Rule MOC: порядок
детей — содержание. Не рендерится (это не файл harness'а, а описание фазы), поэтому
`enforcement` нет; сила — в детях.

**now.** Черновик `docs/migration/rule-session-start.md` целиком, с `TBD` в `origin`,
`sprint`, `created`. Его секция `## The Frontier` не входит в список секций
`rules/schema.yaml` — переносится в `## How it works`. Родителя у MOC фазы нет (верхний
уровень). `estimates: [estimate-session-start-context]` — уже назван черновиком.

**problem.** Только сквозная проверка: что именно измеряет Estimate MOC, чего не
измеряют Estimates детей. Дети проверяют, что каждый механизм работает; MOC — что
различение «обычная / рабочая сессия» держится насквозь.

**recommend.** Страница — черновик с реальными значениями, Frontier внутри
`## How it works`. Estimate — два показания, два запуска: обычная сессия (без `/hi`), в
которой агент пишет голую `- decision[...]`-строку → строка не попадает в `ledger.md`, и
человек видит в ответе причину; рабочая сессия (после `/hi`) с той же строкой → строка в
`ledger.md`. Метод ручной, оба показания в строку `estimate[...]`.

**then.**

```
slug: rule-session-start
type: rule
kind: MOC
purpose: Prevents a working session from starting against unknown state
children: [rule-skill-hi, rule-event-log, rule-ledger-write]   # порядок — содержание
sprint: migration
tags: [session, workflow, hooks]       # workflow — новый тег
body: черновик docs/migration/rule-session-start.md, секции Purpose / How it works
      (включая The Frontier) / Children / Estimates / History
estimate:
  slug: estimate-session-start-context
  kind: QA
  criterion: >
    In a session opened without /hi, a bare `- decision[...]` line in a reply does not
    reach raw/<date>/ledger.md and the reply the person sees names the cause. In a session
    opened with /hi, the same line does reach it. Both readings taken end-to-end.
  method: two session starts, by hand, one reading each, recorded in the estimate line
```

Файлы: `vault/wiki/rules/rule-session-start.md`,
`vault/wiki/estimates/estimate-session-start-context.md`. Черновик в `docs/migration/`
остаётся до Slice 5 (spec C6).

Ledger:
```
- decision[case 12][create][rule-session-start]
- decision[case 12][create][estimate-session-start-context]{ref:rule-session-start}
```

**ratification.** Ратифицирован владельцем 2026-09-09, как предложено.

---

## Case 13 — `rule-case-protocol`: секция Case protocol в `CLAUDE.md`

**context.** Правило, которое агент видит всегда: как ведётся Case, когда он делится,
когда и как пишутся ledger-строки. Инструкция, не enforcement — хука на «закончил ли ты
Frontier» не бывает, поэтому текст стоит там, где агент его не пропустит: в `CLAUDE.md`.
Первый Leaf будущего `rule-plan-mode` (Slice 2), описан в `docs/migration/rule-plan-mode.md`
как ребёнок 1.

**now.** `CLAUDE.md` — bootstrap Slice 0: импортирует glossary и case-schema, несёт секцию
«Migration mode» с пунктом «ledger lines are written by hand … until the ledger hook
exists», который после Case 10 станет ложным. Шесть секций Case уже приходят через
`@vault/wiki/case-schema.md` — повторять их нельзя. Правило «fence — предпросмотр, голая
строка — запись» ратифицировано в Case 10 и ещё нигде не записано для агента. `/ask`
появится в Slice 2; до него «спросить vault» — чтение папок категорий.

**problem.** (а) текст секции; (б) правка «Migration mode» под появившийся хук;
(в) `parent: rule-plan-mode` указывает на страницу, которой нет до Slice 2.

**recommend.**

(а) Секция `## Case protocol` в `CLAUDE.md` между маркерами, ~20 строк, без повтора
case-schema:

```markdown
<!-- rule-case-protocol -->
## Case protocol

One reply is one Case, in the six sections of `case-schema.md`. Never move to the next
Case until this one is ratified or deferred. Plan Mode does not end while a Frontier item
is neither ratified nor deferred.

A follow-up question that asks you to justify a choice does not split the Case; one whose
answer needs a new choice does — into sub-cases `N.1`, `N.2`. Ratifying a parent does not
ratify its children.

Before a `create` without a `ref`, ask the vault first: does this exist, what conflicts,
what sits in `draft`, which tags fit. Put the answer in `now`. Use `/ask` once it exists;
until then read the category folders.

Ledger lines are written by the `Stop` hook, from the reply, verbatim. A line inside a
fenced block is a preview and is never written; a bare line at column zero is a record.
Write the bare `- decision[...]` lines only in the reply that acknowledges ratification;
`- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson
exists. Without `/hi` the hook refuses and says so: tell the person, do not retry.
<!-- /rule-case-protocol -->
```

(б) В «Migration mode» пункт про ledger заменяется на: «The ledger hook exists since
Slice 1; lines are emitted bare in the reply and the hook writes them. The nine lines of
2026-09-09 before it were written by hand, in the same format.» Остальные пункты секции
не меняются.

(в) `parent: rule-plan-mode` пишется как есть; brief этого слайса заносит висящую ссылку
в «Known false, and left so on purpose» до Slice 2. Альтернатива — создать `rule-plan-mode`
сейчас с одним ребёнком — не рекомендуется: это страница Slice 2 с четырьмя детьми, и
создавать её пустой значит ратифицировать структуру, которую слайс 2 будет менять.

**then.**

```
slug: rule-case-protocol
type: rule
kind: Leaf
purpose: Prevents a decision from being acted on before it is ratified, or ratified without its content in view
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: rule-plan-mode                 # страницы нет до Slice 2 — известное ложное
sprint: migration
tags: [session, workflow, ledger]
estimate:
  slug: estimate-case-protocol-loaded
  kind: QA
  criterion: >
    At session start the agent states the fence/bare-line rule and the one-Case-at-a-time
    rule without a read call; and a reply whose ledger lines sit only inside a fence adds
    nothing to raw/<date>/ledger.md.
  method: one reading at a session start, by hand, plus the fence case of tests/test_ledger.py
```

Файлы: `CLAUDE.md` (секция между маркерами + правка «Migration mode»),
`vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/estimates/estimate-case-protocol-loaded.md`.

Ledger:
```
- decision[case 13][create][rule-case-protocol]{ref:rule-plan-mode}
- decision[case 13][create][estimate-case-protocol-loaded]{ref:rule-case-protocol}
```

**ratification.** Ратифицирован владельцем 2026-09-09, как предложено.

---

# Work Mode — порядок исполнения

Слайс исполняется **в три сессии**: хуки читаются при старте Claude Code, и каждая
регистрация требует перезапуска. Главный агент делает всё сам, subagents не
диспатчатся (spec Slice 0). Ветка — `migration`, как в Slice 0. `make style` чист перед
каждым коммитом. Английский во всём, что попадает в репозиторий.

## Сессия A — эта, сразу после одобрения

**A0. Артефакты ратификации** (руками, хука ещё нет):
- этот план → второй документ в `vault/raw/2026-09-09/spec.md`, под заголовком
  `# Slice 1 …`, с разделителем;
- 16 строк `decision[case 9–13]` → `vault/raw/2026-09-09/ledger.md`, после строк
  Slice 0, с комментарием «written by hand, the hook arrives with this slice»;
- `vault/wiki/tags.md`: `session, hooks, harness, ledger, git, github, workflow` с
  русскими алиасами — все ратифицированы в Case 9–13;
- `vault/wiki/log.md`: по одной строке на Case, «written by hand».

**A1. Пакет и event log** (Case 9):
- `pyproject.toml`: `[project.scripts] guppi = "guppi.cli:main"`, `pytest` в dev-группу
  (`uv add --group dev pytest`), `[tool.pytest.ini_options] testpaths = ["tests"]`;
- `guppi/__init__.py`, `guppi/cli.py` (argparse: `event`, позже `ledger`, `probe`),
  `guppi/event.py`: `read_payload(stdin)`, `format_line(...)`, `append(vault_raw, line)`;
  корень vault — `vault/raw` относительно `CLAUDE_PROJECT_DIR` или cwd; всегда exit 0;
- `tests/test_event.py`: payload через pipe → строка нужного формата в temp-папке;
  пустой stdin (`hi`) → `--------`; `--session` переопределяет id; ошибка записи → stderr,
  exit 0;
- `Makefile`: `test: uv run pytest -q < /dev/null`; `help` его подхватит;
- `.gitignore`: `vault/raw/*/event_log.md`, `vault/raw/*/probe-*.json`.

**A2. Проба** (Case 10 д): `guppi/probe.py` — пишет stdin в
`vault/raw/<date>/probe-<hook_event_name>-<n>.json`, exit 0. Регистрация в
`.claude/settings.json`:
```
SessionStart              → uv run guppi event session-start
PostToolUse (без matcher) → uv run guppi event tool
PostToolUse ExitPlanMode  → uv run guppi probe
Stop                      → uv run guppi probe
```

**A3. Скилл `/hi`** (Case 11): `.claude/skills/hi/SKILL.md` — текст из Case 11, плюс
на время пробы одна строка `Probe: !`echo "${CLAUDE_SESSION_ID:-unset}"``.

**A4. Страницы** (Case 9–13), руками, по `rules/schema.md` и `estimates/schema.md`:
восемь Rule-страниц в `vault/wiki/rules/`, восемь Estimate в `vault/wiki/estimates/`,
все `status: draft` / `pending`, `origin: raw/2026-09-09/ledger.md#case-N`,
`sprint: migration`, `created: 2026-09-09`, `History` с одной строкой `created`.
`## Render` страниц `/hi` и `rule-case-protocol` — дословно то, что в файлах.

**A5. `CLAUDE.md`** (Case 13): секция между маркерами, правка «Migration mode».

**A6. Коммит** `feat(harness): guppi event, the probe, /hi and the Slice 1 pages`.
Затем `brief.md` переписывается: «перезапустите Claude Code, вызовите `/hi`, сделайте
один вызов инструмента, войдите и выйдите из Plan Mode, ответьте — и сессия B читает
пробу». Коммит `docs(vault): the brief points at the probe`.

**Владелец перезапускает Claude Code и вызывает `/hi`.**

## Сессия B — снимает пробу, строит ledger-хук

**B1.** Прочитать `probe-*.json`, вывод `Probe:` из `/hi`. Записать показания
голыми строками `- lesson[knowledge][lesson-hooks-stop-payload] …` и
`- lesson[knowledge][lesson-hooks-exitplanmode-payload] …` — хука ещё нет, поэтому в
ledger их вписывает рука, в том же формате. Заодно снять показания
`estimate-hi-no-read-calls`, `estimate-internal-context-loaded`,
`estimate-git-context-current`, `estimate-github-issues-listed` — этот старт и есть
измерение; `git check-ignore` и время хука через pipe для `estimate-event-log-records`.

**B2.** `guppi/ledger.py` по ратифицированному контракту и показанию пробы: одна ветка
источника текста; парсер fence/bare; проверка `hi` после последнего `session-start`
своей сессии; дедупликация по дословному совпадению; `stop_hook_active` → exit 0;
отказ → exit 2 + причина в stderr. `tests/test_ledger.py`: голая/fenced/estimate-строка,
повторный запуск, без `hi`, `stop_hook_active`.

**B3.** Удалить `guppi/probe.py`, файлы пробы, строку `Probe:` из скилла; `Stop` →
`uv run guppi ledger` (timeout 30), `PostToolUse ExitPlanMode` снять. Обновить
`implementation_ref` и `## Render` страниц, если текст скилла изменился (id сессии).
Вписать результаты снятых Estimates в их страницы (`status`, `## Result`, `History`) —
руками, генератора нет до Slice 3.

**B4.** `make style`, `make test`. Коммит `feat(harness): guppi ledger on Stop, the
probe leaves`. Brief: «перезапустите; сначала сессия без `/hi` с одной голой
decision-строкой в ответе, затем `/hi` — сессия C».

**Владелец перезапускает дважды: без `/hi`, затем с `/hi`.**

## Сессия C — живые показания и закрытие

**C1.** Без `/hi`: агент пишет голую `- decision[case 0][defer][probe]`-строку в ответ →
хук отказывает, человек видит причину, ledger не тронут. Это первое показание
`estimate-session-start-context`; второе — после `/hi` в этой же сессии C (или в
следующей): строки `estimate[...]` с результатами пишет **хук**, не рука — это и есть
показание `estimate-ledger-write-lifts` и репетиция DoD п. 5.

**C2.** Строки `- estimate[<slug>][passed|failed] <result>` для всех восьми Estimate,
голыми, в ответе; результаты — в страницы. `estimate-case-protocol-loaded` снимается
здесь же.

**C3.** Retro по модели: что сделано, что нет; уроки, если что-то сгорело, —
`- lesson[error][…]` голой строкой. `brief.md` для Slice 2: сделано, deferred (ниже),
known false (`parent: rule-plan-mode`; черновики `docs/migration/` с TBD; две копии
текста скилла до renderer'а). `handoff.md` за 2026-09-09 дополняется секцией Slice 1.
Коммит `docs(vault): Slice 1 closes, the brief points at Slice 2`.

# Что deferred из этого плана (в brief)

- `/grill-me` без страницы — Slice 3 или 5 (перенос).
- Рендер `settings.json` из `rule-hook-registry` — Slice 2 (перенос); после этого слайса
  в `settings.json` три хука, написанных руками.
- `origin` → репозиторий продукта, без upstream у `migration` — Slice 5 (11.1).
- `gh` без логина, GitHub-remote нет — когда появится remote (11.2).
- Две одновременные сессии в одном репозитории неразличимы для проверки `hi`, если
  `$CLAUDE_SESSION_ID` недоступна в `!`-подстановке — решается по показанию пробы.
- Обновление `status`/`## Result` Estimate-страниц делается руками до генератора Slice 3.

# Проверка

- `make style` и `make test` зелёные в каждой сессии перед коммитом.
- `uv run guppi event tool < payload.json` из терминала через pipe: строка в
  `vault/raw/<date>/event_log.md`, `git status` её не видит.
- `printf '{...}' | uv run guppi ledger`: с `hi` — строки в ledger; без — exit 2, текст
  причины; повтор — без дубликатов.
- Восемь показаний Estimates, по одному на страницу, записаны строками `estimate[...]` и
  в страницы; последние из них написаны хуком, не рукой (`git log -p` ledger покажет
  коммит, а `event_log.md` — что Stop-хук отработал).
- `find vault/wiki -type f | wc -l` → 19 + 16 = 35.
- Следующая сессия открывается `/hi` без единого read-tool вызова до Frontier.
