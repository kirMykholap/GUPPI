## Case 656 — The builder of a Case reads this project's saved transcripts with no prompt

> **context:**
> `case-guppi` builds each Case in the mode `permissionMode: acceptEdits` of its agent file, set by case 645.1, so it writes the file of its Case with no prompt while the session is in Plan Mode. The allow list of `.claude/settings.json`, the Render of `rule-permissions`, holds only Edit and Write rules for the session's working files, and no rule for a read outside the project. Claude Code keeps the transcripts of past sessions outside the project, under `~/.claude/projects/c--PROJECTS-GUPPI/`. In this session, as the main agent read in the subagent transcripts, the builders of Cases 654 and 655 searched the transcripts of sessions 0109 and 0311 there to check a past reading, and the person was asked to allow those searches. The person first proposed to remove `acceptEdits`, since the builder ran with no mode line before. Before case 645.1 the builder wrote no file. Without the line it runs in Plan Mode, where Claude Code lets an agent change only its plan file, so its write of the Case file would ask or be refused. The person then chose to keep `acceptEdits` and allow reads of this project's transcript folder alone.
>
> The Case adds `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)` to the allow list. This rests on the Claude Code docs as a guide agent paraphrased them for the main agent; this Case fetched nothing. On that reading, an allow rule with a home path `~/` is valid, a `Read` rule applies to Grep and Glob best-effort, and the docs do not say whether `acceptEdits` alone asks before a read outside the working folder. So the live check is the person's word in the next session on whether a search of `case-guppi` in that folder asked. If it still asks, the person's word fails the reading, and a later Case can add the folder through `permissions.additionalDirectories` instead. The rule applies to every agent of this project, the main agent too. The `/hi` step that takes a reading from the transcript of an earlier session reads the same folder. The person chose a check on the searches of the builder, so the new Criterion judges only those, and the new sentence of `rule-permissions` gives the builder's searches as the reason and says only that the rule covers the other agents too. Whether a read of the main agent at `/hi` still asks is left unchecked, and this Case does not promise it. The Criterion of `estimate-hi-takes-its-readings` judges what `/hi` reads and writes, not whether the client asked, so it stands. The Purpose of `rule-settings` says the file carries what may be written without a question, which the block of `rule-permissions` owns; a pair on it adds reads, as the ask-guppi run at pre-spec found. The purpose of `rule-permissions` and the first sentence of its Purpose say that the list allows writes of the session's working files and nothing else, so this Case sets the purpose anew and adds a sentence on the transcripts. The Criterion of `estimate-permissions` lists the allow list whole, so it is replaced whole. Its `method` names one live probe, a Write of `work.md`, so the same `update` sets the method anew with the new probe. The page has no `purpose` field. The Case leaves `rule-case-build` and `estimate-case-build-writes-the-case` as they stand, because the mode line stays `acceptEdits`. The Case also leaves the guard of Case 650, because it judges only writes. The Case creates no page, so no vault query was run.
>
> The searches this Case rests on. A Grep of `rule-permissions` over the repository, with the glob `!**/decisions/** !vault/archive/** !vault/raw/**`, printed 9 files: `vault/wiki/brief.md`, `.claude/skills/hi/SKILL.md`, `vault/wiki/log.md`, `vault/wiki/insights/insight-session-vault-knowledge-not-loaded.md`, `vault/wiki/rules/rule-permissions.md`, `vault/wiki/rules/rule-settings.md`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/estimates/estimate-permissions.md` and `vault/wiki/estimates/estimate-settings.md`. `rule-permissions` and `estimate-permissions` enter the Case. `.claude/skills/hi/SKILL.md` and its Render page `rule-skill-hi` name the rule for the write of `frontier.md` in Plan Mode, which stays true. The hits in `rule-settings` and `estimate-settings` name the rule as a child of `settings.json` and its place in the order, which stays true; the Purpose of `rule-settings` enters the Case for the reason above. The hit in the Insight is a History line. The brief and the log are not read. A Grep of `\.claude/projects|\.claude\\\\projects` over the repository, with the glob `{vault/wiki/rules/**,.claude/**} !**/decisions/**`, printed nothing, so no rule or harness file sets what happens at a read of that folder.
>
> The check sent back notes, and they stand. Three lines of the old Criterion of `estimate-permissions` are not carried word for word, and each changed on purpose. The line on the allow list now ends with the new `Read` rule. The line on a prompt in Plan Mode was a `＋` line and is now a `－` line, and it names an edit of the main agent, so that a prompt on a search of `case-guppi` in the transcript folder fails the reading. The line on `deny` and `ask` now also says that no other path outside the project is on the list, and that no Edit or Write rule names the transcript folder.
>
> Not done: the folder name holds the path of this project on this machine; a clone at another path would need the rule changed.

> **problem:**
> A builder that searches the saved transcripts of past sessions stops on a permission prompt for each call. The question was how those reads stop asking, and whether the mode line of the builder stays.

> **recommend:**
> - **How the builder's reads of past transcripts stop asking you**
>   - Recommended: (a) allow reading this project's transcript folder by one allow rule in the project settings, and keep `acceptEdits`.
>   - Answer: none of the options; the person proposed to remove `acceptEdits`, since the builder ran with no mode line before and nothing asked, and to check that. The later question Whether to remove the builder's mode line, given that the builder now writes its own file took this up.
> - **Whether to remove the builder's mode line, given that the builder now writes its own file**
>   - Recommended: (b) keep the line and allow reading this project's transcript folder; the check is the person's word in the next session on whether a builder's search of past transcripts asked.
>   - Answer: agreed, (b).

> **given:**
> `rule-permissions`: the allow list of `.claude/settings.json` and why it holds what it holds.
> **＋** `estimate-permissions`: its Criterion is replaced whole.
> **＋** `.claude/settings.json`: the rendered settings of the project.
> **＋** `~/.claude/projects/c--PROJECTS-GUPPI/`: the saved transcripts of this project.
> **＋** `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`: the new allow rule for reading that folder.
> **＋** `.claude/agents/case-guppi.md`: the agent file with `permissionMode: acceptEdits`. Unchanged.
> **＋** `vault/raw/**`: the session folders that hold the working files on the allow list. Unchanged.
> **＋** `vault/wiki/brief.md`: the brief, on the allow list. Unchanged.
> **＋** `wiki/`: the live pages, none of them allowed but the brief. Unchanged.
> **＋** `cases/`: the folder of the Case files, off the allow list. Unchanged.
> **＋** `rule-spec-reconcile`: the guard that keeps the writes of `case-guppi` inside `cases/`. Unchanged.
> **＋** `tests/test_render.py`: the JSON case that fixes the shape of the block. Unchanged.
> **＋** `rule-settings`: its Purpose names what the block of `rule-permissions` carries.
> **＋** `estimate-hi-takes-its-readings`: the check of the reads of `/hi` from past transcripts. Unchanged.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or `case-guppi` calls Read, Grep or Glob on a saved transcript of this project under `~/.claude/projects/c--PROJECTS-GUPPI/`.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** `case-guppi` writes the file of its Case in the mode `permissionMode: acceptEdits` of `.claude/agents/case-guppi.md`, with no prompt in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/`.
> **＋** A Read, Grep or Glob of `case-guppi` under `~/.claude/projects/c--PROJECTS-GUPPI/` runs with no prompt, in Plan Mode too.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names `~/.claude/projects/c--PROJECTS-GUPPI/`.

> **tasks:**
> - [ ] update `rule-permissions`
>   - set:
>     ```
>     purpose: Lets the session write its own working files and read this project's saved transcripts without asking, and nothing else
>     ```
>   - old: `Lets the session write its own working files without asking, and nothing else.`
>   - new: `Lets the session write its own working files and read this project's saved transcripts without asking, and nothing else.`
>   - old: `` and the guard of `rule-spec-reconcile` keeps it inside `cases/` (case 645.16). ``
>   - new: `` and the guard of `rule-spec-reconcile` keeps it inside `cases/` (case 645.16). The saved transcripts of this project, under `~/.claude/projects/c--PROJECTS-GUPPI/` outside the repository, are on the list for reading only: `case-guppi` checks a past reading in them, and a prompt on each of its searches buys nothing; the rule covers every agent of the project, and Claude Code applies a `Read` rule to Grep and Glob best-effort, and whether a search there still asks is the person's word (case 656). ``
>   - old: `"Write(vault/wiki/brief.md)"`
>   - new:
>     ```
>     "Write(vault/wiki/brief.md)",
>           "Read(~/.claude/projects/c--PROJECTS-GUPPI/**)"
>     ```
>   - change: `this project's saved transcripts under ~/.claude/projects join the allow list for reading, so a search of case-guppi there does not ask (case 656)`
> - [ ] update `estimate-permissions`
>   - set:
>     ```
>     status: pending
>     method: "the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probes are the person's word on the client's prompt at a Write of work.md in Work Mode, and at a Read, Grep or Glob of case-guppi under ~/.claude/projects/c--PROJECTS-GUPPI/ in a session after the render, each recorded in the estimate line — never the agent's, which cannot see the prompt"
>     ```
>   - change: `the Criterion replaced whole — the allow list holds a Read rule for this project's saved transcripts, and a search of case-guppi there runs with no prompt (case 656)`
> - [ ] update `rule-settings`
>   - old: `what may be written without a question`
>   - new: `what may be written or read without a question`
>   - change: `the block of rule-permissions also carries what may be read without a question (case 656)`
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-permissions`

> **ratification:**
> ```
> - decision[case 656][update][rule-permissions]{ref:rule-permissions}
> - decision[case 656][update][estimate-permissions]{ref:rule-permissions}
> - decision[case 656][update][rule-settings]{ref:rule-settings}
> ```
