---
type: decision
case: "9"
status: current
kind: [create, create]
target_slug: [rule-event-log, estimate-event-log-records]
origin: raw/2026-09-09/ledger.md#case-9
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness]
---

## When

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

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-9
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
