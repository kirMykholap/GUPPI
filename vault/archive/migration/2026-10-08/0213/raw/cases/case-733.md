## Case 733 — Pre-spec judges the method of a MOC's Estimate by its form

> **context:**
> `/pre-spec` judges the `method` of each Estimate item of a plan by `names_a_form` of `guppi/lint.py`: a `make <target>`, the word `pytest`, a path under `tests/` or the words `by hand`. `make lint` is stricter for an Estimate of a MOC: `check_method` passes there only a `make <target>`, or `by hand` when the children's counted Estimates are readings or a sibling names a target. The check of the Case file runs `prespec.judge`, and so `check_form`, over the Case `case-guppi` writes, so it applies the same test. A MOC's Estimate whose `method` names a test file or `pytest` alone therefore passes both checks in Plan Mode and turns lint red only at the librarian's run. That happened to `estimate-hi-writes-frontier`, whose `method` named the person's answer and `tests/test_prespec.py` without `by hand`; Case 731 fixed that one method and left the gap, and the handoff of session 0050 names it for the next session. The person chose to have pre-spec judge the form alone: on a MOC, a `method` that names neither a `make <target>` nor `by hand` is a finding. The Makefile and the children stay with lint. A page counts as a MOC as the plan leaves it: the live page, or a `create` or an `update` of the plan that writes `kind: MOC`. The test of that form is one predicate in `guppi/lint.py`, which `check_method` calls too, as `CLAUDE.md` sets for one judgment in two places. The check of the Case file calls the same `judge`, so it takes the change with no edit of its own, but in a narrower scope: `judge` builds the blocks `check_form` reads only from the text it is given, and there that text is the Cases of the one file. That check therefore sees a MOC on the live page or in an item of the same file. A MOC that another Case of the session creates, or sets to `kind: MOC`, is seen only by `guppi prespec --check` over the whole plan. The Criterion speaks of `guppi prespec --check` alone, so it makes no claim on that scope. The Criterion of `estimate-case-check-sends-back-a-faulty-case` says that the check of the Case file runs `judge` of `guppi/prespec.py` over the Cases of the file. It stands: this Case changes what `check_form` inside `judge` finds, not how that check calls `judge` or what it stores. The Criterion of `estimate-prespec-catches-a-method-without-a-form` says the MOC branch stays with lint, so this Case replaces it whole: it carries the other lines word for word, drops that line alone, and sets its `purpose` and `method` anew to cover the MOC branch. `estimate-lint-checks-the-method` stands: lint judges each `method` as before, and `tests/test_lint.py` shows that the predicate lifted out of `check_method` leaves its judgment unchanged. A Grep of `branch of a MOC|MOC stays with lint|MOC branch` over the repository, `vault/raw/` and `vault/archive/` left out, printed `guppi/prespec.py` and `vault/wiki/estimates/estimate-prespec-catches-a-method-without-a-form.md`. The first is the docstring of `check_form`, which Work Mode rewrites, and the second is the Criterion this Case replaces. A Grep of `estimate-prespec-catches-a-method-without-a-form` over the same paths printed `vault/wiki/log.md` and `vault/wiki/rules/rule-prespec.md`. The `rule-prespec` hits are its `estimates` list and a History line, which stand. The Render of `rule-prespec` leaves what the check compares to the module docstring of `guppi/prespec.py`, so the page does not change.

> **problem:**
> Pre-spec and the check of the Case file pass a MOC's Estimate whose `method` names a test file or `pytest` alone, which `make lint` reports only at the librarian's run.

> **recommend:**
> - **How much of the MOC test does pre-spec take over?**
>   - Recommended: (a) the form only: on a MOC, a `method` that names neither a `make` target nor `by hand` is a finding; the Makefile and the children stay with lint; one shared function in `guppi/lint.py`.
>   - Answer: agreed, (a).
> - **Which pages count as a MOC when pre-spec judges?**
>   - Recommended: (a) as the plan leaves the page: the live page, a `create` or an `update` of the plan that writes `kind: MOC`.
>   - Answer: agreed, (a).
> - **How is the promise recorded?**
>   - Recommended: (a) replace the Criterion of `estimate-prespec-catches-a-method-without-a-form`, its `purpose` and `method` set anew.
>   - Answer: agreed, (a).

> **given:**
> `estimate-prespec-catches-a-method-without-a-form`: the check of the form of a `method` in the plan; its Criterion, `purpose` and `method` are set anew.
> **＋** `rule-prespec`: the rule the Estimate checks.
> **＋** `guppi/prespec.py`: `check_form` judges the `method` of each Estimate item of the plan.
> **＋** `guppi/lint.py`: `names_a_form`, and `check_method`, whose test of the form of a MOC's `method` becomes one shared predicate.
> **＋** `tests/test_prespec.py`: the unit tests of the findings of `check_form`.
> **＋** `tests/test_lint.py`: the unit tests of `check_method`.
> **＋** `estimate-lint-checks-the-method`: the check of the judgment of `check_method`; its Criterion stands.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks before the Spec is approved.

> **then:**
> A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the forms lint classifies (a `make <target>`, the word `pytest`, a path under `tests/`, or the words `by hand`) gives one line `case N: <create|update> <slug>: method names no form`, which goes on to name those forms.
> **＋** A `create` of an Estimate with no `method` at all gives the same finding.
> **＋** When the target of the Estimate is a MOC as the plan leaves it — the live page, or a `create` or an `update` of the plan that writes `kind: MOC` — a `method` that names neither a `make <target>` nor `by hand` gives one line `case N: <create|update> <slug>: method of a MOC's Estimate names no make target and is not a reading`, in place of the line of no form.
> **＋** The predicate is one, lifted out of `guppi/lint.py`; `pre-spec` writes no second one.
> **＋** The form of a MOC's `method` is one predicate too, in `guppi/lint.py`, which `check_method` of `make lint` calls as well.
> **－** Existence is not checked in the plan: the file under `tests/` is written in Work Mode and lint checks it later.
> **－** Whether the `Makefile` holds the `make <target>` a MOC's `method` names is left to lint.
> **－** Whether every counted Estimate of the MOC's children is a reading, or a sibling Estimate names a `make <target>`, is left to lint.
> **－** An `update` of an Estimate that writes no `method` gives no line of the form of a MOC's `method`.

> **tasks:**
> - [ ] update `estimate-prespec-catches-a-method-without-a-form`
>   - set:
>     ```
>     status: pending
>     purpose: Whether pre-spec refuses an Estimate whose method names none of the forms lint classifies, or, on a MOC, neither a make target nor by hand
>     method: uv run pytest tests/test_prespec.py on a temp plan — a create with a prose method, a create with no method, each of the four forms clean, and on a MOC a tests/ path alone and pytest alone as findings, a make target and by hand clean
>     ```
>   - change: `the Criterion replaced whole — pre-spec judges the method of a MOC's Estimate by its form (case 733)`
> - [ ] `guppi/lint.py`: the test of the form of a MOC's `method` — a `make <target>` or `by hand` — is lifted out of `check_method` into one predicate, which `check_method` calls; the module docstring names it.
> - [ ] `guppi/prespec.py`: `check_form` reads the kind of the target as the plan leaves it and judges a MOC's `method` by that predicate; the module docstring and the docstring of `check_form` say so, in place of the words that the branch of a MOC stays with lint.
> - [ ] `tests/test_prespec.py`: a MOC target, live, created and set by an `update`, with a `tests/` path alone and `pytest` alone as findings, a `make <target>` and `by hand` clean, and an `update` with no `method` clean.
> - [ ] `tests/test_lint.py`: runs green, the judgment of `check_method` unchanged.
> - [ ] read `estimate-prespec-catches-a-method-without-a-form`

> **ratification:**
> ```
> - decision[case 733][update][estimate-prespec-catches-a-method-without-a-form]{ref:rule-prespec}
> ```
