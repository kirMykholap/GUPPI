<!-- approved 15:51:03 · session f5706873 -->

# Spec — session 1343, 2026-10-05

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

```then
create:
- slug: estimate-spec-reconcile-refuses-a-case-file-another-agent-holds
  ref: rule-spec-reconcile
  kind: QA
  purpose: Whether the first call of case-guppi on the file of a Case holds its number in the store, and a call of another case-guppi on that file is refused with a free number
  method: uv run pytest tests/test_ratified.py -k number_held; by hand in a session after the work, the entry of the store that the first Write of a live case-guppi wrote, holding its agent_id
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-spec-reconcile
  replace:
  - old: unless `case-guppi` makes it (cases 453, 645.3);
    new: unless `case-guppi` makes it and no other agent holds the number of that Case (cases 453, 645.3, 650.1);
  - old: 'and every `Edit`, `Write` and `MultiEdit` that names `case-guppi` on a file outside such a folder: exit 2'
    new: 'and every `Edit`, `Write` and `MultiEdit` that names `case-guppi` on a file outside such a folder, or on the file `case-<N>.md` of a Case when the store holds Case N, or a sub-case of it, under its number alone from another `agent_id` (case 650.1): exit 2'
  - old: The exceptions are an `Edit`, `Write` or `MultiEdit` of `case-guppi` under `cases/`, and
    new: The exceptions are an `Edit`, `Write` or `MultiEdit` of `case-guppi` under `cases/` on a file `case-<N>.md` when the store holds neither Case N nor a sub-case of it under its number alone from another `agent_id` — when the store holds no entry under N, N the number of the file `case-<N>.md`, the call writes its `agent_id` there, so the number is held before the agent stops, and a refusal names a free number counted as the check of `rule-case-check` counts one, by the functions of `guppi/casecheck.py` the check runs (case 650.1) —, and
  - old: The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call,
    new: The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, and so does this hook for the entry that holds a number,
  change: the first write of case-guppi on the file of a Case holds its number in the store, and a write of another case-guppi on that file is refused with a free number (case 650.1)
```

```tasks
- [x] create `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`
- [x] update `rule-spec-reconcile`
- [x] `guppi/casecheck.py`: one function reads N from the name `case-<N>.md`, beside `case_file`; the module docstring says that the guard writes the entry of a held number, with an `agent_id` and no text, which the check replaces.
- [x] `guppi/ratified.py`: the guard finds the plan file of the session and its store; it refuses a call of `case-guppi` on `case-<N>.md` when `clashes` finds another holder, the reason naming the file and the number of `new_number`; a call that passes with no entry under N writes the entry of the held number; the module docstring and the docstring of `guard_refusal` say the same.
- [x] `tests/test_ratified.py`: tests `-k number_held` — a first `Write` of `case-guppi` passes and writes the entry with its `agent_id`; a `Write` and an `Edit` of another `agent_id` on that file are refused, the reason naming a free number, and the event log holds the refusal; the same `agent_id` passes; an entry with no `agent_id`, a call with no `agent_id` and a session with no plan file are let through and write nothing; a store that cannot be read or written lets the call through with exit 0 and one line on stderr.
- [ ] read `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`
```

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

```then
update:
- slug: estimate-spec-reconcile-refuses-an-edit-of-the-plan
  set:
    status: pending
  change: the Criterion replaced whole — a call of case-guppi under cases/ passes unless another agent holds the number of the file, the promise of estimate-spec-reconcile-refuses-a-case-file-another-agent-holds (case 650.2)
```

```tasks
- [x] update `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
- [ ] read `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
```

## Case 651 — orchestration.md names the summary of case-guppi and shows by tested examples the forms the main agent writes

> **context:**
> `orchestration.md` tells the main agent what to do in a session. It still calls the reply of `case-guppi` "the answer", from the time that reply held the whole Case. Since case 645, `case-guppi` writes the Case into its file and replies with a summary: the path, and for each Case its id, name, Estimate and ledger lines in a plain fence. Now "the answer" can mean the summary, the file or the text the check stored. The page also leaves out two exact forms that the checks read. It says that the `ratification` of a showing holds the ledger lines "as the answer holds them". The `Stop` check reads only the quote block under `> **ratification:**`, so in session 1834 of 2026-10-02 the main agent put the fence outside the quote and the check refused the showing (`lesson-case-showing-ratification-fence-outside-the-blockquote`). The page says the `then` block of a short-form defer carries "slug, type and purpose". The hook of `rule-spec-write` reads only a list of items, so in session 0109 of 2026-10-05 a single mapping was refused twice (`lesson-orchestration-short-defer-then-block-written-as-a-mapping`). Both lessons are children of `insight-workflow-case-schema-silent-on-what-the-scripts-accept`. Case 646 left that Insight open until a later Case covered the forms the main agent writes.
>
> The person chose the following. Each meaning gets its own word: the summary, the file, and the text the check stored. Only `orchestration.md` changes. The two forms are shown by examples that a test runs the checks over, as case 646 did for `case-schema.md`. Only the two forms of the lessons are covered. The work is three sub-cases. The tests skip until the librarian's render. The example of a showing is a parent with two sub-cases, and its heading is in English because the page is documentation. The Insight is set `actioned` by this Case. A Grep of `answer` over `vault/wiki/rules/rule-orchestration.md` counted 8 lines. The hits on lines 38, 42, 44 and 46 that name a reply of `case-guppi`, the file it writes, or what the check stored from that file enter Case 651.1 as fourteen `replace` pairs, the first reply on an item from which a round may come among them. Line 32 names the person's answer and line 56 the main agent's answer to a refusal, so they stand. Lines 84 and 94 are History. The other hits on lines 38 and 46 name the person's answers, `case-guppi` answering as a verb, or the recommended answer of a question, the option a round recommends, and they stand.
>
> What the frame showed. `estimate-orchestration-shows-the-built-case` already calls the reply "the summary" and reads the showing that the new words describe, so it checks 651.1 and its Criterion stands. `estimate-orchestration-defers-in-one-reply` speaks of "a fence tagged `then` with one `defer` item per target", which the example of 651.3 bears out, so it stands. `estimate-orchestration-signs-a-batch-together` keeps its own words "an answer of a `case-guppi`", which the new page text does not make false, and `estimate-orchestration-forwards-a-discussion-question` keeps "the answer" for the `**Fact:**` reply the page now calls "that reply", with the same meaning. `estimate-prespec-gathers-the-answers-after-findings` sets the loop of `rule-prespec` whose steps the batch sentence of `orchestration.md` takes, which 651.1 rewords. Its words "while an answer is out" and "until every `case-guppi` it sent has answered with its Case" keep their meaning beside the new words of the page. Its line on "the showing that `vault/wiki/orchestration.md` sets" stays true, and that is the showing the example of 651.2 shows. So its Criterion stands. `estimate-guppi-tests-green` says that a skipped test is not a failure, so `make test` stays green while the new tests of `tests/test_orchestration.py` skip, and it stands. `estimate-orchestration-loaded`, `estimate-case-protocol-loaded` and `estimate-ratification-loaded` say that no paragraph of `orchestration.md` repeats one of `case-schema.md` or `ratification.md`. The new paragraphs and examples are worded apart from the example of `case-schema.md`, with another subject and other ledger lines. The checks the examples pass are not changed: `estimate-case-check-refuses-text-outside-the-list` and `estimate-spec-write-writes-a-defer` stand. The tests read text that lands only at the librarian's generate and render. `rule-retro` lets no red test pass, so, as the person chose and as `tests/test_case_schema.py` does, each test skips with a reason while the page holds no block of its tag. A Case of a later session removes the skips after the readings pass.
>
> The searches this Case rests on. A Grep of `rule-orchestration|orchestration\.md` over the repository root, with the glob `!**/decisions/** !**/raw/** !**/archive/** !**/log.md !**/brief.md`, printed 38 files. I read each hit outside History lines, and none says something that this Case makes false. A Grep of `short form|the summary` over `vault/wiki/rules/` printed 6 files: `rule-orchestration`, `rule-case-protocol`, `rule-spec-write`, `rule-case-build`, `rule-decisions-schema` and `rule-compact-recall`. Over `.claude/` it printed `.claude/agents/case-guppi.md`. `rule-spec-write` sets how the hook reads a short-form defer, and it is named in `given` of 651.3 and unchanged. `rule-case-build` and the agent file set the summary that `case-guppi` writes, a moment before the main agent's showing, and they stand. `rule-case-protocol` and `rule-decisions-schema` point to `orchestration.md` for the short form, and `rule-compact-recall` speaks of the summary of a compaction. A Glob `vault/**/*example*` printed `vault/wiki/lessons/lesson-wait-what-invents-an-example.md` and `vault/wiki/estimates/estimate-case-protocol-example-passes-the-check.md`, so both new slugs are free. Both new Estimates carry a `ref`, so the vault query of `ask-guppi` was not run. The Insight is set `actioned` with `addressed_by: decision-case-651.3`, the bare form that case 636 used. The cascade of `generate` then archives its `clustered` children, among them `lesson-case-build-closes-a-sprint-item-without-the-sprint-page` and `lesson-case-build-splits-a-case-whose-line-stands`. A new lesson of the same kind reopens it.
>
> The check sent back notes, and they stand. Three `then` lines of 651.3 share most of their words with 651.2: the paragraph before the block, the test that holds no copy, and the skip. Each sub-case still sets its own promise. 651.2 covers the block tagged `showing` and the `Stop` check of `rule-case-check`. 651.3 covers the block tagged `defer` and the hook of `rule-spec-write`.
>
> Not done:
> - `rule-case-check`, `rule-spec-write`, the other Estimates and the code keep the word "answer", the refusal of the `Stop` comparison included.
> - The acknowledging reply gets no example.
> - The tests keep their skips until a Case of a later session removes them.

> **problem:**
> `orchestration.md` calls the reply of `case-guppi` "the answer" while that reply is now a summary, and it states the `ratification` of a showing and the `then` block of a short-form defer in words that the main agent has twice read into a form the checks refuse. The question was which words replace "the answer", how far the change reaches, how the two forms are shown and checked, and what happens to the Insight.

> **recommend:**
> - **Which word replaces "the answer"**
>   - Recommended: (a) a word for each meaning: the summary where the main agent reads the reply of `case-guppi`, the file where the Case is sent, and the text the check stored where the Spec hook reads; a round and a Fact reply keep their names.
>   - Answer: agreed, (a).
> - **How far the change reaches**
>   - Recommended: (a) only `orchestration.md`; the other pages and the code keep their words.
>   - Answer: agreed, (a).
> - **How the page states the two forms**
>   - Recommended: (b) an example checked by a test that runs the checks over it and fails on any refusal.
>   - Answer: agreed, (b).
> - **Which forms the page covers**
>   - Recommended: (a) the `ratification` of a showing and the `then` block of a short-form defer, the two the lessons name.
>   - Answer: agreed, (a).
> - **One check or one per form**
>   - Recommended: (a) three sub-cases: the rewording, checked by `estimate-orchestration-shows-the-built-case` as it stands; the example of a showing with a new Estimate; the example of a short-form defer with a new Estimate.
>   - Answer: agreed, (a).
> - **What the test does before the page holds the example**
>   - Recommended: (a) skip until the render, with a reason that names `orchestration.md`; a Case of a later session removes the skip after the readings pass.
>   - Answer: agreed, (a).
> - **What the example of a showing shows**
>   - Recommended: (a) a parent with two sub-cases: the heading, a list of two items, one `ratification` quote block with the lines of both, the horizontal rule and the agent's own text.
>   - Answer: agreed, (a), with the heading of the example in English, since the example is part of the documentation.
> - **What happens to the open Insight**
>   - Recommended: (a) mark it `actioned`, addressed by this Case.
>   - Answer: agreed, (a).

### Case 651.1 — orchestration.md names the summary, the file and the stored text of case-guppi

> **given:**
> `rule-orchestration`: the rule whose Render is `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: what the main agent does, loaded by `/hi`.
> **＋** `rule-case-build`: the summary, the round and the `**Fact:**` reply of `case-guppi`. Unchanged.
> **＋** `rule-case-check`: its check stores the text of the file of a Case. Unchanged.
> **＋** `rule-spec-write`: its hook writes a Case from that stored text. Unchanged.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.

> **when:**
> The main agent reads `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, to show a summary, a round or a `**Fact:**` reply of `case-guppi`.

> **then:**
> The page calls the reply of `case-guppi` that opens with `**Built:**` the summary, and the main agent writes the list and the `ratification` of a showing from the summary and sends back a summary in which a Case gives no Estimate.
> **＋** The page calls the Case sent at a showing and at a showing again the file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and what the hook of `rule-spec-write` writes the text the check of `rule-case-check` stored from that file.
> **＋** A reply of `case-guppi` with no first line `**Built:**` and no first line `**Fact:**` is a round, and the page names it so.
> **－** No sentence of `vault/wiki/orchestration.md` calls a reply of `case-guppi` the answer; the person's answers keep that word.

```then
update:
- slug: rule-orchestration
  replace:
  - old: the main agent shows that answer translated into {{chat_lang}}
    new: the main agent shows that reply translated into {{chat_lang}}
  - old: The agent shows the Case of the answer at every showing
    new: The agent shows the Case `case-guppi` built at every showing
  - old: an item per Case and sub-case of the answer, its id
    new: an item per Case and sub-case of the summary, its id
  - old: of every Case of the list as the answer holds them, never its
    new: of every Case of the list as the summary holds them, never its
  - old: an answer in which a Case gives no such Estimate goes back
    new: a summary in which a Case gives no such Estimate goes back
  - old: shows the `ratification` as the answer holds it (case 452.4)
    new: shows the `ratification` as the summary holds it (case 452.4)
  - old: an answer with no first line
    new: a reply of `case-guppi` with no first line
  - old: with the number of the answer
    new: with the number the round gives it
  - old: Its new answer is sent again whole, in its file
    new: Its new file is sent again whole
  - old: writes a Case only from its stored answer after a reply
    new: writes a Case only from the text the check of `rule-case-check` stored from its file after a reply
  - old: a round of questions of `case-guppi`, translated from the answer,
    new: a round of questions of `case-guppi`, translated,
  - old: the ledger lines of `ratification` stand in the chat as the answer holds them
    new: the ledger lines of `ratification` stand in the chat as the summary holds them
  - old: while an answer is out
    new: while a `case-guppi` of the batch has not replied
  - old: a round may come at the first answer on an item
    new: a round may come at the first reply on an item
  change: the reply of case-guppi is named the summary, the Case sent is its file, and the Spec hook reads the text the check stored from that file (case 651.1)
```

```tasks
- [x] update `rule-orchestration`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
```

### Case 651.2 — orchestration.md shows a showing by an example the Stop check passes

> **given:**
> `estimate-orchestration-showing-example-passes-the-check`: the new check of the example of a showing.
> **＋** `rule-orchestration`: the rule whose Render is `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: the page that holds the example.
> **＋** `tests/test_orchestration.py`: the new test that runs the check over the example.
> **＋** `guppi/casecheck.py`: `outside_the_list`, `showings` and `against_store`, the functions the `Stop` check runs over a reply that shows a Case.
> **＋** `rule-case-check`: its `Stop` check of a showing. Unchanged.
> **＋** `rule-one-judgment-one-implementation`: one test runs the example and the check over the same input.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `showing` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it the functions of `guppi/casecheck.py` that the `Stop` check of `rule-case-check` runs over a reply that shows a Case, with a store whose sub-cases hold the ledger lines the example's `ratification` gives them.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## Showing and signing a Case`, one block tagged `showing`: a reply that shows a Case with two sub-cases, its heading, one list with an item per sub-case, one `ratification` and the agent's own text after one horizontal rule.
> **＋** The `ratification` of the example is a quote block: the line `> **ratification:**`, then the fence and the ledger lines of both sub-cases, each line opening with `> `.
> **＋** The example is in English; the paragraph before the block says that in the chat the heading, the names and the short texts stand in the language of the chat, that the file goes by `SendUserFile` in the same reply, and that the example passes the `Stop` check of `rule-case-check`, which is the source of the limits; it lists no other limit.
> **＋** The check finds no text outside the list and the `ratification`, reads the `ratification` as the showing of each sub-case it names, and finds no difference from the store, and the test passes.
> **＋** The example with the lines of its fence not quoted gives the finding of a text outside the list, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `showing`, the test is skipped with a reason that names the file; a Case of a later session removes the skip after the reading of `estimate-orchestration-showing-example-passes-the-check` passes.

`````then
create:
- slug: estimate-orchestration-showing-example-passes-the-check
  ref: rule-orchestration
  kind: QA
  purpose: Whether the example of a showing in orchestration.md passes the Stop check of a reply that shows a Case, so the form the main agent copies stays a form the check accepts
  method: uv run pytest tests/test_orchestration.py -k showing_example, passed and not skipped
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-orchestration
  replace:
  - old: Retro counts the unticked (case 59.3).
    new: |-
      Retro counts the unticked (case 59.3).

      ### A showing, by example

      The block below is the text of a reply that shows a Case with two sub-cases, written after the `SendUserFile` call that sends its file. Its `ratification` is a quote block: the fence and each ledger line stand on lines that open with `> `, while the summary of `case-guppi` gives the same lines in a plain fence. In the chat the heading, the names and the short texts stand in {{chat_lang}}; the example is in {{documentation_lang}}, as the vault is. A test runs over the example the functions that the `Stop` check of `rule-case-check` runs over a reply that shows a Case, and fails on any refusal, so the example keeps to that check as the check stands (case 651.2). Copy its form; a refusal of the check names the limit a showing broke.

      ````showing
      ## Case 7 — Members get a reminder before a booking

      - 7.1 — The reminder goes out a day before. Done when `estimate-booking-sends-a-reminder` passes: a test books a slot and finds one reminder queued a day before it.
      - 7.2 — A cancelled booking sends no reminder. Done when `estimate-booking-skips-a-cancelled-reminder` passes: a test cancels a booked slot and finds no reminder queued.

      > **ratification:**
      > ```
      > - decision[case 7.1][create][estimate-booking-sends-a-reminder]{ref:entity-booking}{tags:booking,email}
      > - decision[case 7.1][update][entity-booking]{ref:entity-booking}
      > - decision[case 7.2][create][estimate-booking-skips-a-cancelled-reminder]{ref:entity-booking}{tags:booking,email}
      > ```

      ---

      Do you ratify 7.1 and 7.2, or only some of them?
      ````
  change: the reply that shows a Case has an example that a test runs the Stop check of rule-case-check over (case 651.2)
`````

```tasks
- [x] create `estimate-orchestration-showing-example-passes-the-check`
- [x] update `rule-orchestration`
- [x] `tests/test_orchestration.py`: reads the first block tagged `showing` from `vault/wiki/orchestration.md` by `fence_opening` and `closes_fence` of `guppi/materialize.py`, its lines as they stand, and skips with a reason that names the file while it holds none. It builds a store whose entry for each sub-case id that a ledger line of the example names holds that sub-case's heading and a `ratification` of its own lines, read by `fence_ledger_lines`. Tests `-k showing_example`: `outside_the_list` finds nothing; `showings` reads a showing for each sub-case id and `against_store` finds no difference for each; the example with the `> ` taken off the lines of its fence makes `outside_the_list` return a line.
- [ ] read `estimate-orchestration-showing-example-passes-the-check`
```

### Case 651.3 — orchestration.md shows a short-form defer by an example the Spec hook writes

> **given:**
> `estimate-orchestration-defer-example-passes-the-hook`: the new check of the example of a short-form defer.
> **＋** `rule-orchestration`: the rule whose Render is `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: the page that holds the example.
> **＋** `tests/test_orchestration.py`: the test that runs the hook over the example.
> **＋** `guppi/ratified.py`: `write_defers` and `key_judge`, what the `Stop` hook runs over a defer-only Case.
> **＋** `rule-spec-write`: its hook writes a short-form defer under `## Deferred`. Unchanged.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept`: the Insight this Case acts on.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `defer` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it, as the text of a reply, the functions of `guppi/ratified.py` that the `Stop` hook of `rule-spec-write` runs over a defer-only Case, in a temporary project that holds the schema files of the vault and a plan file, with one `defer` record for each item of the example.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## The short form — deferred decisions`, one block tagged `defer`: a Case in the short form with its heading, `context`, `problem` and a fence tagged `then` whose `defer:` holds a list, one item per target, each item opening with `- slug:` and carrying `type` and `purpose`.
> **＋** The paragraph before the block says that the reply that shows the Case carries its `LEDGER` block with one `defer` line per item, and that the example passes the `Stop` hook of `rule-spec-write`, which is the source of the limits; it lists no other limit.
> **＋** The hook writes the example under `## Deferred` of the plan file with no error, and the test passes.
> **＋** The example with its `defer:` items written as one mapping gives the error that no fence tagged `then` holds its `defer` items, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the hook from `guppi/ratified.py`, and holds no copy of either.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stands `actioned`, addressed by this Case.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `defer`, the test is skipped with a reason that names the file; a Case of a later session removes the skip after the reading of `estimate-orchestration-defer-example-passes-the-hook` passes.

`````then
create:
- slug: estimate-orchestration-defer-example-passes-the-hook
  ref: rule-orchestration
  kind: QA
  purpose: Whether the example of a short-form defer in orchestration.md passes the Stop hook that writes a defer-only Case into the Spec, so the form the main agent copies stays a form the hook accepts
  method: uv run pytest tests/test_orchestration.py -k defer_example, passed and not skipped
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-orchestration
  replace:
  - old: A `create`, `update` or `delete` at Retro waits for the next Plan Mode (cases 52.2, 56, 59.5).
    new: |-
      A `create`, `update` or `delete` at Retro waits for the next Plan Mode (cases 52.2, 56, 59.5).

      ### A short-form defer, by example

      The block below is a deferred decision in the short form as a reply shows it; the same reply carries its `LEDGER` block, with one `defer` line per item. A test runs over the example the functions that the `Stop` hook of `rule-spec-write` runs over a defer-only Case, and fails on any error, so the example keeps to that hook as the hook stands (case 651.3). Copy its form; an error of the hook names the limit a short Case broke.

      ````defer
      ## Case 8 — The export of old bookings put off

      > **context:**
      > The person put off the export of bookings older than a year at the close of Plan Mode. No Case of this session sets the form of the export.

      > **problem:**
      > No Case of this session decides how an owner exports old bookings.

      ```then
      defer:
        - slug: entity-booking-export
          type: entity
          purpose: "Lets an owner export the bookings older than a year; put off at the close of Plan Mode"
      ```
      ````
  change: the short form of a defer has an example that a test runs the Stop hook of rule-spec-write over (case 651.3)
- slug: insight-workflow-case-schema-silent-on-what-the-scripts-accept
  set:
    status: actioned
    addressed_by: decision-case-651.3
  change: 'actioned: case-schema.md and orchestration.md show the forms case-guppi and the main agent write by examples that a test runs the checks over (cases 646, 651)'
`````

```tasks
- [x] create `estimate-orchestration-defer-example-passes-the-hook`
- [x] update `rule-orchestration`
- [x] update `insight-workflow-case-schema-silent-on-what-the-scripts-accept`
- [x] `tests/test_orchestration.py`: reads the first block tagged `defer` from `vault/wiki/orchestration.md` the same way, and skips with a reason that names the file while it holds none. It seeds a temporary project with the `schema.yaml` files of `vault/wiki/` and an empty plan file, and builds one `defer` record of the Case of the example for each slug of its `then` items. Tests `-k defer_example`: `write_defers` with `key_judge` returns no error and the plan file holds the Case under `## Deferred`; the example with its items rewritten as one mapping under `defer:` returns the error `no fence tagged then with its defer items`.
- [ ] read `estimate-orchestration-defer-example-passes-the-hook`
```

## Case 652 — The test of the schema example fails when the page holds no example

> **context:**
> `tests/test_case_schema.py` reads the example Case from `vault/wiki/case-schema.md` and runs over it the check that the `SubagentStop` hook of `rule-case-check` runs over the file of a Case. Case 646 made the test skip, with a reason that names the file, while the page held no block tagged `case`, because the example reached the page only at the librarian's render. The render has put the example there, and at the `/hi` of this session the reading of `estimate-case-protocol-example-passes-the-check` passed with both tests run and none skipped. The skip still stands in the code. A skip leaves `make test` green, so a later render that lost the block or changed its tag would leave the example unchecked with no one told. The person chose that the test fails, with a message that names the file, when the page holds no block tagged `case`.
>
> The last `－` line of the Criterion of `estimate-case-protocol-example-passes-the-check` says the test skips, so this Case makes it false and replaces the Criterion whole: the same lines, with that line rewritten to say both tests fail and none is skipped. The page goes `pending`. The reading is taken at the `/hi` of a later session, since the ledger hook refuses a reading of an Estimate that a decision line of this session updates (case 428.1). Its `purpose` says nothing of the skip and stands. Its `method` reads "passed and not skipped", which stays true when no skip remains, so it stands. The test only goes red and loses nothing, so it keeps no old form. `estimate-guppi-tests-green` says that a skipped test is not a failure, and that line stands: after this Case the test fails rather than skips, which is the behaviour the person chose. Case 651 of this session gives `tests/test_orchestration.py` skips of the same kind. This Case does not touch them, and it does not change `rule-case-protocol` or the page.
>
> The search this Case rests on. A Grep of `test_case_schema|estimate-case-protocol-example-passes-the-check` over the repository root, with the glob `!**/decisions/** !**/raw/** !**/log.md !**/brief.md`, printed 3 files: `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/estimates/estimate-case-protocol-example-passes-the-check.md` and `tests/test_case_schema.py`. On `rule-case-protocol` the hits are the `estimates` field and a History line, which stand. The other two enter the Case.
>
> Not done:
> - The skips of `tests/test_orchestration.py` that Case 651 sets stay until a later Case removes them.

> **problem:**
> `tests/test_case_schema.py` still skips when `vault/wiki/case-schema.md` holds no example, though the example now stands there and its reading passed. A lost example would go unchecked while the tests stay green. The question was what the test does when the page holds no example.

> **recommend:**
> - **What the test does when the page holds no example**
>   - Recommended: (a) fail, with a message that names the file.
>   - Answer: agreed, (a).

> **given:**
> `tests/test_case_schema.py`: the test that runs the check over the example.
> **＋** `estimate-case-protocol-example-passes-the-check`: its Criterion is replaced whole.
> **＋** `vault/wiki/case-schema.md`: the page that holds the example, rendered from `rule-case-protocol`. Unchanged.
> **＋** `rule-case-protocol`: the rule whose Render is that page. Unchanged.
> **＋** `guppi/casecheck.py`: the check of the Cases of a file, which the test imports. Unchanged.
> **＋** `rule-case-check`: its `SubagentStop` hook runs that check over the file of a Case. Unchanged.

> **when:**
> `tests/test_case_schema.py` runs under `uv run pytest`. It reads the block tagged `case` in `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, and runs over it the function of `guppi/casecheck.py` that the `SubagentStop` hook of `rule-case-check` runs over the Cases of a file. It runs in a temporary project that holds the schema files of the vault and the pages the example updates.

> **then:**
> `vault/wiki/case-schema.md` holds, under its own heading after its `## Language` section, one block tagged `case`: one Case with sub-cases, in the chat form that `case-guppi` writes into its file.
> **＋** The example holds a `create` and an `update` with their sub-points, a `replace` pair whose values hold a backtick in spans padded by one space, a `set` in a fenced block, an `update` of an Estimate whose Criterion it replaces, a read line for each Estimate it creates or replaces, and its ledger lines in a quoted fence under `ratification`.
> **＋** The example's `context` says what the sentence around the match of its `replace` pair names.
> **＋** The paragraph before the block says that the example passes the check of the `SubagentStop` hook of `rule-case-check`, and that the check, not the paragraph, is the source of the limits; it lists no limit.
> **＋** The check gives the example no finding and no note, and the test passes.
> **＋** A change of the check that gives the example a finding or a note fails the test, which prints it.
> **＋** The test reads the example from `vault/wiki/case-schema.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/case-schema.md` holds no block tagged `case`, both tests of `tests/test_case_schema.py` fail with a message that names the file; no test of the file is skipped.
> **－** The Spec example and the limits that the prose of `vault/wiki/case-schema.md` already states stay as they are.

```then
update:
- slug: estimate-case-protocol-example-passes-the-check
  set:
    status: pending
  change: the Criterion replaced whole — the test fails, not skips, when case-schema.md holds no block tagged case (case 652)
```

```tasks
- [x] update `estimate-case-protocol-example-passes-the-check`
- [x] `tests/test_case_schema.py`: `example` calls `pytest.fail` with a message that names the file, in place of `pytest.skip`, when the page holds no block tagged `case`; the module docstring says the test fails then and drops the sentence on the skip.
- [ ] read `estimate-case-protocol-example-passes-the-check`, at the `/hi` of a later session
```

## Case 654 — The synthesis names a page whose text it reads to judge a cause

> **context:**
> At the synthesis the librarian compares the `root_cause` of each new lesson with the index lines of the lessons and the Insights, and groups the lessons that share a cause. `estimate-synthesis-clusters` checks this step. Its reading at the `/hi` of session 0311 (line L1 of `raw/2026-10-05/0311/ledger.md`) failed on one clause, which says every lesson page read at synthesis is named in the report with its outcome. In the librarian run of session 0109, call 13 printed the frontmatter fields of six lesson pages and three Insights: their `status`, `insight`, `children` and `tags`, without `root_cause` or `pattern` and without the text of any section. The librarian used these fields to see which lessons were already grouped and which lessons each Insight holds, and its report named none of the six lesson pages. The frame of the librarian, the Render of `rule-documentation`, names a page in the report only when the librarian opens it to judge a duplicate, a shared root cause or a failed script, and says a page opened for any other need is not named (case 567.1). The `－` clause of `estimate-documentation-completes` says the same of a page read for its field names or any other need. The clause that failed asks for more than the frame does. The person chose to narrow the check: the report names a page whose text is read to judge a shared cause, and a read of frontmatter fields alone is not named. The new Criterion leaves out on purpose the clause that names every lesson page read at synthesis. In its place, a page is named when the librarian opens it to judge a shared root cause, which is the reason the frame gives. A read of the Trigger, Root cause, `root_cause`, Pattern or `pattern` of a page outside the two Greps counts as such an opening, whether the librarian reads the body or the frontmatter. A `－` line stands beside it: a read of only `status`, `insight`, `children` and `tags`, made to learn which lessons are grouped or which lessons an Insight holds, is not named. The pre-spec run found that a first wording judged only by which part of the page was read. Under that wording a read of `root_cause` alone, made to judge a shared cause, went unnamed, although the frame names it. The present wording judges by the reason, as the frame does, and lists the fields that need no name. Every other line is carried word for word. The Render of `rule-synthesis` already asks the librarian to read the Trigger and Root cause of a candidate and name the page with its outcome, so it agrees with the new clause and stands. The frame of `rule-documentation` and the Criterion of `estimate-documentation-completes` stand for the same reason. The Criterion of `estimate-synthesis-keeps-actioned-by-the-mark` is about `addressed_by` and `status` on an Insight, not about reads, so it stands. The Case creates no page, so no vault query is needed. A Grep `estimate-synthesis-clusters` over the repository, with the glob `!**/decisions/** !vault/archive/** !vault/raw/**`, printed 4 files: `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-synthesis.md` and `vault/wiki/insights/insight-librarian-frame-omits-required-reads.md`. The hit in `rule-synthesis` is its `estimates` field, which stands. The hit in the Insight is its Proposal, which names a past reading of the Estimate and stays true. The brief and the log are not read. The page has no `purpose` field, and its `method` names only when the reading is taken, not the old promise, so neither is set anew.

> **problem:**
> The Criterion of `estimate-synthesis-clusters` asks the librarian to name in its report every lesson page it reads at synthesis. The frame of the librarian and `estimate-documentation-completes` say a page read for anything but a judgment is not named. The check fails a run that kept its frame.

> **recommend:**
> - **How the clash between the check and the librarian's instructions is settled**
>   - Recommended: (a) narrow the check: name only a page whose text is read to judge a shared cause, a lesson's Trigger and Root cause or an Insight's Pattern; a read of frontmatter fields alone is not named; only the Criterion of `estimate-synthesis-clusters` changes.
>   - Answer: agreed, (a).

> **given:**
> `estimate-synthesis-clusters`: its Criterion is replaced whole.
> **＋** `rule-synthesis`: the rule the Estimate checks, whose Render asks for the Trigger and Root cause of a candidate.
> **＋** `rule-documentation`: the frame of the librarian, in `.claude/agents/librarian-guppi.md`, which says which reads the report names.
> **＋** `estimate-documentation-completes`: its clause on the reads that need no name stands.
> **＋** `vault/wiki/lessons/` and `vault/wiki/insights/`: the pages the synthesis compares and reads.
> **＋** `vault/archive/`: the archive the synthesis does not need.

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The brief names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, with the number of lines each printed.
> **＋** The brief gives one line for each lesson entry: its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every page the librarian opens at synthesis to judge whether a lesson shares its root cause is named in the report with the outcome: the Insight it joined, or none and why. A read of its Trigger, Root cause, `root_cause`, Pattern or `pattern` outside the two Greps is such an opening.
> **＋** A lesson without a pair stays `new`, and its line in the brief is no flag.
> **－** A read at synthesis of only the fields `status`, `insight`, `children` and `tags` of a page under `vault/wiki/lessons/` or `vault/wiki/insights/`, made to learn which lessons are grouped or which lessons an Insight holds, is not named in the report and fails nothing here.
> **－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line until the close of its sprint, and the flag of such a read is the promise of `estimate-documentation-completes`.

```then
update:
- slug: estimate-synthesis-clusters
  set:
    status: pending
  change: the Criterion replaced whole — a page is named in the report when it is opened to judge a shared cause; a read of only its status, insight, children and tags is not (case 654)
```

```tasks
- [x] update `estimate-synthesis-clusters`
- [ ] read `estimate-synthesis-clusters`
```

## Case 655 — The check of the searches of ask-guppi at pre-spec leaves Decision pages to the check of every agent

> **context:**
> At `/pre-spec` the main agent sends the plan to `ask-guppi`, which searches the vault for findings. `estimate-ask-searches-at-prespec` checks how it searches: the Grep of the rules first, one Grep per other category, then further searches as each finding needs, a count over Decision pages not run again, and no search that reaches `vault/wiki/decisions/` but for the two reasons of its frame. The reading at the `/hi` of session 0109 (L9 of `raw/2026-10-05/0109/ledger.md`) failed: call 16 of agent a390781c7f1241c18 ran a Grep over `vault/wiki` with the glob `!decisions/**`, which left nothing out, and printed 29 lines of Decision pages. Case 640 put `.claude/rules/search-leaves-out-decisions.md` in place with a glob that works and created `estimate-search-leaves-out-decisions-in-every-agent`, which reads the same promise for the main agent, `ask-guppi` and `case-guppi` under the stricter letter of that file. Case 649 deferred this Estimate in session 0311. The `/pre-spec` of session 0311 (transcript 6d53e05d) was the first after both renders. Its three ask-guppi runs, a055d35695650c13f, af56f988c579ddc06 and af7cde916f5b24293, each opened with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` and then grepped the other categories, as `case-guppi` saw in their transcripts. The only reading of `estimate-search-leaves-out-decisions-in-every-agent`, at the `/hi` of this session (L10 of `raw/2026-10-05/1343/ledger.md`), found that no Grep of these runs printed a line of a Decision page, and failed. Among its causes, ask-guppi af56f988c579ddc06 ran a Grep at the repository root with the glob `*.py` and no `!**/decisions/**`, and case-guppi a1cf96ac9df5edd1c read `decision-case-432` for neither reason of its frame; the rest were Greps of the main agent and of case-guppi without the exclusion. The clause this Case hands to that Estimate is thus read there under a stricter letter, and that Estimate stands failed until a Case of its own. The person chose to drop the clause on Decision pages from this Estimate and leave it to `estimate-search-leaves-out-decisions-in-every-agent`, whose Criterion already covers `ask-guppi` and stands. The Criterion is replaced whole: its `when` and its first three lines of `then` are carried word for word, and the old `－` line, that no Grep or Read of the agent reaches `vault/wiki/decisions/` but for the two reasons, is left out on purpose; a new `－` line says that clause is outside this promise. The `purpose` and the `method` of the Estimate state the old promise and the old runs, so the same `update` sets both anew. A reading of an Estimate that a decision line of this session updates waits for a later session, and the ledger hook refuses it (case 428.1). So the reading is taken at the `/hi` of the next session. The new `method` names its moment by its kind, as `rule-estimates-schema` asks of a method by hand: the calls of ask-guppi at a `/pre-spec` after the render, read at the `/hi` of a later session. The first reading takes the three ask-guppi runs of the `/pre-spec` of session 0311, as the person chose. The decision line carries `{supersedes:case 649}`, which retires the defer. `.claude/agents/ask-guppi.md` and the Render of `rule-ask` still forbid a search of Decision pages but for the two reasons; the Case does not touch them, and they stay true. The Criterion of `estimate-ask-finds` is about the form of the answer, not the searches, and stands. The Case creates no page, so no vault query is run. A Grep `estimate-ask-searches-at-prespec` over `vault/wiki` with the glob `!**/decisions/**` printed 4 files: `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-ask-finds.md` and `vault/wiki/rules/rule-ask.md`. The hit in `estimate-ask-finds` is a History line. The hits in `rule-ask` are its `estimates` field, which stands, and a History line. The brief and the log are not read.

> **problem:**
> `estimate-ask-searches-at-prespec` stands failed and deferred. Its clause on Decision pages repeats the promise of `estimate-search-leaves-out-decisions-in-every-agent`, and its reading after the fix by case 640 has not been taken.

> **recommend:**
> - **Which runs the new reading reads**
>   - Recommended: (a) the runs of the previous session's `/pre-spec`, read in this session.
>   - Answer: (a), the runs of the previous session; the time of the reading is set by the later question When the reading is taken, and over which runs.
> - **Whether the check keeps its clause on Decision pages**
>   - Recommended: (a) keep the clause as it stands.
>   - Answer: (b), drop the clause and leave Decision pages to `estimate-search-leaves-out-decisions-in-every-agent`.
> - **When the reading is taken, and over which runs**
>   - Recommended: (a) the `/hi` of the next session reads the runs of the previous session's `/pre-spec`.
>   - Answer: agreed, (a).

> **given:**
> `estimate-ask-searches-at-prespec`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-ask`: the rule the Estimate checks, rendered into `.claude/agents/ask-guppi.md`.
> **＋** `.claude/agents/ask-guppi.md`: the frame of `ask-guppi`, which the Criterion reads.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill whose questions the main agent sends.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the check that keeps the clause on Decision pages.
> **＋** `rule-estimates-schema`: the rule on how a method by hand names its moment.
> **＋** `vault/wiki/rules/`: the folder of the rules, whose Grep the agent runs first.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages, left to the other check.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
> **＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
> **－** Whether a Grep or Read of the agent reaches `vault/wiki/decisions/` is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.

```then
update:
- slug: estimate-ask-searches-at-prespec
  set:
    status: pending
    purpose: Whether ask-guppi at /pre-spec starts with the Grep of the rules and one Grep per other category, then greps and reads as each finding needs, a count over Decision pages not run again
    method: 'by hand at the /hi of a later session: the Grep, Glob and Read calls of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md, read in its agent transcript against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the clause on Decision pages left to estimate-search-leaves-out-decisions-in-every-agent; purpose and method set anew (case 655)
```

```tasks
- [x] update `estimate-ask-searches-at-prespec`
- [ ] read `estimate-ask-searches-at-prespec`
```

## Case 656 — The builder of a Case reads this project's saved transcripts with no prompt

> **context:**
> `case-guppi` builds each Case in the mode `permissionMode: acceptEdits` of its agent file, set by case 645.1, so it writes the file of its Case with no prompt while the session is in Plan Mode. The allow list of `.claude/settings.json`, the Render of `rule-permissions`, holds only Edit and Write rules for the session's working files, and no rule for a read outside the project. Claude Code keeps the transcripts of past sessions outside the project, under `~/.claude/projects/c--PROJECTS-GUPPI/`. In this session, as the main agent read in the subagent transcripts, the builders of Cases 654 and 655 searched the transcripts of sessions 0109 and 0311 there to check a past reading, and the person was asked to allow those searches. The person first proposed to remove `acceptEdits`, since the builder ran with no mode line before. Before case 645.1 the builder wrote no file. Without the line it runs in Plan Mode, where Claude Code lets an agent change only its plan file, so its write of the Case file would ask or be refused. The person then chose to keep `acceptEdits` and allow reads of this project's transcript folder alone.
>
> The Case adds `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)` to the allow list. This rests on the Claude Code docs as a guide agent paraphrased them for the main agent; this Case fetched nothing. On that reading, an allow rule with a home path `~/` is valid, a `Read` rule applies to Grep and Glob best-effort, and the docs do not say whether `acceptEdits` alone asks before a read outside the working folder. So the live check is the person's word in the next session on whether a search of `case-guppi` in that folder asked. If it still asks, the person's word fails the reading, and a later Case can add the folder through `permissions.additionalDirectories` instead. The rule applies to every agent of this project, the main agent too. The `/hi` step that takes a reading from the transcript of an earlier session reads the same folder. The person chose a check on the searches of the builder, so the new Criterion judges only those, and the new sentence of `rule-permissions` gives the builder's searches as the reason and says only that the rule covers the other agents too. Whether a read of the main agent at `/hi` still asks is left unchecked, and this Case does not promise it. The Criterion of `estimate-hi-takes-its-readings` judges what `/hi` reads and writes, not whether the client asked, so it stands. The Purpose of `rule-settings` says the file carries what may be written without a question, which the block of `rule-permissions` owns; a pair on it adds reads, as the ask-guppi run at pre-spec found. The purpose of `rule-permissions` and the first sentence of its Purpose say that the list allows writes of the session's working files and nothing else, so this Case sets the purpose anew and adds a sentence on the transcripts. The Criterion of `estimate-permissions` lists the allow list whole, so it is replaced whole. Its `method` names one live probe, a Write of `work.md`, so the same `update` sets the method anew with the new probe. The page has no `purpose` field. The Case leaves `rule-case-build` and `estimate-case-build-writes-the-case` as they stand, because the mode line stays `acceptEdits`. The Case also leaves the guard of Case 650, because it judges only writes. The Case creates no page, so no vault query was run.
>
> The searches this Case rests on. A Grep of `rule-permissions` over the repository, with the glob `!**/decisions/** !vault/archive/** !vault/raw/**`, printed 9 files: `vault/wiki/brief.md`, `.claude/skills/hi/SKILL.md`, `vault/wiki/log.md`, `vault/wiki/insights/insight-session-vault-knowledge-not-loaded.md`, `vault/wiki/rules/rule-permissions.md`, `vault/wiki/rules/rule-settings.md`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/estimates/estimate-permissions.md` and `vault/wiki/estimates/estimate-settings.md`. `rule-permissions` and `estimate-permissions` enter the Case. `.claude/skills/hi/SKILL.md` and its Render page `rule-skill-hi` name the rule for the write of `frontier.md` in Plan Mode, which stays true. The hits in `rule-settings` and `estimate-settings` name the rule as a child of `settings.json` and its place in the order, which stays true; the Purpose of `rule-settings` enters the Case for the reason above. The hit in the Insight is a History line. The brief and the log are not read. A Grep of `\.claude/projects|\.claude\\\\projects` over the repository, with the glob `{vault/wiki/rules/**,.claude/**} !**/decisions/**`, printed nothing, so no rule or harness file sets what happens at a read of that folder.
>
> The check sent back notes, and they stand. Three lines of the old Criterion of `estimate-permissions` are not carried word for word, and each changed on purpose. The line on the allow list now ends with the new `Read` rule. The line on a prompt in Plan Mode was a `＋` line and is now a `－` line, and it names an edit of the main agent, so that a prompt on a search of `case-guppi` in the transcript folder fails the reading. The line on `deny` and `ask` now also says that no other path outside the project is on the list, and that no Edit or Write rule names the transcript folder.
>
> Not done: the folder name holds the path of this project on this machine; a clone at another path would need the rule changed.

> **problem:**
> A builder that searches the saved transcripts of past sessions stops on a permission prompt for each call. The question was how those reads stop asking, and whether the mode line of the builder stays.

> **recommend:**
> - **How the builder's reads of past transcripts stop asking you**
>   - Recommended: (a) allow reading this project's transcript folder by one allow rule in the project settings, and keep `acceptEdits`.
>   - Answer: none of the options; the person proposed to remove `acceptEdits`, since the builder ran with no mode line before and nothing asked, and to check that. The later question Whether to remove the builder's mode line, given that the builder now writes its own file took this up.
> - **Whether to remove the builder's mode line, given that the builder now writes its own file**
>   - Recommended: (b) keep the line and allow reading this project's transcript folder; the check is the person's word in the next session on whether a builder's search of past transcripts asked.
>   - Answer: agreed, (b).

> **given:**
> `rule-permissions`: the allow list of `.claude/settings.json` and why it holds what it holds.
> **＋** `estimate-permissions`: its Criterion is replaced whole.
> **＋** `.claude/settings.json`: the rendered settings of the project.
> **＋** `~/.claude/projects/c--PROJECTS-GUPPI/`: the saved transcripts of this project.
> **＋** `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`: the new allow rule for reading that folder.
> **＋** `.claude/agents/case-guppi.md`: the agent file with `permissionMode: acceptEdits`. Unchanged.
> **＋** `vault/raw/**`: the session folders that hold the working files on the allow list. Unchanged.
> **＋** `vault/wiki/brief.md`: the brief, on the allow list. Unchanged.
> **＋** `wiki/`: the live pages, none of them allowed but the brief. Unchanged.
> **＋** `cases/`: the folder of the Case files, off the allow list. Unchanged.
> **＋** `rule-spec-reconcile`: the guard that keeps the writes of `case-guppi` inside `cases/`. Unchanged.
> **＋** `tests/test_render.py`: the JSON case that fixes the shape of the block. Unchanged.
> **＋** `rule-settings`: its Purpose names what the block of `rule-permissions` carries.
> **＋** `estimate-hi-takes-its-readings`: the check of the reads of `/hi` from past transcripts. Unchanged.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or `case-guppi` calls Read, Grep or Glob on a saved transcript of this project under `~/.claude/projects/c--PROJECTS-GUPPI/`.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** `case-guppi` writes the file of its Case in the mode `permissionMode: acceptEdits` of `.claude/agents/case-guppi.md`, with no prompt in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/`.
> **＋** A Read, Grep or Glob of `case-guppi` under `~/.claude/projects/c--PROJECTS-GUPPI/` runs with no prompt, in Plan Mode too.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names `~/.claude/projects/c--PROJECTS-GUPPI/`.

```then
update:
- slug: rule-permissions
  set:
    purpose: Lets the session write its own working files and read this project's saved transcripts without asking, and nothing else
  replace:
  - old: Lets the session write its own working files without asking, and nothing else.
    new: Lets the session write its own working files and read this project's saved transcripts without asking, and nothing else.
  - old: and the guard of `rule-spec-reconcile` keeps it inside `cases/` (case 645.16).
    new: 'and the guard of `rule-spec-reconcile` keeps it inside `cases/` (case 645.16). The saved transcripts of this project, under `~/.claude/projects/c--PROJECTS-GUPPI/` outside the repository, are on the list for reading only: `case-guppi` checks a past reading in them, and a prompt on each of its searches buys nothing; the rule covers every agent of the project, and Claude Code applies a `Read` rule to Grep and Glob best-effort, and whether a search there still asks is the person''s word (case 656).'
  - old: '"Write(vault/wiki/brief.md)"'
    new: |-
      "Write(vault/wiki/brief.md)",
            "Read(~/.claude/projects/c--PROJECTS-GUPPI/**)"
  change: this project's saved transcripts under ~/.claude/projects join the allow list for reading, so a search of case-guppi there does not ask (case 656)
- slug: estimate-permissions
  set:
    status: pending
    method: the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probes are the person's word on the client's prompt at a Write of work.md in Work Mode, and at a Read, Grep or Glob of case-guppi under ~/.claude/projects/c--PROJECTS-GUPPI/ in a session after the render, each recorded in the estimate line — never the agent's, which cannot see the prompt
  change: the Criterion replaced whole — the allow list holds a Read rule for this project's saved transcripts, and a search of case-guppi there runs with no prompt (case 656)
- slug: rule-settings
  replace:
  - old: what may be written without a question
    new: what may be written or read without a question
  change: the block of rule-permissions also carries what may be read without a question (case 656)
```

```tasks
- [x] update `rule-permissions`
- [x] update `estimate-permissions`
- [x] update `rule-settings`
- [x] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-permissions`
```

## Deferred

## Case 657 — the failed reading of the case-guppi check of the finished Case put off again

> **context:**
> `estimate-case-build-checks-the-finished-case` failed at the Work Mode of session 0109 (L22) and was put off by Case 647 of session 0311. Session 1343 took Cases 650–656 and closed Plan Mode at the person's word with this item still open.

> **problem:**
> No Case of session 1343 decides whether the frame of `case-guppi` or the Criterion of this Estimate changes.

```then
defer:
  - slug: estimate-case-build-checks-the-finished-case
    type: estimate
    purpose: "Whether case-guppi checks its finished Case before it answers, counted by what ask-guppi still finds at pre-spec; failed at L22 of session 0109, put off by sessions 0311 and 1343"
```

## Case 659 — the defer of the old path of guppi casecheck --subagent marks every sub-case of Case 653

> **context:**
> Case 658 put off Case 653 with one mark, `{supersedes:case 653}`. Case 653 has no decision line of its own; its lines are those of 653.1 and 653.2. `materialize` and the pre-spec check mark superseded only the entries that carry the named Case, so the three lines of 653.1 and 653.2 stand unsuperseded, and `uv run guppi prespec --check` prints three findings "no Case 653.x heading in the plan".

> **problem:**
> Case 658 does not supersede the decision lines of 653.1 and 653.2, so the librarian would apply the updates the person put off.

```then
defer:
  - slug: estimate-case-check-sends-back-a-faulty-case
    type: estimate
    purpose: "A Case of case-guppi that the checks refuse goes back to it before the main agent sees it; the removal of the old path of guppi casecheck --subagent, taken by Case 653 and put off by session 1343 until estimate-case-build-writes-the-case passes live"
```
