## Case 884 — The window of a session reaches back past a later resume

> **context:**
> Each hook and command that reads the window of a session finds its `hi` and its plan file in the daily event logs, through `session_event_logs` of `.guppi/guppi/ledger.py`. That function walks the logs back from today and stops at the newest date that holds a start line of the stamp of any kind. A resume writes a start line with the same stamp, so a session resumed on a later date loses the date of its `hi`: `hi_moment` finds no `hi`, `session_dir` names no folder, and `plan_path` names no plan file. This session opened with `/hi` on 2026-10-17 at 23:07:24 and wrote its plan file at 23:55:37 (`vault/raw/2026-10-17/event_log.md`, lines 1472 to 1478). The lesson line of the session's ledger, `lesson-session-window-cut-by-a-resume-on-a-later-date`, records the resume on 2026-10-24 and the run of 2026-10-25 in which `run` of `.guppi/guppi/caseid.py` printed that no plan file stood, since `plan_path` gave None. The person removed the resume line by hand. A compaction on a later date writes a start line too and cuts the window the same way. The same cause hit session `44ee5004` on 2026-10-15 (`lesson-ledger-window-stops-at-a-resume-on-the-next-day`), and `decision-case-876` put it off on `rule-ledger-write`: this Case takes up that defer, so its decision line on `rule-ledger-write` carries `{supersedes:case 876}`. That mark retires the whole of `decision-case-876`, and the same Decision also puts off `rule-orchestration`, whose `deferred_by` names it. So this Case carries that put-off over unchanged: a `defer` of `rule-orchestration` with the text of the section of `decision-case-876` on that page, and an `update` of `rule-orchestration` with only a `change`, since `generate` clears a defer only from the pages the superseding Case names on a line other than a `defer`. The put-off stays in `backlog.md`, and `rule-orchestration` changes in no other way.
>
> The person chose that only a `startup` or a `fork` start line ends the walk. The Claude Code hooks page, https://code.claude.com/docs/en/hooks, calls `startup` the start of a new session and `fork` a new session forked from an existing one, and says nothing on whether `/clear` keeps the session id. A walk that passes a `clear` line is right either way, and is only slower when `/clear` gives a new stamp. A resume keeps the stamp: a Grep of `(0f0c3a58|654272af|44ee5004) (session-start|hi)` over the `event_log.md` files of `vault/raw/` printed lines in the logs of 2026-10-09, 2026-10-12, 2026-10-14 and 2026-10-15, where each `resume` line carries the stamp of an earlier `startup` line. I read `session_event_logs`, `hi_moment`, `session_dir` and `plan_path` of `.guppi/guppi/ledger.py`, `run` of `.guppi/guppi/caseid.py` and `recall` of `.guppi/guppi/recall.py` whole. `hi_moment`, `hi_of` of `.guppi/guppi/event.py` and `retro_mark` of `.guppi/guppi/onward.py` each open the window at the first start line of the stamp over the logs they get, and the wider walk gives them the start of the session.
>
> No code judges the kind of a start line today: a Grep of `"(compact|resume|startup|clear|fork)"` over `.guppi/guppi/` printed `.guppi/guppi/recall.py` alone, whose `SOURCE` judges the `source` of a payload, not a line of the log. So the new judgment stays in `.guppi/guppi/ledger.py` beside the walk, with no second copy (case 752). The test `test_the_walk_stops_at_the_first_date_holding_this_sessions_start` of `.guppi/tests/test_ledger.py` puts a `startup` line on a later date than an older `hi`, and it still passes, since a `startup` line still ends the walk. A Grep of `Path\(__file__\)` over `.guppi/tests/` printed 8 files, and a Grep of `event_log|session_dir|hi_moment` over those 8 printed nothing, so no test reads the live event logs.
>
> A Grep of `back to the (date|first)` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `estimate-prespec-checks-the-plan.md` and `estimate-prespec-hook-gates.md`. Both say that the logs reach back to the date of the session's start line, and both stand: the start that opened the session is still that line. `rule-event-log` says that a `/hi` writes no second `hi` when one follows the first start line of the stamp in the logs the ledger hook walks, and this stays true. `estimate-ledger-write-lifts` and `estimate-session-start-context` promise that the lines of a session opened with `/hi` reach its ledger. Their Criteria stand: the fix makes them hold after a resume on a later date, and the new Estimate checks that case. `estimate-event-log-records` promises that a `/hi` writes a `hi` line only when no `hi` of the stamp follows its first start line, and that a second `/hi` writes nothing and prints `hi: already recorded`. `prompt_line` and `hi_context` of `.guppi/guppi/event.py` judge that by `hi_of`, which reads the logs through `session_event_logs`. So far a `/hi` after a resume on a later date found no `hi`, and wrote a second one: session `44ee5004` holds one at 2026-10-15 05:53:31, which opened a new folder. After the fix it finds the first `hi`, as the Criterion says, so that Criterion stands. `estimate-compact-recall-reloads` promises the read-back of a compaction with a `hi` in the session's window, and nothing printed without one. `recall` of `.guppi/guppi/recall.py` finds the window by `session_dir` and `session_event_logs`, and after the fix a compaction on a later date than the `hi` finds it, so that Criterion stands too. The sprint close keeping the logs from the start date of an open session is the work of Case 886, which finds the start date by `session_dir` and `session_event_logs` and so rests on the walk this Case sets; this Case changes neither `rule-sprint-close`, `rule-raw-archive` nor `.guppi/guppi/sprint_close.py`. The window of this session was cut a second time on 2026-10-25, by a tool line. `session_event_logs` tests whether the text of the stamp, a space and the word `session-start` stands anywhere in the whole text of a day's log, so a logged search or command with that text in it ends the walk on that day, and a `tool Bash:` line of this session whose command held that text after a space did so. The person removed that line by hand: a Grep of `tool (Grep|Bash): .* [0-9a-f]{8} session.start` over `vault/raw/2026-10-25/event_log.md` now prints nothing. The person chose to fix that in this Case too: the walk ends only at a line of the form `- HH:MM:SS <stamp> session-start <kind>`. `hi_moment` already reads a start line by that form, with the line split on spaces and its event word compared, so the walk and `hi_moment` call one function of `.guppi/guppi/ledger.py` that reads a start line of the stamp and gives its kind, and the task adds no second copy (case 752). `hi_of` of `.guppi/guppi/event.py` and `retro_mark` of `.guppi/guppi/onward.py` read the event word by the same split, and this Case leaves them as they are. The person chose a History line alone for `rule-ledger-write`, since its mechanism lives in the docstring of `.guppi/guppi/ledger.py` (case 592), and Case 881.16 changes two other sentences of its Purpose.

> **problem:**
> A session resumed, or compacted, on a later date than its `/hi` loses its `hi`, its folder and its plan file in every hook and command that reads its window, and so does a session whose log on a later date holds a tool line with the text of its start line. Its ledger lines are refused, `guppi caseid` prints no id, and a second `/hi` opens a new folder.

> **recommend:**
> - **Which start line ends the walk back**
>   - Recommended: (a) only a new session ends it: a `startup` or a `fork` start line.
>   - Answer: agreed, (a).
> - **What checks the fix**
>   - Recommended: (a) a new Estimate on `rule-ledger-write`, checked by new tests and one reading on the live logs.
>   - Answer: agreed, (a).
> - **Whether the page `rule-ledger-write` gets a sentence**
>   - Recommended: (a) a History line only.
>   - Answer: agreed, (a).
> - **Where the sprint close's new rule on old logs goes**
>   - Recommended: (b) a new Case beside Case 884.
>   - Answer: (b).
> - **Change**
>   - Asked: the person agreed to the fixes of the findings of `/pre-spec`: name `estimate-event-log-records` and `estimate-compact-recall-reloads` and say why each stands, and carry over the put-off of `rule-orchestration` from `decision-case-876`, so that it stays in `backlog.md`.
>   - Taken: the `context` names both Estimates and why each stands; the Case gains a `defer` of `rule-orchestration` with the text of `decision-case-876` on that page, and an `update` of it with only a `change`, so that `generate` moves the put-off to this Case.
> - **Change**
>   - Asked: the person chose to add to this Case the second cut of the window, by a tool line whose text holds the stamp and the word `session-start`.
>   - Taken: the walk ends only at a start line read by its form, a `－` line of `then` says that a tool line ends no walk, a test puts such a tool line on a later date, the Estimate covers both cuts, and the decision line on `rule-ledger-write` addresses the lesson of the second cut too.

> **given:**
> `.guppi/guppi/ledger.py`: the walk `session_event_logs` and the readers `session_dir` and `plan_path`.
> **＋** `.guppi/guppi/caseid.py`: the command `guppi caseid`, a reader of the window.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the walk.
> **＋** `rule-ledger-write`: the page of the ledger hook, which holds the defer of this cause.
> **＋** `estimate-ledger-write-keeps-the-window-past-a-later-resume`: the new check of the walk.
> **＋** `rule-orchestration`: the page whose put-off this Case carries over.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py`, or `uv run --project .guppi guppi caseid --next --session <stamp>` of `.guppi/guppi/caseid.py`, runs on a later date than the `hi` of the session, and the event log of a later date holds a start line of the stamp of the kind `resume` or `compact`, or a tool line whose text holds the stamp, a space and the word `session-start`.

> **then:**
> `session_event_logs` of `.guppi/guppi/ledger.py` walks back past each start line of the stamp of the kind `resume`, `compact` or `clear`, and stops at the newest date that holds a `startup` or a `fork` start line of the stamp, a line of the form `- HH:MM:SS <stamp> session-start <kind>`.
> **＋** `session_dir` names the folder of the date and the time of the session's `hi`, and the ledger hook writes the lines of the session into its `ledger.md`.
> **＋** `plan_path` names the plan file that the session wrote before the resume, so `guppi caseid` prints an id.
> **－** With no `startup` or `fork` start line of the stamp on any date, the walk reads every event log up to today, and the window opens at the first start line of the stamp.
> **－** A `startup` start line of the stamp on a later date than an older `hi` still ends the walk, so that older `hi` opens no window.
> **－** A tool line whose text holds the stamp and the word `session-start`, such as a logged search or command, ends no walk.

> **tasks:**
> - [ ] `.guppi/guppi/ledger.py`: `session_event_logs` stops only at a date that holds a start line of the stamp of the kind `startup` or `fork`, read line by line by its form through one function that `hi_moment` calls too, never by a search of the whole text of the log; the module docstring and the docstrings of `session_event_logs` and `hi_recorded` say so.
> - [ ] `.guppi/tests/test_ledger.py`: tests with names that hold `later_date`: a `startup` and a `hi` on one date and a `resume` of the stamp on a later date, with a date between them; the same with a `compact`, with a `clear`, and with a `tool Grep:` line and a `tool Bash:` line whose text holds the stamp, a space and the word `session-start`. The ledger hook writes the lines into the folder of the `hi` date, `session_dir` names that folder, and `plan_path` names the plan file written on the date of the `hi`.
> - [ ] update `rule-ledger-write`
>   - change: `the window of a session reaches back past a resume or a compaction on a later date to its startup or fork start line, read by its form, so a tool line that names the start ends no walk`
> - [ ] create `estimate-ledger-write-keeps-the-window-past-a-later-resume`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `A session resumed or compacted on a later date than its /hi, or whose log on a later date holds a tool line with the text of its start line, keeps its hi, its folder and its plan file in every reader of its window`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ledger.py -k later_date; by hand: session_dir of .guppi/guppi/ledger.py for the stamp 44ee5004 over the live event logs, run by uv run --project .guppi python, names raw/2026-10-14/1907`
>   - tags: `[session, hooks, ledger]`
> - [ ] update `rule-orchestration`
>   - change: `the put-off of decision-case-876 carried over unchanged by case 884, which takes up the other put-off of that Decision`
> - [ ] defer `rule-orchestration`
>   - type: `rule`
>   - purpose: `Each round and each rebuild resumes the same case-guppi by SendMessage with its whole transcript, so its context only grows, and nothing caps it or hands a rebuild to a fresh agent with the case file and the reason alone (lesson-case-build-agent-context-grows-on-every-resume); moved here from the defer of the lesson by Case 836, and carried over from decision-case-876 by Case 884`
> - [ ] read `estimate-ledger-write-keeps-the-window-past-a-later-resume`

> **ratification:**
> ```
> - decision[case 884][update][rule-ledger-write]{ref:rule-ledger-write}{supersedes:case 876}{addresses:lesson-session-window-cut-by-a-resume-on-a-later-date}{addresses:lesson-session-window-cut-by-a-tool-line-that-names-the-start}
> - decision[case 884][create][estimate-ledger-write-keeps-the-window-past-a-later-resume]{ref:rule-ledger-write}{tags:session,hooks,ledger}
> - decision[case 884][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 884][defer][rule-orchestration]{ref:rule-orchestration}
> ```
