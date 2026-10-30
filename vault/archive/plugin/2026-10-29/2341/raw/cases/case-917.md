## Case 917 — The event log checks name vault/.gitignore

> **context:**
> When a sprint closes, `guppi sprint-close` moves old daily event logs into `vault/archive/`, and git must ignore them there. Since case 893.1 the lines that ignore the logs stand in `vault/.gitignore`, and the root `.gitignore` holds none. `guppi ship` writes `vault/.gitignore` into the clean version: the constant `VAULT_IGNORE` of `.guppi/guppi/ship.py`, which `plan` adds to the files it writes, checked by `test_it_writes_the_lines_that_keep_the_event_logs_out_of_git` in `.guppi/tests/test_ship.py`. So the brief's line that the clean version holds no `.gitignore` and that no module writes one is half wrong: the root `.gitignore` does not ship, but `vault/.gitignore` does. The defect is that two shipped Estimates name a bare `.gitignore`. The `method` of `estimate-sprint-close-moves-old-event-logs` sends the reader to "the line of .gitignore" in the tree, which reads as the root file and finds no such line there. One line of its Criterion and one line of the Criterion of `estimate-event-log-records` name the same bare file. The module docstring of `.guppi/guppi/sprint_close.py` says the same. The rule that governs these texts is the Criterion of `estimate-clean-branch-ships-neutral-texts`: no sentence of the `purpose` or `method` of a shipped Estimate may hold only in the repository of GUPPI. Its last reading listed the Criterion line of `estimate-sprint-close-moves-old-event-logs` among those that do. Both target rules, `rule-sprint-close` and `rule-event-log`, carry `core: true`, so both Estimates ship. The Criterion of `estimate-clean-branch-ships-neutral-texts` stands, since this Case changes texts it judges and not the promise.
>
> The person chose to replace the Criterion of each Estimate whole, with the one line changed to `vault/.gitignore`, and to fix the docstring. The two Estimates fail apart and need different readings, so the Case splits: 917.1 covers the close and 917.2 the event log. Each Estimate goes `pending` and is read at the Retro of this session. Its rule goes `draft` at the librarian's cascade until that reading passes, so `guppi ship` without `--allow-draft` refuses until then. The `method` of `estimate-event-log-records` asked for a `/hi` by hand in plan mode and one outside it, which wait for another session, and the check of this file refused it. The person chose to drop those two readings. The tests `test_plan_mode_hi_writes_the_line` and `test_plan_mode_hi_outside_it_is_refused` of `.guppi/tests/test_event.py` feed made-up `/hi` payloads in plan mode and in each other mode. A live payload with its mode was read once, at the reading the page's Result records, and is not read again. The new `method` keeps the tests and the ignore and timing readings by hand, all at the Retro of this session. The `purpose` of `estimate-sprint-close-moves-old-event-logs` speaks of logs kept outside git and names no file, so it stands. `estimate-event-log-records` has no `purpose` field: a Grep of its page for `^purpose:` printed nothing, and this Case adds none.
>
> A Grep of `vault/wiki/` for `\.gitignore`, with `brief.md` and `log.md` left out, printed `rules/rule-clean-branch.md`, `rules/rule-guppi-package.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `estimates/estimate-clean-branch-writes-a-clean-copy.md`, `estimates/estimate-event-log-records.md`, `estimates/estimate-guppi-package-runs-from-its-own-folder.md` and `estimates/estimate-sprint-close-moves-old-event-logs.md`. `rule-clean-branch` and `estimate-clean-branch-writes-a-clean-copy` already name `vault/.gitignore`. `rule-guppi-package` and `estimate-guppi-package-runs-from-its-own-folder` speak of `.guppi/.gitignore`, and the hit in `estimate-clean-branch-ships-neutral-texts` is its Result. All of these stand. The same Grep of `.claude/` printed nothing. A Grep of `.guppi/` for `leaves the moved logs|event-log-records|sprint-close-moves`, with `.venv/` left out, printed only `.guppi/guppi/sprint_close.py`, so no test reads either Estimate page or that docstring. Frontier item C3 of this session lists the Criterion line of `estimate-sprint-close-moves-old-event-logs` among the sentences to rewrite. 917.1 rewrites it, and Case 918, which takes C3, leaves that Estimate out of its rewrite for this reason, in its finished file. Case 918 replaces the Criterion of four other Estimates and names neither Estimate of this Case. In their finished files, Case 913 changes `rule-close` and its report Estimate, Case 915 the ledger hook, `rule-orchestration`, `rule-case-build` and `rule-prespec-onward`, and Case 916 `rule-orchestration` and `rule-case-build`. None of them changes a page or a file of this Case.

> **problem:**
> Two shipped Estimates, and the docstring of the close code, name a bare `.gitignore`. The lines that ignore the event logs stand in `vault/.gitignore`. So a reader of the `method` of `estimate-sprint-close-moves-old-event-logs` opens the root `.gitignore` and finds no such line, in this repository and in a project that installed GUPPI.

> **recommend:**
> - **How the Estimate names the ignore file**
>   - Recommended: (a) replace the Criterion whole and set the method, both naming `vault/.gitignore`; read at the Retro of this session.
>   - Answer: agreed, (a).
> - **The docstring of the close code**
>   - Recommended: (a) name `vault/.gitignore` there too.
>   - Answer: agreed, (a).
> - **The event log Estimate with the same bare name**
>   - Recommended: (a) leave it out of this Case.
>   - Answer: (b), a sub-case replaces the Criterion of `estimate-event-log-records` with `vault/.gitignore`.
> - **When the event log check can be read**
>   - Recommended: (a) drop the two `/hi` readings by hand from the `method`, so that the pytest and the ignore and timing readings all run at the Retro of this session.
>   - Answer: agreed, (a).

### Case 917.1 — The close of a sprint names vault/.gitignore

> **given:**
> `estimate-sprint-close-moves-old-event-logs`: its Criterion is replaced whole and its `method` set.
> **＋** `.guppi/guppi/sprint_close.py`: the close; its module docstring names the ignore file.
> **＋** `.guppi/tests/test_sprint_close.py`: the tests of the close over a made-up vault.
> **＋** `.guppi/guppi/ledger.py`: `session_dir` and `session_event_logs`, which find the session of the run.
> **＋** `vault/.gitignore`: the lines that leave the event logs out of git.
> **＋** `vault/raw/<date>/event_log.md`: a daily event log, beside the session folders of `vault/raw/`.
> **＋** `vault/archive/<id>/<date>/event_log.md`: where an old log goes.
> **＋** `estimate-clean-branch-ships-neutral-texts`: constrains the `method` of a shipped Estimate.

> **when:**
> `uv run --project .guppi guppi sprint-close --sprint <id> --apply` of `.guppi/guppi/sprint_close.py` closes a sprint, in the librarian's run or in `.guppi/tests/test_sprint_close.py` over a made-up vault, and the session of the run is the stamp whose `hi` line `session_dir` of `.guppi/guppi/ledger.py` takes to the newest session folder of `vault/raw/`.

> **then:**
> After a close whose run of `guppi cleanup` exits 0, each `vault/raw/<date>/event_log.md` dated before the start date of the session of the run, the first date that `session_event_logs` of `.guppi/guppi/ledger.py` gives for its stamp, moves to `vault/archive/<id>/<date>/event_log.md`.
> **＋** A date folder that the moves leave empty is removed.
> **＋** `vault/.gitignore` leaves out each moved log, so git tracks none.
> **＋** Stdout holds one line per log moved.
> **－** The log of the start date and of each later date stays where it is, since the hooks of that session read them, the start date two or more days before the date of the session folder included.
> **－** With no session folder in `vault/raw/`, or with no stamp or more than one whose `hi` line `session_dir` takes to the newest session folder, no log moves, and stdout holds one line that says why.
> **－** A log whose target exists does not move: one line on stderr, and the close exits 1 after the other moves.
> **－** A refused close moves no log.

> **tasks:**
> - [ ] update `estimate-sprint-close-moves-old-event-logs`
>   - set: `{status: pending, method: "uv run --project .guppi pytest .guppi/tests/test_sprint_close.py -k event_log; the lines of vault/.gitignore read in the tree at Retro"}`
>   - change: `the Criterion replaced whole — the moved logs are left out of git by vault/.gitignore, and the method reads that file`
> - [ ] `.guppi/guppi/sprint_close.py`: the module docstring line `` `.gitignore` leaves the moved logs out of git. `` names `vault/.gitignore`.
> - [ ] read `estimate-sprint-close-moves-old-event-logs`

> **ratification:**
> ```
> - decision[case 917.1][update][estimate-sprint-close-moves-old-event-logs]{ref:rule-sprint-close}
> ```

### Case 917.2 — The event log check names vault/.gitignore

> **given:**
> `estimate-event-log-records`: its Criterion is replaced whole and its `method` set.
> **＋** `.guppi/guppi/event.py`: `guppi event`, which writes the event log.
> **＋** `.guppi/guppi/gate.py`: `guppi gate`, which reads the payload of a `Skill` call.
> **＋** `/hi`: the skill that opens a session, whose prompt the hook judges.
> **＋** `raw/<date>/event_log.md`: the daily event log.
> **＋** `vault/.gitignore`: the lines that leave the event logs out of git.
> **＋** `estimate-clean-branch-ships-neutral-texts`: constrains the texts of a shipped Estimate.

> **when:**
> A session starts, a tool call completes, the person submits a prompt, or the agent calls a skill through `Skill`; `uv run --project .guppi guppi event <name>` and `uv run --project .guppi guppi gate` read the JSON payload through a pipe, its `session_id` the stamp.

> **then:**
> After the start and one tool call, `raw/<date>/event_log.md` carries a `session-start` line with the session's stamp and a `tool` line after it.
> **＋** On `/hi` whose `permission_mode` is `plan`, when no `hi` of this stamp follows its first `session-start`: the line `- HH:MM:SS <stamp> hi` and its `hi:` line on stdout, which names the session's folder; a second `/hi` writes nothing and prints `hi: already recorded`, with the time and the folder; exit 0.
> **＋** On `/hi` whose `permission_mode` is any other value — `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions` — or is missing or empty, a second `/hi` included: no line, nothing on stdout, exit 2 with a reason on stderr that tells the person to turn plan mode on and type `/hi` again; Claude Code blocks the prompt, and the skill does not run.
> **＋** Any other prompt is silent, and its `permission_mode` is not read: exit 0; an error goes to stderr only, exit 0.
> **＋** A call of `pre-spec`, `retro` or `handoff` through `Skill` that the gate lets through appends `- HH:MM:SS <stamp> <mark>` — `prespec`, `retro`, `handoff` — in the form `guppi event` writes; a refusal writes no line; `hi` and other skills get no mark.
> **＋** `git check-ignore` reports the log ignored by `vault/.gitignore`; a hook invocation with piped stdin that refuses nothing exits 0 and finishes under 2 s.

> **tasks:**
> - [ ] update `estimate-event-log-records`
>   - set: `{status: pending, method: "pytest in .guppi/tests/test_event.py and .guppi/tests/test_gate.py with piped JSON payloads against a temp vault; by hand at Retro, git check-ignore on the event log of the day and one hook run through a pipe, timed, both written into the estimate line"}`
>   - change: `the Criterion replaced whole — git check-ignore reports the log ignored by vault/.gitignore; the method drops the /hi readings by hand`
> - [ ] read `estimate-event-log-records`

> **ratification:**
> ```
> - decision[case 917.2][update][estimate-event-log-records]{ref:rule-event-log}
> ```
