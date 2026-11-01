## Case 985 — The builder follows a changed step into the harness code

> **context:**
> When a Case changes what a step writes, copies or shows, `case-guppi` must find each other text that reads that output or does the same step. The rule sends it to Grep `vault/wiki/rules/` and `.claude/` only. The reading of `estimate-case-build-reads-the-readers-of-a-changed-step` failed for the third time (ledger of session 0141, line 18): Case 972 of session 2307 changed the wait check of pre-spec for a `method` the plan writes and missed the `method` an Estimate page keeps when an `update` replaces its Criterion whole. Both inputs are judged in the `update` loop of `plan_findings` in `.guppi/guppi/prespec.py`: a `method` under `set` by `waits_for_another_session`, and with none, the kept one by `kept_method_waits`, which reads it by `kept_method`; I read that loop and both functions whole. The note of that build lists those lines of `prespec.py` among its reads, so the place was in the code, which the Grep the rule sets does not reach. The two earlier failures (sessions 2005 and 0431) missed a text of another kind each, and Cases 948 and 966 added a sentence each. The person chose to widen the rule into `.guppi/guppi/`. The new clause goes into the sentence on a changed step of the Render of `rule-case-build`, and the Criterion of the Estimate is replaced whole to match; its `When` line and its last `Then` line are rewritten on purpose, the first to name a function of `.guppi/guppi/` among the doers of a step, the second to name a place of code among what enters the Case; its `purpose` and `method` are set anew, since the `method` waited for the session of the Render of Case 966, which has passed. The rule that governs the option is `rule-case-build` itself; the new clause is consistent with `rule-one-judgment-one-implementation`, a neighbour of `rule-case-build` in `.guppi/links.md`, since it only reads the places of one judgment. A Grep `does the same step|same step|readers-of-a-changed-step` over `vault/wiki/`, `.claude/` and `.guppi/guppi/` printed `brief.md`, `.claude/agents/case-guppi.md`, `log.md`, the Estimate, `rule-case-build` and `insight-case-build-changes-a-step-without-reading-its-readers`; the insight is `actioned` and its proposal still holds, and `brief.md` and `log.md` are not read. A Grep `case-guppi\.md|rule-case-build` over `.guppi/tests/` printed `test_guppi_package.py`, whose tests over every file of `.claude/` refuse the old commands and the paths `guppi/` and `tests/` at the start of a path, which the new `.guppi/guppi/` is not, by `reword_pattern` of `.guppi/guppi/generate.py`. The block of `.claude/agents/case-guppi.md` in `.guppi/links.md` names no neighbour that this clause makes false. Frontier item C2 also changes the Render of `rule-case-build`, in the sentence on `.guppi/links.md`; this Case leaves that sentence alone. The session's ledger holds no `error` lesson.

> **problem:**
> The search that finds the readers of a changed step does not reach the harness code, so a step done by a function there is changed on one input and missed on another.

> **recommend:**
> - **What changes after the third failed reading**
>   - Recommended: (a) the rule follows a step into the harness code.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: its Render holds the sentence on the readers of a changed step.
> **＋** `.claude/agents/case-guppi.md`: rendered from `rule-case-build`.
> **＋** `estimate-case-build-reads-the-readers-of-a-changed-step`: its Criterion is replaced whole.
> **＋** `vault/wiki/rules/`: the Rule pages the builder searches for the readers of a step.
> **＋** `.claude/`: the harness files the builder searches for the readers of a step.
> **＋** `.guppi/guppi/`: the harness code the builder now searches too.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent, a hook or a function of `.guppi/guppi/` writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

> **then:**
> It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
> **＋** Where a function of `.guppi/guppi/` does the step, it also searches `.guppi/guppi/` for the name of that function and of the function it judges by.
> **＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
> **＋** Where a function of `.guppi/guppi/` does the step, it reads each place that calls that function or the function it judges by, and each other place that makes the same judgment on another input, such as the value a plan writes and the value a live page keeps.
> **＋** Each step, skill or place of code that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` the new path your Case adds and each agent, skill and hook the step leads to included; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924 and 966). ``
>   - new: `` the new path your Case adds and each agent, skill and hook the step leads to included; where a function of `.guppi/guppi/` does the step, such as a check, Grep `.guppi/guppi/` too for the name of that function and of the function it judges by, and read each place that calls them and each other place that makes the same judgment on another input, such as the value a plan writes and the value a live page keeps; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924, 966 and 985). ``
>   - change: `the readers of a changed step include the places of the harness code that call the function of the step or make its judgment on another input`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-reads-the-readers-of-a-changed-step`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether case-guppi, when its Case changes what a step writes, copies or shows or adds a path to it, reads each step and skill that reads that output or does the same step, the steps after it and the new path included, and, where a function of .guppi/guppi/ does the step, each place that calls it or makes the same judgment on another input, and names each one in context or enters it in the Case"
>     method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on following a step into the code of .guppi/guppi/: the findings of ask-guppi at that /pre-spec, read in the agent transcript of that ask-guppi under ~/.claude/projects/, for a Case that changes a step and misses a step, a skill or a place of code that reads its output or does the same step, the count and the transcript in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the readers of a changed step include the places of the harness code; pending again after the failed reading of session 0141`
> - [ ] read `estimate-case-build-reads-the-readers-of-a-changed-step`

> **ratification:**
> ```
> - decision[case 985][update][rule-case-build]{ref:rule-case-build}
> - decision[case 985][update][estimate-case-build-reads-the-readers-of-a-changed-step]{ref:rule-case-build}
> ```
