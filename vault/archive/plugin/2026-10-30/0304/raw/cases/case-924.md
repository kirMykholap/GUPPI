## Case 924 — case-guppi reads the steps that read or repeat a step it changes

> **context:**
> A Case can change what one step of a skill, an agent or a hook writes, copies or shows. Today `case-guppi` judges that change from the step in front of it. The Render of `rule-case-build` makes it search for the slug of a page the change makes false and for the name of a field, term or command whose behaviour changes, but nothing makes it read the other steps that read that output, the other skill that does the same step, or the new path its own Case adds. The Insight `insight-case-build-changes-a-step-without-reading-its-readers` clusters two lessons of this cause. In `lesson-case-build-claims-a-page-stands-without-reading-the-path-it-changes`, Case 851 claimed that the readers of the `Branch:` line stand, judged by the old path alone, though on its new path the line still read `none: …`. In `lesson-case-build-changes-a-step-without-reading-what-reads-it`, Case 903.2 named only /box as the step that shows the librarian's report though /handoff shows it too, and Case 905 left step 5 of the Render of `rule-plugin-install` checking a file that its new step 4 no longer copies. Each time /pre-spec found the fault after the person had ratified the Case. The person chose one new sentence in the paragraph of the Render on the checks before the summary, placed after the sentence on a fact that no slug marks, with a new Estimate of its own, and a search over the rules and `.claude/` only, since the code readers already have the sentences of cases 736.1, 754 and 869. The pair anchors on that sentence; a Grep of the pattern `For a fact that no slug marks, read the index lines` over `vault/wiki/rules/rule-case-build.md` printed a count of 1. `estimate-case-build-checks-the-finished-case` stands: each line of its Criterion names one check before the summary, and none of them becomes false; the new search is a promise of its own, which the new Estimate checks. No other Estimate of the page speaks of the readers of a step. The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed; it is set `actioned` with `addressed_by: decision-case-924`, the bare slug, as `rule-insights-schema` sets it (case 712). A Grep of the slug of the Insight over the repository outside `vault/raw/` printed `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/archive/plugin/2026-10-29/1930/raw/materialize.yaml` and the two lesson pages: the backlog line names the Insight as the source of this item and this Case does not edit `backlog.md`, the log and the archive are not read, and the lessons keep their `insight` link. `.guppi/tests/test_guppi_package.py` reads every file of `.claude/` and every live page for `uv run guppi`, `uv run pytest`, `guppi/` and `tests/`; the new sentence and the new Estimate name none of them. The session's ledger holds no `lesson[error]` line, so no `{addresses:...}` mark is written. Case 926, whose finished file was read after its build ended, also changes the Render of `rule-case-build`: its pair anchors on the sentence of case 869 in the paragraph on the frame and replaces only that sentence, while the pair of this Case anchors on a sentence of the paragraph on the checks before the summary, so the two `old` values do not overlap and neither pair changes the text the other matches. Each Case renders `.claude/agents/case-guppi.md` after its own pair, which takes both changes. The sentence of Case 926 is about a claim on what code does, and the new sentence here is about the steps of the rules and `.claude/` that read or repeat an output, so neither text contradicts the other; this Case changes neither `estimate-case-build-reads-the-code-it-states` nor the Insight that Case 926 actions.

> **problem:**
> `case-guppi` changes what a step writes, copies or shows from the one step in front of it, and does not read the steps and skills that read that output or do the same step, or the new path its own Case adds, so the Case holds for one step only and /pre-spec finds the rest after the person has ratified it.

> **recommend:**
> - **Where the fix goes**
>   - Recommended: (a) a new sentence in the paragraph of the Render on the checks before the summary, a new Estimate `estimate-case-build-reads-the-readers-of-a-changed-step`, and the Insight set actioned by this Case.
>   - Answer: agreed, (a).
> - **What the reading covers**
>   - Recommended: (a) the steps of the harness texts: the rules in `vault/wiki/rules/` and the files under `.claude/`, the steps after it in the same text and the new path the Case adds.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the /pre-spec finding that the second part of the `method` read the /pre-spec of this session, whose Cases were built on the old Render, and so waited for no event that could show the behaviour.
>   - Taken: that part now waits for the /pre-spec of the first session whose `case-guppi` runs on the Render this Case sets; the first part, the Render in the Spec read at the Retro, stays.

> **given:**
> `rule-case-build`: the Rule whose Render is the prompt of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from that Render.
> **＋** `estimate-case-build-reads-the-readers-of-a-changed-step`: the new check of this promise.
> **＋** `insight-case-build-changes-a-step-without-reading-its-readers`: the Insight this Case actions.
> **＋** `rule-insights-schema`: the rule that sets `actioned` and `addressed_by`.
> **＋** `vault/wiki/rules/`: the Rule pages whose Renders the search reads for steps.
> **＋** `.claude/`: the rendered harness files the search reads for steps.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

> **then:**
> It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
> **＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
> **＋** Each step or skill that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. ``
>   - new: `` For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. When the Case changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, Grep `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step, and read each step and skill that reads that output or does the same step, the steps after it in the same text and the new path your Case adds included; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in case 924). ``
>   - change: `case-guppi reads the steps and skills that read or repeat the output of a step its Case changes, and the new path its Case adds`
> - [ ] create `estimate-case-build-reads-the-readers-of-a-changed-step`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi, when its Case changes what a step writes, copies or shows or adds a path to it, reads each step and skill that reads that output or does the same step, the steps after it and the new path included, and names each one in context or enters it in the Case`
>   - method: `by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line; after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on the readers of a changed step: the findings of ask-guppi at that /pre-spec read for a Case that changes a step and misses a step or skill that reads its output or does the same step, the count in the estimate line`
>   - tags: `[session, workflow, harness, case-build]`
> - [ ] update `insight-case-build-changes-a-step-without-reading-its-readers`
>   - set: `{status: actioned, addressed_by: decision-case-924}`
>   - change: `actioned: case-guppi reads the steps that read or repeat a step its Case changes`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-reads-the-readers-of-a-changed-step`

> **ratification:**
> ```
> - decision[case 924][update][rule-case-build]{ref:rule-case-build}
> - decision[case 924][create][estimate-case-build-reads-the-readers-of-a-changed-step]{ref:rule-case-build}{tags:session,workflow,harness,case-build}
> - decision[case 924][update][insight-case-build-changes-a-step-without-reading-its-readers]{ref:insight-case-build-changes-a-step-without-reading-its-readers}
> ```
