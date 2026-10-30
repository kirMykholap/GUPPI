## Case 926 — case-guppi reads what a function calls and the input it walks over before it states what the function does

> **context:**
> `case-guppi` sometimes states what code of the repository does without reading the code that decides it. Case 869 gave `rule-case-build` a sentence against this: read whole the function that decides the claim, each of its conditions, and name it in `context`; it set `insight-case-build-claims-what-code-does-without-reading-it` to `actioned`. The fault came back in session 2312: the trigger of `lesson-case-build-judged-a-check-by-the-last-stretch-of-the-transcript` says that Case 896.4, as first ratified, said that the check on `SubagentStop` takes a round that wrote only the note for an answer with no file written, and that ask-guppi at `/pre-spec` found that `written_case_files` reads every `Write` and `Edit` of the whole transcript; this Case states nothing of that code beyond what the lesson says. Its root cause says that `case-guppi` described `written_case_files` from its name and docstring without following what its loop over `agent_transcript_path` collects, and that it did not search for an existing judgment of the name of a Case file. That lesson reopened the Insight, which now stands `open` in `## Deferred` of `backlog.md` with no `deferred_by`. The sentence of case 869 does not ask for what the input of a function holds, and that input decided this claim. So the sentence now also asks for each function called on the way to the claim and for the place where the caller takes the input that the function walks over. It also says that the name and the docstring of a function are no reading of it. The governing rule is `rule-case-build` itself, together with the line of `CLAUDE.md` that a claim names a real source. The second half of the root cause stands under the sentence of case 752, which already names the Grep of `.guppi/guppi/` for an existing judgment that Case 896.4 skipped. Its Estimate, `estimate-case-build-finds-an-existing-judgment`, checks that search, and its Criterion stands, since no sharper text would have changed that skip. `estimate-case-build-reads-the-code-it-states` checks the sentence, so its Criterion is replaced whole, and its `purpose` and `method` are set anew, since both state the old promise. The `method` ties its event to the Render this Case sets, a `/pre-spec` of a session whose `case-guppi` runs on `.claude/agents/case-guppi.md` as rendered by case 926, since the `/pre-spec` of this session runs before that render and judges Cases built on the sentence of case 869; it names a kind of moment, not the first such `/pre-spec`, as case 898.2 set the method. A Grep of `.guppi/tests/` for `case-guppi\.md|rule-case-build` printed `.guppi/tests/test_guppi_package.py` alone. Its `test_no_caller_runs_the_code_or_the_tests_without_the_project` reads each file under `.claude/` live, through `callers`, for `uv run guppi` and `uv run pytest`, and its `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` reads each live page, through `live_pages`, for those and for `guppi/` and `tests/`; the new sentence, the new Criterion, `purpose` and `method` and the `change` lines name none of them, so the test stands. A Grep of the repository outside `vault/archive/` for `estimate-case-build-reads-the-code-it-states` printed `vault/raw/2026-10-30/0304/cases/case-926.md`, `vault/raw/2026-10-30/0304/cases/case-924.md`, `vault/raw/2026-10-30/0304/cases/note-926.md`, `vault/raw/2026-10-30/0304/ledger.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/lessons/lesson-brief-lists-transcript-readings-under-work.md`. That lesson records the `/hi` of session 1805 and stands, the ledger holds the decision line of this Case on that Estimate, `log.md` is not read, and `case-924.md` names that Estimate only to say that Case 924 does not change it. Case 924, whose finished file was read after its build ended, also changes the Render of `rule-case-build`: its pair anchors on the sentence on a fact that no slug marks, in the paragraph on the checks before the summary, and adds one sentence after it on the steps that read or repeat a changed step. This Case anchors on the sentence of case 869 in the paragraph on the frame, so the two `old` values do not overlap and neither pair changes the text the other matches; each Case renders `.claude/agents/case-guppi.md` after its own pair, and the render takes both changes. Case 924 says that the code readers already have the sentence of case 869, and this Case keeps that sentence and only widens it, so neither text makes the other false. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> `case-guppi` read the function that decided a claim but not what the input of that function holds, and it took the name and the docstring of the function for its behaviour, so a Case was ratified on a false claim about a check.

> **recommend:**
> - **What the Case changes in the sentence on a claim about code**
>   - Recommended: (a) sharpen the sentence: a name or a docstring is no reading; read each function called on the way, and where the function walks over an input, the place where its caller takes that input; name each in `context`.
>   - Answer: agreed, (a).
> - **The second half of the lesson: the search for an existing judgment**
>   - Recommended: (a) leave the sentence of case 752 as it stands; `context` says why.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) replace the Criterion of `estimate-case-build-reads-the-code-it-states`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the `/pre-spec` finding that the `method` of `estimate-case-build-reads-the-code-it-states` does not tie its event to the new Render, so the `/pre-spec` of this session, which runs before the render, would meet it.
>   - Taken: the `method` waits for a `/pre-spec` of a session whose `case-guppi` runs on `.claude/agents/case-guppi.md` as rendered by case 926.

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, holds the sentence on a claim about code.
> **＋** `.claude/agents/case-guppi.md`: the rendered agent file of `case-guppi`.
> **＋** `estimate-case-build-reads-the-code-it-states`: the Estimate of that sentence; its Criterion is replaced whole.
> **＋** `insight-case-build-claims-what-code-does-without-reading-it`: set `actioned`.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and states in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out.

> **then:**
> Before it states the claim, `case-guppi` reads whole the function that decides it, each of its conditions and not only the line it cites.
> **＋** It reads each function that this function calls on the way to what it states.
> **＋** Where the function walks over an input, such as a transcript or a list of files, it reads the place where the caller of the function takes that input.
> **＋** The `context` of the Case names the file and the function that `case-guppi` read for the claim.
> **＋** The `context` of the Case also names each function called on the way and the place of the input that `case-guppi` read for the claim.
> **＋** A claim about code that `case-guppi` did not read stays out of the Case.
> **－** The name and the docstring of a function do not stand for a reading of it.
> **－** `case-guppi` still reads a module of code in parts: the deciding function is one of those parts.
> **－** Each function it reads on the way to the claim is one of those parts too.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` Before you state in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out, read whole the function that decides it, each of its conditions and not only the line you cite, and name its file and the function in `context`; that function is one of the parts of its module that you read, and a claim about code you did not read stays out of the Case (case 869). ``
>   - new: `` Before you state in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out, read whole the function that decides it, each of its conditions and not only the line you cite, each function it calls on the way to what you state, and, where it walks over an input such as a transcript or a list of files, the place where its caller takes that input, so that you know what the input holds; the name of a function and its docstring are no reading of it; name in `context` the file and each function you read for the claim; those functions are among the parts of their modules that you read, and a claim about code you did not read stays out of the Case (as set in cases 869 and 926). ``
>   - change: `case-guppi reads, for a claim about code, each function called on the way and where the caller takes the input, and takes no name or docstring for a reading (case 926)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-reads-the-code-it-states`
>   - set:
>     ```
>     status: pending
>     purpose: Whether case-guppi, before it states what a function or a script of the repository does, prints or leaves out, reads whole the function that decides it, each function it calls on the way and the place where its caller takes the input it walks over, takes no name or docstring of a function for a reading of it, names in context the file and each function it read, and keeps out a claim about code it did not read
>     method: "by hand, after a /pre-spec of a session whose Cases case-guppi built with .claude/agents/case-guppi.md rendered from a Render of rule-case-build that asks, for a claim about code, for each function called on the way and the place where the caller takes the input: the findings of ask-guppi at that /pre-spec read for a claim of a Case about what code of the repository does that its context does not back by the functions it read — the deciding function, each function it calls on the way and the place where its caller takes the input — the count in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the functions called on the way and the source of the input are read too, and a name or a docstring is no reading`
> - [ ] update `insight-case-build-claims-what-code-does-without-reading-it`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-926
>     ```
>   - change: `actioned again: case-guppi reads each function called on the way and where the caller takes the input, and takes no name or docstring for a reading (case 926)`
> - [ ] read `estimate-case-build-reads-the-code-it-states`

> **ratification:**
> ```
> - decision[case 926][update][rule-case-build]{ref:rule-case-build}
> - decision[case 926][update][estimate-case-build-reads-the-code-it-states]{ref:rule-case-build}
> - decision[case 926][update][insight-case-build-claims-what-code-does-without-reading-it]{ref:insight-case-build-claims-what-code-does-without-reading-it}
> ```
