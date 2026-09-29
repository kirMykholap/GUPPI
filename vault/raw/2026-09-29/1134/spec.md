<!-- approved 13:49:20 · session d3c46a47 -->

# Spec — session 1134, 2026-09-29

## Case 506 — The checks of the old Estimate shape leave the scripts, the schema and the sprint

> **context:**
> Until case 193, an Estimate page kept its check method in a `## Method` section and the Case's problem in a `## Context` section, and its Criterion could hold `### case N` blocks. Since then `method` is a one-line field and the Criterion is one text. Old pages were converted one at a time, so the scripts learned both shapes. `guppi lint` counts the old pages in one line, `estimates: unmigrated: <N> pages in the shape before case 193`. It reads `## Method` when a page has no `method` field, and it checks that each `### case N` block names a real Decision page. `guppi generate` refuses a Criterion rewrite on a page with no `method` field, and it deletes `## Context` and `## Method` when an update sets `method`. The schema keeps `purpose` and `method` optional "until their recut", and it describes the two old sections. The last librarian's run counted 0 `unmigrated` pages. No live Estimate has a `## Context`, a `## Method`, a `### case N` block or a `Given:` line. All 157 live Estimates have a `method` field, and 12 have no `purpose`. So the transition code handles nothing now. There is one gap: `check_method` of `guppi/lint.py` gives no finding when a page has no method. Once the count leaves, a new Estimate without `method` would pass unnoticed.
> The person decided in one round. The code leaves `guppi/lint.py` and `guppi/generate.py`. `guppi/materialize.py` keeps its handling of the `context` and `criterion` keys, because those rules deal with how a Case item is written (cases 189, 194.1), not with the shape of a page. `method` becomes a required field and `purpose` stays optional. The schema also loses the sentence that older pages keep their `Given:`. `estimate-sprint-migration-lint-clean` is left as it stands. Its words "`unmigrated` included — the counter at zero" stay true once the old shape is gone, and it is already `pending` for its reading at the close of the sprint. For the same reason the Slice 5 line of `entity-sprint-migration` that names the counter stands.
> What `case-guppi` found in the frame. The case-schema sentence "`set.method` when the page has no `method` field, since the recut brings the page to the shape of case 193 and `generate` refuses one without it (case 211)" would become false. So 506.5 changes it in `rule-case-protocol`, and `vault/wiki/case-schema.md` is rendered again. Five Estimates have a Criterion that speaks of the removed code. Each is replaced whole in its own sub-case: `estimate-estimates-schema-checked`, `estimate-lint-checks-the-method`, `estimate-lint-finds-a-broken-link`, `estimate-generate-fails-alone` and `estimate-generate-writes`. `estimate-lint-counts-the-unmigrated` is deleted, and the cascade takes it out of the `estimates` of `rule-lint`, as in case 445.4. The check of the answer notes the changed or dropped Criterion lines of 506.1 and 506.3 to 506.6 as not carried. They are changed on purpose: each names the old shape, the count, the `## Method` fallback, the `### case N` link, the recut refusal or the `set.method` drop. Every other line is kept word for word. The check also notes that a `then` line of 506.2 and one of 506.3 share words with 506.1. This is expected. 506.1 promises the `schema` finding for a missing `method`. 506.2 promises that no other line reports it. 506.3 promises that `lint` reads no `## Method` section, while 506.1 says the schema text no longer names that section. They are separate promises with separate tests. Pre-spec found that the first rewrite of the description paragraph in 506.1 said `checked` is written "at the first reading". The `checked` field of the same Render says it is "written by `generate` on every reading (case 201.1)". The new clause now uses those words and that source. `estimate-estimates-schema-checked` and `estimate-generate-writes` are already `pending` and are Frontier items W22 and W29. After this Case their readings wait for a later session (case 428.1). The sentence of `rule-decisions-schema` on the `## Criterion` of old Decision pages describes Decision pages, which keep that section, so it stands. No reader here refuses anything. `guppi lint` only goes red, and all live Estimates already have `method`, so no old form is kept. The near backlog item `insight-materialize-estimate-update-lifts-the-criterion-whole` deals with how `materialize` lifts a Criterion into an update. This Case does not touch that, so the item stands. The Case creates no page, so no vault query was run. Not done: the `materialize` key rules of older Case formats, and a `purpose` on the 12 pages without one.

> **problem:**
> The old Estimate shape is gone from the vault, but the scripts, the schema, the case schema and the sprint page still describe and handle it. The count that stood in for a required `method` field is the only guard against an Estimate with no method, so it cannot simply be removed.

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

```then
update:
- slug: rule-estimates-schema
  replace:
  - old: one line each, written on a page born since case 193; the older pages carry none until their recut at their first touch — the update that sets `method` (case 211) — counted by lint as `unmigrated` (case 202), so none is required yet (case 193).
    new: one line each. `method` is required on every page (case 506.1); `purpose` is written from the Case and stays optional, since some older pages carry none; `checked` is written by `generate` on every reading (case 201.1).
  - old: 'required: [type, kind, status, target, origin, sprint, created, tags]'
    new: 'required: [type, kind, status, target, method, origin, sprint, created, tags]'
  - old: 'optional: [purpose, method, checked]'
    new: 'optional: [purpose, checked]'
  - old: 'optional: ["## Context", "## Method", "## Result"]'
    new: 'optional: ["## Result"]'
  - old: Written from the Case on every page born since case 193; absent on the older pages until their recut, counted by lint as `unmigrated` (case 202).
    new: Written from the Case; some older pages carry none, and lint does not ask for it (case 506.1).
  - old: optional; one line. How the promise is checked
    new: required; one line. How the promise is checked
  - old: A page counts as the shape before case 193 on any of four triggers — no `method` field, a `## Context` section, a `## Method` section, a `### case N` block in the Criterion — and goes into the line `unmigrated`; one with no field that keeps a `## Method` section has that section read as its `method`, so it can earn a `method` finding as well.
    new: A page without the field earns the `schema` finding `missing field method` (case 506.1).
  - old: (case 378.2); a page written before carries its `Given:` until the one pass of its migration.
    new: (case 378.2).
  - old: no `### case N` block exists (case 193; the blocks of the shape before it stand on the older pages until their recut, counted by lint as `unmigrated`, case 202).
    new: no `### case N` block exists (case 193).
  - old: '"## Context": | optional. The shape before case 193: the `problem` of the Case that made the Estimate, written once. Not written to a new page — the Case is reached by `origin`; dropped by the `update` that sets `method` (case 211). "## Method": | optional. The shape before case 193: the `method` of the Case as a section. On a new page `method` is a field; the `update` that sets `method` drops the section, and a recut — `sections: Criterion` on a page without the field — is refused by `generate` unless `set` carries `method` (case 211). "## History": |'
    new: '"## History": |'
  change: 'method required, purpose optional; the old shape, the unmigrated count, the recut and the Given: of older pages gone from the schema (case 506.1)'
- slug: estimate-estimates-schema-checked
  set:
    status: pending
  change: the Criterion replaced whole — method required, the two old sections gone (case 506.1)
```

```tasks
- [ ] update `rule-estimates-schema`
- [ ] update `estimate-estimates-schema-checked`
- [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] `tests/test_schemas.py`: a test that an Estimate page without `method` has one finding `missing field method` against the live `schema.yaml`
- [ ] read `estimate-estimates-schema-checked` — `pytest tests/test_schemas.py -k estimates`, then `make lint` with no `schema` finding on `vault/wiki/estimates/`, at a later session
```

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

```then
update:
- slug: rule-lint
  replace:
  - old: its reading (case 182, point 13), a placeholder is red with the count of its defers (case 186.3), the pages of the shape before case 193 are red as one counted line until the last is recut (case 202).
    new: its reading (case 182, point 13), and a placeholder is red with the count of its defers (case 186.3).
  change: the unmigrated count gone from the Purpose (case 506.2)
delete:
- slug: estimate-lint-counts-the-unmigrated
  impact: The count ends with the old shape; a missing method is a schema finding of rule-estimates-schema (case 506.1); rule-lint loses it from estimates by the cascade
```

```tasks
- [x] `guppi/lint.py`: remove `is_old_shape`, `check_unmigrated` and its call in `lint`, and the class `unmigrated` from the docstring
- [x] `tests/test_lint.py`: remove the test of the `unmigrated` count and its fixture of the old shape; a test that a page with `## Context` and `## Method` sections prints no `unmigrated` line
- [ ] update `rule-lint`
- [ ] delete `estimate-lint-counts-the-unmigrated`
```

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

```then
update:
- slug: estimate-lint-checks-the-method
  set:
    status: pending
  change: 'the Criterion replaced whole — the method field only, no ## Method section read (case 506.3)'
```

```tasks
- [x] `guppi/lint.py`: `method_of` returns the field alone; the docstring of the class `method` and of `check_method` drops the `## Method` section
- [x] `tests/test_lint.py`: remove the test that the `## Method` section is read on a page of the old shape; a test that a page with no `method` field and a `## Method` section gets no `method` finding
- [ ] update `estimate-lint-checks-the-method`
- [ ] read `estimate-lint-checks-the-method` — `uv run pytest tests/test_lint.py`, at a later session
```

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

```then
update:
- slug: estimate-lint-finds-a-broken-link
  set:
    status: pending
  change: 'the Criterion replaced whole — no ### case N block of an Estimate followed (case 506.4)'
```

```tasks
- [x] `guppi/lint.py`: `check_criterion` reads Decision pages only; `CASE_BLOCK` removed; the docstring drops the `### case N` block
- [x] `tests/test_lint.py`: the test of a `### case N` block with no Decision page becomes a test that it earns no `ref` finding
- [ ] update `estimate-lint-finds-a-broken-link`
- [ ] read `estimate-lint-finds-a-broken-link` — `uv run pytest tests/test_lint.py`, at a later session
```

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

```then
update:
- slug: estimate-generate-fails-alone
  set:
    status: pending
  change: the Criterion replaced whole — a recut without method no longer fails (case 506.5)
- slug: rule-case-protocol
  replace:
  - old: 'carries `slug`, `set: {status: pending}` and `change` — and `set.method` when the page has no `method` field, since the recut brings the page to the shape of case 193 and `generate` refuses one without it (case 211); the scripts replace'
    new: 'carries `slug`, `set: {status: pending}` and `change`; the scripts replace'
  change: an update of an Estimate needs no set.method; generate refuses no recut without it (case 506.5)
```

```tasks
- [x] `guppi/generate.py`: remove the refusal `a recut without method` from `update` and from the docstring
- [x] `tests/test_generate.py`: remove the test that a recut without method fails alone; a test that an `update` with `sections.Criterion` on an Estimate page without `method` applies
- [ ] update `estimate-generate-fails-alone`
- [ ] update `rule-case-protocol`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-generate-fails-alone` — `pytest tests/test_generate.py`, at a later session
```

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

```then
update:
- slug: estimate-generate-writes
  set:
    status: pending
  change: the Criterion replaced whole — set.method drops no section (case 506.6)
```

```tasks
- [x] `guppi/generate.py`: remove the drop of `## Context` and `## Method` on `set.method` from `update` and from the docstring
- [x] `tests/test_generate.py`: remove the two tests of the drop and the fixture of the old shape; a test that an `update` whose `set` carries `method` leaves every section of the page as it stands
- [ ] update `estimate-generate-writes`
- [ ] read `estimate-generate-writes` — `pytest tests/test_generate.py`, then by hand at a later librarian's run
```

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

```then
update:
- slug: entity-sprint-migration
  replace:
  - old: '### Slice 3g — the model of the Criterion, one pass over the Estimates - the old shape removed: once `make lint` counts no `unmigrated` page, the checks of the shape before case 193 leave the scripts, `rule-estimates-schema` and `estimate-lint-counts-the-unmigrated` (case 202) ### Slice 4 — conversion of the parked pages by group'
    new: '### Slice 4 — conversion of the parked pages by group'
  - old: 'The recut of each old Estimate at its first touch runs on past the Slice: lint counts the remainder as `unmigrated` (42 at the close of 3d) and the old shape is removed when it reaches zero.'
    new: The recut of each old Estimate ran on past the Slice, 42 pages at the close of 3d; Slice 3g recut the last of them (cases 484-500) and closed with case 506, which took the checks of the old shape out of the scripts.
  change: 'Slice 3g closed: the checks of the old shape left the scripts, the schema and lint (case 506)'
```

```tasks
- [ ] update `entity-sprint-migration`
- [ ] `uv run guppi sprint`
```

## Case 508 — Work readings get a trigger at `/hi` and in `/work`

> **context:**
> A reading checks one Estimate against what actually happens and writes the result into the ledger. At `/hi` each `pending` reading becomes a `W` line of the Frontier. Only `/retro` says "take the readings". By then some readings are blocked, because the ledger hook refuses a reading of an Estimate that the same session creates or updates (case 428.1). Other readings are tied to a moment that has already passed. For example, the `method` of `estimate-hi-no-read-calls` names "the /hi of the next session", and the `/hi` reply of this session did not take it; it was read later in the session. So the readings pile up: this session's Frontier opened with 89 reading lines under `## Work`. The librarian is a helper agent and writes no ledger line. Yet the `method` of 32 Estimates names the librarian, counted by a Grep of the `method` lines. The librarian lists these Estimates under Readings due of `vault/wiki/brief.md` with no result. It writes the brief before `guppi archive` and the commit, on purpose: the brief reads the yamls and Specs where they stand, and the librarian may not search `vault/archive/`.
>
> In the rounds the person decided the following:
> - `/hi` takes the readings whose `method` names `/hi` or the librarian's run, in its first reply, and closes their `W` lines there.
> - A reading whose `method` also names a later moment waits for that moment.
> - A reading whose `method` needs a `/hi` run of its own is not taken at `/hi`.
> - `/work` gets a step after the last task that takes every other reading it can, in Frontier order, and the person can stop it.
> - A `W` line that cannot be read stays open.
> - The librarian writes facts, not verdicts: what its run printed or left, on each such Estimate's Readings due line, and the output of `guppi archive` right after that step.
> - The commit reading is taken at the next `/hi` from `git log`, `git status` and the previous transcript.
> - Each behaviour gets a new Estimate.
>
> Frame found by `case-guppi`:
> - The Render of `rule-skill-hi` and the Criterion of `estimate-hi-writes-frontier` both say a `W` line closes "in Work Mode". Closing at `/hi` makes both false, so sub-case 508.2 changes both. A reading taken by `/retro` closes its line at Retro, so the new wording names all three places.
>
> Case 507 and why 508.2 supersedes it:
> - Case 507 of this session replaced the same Criterion whole: at `/hi` the chat shows the Cases as the checklist of `frontier.md`, the detail on an indented line, never as a bold line with a paragraph. The person chose that look from four, and kept `rule-orchestration` out of it.
> - Two whole replacements of one Criterion would sign it twice. So 508.2 supersedes 507 and carries both of its changes: 507's pair on `rule-skill-hi` for the chat look, and its own pair for closing a `W` line.
> - The one Criterion of 508.2 is 507's with two changes. The chat look is described on its own and no longer called the form of the acknowledging reply, since that form folds closed lines and shows no detail line. The `W` closing line is changed.
> - 507 leaves the Spec.
> - Against the Criterion on the page today, two lines are not carried: the old chat line and the old `W` closing line.
>
> Other frame facts:
> - The Render of `rule-skill-hi` assembles the Frontier with "no page opened". That stays: only the new reading step opens the pages of the Estimates it reads.
> - The `W` lines are closed in `frontier.md` before the reply that carries the `LEDGER` block, since that reply ends in text with no tool call after it.
>
> Why some `then` lines look alike:
> - The reading steps of 508.1 at `/hi` and 508.3 in `/work` use similar words on purpose. They are one kind of step at two moments, each with its own promise, and each can fail apart from the other.
> - The line of 508.3 that closes the `W` line before the `LEDGER` reply repeats the matching line of 508.1 on purpose, so that each Estimate reads whole without the other.
> - Some lines of 508.2 share words with 508.1 because both describe `frontier.md`.
>
> These Estimates stand, and why:
> - `estimate-hi-no-read-calls`: the reading calls come after the skill's output is already in context, so they are not calls "to get any of them".
> - `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: it promises the tasks in order, and its `－` line about ticking no `read` box stays true.
> - `estimate-brief-written`: its Criterion promises the sections, their order and their sources. Each Readings due line keeps its three parts, the Estimate, its `draft` rule and where it is read, one line per Estimate. The facts added at the end of the line are promised by the new Estimate of 508.4.
> - `estimate-documentation-completes`: the librarian opens an Estimate page for "a fact for the brief", which its frame already lists, and the archive output still goes into the report.
>
> What does not change:
> - `rule-retro` keeps its reading paragraph and takes whatever is left.
> - The sentence of `rule-case-protocol`, "a `W` line closes when its work is done", names no phase and stays true.
>
> Vault query: every `create` is an Estimate with a `ref`, so no vault query was needed. A Glob found the three new slugs free.
>
> Timing: no hook changes. The skills are rendered at the librarian's run. `/hi` and `/work` act on the new text from the next session. The librarian of this session runs on the frame it loaded at dispatch, so the new brief facts first appear one run later.

> **problem:**
> A Work reading has no trigger before Retro. Readings tied to `/hi` or to the librarian's run pass without being taken, and the other readings pile up until some are blocked.

### Case 508.1 — `/hi` takes the readings of `/hi` and of the librarian's run

> **given:**
> `rule-skill-hi` — the page whose Render is the `/hi` skill and assembles the Frontier with no page opened
> **＋** `.claude/skills/hi/SKILL.md` — the skill file rendered from `rule-skill-hi`
> **＋** `estimate-hi-takes-its-readings` — the promise of the reading step at `/hi`
> **＋** `vault/wiki/brief.md` — loaded at `/hi`; its Readings due carry each `method` and the librarian's facts
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier, whose `W` lines are the readings
> **＋** `rule-ledger-write` — the hook that writes the reading lines of a `LEDGER` block
> **＋** `rule-case-protocol` — a reply that carries a `LEDGER` block ends in text, with no tool call after it

> **when:**
> The person types `/hi` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md`.

> **then:**
> In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose `method` names the `/hi` of a session or the librarian's run and whose whole method can be done at that moment.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the commands of the method, and reads the librarian's report from the transcript of the previous session.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken as `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** A reading whose `method` also names a later moment is not taken at `/hi`. It is taken at that moment, and its `/hi` part is read then from the session's first turn.
> **－** A reading whose `method` asks for a `/hi` run of its own, such as one outside plan mode, is not taken at `/hi`.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

```then
create:
- slug: estimate-hi-takes-its-readings
  type: estimate
  ref: rule-skill-hi
  kind: QA
  purpose: Whether /hi takes, in its first reply, each open W reading whose method names /hi or the librarian's run and can be done whole then, closes its W line and writes its line, opens no page but the Estimates it reads, and leaves the readings that name a later moment or a /hi run of their own
  method: 'by hand at the first /hi after the render: the first reply, its tool calls, its LEDGER block and frontier.md read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - harness
  - workflow
update:
- slug: rule-skill-hi
  replace:
  - old: Wait for the human to pick the order or defer items.
    new: 'Before the question on the order, in the same reply, take each reading of an open `W` line whose `method` names the `/hi` of a session or the librarian''s run and whose whole method can be done now: from the brief, `git log`, `git status`, the commands the method names, and the transcript of the previous session for the librarian''s report. The Frontier is still assembled with no page opened; this step opens the page of each Estimate it reads and judges the reading against its `## Criterion`. Close those lines `[x] … · work` in `frontier.md` first, then write the reading lines in a `LEDGER` block of the reply, which ends in text. A reading whose `method` also names a later moment waits for that moment, its `/hi` part read then from the session''s first turn; a reading whose `method` asks for a `/hi` run of its own is not taken here (case 508.1). Wait for the human to pick the order or defer items.'
  change: /hi takes the readings of /hi and of the librarian's run in its first reply (case 508.1)
```

```tasks
- [ ] update `rule-skill-hi` — the reading step before the question on the order
- [ ] create `estimate-hi-takes-its-readings` — the promise of the reading step at `/hi`
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-takes-its-readings` — by hand, at the first `/hi` of the next session
```

### Case 508.2 — The Frontier at `/hi`: the Cases as a checklist, a `W` line closed where it is read

> **given:**
> `rule-skill-hi` — the page whose Render is the `/hi` skill; it says how the Frontier is shown in the chat and when a `W` line closes
> **＋** `.claude/skills/hi/SKILL.md` — the skill file rendered from `rule-skill-hi`
> **＋** `estimate-hi-writes-frontier` — the promise of the Frontier at `/hi`
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` — the sources of the Frontier
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the file of the Frontier

> **when:**
> The person invokes `/hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, and `## Work`, with lines `- [ ] W<n> — <title> · <source>`. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** `Pull:` and `Open issues:` are a Cases item only when `vault/wiki/sprint.md` names no decision on them.
> **－** Pre-spec finds an open line under `## Cases`. A `W` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: In the chat the Cases are the agenda of Plan Mode, one line each with its detail; the Work is one block; sub-cases are cut in Cases only;
    new: 'In the chat the Cases are the agenda of Plan Mode, shown as a checklist: each line as `frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, its detail on an indented line under it and the `- near` line under that, the line `Backlog: N items` last; no Case stands as a bold line or with its detail as a paragraph (case 508.2); the Work is one block; sub-cases are cut in Cases only;'
  - old: '`/pre-spec` fails on an open line under `## Cases`; a `W` line closes `· work` when its work is done, in Work Mode (case 356.1).'
    new: '`/pre-spec` fails on an open line under `## Cases`; a `W` line closes `· work` when its work is done, where it is done: at `/hi`, in Work Mode or at Retro (cases 356.1, 508.2).'
  change: the Cases shown in the chat at /hi as a checklist, the detail on an indented line; a W line closes where its work is done, at /hi, in Work Mode or at Retro (case 508.2, supersedes 507)
- slug: estimate-hi-writes-frontier
  set:
    status: pending
  change: the Criterion replaced whole — the Cases shown in the chat at /hi as a checklist, no bold line; a W line closes where its work is done (case 508.2, supersedes 507)
```

```tasks
- [ ] update `rule-skill-hi` — the Cases shown in the chat as a checklist; a `W` line closed where its work is done
- [ ] update `estimate-hi-writes-frontier` — the Criterion replaced whole: the Cases as a checklist, a `W` line closed where its work is done
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-writes-frontier` — by hand, at the first `/hi` of the next session
```

### Case 508.3 — `/work` takes the Work readings after the last task

> **given:**
> `rule-work-mode` — the page whose Render is the `/work` skill
> **＋** `.claude/skills/work/SKILL.md` — the skill file rendered from `rule-work-mode`
> **＋** `estimate-work-mode-takes-the-work-readings` — the promise of the reading step of `/work`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier, whose open `W` lines are the readings
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec whose tasks run first
> **＋** `rule-ledger-write` — refuses a reading of an Estimate the session creates or updates
> **＋** `rule-retro` — `/retro`, which follows and takes the readings left
> **＋** `rule-case-protocol` — a reply that carries a `LEDGER` block ends in text, with no tool call after it

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.

> **then:**
> Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
> **＋** A moment of an earlier session, such as the librarian's run, has come.
> **＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and a later reply, ending in text, carries its `estimate[...]` line inside a `LEDGER` block.
> **＋** The person can stop the step in the chat, and the lines not reached stay open.
> **－** A reading of an Estimate this session creates or updates is not taken, and its `W` line stays open.
> **－** A reading whose moment has not come is not taken, and its `W` line stays open.
> **－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

```then
create:
- slug: estimate-work-mode-takes-the-work-readings
  type: estimate
  ref: rule-work-mode
  kind: QA
  purpose: Whether /work, after the last task and before /retro, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line and writes its line, and leaves open the readings this session changes or whose moment has not come
  method: 'by hand at the first /work after the render: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-work-mode
  replace:
  - old: Work Mode ends with `/retro`.
    new: 'When the last task is done, take the Work readings before `/retro`: in the order of `frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come; a moment of an earlier session, such as the librarian''s run, has come. Leave a reading of an Estimate this session creates or updates, and one whose moment has not come: its line stays open. Close the line of each reading taken `[x] … · work` in `frontier.md` first, then write its `estimate[...]` line in a `LEDGER` block of a reply that ends in text; tick no `read` box. The person can stop the step in the chat, and the lines not reached stay open (case 508.3). Work Mode ends with `/retro`.'
  change: /work takes the open W readings after the last task, before /retro (case 508.3)
```

```tasks
- [ ] update `rule-work-mode` — the reading step after the last task
- [ ] create `estimate-work-mode-takes-the-work-readings` — the promise of the reading step of `/work`
- [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [ ] read `estimate-work-mode-takes-the-work-readings` — by hand, at the first `/work` of a session after the render
```

### Case 508.4 — The librarian writes the facts of its run into the brief

> **given:**
> `rule-brief` — the page whose Render is the brief section of the librarian's frame; it adds no decision and no judgment of the work
> **＋** `rule-documentation` — the page whose Render is the librarian's frame, its reasons to open a page and its archive step
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from both
> **＋** `vault/wiki/brief.md` — the brief, whose Readings due carry the facts
> **＋** `estimate-brief-carries-the-run-facts` — the promise of the facts in the brief
> **＋** `rule-raw-archive` — `uv run guppi archive`, the step after the brief
> **＋** `rule-close` — the commit of the librarian's run, its last step
> **＋** `rule-case-protocol` — only the main agent writes ledger lines

> **when:**
> The librarian `librarian-guppi` writes `vault/wiki/brief.md` in its run, and then runs `uv run guppi archive`.

> **then:**
> For each `pending` Estimate whose `method` names the librarian's run, its line under Readings due of `vault/wiki/brief.md` ends with the facts that its `method` and `## Criterion` name, as the steps of the run before the brief printed or left them.
> **＋** After `uv run guppi archive`, the librarian adds its stdout lines at the end of the Readings due line of each `pending` Estimate whose `method` names the archive step, and the close of `rule-close` commits the brief with them.
> **＋** Each Estimate keeps one line under Readings due, with the Estimate, its `draft` rule and where it is read.
> **－** The line compares nothing and carries no passed or failed, and the librarian writes no ledger line.
> **－** The order of the steps does not change: the brief, then `uv run guppi archive`, then the close.
> **－** No line of the brief names the commit of the close.

```then
create:
- slug: estimate-brief-carries-the-run-facts
  type: estimate
  ref: rule-brief
  kind: QA
  purpose: Whether the brief ends the Readings due line of each pending Estimate read at the librarian's run with the facts its method and Criterion name, the stdout of guppi archive included, with no comparison or verdict, one line per Estimate
  method: 'by hand at the /hi of the session after the first librarian run whose frame holds this Render: vault/wiki/brief.md read against the run''s report in the previous transcript, recorded in the estimate line'
  tags:
  - harness
  - workflow
  - librarian
update:
- slug: rule-brief
  replace:
  - old: or, when there is none, from the page's `method` (case 200.3);
    new: or, when there is none, from the page's `method` (case 200.3); for an Estimate whose `method` names the librarian's run, at the end of its line the facts its `method` and `## Criterion` name, as the steps of this run before the brief printed or left them, with no comparison and no passed or failed (case 508.4);
  change: a Readings due line of an Estimate read at the librarian's run ends with the facts of the run, no verdict (case 508.4)
- slug: rule-documentation
  replace:
  - old: the units it moved and the units it kept, with the reason, go into the report.
    new: the units it moved and the units it kept, with the reason, go into the report. Then add its stdout lines at the end of the Readings due line of each `pending` Estimate whose `method` names the archive step of the librarian's run, before the close commits the brief (case 508.4).
  change: the stdout of guppi archive added to the brief for an Estimate that reads it (case 508.4)
```

```tasks
- [ ] update `rule-brief` — the facts of the run at the end of a Readings due line
- [ ] update `rule-documentation` — the archive output added to the brief
- [ ] create `estimate-brief-carries-the-run-facts` — the promise of the facts in the brief
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-brief-carries-the-run-facts` — by hand, at the `/hi` after the first librarian run on the new frame
```

## Deferred

## Case 509 — The form of the Retro report is put off again

> **context:**
> Case 505 of session 0137 put off the form of the Retro report on `rule-retro`: a heading that names it Retro, its parts, and what the agent noticed in Work Mode set apart from the debt. The brief of that run carried it to session 1134 as a Case item. In session 1134 the person put it off again, before any Case was built on it.

> **problem:**
> How the Retro report should look: its heading, its parts and the place of what the agent noticed. The call of `/retro` right after Work Mode stays as it is.

```then
defer:
  - slug: rule-retro
    type: rule
    purpose: Discuss again how the Retro report should look — a heading that names it Retro, its parts, and what the agent noticed in Work Mode set apart from the debt; the call of /retro right after Work Mode stays; put off again in session 1134
```
