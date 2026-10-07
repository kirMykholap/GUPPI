## Case 698 — `case-guppi` reads the saved transcripts in its own permission mode

> **context:**
> Claude Code asks the person before an agent reads a file outside the project folder, unless a rule of the allow list or the permission mode of the agent lets the call run. Today `case-guppi` runs in `permissionMode: acceptEdits`, set by the Render of `rule-case-build`, so it writes its Case file with no prompt. Its reads of this project's saved transcripts, under `~/.claude/projects/c--PROJECTS-GUPPI`, rest on two read rules of the allow list of `rule-permissions`, added by cases 656 and 693. The person was still asked for read permission while `case-guppi` built Case 696 of this session, and said the prompt came after the builder started, so the call that asked was the builder's. The person chose that `case-guppi` runs in the mode `auto`. The modes Claude Code reports are listed in `guppi/event.py`: `default`, `acceptEdits`, `auto`, `dontAsk` and `bypassPermissions`. The archived file of case 645 quotes the subagents page of the Claude Code documentation: in Plan Mode a subagent "runs in the permission mode you set, except `bypassPermissions`". I could not read that documentation, so this Case does not say what `auto` does for a subagent beyond what the vault records.
>
> This Case is built again under its own number, as Case 696 was. As first ratified it removed both read rules; pre-spec found that this puts every read of `case-guppi` there, and the write of its Case file, under the verdict of the classifier of Claude Code. Three pages record that verdict. `insight-hi-skill-substitution-checked-by-a-model-call`, `actioned`, says that when the server of the classifier gives no verdict the call is refused, and that a call a permission rule allows needs no verdict. `lesson-permissions-auto-mode-refuses-a-remote-change-despite-the-chat`, `new`, says that the classifier judges the action against the permission rules of the settings. `rule-skill-hi` says that a `!` command of `/hi` that no rule allows is refused, and that a matching rule needs no classifier. At pre-spec the person chose to keep both read rules beside `auto`: a read they match passes with no verdict, and a call they do not match is judged by `auto` with no prompt to the person. So 698.2 keeps the allow list as it stands and changes only the sentences of `rule-permissions` that name the mode, and the Criterion of `estimate-permissions` checks both paths. The `purpose` and Purpose of `rule-morph`, which say its initiation at install sets the folder name in those rules, stay true. Its update in 698.2 therefore changes no text and carries only a `change` line for its History, which records that the rules it names stay; that keeps the ledger line of 698.2 on `rule-morph` matched by an item of this text. The Frontier line A1 of this session, which asks whether a search of a subagent under the read rules runs with no prompt, stands, and the new `method` of `estimate-permissions` keeps its question. The write of the Case file has no allow rule, so in `auto` it is judged by the classifier; whether it still runs with no prompt is the person's word.
>
> Whether a call asks is the person's word, since only the person can see a prompt (`lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt`). A rendered file changes at the librarian's render after the session, so the new mode holds from the next session. The person chose that the promise sits in `estimate-permissions`, which stays `pending` until the person's word in that session; its `method` is set anew, and like the method case 693 set, it waits for a later session, which pre-spec reports (case 670.4). Case 698.1 replaces the Criterion of `estimate-case-build-writes-the-case`, whose line on the mode names `acceptEdits`. It is written whole under `sections`, with that line alone changed, and the page goes back to `pending`. Its `purpose` and `method` do not name the mode and stand. The check of the file notes lines of the old Criteria that the new ones do not carry; each is the line on the mode, changed on purpose, and in `estimate-permissions` the line of the Case-file write, which leaves the mode and the guard to 698.1 and adds that a read no rule matches runs with no prompt.
>
> What the frame showed, by these searches:
> - A Grep `acceptEdits` over the repository, with the glob `!vault/{raw,archive}/**`, printed `guppi/event.py`, `tests/test_event.py`, `vault/wiki/estimates/estimate-case-protocol-case-form.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md`, `vault/wiki/estimates/estimate-event-log-records.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/log.md`, `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-permissions.md` and `vault/wiki/estimates/estimate-permissions.md`. `guppi/event.py`, `tests/test_event.py` and `estimate-event-log-records` list the modes in which `/hi` is refused, and they stand. The hit in `estimate-case-protocol-case-form` is in its Result, a record of a past reading, and it stands. I did not read `log.md`. The rest enter the Case.
> - A Grep `permissionDecision|allow list|without asking|permission prompt|permissionMode` over `vault/wiki/rules/` printed `rule-permissions.md`, `rule-morph.md` and `rule-case-build.md`, and over `.claude/` printed `.claude/agents/case-guppi.md`. The pattern does not match `rule-skill-hi`, which sets, through `allowed-tools`, whether the `!` commands of `/hi` ask; this Case does not touch those commands, and no other rule that the search printed sets whether a call of `case-guppi` asks.
> - A Grep `PROJECTS-GUPPI|projects|permissionMode|Read\(` over `tests/` printed nothing. The JSON cases of `tests/test_render.py` use an allow list of their own, so no test changes.
>
> Cases 696, 697 and 699 of this session change none of the pages of this Case.

> **problem:**
> `case-guppi` still makes the client ask the person for permission when it reads this project's saved transcripts, though two read rules of the allow list were meant to stop that.

> **recommend:**
> - **Whose prompt the Case removes**
>   - Recommended: (a) the builder only, and say whether the prompt came before or after the builder started.
>   - Answer: (a); the prompt came after the builder started.
> - **Which mode the builder runs in**
>   - Recommended: (a) `auto`.
>   - Answer: (a).
> - **Whether the two read rules stay in the allow list**
>   - Recommended: (a) keep both rules.
>   - Answer: (b), remove both rules.
> - **Which check says the change is done**
>   - Recommended: (a) the promise sits in `estimate-permissions`; `estimate-case-build-writes-the-case` names the new mode and goes back to pending.
>   - Answer: (a).
> - **Change**
>   - Asked: at pre-spec, a call that no permission rule allows is judged by the classifier, which refuses it when its server gives no verdict; the person chose to keep both read rules beside `auto`.
>   - Taken: both read rules stay in the allow list; a read they match passes with no verdict, and a call they do not match is judged by `auto` with no prompt; the update of `rule-morph` changes no text and keeps only a `change` line, and the Case is built again under its own number.

### Case 698.1 — `case-guppi` runs in the mode `auto`

> **given:**
> `rule-case-build`: the rule whose Render is the agent file of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the agent file, which sets the permission mode of `case-guppi`.
> **＋** `estimate-case-build-writes-the-case`: the check of the agent file, whose Criterion is replaced whole.
> **＋** `rule-spec-reconcile`: its guard keeps the writes of `case-guppi` inside `cases/`.

> **when:**
> The main agent dispatches `case-guppi` from `.claude/agents/case-guppi.md`, in a session after the render of `rule-case-build`.

> **then:**
> `.claude/agents/case-guppi.md` sets `permissionMode: auto`.
> **＋** Its model, effort, tools and skills stay as they are.
> **＋** The guard of `rule-spec-reconcile` refuses a write of `case-guppi` outside `cases/` in that mode too.
> **－** The mode of `.claude/agents/case-guppi.md` sets no mode of the main agent.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `permissionMode: acceptEdits`
>   - new: `permissionMode: auto`
>   - change: `case-guppi runs in permissionMode auto instead of acceptEdits, so that a call no rule of the allow list matches is judged by that mode with no prompt (case 698)`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
>     **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
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
>     **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
>     **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
>     **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
>     **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
>     **－** It does not write the whole Case again to fix a finding or make a change.
>     **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
>     **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
>     **－** It writes no file but the file of its Case, and no ledger line.
>     ```
>   - change: `the Criterion replaced whole — case-guppi runs in permissionMode auto; the other lines stand (case 698)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 698.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 698.1][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> ```

### Case 698.2 — The read rules stay beside the mode `auto`

> **given:**
> `rule-permissions`: the rule of the allow list, whose Render is the allow list of `.claude/settings.json`.
> **＋** `estimate-permissions`: the check of the allow list and of the prompts of `case-guppi`, whose Criterion is replaced whole.
> **＋** `.claude/settings.json`: the rendered settings that hold the allow list.
> **＋** `tests/test_render.py`: its JSON case fixes the shape of the rendered block.
> **＋** `.claude/agents/case-guppi.md`: the agent file of `case-guppi`, which sets its permission mode.
> **＋** `rule-spec-reconcile`: its guard keeps the writes of `case-guppi` inside `cases/`.
> **＋** `rule-morph`: the draft rule of the initiation at install, whose History records that the read rules it names stay.
> **＋** `~/.claude/projects/c--PROJECTS-GUPPI`: the folder of this project's saved transcripts, outside the repository.
> **＋** `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`: the read rules for that folder and for what lies inside it.
> **＋** `vault/raw/**`: the folders of the sessions, which hold their working files.
> **＋** `cases/`: the folder of a session that holds the files of its Cases.
> **＋** `vault/wiki/brief.md`: the brief, which `/carry` rewrites.
> **＋** `vault/wiki/`: the live pages of the vault.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder `~/.claude/projects/c--PROJECTS-GUPPI` itself as its path, or a path under it.
> **＋** Or `case-guppi` calls Read, Grep or Glob on a path outside the project that no rule of the allow list names.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** A Read, Grep or Glob whose path is `~/.claude/projects/c--PROJECTS-GUPPI` itself or a path under it runs with no prompt, in Plan Mode too.
> **＋** `case-guppi` writes the file of its Case with no prompt in Plan Mode, and its Read, Grep or Glob on a path outside the project that no rule of the allow list names runs with no prompt to the person.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `vault/wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names `~/.claude/projects/c--PROJECTS-GUPPI`.

> **tasks:**
> - [ ] update `rule-permissions`
>   - old: `` `case-guppi` writes it in the mode `permissionMode: acceptEdits` of its agent file, ``
>   - new: `` `case-guppi` writes it in the mode `permissionMode: auto` of its agent file (case 698), ``
>   - old: `and whether a search there still asks is the person's word (case 656).`
>   - new:
>     ```
>     and whether a search there still asks is the person's word (case 656). A call of `case-guppi` that these rules do not match is judged by its mode `permissionMode: auto`, with no prompt to the person, and a call they match needs no verdict of the classifier of Claude Code, which refuses a call when its server gives none (case 698).
>     ```
>   - change: `case-guppi runs in permissionMode auto; the read rules of the saved transcripts stay, and a call they do not match is judged by that mode (case 698)`
> - [ ] update `estimate-permissions`
>   - set:
>     ```
>     status: pending
>     method: the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of work.md in Work Mode, recorded in the estimate line; the live probe of the transcripts and of the mode of case-guppi is the person's word on the client's prompt, in a session after the librarian's render, at a Grep of a subagent whose path is the folder ~/.claude/projects/c--PROJECTS-GUPPI itself and at one whose path is a file under it, at the Write of the Case file of case-guppi, and at a Read of case-guppi on a path outside the project that no rule names, recorded in the estimate line — never the agent's, which cannot see the prompt; the Estimate stays pending until the person gives that word
>     ```
>   - change: `the Criterion replaced whole — case-guppi runs in permissionMode auto beside the read rules of the saved transcripts, and a call they do not match is judged by that mode with no prompt (case 698)`
> - [ ] update `rule-morph`
>   - change: `the read rules of rule-permissions that its initiation at install names stay, beside the mode auto of case-guppi; no text changes (case 698)`
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-permissions`

> **ratification:**
> ```
> - decision[case 698.2][update][rule-permissions]{ref:rule-permissions}
> - decision[case 698.2][update][estimate-permissions]{ref:rule-permissions}
> - decision[case 698.2][update][rule-morph]{ref:rule-morph}
> ```
