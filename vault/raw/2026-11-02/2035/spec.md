<!-- approved 21:26:28 · session 591bb5b1 -->

# Session 2035 — the sprint plugin: readings put off and the clean branch

## Case 1010 — The note of names narrows to the files a task changes and groups a broad name

> **context:**
> When `case-guppi` stops, the `SubagentStop` hook of `rule-case-check` searches every file under `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/` for the names of each page the Case updates or deletes and of each file whose path a task line writes in a code span. It sends one note for each file that holds a name and that the agent did not read (case 1005.1). `lesson-case-check-names-note-lists-hundreds-of-files` records a probe of the last session over the live repository: 195 files for an update of `rule-case-build`, 103 for `rule-case-check`, 89 for `prespec.py`, and 657 notes for the file of Case 1005, whose task line named in later code spans the modules it only imports. The handoff of session 1548 left the choice until a real note was seen. The person chose to narrow now, from the probe: only the first code span of a task line names a changed file, and a name that more than 20 of the searched files hold gives one note with its count in place of a note for each file. The Case splits in three, as the atomicity rule of `ratification.md` sets, since each part can fail alone and needs its own fix.
> `case-guppi` read in `.guppi/guppi/casecheck.py` whole the functions `looked_files`, `carried_names`, `changed_targets`, `named_files`, `name_pattern`, `names_notes` and the part of `check_answer` that joins them: `changed_targets` takes every code span of the `tasks` section by `CODE_SPAN`, those of the sub-points too, and keeps each that is the path of a file outside `vault/wiki/`; `names_notes` gives each file one note, by the first name of the Case it holds, whatever count of files hold that name. `read_tasks` of `.guppi/guppi/ratified.py` gives the task lines without their sub-points, the one reading of a task line that the Spec hook runs, so the new code imports it with `CODE_SPAN` of `.guppi/guppi/lint.py`. A Grep of `.guppi/guppi/` for `first code span|CODE_SPAN|def task_command|def _first` printed `casecheck.py`, `config.py`, `ratified.py`, `prespec.py`, `pointers.py`, `lint.py` and `generate.py`; read around each hit, no function reads the first code span of a task line as a path: `command_line` of `.guppi/guppi/render.py`, read whole, matches a code span that holds a command, for the ticker, and `title_slugs` of `.guppi/guppi/generate.py` reads a Frontier line, so the task adds no second copy of a judgment (`rule-one-judgment-one-implementation`). A task line that opens with a code span holding a command, such as a render line `uv run --project .guppi guppi render` with the rendered file in its second span, keeps the form `case-schema.md` sets for it, since the ticker matches the command in its first span; the hook takes no changed file from such a line, and the `governs` of the updated rule still carries the names of the rendered file. So `estimate-prespec-catches-a-command-line-off-form` and `estimate-render-harness-ticks-the-spec`, whose criteria speak of the command in the first code span of a task line, stand: the Case leaves command lines as they are, and Case 1010.3 names them as the one exception to its form.
> A Grep over `{vault/wiki,.claude}/**` for `note of names|names note|whose path a task line|in a code span of its task line` printed six files: `rule-case-check`, `rule-case-build` and `.claude/agents/case-guppi.md`, its render, enter the Case; `estimate-case-build-searches-the-names-of-what-it-changes` enters Case 1010.3; `lesson-case-check-names-note-lists-hundreds-of-files` stands, since it records what the probe found; `brief.md` is not read. A Grep of `.guppi/tests/` for `case-guppi\.md|rule-case-check|rule-case-build` printed `test_orchestration.py`, `test_onward.py`, `test_guppi_package.py` and `test_casecheck.py`: the first two name the rule in a docstring; `test_guppi_package.py` reads the live pages for old command forms and old paths, and the new texts write only `.guppi/`-prefixed paths; `test_casecheck.py` runs over a made-up project; `test_case_schema.py` runs `check_answer` with no transcript, so it gives no note of names. The criteria of `estimate-case-check-notes-the-files-that-name-what-a-case-changes` and `estimate-case-build-searches-the-names-of-what-it-changes` speak of the note, so Cases 1010.1 and 1010.3 replace them; no other Estimate of `rule-case-check` or `rule-case-build` speaks of it. L11 of session 1548 is a `knowledge` lesson of another session, so no `{addresses:...}` mark; the ledger of this session holds no lesson line.
> The check of this file sent the first real note of names, as the person was told it likely would: one note for each of some hundreds of files, by the names `rule-case-check`, `rule-case-build`, `case-guppi`, `case-guppi.md`, `casecheck.py`, `test_casecheck.py`, `tags.py`, `settings.json` and `guppi casecheck`, so the note itself shows the breadth this Case cuts. `case-guppi` named them here by name rather than reading each file, as Case 1010.3 sets for a broad name. Each stands, since it names the rule, the agent, the module, its test or the settings for another promise and not for the note of names. That claim rests on a Grep over `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` for `names? what (a|its|the) Case changes|that names? a page or a file|a note once for each|holds a name of a page|names_notes|changed_targets`. It printed `rule-case-check`, `rule-case-build`, `.claude/agents/case-guppi.md`, `estimate-case-check-notes-the-files-that-name-what-a-case-changes`, `estimate-case-build-searches-the-names-of-what-it-changes`, `.guppi/guppi/casecheck.py`, `brief.md` and `log.md`. Each of the first six enters the Case, and the last two are not read. The notes of a Criterion line not carried are meant: Case 1010.1 changes the trigger and adds the first code span, Case 1010.3 changes the trigger, the read of a noted file and the task-line line, and they carry every other line word for word. The limit of 20 files stands in Case 1010.2 alone, whose tasks build it; Case 1010.1 points to its Estimate for a broad name, so the limit is not signed twice. The notes of `then` lines shared between sub-cases stand: those lines state the same frame for the hook and for the agent, and each sub-case promises its own behaviour.

> **problem:**
> The note of names can send `case-guppi` hundreds of notes for one Case, because it takes the modules a task only imports for files it changes, and because a name that hundreds of texts hold gives one note per file.

> **recommend:**
> - **Narrow the note now or wait for a real one**
>   - Recommended: (a) narrow now, from the probe, since the probe ran the hook's own functions over the live files.
>   - Answer: (a), narrow now.
> - **Which paths of a task line count as changed files**
>   - Recommended: (a) only the first code span, when it is a path; a task that changes two files takes two task lines.
>   - Answer: (a).
> - **What the note does with a name that many files hold**
>   - Recommended: (a) one note for a broad name, a name that more than 20 files hold.
>   - Answer: (a), more than 20 files.
> - **How the Case splits and what checks each part**
>   - Recommended: (a) three parts, each with its own check: the first code span, the note of a broad name with a new Estimate, and the answer of `case-guppi`.
>   - Answer: (a).

### Case 1010.1 — Only the first code span of a task line names a changed file

> **given:**
> `rule-case-check`: the rule of the check, whose Purpose names the paths of a task line.
> **＋** `.guppi/guppi/casecheck.py`: `changed_targets`, which takes the paths of the task lines.
> **＋** `.guppi/guppi/ratified.py`: `read_tasks`, the one reading of the task lines, imported.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the note of names.
> **＋** `estimate-case-check-notes-the-files-that-name-what-a-case-changes`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that the hook checks.
> **＋** `vault/wiki/`: the pages the hook searches, the Decision pages under `vault/wiki/decisions/` left out.
> **＋** `.claude/`: the harness files the hook searches.
> **＋** `.guppi/guppi/cli.py`: `COMMANDS`, which maps a command to its module.
> **＋** `estimate-case-check-sends-one-note-for-a-broad-name`: the check of a broad name, set by Case 1010.2.

> **when:**
> The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that `case-guppi` wrote, whose Case updates or deletes a page, or writes in the first code span of a task line the path of a file of the repository outside `vault/wiki/`.
> **＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up file, transcript, plan file and store.

> **then:**
> The hook searches the files under `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/` for every name of each such page and file.
> **＋** The names of a page are its slug, the file name of each path of its `governs`, `implementation_ref` and `code_ref`, the name of the agent, or of the skill with its slash, whose file those paths name, and `guppi <command>` for each command that `COMMANDS` of `.guppi/guppi/cli.py` maps to a module of those paths.
> **＋** The names of a file are its file name and the name of the agent, the skill or the command it carries.
> **＋** A task line names a changed file only by its first code span, where that span holds the path of a file of the repository outside `vault/wiki/`.
> **＋** For each file that holds a name and that the subagent, in `agent_transcript_path`, read by no `Read` call of the file and no `Grep` call whose `path` is the file, it sends a note that names the Case, the path, the name the file holds and, for a page, its `purpose`, `root_cause` or `pattern` line, and asks the agent to read the file or to name it in `context` with the reason it stands.
> **＋** Each note is sent once by exit 2 beside any findings, stored under `notes` in `<plan>.checked.json`, and not sent again for the same Case id.
> **－** A later code span of a task line and a code span of a sub-point name no changed file.
> **－** A name that many files hold is checked by `estimate-case-check-sends-one-note-for-a-broad-name`, not here.
> **－** The note leaves out the file of the page or the file itself, the pages under `vault/wiki/decisions/`, `log.md` and `brief.md`.
> **－** A note is no finding: the `Stop` check of `guppi casecheck` refuses no showing for it, and a transcript the hook cannot read gives no such note.

```then
update:
- slug: rule-case-check
  replace:
  - old: whose path a task line of the Case writes in a code span
    new: whose path the first code span of a task line of the Case writes
  change: the note of names takes only the first code span of a task line as a changed file
- slug: estimate-case-check-notes-the-files-that-name-what-a-case-changes
  set:
    status: pending
    purpose: Whether the check of the file of a Case sends case-guppi a note once for each file that names a page the Case changes or the file in the first code span of a task line and that the agent did not read, with its path, the name it holds and the purpose line of a page
  change: the Criterion replaced whole — only the first code span of a task line names a changed file
```

```tasks
- [ ] update `rule-case-check`
- [ ] update `estimate-case-check-notes-the-files-that-name-what-a-case-changes`
- [x] `.guppi/guppi/casecheck.py`: `changed_targets` takes the task lines by `read_tasks` of the module `ratified`, imported, and of each line only its first code span by `CODE_SPAN`, kept where it is the path of a file outside `vault/wiki/`; the module docstring and the docstrings of `changed_targets` and `check_answer` say so.
- [x] `.guppi/tests/test_casecheck.py`: a test that a path in a later code span of a task line, and one in a code span of a sub-point, gives no note, while the path in the first code span still does.
- [x] `uv run --project .guppi guppi test`: passes.
- [ ] read `estimate-case-check-notes-the-files-that-name-what-a-case-changes`
```

### Case 1010.2 — A name that many files hold gives one note

> **given:**
> `rule-case-check`: the rule of the check, whose Purpose sets the note of names.
> **＋** `.guppi/guppi/casecheck.py`: `names_notes`, which gives the notes.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the note of names.
> **＋** `estimate-case-check-sends-one-note-for-a-broad-name`: the new check of the note of a broad name.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that the hook checks.
> **＋** `vault/wiki/decisions/`: the Decision pages, left out of the count.

> **when:**
> The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that `case-guppi` wrote, and more than 20 of the files it searches for the names of a page or a file the Case changes hold one such name.
> **＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up file, transcript, plan file and store.

> **then:**
> The hook sends one note for that name, which names the Case, the name and the count of the files that hold it, and asks the agent to search for the name and to name in `context` that search and why each file it does not enter stands.
> **＋** A file that holds no other name of the Case, or only other names that more than 20 of the searched files hold, gets no note of its own.
> **＋** A file that also holds a name that 20 or fewer of the searched files hold keeps its own note for that name.
> **－** Neither the file of the page or the file itself, nor a page under `vault/wiki/decisions/`, `log.md` or `brief.md`, adds to the count.

```then
create:
- slug: estimate-case-check-sends-one-note-for-a-broad-name
  ref: rule-case-check
  kind: QA
  purpose: Whether the check of the file of a Case sends case-guppi one note with the name and the count for a name of what the Case changes that more than 20 of the searched files hold, in place of a note for each of those files
  method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py, passed and not skipped
  tags:
  - hooks
  - harness
  - workflow
  - case-build
update:
- slug: rule-case-check
  replace:
  - old: gives no such note (as set in case 1005.1).
    new: gives no such note (as set in case 1005.1). For a name that more than 20 of the files it searches hold, it sends one note in place of a note for each of those files, with the name and the count of the files, and asks `case-guppi` to search for the name and to name in `context` that search and why each file it does not enter stands; a file that holds a name that 20 or fewer of them hold is still noted alone for that name (as set in case 1010.2).
  change: a name that more than 20 of the searched files hold gives one note with its count
```

```tasks
- [ ] update `rule-case-check`
- [ ] create `estimate-case-check-sends-one-note-for-a-broad-name`
- [x] `.guppi/guppi/casecheck.py`: `names_notes` counts for each name of a Case the searched files that hold it, the file of the page or the file itself left out; a name held by more than `BROAD_NAME`, 20, files gives one note `note: case <N>: <count> files name <name>: …` and no note of a file by that name; the module docstring and the docstrings of `names_notes` and `check_answer` say so.
- [x] `.guppi/tests/test_casecheck.py`: a test that 21 unread files that name `rule-x` give one note with the count and no note of a file, that 20 give a note for each file, and that a file which also holds a narrow name keeps its own note.
- [x] `uv run --project .guppi guppi test`: passes.
- [ ] read `estimate-case-check-sends-one-note-for-a-broad-name`
```

### Case 1010.3 — case-guppi answers the note of a name and writes one changed file per task line

> **given:**
> `rule-case-build`: the rule of `case-guppi`, whose Render sets how it answers the note of names.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-case-build-searches-the-names-of-what-it-changes`: its Criterion is replaced whole.
> **＋** `rule-case-check`: the rule of the hook that sends the notes.
> **＋** `vault/wiki/`: the pages a search for a name covers.
> **＋** `.guppi/guppi/`: the code a search for a name covers.
> **＋** `.guppi/tests/`: the tests a search for a name covers.
> **＋** `vault/wiki/case-schema.md`: the form of a command line, such as a render line.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, gets from the `SubagentStop` hook of `rule-case-check` a note on a file, or a note on a name, that names a page or a file its Case changes, and answers again.

> **then:**
> On a note of a file, it reads that file by a `Read` call of it, or by a `Grep` call whose `path` is it, whole or in parts as `rule-case-build` sets for its kind of text, or the `context` of the Case names the file and says why it stands.
> **＋** On a note of a name, it runs a `Grep` for the name with lines of context over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`, and the `context` of the Case names that search, its pattern, its paths and the count it printed, and says why each file it does not enter stands.
> **＋** Each file that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **＋** In its case file, a file of the repository outside `vault/wiki/` that a task changes has a task line of its own that opens with the path in a code span.
> **－** A task line that opens with a code span holding a command, such as `uv run --project .guppi guppi render` with the rendered file in its second span, keeps the form `vault/wiki/case-schema.md` sets for it.

```then
update:
- slug: rule-case-build
  replace:
  - old: and each file outside `vault/wiki/` whose path a task line writes in a code span, and it sends you a note once for each such file you have read by no `Read` call of it and no `Grep` call whose `path` is it, with its path, the name it holds and the purpose line of a page; so write in a code span of its task line the path of each file outside `vault/wiki/` that a task changes, and on each note read that file
    new: and each file outside `vault/wiki/` whose path the first code span of a task line writes; for a name that more than 20 of the files it searches hold it sends you one note with the name and the count of those files, and for each other name a note once for each such file you have read by no `Read` call of it and no `Grep` call whose `path` is it, with its path, the name it holds and the purpose line of a page; so give each file outside `vault/wiki/` that a task changes a task line of its own, its path in the first code span of the line, but for a line that opens with a code span holding a command, such as a render line, which keeps the form `vault/wiki/case-schema.md` sets for it and from which the hook takes no changed file; on a note of a name, Grep for the name with lines of context over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`, judge each hit by the lines the Grep prints, read by `Read` each file the change may make false, and name in `context` that search, its pattern, its paths and the count it printed, and why each file you do not enter stands; and on each note of a file read that file
  - old: says why it stands (as set in case 1005.2).
    new: says why it stands (as set in cases 1005.2 and 1010.3).
  change: case-guppi answers the note of a broad name by a search and writes each changed file in the first code span of a task line of its own
- slug: estimate-case-build-searches-the-names-of-what-it-changes
  set:
    status: pending
    purpose: Whether case-guppi, on each note of the hook of rule-case-check on a file, reads that file by Read or by a Grep whose path is it, or names it in context, on each note on a name runs a Grep for the name and names that search in context, enters each file the change makes false in the Case, and gives each file outside vault/wiki/ that a task changes a task line of its own with its path in the first code span, a line that opens with a command such as a render line kept in its own form
    method: 'by hand, after the /pre-spec of the first session in which the hook of rule-case-check sends case-guppi a note on a file or on a name that names what its Case changes, on the Render of rule-case-build that sets the note on a name: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each note on a file whether the agent read it by Read or by a Grep whose path is it, or named it in context, and for each note on a name whether it ran a Grep for the name and context names that search with its count; and its case file, whether each task line that changes a file outside vault/wiki/ holds its path in its first code span and changes no other such file, a line that opens with a code span holding a command, such as a render line, left out; the count and the transcripts in the estimate line'
  change: the Criterion replaced whole — the note of a name, and one changed file per task line
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-searches-the-names-of-what-it-changes`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-searches-the-names-of-what-it-changes`
```

## Deferred

## Case 1007 — The reading of /retro on a red command put off

> **context:**
> The person put off C5 of the Frontier of session 2035, as the brief of session 1548 proposed. `estimate-retro-loads-on-a-red-command` stands `pending` with target `rule-retro`. The render its `method` names has run: lines 7 and 9 of `.claude/skills/retro/SKILL.md` hold `guppi test --exit-zero` and `guppi style --exit-zero`. Its reading waits for the first load of `/retro` that a transcript can show. Session 1548 loaded `/retro` in the VS Code extension, which handed the `!` commands to the agent as instructions. Session 2035 also runs in the VS Code extension.

> **problem:**
> No Case of this session sets when or in which client the first load of `/retro` after that render is read.

```then
defer:
  - slug: estimate-retro-loads-on-a-red-command
    type: estimate
    purpose: "Whether /retro loads while guppi test or guppi style finds something, its lines Tests and Style running both commands with --exit-zero; waits for the first load of /retro in the Claude Code CLI; put off at /hi of session 2035"
```

## Case 1008 — The reading of /work on a red check put off

> **context:**
> The person put off C4 of the Frontier of session 2035, as the brief of session 1548 proposed. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` stands `pending` with target `rule-work-mode`, last read on 2026-10-31 in session 0431. Its `method` waits for the first load of `/work` while `uv run --project .guppi guppi check` exits 1, read in the transcript of its session. Session 1548 loaded `/work` in the VS Code extension, which handed the `!` commands to the agent as instructions. Session 2035 also runs in the VS Code extension, and `guppi check` exits 0 by the brief.

> **problem:**
> No Case of this session sets when or in which client the first load of `/work` on a red check is read.

```then
defer:
  - slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
    type: estimate
    purpose: "Whether /work loads while guppi check or guppi test finds something, writes the baseline before the first change and runs the tasks of the Spec in order; waits for the first load of /work in the Claude Code CLI while guppi check exits 1; put off at /hi of session 2035"
```

## Case 1009 — The reading of the synthesis on a marked lesson put off

> **context:**
> The person put off C3 of the Frontier of session 2035, as the brief of session 1548 proposed. `estimate-synthesis-keeps-actioned-by-the-mark` stands `pending` with target `rule-synthesis`, last read on 2026-09-27 in session 1819, where one of its branches ran and the not-later, born-Insight and unmarked branches did not. Its `method` waits for a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`; no run of the librarian since has done so, and in session 1548 no lesson entry carried `addressed_by`.

> **problem:**
> No Case of this session sets when the branches of the synthesis that the reading of session 1819 left out are read.

```then
defer:
  - slug: estimate-synthesis-keeps-actioned-by-the-mark
    type: estimate
    purpose: "An Insight stays or is born actioned by the mark of a lesson with addressed_by; waits for a librarian's run that puts such a lesson under an Insight that stands actioned; put off at /hi of session 2035"
```
