<!-- approved 18:00:26 · session 8727d5ce -->

# Session 0431 — the librarian's report.md missing after the run of session 0128

## Case 956 — A hook keeps the librarian's report in the session folder

> **context:**
> Since case 944 the close step of the librarian tells it to write its report by the `Write` tool into `report.md` in the session folder before its commit, so that the agent reads the report from the commit and checks `estimate-close-reports-the-run` by itself. The reading at the /hi of this session found no `report.md` in `vault/raw/2026-10-31/0128/` and none in the commit `c7e796eb`. The transcript of that librarian, `subagents/agent-afc9f2b665331e424.jsonl` of session 850a2e1e (Claude Code 2.1.312), shows why: the librarian called `Write` on `vault/raw/2026-10-31/0128/report.md`, and Claude Code itself refused the call with the error "Subagents should return findings as text, not write report files. Include this content in your final response instead." The librarian did not work around the refusal, named it in the report it returned, and committed without the file. No hook of GUPPI refused the call: the two `PreToolUse` hooks on `Write`, `guppi guard` (`.guppi/guppi/guard.py`, read whole) and `guppi ratified --guard` (`.guppi/guppi/ratified.py`, the functions `guard`, `guard_refusal`, `held_number` and `builder_write` read whole), write a line to the day's event log on each refusal, and `vault/raw/2026-10-31/event_log.md` holds no refusal line between the dispatch of the librarian at 04:10:47 and its handback at 04:19:01; `guard_refusal` judges only the plan file, its store and the files under `cases/`. The documentation of Claude Code does not describe this refusal: `https://code.claude.com/docs/en/sub-agents` (read whole), the six parts of `https://code.claude.com/docs/en/errors.md` and the first part of the changelog `https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md` hold no word of it, so what triggers it is not known. The person chose that a `SubagentStop` hook copies the report the librarian returns into `report.md`, and that `/handoff`, or `/box` in its sessions, shows the text of that file and commits it. A hook writes the file by its own code, so no `Write` call of a subagent is made. The hook gets the path of the subagent's transcript: the payload of `SubagentStop` carries `agent_transcript_path` and `agent_type`, as `lesson-hooks-subagentstop-fires-before-and-after-the-handback` records. `subagent_outputs` and `outputs` of `.guppi/guppi/casecheck.py` (read whole) read from that transcript each text block and the `message` of each `SubagentHandback` call, and the librarian of 0128 handed its report back by such a call. The same lesson records that `SubagentStop` may fire twice in one run, before and after the handback, so the hook writes the file again at each fire. `session_dir` of `.guppi/guppi/ledger.py` (read whole, with `session_event_logs` and `hi_moment` that it calls) gives the session folder from the `hi` line of the session; `session_stamp` of `.guppi/guppi/event.py` (read whole) gives the stamp from the payload. A Grep of `SubagentHandback|agent_transcript_path` over `.guppi/guppi/` printed only `.guppi/guppi/casecheck.py`, so the new module imports these functions and judges no output a second time, as `rule-one-judgment-one-implementation` sets it. The vault query of `.claude/agents/ask-guppi.md`, run on a hook that copies the librarian's report: exists none; near `rule-close`, the close step that the frame renders, with no hook; missing a hook that writes the report; rules `rule-hook-registry`, which requires the `update` of its registry in the Case that creates the hook's Rule, and `lesson-hooks-subagentstop-fires-before-and-after-the-handback`; tags `hooks`, `harness`, `librarian`; the slug `rule-librarian-report-copy` is free, since a Glob `vault/**/rule-librarian-report*.md` printed nothing. The new Rule has `core: true` and the parent `rule-documentation`, whose Render is the frame of the librarian; a child with no Render adds nothing to the file. The person also asked to find out what triggers the refusal, so a task of Case 956.2 probes it by hand in Work Mode. The return of a run that stops at step 1 of the frame is also copied by the hook, so the sentence of step 1 of `rule-documentation` that says such a run writes no `report.md` is reworded; case 944 set that sentence. The librarian's run of this session starts on the frame as it stands now and still calls `Write`, and `/handoff` of this session runs the skill as it stands, so the Estimates of this Case are read after a later run. That librarian renders `.claude/settings.json` before it ends, and Claude Code picks up a registration added to that file in the same session, as `lesson-hooks-stop-payload` and `lesson-plugin-install-hooks-of-the-copy-run-at-once` record, so the hook may write `report.md` for this run while the old skill makes no commit after the librarian; the person chose that a one-off task of Case 956.3, by hand after `/handoff` of this session, shows and commits that file when it stands. A Grep of `report\.md` over `.claude/`, `.guppi/` and `vault/wiki/` printed `.claude/agents/librarian-guppi.md`, `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-documentation.md`, `vault/wiki/estimates/estimate-close-reports-the-run.md` and `vault/wiki/rules/rule-close.md`: the agent file follows by the render, the brief and `log.md` are not read, and the rest enter the Case. A Grep of `librarian's report|its report unchanged|report to the person unchanged|show it to the person unchanged|No commit follows the handoff|Do not commit after this` over the `.md` files of `vault/wiki/` and `.claude/` printed 15 files. `rule-handoff`, `rule-spec-box`, their two skill files and their Estimates `estimate-handoff-dispatches` and `estimate-spec-box-runs-a-conserved-spec` enter the Case. `log.md`, the three lessons and the Insight are not read. `rule-where-to-stop` and `vault/wiki/where-to-stop.md` stand: they name the librarian's report as the end of the run, and the run still ends there. `estimate-where-to-stop-stops-only-on-its-conditions` and `estimate-orchestration-states-a-subagent-fact-from-its-transcript` also stand: they name the report as the end of a run, or as a past reading. The Criterion of `estimate-close-commits` says that `git log` shows one commit after the Retro commit, which the commit of `report.md` makes false in its wording, so Case 956.5 replaces it whole with that line reworded and the other lines carried word for word; its `purpose` and `method` speak of the librarian's commit alone and stand. `estimate-end-of-work-order` stands: it says that no other commit stands between the handoff and the librarian's commit, and the commit of `report.md` comes after the librarian's. The new Render of `rule-close` tells the librarian to write no text after its handback, since `SubagentStop` fires again after the handback and the hook copies the last output then, as `lesson-hooks-subagentstop-fires-before-and-after-the-handback` and `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback` record. `estimate-documentation-completes` stands: the hook, not the librarian, writes `report.md`, so the librarian still puts no file under `vault/` by a shell, and its line on a refusal is unchanged. `estimate-hook-registry-rendered` stands, since it promises only that the file equals the Render. A Grep of `handoff/SKILL\.md|librarian-guppi\.md|box/SKILL\.md|settings\.json` over `.guppi/tests/` printed `test_ratified.py`, `test_guppi_package.py`, `test_guard.py`, `test_render.py` and `test_ship.py`. Only `test_each_hook_command_stands_in_the_settings_in_the_new_form` of `test_guppi_package.py` reads the live `.claude/settings.json`: it asserts that the command of each hook of its list stands there, and a new registration leaves each one in place. The other files write their own copy under a temporary folder. The `## Purpose` of `rule-close` speaks of the commit only and stands. Case 960 of this session sets that a reading by hand names where its evidence is saved and reads a text shown in a chat in the transcript of its session; at its request the methods of 956.3 and 956.4 read the dispatch line and the text shown to the person in the transcript of the session under `~/.claude/projects/`.

> **problem:**
> Claude Code refuses the librarian's `Write` of `report.md`, so no run can leave its report in the session folder, and `estimate-close-reports-the-run` cannot pass.

> **recommend:**
> - **How the report reaches the disk**
>   - Recommended: no recommendation, since what triggers the refusal of Claude Code is not checked and options (a) to (d) rest on it; (e) rests on nothing unchecked but undoes the aim of case 944.
>   - Answer: (a), a script writes the file; the person added that what blocks the librarian should be understood, and pictured the librarian returning its report as text, a hook copying it, and the main agent sending the file instead of retyping the report.
> - **A check for a missing report**
>   - Recommended: (a) no new check.
>   - Answer: (a).
> - **What copies the text into the file**
>   - Recommended: (c) a hook copies the returned report, and the main agent shows and commits it.
>   - Answer: (c).
> - **What `/handoff` shows the person**
>   - Recommended: (a) the text of the file, and the returned text with one line that the file is missing when no file stands.
>   - Answer: (a).
> - **Finding out what triggers the refusal**
>   - Recommended: (a) a probe by hand in Work Mode, its result kept as a `knowledge` lesson.
>   - Answer: (a).
> - **What happens to the report of this session's own run**
>   - Recommended: (b) a one-off task commits it in this session.
>   - Answer: (b).
> - **Change**
>   - Asked: Case 960 of this session sets that a reading by hand names where its evidence is saved, and asked that the methods of `estimate-handoff-dispatches` and `estimate-spec-box-runs-a-conserved-spec` read the dispatch line and the text shown to the person in the transcript of the session under `~/.claude/projects/`, the estimate line naming that transcript.
>   - Taken: both methods now read the dispatch line and the text shown in the transcript of the session and name it in the estimate line; the method of `estimate-handoff-dispatches` names its event by its kind, with no "first". The method of 956.1, a command, already names where its evidence is saved and stands.
> - **Change**
>   - Asked: the findings of `ask-guppi` at `/pre-spec` on Case 956.
>   - Taken: the new Rule gets `core` as a boolean and its `ref` to `rule-documentation`; the commit of `report.md` is allowed in the − line of 956.3 and 956.4; the method of `estimate-close-reports-the-run` also reads the librarian's last output in its agent transcript; the new Render of `rule-close` tells the librarian to write no text after its handback; Case 956.5 replaces the Criterion of `estimate-close-commits`, whose wording the commit of `report.md` made false; `context` names `estimate-end-of-work-order` and why it stands.

### Case 956.2 — The librarian returns its report and writes no file

> **given:**
> `rule-close`: the close step of the librarian's frame.
> **＋** `rule-documentation`: the frame of the librarian, whose step 1 names `report.md`.
> **＋** `estimate-close-reports-the-run`: its Criterion is replaced whole.
> **＋** `.claude/agents/librarian-guppi.md`: the frame both pages render into.
> **＋** `rule-librarian-report-copy`: the hook that writes the file.
> **＋** `vault/raw/<date>/<hi HHMM>/report.md`: the file the hook writes.
> **＋** `/handoff` of `.claude/skills/handoff/SKILL.md` and `/box` of `.claude/skills/box/SKILL.md`: the skills that dispatch the run.

> **when:**
> The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches, or that `/box` of `.claude/skills/box/SKILL.md` dispatches in a session that `/box` runs, reaches the close of `.claude/agents/librarian-guppi.md` and ends, and the hook of `rule-librarian-report-copy` fires.

> **then:**
> `vault/raw/<date>/<hi HHMM>/report.md`, the folder of the `handoff.md` the dispatch names, holds the report that the librarian returned last.
> **＋** The file gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags the run raised and the lint total.
> **＋** The file gives each part that another step of `.claude/agents/librarian-guppi.md` sends to the report.
> **－** The file holds no test result and no list of files.
> **－** No limit of lines binds the file.

```then
update:
- slug: rule-close
  replace:
  - old: Write the report by the `Write` tool into `report.md` in the session's folder, the folder of the `handoff.md` your dispatch names (as set in case 944). The report gives
    new: The report gives
  - old: Then return the text of `report.md` unchanged as your report, and after it the refusal of any call that came after the file was written (as set in case 944).
    new: Then return the report as your last text, and give the same text when you hand your report back; write no text after the handback, since the hook copies your last output, a text after the handback included. The hook of `rule-librarian-report-copy` copies that text into `report.md` in the session's folder, the folder of the `handoff.md` your dispatch names, and `/handoff` or `/box` commits it; write no `report.md` yourself (as set in case 956).
  change: the librarian returns its report as text and writes no report.md; a hook copies the text into the file
- slug: rule-documentation
  replace:
  - old: If it exits 1, return the report as text, write no `report.md`, and stop (as set in case 944).
    new: If it exits 1, return the report as text and stop (as set in cases 944 and 956).
  change: step 1 no longer says that a stopped run writes no report.md, since the hook copies every returned report
- slug: estimate-close-reports-the-run
  set:
    status: pending
    purpose: Whether report.md of the session folder holds the report the librarian returned last at its close, and gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to the report, with no test result and no list of files
    method: 'by hand, after the librarian''s run of a session that starts with the hook of rule-librarian-report-copy in .claude/settings.json and whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close that returns the report as text: the agent reads report.md of the session folder of that run, as the commit of /handoff or /box holds it by git show, beside the last output of the librarian read in its agent transcript under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line'
  change: the Criterion replaced whole — the hook writes report.md from the report the librarian returns
```

```tasks
- [x] update `rule-close`
- [x] update `rule-documentation`
- [x] update `estimate-close-reports-the-run`
- [x] by hand in Work Mode: the main agent dispatches a `general-purpose` subagent that calls `Write` on three files in a new folder outside the repository: `report.md` with a text in the form of a report, `close.md` with the same text, and `report.md` in a second new folder with one plain line. The subagent returns what Claude Code answered to each call, and the main agent records the result as a `knowledge` lesson line with its `source`.
- [x] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-close-reports-the-run`
```

### Case 956.3 — `/handoff` shows the report file and commits it

> **given:**
> `rule-handoff`: the Rule of the skill `/handoff`.
> **＋** `.claude/skills/handoff/SKILL.md`: the skill it renders into.
> **＋** `estimate-handoff-dispatches`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/gate.py`: the gate that reads the tree.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian the skill dispatches.
> **＋** `vault/raw/<date>/event_log.md`: the day's event log.
> **＋** `vault/raw/<date>/<hi HHMM>/report.md`: the file the hook of `rule-librarian-report-copy` writes.
> **＋** `/box` and `raw/<date>/<hi HHMM>/work.md`: the skill that runs a conserved Spec, and the file that marks such a session.

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, the gate of `.guppi/guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

> **then:**
> The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
> **＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
> **＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the sections that `rule-handoff` names, with no Read call on the artifacts.
> **＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written.
> **＋** After the librarian's report, the agent shows the text of `vault/raw/<date>/<hi HHMM>/report.md` unchanged, or, when no `report.md` stands there, the returned report unchanged and one line that says that `report.md` is missing.
> **＋** When `report.md` stands, the agent commits it alone, in one commit after the librarian's, with the message `docs(vault): librarian report, <date>`, and never with `--amend`.
> **－** In a session whose `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec` — one that `/box` runs — the agent dispatches nothing after `handoff.md` and goes back to the step of `/box` that follows `/handoff`.
> **－** No commit follows the handoff but the librarian's and the commit of `report.md`, and no reply between the call and the librarian's report carries a `LEDGER` block.

```then
update:
- slug: rule-handoff
  replace:
  - old: Wait for its report and show it to the person unchanged. Do not commit after this, and write no `LEDGER` block.
    new: 'Wait for its report. Read `vault/raw/<date>/<hi HHMM>/report.md`, which a hook writes from that report, and show its text to the person unchanged; when no `report.md` stands there, show the returned report unchanged and one line that says that `report.md` is missing. When `report.md` stands, commit it alone, by the Bash tool: `git add vault/raw/<date>/<hi HHMM>/report.md && git commit -m "docs(vault): librarian report, <date>"`, never `--amend`. Make no other commit after this, and write no `LEDGER` block (as set in case 956).'
  change: /handoff shows report.md and commits it alone after the librarian's commit
- slug: estimate-handoff-dispatches
  set:
    status: pending
    purpose: /handoff stops on a dirty tree, writes handoff.md from memory into the session's folder, dispatches the librarian with its path, shows report.md and commits it alone after the librarian's commit, or, in a session that /box runs, hands back to /box
    method: 'by hand, after a /handoff whose .claude/skills/handoff/SKILL.md holds the Render of rule-handoff that commits report.md: the event log vault/raw/<date>/event_log.md, handoff.md and git log, and the dispatch line and the text shown to the person read in the transcript of that session under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line; by hand, after a /handoff in a session that /box runs: the event log, and the step of /box that follows read in the transcript of that session under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line'
  change: the Criterion replaced whole — /handoff shows report.md and commits it alone
```

```tasks
- [x] update `rule-handoff`
- [x] update `estimate-handoff-dispatches`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/handoff/SKILL.md`
- [x] by hand, once, after `/handoff` of this session shows the librarian's report: when `vault/raw/2026-10-31/0431/report.md` stands, the main agent shows its text to the person unchanged and commits it alone by the Bash tool, `git add vault/raw/2026-10-31/0431/report.md && git commit -m "docs(vault): librarian report, 2026-10-31"`, never `--amend`, since the skill of this session still says to make no commit after the librarian; when no such file stands, it says so in one line.
- [ ] read `estimate-handoff-dispatches`
```

### Case 956.4 — `/box` shows the report file and commits it

> **given:**
> `rule-spec-box`: the Rule of the skill `/box`.
> **＋** `.claude/skills/box/SKILL.md`: the skill it renders into.
> **＋** `estimate-spec-box-runs-a-conserved-spec`: its Criterion is replaced whole.
> **＋** `.claude/agents/librarian-guppi.md` and `vault/wiki/`: the librarian the skill dispatches, and the pages it writes.
> **＋** `vault/raw/<hi date>/<hi HHMM>/report.md`: the file the hook of `rule-librarian-report-copy` writes.
> **＋** `vault/raw/<date>/<HHMM>/` and `spec/<date>-<HHMM>`: the folder of the conserved Spec and its branch.
> **＋** `rule-spec-capture`: the hook whose line after `ExitPlanMode` calls `/box`.
> **＋** `/work`, `/retro` and `/handoff`: the skills that `/box` runs in one turn.

> **when:**
> The agent calls `/box` on `PreToolUse Skill` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, on the line that the hook of `rule-spec-capture` printed after `ExitPlanMode`, and runs `.claude/skills/box/SKILL.md` as rendered from `rule-spec-box`.

> **then:**
> `uv run --project .guppi guppi render --check` exits 0: `.claude/skills/box/SKILL.md` equals the Render of `rule-spec-box`.
> **＋** The agent first runs `uv run --project .guppi guppi box --check` on the folder; when it prints a line, the agent changes nothing, shows the lines and asks the person.
> **＋** Otherwise the agent commits the tree, runs `git switch` to `spec/<date>-<HHMM>`, and brings that branch up to the branch it came from by `git merge --ff-only`; when the merge refuses, it switches back, shows the refusal and asks the person.
> **＋** It calls `/work` with the folder, and Work Mode, the Work readings, `/retro` and `/handoff` run in one turn.
> **＋** After `handoff.md` stands, it switches back, brings the branch it came from up to `spec/<date>-<HHMM>` by `git merge --ff-only`, deletes `spec/<date>-<HHMM>` by `git branch -d` and runs `uv run --project .guppi guppi test`; a merge that refuses is a stop.
> **＋** Then it dispatches `librarian-guppi` with the path of the session's `handoff.md`, shows the text of `vault/raw/<hi date>/<hi HHMM>/report.md` unchanged, or, when no `report.md` stands there, the returned report unchanged and one line that says that `report.md` is missing, and then the exit code of `uv run --project .guppi guppi test`.
> **＋** When `report.md` stands, it commits it alone, in one commit after the librarian's, with the message `docs(vault): librarian report, <hi date>`, and never with `--amend`.
> **－** Nothing under `vault/wiki/` is written on `spec/<date>-<HHMM>`, and the librarian runs once, on the branch the session came from.
> **－** No commit follows the handoff but the librarian's and the commit of `report.md`.

```then
update:
- slug: rule-spec-box
  replace:
  - old: Wait for its report and show it to the person unchanged, then one line with the exit code of `uv run --project .guppi guppi test`. Do not commit after this, and write no `LEDGER` block.
    new: 'Wait for its report. Read `vault/raw/<hi date>/<hi HHMM>/report.md`, which a hook writes from that report, and show its text to the person unchanged, or, when no `report.md` stands there, the returned report unchanged and one line that says that `report.md` is missing; then one line with the exit code of `uv run --project .guppi guppi test`. When `report.md` stands, commit it alone: `git add vault/raw/<hi date>/<hi HHMM>/report.md && git commit -m "docs(vault): librarian report, <hi date>"`, never `--amend`. Make no other commit after this, and write no `LEDGER` block (as set in case 956).'
  change: /box shows report.md and commits it alone after the librarian's commit
- slug: estimate-spec-box-runs-a-conserved-spec
  set:
    status: pending
    purpose: Whether /box checks a conserved Spec, runs it on its own branch brought up to the shared branch by a fast-forward, merges the branch back by a fast-forward after the handoff, has the librarian write the pages on the shared branch, and shows report.md and commits it alone after the librarian's commit, stopping when the check or a merge refuses
    method: 'uv run --project .guppi guppi render --check; by hand, after a session that runs a conserved Spec by /box on the Render of rule-spec-box that commits report.md: git log, the branches, the folders of the session and of the conserved Spec, the librarian''s commit and the commit of report.md, and the dispatch line and the text shown to the person read in the transcript of that session under ~/.claude/projects/, recorded in the estimate line with that transcript named'
  change: the Criterion replaced whole — /box shows report.md and commits it alone
```

```tasks
- [x] update `rule-spec-box`
- [x] update `estimate-spec-box-runs-a-conserved-spec`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/box/SKILL.md`
- [ ] read `estimate-spec-box-runs-a-conserved-spec`
```

### Case 956.5 — The librarian's commit stays one commit, and the commit of the report may follow it

> **given:**
> `estimate-close-commits`: its Criterion is replaced whole.
> **＋** `rule-close`: the close step that commits.
> **＋** `.claude/agents/librarian-guppi.md`: the frame that holds the close command.
> **＋** `.guppi/guppi/render.py` and `vault/`: the render, whose `--paths` list the commit takes with the vault.
> **＋** `/handoff` and `/box`: the skills that commit `report.md` after the librarian's commit.
> **＋** `rule-plugin-install` and `plugin/skills/install/SKILL.md`: the file a project without that rule never commits.

> **when:**
> After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says, with the list that `uv run --project .guppi guppi render --paths` prints.

> **then:**
> `uv run --project .guppi guppi render --paths` prints each file that `guppi render` writes, one path per line, each line ended by a bare line feed with no carriage return, on Windows too, and writes nothing.
> **＋** The close command, as `.claude/agents/librarian-guppi.md` writes it, passes each path of that list to `git add` as the path stands, with no filter added to it.
> **＋** `git log` shows the librarian's commit as one commit after the Retro commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`; only the commit of `report.md` that `/handoff` or `/box` makes follows it.
> **＋** The commit takes `vault/` and each file of that list: `git add vault $(uv run --project .guppi guppi render --paths)`.
> **＋** After the commit, `git status` shows no file that `.guppi/guppi/render.py` wrote as modified or untracked.
> **－** The commit takes no path that neither `vault/` nor that list names.
> **－** In a project without `rule-plugin-install`, the list and the commit name no `plugin/skills/install/SKILL.md`.

```then
update:
- slug: estimate-close-commits
  set:
    status: pending
  change: the Criterion replaced whole — the commit of report.md by /handoff or /box may follow the librarian's commit
```

```tasks
- [x] update `estimate-close-commits`
- [ ] read `estimate-close-commits`
```

## Case 959 — The sprint as a kind gets an Estimate over all sprints

> **context:**
> `entity-sprint` is the MOC of the sprint as a kind: each sprint page `entity-sprint-<id>` is a Leaf under it, and it carries `core: true`, so it ships in the clean version. Its `estimates` is empty. The cascade of `guppi generate` (`cascade` of `.guppi/guppi/generate.py`, read whole) takes the live Estimates of each `draft` or `built` page and skips a page with none, so `entity-sprint` stays `draft` for good. `is_draft_core` of `.guppi/guppi/pages.py` (read whole, with `is_core`) accepts it, so `check_status` of `.guppi/guppi/lint.py` reports it and `guppi ship` writes no clean version while it stands; the brief of the librarian of session 0128 gives the last `guppi check`: "13 lines, exit 1, each a page with `core: true` that stands `draft`", `entity-sprint` among them. The page itself says that it carries no Estimate because the person named none, and that a measure over all sprints goes there when one is named (case 241). The person chose an Estimate on `entity-sprint` over keeping it out of the clean version, over a MOC with no Estimates following its children, and over not counting a draft page with no Estimates; `rule-entities-schema` governs the choice, since its schema says that `built` follows from every Estimate having passed and that the Estimates of a MOC measure what no child owns. The person chose that the Estimate promises at most one live sprint page and each other sprint page in the archive, read on the real vault. Today `vault/wiki/entities/` holds the one live sprint page `entity-sprint-plugin` and `vault/archive/` the one page `vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md`. The guard of one live page is `guppi sprint`: its docstring in `.guppi/guppi/sprint.py` says that two sprint pages give one line on stderr, exit 1 and no file written, and `test_two_sprint_pages_are_an_error_and_nothing_is_written` of `.guppi/tests/test_sprint.py` (read whole) asserts it. `estimate-sprint-checks-the-file` of `rule-sprint` already promises that refusal, by its line that two sprint pages are one line on stderr and exit 1, as with `guppi sprint`; so the Criterion of the new Estimate does not promise it again, and only its method runs that test before the reading, as the guard behind the count of live pages (finding 2.2 of `/pre-spec`). `check_method` of `.guppi/guppi/lint.py` (read whole, with `names_a_moc_form`, `names_test_files`, `missing_test_files`, `sibling_names_a_target` and `is_reading`) gives a MOC's Estimate whose method says `by hand` alone a finding while an Estimate of a child names a test file, and `estimate-sprint-plugin-ci-writes-a-clean-branch` of the child names `.guppi/tests/test_ship.py`; a method that names `pytest` with a test file that exists passes, so the method names `.guppi/tests/test_sprint.py`. The reading is taken at the Retro of this session, so the librarian's run of this session sets `entity-sprint` `built` once it passes. The Estimates of `rule-sprint` and `rule-sprint-close` test their code on a scratch vault, and no code changes here, so they stand. `entity-guppi`, its parent, has Estimates of its own, and the cascade reads no child of a page, so it is untouched. A Grep of `entity-sprint\.md|entities/entity-sprint[^-]|"entity-sprint"` over `.guppi/tests/` printed `.guppi/tests/test_sprint_close.py` and `.guppi/tests/test_sprint.py`; both write the page under a temporary folder, so no test reads the live page. A Glob `vault/**/estimate-sprint-keeps-one-live-page.md` printed nothing, so the slug is free. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> `entity-sprint` has `core: true` and no Estimate, so the cascade never sets it `built`, and `guppi ship` refuses for as long as it stands `draft`.

> **recommend:**
> - **How does `entity-sprint` become `built`?**
>   - Recommended: (a) an Estimate over all sprints, on something that holds across all sprints and that no single sprint page owns.
>   - Answer: agreed, (a).
> - **What does the Estimate of `entity-sprint` measure?**
>   - Recommended: (a) at most one live sprint page, and each other sprint page in the archive, read on the real vault at the Retro of this session.
>   - Answer: agreed, (a).

> **given:**
> `estimate-sprint-keeps-one-live-page`: the new check of the sprint as a kind.
> **＋** `entity-sprint`: the MOC of the sprint as a kind, whose Purpose names its Estimate.
> **＋** `vault/wiki/entities/` and `vault/archive/`: where the live and the archived sprint pages `entity-sprint-<id>` stand.
> **＋** `.guppi/tests/test_sprint.py`: the test of the guard of one live sprint page, which the method of the new check runs.
> **＋** `rule-entities-schema`: `built` follows from the Estimates, and a MOC's Estimates measure what no child owns.

> **when:**
> At the Retro of a session, the sprint pages `entity-sprint-<id>` under `vault/wiki/entities/` and under `vault/archive/` are read.

> **then:**
> At most one sprint page `entity-sprint-<id>` stands under `vault/wiki/entities/`.
> **＋** Each other sprint page `entity-sprint-<id>` stands under `vault/archive/`.
> **－** A vault with no live sprint page, between the close of one sprint and the opening of the next, does not fail this.

```then
create:
- slug: estimate-sprint-keeps-one-live-page
  ref: entity-sprint
  kind: QA
  purpose: Whether the vault holds at most one live sprint page and each other sprint page stands in the archive
  method: 'uv run --project .guppi pytest .guppi/tests/test_sprint.py -k two_sprint_pages; by hand, at Retro: a Glob of vault/wiki/entities/entity-sprint-*.md and of vault/archive/**/entities/entity-sprint-*.md read against the Criterion'
  tags:
  - sprint
  - workflow
update:
- slug: entity-sprint
  replace:
  - old: This page carries no Estimate yet — the person named none; a measure over all sprints, which no single sprint owns, goes here when one is named (case 241).
    new: 'Its Estimate is a measure over all sprints, which no single sprint owns: at most one sprint page is live, and each other one stands in the archive (as set in case 959).'
  change: the sprint as a kind gets its Estimate over all sprints
```

```tasks
- [x] create `estimate-sprint-keeps-one-live-page`
- [x] update `entity-sprint`
- [x] read `estimate-sprint-keeps-one-live-page`
```

## Case 960 — A reading by hand names where its evidence is saved

> **context:**
> Some Estimates are checked by a reading by hand that waits for an event, and then reads what an agent did in a chat. `estimate-where-to-stop-writes-each-step-whole` reads the reply of a stop of Work Mode that asks the person to run commands by hand. `estimate-case-build-reads-the-readers-of-a-changed-step` reads the findings of `ask-guppi` at a `/pre-spec`. Both events came in the session 2026-10-31/0128: its handoff names the by-hand test of Case 953 in Work Mode and eleven findings of `ask-guppi` at its `/pre-spec`. Both texts stood only in the chat of that session, and neither method names a place where they are saved. So `/hi` cannot take the readings, since it reads no transcript of an earlier session (case 670.5), and the Work lines stay open from session to session, as `lesson-brief-lists-transcript-readings-under-work` records. Claude Code saves every chat as a transcript under `~/.claude/projects/`; the transcript of the main session of 0128, `850a2e1e-ab70-422f-8401-df00a3a64d5e.jsonl`, stands there, as a Glob printed. Both methods also tie the reading to the first event of a kind. The description of the field `method` in `rule-estimates-schema` already says that any moment of the named kind counts, in this session or an earlier one, and that the word "first" fits only an event that has never happened. It says nothing about where the evidence of a reading must stand, and `case-schema.md`, which `case-guppi` reads when it writes a method, says nothing about it either. The person chose that a reading by hand names the place where its evidence is saved: a file of the repository, the output of a command, or a transcript. The rule goes into the field description of `rule-estimates-schema` and into one sentence of `case-schema.md`, with no lint check. The two methods name an event of a kind, not the first one, and read in the transcript of a session where it happened. Retro (`.claude/skills/retro/SKILL.md`, line 22) reads an Estimate whose `method` opens with `by hand, after` and names its event before a colon only when the event came in this session, and leaves it `pending` otherwise. The events came in 0128, so the two methods open with `by hand, at Retro` and name the event by its kind inside the reading, as the finding 1.7 of `ask-guppi` at the `/pre-spec` of this session asked. Case 961 of this session, read whole in its finished file, writes its methods whose event has already come in the same form, with the case or session it reads now in a bracket of its own at the end of the method, so the method reads whole without it; the two methods here take that bracket too. A new Estimate on `rule-estimates-schema` checks the rule, read at the Retro of this session over the methods of its Spec. In `lint.py` I read `tied_to_a_one_off_moment`, `waits_for_an_event`, `waits_for_another_session`, `waits_for_a_later_moment`, `check_moment` and `check_unread` whole: the new methods hold no "first", so the class `moment` gives no finding; they wait for no later moment, so `check_unread` gives each one the finding `unread: pending` until its reading of this Retro lands at the librarian's run of this session. `/work` (`.claude/skills/work/SKILL.md`, line 25) leaves the reading of an Estimate that this session updates to Retro. Retro (`.claude/skills/retro/SKILL.md`, line 22) reads such an Estimate on the Criterion of the Spec, but neither reads an Estimate whose `update` names one part of the page alone nor sets it `failed`. So Cases 960.2 and 960.3 set each Estimate `pending` and write its Criterion back word for word as their `when` and `then`. With a method that opens with `by hand, at Retro`, the Retro of this session reads both from the transcripts of 0128. A Grep of `transcript of an earlier session|read no transcript|only in the chat|shown only in the chat` over the `.md` files of `vault/wiki/` and `.claude/` printed `.claude/skills/hi/SKILL.md`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/estimates/estimate-hi-takes-its-readings.md` and `vault/wiki/lessons/lesson-brief-lists-transcript-readings-under-work.md`. The skill, its Rule and its Estimate stand: `/hi` still reads no transcript, and the readings that do are taken in Work Mode or at Retro. The lesson stands as a record. A Grep of `rule-case-protocol|rule-estimates-schema|estimate-where-to-stop-writes|estimate-case-build-reads-the-readers` over `.guppi/` printed `.guppi/tests/test_casecheck.py`, `.guppi/guppi/materialize.py`, `.guppi/tests/test_guard.py` and `.guppi/tests/test_glossary.py`. Each test writes its own copy under a temporary folder or a string, and `materialize.py` names the slug in a docstring. `.guppi/tests/test_schemas.py` reads the live `vault/wiki/estimates/schema.yaml`, but only its lists of fields, values and sections, which this Case leaves unchanged. `estimate-estimates-schema-checked` stands, since it checks those lists and that each name has a description. `estimate-case-protocol-loaded` and `estimate-case-protocol-case-form` stand, since one checks that the file equals the Render and the other checks the form of a Case, not what a `method` reads. The row of the Estimate fields in `glossary.md` stands. A Glob `vault/**/estimate-estimates-schema-method*.md` printed nothing, so the new slug is free. Case 956 of this session is a related Case. Its methods for `estimate-handoff-dispatches` (956.3) and `estimate-spec-box-runs-a-conserved-spec` (956.4) now read the dispatch line and the text shown to the person in the transcript of the session under `~/.claude/projects/`, the transcript named in the estimate line, as its case file holds them, so they keep the new rule and ask no change of Case 956. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> A reading by hand may point at a text that stood only in the chat of a session, so it cannot be taken once that chat ends. No rule says where the evidence of a reading must stand.

> **recommend:**
> - **Where the evidence of a reading may stand**
>   - Recommended: (a) a saved file, a transcript included: a file of the repository, the output of a command, or the transcript of the session under `~/.claude/projects/`.
>   - Answer: agreed, (a).
> - **Which texts carry the new rule**
>   - Recommended: (c) both texts, the field `method` of `rule-estimates-schema` and one sentence of `case-schema.md`, with no lint check.
>   - Answer: agreed, (c).
> - **How the two methods change**
>   - Recommended: (a) any event of the kind, read in its transcript, read in this session.
>   - Answer: agreed, (a).
> - **Which methods this Case fixes**
>   - Recommended: (a) the two Estimates, and a change asked of the Case of this session.
>   - Answer: agreed, (a).
> - **How the new rule is checked**
>   - Recommended: (a) a new Estimate on `rule-estimates-schema`.
>   - Answer: agreed, (a).

### Case 960.1 — A reading by hand names where its evidence is saved

> **given:**
> `rule-estimates-schema`: the field `method` of the schema of an Estimate, rendered into `vault/wiki/estimates/schema.yaml`.
> **＋** `rule-case-protocol`: the form of a Case, rendered into `vault/wiki/case-schema.md`, which `case-guppi` reads when it writes a method.
> **＋** `estimate-estimates-schema-method-names-its-evidence`: the new check of the rule.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose methods the check reads.
> **＋** `~/.claude/projects/`: the folder where Claude Code saves the transcripts of sessions and agents.

> **when:**
> At the Retro of a session, the `method` of each Estimate that a Case of its Spec `raw/<date>/<hi HHMM>/spec.md` creates or sets `pending` is read.

> **then:**
> Each reading by hand in such a method names the place where its evidence is saved: a file of the repository, the output of a command, or the transcript of a session under `~/.claude/projects/`.
> **＋** A reading whose evidence is a reply, a text shown to the person or the output of an agent reads it in the transcript of the session where it stood.
> **＋** A reading that waits for an event names the kind of the event, and the word "first" stands only for an event that has never happened.
> **－** No reading by hand names a text of a chat as its evidence with no file, command or transcript to read it in.
> **－** A reading that is the person's answer is no fault: the estimate line keeps that answer.

```then
create:
- slug: estimate-estimates-schema-method-names-its-evidence
  ref: rule-estimates-schema
  kind: QA
  purpose: Whether each reading by hand of a method that a Spec creates or sets pending names the file, command or transcript where its evidence is saved, reads a text of a chat in its transcript, and names an event by its kind
  method: 'by hand, at Retro: the method of each Estimate that a Case of the session''s spec.md creates or sets pending, read against the Criterion, each fault counted in the estimate line'
  tags:
  - schema
  - workflow
update:
- slug: rule-estimates-schema
  replace:
  - old: the word "first" stands only for an event that has never happened.
    new: 'the word "first" stands only for an event that has never happened. A reading by hand names the place where its evidence is saved: a file of the repository, the output of a command, or the transcript of a session under `~/.claude/projects/`; it reads a reply, a text shown to the person or the output of an agent in the transcript of the session where it stood, never in the chat alone, and the estimate line names that file; the person''s answer is kept by the estimate line itself (as set in case 960.1).'
  change: a reading by hand names the place where its evidence is saved, a transcript included
- slug: rule-case-protocol
  replace:
  - old: or under `Ask the person` when its `method` names the person's answer (case 781).
    new: or under `Ask the person` when its `method` names the person's answer (case 781). A reading by hand names the place where its evidence is saved — a file of the repository, the output of a command, or the transcript of a session under `~/.claude/projects/` — and reads a reply, a text shown to the person or the output of an agent in the transcript of the session where it stood, as `rule-estimates-schema` sets it for the field `method` (as set in case 960.1).
  change: a method names the place where the evidence of its reading by hand is saved
```

```tasks
- [x] update `rule-estimates-schema`
- [x] update `rule-case-protocol`
- [x] create `estimate-estimates-schema-method-names-its-evidence`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-estimates-schema-method-names-its-evidence`
```

### Case 960.2 — The reading of a stop that asks for commands reads its transcript

> **given:**
> `estimate-where-to-stop-writes-each-step-whole`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-where-to-stop`: the rule it checks.
> **＋** `vault/wiki/where-to-stop.md`: the Render of that rule, the text of a stop.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session where the stop came.

> **when:**
> Work Mode stops on a condition of `vault/wiki/where-to-stop.md`, and the reply asks the person to run commands by hand.

> **then:**
> Each step of the reply writes out whole each command it asks the person to run, as the person types it, with each variable, folder and flag the command needs.
> **＋** A step that starts a program in a new window or terminal writes the variables that the start needs in its own command.
> **－** No step names a part of its command by a reference to another step.

```then
update:
- slug: estimate-where-to-stop-writes-each-step-whole
  set:
    status: pending
    method: 'by hand, at Retro: the reply of a stop of Work Mode under the text of vault/wiki/where-to-stop.md that holds the sentence on each command written whole in each step, which asks the person to run commands by hand, read in the transcript of a session where such a stop came, under ~/.claude/projects/, against each line of the Criterion, the transcript named in the estimate line (the stop of the by-hand test of Case 953, in session 2026-10-31/0128)'
  change: the method reads the reply of any such stop in the transcript of its session, the Criterion written back unchanged
```

```tasks
- [x] update `estimate-where-to-stop-writes-each-step-whole`
- [x] read `estimate-where-to-stop-writes-each-step-whole`
```

### Case 960.3 — The reading of the findings at a pre-spec reads its transcript

> **given:**
> `estimate-case-build-reads-the-readers-of-a-changed-step`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-case-build`: the rule it checks, rendered into `.claude/agents/case-guppi.md`.
> **＋** `vault/wiki/rules/` and `.claude/`: the texts the agent searches for the readers of a step.
> **＋** `log.md` and `brief.md`: files whose hits are not read.
> **＋** `~/.claude/projects/`: the folder of the agent transcript of `ask-guppi` at the `/pre-spec`.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

> **then:**
> It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
> **＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
> **＋** Each step or skill that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
update:
- slug: estimate-case-build-reads-the-readers-of-a-changed-step
  set:
    status: pending
    method: 'by hand, at Retro: the findings of ask-guppi at a /pre-spec of a session whose case-guppi runs on the Render of rule-case-build that holds the sentence on the readers of a changed step, read in the agent transcript of that ask-guppi under ~/.claude/projects/, for a Case that changes a step and misses a step or skill that reads its output or does the same step, the count and the transcript in the estimate line (the /pre-spec of session 2026-10-31/0128)'
  change: the method reads the findings of any such /pre-spec in the agent transcript of ask-guppi, the Criterion written back unchanged
```

```tasks
- [x] update `estimate-case-build-reads-the-readers-of-a-changed-step`
- [x] read `estimate-case-build-reads-the-readers-of-a-changed-step`
```

## Case 961 — Estimates that wait for a rare event are read in this session

> **context:**
> Ten Estimates stay `pending` because each waits for an event that seldom comes. Their pages keep `draft`, and a page with `core: true` that stands `draft` blocks `guppi ship`. Today the reading of such an Estimate is taken only when the librarian sees the event and puts it on the Work list of a later session. Some of the events have already come, in this session or in an earlier one, and nothing reads them. Retro reads, on the Criterion of the Spec, an Estimate that a Case of the session sets `pending`. It leaves `pending` an Estimate whose `method` waits for an event that has not come in this session (`.claude/skills/retro/SKILL.md`, read whole). So each sub-case below sets its Estimate `pending`, writes its Criterion back word for word as its `when` and `then`, and rewrites its `method` as Case 960 of this session sets for a reading by hand: the method names the place where the evidence is saved, and names an event by its kind with no "first". A method whose event has already come opens with `by hand, at Retro`, so that Retro reads it in this session. Case 961.1 reads the showing of Cases 960 and 956: the main transcript of this session, line 777, holds the summary of Case 960 with a line `**Other Case:** Case 956`. Case 961.2 reads the dispatch of this Case, whose prompt names Case 960, which sets the form of the `method` of an Estimate, a text this Case writes. Case 961.3 reads the `/pre-spec` of this session, whose plan holds Case 956.1; that Case adds the hook `guppi libreport` to the `SubagentStop` hooks of `rule-hook-registry`, a list. Case 961.4 reads two earlier builds of a `create` with no `ref`. A Grep `\]\[create\]\[[a-z0-9-]+\](\{tags|$)` over `vault/**/ledger.md` printed, after the render of case 626.1 on 2026-10-04, `vault/archive/plugin/2026-10-12/2349/raw/ledger.md` (787.1, `rule-github-repository`) and `vault/archive/plugin/2026-10-13/1753/raw/ledger.md` (804.6, `rule-clean-branch`). Their case files stand in the archive, and agent transcripts under `~/.claude/projects/` hold those builds. Case 961.5 reads `estimate-ratification-ledger-line-form` from archived ledgers. A Grep `\{addresses:|addressed_by:case` over the ledgers of `vault/archive/plugin/` printed `2026-10-14/0232`, `2026-10-14/1536`, `2026-10-16/2104`, `2026-10-17/2307` and `2026-10-29/2341`. Its last Result read the take-up line of case 629.2 in the ledger of session 2026-10-04/1439. A Grep `\{newtag:` over `vault/**/ledger.md` printed no file, so the line on a new tag cannot be read yet. As the person chose, its method waits only for a lesson line that declares a new tag. Case 961.6 stages the event of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` on purpose. A task stops Work Mode, and a new Case replaces Case 961.6, its one change being the id of that new Case written into the bracket at the end of the method. The person ratifies it, and Retro reads the run. Each method names its event by its kind, and the case, decision or session it reads now stands in a bracket of its own at the end, as `rule-clean-branch` sets for the text of an Estimate, so the method reads whole without it; `/pre-spec` reported those pointers outside a bracket. Four Estimates keep waiting, as the person chose, since staging them would plant a record or cost a large build that yields no Case. `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` waits for a Case that changes a check and the text it reads. `estimate-case-build-goes-on-after-a-live-compaction` waits for a compaction: a Grep `"subtype":"compact_boundary"` over the subagent transcripts under `~/.claude/projects/c--PROJECTS-GUPPI/` printed no file. `estimate-orchestration-signs-items-taken-together` waits for one answer that takes up two items, and C7 is the last open item. `estimate-synthesis-keeps-actioned-by-the-mark` waits for a real `error` lesson under an `actioned` Insight. `rule-ratification` and `rule-work-mode` both have a line in `backlog.md`. `rule-ratification` carries `deferred_by: ["[[decision-case-907]]"]`. `rule-work-mode` carries no `deferred_by`: its line comes from the Backlog of the closed sprint page `entity-sprint-migration`, archived at `vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md`. This Case changes only one Estimate of each and no line of either page, so it takes up neither line. A Grep of the six slugs over `.guppi/` printed no file, so no test reads these pages. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`. The check of this file notes that a `－` line of 961.6 on a `/work` that `/box` calls shares most of its words with one of 961.1. Both stand, since each is a line of a live Criterion written back word for word: one bounds what `/work` does, the other what the main agent builds. Cases 960, 956 and 959 of this session are related. This Case writes methods under the rule of Case 960 and changes no page that Case 956 or 959 changes.

> **problem:**
> Ten Estimates wait for an event that seldom comes, and their pages stay `draft`. For several of them the event has already come, or can be staged, but no reading in this session is set to take it.

> **recommend:**
> - **How an Estimate is read in this session**
>   - Recommended: (a) one sub-case per Estimate read in this session: its `method` rewritten to name the event by its kind and the file or transcript that holds the evidence, the Estimate set `pending`, its Criterion kept word for word, so that Retro reads it.
>   - Answer: agreed, (a).
> - **Which Estimates are read from an event that already came**
>   - Recommended: (a) read all five in this session: `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-ask-query-before-a-create` and `estimate-ratification-ledger-line-form`.
>   - Answer: agreed, (a).
> - **Which events are staged on purpose in Work Mode**
>   - Recommended: (a) stage only the Work Mode trial: a task stops the run, a new Case replaces a sub-case of this Case with a small real change, and the person ratifies it; the other four Estimates keep waiting.
>   - Answer: agreed, (a).
> - **How the Estimate on the form of a ledger line is read**
>   - Recommended: (b) read the archived ledgers now, and wait only for a lesson line that declares a new tag, since no ledger holds one.
>   - Answer: agreed, (b).

### Case 961.1 — The showing of a built Case is read in this session

> **given:**
> `estimate-orchestration-shows-the-built-case`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-orchestration`: the rule it checks, rendered into `vault/wiki/orchestration.md`.
> **＋** `case-guppi` and `ask-guppi`: the agents the main agent dispatches, and `estimate-orchestration-starts-ask-guppi-for-a-hook-test`, which reads a start of `ask-guppi`.
> **＋** `/wait-what`, `.claude/skills/wait-what/SKILL.md` and `.claude/skills/grill-me/SKILL.md`: the explanation and the form of a round.
> **＋** `rule-case-check`, `rule-prespec-onward` and `rule-spec-box` with `/work` and `/box`: the checks and the runs that bound the showing.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/cases/case-<N>.md`, `raw/<date>/<hi HHMM>/ledger.md`, `raw/<date>/<hi HHMM>/handoff.md` and `uv run --project .guppi guppi caseid`: the files and the command of the session.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
> **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
> **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
> **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into the language of the chat line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in the language of the chat translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in the language of the chat, and a short text in the language of the chat on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands. In Plan Mode the main agent asks the person no question on it: it sends the other Case to its `case-guppi` by `SendMessage` with the change the line names, and the two Cases are shown together in a batch; in a send of Cases built at the same time it does so after the second pass that `vault/wiki/orchestration.md` sets. Where the `case-guppi` of the other Case answers with a round instead, the round stands in the list of the rounds of the batch, as any round does. In Work Mode it asks the person whether that other Case changes.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
> **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; outside the start of `ask-guppi` that `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads, it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
> **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
> **－** A start of `ask-guppi` in Work Mode that `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads is outside this promise.
> **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
> **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
> **－** The main agent writes the heading, the list, the `ratification` and the send of another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
> **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.

```then
update:
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
    method: 'by hand, at Retro: vault/wiki/orchestration.md read against the Criterion, and the replies of the main agent from a summary of case-guppi in Plan Mode that carries a line Other Case naming a Case of the session to the reply that shows the two Cases, read in the transcript of the session under ~/.claude/projects/ against the Criterion, both recorded in one estimate line with the transcript named (the summary of Case 960 that names Case 956, in session 2026-10-31/0431)'
  change: the method reads the showing of Cases 960 and 956 in the transcript of session 0431, the Criterion written back unchanged
```

```tasks
- [x] update `estimate-orchestration-shows-the-built-case`
- [x] read `estimate-orchestration-shows-the-built-case`
```

### Case 961.2 — The dispatch that names related Cases is read in this session

> **given:**
> `estimate-orchestration-names-related-cases-in-the-dispatch`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-orchestration`: the rule it checks, rendered into `vault/wiki/orchestration.md`.
> **＋** `case-guppi`: the agent the dispatch starts.
> **＋** `raw/<date>/<hi HHMM>/frontier.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the item and the case files the prompt names.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of an item of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** The prompt also names each Case of the session, ratified or already shown, that sets the form of a text a check reads, or how the check reads it, when the Case of the item may write text of that kind, such as the `method` of an Estimate.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** When the item is one of two or more items that one answer of the person took up, the prompt also names each other Case of that batch by its id and its Frontier item, and by the path of its case file where that file stands.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names, acts at another moment, sets no form of a text of a kind the Case of the item may write and is no Case of the same batch need not stand in the prompt.
> **－** A Case that only writes a text a check reads, and sets no form of it, is not related by that text alone.
> **－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

```then
update:
- slug: estimate-orchestration-names-related-cases-in-the-dispatch
  set:
    status: pending
    method: 'by hand, at Retro: an Agent call that dispatched case-guppi for the Case of an item while a Case of the session sets the form of the method of an Estimate and the Case of the item may write such a method, read in the transcript of the session under ~/.claude/projects/ against the Criterion, a related Case left unnamed counted in the reading line and the transcript named (the dispatch of Case 961, which names Case 960, in session 2026-10-31/0431)'
  change: the method reads the dispatch of Case 961 in the transcript of session 0431, the Criterion written back unchanged
```

```tasks
- [x] update `estimate-orchestration-names-related-cases-in-the-dispatch`
- [x] read `estimate-orchestration-names-related-cases-in-the-dispatch`
```

### Case 961.3 — The search for a new member of a list is read in this session

> **given:**
> `estimate-case-build-reads-each-list-of-a-new-member`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-case-build`: the rule it checks, rendered into `.claude/agents/case-guppi.md`.
> **＋** `vault/wiki/`, `.claude/` and `.guppi/guppi/`: the texts the agent searches for a member of the list, and `decisions/`, the folder of `vault/wiki/` it leaves out.
> **＋** `log.md` and `brief.md`: files whose hits are not read.
> **＋** `~/.claude/projects/`: the folder of the agent transcripts of `case-guppi` and `ask-guppi`.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that adds a member to a list that texts spell out one by one — a key of an item, a kind, a status or a field — and is about to answer with its summary.

> **then:**
> It searches the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already.
> **＋** It reads each hit that lists the members of the list.
> **＋** Each text that lists the members and would miss the new member enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
update:
- slug: estimate-case-build-reads-each-list-of-a-new-member
  set:
    status: pending
    method: 'by hand, at Retro: .claude/agents/case-guppi.md read against the Criterion; the agent transcript of a case-guppi that built a Case that adds a hook to the SubagentStop hooks of rule-hook-registry, read for its search of a hook that stands in the list already; and the findings of ask-guppi at the /pre-spec of that session, read in its agent transcript, for a Case that adds a member to a list and misses a text that lists the members; all under ~/.claude/projects/, recorded in one estimate line with the count and the transcripts (the build of Case 956.1, which adds the hook guppi libreport, and the /pre-spec of session 2026-10-31/0431)'
  change: the method reads the build of Case 956 and the /pre-spec of session 0431 in their transcripts, the Criterion written back unchanged
```

```tasks
- [x] update `estimate-case-build-reads-each-list-of-a-new-member`
- [x] read `estimate-case-build-reads-each-list-of-a-new-member`
```

### Case 961.4 — The vault query before a create is read from two earlier builds

> **given:**
> `estimate-ask-query-before-a-create`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-ask`: the rule it checks, rendered into `.claude/agents/ask-guppi.md`.
> **＋** `.claude/agents/case-guppi.md`: the agent that runs the query.
> **＋** `vault/wiki/rules/` and `vault/archive/`: the folders the query searches.
> **＋** `vault/archive/plugin/2026-10-12/2349/raw/cases/case-787.md` and `vault/archive/plugin/2026-10-13/1753/raw/cases/case-804.md`: the case files of the two builds.
> **＋** `~/.claude/projects/`: the folder of their agent transcripts.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> It starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** A page that already holds the thing is found by meaning, whether the person's words name it in the language of the chat or in the language of the repository, and the `context` of the Case names its slug.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
> **＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
> **＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
> **－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.

```then
update:
- slug: estimate-ask-query-before-a-create
  set:
    status: pending
    method: 'by hand, at Retro: the agent transcripts under ~/.claude/projects/ of the two builds of case-guppi that create rule-github-repository and rule-clean-branch with no ref, their Grep and Glob calls read against the Criterion, and the context of vault/archive/plugin/2026-10-12/2349/raw/cases/case-787.md and vault/archive/plugin/2026-10-13/1753/raw/cases/case-804.md read with them, recorded in one estimate line with the transcripts named (Cases 787.1 and 804.6, of the sessions 2026-10-12/2349 and 2026-10-13/1753)'
  change: the method reads the builds of Cases 787 and 804 in their transcripts and case files, the Criterion written back unchanged
```

```tasks
- [x] update `estimate-ask-query-before-a-create`
- [x] read `estimate-ask-query-before-a-create`
```

### Case 961.5 — The form of a ledger line waits only for a new tag

> **given:**
> `estimate-ratification-ledger-line-form`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-ratification`: the rule it checks, rendered into `vault/wiki/ratification.md`.
> **＋** `vault/wiki/tags.md`: the tags a lesson line may carry.
> **＋** The ledgers of `vault/archive/plugin/` and `vault/archive/migration/2026-10-04/1439/raw/ledger.md`: the lines read now.
> **＋** `~/.claude/projects/`: the folder of the transcripts that hold the previews.

> **when:**
> The agent writes the ledger lines of a session — the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists — with `vault/wiki/ratification.md` rendered from `rule-ratification`.

> **then:**
> A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
> **＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
> **＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
> **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
> **＋** For a Case with sub-cases, the `N` of `{addressed_by:case N}` is the sub-case whose decision line closes the cause, never the parent, which has no decision line.
> **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
> **＋** A lesson line whose tag `vault/wiki/tags.md` does not hold carries one `{newtag:<tag>|<meaning>|<aliases>}` block per such tag before `trigger:`, the tag also in its `{tags:...}`, the meaning one line and the aliases the words of the chat language for it.
> **－** A lesson whose fix is ratified in another session gets no mark.

```then
update:
- slug: estimate-ratification-ledger-line-form
  set:
    status: pending
    method: 'by hand, after a lesson line that declares a new tag by a newtag block: that line read in the ledger of its session and its LEDGER block in the transcript of that session under ~/.claude/projects/; with it, the decision and lesson lines that carry an addresses or addressed_by mark in vault/archive/plugin/2026-10-14/0232/raw/ledger.md, vault/archive/plugin/2026-10-14/1536/raw/ledger.md, vault/archive/plugin/2026-10-16/2104/raw/ledger.md, vault/archive/plugin/2026-10-17/2307/raw/ledger.md and vault/archive/plugin/2026-10-29/2341/raw/ledger.md, and the line in vault/archive/migration/2026-10-04/1439/raw/ledger.md that takes up a page with two Cases in its deferred_by, each with its preview in the transcript of its session, read against the Criterion, all recorded in one estimate line (the take-up line is that of case 629.2)'
  change: the method reads the marks and the take-up line in archived ledgers and waits only for a lesson line that declares a new tag, the Criterion written back unchanged
```

```tasks
- [x] update `estimate-ratification-ledger-line-form`
- [ ] read `estimate-ratification-ledger-line-form`
```

## Case 962 — The open work of Work Mode and of the Spec box stays in the backlog list

> **context:**
> `guppi backlog` writes `vault/wiki/backlog.md`, and it lists each line of the `## Backlog` of each sprint page, the closed ones under `vault/archive/` too. A line of a closed sprint that names a page leaves the list once that page stands `built`, `passed` or `archived` (`deferred` and `finished` of `.guppi/guppi/backlog.py`, read whole, with `item_slugs`, `item_statuses` and `is_done` of `.guppi/guppi/sprint.py`; case 743.4). While it stands, such a line shows only the page's `purpose`, not its own text. The Backlog of the closed sprint `migration` (`vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md`) names on its `rule-work-mode` line the work still open: the test of each Estimate written first and turned green, and the full model the person plans (cases 183, 206, 479.2). Case 961.6 of this session may set `rule-work-mode` `built`, and that line would then leave the list. The same rule already took the `rule-spec-box` line out of the list: `rule-spec-box` stands `built`, and its Purpose says that two cases wait for a second part, a line of that same Backlog. A line that names no page is a note: `item_slugs` reads a page only as a `[[slug]]` before the first ` — `. `deferred` keeps a note of the live sprint always, and a note of a closed sprint until the live sprint holds the same text, whatever the status of any page. `test_a_line_of_a_closed_sprint_leaves_once_taken_or_finished` and `test_the_backlog_of_an_archived_sprint_page_stays_beside_the_live_one` of `.guppi/tests/test_backlog.py` (read at lines 209–276) check this on a made-up vault under `estimate-backlog-renders`. The person chose to keep both pieces of work in sight as note lines on the live sprint page `entity-sprint-plugin`, which already holds such a note for the work taken out of `rule-morph` (case 802). No code changes. The sentence of the Purpose of `rule-work-mode` that says the test of each Estimate written first and the rest of the model are not decided yet stays true. So does the sentence of `rule-spec-box` that points to a line of the Backlog of `entity-sprint-migration`: that line still stands in the archive. A Grep of ``Backlog of `?entity-sprint-migration|second part|written first`` over `vault/wiki/` (with `log.md` and `brief.md` left out) printed `rule-search-leaves-out-decisions.md`, `rule-spec-box.md` and `rule-work-mode.md`. Over `.claude/` it printed `.claude/rules/search-leaves-out-decisions.md`. The hits in the search rules are about an exclusion written first, and they stand. None of the Estimates of `entity-sprint-plugin` checks its Backlog. `estimate-backlog-renders` checks only the mechanism. So the new Estimate on `rule-backlog` reads the live list. As the person said, it is a one-time check of this data, not a promise of lasting behaviour. Whether a one-time Estimate should be told apart from one that promises a behaviour is item C9 of the Frontier, which the main agent takes up after this Case. `rule-backlog` has `core: true` and stands `built`. With a `pending` Estimate it goes back to `draft` at the librarian's run of this session. `guppi check` then gives one more line until a later session reads the Estimate from its Work list. The last brief reports 13 such lines. The method waits for the librarian's run and names the file where its evidence stands, as Case 960 of this session sets it for a method. A Glob `vault/**/estimate-backlog-keeps-*.md` printed nothing, so the slug is free. A Grep of `entity-sprint-plugin|rule-spec-box|rule-work-mode|backlog\.md` over `.guppi/tests/` printed `test_box.py`, `test_backlog.py`, `test_glossary.py`, `test_prespec.py`, `test_ship.py`, `test_sprint.py` and `test_lint.py`. Each one writes its own vault under a temporary folder or names the slug in a string or a docstring, so no test reads the live pages or the live list. Cases 961, 960 and 959 of this session are related: this Case changes no page that they change. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> A line of a closed sprint's Backlog that names a page leaves the backlog list once that page is `built`, even when it names work beyond the page. The open work of Work Mode would drop out of sight that way, and the second part of the Spec box already has.

> **recommend:**
> - **What happens to the open work of Work Mode?**
>   - Recommended: (a) a note line in the Backlog of the live sprint `entity-sprint-plugin`, in its own words, taken out of `rule-work-mode`.
>   - Answer: agreed, (a).
> - **What happens to the second part of the Spec box?**
>   - Recommended: (a) bring it back the same way as the work of Work Mode, as a note line on the live sprint page.
>   - Answer: agreed, (a).
> - **How is it checked that the list keeps the open work?**
>   - Recommended: (a) a new Estimate on `rule-backlog`, read by hand on the live list after the librarian's run.
>   - Answer: agreed, (a). The person noted that it is a one-time check and asked to discuss telling one-time Estimates apart from those that promise a behaviour; that is a separate Frontier item.

> **given:**
> `entity-sprint-plugin`: the live sprint page, whose `## Backlog` takes the notes.
> **＋** `rule-work-mode` and `rule-spec-box`: the pages the work is taken out of; their text stands.
> **＋** `vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md`: the closed sprint page whose Backlog named the work.
> **＋** `rule-backlog`: the rule that keeps a deferred item in sight, the target of the new Estimate.
> **＋** `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`: the new one-time check.
> **＋** `.guppi/guppi/backlog.py` and `vault/wiki/backlog.md`: the script and the list it writes.

> **when:**
> The librarian runs `uv run --project .guppi guppi backlog` over `vault/wiki/` and `vault/archive/`, after the `## Backlog` of `entity-sprint-plugin` holds the notes taken out of `rule-work-mode` and `rule-spec-box`.

> **then:**
> `vault/wiki/backlog.md` holds under `## Deferred` a line with the text of the note on the rest of Work Mode: the test of each Estimate written first and turned green, and the full model the person plans.
> **＋** It holds a line with the text of the note on the second part of the Spec box.
> **＋** Each of these lines stands whatever the status of `rule-work-mode` and of `rule-spec-box`, `built` included.
> **－** The line of `vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md` that names `rule-work-mode` does not keep the work in the list: it may leave once that page stands `built`.

```then
create:
- slug: estimate-backlog-keeps-the-work-taken-out-of-a-built-page
  ref: rule-backlog
  kind: QA
  purpose: Whether backlog.md shows the open work of Work Mode and the second part of the Spec box, kept as notes of the live sprint page, whatever the status of rule-work-mode and rule-spec-box; a one-time check of this data
  method: 'by hand, after the librarian''s run of a session in which the Backlog of entity-sprint-plugin holds the notes taken out of rule-work-mode and rule-spec-box: vault/wiki/backlog.md, the file of the repository where the evidence is saved, read against the Criterion in the session whose brief puts the reading under Work, the file named and its lines quoted in the estimate line'
  tags:
  - sprint
  - workflow
update:
- slug: entity-sprint-plugin
  replace:
  - old: the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md
    new: |-
      the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md
      - The rest of Work Mode past the skill /work: the test of each Estimate written first and turned green, and the full model the person plans; taken out of rule-work-mode (case 962)
      - The Spec box, its second part: a conserved Spec checked against the pages changed after it was conserved, a Case on such a page built again, ratified again and written into the folder of the conserved Spec, and a conserved Spec taken after other Cases of its session; taken out of rule-spec-box (case 962)
  change: the Backlog takes the open work of rule-work-mode and rule-spec-box as notes
```

```tasks
- [x] update `entity-sprint-plugin`
- [x] create `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`
- [x] `uv run --project .guppi guppi sprint`
- [x] read `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`
```

## Case 964 — The Case ratified in Work Mode names itself in the method

> **context:**
> This Case replaces Case 961.6 whole, in the Work Mode of this session (`vault/raw/2026-10-31/0431/cases/case-961.md`, read whole). Case 961.6 stages on purpose the event that `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` waits for: a Case ratified in Work Mode that replaces a sub-case of a ratified Case. Its `stop:` task asks for this Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, with one change. The bracket at the end of the `method` named the Case only as the Case that replaces Case 961.6. Here it names Case 964 by its id. Everything else of Case 961.6 stands word for word: its `given`, `when` and `then`, the `then` block but for that bracket, and its tasks. The `when` and `then` are the Criterion of the page, written back unchanged. The `method` keeps the form that Case 960 of this session sets: it names the place of the evidence and the event by its kind, and the pointer stands in a bracket of its own at its end, as `rule-clean-branch` sets for the text of an Estimate. The `stop:` task stays in the Case, since this Case holds Case 961.6 whole. Its work stands once the person ratifies this Case, so the main agent ticks it and does not run it again, as `.claude/skills/work/SKILL.md` sets it for a task done under the sub-case a Case replaces (read whole). The `update` and `read` lines stay open. The `update` of the page lands at the librarian's run, and the page still holds its old `method` (`vault/wiki/estimates/estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline.md`, read whole). A Grep of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` over `.guppi/` printed no file, so no test reads the page. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`. Case 965 is built at the same time and replaces Case 956.1 for another defect; this Case changes no page it changes and rests on nothing of it, and its file was not read.

> **problem:**
> The staged trial of Case 961 needs its Case ratified in Work Mode, and the `method` must name that Case by its id so that Retro reads the right run.

> **recommend:**
> - Recommended: replace Case 961.6 whole, with Case 964 named in the bracket at the end of the `method`.
> - Answer: ratified as built

> **given:**
> `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-work-mode`: the rule it checks, rendered into `.claude/skills/work/SKILL.md`, with `/work` and `/box`, and `vault/raw/<date>/<HHMM>/`, the folder of a conserved Spec.
> **＋** `raw/<date>/<hi HHMM>/work.md`, `raw/<date>/<hi HHMM>/spec.md` and `raw/<date>/<hi HHMM>/handoff.md`: the files of the run.
> **＋** `vault/wiki/where-to-stop.md`, `rule-prespec-onward`, `rule-spec-box` and `/retro`: the stops and the steps around the run.
> **＋** `uv run --project .guppi guppi render`, `uv run --project .guppi guppi test`, `uv run --project .guppi guppi check`, `uv run --project .guppi guppi prespec --check` and `git branch --show-current`: the commands of the run.
> **＋** `case-guppi`: the agent that builds the Case ratified in Work Mode.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run --project .guppi guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
> **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.
> **＋** Or, while the run of `/work` goes on, the person ratifies a Case built in Work Mode.

> **then:**
> `uv run --project .guppi guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `uv run --project .guppi guppi test` and `uv run --project .guppi guppi check` before the first change — and uses that result.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `uv run --project .guppi guppi test` and of `uv run --project .guppi guppi check` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
> **＋** The reply that acknowledges a Case ratified in Work Mode ends the turn, since the hook of `rule-prespec-onward` sends nothing on once `raw/<date>/<hi HHMM>/spec.md` stands; at the person's next message the run goes on from where it stopped.
> **＋** After the reply that acknowledges a Case ratified in Work Mode, and before the first task of that Case, the agent runs `uv run --project .guppi guppi prespec --check` on the plan file of the session, with the session id of its `hi:` line.
> **＋** When that check prints a line that does not open with `note:`, the agent stops as the first condition of `vault/wiki/where-to-stop.md` sets it and sends the finding to the `case-guppi` of that Case; the run goes on after the person ratifies the fixed Case and the check prints no such line.
> **＋** A task of that Case whose work already stands, done under the sub-case the Case replaces, is ticked in `raw/<date>/<hi HHMM>/spec.md` and not run again.
> **＋** A task that changes `uv run --project .guppi guppi check`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **＋** When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `uv run --project .guppi guppi test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
> **＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
> **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.
> **－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
> **－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.
> **－** In a `/work` that `/box` calls no Case is ratified, so the check of the plan does not run there: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.

```then
update:
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    status: pending
    method: 'by hand, at Retro: uv run --project .guppi guppi render --check; .claude/skills/work/SKILL.md read against each line of the Criterion; a Case ratified in the Work Mode of the session that replaces a sub-case of a ratified Case, the end of the turn after its acknowledging reply, the check of the plan before its first task, what followed a finding and the ticks of its tasks read in the transcript of the session under ~/.claude/projects/ and in its spec.md and work.md against the Criterion, recorded in the estimate line with the transcript named (Case 964, ratified in Work Mode, which replaces Case 961.6, staged in session 2026-10-31/0431)'
  change: the method reads Case 964, ratified in the Work Mode of session 0431 and staged on purpose, the Criterion written back unchanged
```

```tasks
- [x] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [x] stop: in Work Mode, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, which replaces Case 961.6 whole with one change: the bracket at the end of the `method` names the id of that new Case as the Case ratified in Work Mode; the person ratifies it, and the run goes on as `.claude/skills/work/SKILL.md` sets it.
- [x] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
```

## Case 965 — The hook copies the librarian's report into the session folder, and its Rule is born core

> **context:**
> This Case replaces sub-case 956.1 whole, found wrong in Work Mode by the first condition of `rule-where-to-stop`: a ratified Case turns out wrong. Case 956 and the findings of `/pre-spec` on it set that `rule-librarian-report-copy` has `core: true` as a boolean, since `rule-rules-schema` allows only `core: [true]`. The file of Case 956 wrote `core` as a fenced value under the `create`, and the hook of `rule-spec-write` lifted it into the `then` block of `vault/raw/2026-10-31/0431/spec.md` as the string `'true'`. The fault lies in that lift. `put` of `.guppi/guppi/ratified.py` (read whole, with `read_tasks`, `code_value` and `fenced_value`, which hand it each sub-point) parses a value as YAML only under `set`, or when the value opens with `[` or `{`; every other value, a code span or a fenced block alike, stays a string. So no sub-point of a `create` in the chat form lifts a bare boolean, and `case-schema.md` names no such form. `create_fields` and `_lift_item` of `.guppi/guppi/materialize.py` carry the string as it stands, the `create` of `.guppi/guppi/generate.py` puts it into the props, and `frontmatter` and `scalar` write a string `true` quoted, as `"true"`; so the page would be born without `core: true`. `core_as_left` of `.guppi/guppi/prespec.py` answers False for a `create` whose `core` is not `True`, which is why `guppi prespec --check` printed no finding on it. Whether the hook of `rule-spec-write` lifts `true` and `false` as booleans is not this Case; the main agent records it as a lesson. This Case writes the same Rule, Estimate and registration as 956.1, with one change: the `create` of `rule-librarian-report-copy` carries no `core`, and an `update` of that Rule right after it carries `set: {core: true}`, which `put` parses as YAML, so the `then` block holds `core: true` as a boolean. `apply` of `generate.py` applies the entries in the order of the ledger lines, so the `create` writes the page and the `update` finds it and sets the field by `update`, which puts each key of `set` into the props as it stands; `core_as_left` answers True on that `set`. The `update` names a field alone, so it carries no `status` and touches no Estimate. The `then`, the Estimate and its Criterion are those of 956.1, unchanged; `estimate-librarian-report-copy-writes-the-file` checks the hook, and no Estimate checks the field `core`, as in 956.1. The code of `.guppi/guppi/libreport.py`, `.guppi/guppi/cli.py` and `.guppi/tests/test_libreport.py` was written in this Work Mode under 956.1; the main agent ticks those tasks with no new run. The `## Render` of `rule-hook-registry`, read whole around the pair, is the `"hooks"` key of `.claude/settings.json`, from `"SessionStart"` to the closing marker, with the `"PostToolUse"`, `"Stop"` and `"SubagentStop"` entries last; the `old` of the pair hits that page once, on the one line of the `"SubagentStop"` entry, whose `hooks` list holds only `guppi casecheck --subagent`, and ends at the `] }` that closes that list and that entry. The `new` keeps that command and its timeout, adds `guppi libreport` with a timeout of 30 as the second hook of the same list, and closes the list and the entry as before, so the `"SubagentStop"` key holds one entry with two hooks and the `]` after it still closes the key. No other entry of the Render changes. Of the Cases of this session, only Case 956, in its sub-case 956.1, wrote into this page, by the same pair; Case 965 replaces 956.1, so no other pair of the session meets this one. The rest of the frame, the vault query and the searches are those of the `context` of Case 956, which stands in its file.

> **problem:**
> The `then` block of 956.1 creates `rule-librarian-report-copy` with `core` as the string `true`, so the page would be born without `core: true`.

> **recommend:**
> - Recommended: the Rule, the Estimate and the registration of 956.1 as they stood, with `core: true` set by an `update` of the new Rule right after its `create`, so that the `then` block holds a boolean.
> - Answer: ratified as built

> **given:**
> `rule-librarian-report-copy`: the new Rule of the hook.
> **＋** `estimate-librarian-report-copy-writes-the-file`: the new check of the hook.
> **＋** `rule-hook-registry`: the registry of hooks in `.claude/settings.json`, which gains the hook.
> **＋** `.guppi/guppi/libreport.py`: the new module of the hook.
> **＋** `.guppi/guppi/cli.py`: the command table, which gains `libreport`.
> **＋** `.guppi/tests/test_libreport.py`: the new test of the hook.
> **＋** `.guppi/guppi/casecheck.py` and `.guppi/guppi/ledger.py`: the reading of the outputs and of the session folder that the module imports.
> **＋** `vault/raw/<hi date>/<hi HHMM>/`: the session folder where the hook writes `report.md`.

> **when:**
> `SubagentStop` fires at the end of an agent, and `uv run --project .guppi guppi libreport` of `.guppi/guppi/libreport.py` reads its payload.

> **then:**
> For `librarian-guppi`, the hook writes the last output of the agent in its `agent_transcript_path`, a text or the `message` of a `SubagentHandback` call, whole into `report.md` in the session folder `vault/raw/<hi date>/<hi HHMM>/`, and replaces a file that stands there.
> **＋** A second `SubagentStop` of the same run writes the file again from the last output at that moment.
> **＋** The hook reads the outputs by `subagent_outputs` of `.guppi/guppi/casecheck.py` and the folder by `session_dir` of `.guppi/guppi/ledger.py`.
> **－** For any other agent, the hook writes nothing.
> **－** The hook blocks nothing and exits 0; with no readable transcript, no output or no session folder it writes nothing and prints one line on stderr.

```then
create:
- slug: rule-librarian-report-copy
  ref: rule-documentation
  type: rule
  kind: Leaf
  purpose: Prevents the librarian's report from standing in no file when Claude Code refuses the Write of a report file by a subagent
  enforcement: hook
  implementation_ref:
  - .guppi/guppi/libreport.py
  - .guppi/tests/test_libreport.py
  - .claude/settings.json
  tags:
  - hooks
  - harness
  - librarian
  sections:
    Purpose: Prevents the librarian's report from standing in no file when Claude Code refuses the `Write` of a report file by a subagent. Claude Code refused the librarian's `Write` of `report.md` with the message that subagents return findings as text and write no report files (as set in case 956). The `SubagentStop` hook `uv run --project .guppi guppi libreport` copies the last output that `librarian-guppi` returned into `report.md` in the session folder by its own code, so no `Write` call of a subagent is made, and `/handoff` or `/box` shows that file and commits it (as set in case 956).
- slug: estimate-librarian-report-copy-writes-the-file
  ref: rule-librarian-report-copy
  kind: QA
  purpose: Whether the SubagentStop hook writes the last output of librarian-guppi, a text or a handback message, into report.md of the session folder, writes it again at a second fire, and writes nothing for another agent or with no transcript, output or folder
  method: uv run --project .guppi guppi test, which runs .guppi/tests/test_libreport.py
  tags:
  - hooks
  - harness
  - librarian
update:
- slug: rule-librarian-report-copy
  set:
    core: true
  change: core set as a boolean
- slug: rule-hook-registry
  replace:
  - old: '"command": "uv run --project .guppi guppi casecheck --subagent", "timeout": 30 } ] }'
    new: '"command": "uv run --project .guppi guppi casecheck --subagent", "timeout": 30 }, { "type": "command", "command": "uv run --project .guppi guppi libreport", "timeout": 30 } ] }'
  change: the SubagentStop hook guppi libreport registered
```

```tasks
- [x] create `rule-librarian-report-copy`
- [x] update `rule-librarian-report-copy`
- [x] create `estimate-librarian-report-copy-writes-the-file`
- [x] update `rule-hook-registry`
- [x] `.guppi/guppi/libreport.py`: the hook as `then` sets it, importing `subagent_outputs` from `casecheck.py`, `session_dir` from `ledger.py` and `session_stamp` and `read_payload` from `event.py`; written in this Work Mode under 956.1, ticked with no new run.
- [x] `.guppi/guppi/cli.py`: the command `libreport` runs `libreport.run`; written in this Work Mode under 956.1, ticked with no new run.
- [x] `.guppi/tests/test_libreport.py`: one test per line of `then`, over a transcript and an event log under a temporary folder: a last text, a last handback message, a second fire, another agent, and no transcript, no output or no session folder; written in this Work Mode under 956.1, ticked with no new run.
- [x] `uv run --project .guppi guppi render`: `.claude/settings.json`
- [x] read `estimate-librarian-report-copy-writes-the-file`
```

## Deferred

## Case 957 — The fix of the approval of a long plan put off

> **context:**
> The by-hand test of session 0128 showed that the Claude Code CLI withholds the approval of a long plan in any terminal, the terminal of VS Code included, with no GUPPI in the folder, while the Claude Code extension of VS Code approves it. The person judged it a bug of Claude Code, which has been reported to Anthropic, and put off any fix in GUPPI at /hi of session 0431: the person works in the extension, and only users of the plugin who approve a Spec in the CLI meet the fault.

> **problem:**
> No Case of this session decides how GUPPI lets a long Spec be approved in the Claude Code CLI.

```then
defer:
  - slug: insight-plugin-cli-withholds-approval-of-a-long-plan
    type: insight
    purpose: "Wait for Claude Code to fix the approval of a long plan in the CLI, a bug reported to Anthropic; read it again before the plugin ships, and name the limit in README.md for the users of the plugin"
```

## Case 963 — The split of one-time Estimates from lasting ones put off

> **context:**
> At /hi of session 0431 the person asked whether an Estimate that checks one action should be told apart from one that promises a lasting behaviour, so that one-time Estimates leave after the close of their sprint and only behaviour stays. A scan of the frontmatter of the 332 live Estimates found 5 on the live sprint page, which go to the archive with it at the close, and few one-time checks on rules or entities, such as `estimate-guppi-keeps-no-defer-of-its-shape` and `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`; the 332 Criteria were not read one by one. A one-time Estimate on a page with `core: true` keeps that page `draft` while it is pending, and `ships` of `.guppi/guppi/ship.py` takes it into the clean version once it passes. The person liked both ways the main agent named, a one-time Estimate on the live sprint page and a marker in its frontmatter, said they may be joined, and put the item off to the next session.

> **problem:**
> No Case of this session decides how a one-time Estimate is told apart from one that promises a lasting behaviour.

```then
defer:
  - slug: rule-estimates-schema
    type: rule
    purpose: "Tell one-time Estimates apart from those that promise a lasting behaviour: a one-time Estimate targets the live sprint page and carries a marker such as once: true, so it leaves at the close of the sprint, keeps no page with core: true draft and does not ship; and a pass over the live Estimates sorts them; put off at /hi of session 0431"
```
