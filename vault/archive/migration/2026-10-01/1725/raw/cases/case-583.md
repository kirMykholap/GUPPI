## Case 583 — A test for each section a schema requires only under a condition

> **context:**
> Lint checks every page against the `schema.yaml` of its category. A schema can require a section only under a condition: an Estimate page with `status: passed` or `status: failed` must have `## Result`, and a Rule page with `enforcement: render` must have `## Render`. `check_schema` in `guppi/lint.py` reports a page that breaks such a condition, for example `missing section ## Result (given {'status': 'passed'})`. No test covers that branch. `tests/test_schemas.py` tests only the first condition on a field, and it skips Estimate pages with "no conditional on a field". A Grep of `missing section|\(given` over `tests/` printed `test_schemas.py`, `test_prespec.py`, `test_lint.py`, `test_generate.py` and `test_casecheck.py`. Every hit about a condition names a missing field, and none names a missing section. A broken section branch in lint would leave every test green.
> The Criterion of `estimate-estimates-schema-checked` already promises one finding for a condition that is not met. Its Criterion stands, and it is the Estimate that checks this change. The `update` of this Case sets no `status` and writes no Criterion, so the scripts keep the whole Criterion of the page. Its method, `pytest tests/test_schemas.py -k estimate`, selects the new test through the `estimates` id of the parametrized test. The page is `pending`. Case 576 put off the question whether the skipped test leaves the `## Result` condition untested. That defer stands as the page `decision-case-576` and as a History line of the Estimate, `deferred · [[decision-case-576]]`. The Estimate has no `deferred_by` field, since its schema allows only `purpose` and `checked` as optional fields. This Case answers the deferred question, so its decision line carries `{supersedes:case 576}`, which supersedes the Decision page of case 576 and clears no field on the Estimate. The line names the Estimate by an `update` that changes only History. The ledger hook refuses a reading of an Estimate that a decision line of this session names (case 428.1), so the reading of this Estimate, Work line W26, waits for the next session. The Criterion of `estimate-rules-schema-checked` makes the same promise for Rule pages, and the new test runs under `-k rules` too. That Criterion stands, since the test adds a check of a promise it already makes and changes no promise. The page stays `passed` until its next reading.
> A Grep of `^(method|purpose):|test_schemas|skipped|conditional` over the pages `estimate-lint-catches`, `estimate-decisions-schema-checked`, `estimate-entities-schema-checked`, `estimate-insights-schema-checked` and `estimate-lessons-schema-checked` found no sentence that the new test makes false. Their methods name `-k <category>` and `make lint` and give no count of tests, and their Results are overwritten at the next reading. The module docstring of `tests/test_schemas.py` already names a condition that is not met. `guppi/lint.py` does not change. No `create` is made, so no vault query ran.

> **problem:**
> Lint enforces sections that a schema requires only under a condition, but no test checks it. The promise of `estimate-estimates-schema-checked` therefore rests on code that no test protects. The question is whether to write the test or to narrow the promise, and how far the test reaches.

> **recommend:**
> - **Write a test, or narrow the promise?**
>   - Recommended: (b) one test for every schema that has a section condition, written like the existing test for field conditions. It covers `## Result` on Estimate pages and `## Render` on Rule pages, and both Criteria stand.
>   - Answer: (b), one test for every schema that has a section condition.

> **given:**
> `tests/test_schemas.py` — gets the test of section conditions
> **＋** `pytest tests/test_schemas.py` — the command that runs it
> **＋** `vault/wiki/<category>/schema.yaml` — the live schemas the test reads
> **＋** `guppi/lint.py` — `check_schema`, the code under test, not changed
> **＋** `vault/wiki/estimates/schema.yaml` — the live schema with the `## Result` condition
> **＋** `vault/wiki/rules/schema.yaml` — the live schema with the `## Render` condition
> **＋** `estimate-estimates-schema-checked` — the Estimate that checks the change, named to answer the question case 576 put off

> **when:**
> `pytest tests/test_schemas.py` runs the test of section conditions once per category, over the live `vault/wiki/<category>/schema.yaml`.

> **then:**
> For each rule under `body.conditional` of the schema, a page in the shape that has the values of its `when` and lacks its required sections has one `schema` finding per missing section, `missing section <section> (given <when>)`, and no other finding.
> **＋** Under `-k estimate`, the test reads `vault/wiki/estimates/schema.yaml`: an Estimate page with `status: passed` and no `## Result` has one such finding, and an Estimate page with `status: failed` and no `## Result` has one.
> **＋** Under `-k rules`, the test reads `vault/wiki/rules/schema.yaml`: a Rule page with `enforcement: render` and no `## Render` has one such finding.
> **－** A schema with no `body.conditional` skips the test, with a reason that names the missing section condition.
> **－** `check_schema` in `guppi/lint.py` and every `vault/wiki/<category>/schema.yaml` stay as they are.

> **tasks:**
> - [ ] `tests/test_schemas.py`: a test parametrized over the categories that takes each rule of `body.conditional` of the live schema, gives a page in the shape the values of its `when`, removes its required sections and expects one `missing section <section> (given <when>)` finding each; it skips a schema with no `body.conditional`
> - [ ] `uv run pytest tests/test_schemas.py`: green, the new test passing under `-k estimate` and `-k rules`
> - [ ] update `estimate-estimates-schema-checked`
>   - change: `the test of a section required under a condition now covers ## Result on passed and failed; the Criterion stands, and the question case 576 put off is answered (case 583)`
> - [ ] read `estimate-estimates-schema-checked` — in the next session: `uv run pytest tests/test_schemas.py -k estimate` on the live schema, and the live reading `make lint`, no schema finding on `wiki/estimates/`

> **ratification:**
> ```
> - decision[case 583][update][estimate-estimates-schema-checked]{ref:rule-estimates-schema}{supersedes:case 576}
> ```
