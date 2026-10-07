## Case 714 — Pre-spec reports a Case that breaks a condition of a schema

> **context:**
> The `schema.yaml` of a page category can make a field or a section required once another field holds a given value: an `actioned` Insight requires `addressed_by`, for example. Today only `make lint` of `guppi/lint.py` reads these conditions, by `check_schema`, on the live pages at the librarian's run. `judge` of `guppi/prespec.py`, which `/pre-spec`, the check of the Case file of `rule-case-check` and the check after ratification of `rule-spec-write` run, does not. So Case 701.1 set `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` `actioned` with no `addressed_by`, was ratified, and `make lint` then reported the missing field; Case 706 of the next session fixed that one field and left this check not done, and the handoff of session 0636 and the brief carry it. The person chose a check of every condition of every schema, inside `judge`, so that all three places run it; a finding only for the Case that causes the break; only the page and the Cases judged together, so the check of one Case file does not see a field another Case of the session sets; the same skip as the check of the keys for a category whose schema rule the session changes; and a new Estimate on `rule-prespec-hook`, checked by tests.
>
> The page as the Case leaves it counts a field that `guppi/generate.py` fills from the item itself, such as `parent` from `ref`, since `case-schema.md` says a Case does not write derivable fields. Case 712 of this session says that a Case writes `addressed_by` as the bare slug of a decision of its own session; the new check counts the field as present in any form, so the two agree. The Purpose of `rule-case-check` says the checks of a Case are those of pre-spec and of the Spec hook, imported, and `estimate-case-check-sends-back-a-faulty-case` says the check of the file runs `judge`; both stay true, so neither changes. The Purpose of `rule-prespec-hook` says the list of what `--check` compares stands in the docstring of `guppi/prespec.py`, which this Case extends, so the page stands. A Grep for `(?i)conditional` over `vault/wiki/estimates/` printed `schema.yaml`, `estimate-insights-schema-checked.md`, `estimate-estimates-schema-checked.md`, `estimate-rules-schema-checked.md`, `estimate-lessons-schema-checked.md`, `estimate-entities-schema-checked.md` and `estimate-lint-catches.md`. `schema.yaml` holds the conditions of an Estimate, which this Case reads and does not change; the Criterion of each of the six Estimates speaks of what `make lint` reports on a page, which does not change since lint calls the shared function, so each Criterion stands. The new code runs from the working tree at once and reads the `schema.yaml` files, which this Case does not change; a refused Case goes back to `case-guppi` and loses nothing, so no old form is kept.

> **problem:**
> A Case can break a condition of a schema, such as an `actioned` Insight with no `addressed_by`, and no check before ratification sends it back; `make lint` reports it only after the librarian's run.

> **recommend:**
> - **What should a check before ratification cover?**
>   - Recommended: (b) every such condition of every schema, on the page as the Case leaves it, through the code of `make lint`.
>   - Answer: agreed, (b).
> - **Where should the check run?**
>   - Recommended: (a) inside the shared function of `guppi/prespec.py`, so `/pre-spec`, the check of the Case file and the check after ratification all run it.
>   - Answer: agreed, (a).
> - **Which Case does the check send back?**
>   - Recommended: (a) only the Case that causes the break: a `create` that breaks a condition, or a `set` of the value that starts one with no required field or section on the page or in the Case.
>   - Answer: agreed, (a).
> - **Do the fields set by another Case of the same session count?**
>   - Recommended: (a) only the page and the Cases checked together.
>   - Answer: agreed, (a).
> - **What happens when the same session changes the schema itself?**
>   - Recommended: (a) skip that page type, as the key check does.
>   - Answer: agreed, (a).
> - **How is the check proven to work?**
>   - Recommended: (a) a new Estimate on `rule-prespec-hook`, checked by tests.
>   - Answer: agreed, (a).

> **given:**
> `guppi/prespec.py`: `judge`, the shared check of a plan, and its docstring.
> **＋** `guppi/lint.py`: `check_schema`, whose judgment of a condition becomes one shared function.
> **＋** `tests/test_prespec.py` and `tests/test_lint.py`: the tests of the check and of lint.
> **＋** `estimate-prespec-hook-reports-a-schema-condition-not-met`: the new check of the finding.
> **＋** `rule-prespec-hook`: the rule of `/pre-spec`, the target of the Estimate. Unchanged.
> **＋** `rule-case-check` and `rule-spec-write`: the checks of a Case file and after ratification, which run `judge`. Unchanged.
> **＋** `guppi/generate.py`: fills derivable fields, such as `parent` from `ref`. Unchanged.

> **when:**
> `judge` of `guppi/prespec.py` — run by `uv run guppi prespec --check <plan> --session <id>`, by the check of a Case file of `rule-case-check` or by the check after ratification of `rule-spec-write` — reads a `create` or an `update` item of the `then` blocks, and the page it names, by the `schema.yaml` of the category of its slug.

> **then:**
> A `create` that leaves its page without a field or section that a condition of the schema requires, or an `update` whose `set` gives the value a condition starts on while neither the page nor the Cases judged hold what it requires, gives one finding that names the Case, the slug, the missing field or section and the condition.
> **＋** The judgment of a condition is one function of `guppi/lint.py`, which `check_schema` and `guppi/prespec.py` both call, and `make lint` reports what it reported before.
> **＋** A field that `guppi/generate.py` fills from the item, such as `parent` from `ref`, counts as present, and so does a field or section that an earlier Case of the plan writes on the same page.
> **－** An `update` that sets no value a condition starts on gives no such finding, even when the page already breaks a condition.
> **－** A category whose schema rule a Case of the session changes is not judged, as for the check of the keys.
> **－** In the check of a Case file of `rule-case-check`, a field that only a Case of the session outside the file writes does not count.
> **－** A `defer` item is not judged.

> **tasks:**
> - [ ] create `estimate-prespec-hook-reports-a-schema-condition-not-met`
>   - ref: `rule-prespec-hook`
>   - kind: `QA`
>   - purpose: `Whether pre-spec reports a Case whose create or set leaves a page short of what a condition of its schema requires, by one function of guppi/lint.py, and leaves alone a Case that does not cause the break`
>   - method: `uv run pytest tests/test_prespec.py tests/test_lint.py -k condition`
>   - tags: `[harness, workflow, schema]`
> - [ ] `guppi/lint.py`: one function gives each condition of a schema that a set of fields and sections does not meet; `check_schema` calls it, and its findings stay as they are.
> - [ ] `guppi/prespec.py`: a check in `judge`, after the check of the keys and with its `schema_free`, builds for each `create` and `update` the page as the plan leaves it — the live page, the fields and sections of the items of earlier Cases and of the item, and the fields `generate` fills from the item — and calls the function of `guppi/lint.py` only for a `create`, or for an `update` whose `set` gives the value a condition starts on; a `defer` is not judged; the module docstring gains the finding in its list.
> - [ ] `tests/test_prespec.py` and `tests/test_lint.py`: a `create` of a rule with `enforcement: hook` and no `implementation_ref`, an `update` that sets an Insight `actioned` with no `addressed_by`, and an `update` that sets an Estimate `passed` with no `## Result` each give a finding; the same with the field or section in the item, on the page or in an earlier Case of the plan, a Leaf Entity whose `parent` comes from `ref`, an `update` with only `change` on a page that already breaks a condition, a category in `schema_free` and a `defer` give none; lint gives the same findings on a page as before.
> - [ ] read `estimate-prespec-hook-reports-a-schema-condition-not-met`

> **ratification:**
> ```
> - decision[case 714][create][estimate-prespec-hook-reports-a-schema-condition-not-met]{ref:rule-prespec-hook}{tags:harness,workflow,schema}
> ```
