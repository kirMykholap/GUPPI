## Case 969 — A one-time Estimate is marked and stands on the sprint page

> **context:**
> Most Estimates promise a behaviour that lasts. A few check one state of the data once, such as `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` of Case 962, whose `purpose` ends "a one-time check of this data" and which the ledger of this session reads `passed`. Nothing tells the two kinds apart. A one-time check stands on the rule it checks, so `cascade` of `.guppi/guppi/generate.py`, read whole, keeps that rule `draft` while it is `pending`, and `is_draft_core` of `.guppi/guppi/pages.py`, read whole, makes such a rule with `core: true` stop `guppi ship`. Once it passes it stays live after the close, since `Close` of `.guppi/guppi/sprint_close.py`, read with `judge_estimates` and `settled`, moves the sprint page and the Estimates it lists and leaves every other `passed` Estimate. And `ships` of `.guppi/guppi/ship.py`, read whole with `plan`, writes a `passed` Estimate whose target carries `core: true` into the clean version; `rule-backlog` and `entity-guppi` carry it, so both known one-time checks would ship. Case 963 put the question off at session 0431, the person liking both ways the main agent named. Now the person chose both together: a one-time Estimate targets the live sprint page and carries `once: true`, and lint reports one whose target is not a sprint page. The sprint page `entity-sprint-plugin` has no `core: true`, so its Estimates never ship, keep no shipped page `draft` and leave with it at the close; a one-time Estimate still `pending` at the close is read or archived unread, as for every Estimate of the sprint page. The sentence of `entity-sprint` that its Estimates are the Definition of done of a sprint stands: a one-time check is part of that done. Case 969.1 adds the field to `rule-estimates-schema` and a sentence to `rule-case-protocol`, since `case-guppi` reads `case-schema.md` and not the schema of Estimates. The pair on `rule-case-protocol` sits in `## The then block lives in the Spec`, in the paragraph on a `create`, read whole: its `old` ends the sentence that names an Estimate whose target is a sprint page the exception whose `method` may wait for a later session of that sprint, up to the session that closes it, and the new sentence after it names the one-time Estimate that stands on that page; no other Case of this session writes into that paragraph. Its decision line on `rule-estimates-schema` carries `{supersedes:case 963}`, which retires the one defer of that page. The `update` of the Render of `rule-case-protocol` touches no Estimate of the live reading, `estimate-case-protocol-loaded`, and `estimate-case-protocol-case-form` speaks of the form of a Case, not of one-time Estimates, so both stand. The Criterion of `estimate-estimates-schema-checked` lists the optional fields and values, which the field makes false, so it is replaced whole; its `purpose` states the shape of the rendered schema in general and stands, and its `method` is set anew to wait for the librarian's run that renders the schema, since the live file gains `once` only at that render and the new tests of `once` skip before it, so the reading cannot be taken at the Retro of this session. Case 968 changes another sentence of `case-schema.md`, in `## Language`, and reads a `create` value whose allowed values hold no text as YAML from the schema on disk; `once` becomes such a field at the render, and no Case of this session creates an Estimate with `once`, so the order does not matter. The finished file of Case 968, read whole after its build ended, holds these claims: it moves the comparison of `check_schema` with the allowed values into `materialize.py`, which `check_status` does not use, and its own `context` names the sentence of Case 969.1 in `## The then block lives in the Spec` and finds no contradiction. The finished file of Case 967, read whole after its build ended, imports `links_of` of `lint.py` unchanged, writes into neither `rule-estimates-schema` nor `rule-case-protocol`, changes no function of `lint.py`, and creates no Estimate with `once`. Case 969.2 puts the finding into `check_status` of `.guppi/guppi/lint.py`, read whole with `check_schema` and `unmet_conditions`, beside the finding of a target that is no entity or rule. A Grep `SPRINT_PAGE|entity-sprint-` over `.guppi/guppi/` printed `prespec.py`, `generate.py`, `materialize.py`, `sprint_close.py`, `ledger.py`, `lint.py`, `sprint.py` and `backlog.py`; `is_sprint_page` of `ledger.py`, read whole, is the one judgment of a sprint page, which `materialize.py`, `prespec.py` and `sprint.py` import, so lint imports it too, and `ledger.py` imports only `event` and `pages`, so no import loop follows. A Grep `"once"|\bonce:` over `.guppi/guppi/` printed `ledger.py` and `prespec.py`, both in prose, so no code judges the field today. `/pre-spec` does not report a `create` with `once: true` whose `ref` is no sprint page; lint reports it once the page stands, and a check at the plan is not done. Case 969.3 archives the two known one-time Estimates: `estimate-guppi-keeps-no-defer-of-its-shape` stands `passed` on its page, and `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` stands `pending` on its page and `passed` only in the first line of the ledger of this session, a reading not yet applied; a `delete` archives either status; `estimate-cleanup-moves`, `passed`, promises that an archived page moves under the archive and its slug leaves the `estimates` of entities and rules, so it checks the move and its Criterion stands. A Grep of the two slugs over `vault/wiki/`, `.claude/` and `.guppi/` printed `brief.md`, `log.md`, `rules/rule-backlog.md` and `entities/entity-guppi.md`; the hits in `brief.md` and `log.md` are not read, and the two pages lose the slug from `estimates` at the cleanup while their History lines stay. A full pass over the other live Estimates is not done. A Grep `deferred_by, core` over `vault/wiki/`, `.claude/` and `.guppi/guppi/` printed `estimates/schema.yaml`, `rules/rule-estimates-schema.md` and `estimates/estimate-estimates-schema-checked.md`, each changed here; the glossary row `Estimate fields` names `method`, `purpose` and `checked` and no other optional field, and stands. `.guppi/tests/test_schemas.py` reads the live schema: its tests take the first field of `values`, `kind`, so the new field breaks none, and its new test of `once: false` runs only where the live schema lists `once`, so it passes before the render and after it. A Grep `^once:` over `vault/wiki/` printed nothing, so the new finding of lint falls on no live page. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> No Case decides how a one-time Estimate is told apart from one that promises a lasting behaviour, so a one-time check keeps its page `draft` while it waits, stays live after its sprint and ships in the clean version.

> **recommend:**
> - **How a one-time Estimate is told apart**
>   - Recommended: (a) it targets the live sprint page, with no new field.
>   - Answer: (c), both joined: it targets the live sprint page and carries a marker, and lint reports a marked Estimate whose target is not a sprint page.
> - **Whether this Case also sorts the existing Estimates**
>   - Recommended: (b) the two known one-time Estimates are archived too, with no full pass.
>   - Answer: (b), as recommended.
> - **The name of the marker**
>   - Recommended: (a) `once: true`.
>   - Answer: (a), as recommended.
> - **Whether the Case form tells the builder about it**
>   - Recommended: (a) one sentence in `case-schema.md`.
>   - Answer: (a), as recommended.
> - **How the new lint finding is checked**
>   - Recommended: (a) a line added to `estimate-lint-checks-the-statuses`, its Criterion replaced whole.
>   - Answer: (a), as recommended.
> - **How the removal of the two old Estimates is checked**
>   - Recommended: (a) `estimate-cleanup-moves` covers it, with no new Estimate.
>   - Answer: (a), as recommended.

### Case 969.1 — The schema of Estimates holds the field once

> **given:**
> `rule-estimates-schema`: its Render, `vault/wiki/estimates/schema.yaml`, gains the field `once`.
> **＋** `rule-case-protocol`: its Render, `vault/wiki/case-schema.md`, says how a one-time Estimate is created.
> **＋** `estimate-estimates-schema-checked`: its Criterion is replaced whole.
> **＋** `.guppi/tests/test_schemas.py`: the tests of the live schemas.
> **＋** `rule-sprint-close`: the close archives the sprint page with its Estimates.
> **＋** `vault/raw/2026-10-31/1831/cases/case-968.md`: the Case that changes another sentence of `case-schema.md`.

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked, deferred_by, core, once`; values `kind: QA | Research`, `status: pending | passed | failed`, `core: true`, `once: true`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
> **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
> **＋** An Estimate page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** An Estimate page in the shape with `once: true` has no `schema` finding, and one with any other value of `once` has one finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` and `once` among them; the description of `once` says that a one-time Estimate targets the live sprint page and that lint reports one whose target is not a sprint page; the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds, among its paragraphs, the introduction, the sentence on a one-time Estimate, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
> **－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.

> **tasks:**
> - [ ] update `rule-estimates-schema`
>   - old: `` `target` names an Entity or a Rule; lint reports any other category (case 53.1). ``
>   - new: `` `target` names an Entity or a Rule; lint reports any other category (case 53.1). An Estimate that checks one state of the data once, rather than a behaviour that lasts, targets the live sprint page and carries `once: true`: it leaves with the sprint page at the close, keeps no page with `core: true` in `draft` and is not written into the clean version, and lint reports one whose target is not a sprint page (as set in case 969.1). ``
>   - old: `optional: [purpose, checked, deferred_by, core]`
>   - new: `optional: [purpose, checked, deferred_by, core, once]`
>   - old: `core: [true]`
>   - new:
>     ```
>     core: [true]
>         once: [true]
>     ```
>   - old: `no Estimate of the repository that builds that version carries it (cases 804, 822).`
>   - new:
>     ```
>     no Estimate of the repository that builds that version carries it (cases 804, 822).
>       once: |
>         optional; `true`. It marks a one-time Estimate: one that checks one state of the data once, such as the lines of a file after a run, rather than a behaviour that lasts. Its `target` is the live sprint page `entity-sprint-<id>`, so it leaves with that page at the close of the sprint, keeps no page with `core: true` in `draft` and is never written into the clean version; lint reports an Estimate with `once: true` whose `target` is not a sprint page (as set in case 969.1).
>     ```
>   - change: `the field once marks a one-time Estimate, which targets the live sprint page; the defer of case 963 retired`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] update `rule-case-protocol`
>   - old: `up to the session that closes it (case 772.4).`
>   - new: `` up to the session that closes it (case 772.4). An Estimate that checks one state of the data once, rather than a behaviour that lasts, targets the live sprint page and carries `once: true`, so it leaves with that page at the close, keeps no page with `core: true` in `draft` and does not ship; lint reports one with `once: true` whose target is not a sprint page (as set in case 969.1). ``
>   - change: `a one-time Estimate is created on the live sprint page with once: true`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
> - [ ] update `estimate-estimates-schema-checked`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the librarian's run that renders vault/wiki/estimates/schema.yaml from the Render of rule-estimates-schema that holds the field once: the output of uv run --project .guppi pytest .guppi/tests/test_schemas.py -k estimate over that live file, the tests of once among them, and the output of uv run --project .guppi guppi check, no schema finding on wiki/estimates/, read against the Criterion, both outputs in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the optional field once with its one value true; the method waits for the render of the schema`
> - [ ] `.guppi/tests/test_schemas.py`: a test that an Estimate page in the shape with `once: true` has no finding, and a test that one with `once: false` has one finding, run only where the live schema lists `once` among its values, so that it passes before the render and after it; a Case of a later session removes that condition.
> - [ ] read `estimate-estimates-schema-checked`

> **ratification:**
> ```
> - decision[case 969.1][update][rule-estimates-schema]{ref:rule-estimates-schema}{supersedes:case 963}
> - decision[case 969.1][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 969.1][update][estimate-estimates-schema-checked]{ref:rule-estimates-schema}
> ```

### Case 969.2 — Lint reports a one-time Estimate off the sprint page

> **given:**
> `.guppi/guppi/lint.py`: `check_status` and the docstring of the class `status` gain the finding.
> **＋** `.guppi/guppi/ledger.py`: `is_sprint_page`, the one judgment of a sprint page `entity-sprint-<id>`.
> **＋** `.guppi/guppi/pages.py`: `ship_stands` and `is_draft_core`, which other findings of the class read.
> **＋** `vault/wiki/`: the live pages lint reads.
> **＋** `/hi`: a moment a `method` may wait for.
> **＋** `estimate-lint-checks-the-statuses`: its Criterion and `purpose` are replaced.
> **＋** `.guppi/tests/test_lint.py`: the test of the finding.
> **＋** `rule-lint`: the rule of the checks of lint.

> **when:**
> `uv run --project .guppi guppi lint` reads the `status` of the live pages under `vault/wiki/`, and the `method`, the `target` and the `once` of each Estimate.

> **then:**
> `status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged for these two.
> **＋** `status`: where `ship_stands` of `.guppi/guppi/pages.py` finds the module of the command `ship`, each entity or rule that `is_draft_core` accepts, with Estimates or without, one finding each.
> **＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
> **＋** `status`: an Estimate with `once: true` whose `target` is not a sprint page `entity-sprint-<id>`, as `is_sprint_page` of `.guppi/guppi/ledger.py` judges it, one finding.
> **＋** `unread`: every Estimate `failed`, and every Estimate `pending` whose `method` does not wait for a later moment, one finding each, `unread: <status>`.
> **＋** A `method` waits for a later moment when a part of it between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon, or names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`.
> **＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.
> **－** `guppi lint` in a project that installed GUPPI reports none of these pages, since `ship_stands` answers no there.
> **－** A `pending` Estimate whose `method` waits for a later moment earns no `unread` finding.
> **－** A `failed` Estimate earns its `unread` finding whatever its `method` says.
> **－** An Estimate with `once: true` whose target is a sprint page, and an Estimate without `once`, earn no finding of a one-time Estimate.

> **tasks:**
> - [ ] `.guppi/guppi/lint.py`: `check_status` gives one `status` finding `target <slug> is not a sprint page; once: true marks a one-time Estimate` for an Estimate whose `once` is `True` and whose `target` `is_sprint_page` of `.guppi/guppi/ledger.py`, imported, does not accept; the docstring of the class `status` names the finding.
> - [ ] `.guppi/tests/test_lint.py`: a test of the finding over a vault in a temporary folder: an Estimate with `once: true` on a rule has one finding, one on a sprint page has none, and one without `once` has none.
> - [ ] update `estimate-lint-checks-the-statuses`
>   - set:
>     ```
>     status: pending
>     purpose: "A status its Estimates do not support, a draft page with core true where the command ship stands, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, a one-time Estimate whose target is not a sprint page, and a placeholder are findings of lint"
>     ```
>   - change: `the Criterion replaced whole — a one-time Estimate whose target is not a sprint page is a status finding`
> - [ ] read `estimate-lint-checks-the-statuses`

> **ratification:**
> ```
> - decision[case 969.2][update][estimate-lint-checks-the-statuses]{ref:rule-lint}
> ```

### Case 969.3 — The two known one-time Estimates leave the live pages

> **given:**
> `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`: a one-time check of `rule-backlog`, archived.
> **＋** `estimate-guppi-keeps-no-defer-of-its-shape`: a one-time check of `entity-guppi`, archived.
> **＋** `rule-backlog` and `entity-guppi`: the pages that list them in `estimates`.
> **＋** `estimate-cleanup-moves`: the check of the move into the archive.
> **＋** `.guppi/guppi/ship.py`: `ships`, which writes a `passed` Estimate into the clean version.
> **＋** `vault/wiki/`: the live pages the run reads and changes.
> **＋** `vault/archive/`: where an archived page moves.

> **when:**
> The librarian's run applies the Spec of this session: `uv run --project .guppi guppi generate`, then `uv run --project .guppi guppi cleanup` over `vault/wiki/`.

> **then:**
> `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` and `estimate-guppi-keeps-no-defer-of-its-shape` stand `archived` and move under `vault/archive/`.
> **＋** Their slugs leave the `estimates` of `rule-backlog` and of `entity-guppi`.
> **＋** `ships` writes neither of them into the clean version.
> **－** The other Estimates of `rule-backlog` and `entity-guppi` stay live with their status.

> **tasks:**
> - [ ] delete `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`
>   - impact: `A one-time check of the backlog after Case 962, read passed at the /hi of session 1831; rule-backlog no longer lists it and it does not ship`
> - [ ] delete `estimate-guppi-keeps-no-defer-of-its-shape`
>   - impact: `A one-time check of entity-guppi after Case 955, read passed at the /hi of session 0431; entity-guppi no longer lists it and it does not ship`

> **ratification:**
> ```
> - decision[case 969.3][delete][estimate-backlog-keeps-the-work-taken-out-of-a-built-page]
> - decision[case 969.3][delete][estimate-guppi-keeps-no-defer-of-its-shape]
> ```
