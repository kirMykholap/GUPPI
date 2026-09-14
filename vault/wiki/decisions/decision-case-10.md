---
type: decision
case: "10"
status: current
create: ["[[rule-ledger-write]]", "[[estimate-ledger-write-lifts]]"]
origin: raw/2026-09-09/ledger.md#case-10
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, ledger]
---

## When

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

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-10
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
