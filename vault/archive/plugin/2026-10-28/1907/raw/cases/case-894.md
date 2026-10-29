## Case 894 — The guard writes the file of case-guppi, so no permission prompt comes

> **context:**
> `case-guppi` writes the file of its Case by `Write` and fixes it by `Edit`. Its agent file sets `permissionMode: auto`, and `rule-permissions` keeps every path under `cases/` off the allow list on the claim that Claude Code keeps that mode for a subagent while the session is in Plan Mode (case 698). That claim no longer holds, so in this session each write of a Case file asked the person for permission. The section "Permission modes" of https://code.claude.com/docs/en/sub-agents says that when the main conversation is in `plan` mode the subagent stays in plan mode whichever `permissionMode` is set, and that in `bypassPermissions`, `acceptEdits` or auto mode the subagent takes that mode and the value set is ignored; the value applies only when the main conversation is in `default` or `dontAsk`. An allow rule does not help either: the person said that the main agent's write of `frontier.md`, which the allow list names, asked in this session too, and https://code.claude.com/docs/en/permission-modes says only that edits stay blocked until the plan is approved. The section "Hook approvals in plan mode" of https://code.claude.com/docs/en/permissions says that an `"allow"` of a `PreToolUse` hook has no effect on a file edit in plan mode, and its section on precedence says that a hook that exits with code 2 stops the tool call before permission rules are evaluated. A hook runs as a process of its own and writes with no tool call, as the hooks of `rule-spec-write` and `rule-case-check` already write the plan and the store. So the guard of `rule-spec-reconcile`, which already reads each `Edit`, `Write` and `MultiEdit` of `case-guppi` on its case file, makes the write itself and stops the call with exit 2, and no prompt comes. Option (c) of the round, a session started with `--allow-dangerously-skip-permissions`, breaks the Purpose of `rule-default-mode`, which keeps a session from writing anything before a Case is ratified, and the same page of permission modes says that the VS Code chat panel keeps the blocks of plan mode with that flag; the person did not take it.
> In `.guppi/guppi/ratified.py` the guard reads a call by `guard_refusal`, which lets a call of `case-guppi` on a file under `cases/` through and refuses any other agent there, and next by `held_number`, which refuses a number another `agent_id` holds in the store, writes the entry of a first call, and on its own error prints one line and lets the call run; `guard` exits 2 on a refusal after one event-log line `ratified refused`. `written_case_files` of `.guppi/guppi/casecheck.py` takes each case file that a `Write`, `Edit` or `MultiEdit` tool use of the subagent names, whatever the result of the call, so the `SubagentStop` check still finds a file the hook wrote from a stopped call, and `subagent` keeps the files that stand; it needs no change. A Grep for `old_string|replace_all` over `.guppi/guppi/` printed nothing, so no code applies an `Edit` today, and the new code is no second copy of a judgment.
> A Grep for `permissionMode` over `vault/wiki/` and `.claude/` printed `vault/wiki/rules/rule-case-build.md`, `vault/wiki/rules/rule-permissions.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md`, `vault/wiki/estimates/estimate-permissions.md`, `vault/wiki/estimates/estimate-case-protocol-case-form.md`, `vault/wiki/log.md` and `.claude/agents/case-guppi.md`. Case 894.2 changes the two sentences of `rule-permissions` that rest on the mode, and Case 894.3 the clause of `rule-case-build` and the line of its Estimate; the History lines of these pages and `log.md` are not read; the hit in `estimate-case-protocol-case-form` is a reading in its Result and stands; `permissionMode: auto` stays in the agent file, by the person's answer. The Purpose of `rule-spec-reconcile` stands: a hook still refuses any edit of a case file unless `case-guppi` makes it. The sentences of `rule-case-build` and `estimate-case-build-writes-the-case` that say `case-guppi` writes its file by `Write` stand, since it still calls `Write`, and the guard carries the call out. The Criterion of `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` stands: the number check is unchanged and runs before the write, and on its own error it still lets the call run; its tests under `-k number_held` that expect a passing call to exit 0 change under Case 894.1. A Grep for `case-guppi\.md|rule-case-build|rule-spec-reconcile\.md|rule-permissions` over `.guppi/tests/` printed one docstring line of `.guppi/tests/test_guppi_package.py`, so no test reads the live files this Case renders. The Render of `rule-permissions` does not change, so `.claude/settings.json` stays as it is. The Criterion of `estimate-spec-write-exits-2-on-an-error` stands: its line that the guard keeps exit 0 with its line on stderr on its own error still holds, since an error of the number check or of the write lets the call run with exit 0 and one line; its `method`, all of `.guppi/tests/test_ratified.py`, runs the tests that Case 894.1 changes. Whether Claude Code knows the file as read after a call the guard stopped is not settled: the section "Edit tool behavior" of https://code.claude.com/docs/en/tools-reference says that an `Edit` needs a read of the file in the conversation, that a newer model may edit an unread file when reading it would not ask, and that a file changed on disk since the last read can still be edited when `old_string` matches its current text; it does not say whether these checks run before the `PreToolUse` hooks. So `case-guppi` reads its file by `Read` after a write of the guard and before its next `Edit`, which asks nothing inside the project. That read is in Case 894.3. Whether the client asks at the write is the promise of `estimate-permissions` alone (Case 894.2); the Criterion of Case 894.1 does not repeat it, since its `method` cannot see a prompt.

> **problem:**
> In Plan Mode Claude Code asks the person before each write of `case-guppi` to its Case file, though the person ratifies each Case anyway. The setting the harness relied on, `permissionMode: auto`, is ignored in plan mode, and the allow list does not stop the prompt there.

> **recommend:**
> - **How does the write of a Case file stop asking?**
>   - Recommended: no option recommended, since the documentation does not settle whether an allow rule works in plan mode; (a), case files on the allow list, if the write of `frontier.md` did not ask.
>   - Answer: the write of `frontier.md` asked for permission in this session; what to do then, and how to keep `case-guppi` from asking. Replaced by the question who writes the Case file.
> - **What happens to the `permissionMode: auto` line of the helper?**
>   - Recommended: (a) keep the line, and fix what the pages claim for it.
>   - Answer: agreed, (a).
> - **What does the check of `rule-permissions` promise for reads outside the project?**
>   - Recommended: (a) drop that promise.
>   - Answer: agreed, (a).
> - **Who writes the Case file, so that no question comes?**
>   - Recommended: (a) the guard hook writes the file and stops the call.
>   - Answer: agreed, (a); let us try it this way.
> - **How is the hook's write checked?**
>   - Recommended: (a) rewrite the guard's check, and keep the "no question" promise in the check of `rule-permissions`, read after the first Case file written in plan mode of a later session.
>   - Answer: agreed, (a).
> - **What happens when the hook cannot make the write?**
>   - Recommended: (a) an Edit that cannot apply is stopped with its reason; an error of the hook lets the call run.
>   - Answer: agreed, (a).
> - **One Case, or one part per page?**
>   - Recommended: (a) three parts under one Case.
>   - Answer: agreed, (a).

### Case 894.1 — The guard writes the file of case-guppi and stops the call

> **given:**
> `.guppi/guppi/ratified.py`: the guard of the plan and of the case files, by `guard`, `guard_refusal` and `held_number`.
> **＋** `.guppi/tests/test_ratified.py`: the tests of the guard.
> **＋** `rule-spec-reconcile`: the rule of the guard.
> **＋** `estimate-spec-reconcile-refuses-an-edit-of-the-plan`: its Criterion is replaced whole.
> **＋** `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`: the number check, which runs before the write.
> **＋** `.guppi/guppi/casecheck.py`: `is_case_file`, the judgment of a case file.
> **＋** `.guppi/guppi/ledger.py`: `is_plan_file`, which judges a plan file under `.claude/plans/`, and `plan_path`.
> **＋** `vault/raw/<date>/<HHMM>/`: a session folder, whose `cases/` folder holds the case files.

> **when:**
> An agent calls `Edit`, `Write` or `MultiEdit` on a file, and `uv run --project .guppi guppi ratified --guard` on `PreToolUse` reads the path, the content, the agent type and the `agent_id` of the call from the hook input.

> **then:**
> The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
> **＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
> **＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way, and so is one of a file under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`, whatever its name and whether it exists or not, when the hook input does not name `case-guppi` as the agent type; the reason names the file and says that `case-guppi` alone writes it.
> **＋** An `Edit`, `Write` or `MultiEdit` whose hook input names `case-guppi` on a file outside such a `cases/` folder is refused the same way.
> **＋** A call whose hook input names `case-guppi` on a file under such a folder, which `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` neither refuses nor lets run on an error of the guard, is written by the hook itself: the content of a `Write`, or each `old_string` of an `Edit` or a `MultiEdit` replaced by its `new_string`, in order, once, or at each match with `replace_all`.
> **＋** After that write the hook exits 2 with one line on stderr that names the file, says that the hook wrote it and tells the agent not to make the call again, so the call does not run.
> **＋** A file under that folder is judged by `is_case_file` of `.guppi/guppi/casecheck.py`, which the check of the file uses too; a plan file is a `.md` file under `.claude/plans/`, judged by `is_plan_file` of `.guppi/guppi/ledger.py`, which `plan_path` uses too.
> **＋** A refusal writes one line `ratified refused` to the day's event log, the write of the hook one line `ratified wrote`, and neither writes a `tool` line, so `plan_path` of `.guppi/guppi/ledger.py` still names the plan file.
> **－** An `Edit` or `MultiEdit` of `case-guppi` whose old string is missing from the file, is found more than once without `replace_all`, or names a file that does not exist leaves the file as it stands: exit 2 with that reason, and nothing of a `MultiEdit` is written.
> **－** An error of the hook while it writes the file of `case-guppi` lets the call run: exit 0 with one line on stderr.
> **－** An edit of a file outside `.claude/plans/` and outside such a `cases/` folder by any agent but `case-guppi` is not judged by this hook.
> **－** A payload the hook cannot read: exit 0 with one line on stderr.
> **－** No `PostToolUse` hook compares an edit of the plan.

> **tasks:**
> - [ ] update `rule-spec-reconcile`
>   - old: `and so does this hook for the entry that holds a number,`
>   - new: `` and so does this hook for the entry that holds a number and for the file of `case-guppi`, ``
>   - old: `so no hook can create it. A refusal writes one line to the day's event log;`
>   - new: `` so no hook can create it. On the first of these exceptions the hook makes the write itself, since Claude Code keeps a subagent in plan mode in Plan Mode whatever its `permissionMode` and asks the person before its edit: it writes the content of a `Write`, or replaces each `old_string` of an `Edit` or a `MultiEdit` by its `new_string` in order, once or at each match with `replace_all`, writes one line `ratified wrote` to the day's event log, and exits 2 with one line that says the file is written and the call is not to be made again, so the call does not run and Claude Code asks nothing (as set in case 894.1). An old string missing from the file, found more than once without `replace_all`, or a file that does not exist leaves the file as it stands and is refused with that reason; an error of the hook while it writes lets the call run, and Claude Code may ask the person that one time (as set in case 894.1). A refusal writes one line to the day's event log; ``
>   - change: `the guard writes the file of case-guppi itself and stops the call, so no permission prompt comes in Plan Mode (case 894.1)`
> - [ ] update `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
>   - set:
>     ```
>     status: pending
>     purpose: "An edit of the plan file or its store is refused, the one Write that creates the plan with its title line excepted, and so is an edit of a file of a built Case under cases/ by any agent but case-guppi, and any edit of case-guppi outside cases/; an edit of case-guppi under cases/ is written by the hook itself and the call stopped"
>     method: "uv run --project .guppi pytest .guppi/tests/test_ratified.py -k guard; by hand at the Work readings of the session that changes the guard, one probe Write of the main agent under cases/, refused and in the event log"
>     ```
>   - change: `the Criterion replaced whole — the guard writes the file of case-guppi itself and stops the call; the purpose and the method follow (case 894.1)`
> - [ ] `.guppi/guppi/ratified.py`: after `guard_refusal` and `held_number` let a call of `case-guppi` on a case file through, `guard` writes the content of a `Write`, or applies the `old_string`, `new_string` and `replace_all` of an `Edit` and of each edit of a `MultiEdit` in order on the text read and written as UTF-8 with no change of line ends, writes one event-log line `ratified wrote <tool> <path>` and exits 2 with one stderr line that names the file, says that the hook wrote it and tells the agent not to make the call again; an old string missing, found more than once without `replace_all`, or a file that does not exist is refused with that reason and writes nothing; `held_number` tells its own error apart, so that on that error and on an error of the write the call runs with exit 0 and one stderr line; the module docstring says so.
> - [ ] `.guppi/tests/test_ratified.py`: the tests of the guard and of `-k number_held` that expect a call of `case-guppi` on a case file to exit 0 expect the hook's write and exit 2 instead, and their `Edit` calls carry an `old_string`; new tests cover a `Write` written whole, an `Edit` once and with `replace_all`, a `MultiEdit` in order, a missing old string, an old string found twice and a missing file each refused with the file unchanged, an error of the write and an error of the number check each letting the call run with exit 0, and the `ratified wrote` line with no `tool` line.
> - [ ] read `estimate-spec-reconcile-refuses-an-edit-of-the-plan`

> **ratification:**
> ```
> - decision[case 894.1][update][rule-spec-reconcile]{ref:rule-spec-reconcile}
> - decision[case 894.1][update][estimate-spec-reconcile-refuses-an-edit-of-the-plan]{ref:rule-spec-reconcile}
> ```

### Case 894.2 — The allow list says why case files stay off it

> **given:**
> `rule-permissions`: the allow list and the reason for each path on it or off it.
> **＋** `estimate-permissions`: its Criterion is replaced whole.
> **＋** `.claude/settings.json`: the rendered allow list, unchanged.
> **＋** `.guppi/tests/test_render.py`: the JSON case that fixes the shape of the block.
> **＋** `rule-spec-reconcile`: the guard that writes the file of `case-guppi`.
> **＋** `vault/raw/**`: the session folders, whose working files the list names and whose `cases/` folders stay off it.
> **＋** `vault/wiki/brief.md`: the one file of `vault/wiki/` on the list.
> **＋** `~/.claude/projects/c--PROJECTS-GUPPI`: the folder of saved transcripts, which `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)` name.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder `~/.claude/projects/c--PROJECTS-GUPPI` itself as its path, or a path under it.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `.guppi/tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only: the reading line records it from the person, never from the agent, whose reply does not tell an approved call from one not asked.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** A Read, Grep or Glob whose path is `~/.claude/projects/c--PROJECTS-GUPPI` itself or a path under it runs with no prompt, in Plan Mode too.
> **＋** `case-guppi` writes the file of its Case with no prompt in Plan Mode, since the guard of `rule-spec-reconcile` makes the write and stops its call.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** An error of the guard of `rule-spec-reconcile` while it writes that file lets the call run, and the client may ask the person that one time; that prompt is not a finding and not a `failed`.
> **－** A Read, Grep or Glob of `case-guppi` on a path outside the project that no rule of the allow list names is not bound by this Criterion: it may ask the person.
> **－** `deny` and `ask` are empty; nothing else under `vault/wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names `~/.claude/projects/c--PROJECTS-GUPPI`.

> **tasks:**
> - [ ] update `rule-permissions`
>   - old: `` The file of a built Case under `cases/` is not on the list: `case-guppi` writes it in the mode `permissionMode: auto` of its agent file (case 698), which Claude Code keeps for a subagent while the session is in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/` (case 645.16). ``
>   - new: `` The file of a built Case under `cases/` is not on the list: in Plan Mode Claude Code keeps a subagent in plan mode whatever its `permissionMode` and asks before its edit, allow list or not, so the guard of `rule-spec-reconcile` writes the file of `case-guppi` itself, stops its call so that nothing is asked unless the guard fails to write, and keeps it inside `cases/` (as set in case 894.2). ``
>   - old: `` A call of `case-guppi` that these rules do not match is judged by its mode `permissionMode: auto`, with no prompt to the person, and a call they match needs no verdict of the classifier of Claude Code, which refuses a call when its server gives none (case 698). ``
>   - new: `` A call of `case-guppi` that these rules do not match is judged by the mode of the session, and by its own `permissionMode: auto` only while the session runs in `default` or `dontAsk` mode, so a read outside the project that no rule names may ask the person, in Plan Mode too; a call the rules match needs no verdict of the classifier of Claude Code, which refuses a call when its server gives none (as set in case 894.2). ``
>   - change: `case-guppi stays in plan mode in Plan Mode whatever its permissionMode; the guard of rule-spec-reconcile writes its Case file, and a read outside the project that no rule names may ask (case 894.2)`
> - [ ] update `estimate-permissions`
>   - set:
>     ```
>     status: pending
>     method: "the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of .guppi/tests/test_render.py; by hand, after the first Case file that case-guppi writes in Plan Mode of a session after the Work Mode that changes the guard of rule-spec-reconcile: the person's word on whether the client asked at that write, and at a Grep of a subagent whose path is the folder of the project's saved transcripts itself and at one whose path is a file under it, recorded in the estimate line, never the agent's, which cannot see the prompt"
>     ```
>   - change: `the Criterion replaced whole — case-guppi writes its Case file with no prompt in Plan Mode by the guard of rule-spec-reconcile, and a read outside the project that no rule names is not bound; the method follows (case 894.2)`
> - [ ] read `estimate-permissions`

> **ratification:**
> ```
> - decision[case 894.2][update][rule-permissions]{ref:rule-permissions}
> - decision[case 894.2][update][estimate-permissions]{ref:rule-permissions}
> ```

### Case 894.3 — case-guppi takes the guard's line as the write done

> **given:**
> `rule-case-build`: the Render of the agent file of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from it.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `rule-spec-reconcile`: the guard that writes the file of `case-guppi`.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of its case file.

> **when:**
> `case-guppi` calls `Write` or `Edit` on the file of its Case under `raw/<date>/<hi HHMM>/cases/`, as the text of `.claude/agents/case-guppi.md` sets it.

> **then:**
> It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write, Edit and WebFetch, and `permissionMode: auto`, which Claude Code applies only while the session runs in `default` or `dontAsk` mode.
> **＋** In Plan Mode the guard of `rule-spec-reconcile` writes the text of its `Write` or `Edit` into its file and stops the call; a line of the guard that says the file is written it takes as the write done, does not make the call again, and reads the file by `Read` before its next `Edit` of it.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `the file of your Case is the one file this harness lets you write, in the permission mode your agent file sets, and its guard refuses any other.`
>   - new: `` the file of your Case is the one file this harness lets you write: its guard writes the text of your `Write` or `Edit` into it itself and stops your call with a line that says the file is written, which is no failure and no call to make again, and you read the file by `Read` before your next `Edit` of it; the guard refuses any other file (as set in case 894.3). ``
>   - change: `the guard writes the Case file for case-guppi and stops the call; case-guppi takes that line as the write done (case 894.3)`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
>     **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
>     **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.
>     **＋** Or, in Work Mode, the main agent dispatches it with the id of a new top-level Case, the path of the file of a ratified Case of the approved Spec, the sub-case of it that must change and the reason.
>
>     Then:
>     `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
>     **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
>     **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
>     **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
>     **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
>     **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
>     **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
>     **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
>     **＋** Where an Estimate that the Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate, never that promise written again.
>     **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
>     **＋** Asked, by a message or by a finding of `/pre-spec`, to change a Case, it builds the change under the number of that Case; outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one for it.
>     **＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it writes no new file and answers with a round that asks whether the behaviour goes into that Case, built again under a new number as `vault/wiki/case-schema.md` sets it, or into a new top-level Case beside it.
>     **＋** Where the person chooses a new Case beside it, it builds that behaviour as a new top-level Case in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `.guppi/guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
>     **＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
>     **＋** Dispatched in Work Mode with a ratified Case and the sub-case of it that must change, it reads the file of that Case whole and builds under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand: each page change, task and Estimate of that sub-case that still holds, with the change.
>     **＋** Each decision line of that new Case carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases, and the file of the ratified Case stays as it is.
>     **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
>     **＋** In Work Mode a round may also come when it builds a new Case that replaces a sub-case of a ratified Case.
>     **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write, Edit and WebFetch, and `permissionMode: auto`, which Claude Code applies only while the session runs in `default` or `dontAsk` mode.
>     **＋** In Plan Mode the guard of `rule-spec-reconcile` writes the text of its `Write` or `Edit` into its file and stops the call; a line of the guard that says the file is written it takes as the write done, does not make the call again, and reads the file by `Read` before its next `Edit` of it.
>     **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
>     **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
>     **－** It does not put a change asked on a named Case into a new top-level Case without the person's answer to a round.
>     **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
>     **－** In Work Mode it never builds a Case of the approved Spec again under its own number; a Case ratified in that Work Mode that comes back to it before any of its tasks has run it changes under its own number, as in Plan Mode.
>     **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
>     **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
>     **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
>     **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
>     **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, and the file of a new Case it builds beside a ratified Case, and no ledger line.
>     **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.
>     ```
>   - change: `the Criterion replaced whole — permissionMode auto applies only in default or dontAsk mode; in Plan Mode the guard writes the Case file, and case-guppi takes its line as the write done and reads the file before its next Edit (case 894.3)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 894.3][update][rule-case-build]{ref:rule-case-build}
> - decision[case 894.3][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> ```
