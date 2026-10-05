## Case 645 — case-guppi writes its own Case file, and the hooks check it

> **context:**
> Today `case-guppi` hands back the whole Case as text. When the agent stops, the `SubagentStop` hook `guppi casecheck --subagent` reads that text from the agent's transcript and checks it. It stores the text in `<plan>.checked.json`, and when no finding stands it writes the text into `raw/<date>/<hi HHMM>/cases/case-<N>.md`. The `Stop` comparison of a showing and the Spec hook of `rule-spec-write` read the store. The guard `guppi ratified --guard` refuses every edit under `cases/`. When the check finds a fault, the agent must write the whole Case again. Case 644 shows the cost. It had seven sub-cases and about 30,000 characters. It was sent back for faults in 644.1, 644.2, 644.5 and 644.6, and it was generated again whole, though 644.3, 644.4 and 644.7 came back the same, character for character. The whole text also enters the main agent's context at every answer.
>
> The person chose these changes:
> - `case-guppi` writes its Case into its file by Write. It fixes findings, or makes a change the person asks for, by Edit of the lines at fault.
> - The same `SubagentStop` hook checks the file when the agent stops, and copies its text into the store, which stays the source that the Spec hook and the `Stop` comparison read.
> - A file changed after its check is refused, both at the showing and at the write into the Spec. Each of these two refusals gets a new Estimate.
> - The agent hands back a short summary: the path, then each Case's id and name, the Estimate that checks it, its ledger lines, and a line `**Other Case:**` when its `context` says another Case of the session should change instead (case 629.1). The main agent shows the Case from the summary and does not read the file.
> - The guard lets a Write or Edit under `cases/` through only for `case-guppi`, and refuses that agent anywhere else. The main agent stays the orchestrator and writes no Case.
> - The check reads the whole file every time, so `stored_parents` (case 629.3) and its Estimate go.
>
> This build answers the findings of pre-spec, with the person's answers:
> - The probe. The `case-guppi` of this session cannot run it. The render of `rule-render-harness` is the librarian's step, and the client reads `.claude/agents/` only at the start of a session (`lesson-agents-read-at-session-start-in-claude-code-2-1-228`). So the new form is live from the next session. The probe of 645.3 is made in Work Mode by a subagent this session can dispatch. It measures only whether the `PreToolUse` input names the agent type. The hooks reference says it does: `agent_type` is "Present when the session uses `--agent` or the hook fires inside a subagent" (https://code.claude.com/docs/en/hooks.md, read by the main agent at pre-spec).
> - Permission in Plan Mode. The person said no allow rule is needed when a subagent runs in Plan Mode, and asked that the documentation be checked. The subagents page says that a subagent with no `permissionMode` inherits the main conversation's mode, and that in `plan` mode the subagent "runs in the permission mode you set, except `bypassPermissions`". `acceptEdits` auto-accepts file edits in the working directory (https://code.claude.com/docs/en/sub-agents.md). So 645.1 sets `permissionMode: acceptEdits` in the agent file, and the guard of 645.3 keeps the agent inside `cases/`. A Grep of `asks before every edit|asks all the same` over `vault/wiki/`, with `!**/decisions/**`, printed 4 files: `log.md`, `lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt.md`, `rule-permissions.md` and `estimate-permissions.md`. I did not read `log.md`. `rule-permissions` and `estimate-permissions` say that in Plan Mode the client asks before every edit outside the plan file, which 645.16 bounds to the main agent. The lesson stands as the record of what the main conversation does. Its claim that the allow list does not lift the prompt stays true, and the allow list gains no path.
> - The old form. `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` speaks of this Case. The check changes in Work Mode, but the new frame of `case-guppi` is live only from the next session. A Case built again in this session's Work Mode would otherwise be stored by nobody, and its showing and its Spec write would be refused. So 645.2 keeps the old path: when the subagent wrote no case file and its newest output holds a Case heading, the check reads that output, stores it and writes the file as today, until a reading of `estimate-case-build-writes-the-case` passes live. A Case of a later session removes that path. On that path, an answer of sub-cases alone is judged without its parent's `given`, since `stored_parents` goes now. Its sections are still placed in the file beside the others.
> - The sentences that 645 makes false on `rule-case-build`, `rule-spec-reconcile`, `rule-spec-write` and `rule-case-check` get replace pairs in 645.1, 645.3, 645.5 and 645.2.
> - The Criterion of `estimate-case-check-shows-only-the-checked-case` is replaced in 645.11, because its pass condition for a showing of `ratification` alone holds no comparison of the file.
> - `estimate-case-build-answers-what-done-means`, `estimate-case-build-records-the-rounds-in-recommend`, `estimate-case-check-requires-a-backlog-item-decided-on-its-page` and `estimate-case-check-sends-back-a-ratified-case-in-another-shape` speak of the answer as the Case. They are replaced in 645.12 to 645.15, their moment the Case written into its file.
> - `estimate-case-build-checks-the-finished-case` is deferred by Case 647 of this plan. Its Criterion stays for the session that takes 647 up, though 645.1 changes the render sentences on the moment before the agent answers.
>
> What the frame showed, by these searches:
> - A Grep of `writes no file|file of the Case is written|is written for the answer|writing of the file|wrote from the answer|writes it into a file|writes from the answer|writes a Case that` over `vault/wiki/`, with `!**/decisions/**`, printed 18 files. They are placed as follows:
>   - These enter the Case: `rule-case-check`, `rule-case-build`, `rule-orchestration` and its render `orchestration.md`, `estimate-case-build-writes-the-case`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, `estimate-orchestration-shows-the-built-case`, `estimate-case-protocol-case-form`, `estimate-case-check-refuses-a-letter-outside-the-script` and `estimate-case-check-notes-a-criterion-line-not-carried`.
>   - These stand: `estimate-case-check-sends-back-a-faulty-round`, `estimate-case-check-refuses-text-outside-the-list` and `estimate-case-check-refuses-text-before-a-round` say that their own check writes no file, and it still writes none. `estimate-compact-recall-reloads`, `estimate-glossary-checks-the-file`, `estimate-prespec-onward-sends-the-agent-on` and `estimate-retro-onward-sends-the-agent-to-the-handoff` speak of other hooks.
> - A Grep of `SubagentStop` over `vault/wiki/rules/` printed `rule-case-check.md`, `rule-orchestration.md`, `rule-hook-registry.md` and `rule-spec-reconcile.md`. Over `.claude/` it printed `.claude/settings.json`. The registration in `rule-hook-registry` and `.claude/settings.json` stays as it is.
> - A Grep of `write_case_files|is_case_file|stored_parents|stored_family` over the `*.py` files of the repository printed `guppi/casecheck.py`, `guppi/ratified.py` and `tests/test_casecheck.py`. `stored_parents` goes. `write_case_files` stays for the old path until the later Case. `is_case_file` stays, the one judgment of the guard and the check. `stored_family` (case 629.4) stays: when the file holds the whole family it finds nothing to add, and the line of `estimate-case-check-requires-each-question-of-the-rounds` that describes it stays true.
>
> The other Estimates of `rule-case-check` (clash, problem in a sub-case, rounds, `then` line shared by siblings) speak of the Cases the check reads. They stay true when those Cases are read from the file. Case 644 is built again now. Its 644.1 takes a pair on the error sentence of `rule-spec-write`, and the pairs of 645.5 stand on other sentences of that page. Case 646 replaces the sentences of `rule-case-protocol` that call the reply of `case-guppi` its answer. The new Estimates carry a `ref`, so the vault query of `ask-guppi` was not run. A Glob `vault/**/*changed-case-file*` printed nothing, so both slugs are free.
>
> The check sent back two kinds of notes, and both kinds stand:
> - Notes on lines of the old Criteria that the new Criteria do not carry. Each of those lines was changed on purpose, for one of these reasons:
>   - It spoke of the answer as the Case, of a file the hook writes, of the tools Read, Grep and Glob alone, or of a sub-case answered alone.
>   - In 645.11, the pass condition and the list of refusals add the comparison of the file.
>   - In 645.16, the moment adds the write of `case-guppi`, the prompt in Plan Mode is bound to the main agent, and the line on `deny` and `ask` adds that no path under `cases/` is allowed.
> - Notes on `then` lines of sibling sub-cases that share many words. They share the words of files, the store, refusals and the rounds, but each sub-case sets its own promise.
>
> Not done:
> - When a second agent builds a Case under a number another agent holds, it overwrites that Case's file before the check sends it back. The comparison of 645.4 then refuses the showing of that Case until its own agent writes the file again. No guard stops the overwrite.
> - `orchestration.md` still calls the agent's reply "the answer". The summary is that answer now.
> - The old path of 645.2 stays until a later session removes it.

> **problem:**
> The check reads the text the agent hands back and writes the file from it. So every fix after a finding means generating the whole Case again, and the whole Case enters the main agent's context at every answer. The question was where the check runs, which copy reaches the Spec, what the agent hands back, how the guard tells `case-guppi` from the main agent, how a file changed after its check is caught, and what happens to the handling of an answer of sub-cases alone.

> **recommend:**
> - **When the check reads the file the agent wrote**
>   - Recommended: (a) when the agent stops, from the file: the same stop hook finds the file by the agent's own Write and Edit calls and checks it whole; findings are fixed by Edit; rounds and Fact answers stay plain text.
>   - Answer: agreed, (a). The person added that `case-guppi` must be allowed to write into `cases/`; as the person recalls, a subagent is not asked for permission to write in Plan Mode, so this stays convenient; the main agent still writes no Case and stays the orchestrator.
> - **Which copy reaches the Spec**
>   - Recommended: (a) keep the store: the check copies the passed file into it, and the Spec hook and the `Stop` check keep reading it; the sent file must still equal the stored text at the showing and at the Spec write.
>   - Answer: agreed, (a).
> - **What the agent hands back for a built Case**
>   - Recommended: (a) a short summary: the path, then for each Case and sub-case its id and name, the Estimate that checks it with one line on what it checks, and its ledger lines; a ledger line that differs from the file is caught at the showing.
>   - Answer: agreed, (a).
> - **How the guard tells `case-guppi` from the main agent**
>   - Recommended: (a) by the agent's type in the hook input, measured first: a Write or Edit under `cases/` passes only for `case-guppi`, which is refused anywhere else; a probe that waits for the person's word comes first in Work Mode, and work stops if the field is missing.
>   - Answer: agreed, (a).
> - **How the check of a changed file is itself checked**
>   - Recommended: (a) two new Estimates, one for the `Stop` check of a showing and one for the Spec hook; the existing Criteria stand, and nothing clashes with the other Case of the session.
>   - Answer: agreed, (a).
> - **What happens to the check of a lone sub-case**
>   - Recommended: (a) the whole file is judged every time; the lone-part handling and its Estimate are deleted, and the Estimates that say the agent writes no file or hands back the whole Case are replaced.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, a probe that this session can run, and a context that says the new form is live from the next session.
>   - Taken: the probe of 645.3 is made by a subagent this session can dispatch, and measures only whether the `PreToolUse` input names the agent type; the context says the render lands at the librarian's step and is read at the next session.
> - **Change**
>   - Asked: at pre-spec, check the documentation of Claude Code; when a subagent is dispatched in Plan Mode, no allow rule is needed.
>   - Taken: `permissionMode: acceptEdits` in the agent file of `case-guppi` (645.1), no allow rule, and `rule-permissions` and `estimate-permissions` bound the prompt in Plan Mode to the main agent (645.16).
> - **Change**
>   - Asked: at pre-spec, keep the old form until the writer is live.
>   - Taken: 645.2 still reads the answer text and writes the file when the subagent wrote no case file, until a reading of `estimate-case-build-writes-the-case` passes live; a later Case removes that path.
> - **Change**
>   - Asked: at pre-spec, replace the sentences of `rule-case-build`, `rule-spec-reconcile`, `rule-spec-write` and `rule-case-check` that the Case makes false.
>   - Taken: replace pairs in 645.1, 645.3, 645.5 and 645.2, and a `set` of the `purpose` of `rule-spec-write`.
> - **Change**
>   - Asked: at pre-spec, the summary carries a line when the Case's `context` says another Case should change instead, and the showing shows it.
>   - Taken: a line `**Other Case:**` in the summary (645.1), and the main agent asks about that Case from it (645.6).
> - **Change**
>   - Asked: at pre-spec, the Not done no longer names `case-schema.md`.
>   - Taken: removed; Case 646 replaces those sentences.
> - **Change**
>   - Asked: at pre-spec, replace the Criterion of `estimate-case-check-shows-only-the-checked-case`.
>   - Taken: 645.11, its pass condition joined with the comparison of the file.
> - **Change**
>   - Asked: at pre-spec, replace the four Estimates that speak of the answer as the Case, their moment the Case written into its file, and leave `estimate-case-build-checks-the-finished-case` for the session that takes Case 647 up.
>   - Taken: 645.12 to 645.15, and the context says the deferred Estimate stays.

### Case 645.1 — case-guppi writes its Case into its file and hands back a summary

> **given:**
> `rule-case-build`: the rule whose Render is the agent file of `case-guppi`.
> **＋** `estimate-case-build-writes-the-case`: its Criterion, `purpose` and `method` are set anew.
> **＋** `estimate-case-build-checks-the-finished-case`: deferred by Case 647. Unchanged.
> **＋** `.claude/agents/case-guppi.md`: the agent file the render writes.
> **＋** `.claude/skills/grill-me/SKILL.md`: the template of a round.
> **＋** `.claude/agents/ask-guppi.md`: the vault query the agent runs before a `create` without a `ref`.
> **＋** `vault/wiki/case-schema.md` and `vault/wiki/ratification.md`: the form of a Case and of its ledger lines.
> **＋** `.claude/settings.json`: the hooks registered on the event a changed hook runs on.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `rule-case-check`: its `SubagentStop` hook checks the file.
> **＋** `rule-spec-reconcile`: its guard lets `case-guppi` write that file, as 645.3 sets it.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
> **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file, then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
> **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
> **＋** Sent findings by the hook, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; asked by a message that opens a fork, it answers with a round.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: acceptEdits`, so it writes its file with no prompt while the session is in Plan Mode.
> **－** It does not write the whole Case again to fix a finding or make a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, and no ledger line.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` and with the Case alone when none is; the hook of `rule-case-check` checks it and writes it into a file of the session, which the main agent sends the person ``
>   - new: `` and, when none is, writes the Case into its file of the session by `Write` and answers with a short summary of it; the hook of `rule-case-check` checks the file, which the main agent sends the person ``
>   - old: `` and the `Stop` hook compares what the chat shows of it with the answer (cases 441, 452.4) ``
>   - new: `` and the `Stop` hook compares what the chat shows of it, and the file, with the text the check stored (cases 441, 452.4, 645.1) ``
>   - old: `tools: Read, Grep, Glob`
>   - new:
>     ```
>     tools: Read, Grep, Glob, Write, Edit
>     permissionMode: acceptEdits
>     ```
>   - old: `and answer with a round of questions while a fork is open, or with the Case alone.`
>   - new: `and answer with a round of questions while a fork is open, or write the Case into its file and answer with a summary.`
>   - old: `since the Spec is written from your answer; a hook writes your answer into a file that the main agent sends the person, who reads it in {{documentation_lang}}, and the person ratifies it.`
>   - new: `` into its file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, since the Spec is written from the text of that file that a hook checks and stores; the main agent sends the file to the person, who reads it in {{documentation_lang}}, and the person ratifies it. ``
>   - old: `answer with the next round, or with the Case when no fork is left.`
>   - new: `answer with the next round, or, when no fork is left, write the Case into its file and answer with the summary.`
>   - old: `Before you answer with the Case, check it whole, its sub-cases with it.`
>   - new: `Before you answer with the summary of a Case, check the Case in its file whole, its sub-cases with it.`
>   - old: `Just before you answer with the Case, run again each search`
>   - new: `Just before you answer with the summary, run again each search`
>   - old: `` When no fork is open, answer with the Case in the chat form of the schema, from its heading to the fence of `ratification`, and nothing else: no line before it, no note after it. A hook checks the answer before the main agent sees it; when it sends findings back, fix the Case and answer with it again. ``
>   - new: `` When no fork is open, write the Case in the chat form of the schema, from its heading to the fence of `ratification` and nothing else, into its file by `Write`. Claude Code may tell you in Plan Mode that you may edit only your own plan file: the file of your Case is the one file this harness lets you write, in the permission mode your agent file sets, and its guard refuses any other. Then answer with the summary alone: a first line `**Built:**` and the path of the file, then one list item per Case and sub-case — its id and name, the Estimate that checks it and one line on what that Estimate checks — and under the item its ledger lines in an untagged fence, as the file holds them. A hook checks the file when you stop, before the main agent sees your answer; when it sends findings back, fix the lines at fault by `Edit` and answer with the summary again, never by writing the whole Case again (case 645.1). ``
>   - old: `` and name in `context` the other Case and the change it needs; the main agent asks the person whether that Case is built again (case 637.2). ``
>   - new: `` and name in `context` the other Case and the change it needs, and again on a line `**Other Case:**` under the item of your Case in the summary; the main agent asks the person whether that Case is built again (cases 637.2, 645.1). ``
>   - old: `` Asked again by a message, answer with the Case again, changed as asked, or with a round when the message opens a fork. An answer again holds the Case whole, or, where the parent's `context`, `problem` and `recommend` stand as they were, the changed sub-cases alone, each from its heading to the fence of its `ratification`, an item of `recommend` whose answer changed only that sub-case under its heading; the hook writes them into the file of the Case beside the parts that did not change (case 629.2). ``
>   - new: `` Asked again by a message, change the file as asked, by `Edit` of the lines that change, and answer with the summary again, or answer with a round when the message opens a fork (case 645.1). ``
>   - old: `Write no file and no ledger line.`
>   - new: `Write no file but the file of your Case, and no ledger line.`
>   - change: `case-guppi writes its Case into its file by Write in permissionMode acceptEdits, fixes it by Edit and answers with a summary that names another Case to change; its tools gain Write and Edit (case 645.1)`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set:
>     ```
>     status: pending
>     purpose: 'case-guppi asks about the forks of an item in rounds by the skill grill-me, then builds the Case against the vault and its frame, writes it into its file and answers with a short summary'
>     method: 'by hand: live dispatches in a session after the render — one item with a fork, answered by a round and then the Case written into its file and a summary, one Case with a create without a ref, one that changes a hook, a Case the hook sent back and fixed by Edit, and a change the person asked for on one sub-case, made by Edit of that sub-case, the file written in Plan Mode with no prompt; the tokens and seconds of each dispatch in the estimate line'
>     ```
>   - change: `the Criterion replaced whole — case-guppi writes its Case into its file in permissionMode acceptEdits, fixes it by Edit and answers with a summary; the purpose and the method follow (case 645.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 645.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 645.1][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> ```

### Case 645.2 — The check reads the file case-guppi wrote

> **given:**
> `rule-case-check`: the rule of the check of a built Case.
> **＋** `estimate-case-check-sends-back-a-faulty-case`: its Criterion and `method` are set anew.
> **＋** `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`: deleted.
> **＋** `estimate-case-check-sends-back-a-faulty-round`: the promise of the form of a round. Unchanged.
> **＋** `estimate-case-build-writes-the-case`: its live reading ends the old path.
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`: the rule of the old path. Unchanged.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/ratified.py`: the reading of the chat form the check builds the Spec section by.
> **＋** `guppi/prespec.py`: `judge`, the checks of pre-spec.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.
> **＋** `.claude/settings.json`: the `SubagentStop` registration. Unchanged.

> **when:**
> `SubagentStop` fires when `case-guppi` stops; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

> **then:**
> `uv run guppi casecheck --subagent` takes each file under the `cases/` folder of a session folder, judged by `is_case_file` of `guppi/casecheck.py`, that a `Write` or `Edit` call of the subagent in `agent_transcript_path` names, and reads its Cases as the file stands now.
> **＋** A file whose Cases `<plan>.checked.json` already holds with the same text, line ends and trailing spaces aside, and with no findings is not checked or stored again, so the time of its store stands.
> **＋** Any other such file is checked whole: each Case is read in the chat form by the functions of `guppi/ratified.py`, its section of the Spec is built in memory as the Spec hook writes it, and `judge` of `guppi/prespec.py` runs over them, the decision lines of the `ratification` fences standing for the ledger and, with the session's window, giving the categories whose schema rule the session changes.
> **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
> **＋** Each Case of the file is stored, its text as the file holds it, with its findings and the time of the store, in `<plan>.checked.json`; the hook does not write that file.
> **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` fixes the file and stops again, whatever `stop_hook_active` says.
> **＋** Until a reading of `estimate-case-build-writes-the-case` passes live, a transcript that names no such file and whose newest output holds a Case heading is read the old way: that output is checked and stored as the Cases of a file are, and with no finding the hook writes it into `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the whole file when it holds the top-level Case, the section of each sub-case otherwise. A Case of a later session removes this path.
> **－** A finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged file is not sent back twice.
> **－** An output of the subagent with no Case heading — a summary, a round or a `**Fact:**` answer — is not read as a Case; the form of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`.
> **－** A subagent of another type, and a transcript the hook cannot read, get none of these checks, and nothing is stored. A session with no plan file is not sent back for a fault of a Case.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old: `the Case reaches the person in a file the hook writes from the answer that passed them (case 452.1).`
>   - new: `` the Case reaches the person in the file `case-guppi` writes, which the hook checks whole when the agent stops and stores, and a file that differs from its stored text is not shown or written into the Spec (cases 452.1, 645.2). ``
>   - old: `The check of an answer compares its Cases with the other Cases of the session`
>   - new: `The check of the file of a Case compares its Cases with the other Cases of the session`
>   - change: `the check reads the file case-guppi wrote, whole, when the agent stops, and keeps the old path of the answer text until the writer is live (case 645.2)`
> - [ ] update `estimate-case-check-sends-back-a-faulty-case`
>   - set:
>     ```
>     status: pending
>     method: 'uv run pytest tests/test_casecheck.py -k subagent, then by hand in a session after the render a file of case-guppi the hook sends back, fixed by Edit and passed, and a live round after a built Case, which leaves the stored entry of that Case as it stood'
>     ```
>   - change: `the Criterion replaced whole — the check reads the file case-guppi wrote, whole, and keeps the old path until the writer is live; the method follows (case 645.2)`
> - [ ] delete `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`
>   - impact: `the check reads the whole file of a Case; stored_parents of guppi/casecheck.py and its tests -k lone go, and on the old path an answer of sub-cases alone is judged without the given of its parent`
> - [ ] `guppi/casecheck.py`: `subagent` takes the files of `cases/` that the Write and Edit calls of the subagent name, skips one the store holds unchanged with no findings, and checks and stores each other one whole; with no such file and a newest output that holds a Case heading, the old path as today; `stored_parents` removed; the module docstring says the same and names the old path as kept until the writer is live.
> - [ ] `tests/test_casecheck.py`: tests `-k subagent` over a temp transcript with Write and Edit calls and temp case files — a file with a fault sent back and stored; the file fixed by Edit passes and is stored and not written; an unchanged passed file is not stored again; a round after a built Case leaves its entry as it stood; an answer text with no case file still stored and written; the tests `-k lone` removed.
> - [ ] read `estimate-case-check-sends-back-a-faulty-case`

> **ratification:**
> ```
> - decision[case 645.2][update][rule-case-check]{ref:rule-case-check}
> - decision[case 645.2][update][estimate-case-check-sends-back-a-faulty-case]{ref:rule-case-check}
> - decision[case 645.2][delete][estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent]{ref:rule-case-check}
> ```

### Case 645.3 — The guard lets case-guppi alone write under cases/

> **given:**
> `rule-spec-reconcile`: the rule of the guard.
> **＋** `estimate-spec-reconcile-refuses-an-edit-of-the-plan`: its Criterion, `purpose` and `method` are set anew.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the guard and its tests.
> **＋** `guppi/casecheck.py`: `is_case_file`, the judgment of a file under `cases/`.
> **＋** `guppi/ledger.py`: `is_plan_file` and `plan_path`.
> **＋** `.claude/plans/`: the folder of the plan files.
> **＋** `<plan>.checked.json`: the store beside the plan file.
> **＋** `vault/raw/<date>/<HHMM>/`: a session folder, which holds `cases/`.
> **＋** `.claude/settings.json`: the `PreToolUse` registration of the guard. Unchanged.

> **when:**
> An agent calls `Edit`, `Write` or `MultiEdit` on a file, and `uv run guppi ratified --guard` on `PreToolUse` reads the path, the content and the agent type of the call from the hook input.

> **then:**
> The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
> **＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
> **＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way.
> **＋** An `Edit`, `Write` or `MultiEdit` of a file under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`, whatever its name and whether it exists or not, is let through when the hook input names `case-guppi` as the agent type, and refused the same way otherwise; the reason names the file and says that `case-guppi` alone writes it.
> **＋** An `Edit`, `Write` or `MultiEdit` whose hook input names `case-guppi` on a file outside such a `cases/` folder is refused the same way.
> **＋** A file under that folder is judged by `is_case_file` of `guppi/casecheck.py`, which the check of the file uses too; a plan file is a `.md` file under `.claude/plans/`, judged by `is_plan_file` of `guppi/ledger.py`, which `plan_path` uses too.
> **＋** A refusal writes one line of the refusal to the day's event log and no `tool` line, so `plan_path` of `guppi/ledger.py` still names the plan file.
> **－** An edit of a file outside `.claude/plans/` and outside such a `cases/` folder by any agent but `case-guppi` is not judged by this hook.
> **－** A payload the hook cannot read: exit 0 with one line on stderr.
> **－** No `PostToolUse` hook compares an edit of the plan.

> **tasks:**
> - [ ] stop: before the guard code, a probe: a temporary dump of the keys of the `PreToolUse` input in `guppi ratified --guard` to the scratchpad, and a subagent this session can dispatch, its type named in the result, that calls Write on a probe file in the scratchpad; the dumped keys shown to the person; with no agent type in the input, the work stops and the person decides; the dump and the probe file removed after.
> - [ ] update `rule-spec-reconcile`
>   - old: `` the `Stop` hook of `rule-spec-write` writes the stored answer of `case-guppi`, ``
>   - new: `` the `Stop` hook of `rule-spec-write` writes the text of the file of `case-guppi` that `rule-case-check` stored, ``
>   - old: `and any edit of the file of a built Case that the person is sent, before it lands (case 453);`
>   - new: `` and any edit of the file of a built Case that the person is sent, before it lands, unless `case-guppi` makes it (cases 453, 645.3); ``
>   - old: `` and every `Edit`, `Write` and `MultiEdit` of a file under the `cases/` folder of a session folder under `vault/raw/` — the file of a built Case that the `SubagentStop` hook of `rule-case-check` writes from the stored answer, judged by one function of `guppi/casecheck.py` that its writer uses too (case 453): exit 2 ``
>   - new: `` and every `Edit`, `Write` and `MultiEdit` of a file under the `cases/` folder of a session folder under `vault/raw/` whose hook input does not name `case-guppi` as the agent type — the file of a built Case that `case-guppi` writes and the `SubagentStop` hook of `rule-case-check` checks, judged by one function of `guppi/casecheck.py` that the check uses too (cases 453, 645.3) — and every `Edit`, `Write` and `MultiEdit` that names `case-guppi` on a file outside such a folder: exit 2 ``
>   - old: `` The one exception is a `Write` of a plan file that does not exist whose content, trimmed, is one line that opens with `# ` ``
>   - new: `` The exceptions are an `Edit`, `Write` or `MultiEdit` of `case-guppi` under `cases/`, and a `Write` of a plan file that does not exist whose content, trimmed, is one line that opens with `# ` ``
>   - old: `` The hooks of `rule-spec-write` and `rule-case-check` write the plan, the store and the files of `cases/` with no tool call, and this hook does not judge them; ``
>   - new: `` The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, and the old path of `rule-case-check` writes a file of `cases/` the same way until the writer is live; this hook does not judge them; ``
>   - change: `the guard lets case-guppi alone write under cases/, and refuses case-guppi anywhere else (case 645.3)`
> - [ ] update `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
>   - set:
>     ```
>     status: pending
>     purpose: 'An edit of the plan file or its store is refused, the one Write that creates the plan with its title line excepted, and so is an edit of a file of a built Case under cases/ by any agent but case-guppi, and any edit of case-guppi outside cases/'
>     method: 'uv run pytest tests/test_ratified.py -k guard; by hand in a later session, one probe Write of the main agent under cases/, refused and in the event log, and one file under cases/ written by case-guppi'
>     ```
>   - change: `the Criterion replaced whole — case-guppi alone writes under cases/ and is refused anywhere else; the purpose and the method follow (case 645.3)`
> - [ ] `guppi/ratified.py`: `guard_refusal` reads the agent type of the hook input; a file under `cases/` passes for `case-guppi` alone; an edit of `case-guppi` outside `cases/` is refused; the reason and the module docstring say the same.
> - [ ] `tests/test_ratified.py`: tests `-k guard` — a Write and an Edit of `case-guppi` under `cases/` pass; the same calls with no agent type or another one are refused; a Write of `case-guppi` outside `cases/` is refused.
> - [ ] read `estimate-spec-reconcile-refuses-an-edit-of-the-plan`

> **ratification:**
> ```
> - decision[case 645.3][update][rule-spec-reconcile]{ref:rule-spec-reconcile}
> - decision[case 645.3][update][estimate-spec-reconcile-refuses-an-edit-of-the-plan]{ref:rule-spec-reconcile}
> ```

### Case 645.4 — The Stop check refuses a showing whose file changed after its check

> **given:**
> `estimate-case-check-refuses-a-changed-case-file`: the new check of a showing whose file differs from the store.
> **＋** `rule-case-check`: the rule of the `Stop` check of a showing.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/materialize.py`: `split_cases`, the reading of the Cases of a text.
> **＋** `guppi/ratified.py`: the Spec hook, which imports the comparison.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, and `uv run guppi casecheck` reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

> **then:**
> The hook reads the Cases of that file by `split_cases` of `guppi/materialize.py` and compares each with the entry of the store under its id alone, line ends and trailing spaces aside.
> **＋** A Case of the file whose text differs from its entry, or that the store does not hold, exits 2 with a reason that names the Case and the file, joined with the other reasons of the hook.
> **＋** The comparison is one function of `guppi/casecheck.py`, which the Spec hook `guppi/ratified.py` imports.
> **－** A heading with no section, a fence tagged `DIFF` and a deferred decision in the short form are not compared, and no file is read for them.
> **－** On the re-fire (`stop_hook_active`) it exits 0, as the other checks of the same run do.

> **tasks:**
> - [ ] create `estimate-case-check-refuses-a-changed-case-file`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the Stop check refuses a showing of a Case whose file under cases/ differs from the text the store holds for it`
>   - method: `uv run pytest tests/test_casecheck.py -k changed_file`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: one function compares the Cases of a case file with the store; `stop` refuses a showing whose file differs; the module docstring says the same.
> - [ ] `tests/test_casecheck.py`: tests `-k changed_file` — a file equal to the store passes; a line changed after the store is refused with the Case and the file named; a Case of the file the store lacks is refused.
> - [ ] read `estimate-case-check-refuses-a-changed-case-file`

> **ratification:**
> ```
> - decision[case 645.4][create][estimate-case-check-refuses-a-changed-case-file]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 645.5 — The Spec hook writes nothing from a file changed after its check

> **given:**
> `estimate-spec-write-refuses-a-changed-case-file`: the new check of the Spec hook on a file that differs from the store.
> **＋** `rule-spec-write`: the rule of the Spec hook.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.
> **＋** `guppi/casecheck.py`: the comparison of a case file with the store.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the approved Spec the hook writes into.
> **＋** `estimate-spec-write-answers-a-refusal`: the write on a reply with `stop_hook_active` set, created by Case 644.
> **＋** `estimate-spec-write-tells-each-reason-once`: the guard that gives each reason once a stretch, created by Case 644.
> **＋** `raw/2026-10-05/0311/cases/case-644.md`: the ratified Case that changes the same hook and other sentences of the same rule page.

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, and reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

> **then:**
> The hook compares the Cases of that file with the entries of the store under their ids, by the one function of `guppi/casecheck.py` that the `Stop` check of a showing runs.
> **＋** A Case of the file that differs from its entry, or that the store does not hold: exit 2 with the reason on stderr, and nothing of Case N is written into the plan file or into `raw/<date>/<hi HHMM>/spec.md`.
> **＋** With `stop_hook_active` set, the hook compares and refuses as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a reason it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
> **－** A defer-only Case has no file and is not compared.

> **tasks:**
> - [ ] create `estimate-spec-write-refuses-a-changed-case-file`
>   - ref: `rule-spec-write`
>   - kind: `QA`
>   - purpose: `Whether the Spec hook writes nothing of a ratified Case whose file under cases/ differs from the text the store holds for it`
>   - method: `uv run pytest tests/test_ratified.py -k changed_file`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-spec-write`
>   - set: `{purpose: "Prevents a ratified Case from entering the Spec in other words than the Case case-guppi wrote into its file, whose given, when, then, tasks and ratification the person signed and the check of rule-case-check stored"}`
>   - old: `` Prevents a ratified Case from entering the Spec in other words than the answer of `case-guppi` whose `given`, `when`, `then`, `tasks` and `ratification` the person signed. ``
>   - new: `` Prevents a ratified Case from entering the Spec in other words than the Case `case-guppi` wrote into its file, whose `given`, `when`, `then`, `tasks` and `ratification` the person signed and the check of `rule-case-check` stored (case 645.5). ``
>   - old: `` it reads `<plan>.checked.json` for the answer of `case-guppi` stored under Case N by `rule-case-check`, ``
>   - new: `` it reads `<plan>.checked.json` for the text of the file of `case-guppi` stored under Case N by `rule-case-check` (case 645.5), ``
>   - old: `no such call made after the time of the store (case 452.3),`
>   - new: `` no such call made after the time of the store (case 452.3), a file of Case N whose Cases differ from the text the store holds under their ids or that the store does not hold, by the one comparison of `guppi/casecheck.py` that the `Stop` check of a showing runs (case 645.5), ``
>   - old: `a showing that differs from that answer in a section it shows`
>   - new: `a showing that differs from that stored text in a section it shows`
>   - change: `the hook copies the text of the file case-guppi wrote, as the check stored it, and writes nothing of a Case whose file differs from it; the purpose follows (case 645.5)`
> - [ ] `guppi/ratified.py`: before it writes Case N, the hook compares its case file with the store by the function of `guppi/casecheck.py`; the module docstring says the same.
> - [ ] `tests/test_ratified.py`: tests `-k changed_file` — a ratified Case whose file equals the store is written; a file changed after the store writes nothing and exits 2.
> - [ ] read `estimate-spec-write-refuses-a-changed-case-file`

> **ratification:**
> ```
> - decision[case 645.5][create][estimate-spec-write-refuses-a-changed-case-file]{ref:rule-spec-write}{tags:hooks,harness,workflow}
> - decision[case 645.5][update][rule-spec-write]{ref:rule-spec-write}
> ```

### Case 645.6 — The main agent shows a Case from the summary

> **given:**
> `rule-orchestration`: the rule whose Render is `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file the render writes.
> **＋** `rule-case-check`: its hook checks the file and refuses a showing.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `.claude/skills/grill-me/SKILL.md`: the template of a round.
> **＋** `.claude/skills/wait-what/SKILL.md`: the skill of a plain explanation.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**` and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case with its name in Russian and, under it, one list with an item per Case and sub-case of the summary `case-guppi` answered with: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it; a reply that shows a round and that the `Stop` check refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, never to build a Case, and asks a run again only to confirm its own findings.
> **－** The main agent writes the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` the file the `SubagentStop` hook of `rule-case-check` writes from the answer; ``
>   - new: `` the file `case-guppi` writes and the `SubagentStop` hook of `rule-case-check` checks; `case-guppi` answers with a summary of it — the path, then for each Case and sub-case its id, its name, the Estimate that checks it, its ledger lines and, when its `context` says another Case of the session should change instead, a line `**Other Case:**` — and the main agent writes the reply from the summary without reading the file (case 645.6); ``
>   - old: `` a Case whose `context` says that another Case of the session, which it was bounded around after a clash, should change instead ``
>   - new: `` a Case whose item in the summary carries a line `**Other Case:**`, since its `context` says that another Case of the session, which it was bounded around after a clash, should change instead, ``
>   - old: `` an answer with no Case heading and no first line `**Fact:**` is a round of questions ``
>   - new: `` an answer with no first line `**Built:**` and no first line `**Fact:**` is a round of questions ``
>   - change: `the main agent shows a built Case from the summary of case-guppi, its Other Case line included, and a round is an answer with neither a Built nor a Fact first line (case 645.6)`
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Case is shown from the summary of case-guppi, the file written by case-guppi, another Case asked about from the Other Case line, and a round known by no Built and no Fact first line (case 645.6)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 645.6][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 645.6][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```

### Case 645.7 — A letter outside the script holds a Case back from the showing and the Spec

> **given:**
> `estimate-case-check-refuses-a-letter-outside-the-script`: its Criterion and `purpose` are set anew.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/prespec.py`: `check_untranslated`, the language finding of pre-spec.
> **＋** `/pre-spec`: the skill whose check runs the same function.
> **＋** `guppi/config.py`: the table of languages.
> **＋** `guppi.toml`: sets `documentation_lang`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file and `guppi.toml`.

> **then:**
> A name, `context` or `problem` of a Case of the file that holds, outside a code span, a letter outside the script of the language `guppi.toml` sets as `documentation_lang`, or, inside a code span, a letter that is neither Latin nor of that script, is a finding of that Case, stored with the Case in `<plan>.checked.json`: the hook exits 2 with it on stderr, and `case-guppi` fixes the file.
> **＋** While such a finding stands, the store holds the Case with it, so the `Stop` check refuses its showing and the Spec hook writes nothing of it.
> **＋** A file whose names, contexts and problems hold no such letter gets no finding from this check.
> **＋** A Latin slug or path in a code span is no finding, whatever the documentation language.
> **＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`.
> **＋** The hook runs `check_untranslated` of `guppi/prespec.py`, the function `/pre-spec` runs, and holds no second copy of its judgment.
> **－** A file whose text `<plan>.checked.json` already holds with findings is stored again with this finding and exits 0, so an unchanged file is not sent back twice.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.

> **tasks:**
> - [ ] update `estimate-case-check-refuses-a-letter-outside-the-script`
>   - set:
>     ```
>     status: pending
>     purpose: 'A Case of case-guppi whose name, context or problem holds a letter outside the script of the documentation language, a Latin letter in a code span excepted, is a finding of the check, and the Case is not shown or written into the Spec while it stands'
>     ```
>   - change: `the Criterion replaced whole — the check reads the file case-guppi wrote, and a finding holds the Case back from the showing and the Spec instead of keeping a file unwritten; the purpose follows (case 645.7)`
> - [ ] `tests/test_casecheck.py`: tests `-k script` read a temp case file in place of an answer text.
> - [ ] read `estimate-case-check-refuses-a-letter-outside-the-script`

> **ratification:**
> ```
> - decision[case 645.7][update][estimate-case-check-refuses-a-letter-outside-the-script]{ref:rule-case-check}
> ```

### Case 645.8 — A note on a Criterion line goes back on the file

> **given:**
> `estimate-case-check-notes-a-criterion-line-not-carried`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/prespec.py` and `tests/test_prespec.py`: the notes and their tests.
> **＋** `guppi/materialize.py`: `names_a_part`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `uv run guppi casecheck --subagent` checks on `SubagentStop` the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that `case-guppi` wrote, or `uv run guppi prespec --check <plan>` checks the plan, and a Case of it holds an `update` of an Estimate that names no part of the page by `names_a_part` of `guppi/materialize.py`, and so replaces its `## Criterion` whole.

> **then:**
> The old Criterion is the `## Criterion` of the Estimate page as it stands. The new one is the Criterion the item writes under `sections`, or else the `when` and `then` of the Case that holds the item.
> **＋** Each line of the old Criterion that no line of the new one equals is a note that names the Case, the Estimate and the line. The operand at the head of a line, the labels `When:`, `Then:` and `Given:`, and whitespace are set aside.
> **＋** The notes of a Case are judged by functions of `guppi/prespec.py`, and `guppi/casecheck.py` imports them, not copies.
> **＋** `uv run guppi prespec --check <plan>` prints each note as a line opening with `note:`, which sets no exit code.
> **＋** `uv run guppi casecheck --subagent` exits 2 with the notes on stderr, beside any findings, and `case-guppi` changes the file: it restores the line, or it keeps the change and says why in `context`.
> **＋** It stores the notes it sent for each Case id in `<plan>.checked.json`, apart from the findings, and a later check of the same id keeps them.
> **－** A note that the store already holds for the same Case id is not sent again, and a check whose only notes are held exits 0.
> **－** A note is not a finding: the Case is stored with no finding for it, and the `Stop` check of `guppi casecheck` does not refuse a showing for a note.
> **－** An Estimate that a Case creates has no old Criterion and gets no note.

> **tasks:**
> - [ ] update `estimate-case-check-notes-a-criterion-line-not-carried`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the note goes back on the file case-guppi wrote, and a note writes no file since the hook writes none (case 645.8)`
> - [ ] `tests/test_casecheck.py`: tests `-k note` read a temp case file in place of an answer text.
> - [ ] read `estimate-case-check-notes-a-criterion-line-not-carried`

> **ratification:**
> ```
> - decision[case 645.8][update][estimate-case-check-notes-a-criterion-line-not-carried]{ref:rule-case-check}
> ```

### Case 645.9 — A number held by another agent is judged on the file

> **given:**
> `estimate-case-check-sends-back-a-case-number-held-by-another-agent`: its Criterion is replaced whole.
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape`: the count of a free number.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, `agent_id` of the payload, and `<plan>.checked.json`.

> **then:**
> The hook stores each Case of the file in `<plan>.checked.json` with the `agent_id` of the payload beside its text, its findings and the time of the store.
> **＋** A top-level Case N of the file is sent back when the store holds Case N, or a sub-case of it, under its number from an answer with another `agent_id`.
> **＋** Its message gives `case-guppi` a free number, counted as `estimate-case-check-sends-back-a-ratified-case-in-another-shape` counts it, to build the Case under, and the exit code is 2.
> **＋** Each Case of that file is stored apart, under its number joined with its `agent_id`, and the entry of the other agent under the number alone stays as it was.
> **＋** The Spec hook, the `Stop` comparison and the comparison of a case file with the store read the entry under the number alone.
> **－** An unchanged file whose text its entry apart already holds with this finding is stored again and exits 0, so it is not sent back twice.
> **－** An entry with no `agent_id`, stored before the change, gives no finding of this check, and neither does a file whose `agent_id` is the one of the entry under the number.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Cases are read from the file case-guppi wrote, and no hook writes the file from the entry (case 645.9)`
> - [ ] `tests/test_casecheck.py`: tests `-k subagent_clash` read a temp case file in place of an answer text.
> - [ ] read `estimate-case-check-sends-back-a-case-number-held-by-another-agent`

> **ratification:**
> ```
> - decision[case 645.9][update][estimate-case-check-sends-back-a-case-number-held-by-another-agent]{ref:rule-case-check}
> ```

### Case 645.10 — The form of a Case stands in the file case-guppi writes

> **given:**
> `estimate-case-protocol-case-form`: its Criterion is replaced whole.
> **＋** `rule-case-protocol`: the rule whose Render is `vault/wiki/case-schema.md`.
> **＋** `vault/wiki/case-schema.md`: the form of a Case.
> **＋** `rule-case-check`: its hook checks the file.
> **＋** `estimate-orchestration-shows-the-built-case`: the showing in the chat.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `make lint`: the check of the librarian's run.

> **when:**
> `case-guppi` writes a Case it built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the hook of `rule-case-check` checks it, and the main agent sends that file to the person, at its first showing or again.

> **then:**
> The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
> **＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** `tasks` holds no `by hand` box whose moment comes after Work Mode of the Case's own session — the librarian's run of that session or a later session; such a check stands as the reading of an Estimate or is left to the `make lint` of the librarian's run.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification` of `estimate-orchestration-shows-the-built-case`, and the reply ends with a plain question.
> **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
> **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.

> **tasks:**
> - [ ] update `estimate-case-protocol-case-form`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — case-guppi writes the file of the Case and the hook checks it (case 645.10)`
> - [ ] read `estimate-case-protocol-case-form`

> **ratification:**
> ```
> - decision[case 645.10][update][estimate-case-protocol-case-form]{ref:rule-case-protocol}
> ```

### Case 645.11 — A showing passes only when its file equals the store

> **given:**
> `estimate-case-check-shows-only-the-checked-case`: its Criterion is replaced whole.
> **＋** `estimate-case-check-refuses-a-changed-case-file`: the refusal of a showing whose file differs from the store, created in 645.4.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/ratified.py`: the Spec hook, which imports the comparison and the reading of a sending.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

> **then:**
> `uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line once line ends and trailing spaces are the same.
> **＋** Under the heading of a top-level Case, one `ratification` whose fence holds the ledger lines of its sub-cases, as the list of a showing holds them, is read as the showing of each sub-case whose id a line names: the lines that name that id are compared with the `ratification` of that sub-case in the store, and a stored line that is missing or a line the store lacks is a difference.
> **＋** A section the reply does not show is not compared: a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the stored text and `raw/<date>/<hi HHMM>/cases/case-<N>.md` equals the store, as `estimate-case-check-refuses-a-changed-case-file` sets it.
> **＋** The name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared.
> **＋** A Case the store does not hold, a Case that differs in a compared section, a Case stored with findings, a Case whose file differs from the store, or a Case with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2, the reason and the findings on stderr.
> **＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
> **＋** The Spec hook `guppi/ratified.py` judges a showing by the same comparison, and a sending by the same reading of the transcript, both imported from `guppi/casecheck.py`.
> **－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared and need no sending.
> **－** On the re-fire (`stop_hook_active`) it exits 0.

> **tasks:**
> - [ ] update `estimate-case-check-shows-only-the-checked-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a showing passes only when the file of the Case equals the store too (case 645.11)`
> - [ ] `tests/test_casecheck.py`: tests `-k stop` — a showing of `ratification` alone with a file changed after the store is refused.
> - [ ] read `estimate-case-check-shows-only-the-checked-case`

> **ratification:**
> ```
> - decision[case 645.11][update][estimate-case-check-shows-only-the-checked-case]{ref:rule-case-check}
> ```

### Case 645.12 — Each Case written into its file names what done means

> **given:**
> `estimate-case-build-answers-what-done-means`: its Criterion is replaced whole.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `rule-case-build`: the rule of the agent.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.

> **when:**
> `case-guppi` writes a Case into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`.

> **then:**
> Each Case and sub-case of the file creates an Estimate or replaces the Criterion of one, or its `context`, or its parent's, names by slug the Estimate that already checks the change and says why its Criterion stands.
> **＋** The summary that `case-guppi` answers with names that Estimate under the item of each Case and sub-case.
> **＋** When the person's words and the frame give neither, `case-guppi` asks in a round, before it writes the Case, what the Estimate will check, and the `recommend` of the Case holds that question.
> **－** A deferred decision in the short form is not written by `case-guppi` and carries no such Estimate.

> **tasks:**
> - [ ] update `estimate-case-build-answers-what-done-means`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Case is written into its file, and the summary names the Estimate of each Case (case 645.12)`
> - [ ] read `estimate-case-build-answers-what-done-means`

> **ratification:**
> ```
> - decision[case 645.12][update][estimate-case-build-answers-what-done-means]{ref:rule-case-build}
> ```

### Case 645.13 — The recommend of a Case written into its file records the rounds

> **given:**
> `estimate-case-build-records-the-rounds-in-recommend`: its Criterion is replaced whole.
> **＋** `estimate-case-check-requires-each-question-of-the-rounds`: the check of each title. Unchanged.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `rule-case-build`: the rule of the agent.
> **＋** `vault/wiki/case-schema.md`: the form of a Case, rendered from `rule-case-protocol`.
> **＋** `rule-case-protocol`: the rule of the form.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.

> **when:**
> `case-guppi` writes a Case into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, with a sub-item `Recommended:` with what the agent recommended and a sub-item `Answer:` with the person's answer in English, both as they stood when the person answered that question.
> **＋** A later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer.
> **＋** A question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it.
> **＋** A question the person left unanswered is asked again in the next round under the same title; a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did.
> **＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
> **＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
> **＋** An item whose answer changed only one sub-case stands in the parent's `recommend` or in a `recommend` under that sub-case's heading; every other item stands in the parent's `recommend`.
> **＋** A Case with sub-cases carries `problem` on the parent only.
> **－** No item quotes the person's words word for word.
> **－** The promise of `estimate-case-check-requires-each-question-of-the-rounds` stands: each question title of the rounds has an item.

> **tasks:**
> - [ ] update `estimate-case-build-records-the-rounds-in-recommend`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — its moment is the Case written into its file (case 645.13)`
> - [ ] read `estimate-case-build-records-the-rounds-in-recommend`

> **ratification:**
> ```
> - decision[case 645.13][update][estimate-case-build-records-the-rounds-in-recommend]{ref:rule-case-build}
> ```

### Case 645.14 — A backlog item is judged on the file

> **given:**
> `estimate-case-check-requires-a-backlog-item-decided-on-its-page`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/prespec.py`: `decided_on_its_page`, the judgment of pre-spec.
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, and the pages of the vault.

> **then:**
> For each open line of the Frontier whose source is `backlog`, each page that its title names in a code span and that carries `deferred_by` is checked against each top-level Case N of the file that, itself or through a sub-case, names that page on a decision line other than a `defer`.
> **＋** Case N gets a finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases in the file both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and the missing mark. The hook exits 2, and `case-guppi` fixes the file.
> **＋** The judgment is the function of `guppi/prespec.py` that the pre-spec check runs, imported, not copied.
> **－** A Case of the file that names no such page, a file while no open line of the source `backlog` stands, and a page without `deferred_by` get no finding of this check.

> **tasks:**
> - [ ] update `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Cases are read from the file case-guppi wrote (case 645.14)`
> - [ ] `tests/test_casecheck.py`: tests `-k backlog` read a temp case file in place of an answer text.
> - [ ] read `estimate-case-check-requires-a-backlog-item-decided-on-its-page`

> **ratification:**
> ```
> - decision[case 645.14][update][estimate-case-check-requires-a-backlog-item-decided-on-its-page]{ref:rule-case-check}
> ```

### Case 645.15 — A ratified Case in another shape is judged on the file

> **given:**
> `estimate-case-check-sends-back-a-ratified-case-in-another-shape`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

> **then:**
> For a file that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
> **＋** Case N gets a finding when a number of its family that has such a line has no section in the file, or when a number that has such a line has a sub-case in the file.
> **＋** The finding names each such number and a new number: one above the highest top-level Case number that the decision lines of the session's ledger and the keys of `<plan>.checked.json` hold.
> **＋** The finding tells `case-guppi` to build the Case under the new number. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr, and `case-guppi` fixes the file or writes the Case under the new number.
> **＋** The judgment and the new number come from one function of `guppi/casecheck.py`.
> **－** An answer on the old path that holds sub-cases of Case N without Case N gets no finding of this check.
> **－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Cases are read from the file case-guppi wrote (case 645.15)`
> - [ ] `tests/test_casecheck.py`: tests `-k shape` read a temp case file in place of an answer text.
> - [ ] read `estimate-case-check-sends-back-a-ratified-case-in-another-shape`

> **ratification:**
> ```
> - decision[case 645.15][update][estimate-case-check-sends-back-a-ratified-case-in-another-shape]{ref:rule-case-check}
> ```

### Case 645.16 — The prompt in Plan Mode binds the main agent, not case-guppi

> **given:**
> `rule-permissions`: the rule of the allow list of `.claude/settings.json`.
> **＋** `estimate-permissions`: its Criterion is replaced whole.
> **＋** `.claude/settings.json`: its allow list. Unchanged.
> **＋** `.claude/agents/case-guppi.md`: sets `permissionMode: acceptEdits`, as 645.1 sets it.
> **＋** `tests/test_render.py`: fixes the shape of the block.
> **＋** `rule-spec-reconcile`: its guard keeps `case-guppi` inside `cases/`.
> **＋** `vault/raw/**`: the folder of the working files of a session.
> **＋** `vault/wiki/brief.md`: the brief of the session.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, and Edit and Write for `vault/wiki/brief.md`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** `case-guppi` writes the file of its Case in the mode `permissionMode: acceptEdits` of `.claude/agents/case-guppi.md`, with no prompt in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/`.
> **＋** A prompt in Plan Mode, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed, and no path under `cases/` is on the allow list.

> **tasks:**
> - [ ] update `rule-permissions`
>   - old: `in Plan Mode the client asks before every edit outside the plan file all the same, the person approves, and whether it asked is the person's word, never the agent's, which cannot see the prompt (case 237).`
>   - new: `` in Plan Mode the client asks before every edit of the main agent outside the plan file all the same, the person approves, and whether it asked is the person's word, never the agent's, which cannot see the prompt (case 237). The file of a built Case under `cases/` is not on the list: `case-guppi` writes it in the mode `permissionMode: acceptEdits` of its agent file, which Claude Code keeps for a subagent while the session is in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/` (case 645.16). ``
>   - change: `the prompt in Plan Mode binds the main agent; case-guppi writes its Case file in permissionMode acceptEdits, with no allow rule (case 645.16)`
> - [ ] update `estimate-permissions`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the prompt in Plan Mode binds the main agent, and case-guppi writes its Case file with no prompt and no allow rule (case 645.16)`
> - [ ] read `estimate-permissions`

> **ratification:**
> ```
> - decision[case 645.16][update][rule-permissions]{ref:rule-permissions}
> - decision[case 645.16][update][estimate-permissions]{ref:rule-permissions}
> ```
