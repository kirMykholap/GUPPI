## Case 548 — The schema tests match the live Decision schema, and its promise names the tests it runs

> **context:**
> `tests/test_schemas.py` checks each page schema against its live file. One test, written for case 513.1, builds the smallest Decision page the schema accepts, removes `## Context`, and first asserts that the page still holds `## Problem` and `## History`. Case 544.8 made `## Problem` optional, and the librarian rewrote `vault/wiki/decisions/schema.yaml` from its rule page. Now the smallest accepted page holds `## History` alone, so the test fails on its setup before it checks for findings. The brief of session 1306 records the result: 1 failed, 964 passed, 2 skipped. The schema is right. The Criterion of `estimate-decisions-schema-checked` already says that a page without `## Context`, and a page without `## Problem`, get no finding.
> The same file holds three tests that skip themselves until the librarian rewrites a schema file: the test of `method` on an Estimate page (case 506.1), and the two Decision-page tests (cases 513.1 and 544.8). All three files have been rewritten, so the skips no longer happen. They would only hide a regression. A Grep of the repository outside `vault/raw/` and `vault/archive/` for the words of these skips finds them only in `tests/test_schemas.py`.
> The method line of `estimate-decisions-schema-checked` is out of date in two ways. It does not name a page without `## Problem`. Its lint reading also expects findings on the pages of Cases 1–28 for a missing `## Problem`, and the brief says those findings went away with the new schema file. The frame also shows that its command, `pytest tests/test_schemas.py -k decisions`, does not select the two Decision-page tests: pytest matches `-k` against the test names, and theirs contain `decision_page`, not `decisions`. The earlier reading, 4 passed and 1 skipped, fits the five tests that run once for each category. The new method runs `-k decision`, which selects those five tests and the two Decision-page tests. This keeps the person's choice that the method names both pages. The method of `estimate-estimates-schema-checked` has the same gap: `-k estimates` does not select the test of `method`. That promise is outside this Case, so it stays for a later session. A Grep of the repository outside `vault/raw/` and `vault/archive/` for `estimate-decisions-schema-checked` finds `brief.md`, `log.md`, the `estimates` field of `rule-decisions-schema`, and Decision pages, and no code. `brief.md` and `log.md` were not read for this, and the field of `rule-decisions-schema` only links the promise. So no other live text repeats the method.
> `rule-ledger-write` refuses a reading of a promise that a decision line of the same session updates. So the reading of `estimate-decisions-schema-checked`, on today's list of work, waits for a later session. The person chose this over reading the promise today under the old method. The update changes the `method` field alone. The Criterion and the `pending` status stay, and no Criterion is replaced. The Criterion of `estimate-estimates-schema-checked` stands: the test of `method` still checks the same behaviour, and it now runs every time. No reader of a text changes, so no old form needs to be kept. This Case creates no page, so no vault query ran.

> **problem:**
> A test of the Decision schema fails on its own setup after the schema made `## Problem` optional, although the schema and its promise are right. Three tests still skip on text that the schema files no longer hold. The method of the schema's promise names neither the page without `## Problem` nor a command that runs the Decision-page tests, and it expects lint findings that are gone.

> **recommend:**
> - **How should the out-of-date test be fixed?**
>   - Recommended: add `## Problem` to the page in the test, remove `## Context`, and expect no finding.
>   - Answer: agreed.
> - **Should the "skip until the file is rewritten" lines be removed?**
>   - Recommended: remove the skip from all three tests.
>   - Answer: agreed.
> - **Should the method line of the schema's promise be fixed too?**
>   - Recommended: rewrite the method line so that it names a page without `## Context` and a page without `## Problem`, and expects no schema finding on `wiki/decisions/`.
>   - Answer: agreed.
> - **Fix the method line now, or read the promise today?**
>   - Recommended: fix the method line now, and read the promise in a later session.
>   - Answer: fix the method line now; the reading waits for a later session.
> - **Change**
>   - Asked: correct the claim of `context` about the Grep for `estimate-decisions-schema-checked`, so that it states what the Grep printed.
>   - Taken: `context` names the hits `brief.md`, `log.md`, the `estimates` field of `rule-decisions-schema` and Decision pages, and says why none of them repeats the method.

> **given:**
> `tests/test_schemas.py` — the tests of the page schemas on the live files
> **＋** `uv run pytest tests/test_schemas.py` — the command that runs every test of the file
> **＋** `pytest tests/test_schemas.py -k decision` — the command of the method, which selects the tests of the Decision schema by name
> **＋** `vault/wiki/decisions/schema.yaml` — the live schema of a Decision page that the tests read
> **＋** `vault/wiki/estimates/schema.yaml` — the live schema of an Estimate page that the test of `method` reads
> **＋** `estimate-decisions-schema-checked` — the promise of the Decision schema, whose method this Case sets
> **＋** `rule-ledger-write` — the rule that holds a reading of a promise the session changes for a later session

> **when:**
> `uv run pytest tests/test_schemas.py` runs over the live schema files, and the reading of `estimate-decisions-schema-checked` follows its method.

> **then:**
> The test of a Decision page without `## Context` takes the page in the shape, adds `## Problem`, removes `## Context`, and finds no `schema` finding.
> **＋** The test of a Decision page without `## Problem` and the test of an Estimate page without `method` run on every call, and no test of `tests/test_schemas.py` skips on the text of a schema file.
> **＋** A schema file whose required lists go back to their older text makes these tests fail, not skip.
> **＋** `tests/test_schemas.py` passes on the live files of `vault/wiki/decisions/schema.yaml` and `vault/wiki/estimates/schema.yaml`.
> **＋** The method of `estimate-decisions-schema-checked` runs `pytest tests/test_schemas.py -k decision`, which selects the tests for each category and the two Decision-page tests, names a page without `## Context` and a page without `## Problem`, and expects no schema finding on `wiki/decisions/` in `make lint`.
> **－** The Criterion and the `pending` status of `estimate-decisions-schema-checked` do not change.
> **－** The reading of `estimate-decisions-schema-checked` is not taken in this session, as `rule-ledger-write` requires.

> **tasks:**
> - [ ] update `estimate-decisions-schema-checked`
>   - set: `{method: "pytest tests/test_schemas.py -k decision on the live vault/wiki/decisions/schema.yaml — a page in the shape, a page without ## Context, a page without ## Problem, then one defect at a time; the live reading make lint, no schema finding on wiki/decisions/"}`
>   - change: `the method runs -k decision, names a page without ## Problem, and expects no schema finding on wiki/decisions/ (case 548)`
> - [ ] `tests/test_schemas.py`: the test of a Decision page without `## Context` adds `## Problem` to the page in the shape itself; the skip on the text of the schema file and the words "Skipped until" of the docstring are removed from the tests of cases 506.1, 513.1 and 544.8
> - [ ] `uv run pytest tests/test_schemas.py`: every test passes, with no skip but the tests of a conditional on a category that has none

> **ratification:**
> ```
> - decision[case 548][update][estimate-decisions-schema-checked]{ref:estimate-decisions-schema-checked}
> ```
