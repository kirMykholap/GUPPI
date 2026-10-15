## Case 813 — The main agent runs guppi caseid only for a new Case

> **context:**
> `uv run guppi caseid --next --session <stamp>` has one mode: each run prints the next free id and holds it in `<plan>.checked.json`, so the next run gets the id after it. In session 0232 a Case was built again under a number of its own, and the main agent ran the command to check that the number was held; that run held 813, which no Case used (`lesson-caseid-run-to-check-an-id-held-a-new-one`, handoff of session 0232). The check was never needed: the guard `guppi ratified --guard` of `guppi/ratified.py` holds the number at the first call of a `case-guppi` on its case file (docstring of `guppi/casecheck.py`, case 650.1). `rule-orchestration` says when the main agent runs the command, before the dispatch of a new top-level Case, but not that it runs it for nothing else. The person chose one sentence in that Render and no new mode of the command, so `guppi/caseid.py` and its tests do not change. The rule that governs the change is `rule-orchestration` itself; no rule forbids it. `estimate-ratification-case-id-carries-the-sprint` already promises when the main agent runs the command, so its Criterion is replaced whole: every line it holds is kept, one `－` line is added, and its `purpose` and `method` are set anew, since the `purpose` names the use of the main agent and the `method` named a new Render of `rule-ratification`, which this Case does not change. A Grep `caseid` over `vault/wiki/` (Decision pages left out) printed 13 files: `brief.md`, `log.md`, `orchestration.md`, `ratification.md`, `rules/rule-orchestration.md`, `rules/rule-ratification.md`, `lessons/lesson-caseid-run-to-check-an-id-held-a-new-one.md`, `insights/insight-caseid-printed-an-id-it-did-not-hold.md`, `estimates/estimate-ratification-case-id-carries-the-sprint.md`, `estimates/estimate-orchestration-shows-the-built-case.md`, `estimates/estimate-case-check-sends-back-a-case-number-held-by-another-agent.md`, `estimates/estimate-case-check-sends-back-a-ratified-case-in-another-shape.md` and `estimates/estimate-spec-box-refuses-a-stale-spec.md`; the same Grep over `.claude/` printed nothing. None of them is made false: `ratification.md` says what the command does, which stands; the Criterion of `estimate-orchestration-shows-the-built-case` names the command for the Work Mode dispatch of a new top-level Case, which the new sentence keeps; the two `case-check` Estimates speak of the count and of an id the command holds; `estimate-spec-box-refuses-a-stale-spec` names `guppi/caseid.py` as a reader of ids; the Insight speaks of a run with no plan file. `tests/test_orchestration.py` reads the live `orchestration.md`, but only its blocks tagged `showing` and `defer` by `example`, and the new sentence stands outside them. The decision lines carry no `{addresses}` mark: the lesson line stands in the ledger of session 0232, and a lesson whose fix is ratified in another session gets no mark (`ratification.md`).

> **problem:**
> `orchestration.md` does not tell the main agent that each run of `guppi caseid --next` holds a new id, so the agent ran it to check an id and held one that no Case uses.

> **recommend:**
> - **How do we stop a run that only checks from holding an id?**
>   - Recommended: (a) a sentence in `orchestration.md` only: the main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id; no code changes.
>   - Answer: agreed, (a).
> - **Which Estimate checks the fix?**
>   - Recommended: (a) replace the Criterion of `estimate-ratification-case-id-carries-the-sprint` with one more line, read at the Retro of this session against the new Render of `orchestration.md`.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, sets when the main agent runs the command.
> **＋** `guppi/caseid.py`: the command `guppi caseid --next`, which this Case does not change.
> **＋** `<plan>.checked.json`: the store of the ids the command and the guard hold.
> **＋** `guppi/ratified.py`: the guard that holds the number of a case file at the first call of its `case-guppi`.
> **＋** `estimate-ratification-case-id-carries-the-sprint`: its Criterion is replaced whole.

> **when:**
> The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, needs a Case id: for a new top-level Case, or to check the number of a Case built again.

> **then:**
> The main agent runs `uv run guppi caseid --next --session <stamp>` of `guppi/caseid.py` only to get the id of a new top-level Case, once for each Case.
> **＋** `vault/wiki/orchestration.md` says that each run of the command holds a new id.
> **－** The main agent never runs the command to check an id or what `<plan>.checked.json` holds.
> **－** A number that `case-guppi` takes for a Case built again is held by the guard of `guppi/ratified.py`, with no run of the command.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `since the command prints no id without that file.`
>   - new: `` since the command prints no id without that file. The main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id or what the store holds, since each run holds a new id; a number that `case-guppi` takes for a Case built again is held by the guard of its case file (as set in case 813). ``
>   - change: `the main agent runs guppi caseid --next only for the id of a new top-level Case, never to check an id`
> - [ ] update `estimate-ratification-case-id-carries-the-sprint`
>   - set:
>     ```
>     status: pending
>     purpose: Whether every reader of a Case id takes an id that carries its sprint and a plain id from before sprint ids alike, and guppi caseid --next --session <stamp> prints and holds the next id of the open sprint, which the main agent runs only for the id of a new top-level Case and never to check an id, and prints no id without --session or without the plan file of the session
>     method: "uv run pytest tests/test_caseid.py; by hand at the Retro of this session: the new Render of rule-orchestration in raw/<date>/<hi HHMM>/spec.md, and the Render of rule-ratification, read against the Criterion"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py` or `guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
>     **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
>     **＋** Or `uv run guppi caseid --next` runs without `--session`, or with a stamp whose session has no plan file.
>
>     Then:
>     A Case id of a sprint opened after case 788.2 is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case.
>     **＋** The readers read a Case id through `guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
>     **＋** The sprints `migration` and `plugin`, opened before case 788.2, keep plain ids to their close, by a fixed list in `guppi/caseid.py`.
>     **＋** The main agent creates the plan file of its session with its title line before its first run of the command.
>     **＋** `uv run guppi caseid --next --session <stamp>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
>     **＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
>     **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
>     **－** The main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id or what the store holds, since each run holds a new id.
>     **－** Without `--session` the command prints no id: it prints its usage error and exits 2.
>     **－** With a stamp whose session has no plan file, the command prints no id, holds nothing, prints one line on stderr and exits 1.
>     **－** An id with no sprint part, such as `785.1`, stays a Case from before sprint ids, and no page, file or citation is renamed.
>     ```
>   - change: `the Criterion replaced whole — the main agent runs guppi caseid --next only for the id of a new top-level Case, never to check an id`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-ratification-case-id-carries-the-sprint`

> **ratification:**
> ```
> - decision[case 813][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 813][update][estimate-ratification-case-id-carries-the-sprint]{ref:rule-ratification}
> ```
