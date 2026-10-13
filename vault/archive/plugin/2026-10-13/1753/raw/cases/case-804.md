## Case 804 — CI writes a clean version of GUPPI to the branch prod

> **context:**
> Other people will install GUPPI from a clean copy of this project. That copy has no pointers to the decisions of this repository and none of its session records. Today nothing builds such a copy. `.github/workflows/checks.yml` runs the style, test and lint checks, and it skips a push to `prod`. The ruleset on `prod` that `rule-github-repository` sets lets only the owner write that branch, and that page plans to add the CI that writes `prod` to the bypass list. The texts carry these pointers everywhere. A Grep `\(cases? [0-9]` over `.claude/` counted 66 in 13 files, and a Grep `case [0-9]` over `guppi/` counted 894 in 32 files. Some sit inside a sentence, such as a link from `rule-page-read` to a Lesson page that names session 0051. The person chose, in this order:
> - the copy holds the code, the harness, the pages marked by a new optional field `core` and the files rendered from them (the person proposed the field, so that a page can stay in `main` while it is tried live)
> - a command removes what it can safely remove and fails on the rest
> - a push to `main`, or a push of a tag `prod-*` on a commit of another branch, writes `prod` as one commit on top of the last (at pre-spec the person put the tag in place of a run the owner starts by hand)
> - a deploy key with write access goes on the bypass list, and the workflow pushes to `prod` with it (in Work Mode, the GitHub Actions app could not be put on the bypass list of this repository, which belongs to a personal account, so the person chose the key in place of the app)
> - a new rule page, `rule-clean-branch`, which applies only to this repository and does not ship
> - the schema of rules says that a page with `core: true` comes into a new project without its Estimates, which that project writes through its own Cases (at pre-spec)
> - `entity-guppi`, `entity-sprint`, `entity-glossary` and every rule page but `rule-github-repository` get `core` now; no Estimate does
> - a shipped page carries `origin: guppi`, `sprint: guppi` and a History of one line, and the schemas and lint accept that
> - a later Case of this sprint rewords the text the command refuses
> - the copy leaves out `guppi.toml`, so the install step of Case 802 starts in a new project
> - the put-off question on the future shape of GUPPI, decision 616 on `entity-guppi`, stays open
>
> The rule that governs the options is `rule-ratification`: every page that ships carries a signed `core`, set by a decision line of its own, and no script marks a page. The removal and the check are new code that judges text. `rule-one-judgment-one-implementation` sets that they share the judgments that exist. A Grep `\\\(cases?` over `guppi/` printed nothing, so no code judges a parenthesis of case references today. A Grep `WIKILINK\s*=|CODE_SPAN\s*=` over `guppi/` printed `guppi/glossary.py`, `guppi/lint.py` and `guppi/sprint.py`. The check of body links calls `links_of` of `guppi/lint.py`, the function that the `ref` check of lint calls. The pattern of `guppi/glossary.py` reads one table cell, and the one of `guppi/sprint.py` reads a milestone line, so neither judges a page body. A Grep `^(ID|CASE_ID)\s*=|import ID as CASE_ID` over `guppi/` printed `guppi/caseid.py`, `guppi/box.py` and `guppi/lint.py`, so the pattern of a case reference is built on `ID` of `guppi/caseid.py`. The value `guppi` and the test for `core` are new. Both live in `guppi/pages.py`, which lint and the new `guppi/ship.py` import. The session folder patterns of `guppi/generate.py` and `guppi/materialize.py` judge a folder name, not a sentence, so the pattern of a session mention in prose is new.
>
> The frame showed four Criteria that the change makes false. `estimate-entities-schema-checked`, `estimate-rules-schema-checked` and `estimate-estimates-schema-checked` list every optional field of their schema, and `estimate-lint-finds-a-broken-link` calls an `origin` of another form a finding. Sub-cases 804.1 to 804.4 replace them, by the person's answer. Their `purpose` and `method` do not state the old promise, so they stand. A Grep `check_origin|ORIGIN_CASE|ORIGIN_LINE` over `guppi/` and `tests/` printed `guppi/lint.py`, `guppi/caseid.py` and `tests/test_caseid.py`. The test there reads both forms of a ledger origin, and that still holds. A Grep `` `origin` `` over `vault/wiki/` without `log.md` and `brief.md` printed 27 files. Two other sentences state the form of the field. The row `origin` of `entity-glossary` speaks of a page a Case created, which a shipped page in a new project is not, so it stands. The sentence of `rule-vault-layout` that `ref` and `origin` name filenames speaks of references to pages, and `guppi` names no page, so it stands. A Grep `\bcore\b` over `vault/wiki/` without `log.md` and `brief.md`, and over `.claude/`, printed nothing, so the new field clashes with no term.
>
> A Grep `schema\.yaml|rule-github-repository|estimate-lint-finds-a-broken-link|estimate-sprint-plugin-ci|checks\.yml` over `tests/` printed `tests/test_lint.py`, `tests/test_prespec.py`, `tests/test_casecheck.py`, `tests/test_ratified.py`, `tests/test_generate.py`, `tests/test_schemas.py`, `tests/test_materialize.py`, `tests/test_orchestration.py` and `tests/test_case_schema.py`.
> - `tests/test_schemas.py` reads the live schema files. Its value test takes the first entry of `values`, which stays `kind`. `core` adds no conditional.
> - `tests/test_generate.py`, `tests/test_materialize.py`, `tests/test_orchestration.py` and `tests/test_case_schema.py` copy the live schema files into a temporary folder. An optional field more lets a `create` key `core` through, and none of them writes that key. The stray-key test of `tests/test_materialize.py` uses `contract_note`.
> - The other files write schemas of their own.
>
> A Grep `\bprod\b` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `.github/workflows/checks.yml`, `vault/wiki/entities/entity-guppi-repository.md`, `vault/wiki/rules/rule-github-repository.md` and `vault/wiki/estimates/estimate-sprint-plugin-pull-requests-reviewed-on-github.md`. The sentence of `rule-github-repository` that plans the bypass changes in 804.7. So do its sentences on who writes `prod` and who pushes, and its `purpose`. The Purpose of `entity-guppi-repository` names `rule-github-repository` as its only rule, and 804.6 changes it. The Criterion on pull requests from a second account, which cannot push to `prod`, stays true. `checks.yml` keeps skipping a push to `prod`.
>
> Before the `create` of `rule-clean-branch`, which has no `ref`, the vault query of `ask-guppi` ran. The Greps `^(purpose|deferred_by):` over the rules and the entities show no page on a clean version. The nearest page is `rule-github-repository`, which holds the settings of the repository. `entity-guppi` carries the put-off decision 616, which the person left open. A Glob `vault/**/*clean-branch*` printed only `vault/wiki/estimates/estimate-sprint-plugin-ci-writes-a-clean-branch.md`, so `rule-clean-branch` and `estimate-clean-branch-writes-a-clean-copy` are free. The tags `ci`, `git` and `plugin` stand in `tags.md`.
>
> In 804.5 the marking adds one field and no sentence, and it changes no Render. I did not read the rule pages whole. A Grep `\bcore\b` over them printed nothing. Cases of this session change the text of some of them:
> - Case 802 changes `rule-morph` and `rule-guppi-config`.
> - Case 803 changes `rule-case-build` and `rule-case-protocol`.
> - Cases 800 and 801 change `rule-ask` and `rule-case-build`, by the ledger.
>
> A field beside their text contradicts none of them. The marks of 804.5 are checked by `estimate-sprint-plugin-ci-writes-a-clean-branch`, whose Criterion in 804.7 gains the line that `prod` holds each page with `core: true` and no other page: the live run reads exactly the set the marks choose, so a missing or stray mark shows there, by the person's answer at pre-spec. The new text of `rule-morph` from Case 802 links `entity-sprint-plugin` in its body. That link does not ship, so the check of 804.6 will refuse it, and it goes to the rewording Case. The pages get `core` at the librarian's run, after Work Mode. So the Work Mode run of `guppi ship` lists only the leftovers of the code and the harness. The leftovers of the pages come from the first CI run, which the owner starts by a tag `prod-*` on a commit of `plugin` after pushing the librarian's commit, by the person's answer.
>
> At pre-spec the check of the plan asked for an update of the sprint page, since this Case works on an item of the sprint. 804.7 gives the item of the milestone The clean branch of `entity-sprint-plugin` two links, `rule-clean-branch` and `estimate-sprint-plugin-ci-writes-a-clean-branch`. By the person's answer, the item ticks only when the rule is `built` and the live run has passed, which comes after the rewording Case. Case 802, as its file stands, updates the same page in its `## Backlog`. The pair of 804.7 changes only the line of the item of The clean branch, so the two changes do not touch the same text. Its Estimate `estimate-sprint-plugin-ci-writes-a-clean-branch` gets a new trigger in 804.7. Its `purpose` still states the promise and stands. Its `method` is set anew to name the run by tag and the reading of the `on:` block. The last brief, under `## Readings at the close`, reports `make test` at 1587 passed and 6 skipped, and `make lint` at 2 lines: the defer count of `rule-morph`, and the failed reading of `estimate-case-build-reads-the-last-output-of-a-check`. No check of this Case rests on lint over the copy.

> **problem:**
> Nothing builds the version of GUPPI that other people install. Every text points to this repository's decisions and sessions, nothing marks which pages belong to GUPPI itself, and the schemas and lint have no shape for a page that shipped.

> **recommend:**
> - **What does the clean version hold?**
>   - Recommended: (a) code, harness and rule pages, with history fields and links to pages left out removed; no Entity, Estimate, Lesson, Insight or Decision page, and no session records.
>   - Answer: agreed, (a). The person asked whether the Entity page of the sprint as a kind should ship too, since it is part of how GUPPI works. A later question took that up.
> - **How do the pointers to past decisions leave the text?**
>   - Recommended: (a) a script removes them, and a check fails on the rest.
>   - Answer: agreed, (a).
> - **What starts a run, and from which branch?**
>   - Recommended: (a) a push to `main`, plus a run by hand on any branch.
>   - Answer: agreed, (a).
> - **How does `prod` keep its history?**
>   - Recommended: (a) one new commit per run, on top of the last one.
>   - Answer: agreed, (a).
> - **How does CI get the right to write `prod`?**
>   - Recommended: (a) the built-in GitHub Actions account on the bypass list.
>   - Answer: agreed, (a).
> - **Which page sets the rule of the clean branch?**
>   - Recommended: (a) a new rule page, `rule-clean-branch`.
>   - Answer: agreed, (a).
> - **Which Entity pages go into the clean version?**
>   - Recommended: (a) the three pages that describe GUPPI as a tool: `entity-guppi`, `entity-sprint` and `entity-glossary`.
>   - Answer: agreed, (a).
> - **Do the rules that apply only to this repository ship?**
>   - Recommended: (a) a rule that applies only to a page left out stays out.
>   - Answer: agreed, (a). The person proposed an explicit page field, `core`, that tells the build which pages ship, so that a page can stay in `main` while it is tried live. The next question took it up.
> - **Does each page carry an explicit flag that says it ships?**
>   - Recommended: (a) an opt-in `core` field on Entity, Rule and Estimate pages.
>   - Answer: agreed, (a).
> - **What do shipped pages carry in place of their history fields?**
>   - Recommended: (a) the copy writes neutral values, and the schema accepts them.
>   - Answer: agreed, (a).
> - **Do any Estimate pages ship?**
>   - Recommended: (a) none now.
>   - Answer: agreed, (a).
> - **Which pages get `core` now, and how?**
>   - Recommended: (a) all of them in this Case, in a sub-case of their own.
>   - Answer: agreed, (a).
> - **What happens to text the script cannot clean on the first run?**
>   - Recommended: (a) a later Case of this sprint rewords them.
>   - Answer: agreed, (a).
> - **How does the Case split, and how is each part checked?**
>   - Recommended: (a) four sub-cases, each with its own check.
>   - Answer: agreed, (a).
> - **Does this Case settle the put-off question on GUPPI's future shape?**
>   - Recommended: (a) it stands open.
>   - Answer: agreed, (a).
> - **What else does the check refuse in the copy?**
>   - Recommended: (a) both a link in the text to a page left out and a mention of a session fail the run.
>   - Answer: agreed, (a).
> - **How does the part on the schemas and lint split?**
>   - Recommended: (a) four sub-cases, each replacing one existing Criterion, and no new Estimate.
>   - Answer: agreed, (a).
> - **Does the copy carry this project's `guppi.toml`?**
>   - Recommended: (a) the copy leaves out `guppi.toml`.
>   - Answer: agreed, (a).
> - **Where does the list of leftovers for the pages come from?**
>   - Recommended: (a) code and harness from Work Mode, pages from the first run on GitHub.
>   - Answer: agreed, (a).
> - **Do the Estimates of the shipped rules ship after all?**
>   - Recommended: (a) no Estimate ships, and the schema of rules says why.
>   - Answer: agreed, (a): let us try it that way.
> - **When does the milestone The clean branch count as done?**
>   - Recommended: (a) the item links the rule and the sprint's check of the live run.
>   - Answer: agreed, (a).
> - **How does the workflow get the right to write `prod`?**
>   - Recommended: (a) a deploy key on the bypass list.
>   - Answer: agreed, (a); the person asked what to do, and the steps stand as `stop:` tasks of 804.7.
> - **Change**
>   - Asked: at pre-spec, the Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` names that `prod` holds exactly the pages with `core: true`, so that the marks of 804.5 are checked.
>   - Taken: 804.7 adds that line to the Criterion, and the `context` names it.
> - **Change**
>   - Asked: at pre-spec, a push of a tag `prod-*` on a commit of `plugin` starts the run in place of a run by hand; a push to `main` still starts it, and that line is checked by reading the `on:` block of the workflow.
>   - Taken: the `when` and `then` of 804.7, the `method` of its Estimate, the workflow task and the Purpose of `rule-clean-branch` say so.

### Case 804.1 — The Entity schema carries the field core and the shipped values

> **given:**
> `rule-entities-schema`: renders the schema of Entity pages.
> **＋** `vault/wiki/entities/schema.yaml`: the file rendered from it.
> **＋** `estimate-entities-schema-checked`: its Criterion is replaced whole.
> **＋** `tests/test_schemas.py`: the tests of the live schema files.

> **when:**
> `guppi render` writes `vault/wiki/entities/schema.yaml` from `rule-entities-schema`, and `guppi lint` reads a page of `vault/wiki/entities/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `parent, children, code_ref, deferred_by, rules, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `core: true`; conditional — `Leaf` requires `parent`, `MOC` requires `children`; the sections `## Purpose` and `## History` required, `## How it works`, `## Milestones`, `## Backlog`, `## Closed`, `## Terms` optional.
> **＋** The file also holds `computed: [rules]`, which lint does not read.
> **＋** An Entity page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; an Entity with `rules` on live Rules has none; the glossary page with `## Terms` has none.
> **＋** An Entity page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `rules`, `core` and `## Terms` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, the Slug, `built`, `How it works` and Constraints notes, the sentence on the edge Rule → Entity and the one on the glossary page; `examples` holds the example pages.

> **tasks:**
> - [ ] update `rule-entities-schema`
>   - old: `optional: [parent, children, code_ref, deferred_by, rules]`
>   - new: `optional: [parent, children, code_ref, deferred_by, rules, core]`
>   - old: `status: [draft, built, archived]`
>   - new:
>     ```
>     status: [draft, built, archived]
>         core: [true]
>     ```
>   - old: `(case 103.6). The ratified decision that created it.`
>   - new: `` (case 103.6). The ratified decision that created it. On a page with `core: true` in the clean version that `guppi ship` writes, it is `guppi`, and lint accepts it there (case 804). ``
>   - old: `required; the sprint id.`
>   - new:
>     ```
>     required; the sprint id; `guppi` on a page with `core: true` in the clean version that `guppi ship` writes (case 804).
>       core: |
>         optional; `true`. The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. Set by a Case, never by hand (case 804).
>     ```
>   - change: `the field core, and the value guppi of origin and sprint on a page of the clean version (case 804)`
> - [ ] update `estimate-entities-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the field core and the shipped values (case 804)`
> - [ ] `uv run guppi render`: `vault/wiki/entities/schema.yaml`
> - [ ] `tests/test_schemas.py`: the case `entities` of a test that a page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> - [ ] read `estimate-entities-schema-checked`

> **ratification:**
> ```
> - decision[case 804.1][update][rule-entities-schema]{ref:rule-entities-schema}
> - decision[case 804.1][update][estimate-entities-schema-checked]{ref:rule-entities-schema}
> ```

### Case 804.2 — The Rule schema carries the field core and the shipped values

> **given:**
> `rule-rules-schema`: renders the schema of Rule pages.
> **＋** `vault/wiki/rules/schema.yaml`: the file rendered from it.
> **＋** `estimate-rules-schema-checked`: its Criterion is replaced whole.
> **＋** `tests/test_schemas.py`: the tests of the live schema files.

> **when:**
> `guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`, and `guppi lint` reads a page of `vault/wiki/rules/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`, `core: true`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional.
> **＋** The file also holds `ordered_children: true`, which lint does not read.
> **＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
> **＋** A Rule page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, Ordering, MOCs and enforcement, Enforcement, the sentence on the edge Rule → Entity, the one on the guard of the agent's own conduct and the one that a page with `core: true` comes into a new project without its Estimates, which that project writes through its own Cases; `examples` holds the example pages.

> **tasks:**
> - [ ] update `rule-rules-schema`
>   - old: `Every Rule requires an Estimate.`
>   - new: `` Every Rule requires an Estimate; a page with `core: true` comes into a new project without its Estimates, and that project writes its own through its Cases (case 804). ``
>   - old: `optional: [enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to]`
>   - new: `optional: [enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to, core]`
>   - old: `render_mode: [full, partial]`
>   - new:
>     ```
>     render_mode: [full, partial]
>         core: [true]
>     ```
>   - old: `on pages born before 2026-09-13 (case 103.6).`
>   - new: `` on pages born before 2026-09-13 (case 103.6). On a page with `core: true` in the clean version that `guppi ship` writes, it is `guppi`, and lint accepts it there (case 804). ``
>   - old: `required; the sprint id.`
>   - new:
>     ```
>     required; the sprint id; `guppi` on a page with `core: true` in the clean version that `guppi ship` writes (case 804).
>       core: |
>         optional; `true`. The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. Set by a Case, never by hand (case 804).
>     ```
>   - change: `the field core, and the value guppi of origin and sprint on a page of the clean version (case 804)`
> - [ ] update `estimate-rules-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the field core and the shipped values (case 804)`
> - [ ] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
> - [ ] `tests/test_schemas.py`: the case `rules` of a test that a page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> - [ ] read `estimate-rules-schema-checked`

> **ratification:**
> ```
> - decision[case 804.2][update][rule-rules-schema]{ref:rule-rules-schema}
> - decision[case 804.2][update][estimate-rules-schema-checked]{ref:rule-rules-schema}
> ```

### Case 804.3 — The Estimate schema carries the field core and the shipped values

> **given:**
> `rule-estimates-schema`: renders the schema of Estimate pages.
> **＋** `vault/wiki/estimates/schema.yaml`: the file rendered from it.
> **＋** `estimate-estimates-schema-checked`: its Criterion is replaced whole.
> **＋** `tests/test_schemas.py`: the tests of the live schema files.

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked, deferred_by, core`; values `kind: QA | Research`, `status: pending | passed | failed`, `core: true`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
> **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
> **＋** An Estimate page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds, among its paragraphs, the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
> **－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.

> **tasks:**
> - [ ] update `rule-estimates-schema`
>   - old: `optional: [purpose, checked, deferred_by]`
>   - new: `optional: [purpose, checked, deferred_by, core]`
>   - old: `status: [pending, passed, failed]`
>   - new:
>     ```
>     status: [pending, passed, failed]
>         core: [true]
>     ```
>   - old: `(case 103.6). The ratified decision that created it.`
>   - new: `` (case 103.6). The ratified decision that created it. On a page with `core: true` in the clean version that `guppi ship` writes, it is `guppi`, and lint accepts it there (case 804). ``
>   - old: `required; the sprint id.`
>   - new:
>     ```
>     required; the sprint id; `guppi` on a page with `core: true` in the clean version that `guppi ship` writes (case 804).
>       core: |
>         optional; `true`. The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. Set by a Case, never by hand (case 804).
>     ```
>   - change: `the field core, and the value guppi of origin and sprint on a page of the clean version (case 804)`
> - [ ] update `estimate-estimates-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the field core and the shipped values (case 804)`
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] `tests/test_schemas.py`: the case `estimates` of a test that a page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> - [ ] read `estimate-estimates-schema-checked`

> **ratification:**
> ```
> - decision[case 804.3][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 804.3][update][estimate-estimates-schema-checked]{ref:rule-estimates-schema}
> ```

### Case 804.4 — Lint accepts the origin guppi on a page marked core

> **given:**
> `guppi/lint.py`: `check_origin` judges the `origin` of a page.
> **＋** `guppi/pages.py`: holds the value `guppi` and the test of `core: true`, which lint and `guppi/ship.py` import.
> **＋** `tests/test_lint.py`: the tests of lint.
> **＋** `estimate-lint-finds-a-broken-link`: its Criterion is replaced whole.
> **＋** `rule-lint`: the rule of lint, whose `implementation_ref` names `guppi/lint.py`.
> **＋** `vault/wiki/`: the live pages lint reads.
> **＋** `vault/raw/` and `vault/archive/`: where the ledger of an `origin` stands.
> **＋** `raw/<date>[/<HHMM>]/ledger.md#case-N`: the form of an `origin` that names a ledger.
> **＋** `guppi/materialize.py`: `category_of`, which gives the category of a slug by its prefix, `decision-` included.

> **when:**
> `uv run guppi lint` follows the links of the live pages under `vault/wiki/`.

> **then:**
> `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a body `[[…]]` that no live or archived page carries; a body `[[…]]` may name a file under `vault/wiki/` by stem or path; a `[[…]]` inside a code span is no link.
> **＋** `ref`: an `applies_to` naming a page that is not an Entity; an Entity whose `rules` differs from the live rules whose `applies_to` names it, the difference as `+slug` and `-slug`.
> **＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate.
> **＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
> **＋** An `origin` `#case-N` of a Case that has no ledger line of its own is found by a line of one of its sub-cases, `[case N.M]`.
> **＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer` and no `children`, or with `kind` or `target_slug`; a slug of its lists that `category_of` of `guppi/materialize.py` gives a category — the prefix `decision-` included — and that no live or archived page carries.
> **＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.
> **－** A `### case N` line under an Estimate's `## Criterion` is not read as a link.
> **－** An `origin` `guppi` on a page with `core: true` is no finding; on a page without `core: true` it is an `origin` of another form.

> **tasks:**
> - [ ] `guppi/pages.py`: `SHIPPED = "guppi"`, the value of `origin` and `sprint` on a page of the clean version, and `is_core(page)`, true when the page carries `core: true` — the one judgment of both, which `guppi/lint.py` and `guppi/ship.py` import.
> - [ ] `guppi/lint.py`: `check_origin` returns no finding for an `origin` equal to `SHIPPED` on a page that `is_core` accepts; the docstring names it.
> - [ ] `tests/test_lint.py`: a page with `core: true` and `origin: guppi` has no `origin` finding, and a page with `origin: guppi` and no `core` has one.
> - [ ] update `estimate-lint-finds-a-broken-link`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the origin guppi on a page with core: true is no finding (case 804)`
> - [ ] read `estimate-lint-finds-a-broken-link`

> **ratification:**
> ```
> - decision[case 804.4][update][estimate-lint-finds-a-broken-link]{ref:rule-lint}
> ```

### Case 804.5 — The pages that ship carry core

> **given:**
> `vault/wiki/rules/`: each rule page but `rule-github-repository` gains `core: true`.
> **＋** The rule pages that gain `core: true`: `rule-agent-writing`, `rule-ask`, `rule-atomicity`, `rule-backlog`, `rule-bash-guard`, `rule-brief`, `rule-carry-over`, `rule-case-build`, `rule-case-check`, `rule-case-example`, `rule-case-protocol`, `rule-claude-md`, `rule-cleanup`, `rule-close`, `rule-compact-recall`, `rule-context-size`, `rule-decisions-schema`, `rule-default-mode`, `rule-documentation`, `rule-end-of-work`, `rule-entities-schema`, `rule-estimates-schema`, `rule-event-log`, `rule-git-context`, `rule-glossary`, `rule-governed-files-hook`, `rule-guppi-config`, `rule-handoff`, `rule-harness`, `rule-hook-registry`, `rule-index-check`, `rule-insights-schema`, `rule-internal-context`, `rule-language`, `rule-ledger-tail`, `rule-ledger-write`, `rule-lessons-schema`, `rule-lint`, `rule-materialize`, `rule-morph`, `rule-one-judgment-one-implementation`, `rule-orchestration`, `rule-page-generation`, `rule-page-read`, `rule-page-schemas`, `rule-permissions`, `rule-plan-mode`, `rule-powershell-guard`, `rule-prespec`, `rule-prespec-hook`, `rule-prespec-onward`, `rule-python-utf8`, `rule-ratification`, `rule-raw-archive`, `rule-render-harness`, `rule-retro`, `rule-retro-commit`, `rule-retro-onward`, `rule-rules-schema`, `rule-search-leaves-out-decisions`, `rule-session`, `rule-session-start`, `rule-settings`, `rule-shell-write-check`, `rule-skill-grill-me`, `rule-skill-hi`, `rule-skill-merge-main`, `rule-skill-pr-review`, `rule-skill-sprint-close`, `rule-skill-sprint-open`, `rule-skill-wait-what`, `rule-spec-box`, `rule-spec-capture`, `rule-spec-reconcile`, `rule-spec-write`, `rule-sprint`, `rule-sprint-close`, `rule-synthesis`, `rule-tests-clock-pinned`, `rule-vault-layout`, `rule-where-to-stop` and `rule-work-mode`.
> **＋** `entity-guppi`, `entity-sprint` and `entity-glossary`: each gains `core: true`.
> **＋** `rule-github-repository`, `rule-clean-branch`, `entity-guppi-repository` and `entity-sprint-plugin`: the pages of this repository alone, with no `core`.
> **＋** `rule-clean-branch`: the rule of `guppi ship`, which chooses the pages by `core`.
> **＋** `vault/raw/2026-10-13/1753/cases/case-802.md`: Case 802 changes the text of `rule-morph` and `rule-guppi-config`.
> **＋** `vault/raw/2026-10-13/1753/cases/case-803.md`: Case 803 changes the text of `rule-case-build` and `rule-case-protocol`.

> **when:**
> `uv run guppi ship`, as `rule-clean-branch` sets it, reads the pages under `vault/wiki/` to choose the pages of the clean version.

> **then:**
> Each rule page under `vault/wiki/rules/` but `rule-github-repository` and `rule-clean-branch`, and `entity-guppi`, `entity-sprint` and `entity-glossary`, carries `core: true`, and the clean version holds it.
> **－** `rule-github-repository`, `rule-clean-branch`, `entity-guppi-repository`, `entity-sprint-plugin` and every Estimate carry no `core`, and the clean version does not hold them.

> **tasks:**
> - [ ] update `rule-agent-writing`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-ask`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-atomicity`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-backlog`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-bash-guard`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-brief`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-carry-over`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-case-build`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-case-check`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-case-example`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-case-protocol`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-claude-md`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-cleanup`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-close`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-compact-recall`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-context-size`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-decisions-schema`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-default-mode`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-documentation`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-end-of-work`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-entities-schema`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-estimates-schema`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-event-log`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-git-context`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-glossary`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-governed-files-hook`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-guppi-config`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-handoff`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-harness`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-hook-registry`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-index-check`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-insights-schema`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-internal-context`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-language`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-ledger-tail`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-ledger-write`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-lessons-schema`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-lint`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-materialize`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-morph`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-one-judgment-one-implementation`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-orchestration`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-page-generation`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-page-read`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-page-schemas`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-permissions`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-plan-mode`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-powershell-guard`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-prespec`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-prespec-hook`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-prespec-onward`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-python-utf8`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-ratification`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-raw-archive`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-render-harness`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-retro`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-retro-commit`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-retro-onward`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-rules-schema`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-search-leaves-out-decisions`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-session`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-session-start`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-settings`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-shell-write-check`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-skill-grill-me`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-skill-hi`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-skill-merge-main`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-skill-pr-review`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-skill-sprint-close`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-skill-sprint-open`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-skill-wait-what`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-spec-box`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-spec-capture`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-spec-reconcile`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-spec-write`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-sprint`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-sprint-close`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-synthesis`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-tests-clock-pinned`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-vault-layout`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-where-to-stop`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `rule-work-mode`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `entity-guppi`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `entity-sprint`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`
> - [ ] update `entity-glossary`
>   - set: `{core: true}`
>   - change: `ships in the clean version (case 804)`

> **ratification:**
> ```
> - decision[case 804.5][update][rule-agent-writing]{ref:rule-agent-writing}
> - decision[case 804.5][update][rule-ask]{ref:rule-ask}
> - decision[case 804.5][update][rule-atomicity]{ref:rule-atomicity}
> - decision[case 804.5][update][rule-backlog]{ref:rule-backlog}
> - decision[case 804.5][update][rule-bash-guard]{ref:rule-bash-guard}
> - decision[case 804.5][update][rule-brief]{ref:rule-brief}
> - decision[case 804.5][update][rule-carry-over]{ref:rule-carry-over}
> - decision[case 804.5][update][rule-case-build]{ref:rule-case-build}
> - decision[case 804.5][update][rule-case-check]{ref:rule-case-check}
> - decision[case 804.5][update][rule-case-example]{ref:rule-case-example}
> - decision[case 804.5][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 804.5][update][rule-claude-md]{ref:rule-claude-md}
> - decision[case 804.5][update][rule-cleanup]{ref:rule-cleanup}
> - decision[case 804.5][update][rule-close]{ref:rule-close}
> - decision[case 804.5][update][rule-compact-recall]{ref:rule-compact-recall}
> - decision[case 804.5][update][rule-context-size]{ref:rule-context-size}
> - decision[case 804.5][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 804.5][update][rule-default-mode]{ref:rule-default-mode}
> - decision[case 804.5][update][rule-documentation]{ref:rule-documentation}
> - decision[case 804.5][update][rule-end-of-work]{ref:rule-end-of-work}
> - decision[case 804.5][update][rule-entities-schema]{ref:rule-entities-schema}
> - decision[case 804.5][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 804.5][update][rule-event-log]{ref:rule-event-log}
> - decision[case 804.5][update][rule-git-context]{ref:rule-git-context}
> - decision[case 804.5][update][rule-glossary]{ref:rule-glossary}
> - decision[case 804.5][update][rule-governed-files-hook]{ref:rule-governed-files-hook}
> - decision[case 804.5][update][rule-guppi-config]{ref:rule-guppi-config}
> - decision[case 804.5][update][rule-handoff]{ref:rule-handoff}
> - decision[case 804.5][update][rule-harness]{ref:rule-harness}
> - decision[case 804.5][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 804.5][update][rule-index-check]{ref:rule-index-check}
> - decision[case 804.5][update][rule-insights-schema]{ref:rule-insights-schema}
> - decision[case 804.5][update][rule-internal-context]{ref:rule-internal-context}
> - decision[case 804.5][update][rule-language]{ref:rule-language}
> - decision[case 804.5][update][rule-ledger-tail]{ref:rule-ledger-tail}
> - decision[case 804.5][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 804.5][update][rule-lessons-schema]{ref:rule-lessons-schema}
> - decision[case 804.5][update][rule-lint]{ref:rule-lint}
> - decision[case 804.5][update][rule-materialize]{ref:rule-materialize}
> - decision[case 804.5][update][rule-morph]{ref:rule-morph}
> - decision[case 804.5][update][rule-one-judgment-one-implementation]{ref:rule-one-judgment-one-implementation}
> - decision[case 804.5][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 804.5][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 804.5][update][rule-page-read]{ref:rule-page-read}
> - decision[case 804.5][update][rule-page-schemas]{ref:rule-page-schemas}
> - decision[case 804.5][update][rule-permissions]{ref:rule-permissions}
> - decision[case 804.5][update][rule-plan-mode]{ref:rule-plan-mode}
> - decision[case 804.5][update][rule-powershell-guard]{ref:rule-powershell-guard}
> - decision[case 804.5][update][rule-prespec]{ref:rule-prespec}
> - decision[case 804.5][update][rule-prespec-hook]{ref:rule-prespec-hook}
> - decision[case 804.5][update][rule-prespec-onward]{ref:rule-prespec-onward}
> - decision[case 804.5][update][rule-python-utf8]{ref:rule-python-utf8}
> - decision[case 804.5][update][rule-ratification]{ref:rule-ratification}
> - decision[case 804.5][update][rule-raw-archive]{ref:rule-raw-archive}
> - decision[case 804.5][update][rule-render-harness]{ref:rule-render-harness}
> - decision[case 804.5][update][rule-retro]{ref:rule-retro}
> - decision[case 804.5][update][rule-retro-commit]{ref:rule-retro-commit}
> - decision[case 804.5][update][rule-retro-onward]{ref:rule-retro-onward}
> - decision[case 804.5][update][rule-rules-schema]{ref:rule-rules-schema}
> - decision[case 804.5][update][rule-search-leaves-out-decisions]{ref:rule-search-leaves-out-decisions}
> - decision[case 804.5][update][rule-session]{ref:rule-session}
> - decision[case 804.5][update][rule-session-start]{ref:rule-session-start}
> - decision[case 804.5][update][rule-settings]{ref:rule-settings}
> - decision[case 804.5][update][rule-shell-write-check]{ref:rule-shell-write-check}
> - decision[case 804.5][update][rule-skill-grill-me]{ref:rule-skill-grill-me}
> - decision[case 804.5][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 804.5][update][rule-skill-merge-main]{ref:rule-skill-merge-main}
> - decision[case 804.5][update][rule-skill-pr-review]{ref:rule-skill-pr-review}
> - decision[case 804.5][update][rule-skill-sprint-close]{ref:rule-skill-sprint-close}
> - decision[case 804.5][update][rule-skill-sprint-open]{ref:rule-skill-sprint-open}
> - decision[case 804.5][update][rule-skill-wait-what]{ref:rule-skill-wait-what}
> - decision[case 804.5][update][rule-spec-box]{ref:rule-spec-box}
> - decision[case 804.5][update][rule-spec-capture]{ref:rule-spec-capture}
> - decision[case 804.5][update][rule-spec-reconcile]{ref:rule-spec-reconcile}
> - decision[case 804.5][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 804.5][update][rule-sprint]{ref:rule-sprint}
> - decision[case 804.5][update][rule-sprint-close]{ref:rule-sprint-close}
> - decision[case 804.5][update][rule-synthesis]{ref:rule-synthesis}
> - decision[case 804.5][update][rule-tests-clock-pinned]{ref:rule-tests-clock-pinned}
> - decision[case 804.5][update][rule-vault-layout]{ref:rule-vault-layout}
> - decision[case 804.5][update][rule-where-to-stop]{ref:rule-where-to-stop}
> - decision[case 804.5][update][rule-work-mode]{ref:rule-work-mode}
> - decision[case 804.5][update][entity-guppi]{ref:entity-guppi}
> - decision[case 804.5][update][entity-sprint]{ref:entity-sprint}
> - decision[case 804.5][update][entity-glossary]{ref:entity-glossary}
> ```

### Case 804.6 — guppi ship builds and checks the clean version

> **given:**
> `rule-clean-branch`: the new rule of the clean version, applied to `entity-guppi-repository`.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: the new check of the command.
> **＋** `guppi/ship.py`: the new command that builds and checks the clean version.
> **＋** `guppi/cli.py`: registers the command `ship`.
> **＋** `tests/test_ship.py`: the tests of the command over a sample tree.
> **＋** `guppi/lint.py`, `guppi/caseid.py` and `guppi/pages.py`: the judgments the command imports — `links_of`, `ID`, `HISTORY`, `MARKER`, `SHIPPED` and `is_core`.
> **＋** `entity-guppi-repository`: its Purpose names its rules.
> **＋** `rule-one-judgment-one-implementation`: one judgment, one implementation.
> **＋** `.claude/`, `vault/wiki/` and `vault/wiki/tags.md`: the harness, the pages and the tag registry the command copies.
> **＋** `vault/raw/`, `vault/archive/` and `.github/`: the session records and the workflows the command leaves out.

> **when:**
> `uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

> **then:**
> It writes `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
> **＋** In each file it writes, it removes a parenthesis that holds only references to cases, the references to cases inside a longer parenthesis, and each `[[decision-case-N]]` link.
> **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
> **＋** It exits 1, and prints the file and the line, for each reference to a case, each link in a text to a page or a file it does not write, and each mention of a session of this repository by its id that remains.
> **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
> **－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
> **－** It writes no file that a page without `core: true` renders in full.
> **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.

> **tasks:**
> - [ ] create `rule-clean-branch`
>   - kind: `Leaf`
>   - purpose: `Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install`
>   - enforcement: `check`
>   - implementation_ref: `[guppi/ship.py, tests/test_ship.py, .github/workflows/prod.yml]`
>   - applies_to: `["[[entity-guppi-repository]]"]`
>   - tags: `[ci, git, plugin]`
>   - sections.Purpose:
>     ```
>     Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install. `guppi ship` builds that version from the working tree into an empty folder: `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page with `core: true` and each file rendered from such a page, but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project. It removes a parenthesis that holds only references to cases, the references to cases inside a longer parenthesis, and each `[[decision-case-N]]` link. It gives each page `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line, and keeps in its link fields only the pages it writes. It exits 1 on each reference to a case, link to a page or a file it does not write, mention of a session of this repository, or section of a page without `core: true` that remains; a Case rewords that text at its source.
> 
>     The workflow `.github/workflows/prod.yml` runs it on each push to `main`, and on each push of a tag `prod-*`, such as `prod-1`, on a commit of another branch. It writes the result to the branch `prod` as one new commit on top of the last, whose message names the commit it was built from, and writes none when nothing changed or when the command exits 1. It pushes with a deploy key of this repository with write access, whose private half is the repository secret `PROD_DEPLOY_KEY`; deploy keys stand on the bypass list of the ruleset on `prod` that [[rule-github-repository]] sets. This rule and the workflow belong to this repository: neither carries `core`, and `.github/` is not part of the clean version (case 804).
>     ```
> - [ ] create `estimate-clean-branch-writes-a-clean-copy`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether guppi ship writes only the code, the harness and the pages with core: true, removes the references to cases, writes the shipped values, and exits 1 on what it cannot clean`
>   - method: `uv run pytest tests/test_ship.py`
>   - tags: `[ci, plugin]`
> - [ ] update `entity-guppi-repository`
>   - old: `` Its rules are those of `rule-github-repository`, which names this page in `applies_to`: the rulesets on `main` and `prod`, the workflow of checks, and the approval of the runs of an outside contributor. ``
>   - new: `` Its rules are `rule-github-repository` — the rulesets on `main` and `prod`, the workflow of checks and the approval of the runs of an outside contributor — and `rule-clean-branch`, the workflow that writes the clean version of GUPPI to `prod`; each names this page in `applies_to` (case 804). ``
>   - change: `its rules name rule-clean-branch beside rule-github-repository (case 804)`
> - [ ] `guppi/ship.py`: the command `guppi ship <folder>` as the `then` of this Case sets it. It reads pages by `read_vault`, `HISTORY` and `is_core` of `guppi/pages.py`, body links by `links_of` of `guppi/lint.py`, markers by `MARKER` of `guppi/pages.py`, and a case id by `ID` of `guppi/caseid.py`, and writes `SHIPPED` of `guppi/pages.py`; its own patterns are the parenthesis of case references and the mention of a session in prose, which no module of `guppi/` judges today.
> - [ ] `guppi/cli.py`: registers `ship`.
> - [ ] `tests/test_ship.py`: over a sample tree under a temporary folder, one test per line of the `then` of this Case, and one test that runs `guppi/lint.py` over a page that `guppi ship` wrote and asserts no `origin` finding.
> - [ ] `uv run guppi ship` over the working tree into a temporary folder: the files and lines it refuses go into the handoff, with the note that the leftovers of the pages come from the first CI run, which the owner starts by a tag `prod-*` on a commit of `plugin` after the push of the librarian's commit.
> - [ ] read `estimate-clean-branch-writes-a-clean-copy`

> **ratification:**
> ```
> - decision[case 804.6][create][rule-clean-branch]{tags:ci,git,plugin}
> - decision[case 804.6][create][estimate-clean-branch-writes-a-clean-copy]{ref:rule-clean-branch}{tags:ci,plugin}
> - decision[case 804.6][update][entity-guppi-repository]{ref:entity-guppi-repository}
> ```

### Case 804.7 — CI writes the clean version to prod

> **given:**
> `.github/workflows/prod.yml`: the new workflow that writes `prod`.
> **＋** `estimate-sprint-plugin-ci-writes-a-clean-branch`: its Criterion is replaced whole.
> **＋** `rule-clean-branch`: the rule of the clean version.
> **＋** `rule-github-repository`: the rulesets on `main` and `prod`, and who writes them.
> **＋** `.github/workflows/checks.yml`: the checks, which skip a push to `prod`.
> **＋** `entity-sprint-plugin`: the sprint page; the item of its milestone The clean branch links the rule and the Estimate.
> **＋** `vault/raw/2026-10-13/1753/cases/case-802.md`: Case 802 updates the same sprint page elsewhere.
> **＋** `PROD_DEPLOY_KEY`: the repository secret that holds the private half of the deploy key that writes `prod`.

> **when:**
> In a session of the sprint `plugin` before its close, the owner pushes a tag `prod-*`, such as `prod-1`, on a commit of the branch `plugin` to the repository of the project on GitHub, and the workflow `.github/workflows/prod.yml` runs on that commit.

> **then:**
> The run writes the clean version that `uv run guppi ship` builds to the branch `prod`, as one new commit on top of its last commit, or as its first commit when `prod` does not stand yet, whose message names the commit it was built from.
> **＋** The run pushes to `prod` with the deploy key whose private half is the secret `PROD_DEPLOY_KEY`, which the bypass list of the ruleset on `prod` lets through.
> **＋** `prod` holds each page with `core: true` and no other page.
> **＋** No text of the clean version holds a reference to a case or a decision, a link to a page that the clean version leaves out, or a mention of a session of this repository.
> **＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
> **＋** The `on:` block of `.github/workflows/prod.yml` starts the same run on a push to `main`.
> **－** A run whose `uv run guppi ship` exits 1 fails and writes nothing to `prod`.
> **－** A run whose clean version equals the last commit of `prod` adds no commit.

> **tasks:**
> - [ ] `.github/workflows/prod.yml`: runs on a push to `main` and on a push of a tag `prod-*`, with `contents: write`; runs `uv run guppi ship` into an empty folder; when it exits 0, commits that folder to `prod` on top of its last commit with a message that names the commit it was built from, adds no commit when nothing changed, and pushes over SSH with the private key of the secret `PROD_DEPLOY_KEY`, never with the token of the run; when it exits 1, fails and pushes nothing; its header comment names the deploy key in place of the GitHub Actions app.
> - [ ] update `rule-github-repository`
>   - set:
>     ```
>     purpose: "Prevents a pull request from reaching main unchecked, and an account other than the owner's from writing to main, or to prod, which only the owner and the workflow of rule-clean-branch write"
>     ```
>   - old: `` Prevents a pull request from reaching `main` unchecked, and an account other than the owner's from writing to `main` or `prod`. ``
>   - new: `` Prevents a pull request from reaching `main` unchecked, and an account other than the owner's from writing to `main`, or to `prod`, which only the owner and the workflow of [[rule-clean-branch]] write. ``
>   - old: `` Only the owner bypasses it, so a pull request into `prod` cannot be merged. The item The clean branch of [[entity-sprint-plugin]] adds the CI that writes `prod` to that bypass list. ``
>   - new: `` Only the owner and the deploy keys of the repository bypass it, so a pull request into `prod` cannot be merged, and besides the owner only the workflow `.github/workflows/prod.yml` of [[rule-clean-branch]] writes `prod`, with the one deploy key whose private half is the secret `PROD_DEPLOY_KEY` (case 804). ``
>   - old: `` Only the owner pushes, by hand when the owner wants, by `! git push`. ``
>   - new: `` Only the owner pushes, by hand when the owner wants, by `! git push`; the one other push is that of the workflow of [[rule-clean-branch]] to `prod` (case 804). ``
>   - change: `deploy keys on the bypass list of prod, and the workflow of rule-clean-branch writes prod with the key of the secret PROD_DEPLOY_KEY (case 804)`
> - [ ] update `entity-sprint-plugin`
>   - old: `- CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint`
>   - new: `- [[rule-clean-branch]], [[estimate-sprint-plugin-ci-writes-a-clean-branch]] — CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint`
>   - change: `the item of The clean branch links rule-clean-branch and the Estimate of the live run (case 804)`
> - [ ] `uv run guppi sprint`
> - [ ] stop: the owner makes an SSH key pair on the owner's machine, such as by `ssh-keygen -t ed25519 -N "" -C prod-deploy -f prod_deploy_key`, outside the repository.
> - [ ] stop: the owner adds the public half, `prod_deploy_key.pub`, as a deploy key of the repository on GitHub, with write access, under Settings, Deploy keys.
> - [ ] stop: the owner stores the private half, `prod_deploy_key`, as the repository secret `PROD_DEPLOY_KEY` under Settings, Secrets and variables, Actions, and then deletes both files from the machine.
> - [ ] stop: the owner adds `Deploy keys` to the bypass list of the ruleset `prod`, with the mode always, in the settings of the repository on GitHub.
> - [ ] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
>   - set:
>     ```
>     status: pending
>     method: "by hand, in a session of the sprint plugin before its close: the CI run that a tag prod-* on a commit of plugin starts, its push with the deploy key of the secret PROD_DEPLOY_KEY, the branch prod it wrote and the on: block of .github/workflows/prod.yml read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the run on a tag prod-* of plugin, the commit on top of prod, prod holds exactly the pages with core: true, the push with the deploy key of PROD_DEPLOY_KEY (case 804)`
> - [ ] read `estimate-sprint-plugin-ci-writes-a-clean-branch`

> **ratification:**
> ```
> - decision[case 804.7][update][rule-github-repository]{ref:rule-github-repository}
> - decision[case 804.7][update][estimate-sprint-plugin-ci-writes-a-clean-branch]{ref:entity-sprint-plugin}
> - decision[case 804.7][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> ```
