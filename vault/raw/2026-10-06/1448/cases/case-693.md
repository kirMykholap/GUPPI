## Case 693 — The read rule for the saved transcripts covers their folder itself

> **context:**
> The allow list of `.claude/settings.json`, rendered from `rule-permissions`, lets every agent read this project's saved transcripts without a prompt through one rule, `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`, added by case 656 so that `case-guppi` can search them. In this session the person saw the client ask for permission at a Grep of a subagent, and confirmed that the prompt named the transcripts folder. The transcript of the subagent `case-guppi` of this session, `agent-a31d1300c6c7c12ad.jsonl`, shows two Greps there: one whose path was the folder itself, sent at 21:19:46 and answered at 21:20:10, and one whose path was a file under it, answered after 3 seconds; the Greps of the subagent of Case 691 over `vault/wiki/rules/` and the repository root whose times were read, in its transcript `agent-aa462e55a2a73f942.jsonl`, were answered in under a second, so the hook `guppi grepguard`, which adds the Decision-page filter to a Grep over the wiki and decides no permission, did not cause the wait. A likely cause, not proven, is that a rule ending in `/**` names what lies inside the folder and not the folder itself; the Purpose of `rule-permissions` already says that Claude Code applies a `Read` rule to Grep and Glob best-effort. The person chose a second read rule that names the folder itself, beside the present one, and nothing else on the allow list. The folder name follows where this repository sits on the person's disk, `C:\PROJECTS\GUPPI`; on another install both rules match nothing. The person chose to leave that not done here: it waits for `rule-morph`, the draft rule of the initiation at install, deferred by case 239, whose `purpose` named only the category set; at pre-spec the person chose that this Case widens that `purpose` to the name of the transcripts folder in the read rules, and the Purpose of `rule-permissions` points there. The defer of `rule-morph` stands, since this Case does not take it up; `rule-guppi-config` already says that the questions asked at install stay with `rule-morph` and stays true; `vault/wiki/backlog.md` is rendered from the pages by `guppi backlog` and follows the new `purpose` at its next run. A Grep `rule-morph` over `vault/wiki/` printed `vault/wiki/brief.md` and `vault/wiki/log.md`, not read, `vault/wiki/backlog.md`, `vault/wiki/entities/entity-sprint-migration.md`, whose line names the category set as case 239 set it and stays true, and `vault/wiki/rules/rule-guppi-config.md`. The Criterion of `estimate-permissions` speaks of a search under the folder and leaves the folder itself unclear, so this Case replaces it whole and sets its `method` anew. A file rendered from a Rule page changes at the librarian's render after the session (case 690.2), so no search of this session runs under the new rule: at pre-spec the person chose that the live probe is the person's word in a session after the librarian's render, and the Estimate stays `pending` until then. `estimate-orchestration-says-when-a-rendered-change-lands` checks that the reply that acknowledges such a Case says so; its Criterion speaks of that reply, which this Case does not change, so it stands. A Grep `permissionDecision|allow list|without asking|permission prompt` over `vault/wiki/rules/` and `.claude/` printed only `vault/wiki/rules/rule-permissions.md`, so no other rule sets whether a tool call asks. A Grep `c--PROJECTS-GUPPI|saved transcript` over `.claude/`, `vault/wiki/`, `guppi/` and `tests/` printed `.claude/settings.json`, `vault/wiki/log.md`, not read, `vault/wiki/lessons/lesson-transcript-keeps-the-text-before-a-tool-call.md`, whose hit is its `source` field and stands, `vault/wiki/rules/rule-permissions.md` and `vault/wiki/estimates/estimate-permissions.md`; no frame text and no test names the folder, so no test changes. Case 691 of this session changes `rule-ledger-write` and the ledger hook, and touches neither page of this Case.

> **problem:**
> A search whose path is the saved transcripts folder itself still makes the client ask for permission, though the allow list was meant to let every search there run without a prompt.

> **recommend:**
> - **Which search asked for permission**
>   - Recommended: (a) the records folder if the prompt named the `.claude\projects` path, otherwise (c), treat the records folder as the cause.
>   - Answer: (a), the records folder.
> - **How a search of the records folder stops asking**
>   - Recommended: (a) a second read rule for the folder itself, beside the present one.
>   - Answer: agreed, (a); with the note that these allow rules name the person's own folders and system, so another install of guppi would need its own.
> - **The allow rule on another person's machine**
>   - Recommended: (a) the rule for this machine now; `context` and the Purpose of `rule-permissions` say that another install needs its own folder name, which waits for `rule-morph`.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) replace the Criterion of `estimate-permissions` so it names the folder itself and everything inside it, checked by the person's word in Work Mode of this session after the render.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, the live probe of `estimate-permissions` cannot run in Work Mode of this session, since a rendered file changes at the librarian's render after the session; the person chose that the probe runs in a session after the librarian's render, the Estimate staying `pending` until then.
>   - Taken: the `method` of `estimate-permissions` names a session after the librarian's render and the person's word there.
> - **Change**
>   - Asked: at pre-spec, the `purpose` of `rule-morph` names only the category set, not the questions of the install; the person chose that this Case widens it to the name of the transcripts folder in the allow list.
>   - Taken: an `update` of `rule-morph` widens its `purpose` and its Purpose, and the new text of `rule-permissions` says that its initiation at install sets the folder name.

> **given:**
> `rule-permissions`: the rule of the allow list, whose Render is the allow list of `.claude/settings.json`.
> **＋** `estimate-permissions`: the check of the allow list, whose Criterion is replaced whole.
> **＋** `.claude/settings.json`: the rendered settings, whose allow list names the working files of the session under `vault/raw/**` and `vault/wiki/brief.md`.
> **＋** `tests/test_render.py`: its JSON case fixes the shape of the rendered block.
> **＋** `rule-morph`: the draft rule of the initiation at install, whose `purpose` is widened.
> **＋** `.claude/agents/case-guppi.md`: the agent file of `case-guppi`, which sets its permission mode.
> **＋** `rule-spec-reconcile`: its guard keeps the writes of `case-guppi` inside `cases/`.
> **＋** `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`: the read rules for `~/.claude/projects/c--PROJECTS-GUPPI`, the folder of this project's saved transcripts, and for what lies inside it.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder `~/.claude/projects/c--PROJECTS-GUPPI` itself as its path, or a path under it.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** `case-guppi` writes the file of its Case in the mode `permissionMode: acceptEdits` of `.claude/agents/case-guppi.md`, with no prompt in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/`.
> **＋** A Read, Grep or Glob whose path is `~/.claude/projects/c--PROJECTS-GUPPI` itself or a path under it runs with no prompt, in Plan Mode too.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names `~/.claude/projects/c--PROJECTS-GUPPI`.

> **tasks:**
> - [ ] update `rule-permissions`
>   - old: `"Read(~/.claude/projects/c--PROJECTS-GUPPI/**)"`
>   - new:
>     ```
>     "Read(~/.claude/projects/c--PROJECTS-GUPPI)",
>           "Read(~/.claude/projects/c--PROJECTS-GUPPI/**)"
>     ```
>   - old: `and whether a search there still asks is the person's word (case 656).`
>   - new:
>     ```
>     and whether a search there still asks is the person's word (case 656). A Grep whose path was that folder itself asked all the same in session 1448, so a second rule names the folder itself beside the rule for what lies inside it (case 693). The folder name follows where this repository sits on the person's disk: another install needs its own name in both rules, and that is not done here; it waits for [[rule-morph]], whose initiation at install sets the folder name (case 693).
>     ```
>   - change: `the folder of the saved transcripts itself joins the allow list for reading, beside what lies inside it; another install needs its own folder name, left to rule-morph`
> - [ ] update `estimate-permissions`
>   - set:
>     ```
>     status: pending
>     method: the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of work.md in Work Mode, recorded in the estimate line; the live probe of the transcripts is the person's word on the client's prompt, in a session after the librarian's render, at a Grep of a subagent whose path is the folder ~/.claude/projects/c--PROJECTS-GUPPI itself and at one whose path is a file under it, recorded in the estimate line — never the agent's, which cannot see the prompt; the Estimate stays pending until the person gives that word
>     ```
>   - change: `the Criterion replaced whole — the allow list also names the folder of the saved transcripts itself, and a search with that folder as its path runs with no prompt`
> - [ ] update `rule-morph`
>   - old: `so a changed set rewrites no rule;`
>   - new:
>     ```
>     so a changed set rewrites no rule; it also sets the name of this project's folder of saved transcripts under ~/.claude/projects in the read rules of the allow list of [[rule-permissions]], which name the folder of one machine until then (case 693);
>     ```
>   - set:
>     ```
>     purpose: "The initiation at install: the person sets the category set of the project — the development set entity, rule, estimate by default — and the harness holds it as data, so a changed set rewrites no rule; it also sets the name of this project's folder of saved transcripts under ~/.claude/projects in the read rules of the allow list of rule-permissions, which name the folder of one machine until then (case 693); the categories discussion of session 1119, raw/2026-09-17/1119/categories-discussion.md; Slice 5"
>     ```
>   - change: `the initiation at install also sets the name of the transcripts folder in the read rules of rule-permissions`
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-permissions`

> **ratification:**
> ```
> - decision[case 693][update][rule-permissions]{ref:rule-permissions}
> - decision[case 693][update][estimate-permissions]{ref:rule-permissions}
> - decision[case 693][update][rule-morph]{ref:rule-morph}
> ```
