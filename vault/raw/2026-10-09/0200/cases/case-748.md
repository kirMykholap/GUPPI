## Case 748 — A new page takes its type from its folder, and a missing required field is caught before the Spec

> **context:**
> `guppi materialize` lists, in `REQUIRED` of `guppi/materialize.py`, the fields that a `create` item must write for each category: `type`, `kind`, `purpose` and `tags` for a rule or an entity, `kind`, `purpose` and `method` for an Estimate, `pattern`, `children` and `tags` for an Insight. It marks a missing one `incomplete` only after ratification, and nothing before the Spec judges these fields: `judge` of `guppi/prespec.py` checks the keys an item may hold (`check_keys`) and the conditions of a schema (`check_conditions`, case 714), and `created_page` fills `type` from the category, so a missing `type` gives no finding there. In session 2352 the `create` items of `rule-skill-sprint-open` and `rule-skill-sprint-close` (Cases 743.6, 743.8) held no `type: rule`, `materialize` marked them `incomplete: [type]`, and the Retro read the mark as a page not built, while `guppi/generate.py` had written both pages with `type: rule` taken from the category (lesson `lesson-case-build-rule-create-without-type`, Case 746). The `type` of a page never needs a judgment: it follows from the slug prefix, and `_lift_item` already fills `type: estimate` for an Estimate.
>
> The person chose two parts. 748.1 has `materialize` fill `type` from the category for every `create`, as it does for an Estimate, so a missing `type` is no longer `incomplete`; a new Estimate checks it, and `estimate-materialize-assembles` stands, since a type taken from the slug prefix is derived like `category`, not invented. `estimate-materialize-lifts-a-create-by-the-schema` stands too: its Criterion lets only the fields of the category's `schema.yaml` reach `fields`, and `type` is a required field of each `schema.yaml` of the four categories. The map from a category to its type is `SINGULAR` of `guppi/generate.py`, which `generate` and `created_page` of `guppi/prespec.py` use, while `_lift_item` writes `type: estimate` as a literal of its own; `guppi/generate.py` imports `guppi/materialize.py`, so the map moves into `guppi/materialize.py`, and the lift, `generate` and `guppi/prespec.py` all read that one map (found by the pre-spec run of `ask-guppi`). 748.2 has `judge` give a finding for a `create` item that lacks any other required field, by one function of `guppi/materialize.py` that the lift and `guppi/prespec.py` both call; it is a finding, not a note, and a new Estimate checks it, while `estimate-prespec-hook-reports-a-schema-condition-not-met` stands, since an unmet condition and a missing plain field fail apart and are fixed in different code. `judge` runs in `/pre-spec`, in the check of a case file of `rule-case-check` and in the check after a write of `rule-spec-write`, so all three take the finding with no change to those rules. The tags of a `create` stand on its decision line as well as in its item, and the lift counts either, so the check counts either too. An Estimate with no `method` already gets a finding of `check_form` (case 331), so the new check gives no second one for it.
>
> The pages stand. `rule-materialize` says that what is missing is named and not invented, and a type taken from the slug prefix is neither. `rule-prespec-hook` points to the module docstring of `guppi/prespec.py` for what the check compares, and that docstring takes the new finding in Work Mode. `case-schema.md` says that a `create` holds the fields the target schema needs a judgment for, and `type` needs none. `vault/wiki/case-example.md` writes `type`, `kind`, `purpose` and `tags` for `entity-cart` and `kind`, `purpose` and `method` for its Estimate, so the test of `tests/test_case_schema.py` that runs the check over that live file finds nothing new. The Glob `vault/**/estimate-*{fills-the-type,required-field}*.md` printed nothing, so both new slugs are free.
>
> Not done: a put-off item with no `purpose` is still marked only after ratification, by the person's choice, and the `incomplete: [parent]` of a Leaf rule with no `ref` and no `parent` stays a mark of the lift alone. The lesson came from an earlier session, so no decision line carries `{addresses:...}`.

> **problem:**
> A `create` item can reach the ratified Spec without a field that `materialize` requires, since nothing before the Spec judges those fields. Among them, `type` is one that the page writer derives anyway, so its absence raises a false mark that a Retro read as a page not built.

> **recommend:**
> - **What the fix does about the type field**
>   - Recommended: (a) fill the type, check the rest: `materialize` fills `type` from the folder for every new page, and `/pre-spec` and the check of each case file report a new page whose item lacks any other required field, by one list the tool uses; two parts with a check each.
>   - Answer: agreed, (a).
> - **Whether a missing field stops the Case or only warns**
>   - Recommended: (a) a finding, which sends the case file back and keeps `/pre-spec` from passing, as for an unmet schema condition.
>   - Answer: agreed, (a).
> - **How the filled-in type is checked**
>   - Recommended: (a) a new check of its own on `rule-materialize`, read by a test in this session; `estimate-materialize-assembles` stays as it is.
>   - Answer: agreed, (a).
> - **How the new missing-field check is checked**
>   - Recommended: (a) a new check of its own on `rule-prespec-hook`, read by a test in this session; `estimate-prespec-hook-reports-a-schema-condition-not-met` stays as it is.
>   - Answer: agreed, (a).
> - **Whether a put-off item is checked too**
>   - Recommended: (a) new pages only; a put-off item with no `purpose` is still marked only after ratification.
>   - Answer: agreed, (a).

### Case 748.1 — `materialize` takes the type of a new page from its category

> **given:**
> `guppi/materialize.py`: the lift of a `create` item into its entry.
> **＋** `guppi/generate.py`: the page writer, which takes the type of a page from the same map.
> **＋** `guppi/prespec.py`: the check of a plan, whose `created_page` takes the type from the same map.
> **＋** `tests/test_materialize.py`: the tests of the lift.
> **＋** `rule-materialize`: the rule of the lift, which the new Estimate checks.
> **＋** `estimate-materialize-fills-the-type-from-the-category`: the new check of the filled type.

> **when:**
> `uv run guppi materialize` lifts a `create` item of a page of `rules`, `entities`, `estimates` or `insights` from the `then` block of its Case.

> **then:**
> When the item writes no `type`, the `fields` of the entry hold the `type` of its category: `rule`, `entity`, `estimate` or `insight`.
> **＋** The entry carries no `incomplete: [type]`.
> **＋** The type of each category is one map of `guppi/materialize.py`, which the lift, `guppi/generate.py` and `guppi/prespec.py` read.
> **＋** A missing `kind`, `purpose`, `tags`, `method`, `pattern` or `children` is still named under `incomplete`, as before.
> **－** A `type` that the item writes stands as written.
> **－** The `type` of a `defer` item is its own key and is not filled.

> **tasks:**
> - [ ] create `estimate-materialize-fills-the-type-from-the-category`
>   - ref: `rule-materialize`
>   - kind: `QA`
>   - purpose: `Whether materialize gives a create item with no type the type of its category, and marks no incomplete type`
>   - method: `uv run pytest tests/test_materialize.py -k type_from_the_category`
>   - tags: `[harness, workflow, ledger]`
> - [ ] `guppi/materialize.py`: `SINGULAR` moves here from `guppi/generate.py`; `_lift_item` fills `type` by it for every `create` item that writes none, in place of its literal `type: estimate`, and the module docstring says so.
> - [ ] `guppi/generate.py` and `guppi/prespec.py`: import `SINGULAR` from `guppi/materialize.py`; no second copy of the map stays.
> - [ ] `tests/test_materialize.py`: tests named `type_from_the_category` — a rule and an entity `create` with no `type` get it and no `incomplete: [type]`, a written `type` stands, a missing `purpose` is still `incomplete`.
> - [ ] read `estimate-materialize-fills-the-type-from-the-category`

> **ratification:**
> ```
> - decision[case 748.1][create][estimate-materialize-fills-the-type-from-the-category]{ref:rule-materialize}{tags:harness,workflow,ledger}
> ```

### Case 748.2 — Pre-spec reports a `create` item without a required field

> **given:**
> `guppi/prespec.py`: the judgment of a plan, `judge`.
> **＋** `guppi/materialize.py`: the module that holds the list of required fields and the judgment of what is missing.
> **＋** `tests/test_prespec.py`: the tests of the judgment.
> **＋** `rule-prespec-hook`: the rule of the check, which the new Estimate checks.
> **＋** `rule-case-check`: the check of a case file, which runs `judge`.
> **＋** `rule-spec-write`: the check after ratification, which runs `judge`.
> **＋** `estimate-prespec-hook-reports-a-create-without-a-required-field`: the new check of the finding.

> **when:**
> `judge` of `guppi/prespec.py` — run by `uv run guppi prespec --check <plan> --session <id>`, by the check of a case file of `rule-case-check` or by the check after ratification of `rule-spec-write` — reads a `create` item of a page of `rules`, `entities`, `estimates` or `insights` in the `then` blocks.

> **then:**
> A `create` item that lacks a field which `guppi materialize` would name under `incomplete` gives one finding that names the Case, the slug and the missing field.
> **＋** The list of required fields and the judgment of what is missing are one function of `guppi/materialize.py`, which the lift and `guppi/prespec.py` both call.
> **＋** A field counts as present when the item writes it as a key or under `sections`, and the tags count as present when the item or its decision line carries them.
> **－** The finding never names `type`, since the lift fills it from the category.
> **－** An Estimate with no `method` gives no second finding beside the one of the form of its method.
> **－** A `defer`, an `update` or a `delete` item gives no such finding.

> **tasks:**
> - [ ] create `estimate-prespec-hook-reports-a-create-without-a-required-field`
>   - ref: `rule-prespec-hook`
>   - kind: `QA`
>   - purpose: `Whether pre-spec reports a create item that lacks a field materialize requires, by one function of guppi/materialize.py, and gives none for a missing type`
>   - method: `uv run pytest tests/test_prespec.py tests/test_materialize.py -k required_field`
>   - tags: `[harness, workflow, schema]`
> - [ ] `guppi/materialize.py`: one function gives the required fields that a `create` item lacks, `type` filled first; `_lift_item` calls it.
> - [ ] `guppi/prespec.py`: `judge` reports each missing field by that function, the tags of the decision line counted, no second finding for a missing `method`; the module docstring lists the finding.
> - [ ] `tests/test_prespec.py`: tests named `required_field` — a rule `create` with no `purpose` or no `tags` gives a finding, one with no `type` gives none, tags on the decision line alone count, a `defer` with no `purpose` gives none, and the lift and the check answer alike over the same items.
> - [ ] read `estimate-prespec-hook-reports-a-create-without-a-required-field`

> **ratification:**
> ```
> - decision[case 748.2][create][estimate-prespec-hook-reports-a-create-without-a-required-field]{ref:rule-prespec-hook}{tags:harness,workflow,schema}
> ```
