## Case 996 — The clean build is blocked only by a shipped page that was never built or has a failed check

> **context:**
> `guppi ship` builds the clean version of GUPPI, and the workflow `.github/workflows/prod.yml` writes it to the branch `prod` on a push of a tag `prod-x.y.z`. Today the build writes nothing while any rule or entity with `core: true` stands `draft`, by `is_draft_core` of `.guppi/guppi/pages.py`, which `drafts` of `.guppi/guppi/ship.py` and `check_status` of `.guppi/guppi/lint.py` import; I read the three functions whole. The cascade of `.guppi/guppi/generate.py`, read whole as `cascade`, sets a rule `draft` whenever one of its Estimates is not `passed`, and writes the History line `status: <before> → <after> · cascade`. So a page falls back to `draft` each time a Case adds or replaces one of its Estimates. The lint of the last run, as the brief reports it, flags eight such pages: `rule-ask`, `rule-case-build`, `rule-morph`, `rule-orchestration`, `rule-skill-approve-spec`, `rule-skill-hi`, `rule-spec-box` and `rule-synthesis`. Case 994 of this session sets `estimate-close-reports-the-run`, an Estimate of `rule-close`, back to `pending`, and Case 995 adds a waiting Estimate to `rule-prespec`; both pages carry `core: true`. A Grep of the History status lines of the eight pages showed lines `draft → built` on six of them and none on `rule-morph` and `rule-skill-approve-spec`. Most of the waiting Estimates wait for an event of a later session, so `prod` could stay empty through the sprint.
> The person chose that the build is blocked only by a page with `core: true` that stands `draft` and whose History holds no line that set it `built`, or by such a page with an Estimate `failed`; a page built before that only waits for the reading of a newer Estimate ships as it stands. Lint reports the same pages through the same function, `is_draft_core`, whose name the tests of `.guppi/tests/test_lint.py` and `.guppi/tests/test_ship.py` assert both sides import. The Criterion of `estimate-clean-branch-refuses-a-draft-core-page` is replaced whole (996.1). Taking `core: true` off the blocking pages was offered and not chosen: of the ten pages, seven render a harness file in full — `/hi`, `/pre-spec`, `orchestration.md`, the agent files of `case-guppi` and `ask-guppi`, `/box` and `/approve-spec` — and `governed` of `.guppi/guppi/ship.py`, read whole, refuses such a file when its page carries no `core`, so `prod` could not run a session.
> What this session does: Work Mode changes `is_draft_core` and its tests, the librarian applies the page updates, and the Retro reads `estimate-clean-branch-refuses-a-draft-core-page` by its tests. What stays: `prod` still waits for `rule-morph`, whose setup skill the next milestone builds, and for `rule-skill-approve-spec`, whose reading needs a trial in the Claude Code CLI; after both are built, the owner pushes `plugin` and a tag `prod-x.y.z`, and `estimate-sprint-plugin-ci-writes-a-clean-branch` is read on that run before the close of `plugin`, so the sprint item stays open after this Case.
> The search for code that already judges the History of a page: a Grep of `.guppi/guppi/` for `→` outside `generate.py` printed 14 files: `onward.py`, `prespec.py`, `event.py`, `sprint_close.py`, `casecheck.py`, `lint.py`, `pages.py`, `links.py`, `materialize.py`, `ratified.py`, `guard.py`, `archive.py`, `render.py` and `config.py`. I read the hits around their lines: they are arrows in docstrings and comments, print lines, the History writer of `sprint_close.py`, and a pattern of `casecheck.py` for the line numbers of a Read output; none reads a status line of a History. So the new judgment lives in `.guppi/guppi/pages.py` alone, and since the writer, the cascade of `generate`, formats the line in another module, a test runs the cascade and the judgment over one page, as `rule-one-judgment-one-implementation` sets it.
> A Grep of the live pages of `vault/wiki/` but `log.md` and `brief.md` for `core: true[^.\n]{0,60}draft|draft[^.\n]{0,60}core|is_draft_core` printed 17 files: `sprint.md`, `estimates/schema.yaml`, `case-schema.md`, `entity-sprint-plugin`, `estimate-rules-schema-checked`, `rule-estimates-schema`, `estimate-materialize-lifts-a-create-value-by-the-schema`, `estimate-lint-checks-the-statuses`, `rule-case-protocol`, `estimate-clean-branch-pages-hold-pointers-only-in-brackets`, `rule-clean-branch`, `estimate-clean-branch-code-holds-pointers-only-in-brackets`, `rule-lint`, `estimate-clean-branch-ships-neutral-texts`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, `estimate-clean-branch-refuses-a-draft-core-page` and `estimate-entities-schema-checked`. The hits that this change makes false enter the Case: three sentences of `rule-clean-branch`, one of `rule-lint`, the `purpose` and the Criterion of `estimate-lint-checks-the-statuses`, the milestone line of `entity-sprint-plugin` and one `－` line of the Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` (996.2). The third sentence of `rule-clean-branch`, that a draft page a new project can go without loses `core` until it is `built`, now speaks only of a page that blocks the build, since a page built before ships as it stands. `ask-guppi` found at `/pre-spec` that a page shipped as `draft` would fail lint in the project that installs it. `ships` of `.guppi/guppi/ship.py` writes only the `passed` Estimates of a page, and `shipped_page` keeps its `status` and cuts its `estimates` to those, so `check_status` of `.guppi/guppi/lint.py` gives `draft while every Estimate is passed` on such a page there, as on `rule-orchestration`, and the lint job of the shipped `.github/workflows/checks.yml` goes red. The person chose that the page stays `draft` and that lint, where `ship_stands` answers no, gives no such finding, as it already gives none from `is_draft_core` there. So the new sub-case 996.3 replaces the Criterion of `estimate-lint-checks-the-statuses`, the one that lists the findings lint gives and leaves out in a project that installed GUPPI, since `case-schema.md` sets one promise per sub-case and 996.1 replaces the Criterion of the build. 996.1 keeps its update of that Estimate, which sets only its `purpose`, and the line of lint on the pages that block the build moves from the `then` of 996.1 to the Criterion of 996.3, so no promise is signed twice. In that Criterion the line on `is_draft_core` names the new judgment, and the `－` line on a project that installed GUPPI adds the `draft` page with every Estimate `passed`; the other lines stand word for word. The check of this file noted that some lines of 996.3 share words with lines of 996.1 and 996.2. They stand. 996.1 sets what blocks the build. 996.3 sets which findings lint gives on those pages, and repeats the words of the judgment only to name it. The line of 996.2 on `prod` speaks of the pages a run writes, not of a finding. `estimate-clean-branch-ships-the-passed-estimates` stays true: the build still writes no Estimate that is `pending` or `failed`, and the field `estimates` of each page it writes still lists only the Estimates it writes; only the finding that lint gives over such a page changes. The rest stand. The sentences of `rule-case-protocol`, `case-schema.md`, `rule-estimates-schema` and `estimates/schema.yaml` say that an Estimate with `once: true` keeps no page with `core: true` in `draft`. The `－` lines of `estimate-clean-branch-code-holds-pointers-only-in-brackets` and `estimate-clean-branch-pages-hold-pointers-only-in-brackets` say that a draft page stops no `--check` and no `--allow-draft` run. The other hits are Result lines, History lines, sprint records or the word `core` beside a `draft` value of a schema. `.claude/` printed none. In `.guppi/tests/`, the existing `draft_core` tests build pages whose History holds only a `created` line, so they still block and pass. A Grep of `.guppi/tests/` for `draft while every Estimate` printed `test_lint.py` alone: `test_draft_with_every_estimate_passed_is_a_status_finding` runs with the module of `ship` as it stands, which the clean version does not hold, so a task sets it standing there by `ship_module`. The comment of `test_the_clean_version_holds_no_pyproject_and_no_lock_at_its_root` of `.guppi/tests/test_guppi_package.py` speaks of `ship.ship`, which reads no status, and stands. The glossary rows on `draft` and `built` stand.
> I read the blocks of `.guppi/links.md` for `rule-clean-branch`, `estimate-clean-branch-refuses-a-draft-core-page`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, `entity-sprint-plugin`, `rule-lint`, `estimate-lint-checks-the-statuses`, `.guppi/guppi/pages.py`, `.guppi/guppi/ship.py` and `.guppi/guppi/lint.py`. `estimate-sprint-plugin-installs-as-a-plugin` builds with `--allow-draft`, which prints the lines and writes all the same, so it stands. `rule-morph` stands; its text does not speak of the guard. `rule-github-repository` and `rule-plugin-install` do not speak of the status of a page. The new texts of `rule-lint`, which has `core: true`, and the new docstrings put each pointer to a Case in a bracket at the end of its sentence. I read `entity-sprint-plugin` whole. The pair on it changes the last clause of the item of the milestone The clean branch, and the rest of that sentence stays true: the owner still pushes `plugin` and a tag, and the run is still read by its Estimate. No other Case of this session writes into that page. The check of this file noted the lines of the old Criteria that are not carried. In 996.1 the lines on `ship`, `--allow-draft`, the workflow and `is_draft_core` stand rewritten, since each now names the pages that block the build, and the `When` gains the run of `guppi lint`. In 996.2 one `－` line now names a page that blocks the build in place of any draft page. The check also noted that some `then` lines of 996.2 share words with lines of 996.1. They stand: 996.1 sets what the build and lint judge, and 996.2 carries the whole Criterion of the CI run, whose lines on `prod` and on a failed run only point to that judgment. Each promise stands in one Criterion only. The Greps `lesson\[error\]` and `\{addresses:` over the ledger of session 2227 printed nothing.

> **problem:**
> A shipped page falls back to `draft` each time a Case adds a check to it, and the build writes nothing while any such page stands, so the tagged run may never write `prod` in this sprint.

> **recommend:**
> - **What lets the tagged run write `prod` while harness pages stand draft**
>   - Recommended: (c) block only on pages that were never finished.
>   - Answer: the person asked instead to take `core: true` off the blocking pages and leave a backlog entry to fix them and give it back.
> - **Which pages lose `core: true` so the tagged run can write `prod`**
>   - Recommended: (c) no page loses the mark; block only on pages that were never finished.
>   - Answer: (c); `prod` is not stripped.
> - **How the build tells a page that was never finished**
>   - Recommended: (a) by the History of the page.
>   - Answer: agreed, (a).
> - **Whether a failed check still blocks a page that was finished before**
>   - Recommended: (a) a failed check blocks.
>   - Answer: agreed, (a).
> - **What lint keeps reporting**
>   - Recommended: (a) lint reports only what blocks the build, by the one shared function.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) replace the promise of `estimate-clean-branch-refuses-a-draft-core-page`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, how the clean version shows a page that ships as `draft`, since lint there would report it `draft while every Estimate is passed`; the person took the recommended answer, that the page stays `draft` and lint where the command `ship` is missing gives no such finding. The findings of `/pre-spec` also asked to fix the sentence of `rule-clean-branch` on a draft page that loses `core`, to give the cascade test a `draft_core` name, and to correct what Case 994 does to `rule-close`.
>   - Taken: the new sub-case 996.3 replaces the Criterion of `estimate-lint-checks-the-statuses` and carries the task on `.guppi/guppi/lint.py` for that exemption; 996.1 adds it to the sentence of `rule-lint` and the `purpose` of that Estimate, rewords the sentence of `rule-clean-branch` to a page that blocks the build, names the cascade test, and `context` is corrected.

### Case 996.1 — The build and lint judge a shipped draft page by its History and its failed checks

> **given:**
> `rule-clean-branch`: the rule whose Purpose sets when `guppi ship` refuses to build.
> **＋** `estimate-clean-branch-refuses-a-draft-core-page`: its Criterion is replaced whole.
> **＋** `rule-lint`: the rule whose Purpose says which draft pages lint reports.
> **＋** `estimate-lint-checks-the-statuses`: its `purpose` names the pages lint reports; its Criterion is 996.3.
> **＋** `.guppi/guppi/pages.py`: holds `is_draft_core`, the one judgment.
> **＋** `.guppi/guppi/ship.py`: the build, whose `drafts` imports it.
> **＋** `.guppi/guppi/lint.py`: lint, whose `check_status` imports it.
> **＋** `.guppi/guppi/generate.py`: its cascade writes the History line that sets a page `built`.
> **＋** `.guppi/tests/test_ship.py`: the tests of the build.
> **＋** `.guppi/tests/test_lint.py`: the tests of lint, and the test that runs the cascade and the judgment together.
> **＋** `.github/workflows/prod.yml`: the workflow that writes `prod`.
> **＋** `rule-skill-merge-main`: a rule without `core`.
> **＋** `rule-skill-pr-review`: a rule without `core`.

> **when:**
> `uv run --project .guppi guppi ship <folder>` or `uv run --project .guppi guppi ship --review <folder>`, as `rule-clean-branch` sets it, builds the clean version into an empty folder, with or without the option `--allow-draft`, or `uv run --project .guppi guppi lint` runs where the module of the command `ship` stands.

> **then:**
> A rule or an entity with `core: true` that stands `draft` blocks the build when its `## History` holds no line that set its status to `built`, or when one of its Estimates stands `failed`.
> **＋** While a page that blocks the build stands, `guppi ship` prints one line for each such page, writes nothing and exits 1.
> **＋** A `draft` page with `core: true` whose History holds such a line and none of whose Estimates stands `failed` gets no line, and the build writes it as it stands.
> **＋** With `--allow-draft`, the build writes the clean version all the same and prints those lines, which set no exit code; `.github/workflows/prod.yml` never passes that option.
> **＋** The build and lint tell a page that blocks the build by `is_draft_core` of `.guppi/guppi/pages.py`, imported by both, and a test runs the cascade of `.guppi/guppi/generate.py` that sets a page `built` and asserts that the page, set `draft` again, then blocks nothing.
> **＋** `rule-skill-merge-main` and `rule-skill-pr-review` carry no `core`, so the clean version holds neither them nor the files they render.
> **－** `uv run --project .guppi guppi ship --check` does not judge the status of a page.

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old: `` While a rule or an entity with `core: true` stands `draft`, `guppi ship <folder>` prints one line for each such page, writes nothing and exits 1, so the workflow writes nothing to `prod`; with the option `--allow-draft` it writes ``
>   - new: `` A rule or an entity with `core: true` that stands `draft` blocks the build when its `## History` holds no line that set its status to `built`, or when one of its Estimates stands `failed`; one that was `built` before and only waits for the reading of a newer Estimate blocks nothing and is written as it stands (as set in case 996.1). While a page that blocks the build stands, `guppi ship <folder>` prints one line for each such page, writes nothing and exits 1, so the workflow writes nothing to `prod`; with the option `--allow-draft` it writes ``
>   - old: `` `guppi ship --check` does not judge the status of a page, and `guppi lint` reports each such page where the module of the command `ship` stands; both judge it by `is_draft_core` of `.guppi/guppi/pages.py`. A draft page that a new project can go without loses `core` until it is `built` (case 822). ``
>   - new: `` `guppi ship --check` does not judge the status of a page, and `guppi lint` reports each page that blocks the build where the module of the command `ship` stands, and no other `draft` page with `core: true`; both judge it by `is_draft_core` of `.guppi/guppi/pages.py`, and a test of `.guppi/tests/test_lint.py` runs the cascade of `generate` that sets a page `built` and the judgment over that page (as set in case 996.1). A page that blocks the build and that a new project can go without loses `core` until it is `built` (as set in cases 822 and 996.1). A page that the clean version holds as `draft` keeps that status there, and `guppi lint` of a project that installed GUPPI reports neither it nor its Estimates that the build leaves out (as set in case 996.1). ``
>   - change: `the build is blocked only by a draft page with core: true that was never built or has a failed Estimate; a page shipped as draft draws no lint finding in an installed project`
> - [ ] update `rule-lint`
>   - old: `` `guppi lint` also reports each rule or entity with `core: true` that is `draft`, since `guppi ship` builds no clean version while one stands; a project that installed GUPPI gets no such line (case 822). ``
>   - new: `` `guppi lint` also reports each rule or entity with `core: true` that is `draft` and whose History holds no line that set it `built`, or one of whose Estimates stands `failed`, since `guppi ship` builds no clean version while one stands; a project that installed GUPPI gets no such line (as set in cases 822 and 996.1). Where the module of the command `ship` is missing, lint also gives no finding on a `draft` rule or entity with every Estimate `passed`, since the clean version keeps the status of a page and writes only its `passed` Estimates (as set in case 996.1). ``
>   - change: `lint reports only the draft pages with core: true that block the clean build, and none shipped as draft in an installed project`
> - [ ] update `estimate-lint-checks-the-statuses`
>   - set:
>     ```
>     purpose: A status its Estimates do not support, a draft page with core true that blocks the clean build where the command ship stands, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, a one-time Estimate whose target is not a sprint page, and a placeholder are findings of lint, and a draft page with every Estimate passed is none where the command ship is missing
>     ```
>   - change: `the purpose names the draft pages with core: true that block the clean build, and the draft page that is no finding in an installed project`
> - [ ] update `estimate-clean-branch-refuses-a-draft-core-page`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether guppi ship writes nothing and exits 1 while a draft page with core: true stands that was never built or has a failed Estimate, writes as it stands one built before that only waits for a reading, writes the copy with --allow-draft, and lint judges by the same is_draft_core"
>     method: uv run --project .guppi pytest .guppi/tests/test_ship.py .guppi/tests/test_lint.py -k draft_core
>     ```
>   - change: `the Criterion replaced whole — only a draft page with core: true that was never built or has a failed Estimate blocks the build`
> - [ ] `.guppi/guppi/pages.py`: `is_draft_core` takes the pages by slug beside the page and accepts a rule or an entity with `core: true` that stands `draft` only when its `## History` holds no line that set its status to `built` or one of its Estimates stands `failed`; its docstring says so, each pointer in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/ship.py`: `drafts` passes the pages by slug to `is_draft_core`; the module docstring names the new judgment.
> - [ ] `.guppi/guppi/lint.py`: `check_status` passes `by_slug` to `is_draft_core`; the module docstring and that of `check_status` name the new judgment.
> - [ ] `.guppi/tests/test_ship.py`: tests whose names hold `draft_core` — a draft page with `core: true` whose History holds a line that set it `built` and whose Estimate is `pending` gets no line and is written, exit 0; the same page with a `failed` Estimate gets its line, writes nothing, exit 1.
> - [ ] `.guppi/tests/test_lint.py`: a test whose name holds `draft_core` that runs the cascade of `.guppi/guppi/generate.py` over a draft page with `core: true` whose Estimates all passed, sets the page `draft` again with a `pending` Estimate, and asserts that `is_draft_core` does not accept it.
> - [ ] read `estimate-clean-branch-refuses-a-draft-core-page`

> **ratification:**
> ```
> - decision[case 996.1][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 996.1][update][rule-lint]{ref:rule-lint}
> - decision[case 996.1][update][estimate-lint-checks-the-statuses]{ref:rule-lint}
> - decision[case 996.1][update][estimate-clean-branch-refuses-a-draft-core-page]{ref:rule-clean-branch}
> ```

### Case 996.2 — The sprint item and its check name the pages that block the build

> **given:**
> `entity-sprint-plugin`: the sprint page, whose milestone line names the pages that stop the run.
> **＋** `estimate-sprint-plugin-ci-writes-a-clean-branch`: its Criterion is replaced whole.
> **＋** `estimate-clean-branch-refuses-a-draft-core-page`: the check of the pages that block the build.
> **＋** `rule-clean-branch`: the rule of the clean version.
> **＋** `.github/workflows/prod.yml`: the workflow that writes `prod`.
> **＋** `.claude-plugin/plugin.json`: the manifest whose `version` the build sets.

> **when:**
> In a session of the sprint `plugin` before its close, the owner pushes a tag `prod-x.y.z`, such as `prod-0.2.0`, on a commit of the branch `plugin` to the repository of the project on GitHub, and the workflow `.github/workflows/prod.yml` runs on that commit.
> **＋** `uv run --project .guppi guppi ship <folder>` runs on a commit with no tag `prod-x.y.z` in its history.

> **then:**
> The run writes the clean version that `uv run --project .guppi guppi ship` builds to the branch `prod`, as one new commit on top of its last commit, or as its first commit when `prod` does not stand yet, whose message names the commit it was built from.
> **＋** The run pushes to `prod` with the deploy key whose private half is the secret `PROD_DEPLOY_KEY`, which the bypass list of the ruleset on `prod` lets through.
> **＋** `prod` holds each page with `core: true` and no other page.
> **＋** No text of the clean version holds a reference to a case or a decision, a link to a page that the clean version leaves out, or a mention of a session of this repository; a sample, as `rule-clean-branch` sets it, such as a string of a test, is no reference.
> **＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
> **＋** The `version` of `.claude-plugin/plugin.json` on `prod` is the number of the highest tag `prod-x.y.z` in the history of the commit it was built from, such as `0.2.0` for `prod-0.2.0`, and a tag of another form, such as `prod-2`, gives no version.
> **＋** The `on:` block of `.github/workflows/prod.yml` starts the same run on a push to `main`.
> **－** `uv run --project .guppi guppi ship <folder>` with no tag `prod-x.y.z` in that history exits 1 and writes nothing, and `uv run --project .guppi guppi ship --check` reads no tag.
> **－** A run whose `uv run --project .guppi guppi ship` exits 1 fails and writes nothing to `prod`, as it does while a page with `core: true` stands that blocks the build, which `estimate-clean-branch-refuses-a-draft-core-page` checks.
> **－** A run whose clean version equals the last commit of `prod` adds no commit.

> **tasks:**
> - [ ] update `entity-sprint-plugin`
>   - old: `` while a page with `core: true` stands `draft`, that run writes nothing to `prod` ``
>   - new: `` while a page with `core: true` that blocks the build stands — a `draft` one never `built`, or one with an Estimate `failed` — that run writes nothing to `prod` ``
>   - change: `the milestone The clean branch names the pages that block the build`
> - [ ] `uv run --project .guppi guppi sprint`
> - [ ] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a run fails while a page that blocks the build stands`
> - [ ] read `estimate-sprint-plugin-ci-writes-a-clean-branch`

> **ratification:**
> ```
> - decision[case 996.2][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> - decision[case 996.2][update][estimate-sprint-plugin-ci-writes-a-clean-branch]{ref:entity-sprint-plugin}
> ```

### Case 996.3 — Lint reports the draft pages that block the build, and none shipped as draft in an installed project

> **given:**
> `estimate-lint-checks-the-statuses`: its Criterion is replaced whole.
> **＋** `rule-lint`: the rule of lint.
> **＋** `vault/wiki/`: the live pages lint reads.
> **＋** `.guppi/guppi/lint.py`: lint, whose `check_status` gives the `status` findings.
> **＋** `.guppi/guppi/pages.py`: holds `ship_stands` and `is_draft_core`.
> **＋** `.guppi/guppi/ledger.py`: holds `is_sprint_page`.
> **＋** `entity-sprint-<id>`: a sprint page, the target a one-time Estimate needs.
> **＋** `/hi`: the skill that opens a session, one of the moments a `method` may wait for.
> **＋** `.guppi/tests/test_lint.py`: the tests of lint.

> **when:**
> `uv run --project .guppi guppi lint` reads the `status` of the live pages under `vault/wiki/`, and the `method`, the `target` and the `once` of each Estimate.

> **then:**
> `status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged for these two.
> **＋** `status`: where `ship_stands` of `.guppi/guppi/pages.py` finds the module of the command `ship`, each entity or rule that `is_draft_core` accepts — one with `core: true` that stands `draft` and whose `## History` holds no line that set it `built`, or one of whose Estimates stands `failed` — with Estimates or without, one finding each, and none on another `draft` page with `core: true`.
> **＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
> **＋** `status`: an Estimate with `once: true` whose `target` is not a sprint page `entity-sprint-<id>`, as `is_sprint_page` of `.guppi/guppi/ledger.py` judges it, one finding.
> **＋** `unread`: every Estimate `failed`, and every Estimate `pending` whose `method` does not wait for a later moment, one finding each, `unread: <status>`.
> **＋** A `method` waits for a later moment when a part of it between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon, or names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`.
> **＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.
> **－** `guppi lint` in a project that installed GUPPI, where `ship_stands` answers no, reports none of the pages that `is_draft_core` accepts, and no `draft` entity or rule with every Estimate `passed`, since the clean version keeps the `status` of a page and writes only its `passed` Estimates.
> **－** A `pending` Estimate whose `method` waits for a later moment earns no `unread` finding.
> **－** A `failed` Estimate earns its `unread` finding whatever its `method` says.
> **－** An Estimate with `once: true` whose target is a sprint page, and an Estimate without `once`, earn no finding of a one-time Estimate.

> **tasks:**
> - [ ] update `estimate-lint-checks-the-statuses`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — lint reports only the draft pages with core: true that block the clean build, and none shipped as draft in an installed project`
> - [ ] `.guppi/guppi/lint.py`: `check_status` gives the finding `draft while every Estimate is passed` only where `ship_stands` answers yes; the module docstring and that of `check_status` name the exemption, each pointer in a bracket at the end of its sentence.
> - [ ] `.guppi/tests/test_lint.py`: tests whose names hold `draft_core` — a draft page with `core: true` whose History holds a line that set it `built` and whose Estimate is `pending`, no finding; the same page with a `failed` Estimate, one finding; a `draft` rule with every Estimate `passed`, one finding where the module of `ship` stands and none where it is missing; and `test_draft_with_every_estimate_passed_is_a_status_finding` sets the module of `ship` as standing by `ship_module`, so it passes in the clean version, where that module is missing.
> - [ ] read `estimate-lint-checks-the-statuses`

> **ratification:**
> ```
> - decision[case 996.3][update][estimate-lint-checks-the-statuses]{ref:rule-lint}
> ```
