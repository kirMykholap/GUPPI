## Case 513 — A Decision page keeps the Problem, and the Case file keeps the rest

> **context:**
> When a Case is ratified, the librarian's `guppi generate` writes a Decision page into `vault/wiki/decisions/`. Today the page copies three sections of the Case: `## Context`, `## Problem` and `## Given`. It adds the lists of the pages the Case created, updated, deleted or deferred, `## Deferred` for a Case that put something off, and `## History`. Since session 2026-09-27/1819 (case 457), the `SubagentStop` hook of `rule-case-check` also writes every Case that `case-guppi` builds to `raw/<date>/<HHMM>/cases/case-<N>.md`, with all eight sections. The session folder then moves whole into `vault/archive/<sprint>/<date>/<HHMM>/raw/`. So the same text is stored three times: in the Case file, in `spec.md` (which holds no `recommend`) and on the Decision page. The Context is the longest of these copies and is written for the agent. For example, the page of case 506.2 repeats a context of several hundred words that its Case file already holds.
> In one round the person accepted every recommendation. A new Decision page keeps only `## Problem`, the lists, `## Deferred` and `## History`. The schema's text says where the Case file lies, and no new field is added. The page of a short-form deferred decision keeps `## Context`, because the main agent writes that form and it gets no Case file. The pages already written are not rewritten, so `## Context` becomes optional in the schema.
> What `case-guppi` found in the frame. I checked the facts the person was given. `case-510.md` holds all eight sections. `spec.md` holds no `recommend`. The archive holds Case files from `2026-09-27/1819` on, and the older sessions hold only `spec.md`. `rule-decisions-schema` says that `recommend` is "recoverable from the archived ledger", which is false today. 513.1 changes that sentence, the required sections, the `## Context` and `## Given` descriptions, the `origin` field and the example page. It also replaces the Criterion and the `method` of `estimate-decisions-schema-checked`. `estimate-generate-writes-the-decision-page` names the body `## Context` and `## Problem`, so 513.2 replaces its Criterion whole. `estimate-generate-writes-the-given` promises a `## Given` that is no longer written, so 513.2 deletes it and carries its `－` line on the old pages into the other Criterion. The cascade takes it out of the `estimates` of `rule-page-generation`, as in case 506.2. That rule's Purpose names no body section, so the rule stands. Two sentences of `rule-case-protocol` say that `given` "stays in the Case and on the Decision page", so 513.3 changes them. That rule's Estimates speak of the form of a Case, not of a Decision page, and an `update` of its Render touches no Estimate of the live reading (case 378.5).
> The person accepted four fixes from pre-spec. First, a Case superseded in its own session keeps its two-line body, `## Context` included (case 299.4), and `decision-case-511.2` of this session gets that body. So the schema text of 513.1 and its `then` name that body next to the short form. Second, the `method` of the Estimate said the pages of Cases 1–28 lack "Context and Problem". With Context optional, only Problem is a finding on them, so 513.1 sets the `method` anew. Third, I checked `## Given` on the live Decision pages. The pages of Cases before 201 carry it, from the model of case 52.1. The pages of Cases 201 to 375 carry none. The pages from 376 on carry it again. The new description says exactly this and no longer says "before case 378.3". Fourth, the sentence on this session's pages below is corrected.
> What the check of the answer notes, and why each note stands. Three Criterion lines are not carried word for word, on purpose. In 513.1 the line on the sections moves `## Context` from the required list to the optional one. In 513.2 the body line names `## Problem` alone. The old `－` line on no `## When` and no `## Criterion` becomes one `－` line that also says no `## Given`, and no `## Context` for a Case with `given`. Every other line is kept word for word. Three `then` lines of 513.2 share words with 513.1: the `## Context` of a Case without `given`, the sections the page does not hold, and the old pages that are not rewritten. This is expected. 513.1 promises what the schema file says and what lint accepts, while 513.2 promises what `generate` writes and leaves alone. They are separate promises with separate tests.
> Several sentences stay true and stand. `ask-guppi.md` reads the `## Problem` of a deferred decision, and that section stays. The case schema says that a deferred decision is taken up "from its page — `context` and `problem` as they stand". That page keeps its Context. `estimate-lint-catches`, `estimate-generate-renames` and `estimate-generate-cascades` speak of Decision pages but not of their body sections.
> Code and timing. `guppi/materialize.py` still lifts `context` and `given` into `case_text`, and `generate` uses `given` to tell the short form apart. The code changes in Work Mode, and the yaml is rendered in the librarian's run. So the pages of 510, 511.1 and 512 to 516 are written without Context. 511.2, superseded in its session, gets the two-line body, and 517 and 518, in the short form, keep Context. A `make lint` run before the render reports `missing section ## Context` on the pages written without it. `lint` only goes red, so no old form is kept, and that red is a note for the handoff by `rule-retro`. The Case creates no page, so no vault query was run.
> Not done: the old pages are not rewritten; `materialize`, `ask-guppi` and the archive are unchanged; no `case_file` field is added; the short form still writes no Case file.

> **problem:**
> The Decision page repeats the Case's Context and Given, which the Case file now keeps whole. The repeated Context is long, written for the agent, and makes the page hard to read. The schema also sends a reader to the ledger for the recommendation, but the ledger does not hold it.

> **recommend:**
> A new Decision page keeps `## Problem`, the one paragraph that says why the decision was needed, at the end of every link. It leaves Context and Given to the Case file, and the schema says where that file is. The short-form deferred decision keeps its Context, since it has no Case file. Old pages stay as they are. Rejected: keeping all three sections, which stores the text three times; adding a line per changed page, which repeats the `change` each target already gets in its History; lists only, which sends every "why" into the archive; and a `case_file` field, which goes stale when the folder moves to the archive.

### Case 513.1 — The Decision schema makes Context optional and points to the Case file

> **given:**
> `rule-decisions-schema` — the rule; its Render is the schema of a Decision page
> **＋** `vault/wiki/decisions/schema.yaml` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `guppi/lint.py` — reads the lists of the file for every page of `vault/wiki/decisions/`
> **＋** `cases/case-<N>.md` — the Case file in the folder of `origin`, which the schema names as the whole record of a Case
> **＋** `estimate-decisions-schema-checked` — the promise; its Criterion and `method` are replaced
> **＋** `tests/test_schemas.py` — the tests the reading runs

> **when:**
> `guppi render` writes `vault/wiki/decisions/schema.yaml` from `rule-decisions-schema`, and `guppi lint` reads a page of `vault/wiki/decisions/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, case, status, origin, sprint, created, tags`; optional `create, update, delete, defer, source, supersedes, superseded_by`; values `status: current | superseded | archived`; the sections `## Problem` and `## History` required, `## Context`, `## Given`, `## When`, `## Criterion`, `## Deferred`, `## Note` optional.
> **＋** A Decision page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list or lacking a required section has one finding per defect.
> **＋** A Decision page without `## Context` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, the fields deliberately absent and the body paragraph; `examples` holds the example page.
> **＋** The file says that the History of a Decision takes `created`, `superseded by` and one `updated:` line of a Case that signs its text after the fact.
> **＋** The file says that the Case file, `cases/case-<N>.md` in the folder of `origin` with N the id of the top-level Case, holds the whole Case, `recommend` included, and moves into the archive with its session.
> **＋** The file says that a new page carries `## Context` only for a Case without `given`, the short form of a deferred decision, and in the two-line body of a Case superseded in its own session; that it never carries `## Given`; and that the pages written before keep the sections they carry.
> **－** The example page holds no `## Context` and no `## Given`.

> **tasks:**
> - [ ] update `rule-decisions-schema`
>   - old: `Either way the original is conversation history, recoverable from the archived ledger.`
>   - new: `` Either way the original stays in the Case file, `cases/case-<N>.md` in the folder of `origin` (case 513). ``
>   - old: `The body is the Case that produced it, minus what belongs to the conversation rather than the decision.`
>   - new: `` The body is the `problem` of the Case that produced it: the one paragraph a reader needs at the end of a link. The rest of the Case — `context`, `recommend`, `given`, `when`, `then`, `tasks`, `ratification` — stays in its Case file. A Case without `given`, the short form of a deferred decision, has no Case file, so its page keeps `## Context` as well; the page of a Case superseded in its own session has the two-line body of `## Context` and `## Problem` that names the superseding Decision (case 299.4). A page written before case 513 keeps the sections it carries and is not rewritten (case 513). ``
>   - old: `required: ["## Context", "## Problem", "## History"]`
>   - new: `required: ["## Problem", "## History"]`
>   - old: `optional: ["## Given", "## When",`
>   - new: `optional: ["## Context", "## Given", "## When",`
>   - old: `The folder also holds the Spec with the Case.`
>   - new: `` The folder also holds the Spec with the Case and, for a Case built by `case-guppi` from session 2026-09-27/1819 on, its Case file `cases/case-<N>.md` with every section, N the id of the top-level Case; once the session is archived, the folder lies under `vault/archive/<sprint>/` (case 513). ``
>   - old: `required. What this is about.`
>   - new: `` optional. What this is about. Written for a Case without `given`, the short form of a deferred decision, which has no Case file, and in the two-line body of a Case superseded in its own session (case 299.4); kept on the pages written before case 513; any other Case keeps it in its Case file (case 513). ``
>   - old: `` written by `generate` on the page of a Case that has one (case 378.3); a page written between case 201.2 and case 378.3 carries none. ``
>   - new: `` written by `generate`, before case 513, on the page of a Case that had one: the pages of Cases before 201 carry it by the model of case 52.1, and the pages from case 376 on by case 378.3; the pages of Cases 201 to 375 carry none. A page written after case 513 carries none, and the Case file holds it (case 513). ``
>   - old: `## Context The site has checkout but no cart — items go straight from the catalogue to payment. ## Problem`
>   - new: `## Problem`
>   - old: `` ## Given `entity-cart` — the page this Case creates. **＋** `entity-checkout` — the page the cart precedes. ## History ``
>   - new: `## History`
>   - change: `a new page carries Problem and no Context or Given, a short-form defer and a Case superseded in its session keep Context; the Case file named as the whole record, recommend included (case 513.1)`
> - [ ] update `estimate-decisions-schema-checked`
>   - set: `{status: pending, method: "pytest tests/test_schemas.py -k decisions on the live vault/wiki/decisions/schema.yaml — a page in the shape, a page without ## Context, then one defect at a time; the live reading make lint, no schema finding on wiki/decisions/ but the pages of Cases 1–28 without Problem (Slice 5)"}`
>   - change: `the Criterion replaced whole and the method set anew — Context optional, the Case file named, the example without Context and Given (case 513.1)`
> - [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] `tests/test_schemas.py`: a test that a Decision page without `## Context` has no finding against the live `schema.yaml`, skipped until the librarian renders the file of 513.1
> - [ ] read `estimate-decisions-schema-checked` — `pytest tests/test_schemas.py -k decisions`, then `make lint` with no `schema` finding on `vault/wiki/decisions/` but the pages of Cases 1–28, at a later session

> **ratification:**
> ```
> - decision[case 513.1][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 513.1][update][estimate-decisions-schema-checked]{ref:estimate-decisions-schema-checked}
> ```

### Case 513.2 — `generate` writes the Problem, and Context only for a short-form defer

> **given:**
> `guppi/generate.py` — `decision` and the docstring paragraph on the Decision page
> **＋** `tests/test_generate.py` — the tests of the Decision page and their fixture schema
> **＋** `vault/raw/<date>/<HHMM>/materialize.yaml` — the input; its `decisions` records carry `case_text`
> **＋** `vault/wiki/decisions/decision-case-<N>.md` — the Decision page of a Case
> **＋** `estimate-generate-writes-the-decision-page` — the promise; its Criterion is replaced whole
> **＋** `estimate-generate-writes-the-given` — the promise of `## Given`, deleted
> **＋** `rule-page-generation` — the rule of `generate`; the cascade drops the deleted Estimate from its `estimates`

> **when:**
> `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

> **then:**
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` from `case_text`, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** A Case whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded` and appends to its `superseded_by`. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
> **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given`.
> **－** The Decision pages already written are not rewritten.

> **tasks:**
> - [ ] update `estimate-generate-writes-the-decision-page`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the body is Problem, Context only for a Case without given, no Given (case 513.2)`
> - [ ] delete `estimate-generate-writes-the-given`
>   - impact: `A new Decision page carries no Given; the Case file holds it (case 513). The promise that no Given is written and old pages are not rewritten stands in estimate-generate-writes-the-decision-page; rule-page-generation loses it from estimates by the cascade`
> - [ ] `guppi/generate.py`: `decision` writes `## Problem` from `case_text`, `## Context` only when `case_text` has no `given`, and no `## Given`; the docstring paragraph on the Decision page says so
> - [ ] `tests/test_generate.py`: the Decision-page tests assert `## Problem` then `## History` with no `## Context` or `## Given` for a Case with `given`; `## Context` then `## Problem` for a Case without `given`; the fixture schema takes `## Context` as optional
> - [ ] read `estimate-generate-writes-the-decision-page` — `pytest tests/test_generate.py`, the tests of the Decision page, and the pages of the librarian's run, at a later session

> **ratification:**
> ```
> - decision[case 513.2][update][estimate-generate-writes-the-decision-page]{ref:estimate-generate-writes-the-decision-page}
> - decision[case 513.2][delete][estimate-generate-writes-the-given]{ref:estimate-generate-writes-the-given}
> ```

### Case 513.3 — The case schema keeps `given` in the Case, not on the Decision page

> **given:**
> `rule-case-protocol` — the rule; its Render is the case schema
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render

> **when:**
> `case-guppi` or the main agent reads `vault/wiki/case-schema.md`.

> **then:**
> The row of `given` and the paragraph on `when` and `then` say that `given` stays in the Case, in its Case file and in the Spec, and not on a Decision page.
> **－** The row of `recommend` still says that it is not carried onto the Decision page.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `It stays in the Case and on the Decision page and never enters an Estimate (case 378.1).`
>   - new: `It stays in the Case, in its Case file and in the Spec, and never enters an Estimate or a Decision page (cases 378.1, 513).`
>   - old: `` `given` stays in the Case and on the Decision page, so `when` names ``
>   - new: `` `given` stays in the Case file and in the Spec, so `when` names ``
>   - change: `given stays in the Case file and the Spec, not on a Decision page (case 513.3)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`

> **ratification:**
> ```
> - decision[case 513.3][update][rule-case-protocol]{ref:rule-case-protocol}
> ```
