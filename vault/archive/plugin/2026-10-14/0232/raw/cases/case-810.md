## Case 810 — The id of a new Case comes only with the session's stamp

> **context:**
> The main agent takes the number of a new top-level Case from `uv run guppi caseid --next`, which prints the next free id and holds it in the store of the session's plan file, so that the next run prints the id after it. `guppi/caseid.py` finds the session by its stamp, which `session_stamp` of `guppi/event.py` takes from `--session` or a hook payload; a Bash call has no payload, so without the option the stamp is `--------`, `session_dir` and `plan_path` of `guppi/ledger.py` find no folder and no plan file, and the command prints an id it does not hold and counts it without the session's ledger and Case files. `orchestration.md` (twice) and `ratification.md` name the command without the option, and last session it printed one id twice, as `lesson-caseid-held-no-id-without-the-session-option` records. The person chose that the pages name `--session <id>`, the stamp of the `hi:` line, and that the command refuses to run without it, as `guppi box` does: a Grep of `add_argument\("--session"` over `guppi/` printed `guppi/box.py` (`required=True`), `guppi/caseid.py`, `guppi/event.py` and `guppi/prespec.py`. The rule weighed against the option of reading the newest `hi` line of the event log is the one that `resolve_session` of `guppi/prespec.py` states for the same stamp: the session is never guessed, since a parallel session writes its own `hi` into the same log and after midnight today's log holds none (case 213.1). The change adds no judgment of a text, only a required option of the parser.
> `estimate-ratification-case-id-carries-the-sprint` checks the command, and its Criterion names it without the option, so its Criterion is replaced whole, written under `sections`, and its `purpose` names the option; its `method`, `uv run pytest tests/test_caseid.py` and the reading of the new Renders in `spec.md` at Retro, stands. The check of this file notes five lines of the old Criterion that the new one does not carry word for word: three now name `--session` — the run of the main agent, the sprint the command takes and the id it holds — and two name case 788.2 where they said this Case, since in a Criterion replaced by case 810 those words would name case 810, which brought in no sprint ids. A Grep of `caseid` over `vault/wiki/` printed `brief.md`, `ratification.md`, `orchestration.md`, `log.md`, `lesson-caseid-held-no-id-without-the-session-option.md`, `rule-orchestration.md`, `rule-ratification.md`, `estimate-orchestration-shows-the-built-case.md`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent.md`, `estimate-spec-box-refuses-a-stale-spec.md`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape.md` and `estimate-ratification-case-id-carries-the-sprint.md`; over `.claude/` it printed nothing. `brief.md` and `log.md` are not read. The Criterion of `estimate-orchestration-shows-the-built-case` names the Work Mode dispatch under the id that `uv run guppi caseid --next` prints: it stands, since it names the command by its name for the dispatch it promises, and the option is the promise of `estimate-ratification-case-id-carries-the-sprint`, which this Case replaces, so nothing is signed twice. `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape` and `estimate-spec-box-refuses-a-stale-spec` speak of the store entry, of `next_id` and of the grammar of an id, which do not change, so they stand. The lesson gets no mark, since it was written in another session. A Grep of `orchestration\.md|ratification\.md` over `tests/` printed `tests/test_ship.py`, `tests/test_ledger.py` and `tests/test_orchestration.py`: the first reads a copy under a temporary folder, the second only names the file in a message, and the third reads only the blocks tagged `showing` and `defer`, which this Case does not touch, so they stand.

> **problem:**
> The command that numbers a new Case is written without the option that tells it the session, and without it the command prints an id that it does not hold and that may already be taken.

> **recommend:**
> - **Where should the command get the session id when you start a new Case?**
>   - Recommended: (c) the pages name `--session <id>`, and the command refuses to run without it.
>   - Answer: agreed, (c).
> - **Which check should prove the fix?**
>   - Recommended: (a) rewrite the text of `estimate-ratification-case-id-carries-the-sprint` whole.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, gives the command for a new top-level Case.
> **＋** `rule-ratification`: its Render, `vault/wiki/ratification.md`, states what the command does.
> **＋** `guppi/caseid.py`: the command `guppi caseid --next`.
> **＋** `tests/test_caseid.py`: the tests of the command.
> **＋** `estimate-ratification-case-id-carries-the-sprint`: its Criterion is replaced whole.

> **when:**
> The main agent runs `guppi/caseid.py` by `uv run guppi caseid --next` before it dispatches a new top-level Case, with `vault/wiki/orchestration.md` and `vault/wiki/ratification.md` rendered from `rule-orchestration` and `rule-ratification`.

> **then:**
> `vault/wiki/orchestration.md` and `vault/wiki/ratification.md` give the command as `uv run guppi caseid --next --session <id>`, `<id>` the stamp of the `hi:` line of the session.
> **＋** With `--session`, `guppi/caseid.py` prints and holds the next id of the session of that stamp, as before.
> **－** Without `--session`, `guppi/caseid.py` prints no id: it prints its usage error and exits 2.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` for a new top-level Case the id that `uv run guppi caseid --next` prints and holds ``
>   - new: `` for a new top-level Case the id that `uv run guppi caseid --next --session <id>` prints and holds, `<id>` the stamp of the `hi:` line of the session ``
>   - old: `` under the id that `uv run guppi caseid --next` prints, with the path of the file of the ratified Case ``
>   - new: `` under the id that `uv run guppi caseid --next --session <id>` prints, with the path of the file of the ratified Case ``
>   - change: `the command for the id of a new Case carries --session with the stamp of the hi: line`
> - [ ] update `rule-ratification`
>   - old: `` `uv run guppi caseid --next` prints the id of the next Case of the open sprint and holds it ``
>   - new: `` `uv run guppi caseid --next --session <id>`, `<id>` the stamp of the `hi:` line of the session, prints the id of the next Case of the open sprint and holds it, and without `--session` it prints no id ``
>   - change: `guppi caseid --next takes --session, and prints no id without it`
> - [ ] update `estimate-ratification-case-id-carries-the-sprint`
>   - set:
>     ```
>     status: pending
>     purpose: Whether every reader of a Case id takes an id that carries its sprint and a plain id from before sprint ids alike, and guppi caseid --next --session <id> prints and holds the next id of the open sprint, which the main agent uses, and prints no id without --session
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py` or `guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
>     **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run guppi caseid --next --session <id>`, `<id>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
>     **＋** Or `uv run guppi caseid --next` runs without `--session`.
>
>     Then:
>     A Case id of a sprint opened after case 788.2 is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case.
>     **＋** The readers read a Case id through `guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
>     **＋** The sprints `migration` and `plugin`, opened before case 788.2, keep plain ids to their close, by a fixed list in `guppi/caseid.py`.
>     **＋** `uv run guppi caseid --next --session <id>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
>     **＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
>     **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
>     **－** Without `--session` the command prints no id: it prints its usage error and exits 2.
>     **－** An id with no sprint part, such as `785.1`, stays a Case from before sprint ids, and no page, file or citation is renamed.
>     ```
>   - change: `the Criterion replaced whole — guppi caseid --next takes --session with the stamp of the hi: line, and prints no id without it`
> - [ ] `guppi/caseid.py`: the option `--session` is required, and the first line of the docstring names it as required.
> - [ ] `tests/test_caseid.py`: a test that a run of `guppi caseid --next` without `--session` exits 2, prints no id and holds nothing in the store.
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] `uv run guppi render`: `vault/wiki/ratification.md`
> - [ ] read `estimate-ratification-case-id-carries-the-sprint`

> **ratification:**
> ```
> - decision[case 810][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 810][update][rule-ratification]{ref:rule-ratification}
> - decision[case 810][update][estimate-ratification-case-id-carries-the-sprint]{ref:rule-ratification}
> ```
