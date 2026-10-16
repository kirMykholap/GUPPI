## Case 867 — The check of the page schemas names its test files

> **context:**
> `estimate-page-schemas-one-file-per-rule` checks `rule-page-schemas`, a MOC over the six rules of the page formats. For the Estimate of a MOC, `check_method` of `.guppi/guppi/lint.py` passes a `make <target>` of the Makefile, or the word `pytest` with test files that each exist; `by hand` alone passes only when every counted Estimate of the children is a reading or a sibling Estimate names such a form. The `method` of this Estimate names `guppi check`, a test path without `pytest`, and a reading by hand after the librarian's first render. Five of the six child Estimates name `.guppi/tests/test_schemas.py` and no `by hand`, so lint gives a finding. The brief of the librarian of session 1712 reports it under `## Readings at the close`: "`estimate-page-schemas-one-file-per-rule` (says by hand while `estimate-entities-schema-checked` names a test file)", and the same run printed 11 lines of `guppi check` at exit 1. Case 829 deferred the Estimate for this finding. Case 861 superseded Case 829 but named only `estimate-guppi-tests-green`, so `guppi generate` kept `decision-case-829` in the `deferred_by` of this page, and the librarian's run of 1712 archived `decision-case-829`. `backlog.md` still lists the item.
>
> The rule that governs the choice is the `method` field of `rule-estimates-schema`. It says that the form of a MOC's Estimate is "a `make <target>` of the Makefile, or the word `pytest` with the test files of its pipeline, each of which must exist". The new `method` names `pytest` with four test files: `.guppi/tests/test_schemas.py` for the six children, `.guppi/tests/test_render.py` for two `full` pages on one file, `.guppi/tests/test_lint.py` for the findings of the classes `path` and `schema-description`, and `.guppi/tests/test_guard.py` for the refused hand edit. All four files exist. The `guppi check` part stays, and the reading by hand goes, since the reading after the first render passed on 2026-09-29. A `make` target was not chosen. `rule-rules-schema` brings a page with `core: true` into a new project with each of its Estimates "whose `method` names no target of the `Makefile`", and `rule-page-schemas` has `core: true`. `/pre-spec` judges the new `method` by `names_a_moc_form`, `tied_to_a_one_off_moment` and `waits_for_another_session` of `.guppi/guppi/lint.py`. It passes all three: it names `pytest` with test paths, holds no `by hand`, and names no later session, librarian or `/hi`. The Case adds no code, so no second copy of a judgment is written.
>
> The decision line carries `{supersedes:case 829}`. `decision` of `.guppi/guppi/generate.py` finds `decision-case-829` under `vault/archive/` by `find`, keeps it `archived`, adds this Case to its `superseded_by`, and `clear_deferred_by` drops it from the `deferred_by` of each target that a decision line of this Case names. This Case names only this page, so `estimate-guppi-tests-green`, which Case 861 already cleared, is not touched.
>
> Frontier item C2 asks whether a MOC with no parent may name `guppi test` alone. `rule-page-schemas` has the parent `rule-harness`, and the finding here comes from the branch of `check_method` for `by hand`, not from `names_a_moc_form`, so C2 does not reach this Case. The promise, `status` and Result of the Estimate do not change. `estimate-lint-checks-the-method` already checks the judgment of lint on this form: "For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it, and so does the word `pytest` with one or more test files, each of which exists." Its Criterion stands, because the Case changes no code of lint. A Grep for `estimate-page-schemas-one-file-per-rule` over the repository, with `vault/raw/` and `vault/archive/` left out, printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-page-schemas.md`. The brief and the log are records. `backlog.md` is written by `guppi backlog`. `rule-page-schemas` lists the slug only in `estimates`. A Grep for `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `.guppi/tests/` printed `test_case_schema.py`, `test_generate.py`, `test_schemas.py`, `test_orchestration.py` and `test_guppi_package.py`. None of them reads an Estimate page.

> **problem:**
> The `method` of `estimate-page-schemas-one-file-per-rule` has no form that lint accepts on the Estimate of a MOC. Its defer points at an archived Decision page, so the item stays in the backlog.

> **recommend:**
> - **What should the `method` of `estimate-page-schemas-one-file-per-rule` say?**
>   - Recommended: (a) `pytest` over the four test files that cover the promise, then `guppi check`.
>   - Answer: agreed, (a).
> - **How is the fix checked?**
>   - Recommended: (a) the existing check covers it: `estimate-lint-checks-the-method`, whose Criterion stands.
>   - Answer: agreed, (a).

> **given:**
> `estimate-page-schemas-one-file-per-rule`: the Estimate whose `method` changes.
> **＋** `rule-page-schemas`: the MOC it checks.
> **＋** `rule-estimates-schema`: the rule of the `method` of a MOC's Estimate.
> **＋** `.guppi/guppi/lint.py`: `check_method`, which judges the `method`.
> **＋** `.guppi/tests/test_schemas.py`, `.guppi/tests/test_render.py`, `.guppi/tests/test_lint.py` and `.guppi/tests/test_guard.py`: the test files the new `method` names.
> **＋** `decision-case-829`: the archived Decision page whose defer the Case retires.
> **＋** `vault/wiki/backlog.md`: the list of deferred items.

> **when:**
> `uv run --project .guppi guppi lint` reads the `method` of `estimate-page-schemas-one-file-per-rule`.
> **＋** `guppi backlog` writes `vault/wiki/backlog.md` after `guppi generate` applies the decision line of this Case.

> **then:**
> Lint gives no finding of the class `method` on `estimate-page-schemas-one-file-per-rule`.
> **＋** Its `method` names `pytest` with `.guppi/tests/test_schemas.py`, `.guppi/tests/test_render.py`, `.guppi/tests/test_lint.py` and `.guppi/tests/test_guard.py`, then `guppi check`.
> **＋** Its `deferred_by` no longer names `decision-case-829`, and `vault/wiki/backlog.md` does not list it.
> **－** Its `method` holds no reading by hand.
> **－** Its Criterion, `status` and Result do not change.

> **tasks:**
> - [ ] update `estimate-page-schemas-one-file-per-rule`
>   - set:
>     ```
>     method: "uv run --project .guppi pytest .guppi/tests/test_schemas.py .guppi/tests/test_render.py .guppi/tests/test_lint.py .guppi/tests/test_guard.py; uv run --project .guppi guppi check — render --check exit 0 and no path or schema-description finding on a <category>/schema"
>     ```
>   - change: `the method names pytest with the test files of the MOC; the reading by hand after the first render is gone`
> - [ ] `uv run --project .guppi pytest .guppi/tests/test_schemas.py .guppi/tests/test_render.py .guppi/tests/test_lint.py .guppi/tests/test_guard.py`: the four files of the new `method` pass.

> **ratification:**
> ```
> - decision[case 867][update][estimate-page-schemas-one-file-per-rule]{ref:rule-page-schemas}{supersedes:case 829}
> ```
