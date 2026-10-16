## Case 872 — Cases built at the same time read no sibling mid-build

> **context:**
> The main agent often sends two or more Cases to their `case-guppi` at once: the first build of a batch, the answers of a batch, and the loop after the findings of `/pre-spec`. Each `case-guppi` reads the case files of the related Cases whenever it gets to them. If a sibling Case is still being built, it reads the half-done text and takes it for the result. `insight-subagents-read-a-sibling-mid-flight` clusters two lessons of this cause. In session 0104 the `case-guppi` of Case 843 read `case-846.md` before the rebuild of Case 846 ended. Case 843 then kept an `**Other Case:**` line that asked for a reading the finished `case-846.md` already held (`lesson-case-build-reads-a-sibling-case-file-mid-rebuild`). In session I of 2026-09-12 four agents edited one working tree at once, and each saw the tests red mid-run on files it had not touched (`lesson-subagents-parallel-on-one-tree-red-mid-flight`). The person chose to action the Insight. During a joint send, a `case-guppi` reads no file of a Case built at the same time. Its summary names the siblings its Case rests on on a `**Sibling:**` line. Once every `case-guppi` has answered, each Case with such a line goes back alone, one after another, to read the finished files. That pass runs once. By the person's words in this session, the main agent also asks the person no question on an `**Other Case:**` line in Plan Mode: it sends the other Case back by itself, and the person agrees or not at its showing. The Insight's own proposal had the main agent check the cross-references itself. It was not taken, since `rule-orchestration` has the main agent write from the summary without reading a case file (case 645.6). The second lesson stays out of the Case: `rule-work-mode` already runs `uv run --project .guppi guppi test` in full once after the last task, against the baseline, and its `Purpose` leaves subagents in Work Mode undecided (case 479.2).
>
> The rules that govern the choice are `rule-ratification`, whose atomicity rule splits the three parts, since each can fail alone and needs its own fix, and `rule-orchestration`, by which the main agent reads no case file, so the second pass is found from the summary. The `**Sibling:**` line is judged by no code. `summary_names` and `summary_findings` of `.guppi/guppi/casecheck.py`, read whole, read only the `**Built:**` and `**Case:**` lines of a summary, so a new line passes the check. A Grep `Other Case|whether that other Case|whether another Case` over `.guppi/guppi/` printed nothing, so no code judges the `**Other Case:**` line either. `rule-case-check` compares a case file with the other Cases of the session from the plan file and the store, the texts its check stored, so this Case does not change it. No option rests on a check passing.
>
> In `rule-case-build`, read whole, these sentences state the behaviour. The sentence of case 579.2 has the agent read the case file of each Case the prompt names. It stays, and the new sentence of Case 872.1 follows it and sets the exception for a Case built at the same time. The sentence of cases 637.2 and 645.1 says that the main agent asks the person whether the other Case is built again. Case 872.3 changes it. In `rule-orchestration`, read whole, three passages set the question on an `**Other Case:**` line: the showing of a summary, the list of questions the main agent puts itself, and the batch paragraph. Case 872.3 changes the first two, and Case 872.5 the third. The description of the summary gains the `**Sibling:**` line in Case 872.2, and the joint send and the second pass join the end of the batch paragraph. The dispatch sentence of case 684.2, which names each other Case of a batch by the path of its case file where it stands, stays true. In `rule-prespec`, step 2 sends the findings in one message and step 6 starts the confirmation of `ask-guppi`. Case 872.2 changes both.
>
> A Grep `Other Case` over `vault/wiki/` printed `orchestration.md`, `log.md`, `lessons/lesson-case-build-reads-a-sibling-case-file-mid-rebuild.md`, `insights/insight-subagents-read-a-sibling-mid-flight.md`, `rules/rule-case-build.md`, `estimates/estimate-orchestration-signs-items-taken-together.md`, `estimates/estimate-case-build-writes-the-case.md`, `estimates/estimate-orchestration-shows-the-built-case.md` and `rules/rule-orchestration.md`. `orchestration.md` changes by the render. `log.md` is not read. The lesson and the Insight are records this Case closes. The line of `estimate-case-build-writes-the-case` says that `case-guppi` writes the `**Other Case:**` line, which stays true, and Case 870 replaces that Criterion. The Criteria of `estimate-orchestration-shows-the-built-case` and `estimate-orchestration-signs-items-taken-together` promise the question. Case 872.3 replaces the first and Case 872.5 the second, each whole under `sections`, and each sets the `method` anew to wait for the next such line, since both methods read only the old promise. The check of this file notes the line of each Criterion on the question, and the line of the first on what the main agent writes from the summary, as not carried: each is rewritten, not dropped. The check found two promises in Case 872.3 when both Estimates stood under it, so the batch side is Case 872.5. The check notes `then` lines of Case 872.5 that share most of their words with Case 872.3. Case 872.3 sets the send of the other Case at the showing of any summary, and Case 872.5 sets it in the list of the rounds of a batch, each under its own Estimate. The check also notes `then` lines of Cases 872.2, 872.4 and 872.7 that share most of their words with Case 872.1. They state the hold-off from four sides — what `case-guppi` does, what the main agent sends, the reading by need and the check of the finished Case — and do not sign one promise twice: Cases 872.4 and 872.7 point at the Estimate of Case 872.1. A Grep `whether (that|another|the) (other )?Case is built again|another Case is built again` over `vault/wiki/` also printed `estimates/estimate-orchestration-asks-in-the-grill-me-shape.md`, besides `orchestration.md`, `rules/rule-case-build.md`, `rules/rule-orchestration.md` and the two Estimates above. Its Criterion lists that question, and its `purpose` names it, with no bound to Work Mode, while the new Render holds it in Work Mode only (a finding of `ask-guppi` at `/pre-spec`). Case 872.6 replaces that Criterion whole and sets its `purpose` anew. It also sets its `method`, which waited for a later session, to read the new Render at the Retro of this session. The check notes that Criterion's line on the question as not carried: it is rewritten, bound to Work Mode, not dropped. A Grep `Other Case` over `.claude/` printed `.claude/agents/case-guppi.md`, which changes by the render.
>
> A Grep `case file of each Case|caller's prompt names|related to the item` over `vault/wiki/estimates/` printed `estimate-case-build-reads-by-need-and-in-parts.md`. Its Criterion says that `case-guppi` reads whole the case file of each Case the prompt names, which Case 872.1 makes false for a Case built at the same time. So Case 872.4 replaces it whole, with one `－` line added that points at the new Estimate of Case 872.1. The person chose three parts; the check of this file found the update of that Estimate a second promise inside Case 872.1, so it stands as a sub-case of its own, which sets no new behaviour. Its `purpose` and `method` stand, since they speak of the related Cases in general and of a reading of the Render. `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-orchestration-batches-cases-out-at-once`, `estimate-prespec-gathers-the-answers-after-findings` and `estimate-prespec-confirms-the-findings-once` speak of joint sends. Their Criteria stay true: the prompt still names the Cases, the Cases still go out together, and the confirmation still waits until every `case-guppi` has answered. So they stand, and the new Estimates of Cases 872.1 and 872.2 check the change.
>
> A Grep `orchestration\.md|case-guppi\.md|pre-spec/SKILL|rule-orchestration|rule-prespec\b|rule-case-build` over `.guppi/tests/` printed `test_prespec.py`, `test_orchestration.py` and `test_config.py`. `test_orchestration.py` reads the two examples of `orchestration.md`, which this Case leaves as they are. The other two only name a rule in a docstring or a string. `.guppi/tests/test_guppi_package.py` reads every file under `.claude/` and the live pages, and fails on the strings of `OLD_COMMANDS` and `OLD_PATHS` (a Grep `OLD_COMMANDS|OLD_PATHS` over it). The new texts hold none of them. A Glob `vault/**/*{sibling,joint-send}*` printed `estimates/estimate-case-check-notes-a-then-line-shared-by-siblings.md`, the Insight and the lesson, so both new slugs are free.
>
> The findings of `ask-guppi` at `/pre-spec` shaped this build too. A sibling's case file never stands in `given`, since the frame paragraph of `rule-case-build` reads each file `given` names; it is named in `context` and on the `**Sibling:**` line only. Case 870 rests on the same frame paragraph, since its new Criterion of `estimate-case-build-writes-the-case` keeps the line that `case-guppi` reads each page and file `given` names. That line stays true with this Case, as no sibling's file stands in `given`; the main agent passed that point on to Case 870. Where the other Case that an `**Other Case:**` line names answers with a round, as Case 870 lets a `case-guppi` do, the round goes into the list of the batch. Step 5 of `rule-prespec` is a joint send too, so it names the siblings as step 2 does. `estimate-case-build-checks-the-finished-case` holds the new text against each Case the prompt names, and `estimate-orchestration-signs-a-batch-together` shows a batch once every answer is in. Cases 872.7 and 872.8 replace those Criteria, and each adds one `－` or `＋` line that points at the Estimate of Case 872.1 or Case 872.2. Their `purpose` and `method` speak of the Cases of the session in general and of a reading of the Render, so they stand. Each replaced Criterion is a promise of its own, so it stands in a sub-case of its own.
>
> Cases 868, 869, 870 and 871 of this batch change `rule-case-build`. Their files were read after their first builds ended. In this rebuild they are built at the same time, so their files were not read again, and the summary names them on a `**Sibling:**` line. Their anchors are the sentence on a reader that only goes red, the sentence of case 785, the sentence of case 725.1, and the `tools` line with the sentence of cases 798.2 and 801. The anchors of this Case are the sentence of case 579.2 and the sentence of cases 637.2 and 645.1, so no pair overlaps. The Insight leaves the backlog by an `update` to `actioned` with `addressed_by: decision-case-872.1`, as `rule-insights-schema` sets it (case 712). It has no `deferred_by`, so no `{supersedes:...}` mark is needed. Its `clustered` lessons go to the archive by the cascade of `generate`.

> **problem:**
> Agents that run at the same time read files that a sibling agent is still writing. A Case then rests on a sibling's half-done text. And the person gets a separate question just to pass a change from one Case to another.

> **recommend:**
> - **What to do with the Insight**
>   - Recommended: (a) during a joint send, `case-guppi` reads no file of a Case built at the same time; once all have answered, each Case that points at a sibling goes back once to read the finished file.
>   - Answer: agreed, (a).
> - **One promise or two parts**
>   - Recommended: (a) two sub-cases, one on `rule-case-build` and one on `rule-orchestration` and `rule-prespec`.
>   - Answer: not answered; replaced by the question One promise or several parts, after the person's words on the question round for another Case.
> - **One promise or several parts**
>   - Recommended: (a) three sub-cases: the build during a joint send, the second pass of the main agent, and the send of another Case with no question.
>   - Answer: agreed, (a).
> - **Which joint sends it covers**
>   - Recommended: (a) every time Cases are out together, the first build of a batch included.
>   - Answer: agreed, (a).
> - **Agents that edit one working tree in Work Mode**
>   - Recommended: (a) leave Work Mode out; `context` says that the full test run after the last task covers that lesson.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) a new Estimate for the hold-off and one for the second pass, read after the next joint send; the two Estimates that promise the question have their Criteria replaced whole.
>   - Answer: agreed, (a).
> - **Where the question about another Case goes away**
>   - Recommended: (a) everywhere in Plan Mode: the main agent sends the other Case back by itself, and the person agrees or not at its showing; Work Mode stays as it is.
>   - Answer: agreed, (a). The person had said that a separate round only to pass information between Cases is bad, and that the agent should handle it.
> - **How the main agent knows which Case points at a sibling**
>   - Recommended: (a) a new summary line `**Sibling:**` from `case-guppi`, naming each Case of the send whose file it did not read and on which its Case rests.
>   - Answer: agreed, (a).
> - **How the second pass runs**
>   - Recommended: (a) one Case after another, once, with no further loop; then an `**Other Case:**` line that still stands sends its Case back with no question.
>   - Answer: agreed, (a).

### Case 872.1 — case-guppi reads no file of a Case built at the same time

> **given:**
> `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.
> **＋** `estimate-case-build-reads-no-sibling-file-mid-send`: the new Estimate of the hold-off.
> **＋** `insight-subagents-read-a-sibling-mid-flight`: the Insight this Case actions.
> **＋** `rule-case-check`: the check of the file of a Case, whose findings may name another Case.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case from a prompt or a message that names another Case of the session as built at the same time.

> **then:**
> `case-guppi` reads no case file of that other Case in that build, though the prompt or a finding of the check of `rule-case-check` names it.
> **＋** It names no case file of that other Case in `given`, so the frame it reads holds none.
> **＋** It bounds its Case by the sentence the prompt gives on that other Case.
> **＋** Where its Case rests on that other Case — a claim of `context` or a line `**Other Case:**` — its `context` names that Case, and the item of its Case in the summary carries a line `**Sibling:**` that names it.
> **＋** Sent a later message that says that the build of that Case has ended, it reads the finished case file whole and fixes its Case against it.
> **－** A Case of the session that no prompt or message names as built at the same time it reads as before.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `and read your new text of that page beside its text and fix a contradiction between them (case 579.2).`
>   - new: `` and read your new text of that page beside its text and fix a contradiction between them (case 579.2). Where the prompt or a message names a Case as built at the same time as yours, read no file of that Case in this build, though this paragraph or a finding of the check names it, and name no file of it in `given`, so that the frame you read holds none: bound your Case by the sentence the prompt gives on that Case, and where your Case rests on it — a claim of `context` or a line `**Other Case:**` — name that Case in `context` and write under the item of your Case in the summary a line `**Sibling:**` that names each such Case; when a later message says that the build of that Case has ended, read its finished file whole and fix your Case against it, as this paragraph sets it for a Case of the session (as set in case 872.1). ``
>   - change: `case-guppi reads no file of a Case built at the same time, names the Cases its Case rests on in a Sibling line, and reads their finished files when their build has ended (case 872.1)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-reads-no-sibling-file-mid-send`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi reads no case file of a Case that its prompt or a message names as built at the same time and names none in given, names in context and in a Sibling line of its summary each such Case its Case rests on, and reads the finished file whole once a message says that build has ended`
>   - method: `by hand, after the first send of two or more Cases to case-guppi at the same time under the new Render of rule-case-build: the tool calls and the summary of each case-guppi of that send read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness, case-build]`
> - [ ] read `estimate-case-build-reads-no-sibling-file-mid-send`
> - [ ] update `insight-subagents-read-a-sibling-mid-flight`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-872.1
>     ```
>   - change: `actioned: Cases built at the same time read no sibling file mid-build, and a second pass reads the finished files, in rule-case-build, rule-orchestration and rule-prespec (case 872)`

> **ratification:**
> ```
> - decision[case 872.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 872.1][create][estimate-case-build-reads-no-sibling-file-mid-send]{ref:rule-case-build}{tags:session,workflow,harness,case-build}
> - decision[case 872.1][update][insight-subagents-read-a-sibling-mid-flight]{ref:insight-subagents-read-a-sibling-mid-flight}
> ```

### Case 872.4 — The reading by need leaves out a Case built at the same time

> **given:**
> `estimate-case-build-reads-by-need-and-in-parts`: its Criterion is replaced whole.
> **＋** `estimate-case-build-reads-no-sibling-file-mid-send`: the Estimate of the hold-off, which the replaced Criterion points to.
> **＋** `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.

> **when:**
> The main agent dispatches `case-guppi` by `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, or sends it a message by `SendMessage`.

> **then:**
> `case-guppi` reads whole the case file of each Case of the session that the prompt of its call names, and of each Case of the session that the check of its file names in a finding or a note.
> **－** The case file of a Case that the prompt or a message names as built at the same time it does not read in that build, as `estimate-case-build-reads-no-sibling-file-mid-send` checks.

> **tasks:**
> - [ ] update `estimate-case-build-reads-by-need-and-in-parts`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     The main agent dispatches `case-guppi` by `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, or sends it a message by `SendMessage`.
>
>     Then:
>     `case-guppi` reads `vault/wiki/case-example.md` once in a dispatch, just before its first `Write` of the file of a Case.
>     **＋** It reads whole each page the Case changes and the Criterion of each Estimate such a page lists.
>     **＋** It reads in parts, by a Grep with lines of context or a Read with `offset` and `limit`, the case file of a Case of an earlier session, the brief and the handoff of the session, a page it reads only for background, and a module of code, of which it reads the functions the Case changes and the places that call them.
>     **＋** It reads whole the case file of each Case of the session that the prompt of its call names, and of each Case of the session that the check of its file names in a finding or a note.
>     **＋** It makes the tool calls that do not wait on each other's output in one turn.
>     **＋** `.claude/agents/case-guppi.md` sets the cache of the agent to live one hour, by `cacheTtl: "1h"` under `experimental`.
>     **－** A dispatch that answers only with rounds does not read `vault/wiki/case-example.md`.
>     **－** The case file of a Case that the prompt or a message names as built at the same time it does not read in that build; it reads that file whole only after a later message says that the build of that Case has ended, as `estimate-case-build-reads-no-sibling-file-mid-send` checks.
>     ```
>   - change: `the Criterion replaced whole — the case file of a Case built at the same time is read only after its build has ended`
> - [ ] read `estimate-case-build-reads-by-need-and-in-parts`

> **ratification:**
> ```
> - decision[case 872.4][update][estimate-case-build-reads-by-need-and-in-parts]{ref:rule-case-build}
> ```

### Case 872.2 — The main agent re-sends a Case that rests on a sibling, once, one at a time

> **given:**
> `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `rule-prespec`: the rule of `/pre-spec`, rendered into `.claude/skills/pre-spec/SKILL.md`.
> **＋** `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`: the new Estimate of the second pass.
> **＋** `rule-case-build`: the rule that has `case-guppi` write the `**Sibling:**` line.
> **＋** `rule-case-check`: the check of the file of a Case.

> **when:**
> The main agent sends two or more Cases of the session to their `case-guppi` at the same time — the dispatch of a batch, the answers of a batch sent back, or the loop after the findings of `/pre-spec` — with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The prompt or message to each `case-guppi` names each other Case of that send as built at the same time.
> **＋** Once every `case-guppi` of the send has answered with its Case, the main agent sends back each Case whose item in the summary carries a line `**Sibling:**`, one at a time, each after the one before has answered, with a message that the build of each Case that line names has ended.
> **＋** The second pass runs once, and the Cases of the send are shown after it, together, for one ratification.
> **＋** In the loop after the findings of `/pre-spec`, the second pass comes before the `ask-guppi` runs confirm their findings.
> **－** A Case whose summary carries no line `**Sibling:**` does not go back in the second pass.
> **－** The main agent reads no case file to find the Cases of the second pass.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` should change instead, a line `**Other Case:**` — and the main agent writes the reply ``
>   - new: `` should change instead, a line `**Other Case:**`, and, when its Case rests on a Case built at the same time whose file it did not read, a line `**Sibling:**` that names that Case — and the main agent writes the reply ``
>   - old: `and every Case of the batch is shown in one reply (case 730.1).`
>   - new: `` and every Case of the batch is shown in one reply (case 730.1). When the main agent sends two or more Cases to their `case-guppi` at the same time — the dispatch of a batch, the answers of a batch sent back, or the loop after the findings of `/pre-spec` — its prompt or message to each names each other Case of that send as built at the same time, so that `case-guppi` reads no file of it in that build (as set in case 872.2). Once every `case-guppi` of the send has answered with its Case, the main agent takes one second pass: it sends back each Case whose item in the summary carries a line `**Sibling:**`, one at a time, each after the one before has answered, with a message that the build of each Case that line names has ended, so that its `case-guppi` reads the finished files and fixes its Case against them (as set in case 872.2). The second pass runs once, a clash it leaves is left to the check of the file of `rule-case-check` and to `/pre-spec`, and the Cases of the send are shown after it, together, for one ratification (as set in case 872.2). ``
>   - change: `Cases sent at the same time name each other as built at the same time, and a second pass, one Case at a time, sends back each Case whose summary carries a Sibling line (case 872.2)`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] update `rule-prespec`
>   - old: `` to the `case-guppi` of that Case by `SendMessage`, all of them in one message. ``
>   - new: `` to the `case-guppi` of that Case by `SendMessage`, all of them in one message, and name in each `SendMessage` the other Cases you send in that message as built at the same time, as `vault/wiki/orchestration.md` sets it (as set in case 872.2). ``
>   - old: `` 5. Send each answer to the `case-guppi` of its Case, all in one message, ``
>   - new: `` 5. Send each answer to the `case-guppi` of its Case, all in one message, naming in each `SendMessage` the other Cases you send in that message as built at the same time, ``
>   - old: `` 6. Send each `ask-guppi` run whose findings sent a Case back the Cases built again on them, ``
>   - new: `` 6. Once every `case-guppi` you sent has answered with its Case, first take the second pass that `vault/wiki/orchestration.md` sets for Cases sent at the same time, one Case at a time (as set in case 872.2). Then send each `ask-guppi` run whose findings sent a Case back the Cases built again on them, ``
>   - change: `the Cases sent back after the findings and with the answers name each other as built at the same time, and the second pass of orchestration.md comes before the confirmation of ask-guppi (case 872.2)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] create `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the main agent names the Cases it sends to case-guppi at the same time as built at the same time, and, once all have answered, sends back each Case whose summary carries a Sibling line, one at a time and once, before the Cases are shown together`
>   - method: `by hand, after the first send of two or more Cases to case-guppi at the same time under the new Render of rule-orchestration: the prompts and messages of the main agent from that send to the showing of its Cases read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow]`
> - [ ] read `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`

> **ratification:**
> ```
> - decision[case 872.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 872.2][update][rule-prespec]{ref:rule-prespec}
> - decision[case 872.2][create][estimate-orchestration-rechecks-a-sibling-after-a-joint-send]{ref:rule-orchestration}{tags:session,workflow}
> ```

### Case 872.3 — The main agent sends another Case back with no question

> **given:**
> `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `rule-case-build`: the rule of `case-guppi`, which says what follows an `**Other Case:**` line.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of a round, which goes into the list of a batch.

> **when:**
> In Plan Mode, a summary of `case-guppi` carries a line `**Other Case:**` under the item of a Case, with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The main agent asks the person no question whether the other Case is built again.
> **＋** It sends the other Case to its `case-guppi` by `SendMessage` with the change the line names, and the two Cases are shown together in a batch.
> **＋** In a send of Cases built at the same time it does so after the second pass, so that a line the finished file of a sibling already answers is dropped first.
> **＋** The person agrees or not at the showing of the other Case built again.
> **＋** Where the `case-guppi` of the other Case answers with a round instead of its Case, the round stands in the list of the rounds of the batch, as any round does, and the other Case is shown once it is built.
> **－** In Work Mode the main agent still asks the person whether the other Case changes, and the change takes the way of Work Mode.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` is shown as it stands, and the main agent asks the person, in the shape of a question it puts itself, whether that other Case is built again, and on the person's yes sends it to its `case-guppi` by `SendMessage`, in a batch when it is ratified, as `## Showing and signing a Case` sets it (case 629.1); in a batch of items the person took up together, the question stands in the list of the batch before any Case of it is shown (case 684.1); ``
>   - new: `` is shown as it stands; in Plan Mode the main agent asks the person no question on it and sends that other Case to its `case-guppi` by `SendMessage` with the change the line names, in a batch, as `## Showing and signing a Case` sets it, after the second pass of a send of Cases built at the same time where one runs, so that a line the finished file of a sibling answers is dropped first, and the showing of the other Case built again is where the person agrees or not, and where its `case-guppi` answers with a round instead, the round stands in the list of the rounds of the batch, as any round does; in Work Mode it asks the person, in the shape of a question it puts itself, whether that other Case changes, and on the person's yes the change takes the way of Work Mode that `## Showing and signing a Case` sets (cases 629.1, 684.1, 872.3); ``
>   - old: `the question whether another Case is built again after a clash (case 629.1),`
>   - new: `the question in Work Mode whether another Case changes after a clash (cases 629.1, 872.3),`
>   - change: `in Plan Mode an Other Case line raises no question: the main agent sends the other Case back by itself, and the person agrees or not at its showing (case 872.3)`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] update `rule-case-build`
>   - old: `` and again on a line `**Other Case:**` under the item of your Case in the summary; the main agent asks the person whether that Case is built again (cases 637.2, 645.1). ``
>   - new: `` and again on a line `**Other Case:**` under the item of your Case in the summary; in Plan Mode the main agent sends that Case back to its `case-guppi` with that change, with no question to the person, and in Work Mode it asks the person first (cases 637.2, 645.1, 872.3). ``
>   - change: `in Plan Mode the main agent sends the Case an Other Case line names back with no question to the person (case 872.3)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set:
>     ```
>     status: pending
>     method: "by hand at the Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion; after the first summary of case-guppi in Plan Mode that carries a line Other Case under that Render: the replies of the main agent from that summary to the showing of the other Case read against the Criterion, recorded in the estimate line"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
>     **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
>     **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
>     **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.
>
>     Then:
>     The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
>     **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
>     **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
>     **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
>     **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
>     **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands. In Plan Mode the main agent asks the person no question on it: it sends the other Case to its `case-guppi` by `SendMessage` with the change the line names, and the two Cases are shown together in a batch; in a send of Cases built at the same time it does so after the second pass that `vault/wiki/orchestration.md` sets. Where the `case-guppi` of the other Case answers with a round instead, the round stands in the list of the rounds of the batch, as any round does. In Work Mode it asks the person whether that other Case changes.
>     **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
>     **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
>     **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
>     **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
>     **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
>     **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
>     **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
>     **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
>     **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
>     **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
>     **－** The main agent writes the heading, the list, the `ratification` and the send of another Case from the summary, and does not read the file of the Case.
>     **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
>     **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
>     **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
>     **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
>     **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.
>     ```
>   - change: `the Criterion replaced whole — in Plan Mode an Other Case line raises no question, and the main agent sends the other Case back by itself`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 872.3][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 872.3][update][rule-case-build]{ref:rule-case-build}
> - decision[case 872.3][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```

### Case 872.5 — An Other Case line of a batch raises no question

> **given:**
> `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-signs-items-taken-together`: its Criterion is replaced whole.
> **＋** `/pre-spec`: the skill of `rule-prespec`, before which a batch of items taken up together runs.

> **when:**
> In Plan Mode before `/pre-spec`, a summary of a `case-guppi` of a batch carries a line `**Other Case:**`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The line raises no question to the person in the list of the rounds of the batch.
> **＋** The other Case it names goes back to its `case-guppi` with the change the line names and joins the batch, before any Case of the batch is shown.
> **＋** In a send of Cases built at the same time, this comes after the second pass.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` A question whether another Case is built again, which the line `**Other Case:**` of a summary of that batch raises, stands in the list of its rounds, numbered `<Case id>.Q<n>` under the Case that raised it, before any Case of the batch is shown, and on the person's yes that other Case goes back to its `case-guppi` and joins the batch (case 684.1). ``
>   - new: `` A line `**Other Case:**` of a summary of that batch raises no question to the person: the other Case it names goes back to its `case-guppi` with the change the line names and joins the batch, before any Case of the batch is shown, after the second pass of Cases sent at the same time where one runs (as set in case 872.5). ``
>   - change: `an Other Case line of a batch raises no question: the other Case joins the batch by itself (case 872.5)`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] update `estimate-orchestration-signs-items-taken-together`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the first batch of items taken up together in Plan Mode under the new Render of rule-orchestration in which a summary carries a line Other Case: the replies of the main agent from the dispatch of the batch to the reply that acknowledged it read against the Criterion, recorded in the estimate line"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     In Plan Mode before `/pre-spec`, one answer of the person takes up two or more items of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
>
>     Then:
>     The main agent dispatches a `case-guppi` for each item, and shows no round and no Case of them alone: they are one batch.
>     **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
>     **＋** It shows one list of every round that came back, each question numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
>     **＋** A line `**Other Case:**` in a summary of the batch raises no question to the person: the other Case it names goes back to its `case-guppi` with the change the line names and joins the batch, before any Case of the batch is shown.
>     **＋** Before it shows the Cases of the batch, it takes the second pass that `vault/wiki/orchestration.md` sets for Cases sent at the same time, as `estimate-orchestration-rechecks-a-sibling-after-a-joint-send` checks.
>     **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification. The person ratifies the batch at once or names the ids.
>     **－** An item the person takes up alone is shown alone, and the next item waits until its Case is ratified or deferred.
>     **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.
>     ```
>   - change: `the Criterion replaced whole — an Other Case line of a batch raises no question, and the other Case joins the batch by itself`
> - [ ] read `estimate-orchestration-signs-items-taken-together`

> **ratification:**
> ```
> - decision[case 872.5][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 872.5][update][estimate-orchestration-signs-items-taken-together]{ref:rule-orchestration}
> ```

### Case 872.6 — The question on another Case keeps the grill-me shape in Work Mode only

> **given:**
> `estimate-orchestration-asks-in-the-grill-me-shape`: its Criterion and `purpose` are replaced.
> **＋** `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the question shape.

> **when:**
> The main agent puts a question to the person itself in Work Mode, after a Case was bounded around a clash with another Case of the session, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The question asks whether that other Case changes, and takes the question shape of `.claude/skills/grill-me/SKILL.md`.
> **－** In Plan Mode no such question is put.

> **tasks:**
> - [ ] update `estimate-orchestration-asks-in-the-grill-me-shape`
>   - set:
>     ```
>     status: pending
>     purpose: Whether each question the main agent puts to the person itself, at pre-spec, at /hi, at a stop of Work Mode, in Work Mode after a clash on whether another Case changes, or at pre-spec on whether a finding of ask-guppi not closed is fixed or left, takes the question shape of grill-me, the exceptions kept in their own form
>     method: "by hand at the Retro of the session that changes it: the new Render of rule-orchestration in the Spec read against the Criterion, recorded in the estimate line"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     The main agent puts a question to the person itself, outside a round of `case-guppi`. The question is one of these:
>     - a decision it needs in the report of `/pre-spec`;
>     - a question at `/hi`;
>     - a question at a stop of Work Mode;
>     - in Work Mode, the question whether another Case of the session changes after a Case was bounded around a clash with it;
>     - at `/pre-spec`, after the `ask-guppi` runs confirm their findings, the question whether each finding not closed is fixed or left.
>
>     This is with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
>
>     Then:
>     Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
>     **＋** It stands in Russian, and its labels may stand translated.
>     **－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, the question whether to go on to `/pre-spec` when no line under `## Cases` is open, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.
>     **－** In Plan Mode the main agent puts no question whether another Case is built again after a clash.
>     ```
>   - change: `the Criterion replaced whole — the question on another Case after a clash stands in Work Mode only`
> - [ ] read `estimate-orchestration-asks-in-the-grill-me-shape`

> **ratification:**
> ```
> - decision[case 872.6][update][estimate-orchestration-asks-in-the-grill-me-shape]{ref:rule-orchestration}
> ```

### Case 872.7 — The finished Case is held against a sibling only after its build

> **given:**
> `estimate-case-build-checks-the-finished-case`: its Criterion is replaced whole.
> **＋** `estimate-case-build-reads-no-sibling-file-mid-send`: the Estimate of the hold-off, which the replaced Criterion points to.
> **＋** `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it, while its prompt or a message names another Case of the session as built at the same time.

> **then:**
> It holds its new text against the case file of that other Case only after a later message says that the build of that Case has ended.
> **－** Until then it does not name that case file in `given`.

> **tasks:**
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.
>
>     Then:
>     It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
>     **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
>     **＋** For each field, term or command whose behaviour the Case changes, it searches the live pages of the vault, leaving out the Decision pages, and `.claude/`, for its name, and reads each hit around its line, a row of `vault/wiki/glossary.md` and the Criterion of an Estimate included; each hit that the change makes false enters the Case, or its `context` says why it stands.
>     **＋** In each page the Case changes, which it has read whole, it lists each sentence that states the behaviour the change touches, judged by what the sentence says and not found by a search for the words of the sentence it changes, so that a sentence that states the same rule in other words is on the list; each sentence on that list that the change makes false enters the Case, or its `context` says why it stands.
>     **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
>     **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and of each Case of the session that the check of `rule-case-check` names in a finding or a note on its file, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
>     **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
>     **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
>     **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
>     **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
>     **＋** In a Case with sub-cases, it lists each behaviour, field and term that a sub-case sets, reads side by side every sentence of the new texts of all its sub-cases that speaks of it, whatever page each sub-case changes, and the Case holds no contradiction between them.
>     **－** A hit in a History line, in `log.md` or in `brief.md` is not read.
>     **－** The case file of a Case that the prompt or a message names as built at the same time it does not read in that build and does not name in `given`; it holds its new text against that file only after a later message says that the build of that Case has ended, as `estimate-case-build-reads-no-sibling-file-mid-send` checks.
>     ```
>   - change: `the Criterion replaced whole — the finished Case is held against a Case built at the same time only after its build has ended`
> - [ ] read `estimate-case-build-checks-the-finished-case`

> **ratification:**
> ```
> - decision[case 872.7][update][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}
> ```

### Case 872.8 — A batch of a ratified Case asked to change takes the second pass

> **given:**
> `estimate-orchestration-signs-a-batch-together`: its Criterion is replaced whole.
> **＋** `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`: the Estimate of the second pass, which the replaced Criterion points to.
> **＋** `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `/pre-spec`: the skill of `rule-prespec`, before which such a batch runs.

> **when:**
> In Plan Mode before `/pre-spec`, the person's answer to a round of a `case-guppi`, or the person's word on a shown Case, asks that a Case already ratified in the session change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> Before it shows the Cases of the batch, the main agent takes the second pass that `vault/wiki/orchestration.md` sets for Cases sent at the same time.

> **tasks:**
> - [ ] update `estimate-orchestration-signs-a-batch-together`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     In Plan Mode before `/pre-spec`, the person's answer to a round of a `case-guppi`, or the person's word on a shown Case, asks that a Case already ratified in the session change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
>
>     Then:
>     The main agent sends the ratified Case back to its `case-guppi` by `SendMessage`, and shows neither that Case nor the Case being built alone: the two are one batch.
>     **＋** A Case that a Case of the batch asks to change in the same way joins the batch.
>     **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
>     **＋** It shows one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
>     **＋** Before it shows the Cases of the batch, it takes the second pass that `vault/wiki/orchestration.md` sets for Cases sent at the same time, as `estimate-orchestration-rechecks-a-sibling-after-a-joint-send` checks.
>     **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
>     **＋** The person ratifies the batch at once or names the ids. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone only when no other Case of the session is out, or in a new batch with each Case it asks to change; while another Case is out, it is shown as `estimate-orchestration-batches-cases-out-at-once` sets it.
>     **－** Outside a batch and the loop after the findings of `/pre-spec`, the main agent does not take up the next item of `raw/<date>/<hi HHMM>/frontier.md` before the shown Case is ratified or deferred.
>     **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.
>     ```
>   - change: `the Criterion replaced whole — the batch takes the second pass before its Cases are shown`
> - [ ] read `estimate-orchestration-signs-a-batch-together`

> **ratification:**
> ```
> - decision[case 872.8][update][estimate-orchestration-signs-a-batch-together]{ref:rule-orchestration}
> ```
