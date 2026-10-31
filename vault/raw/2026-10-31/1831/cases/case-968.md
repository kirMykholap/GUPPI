## Case 968 — A value of a new page that is not text reaches the page as its value

> **context:**
> When a Case creates a page, each field of the new page is a sub-point of its `create` line, one code span or a fenced block. `put` of `.guppi/guppi/ratified.py`, read whole with `code_value`, `fenced_value` and `read_tasks`, loads a value as YAML only under `set` or when it opens with `[` or `{`, so every other value reaches the Spec as text. `core` written as `true` therefore reaches the Spec as the text "true", and `create_fields` and `_lift_item` of `.guppi/guppi/materialize.py`, read whole, copy it onto the page unchanged; `core_as_left` of `.guppi/guppi/prespec.py`, read whole, answers false for it, since it asks `is True`, and `check_schema` of `.guppi/guppi/lint.py`, read whole, reports it only after the page stands. Session 0431 met this in Case 956.1, which wrote `core` as a fenced `true`, and Case 965 set `core` again by an `update` with `set`; the lesson `lesson-spec-write-lifts-a-create-value-as-a-string` records it, and also that `case-schema.md` gives no form for such a value. The defect is live in this session: Case 967.1 and Case 967.3 create `entity-link-graph` and `rule-link-graph-at-session-start` with `core` written as `true`, so by `put` their `then` blocks hold it as text. The schemas of `vault/wiki/rules/`, `vault/wiki/entities/` and `vault/wiki/estimates/` give `core` the one allowed value `true`; on disk today it is the only field whose allowed values hold no text. Case 969.1 adds to the schema of Estimates, at the render, the field `once` with the one allowed value `true`, and the same reading takes it then; its lint finding asks whether `once` is `True`, which is the value this reading gives. The person chose one function in `materialize.py` that loads a value as YAML for a field whose allowed values in the schema on disk hold no text, which the hook, the lift and `/pre-spec` import; so the two pages of Case 967 come right at the librarian's run, which runs after the code of this session changes, and Case 967 needs no change. A value that reads as none of the allowed values is refused by the hook, and the check of the Case file, which builds the Spec section by `case_section` and `read_tasks` of `ratified.py`, reports it at the build. The allowed values are read from the schema on disk also in a session that changes the schema rule of the category. A Grep `"values"` over `.guppi/guppi/` printed `lint.py` alone: `check_schema` already judges whether a value is one of the allowed values, by `str(value) in [str(a) for a in allowed]`, so that comparison moves into `materialize.py` and both sides import it; with it a value `1` is refused as lint refuses it, though Python takes `1 in [True]` as true. The PyYAML documentation (https://pyyaml.org/wiki/PyYAMLDocumentation) shows `true`, `false`, `on` and `off` loading as booleans. `case-schema.md` gains the form in the sentence of the `## Language` section of `rule-case-protocol` that opens with "The Spec keeps its form", read whole: it names how the hook of `rule-spec-write` reads the chat form of `tasks` — a task line that is an item, its sub-points its keys, the fields of a `create` among them, each value one code span or a fenced block — then the task line `tag`, and ends with a Case off this form not written; the pair adds after the fenced block how a value that is not text is read, and nothing else of the sentence changes. Case 969.1 also writes into that page, a sentence on a one-time Estimate after the one that ends "up to the session that closes it (case 772.4)." in `## The then block lives in the Spec`; the two pairs touch other sentences in other sections, and their new texts do not contradict each other. That `update` of a Render touches no Estimate of the live reading. `estimate-spec-write-copies-the-ratified-case` promises that each value is one code span or a fenced block, which stands, and `estimate-materialize-lifts-a-create-by-the-schema` promises which keys reach the page, which stands; neither speaks of the type of a value, so a new Estimate on `rule-materialize` checks the change. A Grep `core` over `vault/wiki/case-example.md` printed nothing, so `.guppi/tests/test_case_schema.py`, which runs the check of a Case file over that live example with the live schemas, stands; `.guppi/tests/test_schemas.py` reads the live schemas through `check_schema`, whose comparison moves unchanged, and stands. `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`, `passed`, on `rule-prespec-hook`, judges the new text of an item for a page that carries `core: true` "as the plan leaves it", and of an Estimate whose target does so, by `core_as_left` and `core_target` of `prespec.py`, read whole; its Criterion stands, since with this change a `create` that writes `core` as `true` is a page that carries `core: true` as the plan leaves it, which is what its words already promise, and the test of the new Estimate runs `core_as_left` over that value. This session's `/pre-spec` runs on the code as it stands before Work Mode, so it reads the `create` items of `entity-link-graph` and `rule-link-graph-at-session-start` as not core and does not judge their new texts, or those of their Estimates, for a pointer outside a bracket; that gap is a note for the handoff by `rule-retro`, and it closes for later sessions with this change. The finished file of Case 967, read whole after its build again ended, still creates both pages with `core` written as `true` and sets it by no `update`, so the claims on it hold. The lesson stands in the ledger of session 0431, and the ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> A field of a new page whose allowed value is not text, such as `core: true`, reaches the Spec and the page as text, so the page is born without that value, and `case-schema.md` gives no form that avoids it.

> **recommend:**
> - **Where the boolean of a `create` is fixed**
>   - Recommended: (c) one shared function, which the copy hook, the librarian's lift and `/pre-spec` import, loads a value as YAML for a field whose allowed values in the schema hold no text.
>   - Answer: (c), as recommended.
> - **What happens to a value outside the allowed list**
>   - Recommended: (a) the hook refuses it with a line that names the field and its allowed values.
>   - Answer: (a), as recommended.
> - **When the session also changes a page schema**
>   - Recommended: (a) the allowed values are still read from the schema on disk.
>   - Answer: (a), as recommended.
> - **Whether `case-schema.md` describes the form**
>   - Recommended: (a) one sentence in the Render of `rule-case-protocol`.
>   - Answer: (a), as recommended.
> - **How the change is checked**
>   - Recommended: (a) a new Estimate on `rule-materialize`.
>   - Answer: (a), as recommended.

> **given:**
> `.guppi/guppi/materialize.py`: the shared reading of a value and the lift of a `create`.
> **＋** `.guppi/guppi/ratified.py`: `put` and `read_tasks`, the reading of the `Stop` hook and of the check of a Case file.
> **＋** `/pre-spec`, by `core_as_left` of `.guppi/guppi/prespec.py`, and `check_schema` of `.guppi/guppi/lint.py`: the other readers of the value.
> **＋** `vault/wiki/<category>/schema.yaml`: the allowed values of each field.
> **＋** `rule-case-protocol`: its Render, `vault/wiki/case-schema.md`, gains the form of such a value.
> **＋** `estimate-materialize-lifts-a-create-value-by-the-schema`: the new check, on `rule-materialize`.
> **＋** `.guppi/tests/test_materialize.py`: the test of the readers over the same input.
> **＋** `rule-one-judgment-one-implementation`: one judgment lives in one function.

> **when:**
> The `Stop` hook or the check of a Case file reads a sub-point of a `create` item by `read_tasks` of `.guppi/guppi/ratified.py`.
> **＋** `uv run --project .guppi guppi materialize` lifts a `create` item from the `then` block of the Spec.
> **＋** `/pre-spec` judges by `core_as_left` of `.guppi/guppi/prespec.py` whether the page of a `create` carries `core: true`.

> **then:**
> A value of a field whose allowed values in `vault/wiki/<category>/schema.yaml` on disk hold no text, written as one code span or a fenced block, is loaded as YAML, so `true` reaches the `then` block, the page and `core_as_left` as the boolean true.
> **＋** The three readers load the value by one function of `.guppi/guppi/materialize.py`, and whether a value is one of the allowed values is one function of that module, which `check_schema` of `.guppi/guppi/lint.py` imports.
> **＋** A value that loads as none of the allowed values is refused by the hook: exit 2 with `` `<key>`: <value> is not one of <allowed values> `` on stderr, and nothing of the Case is written; the check of a Case file reports the same line as a finding.
> **＋** The allowed values are read from the schema on disk also when the session creates or updates the schema rule of that category.
> **－** A value of a field whose allowed values hold text, or for which the schema names no allowed values, stays text as before.
> **－** `uv run --project .guppi guppi materialize` and `core_as_left` refuse nothing: a value outside the list that reaches them stays as it loads, and `check_schema` reports it on the page.

> **tasks:**
> - [ ] `.guppi/guppi/materialize.py`: a function that gives the `values` of a category's `schema.yaml` on disk, read also for a category whose schema rule the unit changes; a function that judges whether a value is one of the allowed values, the comparison of `check_schema` moved; and a function that loads a text value as YAML for a field whose allowed values hold no text and gives the value and the refusal line when it is none of them; `_lift_item` lifts each field of a `create` through it.
> - [ ] `.guppi/guppi/ratified.py`: `put` reads each field of a `create` through that function, with the values of the item's category beside the keys of `key_judge`, returns its refusal, and the docstring of the module says so.
> - [ ] `.guppi/guppi/prespec.py`: `core_as_left` reads the `core` of a `create` through that function.
> - [ ] `.guppi/guppi/lint.py`: `check_schema` imports the function that judges whether a value is one of the allowed values.
> - [ ] `.guppi/tests/test_materialize.py`: one test that runs `read_tasks`, the lift and `core_as_left` over `core` written as a code span `true`, as a fenced `true` and as a value outside the list, and asserts that they read alike; and a test of each line of the Criterion.
> - [ ] update `rule-case-protocol`
>   - old: `its opening fence longer than any fence of the same character inside it (case 444.3);`
>   - new: ``` its opening fence longer than any fence of the same character inside it (case 444.3); a field whose allowed values in the schema of its category hold no text, such as `core`, takes its YAML value as one code span or a fenced block, such as `true`, and the hook, the lift of `materialize` and `/pre-spec` read it as that value, a value that is none of the allowed values refused (as set in case 968); ```
>   - change: `the form of a field of a create whose allowed values are not text`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
> - [ ] create `estimate-materialize-lifts-a-create-value-by-the-schema`
>   - ref: `rule-materialize`
>   - kind: `QA`
>   - purpose: `Whether a field of a create whose allowed values in the schema hold no text, such as core, reaches the then block, the page and pre-spec as its value by one function, and whether a value outside the list is refused by the hook`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_materialize.py, which runs the hook's reading, the lift and core_as_left over the same values; by hand, after the first librarian's run that creates a page whose create writes core as true: the core field of that page and the output of uv run --project .guppi guppi lint, read against the Criterion, the result in the estimate line`
>   - tags: `[harness, schema]`
> - [ ] read `estimate-materialize-lifts-a-create-value-by-the-schema`

> **ratification:**
> ```
> - decision[case 968][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 968][create][estimate-materialize-lifts-a-create-value-by-the-schema]{ref:rule-materialize}{tags:harness,schema}
> ```
