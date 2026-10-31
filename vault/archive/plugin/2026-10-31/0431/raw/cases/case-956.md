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

### Case 956.1 — The hook copies the librarian's report into the session folder

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

> **tasks:**
> - [ ] create `rule-librarian-report-copy`
>   - ref: `rule-documentation`
>   - type: `rule`
>   - kind: `Leaf`
>   - purpose: `Prevents the librarian's report from standing in no file when Claude Code refuses the Write of a report file by a subagent`
>   - enforcement: `hook`
>   - implementation_ref: `[.guppi/guppi/libreport.py, .guppi/tests/test_libreport.py, .claude/settings.json]`
>   - core:
>     ```
>     true
>     ```
>   - tags: `[hooks, harness, librarian]`
>   - sections.Purpose: `` Prevents the librarian's report from standing in no file when Claude Code refuses the `Write` of a report file by a subagent. Claude Code refused the librarian's `Write` of `report.md` with the message that subagents return findings as text and write no report files (as set in case 956). The `SubagentStop` hook `uv run --project .guppi guppi libreport` copies the last output that `librarian-guppi` returned into `report.md` in the session folder by its own code, so no `Write` call of a subagent is made, and `/handoff` or `/box` shows that file and commits it (as set in case 956). ``
> - [ ] create `estimate-librarian-report-copy-writes-the-file`
>   - ref: `rule-librarian-report-copy`
>   - kind: `QA`
>   - purpose: `Whether the SubagentStop hook writes the last output of librarian-guppi, a text or a handback message, into report.md of the session folder, writes it again at a second fire, and writes nothing for another agent or with no transcript, output or folder`
>   - method: `uv run --project .guppi guppi test, which runs .guppi/tests/test_libreport.py`
>   - tags: `[hooks, harness, librarian]`
> - [ ] update `rule-hook-registry`
>   - old: `"command": "uv run --project .guppi guppi casecheck --subagent", "timeout": 30 } ] }`
>   - new: `"command": "uv run --project .guppi guppi casecheck --subagent", "timeout": 30 }, { "type": "command", "command": "uv run --project .guppi guppi libreport", "timeout": 30 } ] }`
>   - change: `the SubagentStop hook guppi libreport registered`
> - [ ] `.guppi/guppi/libreport.py`: the hook as `then` sets it, importing `subagent_outputs` from `casecheck.py`, `session_dir` from `ledger.py` and `session_stamp` and `read_payload` from `event.py`.
> - [ ] `.guppi/guppi/cli.py`: the command `libreport` runs `libreport.run`.
> - [ ] `.guppi/tests/test_libreport.py`: one test per line of `then`, over a transcript and an event log under a temporary folder: a last text, a last handback message, a second fire, another agent, and no transcript, no output or no session folder.
> - [ ] `uv run --project .guppi guppi render`: `.claude/settings.json`
> - [ ] read `estimate-librarian-report-copy-writes-the-file`

> **ratification:**
> ```
> - decision[case 956.1][create][rule-librarian-report-copy]{ref:rule-documentation}{tags:hooks,harness,librarian}
> - decision[case 956.1][create][estimate-librarian-report-copy-writes-the-file]{ref:rule-librarian-report-copy}{tags:hooks,harness,librarian}
> - decision[case 956.1][update][rule-hook-registry]{ref:rule-hook-registry}
> ```

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

> **tasks:**
> - [ ] update `rule-close`
>   - old: `` Write the report by the `Write` tool into `report.md` in the session's folder, the folder of the `handoff.md` your dispatch names (as set in case 944). The report gives ``
>   - new: `The report gives`
>   - old: `` Then return the text of `report.md` unchanged as your report, and after it the refusal of any call that came after the file was written (as set in case 944). ``
>   - new: `` Then return the report as your last text, and give the same text when you hand your report back; write no text after the handback, since the hook copies your last output, a text after the handback included. The hook of `rule-librarian-report-copy` copies that text into `report.md` in the session's folder, the folder of the `handoff.md` your dispatch names, and `/handoff` or `/box` commits it; write no `report.md` yourself (as set in case 956). ``
>   - change: `the librarian returns its report as text and writes no report.md; a hook copies the text into the file`
> - [ ] update `rule-documentation`
>   - old: `` If it exits 1, return the report as text, write no `report.md`, and stop (as set in case 944). ``
>   - new: `If it exits 1, return the report as text and stop (as set in cases 944 and 956).`
>   - change: `step 1 no longer says that a stopped run writes no report.md, since the hook copies every returned report`
> - [ ] update `estimate-close-reports-the-run`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether report.md of the session folder holds the report the librarian returned last at its close, and gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to the report, with no test result and no list of files"
>     method: "by hand, after the librarian's run of a session that starts with the hook of rule-librarian-report-copy in .claude/settings.json and whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close that returns the report as text: the agent reads report.md of the session folder of that run, as the commit of /handoff or /box holds it by git show, beside the last output of the librarian read in its agent transcript under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the hook writes report.md from the report the librarian returns`
> - [ ] by hand in Work Mode: the main agent dispatches a `general-purpose` subagent that calls `Write` on three files in a new folder outside the repository: `report.md` with a text in the form of a report, `close.md` with the same text, and `report.md` in a second new folder with one plain line. The subagent returns what Claude Code answered to each call, and the main agent records the result as a `knowledge` lesson line with its `source`.
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-close-reports-the-run`

> **ratification:**
> ```
> - decision[case 956.2][update][rule-close]{ref:rule-close}
> - decision[case 956.2][update][rule-documentation]{ref:rule-documentation}
> - decision[case 956.2][update][estimate-close-reports-the-run]{ref:rule-close}
> ```

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

> **tasks:**
> - [ ] update `rule-handoff`
>   - old: `` Wait for its report and show it to the person unchanged. Do not commit after this, and write no `LEDGER` block. ``
>   - new: `` Wait for its report. Read `vault/raw/<date>/<hi HHMM>/report.md`, which a hook writes from that report, and show its text to the person unchanged; when no `report.md` stands there, show the returned report unchanged and one line that says that `report.md` is missing. When `report.md` stands, commit it alone, by the Bash tool: `git add vault/raw/<date>/<hi HHMM>/report.md && git commit -m "docs(vault): librarian report, <date>"`, never `--amend`. Make no other commit after this, and write no `LEDGER` block (as set in case 956). ``
>   - change: `/handoff shows report.md and commits it alone after the librarian's commit`
> - [ ] update `estimate-handoff-dispatches`
>   - set:
>     ```
>     status: pending
>     purpose: "/handoff stops on a dirty tree, writes handoff.md from memory into the session's folder, dispatches the librarian with its path, shows report.md and commits it alone after the librarian's commit, or, in a session that /box runs, hands back to /box"
>     method: "by hand, after a /handoff whose .claude/skills/handoff/SKILL.md holds the Render of rule-handoff that commits report.md: the event log vault/raw/<date>/event_log.md, handoff.md and git log, and the dispatch line and the text shown to the person read in the transcript of that session under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line; by hand, after a /handoff in a session that /box runs: the event log, and the step of /box that follows read in the transcript of that session under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — /handoff shows report.md and commits it alone`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] by hand, once, after `/handoff` of this session shows the librarian's report: when `vault/raw/2026-10-31/0431/report.md` stands, the main agent shows its text to the person unchanged and commits it alone by the Bash tool, `git add vault/raw/2026-10-31/0431/report.md && git commit -m "docs(vault): librarian report, 2026-10-31"`, never `--amend`, since the skill of this session still says to make no commit after the librarian; when no such file stands, it says so in one line.
> - [ ] read `estimate-handoff-dispatches`

> **ratification:**
> ```
> - decision[case 956.3][update][rule-handoff]{ref:rule-handoff}
> - decision[case 956.3][update][estimate-handoff-dispatches]{ref:rule-handoff}
> ```

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

> **tasks:**
> - [ ] update `rule-spec-box`
>   - old: `` Wait for its report and show it to the person unchanged, then one line with the exit code of `uv run --project .guppi guppi test`. Do not commit after this, and write no `LEDGER` block. ``
>   - new: `` Wait for its report. Read `vault/raw/<hi date>/<hi HHMM>/report.md`, which a hook writes from that report, and show its text to the person unchanged, or, when no `report.md` stands there, the returned report unchanged and one line that says that `report.md` is missing; then one line with the exit code of `uv run --project .guppi guppi test`. When `report.md` stands, commit it alone: `git add vault/raw/<hi date>/<hi HHMM>/report.md && git commit -m "docs(vault): librarian report, <hi date>"`, never `--amend`. Make no other commit after this, and write no `LEDGER` block (as set in case 956). ``
>   - change: `/box shows report.md and commits it alone after the librarian's commit`
> - [ ] update `estimate-spec-box-runs-a-conserved-spec`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether /box checks a conserved Spec, runs it on its own branch brought up to the shared branch by a fast-forward, merges the branch back by a fast-forward after the handoff, has the librarian write the pages on the shared branch, and shows report.md and commits it alone after the librarian's commit, stopping when the check or a merge refuses"
>     method: "uv run --project .guppi guppi render --check; by hand, after a session that runs a conserved Spec by /box on the Render of rule-spec-box that commits report.md: git log, the branches, the folders of the session and of the conserved Spec, the librarian's commit and the commit of report.md, and the dispatch line and the text shown to the person read in the transcript of that session under ~/.claude/projects/, recorded in the estimate line with that transcript named"
>     ```
>   - change: `the Criterion replaced whole — /box shows report.md and commits it alone`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/box/SKILL.md`
> - [ ] read `estimate-spec-box-runs-a-conserved-spec`

> **ratification:**
> ```
> - decision[case 956.4][update][rule-spec-box]{ref:rule-spec-box}
> - decision[case 956.4][update][estimate-spec-box-runs-a-conserved-spec]{ref:rule-spec-box}
> ```

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

> **tasks:**
> - [ ] update `estimate-close-commits`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the commit of report.md by /handoff or /box may follow the librarian's commit`
> - [ ] read `estimate-close-commits`

> **ratification:**
> ```
> - decision[case 956.5][update][estimate-close-commits]{ref:rule-close}
> ```
