## Case 922 — The Case-id check states where its list of plain sprints matters

> **context:**
> `guppi ship` copies into the clean version each `passed` Estimate whose target page it writes, its Criterion as it stands, and removes each bracket that holds a pointer to a case by `removed` of `.guppi/guppi/pointers.py`. The reading of `estimate-clean-branch-ships-neutral-texts`, taken at the `/hi` of session 1930, listed in its `## Result` fourteen shipped Estimates whose Criterion holds a sentence true only in the repository of GUPPI, and the handoff of session 2341 named five of them as still waiting. Each of the other nine has had its Criterion replaced since that reading, by its History: Case 920.1–920.4 of this session rewrites `estimate-compact-recall-reloads`, `estimate-ask-query-before-a-create`, `estimate-synthesis-keeps-actioned-by-the-mark` and `estimate-synthesis-clusters`; case 918.1 and case 918.2 name the language of `estimate-case-build-records-the-rounds-in-recommend` and `estimate-case-build-writes-the-case` by its role, case 918.3 names the code page of the locale in `estimate-python-utf8-output-intact` in place of `cp1252`, case 918.4 opens the Criterion of `estimate-guppi-package-is-ready-after-the-install` with the condition in the repository of GUPPI, and case 917.1 has `estimate-sprint-close-moves-old-event-logs` read `vault/.gitignore`, a file that `guppi ship` writes into the clean version by `VAULT_IGNORE` of `.guppi/guppi/ship.py`. Four of the five were rewritten later in session 1930, after that reading: by their History, case 908.1 named the transcripts folder of `estimate-permissions` as the one the Render of `rule-permissions` names, case 908.2 named the language of `estimate-orchestration-forwards-a-discussion-question` by its role, and cases 904.1 and 904.3 removed the old path of the answer text from `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-example-passes-the-check`; each stands `passed` on its new text. The person chose to leave those four as they stand, so this Case changes none of them, and since the defer of `decision-case-893.1` goes by Case 920.5, the line that says the four are done is one that `/handoff` writes after the Retro commit, in the section of the Render of `rule-handoff` that fits it, `## Observations`; this Case leaves no task on that file in Work Mode, since that Render has `/handoff` write the handoff as one document in its sections, in their order, once the tree is clean.
>
> The fifth, `estimate-ratification-case-id-carries-the-sprint`, was rewritten by case 880.15 before the reading, and the reading still listed it for `PLAIN_SPRINTS`. With its pointer brackets removed, its sentence reads that the sprints that `PLAIN_SPRINTS`, a fixed list in `.guppi/guppi/caseid.py`, names keep plain ids to their close; the clean version takes `.guppi/guppi/caseid.py` as it stands, `ship.py` leaving out only the files of its `LEFT_OUT`, and there `PLAIN_SPRINTS = ("migration", "plugin")` names two sprints of GUPPI. The person chose to add one sentence after it that states its condition, in the repository of GUPPI, which the Criterion of `estimate-clean-branch-ships-neutral-texts` accepts: a sentence that states its condition holds as it reads in a project that installed GUPPI. That Criterion is the rule of this Case, and it stands, since this Case changes a text it judges and not its promise. The new sentence holds no pointer, and it says what the comment above `PLAIN_SPRINTS` in `.guppi/guppi/caseid.py` says, that the list holds the sprints opened before sprint ids came in. This Case replaces the Criterion of `estimate-ratification-case-id-carries-the-sprint` whole, every line as it stands and the one sentence added, and that Estimate checks it; its `purpose` and `method` speak of no sentence that changes and stand. The replaced Criterion sets it `pending`, and `rule-ratification`, `core: true`, already stands `draft`, so the clean version loses nothing more; its `method`, the tests of `.guppi/tests/test_caseid.py` and the two Renders, runs at the Retro of this session.
>
> A Grep of the five pages under `vault/wiki/estimates/` for `GUPPI|Russian|English|c--|migration|plugin|old path|writer is live|case \d` printed, inside a `## Criterion`, only lines 23 and 25 of `estimate-ratification-case-id-carries-the-sprint`; its other hits are `sprint` fields, History lines and Results, which stand. A Grep of the repository, `vault/raw/` and `vault/archive/` left out, for `ratification-case-id-carries-the-sprint` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `.guppi/tests/test_caseid.py`, `vault/wiki/estimates/estimate-clean-branch-ships-neutral-texts.md` and `vault/wiki/rules/rule-ratification.md`: the docstring of the test, a Result, the field `estimates` and a History line, which the change does not make false; the brief and the log are not read. Of the tests that read the live vault, the live build of `.guppi/tests/test_ship.py` leaves a `pending` Estimate out and judges a shipped one by `outside` of `.guppi/guppi/pointers.py`, and the new sentence holds no pointer; `.guppi/tests/test_guppi_package.py` looks for old commands and paths, and the new sentence holds none. The Greps of the session's ledger for `lesson\[error\]` and `\{addresses:` printed nothing, so no line carries a mark.

> **problem:**
> The handoff of the last session named five shipped checks that still held a sentence true only in the repository of GUPPI, but four of them were rewritten after the reading that listed them, and the fifth names a fixed list whose sprints exist only in the repository of GUPPI without saying so.

> **recommend:**
> - **What does this Case do with the four checks already rewritten?**
>   - Recommended: (a) leave them as they stand; the handoff says they are done.
>   - Answer: agreed, (a).
> - **What becomes of the plain-id sentence of the Case-id check?**
>   - Recommended: (b) add a sentence that states where the list matters, in the repository of GUPPI.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: at `/pre-spec`, drop the Work Mode task that writes a line into the handoff of this session, since the Render of `rule-handoff` has `/handoff` write that file whole after the Retro commit.
>   - Taken: the task and its line of `given` are gone; the `context` says that `/handoff` writes the line in `## Observations`.
> - **Change**
>   - Asked: at `/pre-spec`, the reading listed fourteen Estimates, not five; check the others against the words it named and fix the count.
>   - Taken: the `context` gives the fourteen and names the Case that replaced the Criterion of each of the other nine; none still holds the words the reading named, so no round was needed.

> **given:**
> `estimate-ratification-case-id-carries-the-sprint`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/caseid.py`: holds `PLAIN_SPRINTS` and reads a Case id in both forms.
> **＋** `.guppi/guppi/casecheck.py`, `.guppi/guppi/ratified.py`, `.guppi/guppi/lint.py`, `.guppi/guppi/gate.py`, `.guppi/guppi/materialize.py`: the readers of a Case id.
> **＋** `vault/wiki/orchestration.md`: the Render of `rule-orchestration` that the main agent follows.
> **＋** `vault/wiki/sprint.md`: the sprint page whose first heading gives the open sprint.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of a session, whose `create` line of a sprint page gives the open sprint.
> **＋** `/sprint-open`: the skill that sets the id of the opening Case of a sprint.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the rule of the texts of a shipped Estimate.

> **when:**
> `.guppi/guppi/casecheck.py`, `.guppi/guppi/ratified.py`, `.guppi/guppi/lint.py`, `.guppi/guppi/gate.py` or `.guppi/guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
> **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run --project .guppi guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
> **＋** Or `uv run --project .guppi guppi caseid --next` runs without `--session`, or with a stamp whose session has no plan file.

> **then:**
> A Case id of a sprint that `PLAIN_SPRINTS` of `.guppi/guppi/caseid.py` does not list is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case (sprint ids came in with case 788.2).
> **＋** The readers read a Case id through `.guppi/guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
> **＋** The sprints that `PLAIN_SPRINTS`, a fixed list in `.guppi/guppi/caseid.py`, names keep plain ids to their close (the sprints of that list opened before case 788.2).
> **＋** In the repository of GUPPI, that list names the sprints opened before sprint ids came in.
> **＋** The main agent creates the plan file of its session with its title line before its first run of the command.
> **＋** `uv run --project .guppi guppi caseid --next --session <stamp>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
> **＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
> **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
> **－** The main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id or what the store holds, since each run holds a new id.
> **－** Without `--session` the command prints no id: it prints its usage error and exits 2.
> **－** With a stamp whose session has no plan file, the command prints no id, holds nothing, prints one line on stderr and exits 1.
> **－** An id with no sprint part, such as `785.1`, stays as it is, and no page, file or citation is renamed.

> **tasks:**
> - [ ] update `estimate-ratification-case-id-carries-the-sprint`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a sentence states that, in the repository of GUPPI, PLAIN_SPRINTS names the sprints opened before sprint ids came in`
> - [ ] read `estimate-ratification-case-id-carries-the-sprint`

> **ratification:**
> ```
> - decision[case 922][update][estimate-ratification-case-id-carries-the-sprint]{ref:rule-ratification}
> ```
