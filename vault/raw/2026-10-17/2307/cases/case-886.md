## Case 886 — The sprint close keeps the event logs from the start of the open session

> **context:**
> At the close of a sprint, `old_logs` of `.guppi/guppi/sprint_close.py` picks the event logs that move from `vault/raw/<date>/` to the archive. It takes the newest session folder by `session_of_run` of `.guppi/guppi/materialize.py`, whose date is the date of the `/hi` of that session, and moves each log dated before the day before that date. It never reads when the session started. The hooks of a session read its logs through `session_event_logs` of `.guppi/guppi/ledger.py`, and after Case 884 that walk reaches back past a later resume to the `startup` or `fork` start line of the stamp. So a session that started two or more days before its `/hi` would lose the logs of its first days at a close, and the texts that give the reason as the day before become false. This session opened with `/hi` on 2026-10-17 and runs on 2026-10-25: its folder is `vault/raw/2026-10-17/2307/`, and a close today would keep the logs from 2026-10-16 on, so the gap does not hit this session. I read `old_logs`, `move_logs`, `empty_raw` and `run` of `sprint_close.py`, `session_of_run` of `materialize.py`, and `session_event_logs`, `hi_moment` and `session_dir` of `ledger.py` whole. The two judgments of the window part on a session whose start line stands two or more days before the date of its folder: `old_logs` keeps the logs from the day before the folder date, `session_event_logs` reads from the start date. The person chose that the close asks the window of the hooks: it finds the stamp whose `hi` line `session_dir` takes to the newest session folder, and keeps the logs from the first date `session_event_logs` gives for that stamp. So the close imports both functions from `ledger.py` and holds no second copy of the window, as `rule-one-judgment-one-implementation` sets it. A Grep of `def \w*(stamp|hi_line|of_folder|folder_stamp|session_id)\w*` over `.guppi/guppi/` printed `session_stamp` of `.guppi/guppi/event.py` and `stamp` of `.guppi/guppi/spec.py`, and neither maps a session folder to its stamp. Without a session folder, or where no stamp or more than one leads to it, the close moves no log and says why on stdout, by the person's choice.
>
> A tool line of this session whose text held the stamp and the word `session-start` cut its window once on 2026-10-25, since `session_event_logs` searched the whole text of a log. The person removed that line by hand, and Case 884, built again, makes the walk end only at a start line read by its form. This Case rests on that walk, so its test with a resume on a later date runs after the task of Case 884 on `ledger.py`. The Criterion of `estimate-sprint-close-moves-old-event-logs` speaks of the logs that move, so this Case replaces it whole. Its purpose and its method still state the promise and stand. Its line on `.gitignore` stays word for word, since the put-off of Case 882.3 names that Criterion and its method as waiting for a Case of their own. The Purpose of `rule-sprint-close` says the close moves the event logs that the hooks of the open session no longer read. The fix makes that true, so it stands. The sentence of `rule-raw-archive` on the logs dated before the day before the session of the run becomes false, and a pair replaces it. A Grep of `day before` over `vault/wiki/`, `.claude/` and `.guppi/guppi/` printed `vault/wiki/orchestration.md` and `vault/wiki/rules/rule-orchestration.md`, on a reminder of an example Case, which stand; `vault/wiki/rules/rule-raw-archive.md`, which the pair changes; `vault/wiki/estimates/estimate-sprint-close-moves-old-event-logs.md`, whose Criterion is replaced; and `.guppi/guppi/sprint_close.py`, whose docstrings a task changes. A Grep of `rule-raw-archive|sprint-close-moves-old-event-logs|rule-sprint-close` over `.guppi/tests/` printed nothing, so no test reads these pages live. The tests of the logs in `.guppi/tests/test_sprint_close.py` write made-up logs with no `hi` line, so they change with the code.

> **problem:**
> The sprint close keeps the event logs from the day before the date of the `/hi` of the open session, while its hooks read back to the date it started, so a session that started days before its `/hi` loses logs it still reads.

> **recommend:**
> - **How the close finds the start of the open session**
>   - Recommended: (a) ask the window the hooks use: the stamp whose `hi` line `session_dir` takes to the newest session folder, and the first date `session_event_logs` gives for it.
>   - Answer: agreed, (a).
> - **When the close cannot tell which session is open**
>   - Recommended: (a) move no log, and say so on stdout.
>   - Answer: agreed, (a).
> - **Where the stop on a tool line is fixed**
>   - Recommended: (a) Case 884 fixes it.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) replace the Criterion of `estimate-sprint-close-moves-old-event-logs`; keep its purpose and method.
>   - Answer: agreed, (a).
> - **Whether the Purpose of `rule-sprint-close` changes**
>   - Recommended: (a) the Purpose stands; the docstring and `rule-raw-archive` change.
>   - Answer: agreed, (a).

> **given:**
> `.guppi/guppi/sprint_close.py`: `old_logs`, which picks the logs the close moves, and its docstrings.
> **＋** `.guppi/guppi/ledger.py`: `session_dir` and `session_event_logs`, the window of a session, which the close imports.
> **＋** `vault/raw/<date>/event_log.md` and `vault/archive/<id>/<date>/event_log.md`: the event log of a date, where it stands before the close moves it and after.
> **＋** `.guppi/tests/test_sprint_close.py`: the tests of the logs the close moves.
> **＋** `estimate-sprint-close-moves-old-event-logs`: its Criterion is replaced whole.
> **＋** `rule-raw-archive`: its sentence on the logs the close moves.
> **＋** `rule-one-judgment-one-implementation`: the rule that the close shares the window of the hooks.
> **＋** `vault/raw/2026-10-17/2307/cases/case-884.md`: the Case that makes the walk end only at a `startup` or `fork` start line.

> **when:**
> `uv run --project .guppi guppi sprint-close --sprint <id> --apply` of `.guppi/guppi/sprint_close.py` closes a sprint, in the librarian's run or in `.guppi/tests/test_sprint_close.py` over a made-up vault, and the session of the run is the stamp whose `hi` line `session_dir` of `.guppi/guppi/ledger.py` takes to the newest session folder of `vault/raw/`.

> **then:**
> After a close whose run of `guppi cleanup` exits 0, each `vault/raw/<date>/event_log.md` dated before the start date of the session of the run, the first date that `session_event_logs` of `.guppi/guppi/ledger.py` gives for its stamp, moves to `vault/archive/<id>/<date>/event_log.md`.
> **＋** A date folder that the moves leave empty is removed.
> **＋** `.gitignore` leaves out each moved log, so git tracks none.
> **＋** Stdout holds one line per log moved.
> **－** The log of the start date and of each later date stays where it is, since the hooks of that session read them, the start date two or more days before the date of the session folder included.
> **－** With no session folder in `vault/raw/`, or with no stamp or more than one whose `hi` line `session_dir` takes to the newest session folder, no log moves, and stdout holds one line that says why.
> **－** A log whose target exists does not move: one line on stderr, and the close exits 1 after the other moves.
> **－** A refused close moves no log.

> **tasks:**
> - [ ] `.guppi/guppi/sprint_close.py`: `old_logs` finds the stamp of the session of the run among the stamps of the `hi` lines of the log of the date of the newest session folder, as the one stamp for which `session_dir` of `.guppi/guppi/ledger.py` names that folder, and keeps each log dated on or after the first date of `session_event_logs` for that stamp; with no session folder, or no such stamp or more than one, it moves no log and `move_logs` prints one line `archive: event logs kept: <reason>` on stdout, with no change to the exit code; the module docstring and the docstring of `old_logs` say so in place of the day before.
> - [ ] `.guppi/tests/test_sprint_close.py`: the tests whose names hold `event_log` write logs with a `startup` and a `hi` line of one stamp; a test where the `startup` stands two days before the date of the session folder keeps the logs from the `startup` date; a test with a `resume` of the stamp on a later date, run after the task of Case 884 on `.guppi/guppi/ledger.py`, keeps the same logs; tests with no `hi` line that leads to the folder, and with `hi` lines of two stamps at the time of the folder, move no log and print the line on stdout.
> - [ ] update `estimate-sprint-close-moves-old-event-logs`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the close keeps the event logs from the start date of the open session, found by the window of the hooks`
> - [ ] update `rule-raw-archive`
>   - old: `` The close of a sprint moves each log dated before the day before the session of its run to `vault/archive/<id>/<date>/`, `<id>` the sprint it closes, still gitignored, as `rule-sprint-close` sets it (case 743.3). ``
>   - new: `` The close of a sprint moves each log dated before the start of the session of its run, the first date of the logs the ledger hook walks for that session, to `vault/archive/<id>/<date>/`, `<id>` the sprint it closes, still gitignored, as `rule-sprint-close` sets it (as set in cases 743.3 and 886). ``
>   - change: `the close of a sprint keeps the event logs from the start date of the open session`
> - [ ] read `estimate-sprint-close-moves-old-event-logs`

> **ratification:**
> ```
> - decision[case 886][update][estimate-sprint-close-moves-old-event-logs]{ref:rule-sprint-close}
> - decision[case 886][update][rule-raw-archive]{ref:rule-raw-archive}
> ```
