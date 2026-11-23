<!-- approved 15:20:30 · session 68550048 -->

# Session 1353 — a ratified Case checked against a later Case of its session before the showing

## Case 1039 — A later Case finds the lines of the session's Cases that it makes stale

> **context:**
> Each Case of a session is built by its own `case-guppi`, which reads only the Cases that the main agent names as related in its prompt. When a later Case changes how a mechanism works, the Cases already built may still hold lines that describe the old way, and no step searches them before the showing. In session 0807 Case 1035 moved how a hook finds its own refusal from the command of the hook to its name, while Cases 1032.2 and 1032.3, ratified earlier, still spoke of the command, and the Criterion lines of Case 1035 named the old hook registration that Case 1032.1 replaced; the audit of `ask-guppi` at `/pre-spec` found them among 15 findings (`lesson-case-build-a-later-case-leaves-a-ratified-text-stale`). That lesson joined `insight-case-build-sibling-texts-unchecked-before-the-showing`, which stands `open` with severity 2 and `addressed_by` Case 872.1, the fix of its first three lessons. The `SubagentStop` hook of `rule-case-check` already sends `case-guppi` one note that lists each file that names a page or a file its Case changes and that the agent did not read, but it searches only `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`: in `.guppi/guppi/casecheck.py`, `NAMED_IN` holds those four folders, `named_files` reads each file under them, `changed_targets` takes the names of each page the Case updates or deletes and of each file in the first code span of a task line, `looked_files` takes the `Read` and `Grep` calls of the agent, `listed_files` the files an earlier note listed, and `names_notes` builds the note from them; `check_answer` calls `names_notes` and holds the session folder as `folder`, which `judge_and_store` passes, and `is_case_file`, `case_number` and `case_file` are the one judgment of a file of a Case. The person chose that the same note also lists each file `case-<N>.md` of the session but the Case's own file, Cases shown and not yet ratified included, so the step runs on every build. The person also chose that `case-guppi` puts a line of such a file that its change makes false on a line `**Other Case:**`, the route a clash takes, so that the main agent sends that Case back in Plan Mode and it is shown again before `/pre-spec`, and that this Case sets the Insight `actioned`, since its fourth lesson now has a fix too; the cascade of `generate` then archives the two children still live and `clustered` under it, `lesson-case-build-a-later-case-leaves-a-ratified-text-stale` and `lesson-orchestration-batch-asks-one-fork-twice-with-opposite-answers`. The other two children are already archived under `vault/archive/plugin/2026-10-17/2104/lessons/`. A note does not stop the hook, so nothing is blocked. Case 1039.1 changes the hook, its rule and the Criterion of `estimate-case-check-notes-the-files-that-name-what-a-case-changes`, whose `purpose` is set anew since it names what the note lists. Case 1039.2 changes what `case-guppi` does with a listed Case file, a choice of form placed on a new Estimate of `rule-case-build`, since `estimate-case-build-searches-the-names-of-what-it-changes` is `failed` and put off by Case 1038 and its Criterion still holds: a file the change makes false enters the Case, here through the `**Other Case:**` line. Case 1039.2 also adds to the Render of `rule-orchestration` that the main agent sends the other Case back for a stale line as it does after a clash; `estimate-orchestration-shows-the-built-case` stands, since its Criterion sends the other Case back for any line `**Other Case:**`, whatever the reason. `estimate-case-build-reads-no-sibling-file-mid-send` stands: its Criterion says the agent reads no file of a Case built at the same time, and a note that lists that file changes nothing of this. The note asks for a file only where its purpose line or path speaks of the change, and the Render of `rule-case-build` let a file whose purpose line and path speak of something else go unread. A Case file is listed with no purpose line, and its path says nothing of the change, so Case 1039.2 adds a pair to that sentence of the Render: a listed Case file of the session is read whole, or named in `context` where its Case is built at the same time. The text the hook prints stays a minimum, and the Render asks more of the agent. `estimate-case-build-checks-the-finished-case` stands. Its Criterion already says that the agent reads the file of each Case of the session that a note names, and that the new text of the Case does not contradict it. It also says that a file of a Case built at the same time is not read. The judgment of a stale line and the line `**Other Case:**` it gives are the new promise of `estimate-case-build-names-a-stale-line-of-another-case`, so nothing is signed twice. `estimate-case-build-writes-the-case` stands, since its Criterion writes a line `**Other Case:**` whenever `context` says that another Case should change. A Grep of `\.claude/.?,? .?\.guppi/guppi/.? and .?\.guppi/tests/` over `{vault/wiki,.claude,.guppi/guppi}/**` from the root of the repository printed `.guppi/guppi/casecheck.py`, `vault/wiki/rules/rule-case-check.md`, `vault/wiki/estimates/estimate-case-check-notes-the-files-that-name-what-a-case-changes.md` and `vault/wiki/estimates/estimate-sprint-plugin-link-graph-is-gone.md`; the first three enter the Case, and the last stands, since its `method` lists those folders for a search of the link graph, not for the note. A Grep of `Other Case` over the same glob printed 14 files: `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `.claude/agents/case-guppi.md`, `vault/wiki/log.md`, `vault/wiki/lessons/lesson-case-build-a-later-case-leaves-a-ratified-text-stale.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md`, `vault/wiki/estimates/estimate-case-build-names-an-item-not-built-on-the-other-case-line.md`, `vault/wiki/estimates/estimate-orchestration-signs-items-taken-together.md`, `vault/wiki/estimates/estimate-orchestration-passes-a-change-to-an-item-not-built.md`, `vault/wiki/estimates/estimate-case-build-reads-no-sibling-file-mid-send.md` and `vault/wiki/insights/insight-subagents-read-a-sibling-mid-flight.md`; the two Renders and the rendered files enter the Case, and each Estimate stands, since it judges what follows from the line and not why the line is written; the lesson and `insight-subagents-read-a-sibling-mid-flight` tell of past sessions and stand, and the second is the reason why the Render of `rule-case-build` now keeps a note, too, from sending the agent to the file of a Case built at the same time; `brief.md` and `log.md` are not read. The question that `vault/wiki/orchestration.md` lists for Work Mode, whether another Case changes after a clash, stands, since a stale line raises that question by the same line. A Grep of `check_answer|names_notes|run\(\["--subagent"|judge_and_store` over `.guppi/tests/` outside `test_casecheck.py` printed `.guppi/tests/test_case_schema.py` and `.guppi/tests/test_prespec.py`: the first calls `check_answer` with no transcript, so it gets no note of names, and the second only holds the words in the name of a test, so neither changes. `.guppi/tests/test_orchestration.py` reads `vault/wiki/orchestration.md` live, but only its blocks tagged `showing` and `defer`, which the pair does not touch. The Case adds no file. The note of names of the check of this file listed the files that name `casecheck.py`, `guppi casecheck` or `test_casecheck.py`. By their purpose lines and paths, each speaks of another check or another hook, or of code that imports the module, so they stand unread. The one exception is `lesson-case-check-names-note-lists-hundreds-of-files`, which was read. It says that a page or a module that many texts name gives a note of hundreds of files. The new search adds only the Case files of the session that hold such a name, so that cost stays the known cost of the note. A second note listed the files that name `rule-case-check`, `settings.json`, the Insight, `rule-case-build`, `case-guppi.md`, `case-guppi`, `rule-orchestration` and `orchestration.md`. By purpose line and path, they speak of other steps, so they stand unread, with three exceptions. `lesson-orchestration-dispatch-named-a-case-of-the-same-wording-not-related` was read. It finds the same gap in the main agent's choice of related Cases, and the new search narrows it from the side of the hook; the lesson is from session 1713, so it gets no mark. `estimate-orchestration-names-related-cases-in-the-dispatch` stands, since the dispatch does not change. `estimate-case-build-reads-by-need-and-in-parts` stands, since a Case file a note names is read whole, as a related Case file is. The check also notes that a `then` line of Case 1039.2 shares words with one of Case 1039.1. The two stand, since one sets what the hook asks and the other what the agent does. The lesson is from session 0807, so no line carries `{addresses:...}`, and the session's ledger holds no `error` lesson.

> **problem:**
> A Case built later in a session can make lines of a Case already built false, and nothing finds them before `/pre-spec`, so the stale Case is built and ratified again late.

> **recommend:**
> - **Which step should find the lines of other Cases of the session that a new Case makes stale?**
>   - Recommended: (a) the check of a built Case also searches the session's Case files.
>   - Answer: agreed, (a).
> - **Which Case files of the session should the check search?**
>   - Recommended: (a) every Case file of the session but the Case's own.
>   - Answer: agreed, (a).
> - **What should the agent do with a line of another Case that its change makes false?**
>   - Recommended: (a) the stale line goes on an `**Other Case:**` line.
>   - Answer: agreed, (a).
> - **Should this Case close the Insight that the lesson joined?**
>   - Recommended: (a) yes, set the Insight to actioned.
>   - Answer: agreed, (a).

### Case 1039.1 — The note of names lists the session's Case files

> **given:**
> `.guppi/guppi/casecheck.py`: the hook of `rule-case-check`, whose note of names gains the Case files of the session.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the note of names.
> **＋** `rule-case-check`: its Purpose names the folders the note searches.
> **＋** `estimate-case-check-notes-the-files-that-name-what-a-case-changes`: its Criterion is replaced whole.
> **＋** `insight-case-build-sibling-texts-unchecked-before-the-showing`: the Insight this Case sets `actioned`.
> **＋** `rule-one-judgment-one-implementation`: a file of a Case is known by the one judgment of `casecheck.py`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that the hook checks.
> **＋** `cases/`: the folder of the Case files of the session folder, which the note now searches.
> **＋** `vault/wiki/`: the pages the note searches.
> **＋** `.claude/`: the harness files the note searches.
> **＋** `.guppi/guppi/cli.py`: its `COMMANDS` map a command to its module.
> **＋** `vault/wiki/decisions/`: the Decision pages the note leaves out.

> **when:**
> The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that `case-guppi` wrote, whose Case updates or deletes a page, or writes in the first code span of a task line the path of a file of the repository outside `vault/wiki/`.
> **＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up file, transcript, plan file, store and session folder.

> **then:**
> The hook searches the files under `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`, and each file `case-<M>.md` under the `cases/` folder of the session folder, for every name of each such page and file.
> **＋** The names of a page are its slug, the file name of each path of its `governs`, `implementation_ref` and `code_ref`, the name of the agent, or of the skill with its slash, whose file those paths name, and `guppi <command>` for each command that `COMMANDS` of `.guppi/guppi/cli.py` maps to a module of those paths.
> **＋** The names of a file are its file name and the name of the agent, the skill or the command it carries.
> **＋** A task line names a changed file only by its first code span, where that span holds the path of a file of the repository outside `vault/wiki/`.
> **＋** It sends one note that names the Case and lists each file that holds a name and that the subagent, in `agent_transcript_path`, read by no `Read` call of the file and no `Grep` call whose `path` is the file, once, under the first name it holds, with, for a page, its `purpose`, `root_cause` or `pattern` line, however many files hold the name.
> **＋** The note asks the agent to read each listed file whose purpose line or path speaks of what the Case changes, or to name it in `context` with the reason it stands.
> **＋** The note is sent by exit 2 beside any findings and stored under `notes` in `<plan>.checked.json`; a later check of the same Case id lists only the files that no earlier note of that id listed, and sends no note when none is left.
> **－** A later code span of a task line and a code span of a sub-point name no changed file.
> **－** The note leaves out the file of the page or the file itself, the file `case-<N>.md` of the Case itself, the working notes `note-<M>.md`, the pages under `vault/wiki/decisions/`, `log.md` and `brief.md`.
> **－** A note is no finding: the `Stop` check of `guppi casecheck` refuses no showing for it, and a transcript the hook cannot read gives no such note.

```then
update:
- slug: rule-case-check
  replace:
  - old: It sends `case-guppi` one note, too, that lists each file under `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/` that holds a name
    new: It sends `case-guppi` one note, too, that lists each file under `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`, and each file `case-<N>.md` under the `cases/` folder of the session folder but the file of the Case itself, that holds a name
  - old: a transcript the hook cannot read gives no such note (as set in cases 1005.1 and 1011.1).
    new: a transcript the hook cannot read gives no such note (as set in cases 1005.1, 1011.1 and 1039.1).
  change: the note of names lists the Case files of the session too
- slug: estimate-case-check-notes-the-files-that-name-what-a-case-changes
  set:
    status: pending
    purpose: Whether the check of the file of a Case sends case-guppi one note that lists each file, a Case file of the session among them, that names a page the Case changes or the file in the first code span of a task line and that the agent did not read, with the purpose line of a page, however many files hold a name, each file listed once for the Case
  change: the Criterion replaced whole — the note searches the Case files of the session too
- slug: insight-case-build-sibling-texts-unchecked-before-the-showing
  set:
    status: actioned
    addressed_by: decision-case-1039.1
  change: 'actioned: the note of names lists the Case files of the session, and case-guppi sends a stale line to its Case'
```

```tasks
- [x] `.guppi/guppi/casecheck.py`: `names_notes` takes the session folder from `check_answer` and searches, beside the files of `named_files`, each file under its `cases/` folder that `case_number` names, but the file `case_file` names for the top-level Case of each Case of the answer; the module docstring of the note of names names the new files.
- [x] `.guppi/tests/test_casecheck.py`: a test with a second file `case-<M>.md` in the session folder of `working` that names `rule-x`, listed in the note with no purpose line, while the Case's own file and a `note-<M>.md` that name `rule-x` are not listed, and the same file read by `Read` is not listed; each test whose output the new note changes set to the new output.
- [x] update `rule-case-check`
- [x] update `estimate-case-check-notes-the-files-that-name-what-a-case-changes`
- [x] update `insight-case-build-sibling-texts-unchecked-before-the-showing`
- [x] read `estimate-case-check-notes-the-files-that-name-what-a-case-changes`
```

### Case 1039.2 — case-guppi sends a stale line to its Case

> **given:**
> `.claude/agents/case-guppi.md`: the agent that answers the note of names, rendered from `rule-case-build`.
> **＋** `rule-case-build`: its Render sets what the agent does with a listed Case file of the session.
> **＋** `rule-orchestration`: its Render sets what the main agent does with a line `**Other Case:**`.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `estimate-case-build-names-a-stale-line-of-another-case`: the new check of the answer.
> **＋** `rule-case-check`: the hook whose note lists the Case files of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<M>.md`: the file of another Case of the session that the note lists.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, gets from the `SubagentStop` hook of `rule-case-check` a note that lists a file `raw/<date>/<hi HHMM>/cases/case-<M>.md` of another Case of the session, and answers again.

> **then:**
> It reads that Case file whole by `Read`, as it reads each Case file of the session that a note names, and judges each line there that rests on what its own Case changes.
> **＋** Where its change makes such a line false and the other Case should change, its `context` names that Case, the line and the change it needs, and the item of its Case in the summary carries a line `**Other Case:**` that names that Case and the change.
> **＋** Where its own Case is the one that is wrong, it fixes its own Case instead.
> **－** It reads no listed file of a Case that its prompt or a message names as built at the same time; its `context` names that Case and says why the file is not read.
> **－** A line that its change leaves true needs no line `**Other Case:**`.

```then
create:
- slug: estimate-case-build-names-a-stale-line-of-another-case
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi, on a note that lists the Case file of another Case of the session, reads it, and names each line there that its change makes false with the change it needs on a line Other Case of its summary, or fixes its own Case where it is the one that is wrong
  method: 'by hand, after the first build in a session on the new Render of rule-case-build in which the note of the hook of rule-case-check lists the Case file of another Case of the session: the agent transcript of that case-guppi under ~/.claude/projects/, its case file and its summary read against the Criterion, the transcript in the estimate line'
  tags:
  - session
  - workflow
  - harness
  - case-build
update:
- slug: rule-case-build
  replace:
  - old: 'and no other Case of the session: where it changes a page your Case changes or sets what happens at the same moment, bound your Case so that it does not cover that moment, or name its case file in `given`, and read your new text of that page beside its text and fix a contradiction between them (case 579.2).'
    new: 'and no other Case of the session: where it changes a page your Case changes or sets what happens at the same moment, bound your Case so that it does not cover that moment, or name its case file in `given`, and read your new text of that page beside its text and fix a contradiction between them (case 579.2). Where a line of such a file rests on what your Case changes and your change makes it false, judge which Case is wrong: fix your own Case where it is, and where the other Case should change, name in `context` that Case, the line and the change it needs, and again on a line `**Other Case:**` under the item of your Case in the summary, as for a clash below (as set in case 1039.2).'
  - old: read no file of that Case in this build, though this paragraph or a finding of the check names it, and name no file of it in `given`
    new: read no file of that Case in this build, though this paragraph, or a finding or a note of the check, names it, and name no file of it in `given`
  - old: a listed file whose purpose line and path speak of something else needs no read and no line in `context`,
    new: a listed file whose purpose line and path speak of something else needs no read and no line in `context`, but for a Case file of the session, listed with no purpose line, which you read whole as the paragraph that opens with the check of the finished Case sets for a Case of the session that a note names, or name in `context` where its Case is built at the same time as yours,
  change: case-guppi sends a line of a listed Case file that its change makes false to that Case by a line Other Case
- slug: rule-orchestration
  replace:
  - old: since its `context` says that another Case of the session, which it was bounded around after a clash, should change instead, is shown as it stands
    new: since its `context` says that another Case of the session, which it was bounded around after a clash or one of whose lines the Case makes false, should change instead, is shown as it stands
  change: a line Other Case for a stale line of another Case is sent back as after a clash
```

```tasks
- [x] update `rule-case-build`
- [x] update `rule-orchestration`
- [x] create `estimate-case-build-names-a-stale-line-of-another-case`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-case-build-names-a-stale-line-of-another-case`
```

## Case 1040 — The install shows one plan when its session stands in Plan Mode

> **context:**
> `/guppi:install` copies GUPPI into a project. Its skill text, the Render of `rule-plugin-install` in `plugin/skills/install/SKILL.md`, says nothing about Plan Mode. A session opens in Plan Mode before the install when the person's own settings of Claude Code set it, since the project holds no settings of GUPPI yet and the skill copies `.claude/settings.json` last. On this machine `C:/Users/kir/.claude/settings.json` holds `"defaultMode": "plan"`. The handoff of session 0358, at line 40, says that the install of each trial asked the person to approve a plan, since the session opened in Plan Mode. The transcript `~/.claude/projects/C--PROJECTS-guppi-trial-0358-no-git/2cb6dba1-836b-489a-8b55-4e1086bd3135.jsonl` shows `"permissionMode":"plan"` at line 2, the plan file written at line 67, the tool result "User has approved your plan" at line 76 and `"permissionMode":"auto"` at line 82, after which the copy ran. So the approval came by chance, from how the agent read Plan Mode, and no text set it. Case 1036 left this step as it was. The page https://code.claude.com/docs/en/skills lists no frontmatter field of a skill that sets or leaves a permission mode. The page https://code.claude.com/docs/en/permission-modes says that the starting mode comes from the flag `--permission-mode`, then `permissions.defaultMode` in a settings file, `~/.claude/settings.json` among them. It also says that edits stay blocked until the person approves the plan, and that the approval offers to switch to auto mode, to approve each edit by hand, or to keep planning. The person chose that the skill, in Plan Mode, shows one plan of the files it copies and the files of the project it sets aside and asks the approval once; that the plan names no option of the approval; that where `uv` is missing and the person says yes, its installer joins that plan as its first item; and that the new Estimate is read by hand after the librarian's run.
>
> The rule that governs this is the Purpose of `rule-plugin-install`: a project loses no file of its own to the install. A plan that lists the files to set aside before anything moves serves it. The plan approval is a permission of Claude Code and no ratification, so the sentence of `rule-morph` that the person ratifies nothing at `/guppi:install` stands, and the one rule of `vault/wiki/ratification.md`, which a picker does not meet, is not touched. `rule-default-mode` sets Plan Mode in a project of GUPPI, after the install, and it stands. By the rule on form of case 1031.1, I settled one Case with no sub-cases and a new Estimate, `estimate-plugin-install-asks-one-approval-in-plan-mode`. The case of the missing `uv` is the same behaviour, one approval before any write, read from a second install, so it is a line of the same Criterion. No Estimate of `rule-plugin-install` speaks of Plan Mode, by its `purpose`. `estimate-plugin-install-offers-to-install-uv` stands: its `When` names no Plan Mode, and in Plan Mode each of its lines still holds, since the installer only waits for the approval and nothing is written before `uv --version` passes. `estimate-plugin-install-sets-aside-the-files-of-the-project` stands, since the plan comes before its moves and changes none of them. `estimate-plugin-install-writes-guppi-into-an-empty-project`, `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` and `estimate-plugin-install-runs-no-hook-before-uv-sync` speak of the copy, the rollback and the order of the settings file, which do not change.
>
> A Grep of `rule-plugin-install|skills/install` over the root with the glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests,plugin}/**` printed 19 files: `vault/wiki/brief.md` and `vault/wiki/log.md`, not read; `vault/wiki/rules/rule-plugin-install.md`, which changes; `.guppi/tests/test_ship.py`, which writes its own skill text into a temporary folder and reads the live `plugin/plugin.json` and `plugin/marketplace.json` only, so no test reads the skill live; `vault/wiki/rules/rule-clean-branch.md`, which says that `guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, so the new Render holds no pointer to a case; `vault/wiki/rules/rule-harness.md`, which names the page as a child; the five Estimates of the page, judged above; `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-morph-takes-in-the-set-aside-files`, `estimate-sprint-plugin-installs-as-a-plugin` and `estimate-guppi-package-is-ready-after-the-install`, whose `When` names the install as `rule-plugin-install` sets it and holds outside Plan Mode and in it; `estimate-close-commits`, on the path of the skill in a project without the page; and `estimate-ask-opens-a-decision-only-for-a-finding`, `estimate-clean-branch-ships-neutral-texts` and `insight-case-build-changes-a-step-without-reading-its-readers`, where the name stands in a Result or a Pattern of another matter. A Grep of `guppi:install` over the root with the glob `{vault/wiki/rules,vault/wiki/entities,.claude}/**` printed `vault/wiki/entities/entity-sprint-plugin.md`, `vault/wiki/rules/rule-morph.md` and `vault/wiki/rules/rule-plugin-install.md`; the first names the setup after the install, and `rule-morph` is judged above. A Grep of the session's ledger for `lesson\[error\]` and for `\{addresses:` printed nothing, so no mark is added.
>
> The check of this file listed the files that name the pages and files this Case changes, and I judged each one by its purpose line or its path. I read `estimate-guppi-package-is-ready-after-the-install` whole. Its Criterion says that the install runs `uv --version` before it writes anything and asks nothing about `uv` where that passes. Both still hold in Plan Mode, since the plan asks for an approval of the plan and not about `uv`, so it stands. I read `estimate-sprint-plugin-installs-as-a-plugin` whole. Its Criterion asks only that the install copies GUPPI with no error, which holds after the approval, so it stands. The other Estimates of the install in that list are judged above. `rule-harness` names the page only as a child. The listed files that name `SKILL.md` speak of other skills, of `/hi`, of the Case check or of the tests of other commands, not of `/guppi:install`, so they stand. Not done: a session outside Plan Mode, where Claude Code may ask before each command that writes, is left as it is.

> **problem:**
> In a session that stands in Plan Mode, `/guppi:install` can write nothing until the person approves a plan, but the skill sets no such step, so the approval comes by chance and the person sees no list of the files of the project that will move.

> **recommend:**
> - **What /guppi:install does when its session stands in Plan Mode**
>   - Recommended: (a) a written plan step: the skill shows a plan of each file it copies and each file of the project it sets aside, asks the approval once, then runs the install.
>   - Answer: agreed, (a).
> - **Which approval option the plan names**
>   - Recommended: (a) the plan names no option, and the person picks one.
>   - Answer: agreed, (a).
> - **What the plan step does when uv is missing**
>   - Recommended: (a) on the person's yes, the installer of `uv` joins the plan as its first item and runs after the one approval.
>   - Answer: agreed, (a).
> - **When the new Estimate is read**
>   - Recommended: (a) by hand, after the librarian's run of this session.
>   - Answer: agreed, (a).

> **given:**
> `rule-plugin-install`: the page of the skill `/guppi:install`, its Purpose and its Render.
> **＋** `plugin/skills/install/SKILL.md`: the Render, the skill `/guppi:install`.
> **＋** `estimate-plugin-install-asks-one-approval-in-plan-mode`: the new check of the install in Plan Mode.
> **＋** `rule-clean-branch`: `guppi ship --check`, which refuses a pointer to a case in the skill.
> **＋** `rule-morph`: the start of a new project, where the install is no Case.
> **＋** `guppi-set-aside/`: the folder of the project where the install sets aside the files of the project.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in a project open in Claude Code whose session stands in Plan Mode, and the project holds a `CLAUDE.md` of its own and no other file of the install.

> **then:**
> Before it writes or moves anything, the agent checks the paths of the install and shows a plan that lists each file it will copy and each file of the project it will set aside under `guppi-set-aside/`, `CLAUDE.md` among them.
> **＋** The agent asks the person to approve that plan once, by the plan approval of Claude Code, and names none of its options.
> **＋** Once the person approves it, the agent runs the install as `rule-plugin-install` sets it, with no second plan.
> **＋** Where `uv --version` fails and the person says yes to installing `uv`, the installer of `uv` is the first item of that plan, and the agent runs it only after the approval.
> **－** When the person does not approve the plan, the agent writes and moves nothing in the project and stops.

```then
create:
- slug: estimate-plugin-install-asks-one-approval-in-plan-mode
  ref: rule-plugin-install
  kind: QA
  purpose: Whether /guppi:install, in a session that stands in Plan Mode, shows one plan of the files it copies and the files of the project it sets aside, with the installer of uv first where the person said yes to it, asks the approval once and names none of its options, writes nothing before it, and stops with nothing written when the person does not approve it
  method: 'by hand, after the librarian''s run of the session that sets this Criterion: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in a project that holds a CLAUDE.md of its own, Claude Code started by claude --permission-mode plan and /guppi:install typed; in a second such project, Claude Code started the same way from a terminal whose PATH holds no folder of uv, /guppi:install typed and the offer of uv answered yes; in a third such project, /guppi:install typed and the plan not approved; the transcripts of the three sessions under ~/.claude/projects/ and the files of the three projects before and after read against the Criterion'
  tags:
  - plugin
  - harness
update:
- slug: rule-plugin-install
  replace:
  - old: It runs no `guppi` and no `git` command.
    new: When the session of the install stands in Plan Mode, as the person's own settings of Claude Code can set it, the skill writes and moves nothing until the person approves, once, a plan that lists each file it will copy and each file of the project it will set aside, with the installer of `uv` as its first item where the person said yes to it; the plan names no option of the approval, and the skill stops when the person does not approve it (as set in case 1040). It runs no `guppi` and no `git` command.
  - old: On a yes, run the command for this system. When it fails,
    new: On a yes, run the command for this system; in Plan Mode, go on with steps 2 and 3 first, and run it only once the person approves the plan of step 3. When it fails,
  - old: When it passes, go on with step 2. When it fails, say that this session
    new: When it passes, go on with step 2, or, in Plan Mode, with step 4. When it fails, say that this session
  - old: list them, say that the install writes nothing into a project that already holds them, and stop. Write and move nothing.
    new: |-
      list them, say that the install writes nothing into a project that already holds them, and stop. Write and move nothing.
         - When this session stands in Plan Mode and nothing above stopped the install, write and move nothing yet. Write a plan that lists each file to install, each of those paths that already stands in the project and that step 4 or step 7 sets aside under `guppi-set-aside/`, and, when the person said yes in step 1, the installer of `uv` as its first item. Ask the person to approve it once by the plan approval of Claude Code, and name none of its options. When the person does not approve it, write and move nothing, and stop. Once the person approves it, run the installer of `uv` where the plan names it, as step 1 sets it, then go on with step 4.
  change: in Plan Mode the install shows one plan of the files it copies and sets aside, and asks the approval once
```

```tasks
- [x] update `rule-plugin-install`
- [x] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
- [x] create `estimate-plugin-install-asks-one-approval-in-plan-mode`
- [ ] read `estimate-plugin-install-asks-one-approval-in-plan-mode`
```

## Case 1041 — The context gives why the page was chosen for code that no page covers

> **context:**
> When an item points to code that no page covers, `case-guppi` settles a page for the thing the Case changes, an existing page given the path or a new page, as a choice of form. Case 1031.2 set this, and its `then` promised that `context` gives the slug of the chosen page and why it was chosen. The Render it wrote into `rule-case-build` says only that `context` names the page, so a Case can name the page with no reason and the agent is not told to give one. The reading at the Retro of session 0807 (L57 of its ledger) found this gap and set `estimate-case-build-offers-a-page-for-code-no-page-covers` to `failed`. The person chose that the Render gains the reason, so the signed promise holds. The pair changes the one sentence of the Render that names what `context` holds for that choice. The Estimate is set `pending` with its Criterion written as it stands, since its promise does not change, and its `method` is set anew, since it waits for the session that replaces the Criterion, which this Case does not do. On a finding of `/pre-spec`, the `method` also waits for a build in a later session: the rendered agent file is read only when a session starts (`lesson-agents-read-at-session-start-in-claude-code-2-1-228`), so only a later session runs the new text, as the `method` of `estimate-case-build-settles-form-by-itself` already waits for one. The general sentence of the paragraph on forks, which asks the agent to name a choice of form in `context`, stands, since it covers every choice of form and this Case binds only the choice of a page for code. Case 1039.2 of this session changes other paragraphs of the same Render, so its pairs and this pair touch different sentences. A Grep of `case-guppi\.md|rule-case-build` over `.guppi/tests/` printed `.guppi/tests/test_casecheck.py` and `.guppi/tests/test_guppi_package.py`: the first only maps a path to the agent name, and the second names the rule in a docstring, so no test reads the changed text live. The note of names of the check of this file listed the files that name `rule-case-build`, `case-guppi.md` and `case-guppi`. By their purpose lines and paths they speak of other steps, so they stand unread, with two exceptions that were read. `estimate-case-build-settles-form-by-itself` stands, since its Criterion asks `context` to name a choice of form and a reason added for one choice keeps that line true. `.guppi/tests/test_agents.py` stands, since it names `case-guppi` only in made-up transcripts. `estimate-clean-branch-ships-neutral-texts` stands, since the new words put the pointer to this Case in a bracket of its own at the end of the clause. The session's ledger holds no `error` lesson.

> **problem:**
> The Render of `rule-case-build` lets `context` name the chosen page with no reason, while the ratified promise asks for the reason too.

> **recommend:**
> - **Which text changes: the Render or the Criterion?**
>   - Recommended: (a) the Render gains the reason.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: its Render sets what `context` holds for the page of code that no page covers.
> **＋** `.claude/agents/case-guppi.md`: the agent rendered from `rule-case-build`.
> **＋** `estimate-case-build-offers-a-page-for-code-no-page-covers`: its Criterion is written again as it stands and read.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`, builds a Case on an item whose words point to code, a file, a module or a function, that no live page names, by its file or by a folder that holds it, in `code_ref`, `implementation_ref` or `governs`.

> **then:**
> It reads that code in parts, the functions the Case changes and the places that call them, and searches the pages by meaning for the thing that code does.
> **＋** It settles a page only for the thing the Case changes, described from the code it read: where a page already describes that thing, the path added to the field of that page that lists its code; otherwise a new page, its category by the check of the schema of that category, with its slug, its one-line purpose, its parent and its paths.
> **＋** Its `context` gives the slug of the chosen page and why it was chosen.
> **＋** Where the two options differ in behaviour, in cost or in what they block, a round offers them before it writes the Case, and where the person turns down both, it asks in a round which page the Case changes.
> **＋** The page, created or given the path, is a task of the same Case, and the Estimate that checks the change stands on that page.
> **－** Code that the Case does not change gets no page.
> **－** Code that a page names, by its file or by a folder that holds it, gets no page.

```then
update:
- slug: rule-case-build
  replace:
  - old: That is a choice of form, and `context` names the page;
    new: That is a choice of form, and `context` names the page and why you chose it (as set in case 1041);
  change: context gives why the page of code that no page covers was chosen
- slug: estimate-case-build-offers-a-page-for-code-no-page-covers
  set:
    status: pending
    method: 'by hand, at the Retro of the session whose Render of rule-case-build asks context for why the page was chosen: that Render in the Spec read against the Criterion, recorded in the estimate line; by hand, after a session whose case-guppi.md holds this text in which case-guppi settles a page for code that no page covers: the agent transcript of that case-guppi under ~/.claude/projects/ and its case file read against the Criterion, the transcript in the estimate line'
  change: pending again — the Render now asks for the reason, the Criterion as it stood
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] update `estimate-case-build-offers-a-page-for-code-no-page-covers`
- [ ] read `estimate-case-build-offers-a-page-for-code-no-page-covers`
```

## Case 1042 — The workflow of `prod` commits only a copy that passes its style and tests

> **context:**
> The workflow `.github/workflows/prod.yml` builds the clean version by `guppi ship`, runs `claude plugin validate` on it and commits it to `prod`. It runs no style check and no test over the copy, so a copy whose tests fail still reaches `prod` while it stays a valid plugin. Session 0807 added two tests to `.guppi/tests/test_ship.py`, `test_own_style_passes_over_the_copy` and `test_own_tests_pass_over_the_copy` (marked `live`), which build a copy of the repository and run over it the commands of the keys `style` and `test` of `guppi.toml`. The first has no `live` mark, so `guppi test` runs it, and the job `test` of `.github/workflows/checks.yml` runs `guppi test` on `windows-latest` on each pull request and each push but to `prod`; that run does not gate `prod.yml`, which runs beside it. The second is marked `live`, which `addopts = '-m "not live"'` of `.guppi/pyproject.toml` leaves out, so only a person runs it by `-m live`. The selection `-k own_style` takes four tests of `test_ship.py`: `test_own_style_passes_over_the_copy` builds a clean version of the commit and runs the commands of the key `style` over it, and the other three build a made-up tree, call `without_empty_comments`, or stub the format step; the selection `-m live -k own_tests` takes `test_own_tests_pass_over_the_copy` alone, which builds a clean version of the commit and runs the commands of the key `test` over it. The Result of `estimate-clean-branch-copy-passes-its-style-and-tests` reads 4 passed for the first and 1 passed for the second. The job of `prod.yml` runs on `ubuntu-latest`, and no run of the suite on Linux has been read; `checks.yml` runs on `windows-latest`. The copy holds no `guppi.toml`, since `LEFT_OUT` of `.guppi/guppi/ship.py` lists it, so `guppi style` and `guppi test` cannot run inside the copy folder; the person chose the two copy tests of `test_ship.py`, run in the repository, as a step of the same Linux job before the commit, so the first run also reads the suite on Linux, and a red run leaves `prod` at its last commit. The last reading of the suite is under Readings at the close of `brief.md`: `guppi test`: exit 0, 1976 passed, 6 skipped, 2 deselected, which ran on Windows; whether the copy tests pass on Linux is not read, and the new Estimate reads it. Lint there names three pages with `core: true` that are `draft`, so today the step `guppi ship` of a run exits 1; the `when` of Case 1042.1 waits for a run whose `guppi ship` exits 0. As a choice of form, the change splits in two sub-cases: Case 1042.1 adds the step, a sentence to the third paragraph of the Purpose of `rule-clean-branch` and a new Estimate `estimate-clean-branch-prod-commits-only-a-tested-copy`; Case 1042.2 replaces the Criterion of `estimate-clean-branch-copy-passes-its-style-and-tests` without its last line, which says that `prod.yml` does not change and runs neither command, since the rule of atomicity of `ratification.md` keeps the gate of the workflow and the build of the copy apart. Of the Estimates of `rule-clean-branch`, only the purpose of `estimate-clean-branch-installs-as-a-plugin` speaks of the workflow: its Criterion promises the step of `claude plugin validate` before the commit, which stays, so it stands. `estimate-sprint-plugin-ci-writes-a-clean-branch` promises what a run that writes `prod` writes; a red test adds one more way for a run to fail and write nothing, so it stands. The Criterion of `estimate-guppi-repository-keeps-the-development-project` asks that each command of `prod.yml` that runs the tests run through `uv run --project .guppi`; the new commands do, so it stands. `test_no_caller_runs_the_code_or_the_tests_without_the_project` of `.guppi/tests/test_guppi_package.py` reads every file under `.github/workflows` live, by `callers`, and fails on `uv run pytest` as a whole word by `reword_pattern` of `.guppi/guppi/generate.py`; the new commands write `uv run --project .guppi pytest`, which holds no such word, so it stands. The paragraph of `rule-github-repository` on `windows-latest` speaks of `checks.yml`, which does not change, so it stands. A Grep for `prod\.yml` over `vault/wiki/` printed `brief.md`, `log.md`, `rules/rule-clean-branch.md`, `rules/rule-github-repository.md` and the estimates `estimate-clean-branch-copy-passes-its-style-and-tests`, `estimate-clean-branch-installs-as-a-plugin`, `estimate-clean-branch-refuses-a-draft-core-page`, `estimate-clean-branch-ships-the-checks-workflow`, `estimate-guppi-package-runs-from-its-own-folder`, `estimate-guppi-repository-keeps-the-development-project` and `estimate-sprint-plugin-ci-writes-a-clean-branch`; of these, only the last line of the Criterion of `estimate-clean-branch-copy-passes-its-style-and-tests` is made false, and the rest stand as said above, or name only `--allow-draft`, the files that `guppi ship` writes, or History. A Grep for `prod\.yml|runs neither command` over `.claude/` printed nothing. A Glob `vault/**/estimate-clean-branch-prod-*` printed nothing, so the new slug is free. Of the files that name `rule-clean-branch`, the purpose lines of `entity-sprint-plugin` and `entity-guppi-repository` speak of the workflow: the milestone The clean branch of the first says that a CI run writes the clean version and writes nothing to `prod` while a blocking page stands, and the second names `rule-clean-branch` as the workflow that writes `prod`; both stay true with one more step that can stop the run, so both stand. The other files on that list speak of other parts of the clean version, of `guppi ship` or of the settings, not of the workflow. The `then` of Case 1042.2 leaves out on purpose the line of the old Criterion on `prod.yml`, and its line on the key `style` speaks of the test that `guppi test` runs, while the first line of Case 1042.1 speaks of the step of the workflow, so the two do not sign one promise twice. The ledger of the session holds no `error` lesson.

> **problem:**
> A clean version whose style check or tests fail can reach `prod`, and nobody has run the suite on Linux, the system of the job that writes `prod`.

> **recommend:**
> - **What the run checks before it commits**
>   - Recommended: (b) the two copy tests of `test_ship.py`, `-k own_style` and `-m live -k own_tests`.
>   - Answer: agreed, (b).
> - **On which system the check runs**
>   - Recommended: (a) a step in the same Linux job, before the commit.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) a new Estimate for the workflow, and the old Criterion replaced without its line on `prod.yml`.
>   - Answer: agreed, (a).

### Case 1042.1 — The workflow runs the copy tests before it commits

> **given:**
> `.github/workflows/prod.yml`: the workflow that writes `prod`, which gains the step.
> **＋** `rule-clean-branch`: the rule of the clean version and of its workflow.
> **＋** `estimate-clean-branch-prod-commits-only-a-tested-copy`: the new check of the step.
> **＋** `.guppi/tests/test_ship.py`: the two tests that run the style and the tests over a copy.
> **＋** `uv run --project .guppi pytest .guppi/tests/test_ship.py -k own_style`: the command of the test of the style over a copy.
> **＋** `uv run --project .guppi pytest .guppi/tests/test_ship.py -m live -k own_tests`: the command of the test of the tests over a copy.
> **＋** `guppi.toml`: the commands of the keys `style` and `test`.
> **＋** `.github/workflows/checks.yml`: the CI of pull requests, which stays as it is.

> **when:**
> A push to `main`, or a push of a tag `prod-*` on a commit of another branch, starts a run of `.github/workflows/prod.yml` on GitHub, as `rule-clean-branch` sets it, and its step `uv run --project .guppi guppi ship` exits 0.

> **then:**
> Before its step that commits to `prod`, the job runs `uv run --project .guppi pytest .guppi/tests/test_ship.py -k own_style` and `uv run --project .guppi pytest .guppi/tests/test_ship.py -m live -k own_tests` on its runner `ubuntu-latest`.
> **＋** Each of the two exits 0 there on a commit whose clean version passes the commands of the keys `style` and `test` of `guppi.toml`.
> **－** A run where either of the two exits non-zero fails and writes nothing to `prod`.
> **－** `.github/workflows/checks.yml` does not change.

```then
create:
- slug: estimate-clean-branch-prod-commits-only-a-tested-copy
  ref: rule-clean-branch
  kind: QA
  purpose: Whether the workflow prod.yml runs the tests of test_ship.py selected by -k own_style and by -m live -k own_tests, which check the style and the tests of a clean version, on its Linux runner before it commits, and writes nothing to prod when one of them fails
  method: 'by hand: .github/workflows/prod.yml read against the Criterion; by hand, after a run of .github/workflows/prod.yml on GitHub whose step guppi ship exits 0: the output of gh run view --log of that run read against the Criterion, written into the estimate line'
  tags:
  - ci
  - plugin
  - tests
update:
- slug: rule-clean-branch
  replace:
  - old: Before it commits, it installs Claude Code and runs `claude plugin validate` on the clean folder, and writes nothing when that check fails (case 816).
    new: Before it commits, it installs Claude Code and runs `claude plugin validate` on the clean folder, and writes nothing when that check fails (case 816). Before it commits, the same job, on Linux, also runs the tests of `.guppi/tests/test_ship.py` whose names hold `own_style`, among them the one that builds a clean version of the commit and runs over it the commands of the key `style` of `rule-guppi-config`, and the test marked `live` whose name holds `own_tests`, which builds one and runs over it the commands of the key `test`, and writes nothing when one of them fails, so a clean version whose style or tests fail never reaches `prod` (as set in case 1042.1).
  change: the workflow of prod runs the style and the tests over a copy before it commits
```

```tasks
- [x] update `rule-clean-branch`
- [x] create `estimate-clean-branch-prod-commits-only-a-tested-copy`
- [x] `.github/workflows/prod.yml`: a step after the step that runs `claude plugin validate` and before the step that commits to `prod` runs `uv run --project .guppi pytest .guppi/tests/test_ship.py -k own_style` and then `uv run --project .guppi pytest .guppi/tests/test_ship.py -m live -k own_tests`; the comment at its head says that the run commits only when both pass.
- [ ] read `estimate-clean-branch-prod-commits-only-a-tested-copy`
```

### Case 1042.2 — The build of the copy no longer promises that `prod.yml` runs no check

> **given:**
> `estimate-clean-branch-copy-passes-its-style-and-tests`: its Criterion is replaced whole, without its line on `prod.yml`.
> **＋** `rule-clean-branch`: the rule of the clean version.
> **＋** `.guppi/guppi/ship.py`: the command `guppi ship`.
> **＋** `.guppi/tests/test_ship.py`: the tests that run the style and the tests over a copy.
> **＋** `guppi.toml`: the commands of the keys `style` and `test`.
> **＋** `.ruff_cache/`: the cache folder of ruff, which the clean version does not hold.

> **when:**
> `uv run --project .guppi guppi ship <folder>` of `.guppi/guppi/ship.py`, as `rule-clean-branch` sets it, builds the clean version from the working tree into an empty folder.
> **＋** Then `.guppi/tests/test_ship.py` runs over that folder the commands of the keys `style` and `test` of `guppi.toml`.

> **then:**
> In a Python file it writes, it removes each comment that the removal of a bracket left empty, with the spaces before it, and the whole line where that comment stood alone.
> **＋** In each text file it writes, a bracket that holds a pointer and stands alone on its line goes with that line.
> **＋** As its last step it runs `ruff format` over `.guppi/` of the folder.
> **＋** The commands of the key `style` exit 0 over the folder, in a test that `uv run --project .guppi guppi test` runs.
> **＋** The commands of the key `test` exit 0 over the folder, in a test marked `live`, and a test that needs a file or a module that the clean version does not hold is skipped.
> **－** Where `ruff format` does not start or does not exit 0, it prints one `ship:` line and exits 1.
> **－** That run keeps its cache in a temporary folder outside the folder, so the clean version holds no `.ruff_cache/`.
> **－** `--check` runs no `ruff format`.

```then
update:
- slug: estimate-clean-branch-copy-passes-its-style-and-tests
  set:
    status: pending
  change: the Criterion replaced whole — the line that prod.yml runs neither command is gone, since the workflow now runs both
```

```tasks
- [x] update `estimate-clean-branch-copy-passes-its-style-and-tests`
- [x] read `estimate-clean-branch-copy-passes-its-style-and-tests`
```

## Case 1043 — The README says what GUPPI is, and the repository carries the MIT license

> **context:**
> The root `README.md` is a note left from the split of this repository from another one. It is titled "Vault harness", tells of that split and points to `make help`. It says neither what GUPPI is nor how to install it, and no `LICENSE` file stands at the root. The milestone The plugin of `entity-sprint-plugin` asks for a README on what the project is, what it is for, its main parts and its use. Before the Case the person chose one README in English for a reader who finds the repository on GitHub, a first-person Why on the trade-off between control and cost, an Is it for you section, a plain tone, an honest status, and the MIT license. `guppi ship` of `.guppi/guppi/ship.py` takes from the root only the files of `ROOT_FILES`, which are `CLAUDE.md` and `.gitattributes`, so the copy on `prod` holds neither file. Step 2 of `plugin/skills/install/SKILL.md` copies each file of the plugin into the project, and step 3 stops on a path other than `CLAUDE.md`, a file under `.claude/`, `.gitattributes` or `.github/workflows/checks.yml`. A README or a license in the copy would therefore stop the install in a project that holds its own, and the person chose to keep both files on `main` only. Not done: the copy that people install carries no license text, which the MIT license asks of each copy; as the person chose at `/pre-spec` under `rule-backlog`, Case 1043.2 adds that item to the `## Backlog` of `entity-sprint-plugin`, so that it shows in `backlog.md`, and no line of `then` promises it. Lint, under Flags of `vault/wiki/brief.md`, names three pages with `core: true` that are `draft`, so a run of the workflow writes nothing to `prod` yet. The README therefore gives the install from GitHub by `#prod`, which the page https://code.claude.com/docs/en/plugins/host-marketplace.md sets as the way to add a marketplace from a branch, says that no release has reached `prod` yet, and gives the install from a local copy by `guppi ship --allow-draft`. Whether the branch `prod` stands on GitHub was not checked. The person chose no cost figure, since the trial of `estimate-sprint-plugin-case-guppi-level-trial-decided` is read only at the close of the sprint. The README may describe `/guppi:install` as Case 1040 leaves it, with one plan in Plan Mode, and the workflow of `prod` as Case 1042 leaves it; it states neither in more detail than those Cases set.
>
> No page names `README.md` or `LICENSE` in `code_ref`, `implementation_ref` or `governs`. As a choice of form, both paths go into the `code_ref` of `entity-guppi-repository`, the page of the repository on GitHub, since both files belong to this repository and not to the copy. That page has no `core`, so the change blocks no build. The README is checked by `estimate-sprint-plugin-readme-describes-the-project`. Its Criterion signs only part of what the person chose, and in other words, and its `When` names no branch, so, by the finding of `/pre-spec`, Case 1043.1 replaces that Criterion whole with its own `when` and `then`. The person's confirmation stays a line of it, and the `method`, which reads at the `/hi` of the session after the one whose Work Mode writes `README.md`, stands; its `purpose` still states the promise, so it stands too. Work Mode writes on the branch of the session, `plugin`, and the files reach `main` only by a later merge that no Case of this session makes, so both Criteria read each file at the root of the branch of the session that wrote it. The license is a condition that can fail apart from the README, so Case 1043.2 creates `estimate-guppi-repository-carries-the-mit-license`; a Glob `vault/**/estimate-guppi-repository-*license*` printed nothing, so the slug is free. The Estimates of `entity-guppi-repository` speak of the remote, of the development project and of the merge tasks, by their `purpose`, so none of them changes. The root `.gitignore` ignores neither file. A Grep of `os\.walk|rglob|\.glob\(|iterdir` over `.guppi/guppi/` printed hits in 15 modules: `agents.py`, `archive.py`, `backlog.py`, `casecheck.py`, `caseid.py`, `cleanup.py`, `generate.py`, `ledger.py`, `lint.py`, `materialize.py`, `onward.py`, `pages.py`, `prespec.py`, `ship.py` and `sprint_close.py`. Each walks a folder of the vault, of a session or of the copy, and none walks the root: `ship.py` walks only `.guppi` and `.claude`, and `named_files` of `casecheck.py` walks only the folders of `NAMED_IN`. The same Grep over `.guppi/tests/` printed 16 files. Of those that walk the real repository, `test_case_schema.py` at line 47 and `test_orchestration.py` at line 108 take only the `schema.yaml` of each category under `vault/wiki/`, and `callers` of `test_guppi_package.py` takes the root `Makefile` and each file under `.claude` and `.github/workflows`; the others walk a temporary folder. Two readers take every file of the root: line 27 of `.gitattributes`, `* text=auto eol=lf`, which gives `LICENSE` LF line ends, as it should, and the commands of the key `style` of `guppi.toml`, `ruff check .` and `ruff format --check .`, which judge Python files only. So the new file makes no reader wrong. The check of this file listed the files that name what the Case changes. `.guppi/tests/test_ship.py` names a `README.md` only under `.guppi/.pytest_cache/` of a temporary folder, and `.guppi/tests/test_generate.py` names one only as the `governs` of a sample page in a temporary folder, so neither reads the root file and both stand. `vault/wiki/sprint.md` names the README in a milestone line of The plugin. This Case closes no milestone line: the update of `entity-sprint-plugin` in Case 1043.2 only adds a line to its `## Backlog`, so the line stays until the README Estimate is read. `entity-guppi`, `rule-github-repository` and the three Estimates of `entity-guppi-repository` name the page, and by their purpose lines they speak of GUPPI as a whole, of pull requests and rulesets, of the remote, of the development project and of the merge tasks. None of them speaks of the README or the license, so they stand. The new Criterion keeps each line of the old one word for word and adds lines after them. `lesson-hi-unread-sprint-reading-made-a-case-line` names the README Estimate. Its root cause is a step of `/hi` that makes a Cases line for an open reading, so it stands. `vault/wiki/backlog.md` is rendered from the `## Backlog` of the sprint page and gains the new line at the render. The other files that name `entity-sprint-plugin` stand, since none of them speaks of its Backlog or of the README:
> - `entity-sprint`, `rule-guppi-config`, `rule-morph` and `rule-spec-box`, by their purpose lines;
> - the other Estimates of the sprint page and `estimate-case-build-reads-the-readers-of-a-new-files-folder`, `estimate-spec-box-runs-a-conserved-spec` and `estimate-sprint-keeps-one-live-page`, by their purpose lines;
> - `.guppi/guppi/lint.py` at line 753 and `.guppi/tests/test_lint.py` at line 928, which name the page only in samples of a `method`;
> - `.guppi/tests/test_prespec.py` from line 1383, which seeds a page of that name in a temporary folder.
>
> A Grep of the session's ledger for `lesson\[error\]` and for `\{addresses:` printed nothing, so no mark is added.

> **problem:**
> A reader who finds GUPPI on GitHub learns neither what it is nor how to install it, and the repository states no license.

> **recommend:**
> - **Which branches hold README.md and LICENSE**
>   - Recommended: (a) main only.
>   - Answer: agreed, (a).
> - **What the install section tells a reader while prod holds no release**
>   - Recommended: (a) both paths, with a note that no release is out yet.
>   - Answer: agreed, (a).
> - **Whose name the MIT license names**
>   - Recommended: (a) the GitHub name `kirMykholap`.
>   - Answer: agreed, (a).
> - **Whether the README gives a figure for the cost**
>   - Recommended: (a) no figure now.
>   - Answer: agreed, (a).
> - **How the README and the license are checked**
>   - Recommended: (a) the existing README Estimate, plus a new Estimate for the license.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person agreed that the license text of the clean copy goes into the `## Backlog` of `entity-sprint-plugin`, and that no line of `then` promises it.
>   - Taken: Case 1043.2 updates `entity-sprint-plugin` with that Backlog line, and its `－` line is dropped; by the other findings, Case 1043.1 replaces the Criterion of the README Estimate, and both Criteria read the files on the branch of the session.

### Case 1043.1 — The README says what GUPPI is, its parts and its use

> **given:**
> `README.md`: the README at the root of the repository, written anew.
> **＋** `entity-guppi-repository`: the page of the repository, whose `code_ref` names the file.
> **＋** `estimate-sprint-plugin-readme-describes-the-project`: the check of the README, whose Criterion is replaced whole.
> **＋** `rule-plugin-install`: the install that the README describes.
> **＋** `rule-clean-branch`: the copy on `prod`, which holds no README.

> **when:**
> In a session of the sprint `plugin` before its close, the person reads `README.md`.
> **＋** The person reads it at the root of the branch of the session whose Work Mode wrote it.

> **then:**
> `README.md` says what GUPPI is and what it is for.
> **＋** It names the main parts of the project and what each one does.
> **＋** It says how to install GUPPI and how to use it.
> **＋** It holds a first-person Why on control against cost, an Is it for you section, and how a session goes, from its opening through planning, the Spec, the work and the retro to the handoff and the librarian's run.
> **＋** The parts it names are the vault, the harness rendered from the rules, the package with the command `guppi`, and the plugin with the branch `prod`.
> **＋** Its install gives the path from GitHub by `#prod`, says that no release has reached `prod` yet, gives the path from a local copy by `guppi ship --allow-draft` and a table of the commands, and its status reads early, opinionated and expensive in tokens, with no figure of cost, beside the MIT license.
> **＋** The person says that it describes the project as it stands.

```then
update:
- slug: entity-guppi-repository
  set:
    code_ref:
    - README.md
    - LICENSE
  change: code_ref names README.md and LICENSE, the files of the repository on GitHub
- slug: estimate-sprint-plugin-readme-describes-the-project
  set:
    status: pending
  change: the Criterion replaced whole — it reads README.md at the root of the branch of the session that wrote it and names each section the person chose
```

```tasks
- [x] update `entity-guppi-repository`
- [x] `README.md`: written anew in English, about 150 to 250 lines, in the plain tone set above: a header with `plugin/assets/logo_guppi.png` and one sentence; Why; Is it for you; how a session goes; the main parts; install, by `/plugin marketplace add kirMykholap/GUPPI#prod`, `/plugin install guppi@guppi-marketplace` and `/guppi:install`, the note that no release has reached `prod` yet and the local path by `uv run --project .guppi guppi ship --allow-draft <folder>`; use, a table of the commands; status and limits; contributing; license, MIT. Each install step is checked against `plugin/skills/install/SKILL.md` as it stands when the README is written.
- [x] update `estimate-sprint-plugin-readme-describes-the-project`
- [ ] read `estimate-sprint-plugin-readme-describes-the-project`
```

### Case 1043.2 — The repository carries the MIT license

> **given:**
> `LICENSE`: the new license file at the root of the repository.
> **＋** `entity-guppi-repository`: the page of the repository, whose `code_ref` names the file.
> **＋** `estimate-guppi-repository-carries-the-mit-license`: the new check of the license.
> **＋** `entity-sprint-plugin`: the sprint page, whose `## Backlog` keeps the license of the clean copy.

> **when:**
> A person reads `LICENSE` at the root of the branch of the session whose Work Mode wrote it.

> **then:**
> `LICENSE` holds the text of the MIT license, whole and unchanged.
> **＋** Its copyright line reads `Copyright (c) 2026 kirMykholap`.

```then
create:
- slug: estimate-guppi-repository-carries-the-mit-license
  ref: entity-guppi-repository
  kind: QA
  purpose: Whether LICENSE at the root of the repository holds the whole MIT license with the copyright line of kirMykholap
  method: 'by hand, in the Work Mode of the session that writes LICENSE: the file at the root of the branch of that session read against the text of the MIT license at https://opensource.org/license/mit and against the Criterion'
  tags:
  - github
  - git
update:
- slug: entity-sprint-plugin
  replace:
  - old: the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)
    new: |-
      the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)
      - The MIT license text carried into the clean copy without breaking the install: `guppi ship` writes `LICENSE` into the copy, and `/guppi:install` leaves it out of the files it copies into a project; taken out of the README and the license (case 1043.2)
  change: the Backlog keeps the MIT license text of the clean copy
```

```tasks
- [x] create `estimate-guppi-repository-carries-the-mit-license`
- [x] `LICENSE`: the text of the MIT license, its copyright line `Copyright (c) 2026 kirMykholap`.
- [x] read `estimate-guppi-repository-carries-the-mit-license`
- [x] update `entity-sprint-plugin`
- [x] `uv run --project .guppi guppi sprint`
```
