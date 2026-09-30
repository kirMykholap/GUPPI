## Case 556 — The method of the Estimate schema promise runs the test of `method`

> **context:**
> `estimate-estimates-schema-checked` promises that lint checks every Estimate page against its schema. One line of its Criterion promises that a page without a `method` field gets the finding `schema: missing field method`. The page's `method` field is the command that checks the promise: `pytest tests/test_schemas.py -k estimates`. pytest matches `-k` against the test names. The shared tests that run once per category are labelled with the category name, so `estimates` selects them. The test of a page without `method` is `test_an_estimate_without_method_is_one_finding`. Its name holds `estimate` but not `estimates`, so the filter skips it. The reading of 2026-09-29, "4 passed, 1 skipped", fits the five shared tests alone. So the page stands `passed` on a run that never checked the line about `method`. The handoff of session 1736 recorded this gap, and case 548 noted it and left it for a later session. Case 548 fixed the same gap on `estimate-decisions-schema-checked` with the singular filter `-k decision`. This Case follows that fix. The new method runs `-k estimate`. By a read of `tests/test_schemas.py`, that filter selects the five shared tests for Estimate pages and the test of a page without `method`, and no other test. The method text also names a page without `method` among its steps. The new method keeps two of the forms that the Render of `rule-estimates-schema` asks of a `method`: the word `pytest`, and a path under `tests/` that exists. The page goes back to `pending`. Its Criterion is written back word for word, since only a replaced Criterion sets `pending`. `rule-ledger-write` refuses a reading of a promise that a decision line of the same session updates, so the reading with the new command waits for a later session. Until then, the cascade of `generate` sets `rule-estimates-schema` from `built` to `draft`, since its one Estimate no longer stands `passed`. A Grep of the repository outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` for `estimate-estimates-schema-checked` found `brief.md`, `log.md` and the `estimates` field of `rule-estimates-schema`. `brief.md` and `log.md` were not read for this, and the field only links the promise. So no other live text repeats the method. A Grep of `vault/wiki/estimates/` for methods that run `tests/test_schemas.py` found the six schema Estimates. The four for entities, lessons, insights and rules run `-k` with their category name. The file holds no test for those four categories beyond the shared ones, so their filters miss nothing. The docstring of `tests/test_schemas.py` names `estimate-<category>-schema-checked` in general terms, and it stays true. No reader of a text changes, so no old form needs to be kept. This Case creates no page, so no vault query ran.

> **problem:**
> The method of `estimate-estimates-schema-checked` selects the tests by a name that the test of a page without `method` does not contain. So the reading behind the page's `passed` never ran the test of one of its promises. The question is how the method selects that test, and whether the page waits for a new reading.

> **recommend:**
> - **How should the method select the test for a missing `method`?**
>   - Recommended: (a) the singular filter `-k estimate`, as the method of `estimate-decisions-schema-checked` uses, with the method text naming a page without `method`; no code change.
>   - Answer: (a). The person asked for a plain explanation first, and then agreed with the recommendation.
> - **Should the page go back to waiting for a new reading?**
>   - Recommended: (a) set the page `pending`, write its Criterion back word for word, and read it with the new command in a later session.
>   - Answer: (a). The person agreed with the recommendation after the explanation.

> **given:**
> `estimate-estimates-schema-checked` — the promise of the Estimate schema, whose method and status this Case sets
> **＋** `tests/test_schemas.py` — the tests of the page schemas on the live files, which the method selects by name
> **＋** `pytest tests/test_schemas.py -k estimate` — the command of the new method
> **＋** `make lint` — the live reading the method names
> **＋** `wiki/estimates/` — the folder of the Estimate pages that `make lint` reads
> **＋** `rule-estimates-schema` — the rule the promise belongs to, whose Render sets the forms of a `method`
> **＋** `rule-ledger-write` — the rule that holds a reading of a promise the session changes for a later session

> **when:**
> The reading of `estimate-estimates-schema-checked` follows its method.

> **then:**
> The method of `estimate-estimates-schema-checked` runs `pytest tests/test_schemas.py -k estimate`, which selects the tests for each category on an Estimate page and the test of an Estimate page without `method`.
> **＋** The method names a page in the shape, a page without `method`, then one defect at a time, and expects no schema finding on `wiki/estimates/` in `make lint`.
> **＋** `estimate-estimates-schema-checked` stands `pending` until a reading with the new method, and `rule-estimates-schema` stands `draft` until that reading passes.
> **－** The text of the Criterion of `estimate-estimates-schema-checked` does not change.
> **－** `tests/test_schemas.py` does not change.
> **－** The reading of `estimate-estimates-schema-checked` is not taken in this session, as `rule-ledger-write` requires.

> **tasks:**
> - [ ] update `estimate-estimates-schema-checked`
>   - set: `{status: pending, method: "pytest tests/test_schemas.py -k estimate on the live vault/wiki/estimates/schema.yaml — a page in the shape, a page without method, then one defect at a time; the live reading make lint, no schema finding on wiki/estimates/"}`
>   - sections.Criterion:
>     ````
>     When:
>     `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.
>
>     Then:
>     The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
>     **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
>     **＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
>     **＋** `fields` and `sections` describe each name of these lists; `description` holds, among its paragraphs, the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
>     **－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.
>     ````
>   - change: `the method runs -k estimate and names a page without method, so the test of method runs; the reading is due again, the Criterion stands (case 556)`
> - [ ] `uv run pytest tests/test_schemas.py -k estimate --collect-only -q`: the tests for each category on `estimates` and `test_an_estimate_without_method_is_one_finding` are listed, and no other test
> - [ ] read `estimate-estimates-schema-checked` — in a later session: `uv run pytest tests/test_schemas.py -k estimate`, then `make lint`

> **ratification:**
> ```
> - decision[case 556][update][estimate-estimates-schema-checked]{ref:estimate-estimates-schema-checked}
> ```
