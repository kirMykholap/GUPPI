## Case 652 — The test of the schema example fails when the page holds no example

> **context:**
> `tests/test_case_schema.py` reads the example Case from `vault/wiki/case-schema.md` and runs over it the check that the `SubagentStop` hook of `rule-case-check` runs over the file of a Case. Case 646 made the test skip, with a reason that names the file, while the page held no block tagged `case`, because the example reached the page only at the librarian's render. The render has put the example there, and at the `/hi` of this session the reading of `estimate-case-protocol-example-passes-the-check` passed with both tests run and none skipped. The skip still stands in the code. A skip leaves `make test` green, so a later render that lost the block or changed its tag would leave the example unchecked with no one told. The person chose that the test fails, with a message that names the file, when the page holds no block tagged `case`.
>
> The last `－` line of the Criterion of `estimate-case-protocol-example-passes-the-check` says the test skips, so this Case makes it false and replaces the Criterion whole: the same lines, with that line rewritten to say both tests fail and none is skipped. The page goes `pending`. The reading is taken at the `/hi` of a later session, since the ledger hook refuses a reading of an Estimate that a decision line of this session updates (case 428.1). Its `purpose` says nothing of the skip and stands. Its `method` reads "passed and not skipped", which stays true when no skip remains, so it stands. The test only goes red and loses nothing, so it keeps no old form. `estimate-guppi-tests-green` says that a skipped test is not a failure, and that line stands: after this Case the test fails rather than skips, which is the behaviour the person chose. Case 651 of this session gives `tests/test_orchestration.py` skips of the same kind. This Case does not touch them, and it does not change `rule-case-protocol` or the page.
>
> The search this Case rests on. A Grep of `test_case_schema|estimate-case-protocol-example-passes-the-check` over the repository root, with the glob `!**/decisions/** !**/raw/** !**/log.md !**/brief.md`, printed 3 files: `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/estimates/estimate-case-protocol-example-passes-the-check.md` and `tests/test_case_schema.py`. On `rule-case-protocol` the hits are the `estimates` field and a History line, which stand. The other two enter the Case.
>
> Not done:
> - The skips of `tests/test_orchestration.py` that Case 651 sets stay until a later Case removes them.

> **problem:**
> `tests/test_case_schema.py` still skips when `vault/wiki/case-schema.md` holds no example, though the example now stands there and its reading passed. A lost example would go unchecked while the tests stay green. The question was what the test does when the page holds no example.

> **recommend:**
> - **What the test does when the page holds no example**
>   - Recommended: (a) fail, with a message that names the file.
>   - Answer: agreed, (a).

> **given:**
> `tests/test_case_schema.py`: the test that runs the check over the example.
> **＋** `estimate-case-protocol-example-passes-the-check`: its Criterion is replaced whole.
> **＋** `vault/wiki/case-schema.md`: the page that holds the example, rendered from `rule-case-protocol`. Unchanged.
> **＋** `rule-case-protocol`: the rule whose Render is that page. Unchanged.
> **＋** `guppi/casecheck.py`: the check of the Cases of a file, which the test imports. Unchanged.
> **＋** `rule-case-check`: its `SubagentStop` hook runs that check over the file of a Case. Unchanged.

> **when:**
> `tests/test_case_schema.py` runs under `uv run pytest`. It reads the block tagged `case` in `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, and runs over it the function of `guppi/casecheck.py` that the `SubagentStop` hook of `rule-case-check` runs over the Cases of a file. It runs in a temporary project that holds the schema files of the vault and the pages the example updates.

> **then:**
> `vault/wiki/case-schema.md` holds, under its own heading after its `## Language` section, one block tagged `case`: one Case with sub-cases, in the chat form that `case-guppi` writes into its file.
> **＋** The example holds a `create` and an `update` with their sub-points, a `replace` pair whose values hold a backtick in spans padded by one space, a `set` in a fenced block, an `update` of an Estimate whose Criterion it replaces, a read line for each Estimate it creates or replaces, and its ledger lines in a quoted fence under `ratification`.
> **＋** The example's `context` says what the sentence around the match of its `replace` pair names.
> **＋** The paragraph before the block says that the example passes the check of the `SubagentStop` hook of `rule-case-check`, and that the check, not the paragraph, is the source of the limits; it lists no limit.
> **＋** The check gives the example no finding and no note, and the test passes.
> **＋** A change of the check that gives the example a finding or a note fails the test, which prints it.
> **＋** The test reads the example from `vault/wiki/case-schema.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/case-schema.md` holds no block tagged `case`, both tests of `tests/test_case_schema.py` fail with a message that names the file; no test of the file is skipped.
> **－** The Spec example and the limits that the prose of `vault/wiki/case-schema.md` already states stay as they are.

> **tasks:**
> - [ ] update `estimate-case-protocol-example-passes-the-check`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the test fails, not skips, when case-schema.md holds no block tagged case (case 652)`
> - [ ] `tests/test_case_schema.py`: `example` calls `pytest.fail` with a message that names the file, in place of `pytest.skip`, when the page holds no block tagged `case`; the module docstring says the test fails then and drops the sentence on the skip.
> - [ ] read `estimate-case-protocol-example-passes-the-check`, at the `/hi` of a later session

> **ratification:**
> ```
> - decision[case 652][update][estimate-case-protocol-example-passes-the-check]{ref:rule-case-protocol}
> ```
