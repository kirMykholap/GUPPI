## Case 994 — The librarian gives its report back once, as its last output

> **context:**
> At its close the librarian gives its report back, and the `SubagentStop` hook `uv run --project .guppi guppi libreport` copies the last output of the agent into `report.md` of the session folder. The Render of `rule-close` asks for the report twice: as the last text, and again as the text of the handback, the `SubagentHandback` tool call by which a subagent delivers its final report. The librarian of session 0141 gave the report only in its handback, and its last plain text was a one-line note before its commit (handoff of session 2038, Observations). The hook copied the handback, so `report.md` was right, but the run and the words of the frame differ. The person chose that the frame asks for the report once, as the last output: the message of the handback where the agent has that tool, else its last text, and nothing after it; the stop at step 1 of `rule-documentation` says the same; and the Criterion of `estimate-close-reports-the-run` gains that promise.
> A handback alone was not chosen. The tools reference of Claude Code (https://code.claude.com/docs/en/tools-reference) says that `SubagentHandback` is "Provided only in auto mode, to subagents that the Agent tool runs locally other than forks", and the subagents page (https://code.claude.com/docs/en/sub-agents) gives the tool "for a subagent that reports through it". A librarian run outside auto mode has no handback, so its report must be its last text.
> The hook needs no change. `copy` and `last_output` of `.guppi/guppi/libreport.py`, `outputs` and `subagent_outputs` of `.guppi/guppi/casecheck.py` and `read_records` of `.guppi/guppi/ledger.py`, read whole, take every text block and the `message` of every `SubagentHandback` call of the assistant records of `agent_transcript_path`, in order, and write the last one that holds text. So the hook copies the report whichever way it goes back, and copies a later text in its place. The Purpose of `rule-librarian-report-copy` and the Criterion of `estimate-librarian-report-copy-writes-the-file` say the same, and stand.
> A Grep of the live pages of `vault/wiki/` but `log.md` and `brief.md` for the pattern `librarian.{0,80}(returns?|gives?|hands?) (its|the) report|report.{0,40}(as text|last text|last output|handback)` printed 5 files: `rule-close.md`, `rule-documentation.md`, `estimate-close-reports-the-run.md`, `rule-librarian-report-copy.md` and `estimate-librarian-report-copy-writes-the-file.md`. The first three change here, and the last two stand for the reason above. A Grep of `.claude/` for `last text|handback|hand .{0,15}back|as text` printed `.claude/agents/librarian-guppi.md`, at step 1 and at the close, which the render writes again, and `.claude/skills/wait-what/SKILL.md`, which speaks of the main agent's last text and stands. `/handoff` and `/box` read `report.md`, "which a hook writes from that report", and stand.
> The blocks of `.guppi/links.md` of `rule-close`, `rule-documentation`, `estimate-close-reports-the-run` and `.claude/agents/librarian-guppi.md` were read. Their neighbours that speak of the report are `rule-librarian-report-copy` and `estimate-close-reports-the-run`. `estimate-documentation-completes`, the Estimate of `rule-documentation`, speaks of the pages the report names, not of how the report goes back, and stands. `estimate-close-commits` speaks of the commit and stands. No test of `.guppi/tests/` reads `.claude/agents/librarian-guppi.md` by name. `callers()` of `.guppi/tests/test_guppi_package.py` reads every file under `.claude/`, and the new text holds no `uv run guppi` and no `uv run pytest`.
> The reading of the new Criterion waits for the next librarian run, by hand. A run that stops at step 1 is not read by it, since its report is no full report. The step 1 sentence says how the report goes back in the words of the close, and says that the run stops with no `guppi check` and no commit, since finding 1.6 of `/pre-spec` showed that a pointer to the close could be read as running the check and the commit too; the old step 1 asked for neither. The session's ledger holds no `error` lesson.

> **problem:**
> The frame of the librarian asks for its report twice, as its last text and in its handback, while the hook copies only the last output and a run outside auto mode has no handback. A run that follows only one of the two steps departs from the frame, and nothing checks that the report is the last output.

> **recommend:**
> - **How the close tells the librarian to give its report back**
>   - Recommended: (a) the handback where the tool exists, else plain text: the report given once, as the last output, nothing after it.
>   - Answer: agreed, (a).
> - **Whether the stop at the first step says the same**
>   - Recommended: (a) the same wording as the close, in step 1 of `rule-documentation`.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) the Criterion of `estimate-close-reports-the-run` replaced with one more line, its purpose and method set anew, and a new reading after the next librarian run.
>   - Answer: agreed, (a).

> **given:**
> `rule-close`: its Render, the close of the frame of the librarian.
> **＋** `rule-documentation`: its Render, step 1 of the frame of the librarian.
> **＋** `.claude/agents/librarian-guppi.md`: the frame, rendered from both pages.
> **＋** `estimate-close-reports-the-run`: its Criterion is replaced whole.
> **＋** `rule-librarian-report-copy`: the hook that copies the last output of the librarian into `report.md`.
> **＋** `/handoff`: the skill of `.claude/skills/handoff/SKILL.md`, which dispatches the librarian.
> **＋** `.claude/skills/handoff/SKILL.md`: the file of `/handoff`, which reads `report.md`.
> **＋** `/box`: the skill of `.claude/skills/box/SKILL.md`, which dispatches the librarian in a session it runs.
> **＋** `.claude/skills/box/SKILL.md`: the file of `/box`, which reads `report.md`.
> **＋** `vault/raw/<date>/<hi HHMM>/report.md`: the file the hook writes from the report.

> **when:**
> The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches, or that `/box` of `.claude/skills/box/SKILL.md` dispatches in a session that `/box` runs, reaches the close of `.claude/agents/librarian-guppi.md` and ends, and the hook of `rule-librarian-report-copy` fires.

> **then:**
> `vault/raw/<date>/<hi HHMM>/report.md`, the folder of the `handoff.md` the dispatch names, holds the report that the librarian returned last.
> **＋** The librarian gives the report once, as its last output: the `message` of its `SubagentHandback` call where it has that tool, else its last text, with no output after it.
> **＋** The file gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags the run raised and the lint total.
> **＋** The file gives each part that another step of `.claude/agents/librarian-guppi.md` sends to the report.
> **－** The file holds no test result and no list of files.
> **－** No limit of lines binds the file.

> **tasks:**
> - [ ] update `rule-close`
>   - old: `` Then return the report as your last text, and give the same text when you hand your report back; write no text after the handback, since the hook copies your last output, a text after the handback included. The hook of `rule-librarian-report-copy` copies that text ``
>   - new: `` Then give the report back once, as your last output: as the message of your handback where you have the tool `SubagentHandback`, and as your last text where you have no such tool, since Claude Code gives that tool only in auto mode; write no text after it, since the hook copies your last output, a text after the handback included (as set in case 994). The hook of `rule-librarian-report-copy` copies that report ``
>   - change: `the librarian gives its report back once, as its last output: the handback where it has the tool, else its last text`
> - [ ] update `rule-documentation`
>   - old: `If it exits 1, return the report as text and stop (as set in cases 944 and 956).`
>   - new: `` If it exits 1, give the report back once, as your last output: as the message of your handback where you have the tool `SubagentHandback`, and as your last text where you have no such tool; write no text after it, and stop, with no `guppi check` and no commit (as set in cases 944, 956 and 994). ``
>   - change: `a run that stops at step 1 gives its report back once, as its last output, and runs no check and no commit`
> - [ ] update `estimate-close-reports-the-run`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the librarian gives its report back once at its close, as its last output, by its handback where it has the tool or as its last text, and report.md of the session folder holds that report and gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to the report, with no test result and no list of files"
>     method: "by hand, after the librarian's run of a session whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close that gives the report back once as the last output: the agent reads report.md of the session folder of that run, as the commit of /handoff or /box holds it by git show, beside every output of the librarian, its texts and the message of each SubagentHandback call, read in its agent transcript under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — the librarian gives the report once, as its last output, by its handback or its last text`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-close-reports-the-run`

> **ratification:**
> ```
> - decision[case 994][update][rule-close]{ref:rule-close}
> - decision[case 994][update][rule-documentation]{ref:rule-documentation}
> - decision[case 994][update][estimate-close-reports-the-run]{ref:rule-close}
> ```
