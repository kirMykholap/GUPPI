## Case 954 — The hook's refusal of ask-guppi is tested by a deliberate start

> **context:**
> The hook `guppi grepguard` of `.guppi/guppi/grepguard.py`, registered on `PreToolUse` of `Read` and of `Grep` in `.claude/settings.json`, refuses a Read of a Decision page and a Grep inside `vault/wiki/decisions/` when the payload names `ask-guppi` as `agent_type`. I read `before`, `searched_folder` and `refused` whole. `estimate-search-leaves-out-decisions-refuses-ask-guppi` checks it. Its `method` runs `test_grepguard.py`, then waits for a refused call in the transcript of `ask-guppi` after a `/pre-spec`. No such call came, since `.claude/agents/ask-guppi.md` tells the agent that it opens and greps no page under `vault/wiki/decisions/`. `decision-case-936` put the reading off for that reason, and `vault/wiki/backlog.md` lists the Estimate. The registration now stands in `.claude/settings.json`. The person chose a deliberate trial. The main agent starts `ask-guppi` and asks it, openly as a test of the hook, to make the two calls. `.claude/agents/ask-guppi.md` forbids that call, and the Render of `rule-search-leaves-out-decisions` says that the frame of `ask-guppi` names no reason for it. An `ask-guppi` that follows its frame would make no call, so, by the person's answer on a finding of `/pre-spec`, Case 954.3 gives the frame one reason to try the call: a trial of the hook that a ratified Case names, the call made to be refused and the page never read. The Claude Code hooks documentation at https://code.claude.com/docs/en/hooks says that hooks from settings files fire for the tool calls of a subagent, and that the input carries `agent_type`, the name of the subagent. The Render of `rule-orchestration` lets the main agent dispatch `ask-guppi` only at pre-spec, so Case 954.2 adds the one exception the person chose: a test by hand of a hook that judges a call of `ask-guppi` apart from the same call of another agent. A later session takes the trial as the Work reading of the Estimate, not as a task of this session, so, on a finding of `/pre-spec`, the exception covers a task of a ratified Case and the Work reading of an Estimate whose `method` a ratified Case set. The new texts reach the agents only at the librarian's render after this session, so every reading waits for the Work Mode of the session whose brief puts the reading of `estimate-search-leaves-out-decisions-refuses-ask-guppi` under Work, and this session runs the hook's tests and retires the defer. Each new `method` holds one part that opens with `by hand, after` and names its event before a colon, as `case-schema.md` allows (case 781), and the test part stands inside it, since an estimate line cannot hold half a reading. The hook and the promise of `estimate-search-leaves-out-decisions-refuses-ask-guppi` do not change, so Case 954.1 writes its Criterion back word for word as its `when` and `then`, and sets it `pending` with the new `method`, so that its `read` box has an Estimate to read, as `case-schema.md` sets for a `read` box. The mark `{supersedes:case 936}` retires the defer, and `estimate-backlog-renders` checks that the item leaves `vault/wiki/backlog.md` once its `deferred_by` is empty. A Grep of `refuses-ask-guppi` over `{vault/wiki/**,.claude/**,.guppi/**}` printed `brief.md`, `backlog.md`, `log.md`, `estimate-search-leaves-out-decisions-in-every-agent.md`, `estimate-ask-opens-a-decision-only-for-a-finding.md`, `rule-search-leaves-out-decisions.md`, `estimate-page-read-cuts-the-history.md`, `estimate-search-leaves-out-decisions-by-the-grep-hook.md` and `test_grepguard.py`. Each hit outside `brief.md`, `backlog.md` and `log.md` points to the Estimate as the check of the refusal or names it in a list, and stays true. The Criterion of `estimate-ask-opens-a-decision-only-for-a-finding` speaks of the run of `ask-guppi` at `/pre-spec` alone, so it stands. A Grep of ``dispatches `?ask-guppi`? only|ask-guppi`? only at|only at pre-spec|only at `/pre-spec` `` over `{vault/wiki/**,.claude/**,.guppi/**}` printed `orchestration.md`, `log.md`, `rule-orchestration.md` and `estimate-orchestration-shows-the-built-case.md`. The Criterion of `estimate-orchestration-shows-the-built-case`, on line 34 of its page, says that the main agent dispatches `ask-guppi` only at pre-spec. Case 950.2 of this session replaces that Criterion whole: its line on `ask-guppi` at pre-spec takes the exception of the start that `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads, and one `－` line leaves that start out of its promise, so the Criterion stays true beside Case 954.2. The sentence of the Render that `ask-guppi` asks the vault at `/pre-spec`, and line 21 of `estimate-orchestration-puts-the-harness-before-plan-mode`, speak of Plan Mode, so they stand. `.guppi/tests/test_orchestration.py` reads only the blocks tagged `showing` and `defer` of `vault/wiki/orchestration.md`, which this Case does not touch. A Glob `vault/**/estimate-orchestration-starts-ask-guppi*` printed nothing, so the new slug is free. For Case 954.3 I read `rule-ask` whole. Its Purpose and the `description` of its Render say that the main agent asks the vault at pre-spec, and they stand, since the trial asks the vault no question. The Criteria of `estimate-ask-finds`, `estimate-ask-query-before-a-create`, `estimate-ask-searches-at-prespec` and `estimate-ask-opens-a-decision-only-for-a-finding` speak of `/pre-spec` and of the query before a `create`, so they stand. The Criterion of `estimate-search-leaves-out-decisions-in-every-agent` says that the text of a Decision page reaches `ask-guppi` by no call, and the trial keeps that true, since the hook refuses the call. The Render line of `rule-search-leaves-out-decisions` that lets an agent read a Decision page only for a reason of its frame stands, since the trial reads no page. A Grep of `ask-guppi\.md|search-leaves-out-decisions\.md` over `.guppi/tests` printed one line, in the docstring of `test_grepguard.py`, so no test reads either rendered file live. A Glob `vault/**/estimate-ask-tries-a-decision-call*` printed nothing, so that slug is free too. A Grep of the session's ledger for `lesson\[error\]` and for `\{addresses:` printed nothing, so this Case closes no lesson of the session.

> **problem:**
> The hook that keeps `ask-guppi` out of the Decision pages was never seen to refuse a real call, since `ask-guppi` never makes one; the main agent may not start `ask-guppi` outside `/pre-spec` to make one on purpose, and the frame of `ask-guppi` names no reason to make one.

> **recommend:**
> - **What to do with the deferred reading**
>   - Recommended: (b) a test by hand in this session's Work Mode, method changed.
>   - Answer: agreed, (b).
> - **How the trial reaches `ask-guppi` outside `/pre-spec`**
>   - Recommended: (b) the Case also changes the sentence of `rule-orchestration`.
>   - Answer: agreed, (b).
> - **How the change to the rule is checked**
>   - Recommended: (a) a new check, read by the trial itself.
>   - Answer: agreed, (a).
> - **How wide the exception is**
>   - Recommended: (b) only a test of a hook that judges the calls of `ask-guppi` itself.
>   - Answer: agreed, (b).
> - **When the trial runs**
>   - Recommended: (a) the trial waits for the first Work Mode after that render.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, a finding that the frame of `ask-guppi` forbids the call the trial asks for, and that the rule says that frame names no reason for it; the person chose that Case 954 also changes the frame of `ask-guppi`, so that it names one reason to try such a call, the hook trial a ratified Case names, the call made to be refused and the page never read, with an Estimate of its own.
>   - Taken: Case 954.3 updates `rule-ask` and `rule-search-leaves-out-decisions` and creates `estimate-ask-tries-a-decision-call-only-for-a-hook-trial`.
> - **Change**
>   - Asked: at `/pre-spec`, findings that the exception allowed a task but not a Work reading, that an `update` of the `method` alone leaves the `read` box with nothing to read, that the `then` of Case 954.1 named a backlog reading its `method` does not take, and that the `method` of the new check of Case 954.2 named no session.
>   - Taken: the exception and the `when` of Case 954.2 cover the Work reading of an Estimate too; Case 954.1 writes its Criterion back word for word and sets it `pending`; each new `method` names the session whose brief puts the reading under Work.

### Case 954.1 — The refusal is read from a deliberate start of ask-guppi

> **given:**
> `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal; set `pending`, its Criterion written back, its `method` set anew and its defer retired.
> **＋** `ask-guppi` and `.claude/agents/ask-guppi.md`: the agent whose calls the hook refuses.
> **＋** `case-guppi`: an agent whose same call passes.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `.guppi/guppi/grepguard.py`: the hook, run by `uv run --project .guppi guppi grepguard`.
> **＋** `.claude/settings.json`: registers the hook on `PreToolUse` of `Read` and of `Grep`.
> **＋** `.guppi/tests/test_grepguard.py`: the tests of the hook.
> **＋** `rule-search-leaves-out-decisions`: the rule the hook enforces, named in its reason.

> **when:**
> `ask-guppi` calls Read with a `file_path` under `vault/wiki/decisions/`, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it, and `uv run --project .guppi guppi grepguard` of `.guppi/guppi/grepguard.py`, registered on `PreToolUse` of `Read` and of `Grep` in `.claude/settings.json`, reads the call with `agent_type` `ask-guppi`.

> **then:**
> The hook refuses the call by `permissionDecision: deny`, with a reason that names the path and `rule-search-leaves-out-decisions`, and exits 0; the call does not run.
> **＋** The same Read or Grep by the main agent, by `case-guppi` or by the librarian passes unchanged.
> **＋** A Read of `ask-guppi` outside `vault/wiki/decisions/` passes unchanged, and a Grep of `ask-guppi` over a folder that holds `vault/wiki/decisions/` gets the exclusion at the end of its `glob`, as for any agent.
> **－** A Glob of `ask-guppi` that prints the path of a Decision page passes: a path is no text of the page.
> **－** A payload the hook cannot read, or an error, lets the call pass, with one line on stderr.

> **tasks:**
> - [ ] update `estimate-search-leaves-out-decisions-refuses-ask-guppi`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the librarian's run that renders vault/wiki/orchestration.md, .claude/agents/ask-guppi.md and .claude/rules/search-leaves-out-decisions.md with the trial of this hook by a deliberate start of ask-guppi: uv run --project .guppi pytest .guppi/tests/test_grepguard.py, and, in the Work Mode of the session whose brief puts this reading under Work, the main agent starts ask-guppi with a prompt that names the trial and asks it to Read one named page under vault/wiki/decisions/ and to Grep inside that folder; each of the two calls in the transcript of ask-guppi read against the Criterion, both parts recorded in one estimate line"
>     ```
>   - change: `the Criterion written back unchanged; the method reads the refusal from a deliberate start of ask-guppi after the render of the hook trial; the defer retired (case 954.1)`
> - [ ] by hand, in Work Mode: `uv run --project .guppi pytest .guppi/tests/test_grepguard.py` passes.
> - [ ] read `estimate-search-leaves-out-decisions-refuses-ask-guppi`

> **ratification:**
> ```
> - decision[case 954.1][update][estimate-search-leaves-out-decisions-refuses-ask-guppi]{ref:rule-search-leaves-out-decisions}{supersedes:case 936}
> ```

### Case 954.2 — The main agent may start ask-guppi to test a hook that judges its calls

> **given:**
> `rule-orchestration`: one sentence of its Render changes.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-starts-ask-guppi-for-a-hook-test`: the new check of the exception.
> **＋** `.claude/agents/ask-guppi.md`: the agent the main agent starts.
> **＋** `rule-prespec`: sets the run of `ask-guppi` at `/pre-spec`; unchanged.

> **when:**
> In Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the main agent takes a task of a ratified Case, or the Work reading of an Estimate whose `method` a ratified Case set, that names a test by hand of a hook which judges a call of `ask-guppi` apart from the same call of another agent.

> **then:**
> The main agent starts `ask-guppi` through the Agent tool for that test, with a prompt that says the calls it asks for are a test of that hook.
> **＋** In Work Mode the main agent starts `ask-guppi` for no other reason.
> **－** A test of a hook that judges the calls of every agent alike starts no `ask-guppi`.
> **－** The run of `ask-guppi` at `/pre-spec` keeps the form that `rule-prespec` sets.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` the agent dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, and asks that run again only to confirm its own findings, as `rule-prespec` sets it (cases 634.3, 674.2). ``
>   - new: `` the agent dispatches `ask-guppi` at pre-spec, one run over the whole plan at its first run, and asks that run again only to confirm its own findings, as `rule-prespec` sets it (cases 634.3, 674.2). Outside pre-spec it dispatches `ask-guppi` only in Work Mode, where a task of a ratified Case, or the Work reading of an Estimate whose `method` a ratified Case set, names a test by hand of a hook that judges a call of `ask-guppi` apart from the same call of another agent, and only for that test, with a prompt that says the calls it asks for are a test of that hook (as set in case 954.2). ``
>   - change: `the main agent may start ask-guppi in Work Mode for a test by hand of a hook that judges its calls, named by a task or a Work reading (case 954.2)`
> - [ ] create `estimate-orchestration-starts-ask-guppi-for-a-hook-test`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the main agent starts ask-guppi outside pre-spec only in Work Mode, for a test by hand of a hook that judges its calls that a task of a ratified Case or a Work reading names, with a prompt that says the calls are a test of that hook`
>   - method: `by hand, after the librarian's run that renders vault/wiki/orchestration.md with the start of ask-guppi for a test of a hook that judges its calls: the Agent calls of the main agent in the Work Mode of the session whose brief puts the reading of estimate-search-leaves-out-decisions-refuses-ask-guppi under Work, in its transcript, read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-starts-ask-guppi-for-a-hook-test`

> **ratification:**
> ```
> - decision[case 954.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 954.2][create][estimate-orchestration-starts-ask-guppi-for-a-hook-test]{ref:rule-orchestration}{tags:session,workflow,harness}
> ```

### Case 954.3 — The frame of ask-guppi names the hook trial as its one Decision call

> **given:**
> `rule-ask`: two passages of its Render change.
> **＋** `.claude/agents/ask-guppi.md`: the frame of `ask-guppi`, rendered from `rule-ask`.
> **＋** `rule-search-leaves-out-decisions`: one line of its Render changes.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the file rendered from `rule-search-leaves-out-decisions`.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `estimate-ask-tries-a-decision-call-only-for-a-hook-trial`: the new check of the frame.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal itself.

> **when:**
> The main agent starts `ask-guppi`, which follows `.claude/agents/ask-guppi.md` rendered from `rule-ask` and `.claude/rules/search-leaves-out-decisions.md` rendered from `rule-search-leaves-out-decisions`, with a prompt that names a trial, named by a ratified Case, of the hook on `vault/wiki/decisions/`, and the Read and the Grep that the trial makes.

> **then:**
> `ask-guppi` makes the Read and the Grep that the prompt names, once each, and no other call on `vault/wiki/decisions/`.
> **＋** It answers with one line per call: the call and the reason of its refusal as the hook gave it, or, where the call ran, that it ran, with none of the text it printed.
> **－** Without such a trial in its prompt, the agent tries no call on the Decision folder.
> **－** Whether the hook refuses the call is outside this promise: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads it.

> **tasks:**
> - [ ] update `rule-ask`
>   - old: `` Run as the agent `ask-guppi`, you open and grep no page under `vault/wiki/decisions/`, and a hook refuses such a Read or Grep (as set in cases 925.1 and 925.4). ``
>   - new: `` Run as the agent `ask-guppi`, you open and grep no page under `vault/wiki/decisions/`, and a hook refuses such a Read or Grep; the one such call you make is the trial of that hook set at the end (as set in cases 925.1, 925.4 and 954.3). ``
>   - old: `` no summary of the findings and no list of what holds (case 633.1). ``
>   - new:
>     ````
>     no summary of the findings and no list of what holds (case 633.1).
>
>     Where the caller's prompt names a trial, named by a ratified Case, of the hook on `vault/wiki/decisions/`, make the Read and the Grep that the prompt names, once each, so that the hook refuses them, and try no other way to the text of the page. Answer with one line per call: the call and the reason of its refusal as the hook gave it, or, where the call ran, that it ran, with none of the text it printed (as set in case 954.3).
>     ````
>   - change: `the frame of ask-guppi names one call on vault/wiki/decisions/, the hook trial a ratified Case names, made to be refused, and its answer (case 954.3)`
> - [ ] update `rule-search-leaves-out-decisions`
>   - old: `` The frame of `ask-guppi` names no reason to read a Decision page, so the same hook, on `Read` and on `Grep`, refuses a Read of a Decision page and a Grep inside `vault/wiki/decisions/` made by `ask-guppi`, and leaves such a call of another agent unchanged (as set in case 925.1). ``
>   - new: `` The frame of `ask-guppi` names no reason to read a Decision page, and one reason to try such a call: a trial of the hook that a ratified Case names, the call made to be refused; so the same hook, on `Read` and on `Grep`, refuses a Read of a Decision page and a Grep inside `vault/wiki/decisions/` made by `ask-guppi`, and leaves such a call of another agent unchanged (as set in cases 925.1 and 954.3). ``
>   - change: `the frame of ask-guppi names the hook trial as its one reason to try a call on a Decision page (case 954.3)`
> - [ ] create `estimate-ask-tries-a-decision-call-only-for-a-hook-trial`
>   - ref: `rule-ask`
>   - kind: `QA`
>   - purpose: `Whether ask-guppi makes a Read or a Grep on vault/wiki/decisions/ only for a hook trial that a ratified Case names and its prompt names, once each, and answers with each refusal and none of the text of a page`
>   - method: `by hand, after the librarian's run that renders .claude/agents/ask-guppi.md and .claude/rules/search-leaves-out-decisions.md with the hook trial: the calls and the answer of ask-guppi in the trial of the session whose brief puts the reading of estimate-search-leaves-out-decisions-refuses-ask-guppi under Work, in its transcript, read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] `uv run --project .guppi guppi render`: `.claude/rules/search-leaves-out-decisions.md`
> - [ ] read `estimate-ask-tries-a-decision-call-only-for-a-hook-trial`

> **ratification:**
> ```
> - decision[case 954.3][update][rule-ask]{ref:rule-ask}
> - decision[case 954.3][update][rule-search-leaves-out-decisions]{ref:rule-search-leaves-out-decisions}
> - decision[case 954.3][create][estimate-ask-tries-a-decision-call-only-for-a-hook-trial]{ref:rule-ask}{tags:session,workflow,harness}
> ```
