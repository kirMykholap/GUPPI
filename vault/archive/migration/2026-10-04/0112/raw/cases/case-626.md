## Case 626 — ask-guppi answers /pre-spec in findings and the five lines answer whether a thing exists

> **context:**
> `ask-guppi` searches the vault for its caller. Its frame, `.claude/agents/ask-guppi.md`, rendered from `rule-ask`, tells it to answer every question in exactly five lines: `exists`, `near`, `missing`, `rules` and tags/slug. The main agent dispatches it at only one moment: once, at the first `/pre-spec` of a session. There the `/pre-spec` skill asks it three questions of another kind: which Case contradicts a page, a rule or another Case; which Estimate a Case does not name speaks of the thing the Case changes; and which fact of a `context` the vault does not bear out. The two texts pull apart, so the form of the answer changes from run to run. `estimate-ask-finds` failed in session 0004 (ledger line 17). Of the four dispatches it read, the answers of sessions 0317 and 1416 opened with numbered findings, and the answer of 0115 held nested lists under the five labels. Case 623 put the item off. The dispatch at the `/pre-spec` of session 0004 (transcript a17e0a5f), which that reading did not read, forced its findings into labels that do not fit. Its `exists` line said that no Case contradicts a page, and its `near` and `missing` lines held contradictions and wrong counts.
>
> The person chose to give `/pre-spec` a form of its own in the frame: one numbered list of findings under each of the three questions, in their order. Each finding names its Case and the page or Cases it bears on, and a question with no finding says "none". The five lines stay the answer to a question whether a thing exists. A list of the paths of the files read may still follow, as case 582 allows. The skill `/pre-spec` and `rule-prespec` stay as they are, so only the frame sets the form. The lines of the Criterion that no normal run exercises are moved to a new Estimate on `rule-ask`, `estimate-ask-query-before-a-create`. They cover a page asked about in either language, the rule a proposal crosses and the state of a slug in the archive. That Estimate is read where the query really runs: in the transcript of `case-guppi`, which runs the recipe itself before a `create` without a `ref`. `estimate-ask-finds` keeps only the dispatch at `/pre-spec`. Its Criterion is replaced whole, and its `purpose` and `method` are set anew, since both state the old promise. `estimate-case-build-writes-the-case` keeps its Criterion. Its line that `case-guppi` runs the query and gives the answer in `context` stays true, and the new Estimate checks the same behaviour from the side of the recipe.
>
> The pre-spec of this session found one more sentence of the frame that the new form left without a place. For a page that carries `deferred_by`, the frame tells the agent to give the `## Problem` of the deferring Decision on the `exists` or `near` line. At `/pre-spec` there is no such line. The person chose to put that Problem in the finding that names the page. A fourth replace pair in `rule-ask` says so, and a line of the new Criterion of `estimate-ask-finds` checks it.
>
> The check of this answer noted that the lines of the old Criterion of `estimate-ask-finds` are not carried word for word. That is on purpose, and each line has a new place:
> - The old `When`, any dispatch with a question, narrows to the dispatch at `/pre-spec`, the only one the main agent makes.
> - The old line on the five lines becomes the line on one numbered list under each question. The five lines leave this Criterion, since no dispatch asks whether a thing exists.
> - The lines on the list of paths, the event log and nothing else reaching the caller are carried, with "the findings" in place of "the five lines".
> - The line on the Grep of the rules is carried word for word.
> - The lines on a page asked in either language, a crossed rule, the state of a named slug, an archived page opened only when asked and the archive never searched by meaning move to 626.2. There they are worded for the `context` of the Case that `case-guppi` builds, not for the lines of an answer.
>
> The check also noted that 626.1 and 626.2 share the line on the Grep of the rules. That is on purpose: both run the same recipe, one when the main agent dispatches the agent at `/pre-spec` and one when `case-guppi` runs it itself. Each Estimate reads that line at its own moment.
>
> `rule-ask` carries `deferred_by` `decision-case-553`, and `backlog.md` lists `rule-ask`. That defer asked that `ask-guppi` and `case-guppi` read Decision pages by one rule. The frame of `case-guppi` now reads Decision pages only as `ask-guppi.md` allows, so both follow one rule already. The person chose to retire the defer with no change on that point. The decision line of 626.1 on `rule-ask` carries `{supersedes:case 553}`. Case 623 deferred `estimate-ask-finds` with a History line and no `deferred_by` field, and `backlog.md` does not list it. So, as in Case 624, no `{supersedes:case 623}` is written.
>
> Frame checks. A Grep of `five lines` over the repository outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` printed 5 files: `brief.md`, `.claude/agents/ask-guppi.md`, `log.md`, `estimate-ask-finds.md` and `rule-ask.md`. The hits in `brief.md` and `log.md` were not read. The other three are changed by 626.1. A Grep of `ask-guppi|ask_guppi` over `guppi/` printed nothing. In `tests/test_casecheck.py`, line 334 shows that the check of `rule-case-check` passes an answer of `ask-guppi` unjudged. So no code reads the form. The moment this Case sets is the answer of `ask-guppi` at `/pre-spec`. A Grep of `ask-guppi.{0,200}(answer|five|form|finding)` over `vault/wiki/rules/*.md` and `.claude/**` printed 4 files: `.claude/agents/case-guppi.md`, `rule-prespec.md`, `rule-orchestration.md` and `rule-case-build.md`. `rule-prespec` sets what to send `ask-guppi` and the main agent's own report, not the form of the agent's answer. `rule-orchestration` sets only that `ask-guppi` asks at `/pre-spec`. `rule-case-build` and `case-guppi.md` have `case-guppi` run the query itself, which keeps the five lines. Each stays true. `estimate-prespec-reconciles` names the three questions and not the form, and `estimate-case-build-checks-the-finished-case` counts what `ask-guppi` finds at `/pre-spec` without a form. Both Criteria stand. `rule-ask` lists only `estimate-ask-finds` in `estimates`. A Glob of `vault/**/estimate-ask-*.md` printed only `estimate-ask-finds.md`, so the new slug is free. Cases 624 and 625 of this session change none of these pages and set nothing at `/pre-spec`. The new Estimate has `ref: rule-ask`, so the vault query was not run.

> **problem:**
> The frame of `ask-guppi` requires five lines for every answer, while `/pre-spec`, the one moment the main agent dispatches it, asks for three kinds of findings. The answers swing between the two forms, and `estimate-ask-finds` fails on them. Its lines about a page asked in either language, a crossed rule and an archived slug wait for a dispatch that no normal run makes. The question is which form the answer takes at `/pre-spec`, and where the rest of the check is read.

> **recommend:**
> - **Which form the answer of ask-guppi takes at /pre-spec**
>   - Recommended: (a) a second form for `/pre-spec`: the frame keeps five lines for a question whether a thing exists and sets, for `/pre-spec`, numbered findings under the three questions, each naming its Case and page, "none" for a question with no finding, a file list allowed after; `rule-ask` and the Criterion of `estimate-ask-finds` change.
>   - Answer: agreed with the recommendation, (a).
> - **How the "does it exist" parts of the check get read**
>   - Recommended: (b) read them in the transcript of `case-guppi` when it runs the search itself before a `create`; `estimate-ask-finds` keeps only the dispatch at `/pre-spec`.
>   - Answer: agreed with the recommendation, (b).
> - **The question put off on rule-ask: may ask-guppi open Decision pages**
>   - Recommended: (a) close it as already settled: both agents now read Decision pages by the rule of `ask-guppi.md`; the change of `rule-ask` retires the defer, and nothing about Decision pages changes.
>   - Answer: agreed with the recommendation, (a).
> - **Where the "does it exist" lines of the check go**
>   - Recommended: (a) a new Estimate on `rule-ask`, `estimate-ask-query-before-a-create`, read by hand in a session where `case-guppi` builds a Case with a `create` without a `ref`.
>   - Answer: agreed with the recommendation, (a).
> - **Does the /pre-spec skill also state the form**
>   - Recommended: (a) the form lives in the frame of `ask-guppi` alone; `rule-prespec` and its Estimate stay.
>   - Answer: agreed with the recommendation, (a).
> - **Where the put-off question of a page goes in the /pre-spec answer**
>   - Recommended: (a) in the finding that names the page, by a second replace pair in `rule-ask`; the five-line answer keeps it on the `exists` or `near` line; one more line of the Criterion of `estimate-ask-finds` checks it.
>   - Answer: agreed with the recommendation, (a).

### Case 626.1 — ask-guppi answers /pre-spec with a numbered list under each question

> **given:**
> `rule-ask` — its Render is the text of `.claude/agents/ask-guppi.md`; four passages change
> **＋** `.claude/agents/ask-guppi.md` — the agent rendered from `rule-ask`
> **＋** `estimate-ask-finds` — the check whose Criterion is replaced whole and whose `purpose` and `method` are set anew
> **＋** `.claude/skills/pre-spec/SKILL.md` — sends `ask-guppi` the plan file and the three questions; unchanged
> **＋** `rule-prespec` — the main agent's report built from the findings; unchanged
> **＋** `vault/wiki/rules/` — the rule pages the agent greps first
> **＋** `vault/raw/<date>/event_log.md` — records each dispatch

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with one numbered list of findings under each question of `.claude/skills/pre-spec/SKILL.md`, in its order: what contradicts a page, a rule or another Case; an Estimate a Case does not name that speaks of the thing the Case changes; a fact of a `context` the vault does not bear out.
> **＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
> **＋** A finding that names a page carrying `deferred_by` gives the `## Problem` of the Decision that field names.
> **＋** After the findings a list of the paths of files the agent read may stand, as the general note of Claude Code asks of a sub-agent.
> **＋** The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
> **－** No index line, page text or other note reaches the caller beyond the findings and that list of paths.
> **－** An answer with no list after the findings holds the promise as well.

> **tasks:**
> - [ ] update `rule-ask`
>   - old: `for the caller and answer in five lines.`
>   - new: `for the caller and answer in one of the two forms set at the end.`
>   - old: `` give its `## Problem` on the `exists` or `near` line, ``
>   - new: `` give its `## Problem` on the `exists` or `near` line, or, at `/pre-spec`, in the finding that names the page, ``
>   - old: `Answer with exactly these five lines, each present, "none" when empty:`
>   - new: `To a question whether a thing exists — what is close, what is missing, which rule it crosses, which tags fit, whether a slug is free — answer with exactly these five lines, each present, "none" when empty:`
>   - old: `` - tags/slug: tags that fit, existing first; the named slug — `free`, `live` (with its category), or `archived at <path> by [[decision-case-N]]`, N from the page's `origin` ``
>   - new:
>     ````
>     - tags/slug: tags that fit, existing first; the named slug — `free`, `live` (with its category), or `archived at <path> by [[decision-case-N]]`, N from the page's `origin`
>
>     At `/pre-spec`, where the caller asks which Case of the plan contradicts a page of the vault, a rule of the vault or another Case, which Estimate a Case does not name speaks of the thing the Case changes, and which fact of a `context` the vault does not bear out, answer instead with one numbered list of findings under each question, in that order: each finding names its Case and the page or the Cases it bears on, and a question with no finding says "none" (case 626.1).
>     ````
>   - change: `ask-guppi answers /pre-spec with one numbered list of findings under each question, the Problem of a page's deferred_by in the finding that names the page; the five lines answer a question whether a thing exists; the defer of case 553 retired, both agents reading Decision pages by the rule of ask-guppi.md (case 626.1)`
> - [ ] update `estimate-ask-finds`
>   - set: `{status: pending, purpose: "Whether ask-guppi answers the questions of /pre-spec with one numbered list of findings under each question, each finding naming its Case and the page or Cases it bears on, a list of the paths of the files it read allowed after them", method: "by hand at the /hi of a later session: the answer of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 626.1, read in its agent transcript against the event log, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — the dispatch at /pre-spec answered by one numbered list of findings under each question, not by the five lines, the Problem of a deferred page in its finding; the lines on a page asked in either language, a crossed rule and an archived slug moved to estimate-ask-query-before-a-create (case 626.1)`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-ask-finds`

> **ratification:**
> ```
> - decision[case 626.1][update][rule-ask]{ref:rule-ask}{supersedes:case 553}
> - decision[case 626.1][update][estimate-ask-finds]{ref:rule-ask}
> ```

### Case 626.2 — The vault query that case-guppi runs is checked by an Estimate of its own

> **given:**
> `rule-ask` — the recipe of the vault query, the target of the new Estimate
> **＋** `.claude/agents/ask-guppi.md` — the recipe as rendered
> **＋** `.claude/agents/case-guppi.md` — runs the query itself before a `create` without a `ref`
> **＋** `vault/wiki/rules/` — the rule pages the query greps first
> **＋** `vault/archive/` — where a named slug is checked by Glob
> **＋** `estimate-ask-query-before-a-create` — the new Estimate
> **＋** `estimate-case-build-writes-the-case` — already checks that the query runs and its answer stands in `context`; unchanged

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> It starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** A page that already holds the thing is found by meaning, whether the person's words name it in Russian or in English, and the `context` of the Case names its slug.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
> **＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
> **＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
> **－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.

> **tasks:**
> - [ ] create `estimate-ask-query-before-a-create`
>   - type: `estimate`
>   - ref: `rule-ask`
>   - kind: `QA`
>   - purpose: `Whether the vault query that case-guppi runs before a create without a ref, by the recipe of ask-guppi, starts with the rules, finds an existing page by meaning in either language, and names the rule a proposal crosses and the state of a named slug`
>   - method: `by hand at the /hi of a later session: the transcript of a case-guppi that built a Case with a create without a ref after the render of .claude/agents/ask-guppi.md by case 626.1, its Grep and Glob calls and the context of its Case read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] read `estimate-ask-query-before-a-create`

> **ratification:**
> ```
> - decision[case 626.2][create][estimate-ask-query-before-a-create]{ref:rule-ask}{tags:session,workflow,harness}
> ```
