<!-- approved 11:16:36 · session 3893518e -->

# Spec — 2026-09-10/11, session H

Plan Mode over the Frontier of `brief.md` plus the owner's three observations (Decision pages,
`raw/`, Estimates). Cases in the order ratified. The `then` blocks are what `guppi materialize`
reads; `replace` pairs that need the page text are filled at pre-task, before approval.

Before Work Mode, outside any Case (mechanical, ratified earlier): `uv run guppi render`, commit
together with the ten uncommitted ledger lines of 16:15:34. The Cases of 52 are appended by
hand to `raw/2026-09-10/spec.md` too, since their ledger lines are dated 2026-09-10. The
owner's instruction: `vault/pages.base` (their Obsidian Bases file) goes into `.gitignore`.

## Work Mode order

1. `uv run guppi render`; commit with the ledger tail and `.gitignore`.
2. Code, test-first, one commit per Case: `guppi/ledger.py` (55.1 the joined event logs, 55.2
   the transcript read-back); `guppi/materialize.py` (53.3 sections for a standalone
   estimate, 56 the incomplete rule); `guppi/generate.py` (52.1 decision fields and body,
   52.3 `deferred_by` and its removal on supersedes, 52.4 decision first and History
   wikilinks, 53.1 no paired estimate, 53.2 no skip, 53.3 stale `failed` dropped);
   `guppi/index.py` (52.3 the suffix, 53.4 four files); `guppi/cleanup.py` (57 four
   indexes, `estimates` lists of entities and rules only); `guppi/lint.py` (the classes of
   52 and 53, four files). `make test` green, `make style` clean.
3. Rule-class files by hand, each named `file` + `change` in the blocks above: `index.md`
   (§1, §3, §5, §7, §8, §10, §11), `glossary.md`, `case-schema.md`, `CLAUDE.md`, the six
   `schema.yaml` / `schema.md` pairs (decisions, rules, entities, estimates, lessons).
4. One-off scripts under their Cases, run once, not kept: the 65 decision pages to the new
   shape (52.1); the `estimates` field and section off the 17 lesson pages (53.1); the two
   `*-walks-dates` estimates' fields into sections and the stale `failed` off `old-harness`
   in the 2026-09-09 yaml (53.3); delete `vault/wiki/estimates-index.md` (53.4).
5. `uv run guppi render` for `rule-retro`, `rule-ask`, `rule-documentation`, `rule-synthesis`,
   `rule-brief`, `rule-pretask`, `rule-index-check`; `make lint` against the known-false list.
6. Readings that can be taken in session: `estimate-ledger-write-lifts` (the midnight window
   by test; the `/pre-task` read-back live), `estimate-generate-writes`,
   `estimate-materialize-assembles`, `estimate-index-lists`, `estimate-lint-catches`,
   `estimate-cleanup-moves`. Left for the next session's `/retro` and librarian run:
   `estimate-retro-loads`, `estimate-spec-capture-appends`, `estimate-documentation-completes`,
   `estimate-synthesis-clusters`.
7. `/retro` in the new form, commit, `/handoff`, the librarian.

## State on 2026-09-11 morning (for a resume)

- Case 52 (52.1–52.4): ratified, 19 ledger lines written 2026-09-10 20:50:18.
- Case 53 (53.1–53.4): ratified 2026-09-11; the Stop hook refused its 44 lines (no
  `session-start` of session 3893518e in `raw/2026-09-11/event_log.md`; `hi` alone at 09:59:22).
  After a resume or compact and a fresh `/hi`, repeat the block below verbatim in a `LEDGER` fence.
- Case 54: drafted, not ratified (below).
- Case 55 to draft: `rule-ledger-write` — the hook walks `raw/*/event_log.md` back to the last
  `session-start` of its session; together with Case 51 (a reply ending in a tool call).
- `vault/pages.base`: the owner's Obsidian Bases file, untracked; owner decides.

Lines to repeat (Case 53) plus the lesson of the midnight bug:

```
- decision[case 53.1][update][estimates-schema-yaml]
- decision[case 53.1][update][estimates-schema]
- decision[case 53.1][update][lessons-schema-yaml]
- decision[case 53.1][update][lessons-schema]
- decision[case 53.1][update][index]
- decision[case 53.1][update][glossary]
- decision[case 53.1][update][rule-page-generation]
- decision[case 53.1][update][rule-lint]
- decision[case 53.1][delete][estimate-agents-at-import-not-expanded]
- decision[case 53.1][delete][estimate-agents-loaded-at-session-start]
- decision[case 53.1][delete][estimate-agents-visible-in-session]
- decision[case 53.1][delete][estimate-estimates-criterion-stale-after-contract-change]
- decision[case 53.1][delete][estimate-generate-log-written-last]
- decision[case 53.1][delete][estimate-generate-replace-mapping-crashes]
- decision[case 53.1][delete][estimate-generate-walk-history-dated-by-yaml]
- decision[case 53.1][delete][estimate-hooks-exitplanmode-payload]
- decision[case 53.1][delete][estimate-hooks-messagedisplay-cannot-block]
- decision[case 53.1][delete][estimate-hooks-sessionstart-cannot-block]
- decision[case 53.1][delete][estimate-hooks-stop-payload]
- decision[case 53.1][delete][estimate-hooks-windows-stdin-encoding]
- decision[case 53.1][delete][estimate-ledger-hook-misses-a-reply-ending-in-a-tool-call]
- decision[case 53.1][delete][estimate-librarian-reads-beyond-the-four-inputs]
- decision[case 53.1][delete][estimate-materialize-assumes-every-entry-has-a-line]
- decision[case 53.1][delete][estimate-readings-after-librarian-invisible-to-next-hi]
- decision[case 53.1][delete][estimate-tests-cli-date-pinned]
- decision[case 53.2][update][index]
- decision[case 53.2][update][case-schema]
- decision[case 53.2][update][rule-page-generation]
- decision[case 53.2][update][rule-ask]
- decision[case 53.2][update][rule-pretask]
- decision[case 53.2][update][estimate-generate-writes]
- decision[case 53.2][delete][estimate-generate-rejects-shape-alone]
- decision[case 53.2][delete][estimate-generate-logs-per-entry]
- decision[case 53.2][delete][estimate-generate-dates-history-by-run]
- decision[case 53.2][delete][estimate-generate-passes-delete-outside-vault]
- decision[case 53.3][update][rule-materialize]
- decision[case 53.3][update][rule-page-generation]
- decision[case 53.3][update][estimate-materialize-assembles]
- decision[case 53.3][update][estimate-generate-writes]
- decision[case 53.4][update][index]
- decision[case 53.4][update][rule-index]
- decision[case 53.4][update][rule-index-check]
- decision[case 53.4][update][rule-lint]
- decision[case 53.4][update][estimate-index-lists]
- lesson[error][lesson-ledger-hook-hi-lost-at-midnight]{tags:harness,hooks,ledger}{source:guppi/ledger.py hi_recorded; raw/2026-09-11/event_log.md} trigger: session H crossed midnight; the Stop hook refused the 44 lines of Case 53 with "no /hi recorded", and a fresh /hi on 2026-09-11 did not help root_cause: the hook reads raw/<today>/event_log.md only and needs a session-start of its own session before the hi; both lay in raw/2026-09-10/event_log.md, and the day's new log held tool lines and a hi with no start; a session that crosses midnight, or any hi whose start is in another day's file, cannot write the ledger until the session restarts
```

## Case 52 — Decision page: fields, body, defer, the loop back from the target

> **context:**
> Decision-страница сегодня — журнал по Case: `targets` списком объектов, тело из четырёх секций старой формы Case, пустое у defer с Retro. Цель defer не знает, что по ней что-то отложено; её History указывает на строку ledger, не на решение.

> **problem:**
> Форма полей Decision и тела; откуда у Retro-Case берётся текст; поле `deferred_by` на цели и его путь через индекс в ask; History и порядок записи.

> **recommend:**
> Четыре sub-cases. Все `update`; 65 существующих Decision-страниц переписывает скрипт под 52.1.

> **given:**
> `decisions/schema.yaml`: required `targets`, body `## Context`, `## Now`, `## Problem`, `## Then`, `## History`.
> **＋** `generate.py`: entries applied (line 629) before decision pages (line 662). History `<action> · <origin>`.
> **＋** `materialize.py`: `case_text` from `## Case N` in `spec.md`; Retro Cases never reach the Spec; Cases 50, 51 `incomplete`.
> **＋** `rules/schema.yaml`, `entities/schema.yaml`: no `deferred_by`; `built` computed by the cascade.
> **＋** `rule-index`: `slug: purpose`. `ask-guppi` never opens `decisions/` unless asked why.
> **＋** `materialize` marks `superseded_by` on `{supersedes:case N}`.
> **－** `origin` stays a ledger path until Slice 3c.

### Case 52.1 — Decision fields and body

> **when:**
> `guppi generate` writes a Decision page; lint checks it; someone reads `decisions/schema.md`.

> **then:**
> Frontmatter carries two lists aligned by position, one position per ledger line of the Case: `kind: [update, create]`, `target_slug: [rule-x, estimate-y]`. The category is derived from the slug prefix; a Rule-class slug (`case-schema`, `rules-schema-yaml`) names a file.
> **＋** `targets`, `ref`, `path` go; `source` is a page field, a list, when present.
> **＋** Body: `## Context`, `## Problem`, `## Given`, `## When`, `## Note` (optional), `## History` last, as on every page. `## Now` and `## Then` go.
> **＋** Lint checks the two lists have equal length and every vault-category `target_slug` is a page.
> **＋** A one-off script under this Case rewrites the 65 pages of `decisions/`, History `migrated · [[decision-case-52.1]]`.
> **－** One page per Case, slug `decision-case-<N>`, unchanged.

> **ratification:** ratified 2026-09-10 with the owner's change: no `target_category`; History stays.

```then
update:
  - slug: decisions-schema-yaml
    file: vault/wiki/decisions/schema.yaml
    change: "required: type, case, status, kind, target_slug, origin, sprint, created, tags; optional: source, supersedes, superseded_by; kind values create|update|delete|defer per position; body required Context, Problem, Given, When, History; optional Note"
  - slug: decisions-schema
    file: vault/wiki/decisions/schema.md
    change: "the Properties table: targets replaced by kind and target_slug, two lists aligned by position, the category derived from the slug prefix or the Rule-class map; ref and path gone; source optional; Body table: Context, Problem, Given, When, Note; the example rewritten; History stays last"
  - slug: rule-page-generation
    replace:
      - old: "One Decision page per Case, `decisions/decision-case-<N>.md`: `case`, `status: current`, `targets`, `supersedes`, `origin`, `sprint`, `created`, `tags` (the union of the targets' tags); body `Context`, `Now`, `Problem`, `Then` from `case_text` (`given` fills `Now`)."
        new: "One Decision page per Case, `decisions/decision-case-<N>.md`: `case`, `status: current`, `kind` and `target_slug` (two lists aligned by position, one position per ledger line of the Case; the category is derived from the slug prefix or the Rule-class map, never written), `source` when a line carries one, `supersedes`, `origin`, `sprint`, `created`, `tags` (the union of the targets' tags); body `Context`, `Problem`, `Given`, `When` from `case_text`."
    change: "a decision page carries kind and target_slug lists and the sections Context, Problem, Given, When from case_text"
  - slug: rule-lint
    sections:
      How it works: |
        `uv run guppi lint` reads every live page against its category's `schema.yaml`:
        required fields and sections, legal statuses, `origin` as a grep target in `raw/`,
        every ref (`parent`, `target`, `children`, `estimates`, `insight`) as an existing page,
        orphans, a `built` page with an Estimate not `passed`, the two Method classes of
        case 26.2. A decision page: `kind` and `target_slug` of equal length; every
        `target_slug` with a category prefix an existing page. It reports and exits 1 on any
        finding, 0 with no output on a clean vault.
    change: "the classes listed; decision pages: kind and target_slug of equal length, every vault target_slug an existing page"
```

### Case 52.2 — A Retro Case reaches the Spec

> **when:**
> At Retro a Case is ratified or deferred; the agent writes the `LEDGER` block.

> **then:**
> Before the `LEDGER` block the agent appends the Case to `raw/<date>/spec.md` under `## Retro`, in the same form: `## Case N`, the seven sections, the `then` block. `materialize` finds it like any other.
> **＋** A defer at Retro is a Case with one-sentence `context`, `problem`, `given`, `when` and a `defer` block with `purpose`; a bare line without a Case is forbidden, `materialize` marks it `incomplete`.
> **＋** `rule-retro` and `case-schema.md` say so.
> **－** No hook: writing into `raw/` is the agent's work, like `handoff.md`.

> **ratification:** ratified 2026-09-10.

```then
update:
  - slug: rule-retro
    replace:
      - old: "Any other change is new scope: write a `- decision[case N][defer][slug]`\nline instead and, when it is a bug, a `- lesson[error][...]` line too."
        new: "Any other change is new scope: discuss it as a Case, append the Case to\n`vault/raw/<date>/spec.md` under a `## Retro` heading in the form of Plan Mode (the\nseven sections and the `then` block, a `defer` block with `purpose`), then write the\n`- decision[case N][defer][slug]` line and, when it is a bug, a `- lesson[error][...]`\nline too. A defer line without its Case in the Spec is marked incomplete by materialize."
    change: "a Retro Case is appended to spec.md under ## Retro before its ledger line; a bare defer is forbidden"
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "a Case ratified or deferred at Retro is appended by the agent to raw/<date>/spec.md under ## Retro, same form; a defer block carries purpose; every defer has its Case"
```

### Case 52.3 — `deferred_by` on the target, in the index, in ask

> **when:**
> `guppi generate` applies a `defer`; `guppi index` builds the index; `ask-guppi` answers about a page carrying the field.

> **then:**
> Rule and Entity get an optional `deferred_by: [decision slugs]`. `generate` appends the decision slug on a `defer`; a placeholder page is born with it.
> **＋** A later decision with `{supersedes:case N}` removes `decision-case-N` from the list; an empty list is removed.
> **＋** Index line: `slug: purpose · deferred_by: decision-case-50`.
> **＋** `ask-guppi`: when a page in its answer carries `deferred_by`, it opens the named decision and gives its `## Problem` on the `exists` or `near` line. Otherwise `decisions/` stays closed.
> **＋** Lint: every slug in `deferred_by` is an existing Decision page.
> **－** The target's `status` does not change; the cascade as before.

> **ratification:** ratified 2026-09-10.

```then
update:
  - slug: rules-schema-yaml
    file: vault/wiki/rules/schema.yaml
    change: "optional deferred_by: list of decision slugs"
  - slug: rules-schema
    file: vault/wiki/rules/schema.md
    change: "deferred_by row: the Decision pages whose defer targets this page; written and cleared by generate, never by hand"
  - slug: entities-schema-yaml
    file: vault/wiki/entities/schema.yaml
    change: "optional deferred_by: list of decision slugs"
  - slug: entities-schema
    file: vault/wiki/entities/schema.md
    change: "deferred_by row, as for rules"
  - slug: rule-page-generation
    replace:
      - old: "A `defer` with a page appends History `deferred`; without one it writes a placeholder page, `status: draft`, with only the fields the Case gave."
        new: "A `defer` with a page appends History `deferred` and the decision slug to its `deferred_by`; without one it writes a placeholder page, `status: draft`, with only the fields the Case gave and `deferred_by`."
      - old: "A `supersedes` sets the earlier page `status: superseded` and appends the new slug to its `superseded_by`."
        new: "A `supersedes` sets the earlier page `status: superseded`, appends the new slug to its `superseded_by`, and removes the earlier decision's slug from the `deferred_by` of every target it deferred; an empty `deferred_by` is dropped."
    change: "a defer with a page appends the decision slug to deferred_by; a placeholder is born with it; a supersedes removes the superseded decision from the list"
  - slug: rule-index
    replace:
      - old: "`uv run guppi index` writes `vault/wiki/<category>-index.md` for entities, rules, estimates, lessons and insights;"
        new: "`uv run guppi index` writes `vault/wiki/<category>-index.md` for entities, rules, estimates, lessons and insights; the line of a page carrying `deferred_by` ends with ` · deferred_by: <slugs>`, so a deferred decision is visible without opening the page;"
    change: "a line of a page with deferred_by ends with · deferred_by: <slugs>"
  - slug: rule-ask
    replace:
      - old: "Do not open or grep `vault/wiki/decisions/` unless the question asks why something was decided; then reach the Decision through the page's `origin`. Decisions have no index on purpose."
        new: "Do not open or grep `vault/wiki/decisions/` except for two reasons: a page in your answer carries `deferred_by` — open the decision it names and give its `## Problem` on the `exists` or `near` line, since a deferred decision is something already decided; or the question asks why something was decided — reach the Decision through the page's `origin`. Decisions have no index on purpose."
    change: "a page with deferred_by in the answer: open the named decision, give its Problem on the exists or near line"
  - slug: rule-lint
    replace:
      - old: "every `target_slug` with a category prefix an existing page."
        new: "every `target_slug` with a category prefix an existing page; every slug in `deferred_by` an existing decision page."
    change: "deferred_by: every slug an existing decision page"
  - slug: index
    file: vault/wiki/index.md
    change: "§5 defer rows: existing → deferred_by on the target; §11: a Decision is opened by ask only through deferred_by or origin"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "deferred_by row under Fields; the Decision row names kind and target_slug"
```

### Case 52.4 — History names the decision; the decision is written first

> **when:**
> `guppi generate` applies the yaml of one date.

> **then:**
> For each Case its Decision page is written first, then the entries of its lines.
> **＋** History of the targets and `log.md`: `<action> · [[decision-case-N]]`.
> **＋** Lint checks the wikilink in a History line resolves.
> **－** A reading or a lesson has no decision: their History stays `· raw/<date>/ledger.md#L<n>` until Slice 3c.
> **－** `origin` unchanged.

> **ratification:** ratified 2026-09-10.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: "`uv run guppi generate [--date]` applies the entries of `raw/<date>/materialize.yaml` in order"
        new: "`uv run guppi generate [--date]` applies the entries of `raw/<date>/materialize.yaml` in order, the Decision page of a Case written before the first entry of its lines,"
      - old: "History lines: `created`, `updated: <change>`, `status: a → b`, `deleted`, `deferred`, `child <slug> added`, `estimate <slug> added`, each `· <origin>`;"
        new: "History lines: `created`, `updated: <change>`, `status: a → b`, `deleted`, `deferred`, `child <slug> added`, `estimate <slug> added`, each `· [[decision-case-N]]` when the entry belongs to a Case and `· <origin>` (the ledger pointer) when it is a reading or a lesson;"
    change: "the decision page of a Case is written before its entries; History and log lines end with · [[decision-case-N]] when a decision exists, else the ledger pointer"
  - slug: rule-lint
    replace:
      - old: "every slug in `deferred_by` an existing decision page."
        new: "every slug in `deferred_by` an existing decision page; a `[[decision-…]]` wikilink in a History line resolves to a page."
    change: "a History wikilink resolves to a page"
  - slug: index
    file: vault/wiki/index.md
    change: "§1 History example and §5: History lines name the decision as a wikilink; readings and lessons keep the ledger pointer"
```

## Case 53 — Estimates: one page per judgment

> **context:**
> 53 Estimate-страниц на 33 правила: 17 парных к урокам с шаблонной фразой, четыре новых у `rule-page-generation` вместо правки одной, шесть с `criterion` полем без секции. Estimate — проверка контракта: критерий, метод, результат, статус; от неё считается `built`. Существует только у страницы с `when` + `then`.

> **problem:**
> Снять пары у уроков; изменение контракта — `update` существующей Estimate; ask доходит до Estimate через цель; два дефекта хвоста; нужен ли `estimates-index.md`.

> **recommend:**
> Четыре sub-cases; 21 `delete`, остальное `update`.

> **given:**
> `lessons/schema.md` строка 18: `estimates` required, `error` born `passed`, `knowledge` Research «before an Insight». §8 то же; глоссарий повторяет. `insight-harness-agent-visibility` стоит на уроке с Research `pending`.
> **＋** `generate.estimate()` 439: same status with a Result → skipped. `lesson_estimate()` 343 пишет пару по шаблону.
> **＋** `materialize` 326–330: sections only for the nested estimate; `apply()` never clears `failed`.
> **＋** §3 «Estimates count too»; `ask-guppi` читает `estimates-index.md`; index check сравнивает estimate creates; `estimate-index-lists` требует строку estimate.
> **＋** На 17 парных Estimate ссылаются только их уроки. `estimate-librarian-reads-beyond-the-four-inputs` прошла живым чтением 13:10:37; чтение остаётся в ledger.
> **－** Estimate как секция на Leaf — не здесь. `rule-index-check` сравнение остальных категорий не меняется.

### Case 53.1 — An Estimate exists only for a page with a contract

> **when:**
> `guppi generate` применяет `lesson`; lint проверяет урок и Estimate; библиотекарь пишет Insight.

> **then:**
> `target` Estimate — slug Entity или Rule. У Lesson и Insight Estimate нет: урок — запись наблюдения, без контракта.
> **＋** `estimates`, `## Estimates` уходят из схемы урока; `generate` не пишет пару; lint не требует `estimates` у урока.
> **＋** §8, глоссарий, `rule-page-generation`: условие «Research `passed` до Insight» снято.
> **＋** 17 парных Estimate — `delete`; `cleanup` уносит в `archived/`. Влияние: у их уроков поле `estimates` и секцию удаляет скрипт под этим Case; Insights не затронуты.
> **－** Ledger-строки чтений остаются.

> **ratification:** ratified 2026-09-11.

```then
update:
  - slug: estimates-schema-yaml
    file: vault/wiki/estimates/schema.yaml
    change: "target: an entity or rule slug"
  - slug: estimates-schema
    file: vault/wiki/estimates/schema.md
    change: "target row: the Entity or Rule this verifies; an Estimate exists only for a page with a when and then; a Lesson or Insight has none"
  - slug: lessons-schema-yaml
    file: vault/wiki/lessons/schema.yaml
    change: "estimates removed from required; ## Estimates removed from body"
  - slug: lessons-schema
    file: vault/wiki/lessons/schema.md
    change: "the estimates row and the ## Estimates section removed; a lesson is a recorded fact and carries no check; the examples rewritten"
  - slug: index
    file: vault/wiki/index.md
    change: "§8 Estimates paragraph removed: a lesson has no Estimate; a knowledge claim is checked by the Estimate of the Rule that leans on it; §7: an Estimate targets an Entity or a Rule"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "Lesson row: no Estimate; Estimate row: exists only for an Entity or Rule"
  - slug: rule-page-generation
    replace:
      - old: "A lesson's paired Estimate is `estimate-<lesson slug without lesson->`, target the lesson, tags the lesson's. `error`: kind `QA`, status `passed`, criterion \"The failure named in Trigger was observed directly\", method \"The observation itself, by hand; recorded in the ledger line\", result \"Observed. The ledger line is the record.\" `knowledge`: kind `Research`, status `pending`, criterion \"The claim in Root cause holds when read live\", method \"One live reading by hand, recorded in the estimate line\". A missing `source` is not invented; lint names it."
        new: "A lesson entry writes the lesson only: a lesson is a recorded fact and has no Estimate. A missing `source` is not invented; lint names it."
    change: "a lesson entry writes the lesson only; no paired Estimate"
  - slug: rule-lint
    replace:
      - old: "resolves to a page."
        new: "resolves to a page. A lesson needs no `estimates`; an estimate whose `target` is not an entity or a rule is a finding."
    change: "lessons: estimates not required; an estimate whose target is not an entity or rule is a finding"
delete:
  - slug: estimate-agents-at-import-not-expanded
    impact: paired Estimate of a lesson; referenced by its lesson only; the field is removed by the migration script
  - slug: estimate-agents-loaded-at-session-start
    impact: as above
  - slug: estimate-agents-visible-in-session
    impact: as above
  - slug: estimate-estimates-criterion-stale-after-contract-change
    impact: as above
  - slug: estimate-generate-log-written-last
    impact: as above
  - slug: estimate-generate-replace-mapping-crashes
    impact: as above
  - slug: estimate-generate-walk-history-dated-by-yaml
    impact: as above
  - slug: estimate-hooks-exitplanmode-payload
    impact: as above
  - slug: estimate-hooks-messagedisplay-cannot-block
    impact: as above
  - slug: estimate-hooks-sessionstart-cannot-block
    impact: as above
  - slug: estimate-hooks-stop-payload
    impact: as above
  - slug: estimate-hooks-windows-stdin-encoding
    impact: as above
  - slug: estimate-ledger-hook-misses-a-reply-ending-in-a-tool-call
    impact: as above
  - slug: estimate-librarian-reads-beyond-the-four-inputs
    impact: as above; its live reading of 13:10:37 stays in the ledger
  - slug: estimate-materialize-assumes-every-entry-has-a-line
    impact: as above
  - slug: estimate-readings-after-librarian-invisible-to-next-hi
    impact: as above
  - slug: estimate-tests-cli-date-pinned
    impact: as above
```

### Case 53.2 — A contract change updates the Estimate; ask reaches Estimates through the target

> **when:**
> Case меняет контракт Leaf; `guppi generate` применяет строку чтения; `ask-guppi` отвечает про проверку.

> **then:**
> Case, меняющий контракт страницы, в том же Case правит `Criterion` (и `Method`) её существующей Estimate и ставит `status: pending`. Новая Estimate — только по §6: условие, которое падает и чинится отдельно.
> **＋** `generate`: строка чтения всегда пишет Result и History; пропуск снят; повтор держат метки `applied`.
> **＋** `ask-guppi` доходит до Estimate через поле `estimates` цели, когда вопрос о проверке. §3: «the Estimates of a page whose contract changes are named in `given`».
> **＋** Четыре Estimate Cases 47–48 — `delete`; их критерии — строки **＋** в `Criterion` `estimate-generate-writes`, `pending`, чтение на End of Work из тех же тестов. `*-walks-dates` остаются.

> **ratification:** ratified 2026-09-11.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§3 pre-task: 'Estimates count too' replaced by 'the Estimates of a page whose contract changes are named in given, and the Case updates their criterion'; §7: a reading overwrites Result; a contract change updates the criterion and sets pending; a new Estimate only by §6"
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "an update of a Leaf's contract carries, in the same then block, the update of its Estimate: sections Criterion (and Method) and set status pending"
  - slug: rule-page-generation
    replace:
      - old: "An `estimate` entry sets `status`, overwrites `## Result` and appends History; a page already at that status with a Result is skipped."
        new: "An `estimate` entry sets `status`, overwrites `## Result` and appends History, whatever the page held before: a reading always lands, and reruns are held off by the `applied` marks alone."
    change: "an estimate entry always sets status, overwrites Result and appends History; no skip"
  - slug: rule-ask
    replace:
      - old: "Read `vault/wiki/<category>-index.md` for every other category the question touches (entities, estimates, lessons, insights; decisions have none)."
        new: "Read `vault/wiki/<category>-index.md` for every other category the question touches (entities, lessons, insights; decisions and estimates have none). When the question is about a check, reach the Estimates through the `estimates` field of the page it is about, and open them only when the question asks what they say."
    change: "Estimates are reached through the estimates field of the page the question is about; no estimates index"
  - slug: rule-pretask
    replace:
      - old: "List every decision ratified in this Plan Mode, one line each: slug — decision type — purpose."
        new: "List every decision ratified in this Plan Mode, one line each: slug — decision type — purpose; for an `update` that changes a page's contract, add the page's `estimates` and whether the Case updates their criterion — an Estimate whose criterion quotes the changed wording and has no update line is a finding."
    change: "a Case changing a page's contract names the page's Estimates; a stale criterion is a finding"
  - slug: estimate-generate-writes
    set: {status: pending}
    sections:
      Criterion: |
        Against a temp vault from one yaml: a MOC rule create, a Leaf child create with ref
        and its nested estimate yield three pages that pass their schema.yaml, the parent's
        children and ## Children in order, the target's estimates and ## Estimates; an
        update with set, sections, replace and change changes the field, the section, the
        text and appends History; a replace absent or not unique fails that entry alone,
        exit 1; a delete sets archived with History; a defer without a page writes a
        placeholder with only the Case's fields and deferred_by, a defer with a page appends
        the decision slug to its deferred_by, and a supersedes removes it; an estimate entry
        sets status and overwrites ## Result whatever the page held; a lesson entry writes
        the lesson and no Estimate; one decision page per Case with kind and target_slug
        aligned by position and the sections Context, Problem, Given, When, written before
        the entries of its lines, and supersedes marks the earlier page superseded; History
        and log lines of a Case's entries end with the decision wikilink, a reading's or a
        lesson's with the ledger pointer; the cascade sets built; a declared new tag lands
        in tags.md, an undeclared one is reported; log.md gains one line per write.
        **＋** An entry whose field has a shape the script does not expect, or in which any
        exception is raised, is marked failed, reported on stderr and skipped; the rest
        apply; exit 1.
        **＋** After each applied entry its lines are in log.md; a run that stops at entry N
        leaves the feed level with the pages up to N.
        **＋** History lines and log.md lines carry the date of the run; created carries the
        yaml's date.
        **＋** A delete whose slug is neither a category prefix nor a Rule-class file is
        printed on stdout as outside the vault and marked applied; a delete of a missing
        page with a category fails.
        Applied entries are marked and a rerun writes nothing; a create colliding with a
        page not marked exists fails. Live: the yaml of the session's librarian run; the
        reading records pages created per category, make lint afterwards against the
        known-false list, and git diff --stat.
    change: "the criteria of the four Estimates of Cases 47–48 folded in; no skip, no paired estimate, the decision-page shape and deferred_by of Case 52; pending until the End of Work reading"
delete:
  - slug: estimate-generate-rejects-shape-alone
    impact: folded into estimate-generate-writes; rule-page-generation's estimates field loses it by cleanup
  - slug: estimate-generate-logs-per-entry
    impact: as above
  - slug: estimate-generate-dates-history-by-run
    impact: as above
  - slug: estimate-generate-passes-delete-outside-vault
    impact: as above
```

### Case 53.3 — Two defects of the tail

> **when:**
> `guppi materialize` читает standalone `create` Estimate с `ref`; `guppi generate` применяет запись с `failed` прошлого прогона.

> **then:**
> `materialize` кладёт `context`, `criterion`, `method` standalone Estimate в `sections`, как у вложенной.
> **＋** Успешно применённая запись теряет `failed`.
> **＋** По 53.2: `Criterion` `estimate-materialize-assembles` и `estimate-generate-writes` получают по строке **＋**, `pending`.
> **＋** Скрипт-однодневка переносит поля в секции у `estimate-generate-walks-dates`, `estimate-materialize-walks-dates`; снимает `failed` у `old-harness` в yaml 2026-09-09.

> **ratification:** ratified 2026-09-11.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "A Leaf's nested `estimate` becomes its own `create` entry."
        new: "A Leaf's nested `estimate` becomes its own `create` entry; a standalone estimate `create` with `ref` maps `context`, `criterion` and `method` into `sections` the same way, so the page gets its Criterion and Method sections whichever way it was born."
    change: "a standalone estimate create maps context, criterion and method into sections, as the nested one does"
  - slug: rule-page-generation
    replace:
      - old: "marks each applied entry `applied: <time>` in the yaml, so a rerun writes nothing."
        new: "marks each applied entry `applied: <time>` in the yaml and drops a `failed` mark an earlier run left on it, so a rerun writes nothing and no reader of the yaml sees a failure that is over."
    change: "an entry that applies loses a failed mark left by an earlier run"
  - slug: estimate-materialize-assembles
    set: {status: pending}
    replace:
      - old: "one decision entry per Case carries case_text and targets."
        new: "one decision entry per Case carries case_text and targets, and is marked incomplete for a missing given or when only when a kind other than defer is among its lines; a standalone estimate create with ref carries context, criterion and method as sections, as the nested one does."
    change: "criterion: the standalone estimate create maps to sections; the incomplete rule for a defer-only Case (case 56)"
  - slug: estimate-generate-writes
    set: {status: pending}
    replace:
      - old: "Applied entries are marked and a rerun writes nothing;"
        new: "Applied entries are marked, a stale failed mark left by an earlier run is dropped on apply, and a rerun writes nothing;"
    change: "criterion: a stale failed mark is dropped on apply (case 53.3)"
```

### Case 53.4 — No `estimates-index.md`

> **when:**
> `guppi index` пишет индексы; библиотекарь делает index check; `make lint` идёт.

> **then:**
> Индексов четыре: entities, rules, lessons, insights. `estimates-index.md` не пишется; файл удаляется под этим Case.
> **＋** Index check сравнивает четыре категории.
> **＋** `estimate-index-lists`: строка про estimate уходит из Criterion, `pending`.
> **＋** §1, §11, `rule-index`, `rule-index-check`, `rule-lint`: четыре.
> **－** `cleanup` перестраивает четыре.

> **ratification:** ratified 2026-09-11.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§1 layout and §11: four indexes; no estimates-index.md; Estimates are reached through their target"
  - slug: rule-index
    replace:
      - old: "for entities, rules, estimates, lessons and insights;"
        new: "for entities, rules, lessons and insights — there is no estimates index: an Estimate is reached through the `estimates` field of its target, and nothing searches by criterion;"
    change: "four category files; no estimates index"
  - slug: rule-index-check
    replace:
      - old: "for each `create` entry in `materialize.yaml`, compare its `purpose` (`criterion` for an estimate, `root_cause` for a lesson)"
        new: "for each `create` entry in `materialize.yaml` other than an estimate — an Estimate is born with its Leaf and has no index — compare its `purpose` (`root_cause` for a lesson)"
    change: "estimate creates are not compared; four categories"
  - slug: rule-lint
    replace:
      - old: "`make lint` runs it after `render --check` and `index --check`;"
        new: "`make lint` runs it after `render --check` and `index --check` over the four index files;"
    change: "index --check over four files"
  - slug: estimate-index-lists
    set: {status: pending}
    replace:
      - old: "in slug order with the field its schema names; an estimate line carries its whole criterion on one line; an archived page"
        new: "in slug order with the field its schema names, a page with deferred_by ending with · deferred_by: <slugs>; an archived page"
      - old: "five files appear,"
        new: "four files appear and none for estimates,"
    change: "no estimates index; four files; the deferred_by suffix"
```

## Case 54 — The librarian's frame: four reasons to open a page

> **context:**
> Case 44 разрешил библиотекарю открывать страницу `wiki/` в трёх случаях: строка индекса не решает «то же или рядом»; он пишет Insight и ему нужны Trigger и Root cause его уроков; скрипт назвал страницу в ошибке. Прогон G нарушил это дважды, и оба чтения были нужны: два урока, чтобы решить, кластеризуется ли третий (Insight не родился); свой Insight и статусы Estimate для брифа. Оба чтения снова `failed`, Slice 3 не закрывается.

> **problem:**
> Фрейм называет чтения по итогу, а не по вопросу; у брифа нет входа со статусом Estimate и severity Insight.

> **recommend:**
> Четыре причины, каждая по вопросу; каждое чтение названо с причиной и исходом; критерии переписаны; «five indexes» → «four» после 53.4.

> **given:**
> `rule-documentation` Render 43–47: «the five index files», три случая. `rule-synthesis` Render 39: «the lessons you cluster». `rule-brief`: нужны failed Estimates, severity, счёт страниц; входа нет.
> **＋** `estimate-documentation-completes`: «five indexes», «three reasons». `estimate-synthesis-clusters`: «named as a child of the Insight written». Оба `failed` 16:15:34 на этих чтениях; урок `lesson-frame-read-clauses-omit-candidate-check-and-brief`.
> **＋** Event log G: 16:06:54 два урока; 16:09:57 свой Insight; 16:10:41 grep статусов.
> **－** `rule-index-check` не меняется. Чтение снимается после прогона библиотекаря этой сессии, в хвост ledger.

> **when:**
> Библиотекарь запускается по агент-файлу из `rule-documentation`; после прогона снимаются `estimate-documentation-completes` и `estimate-synthesis-clusters`.

> **then:**
> Входов четыре: `handoff.md`, yaml-ы из stdout `materialize`, четыре индекса, `tags.md`. Страницу `wiki/` библиотекарь открывает по четырём причинам: строка индекса не решает «то же или рядом»; строка индекса не решает, делит ли урок root cause с другим уроком или Insight; скрипт назвал страницу в ошибке; брифу нужен факт, которого нет ни в одном входе (статус Estimate, severity Insight). Каждую открытую страницу он называет в отчёте с причиной и исходом.
> **＋** `rule-synthesis` Render: читать Trigger и Root cause урока-кандидата, когда строки индекса мало, кластер или нет; называть с исходом.
> **＋** `rule-brief` Render: статус Estimate и severity Insight со страницы, когда входа нет; каждая названа.
> **＋** `estimate-documentation-completes`: «four indexes», «one of the four reasons»; `pending`.
> **＋** `estimate-synthesis-clusters`: «every lesson page read is named with the outcome: the Insight it joined, or none and why»; `pending`.
> **－** Запреты на `ledger.md`, `spec.md`, `plan.md`, `decisions/`, `archived/`, `guppi/`, `tests/` без изменений.

> **ratification:** ratified 2026-09-11, the owner not fully sure; the reading after this session's librarian run decides.

```
- decision[case 54][update][rule-documentation]
- decision[case 54][update][rule-synthesis]
- decision[case 54][update][rule-brief]
- decision[case 54][update][estimate-documentation-completes]
- decision[case 54][update][estimate-synthesis-clusters]
```

```then
update:
  - slug: rule-documentation
    replace:
      - old: "Your inputs are four: `vault/raw/<today>/handoff.md`, every `materialize.yaml`\nthat `guppi materialize` names on its stdout, the five `vault/wiki/<category>-index.md`\nfiles, and `vault/wiki/tags.md`. Open a page under `vault/wiki/` in three cases only:\nan index line does not tell you whether a create is the same page or a near one; you\nwrite an Insight and need the Trigger and Root cause of its lessons; a script names a\npage in an error and you say why it failed. Name every page you open in the report,\nwith the reason."
        new: "Your inputs are four: `vault/raw/<today>/handoff.md`, every `materialize.yaml`\nthat `guppi materialize` names on its stdout, the four `vault/wiki/<category>-index.md`\nfiles, and `vault/wiki/tags.md`. Open a page under `vault/wiki/` for four reasons only:\nan index line does not tell you whether a create is the same page or a near one; an\nindex line does not tell you whether a lesson shares its root cause with another lesson\nor an Insight, whether or not you then write one; a script names a page in an error\nand you say why it failed; the brief needs a fact no input carries — the status of an\nEstimate, the severity of an Insight. Name every page you open in the report, with\nthe reason and the outcome."
    change: "four indexes; four reasons to open a page, each by the question asked, named with reason and outcome"
  - slug: rule-synthesis
    replace:
      - old: "Read the Trigger and Root cause of the lessons you cluster and name those pages in\nthe report."
        new: "When an index line does not settle whether a lesson shares a root cause, read the\nTrigger and Root cause of the candidate and name the page in the report with the\noutcome, clustered or not."
    change: "a candidate lesson is read when the index line is not enough, clustered or not, and named with the outcome"
  - slug: rule-brief
    replace:
      - old: "Write facts and flags only."
        new: "When a fact the brief needs is in no input — the status of an Estimate, the severity\nof an Insight — read it from the page and name the page in the report. Write facts\nand flags only."
    change: "a fact no input carries is read from the page and named"
  - slug: estimate-documentation-completes
    set: {status: pending}
    replace:
      - old: "the five\nindexes and tags.md, plus the wiki pages it names in the report with one of the\nthree reasons of its frame (same or near, the lessons of an Insight, a script's\nerror)"
        new: "the four\nindexes and tags.md, plus the wiki pages it names in the report with one of the\nfour reasons of its frame (same or near; a candidate cluster; a script's error; a\nfact for the brief) and the outcome"
    change: "four indexes; four reasons; outcome named"
  - slug: estimate-synthesis-clusters
    set: {status: pending}
    replace:
      - old: "every lesson page read is named in the report as a\nchild of the Insight written"
        new: "every lesson page read is named in the report with\nthe outcome: the Insight it joined, or none and why"
    change: "a lesson page read is named with its outcome, clustered or not"
```

## Case 55 — `rule-ledger-write`: the `hi` window across midnight, and a reply that ends in a tool call

> **context:**
> Хук ledger дважды терял ратифицированные строки. Вчера: реплики Cases 48 и 49 кончались `/pre-task` и `ExitPlanMode`, `Stop` не сработал (Case 51, отложен). Сегодня: сессия перешла полночь, хук искал `session-start` и `hi` в сегодняшнем логе; 44 строки Case 53 ушли только после resume.

> **problem:**
> Окно `hi` привязано к файлу одного дня; хук привязан к одному событию, которого у части реплик нет.

> **recommend:**
> Два sub-cases на одном правиле. 55.1 — склейка логов по датам. 55.2 — `Stop` смотрит назад по транскрипту, без нового события: `MessageDisplay` не может отказать и сказать (`lesson-hooks-messagedisplay-cannot-block`), `PostToolUse` не несёт реплику.

> **given:**
> `ledger.py`: `log_path(project_dir, now)` — только `raw/<today>/event_log.md`; `hi_recorded` требует `session-start` своей сессии до `hi` в одном тексте. `reply_text` берёт `last_assistant_message` из payload `Stop`; payload несёт и `transcript_path` (`lesson-hooks-stop-payload`).
> **＋** `existing_bodies` не пишет строку, чей текст уже в ledger.
> **＋** `rule-ledger-write` `built`, `estimate-ledger-write-lifts` `passed`; по 53.2 критерий правится, `pending`. `deferred_by` Case 51 снимается `{supersedes:case 51}`.
> **＋** Уроки: `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`, `lesson-ledger-hook-hi-lost-at-midnight`.
> **－** Формат строки, тег `LEDGER`, отказ без `hi`, `settings.json` — без изменений.

### Case 55.1 — The `hi` window is the session's, not the day's

> **when:**
> Хук `Stop` проверяет, открыта ли сессия.

> **then:**
> Хук читает `raw/<date>/event_log.md` всех дат от сегодняшней назад до первой с `session-start` его сессии и склеивает их в порядке дат; окно `hi` считается по склейке тем же правилом.
> **＋** Нет ни одной даты со стартом этой сессии — отказ как сейчас.
> **＋** Тест: старт и `hi` во вчерашнем файле, сегодня только `tool` — строки пишутся в сегодняшний ledger.
> **－** Дальше самой ранней даты со стартом хук не идёт.

> **ratification:** ratified 2026-09-11.

```then
update:
  - slug: rule-ledger-write
    replace:
      - old: "**Checks the event log first.** The session is a working one when a `hi` line follows a\n`session-start` line of this session's id, with no other session's start in between."
        new: "**Checks the event log first.** The log it reads is `raw/<date>/event_log.md` of every\ndate from today back to the first that holds a `session-start` of this session, joined in\ndate order; a session that crosses midnight keeps its window. The session is a working one\nwhen a `hi` line follows a `session-start` line of this session's id, with no other\nsession's start in between."
    change: "the hi window spans the dates of the session: the event logs back to its start are joined"
  - slug: estimate-ledger-write-lifts
    set: {status: pending}
    replace:
      - old: "In a\nlive session, the last lines of this slice reach `raw/2026-09-09/ledger.md` written by the\nhook, not by hand."
        new: "With the `session-start` and the `hi` in yesterday's event log and only `tool` lines\nin today's, the lines are written into today's ledger. In a\nlive session, the last lines of this slice reach `raw/2026-09-09/ledger.md` written by the\nhook, not by hand."
    change: "the midnight window added to the criterion; pending until the reading"
```

### Case 55.2 — The `Stop` hook reads the whole session back

> **when:**
> Хук `Stop` срабатывает.

> **then:**
> Хук читает все сообщения ассистента этой сессии из `transcript_path`, в порядке хода, и берёт строки из каждого блока `LEDGER`; строка, чьего текста в сегодняшнем ledger нет, пишется со временем этого `Stop`.
> **＋** `last_assistant_message` — запасной вход, когда транскрипта нет или он не читается.
> **＋** Реплика, кончившаяся `Skill` или `ExitPlanMode`, попадает в ledger на следующем `Stop` той же сессии.
> **＋** Критерий: реплика с блоком `LEDGER`, кончающаяся `/pre-task`, оказывается в ledger один раз после следующего `Stop`; живое чтение в этой сессии.
> **－** `settings.json`, `rule-hook-registry` не меняются.
> **－** Последняя реплика сессии, кончившаяся tool-вызовом без дальнейшего `Stop`, остаётся потерянной; её видит Retro.

> **ratification:** ratified 2026-09-11.

```then
update:
  - slug: rule-ledger-write
    replace:
      - old: "Reads the reply that just finished, finds every line that starts\nwith `- decision[`, `- estimate[` or `- lesson[` **inside a fenced block opened with the\n`LEDGER` tag**"
        new: "Reads every assistant message of this session from `transcript_path`, in order,\nfalling back to the reply that just finished (`last_assistant_message`) when the\ntranscript is absent or unreadable, and finds every line that starts with `- decision[`,\n`- estimate[` or `- lesson[` **inside a fenced block opened with the `LEDGER` tag**"
      - old: "A line whose text is already in today's ledger"
        new: "So a reply that ended in a tool call (`Skill`, `ExitPlanMode`), which has no `Stop` of\nits own, reaches the ledger at the next `Stop` of the session, with that time; only the\nlast reply of a session can still be lost, and Retro sees it. A line whose text is already\nin today's ledger"
    change: "the hi window spans the dates of the session; every LEDGER block of the session's transcript is read at each Stop, the last reply as fallback"
  - slug: estimate-ledger-write-lifts
    set: {status: pending}
    replace:
      - old: "the lines are written into today's ledger. In a\nlive session,"
        new: "the lines are written into today's ledger. A reply carrying a `LEDGER` block\nthat ends in `/pre-task` reaches the ledger once, at the next `Stop` of the session. In a\nlive session,"
    change: "the transcript read-back added to the criterion; pending until the live reading"
```

## Case 56 — Retro is an analysis: a frontier, then lessons, readings and short defers

> **context:**
> Case 50 отложил переосмысление Retro без текста; восстановлено из handoff G (строки 104–107) и дополнения владельца: Retro открывается фронтиром работ, замечания агента и человека, исход каждого — строка, решения только `defer` в короткой форме.

> **problem:**
> `rule-retro` читается как малый Plan Mode. Нет открывающего фронтира, нет шага чтений, нет пути «откатить и отложить». Полная форма Case для defer избыточна; Decision-страница по 52.1 требует Given и When, которых у отсрочки нет.

> **recommend:**
> Render `rule-retro` переписан; короткая форма defer в `case-schema.md`; Given и When необязательны у Decision, где все `kind` — `defer`; критерий дополнен. Закрывает Case 50.

> **given:**
> `rule-retro` Render: контекст загружает `make test`, `make style`, ledger дня; «Discuss … in the Case form»; правки в счёт ratified; остальное defer; красные тесты — урок; три списка, коммит, `/handoff`.
> **＋** 52.1: Decision body Given, When required. 52.2: Retro Case — семь секций. `materialize` метит отсутствующие секции `incomplete`.
> **＋** `estimate-retro-loads` `passed`; по 53.2 дополняется, `pending`. `rule-retro-commit` требует чистое дерево.
> **－** Три списка, коммит, `/handoff`, загрузка контекста — без изменений.

> **when:**
> Человек вызывает `/retro`; в Retro возникает замечание; красные тесты; Estimates этой сессии в `pending` с законченной работой.

> **then:**
> Первое сообщение Retro — фронтир: ратифицировано (строки ledger по Case), сделано и не сделано против Spec, замечено агентом. Человек добавляет своё.
> **＋** Каждый пункт кончается одним из четырёх: `lesson[...]`, `estimate[...]`, короткий `defer`, или запись в handoff.
> **＋** Короткий defer: `## Case N` под `## Retro` с `context`, `problem` и блоком `defer` с `purpose`.
> **＋** Decision-страница: `## Given`, `## When` optional; `materialize` метит их отсутствие `incomplete` только когда среди `kind` есть не-`defer`.
> **＋** Retro снимает чтения Estimates с законченной работой; несъёмная названа в handoff.
> **＋** Красные тесты: чинить в счёт ratified, иначе `git diff` в `raw/<date>/patch-<slug>.diff`, откат, короткий `defer`. В обоих случаях `lesson[error]`; handoff зелёный.
> **＋** `estimate-retro-loads` дополнен, `pending`.
> **－** Правки в счёт ratified остаются разрешены.

> **ratification:** ratified 2026-09-11 («попробуем так, если что — поменяем»).

```then
update:
  - slug: rule-retro
    sections:
      Render: |
        <!-- rule-retro -->
        ---
        name: retro
        description: Review this session's work — tests, style, the ledger — before the commit and the handoff.
        disable-model-invocation: true
        ---
        Recorded: !`uv run guppi event retro --session "${CLAUDE_SESSION_ID:-}"`

        Tests: !`make test`

        Style: !`make style`

        Ledger of today: !`cat "vault/raw/$(date +%F)/ledger.md"`

        Retro is an analysis of this session, not planning. Open with the frontier, in one
        message and with no read call: what was ratified (the ledger lines of today grouped
        by Case, one line per Case); what got done and what did not, against the Spec; what
        you noticed during Work Mode, as a numbered list — bugs, forks, a contract that
        turned out imprecise. The person adds their own observations. Every item, theirs or
        yours, ends in one of four ways: a `- lesson[...]` line; a `- estimate[...]` line, a
        reading of an Estimate whose work is finished; a short defer; or a note for the
        handoff. Retro ratifies no other decision: a `create`, `update` or `delete` waits for
        the next Plan Mode.

        A short defer is a Case in the short form, appended to `vault/raw/<date>/spec.md`
        under a `## Retro` heading before its ledger line: `## Case N`, `context`, `problem`,
        and a `defer` block with `purpose`; no `recommend`, `given`, `when` or `then`. A defer
        line without its Case is marked incomplete by materialize.

        Edit code only when the edit finishes work that traces to a line of today's ledger.
        Red tests: fix now when the fix finishes ratified work; otherwise save the change
        with `git diff` into `raw/<date>/patch-<slug>.diff`, revert it, and write a short
        defer naming the patch. Either way write a `- lesson[error][...]` line whose root
        cause says why Retro was reached with a regression; the handoff still needs green.
        `gh` is not available: name a deferred bug in the handoff, so the brief carries it.
        Do not run `make lint` here: the vault is written after handoff, by the librarian.

        Take the readings of this session's Estimates whose work is finished and write their
        lines; name in the handoff any Estimate whose reading cannot be taken yet.

        Close with three lists: every ratification of this session, one line each; what
        got done; what did not. When the person approves, commit (`make style` clean,
        `make test` green), then call `/handoff`.
        <!-- /rule-retro -->
    change: "Retro opens with the frontier; every item ends as a lesson, a reading, a short defer or a handoff note; red tests are fixed or reverted into a patch; readings are a step"
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "a short form for Retro: ## Case N with context, problem and a defer block with purpose, appended to spec.md under ## Retro; the seven-section form stays the form of Plan Mode; replaces the 52.2 clause"
  - slug: decisions-schema-yaml
    file: vault/wiki/decisions/schema.yaml
    change: "## Given and ## When move from required to optional; a note: required by materialize when any kind is not defer"
  - slug: decisions-schema
    file: vault/wiki/decisions/schema.md
    change: "Given and When rows: optional on a page whose every kind is defer; the short-form example"
  - slug: rule-materialize
    replace:
      - old: "One decision entry per Case: `decision: decision-case-<N>`, `case_text` (the seven quoted sections of the Case, verbatim, in the language of the Spec), `targets` (one item per line of the Case)."
        new: "One decision entry per Case: `decision: decision-case-<N>`, `case_text` (the quoted sections of the Case, verbatim, in the language of the Spec), `targets` (one item per line of the Case); a Case whose text lacks `given` or `when` is marked `incomplete` only when a kind other than `defer` is among its lines, since the short form of Retro has neither."
    change: "a decision entry lacks given or when: incomplete only when a kind other than defer is among its lines"
  - slug: estimate-retro-loads
    set: {status: pending}
    sections:
      Criterion: |
        After a live /retro: the first turn's context holds the output of make test, make
        style and today's ledger with no read-tool call; event_log.md carries a retro line;
        the first message is the frontier in three blocks — ratified by Case, done and not
        done against the Spec, noticed — with no read call; every item raised by either side
        ends as a lesson line, an estimate line, a short defer with its Case under ## Retro in
        spec.md, or a handoff note; no decision line other than defer is written in Retro;
        every Estimate whose work is finished has its reading line; a red test ends as a fix
        that traces to today's ledger or as a patch in raw/ with a short defer, with a
        lesson[error] either way; every edit made in Retro traces to a line of today's ledger;
        the closing reply lists the ratifications, the done and the not done; the commit
        precedes the /handoff call.
    change: "the frontier, the four outcomes, the readings and the red-test paths added; pending until the next live /retro"
```

## Case 57 — Pre-task findings: the pages the Cases forgot

> **context:**
> Cases 52–56 меняют форму Decision, число индексов, чтения библиотекаря, форму Retro и `spec.md`. Pre-task (`ask-guppi`, 2026-09-11) нашёл страницы, которые описывают то же и не названы ни в одной строке.

> **problem:**
> §5 и §10 `index.md` описывают старую форму; `CLAUDE.md` требует семь секций для любого ответа; `rule-cleanup` перестраивает пять индексов; `rule-spec-capture` считает хук единственным писателем `spec.md`; критерии `estimate-lint-catches` и `estimate-cleanup-moves` не знают новых классов и четырёх файлов.

> **recommend:**
> Семь `update`; три критерия, уже названные в 53, расширены в их блоках.

> **given:**
> `index.md` §5 строки 211, 225 (`targets`, `category` explicitly); §10 строка 333 («That is all … not the pages themselves»). `CLAUDE.md` строка 46: «One reply is one Case, in the seven sections». `rule-cleanup`: пять индексов, `estimates` всех живых страниц. `rule-spec-capture`: один писатель. `estimate-lint-catches`, `estimate-cleanup-moves`, `estimate-spec-capture-appends` — `passed`, по 53.2 `pending`.
> **－** Ворота «Research `passed` до Insight» уходят без замены (53.1).

> **when:**
> Кто-то читает `index.md`, `CLAUDE.md`, `rule-cleanup`, `rule-spec-capture`; `guppi cleanup` и `guppi lint` идут; снимаются их чтения.

> **then:**
> §5: `kind` и `target_slug` по позициям, категория из префикса; Case, берущий отложенное, пишет `{supersedes:case N}`, и `deferred_by` снимается. §10: четыре причины фрейма. §1: четыре индекса.
> **＋** `CLAUDE.md`: семь секций — форма Plan Mode; короткая форма Retro.
> **＋** `rule-cleanup`: четыре индекса; slug архивированной Estimate снимается из `estimates` Entity и Rule. `estimate-cleanup-moves` `pending`.
> **＋** `rule-spec-capture`: два писателя `spec.md`. `estimate-spec-capture-appends` `pending`.
> **＋** `estimate-lint-catches`: классы 52 и 53, `pending`.

> **ratification:** ratified 2026-09-11.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§5 line 211: one page per Case with kind and target_slug aligned by position; line 225: the category is derived from the slug prefix, never written; the Case that takes up a deferred item writes {supersedes:case N} and deferred_by is cleared; §10 Reads: the four inputs, and a page for one of the four reasons of the librarian's frame (case 54); §1: the four index files"
  - slug: claude-md
    file: CLAUDE.md
    change: "Case protocol: the seven sections are the form of Plan Mode; at Retro a defer is the short form — context, problem, a defer block with purpose — appended to spec.md under ## Retro"
  - slug: rule-cleanup
    replace:
      - old: "The slug is removed from the `children` and `estimates` lists of live pages, their sections are rebuilt and they get a History line;"
        new: "The slug is removed from the `children` lists of live pages and from the `estimates` lists of entities and rules, their sections are rebuilt and they get a History line;"
      - old: "Then the indexes are rewritten with the writer of `guppi index`."
        new: "Then the four indexes are rewritten with the writer of `guppi index`; an archived Estimate leaves no line, since estimates have none."
    change: "four indexes; estimates lists of entities and rules only"
  - slug: estimate-cleanup-moves
    set: {status: pending}
    replace:
      - old: "its slug leaves the children and estimates lists of live pages and their sections, with a History line there;"
        new: "its slug leaves the children lists of live pages and the estimates lists of entities and rules, and their sections, with a History line there;"
      - old: "the category indexes are rewritten without the moved page;"
        new: "the four category indexes are rewritten without the moved page, and an archived Estimate leaves no line anywhere;"
    change: "four indexes; estimates lists of entities and rules only; pending until the live run"
  - slug: rule-spec-capture
    sections:
      How it works: |
        `uv run guppi spec` on `PostToolUse` of `ExitPlanMode` appends the approved plan to
        `raw/<date>/spec.md`: a `---` separator when the file has content, the stamp
        `<!-- approved HH:MM:SS · session xxxxxxxx -->`, the plan text, once. The file has
        a second writer: at Retro the agent appends the short-form Cases under a `## Retro`
        heading, before their ledger lines (`rule-retro`). `guppi materialize` reads both by
        their `## Case N` headings, so a Retro defer gets its Decision page like any other.
    change: "spec.md has two writers: the hook at ExitPlanMode and the agent at Retro under ## Retro"
  - slug: estimate-spec-capture-appends
    set: {status: pending}
    replace:
      - old: "Live: the next plan approval lands in `raw/<date>/spec.md` by the hook, not by hand, and the reading records what a rejected plan produces."
        new: "A `## Retro` section appended by the agent stays intact under a later approval's separator, and materialize reads its Cases. Live: the next plan approval lands in `raw/<date>/spec.md` by the hook, not by hand, and the reading records what a rejected plan produces."
    change: "the Retro section survives a later approval; pending until the live reading"
  - slug: estimate-lint-catches
    set: {status: pending}
    replace:
      - old: "the two Method classes (case 26.2) are seeded too."
        new: "the two Method classes (case 26.2) are seeded too, and the classes of cases 52 and 53: decision lists of unequal length, a target_slug naming no page, a deferred_by naming no decision, a History wikilink resolving to nothing, an estimate whose target is not an entity or a rule; a lesson without estimates is not a finding."
    change: "the classes of cases 52 and 53 seeded; a lesson without estimates is clean; pending until the suite"
```
