## Case 516 — The check of the lift on a schema change names its tests

> **context:**
> Each Estimate carries a `method`: the command that checks its promise. The `method` of `estimate-materialize-lifts-unfiltered-on-a-schema-change` runs `uv run pytest tests/test_materialize.py -k schema_change`. The promise is about a session that changes a `rule-<category>-schema`: a `create` of that category keeps every key and gets no `unknown`. `-k` picks tests by a word in their names, and no test name holds `schema_change`. The command runs zero tests, and pytest does not fail on that. At the last reading (1134 ledger, L28: "-k schema_change selects 0 tests; the two tests of case 308.2 run by name ... 2 passed") the reader ran the two real tests by other words, but the `method` was never fixed. The `method` also says the test holds a "create rule-rules-schema", but the test `update`s it. The Criterion says the lift holds "wherever the schema entry stands in the Spec, before or after". The test puts the schema decision first in the ledger and its Case after the creates in the Spec. The other order passed only because the code was read: `schema_changed()` in `guppi/materialize.py` reads the whole ledger before the lift.
>
> In one round the person chose three things:
> - The `method` names each test by its full node id, so pytest stops with "not found" when a test is renamed or removed and never quietly runs nothing.
> - A third test covers the other order: the schema decision after the creates in the ledger, and its Case before them in the Spec.
> - Only this `method` changes. The other `method`s that pick tests with `-k` are not checked here.
>
> What the frame shows:
> - The Case sets only the `method` field. Under `rule-case-protocol` an `update` that names a part alone keeps the Criterion and the `passed` status, so there is no `set.status` and no reading line.
> - `vault/wiki/estimates/schema.yaml` asks for a `method` in one of four forms. The new text holds the word `pytest` and a `tests/` path. Lint's `TEST_PATH` in `guppi/lint.py` takes `tests/test_materialize.py` from before the `::`, and that file exists, so the check of `estimate-lint-checks-the-method` stays green.
> - `rule-materialize` and its paragraph on case 308.2 describe behaviour that does not change. No other Estimate of the rule has a Criterion that speaks of this `method` or these tests.
> - No hook changes, and no code reads the `method` to run it.
> - The Case creates no page, so no vault query was run.
>
> Not done: the other `-k` methods of the vault are not checked. Lint gets no check that a `-k` picks at least one test.

> **problem:**
> The command that checks this promise runs no test and still passes. So a reading that follows the `method` proves nothing, and one part of the Criterion, the other order, has no test at all.

> **recommend:**
> Name the three tests by their node ids in the `method`, add the test of the other order, and write "update" where the `method` says "create". A node id that misses stops pytest with an error, and a `-k` word that misses does not. The rejected option was a new `-k` word such as `-k "schema_rule or without_a_schema_line"`, which a later rename can empty again without any error.

> **given:**
> `estimate-materialize-lifts-unfiltered-on-a-schema-change` — the promise whose `method` changes.
> **＋** `tests/test_materialize.py` — the two tests the `method` names, and the new test of the other order.
> **＋** `rule-materialize` — the rule whose lift the tests check, left as it is.
> **＋** `vault/wiki/estimates/schema.yaml` — the forms a `method` may take.

> **when:**
> Someone runs the `method` of `estimate-materialize-lifts-unfiltered-on-a-schema-change`.

> **then:**
> pytest runs each test of `tests/test_materialize.py` that the `method` names by its node id, and runs no other test.
> **＋** A test runs a unit whose schema decision line stands after the `create` lines in the ledger, and whose schema Case stands before the creates in the Spec. That `create` is lifted whole: the key is in `fields`, and no key is `unknown`.
> **＋** When a test the `method` names is renamed or removed, pytest stops with a "not found" error and does not report a run of no tests.
> **－** The Criterion and the `passed` status of `estimate-materialize-lifts-unfiltered-on-a-schema-change` do not change.

> **tasks:**
> - [ ] update `estimate-materialize-lifts-unfiltered-on-a-schema-change`
>   - set: `{method: "uv run pytest tests/test_materialize.py::test_a_create_of_a_category_whose_schema_rule_the_unit_changes_is_lifted_whole tests/test_materialize.py::test_a_schema_line_after_the_create_still_lifts_it_whole tests/test_materialize.py::test_without_a_schema_line_the_lift_filters_as_before — a unit with update rule-rules-schema and create rule-x carrying a key the disk schema lacks, the key in fields and no unknown, with the schema line before and after the create; the same create without the schema entry, unknown as before"}`
>   - change: `the method names its tests by node id, -k schema_change selected none, and a test of the other order joins (case 516)`
> - [ ] `tests/test_materialize.py`: `test_a_schema_line_after_the_create_still_lifts_it_whole` — the schema decision line appended after the `create` lines of the ledger, the schema Case placed before the creates in the Spec; the `create` of `rule-x` lifted whole, the other category filtered as before
> - [ ] `uv run pytest tests/test_materialize.py::test_a_create_of_a_category_whose_schema_rule_the_unit_changes_is_lifted_whole tests/test_materialize.py::test_a_schema_line_after_the_create_still_lifts_it_whole tests/test_materialize.py::test_without_a_schema_line_the_lift_filters_as_before` — 3 passed
> - [ ] `make test`

> **ratification:**
> ```
> - decision[case 516][update][estimate-materialize-lifts-unfiltered-on-a-schema-change]{ref:rule-materialize}
> ```
