## Case 650 — A guard stops a second case-guppi from overwriting the file of a Case another one holds

> **context:**
> Each Case is built by its own `case-guppi`, which writes it into `raw/<date>/<hi HHMM>/cases/case-<N>.md`. When the agent stops, the check of `rule-case-check` reads the file and stores each Case in `<plan>.checked.json` with the `agent_id` of the agent. Since case 645.3 the guard of `rule-spec-reconcile` lets any `case-guppi` write any file under `cases/`. Two agents can hold one number: the main agent gives a number twice, or the check gives the same free number to two agents it sends back at about the same time (the clash that case 610.2 counts numbers for). Then the second agent's `Write` replaces the first agent's file before the check sends the second agent back. The `Stop` comparison refuses the showing of the first Case, and nothing tells its agent to write the Case again (the handoff of session 0311, from the Not done of Case 645). The person chose a guard that claims the number at the first write. When the store holds no entry under the number of the file, the first call of a `case-guppi` on that file writes its `agent_id` there. A call of another agent on that file is refused with a free number, and that agent builds its Case under the free number. The holder is judged by `clashes` and the number is counted by `new_number` of `guppi/casecheck.py`. These are the judgments the check runs, so the guard and the check share one function. Case 650.1 creates the Estimate of this promise. The Criterion of `estimate-spec-reconcile-refuses-an-edit-of-the-plan` says that a call that names `case-guppi` under `cases/` is let through. That line becomes false, so Case 650.2 replaces the Criterion whole, and its line on `case-guppi` becomes an exception that names the new Estimate. Its `purpose` and `method` do not say that a call of `case-guppi` passes, so they stand. The Purpose and How it works of `rule-spec-reconcile` say that every write of `case-guppi` under `cases/` is an exception, and that only the hooks of `rule-spec-write` and `rule-case-check` write the store. Four pairs in Case 650.1 fix those sentences. Both Estimates carry a `ref`, so the vault query of `ask-guppi` was not run. A Glob `vault/**/*another-agent-holds*` printed nothing, so the new slug is free.
>
> What the frame showed, by these searches. A Grep of `checked\.json` over `vault/wiki/`, with `*.md !**/decisions/**`, printed 15 files. `rule-spec-reconcile` and `estimate-spec-reconcile-refuses-an-edit-of-the-plan` enter the Case. Ten files read the text, findings or notes of an entry that the check stores: `rule-spec-write`, `estimate-spec-write-refuses-a-changed-case-file`, `estimate-spec-write-copies-the-ratified-case`, `estimate-case-check-refuses-a-changed-case-file`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-notes-a-criterion-line-not-carried`, `estimate-case-check-refuses-a-letter-outside-the-script`, `estimate-case-check-requires-each-question-of-the-rounds` and `estimate-case-check-sends-back-a-clash-with-another-case`. They stand. The check replaces the entry of a held number with the Case of the same agent. Until then the entry holds no text, so the Spec hook and the `Stop` comparison refuse a showing, as they refuse one that differs from the store. `estimate-case-check-sends-back-a-ratified-case-in-another-shape` stands: it counts the keys of the store, and a held number is one of them, so the check does not give out a held number. `estimate-case-check-sends-back-a-case-number-held-by-another-agent` stands: it judges an entry by its `agent_id`, so an answer of the old path under a held number is sent back, as the person chose. Its words "from an answer" name the entry of the agent that holds the number. `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback` records a past session. A Grep of `PreToolUse` over `vault/wiki/rules/` printed 14 files, and over `.claude/` it printed `.claude/settings.json`. Only `rule-spec-reconcile` sets what happens at an `Edit` or `Write` of a file under `cases/`. `rule-governed-files-hook` runs `uv run guppi guard` on the same event, for rendered harness files only. `rule-hook-registry` and `.claude/settings.json` keep the registration of the guard as it is. The other hits name other tools or quote an example.
>
> `rule-case-build` stands. Its agent file says that the file of its Case is the one file the guard lets the agent write, and that stays true. The refusal itself tells the agent to build under the free number, as the finding of the check has done since case 610.1. In Work Mode, a new agent dispatched to build again a Case that another agent holds is refused. The check of case 610.2 already sends such an agent back. The guard reads entries that the check already writes with an `agent_id`, and an entry with no `agent_id` is not compared, so the guard needs no old form.
>
> Pre-spec raised three findings, and this build answers them. The pairs on `rule-spec-reconcile` now match the `then` lines: the first write passes when no other agent holds the number, and a number counts as held when the store holds Case N or a sub-case of it from another agent, as `clashes` judges it. On its own error the guard keeps exit 0 and lets the call run, as the existing rule of the guard sets it in `estimate-spec-write-exits-2-on-an-error`. That Criterion stays true, and 650.1 names the error in a `－` line. A store that cannot be read or written then holds no number, and the check of `rule-case-check` still sends back a number held by another agent when the agent stops. The guard reads `agent_id` from the `PreToolUse` input. The handoff of session 0311 records this field in the probe of 645.3: "the `PreToolUse` input held `agent_id` and `agent_type` (`claude`)". So this Case adds no probe. The method of the new Estimate adds a reading by hand of the entry that a live `case-guppi` writes with its first `Write`.
>
> The check sent back notes, and they stand. In Case 650.2, the old line that let a call of `case-guppi` under `cases/` through is not carried word for word. It changed on purpose: it is now a line on the other agents and an exception that names the new Estimate. Two `then` lines of 650.2 share many words with 650.1, the refusal under `cases/` and the line of the event log. Each sub-case still sets its own promise: 650.2 the refusal of an agent that is not `case-guppi`, 650.1 the refusal of a `case-guppi` whose number another agent holds.
>
> Not done: the guard and the check each read the store whole and write it whole. Two writes at the same instant can still lose one of them, and this Case does not lock the store.

> **problem:**
> A second `case-guppi` that builds under a number another agent holds replaces that agent's file before any check runs. The first Case can no longer be shown until its agent writes it again, and nothing tells that agent to do so. The question was whether a guard stops the second write and how it knows that a number is taken, what the refused agent does, and how done is checked.

> **recommend:**
> - **Whether a guard stops the second write, and how it knows the number is taken**
>   - Recommended: (a) the guard claims the number at the first write: the first builder whose write creates the file is recorded in the store as the holder of the number at once, and a write or edit of that file by any other builder is refused before it runs, with a free number counted as the check counts one; this covers the time between the first builder's write and its stop.
>   - Answer: agreed, (a).
> - **What the refused builder does next**
>   - Recommended: (a) it builds under the free number the refusal names, counted as the check counts one, and the main agent learns the number from the summary.
>   - Answer: agreed, (a).
> - **How the new refusal is checked**
>   - Recommended: (a) a new check for the claim under the guard's rule, and the old check of the guard replaced whole, its line on builders now naming a number held by another builder as the exception; two sub-cases.
>   - Answer: agreed, (a).

### Case 650.1 — The first write of case-guppi holds the number of its file

> **given:**
> `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`: the new check of a call on a file whose number another agent holds.
> **＋** `rule-spec-reconcile`: the rule of the guard.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the guard and its tests.
> **＋** `guppi/casecheck.py`: `clashes`, `new_number` and `case_file`, the judgments of the check of `rule-case-check`, unchanged in what they judge.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.
> **＋** `estimate-spec-write-exits-2-on-an-error`: the guard keeps exit 0 on its own error. Unchanged.
> **＋** `.claude/settings.json`: the `PreToolUse` registration of the guard. Unchanged.

> **when:**
> `case-guppi` calls `Edit`, `Write` or `MultiEdit` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi ratified --guard` on `PreToolUse` reads the path, the agent type and the `agent_id` of the call from the hook input, and `<plan>.checked.json` beside the plan file of the session.

> **then:**
> The call is refused when `<plan>.checked.json` holds Case N, or a sub-case of it, under its number alone with an `agent_id` other than the one of the call: exit 2 with the reason on stderr, and the call does not run.
> **＋** The reason names the file and a free number, and tells `case-guppi` to build its Case under that number.
> **＋** The holder is judged by `clashes` and the free number is counted by `new_number` of `guppi/casecheck.py`, the judgments that the check of `rule-case-check` runs.
> **＋** A call that passes while `<plan>.checked.json` holds no entry under N alone writes there, under N, an entry with the `agent_id` of the call and the time, and no text, so the number is held before the agent stops.
> **＋** A refusal writes one line of the refusal to the day's event log.
> **－** A call whose `agent_id` is the one of the entry under N, and an entry with no `agent_id`, are not refused by this check.
> **－** A call with no `agent_id`, a file whose name gives no number, and a session with no plan file are not judged by this check, and nothing is written into `<plan>.checked.json`.
> **－** An error of the guard while it finds the plan file or reads or writes `<plan>.checked.json` lets the call run: exit 0 with one line on stderr, as `estimate-spec-write-exits-2-on-an-error` sets it for the guard.

> **tasks:**
> - [ ] create `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`
>   - ref: `rule-spec-reconcile`
>   - kind: `QA`
>   - purpose: `Whether the first call of case-guppi on the file of a Case holds its number in the store, and a call of another case-guppi on that file is refused with a free number`
>   - method: `uv run pytest tests/test_ratified.py -k number_held; by hand in a session after the work, the entry of the store that the first Write of a live case-guppi wrote, holding its agent_id`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-spec-reconcile`
>   - old: `` unless `case-guppi` makes it (cases 453, 645.3); ``
>   - new: `` unless `case-guppi` makes it and no other agent holds the number of that Case (cases 453, 645.3, 650.1); ``
>   - old: `` and every `Edit`, `Write` and `MultiEdit` that names `case-guppi` on a file outside such a folder: exit 2 ``
>   - new: `` and every `Edit`, `Write` and `MultiEdit` that names `case-guppi` on a file outside such a folder, or on the file `case-<N>.md` of a Case when the store holds Case N, or a sub-case of it, under its number alone from another `agent_id` (case 650.1): exit 2 ``
>   - old: `` The exceptions are an `Edit`, `Write` or `MultiEdit` of `case-guppi` under `cases/`, and ``
>   - new: `` The exceptions are an `Edit`, `Write` or `MultiEdit` of `case-guppi` under `cases/` on a file `case-<N>.md` when the store holds neither Case N nor a sub-case of it under its number alone from another `agent_id` — when the store holds no entry under N, N the number of the file `case-<N>.md`, the call writes its `agent_id` there, so the number is held before the agent stops, and a refusal names a free number counted as the check of `rule-case-check` counts one, by the functions of `guppi/casecheck.py` the check runs (case 650.1) —, and ``
>   - old: `` The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, ``
>   - new: `` The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, and so does this hook for the entry that holds a number, ``
>   - change: `the first write of case-guppi on the file of a Case holds its number in the store, and a write of another case-guppi on that file is refused with a free number (case 650.1)`
> - [ ] `guppi/casecheck.py`: one function reads N from the name `case-<N>.md`, beside `case_file`; the module docstring says that the guard writes the entry of a held number, with an `agent_id` and no text, which the check replaces.
> - [ ] `guppi/ratified.py`: the guard finds the plan file of the session and its store; it refuses a call of `case-guppi` on `case-<N>.md` when `clashes` finds another holder, the reason naming the file and the number of `new_number`; a call that passes with no entry under N writes the entry of the held number; the module docstring and the docstring of `guard_refusal` say the same.
> - [ ] `tests/test_ratified.py`: tests `-k number_held` — a first `Write` of `case-guppi` passes and writes the entry with its `agent_id`; a `Write` and an `Edit` of another `agent_id` on that file are refused, the reason naming a free number, and the event log holds the refusal; the same `agent_id` passes; an entry with no `agent_id`, a call with no `agent_id` and a session with no plan file are let through and write nothing; a store that cannot be read or written lets the call through with exit 0 and one line on stderr.
> - [ ] read `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`

> **ratification:**
> ```
> - decision[case 650.1][create][estimate-spec-reconcile-refuses-a-case-file-another-agent-holds]{ref:rule-spec-reconcile}{tags:hooks,harness,workflow}
> - decision[case 650.1][update][rule-spec-reconcile]{ref:rule-spec-reconcile}
> ```

### Case 650.2 — The check of the guard leaves a held number to its own check

> **given:**
> `estimate-spec-reconcile-refuses-an-edit-of-the-plan`: its Criterion is replaced whole.
> **＋** `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`: the promise of a call of `case-guppi` on a file whose number another agent holds.
> **＋** `rule-spec-reconcile`: the rule of the guard.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the guard and its tests.
> **＋** `guppi/casecheck.py`: `is_case_file`, the judgment of a file under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`.
> **＋** `guppi/ledger.py`: `is_plan_file` and `plan_path`, the judgment of a plan file under `.claude/plans/`.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> An agent calls `Edit`, `Write` or `MultiEdit` on a file, and `uv run guppi ratified --guard` on `PreToolUse` reads the path, the content and the agent type of the call from the hook input.

> **then:**
> The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
> **＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
> **＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way.
> **＋** An `Edit`, `Write` or `MultiEdit` of a file under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`, whatever its name and whether it exists or not, is refused the same way when the hook input does not name `case-guppi` as the agent type; the reason names the file and says that `case-guppi` alone writes it.
> **＋** An `Edit`, `Write` or `MultiEdit` whose hook input names `case-guppi` on a file outside such a `cases/` folder is refused the same way.
> **＋** A file under that folder is judged by `is_case_file` of `guppi/casecheck.py`, which the check of the file uses too; a plan file is a `.md` file under `.claude/plans/`, judged by `is_plan_file` of `guppi/ledger.py`, which `plan_path` uses too.
> **＋** A refusal writes one line of the refusal to the day's event log and no `tool` line, so `plan_path` of `guppi/ledger.py` still names the plan file.
> **－** A call whose hook input names `case-guppi` on a file under such a `cases/` folder is let through unless `<plan>.checked.json` holds the number of the file from another agent, as `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` sets it.
> **－** An edit of a file outside `.claude/plans/` and outside such a `cases/` folder by any agent but `case-guppi` is not judged by this hook.
> **－** A payload the hook cannot read: exit 0 with one line on stderr.
> **－** No `PostToolUse` hook compares an edit of the plan.

> **tasks:**
> - [ ] update `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a call of case-guppi under cases/ passes unless another agent holds the number of the file, the promise of estimate-spec-reconcile-refuses-a-case-file-another-agent-holds (case 650.2)`
> - [ ] read `estimate-spec-reconcile-refuses-an-edit-of-the-plan`

> **ratification:**
> ```
> - decision[case 650.2][update][estimate-spec-reconcile-refuses-an-edit-of-the-plan]{ref:rule-spec-reconcile}
> ```
