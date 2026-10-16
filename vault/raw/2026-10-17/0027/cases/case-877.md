## Case 877 — A MOC with no parent may name guppi test

> **context:**
> Lint reads the `method` of each Estimate. On a MOC it accepts a `make <target>`, `pytest` with named test files, or a reading by hand, and it refuses a project command alone; `names_a_moc_form` of `.guppi/guppi/lint.py` makes that judgment, and `form_finding` inside `check_form` of `.guppi/guppi/prespec.py` calls the same function over the plan. The rule wants the Estimate of a MOC to run the tests of its own part. A MOC with no parent has no smaller part: `estimate-guppi-tests-green` on `entity-guppi` promises that the whole suite passes, lint refused it when it named `guppi test`, and Case 861 turned it into a reading by hand. The person doubted the rule on Case 861 (the handoff of session 1712), and Case 873 put the question off on `rule-estimates-schema`, which `backlog.md` lists. The person chose that a MOC with no `parent` may name `guppi test` alone, and that `guppi check` and `guppi style` alone stay findings on every MOC. The line of `rule-entities-schema` on `estimates` governs the choice: on a MOC they are cross-cutting checks that belong to all children and to none alone, which the whole suite is for a top MOC. The live MOCs with no `parent` are `entity-guppi`, `rule-harness` and `rule-session`.
>
> This Case takes up the defer of Case 873: the decision line of Case 877.1 that names `rule-estimates-schema` carries `{supersedes:case 873}`, and `decision-case-873` defers that page alone. The Render of `rule-estimates-schema` changes by one pair in the description of `method`, which makes `guppi test` on a MOC with no `parent` a form of its own in the list of the forms of a MOC; by case 378.5 an `update` of a Render touches no Estimate of the live reading, so the Criterion of `estimate-estimates-schema-checked`, which reads the lists and the required descriptions, stands. `estimate-guppi-tests-green` keeps its reading by hand, as the person chose: it still passes, and it names its moment.
>
> Code read. `check_method` of `.guppi/guppi/lint.py`, read whole: on a MOC it returns the finding when `names_a_moc_form` refuses, then judges a make target, then test files, then `sibling_names_a_target`, then the children's readings; a `guppi test` that passes the form would fall through to the children's check, so the task returns no finding before the Makefile, the test files and the children are read. `names_a_moc_form` takes the `method` alone, so it gains the answer whether the target has a `parent`. `plan_kind` of `.guppi/guppi/prespec.py` reads the `kind` of a page as the plan leaves it; no function there reads the `parent` that way, so Case 877.2 adds one beside it, and `props["parent"] = ref` in that module (the props of a `create`) shows that a `create` takes its `parent` from `ref`. A Grep of `get\("parent"\)` over `.guppi/guppi/` printed `.guppi/guppi/generate.py`, `.guppi/guppi/materialize.py` and `.guppi/guppi/glossary.py`. The hit of `generate.py` reads the parent of a decision record, and the hit of `materialize.py` judges whether a `create` of a Leaf rule names its place by `ref`, `parent` or `applies_to`: neither judges whether a page has a parent, and that hit shows that a `create` may write `parent` beside `ref`. `group_of` of `glossary.py` judges a page without a `parent` by an empty `parent` field, the same answer the new judgment gives on each input, a placeholder with no `parent` included; so the judgment moves into one predicate of `.guppi/guppi/pages.py`, which lint, pre-spec and `group_of` import, as `rule-one-judgment-one-implementation` sets it. The behaviour of `group_of` does not change: `estimate-glossary-renders-the-terms` already checks it, since its Criterion says that a page in `where` that has no `parent`, such as a root MOC or a placeholder not yet placed, is its own group, and its `method` runs `.guppi/tests/test_glossary.py`, which Work Mode runs with the suite; so its Criterion stands.
>
> Tests. In `.guppi/tests/test_lint.py` the MOC of `seed_moc_method`, `rule-root`, has no `parent`, and `test_a_moc_method_naming_pytest_a_path_or_a_command_alone_is_a_finding` asserts a finding for `guppi test` alone on it; in `.guppi/tests/test_prespec.py` the live MOC of `with_page` has no `parent`, and `test_a_moc_estimate_naming_a_test_file_pytest_or_a_command_alone_is_a_finding` asserts the same. Both would fail on the new code, so the tasks change them. `test_the_moc_form_is_one_predicate_lint_and_prespec_share` calls `names_a_moc_form` with the `method` alone, which keeps its answer. A Grep of `schema\.yaml` over `.guppi/tests/` printed `test_generate.py`, `test_ratified.py`, `test_case_schema.py`, `test_orchestration.py`, `test_prespec.py`, `test_materialize.py`, `test_lint.py`, `test_schemas.py`, `test_casecheck.py` and `test_ship.py`; those that read the live `vault/wiki/estimates/schema.yaml` (`test_schemas.py`, `test_generate.py`, `test_case_schema.py`, `test_orchestration.py`) read its lists, never the text of the description of `method`, which alone changes, so none goes red.
>
> Searches. A Grep of `test files of its pipeline|with test files|commands of the project alone|guppi test alone` over `vault/wiki/`, `.claude/` and `CLAUDE.md` printed `vault/wiki/log.md`, `vault/wiki/rules/rule-estimates-schema.md`, `vault/wiki/estimates/estimate-lint-checks-the-method.md`, `vault/wiki/estimates/estimate-prespec-catches-a-method-without-a-form.md` and `vault/wiki/estimates/schema.yaml`: the log is a record, the schema file is the Render, and the other three are changed here; the `method` and `purpose` of `estimate-prespec-catches-a-method-without-a-form` name `guppi test` alone on a MOC as a finding, so Case 877.2 sets both anew, while the `purpose` and `method` of `estimate-lint-checks-the-method` state no MOC form and stand. A Grep of `MOC` over `.claude/` printed `.claude/agents/librarian-guppi.md`, whose line lists MOC candidates in the brief and stands. A Grep of `names_a_moc_form|guppi test|MOC|lint-checks-the-method|prespec-catches|estimates-schema` over `vault/raw/2026-10-17/0027/cases/`, this file left out, printed only `vault/raw/2026-10-17/0027/cases/case-875.md`. Its finished file, read whole after its second build, changes one page that this Case names, `estimate-claude-md-rendered`, and the `then` line of Case 877.1 on it still holds. Case 875 sets a new `method` on `estimate-claude-md-rendered`, which Case 877.1 names in a `then` line: "by hand, after a render of CLAUDE.md: …", a reading by hand like the live one. The target `rule-claude-md` is a MOC with a `parent`, so `check_method` judges both the old and the new `method` by the rule for `by hand` that this Case keeps, with the same children counted, and the `then` line holds. Case 875 also updates the Purpose of `rule-harness`, a MOC with no `parent`, and of `rule-guppi-package`, and the `purpose` and `method` of `estimate-case-build-records-the-rounds-in-recommend` and `estimate-python-utf8-output-intact`. None of these texts states a form of the `method` of a MOC, and the new Purpose of `rule-harness` still says that one target of the `Makefile` runs the tests of each pipeline of a MOC, which this Case leaves true. Case 876 touches no page or file of this Case.
>
> The two Criteria are copied from the live ones. The lines that state the forms of a MOC are written anew on purpose: the line of `by hand` and the `－` line of the commands in `estimate-lint-checks-the-method`, and the line of the form of a MOC and the line of the one predicate in `estimate-prespec-catches-a-method-without-a-form`. Several `then` lines of Cases 877.1 and 877.2 share most of their words. That is the same judgment, read from lint and from pre-spec, which use one predicate; each sub-case is checked by its own test file.

> **problem:**
> Lint and pre-spec refuse `guppi test` alone on the Estimate of a MOC with no parent, whose own check is the whole suite, and the question of Case 873 stays open in the backlog.

> **recommend:**
> - **May the Estimate of a MOC name `guppi test` alone?**
>   - Recommended: (a) only a MOC with no parent.
>   - Answer: agreed, (a).
> - **Which project commands may a top MOC name alone?**
>   - Recommended: (a) `guppi test` only.
>   - Answer: agreed, (a).
> - **Does `estimate-guppi-tests-green` go back to `guppi test` alone?**
>   - Recommended: (a) keep it as it is.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) replace the Criterion of both Estimates, one sub-case each.
>   - Answer: agreed, (a).

### Case 877.1 — Lint passes guppi test on a MOC with no parent

> **given:**
> `estimate-lint-checks-the-method`: its Criterion is replaced whole.
> **＋** `rule-estimates-schema`: the forms of a `method`, rendered into `vault/wiki/estimates/schema.yaml`.
> **＋** `.guppi/guppi/lint.py`: `names_a_moc_form` and `check_method` judge the `method`.
> **＋** `.guppi/guppi/pages.py`: the one predicate of a page with no `parent`.
> **＋** `.guppi/guppi/glossary.py`: `group_of` imports that predicate.
> **＋** `.guppi/tests/test_lint.py`: the tests of the forms of a MOC.
> **＋** `estimate-claude-md-rendered`: an Estimate that gets no `method` finding.
> **＋** `Makefile`: the targets a `make <target>` names.

> **when:**
> `uv run --project .guppi guppi lint` reads the `method` field of each live Estimate.

> **then:**
> For an Estimate of a Leaf, a test file that exists, the word `pytest`, a `make <target>` of the `Makefile`, one of the commands `guppi test`, `guppi check` and `guppi style`, or `by hand` passes; else the finding "method: names no test file, pytest, guppi command or make target and is not a reading".
> **＋** A named test file that does not exist, or a `make <target>` that the `Makefile` does not hold, is a finding.
> **＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it, and so does the word `pytest` with one or more test files, each of which exists.
> **＋** For an Estimate of a MOC with no `parent`, the command `guppi test` passes whatever stands beside it.
> **＋** For an Estimate of a MOC, `by hand` without any of these passes when every counted Estimate of the children is a reading or a sibling Estimate names a `make <target>` or `pytest` with test files; else a finding.
> **＋** On a MOC with `render_mode: full`, the Estimates of a child with `enforcement: render` are not counted.
> **＋** `estimate-claude-md-rendered` gets no `method` finding.
> **－** On a MOC, the word `pytest` with no test file, a test file with no `pytest`, and a command `guppi check` or `guppi style` alone are each a finding.
> **－** On a MOC with a `parent`, the command `guppi test` alone is a finding.
> **－** On a MOC with `render_mode: full`, the Estimates of a child without `enforcement: render` are counted.
> **－** On a MOC without `render_mode: full`, the Estimates of every child are counted, a child with `enforcement: render` included.
> **－** A `## Method` section is not read as the `method` of a page.

> **tasks:**
> - [ ] update `rule-estimates-schema`
>   - old: `` On the Estimate of a MOC the form is a `make <target>` of the Makefile, or the word `pytest` with the test files of its pipeline, each of which must exist — there `pytest` without a test file, a path without `pytest`, or one of the commands of the project alone earns a finding, ``
>   - new: `` On the Estimate of a MOC the form is a `make <target>` of the Makefile, the word `pytest` with the test files of its pipeline, each of which must exist, or, on a MOC with no `parent`, the command `guppi test`, which passes there whatever stands beside it, since the whole suite of the project is the check that belongs to all its parts and to none alone — there `pytest` without a test file, a path without `pytest`, `guppi check` or `guppi style` alone, and `guppi test` alone on a MOC with a `parent` each earn a finding, ``
>   - change: `the Estimate of a MOC with no parent may name guppi test alone; the defer of case 873 retired`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] update `estimate-lint-checks-the-method`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — on a MOC with no parent, guppi test passes`
> - [ ] `.guppi/guppi/pages.py`: a predicate `has_no_parent(props)`, true when the `parent` field is empty; `group_of` of `.guppi/guppi/glossary.py` imports it in place of its own test of `parent`.
> - [ ] `.guppi/guppi/lint.py`: a pattern `GUPPI_TEST` for the command `guppi test` beside `GUPPI_COMMAND`; `names_a_moc_form(method, top=False)` passes `guppi test` when `top`; `check_method` passes `top` by `has_no_parent` of the target and returns no finding for `guppi test` on a MOC with no `parent` before the Makefile, the test files and the children are read; the module docstring and the docstrings of `names_a_moc_form` and `check_method` say so.
> - [ ] `.guppi/tests/test_lint.py`: `test_a_moc_method_naming_pytest_a_path_or_a_command_alone_is_a_finding` asserts the finding for `guppi test` alone on a MOC with a `parent`, written so that lint finds nothing else on it, and for `guppi check` and `guppi style` alone on `rule-root`; a new test asserts that `guppi test` alone on `rule-root`, which has no `parent` and whose child carries a tested Estimate, gets no finding.
> - [ ] read `estimate-lint-checks-the-method`

> **ratification:**
> ```
> - decision[case 877.1][update][rule-estimates-schema]{ref:rule-estimates-schema}{supersedes:case 873}
> - decision[case 877.1][update][estimate-lint-checks-the-method]{ref:rule-lint}
> ```

### Case 877.2 — Pre-spec passes guppi test on a MOC with no parent

> **given:**
> `estimate-prespec-catches-a-method-without-a-form`: its Criterion, `purpose` and `method` are set anew.
> **＋** `.guppi/guppi/prespec.py`: `check_form` judges the `method` of an Estimate in the plan.
> **＋** `.guppi/guppi/lint.py`: `names_a_form` and `names_a_moc_form`, the predicates pre-spec shares.
> **＋** `.guppi/guppi/pages.py`: the one predicate of a page with no `parent`.
> **＋** `.guppi/tests/test_prespec.py`: the tests of the forms of a MOC in the plan.
> **＋** `/pre-spec`: the skill that runs this check over the plan.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks before the Spec is approved.

> **then:**
> A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the forms lint classifies (a `make <target>`, the word `pytest`, a test path, one of the commands `guppi test`, `guppi check` and `guppi style`, or the words `by hand`) gives one line `case N: <create|update> <slug>: method names no form`, which goes on to name those forms.
> **＋** A `create` of an Estimate with no `method` at all gives the same finding.
> **＋** When the target of the Estimate is a MOC as the plan leaves it — the live page, or a `create` or an `update` of the plan that writes `kind: MOC` — a `method` that names neither a `make <target>`, nor the word `pytest` with a test path, nor `by hand`, nor, on a MOC with no `parent`, the command `guppi test`, gives one line `case N: <create|update> <slug>: method of a MOC's Estimate names no make target or test files and is not a reading`, in place of the line of no form.
> **＋** Whether the MOC has a `parent` is read as the plan leaves it: the `parent` that the `set` of an `update` of the plan gives, or the `parent` or the `ref` of a `create` of the plan that writes the page, else the `parent` of the live page.
> **＋** The predicate is one, lifted out of `.guppi/guppi/lint.py`; `/pre-spec` writes no second one.
> **＋** The form of a MOC's `method` is one predicate too, in `.guppi/guppi/lint.py`, which `check_method` of `guppi lint` calls as well, and whether a page has no `parent` is one predicate of `.guppi/guppi/pages.py`, which lint calls as well.
> **－** On a MOC with a `parent`, `guppi test` alone gives the line of a MOC's `method`, and on every MOC so does `guppi check` or `guppi style` alone.
> **－** Existence is not checked in the plan: the test file is written in Work Mode, and lint checks it later.
> **－** Whether the `Makefile` holds the `make <target>` that a MOC's `method` names is left to lint.
> **－** Whether every counted Estimate of the MOC's children is a reading, or a sibling Estimate names a form of a MOC, is left to lint.
> **－** An `update` of an Estimate that writes no `method` gives no line of the form of a MOC's `method`.

> **tasks:**
> - [ ] update `estimate-prespec-catches-a-method-without-a-form`
>   - set:
>     ```
>     status: pending
>     purpose: Whether pre-spec refuses an Estimate whose method names none of the forms lint classifies, or, on a MOC, neither a make target, nor pytest with a test path, nor by hand, nor guppi test on a MOC with no parent
>     method: uv run --project .guppi pytest .guppi/tests/test_prespec.py on a temp plan — a create with a prose method, a create with no method, each of the five forms clean, and on a MOC a test path alone, pytest alone, guppi check alone and guppi test alone with a parent as findings, a make target, pytest with a test path, by hand and guppi test alone with no parent clean
>     ```
>   - change: `the Criterion replaced whole — on a MOC with no parent, guppi test is a form`
> - [ ] `.guppi/guppi/prespec.py`: `plan_parent(blocks, slug, project_dir)` beside `plan_kind` — as `plan_kind` reads `kind`, the `parent` that the `set` of the last `update` of the plan gives, or the `parent`, else the `ref`, of the last `create` of the plan that writes the page, else the `parent` of the live page; `form_finding` passes `top` by `has_no_parent` of `.guppi/guppi/pages.py` to `names_a_moc_form`; the module docstring and the docstring of `check_form` say so.
> - [ ] `.guppi/tests/test_prespec.py`: `test_a_moc_estimate_naming_a_test_file_pytest_or_a_command_alone_is_a_finding` moves `guppi test` alone on the live MOC with no `parent` to the clean list and asserts the line for `guppi check` alone; a new test asserts the line for `guppi test` alone on a live MOC with a `parent` and on a MOC that a `create` of the plan writes with a `ref`; `test_the_moc_form_is_one_predicate_lint_and_prespec_share` asserts that `names_a_moc_form` with `top` passes `guppi test` and refuses `guppi check`, and that lint, pre-spec and `group_of` of `.guppi/guppi/glossary.py` use the one `has_no_parent` of `.guppi/guppi/pages.py`.
> - [ ] read `estimate-prespec-catches-a-method-without-a-form`

> **ratification:**
> ```
> - decision[case 877.2][update][estimate-prespec-catches-a-method-without-a-form]{ref:rule-prespec}
> ```
