<!-- approved 07:32:52 · session 16ad52b9 -->

# Session 0605 — Plan Mode of 2026-11-25

## Case 1045 — The event log keeps the whole path of a file

> **context:**
> The `PostToolUse` hook `guppi event tool` writes one line per tool call into `vault/raw/<date>/event_log.md`, and `tool_detail` of `.guppi/guppi/event.py` cuts the detail of the line to 80 characters by `one_line` and `DETAIL_LIMIT`, a file path included. `plan_path` of `.guppi/guppi/ledger.py` takes the session's plan file from the last `tool Write:`, `tool Edit:` or `tool MultiEdit:` line of the session's stamp whose path `is_plan_file` judges a `.md` file under `.claude/plans/`; I read both functions whole. Claude Code now names a plan file with the id of the session after `-of-`: line 20 of `vault/raw/2026-11-25/event_log.md` holds the plan path of this session cut to `C:\Users\kir\.claude\plans\frolicking-crafting-backus-of-16ad52b9-2613-43c4-8115`, while line 994 of `vault/raw/2026-11-20/event_log.md` holds the short plan path `C:\Users\kir\.claude\plans\fluttering-weaving-matsumoto.md` of session 1353. The cut name has no `.md` suffix, so `is_plan_file` skips it, `plan_path` returns None, and `run` of `.guppi/guppi/caseid.py` printed no id; the session went on after the person appended the whole path as line 30 of the log by hand, which stands. A Grep for `plan_path\(` over `.guppi/guppi/` printed eight files — `casecheck.py`, `ledger.py`, `ratified.py`, `prespec.py`, `spec.py`, `gate.py`, `recall.py` and `caseid.py` — and each reader there finds the plan through that one function, so the fix in the writer reaches each of them and no reader changes. Of the texts that name `guppi event` or `event.py`, these speak of the plan file the log names and stay true: `spec_of` of `.guppi/guppi/recall.py` and the Criterion of `estimate-compact-recall-reloads` take the plan file the event log names last, and `.guppi/guppi/spec.py` finds it by `plan_path`, so each now finds a long path too; `.claude/agents/librarian-guppi.md` registers the same `guppi event tool` hook for the librarian, whose lines change in the same way.
>
> The person chose that a file path stays whole while every other detail is cut at 80 characters as before. This fits the Purpose of `rule-event-log`, which sets the job of the log to name the session's plan file by its `tool Write:` and `tool Edit:` lines; that sentence stays true, so the page changes by no `update`, and the new Estimate stands on it as the page that lists `.guppi/guppi/event.py` in `implementation_ref`. The promise takes a new Estimate, `estimate-event-log-keeps-the-whole-path`, a choice of form: the Criterion of `estimate-event-log-records`, the one Estimate of the page, speaks of the lines of a start, a tool call, `/hi` and the marks, not of the length of a detail, so it stands; a Glob `vault/**/estimate-event-log-keeps*.md` printed nothing, so the slug is free. A Grep for `80 char|DETAIL_LIMIT|truncated` over `vault/wiki`, `.claude`, `.guppi/guppi` and `.guppi/tests` printed `.guppi/guppi/event.py`, `.guppi/guppi/ledger.py` and `vault/wiki/lessons/lesson-gate-plan-path-cut-by-the-event-log-detail-limit.md`: the sentence of the docstring of `event.py` on the cut changes by the task on that file; the docstring of `plan_path`, which says a path the log truncated is skipped, stays true for the lines written before the change; and the `knowledge` lesson of 2026-09-14, which foresaw this cut, is a recorded fact and is not changed. By `rule-one-judgment-one-implementation`, a Grep for `one_line\(|DETAIL_LIMIT` over `.guppi/guppi/` printed `event.py` and `backlog.py`; `one_line` of `backlog.py` collapses a field of an index line and cuts nothing, so the new judgment of which detail stays whole lives in `tool_detail` alone and no second copy is added. The test `test_bash_detail_is_one_line_and_at_most_eighty_characters` of `.guppi/tests/test_event.py` stands, since a command is still cut.
>
> A subagent's tool calls go into the log under the session's stamp, as line 50 of today's log shows a `Read` of `vault/wiki/case-schema.md` by this agent, and Claude Code offers a subagent in Plan Mode a plan file in the same folder whose name adds `-agent-<id>` to the session's. Today that path is cut and skipped by chance. With whole paths, a subagent that creates its plan file with a title line alone, the one write of a new plan file that `guard_refusal` of `.guppi/guppi/ratified.py` lets through, would be taken by `plan_path` as the session's plan. The person chose to leave this out of the Case: a Grep for `plans.*-agent-` over the event logs under `vault/raw/` printed no line, and the Claude Code settings page at https://code.claude.com/docs/en/settings, which I read, says nothing of how plan files are named. The Case closes the `error` lesson `lesson-event-log-cuts-the-path-of-the-plan-file` of this session, whose root cause is the cut of the path, by `{addresses:lesson-event-log-cuts-the-path-of-the-plan-file}`.

> **problem:**
> The event log cuts a file path at 80 characters, and the plan file of a session now has a longer path, so `plan_path` finds no plan file and each hook that needs it, `guppi caseid` first, fails or passes with nothing to check.

> **recommend:**
> - **How the event log keeps a path**
>   - Recommended: (a) a file path stays whole; shell commands, patterns and the other details are still cut at 80 characters.
>   - Answer: agreed, (a).
> - **A plan file that a subagent writes**
>   - Recommended: (a) left out of this Case, since the guard lets through only a title line of a new plan file and no such line was ever logged, and the naming of those files is not in the Claude Code documentation.
>   - Answer: agreed, (a).

> **given:**
> `.guppi/guppi/event.py`: the hook that writes the `tool` line of the event log.
> **＋** `.guppi/guppi/ledger.py`: `plan_path`, the reader of the plan file from the log, not changed.
> **＋** `raw/<date>/event_log.md`: the event log of the day, which the hook writes.
> **＋** `.claude/plans/`: the folder of the plan files of the sessions.
> **＋** `.guppi/tests/test_event.py`: the tests of the event log.
> **＋** `rule-event-log`: the rule of the event log and its job to name the plan file.
> **＋** `estimate-event-log-keeps-the-whole-path`: the new check of the whole path.

> **when:**
> The `PostToolUse` hook `uv run --project .guppi guppi event tool` of `.guppi/guppi/event.py` reads through a pipe the payload of a tool call whose `tool_input` holds a `file_path` longer than 80 characters, and `plan_path` of `.guppi/guppi/ledger.py` then reads the event log of the session.

> **then:**
> The `tool` line in `raw/<date>/event_log.md` holds the whole `file_path` on one line.
> **＋** `plan_path` names a plan file under `.claude/plans/` whose path is longer than 80 characters.
> **＋** A detail taken from `command`, `subagent_type`, `skill`, `pattern` or `description`, and the words of a free event, is still cut to 80 characters on one line.
> **－** A line written before the change keeps its cut path, and `plan_path` skips it.

```then
create:
- slug: estimate-event-log-keeps-the-whole-path
  ref: rule-event-log
  kind: QA
  purpose: Whether the event log keeps the whole path of a file that a tool call names, so that plan_path finds a plan file of any length
  method: pytest in .guppi/tests/test_event.py with piped JSON payloads against a temp vault; by hand at Retro, a tool line of a Read, Write or Edit in the day's event log written after the change whose path is longer than 80 characters read against the Criterion and written into the estimate line
  tags:
  - session
  - hooks
  - harness
```

```tasks
- [ ] create `estimate-event-log-keeps-the-whole-path`
- [x] `.guppi/guppi/event.py`: `tool_detail` writes the `file_path` of a tool input whole on one line, and every other detail is cut at `DETAIL_LIMIT` as before; the sentence of the module docstring on the cut says that a file path stays whole.
- [x] `.guppi/tests/test_event.py`: a test runs `guppi event tool` on a `Write` payload whose `file_path` under `.claude/plans/` is longer than 80 characters, asserts that the line holds the whole path, and asserts that `ledger.plan_path` over that log names it; the test of a Bash detail cut to 80 characters stands.
- [ ] read `estimate-event-log-keeps-the-whole-path`
```

## Case 1046 — A one-off check of the sprint page is done once it is read

> **context:**
> The sprint page `entity-sprint-plugin` lists the Estimates that must be read before the sprint closes. Its Purpose says two things that do not fit together: the sprint is done when every Estimate of the page passes, and an Estimate that has not passed by the close goes to the archive with the page, its status kept. `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` checked one past build once, carries `once: true`, and stands `failed` by the person's decision of case 1025.1, since that build did not read the root `.gitignore`. That build is over, so the Estimate can never pass, and the first sentence can never be met. The close already accepts it: `judge_estimates`, `settled` and `estimate_lines` of `.guppi/guppi/sprint_close.py` take a `failed` Estimate of the sprint page as settled and print that it goes with the sprint page, its status kept, and the History of `rule-sprint-close` (case 627.1) says a failed reading settles an Estimate. So the person chose to reword only the definition of done: a one-off Estimate is done once it is read, a failure kept as its record, and a lasting one still has to pass. The failed Estimate stays `failed` as a true record. `check_unread` of `.guppi/guppi/lint.py` still prints `unread: failed` for it until the close, as the person chose. A Grep of `every Estimate of (this|the sprint) page pass|Done when every` over `{vault/wiki,.claude,.guppi/guppi}/**` printed `vault/wiki/entities/entity-sprint-plugin.md` and `vault/wiki/sprint.md`, the second rendered from the first by `guppi sprint`; no other text sets this definition. The Purpose of `entity-sprint`, the kind, says only that an Estimate not passed by the close goes to the archive with its status kept, so it stands. The other files that name `entity-sprint-plugin` — `backlog.md`, the other Estimates of the page, `rule-guppi-config`, `rule-morph`, `rule-spec-box`, the docstring of `lint.py` and the tests `test_lint.py` and `test_prespec.py` — name the page for another thing and do not state its definition of done, judged by their purpose lines and paths, so they stand. Done in this wording is not the status `built`: by `rule-entities-schema`, `status: built` follows from every Estimate having passed, so with a failed one-off Estimate the cascade keeps `entity-sprint-plugin` `draft` until the close, which archives it whatever its status, as the person chose; the rule stands. How `vault/wiki/sprint.md` ticks such an Estimate under Done when is case 1051, a Case beside this one, which changes `.guppi/guppi/sprint.py` and `rule-sprint`. As a choice of form, a new one-off Estimate on the sprint page checks the new wording, since no Estimate of the page speaks of its definition of done. The one `error` lesson of the session's ledger is already addressed by case 1045.

> **problem:**
> The sprint page asks every Estimate to pass, while a one-off Estimate of a past event that failed can never pass, though the close already settles it.

> **recommend:**
> - **What happens to the failed one-off check of the sprint page**
>   - Recommended: (b) make done mean read for a one-off check; the failure stays as the record.
>   - Answer: agreed, (b).
> - **Whether `guppi check` stops showing red for a failed one-off check**
>   - Recommended: (a) keep the red line until the close.
>   - Answer: agreed, (a).
> - **Whether the sprint page can reach the status "built" with a failed one-off check**
>   - Recommended: (a) the sprint page stays draft until the close.
>   - Answer: agreed, (a).
> - **How `sprint.md` shows a one-off check that was read and failed**
>   - Recommended: (b) tick a read one-off check, its status `failed` kept after it.
>   - Answer: agreed, (b); case 1051 carries it.

> **given:**
> `entity-sprint-plugin`: the sprint page, whose Purpose sets when the sprint is done.
> **＋** `vault/wiki/sprint.md`: the view of the sprint, rendered from that page.
> **＋** `estimate-sprint-plugin-done-counts-a-one-off-reading`: the new check of the wording.
> **＋** `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`: the failed one-off Estimate of the page.
> **＋** `rule-sprint-close`: a failed reading settles an Estimate at the close.
> **＋** `rule-entities-schema`: `built` follows from every Estimate having passed.

> **when:**
> Someone reads the Purpose of `entity-sprint-plugin` and the Done when of `vault/wiki/sprint.md` after the librarian's run.

> **then:**
> An Estimate of the page that checks a lasting behaviour is done when it passes.
> **＋** An Estimate of the page with `once: true` is done once it is read, a failed reading kept as the record of what it found.
> **－** `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` keeps its status `failed`.

```then
create:
- slug: estimate-sprint-plugin-done-counts-a-one-off-reading
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether the sprint page and sprint.md say that a one-off Estimate is done once it is read, a failed reading kept, and a lasting one when it passes; read once
  method: 'by hand, after the librarian''s run of this session: the Purpose of vault/wiki/entities/entity-sprint-plugin.md and the Done when of vault/wiki/sprint.md read against the Criterion, in the estimate line'
  once: true
  tags:
  - sprint
  - workflow
update:
- slug: entity-sprint-plugin
  replace:
  - old: 'Done when every Estimate of this page passes:'
    new: 'Done when every Estimate of this page that checks a lasting behaviour passes, and each one-off Estimate, which carries `once: true`, is read, a failed reading kept as the record of what it found:'
  change: a one-off Estimate is done once it is read
```

```tasks
- [ ] update `entity-sprint-plugin`
- [ ] create `estimate-sprint-plugin-done-counts-a-one-off-reading`
- [ ] `uv run --project .guppi guppi sprint`
- [ ] read `estimate-sprint-plugin-done-counts-a-one-off-reading`
```

## Case 1047 — The searches of case-guppi for the names of what it changes are read again

> **context:**
> When `case-guppi` stops, the `SubagentStop` hook of `rule-case-check` sends it a note, `names_notes` of `.guppi/guppi/casecheck.py`, that lists each file that names a page or a file its Case changes and that it has not read. The note is no finding and does not send the agent back. `estimate-case-build-searches-the-names-of-what-it-changes` checks that the agent reads or names in `context` each listed file that bears on its change. It stands `failed` from the `/hi` of session 0358: after a note of 47 files, the build of Case 1015 of session 0316 neither read nor named three files whose paths speak of the searches it widened. Case 1038 put it off. Only that one build has been judged on the rule as it stands, so the person chose to read it again on the builds of this session, its Criterion and the Render of `rule-case-build` unchanged. The `update` sets the page `pending`, and its Criterion is this Case's `when` and `then`, the old Criterion word for word. Its `method` waited for the first session in which the hook sends the note, which has passed, so the `method` is set anew to wait for the `/pre-spec` of this session. That is a choice of form. The `update` carries `{supersedes:case 1038}` and names the page on a line other than a `defer`, as `case-schema.md` sets for a deferred decision. No Estimate of `rule-case-build` other than this one is touched, since the rule does not change. No `error` lesson of this session's ledger is closed by this Case. The note of the check listed `vault/wiki/rules/rule-case-build.md` and `vault/wiki/backlog.md`, which name the Estimate. Both stand: the rule lists the Estimate under `estimates`, and the Case changes neither the rule nor the slug. `backlog.md` is no page and holds the line of the deferred item, which the librarian's run writes anew from the pages, so this Case writes no task for it.

> **problem:**
> The Estimate stands `failed` on one build, and no Case decides whether the rule is wrong or whether a new reading is due.

> **recommend:**
> - **What this Case does with the failed reading**
>   - Recommended: (a) read it again on this session's builds, its Criterion unchanged.
>   - Answer: agreed, (a).

> **given:**
> `estimate-case-build-searches-the-names-of-what-it-changes`: set `pending`, its Criterion unchanged in substance.
> **＋** `rule-case-build`: the rule that sets the answer of `case-guppi` to the note.
> **＋** `.guppi/guppi/casecheck.py`: the hook code that sends the note.
> **＋** `rule-case-check`: the rule of the hook that sends the note.
> **＋** `.claude/agents/case-guppi.md`: the agent rendered from `rule-case-build`.
> **＋** `vault/wiki/case-schema.md`: the form of a task line that the Criterion names.
> **＋** `vault/wiki/`: the folder whose files a task line may leave out of its code span.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, gets from the `SubagentStop` hook of `rule-case-check` the note that lists the files that name a page or a file its Case changes, and answers again.

> **then:**
> For each listed file whose purpose line or path speaks of what its Case changes, it reads that file by a `Read` call of it, or by a `Grep` call whose `path` is it, whole or in parts as `rule-case-build` sets for its kind of text, or the `context` of the Case names the file and says why it stands.
> **＋** Each file that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **＋** In its case file, a file of the repository outside `vault/wiki/` that a task changes has a task line of its own that opens with the path in a code span.
> **－** A listed file whose purpose line and path speak of something else needs no read and no line in `context`.
> **－** A task line that opens with a code span holding a command, such as `uv run --project .guppi guppi render` with the rendered file in its second span, keeps the form `vault/wiki/case-schema.md` sets for it.

```then
update:
- slug: estimate-case-build-searches-the-names-of-what-it-changes
  set:
    status: pending
    method: 'by hand, after the /pre-spec of the session that sets this method: the agent transcript of each case-guppi of that session under ~/.claude/projects/ that got the note of the hook of rule-case-check, for each listed file whose purpose line or path speaks of what its Case changes whether the agent read it by Read or by a Grep whose path is it, or named it in context; and its case file, whether each task line that changes a file outside vault/wiki/ holds its path in its first code span and changes no other such file, a line that opens with a code span holding a command, such as a render line, left out; the count and the transcripts in the estimate line'
  change: pending again after the failed reading, the Criterion unchanged; read on the builds of a later session
```

```tasks
- [ ] update `estimate-case-build-searches-the-names-of-what-it-changes`
- [ ] read `estimate-case-build-searches-the-names-of-what-it-changes`
```

## Case 1048 — The searches of ask-guppi at pre-spec are read again

> **context:**
> At `/pre-spec`, `ask-guppi` runs the four index Greps of the vault first and then searches as each finding needs. Since case 1015.1, those searches may cover the code, the tests and the harness files, and they may not reach `vault/archive/`. `estimate-ask-searches-at-prespec` checks this. It stands `failed` from the `/hi` of session 0358: in the pre-spec of session 1825 a Grep over the repository root reached `vault/archive/`, and the agent searched the archive by a session path. Case 1037 put it off. A Grep of `1015\.1` over `.claude/agents/ask-guppi.md` printed line 25, so the Render that allows code searches is live. `case-guppi` read the `ask-guppi` transcript of the pre-spec of session 1353, `~/.claude/projects/c--PROJECTS-GUPPI/68550048-efc7-4790-9bd8-17ed548134c2/subagents/agent-aa9fe3289c813bff9.jsonl`. Its first four Greps, at lines 16 to 22, take the patterns as written. Later searches covered `casecheck.py`, `ship.py`, `test_ship.py`, `prod.yml`, `.gitignore` and `.gitattributes`. Each Grep over the repository root took a glob limited to `vault/wiki`, `.claude`, `.guppi/guppi` and `plugin`. Its list of what it did not check names no code search as a broken rule. Two Globs at lines 321 and 322, `vault/**/estimate-guppi-repository-*license*` and `vault/**/estimate-clean-branch-prod-*`, reach the archive by a part of a slug. They search for Estimate pages, not code, so they fall outside this Criterion. That run was never recorded as a reading, so the person chose a new reading at this session's `/pre-spec`. The `update` sets the page `pending`. Its Criterion is this Case's `when` and `then`, the old Criterion word for word. Its `method` is set anew to wait for that `/pre-spec`, which is a choice of form, as in Case 1047. The `update` carries `{supersedes:case 1037}` and names the page on a line other than a `defer`, as `case-schema.md` sets for a deferred decision. No other Estimate of `rule-ask` is touched, since the rule does not change. No `error` lesson of this session's ledger is closed by this Case. The note of the check listed `vault/wiki/backlog.md`, `estimate-ask-finds` and `estimate-prespec-finds-a-reader-of-a-new-files-folder`, which name the Estimate. All three stand, since the Case keeps the slug and the Criterion of the Estimate unchanged. `backlog.md` is no page, and the librarian's run writes it anew from the pages.

> **problem:**
> The Estimate stands `failed` and put off, while a run on the live rule that was never read as a reading looks like it meets the Criterion.

> **recommend:**
> - **What this Case does with the failed reading**
>   - Recommended: (a) read it again at this session's /pre-spec, its Criterion unchanged.
>   - Answer: agreed, (a).

> **given:**
> `estimate-ask-searches-at-prespec`: set `pending`, its Criterion unchanged in substance.
> **＋** `rule-ask`: the rule whose Render sets the searches of `ask-guppi`.
> **＋** `.claude/agents/ask-guppi.md`: the agent rendered from `rule-ask`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the questions the main agent sends.
> **＋** `vault/wiki/rules/`, `vault/wiki/entities/`, `vault/wiki/lessons/` and `vault/wiki/insights/`: the folders of the index Greps.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `vault/archive/`: the archive, searched by slug alone.
> **＋** `estimate-prespec-finds-a-reader-of-a-new-files-folder`, `estimate-search-leaves-out-decisions-by-the-grep-hook` and `estimate-search-leaves-out-decisions-in-every-agent`: the Estimates that read what this promise leaves out.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs, whatever the question, the Grep `^(purpose|deferred_by):` over `vault/wiki/entities/`, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, each with its pattern as the recipe writes it and no word added.
> **＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
> **＋** Those Greps and Reads may cover the code, the tests and the harness files as well as the vault.
> **＋** The list of what the agent did not check names no search of the code as a broken rule of `.claude/agents/ask-guppi.md`.
> **＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
> **－** No search of the code, the tests or the harness files reaches `vault/archive/`, which the agent searches by slug alone.
> **－** Whether the folder-walk Grep runs for a Case that adds a file that is no page of the vault is outside this promise: `estimate-prespec-finds-a-reader-of-a-new-files-folder` reads it.
> **－** Whether a Grep of the agent over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
> **－** Whether a Read of the agent, or a Grep inside `vault/wiki/decisions/`, reaches a Decision page only for a reason of its frame is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.

```then
update:
- slug: estimate-ask-searches-at-prespec
  set:
    status: pending
    method: 'by hand, after the first /pre-spec that runs once this Criterion is set: the Grep, Glob and Read calls of ask-guppi at that /pre-spec and its list of what it did not check, read in its agent transcript under ~/.claude/projects/ against the Criterion, the transcript in the estimate line'
  change: pending again after the failed reading of session 0358, the Criterion unchanged; read at the /pre-spec of session 0605
```

```tasks
- [ ] update `estimate-ask-searches-at-prespec`
- [ ] read `estimate-ask-searches-at-prespec`
```

## Case 1049 — The clean copy carries the MIT license, and the install keeps a project's own license

> **context:**
> `guppi ship` of `.guppi/guppi/ship.py` builds the clean copy that people install. From the root of the repository it takes only the files of `ROOT_FILES`, `CLAUDE.md` and `.gitattributes`, so the copy on `prod` holds no license text. The condition of the MIT license in `LICENSE` asks that the notice be included in all copies or substantial portions of the software. Step 2 of `plugin/skills/install/SKILL.md` lists each file of the plugin but those under `.claude-plugin/`, `skills/` and `.git/`. Step 3 stops when the project already holds one of those paths, unless the path is `CLAUDE.md`, a file under `.claude/`, `.gitattributes` or `.github/workflows/checks.yml`. So a `LICENSE` added at the root of the copy would stop the install in each project that has a license of its own. Case 1043.2 put this item into the `## Backlog` of `entity-sprint-plugin`: `guppi ship` writes `LICENSE` into the copy, and `/guppi:install` leaves it out. The person then chose that the project that installs GUPPI still gets the notice, as `.guppi/LICENSE` beside the code. Option (a), the root only, would have left each installed project with the code of GUPPI and no notice, against that same condition of the license, so it was not recommended.
>
> As a choice of form, the Case splits in two, since the build and the install can fail apart and need different fixes. Case 1049.1 adds `LICENSE` to `ROOT_FILES`, and a map in the manner of `PLUGIN_FILES` writes the same root file to `.guppi/LICENSE` of the copy, so the repository keeps one license file and the two texts cannot part. `plan` of `ship.py` takes a source only when it stands as a file, so a working tree with no `LICENSE` gives neither file. `test_it_writes_the_code_the_harness_and_the_core_pages_only` of `.guppi/tests/test_ship.py` asserts the exact set of files of a copy built from a temporary tree that holds no `LICENSE`, so it stays green. `settled` and `judged` judge and clean each written file, and `check` judges each source outside `vault/` in place. The text of `LICENSE` holds none of the pointer forms of `POINTERS` of `.guppi/guppi/pointers.py`: no word case, no `decision-case-N` and no word session before a number. So the build and `--check` print no line on it, and its bracket `(c)` holds no pointer and stays. No Estimate of `rule-clean-branch` checks a license, so Case 1049.1 creates `estimate-clean-branch-ships-the-license`; a Glob `vault/**/estimate-*licen*` printed only `estimate-guppi-repository-carries-the-mit-license`, so the slug is free. `estimate-clean-branch-writes-a-clean-copy` lists the files the copy holds, and no line of its Criterion says that the copy holds no other root file, so it stands. `estimate-clean-branch-code-holds-pointers-only-in-brackets` names `Makefile`, `pyproject.toml` and `.gitattributes` and not `LICENSE`, so it stands. The other Estimates of the page speak of other things by their purpose lines.
>
> Case 1049.2 leaves the root `LICENSE` out of step 2 of the install, so a project's own `LICENSE` is neither a clash nor set aside, and `.guppi/LICENSE` comes in with the rest of `.guppi/`. The Then of `estimate-plugin-install-writes-guppi-into-an-empty-project` says that the install copies each file but those under the three folders, and the change makes that line false. So, as a choice of form, Case 1049.2 replaces that Criterion whole and reads it in a project that holds only a `LICENSE` of its own. That test is the case this item is about, and it takes no more install runs than an empty project would. Its `purpose` and `method` state the old promise, so the same update sets both anew. `estimate-plugin-install-sets-aside-the-files-of-the-project` says that the install sets aside no file at a path it does not write. Once `LICENSE` is no path of the install, that stays true, so it stands. The other Estimates of `rule-plugin-install` speak of `uv`, the rollback, the order of the hooks and Plan Mode, so they stand. `estimate-sprint-plugin-installs-as-a-plugin` promises that the install copies GUPPI with no error, not which files it copies, so it stands. Case 1049.2 also removes the item's line from the `## Backlog` of the sprint page, which ends the item, as `orchestration.md` sets it for an item of the sprint. Case 1046 changes only the Purpose of the same page, so the two pairs do not meet.
>
> Readers. The page https://code.claude.com/docs/en/plugins-reference says that `claude plugin validate` checks the manifest and the paths it names, and that it warns on a `CLAUDE.md` at the plugin root; it names no check on another file at the root, such as a license. The page https://docs.astral.sh/uv/concepts/build-backend/ says that the uv build backend puts into a wheel only the license files that `project.license-files` names, and a Grep of `build|licen|package` over `.guppi/pyproject.toml` printed only its lines on the build backend, two comments, `[build-system]` with its two keys and `[tool.uv.build-backend]`, with no such key. So `uv sync` takes no account of `.guppi/LICENSE`. For the new file `.guppi/LICENSE` of the copy, a Grep of `\.guppi` printed 262 hits in 39 files of `.guppi/guppi/`, 59 in 14 files of `.claude/` and 303 in 66 files of `vault/wiki/rules/`, with the bare name the same pattern. Those hits name the command `uv run --project .guppi`, a single file or the folder as a whole. The readers of every file of a folder come from a Grep of `os\.walk|rglob|\.glob\(|iterdir`, which printed hits in 15 modules of `.guppi/guppi/`: `agents.py`, `archive.py`, `backlog.py`, `casecheck.py`, `caseid.py`, `cleanup.py`, `generate.py`, `ledger.py`, `lint.py`, `materialize.py`, `onward.py`, `pages.py`, `prespec.py`, `ship.py` and `sprint_close.py`. Over `.guppi/tests/` it printed 16 files. Of those, only `tree_files` of `ship.py` walks `.guppi/`, and the working tree holds no `.guppi/LICENSE` for it to meet. `named_files` of `casecheck.py` walks `.guppi/guppi` and `.guppi/tests` only, and `callers` of `.guppi/tests/test_guppi_package.py` walks `.claude` and `.github/workflows`. The other walks take a folder of the vault, of a session or of a temporary tree. `.guppi/.gitignore` ignores `.venv/` and `__pycache__/`, and the root `.gitignore` ignores neither `LICENSE` nor `.guppi/LICENSE`. Line 27 of `.gitattributes` gives every text file LF line ends, as it should. Ruff reads three sets of files here: the commands of the key `style` of `guppi.toml`, `ruff check .` and `ruff format --check .`, and `FORMAT` of `ship.py`, `ruff format .guppi`, which the build runs over `.guppi/` of the copy. The page https://docs.astral.sh/ruff/configuration/ says that Ruff by default finds the files that match `*.py`, `*.pyi`, `*.ipynb`, `*.md`, `pyproject.toml`, `ruff.toml` or `.ruff.toml`. `.guppi/pyproject.toml` sets only `extend-exclude`, no `include`, so Ruff takes neither `LICENSE` nor `.guppi/LICENSE`, and those three readers stand. The step that commits the copy to `prod` in `.github/workflows/prod.yml`, lines 62 to 64, also reads every file. It removes every file of the work tree but `.git`, copies every file of the clean folder by `cp -a "$RUNNER_TEMP/clean/." .` and stages them all by `git add -A`. So it commits both new files with the rest of the copy, as it should, and it stands. Step 2 of the install copies the file, as chosen. So the new file makes no reader wrong.
>
> Tests. A Grep of `rule-plugin-install|rule-clean-branch|skills/install|entity-sprint-plugin|ROOT_FILES` over `.guppi/tests/` printed `test_lint.py`, `test_prespec.py` and `test_ship.py`. `test_lint.py` and `test_prespec.py` name the sprint page only in samples. `test_ship.py` writes its own `SKILL.md` into a temporary tree and reads no live skill file. `test_own_style_passes_over_the_copy` and `test_live_build_of_this_repository_prints_no_line_on_a_shipped_page_of_the_checks` build the live repository and keep only the lines on `ruff` and on `vault/wiki/estimates/`, so the license file gives them no line. Neither rule page has `core: true`, so the copy holds neither new text. `test_guppi_package.py` reads every live page for the old paths `guppi/` and `tests/` by `reword_pattern` of `.guppi/guppi/generate.py`, which takes no match after a dot, so `.guppi/LICENSE` is no hit.
>
> Lists. A Grep of `\.gitattributes` over the repository root with the glob `{vault/wiki,.claude,.guppi/guppi}/**`, in the mode of paths only, printed 22 files. Of those, the lists of the root files of the copy are `ship.py`, `rule-clean-branch` and `estimate-clean-branch-writes-a-clean-copy`, and the lists of what the install sets aside are `rule-plugin-install` and its Estimates, each judged above. The others name `.gitattributes` for its `merge=union` lines, for the line ends it sets, for a set-aside file that the setup Case shows, or in a past reading. A Grep of `\.claude-plugin/` over the same root and glob printed 6 files: `rule-clean-branch.md`, `rule-plugin-install.md`, `ship.py`, `estimate-sprint-plugin-ci-writes-a-clean-branch.md`, `estimate-plugin-install-writes-guppi-into-an-empty-project.md` and `estimate-clean-branch-installs-as-a-plugin.md`. The first five are judged above, and the last names the folder of the manifest only. A Grep of `estimate-plugin-install-writes-guppi-into-an-empty-project` over `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` printed `log.md` and `rule-plugin-install.md`. A Grep of `guppi:install|files to install` over `{vault/wiki/rules,.claude}/**` printed `rule-plugin-install.md` and `rule-morph.md`, and `rule-morph` says only that the install copies the files of GUPPI. `README.md` says that the install copies the files of GUPPI and sets aside `CLAUDE.md`, files under `.claude/`, `.gitattributes` and `.github/workflows/checks.yml`, which stays true.
>
> The check of this file listed the files that name what the Case changes. Two lines of the old Criterion of the install Estimate change on purpose: the line of the install now names a project with a `LICENSE` of its own, and the line of the copy now leaves out the root `LICENSE`. The other lines are carried word for word. Case 1048 names `ship.py` and the skill files only as places that `ask-guppi` searched, and it changes neither, so it stands. Of the listed files whose purpose lines speak of the copy or the install, four were read. `estimate-guppi-package-is-ready-after-the-install` says that the install copies each file of the install, and `LICENSE` is then no such file. `estimate-guppi-repository-keeps-the-development-project` says that the copy holds no `pyproject.toml` and no `uv.lock` at its root. `rule-guppi-package` keeps a project from depending on root files it does not own, which the choice of `.guppi/LICENSE` keeps. `entity-guppi-repository` names `LICENSE` only in its `code_ref`, and the file stays in the repository. All four stand. Each other listed file stands, since by its purpose line or its path it speaks of something else. These are the other Estimates of `rule-clean-branch`, `rule-plugin-install`, `entity-sprint-plugin` and the setup of `rule-morph`, the pages and code that name `guppi ship`, `settings.json`, `guppi codewrite` or `SKILL.md` for another purpose, and the lessons and Insights, which are records. `backlog.md` loses the item's line when it is rendered again from the sprint page. The session's ledger holds one `error` lesson, which the line `{addresses:lesson-event-log-cuts-the-path-of-the-plan-file}` of Case 1045 already ties, so no mark is added.

> **problem:**
> The copy of GUPPI that people install carries no license text, and a license file added to it would stop the install in each project that has a license of its own.

> **recommend:**
> - **Whether the installed project carries the license notice**
>   - Recommended: (b) at the root of the copy, and a second copy inside `.guppi/` that the install copies.
>   - Answer: agreed, (b).

### Case 1049.1 — The clean copy carries the license at its root and in `.guppi/`

> **given:**
> `.guppi/guppi/ship.py`: the build of the clean copy, which takes the root files.
> **＋** `.guppi/tests/test_ship.py`: the tests of the build.
> **＋** `LICENSE`: the MIT license at the root of the repository.
> **＋** `.guppi/LICENSE`: the second place of the license in the clean copy.
> **＋** `rule-clean-branch`: the rule of what the clean copy holds.
> **＋** `estimate-clean-branch-ships-the-license`: the new check of the license in the copy.
> **＋** `rule-plugin-install`: the install, which the new text names.

> **when:**
> `uv run --project .guppi guppi ship <folder>` of `.guppi/guppi/ship.py`, as `rule-clean-branch` sets it, builds the clean copy from a working tree that holds `LICENSE` at its root.
> **＋** Or it builds the clean copy from a working tree with no `LICENSE`.
> **＋** Or `uv run --project .guppi guppi ship --check` judges a working tree that holds `LICENSE`.

> **then:**
> The clean copy holds `LICENSE` at its root, with the text of the `LICENSE` of the working tree, judged and cleaned like each other file it writes.
> **＋** It holds the same text at `.guppi/LICENSE`, written from the root file, and the working tree holds no file at that path.
> **＋** `--check` judges `LICENSE` in place and prints no line on the text of the MIT license.
> **－** From a working tree with no `LICENSE` it writes neither file and prints no line for them.

```then
create:
- slug: estimate-clean-branch-ships-the-license
  ref: rule-clean-branch
  kind: QA
  purpose: Whether guppi ship writes the LICENSE of the working tree to the root of the clean version and to .guppi/LICENSE there, judged like each other file, writes neither when the tree holds no LICENSE, and whether --check judges it in place
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k license
  tags:
  - ci
  - plugin
update:
- slug: rule-clean-branch
  replace:
  - old: '`.claude/`, `CLAUDE.md`, `.gitattributes`, `vault/.gitignore`, whose lines keep'
    new: '`.claude/`, `CLAUDE.md`, `.gitattributes`, `LICENSE`, `vault/.gitignore`, whose lines keep'
  - old: It writes each file under `plugin/skills/` of this repository
    new: It also writes the text of `LICENSE`, the MIT license, to `.guppi/LICENSE` of the clean version, so that a project that installs GUPPI holds the license beside the code, as [[rule-plugin-install]] sets it. It writes each file under `plugin/skills/` of this repository
  change: the clean version holds LICENSE at its root and at .guppi/LICENSE
```

```tasks
- [x] `.guppi/guppi/ship.py`: `LICENSE` joins `ROOT_FILES`, and a map in the manner of `PLUGIN_FILES` writes the root `LICENSE` to `.guppi/LICENSE` of the copy too, taken only where the root file stands; the module docstring names both paths.
- [x] `.guppi/tests/test_ship.py`: tests whose names hold `license`: a tree with the text of the live `LICENSE` at its root gives a copy with that text at `LICENSE` and at `.guppi/LICENSE`, and `--check` prints no line on it; a tree with no `LICENSE` gives a copy with neither file.
- [ ] update `rule-clean-branch`
- [ ] create `estimate-clean-branch-ships-the-license`
- [ ] read `estimate-clean-branch-ships-the-license`
```

## Case 1051 — The sprint view ticks a one-off Estimate once it is read

> **context:**
> `render` of `.guppi/guppi/sprint.py` writes one line per Estimate of the sprint page under Done when of `vault/wiki/sprint.md`, and ticks it by `tick(status == 'passed')`; its module docstring says `- [x]` when `passed`, `- [ ]` otherwise. Case 1046 rewords the sprint page so that a one-off Estimate, one with `once: true`, is done once it is read, a failed reading kept. So `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`, read and `failed`, would still show an open box under a text that calls it done; the pre-spec audit of case 1046 found this, and the person chose that the view ticks such a line. This is a second behaviour with a promise of its own, and case 1046 already has decision lines, so as a choice of form it stands in this new Case beside it, with no mark on case 1046. The status still stands after the tick, so the view keeps showing `failed`. `check_unread` of `.guppi/guppi/lint.py` keeps its red line and the sprint page stays `draft`, as the person chose in case 1046. The judgment of a one-off Estimate stands today once, inline, in `check_status` of `.guppi/guppi/lint.py` at line 605, as `page.props.get("once") is True`; a Grep of `\bonce\b["']|get\(["']once|\bONCE\b` over `.guppi/guppi/` printed only `lint.py`. So the task puts it into one function `is_one_off` in `.guppi/guppi/ledger.py`, beside `is_sprint_page`, which `sprint.py` and `lint.py` already import, and both import it, as `rule-one-judgment-one-implementation` sets it. No Estimate of `rule-sprint` speaks of the ticks under Done when: `estimate-sprint-renders-the-backlog` writes one line per Estimate and ticks the items of the milestones only, so it stands, and the other four speak of `--check`, the Spec ticks, the moves of items and a closed sprint. So this Case creates `estimate-sprint-ticks-a-read-one-off-estimate`. Its creation sets `rule-sprint`, which has `core: true`, `draft` by the cascade until the Retro of this session reads it by a test, so no CI run writes to `prod` before then. No test of `.guppi/tests/` reads `rule-sprint` live: a Grep of `rule-sprint\.md|rules/rule-sprint"|"rule-sprint"` there printed nothing. The `EXPECTED` text of `.guppi/tests/test_sprint.py` holds a `pending` and a `passed` Estimate, which the change does not touch. The other files that name `rule-sprint`, `sprint.py`, `sprint.md`, `guppi sprint`, `ledger.py` or `lint.py` — the glossary, the schemas, the other rules, skills, Estimates and modules the check of this file listed — name them for another thing, judged by their purpose lines and paths: none states how a line under Done when is ticked, and a Grep of `Done when` over `vault/wiki/glossary.md` printed nothing, so they stand. Case 1046 changes only the Purpose of `entity-sprint-plugin`, which this Case reads, and names this Case for the tick.

> **problem:**
> The sprint view leaves a one-off Estimate unticked after it is read and failed, while the sprint page calls it done.

> **recommend:**
> - **What happens to the failed one-off check of the sprint page**
>   - Recommended: (b) make done mean read for a one-off check; the failure stays as the record.
>   - Answer: agreed, (b); case 1046 carries it.
> - **Whether `guppi check` stops showing red for a failed one-off check**
>   - Recommended: (a) keep the red line until the close.
>   - Answer: agreed, (a).
> - **Whether the sprint page can reach the status "built" with a failed one-off check**
>   - Recommended: (a) the sprint page stays draft until the close.
>   - Answer: agreed, (a).
> - **How `sprint.md` shows a one-off check that was read and failed**
>   - Recommended: (b) tick a read one-off check, its status `failed` kept after it.
>   - Answer: agreed, (b).

> **given:**
> `.guppi/guppi/sprint.py`: the render of `vault/wiki/sprint.md`.
> **＋** `.guppi/guppi/ledger.py`: the home of the one judgment of a one-off Estimate.
> **＋** `.guppi/guppi/lint.py`: the other place that judges a one-off Estimate.
> **＋** `.guppi/tests/test_sprint.py`: the tests of the render.
> **＋** `rule-sprint`: the rule of the sprint view.
> **＋** `estimate-sprint-ticks-a-read-one-off-estimate`: the new check of the tick.
> **＋** `entity-sprint-plugin`: the sprint page, whose Purpose sets when a one-off Estimate is done.

> **when:**
> `uv run --project .guppi guppi sprint` of `.guppi/guppi/sprint.py` renders `vault/wiki/sprint.md` from a sprint page whose `estimates` hold a `passed` Estimate, a `pending` one, a `failed` one with `once: true` and a `failed` one with no `once`.

> **then:**
> The line of the `passed` Estimate and the line of the `failed` one with `once: true` stand under Done when as `- [x]`.
> **＋** Each line keeps its status after ` · `, `failed` included.
> **－** The line of the `pending` Estimate and the line of the `failed` one with no `once` stay `- [ ]`.

```then
create:
- slug: estimate-sprint-ticks-a-read-one-off-estimate
  ref: rule-sprint
  kind: QA
  purpose: 'Whether guppi sprint ticks under Done when an Estimate that is passed, or failed with once: true, keeps each status, and leaves a pending one and a failed one with no once unticked'
  method: uv run --project .guppi pytest .guppi/tests/test_sprint.py -k one_off
  tags:
  - harness
  - sprint
update:
- slug: rule-sprint
  replace:
  - old: reads the file as before.
    new: 'reads the file as before. Under Done when, the line of an Estimate is ticked when it is `passed`, or when it is `failed` and carries `once: true`, since a one-off Estimate is done once it is read; its status stands after ` · ` (as set in case 1051).'
  change: a read one-off Estimate is ticked under Done when
```

```tasks
- [x] `.guppi/guppi/ledger.py`: a function `is_one_off(page)`, beside `is_sprint_page`, true when the `once` field of the page is `true`, the one judgment of a one-off Estimate.
- [x] `.guppi/guppi/lint.py`: `check_status` imports `is_one_off` and judges by it in place of its inline test of `once`.
- [x] `.guppi/guppi/sprint.py`: `render` ticks the line of an Estimate when it is `passed`, or when it is `failed` and `is_one_off` holds; the module docstring says so.
- [x] `.guppi/tests/test_sprint.py`: a test whose name holds `one_off` renders a sprint page with the four Estimates of the Criterion and asserts their ticks and statuses.
- [ ] update `rule-sprint`
- [ ] create `estimate-sprint-ticks-a-read-one-off-estimate`
- [ ] `uv run --project .guppi guppi sprint`
- [ ] read `estimate-sprint-ticks-a-read-one-off-estimate`
```

## Case 1052 — The install leaves the root license out and keeps a project's own, read after the librarian's run

> **context:**
> This Case replaces Case 1049.2 whole and changes one thing in it: the moment of the reading by hand of `estimate-plugin-install-writes-guppi-into-an-empty-project`. The `method` that Case 1049.2 set asks for the install at a stop of the Work Mode of the session that sets the Criterion. That reading cannot be taken in this session. The clean copy takes the skill `/guppi:install` from `plugin/skills/install/SKILL.md`, the Render of `rule-plugin-install`, and that file changes only at the render of the librarian's run after this session. So at a stop of this Work Mode the copy still holds the old skill text, which copies every file of the plugin. The Work Mode of this session already made `guppi ship` write `LICENSE` at the root of the copy, by Case 1049.1: a Grep of `LICENSE` over `.guppi/guppi/ship.py` printed `ROOT_FILES = ("CLAUDE.md", ".gitattributes", "LICENSE")` and `LICENSE_FILES = {".guppi/LICENSE": "LICENSE"}`. An install now would test the old skill and stop on the project's `LICENSE`. The person chose, at the stop of Work Mode, that a new Case moves the reading to a session after the librarian's run of this session and keeps the Criterion of Case 1049.2.
>
> So the new `method` puts the reading by hand in a part that opens with `by hand, after the librarian's run of the session that sets this Criterion:`, the form that case 781 sets for a reading that waits for an event; Retro leaves the Estimate `pending` until that event, and the brief of a later session puts the reading under `Work`. The `stop:` task of Case 1049.2 leaves, since no stop of this Work Mode takes the install; the `read` line stays, as `case-schema.md` sets it for an Estimate set `pending`. The `when` and `then` of Case 1049.2 stand word for word, so the Criterion is the one already ratified. The page updates, the render line, the sprint line and the change of the `## Backlog` of `entity-sprint-plugin` stand as Case 1049.2 wrote them, since `materialize` applies nothing of a sub-case that a mark retires; no task of Case 1049.2 has run. Case 1049.1 stands as approved. The sentences around each pair were read whole on the live pages. In the Purpose of `rule-plugin-install`, the sentence of the files it copies is followed by the sentence that lists those files, which the second pair changes so that the root files leave out `LICENSE`; the next sentences, on the files set aside and on a clash at another path, still hold, since `LICENSE` is then no path of the install. Step 2 of the Render goes on with the sentence that these are the files to install, each at the same path, which stays true. In the `## Backlog` of `entity-sprint-plugin`, the pair takes the line that ends with case 1019.4 and the license line after it, and keeps the first. Case 1046 changes only the sentence of its Purpose that opens with `Done when every Estimate of this page passes:`, so the two pairs of that page do not meet, and no other Case of this session writes into `rule-plugin-install`. The frame of Case 1049.2, its searches and its readers are those that the `context` of Case 1049 names, and this Case changes no text they judged but the `method`. The session's ledger holds one `error` lesson, which the line `{addresses:lesson-event-log-cuts-the-path-of-the-plan-file}` of Case 1045 already ties, so no mark is added.

> **problem:**
> The reading by hand that Case 1049.2 sets for the install cannot be taken in the session that sets it, since the skill it reads changes only at the librarian's render after that session.

> **recommend:**
> - Recommended: (a) a new Case moves the reading of the install to a session after the librarian's run of this session, and keeps the Criterion of Case 1049.2.
> - Answer: ratified as built

> **given:**
> `rule-plugin-install`: the install, whose Render writes the skill.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install`, rendered from that page.
> **＋** `estimate-plugin-install-writes-guppi-into-an-empty-project`: the check of which files the install copies, its Criterion replaced whole.
> **＋** `rule-clean-branch`: the clean copy, which holds `LICENSE` and `.guppi/LICENSE`.
> **＋** `entity-sprint-plugin` and `vault/wiki/sprint.md`: the sprint page, whose `## Backlog` holds this item, and its rendered view.
> **＋** `.claude-plugin/` and `.git/`: with `skills/`, the folders of the plugin that the install does not copy.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands of Claude Code that add the catalogue and install the plugin.
> **＋** `.claude/settings.json`, `.claude/skills/` and `/hi`: the harness that the install copies, and the skill that opens the first session on it.

> **when:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
> **＋** The agent writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`; the person adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` of `plugin/skills/install/SKILL.md`, as `rule-plugin-install` sets it, in a project open in Claude Code that holds a `LICENSE` of its own and none of the files the install writes.

> **then:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
> **＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
> **＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
> **＋** `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/` and the file `LICENSE` at the root of the plugin, such as `CLAUDE.md`, `.claude/settings.json`, `.guppi/LICENSE`, the code under `.guppi/` and the pages under `vault/wiki/`.
> **＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
> **－** The `LICENSE` of the project stays at its path with its text unchanged: the install neither stops on it nor sets it aside.
> **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
> **－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
> **－** Which files a new project needs, what the install does about `uv` and the Python environment under `.guppi/`, and what it does with a file of the project that stands at one of its paths are no part of this promise.

```then
update:
- slug: rule-plugin-install
  replace:
  - old: It copies into the project each file of the plugin but its own files, those under `.claude-plugin/`, `skills/` and `.git/`.
    new: It copies into the project each file of the plugin but its own files, those under `.claude-plugin/`, `skills/` and `.git/`, and the file `LICENSE` at the root of the plugin, so that the `LICENSE` of a project stays as it is and stops no install; the license text reaches the project as `.guppi/LICENSE`, which `guppi ship` writes beside the code.
  - old: the harness `.claude/` and `CLAUDE.md`, the files at the root and the pages
    new: the harness `.claude/` and `CLAUDE.md`, the files at the root but `LICENSE` and the pages
  - old: 2. List each file under `${CLAUDE_PLUGIN_ROOT}`, but the files under `.claude-plugin/`, `skills/` and `.git/`.
    new: 2. List each file under `${CLAUDE_PLUGIN_ROOT}`, but the files under `.claude-plugin/`, `skills/` and `.git/` and the file `LICENSE` at its root, whose text the project gets as `.guppi/LICENSE`.
  change: the install leaves the LICENSE at the root of the plugin out, and the project gets the license text as .guppi/LICENSE
- slug: estimate-plugin-install-writes-guppi-into-an-empty-project
  set:
    status: pending
    purpose: Whether guppi ship puts the skill install into the clean version, and whether /guppi:install copies every file of the plugin but its own and the LICENSE at its root into a project that holds none of them, the LICENSE of the project left as it stands
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, after the librarian''s run of the session that sets this Criterion: in a later session, with a tag prod-x.y.z in the history of HEAD, the clean version written by the agent in Work Mode into a local folder by uv run --project .guppi guppi ship --allow-draft; at a stop of that Work Mode, in a project that holds only a LICENSE of its own, the person adds that folder as a catalogue by /plugin marketplace add, installs guppi by /plugin install guppi@guppi-marketplace and types /guppi:install; the files of the project, its LICENSE among them, read against those of the plugin and against the Criterion, and the calls of the install read in the transcript of that session under ~/.claude/projects/'
  change: the Criterion replaced whole — the install leaves the LICENSE at the root of the plugin out and keeps the LICENSE of the project; its reading by hand waits for the librarian's run of the session
- slug: entity-sprint-plugin
  replace:
  - old: |-
      the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)
      - The MIT license text carried into the clean copy without breaking the install: `guppi ship` writes `LICENSE` into the copy, and `/guppi:install` leaves it out of the files it copies into a project; taken out of the README and the license (case 1043.2)
    new: the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)
  change: the Backlog line of the MIT license text of the clean copy leaves, decided by case 1049 and case 1052
```

```tasks
- [ ] update `rule-plugin-install`
- [ ] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
- [ ] update `estimate-plugin-install-writes-guppi-into-an-empty-project`
- [ ] read `estimate-plugin-install-writes-guppi-into-an-empty-project`
- [ ] update `entity-sprint-plugin`
- [ ] `uv run --project .guppi guppi sprint`
```

## Deferred

## Case 1050 — The rest of the milestone The plugin put off

> **context:**
> At the close of Plan Mode the person put off the open items left: the line of the brief that names the clean version made into a Claude Code plugin, `rule-morph` and the close of `plugin`, three items of the milestone The plugin of `entity-sprint-plugin`. No Case of this session builds them.

> **problem:**
> No Case of this session decides how the clean version becomes a plugin, how `rule-morph` is read in a new project, or when `plugin` closes.

```then
defer:
  - slug: entity-sprint-plugin
    type: entity
    purpose: "The clean version made into a Claude Code plugin, rule-morph and the close of plugin, three items of the milestone The plugin; put off at the close of Plan Mode of session 0605"
```
