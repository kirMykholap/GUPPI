## Case 925 — A hook keeps ask-guppi from reading a Decision page

> **context:**
> `ask-guppi` checks the plan against the vault at `/pre-spec`. Its frame, `.claude/agents/ask-guppi.md` rendered from `rule-ask`, lets it open a Decision page for two reasons: a page of its answer carries `deferred_by`, or the question asks why something was decided. At `/pre-spec` it may open the Decision only after a finding of its own names the page (case 800.2). Only the agent's judgment holds this rule. The hook of `rule-search-leaves-out-decisions`, `.guppi/guppi/grepguard.py`, leaves the Decision pages out of a wide Grep. It lets a Grep inside `vault/wiki/decisions/` pass unchanged, and it never runs on a Read (`before` of that file, read whole). The agent broke the rule twice, by the two children of `insight-ask-guppi-reads-a-decision-outside-its-frame`. At the `/pre-spec` of session 1426 it read the Decision behind the `deferred_by` of `entity-guppi`, a page that no finding named. Case 800.2 then made the text stricter. Case 800 chose text over a hook, since a hook cannot see the findings. At the `/pre-spec` of session 1907 the agent grepped `decision-case-882.3.md`, the Decision behind the `deferred_by` of `rule-clean-branch`, a page that Case 893.1 took up and that no finding named. That was the case that the text of 800.2 forbids. Both times the agent reported the break itself.
>
> The person chose a hook that needs no finding: it refuses every Read of a Decision page and every Grep inside `vault/wiki/decisions/` that `ask-guppi` makes. The hook tells `ask-guppi` from other agents by `agent_type`. The hooks documentation, https://code.claude.com/docs/en/hooks, says that when a subagent calls a tool, the `PreToolUse` input carries the `agent_id` and `agent_type` that identify the subagent, and that a hook denies a call by `permissionDecision: deny`. `ratified.py` reads the same field for `case-guppi` (its docstring: measured 2026-10-05, session 0311). Today only `/pre-spec` dispatches `ask-guppi` as an agent (a Grep of `ask-guppi` over `.claude/` printed `.claude/agents/ask-guppi.md`, `.claude/agents/case-guppi.md`, `.claude/rules/search-leaves-out-decisions.md`, `.claude/skills/hi/SKILL.md` and `.claude/skills/pre-spec/SKILL.md`; the agent file names itself, the hit in `hi/SKILL.md` names the source of a Frontier line, and `case-guppi` runs the recipe itself). So the agent keeps no reason. A finding or an `exists` or `near` line on a page with `deferred_by` names the Decision by its slug, and an answer to why something was decided gives the slug that the page's `origin` points to. `case-guppi`, which runs the recipe itself with its own `agent_type`, keeps both reasons. So the sentence of `rule-case-build` that it opens `vault/wiki/decisions/` only as `ask-guppi.md` allows stays true, and so does the Criterion of `estimate-ask-query-before-a-create` that Case 920.2 sets, since that Criterion speaks of the run of `case-guppi` and Case 920 changes no text of `rule-ask`. By the person's answers, `grepguard` also runs on `Read`: `rule-hook-registry` adds it to the `Read` matcher beside `pageread`, the hook of `rule-page-read`. On a Read under `vault/wiki/` with no `offset` or `limit`, `before` of `.guppi/guppi/pageread.py` (read whole) returns `updatedInput` with `limit` set to the line before `## History` and no permission decision, a Decision page included. The hooks documentation says that when several `PreToolUse` hooks return different decisions, `deny` wins over `defer`, `ask` and `allow`, so the refusal holds and the Read does not run; it does not say what becomes of the `updatedInput`, and the Case rests on nothing of it. `estimate-page-read-cuts-the-history` says that the agent gets the frontmatter and the body, which a refused Read does not give, so Case 925.6 replaces its Criterion with one more `－` line and sets its `method` to a reading in Work Mode; until that reading passes, `rule-page-read`, with `core: true`, stands `draft`. A Grep refusal works once Work Mode changes the code, since the hook already runs on `Grep`. A Read refusal works after the librarian's run renders `.claude/settings.json`. `orchestration.md` says that the agent dispatches `ask-guppi` only at pre-spec, so the live part of the new check waits for the first `/pre-spec` after that render, and reads each Decision call of `ask-guppi` there. `estimate-hook-registry-rendered` promises only that the file equals the Render, so it stands (case 378.5).
>
> Sentences of six checks become false, so the Case has one sub-case per promise. Case 925.1 creates `estimate-search-leaves-out-decisions-refuses-ask-guppi`; a Glob `vault/**/estimate-search-leaves-out-decisions-refuses*.md` printed nothing, so the slug is free, and the `create` has a `ref`, so no vault query runs before it. Case 925.2 replaces the Criterion of `estimate-search-leaves-out-decisions-by-the-grep-hook`, whose lines say that the hook never refuses a call and that a Grep inside the folder passes unchanged; a Grep of `never refuses|refuses no call` over `vault/wiki/` printed only that page. Its `method` waited for the `/hi` of a later session and is set anew, since the Grep exclusion already runs live. Case 925.3 replaces the Criterion of `estimate-search-leaves-out-decisions-in-every-agent`, which gives `ask-guppi` the reasons of its frame. Case 925.4 changes the Render of `rule-ask` and replaces the Criterion of `estimate-ask-opens-a-decision-only-for-a-finding`. Case 925.5 replaces the Criterion of `estimate-ask-finds`, whose line says that a finding on a page with `deferred_by` gives the `## Problem` of its Decision. A Grep of `deferred_by.{0,120}(Problem|open the decision|Decision it names)|(Problem|open the decision).{0,120}deferred_by` over `vault/wiki/` printed `log.md`, `lessons/lesson-ask-guppi-read-a-decision-page-without-a-reason.md`, `insights/insight-ask-guppi-reads-a-decision-outside-its-frame.md`, `estimates/estimate-ask-finds.md` and `rules/rule-ask.md`. The lesson and the Pattern of the Insight record the past and stand. The Insight stands `open` and `backlog.md` lists it, so Case 925.1 sets it `actioned` with `addressed_by` naming its own Decision, which `rule-insights-schema` requires for `actioned`. A Grep of `` reaches the deferred decision|Decisions through `deferred_by` `` over `vault/wiki/` printed `entities/entity-glossary.md`, `glossary.md`, `rules/rule-rules-schema.md` and `rules/schema.yaml`. Their sentences say that `ask-guppi` reaches the deferred decision through the `deferred_by` of an index line, without opening the page that carries it. That stays true: the agent still finds the Decision there, and now names it by that slug. So they stand.
>
> A Grep of `ask-guppi.{0,200}(Decision|decisions/)|(Decision|decisions/).{0,200}ask-guppi` over `vault/wiki/`, `log.md` and `brief.md` left out, printed `backlog.md`, `rules/rule-case-build.md`, the two lessons, the Insight, `rules/rule-search-leaves-out-decisions.md`, `estimates/estimate-search-leaves-out-decisions-in-every-agent.md`, `estimates/estimate-ask-opens-a-decision-only-for-a-finding.md`, `rules/rule-ask.md` and `estimates/estimate-ask-searches-at-prespec.md`. The line of `backlog.md` is the generated line of this item. The `－` line of `estimate-ask-searches-at-prespec` hands Decision reads to `estimate-search-leaves-out-decisions-in-every-agent`, which still reads them, so it stands. The same Grep over `.claude/` printed `.claude/agents/case-guppi.md`, the sentence of `rule-case-build` above. A Grep of `deferred_by|decisions/|Decision` over `.claude/skills/pre-spec/SKILL.md` printed nothing, so the skill sets nothing about Decision reads. A Grep of `agent_type` over `.guppi/guppi/` printed `casecheck.py`, `event.py` and `ratified.py`. Each compares the field with `case-guppi`, or names `subagent_type`, so no code judges a call of `ask-guppi`. The path judgment is `pageread.inside` over `wiki_root(...) / "decisions"`, which `grepguard` already imports, and the Read side uses it too. A Grep of `REPO / "\.claude"|ROOT / "\.claude"|"\.claude" / "(agents|rules)"|rule-ask|rule-search-leaves|rule-hook-registry` over `.guppi/tests/` printed `test_guppi_package.py` and `test_grepguard.py`. `test_guppi_package.py` reads `.claude/settings.json` for the commands of `ledger`, `onward`, `ratified` and `casecheck`, and the files of `.claude/` for `uv run guppi` and `uv run pytest`, which the new texts do not hold. `test_grepguard.py` builds its vault in a temporary folder. Its test that another tool passes unchanged sends a `Read` with no `agent_type`, which still passes. The two lessons were written in sessions 1426 and 1907, so no decision line carries `{addresses:...}` for them (case 284.2), and the session's ledger holds no `error` lesson.

> **problem:**
> A rule that only the agent's judgment holds failed twice: `ask-guppi` read a Decision page for a reason its frame does not name, and the stricter text of case 800.2 did not stop the second read.

> **recommend:**
> - **How should a Decision read outside the frame of ask-guppi be stopped?**
>   - Recommended: (a) a hook refuses every Decision read by `ask-guppi`, and the text drops its reasons: a finding or answer line on a put-off page names the Decision by its slug.
>   - Answer: agreed, (a).
> - **Where does the refusal of a Read run?**
>   - Recommended: (a) the search guard `grepguard` also runs on Read.
>   - Answer: agreed, (a).
> - **One Case or one part per promise?**
>   - Recommended: (a) five parts, one per promise.
>   - Answer: agreed, (a).
> - **How is the refusal checked?**
>   - Recommended: (a) a new check, `estimate-search-leaves-out-decisions-refuses-ask-guppi`.
>   - Answer: agreed, (a).
> - **How is the new text of ask-guppi checked?**
>   - Recommended: (a) rewrite the conditions of `estimate-ask-opens-a-decision-only-for-a-finding`, with its purpose and method.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the `/pre-spec` report, which the person agreed to, asked to put the pointers of the new texts in brackets of their own, to read the live refusal from the first `/pre-spec` after the render instead of a dispatch by hand, to set the Insight `actioned`, to settle the glossary rows and the schema line on `deferred_by`, to settle `estimate-page-read-cuts-the-history`, and to say which hook answer holds on a refused Read.
>   - Taken: the pairs and methods rewritten; the `method` of the new check waits for that `/pre-spec`; Case 925.1 sets the Insight `actioned`; `context` says why the glossary rows and the schema line stand; Case 925.6 adds one exception line to the Criterion of `estimate-page-read-cuts-the-history`; `context` gives the order of precedence of the hooks documentation.

### Case 925.1 — The search guard refuses a Decision read by ask-guppi

> **given:**
> `rule-search-leaves-out-decisions`: the rule of Decision reads; its Purpose and Render change.
> **＋** `.guppi/guppi/grepguard.py`: the hook that refuses the call.
> **＋** `.guppi/tests/test_grepguard.py`: the tests of the hook.
> **＋** `rule-hook-registry`: registers the hook on `Read` too.
> **＋** `.claude/settings.json`: the registrations, rendered from `rule-hook-registry`.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the file rendered from `rule-search-leaves-out-decisions`.
> **＋** `rule-page-read`: the other hook on `PreToolUse` of `Read`; its code is unchanged.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the new check of the refusal.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `insight-ask-guppi-reads-a-decision-outside-its-frame`: the Insight whose cause the hook closes; set `actioned`.

> **when:**
> `ask-guppi` calls Read with a `file_path` under `vault/wiki/decisions/`, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it, and `uv run --project .guppi guppi grepguard` of `.guppi/guppi/grepguard.py`, registered on `PreToolUse` of `Read` and of `Grep` in `.claude/settings.json`, reads the call with `agent_type` `ask-guppi`.

> **then:**
> The hook refuses the call by `permissionDecision: deny`, with a reason that names the path and `rule-search-leaves-out-decisions`, and exits 0; the call does not run.
> **＋** The same Read or Grep by the main agent, by `case-guppi` or by the librarian passes unchanged.
> **＋** A Read of `ask-guppi` outside `vault/wiki/decisions/` passes unchanged, and a Grep of `ask-guppi` over a folder that holds `vault/wiki/decisions/` gets the exclusion at the end of its `glob`, as for any agent.
> **－** A Glob of `ask-guppi` that prints the path of a Decision page passes: a path is no text of the page.
> **－** A payload the hook cannot read, or an error, lets the call pass, with one line on stderr.

> **tasks:**
> - [ ] update `rule-search-leaves-out-decisions`
>   - old: `` a Grep inside `vault/wiki/decisions/` it leaves unchanged, and the file keeps the rule on reading a Decision page ``
>   - new: `` a Grep inside `vault/wiki/decisions/` it leaves unchanged but for a call of `ask-guppi`, whose Read of a Decision page and Grep inside that folder the same hook refuses, and the file keeps the rule on reading a Decision page ``
>   - old: `which the hook leaves unchanged, and only`
>   - new: `` which the hook leaves unchanged but for a call of `ask-guppi`, and only ``
>   - old: `A Glob may print the path of a Decision page: a path is no text of the page.`
>   - new:
>     ```
>     The frame of `ask-guppi` names no reason to read a Decision page, so the same hook, on `Read` and on `Grep`, refuses a Read of a Decision page and a Grep inside `vault/wiki/decisions/` made by `ask-guppi`, and leaves such a call of another agent unchanged (as set in case 925.1).
>     - A Glob may print the path of a Decision page: a path is no text of the page.
>     ```
>   - change: `the hook refuses a Read of a Decision page and a Grep inside vault/wiki/decisions/ by ask-guppi (case 925.1)`
> - [ ] update `rule-hook-registry`
>   - old: `"uv run --project .guppi guppi pageread", "timeout": 30 } ] },`
>   - new: `"uv run --project .guppi guppi pageread", "timeout": 30 }, { "type": "command", "command": "uv run --project .guppi guppi grepguard", "timeout": 30 } ] },`
>   - change: `the hook grepguard registered on PreToolUse of Read beside pageread (case 925.1)`
> - [ ] create `estimate-search-leaves-out-decisions-refuses-ask-guppi`
>   - ref: `rule-search-leaves-out-decisions`
>   - kind: `QA`
>   - purpose: `Whether the PreToolUse hook grepguard refuses a Read of a Decision page and a Grep inside vault/wiki/decisions/ made by ask-guppi, and leaves the same calls of every other agent unchanged`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_grepguard.py; by hand, after the first /pre-spec that runs once the librarian's run has rendered .claude/settings.json: each Read and each Grep of ask-guppi on vault/wiki/decisions/ in its agent transcript refused, recorded in the estimate line`
>   - tags: `[hooks, harness, session]`
> - [ ] update `insight-ask-guppi-reads-a-decision-outside-its-frame`
>   - set: `{status: actioned, addressed_by: decision-case-925.1}`
>   - change: `actioned: a hook refuses every Decision read of ask-guppi (case 925.1)`
> - [ ] `.guppi/guppi/grepguard.py`: `before` refuses a `Read` whose `file_path`, and a `Grep` whose searched path, lies in `vault/wiki/decisions/` when the payload's `agent_type` is `ask-guppi`, by `permissionDecision: deny` with a reason that names the path and `rule-search-leaves-out-decisions`, judged by `pageread.inside` over the folder the exclusion already uses; every other call keeps its behaviour, and the module docstring says so.
> - [ ] `.guppi/tests/test_grepguard.py`: tests that a `Read` of a Decision page and a `Grep` of that folder and of a file in it by `ask-guppi` are refused; that the same calls by `case-guppi`, by the librarian and with no `agent_type` pass unchanged; that a `Read` of `ask-guppi` outside the folder passes; that a `Grep` of `ask-guppi` over the wiki still gets the exclusion.
> - [ ] `uv run --project .guppi guppi render`: `.claude/rules/search-leaves-out-decisions.md`
> - [ ] `uv run --project .guppi guppi render`: `.claude/settings.json`
> - [ ] read `estimate-search-leaves-out-decisions-refuses-ask-guppi`

> **ratification:**
> ```
> - decision[case 925.1][update][rule-search-leaves-out-decisions]{ref:rule-search-leaves-out-decisions}
> - decision[case 925.1][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 925.1][create][estimate-search-leaves-out-decisions-refuses-ask-guppi]{ref:rule-search-leaves-out-decisions}{tags:hooks,harness,session}
> - decision[case 925.1][update][insight-ask-guppi-reads-a-decision-outside-its-frame]{ref:insight-ask-guppi-reads-a-decision-outside-its-frame}
> ```

### Case 925.2 — The check of the search guard names the one refusal

> **given:**
> `estimate-search-leaves-out-decisions-by-the-grep-hook`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/grepguard.py`: the hook the Criterion speaks of.
> **＋** `.claude/settings.json`: where the hook is registered.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `!**/decisions/**`: the exclusion the hook puts at the end of a `glob`.

> **when:**
> The main agent or any subagent calls Grep, and `uv run --project .guppi guppi grepguard` of `.guppi/guppi/grepguard.py`, registered on `PreToolUse` of `Grep` in `.claude/settings.json`, reads the call.

> **then:**
> When the searched folder — the `path` of the call, or the working directory when the call has none — is a folder that holds `vault/wiki/decisions/`, the hook returns the call by `updatedInput` with `!**/decisions/**` at the end of its `glob`, after a space when the `glob` holds another filter, and with no permission decision.
> **＋** A `glob` that already ends with `!**/decisions/**` is not changed; one that holds it elsewhere gets it again at the end.
> **＋** The Grep then prints no line and no path of a file under `vault/wiki/decisions/`.
> **＋** A call of the librarian is changed in the same way as a call of any other agent.
> **－** A Grep of an agent other than `ask-guppi` whose `path` is `vault/wiki/decisions/` or lies in it passes unchanged: an agent greps there only for a reason of its frame.
> **－** A Grep whose `path` is one file outside `vault/wiki/decisions/`, or a folder that does not hold `vault/wiki/decisions/`, passes unchanged.
> **－** The hook refuses no call but a Read or a Grep of `ask-guppi` on a Decision page, which `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads; a payload it cannot read or an error lets the call pass unchanged.

> **tasks:**
> - [ ] update `estimate-search-leaves-out-decisions-by-the-grep-hook`
>   - set:
>     ```
>     status: pending
>     method: "uv run --project .guppi pytest .guppi/tests/test_grepguard.py, then by hand in Work Mode a Grep over vault/wiki/ with no glob in the main agent and in a subagent, whether it prints a file under vault/wiki/decisions/, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the hook refuses the Decision reads of ask-guppi alone (case 925.2)`
> - [ ] read `estimate-search-leaves-out-decisions-by-the-grep-hook`

> **ratification:**
> ```
> - decision[case 925.2][update][estimate-search-leaves-out-decisions-by-the-grep-hook]{ref:rule-search-leaves-out-decisions}
> ```

### Case 925.3 — The check of Decision reads gives ask-guppi no reason

> **given:**
> `estimate-search-leaves-out-decisions-in-every-agent`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the file rendered from `rule-search-leaves-out-decisions`.
> **＋** `.claude/agents/ask-guppi.md`: the frame that names the reasons of `case-guppi`.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal.
> **＋** `estimate-search-leaves-out-decisions-by-the-grep-hook`: the check of the exclusion in a wide Grep.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian, outside this promise.

> **when:**
> A session starts after `uv run --project .guppi guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Read, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it.

> **then:**
> `.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
> **＋** The text of a Decision page reaches `case-guppi` only by a Read of its path or by a Grep whose `path` is `vault/wiki/decisions/` or lies in it, for a reason of `.claude/agents/ask-guppi.md`: a page of its answer carries `deferred_by`, or the question asks why something was decided.
> **＋** The text of a Decision page reaches the main agent for no reason, and reaches `ask-guppi` by no call.
> **－** An `addressed_by` that names a Decision page is no reason to read it.
> **－** Whether the hook refuses a Read or a Grep of `ask-guppi` on a Decision page is outside this promise: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads it.
> **－** Whether a Grep over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
> **－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
> **－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.

> **tasks:**
> - [ ] update `estimate-search-leaves-out-decisions-in-every-agent`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, and the text of a Decision page reaches case-guppi only for a reason its frame names, the main agent for none and ask-guppi by no call"
>     method: "by hand, after a session that runs on the rendered .claude/rules/search-leaves-out-decisions.md and .claude/agents/ask-guppi.md: the transcripts of the main agent and of each ask-guppi and case-guppi of that session, whether the file stands in each context and each Read of a page under vault/wiki/decisions/ and each Grep inside that folder, read against the Criterion, recorded in the estimate line (the render of case 925)"
>     ```
>   - change: `the Criterion replaced whole — ask-guppi reads no Decision page, case-guppi keeps the reasons of its frame (case 925.3)`
> - [ ] read `estimate-search-leaves-out-decisions-in-every-agent`

> **ratification:**
> ```
> - decision[case 925.3][update][estimate-search-leaves-out-decisions-in-every-agent]{ref:rule-search-leaves-out-decisions}
> ```

### Case 925.4 — ask-guppi names a Decision by its slug and opens none

> **given:**
> `rule-ask`: the rule of `ask-guppi`; one passage of its Render changes.
> **＋** `.claude/agents/ask-guppi.md`: the file rendered from `rule-ask`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill that dispatches `ask-guppi` at `/pre-spec`.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `estimate-ask-opens-a-decision-only-for-a-finding`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-search-leaves-out-decisions`: a Decision page is read only for a reason the frame of the agent names.
> **＋** `estimate-ask-finds`: the check of what a finding gives.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the check of Decision reads in every agent.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> `ask-guppi` runs no Read of a page under `vault/wiki/decisions/` and no Grep whose `path` is that folder or lies in it.
> **＋** A page that carries `deferred_by` has its Decision left unread, whether a finding names the page or not, and also when a Case of the plan changes that page.
> **－** What a finding on a page with `deferred_by` gives is outside this promise: `estimate-ask-finds` reads it.
> **－** Whether the hook refuses such a call is outside this promise: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads it.
> **－** Decision reads by the main agent and by `case-guppi` are outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads them.

> **tasks:**
> - [ ] update `rule-ask`
>   - old: `` Do not open or grep `vault/wiki/decisions/` except for two reasons: a page in your answer carries `deferred_by` — open the decision it names and give its `## Problem` on the `exists` or `near` line, or, at `/pre-spec`, in the finding that names the page, since a deferred decision is something already decided; at `/pre-spec` you open it only after a finding of yours names the page, never to judge whether a finding stands, and a page that carries `deferred_by` and stands in no finding has its Decision left closed (case 800.2); or the question asks why something was decided — reach the Decision through the page's `origin`. ``
>   - new: `` Run as the agent `ask-guppi`, you open and grep no page under `vault/wiki/decisions/`, and a hook refuses such a Read or Grep (as set in cases 925.1 and 925.4). A page in your answer that carries `deferred_by` you name with the slug of the Decision that field names, on the `exists` or `near` line, or, at `/pre-spec`, in the finding that names the page, since a deferred decision is something already decided, and you quote none of its text; a question why something was decided you answer with the slug of the Decision that the page's `origin` points to. A caller that runs this recipe itself, `case-guppi`, opens or greps `vault/wiki/decisions/` only for two reasons: a page in its answer carries `deferred_by` — it opens the decision that field names and gives its `## Problem` on the `exists` or `near` line — or the question asks why something was decided — it reaches the Decision through the page's `origin`. ``
>   - change: `ask-guppi opens no Decision page and names the Decision of a page with deferred_by by its slug; case-guppi, running the recipe itself, keeps the two reasons (case 925.4)`
> - [ ] update `estimate-ask-opens-a-decision-only-for-a-finding`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether ask-guppi at /pre-spec reads no Decision page, the Decision of a page with deferred_by left unread whether a finding names the page or not"
>     method: "by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the Read and Grep calls of ask-guppi on vault/wiki/decisions/ in its agent transcript read against the Criterion, recorded in the estimate line (the render of case 925.4)"
>     ```
>   - change: `the Criterion replaced whole — ask-guppi reads no Decision page at /pre-spec (case 925.4)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/ask-guppi.md`
> - [ ] read `estimate-ask-opens-a-decision-only-for-a-finding`

> **ratification:**
> ```
> - decision[case 925.4][update][rule-ask]{ref:rule-ask}
> - decision[case 925.4][update][estimate-ask-opens-a-decision-only-for-a-finding]{ref:rule-ask}
> ```

### Case 925.5 — A finding on a put-off page names its Decision by slug

> **given:**
> `estimate-ask-finds`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.claude/agents/ask-guppi.md`: the frame rendered from `rule-ask`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill whose questions the agent answers.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the search rule the list of what was not checked names.
> **＋** `vault/raw/<date>/event_log.md`: the log of the dispatch.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with one line that names what the agent read: the plan file, or the Spec that the plan's title line names, and the Cases it checked.
> **＋** Then stands one numbered list of findings under each question that `.claude/skills/pre-spec/SKILL.md` sets, in the order of that file.
> **＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
> **＋** A finding that names a page carrying `deferred_by` names the Decision that field names by its slug and quotes none of its text.
> **＋** After the findings stands one list of what the questions ask that the agent did not check. The list says "none" when the agent checked all of it and its searches broke no rule of `.claude/agents/ask-guppi.md` or of `.claude/rules/search-leaves-out-decisions.md`. Its last lines name each rule of those files that a search broke, one line each, and say whether a finding rests on what that search printed. Then stands a list of the paths of the files the agent read.
> **＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
> **－** `.claude/agents/ask-guppi.md` does not list the questions of `/pre-spec` itself.
> **－** Nothing but its numbered findings, or "none" alone, stands under a question. No sentence says what the agent checked and found sound, and this includes a clash with another Case that it did not find.
> **－** No summary of the findings, no list of what holds, no index line and no page text reaches the caller.
> **－** An answer with no list of paths holds the promise as well.

> **tasks:**
> - [ ] update `estimate-ask-finds`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the answer of ask-guppi in its agent transcript read against the Criterion and the event log, recorded in the estimate line (the render of case 925.4)"
>     ```
>   - change: `the Criterion replaced whole — a finding on a page with deferred_by names its Decision by slug, with none of its text (case 925.5)`
> - [ ] read `estimate-ask-finds`

> **ratification:**
> ```
> - decision[case 925.5][update][estimate-ask-finds]{ref:rule-ask}
> ```

### Case 925.6 — The check of the history cut leaves a refused Read out

> **given:**
> `estimate-page-read-cuts-the-history`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/pageread.py`: the hook that cuts the History, unchanged.
> **＋** `.guppi/guppi/pages.py`: `split_sections`, which finds the heading.
> **＋** `.guppi/tests/test_pageread.py`: the tests of the hook.
> **＋** `.claude/settings.json`: where the hooks on `Read` are registered.
> **＋** `estimate-search-leaves-out-decisions-refuses-ask-guppi`: the check of the refusal of a Read.
> **＋** `vault/wiki/`: the folder of the pages whose History the hook cuts.

> **when:**
> An agent — the main agent or a subagent — calls `Read` on a file under `vault/wiki/`.

> **then:**
> When the call carries neither `offset` nor `limit` and the file holds its own `## History` heading, `uv run --project .guppi guppi pageread` on `PreToolUse` sets `limit` to the line before that heading by `updatedInput`, and the agent gets the frontmatter and the body alone.
> **＋** After such a call, `uv run --project .guppi guppi pageread --after` on `PostToolUse` adds one line of `additionalContext`: the History is cut, its first and last line, and a `Read` with `offset` at its first line shows how the page changed.
> **＋** The heading is found by the walk of `split_sections` in `.guppi/guppi/pages.py`, so a `## History` inside a render block of the page does not count.
> **＋** An `Edit` of the page after the cut read works as after a whole read.
> **－** A call with its own `offset` or `limit`, a file with no `## History`, and a file outside `vault/wiki/` are not changed, and no line is added.
> **－** The page on disk is not changed: in Obsidian it shows whole.
> **－** A `Read` that another hook on `PreToolUse` of `Read` refuses does not run, and the agent gets no text of the page: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads that refusal.

> **tasks:**
> - [ ] update `estimate-page-read-cuts-the-history`
>   - set:
>     ```
>     status: pending
>     method: "uv run --project .guppi pytest .guppi/tests/test_pageread.py, then by hand in Work Mode a Read of a vault page in the main agent and in a subagent, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — a Read that another hook refuses is outside the promise (case 925.6)`
> - [ ] read `estimate-page-read-cuts-the-history`

> **ratification:**
> ```
> - decision[case 925.6][update][estimate-page-read-cuts-the-history]{ref:rule-page-read}
> ```
