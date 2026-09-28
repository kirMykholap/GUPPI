## Case 490 — Slice 3g: the Estimates of the page schemas and the layout of the vault recut to `When:` and `Then:`

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds seven such pages: the Estimate of `rule-page-schemas`, the five Estimates of the category schemas under it (rules, entities, estimates, decisions, lessons), and the Estimate of `rule-vault-layout`. The five category pages share one `Given:`, which describes how `render` writes a file, the hook on a hand edit, and the keys lint reads. Each of them also keeps two lines from the day in September when the old `schema.md` files became `schema.yaml` files. One says the prose of "the former `schema.md`" stands in the file "verbatim". The other says `schema.md` "does not exist".
> The person decided in the first round on this item. The item goes in seven Cases by area, one group per Case. A one-time act leaves the Criterion and the lasting behaviour stays. A lost ratified text is restored, and a page with no `purpose` gets one. This group is the third, after cases 488 and 489. None of these pages lost its Criterion to a tool fault like case 211.3. Their History shows only Cases that changed the text on purpose (350, 358, 362.1, 372), so nothing is restored and no commit needs to be read. All seven pages already have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. The line on the keys lint reads names `properties.single`, and none of the five category schemas of this group carries that key. That line promises behaviour of `guppi/lint.py`, which belongs to the Estimates of `rule-lint`. From the prose line of each category page, "the former `schema.md`" and "verbatim" go out, because they tell where the text came from. The paragraphs the `description` holds stay, and so does the rule that `fields` and `sections` describe each name of the lists, which lint checks as the class `schema-description`. The Decision schema keeps its line on the History of a Decision (case 358), since the file still says so. The line "`schema.md` does not exist" leaves the five category pages. `estimate-page-schemas-one-file-per-rule` keeps it for every category, and a second copy would sign one promise twice. Two old lines say lint reads `computed: [rules]` and `ordered_children: true`. `guppi/lint.py` reads neither key, so the new line says the file holds them and lint does not read them. This is a line the code does not honour, corrected here and not dropped. 490.1 states a missing `schema.yaml` as the `schema` finding `schema.yaml is missing`, which `guppi/lint.py` gives. The old `Given:` said only "a missing file is a finding". "The six" files and "no seventh" become a statement with no count, so they cannot go stale. 490.7 moves into `Then:` the fact that `read_vault` does not read `schema.yaml` as a page. It drops the list of the files that may stand at the root of `wiki/`, because the check reads the rule pages for their names and keeps no list. Its old `－` line, "the finding it is today, not this one", becomes "no `layout` finding": 490.1 promises which finding a missing file gives, and 490.7 promises only that it is not a `layout` one.
> The check of the answer also notes that the `then` lines of 490.2 to 490.6 share most of their words. This is expected. The five category schemas are read in the same way, and the old pages were written in one form. Each sub-case names its own file, its own lists and its own `pytest -k` run, so a fault in one schema fails one promise alone. It also notes that 490.7 shares words with 490.1. 490.1 is about the schema files themselves, and 490.7 is about how lint reads the pages next to them.
> The frame. Each kept line was read against the live `schema.yaml` of its category, `check_descriptions`, `check_layout` and the missing-file finding of `guppi/lint.py`. None is contradicted. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. The sentence of `rule-estimates-schema` on `Given:` "until the one pass of its migration" stays true, and so does the rest of its Render, which this Case does not touch. `estimate-insights-schema-checked` has no `Given:` and is not touched. The Case creates no page, so no vault query was run. Not done: the other four groups (17 pages).

> **problem:**
> The seven Estimates of the page schemas and the layout of the vault still open with a `Given:` that describes the code of their day. Some of their lines record where a text came from, or state what lint reads when it does not read it. So their readings check history and stale claims next to the lasting promise.

> **recommend:**
> Replace each Criterion whole with only `When:` and `Then:`. Keep what each file holds and what lint judges, and drop the history of the move from `schema.md` and the copies of the one `schema.md` line. Keeping the prose lines word for word was rejected, because "verbatim from the former `schema.md`" can no longer be read against anything.

### Case 490.1 — One `schema.yaml` per category, from one rule

> **given:**
> `estimate-page-schemas-one-file-per-rule` — the promise, its Criterion replaced whole
> **＋** `rule-page-schemas` — the MOC it promises for; its children render the files
> **＋** `vault/wiki/<category>/schema.yaml` — the schema file of a category
> **＋** `guppi/render.py` — writes each file and `render --check`
> **＋** `guppi/lint.py` — reads each file; the classes `schema`, `path` and `schema-description`
> **＋** `rule-governed-files-hook` — the hook that refuses a hand edit
> **＋** `tests/test_render.py` — the test of two `full` pages on one file

> **when:**
> `guppi render` writes the governed files, and then `guppi lint` reads the vault.

> **then:**
> Each category folder of `vault/wiki/` holds one `schema.yaml`, written from the one child of `rule-page-schemas` that governs it, and `render --check` after the render exits 0.
> **＋** No other `schema.yaml` and no `schema.md` stands in a category folder.
> **＋** Lint reads each file and gives no finding of the class `path` or `schema-description` on the schema of a category.
> **＋** A category folder without its `schema.yaml` is the `schema` finding `schema.yaml is missing`.
> **＋** The hook of `rule-governed-files-hook` refuses a hand edit of any of the files.
> **－** A second `full` page on one of the files fails the render with the two slugs.

> **tasks:**
> - [ ] update `estimate-page-schemas-one-file-per-rule`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the count of files out, the missing file stated (case 490.1)`
> - [ ] read `estimate-page-schemas-one-file-per-rule` — `make lint` and `pytest tests/test_render.py`, then by hand after a later librarian's render

> **ratification:**
> ```
> - decision[case 490.1][update][estimate-page-schemas-one-file-per-rule]{ref:estimate-page-schemas-one-file-per-rule}
> ```

### Case 490.2 — The schema of a Rule page

> **given:**
> `estimate-rules-schema-checked` — the promise, its Criterion replaced whole
> **＋** `rule-rules-schema` — the Leaf whose Render is the file
> **＋** `vault/wiki/rules/schema.yaml` — the file written and read
> **＋** `vault/wiki/rules/` — the pages lint judges by it
> **＋** `guppi/render.py` — writes the file
> **＋** `guppi/lint.py` — the classes `schema` and `schema-description`
> **＋** `tests/test_schemas.py` — the tests the reading runs

> **when:**
> `guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`, and `guppi lint` reads a page of `vault/wiki/rules/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional.
> **＋** The file also holds `ordered_children: true`, which lint does not read.
> **＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, Ordering, MOCs and enforcement, Enforcement, the sentence on the edge Rule → Entity and the one on the guard of the agent's own conduct; `examples` holds the example pages.

> **tasks:**
> - [ ] update `estimate-rules-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given, the history of schema.md and the ordered_children read by lint out (case 490.2)`
> - [ ] read `estimate-rules-schema-checked` — `pytest tests/test_schemas.py -k rules`, then `make lint`

> **ratification:**
> ```
> - decision[case 490.2][update][estimate-rules-schema-checked]{ref:estimate-rules-schema-checked}
> ```

### Case 490.3 — The schema of an Entity page

> **given:**
> `estimate-entities-schema-checked` — the promise, its Criterion replaced whole
> **＋** `rule-entities-schema` — the Leaf whose Render is the file
> **＋** `vault/wiki/entities/schema.yaml` — the file written and read
> **＋** `vault/wiki/entities/` — the pages lint judges by it
> **＋** `guppi/render.py` — writes the file
> **＋** `guppi/lint.py` — the classes `schema` and `schema-description`
> **＋** `tests/test_schemas.py` — the tests the reading runs

> **when:**
> `guppi render` writes `vault/wiki/entities/schema.yaml` from `rule-entities-schema`, and `guppi lint` reads a page of `vault/wiki/entities/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `parent, children, code_ref, deferred_by, rules`; values `kind: MOC | Leaf`, `status: draft | built | archived`; conditional — `Leaf` requires `parent`, `MOC` requires `children`; the sections `## Purpose` and `## History` required, `## How it works`, `## Milestones`, `## Backlog`, `## Closed`, `## Terms` optional.
> **＋** The file also holds `computed: [rules]`, which lint does not read.
> **＋** An Entity page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; an Entity with `rules` on live Rules has none; the glossary page with `## Terms` has none.
> **＋** `fields` and `sections` describe each name of these lists, `rules` and `## Terms` among them; `description` holds the introduction, the Slug, `built`, `How it works` and Constraints notes, the sentence on the edge Rule → Entity and the one on the glossary page; `examples` holds the example pages.

> **tasks:**
> - [ ] update `estimate-entities-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given, the history of schema.md and the computed key read by lint out (case 490.3)`
> - [ ] read `estimate-entities-schema-checked` — `pytest tests/test_schemas.py -k entities`, then `make lint`

> **ratification:**
> ```
> - decision[case 490.3][update][estimate-entities-schema-checked]{ref:estimate-entities-schema-checked}
> ```

### Case 490.4 — The schema of an Estimate page

> **given:**
> `estimate-estimates-schema-checked` — the promise, its Criterion replaced whole
> **＋** `rule-estimates-schema` — the Leaf whose Render is the file
> **＋** `vault/wiki/estimates/schema.yaml` — the file written and read
> **＋** `vault/wiki/estimates/` — the pages lint judges by it
> **＋** `guppi/render.py` — writes the file
> **＋** `guppi/lint.py` — the classes `schema` and `schema-description`
> **＋** `tests/test_schemas.py` — the tests the reading runs

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, status, target, origin, sprint, created, tags`; optional `purpose, method, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Context`, `## Method`, `## Result` optional, `## Result` required on `passed` and on `failed`.
> **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds, among its paragraphs, the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.

> **tasks:**
> - [ ] update `estimate-estimates-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the history of schema.md out (case 490.4)`
> - [ ] read `estimate-estimates-schema-checked` — `pytest tests/test_schemas.py -k estimates`, then `make lint`

> **ratification:**
> ```
> - decision[case 490.4][update][estimate-estimates-schema-checked]{ref:estimate-estimates-schema-checked}
> ```

### Case 490.5 — The schema of a Decision page

> **given:**
> `estimate-decisions-schema-checked` — the promise, its Criterion replaced whole
> **＋** `rule-decisions-schema` — the Leaf whose Render is the file
> **＋** `vault/wiki/decisions/schema.yaml` — the file written and read
> **＋** `vault/wiki/decisions/` — the pages lint judges by it
> **＋** `guppi/render.py` — writes the file
> **＋** `guppi/lint.py` — the classes `schema` and `schema-description`
> **＋** `tests/test_schemas.py` — the tests the reading runs

> **when:**
> `guppi render` writes `vault/wiki/decisions/schema.yaml` from `rule-decisions-schema`, and `guppi lint` reads a page of `vault/wiki/decisions/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, case, status, origin, sprint, created, tags`; optional `create, update, delete, defer, source, supersedes, superseded_by`; values `status: current | superseded | archived`; the sections `## Context`, `## Problem` and `## History` required, `## Given`, `## When`, `## Criterion`, `## Deferred`, `## Note` optional.
> **＋** A Decision page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list or lacking a required section has one finding per defect.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, the fields deliberately absent and the body paragraph; `examples` holds the example page.
> **＋** The file says that the History of a Decision takes `created`, `superseded by` and one `updated:` line of a Case that signs its text after the fact.

> **tasks:**
> - [ ] update `estimate-decisions-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the history of schema.md out (case 490.5)`
> - [ ] read `estimate-decisions-schema-checked` — `pytest tests/test_schemas.py -k decisions`, then `make lint`

> **ratification:**
> ```
> - decision[case 490.5][update][estimate-decisions-schema-checked]{ref:estimate-decisions-schema-checked}
> ```

### Case 490.6 — The schema of a Lesson page

> **given:**
> `estimate-lessons-schema-checked` — the promise, its Criterion replaced whole
> **＋** `rule-lessons-schema` — the Leaf whose Render is the file
> **＋** `vault/wiki/lessons/schema.yaml` — the file written and read
> **＋** `vault/wiki/lessons/` — the pages lint judges by it
> **＋** `guppi/render.py` — writes the file
> **＋** `guppi/lint.py` — the classes `schema` and `schema-description`
> **＋** `tests/test_schemas.py` — the tests the reading runs

> **when:**
> `guppi render` writes `vault/wiki/lessons/schema.yaml` from `rule-lessons-schema`, and `guppi lint` reads a page of `vault/wiki/lessons/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, root_cause, status, origin, sprint, created, tags`; optional `source, insight`; values `kind: error | knowledge`, `status: new | clustered | archived`; conditional — `knowledge` requires `source`, `clustered` requires `insight`; the sections `## Trigger`, `## Root cause` and `## History` required.
> **＋** A Lesson page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, no Estimate and no `reviewed` status; `examples` holds the example pages.

> **tasks:**
> - [ ] update `estimate-lessons-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the history of schema.md out (case 490.6)`
> - [ ] read `estimate-lessons-schema-checked` — `pytest tests/test_schemas.py -k lessons`, then `make lint`

> **ratification:**
> ```
> - decision[case 490.6][update][estimate-lessons-schema-checked]{ref:estimate-lessons-schema-checked}
> ```

### Case 490.7 — A page in the wrong folder, a slug off its filename, a stray file at the root

> **given:**
> `estimate-vault-layout-holds` — the promise, its Criterion replaced whole
> **＋** `rule-vault-layout` — the rule it promises for
> **＋** `guppi/lint.py` — `check_layout`, the class `layout`
> **＋** `guppi/pages.py` — `read_vault`, which reads the pages of a category folder
> **＋** `vault/wiki/` — the category folders and the files at its root
> **＋** `tests/test_lint.py` — the tests the reading runs

> **when:**
> `guppi lint` reads the pages of the category folders of `vault/wiki/` and the `.md` files at its root.

> **then:**
> A page whose `type` does not match its folder is a `layout` finding.
> **＋** A page whose `slug` is not its filename without the extension is a `layout` finding.
> **＋** A `.md` at the root of `vault/wiki/` whose name no live rule page carries — in `governs` or in its text — is a `layout` finding.
> **＋** `read_vault` passes by the schema file of a category folder, so it is never judged as a page.
> **－** A category folder that lacks its schema file gives no `layout` finding.

> **tasks:**
> - [ ] update `estimate-vault-layout-holds`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the schema file not read as a page stated (case 490.7)`
> - [ ] read `estimate-vault-layout-holds` — `uv run pytest tests/test_lint.py -k layout`, then `make lint`

> **ratification:**
> ```
> - decision[case 490.7][update][estimate-vault-layout-holds]{ref:estimate-vault-layout-holds}
> ```

### Case 490.8 — The sprint page records the group of the page schemas and the layout

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on every other Estimate
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-page-schemas` — the MOC whose Estimates and those of its children this Case recuts
> **＋** `rule-vault-layout` — a rule whose Estimate this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of the page schemas and of `rule-vault-layout` are recut.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the Estimates of rule-page-schemas, its five category schemas and rule-vault-layout recut to When and Then; the note on every other Estimate stands (case 490)`

> **ratification:**
> ```
> - decision[case 490.8][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
