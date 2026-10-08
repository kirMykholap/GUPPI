## Case 738 — The pre-spec check of a MOC's method lands from its patch

> **context:**
> `/pre-spec` judges the `method` of each Estimate item of a plan by `names_a_form` of `guppi/lint.py`, so a MOC's Estimate whose `method` names a test file or `pytest` alone passes the plan and turns `make lint` red only at the librarian's run. Case 733 of session 0213 ratified the stricter check: on a MOC as the plan leaves it, a `method` that names neither a `make <target>` nor `by hand` is a finding, by one predicate `names_a_moc_form` that `check_method` of lint calls too. Its code turned `make test` red at that Retro, in `tests/test_case_schema.py::test_case_schema_the_example_passes_the_check`, since the example Case of `vault/wiki/case-example.md` gave the MOC `entity-cart` an Estimate with a `pytest` command alone. The code was saved to `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff` and reverted; the four code boxes of Case 733 stand unticked in the 0213 Spec, and `estimate-prespec-catches-a-method-without-a-form` stands `failed`. Case 735 of session 1547 changed the example, and `vault/wiki/case-example.md` now gives that Estimate `make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time`, in the example Case and in the `then` block example; `MAKE_TARGET` of `guppi/lint.py` matches it, so the patched check passes the example. The person chose that this Case lands the code already ratified, with one decision line, an `update` of `rule-prespec` that adds a History line only, and that the four boxes of the 0213 Spec stay as that session left them; this session's boxes and its handoff say where the code landed. `estimate-prespec-catches-a-method-without-a-form` checks the change: its Criterion, `purpose` and `method`, set by Case 733, already state the stricter check, so they stand and are not signed again; its reading at the Retro of this session runs `tests/test_prespec.py`. The `when` and `then` below are that Criterion word for word. `estimate-lint-checks-the-method` stands: the patch moves the test of the form out of `check_method` into `names_a_moc_form` and keeps each answer of `check_method`, which `tests/test_lint.py` shows. A Grep of `MOC` over `vault/wiki/estimates/` with the glob `estimate-prespec-*.md` printed `vault/wiki/estimates/estimate-prespec-catches-a-method-without-a-form.md` alone, so no other Estimate of `rule-prespec` speaks of a MOC's `method`. The Render of `rule-prespec` leaves what the check compares to the module docstring of `guppi/prespec.py`, which the patch rewrites, so no sentence of the page changes; this Case does not set its `status`. Case 739.1 of this session writes the same module docstring: it names the cascade notes under Notes, while the patch rewrites the item on the `method` of an Estimate item and the docstring of `check_form`, a function Case 739.1 does not touch. The two texts say different things and neither makes the other false; the patch lands first, and Case 739.1 adds its notes after it. `estimate-case-example-passes-the-check` speaks of the check this Case changes: the check gives the example of `vault/wiki/case-example.md` no finding and no note, and a change of the check that gives it one fails `tests/test_case_schema.py`. It already checks that the example still passes, so its Criterion stands; the box on `tests/test_case_schema.py` and the full `make test` of Work Mode run it, and it gets no read line, since this Case neither creates it nor sets it `pending`. The hunks of `guppi/prespec.py` in the patch name line numbers a few lines off the file today, and the lines around them stand as the patch holds them. The patch's `tests/test_prespec.py` holds one long line in `test_a_moc_is_judged_as_the_plan_leaves_it` that `make style` reformats. A Grep of `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_generate.py`, `tests/test_orchestration.py` and `tests/test_schemas.py`. Only `tests/test_case_schema.py` runs a live text through the changed code, the example through `guppi/casecheck.py`, which imports `guppi/prespec.py`; the other three read `schema.yaml` files or `vault/wiki/orchestration.md` and run no Estimate item through `check_form` or `check_method`.

> **problem:**
> The stricter check that Case 733 ratified is not in the code, so pre-spec still passes a MOC's Estimate whose `method` names a test file or `pytest` alone, and its Estimate stands `failed`.

> **recommend:**
> - **How does this session carry the code that is already ratified?**
>   - Recommended: (a) a Case that lands the code by the patch, `make style` and the full `make test`, with one `update` of `rule-prespec` that adds a History line, its `context` naming `estimate-prespec-catches-a-method-without-a-form` as the check, the Criterion unchanged, read at Retro.
>   - Answer: agreed, (a).
> - **What happens to the four unticked boxes in the earlier Spec?**
>   - Recommended: (a) they stay unticked; this session's boxes and its handoff record that the code landed here.
>   - Answer: agreed, (a).

> **given:**
> `rule-prespec`: the rule of pre-spec; a History line only.
> **＋** `guppi/prespec.py`: `check_form` judges the `method` of each Estimate item of the plan.
> **＋** `guppi/lint.py`: `names_a_form`, and `check_method`, whose test of the form of a MOC's `method` becomes `names_a_moc_form`.
> **＋** `tests/test_prespec.py`: the unit tests of the findings of `check_form`.
> **＋** `tests/test_lint.py`: the unit tests of `check_method`.
> **＋** `tests/test_case_schema.py`: the test of `estimate-case-example-passes-the-check`, which runs the check of the Case file over the example of `vault/wiki/case-example.md`.
> **＋** `estimate-prespec-catches-a-method-without-a-form`: the check of the change; its Criterion stands.
> **＋** `vault/raw/2026-10-08/2134/cases/case-739.md`: Case 739.1 writes the module docstring of `guppi/prespec.py` too, after this patch.

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
> - [ ] update `rule-prespec`
>   - change: `the code of case 733 lands from its patch: pre-spec judges the method of a MOC's Estimate by its form (case 738)`
> - [ ] `guppi/lint.py`: the `guppi/lint.py` part of the patch applied: `names_a_moc_form`, which `check_method` calls; the module docstring names it; `make style` passes.
> - [ ] `guppi/prespec.py`: the `guppi/prespec.py` part of the patch applied: `check_form` judges a MOC's `method` by `names_a_moc_form`, the kind read by `plan_kind` and the target of an `update` by `estimate_target`; the two docstrings say so; `make style` passes.
> - [ ] `tests/test_prespec.py`: the four tests of the patch added and formatted by `make style`.
> - [ ] `tests/test_lint.py`: runs green, the judgment of `check_method` unchanged.
> - [ ] `tests/test_case_schema.py`: runs green over the example of `vault/wiki/case-example.md` with the patched check.
> - [ ] read `estimate-prespec-catches-a-method-without-a-form`

> **ratification:**
> ```
> - decision[case 738][update][rule-prespec]{ref:rule-prespec}
> ```
