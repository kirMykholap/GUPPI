## Case 661 — The tests of the orchestration examples fail when the page holds no example

> **context:**
> `tests/test_orchestration.py` reads two examples from `vault/wiki/orchestration.md`, the block tagged `showing` and the block tagged `defer`, and runs over each the check that the scripts run over a real reply: the `Stop` check of `rule-case-check` over a showing, and the `Stop` hook of `rule-spec-write` over a short-form defer. Case 651 made the tests skip, with a reason that names the file, while the page held no such block, because the examples reached the page only at the librarian's render. The render has put both examples there, and at the `/hi` of this session the readings of `estimate-orchestration-showing-example-passes-the-check` and `estimate-orchestration-defer-example-passes-the-hook` both passed, with none skipped. The skip still stands in the code. A skip leaves `make test` green, so a later render that lost a block or changed its tag would leave that example unchecked with no one told. The person chose that the tests fail, with a message that names the file, when the page holds no such block: the same behaviour Case 652 gave `tests/test_case_schema.py`.
>
> The last `－` line of the Criterion of each of the two Estimates says the test is skipped, so this Case makes it false. Each Estimate is a separate promise, so each is a sub-case that replaces its Criterion whole: the same lines, with that line rewritten to say that the tests that read the block fail and no test of the file is skipped. Both pages go `pending`. The two `passed` readings at lines 1 and 2 of this session's ledger were taken at the `/hi`, before this Case existed. They stand before its decision lines and are the ground of the Case. The `update` lines that follow them set both Estimates `pending`, so the librarian records the reading first and the replaced Criterion after it. `estimate-case-protocol-example-passes-the-check` went through the same order in session 1343: its History holds the `passed` reading from that session's ledger, then the update of case 652, and its `status` is `pending`. No new reading of either Estimate is taken in this session. The readings are taken at the `/hi` of a later session, since `rule-retro` says that an Estimate this session creates or updates has no reading in this session, and the ledger hook refuses one (case 428.1). The `purpose` of neither Estimate speaks of the skip, so both stand. Each `method` reads "passed and not skipped", which stays true once no skip remains, so both stand. The skip lives in one function, `example`, which both pairs of tests call, so the code change is one task on Case 661.1 and covers Case 661.2 too. The test only goes red and loses nothing, so it keeps no old form. The defer Criterion said its Insight stands `actioned`, addressed by this Case; in the new Criterion it names case 651.3, the Case that addressed it, since this Case does not. So three old lines are not carried word for word, by intent: the skip line of each Criterion and the Insight line of the defer Criterion. Some `then` lines of the two sub-cases share most of their words, also by intent: the two Estimates check two examples of one page in the same way, and each line names its own block, check or hook. The `－` line of `estimate-guppi-tests-green` that says a skipped test is not a failure stands: after this Case these tests fail rather than skip, which is the behaviour the person chose. This Case changes neither `rule-orchestration` nor its page.
>
> The search this Case rests on. A Grep of `test_orchestration|estimate-orchestration-showing-example-passes-the-check|estimate-orchestration-defer-example-passes-the-hook` over the repository root, with the glob `!**/decisions/** !**/raw/** !**/log.md !**/brief.md`, printed 4 files: `tests/test_orchestration.py`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-orchestration-defer-example-passes-the-hook.md` and `vault/wiki/estimates/estimate-orchestration-showing-example-passes-the-check.md`. On `rule-orchestration` the hits are its `estimates` field and two History lines, which stand. The other three enter the Case.

> **problem:**
> `tests/test_orchestration.py` still skips when `vault/wiki/orchestration.md` holds no `showing` or `defer` example, though both examples now stand there and both readings passed. A lost example would go unchecked while the tests stay green. The question was what the tests do when the page holds no example.

> **recommend:**
> - **What the test does when the page has no example**
>   - Recommended: (a) fail with a message that names the file.
>   - Answer: agreed, (a).

### Case 661.1 — The showing tests fail when the page holds no showing example

> **given:**
> `tests/test_orchestration.py`: the tests that run the checks over the examples.
> **＋** `estimate-orchestration-showing-example-passes-the-check`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the page that holds the examples, rendered from `rule-orchestration`. Unchanged.
> **＋** `rule-orchestration`: the rule whose Render is that page. Unchanged.
> **＋** `guppi/casecheck.py`: the check of a reply that shows a Case, which the test imports. Unchanged.
> **＋** `rule-case-check`: its `Stop` check runs over a reply that shows a Case. Unchanged.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `showing` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it the functions of `guppi/casecheck.py` that the `Stop` check of `rule-case-check` runs over a reply that shows a Case, with a store whose sub-cases hold the ledger lines the example's `ratification` gives them.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## Showing and signing a Case`, one block tagged `showing`: a reply that shows a Case with two sub-cases, its heading, one list with an item per sub-case, one `ratification` and the agent's own text after one horizontal rule.
> **＋** The `ratification` of the example is a quote block: the line `> **ratification:**`, then the fence and the ledger lines of both sub-cases, each line opening with `> `.
> **＋** The example is in English; the paragraph before the block says that in the chat the heading, the names and the short texts stand in the language of the chat, that the file goes by `SendUserFile` in the same reply, and that the example passes the `Stop` check of `rule-case-check`, which is the source of the limits; it lists no other limit.
> **＋** The check finds no text outside the list and the `ratification`, reads the `ratification` as the showing of each sub-case it names, and finds no difference from the store, and the test passes.
> **＋** The example with the lines of its fence not quoted gives the finding of a text outside the list, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `showing`, both tests of `tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

> **tasks:**
> - [ ] update `estimate-orchestration-showing-example-passes-the-check`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the tests fail, not skip, when orchestration.md holds no block tagged showing (case 661.1)`
> - [ ] `tests/test_orchestration.py`: `example` calls `pytest.fail` with a message that names the file and the tag, in place of `pytest.skip`, when the page holds no block tagged that tag; the module docstring says the tests fail then and drops the sentences on the skip.
> - [ ] read `estimate-orchestration-showing-example-passes-the-check`, at the `/hi` of a later session

> **ratification:**
> ```
> - decision[case 661.1][update][estimate-orchestration-showing-example-passes-the-check]{ref:rule-orchestration}
> ```

### Case 661.2 — The defer tests fail when the page holds no defer example

> **given:**
> `tests/test_orchestration.py`: the tests that run the hook over the examples.
> **＋** `estimate-orchestration-defer-example-passes-the-hook`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the page that holds the examples, rendered from `rule-orchestration`. Unchanged.
> **＋** `rule-orchestration`: the rule whose Render is that page. Unchanged.
> **＋** `guppi/ratified.py`: the hook that writes a defer-only Case into the Spec, which the test imports. Unchanged.
> **＋** `rule-spec-write`: its `Stop` hook writes a defer-only Case under `## Deferred`. Unchanged.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept`: the Insight the Criterion names. Unchanged.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `defer` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it, as the text of a reply, the functions of `guppi/ratified.py` that the `Stop` hook of `rule-spec-write` runs over a defer-only Case, in a temporary project that holds the schema files of the vault and a plan file, with one `defer` record for each item of the example.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## The short form — deferred decisions`, one block tagged `defer`: a Case in the short form with its heading, `context`, `problem` and a fence tagged `then` whose `defer:` holds a list, one item per target, each item opening with `- slug:` and carrying `type` and `purpose`.
> **＋** The paragraph before the block says that the reply that shows the Case carries its `LEDGER` block with one `defer` line per item, and that the example passes the `Stop` hook of `rule-spec-write`, which is the source of the limits; it lists no other limit.
> **＋** The hook writes the example under `## Deferred` of the plan file with no error, and the test passes.
> **＋** The example with its `defer:` items written as one mapping gives the error that no fence tagged `then` holds its `defer` items, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the hook from `guppi/ratified.py`, and holds no copy of either.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stands `actioned`, addressed by case 651.3.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `defer`, both tests of `tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

> **tasks:**
> - [ ] update `estimate-orchestration-defer-example-passes-the-hook`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the tests fail, not skip, when orchestration.md holds no block tagged defer (case 661.2)`
> - [ ] read `estimate-orchestration-defer-example-passes-the-hook`, at the `/hi` of a later session

> **ratification:**
> ```
> - decision[case 661.2][update][estimate-orchestration-defer-example-passes-the-hook]{ref:rule-orchestration}
> ```
