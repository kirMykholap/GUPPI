## Case 506 — The checks of the old Estimate shape leave the scripts, the schema and the sprint

> **context:**
> Until case 193, an Estimate page kept its check method in a `## Method` section and the Case's problem in a `## Context` section, and its Criterion could hold `### case N` blocks. Since then `method` is a one-line field and the Criterion is one text. Old pages were converted one at a time, so the scripts learned both shapes. `guppi lint` counts the old pages in one line, `estimates: unmigrated: <N> pages in the shape before case 193`. It reads `## Method` when a page has no `method` field, and it checks that each `### case N` block names a real Decision page. `guppi generate` refuses a Criterion rewrite on a page with no `method` field, and it deletes `## Context` and `## Method` when an update sets `method`. The schema keeps `purpose` and `method` optional "until their recut", and it describes the two old sections. The last librarian's run counted 0 `unmigrated` pages. No live Estimate has a `## Context`, a `## Method`, a `### case N` block or a `Given:` line. All 157 live Estimates have a `method` field, and 12 have no `purpose`. So the transition code handles nothing now. There is one gap: `check_method` of `guppi/lint.py` gives no finding when a page has no method. Once the count leaves, a new Estimate without `method` would pass unnoticed.
> The person decided in one round. The code leaves `guppi/lint.py` and `guppi/generate.py`. `guppi/materialize.py` keeps its handling of the `context` and `criterion` keys, because those rules deal with how a Case item is written (cases 189, 194.1), not with the shape of a page. `method` becomes a required field and `purpose` stays optional. The schema also loses the sentence that older pages keep their `Given:`. `estimate-sprint-migration-lint-clean` is left as it stands. Its words "`unmigrated` included — the counter at zero" stay true once the old shape is gone, and it is already `pending` for its reading at the close of the sprint. For the same reason the Slice 5 line of `entity-sprint-migration` that names the counter stands.
> What `case-guppi` found in the frame. The case-schema sentence "`set.method` when the page has no `method` field, since the recut brings the page to the shape of case 193 and `generate` refuses one without it (case 211)" would become false. So 506.5 changes it in `rule-case-protocol`, and `vault/wiki/case-schema.md` is rendered again. Five Estimates have a Criterion that speaks of the removed code. Each is replaced whole in its own sub-case: `estimate-estimates-schema-checked`, `estimate-lint-checks-the-method`, `estimate-lint-finds-a-broken-link`, `estimate-generate-fails-alone` and `estimate-generate-writes`. `estimate-lint-counts-the-unmigrated` is deleted, and the cascade takes it out of the `estimates` of `rule-lint`, as in case 445.4. The check of the answer notes the changed or dropped Criterion lines of 506.1 and 506.3 to 506.6 as not carried. They are changed on purpose: each names the old shape, the count, the `## Method` fallback, the `### case N` link, the recut refusal or the `set.method` drop. Every other line is kept word for word. The check also notes that a `then` line of 506.2 and one of 506.3 share words with 506.1. This is expected. 506.1 promises the `schema` finding for a missing `method`. 506.2 promises that no other line reports it. 506.3 promises that `lint` reads no `## Method` section, while 506.1 says the schema text no longer names that section. They are separate promises with separate tests. Pre-spec found that the first rewrite of the description paragraph in 506.1 said `checked` is written "at the first reading". The `checked` field of the same Render says it is "written by `generate` on every reading (case 201.1)". The new clause now uses those words and that source. `estimate-estimates-schema-checked` and `estimate-generate-writes` are already `pending` and are Frontier items W22 and W29. After this Case their readings wait for a later session (case 428.1). The sentence of `rule-decisions-schema` on the `## Criterion` of old Decision pages describes Decision pages, which keep that section, so it stands. No reader here refuses anything. `guppi lint` only goes red, and all live Estimates already have `method`, so no old form is kept. The near backlog item `insight-materialize-estimate-update-lifts-the-criterion-whole` deals with how `materialize` lifts a Criterion into an update. This Case does not touch that, so the item stands. The Case creates no page, so no vault query was run. Not done: the `materialize` key rules of older Case formats, and a `purpose` on the 12 pages without one.

> **problem:**
> The old Estimate shape is gone from the vault, but the scripts, the schema, the case schema and the sprint page still describe and handle it. The count that stood in for a required `method` field is the only guard against an Estimate with no method, so it cannot simply be removed.

> **recommend:**
> Remove the old-shape code from `guppi/lint.py` and `guppi/generate.py`. Make `method` a required field in the schema, so a missing method is a `schema` finding. Drop every conversion clause from the schema text and the case schema. Replace each Criterion that speaks of the removed code, delete the counting Estimate, and close Slice 3g. Removing the count and keeping both fields optional was rejected, because a new Estimate without `method` would then pass with no finding.

### Case 506.1 — The Estimate schema requires `method` and names no old shape

> **given:**
> `rule-estimates-schema` — the rule; its Render is the schema of an Estimate page
> **＋** `vault/wiki/estimates/schema.yaml` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `guppi/lint.py` — reads the lists of the file for every page of `vault/wiki/estimates/`
> **＋** `vault/wiki/estimates/` — the live Estimate pages
> **＋** `estimate-estimates-schema-checked` — the promise, its Criterion replaced whole
> **＋** `tests/test_schemas.py` — the tests the reading runs

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
> **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds, among its paragraphs, the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
> **－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.

> **tasks:**
> - [ ] update `rule-estimates-schema`
>   - old: `` one line each, written on a page born since case 193; the older pages carry none until their recut at their first touch — the update that sets `method` (case 211) — counted by lint as `unmigrated` (case 202), so none is required yet (case 193). ``
>   - new: `` one line each. `method` is required on every page (case 506.1); `purpose` is written from the Case and stays optional, since some older pages carry none; `checked` is written by `generate` on every reading (case 201.1). ``
>   - old: `required: [type, kind, status, target, origin, sprint, created, tags]`
>   - new: `required: [type, kind, status, target, method, origin, sprint, created, tags]`
>   - old: `optional: [purpose, method, checked]`
>   - new: `optional: [purpose, checked]`
>   - old: `optional: ["## Context", "## Method", "## Result"]`
>   - new: `optional: ["## Result"]`
>   - old: `` Written from the Case on every page born since case 193; absent on the older pages until their recut, counted by lint as `unmigrated` (case 202). ``
>   - new: `Written from the Case; some older pages carry none, and lint does not ask for it (case 506.1).`
>   - old: `optional; one line. How the promise is checked`
>   - new: `required; one line. How the promise is checked`
>   - old: `` A page counts as the shape before case 193 on any of four triggers — no `method` field, a `## Context` section, a `## Method` section, a `### case N` block in the Criterion — and goes into the line `unmigrated`; one with no field that keeps a `## Method` section has that section read as its `method`, so it can earn a `method` finding as well. ``
>   - new: `` A page without the field earns the `schema` finding `missing field method` (case 506.1). ``
>   - old: `` (case 378.2); a page written before carries its `Given:` until the one pass of its migration. ``
>   - new: `(case 378.2).`
>   - old: `` no `### case N` block exists (case 193; the blocks of the shape before it stand on the older pages until their recut, counted by lint as `unmigrated`, case 202). ``
>   - new: `` no `### case N` block exists (case 193). ``
>   - old: `` "## Context": | optional. The shape before case 193: the `problem` of the Case that made the Estimate, written once. Not written to a new page — the Case is reached by `origin`; dropped by the `update` that sets `method` (case 211). "## Method": | optional. The shape before case 193: the `method` of the Case as a section. On a new page `method` is a field; the `update` that sets `method` drops the section, and a recut — `sections: Criterion` on a page without the field — is refused by `generate` unless `set` carries `method` (case 211). "## History": | ``
>   - new: `"## History": |`
>   - change: `method required, purpose optional; the old shape, the unmigrated count, the recut and the Given: of older pages gone from the schema (case 506.1)`
> - [ ] update `estimate-estimates-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — method required, the two old sections gone (case 506.1)`
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] `tests/test_schemas.py`: a test that an Estimate page without `method` has one finding `missing field method` against the live `schema.yaml`
> - [ ] read `estimate-estimates-schema-checked` — `pytest tests/test_schemas.py -k estimates`, then `make lint` with no `schema` finding on `vault/wiki/estimates/`, at a later session

> **ratification:**
> ```
> - decision[case 506.1][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 506.1][update][estimate-estimates-schema-checked]{ref:estimate-estimates-schema-checked}
> ```

### Case 506.2 — Lint counts no `unmigrated` pages

> **given:**
> `guppi/lint.py` — `is_old_shape`, `check_unmigrated` and the class list of its docstring
> **＋** `vault/wiki/estimates/` — the live Estimate pages lint reads
> **＋** `tests/test_lint.py` — the tests of the count
> **＋** `rule-lint` — the rule; its Purpose names the counted line
> **＋** `estimate-lint-counts-the-unmigrated` — the promise of the count, deleted
> **＋** `rule-estimates-schema` — the rule whose `schema` finding reports a missing `method`

> **when:**
> `uv run guppi lint` reads the live Estimates under `vault/wiki/estimates/`.

> **then:**
> No line of the class `unmigrated` is printed, whatever the pages hold.
> **＋** An Estimate without a `method` field is reported only by the `schema` finding of `rule-estimates-schema`.

> **tasks:**
> - [ ] `guppi/lint.py`: remove `is_old_shape`, `check_unmigrated` and its call in `lint`, and the class `unmigrated` from the docstring
> - [ ] `tests/test_lint.py`: remove the test of the `unmigrated` count and its fixture of the old shape; a test that a page with `## Context` and `## Method` sections prints no `unmigrated` line
> - [ ] update `rule-lint`
>   - old: `` its reading (case 182, point 13), a placeholder is red with the count of its defers (case 186.3), the pages of the shape before case 193 are red as one counted line until the last is recut (case 202). ``
>   - new: `its reading (case 182, point 13), and a placeholder is red with the count of its defers (case 186.3).`
>   - change: `the unmigrated count gone from the Purpose (case 506.2)`
> - [ ] delete `estimate-lint-counts-the-unmigrated`
>   - impact: `The count ends with the old shape; a missing method is a schema finding of rule-estimates-schema (case 506.1); rule-lint loses it from estimates by the cascade`

> **ratification:**
> ```
> - decision[case 506.2][update][rule-lint]{ref:rule-lint}
> - decision[case 506.2][delete][estimate-lint-counts-the-unmigrated]{ref:estimate-lint-counts-the-unmigrated}
> ```

### Case 506.3 — Lint reads the `method` field only

> **given:**
> `guppi/lint.py` — `method_of`, `check_method` and the docstring
> **＋** `tests/test_lint.py` — the tests of the `method` class
> **＋** `estimate-lint-checks-the-method` — the promise, its Criterion replaced whole
> **＋** `Makefile` — the targets a `make <target>` names
> **＋** `estimate-claude-md-rendered` — the Estimate named in the Criterion

> **when:**
> `uv run guppi lint` reads the `method` field of each live Estimate.

> **then:**
> For an Estimate of a Leaf, a `tests/` file that exists, the word `pytest`, a `make <target>` of the `Makefile`, or `by hand` passes; else the finding "method: names no tests/ file, pytest or make target and is not a reading".
> **＋** A named `tests/` file that does not exist, or a `make <target>` the `Makefile` does not hold, is a finding.
> **＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it; `by hand` without one passes when every counted Estimate of the children is a reading or a sibling Estimate names a `make <target>` of the `Makefile`; else a finding.
> **＋** On a MOC with `render_mode: full`, the Estimates of a child with `enforcement: render` are not counted.
> **＋** `estimate-claude-md-rendered` gets no `method` finding.
> **－** On a MOC with `render_mode: full`, the Estimates of a child without `enforcement: render` are counted.
> **－** On a MOC without `render_mode: full`, the Estimates of every child are counted, a child with `enforcement: render` included.
> **－** A `## Method` section is not read as the `method` of a page.

> **tasks:**
> - [ ] `guppi/lint.py`: `method_of` returns the field alone; the docstring of the class `method` and of `check_method` drops the `## Method` section
> - [ ] `tests/test_lint.py`: remove the test that the `## Method` section is read on a page of the old shape; a test that a page with no `method` field and a `## Method` section gets no `method` finding
> - [ ] update `estimate-lint-checks-the-method`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the method field only, no ## Method section read (case 506.3)`
> - [ ] read `estimate-lint-checks-the-method` — `uv run pytest tests/test_lint.py`, at a later session

> **ratification:**
> ```
> - decision[case 506.3][update][estimate-lint-checks-the-method]{ref:estimate-lint-checks-the-method}
> ```

### Case 506.4 — Lint follows no `### case N` block of an Estimate

> **given:**
> `guppi/lint.py` — `check_criterion`, `CASE_BLOCK` and the docstring of the class `ref`
> **＋** `tests/test_lint.py` — the tests of the class `ref`
> **＋** `estimate-lint-finds-a-broken-link` — the promise, its Criterion replaced whole
> **＋** `guppi/materialize.py` — `category_of`, which gives a slug its category by its prefix, `decision-` included
> **＋** `raw/<date>[/<HHMM>]/ledger.md#case-N` — the form of an `origin` that lint resolves
> **＋** `vault/wiki/` — the live pages whose links are followed
> **＋** `vault/raw/` — where an `origin` ledger stands
> **＋** `vault/archive/` — where an archived page or ledger stands

> **when:**
> `uv run guppi lint` follows the links of the live pages under `vault/wiki/`.

> **then:**
> `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a body `[[…]]` that no live or archived page carries; a body `[[…]]` may name a file under `vault/wiki/` by stem or path; a `[[…]]` inside a code span is no link.
> **＋** `ref`: an `applies_to` naming a page that is not an Entity; an Entity whose `rules` differs from the live rules whose `applies_to` names it, the difference as `+slug` and `-slug`.
> **＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate.
> **＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
> **＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer`, or with `kind` or `target_slug`; a slug of its lists that `category_of` of `guppi/materialize.py` gives a category — the prefix `decision-` included — and that no live or archived page carries.
> **＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.
> **－** A `### case N` line under an Estimate's `## Criterion` is not read as a link.

> **tasks:**
> - [ ] `guppi/lint.py`: `check_criterion` reads Decision pages only; `CASE_BLOCK` removed; the docstring drops the `### case N` block
> - [ ] `tests/test_lint.py`: the test of a `### case N` block with no Decision page becomes a test that it earns no `ref` finding
> - [ ] update `estimate-lint-finds-a-broken-link`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — no ### case N block of an Estimate followed (case 506.4)`
> - [ ] read `estimate-lint-finds-a-broken-link` — `uv run pytest tests/test_lint.py`, at a later session

> **ratification:**
> ```
> - decision[case 506.4][update][estimate-lint-finds-a-broken-link]{ref:estimate-lint-finds-a-broken-link}
> ```

### Case 506.5 — `generate` refuses no Criterion rewrite for want of `method`

> **given:**
> `guppi/generate.py` — the refusal `a recut without method` in `update`, and the docstring
> **＋** `tests/test_generate.py` — the tests of a failing entry
> **＋** `estimate-generate-fails-alone` — the promise, its Criterion replaced whole
> **＋** `rule-case-protocol` — its Render names the refusal
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `materialize.yaml` — the entries `generate` applies
> **＋** `vault/wiki/log.md` — the log appended after each entry

> **when:**
> `uv run guppi generate` meets an entry of `materialize.yaml` it cannot apply, or one already handled.

> **then:**
> An entry that fails — a collision, a `ref` naming no page, a `replace` absent or not unique, a field of an unexpected shape, an unknown `kind`, any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` in the yaml and skipped; the rest apply; the exit code is 1; no entry ends the run.
> **＋** Every applied entry is marked `applied: <time>`; a stale `failed` mark is dropped on apply; a rerun writes nothing.
> **＋** An entry with `failed` and no `kind` is skipped with its mark kept and the line `generate: line N: not lifted by materialize; <message>`, exit 1.
> **＋** An entry with `superseded_by` is not applied and leaves no line; the Decision page of its Case is still written.
> **＋** An `update` with no content prints `generate: <slug>: an update with no content in the Spec; nothing applied` on stdout, changes no page and is marked applied.
> **－** The failure of one entry changes no other page: `vault/wiki/log.md` after it is level with the pages.
> **－** An `update` with `sections.Criterion` on an Estimate page does not fail for want of a `method` field.

> **tasks:**
> - [ ] `guppi/generate.py`: remove the refusal `a recut without method` from `update` and from the docstring
> - [ ] `tests/test_generate.py`: remove the test that a recut without method fails alone; a test that an `update` with `sections.Criterion` on an Estimate page without `method` applies
> - [ ] update `estimate-generate-fails-alone`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a recut without method no longer fails (case 506.5)`
> - [ ] update `rule-case-protocol`
>   - old: `` carries `slug`, `set: {status: pending}` and `change` — and `set.method` when the page has no `method` field, since the recut brings the page to the shape of case 193 and `generate` refuses one without it (case 211); the scripts replace ``
>   - new: `` carries `slug`, `set: {status: pending}` and `change`; the scripts replace ``
>   - change: `an update of an Estimate needs no set.method; generate refuses no recut without it (case 506.5)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-generate-fails-alone` — `pytest tests/test_generate.py`, at a later session

> **ratification:**
> ```
> - decision[case 506.5][update][estimate-generate-fails-alone]{ref:estimate-generate-fails-alone}
> - decision[case 506.5][update][rule-case-protocol]{ref:rule-case-protocol}
> ```

### Case 506.6 — `generate` drops no section when an update sets `method`

> **given:**
> `guppi/generate.py` — the drop of `## Context` and `## Method` in `update`, and the docstring
> **＋** `tests/test_generate.py` — the tests of an update of an Estimate
> **＋** `estimate-generate-writes` — the promise, its Criterion replaced whole
> **＋** `estimate-generate-fails-alone` — the promise of an entry that fails, named and not changed here
> **＋** `vault/wiki/` — the live pages written
> **＋** `vault/archive/` — where an entry finds a page not under `vault/wiki/`
> **＋** `raw/` — the session folders inside the archive, which the search passes by

> **when:**
> `guppi generate` applies one entry of a yaml to a page.

> **then:**
> A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the first `## <id>` of `sprint.md`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
> **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
> **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
> **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
> **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
> **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
> **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
> **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by`.
> **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
> **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
> **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
> **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
> **－** No body section is derived from a ref field; a section the entry does not name under `sections` or reach by `replace` is not touched.
> **－** An `update` of an Estimate whose `set` carries `method` drops no section.
> **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

> **tasks:**
> - [ ] `guppi/generate.py`: remove the drop of `## Context` and `## Method` on `set.method` from `update` and from the docstring
> - [ ] `tests/test_generate.py`: remove the two tests of the drop and the fixture of the old shape; a test that an `update` whose `set` carries `method` leaves every section of the page as it stands
> - [ ] update `estimate-generate-writes`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — set.method drops no section (case 506.6)`
> - [ ] read `estimate-generate-writes` — `pytest tests/test_generate.py`, then by hand at a later librarian's run

> **ratification:**
> ```
> - decision[case 506.6][update][estimate-generate-writes]{ref:estimate-generate-writes}
> ```

### Case 506.7 — Slice 3g closes on the sprint page

> **given:**
> `entity-sprint-migration` — the sprint page; its Milestones hold Slice 3g, its `## Closed` the note on the recut
> **＋** `guppi/sprint.py` — renders the sprint page
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `estimate-sprint-migration-lint-clean` — the Estimate of the Slice 5 line, not changed

> **when:**
> `uv run guppi sprint` renders `vault/wiki/sprint.md` from `entity-sprint-migration` at the librarian's run, and the next `/hi` builds the Frontier from it.

> **then:**
> The Milestones hold no Slice 3g, and the Frontier holds no line for it.
> **＋** `## Closed` says that the recut of the old Estimate shape ended and that its checks left the scripts.
> **－** The Slice 5 line on `estimate-sprint-migration-lint-clean` and the Estimates of `entity-sprint-migration` stay as they are.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - old: `` ### Slice 3g — the model of the Criterion, one pass over the Estimates - the old shape removed: once `make lint` counts no `unmigrated` page, the checks of the shape before case 193 leave the scripts, `rule-estimates-schema` and `estimate-lint-counts-the-unmigrated` (case 202) ### Slice 4 — conversion of the parked pages by group ``
>   - new: `### Slice 4 — conversion of the parked pages by group`
>   - old: `` The recut of each old Estimate at its first touch runs on past the Slice: lint counts the remainder as `unmigrated` (42 at the close of 3d) and the old shape is removed when it reaches zero. ``
>   - new: `The recut of each old Estimate ran on past the Slice, 42 pages at the close of 3d; Slice 3g recut the last of them (cases 484-500) and closed with case 506, which took the checks of the old shape out of the scripts.`
>   - change: `Slice 3g closed: the checks of the old shape left the scripts, the schema and lint (case 506)`
> - [ ] `uv run guppi sprint`

> **ratification:**
> ```
> - decision[case 506.7][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
