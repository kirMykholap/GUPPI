## Case 743 — The close of a sprint empties raw/, and two skills lead the close and the opening

> **context:**
> Today the close of a sprint is the command `guppi sprint-close` of `guppi/sprint_close.py`, run by the librarian from the task line of the closing Case. It moves the finished pages of the sprint to the archive and leaves `vault/raw/` alone. The daily step `guppi archive` of `guppi/archive.py` moves only the finished sessions of earlier days, so every session of the closing day, the closing session included, stays in `raw/`. When such a session leaves later, it goes to the folder named by the first heading of `vault/wiki/sprint.md`, which by then names the next sprint. One `event_log.md` per date stays in `raw/` for good. After the close, `guppi sprint` finds no sprint page, stops with an error and leaves `sprint.md` naming the closed sprint. `backlog.md` keeps every line of the Backlog of a closed sprint for good, since nothing changes an archived page. Nothing sets what the Case that opens the next sprint asks. The steps of the closing session stand in a paragraph of `orchestration.md`, which every session loads.
>
> The person wants all of `raw/` to go to the archive at the close, and chose this. The close also moves each finished session of `raw/`, whatever its day (743.1). A session goes to the archive folder of the sprint its own `materialize.yaml` records (743.2). The close moves the event logs that no open session reads, and git still leaves them out (743.3). Three things stay in `raw/` because something still writes or reads them there: the closing session, where Retro writes after the librarian's commit; a session not yet turned into pages; and a conserved Spec, which `backlog.md` and `/box` find only in `raw/`. The opening of a sprint does not go through the old Backlog. It says how many items `backlog.md` holds and asks whether to take any. A line of a closed sprint's Backlog leaves `backlog.md` once the live sprint takes it or its pages are finished (743.4). After the close, `guppi sprint` writes `sprint.md` with the closed sprint marked, for example `## migration — closed`, instead of failing (743.5). The person first chose a key in `guppi.toml`, then replaced that choice with `sprint.md`. A render of `guppi.toml` from the sprint page would break `estimate-guppi-config-fills-the-languages` and `estimate-render-harness-reproduces`, which promise that a rendered file is the text of its page. Two skills replace the paragraph of `orchestration.md`, so that the rare text loads only in the rare sessions. `/sprint-open` asks the opening questions (743.6), and a `UserPromptSubmit` hook on `/hi` tells the agent to start it when `sprint.md` marks the sprint closed (743.7). `/sprint-close` starts when the person takes up the close line of the sprint, which the opening writes in a fixed form. It refuses in a session that already ratified another Case, puts off the other Cases lines, sorts the readings and has the closing Case built (743.8).
>
> The vault's answer: the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` names no rule of a skill for the turn of a sprint. `rule-sprint-close` stands `draft`, deferred by `decision-case-718`, and 743.1 carries the mark that retires that defer. The Glob `vault/**/*{sweeps-raw,files-a-session,moves-old,marks-a-closed,opening-questions,starts-at-hi,leads-the-closing,rule-skill-sprint}*` printed nothing, so the new slugs are free. The Grep `no live sprint page|missing sprint page|finds no live sprint page` over `vault/wiki/`, `.claude/` and `guppi/` printed `.claude/agents/librarian-guppi.md`, `vault/wiki/orchestration.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-documentation.md`, `vault/wiki/rules/rule-ledger-write.md`, `vault/wiki/estimates/estimate-sprint-close-next-session-opens-the-sprint.md`, `vault/wiki/estimates/estimate-ledger-write-holds-a-decision-line-off-the-stored-case.md`, `vault/wiki/log.md` and `guppi/ledger.py`. 743.5 changes the sentence of the librarian's frame in `rule-documentation`, and 743.8 removes the paragraph of `rule-orchestration`. The hits in `guppi/ledger.py` and `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` speak of the ledger hook, which judges the sprint by the live page and not by `sprint.md`, so they stand. The hit in `rule-ledger-write` is a History line. I did not read `log.md`. In `estimate-sprint-close-next-session-opens-the-sprint`, the exception that the error of `guppi sprint` in the closing run is a flag names an error that no longer comes. It stands, since it fails nothing, and its reading waits for the session after the close.
>
> The frame: `estimate-raw-archive` stands. Its Criterion covers `guppi archive` alone: it limits that command to earlier days, keeps `event_log.md` in `raw/` under it, and names no source of `<sprint>`. The sentence of `rule-sprint` that `sprint_id`, `cleanup` and `archive` read the first heading stands: the closed heading keeps the id as its first word, and the archive falls back to it. `guppi cleanup` still files pages by that heading, and this Case does not change it. `estimate-backlog-renders` and `estimate-sprint-checks-the-file` speak of what changes, so 743.4 and 743.9 replace their Criteria and set their `method` to a test of this session. 743.9 drops the old exception that no sprint page is an error of the check, since the check now compares the closed form, and it stands apart from 743.5 because the check is a promise of its own. The Criteria of `estimate-sprint-close-takes-the-readings-in-groups` and `estimate-sprint-close-runs-in-the-librarian-run` stand: the skill keeps the behaviour that the paragraph of `orchestration.md` set. The other Estimates of `rule-sprint-close` speak of the pages the close moves, which do not change. No test reads a live file of `vault/` or `.claude/` through the code this Case changes. `rule-skill-sprint-open` hangs under `rule-session-start` and `rule-skill-sprint-close` under `rule-plan-mode`, as the other skill rules hang under a phase, since a child of `rule-session` would break `estimate-session-phases-in-order`. The start of `/sprint-close` puts off the other items by short-form defers, so 743.8 adds it as a third moment of the short form in `rule-orchestration`. The close keeps a conserved Spec by `is_carried_over` of `guppi/materialize.py`, the judgment `guppi sprint` and `guppi/box.py` already use. `estimate-sprint-ticks-the-spec` stands: its When, a run that wrote the file and exits 0, holds for the closed form, so that run ticks as any other (743.5). Two Estimates of `entity-sprint-migration` keep a reason that the change makes out of date, and they stand. `estimate-sprint-migration-leftovers-gone` says that a past `event_log.md` stays in `raw/` as `rule-raw-archive` keeps it. That still holds at its reading, which comes before the close; the page now adds that the close moves the log afterwards. `estimate-sprint-migration-merges` calls the merge into `main` a line of the Backlog, which 743.8 removes. Neither exception fails anything. Replacing their Criteria needs a `method` that runs in this session, while both are read by their `method` in the session that closes the sprint, as the Definition of done of `migration` (case 628.9). A Case of that session or a later one may correct them. Not done: the close of `migration` itself, which is a session of its own (case 628.9). A skill's behaviour is read in this session from its Render in the Spec, and the first live run is the next close.

> **problem:**
> The close of a sprint leaves `raw/` full and files late sessions under the wrong sprint. It leaves `sprint.md` naming a closed sprint, and it keeps old Backlog lines in `backlog.md` for good. Nothing sets what the opening of the next sprint asks. The steps of the closing session load in every session.

> **recommend:**
> - **What leaves raw/ at the close**
>   - Recommended: (b) the close sweeps every session whose ledger is fully turned into pages, whatever its day; the closing session, an unfinished session and a conserved Spec stay until they can leave.
>   - Answer: agreed, (b).
> - **Which sprint folder a late session goes to**
>   - Recommended: (b) by the sprint the session's own yaml records, `sprint.md` as the fallback.
>   - Answer: agreed, (b).
> - **The old event logs**
>   - Recommended: (b) the close moves the logs of the earlier dates into the archive, still outside git.
>   - Answer: agreed, (b).
> - **The Backlog of the closed sprint**
>   - Recommended: (b) the opening Case lists each line of the old Backlog, and the person moves or drops each one.
>   - Answer: not each line. The opening of a sprint says that the backlog has entries and asks the person whether to take any of them, without going through them all.
> - **What the opening Case of the next sprint asks**
>   - Recommended: (b) a fixed list: the sprint id, its goal in one sentence, its Definition of done as Estimates, the first milestone and its items, and each line of the old Backlog.
>   - Answer: (b), with the backlog question changed to match the answer on the Backlog.
> - **When a line of the old Backlog leaves backlog.md**
>   - Recommended: (b) a line leaves once the live sprint page names its page or its text, or its page is finished.
>   - Answer: agreed, (b).
> - **Where the questions of the opening Case are written down**
>   - Recommended: (a) in `orchestration.md`, beside the paragraph on the closing session.
>   - Answer: in a separate skill, since `orchestration.md` is read in every session, and the close and the opening of a sprint are rare.
> - **What the new skill holds**
>   - Recommended: (b) one skill, for example `/sprint`, for the whole turn of a sprint; the paragraph on the closing session moves out of `orchestration.md`.
>   - Answer: agreed on the content, but as two skills, `/sprint-close` and `/sprint-open`. The person asked whether `/sprint-close` runs in Plan Mode or after it and leads up to the librarian, and asked that `/sprint-open` load by itself at `/hi` when no sprint is active, read from a variable.
> - **How the skill starts**
>   - Recommended: (b) the main agent starts it at those two moments, and the person may type it too.
>   - Answer: agreed, (b).
> - **Where the active sprint is recorded**
>   - Recommended: (a) a key `sprint` in `guppi.toml`, written by `guppi render` from the live sprint page.
>   - Answer: agreed, (a); replaced by the question on where the active sprint is written.
> - **How `/hi` starts `/sprint-open`**
>   - Recommended: (a) `/hi` reads the key and starts the skill when it is missing.
>   - Answer: (b), a hook on `/hi`.
> - **When `/sprint-close` runs and how far it goes**
>   - Recommended: (a) from `/hi` to the end of Work Mode; it reaches the librarian through the close line of the Spec.
>   - Answer: agreed, (a). The person asked how the skill starts when the close item is picked on the Frontier, what happens to the other items, and asked that the opening of a sprint add the close item at once as the last item of its last milestone.
> - **How the agent knows to start `/sprint-close`**
>   - Recommended: (a) the opening Case writes the close line in a fixed form that names `/sprint-close`, and picking it starts the skill.
>   - Answer: agreed, (a).
> - **What happens to the rest of the Frontier**
>   - Recommended: (a) the skill puts off every other Cases line at once; the Work and Ask lines stay open.
>   - Answer: agreed, (a).
> - **When the session has already ratified another Case**
>   - Recommended: (a) the skill refuses and puts the close off for a session of its own.
>   - Answer: agreed, (a).
> - **Where the active sprint is written**
>   - Recommended: (b) in `sprint.md`: after the close `guppi sprint` writes the heading of the closed sprint marked closed, and the hook on `/hi` reads it.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: at `/pre-spec`, the person chose that the merge of `migration` into `main` moves into `/sprint-close`: the closing session gives the merge to the next session as a Work line, and `/sprint-open` stays as decided.
>   - Taken: the closing Case of `/sprint-close` holds a task line for the merge, which Work Mode leaves unticked so that the brief gives it as Work to the session that opens the next sprint; the merge line leaves the Backlog of `entity-sprint-migration` (743.8).
> - **Change**
>   - Asked: at `/pre-spec`, the person chose that 743.9 also rewrites the `purpose` of `estimate-sprint-checks-the-file`, so that it covers both the render of the live page and the closed form.
>   - Taken: the `set` of `estimate-sprint-checks-the-file` in 743.9 writes a new `purpose` that names both.

### Case 743.1 — The close sweeps the finished sessions out of `raw/`

> **given:**
> `rule-sprint-close`: the rule of the close, whose Purpose names what the close moves.
> **＋** `guppi/sprint_close.py`: the command `guppi sprint-close`.
> **＋** `guppi/archive.py`: the judgment of a done unit of `vault/raw/` and its move.
> **＋** `tests/test_sprint_close.py`: the tests of the close.
> **＋** `rule-raw-archive`: the rule of the archive of `vault/raw/`, which names the close.
> **＋** `vault/archive/`: the archive the units move to.
> **＋** `guppi/materialize.py`: `is_carried_over`, the one judgment of a conserved Spec.
> **＋** `estimate-sprint-close-sweeps-raw`: the new check of the sweep.

> **when:**
> `uv run guppi sprint-close --sprint <id>` of `guppi/sprint_close.py` previews or closes a sprint, in the librarian's run or in `tests/test_sprint_close.py` over a made-up vault.

> **then:**
> After a close whose run of `guppi cleanup` exits 0, each unit of `vault/raw/` that `guppi/archive.py` judges done moves to `vault/archive/` by the move of `guppi archive`, whatever its date.
> **＋** Stdout holds one line per unit, moved or kept with its reason, in the form of `guppi archive`.
> **＋** The preview without `--apply` names each unit the close would move, and moves none.
> **－** The session of the run does not move.
> **－** A unit with no yaml, an entry not applied or a ledger line outside the yaml stays in `vault/raw/`.
> **－** A unit whose folder holds `carry.md`, judged by `is_carried_over` of `guppi/materialize.py`, stays in `vault/raw/` with the reason `carried over`.
> **－** A refused close moves no unit.

> **tasks:**
> - [ ] update `rule-sprint-close`
>   - old: `the sprint page and its Estimates of every past sprint stay among the pages that each search of the vault reads (cases 612, 627.1, 632.1).`
>   - new: `` the sprint page and its Estimates of every past sprint stay among the pages that each search of the vault reads (cases 612, 627.1, 632.1). The close also moves to the archive each session of `vault/raw/` whose ledger is fully turned into pages, whatever its day (case 743.1). ``
>   - change: `the close moves every finished session of raw/ to the archive, whatever its day; the defer of case 718 taken up (case 743.1)`
> - [ ] update `rule-raw-archive`
>   - old: `The session of the run is never looked at.`
>   - new: `` The session of the run is never looked at. At the close of a sprint, `guppi sprint-close` moves each done unit the same way whatever its date, the session of the run still left out (`rule-sprint-close`, case 743.1). ``
>   - change: `the close of a sprint moves each done unit whatever its date (case 743.1)`
> - [ ] create `estimate-sprint-close-sweeps-raw`
>   - ref: `rule-sprint-close`
>   - kind: `QA`
>   - purpose: `Whether the close of a sprint moves each finished session of raw/ to the archive whatever its date, and leaves the session of the run, an unfinished unit and a conserved Spec in raw/`
>   - method: `uv run pytest tests/test_sprint_close.py -k sweep`
>   - tags: `[sprint, workflow, librarian]`
> - [ ] `guppi/archive.py`: the walk over the units takes a flag that drops the limit of the date; the run of `guppi archive` keeps the limit; the docstring says so.
> - [ ] `guppi/sprint_close.py`: after `guppi cleanup` exits 0, the run moves the done units by that walk with the flag and prints its lines; the preview names the units it would move; the docstring says so.
> - [ ] `guppi/archive.py`: with the flag of the close, the walk keeps a unit that `is_carried_over` of `guppi/materialize.py` judges carried over, imported and not copied, with the reason `carried over`; the run of `guppi archive` without the flag keeps its reasons.
> - [ ] `tests/test_sprint_close.py`: tests named `sweep` — a done unit of the run day moves; the session of the run, a unit with an entry not applied and a unit with `carry.md` stay; a refused close and the preview move none.
> - [ ] read `estimate-sprint-close-sweeps-raw`

> **ratification:**
> ```
> - decision[case 743.1][update][rule-sprint-close]{ref:rule-sprint-close}{supersedes:case 718}
> - decision[case 743.1][update][rule-raw-archive]{ref:rule-raw-archive}
> - decision[case 743.1][create][estimate-sprint-close-sweeps-raw]{ref:rule-sprint-close}{tags:sprint,workflow,librarian}
> ```

### Case 743.2 — A session goes to the archive folder of its own sprint

> **given:**
> `rule-raw-archive`: the rule of the archive of `vault/raw/`.
> **＋** `guppi/archive.py`: the move of a done unit.
> **＋** `tests/test_archive.py`: the tests of the archive.
> **＋** `guppi/sprint_close.py`: the close of a sprint, which moves units by the same move.
> **＋** `vault/archive/<sprint>/`: the folder of a sprint in the archive.
> **＋** `vault/wiki/sprint.md`: the file whose first heading names the sprint as the fallback.
> **＋** `estimate-raw-archive-files-a-session-by-its-sprint`: the new check of the folder a unit goes to.

> **when:**
> `uv run guppi archive`, or the close of a sprint by `guppi/sprint_close.py`, moves a done unit of `vault/raw/` by the move of `guppi/archive.py`, or `tests/test_archive.py` runs that move over a made-up vault.

> **then:**
> The unit goes under `vault/archive/<sprint>/`, `<sprint>` being the value of the `sprint` field of its own `materialize.yaml`.
> **＋** A unit whose yaml holds no `sprint` field takes the first `## <id>` heading of `vault/wiki/sprint.md`, as before.
> **＋** The stdout line of the unit names the folder it went to.

> **tasks:**
> - [ ] update `rule-raw-archive`
>   - old: `` `<sprint>` is the first `## <id>` heading of `sprint.md`. ``
>   - new: `` `<sprint>` is the `sprint` field of the unit's own `materialize.yaml`, so a session that leaves after the next sprint opened goes to the folder of its own sprint; a unit whose yaml holds none takes the first `## <id>` heading of `sprint.md` (case 743.2). ``
>   - change: `a unit goes to the archive folder of the sprint its own yaml records (case 743.2)`
> - [ ] create `estimate-raw-archive-files-a-session-by-its-sprint`
>   - ref: `rule-raw-archive`
>   - kind: `QA`
>   - purpose: `Whether a done unit of raw/ goes to the archive folder of the sprint its own materialize.yaml records, and to the sprint of sprint.md only when its yaml records none`
>   - method: `uv run pytest tests/test_archive.py -k sprint`
>   - tags: `[harness, librarian, sprint]`
> - [ ] `guppi/archive.py`: the move takes the sprint from the unit's yaml, `sprint_id` as the fallback; the docstring says so.
> - [ ] `tests/test_archive.py`: tests named `sprint` — a unit whose yaml holds `sprint: a` goes under `vault/archive/a/` while `sprint.md` names `b`; a unit whose yaml holds no `sprint` goes under `b`.
> - [ ] read `estimate-raw-archive-files-a-session-by-its-sprint`

> **ratification:**
> ```
> - decision[case 743.2][update][rule-raw-archive]{ref:rule-raw-archive}
> - decision[case 743.2][create][estimate-raw-archive-files-a-session-by-its-sprint]{ref:rule-raw-archive}{tags:harness,librarian,sprint}
> ```

### Case 743.3 — The close moves the old event logs to the archive

> **given:**
> `rule-sprint-close`: the rule of the close.
> **＋** `guppi/sprint_close.py`: the command `guppi sprint-close`.
> **＋** `tests/test_sprint_close.py`: the tests of the close.
> **＋** `.gitignore`: the files git leaves out.
> **＋** `rule-raw-archive`: the rule that names where `event_log.md` stays.
> **＋** `vault/raw/<date>/event_log.md`: the event log of a date.
> **＋** `vault/archive/<id>/<date>/event_log.md`: the place of a moved log.
> **＋** `estimate-sprint-close-moves-old-event-logs`: the new check of the move of the logs.

> **when:**
> `uv run guppi sprint-close --sprint <id> --apply` of `guppi/sprint_close.py` closes a sprint, in the librarian's run or in `tests/test_sprint_close.py` over a made-up vault.

> **then:**
> After a close whose run of `guppi cleanup` exits 0, each `vault/raw/<date>/event_log.md` dated before the day before the date of the session of the run moves to `vault/archive/<id>/<date>/event_log.md`.
> **＋** A date folder that the moves leave empty is removed.
> **＋** `.gitignore` leaves out each moved log, so git tracks none.
> **＋** Stdout holds one line per log moved.
> **－** The log of the date of the session of the run, of each later date and of the day before it stays where it is, since the hooks of that session read them.
> **－** A log whose target exists does not move: one line on stderr, and the close exits 1 after the other moves.
> **－** A refused close moves no log.

> **tasks:**
> - [ ] update `rule-sprint-close`
>   - old: `whatever its day (case 743.1).`
>   - new: `whatever its day (case 743.1), and the event logs that the hooks of the open session no longer read, which git still leaves out there (case 743.3).`
>   - change: `the close moves the old event logs to the archive (case 743.3)`
> - [ ] update `rule-raw-archive`
>   - old: `` `event_log.md` stays in `vault/raw/<date>/`: it is gitignored and the ledger hook walks it for the `hi` window. ``
>   - new: `` `event_log.md` stays in `vault/raw/<date>/`: it is gitignored and the ledger hook walks it for the `hi` window. The close of a sprint moves each log dated before the day before the session of its run to `vault/archive/<id>/<date>/`, `<id>` the sprint it closes, still gitignored (`rule-sprint-close`, case 743.3). ``
>   - change: `the close of a sprint moves the old event logs (case 743.3)`
> - [ ] create `estimate-sprint-close-moves-old-event-logs`
>   - ref: `rule-sprint-close`
>   - kind: `QA`
>   - purpose: `Whether the close of a sprint moves the event logs that the open session no longer reads to the archive, outside git, and keeps the logs that session reads in raw/`
>   - method: `uv run pytest tests/test_sprint_close.py -k event_log; the line of .gitignore read in the tree at Retro`
>   - tags: `[sprint, workflow, librarian]`
> - [ ] `.gitignore`: the line `vault/archive/*/*/event_log.md` under the line of the event log.
> - [ ] `guppi/sprint_close.py`: after the sweep of 743.1, the run moves the old logs and removes the date folders left empty; the docstring says so.
> - [ ] `tests/test_sprint_close.py`: tests named `event_log` — an old log moves and its empty folder goes; the logs of the day before, of the session's date and of a later date stay; a taken target is one stderr line and exit 1; a refused close moves none.
> - [ ] read `estimate-sprint-close-moves-old-event-logs`

> **ratification:**
> ```
> - decision[case 743.3][update][rule-sprint-close]{ref:rule-sprint-close}
> - decision[case 743.3][update][rule-raw-archive]{ref:rule-raw-archive}
> - decision[case 743.3][create][estimate-sprint-close-moves-old-event-logs]{ref:rule-sprint-close}{tags:sprint,workflow,librarian}
> ```

### Case 743.4 — `backlog.md` drops a line of a closed sprint once it is taken or finished

> **given:**
> `rule-backlog`: the rule of `vault/wiki/backlog.md`.
> **＋** `guppi/backlog.py`: the script that writes the file.
> **＋** `guppi/sprint.py`: the item reader and the statuses that tick an item.
> **＋** `tests/test_backlog.py`: the tests of the script.
> **＋** `guppi/materialize.py`: the Spec reader of a conserved Spec.
> **＋** `entity-sprint-<id>`: a sprint page, live under `vault/wiki/entities/` or archived under `vault/archive/`.
> **＋** `vault/raw/`: the sessions the script reads for conserved Specs and Frontiers.
> **＋** `estimate-backlog-renders`: its Criterion is replaced whole.

> **when:**
> `uv run guppi backlog` runs over `vault/wiki/`, `vault/raw/` and `vault/archive/`. The librarian runs it after `guppi sprint`, and the skill `carry` runs it after it writes `carry.md`.
> **＋** Or `tests/test_backlog.py` runs `guppi/backlog.py` over a made-up vault.

> **then:**
> The script writes `vault/wiki/backlog.md`: the heading `# Backlog`, the line `N items`, then `## Conserved Specs` and `## Deferred`.
> **＋** `## Conserved Specs` holds each session folder under `vault/raw/` that holds `carry.md`. Each has one line that names its `spec.md` and its Cases. Under that line stands one line per item of its `then` blocks, with the kind and the slug, read by the Spec reader of `guppi/materialize.py`.
> **＋** `## Deferred` holds one line per item. The items are each live page with a `deferred_by` that is not empty, each Insight whose `status` is `open`, and each line of the `## Backlog` of each `entity-sprint-<id>`, live under `vault/wiki/entities/` or archived under `vault/archive/`. A line holds the slug, the page's `purpose` (for an Insight, its `pattern` and `severity`) and the count. A Backlog line that names no page stands by its text.
> **＋** The count of an item is the number of sessions whose `frontier.md`, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names its slug in a code span of its title. It is read by `generate.frontier_marks`, and `guppi/backlog.py` holds no copy of that reader.
> **＋** `N` counts the conserved Specs and the lines of `## Deferred`. A slug that stands under a conserved Spec does not stand again under `## Deferred`, and a slug of two sources stands once.
> **＋** A folder whose `carry.md` is gone shows nothing. Its defers enter `## Deferred` through `deferred_by` once `materialize` and `generate` have applied them.
> **－** A slug of a line of the `## Backlog` of an archived sprint page does not stand when the live sprint page names it in its `## Milestones` or its `## Backlog`, or when its page stands `built`, `passed` or `archived`, the statuses that tick an item in `guppi/sprint.py`.
> **－** A line of the `## Backlog` of an archived sprint page that names no page does not stand when the live sprint page holds a line of the same text.
> **－** The script writes no page of `vault/wiki/` and no file but `vault/wiki/backlog.md`. The governed-files hook refuses a hand edit of that file.

> **tasks:**
> - [ ] update `rule-backlog`
>   - old: `` so that the Backlog of a closed sprint stays in the list (`rule-sprint-close`, case 628.12) ``
>   - new: `` so that the Backlog of a closed sprint stays in the list (`rule-sprint-close`, case 628.12), but for a line the live sprint page takes into its `## Milestones` or its `## Backlog` and a line whose pages are all `built`, `passed` or `archived` (case 743.4) ``
>   - old: `` a line leaves the sprint page's `## Backlog`, ``
>   - new: `` a line leaves the sprint page's `## Backlog`, a line of a closed sprint is taken by the live sprint or its pages are finished, ``
>   - change: `a line of the Backlog of a closed sprint leaves backlog.md once the live sprint takes it or its pages are finished (case 743.4)`
> - [ ] update `estimate-backlog-renders`
>   - set:
>     ```
>     status: pending
>     purpose: "guppi backlog writes backlog.md from the conserved Specs, the pages with deferred_by, the open Insights and the Backlog of each sprint page, live or archived, a line of a closed sprint left out once the live sprint takes it or its pages are finished, each item with its purpose and its count"
>     method: uv run pytest tests/test_backlog.py
>     ```
>   - change: `the Criterion replaced whole — a line of a closed sprint leaves once taken or finished; the method a test of the session (case 743.4)`
> - [ ] `guppi/backlog.py`: an item of an archived sprint page is left out as the `then` sets it, by `item_slugs` and `DONE` of `guppi/sprint.py`, imported; the docstring says so.
> - [ ] `tests/test_backlog.py`: an archived line whose slug the live page names in a milestone, an archived line whose page is `built`, and an archived note whose text the live Backlog holds are left out; an archived line taken by nothing stays.
> - [ ] `uv run guppi backlog`
> - [ ] read `estimate-backlog-renders`

> **ratification:**
> ```
> - decision[case 743.4][update][rule-backlog]{ref:rule-backlog}
> - decision[case 743.4][update][estimate-backlog-renders]{ref:rule-backlog}
> ```

### Case 743.5 — `sprint.md` marks a closed sprint

> **given:**
> `rule-sprint`: the rule of `vault/wiki/sprint.md`.
> **＋** `guppi/sprint.py`: the script that writes the file.
> **＋** `guppi/materialize.py`: `sprint_id`, the reader of the heading.
> **＋** `tests/test_sprint.py`: the tests of the script.
> **＋** `estimate-sprint-marks-a-closed-sprint`: the new check of the closed mark.
> **＋** `rule-documentation`: the librarian's frame, which names the error of `guppi sprint` after a close.
> **＋** `rule-skill-sprint-open`: the rule whose hook reads the mark.
> **＋** `estimate-sprint-ticks-the-spec`: the check of the ticks of a run that wrote the file.

> **when:**
> `uv run guppi sprint` of `guppi/sprint.py` runs while no live sprint page stands, in the librarian's run after a close or in `tests/test_sprint.py` over a made-up vault.

> **then:**
> `guppi sprint` writes `vault/wiki/sprint.md` as `# Sprint`, the heading `## <id> — closed` and the line `No sprint is open since the close of <id>.`, and exits 0.
> **＋** `<id>` is the id that the first `## ` heading of the file named before, read by `sprint_id` of `guppi/materialize.py`, and a file already marked closed keeps its id.
> **＋** `sprint_id` reads `<id>` from the closed heading, as from any heading.
> **＋** One function of `guppi/sprint.py` writes the mark and judges a heading closed, and the hook of `rule-skill-sprint-open` imports it.
> **＋** The run that writes the closed form is a run that wrote the file and exits 0, so it ticks the task lines of the Specs as `estimate-sprint-ticks-the-spec` sets it.
> **－** With no live sprint page and no `vault/wiki/sprint.md`, the script prints one line on stderr and exits 1, and writes nothing.
> **tasks:**
> - [ ] update `rule-sprint`
>   - old: `` The first `## <id>` heading of the file is the sprint id `sprint_id`, `cleanup` and `archive` read, unchanged. ``
>   - new: `` The first `## <id>` heading of the file is the sprint id `sprint_id`, `cleanup` and `archive` read, unchanged. With no live sprint page, after the close of a sprint, the script writes the file as `# Sprint`, the heading `## <id> — closed` and one line that no sprint is open since the close of `<id>`, the id the file named before, and exits 0; `sprint_id` reads `<id>` from it, and the hook of `rule-skill-sprint-open` reads the mark (case 743.5). ``
>   - change: `with no live sprint page, guppi sprint writes sprint.md with the closed sprint marked, and exits 0 (case 743.5)`
> - [ ] update `rule-documentation`
>   - old: `` After a close, `guppi sprint` in step 5 finds no live sprint page; its error is a flag. ``
>   - new: `` After a close, `guppi sprint` in step 5 finds no live sprint page and writes `vault/wiki/sprint.md` with the closed sprint marked (`rule-sprint`, case 743.5). ``
>   - change: `after a close guppi sprint marks the sprint closed instead of failing (case 743.5)`
> - [ ] create `estimate-sprint-marks-a-closed-sprint`
>   - ref: `rule-sprint`
>   - kind: `QA`
>   - purpose: `Whether guppi sprint, with no live sprint page, writes sprint.md with the closed sprint marked and exits 0`
>   - method: `uv run pytest tests/test_sprint.py -k closed`
>   - tags: `[harness, sprint]`
> - [ ] `guppi/sprint.py`: with no live sprint page, `run` writes the closed form by one function that also judges a heading closed; the docstring says so.
> - [ ] `tests/test_sprint.py`: tests named `closed` — the closed form written with the id of the earlier file and exit 0; a closed file keeps its id; no page and no file is exit 1 and ticks nothing; the closed run ticks the `guppi sprint` line of an applied Spec; `sprint_id` reads the id from the closed heading.
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-sprint-marks-a-closed-sprint`

> **ratification:**
> ```
> - decision[case 743.5][update][rule-sprint]{ref:rule-sprint}
> - decision[case 743.5][update][rule-documentation]{ref:rule-documentation}
> - decision[case 743.5][create][estimate-sprint-marks-a-closed-sprint]{ref:rule-sprint}{tags:harness,sprint}
> ```

### Case 743.9 — `sprint --check` compares the closed form

> **given:**
> `estimate-sprint-checks-the-file`: its Criterion is replaced whole.
> **＋** `guppi/sprint.py`: the script and its check.
> **＋** `tests/test_sprint.py`: the tests of the script.
> **＋** `vault/wiki/sprint.md`: the file the check compares.
> **＋** `Makefile`: its target `lint` runs the check.
> **＋** `estimate-sprint-marks-a-closed-sprint`: the check of the closed form.

> **when:**
> Someone runs `uv run guppi sprint --check`, by hand or through the target `lint` of the `Makefile`, and it renders the file from the sprint page in memory.

> **then:**
> When `vault/wiki/sprint.md` differs from the render of the page, stdout holds one line `sprint: <file> differs from entity-sprint-<id>`, the file named by its path from the project root, and the check exits 1. When the file equals the render, the check exits 0 with no output. The file is written in neither case.
> **＋** The target `lint` of the `Makefile` runs it after `render --check` and before `guppi lint`.
> **＋** With no live sprint page, the check compares the file with the closed form that `estimate-sprint-marks-a-closed-sprint` sets, and the line on stdout reads `sprint: <file> differs from the closed form of <id>`.
> **－** A render error, such as two sprint pages, a slug with no page, or no sprint page and no file, is one line on stderr and exit 1, as with `guppi sprint`.

> **tasks:**
> - [ ] update `estimate-sprint-checks-the-file`
>   - set:
>     ```
>     status: pending
>     purpose: "sprint --check names sprint.md when it differs from the render of the live sprint page, or from the closed form when no live sprint page stands, exit 1, and writes nothing"
>     method: uv run pytest tests/test_sprint.py
>     ```
>   - change: `the Criterion replaced whole — with no live sprint page the check compares the closed form; the purpose covers both; the method a test of the session (case 743.9)`
> - [ ] `guppi/sprint.py`: `--check` with no live sprint page compares the file with the closed form and names it so in its line.
> - [ ] `tests/test_sprint.py`: `--check` is silent with exit 0 on a closed file that matches, and names the file with exit 1 on one that differs.
> - [ ] read `estimate-sprint-checks-the-file`

> **ratification:**
> ```
> - decision[case 743.9][update][estimate-sprint-checks-the-file]{ref:rule-sprint}
> ```

### Case 743.6 — `/sprint-open` asks the questions that open a sprint

> **given:**
> `rule-skill-sprint-open`: the new rule whose Render is the skill `/sprint-open`.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the skill rendered from it.
> **＋** `estimate-skill-sprint-open-asks-the-opening-questions`: the new check of what the skill has the opening Case ask.
> **＋** `rule-skill-hi`: `/hi`, whose Frontier puts the line that opens the next sprint first.
> **＋** `vault/wiki/backlog.md`: the list of the items put off, which the opening Case counts.
> **＋** `vault/wiki/sprint.md`: the file whose heading marks the last sprint closed.
> **＋** `/sprint-close`: the skill that the close line names.

> **when:**
> The main agent starts the skill `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, in a session whose `vault/wiki/sprint.md` marks the last sprint closed.

> **then:**
> The main agent assembles the Frontier as `rule-skill-hi` sets it, the line `open the next sprint` first under `## Cases`.
> **＋** When the person takes up that line, the main agent dispatches `case-guppi` with the questions of the opening in the prompt of the call: the id of the sprint, its goal in one sentence, its Definition of done as Estimates, and the first milestone and its items.
> **＋** The prompt asks that the opening Case say how many items `vault/wiki/backlog.md` holds and ask the person whether to take any of them.
> **＋** The prompt asks that the opening Case write, as the last item of the last milestone of the new sprint page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``.
> **＋** The opening Case is the first Case the session ratifies.
> **－** The opening Case goes through no item of `vault/wiki/backlog.md` that the person does not name.
> **－** The skill decides none of the answers: `case-guppi` puts each to the person in a round.

> **tasks:**
> - [ ] create `rule-skill-sprint-open`
>   - ref: `rule-session-start`
>   - kind: `Leaf`
>   - purpose: `Prevents the next sprint from opening without a goal, a Definition of done, a first milestone, its close line and a look at the backlog, while the text that asks for them stays out of the sessions that open no sprint`
>   - enforcement: `render`
>   - governs: `.claude/skills/sprint-open/SKILL.md`
>   - render_mode: `full`
>   - implementation_ref: `[guppi/sprint.py, tests/test_sprint.py, .claude/settings.json]`
>   - tags: `[sprint, workflow, harness]`
>   - sections.Purpose:
>     ```
>     Prevents the next sprint from opening without a goal, a Definition of done, a first milestone, its close line and a look at the backlog, while the text that asks for them stays out of the sessions that open no sprint. Until case 743 nothing set what the opening Case asks, and the steps of the turn of a sprint stood in `orchestration.md`, which every session loads. The skill loads only in the session that opens a sprint: the `UserPromptSubmit` hook `guppi sprint --hi` tells the agent at `/hi` to start it when `vault/wiki/sprint.md` marks the last sprint closed ([[rule-sprint]], case 743.5), and the person may type it too. The backlog is not gone through: the opening Case says how many items it holds and asks whether to take any (case 743.6). The close line it writes starts [[rule-skill-sprint-close]] in the session that closes the sprint.
>     ```
>   - sections.Render:
>     ````
>     <!-- rule-skill-sprint-open -->
>     ---
>     name: sprint-open
>     description: "Open the next sprint. Run it when the hook on /hi says that no sprint is open, or when the person types /sprint-open."
>     ---
>
>     No sprint is open: the first heading of `vault/wiki/sprint.md` marks the last sprint closed. This session opens the next one. The ledger hook refuses each decision line but a `defer` until a `create` of a page `entity-sprint-<id>` stands, so the opening Case is the first Case the session ratifies.
>
>     1. Assemble the Frontier as `/hi` sets it: the line `open the next sprint` of the brief stands first under `## Cases`, and no item of the closed sprint and no conserved Spec stands there.
>     2. When the person takes up that line, dispatch `case-guppi` for it as `vault/wiki/orchestration.md` sets it, and write into the prompt of the call that the opening Case asks the person, in its rounds:
>        - the id of the sprint, which names the page `entity-sprint-<id>`;
>        - its goal in one sentence, the `purpose` and the `## Purpose` of the page;
>        - its Definition of done, one Estimate per condition, which the page lists in `estimates`;
>        - the first milestone and its items, under `## Milestones`;
>        - whether to take any item of `vault/wiki/backlog.md` into the sprint: the Case says how many items the file holds, and goes through no item the person does not name.
>     3. Write into the same prompt that the opening Case writes, as the last item of the last milestone of the page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that the session that closes the sprint starts `/sprint-close` from it.
>     4. The skill decides none of the answers: `case-guppi` puts each to the person, and the person ratifies the opening Case as any other.
>     <!-- /rule-skill-sprint-open -->
>     ````
> - [ ] create `estimate-skill-sprint-open-asks-the-opening-questions`
>   - ref: `rule-skill-sprint-open`
>   - kind: `QA`
>   - purpose: `Whether /sprint-open has the opening Case of a sprint ask its id, its goal, its Definition of done, its first milestone and whether to take an item of the backlog, and write the close line, with the Frontier assembled as /hi sets it`
>   - method: `by hand, at the Retro of the session that creates it, the new Render of rule-skill-sprint-open in the Spec read against the Criterion`
>   - tags: `[sprint, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-open/SKILL.md`
> - [ ] read `estimate-skill-sprint-open-asks-the-opening-questions`

> **ratification:**
> ```
> - decision[case 743.6][create][rule-skill-sprint-open]{ref:rule-session-start}{tags:sprint,workflow,harness}
> - decision[case 743.6][create][estimate-skill-sprint-open-asks-the-opening-questions]{ref:rule-skill-sprint-open}{tags:sprint,workflow,harness}
> ```

### Case 743.7 — A hook on `/hi` starts `/sprint-open` when the sprint is closed

> **given:**
> `rule-skill-sprint-open`: the rule of the skill, which owns the hook.
> **＋** `rule-hook-registry`: the registrations of `.claude/settings.json`.
> **＋** `.claude/settings.json`: the file of the hooks.
> **＋** `guppi/sprint.py`: the hook `guppi sprint --hi` and the judgment of the closed mark.
> **＋** `guppi/event.py`: `is_hi_prompt`, the judgment of a `/hi` prompt.
> **＋** `tests/test_sprint.py`: the tests of the hook.
> **＋** `vault/wiki/sprint.md`: the file whose heading the hook reads.
> **＋** `estimate-skill-sprint-open-starts-at-hi`: the new check of the hook.

> **when:**
> The person types a prompt, and the `UserPromptSubmit` hook `uv run guppi sprint --hi` of `guppi/sprint.py` reads its payload and `vault/wiki/sprint.md`, or `tests/test_sprint.py` runs it over a made-up vault.

> **then:**
> When the prompt is `/hi`, by `is_hi_prompt` of `guppi/event.py`, and the first `## ` heading of `vault/wiki/sprint.md` carries the closed mark, the hook prints into the agent's context one line that names the closed sprint and tells the agent to start the skill of `rule-skill-sprint-open` before the Frontier.
> **＋** The hook judges the mark by the function of `guppi/sprint.py` that writes it.
> **＋** The hook exits 0 in every case, and an error of its own is one line on stderr.
> **－** Any other prompt, and a `/hi` while the heading carries no mark, print nothing.
> **－** The hook writes no file.

> **tasks:**
> - [ ] update `rule-hook-registry`
>   - old: `{ "type": "command", "command": "uv run guppi casecheck --prompt", "timeout": 30 },`
>   - new: `{ "type": "command", "command": "uv run guppi casecheck --prompt", "timeout": 30 }, { "type": "command", "command": "uv run guppi sprint --hi", "timeout": 30 },`
>   - change: `UserPromptSubmit runs guppi sprint --hi, which tells the agent at /hi to start /sprint-open when the sprint is closed (case 743.7)`
> - [ ] create `estimate-skill-sprint-open-starts-at-hi`
>   - ref: `rule-skill-sprint-open`
>   - kind: `QA`
>   - purpose: `Whether the hook on /hi tells the agent to start /sprint-open when sprint.md marks the last sprint closed, and prints nothing otherwise`
>   - method: `uv run pytest tests/test_sprint.py -k hi`
>   - tags: `[sprint, hooks, harness]`
> - [ ] `guppi/sprint.py`: the flag `--hi` reads the payload on stdin, judges `/hi` by `is_hi_prompt` and the mark by the function of 743.5, and prints the line; exit 0 always; the docstring says so.
> - [ ] `tests/test_sprint.py`: tests named `hi` — `/hi` with a closed heading prints the line; `/hi` with an open heading, another prompt and a missing file print nothing; every case exits 0.
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-skill-sprint-open-starts-at-hi`

> **ratification:**
> ```
> - decision[case 743.7][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 743.7][create][estimate-skill-sprint-open-starts-at-hi]{ref:rule-skill-sprint-open}{tags:sprint,hooks,harness}
> ```

### Case 743.8 — `/sprint-close` leads the session that closes a sprint

> **given:**
> `rule-skill-sprint-close`: the new rule whose Render is the skill `/sprint-close`.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the skill rendered from it.
> **＋** `rule-orchestration`: its paragraph on the closing session moves into the skill.
> **＋** `vault/wiki/orchestration.md`: the text rendered from `rule-orchestration`.
> **＋** `entity-sprint-migration`: its close line takes the fixed form.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian's frame, which runs the close line.
> **＋** `estimate-skill-sprint-close-leads-the-closing-session`: the new check of the skill.

> **when:**
> The person takes up on the Frontier the line of the sprint that names `/sprint-close`, and the main agent starts the skill `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, rendered from `rule-skill-sprint-close`, on `PreToolUse Skill`, or the person types `/sprint-close` on `UserPromptSubmit`.

> **then:**
> When the session's ledger holds a decision line other than a `defer`, the main agent closes the close line `[-] … · sprint · defer`, tells the person that the close needs a session of its own, and the skill stops.
> **＋** Otherwise the main agent closes each other open line under `## Cases` of `frontier.md` by the closer of its source put off, the person's pick of the close line standing as the words that ratify each short-form defer, leaves the lines under `## Work` and `## Ask` open, and shows the Frontier.
> **＋** It sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names and dispatches `case-guppi` for the closing Case with the groups in the prompt, and the closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choice for each Estimate still unread.
> **＋** When the sprint ran on a branch of its own, the closing Case holds a task line for the merge of that branch into the main branch, which Work Mode leaves unticked, so that the brief gives it as Work to the session that opens the next sprint.
> **＋** Work Mode takes each reading whose moment came and neither runs nor ticks the close line; the librarian runs it, as `.claude/agents/librarian-guppi.md` sets it.
> **＋** `vault/wiki/orchestration.md` holds no paragraph on the closing session, names the two skills in one sentence, and counts the start of `/sprint-close` among the moments of a short-form defer.
> **＋** The close line of `entity-sprint-migration` reads ``- the close of `migration` — `/sprint-close`, a session of its own``, and its `## Backlog` holds no line on the merge.
> **－** Besides the closing Case, the session ratifies only the Cases that prepare its readings.

> **tasks:**
> - [ ] create `rule-skill-sprint-close`
>   - ref: `rule-plan-mode`
>   - kind: `Leaf`
>   - purpose: `Prevents the session that closes a sprint from mixing the close with other decisions, or from reaching the close without the readings sorted, while the text that leads it stays out of the sessions that close no sprint`
>   - enforcement: `render`
>   - governs: `.claude/skills/sprint-close/SKILL.md`
>   - render_mode: `full`
>   - tags: `[sprint, workflow, harness]`
>   - sections.Purpose:
>     ```
>     Prevents the session that closes a sprint from mixing the close with other decisions, or from reaching the close without the readings sorted, while the text that leads it stays out of the sessions that close no sprint. Until case 743 these steps stood in a paragraph of `orchestration.md`, which every session loads. The skill starts when the person takes up the close line of the sprint, which [[rule-skill-sprint-open]] writes in a fixed form as the last item of the last milestone, or when the person types it (case 743.8). It reaches the librarian through the close line of the Spec, which `.claude/agents/librarian-guppi.md` runs ([[rule-sprint-close]], case 628.1).
>     ```
>   - sections.Render:
>     ````
>     <!-- rule-skill-sprint-close -->
>     ---
>     name: sprint-close
>     description: "Lead the session that closes the sprint. Run it when the person takes up the line of the sprint that names /sprint-close, or types /sprint-close."
>     ---
>
>     This session closes the sprint that `vault/wiki/sprint.md` names. Its Plan Mode holds only the closing Case and the Cases that prepare its readings, so that all of its decisions belong to the sprint it closes.
>
>     1. When the session's `raw/<date>/<hi HHMM>/ledger.md` holds a decision line other than a `defer`, this session cannot close the sprint. Close the line of the close in `frontier.md` as `[-] … · sprint · defer`, tell the person that the close needs a session of its own, opened by `/hi`, and stop the skill here.
>     2. Close each other open line under `## Cases` of `frontier.md` as put off, by the closer of its source that `vault/wiki/orchestration.md` sets: `[-] … · sprint · defer`, `[-] … · backlog · kept`, or a short-form defer and `[-] … · defer case N`. The person's pick of the close line stands as the words that ratify each such defer, shown in one reply as `## The short form — deferred decisions` of `vault/wiki/orchestration.md` sets it. Leave the lines under `## Work` and `## Ask` open: their readings serve the close. Show the Frontier.
>     3. Sort the Estimates under `vault/wiki/estimates/` that stand `pending` or `failed` into groups by the kind of moment their `method` names.
>     4. Dispatch `case-guppi` for the closing Case as `vault/wiki/orchestration.md` sets it, with the groups in the prompt of the call. The closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choice, `--carry` or `--archive-unread`, for each Estimate still unread after Work Mode; an Estimate of the sprint page is never carried. When the sprint ran on a branch of its own, the closing Case holds too the task line ``the merge of `<branch>` into `main` — the first work of the session that opens the next sprint, after its opening Case``, which Work Mode leaves unticked, so that the brief gives it under `Work` to that session. A Case that prepares a reading is built the same way, and no other Case is ratified in this session.
>     5. In Work Mode set up each moment and take each reading whose moment came. Work Mode neither runs nor ticks the close line.
>     6. The librarian runs the close line after `guppi generate`, as `.claude/agents/librarian-guppi.md` sets it. The close moves the finished pages, the finished sessions of `vault/raw/` and the old event logs to the archive, and `guppi sprint` then marks the sprint closed in `vault/wiki/sprint.md`; the next session opens the next sprint by `/sprint-open`.
>     <!-- /rule-skill-sprint-close -->
>     ````
> - [ ] create `estimate-skill-sprint-close-leads-the-closing-session`
>   - ref: `rule-skill-sprint-close`
>   - kind: `QA`
>   - purpose: `Whether /sprint-close refuses in a session that ratified another Case, puts off the other Cases lines, sorts the readings and has the closing Case built with the close line, while orchestration.md no longer holds the steps of the closing session`
>   - method: `by hand, at the Retro of the session that creates it, the new Renders of rule-skill-sprint-close and rule-orchestration and the update of entity-sprint-migration in the Spec read against the Criterion`
>   - tags: `[sprint, workflow, harness]`
> - [ ] update `rule-orchestration`
>   - old:
>     ```
>     The session that closes a sprint is a session of its own: its Plan Mode holds only the closing Case and the Cases that prepare its readings, so that all of its decisions belong to the sprint it closes, and the closing Case holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choices, which the librarian runs (`rule-sprint-close`, case 628.1). Before the closing Case, the main agent sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names; the closing Case names the groups in its `context` and holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and only an Estimate still unread after Work Mode is carried or archived unread (case 628.2). From the close until the first Case of the next session creates the next sprint page, `guppi sprint` and `make lint` report the missing sprint page, and that is expected (cases 628.3, 632.1).
>     ```
>   - new: `` The session that closes a sprint follows the skill `/sprint-close`, and the session that opens the next sprint the skill `/sprint-open`, which load only in those sessions (`rule-skill-sprint-close`, `rule-skill-sprint-open`, case 743.8). ``
>   - old: `` It has two moments: the close of Plan Mode, when the person defers the items left open, and the take-back of a ratified Case in Plan Mode, as `## Showing and signing a Case` sets it (case 713); ``
>   - new: `` It has three moments: the close of Plan Mode, when the person defers the items left open, the take-back of a ratified Case in Plan Mode, as `## Showing and signing a Case` sets it (case 713), and the start of `/sprint-close`, when the person's pick of the close line of the sprint stands as the words that ratify the defer of each other open item under `## Cases`, as `rule-skill-sprint-close` sets it (case 743.8); ``
>   - change: `the steps of the closing session move into the skill /sprint-close; one sentence names the two skills; the start of /sprint-close is a third moment of a short-form defer (case 743.8)`
> - [ ] update `entity-sprint-migration`
>   - old: `` - the close of migration — a session of its own: the pending readings taken in groups, `make test`, `make lint` and the tree read in its Work Mode, then `uv run guppi sprint-close --sprint migration --apply` in the librarian's run (case 628.9) ``
>   - new: `` - the close of `migration` — `/sprint-close`, a session of its own ``
>   - old: `` held as data so that a changed set rewrites no rule; case 239 - the merge of `migration` into `main` — the first work of the session that opens the next sprint, after its opening Case (case 628.9) ``
>   - new: `held as data so that a changed set rewrites no rule; case 239`
>   - change: `the close line takes the form that starts /sprint-close; the merge into main leaves the Backlog for the closing Case of /sprint-close (case 743.8)`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-close/SKILL.md`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-skill-sprint-close-leads-the-closing-session`

> **ratification:**
> ```
> - decision[case 743.8][create][rule-skill-sprint-close]{ref:rule-plan-mode}{tags:sprint,workflow,harness}
> - decision[case 743.8][create][estimate-skill-sprint-close-leads-the-closing-session]{ref:rule-skill-sprint-close}{tags:sprint,workflow,harness}
> - decision[case 743.8][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 743.8][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
