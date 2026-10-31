## Case 944 — The librarian writes its report into the session folder

> **context:**
> The librarian ends its run with a report, and `/handoff`, or `/box` in a session that `/box` runs, shows it to the person unchanged. No file of the repository holds that report, and `/hi` reads no transcript of an earlier session (case 670.5), so the method of `estimate-close-reports-the-run` asks the person whether the report was complete. At the /hi of this session the person answered from memory on the report of session 2005, and the ledger holds that reading as passed; the person said the Estimate is wrong, since the agent should read and check the report by itself. The `## Result` of the page also holds an earlier failed reading that rested on another report than the one the method meant. With this Case the librarian writes its report by the `Write` tool into `report.md` in the session folder, the folder of the `handoff.md` its dispatch names, before its commit, so the commit of the run takes the file, and it returns the text of that file unchanged. `rule-close` is a Leaf with `core: true` and status `draft`; its Render is the close step of `.claude/agents/librarian-guppi.md`, and the Case rewrites that paragraph whole by one pair; its `## Purpose` stands, since it speaks of the commit only. The Criterion of `estimate-close-reports-the-run` is replaced whole, and its `purpose` and `method` are set anew, since both name the report as `/handoff` shows it and the person's answer; the Estimate goes `pending`, and the passed reading of this session stays in its History. No line of the old Criterion is carried word for word, by the person's choice of a Criterion replaced whole. Its `When` lines, on the run that `/handoff` or `/box` dispatches and the showing of its report, become one `when` line on that run reaching the close. Its lines on the parts of the report, on what the report does not hold and on the limit of lines now speak of the file. Its line on the exit code of `uv run --project .guppi guppi test` that `/box` shows beside the report is dropped, since that exit code is a line of `/box` and never enters the file. The Criterion promises the file and what it holds; that the returned text equals the file stands in the Render only, since the event log of the run keeps a tool name and one input field, never the text written (read in `.guppi/guppi/event.py`, the module docstring and `tool_detail`), and the chat of an earlier session is not read. The librarian's run of this session still loads the old frame when it starts, so the first run that writes `report.md` is that of the next session, and the reading waits for it. The frame already says that a hook's refusal of a call is named in the report; a refused commit comes after the file is written, so the new Render places such a refusal after the text of the file in the returned report, which keeps the two sentences from contradicting each other. A finding of `/pre-spec` on the ratified Case showed that step 1 of the Render of `rule-documentation`, which is `built` and has `core: true`, tells the librarian to write the report and stop when `guppi materialize` exits 1, before any close or commit; the person chose that such a run writes no `report.md` and returns its report as text, as today, and the Case rewrites that sentence by one pair, while the Criterion, whose `when` is a run that reaches the close, does not change. A Grep of `write the report and stop|exits 1, write the report` over the repository outside `vault/raw/` printed `.claude/agents/librarian-guppi.md`, `vault/wiki/rules/rule-documentation.md`, `vault/archive/migration/2026-09-10/raw/materialize.yaml` and `vault/archive/migration/2026-09-10/raw/spec.md`; the two archived files are records of an earlier session and stand, and the agent file follows by the render. The sentence of that Render that the librarian writes only through the scripts named below stands: it follows the sentence on `vault/wiki/`, the same frame already names a write outside the scripts, `vault/wiki/brief.md` by the `Write` tool, and `report.md` lies outside `vault/wiki/`, its write set in the close step. The `## Purpose` and `## How it works` of `rule-documentation` say nothing of where the report goes, and the Criterion of its Estimate `estimate-documentation-completes` has no line on the stop at step 1, so both stand. `estimate-close-commits` stands: its Criterion lets the commit take any path under `vault/`, and `report.md` lies there. `estimate-documentation-completes` stands: `report.md` is no page of `vault/wiki/`, and the librarian writes it by `Write`, not by `cp`, `mv`, a redirect or a heredoc. A Grep of `rule-close|librarian-guppi\.md|close-reports|no test result` over `.guppi/` printed `.guppi/guppi/onward.py` and `.guppi/guppi/render.py`, neither under `.guppi/tests/`, so no test reads the changed file live. A Grep of `librarian.{0,40}report|report of the librarian|its report` over `vault/wiki/` printed the files `rule-handoff`, `rule-spec-box`, `rule-where-to-stop`, `rule-skill-hi`, `rule-retro`, `rule-case-protocol`, `case-schema.md`, `where-to-stop.md`, `glossary.md`, `entity-glossary`, `estimate-close-reports-the-run`, `estimate-handoff-dispatches`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-documentation-completes`, `estimate-orchestration-states-a-subagent-fact-from-its-transcript`, `estimate-sprint-close-runs-in-the-librarian-run`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-synthesis-clusters`, `lesson-hi-reads-the-end-state-of-a-command-that-failed-first`, `lesson-librarian-writes-a-total-no-count-printed`, `lesson-brief-lists-transcript-readings-under-work`, `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback`, `lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction`, `insight-case-build-changes-a-step-without-reading-its-readers` and `log.md`, 25 files; the hits read outside the lessons, the Insight and `log.md` say that `/handoff` and `/box` show the report unchanged, or name the report as the end of a run, and each stays true, since the report the librarian returns is still the one they show.

> **problem:**
> The Estimate of the librarian's report can be read only by the person, from a text shown once in the chat of an earlier session, so the agent cannot check it by itself.

> **recommend:**
> - **How the agent reads the report**
>   - Recommended: (a) the librarian writes the report into `report.md` in the session folder before its commit and returns the same text.
>   - Answer: agreed, (a).
> - **What happens to the promise and to today's passed reading**
>   - Recommended: (a) one Estimate: its Criterion replaced whole with the file, its `purpose` and `method` set anew, its status `pending`.
>   - Answer: agreed, (a).
> - **What the Estimate promises about the text the librarian sends back**
>   - Recommended: (a) the Estimate promises the file and its content only; the frame still tells the librarian to return the text of the file unchanged.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: after a finding of `/pre-spec`, the person chose that a run that stops at step 1 of the frame, when `guppi materialize` exits 1, writes no `report.md` and returns its report as text, as today; the Criterion does not change.
>   - Taken: an `update` of `rule-documentation` rewrites step 1 of its Render so; `context` says why the line on the scripts as the only way to write stands.

> **given:**
> `rule-close`: the Rule whose Render is the close step of the librarian.
> **＋** `rule-documentation`: the Rule whose Render is the frame of the librarian, step 1 among its steps.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian, rendered from both.
> **＋** `estimate-close-reports-the-run`: its Criterion is replaced whole.
> **＋** `.claude/skills/handoff/SKILL.md`: dispatches the librarian's run and shows its report.
> **＋** `.claude/skills/box/SKILL.md`: dispatches the librarian's run in a session that `/box` runs.
> **＋** `vault/raw/<date>/<hi HHMM>/report.md`: the file the run writes.

> **when:**
> The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches, or that `/box` of `.claude/skills/box/SKILL.md` dispatches in a session that `/box` runs, reaches the close of `.claude/agents/librarian-guppi.md`.

> **then:**
> Before its commit, the librarian writes its report by the `Write` tool into `vault/raw/<date>/<hi HHMM>/report.md`, the folder of the `handoff.md` its dispatch names.
> **＋** The commit of the run takes that file.
> **＋** The file gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags the run raised and the lint total.
> **＋** The file gives each part that another step of `.claude/agents/librarian-guppi.md` sends to the report.
> **－** The file holds no test result and no list of files.
> **－** No limit of lines binds the file.

> **tasks:**
> - [ ] update `rule-close`
>   - old:
>     ```
>     Run `uv run --project .guppi guppi check` and keep its output for the report. Commit the vault with the files the render wrote, by the Bash tool, since the command is written for a POSIX shell: `git add vault $(uv run --project .guppi guppi render --paths) && git commit -m "docs(vault): librarian, <date>"`, never `--amend`, never a path that neither `vault` nor that list names. After the commit, no file the render wrote stands modified or untracked. Then return a report: pages created and updated per category, entries marked incomplete or failed, pages archived, the flags you raised, the lint total, and each part that another step of this frame sends to the report. Nothing else: no test result and no list of files (as set in case 913).
>     ```
>   - new:
>     ```
>     Run `uv run --project .guppi guppi check` and keep its output for the report. Write the report by the `Write` tool into `report.md` in the session's folder, the folder of the `handoff.md` your dispatch names (as set in case 944). The report gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags you raised, the lint total, and each part that another step of this frame sends to the report. Nothing else: no test result and no list of files (as set in case 913). Commit the vault with the files the render wrote, by the Bash tool, since the command is written for a POSIX shell: `git add vault $(uv run --project .guppi guppi render --paths) && git commit -m "docs(vault): librarian, <date>"`, never `--amend`, never a path that neither `vault` nor that list names. After the commit, no file the render wrote stands modified or untracked. Then return the text of `report.md` unchanged as your report, and after it the refusal of any call that came after the file was written (as set in case 944).
>     ```
>   - change: `the librarian writes its report into report.md of the session folder before its commit and returns that text`
> - [ ] update `rule-documentation`
>   - old: `` 1. Run `uv run --project .guppi guppi materialize`. If it exits 1, write the report and stop. ``
>   - new: `` 1. Run `uv run --project .guppi guppi materialize`. If it exits 1, return the report as text, write no `report.md`, and stop (as set in case 944). ``
>   - change: `a run that stops at step 1 returns its report as text and writes no report.md`
> - [ ] update `estimate-close-reports-the-run`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the librarian writes its report into report.md of the session folder before its commit, the commit takes it, and the file gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to the report, with no test result and no list of files
>     method: "by hand, after a librarian's run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close that writes report.md: the agent reads report.md of the session folder of that run, as the commit of the run holds it by git show, against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the report is written into report.md of the session folder and the agent reads that file`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-close-reports-the-run`

> **ratification:**
> ```
> - decision[case 944][update][rule-close]{ref:rule-close}
> - decision[case 944][update][estimate-close-reports-the-run]{ref:rule-close}
> - decision[case 944][update][rule-documentation]{ref:rule-documentation}
> ```
