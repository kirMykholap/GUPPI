## Case 754 — case-guppi reads the test code over a live text a Case changes

> **context:**
> Some tests in `tests/` read a live page of the vault, or a file under `.claude/`, and run code over it. Today `case-guppi` has one step for them, set by case 736.1: when a Case changes the code of a check, it reads each live file such a test runs through that check. No step covers a Case that changes the text itself, and no step makes the agent read the test's own helper code. Case 751.6 put a horizontal rule before the example of a showing in `orchestration.md`; its context said that `tests/test_orchestration.py` accepts the changed example, judged by the check functions alone. At Retro the test failed: its helper `store_of_showing` read the ledger lines by `fence_ledger_lines` over the whole text, which stops at the first rule, and the Spec held no task for the test (`lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper`). The synthesis joined that lesson to `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`, which opened again with severity 1. This Case adds one sentence to the Render of `rule-case-build`, after the sentence of case 736.1, and a new Estimate checks it. The person chose a new promise beside the old one, so the Criterion of `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check` stands: it covers a changed check, and this Case covers a changed text. The sentence of the Render that reads a module of code in parts, checked by `estimate-case-build-reads-by-need-and-in-parts`, stands too: the new step reads named functions of a test file, which is a reading in parts. In the page `rule-case-build`, read whole, no other sentence states how the agent reads a test, so no other sentence becomes false. A Grep of `(ROOT|REPO|parents\[1\]) / "(vault|\.claude)"` over `tests/` printed the live reads of `tests/test_orchestration.py`, `tests/test_generate.py`, `tests/test_materialize.py`, `tests/test_schemas.py` and `tests/test_case_schema.py`: they read `orchestration.md`, `case-schema.md`, `case-example.md` and the `schema.yaml` files, and none of these is a file that this Case changes. The change adds no code under `guppi/`, so no judgment is copied. The new text of `.claude/agents/case-guppi.md` lands at the librarian's render, and only `make lint` reads it, so no old form is kept.

> **problem:**
> When a Case changes a live text that a test reads, nothing makes `case-guppi` read the test's own code over the new text. A claim that the test still passes is then signed on the check functions alone, and the test breaks first at Retro.

> **recommend:**
> - **A new promise or the old one widened**
>   - Recommended: (a) a new Estimate, `estimate-case-build-reads-the-test-code-over-a-changed-text`, beside the old one, which stays as it is.
>   - Answer: agreed, (a).
> - **Which changed texts the step covers**
>   - Recommended: (a) any live file of `vault/` or `.claude/` that the Case changes, by a page `update` or by the render of its rule, when a test reads that file.
>   - Answer: agreed, (a).
> - **How far the reading of the test goes**
>   - Recommended: (a) the whole path the text takes: the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `guppi/` they call.
>   - Answer: agreed, (a).
> - **What enters the Case, and whether the Insight closes**
>   - Recommended: (a) each place where the new text would fail the test enters the Case as a task that changes the test or the text, or `context` says why it stands; the Insight is set `actioned`, with `addressed_by` naming this Case.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule whose Render sets how `case-guppi` reads the frame of a Case.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-case-build-reads-the-test-code-over-a-changed-text`: the new check of the step.
> **＋** `lesson-case-build-changed-example-read-by-the-check-not-by-the-test-helper`: the lesson whose cause the step closes.
> **＋** `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`: the Insight that lesson reopened; set `actioned`.
> **＋** `rule-insights-schema`: the rule that sets `addressed_by` of an `actioned` Insight to the latest decision.
> **＋** `vault/`: the live pages a Case changes and a test may read.
> **＋** `tests/`: the tests that `case-guppi` searches for a live read of a changed file.
> **＋** `guppi/`: the code that a test calls over the text it reads.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case that changes a live file of `vault/` or `.claude/`, by a page `update` or by the render of its rule.

> **then:**
> It searches `tests/` for the tests that read that file live, not a copy under a temporary folder.
> **＋** For each such test, it reads the new text against the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `guppi/` they call.
> **＋** Each place where the new text would fail the test enters the Case as a task that changes the test or the text, or its `context` says why it stands.
> **－** `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` stands `actioned` with `addressed_by: decision-case-754` and leaves the backlog.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` each text the new check would refuse enters the Case, or `context` says why it stands (case 736.1). ``
>   - new: `` each text the new check would refuse enters the Case, or `context` says why it stands (case 736.1). When the Case changes a live file of `vault/` or `.claude/`, by a page `update` or by the render of its rule, Grep `tests/` for the tests that read that file live, not a copy under a temporary folder; for each one, read the new text against the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `guppi/` they call; each place where the new text would fail the test enters the Case as a task that changes the test or the text, or `context` says why it stands (case 754). ``
>   - change: `case-guppi reads the code of a test, its helpers included, over a live text the Case changes (case 754)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-reads-the-test-code-over-a-changed-text`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi, for a Case that changes a live file of vault/ or .claude/, reads the code of each test that reads that file live — the test functions, the functions of the test file they call, its helpers included, and the functions of guppi/ they call — against the new text, and puts each place where the new text would fail the test into the Case as a task, or says in context why it stands`
>   - method: `by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; and, for each Case of that session that changes a live file of vault/ or .claude/, its context and tasks read for the tests that read that file live, each one named or said to stand`
>   - tags: `[workflow, harness, tests]`
> - [ ] update `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`
>   - set: `{status: actioned, addressed_by: decision-case-754}`
>   - change: `actioned: case-guppi reads the code of a test, its helpers included, over a live text the Case changes (case 754)`
> - [ ] read `estimate-case-build-reads-the-test-code-over-a-changed-text`

> **ratification:**
> ```
> - decision[case 754][update][rule-case-build]{ref:rule-case-build}
> - decision[case 754][create][estimate-case-build-reads-the-test-code-over-a-changed-text]{ref:rule-case-build}{tags:workflow,harness,tests}
> - decision[case 754][update][insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]{ref:insight-workflow-fact-signed-from-a-check-that-does-not-cover-it}
> ```
