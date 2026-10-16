## Case 871 — case-guppi reads the documentation of an outside tool before it recommends on it

> **context:**
> `case-guppi` sometimes recommends an option that rests on how a tool outside the repository behaves: what GitHub accepts, which file of settings pytest reads from the root of the repository. The agent has only the tools Read, Grep, Glob, Write and Edit, so it cannot read the documentation of such a tool, and no sentence of `rule-case-build` says what it does with such a fact. The fact is taken as given, the person ratifies the Case, and the fact proves false in Work Mode. `insight-case-build-rests-on-an-unchecked-fact-of-a-tool` clusters two lessons of this cause. In `lesson-case-build-recommended-an-unchecked-github-fact` the agent said in its round that it could not read whether GitHub accepts the built-in Actions account on the bypass list of a ruleset, recommended the option all the same, GitHub refused it with HTTP 422 in Work Mode, and Case 804 was built and ratified again. In `lesson-case-build-names-a-pytest-config-the-root-run-does-not-read` Case 823.1 put the pytest settings in the package's own settings file, while a run from the root reads the root `pyproject.toml`, and Work Mode added the same lines there. The person chose to action the Insight: `WebFetch` joins the tools of the agent, the agent reads the documentation of the tool before it recommends such an option and names the page in `context`, and where the documentation does not settle the fact the option says so and is not recommended. `/pre-spec` does not change, since `ask-guppi` has no tool to read the web either.
>
> The rule that governs the choice is `rule-agent-writing`, whose passage says "Name a real source or remove the claim"; an option recommended on a fact nobody read breaks it, and the new sentence keeps it. `rule-insights-schema` sets that an `update` actions an Insight and that `addressed_by` takes the bare slug `decision-case-871` (case 712). The Insight has no `deferred_by`, so no `{supersedes:...}` mark is needed, and its two `clustered` lessons go to the archive by the cascade of `generate`. No option of the rounds rests on whether a check passes, so no output of a check was read. Whether a call of `WebFetch` by the agent under `permissionMode: auto` runs with no prompt was not read; the reading at Retro reads the text of the rule only.
>
> In `rule-case-build`, read whole, three sentences speak of the behaviour. The sentence of case 690.1 keeps a fact of the prompt that the agent cannot read at its source out of the Case; it stays true. The sentence of cases 798.2 and 801 lets an option that rests on whether a check passes be recommended when its last output was not read; the new sentence follows it and leaves that case to it, and the `－` line of `then` says so. The `tools` line of the Render gains `WebFetch`. The `Purpose` of the page names no tools, so it stands. The new sentence speaks of tools outside the repository; Case 869 of this session adds a sentence on a claim about code of the repository, anchored on the sentence of case 785, and Case 868 a sentence anchored on the sentence of a reader that only goes red; their texts were read beside this one, and the anchors and the subjects differ. Cases 870 and 872 of this session also change `rule-case-build` and their files were not read; where one of them anchors a pair on the sentence of cases 798.2 and 801 or on the `tools` line, the two pairs must be read side by side.
>
> A Grep for `tools|WebFetch|documentation|outside` over `vault/wiki/estimates/estimate-case-build-*.md` printed `estimate-case-build-checks-the-finished-case.md` and `estimate-case-build-writes-the-case.md`. The first speaks of the person's answers outside the options, not of this change. The Criterion of `estimate-case-build-writes-the-case` says that the agent runs with the tools Read, Grep, Glob, Write and Edit and `permissionMode: auto`, so that it writes its file with no prompt in Plan Mode. That line stays true: those tools stand, and it promises the write of the file, not the whole list. The new Estimate `estimate-case-build-checks-a-fact-of-an-outside-tool` promises `WebFetch` among the tools, so the promise is not signed twice. `/pre-spec` found that a Criterion lifted from the `when` and `then` of this Case would ask, at the Retro of this session, for the rendered agent file and for the tool calls of an agent rendered from the new rule, which only the render after Retro and a later session produce. The person chose a reading at this Retro, so the Estimate writes its own Criterion under `sections`, bound to the Render of `rule-case-build` in the Spec, which that reading reads; the `when` and `then` of this Case stay the behaviour of the agent. A Grep for `Read, Grep, Glob, Write, Edit|WebFetch|outside tool` over `vault/wiki/`, `.claude/` and `.guppi/` printed `vault/wiki/backlog.md`, `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/insights/insight-case-build-rests-on-an-unchecked-fact-of-a-tool.md`. The agent file changes by the render, `backlog.md` is written again by `guppi backlog`, and the Insight is set `actioned` by this Case. `.guppi/tests/test_guppi_package.py` reads each file under `.claude/` and the live pages, and fails on the old commands and paths its `OLD_COMMANDS` and `OLD_PATHS` hold; the new texts hold none of them. A Glob `vault/**/*outside-tool*` printed nothing, so the slug of the new Estimate is free.

> **problem:**
> `case-guppi` recommends options that rest on how a tool outside the repository behaves, with no means and no duty to check that behaviour. The fact proves false only in Work Mode, after the person ratified the Case, and the Case is built and ratified again.

> **recommend:**
> - **What do we do with this Insight?**
>   - Recommended: (a) act on it: `WebFetch` joins the tools of `case-guppi`, which reads the documentation of the tool before it recommends an option that rests on it and gives the address of the page in `context`.
>   - Answer: agreed, (a).
> - **What if the documentation does not settle the fact?**
>   - Recommended: (a) the option's `**After:**` line and `context` say that the fact is not checked, and the option is not recommended; where each option rests on the fact, the round says so and the person decides.
>   - Answer: agreed, (a).
> - **Does `/pre-spec` check it too?**
>   - Recommended: (a) no, only `rule-case-build` changes.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) a new Estimate `estimate-case-build-checks-a-fact-of-an-outside-tool`, read at the Retro of this session.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`, which gains `WebFetch` and the sentence on a fact of an outside tool.
> **＋** `estimate-case-build-checks-a-fact-of-an-outside-tool`: the new Estimate of that sentence.
> **＋** `insight-case-build-rests-on-an-unchecked-fact-of-a-tool`: the Insight this Case actions.
> **＋** `rule-agent-writing`: the rule that a claim names a real source.
> **＋** `estimate-case-build-writes-the-case`: its Criterion names the tools of the agent, and stands.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, writes a round with an option that rests on how a tool outside the repository behaves, such as what a service accepts or which file of settings a test runner reads.

> **then:**
> Before it recommends that option, `case-guppi` reads that behaviour in the documentation of the tool by `WebFetch`, and the `context` of the Case gives the address of the page it read and what the page says of the fact.
> **＋** `WebFetch` stands among the tools of `.claude/agents/case-guppi.md`.
> **＋** Where the documentation it read does not settle the fact, the `**After:**` line of the option and the `context` say that the fact is not checked, and `case-guppi` does not recommend that option.
> **＋** Where each option of the question rests on that fact, the `➡️` line says that the fact is not checked and leaves the choice to the person.
> **－** An option that rests on whether a check passes stays with the reading of the last output of that check, as `rule-case-build` sets it.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `tools: Read, Grep, Glob, Write, Edit`
>   - new: `tools: Read, Grep, Glob, Write, Edit, WebFetch`
>   - old: `and the option may still be recommended (cases 798.2, 801).`
>   - new: `` and the option may still be recommended (cases 798.2, 801). Where an option rests instead on how a tool outside the repository behaves, such as what a service like GitHub accepts or which file of settings a test runner reads, read that behaviour in the documentation of the tool by `WebFetch` before you recommend the option, and give in `context` the address of the page you read and what it says of the fact; where the documentation you read does not settle the fact, the `**After:**` line of the option and `context` say that the fact is not checked, and you do not recommend that option, and where each option of the question rests on that fact, the `➡️` line says that the fact is not checked and leaves the choice to the person (as set in case 871). ``
>   - change: `case-guppi gains WebFetch and reads the documentation of an outside tool before it recommends an option that rests on how that tool behaves; an unsettled fact is said and its option not recommended (case 871)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-checks-a-fact-of-an-outside-tool`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether the Render of rule-case-build gives case-guppi WebFetch among its tools and tells it to read in the documentation of a tool outside the repository the behaviour an option rests on before it recommends that option, to give the address of the page in context, and not to recommend an option whose fact the documentation does not settle`
>   - method: `by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness, case-build]`
>   - sections.Criterion:
>     ```
>     When:
>     The Render of `rule-case-build` in `raw/<date>/<hi HHMM>/spec.md`, the text that `.claude/agents/case-guppi.md` is rendered from, is read at the Retro of the session that changes it.
>
>     Then:
>     Its `tools` line holds `WebFetch`.
>     **＋** It tells `case-guppi`, before it recommends an option that rests on how a tool outside the repository behaves, to read that behaviour in the documentation of the tool by `WebFetch` and to give in `context` the address of the page it read and what the page says of the fact.
>     **＋** It tells `case-guppi` that, where the documentation it read does not settle the fact, the `**After:**` line of the option and `context` say that the fact is not checked, and the option is not recommended.
>     **＋** It tells `case-guppi` that, where each option of the question rests on that fact, the `➡️` line says that the fact is not checked and leaves the choice to the person.
>     **－** It leaves an option that rests on whether a check passes to the reading of the last output of that check.
>     ```
> - [ ] read `estimate-case-build-checks-a-fact-of-an-outside-tool`
> - [ ] update `insight-case-build-rests-on-an-unchecked-fact-of-a-tool`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-871
>     ```
>   - change: `actioned: case-guppi gains WebFetch and reads the documentation of an outside tool before it recommends on it, in rule-case-build (case 871)`

> **ratification:**
> ```
> - decision[case 871][update][rule-case-build]{ref:rule-case-build}
> - decision[case 871][create][estimate-case-build-checks-a-fact-of-an-outside-tool]{ref:rule-case-build}{tags:session,workflow,harness,case-build}
> - decision[case 871][update][insight-case-build-rests-on-an-unchecked-fact-of-a-tool]{ref:insight-case-build-rests-on-an-unchecked-fact-of-a-tool}
> ```
