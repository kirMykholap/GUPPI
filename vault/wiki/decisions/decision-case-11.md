---
type: decision
case: "11"
status: current
kind: [create, create, create, create, create, create, create, create]
target_slug: [rule-skill-hi, estimate-hi-no-read-calls, rule-internal-context, estimate-internal-context-loaded, rule-git-context, estimate-git-context-current, rule-github-issues, estimate-github-issues-listed]
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness, git, github]
---

## When

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

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
