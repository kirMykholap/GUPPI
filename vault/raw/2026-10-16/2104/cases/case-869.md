## Case 869 — case-guppi reads the function that decides a claim it states about code

> **context:**
> `case-guppi` sometimes says what a function or a script of the repository does, prints or leaves out without reading the function that decides it, and a Case or a recommendation rests on that claim. The claim then proves false after the person signed it, and the Case is built again. `insight-case-build-claims-what-code-does-without-reading-it` clusters three lessons of this cause, and they record these slips. In Case 807 the agent said that the run of `guppi ship` shows every page line that holds a pointer, but `clean_parenthesis` of `.guppi/guppi/ship.py` cuts a pointer out of a longer bracket without printing a line, and a later round withdrew the answer. In Case 856 the agent cited the predicate `ships` of `.guppi/guppi/ship.py` by one line and gave its first condition only. In Case 783 it named a shared judgment without reading the function of the other side; the sentence of case 785 in `rule-case-build` already covers that form, so it stays as it is. Today the Render of `rule-case-build` asks the agent to read code for set tasks only. A fact the prompt states is read at its source (case 690.1). Before a task adds a judgment, `.guppi/guppi/` is searched and `context` names that search (case 752). Over a changed live text, the agent reads the test functions, the functions of the test file they call and the functions of `.guppi/guppi/` they call (case 754). A function named as the judgment two sides share is read whole on each side (case 785). A page offered for code no page covers is described from the code read (case 803). No sentence asks the agent to read the deciding function before every claim it makes itself about what code does, prints or leaves out, in a round, in `context`, in `then` or in a page text. The person chose to action the Insight. Case 869 adds one sentence after the sentence of case 785: before such a claim the agent reads the deciding function whole, each condition and not one line, and `context` names the file and the function. The governing rules are `rule-agent-writing`, whose passage says "Name a real source or remove the claim", and `rule-insights-schema`, by which an `update` actions an Insight and `addressed_by` takes the bare slug `decision-case-869`. The Insight was put off by Case 835, so its decision line carries `{supersedes:case 835}`. Its three lessons are archived by the cascade of `generate` once it is `actioned`. The new sentence names the Case in a bracket at the end of the sentence, since `rule-case-build` has `core: true`. The Criterion of each Estimate of `rule-case-build` was read. `estimate-case-build-reads-by-need-and-in-parts` stands: it reads a module of code in parts, and the new sentence names the deciding function as one of those parts. `estimate-case-build-offers-a-page-for-code-no-page-covers` stands, and its Criterion does not clash with the new sentence. Its Criterion reads that code in parts, the functions the Case changes and the places that call them, and the round offers a page described from the code read. Where that description says what a function does, the new sentence adds that the deciding function is read whole, and a whole function is one of the parts that Criterion reads. Nothing in that Criterion allows a claim about code from a function read at one line. `estimate-case-build-finds-an-existing-judgment` stands: its promise on a shared judgment is not changed. `estimate-case-build-reads-a-prompt-fact-at-its-source` stands: it covers a fact of the prompt, not a claim of the agent. A claim about an outside tool is the item of Case 871, and what a check printed at its last run stays with the sentence of case 798.2. A Grep `case-guppi\.md|rule-case-build` over `.guppi/tests/` printed nothing, so no test reads the live agent file. A Grep `insight-case-build-claims-what-code-does-without-reading-it` over `vault/wiki/` printed `brief.md`, `backlog.md`, `log.md` and the three lessons `lesson-case-build-reused-judgment-not-checked-against-the-other-side`, `lesson-case-build-recommended-on-a-claim-about-code-it-did-not-read` and `lesson-case-build-states-a-predicate-wider-than-the-code`. In the lessons the `insight` field stays true. `backlog.md` is written again by `guppi backlog`, and `brief.md` and `log.md` are not read. A Grep `estimate-case-build-reads-the-code-it-states` over `vault/` printed `raw/2026-10-16/event_log.md`, `raw/2026-10-16/2104/ledger.md` and this case file and no page, so the slug is free. No option rests on a check passing. Each Case of this session was built by `case-guppi` under the old Render, so the `/pre-spec` of this session cannot show the new sentence at work. The `method` of the new Estimate therefore reads the new Render at Retro, and it waits for the first `/pre-spec` of a session whose Cases were built under that Render before it counts the findings. This rebuild did not read the case files of Cases 868, 870, 871 and 872, which are rebuilt at the same time. Their decision lines in the ledger of this session show that Cases 870, 871, 872.1 and 872.3 change `rule-case-build`, and that Case 872.4 changes `estimate-case-build-reads-by-need-and-in-parts`. Where one of them takes the sentence of case 785 as its anchor, the two pairs must be read side by side.

> **problem:**
> `case-guppi` can state what a function or a script of the repository does without reading the function that decides it. A Case the person signed then rests on a false claim and is built again.

> **recommend:**
> - **What happens to this pattern**
>   - Recommended: (a) fix it: add a duty to `rule-case-build`, set the Insight `actioned` and retire its defer.
>   - Answer: agreed, (a).
> - **How wide the duty to read the code is**
>   - Recommended: (a) every claim about code in a round, `context`, `then` or a page text, the whole deciding function read, the file and the function named in `context`.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) a new Estimate `estimate-case-build-reads-the-code-it-states` on `rule-case-build`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by findings of `/pre-spec`: the `context` overstated what the Render lacks, it did not name `estimate-case-build-offers-a-page-for-code-no-page-covers`, and the `method` of the new Estimate counted findings at the `/pre-spec` of this session, whose Cases were built under the old Render.
>   - Taken: the `context` names the sentences of cases 752, 754 and 803 that already read code for set tasks, and says why the Criterion of `estimate-case-build-offers-a-page-for-code-no-page-covers` does not clash with the new sentence. The count of findings in the `method` waits for the first `/pre-spec` of a session whose Cases were built under the new Render.

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, gains the sentence on a claim about code.
> **＋** `estimate-case-build-reads-the-code-it-states`: the new Estimate of that sentence.
> **＋** `insight-case-build-claims-what-code-does-without-reading-it`: set `actioned`, its defer retired.
> **＋** `rule-agent-writing`: the rule that a claim names a real source.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and states in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out.

> **then:**
> Before it states the claim, `case-guppi` reads whole the function that decides it, each of its conditions and not only the line it cites.
> **＋** The `context` of the Case names the file and the function that `case-guppi` read for the claim.
> **＋** A claim about code that `case-guppi` did not read stays out of the Case.
> **－** `case-guppi` still reads a module of code in parts: the deciding function is one of those parts.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `and the task adds one test that runs both sides over that input and asserts they answer alike (case 785).`
>   - new: `` and the task adds one test that runs both sides over that input and asserts they answer alike (case 785). Before you state in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out, read whole the function that decides it, each of its conditions and not only the line you cite, and name its file and the function in `context`; that function is one of the parts of its module that you read, and a claim about code you did not read stays out of the Case (case 869). ``
>   - change: `case-guppi reads whole the function that decides a claim it states about code, and names it in context (case 869)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-reads-the-code-it-states`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi, before it states what a function or a script of the repository does, prints or leaves out, reads whole the function that decides it, names its file and the function in context, and keeps out a claim about code it did not read`
>   - method: `by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion; by hand, after the first /pre-spec of a session whose Cases case-guppi built with .claude/agents/case-guppi.md rendered from that Render: the findings of ask-guppi at that /pre-spec read for a claim of a Case about what code of the repository does that its context does not back by the function it read, the count in the estimate line`
>   - tags: `[session, workflow, harness, case-build]`
> - [ ] update `insight-case-build-claims-what-code-does-without-reading-it`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-869
>     ```
>   - change: `actioned: case-guppi reads whole the function that decides a claim it states about code, and names it in context (case 869)`
> - [ ] read `estimate-case-build-reads-the-code-it-states`

> **ratification:**
> ```
> - decision[case 869][update][rule-case-build]{ref:rule-case-build}
> - decision[case 869][create][estimate-case-build-reads-the-code-it-states]{ref:rule-case-build}{tags:session,workflow,harness,case-build}
> - decision[case 869][update][insight-case-build-claims-what-code-does-without-reading-it]{ref:insight-case-build-claims-what-code-does-without-reading-it}{supersedes:case 835}
> ```
