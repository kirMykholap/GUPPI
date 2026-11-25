<!-- approved 17:45:00 · session b6bc5f17 -->

# Session 0816 — Plan Mode of 2026-11-25

## Case 1053 — A new Case takes no number of the ledger, and a stop before a render is a finding

> **context:**
> Two faults of the build of a Case from session 0605, the Frontier items C4 and C5, which the person asked to be one Case. The first is about numbers. `case-guppi` gives a new Case beside a ratified one the number one above the highest number of the case files of the session and of the decision lines of its ledger, as `rule-case-build` sets it (case 725.1). A short-form Case that the main agent writes, such as the defer of Case 1050, has a decision line and no case file. The `case-guppi` of Case 1046 counted the files alone and wrote `vault/raw/2026-11-25/0605/cases/case-1050.md`, as `lesson-case-build-numbers-a-new-case-from-the-case-files-alone` records. No check stopped it. `held_number` of `.guppi/guppi/ratified.py` refuses a call only when `clashes` of `.guppi/guppi/casecheck.py` finds the number held in the store by another `agent_id`; `clashes` does not compare an entry with no `agent_id`, and `run` of `.guppi/guppi/caseid.py` holds the id it prints with no `agent_id`; with no entry at all the call passes and holds the number. So the guard lets such a write through either way. The check of the file does not see it either: `shape_findings`, `target_findings` and `lined_numbers` of `.guppi/guppi/casecheck.py` leave `defer` lines out. Case 1053.1 makes the guard refuse the first write of a case file whose number, or a sub-case of it, has a decision line of any kind in the session's ledger, and name a free id by `new_number`, the count that `next_id` of `.guppi/guppi/caseid.py` makes over the ledger, the store, the Decision pages and the case files. A file that holds text is not refused, so a Case built again under its own number, after a finding or a change, is written as before. I read whole `held_number`, `guard`, `builder_file` and the guard paragraph of the module docstring of `.guppi/guppi/ratified.py`; `clashes`, `new_number`, `lined_numbers`, `shape_findings`, `target_findings`, `case_number`, `is_case_file` and `ledger_of` of `.guppi/guppi/casecheck.py`; `next_id`, `known_ids`, `file_ids` and `run` of `.guppi/guppi/caseid.py`; and `in_family` of `.guppi/guppi/materialize.py`, the reading of a family that the guard can share. `lined_numbers` cannot serve, since it leaves `defer` lines out, and a short-form defer is the case of the lesson. A Grep of `def in_family` over `.guppi/guppi/` printed `.guppi/guppi/materialize.py` alone, so the task imports it and adds no second copy. The fixture `working` of `.guppi/tests/test_ratified.py` writes no `ledger.md`, so the tests `number_held` still pass.
>
> The second fault is about the moment of a reading. Case 1049.2 asked the person to install the clean copy at a stop of Work Mode. That install runs `plugin/skills/install/SKILL.md`, which the same Case changed by a render line, and a render line runs only at the librarian's run. So the install would have tested the old skill. Case 1052 moved the reading after the librarian's run, as `lesson-case-build-puts-a-reading-before-the-render-it-tests` records. `rule-case-build` already tells `case-guppi` to judge the moment of a reading by the state of the files when it runs (case 797.1). The last question that `/pre-spec` gives `ask-guppi` asks about a reading that the session cannot take, and `ask-guppi` found none, since the `method` named a stop of Work Mode. The person chose a coded finding. Case 1053.2 adds it as a new function of `.guppi/guppi/prespec.py` that `judge` calls beside `check_tasks`: a Case whose `tasks` block holds a line that opens with `stop:` and a render line of a file that its `when` or `then` names in a code span gives a finding. `vault/raw/2026-11-25/0605/cases/case-1049.md` holds all three in Case 1049.2: the render line of `plugin/skills/install/SKILL.md` at line 137, the `stop:` line at line 146, and the `when` that Case 1052 kept word for word names that file. `plan_findings`, `written_findings` and `check_answer` of `.guppi/guppi/casecheck.py` call `judge`, all read whole. So the finding reaches `--check`, the `ExitPlanMode` hook of `rule-prespec-hook`, the check after the Spec write and the check of the case file, which sends the file back before the person sees it. The render line is matched by `command_line` of `.guppi/guppi/render.py`, read whole, the one matcher of the tickers. A Grep of `stop:` over `.guppi/guppi/` printed no file, so no code judges a `stop:` line today and the new predicate is no second copy. The finding is narrow, as the round said. It does not catch a reading by hand at Retro of a rendered file, a reading of a page that the Case updates, or a render line and a `stop:` line under two headings. It does not tell apart a Case whose Work Mode renders the file by hand before the stop, which `rule-case-build` allows by a one-off task. Such a Case would get the finding and need its form changed. By the person's choice, Case 1053.2 also sets `insight-workflow-code-live-before-the-page-it-reads` `actioned`, as cases 473.2 and 868 did. Its one live child is the second lesson, which the cascade of `generate` archives. The first lesson joined no Insight. It is a `new` `error` lesson, so the close of the sprint archives it, as `rule-lessons-schema` sets it, and no page change is needed. By the person's choice, the empty file `vault/raw/2026-11-25/0605/cases/case-1050.md` stays as it stands.
>
> Choices of form: two sub-cases, since the guard and the finding can fail apart and need different fixes. Each one is checked on the page whose code it changes: `rule-spec-reconcile` lists `.guppi/guppi/ratified.py` in `implementation_ref`, and `rule-prespec-hook` lists `.guppi/guppi/prespec.py`. Case 1053.1 replaces whole the Criterion of `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`, the check of the guard of the number, and sets its `purpose` anew; its `method`, the tests `number_held`, stays, and the new tests take that name. Every line of the old Criterion stays word for word but two, both changed on purpose. Its `When` now also reads the decision lines of the session's `ledger.md`. Its exception for an entry with no `agent_id` now says that such an entry is not refused by the store, since the ledger may still refuse the call. A new Estimate would have made a line of `estimate-spec-reconcile-refuses-an-edit-of-the-plan` false, since that line says that the hook writes each call of `case-guppi` under `cases/` that the number Estimate does not refuse. With one Estimate for the number, that line stays true. Case 1053.2 creates a new Estimate on `rule-prespec-hook`. Both pages have `core: true` and stand `built`. An Estimate set `pending` or created sets each page `draft` until it passes, and each `method` is a pytest that Work Mode and Retro run. The finding of Case 1053.2 comes from a new function and not from `check_tasks`, so `estimate-prespec-requires-a-task-line`, whose Criterion lists the findings of `check_tasks`, stays true. The `purpose` lines of the seven Estimates of `rule-prespec-hook` speak of the gate, of methods, of a schema condition, of a required field and of pointers, not of a `stop:` line. `estimate-prespec-catches-a-command-line-off-form` judges the form of a render line, not its moment. The pair on `rule-spec-reconcile` changes the one sentence of its Purpose that names when a write of `case-guppi` under `cases/` passes. The pair takes that sentence to its end, the whole closing bracket with it, so the new pointer stands in a bracket of its own at the end of the sentence, as `rule-clean-branch` sets it. The finding of `/pre-spec` on the first form of the pair, whose `new` stopped inside the bracket, is closed this way. The Render of `rule-case-build` stays as it stands, since it already counts the ledger lines and names the free number of the guard. `rule-prespec` stays too, since its last question to `ask-guppi` stays true beside the coded finding.
>
> Searches. A Grep of `rule-spec-reconcile` over the repository root with the glob `{vault/wiki,.claude}/**`, in the mode that prints files, printed 10 files: `estimate-case-build-writes-the-case.md`, `estimate-clean-branch-ships-neutral-texts.md`, `estimate-permissions.md`, `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds.md`, `estimate-spec-reconcile-refuses-an-edit-of-the-plan.md`, `log.md`, `orchestration.md`, `rule-orchestration.md`, `rule-permissions.md` and `rule-plan-mode.md`. The hits, `log.md` aside, speak of the refused edit of the plan, of the write of the case file by the guard, of a quotation in a Result and of the child list. A refused call writes no file today too, so each one stays true. A Grep of `free number` over the root with the glob `{vault/wiki,.claude,.guppi/guppi}/**` printed 7 files: `.claude/agents/case-guppi.md`, `log.md`, `estimate-case-build-settles-form-by-itself.md`, `rule-case-build.md`, `.guppi/guppi/casecheck.py`, `.guppi/guppi/ratified.py` and `rule-spec-reconcile.md`. The free number that the guard names stays the same count, so each one stays true; the docstring of `held_number` changes in Work Mode. A Grep of `` `stop:` `` over the root with the glob `{vault/wiki/rules,.claude}/**` printed 6 files: `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/pr-review/SKILL.md`, `rule-where-to-stop.md`, `rule-skill-sprint-open.md`, `rule-case-protocol.md` and `rule-skill-pr-review.md`. `rule-where-to-stop` and `rule-case-protocol` set what a `stop:` task is, and the finding leaves that true. The `stop:` tasks of the two skills and their rules run `git push`, `gh pr create` or `gh pr merge`, with no render line beside them, so the finding leaves them alone. A Grep of ``tickers of `render` and `sprint` `` over the root with the glob `{vault/wiki,.claude,.guppi/guppi}/**` printed `.guppi/guppi/prespec.py` and `estimate-prespec-catches-a-command-line-off-form.md`: the list of findings in the docstring of `prespec.py` gets the new one in Work Mode, and the Estimate judges only the form of the line. A Grep of `case-example|project_root\(\)|REPO|Path\(__file__\)\.parents?` over `.guppi/tests/` printed 6 files: `test_ship.py`, `test_guppi_package.py`, `test_generate.py`, `test_schemas.py`, `test_libreport.py` and `test_case_schema.py`. Of these, `test_case_schema.py` runs `check_answer`, and so `judge`, over the live `vault/wiki/case-example.md`, which holds no `stop:` line and no render line, so it stays green. A Grep of `insight-workflow-code-live-before-the-page-it-reads` over the root with the glob `{vault/wiki,.claude,.guppi/guppi}/**` printed `brief.md`, `backlog.md`, `log.md` and the second lesson. `backlog.md` is written by `guppi backlog`, and the lesson leaves by the cascade. The session's ledger holds no `lesson[error]` line and no `{addresses:` mark, by a Grep of each, so no mark is added. The two lessons belong to session 0605, so neither takes a mark.
>
> The note of the check listed the files that name what the Case changes. I read the Criterion of each one whose purpose speaks of the guard of a number, of a stop or of the moment of a reading. `estimate-spec-reconcile-refuses-an-edit-of-the-plan` stays true, as said above. `estimate-case-check-sends-back-a-case-number-held-by-another-agent` stays true, since its exception for an entry with no `agent_id` is bound to its own check of the store. `estimate-case-check-sends-back-a-ratified-case-in-another-shape` stays true, since its exception for a family with only `defer` lines is bound to the check of the file, and the new refusal stands in the guard. `estimate-lint-reports-a-method-tied-to-a-one-off-moment` judges the words of a `method`, not a `stop:` line, and stays true. `estimate-where-to-stop-stops-only-on-its-conditions` sets that Work Mode stops before a `stop:` task, and the new finding leaves that true. `lesson-hooks-guard-broken-mid-edit-of-its-own-contract` records that Work Mode broke the live guard by changing what `held_number` gives `guard` in two steps; the task of `.guppi/guppi/ratified.py` keeps that pair as it stands. `backlog.md` is named above. Every other file of the note speaks, by its purpose line or its path, of the Spec hook, the ledger hook, the store of other checks, `settings.json` or other findings of `guppi prespec --check`, and the Case leaves each one true. The note also listed the case files of Cases 1054, 1055 and 1057 of this session, which name `.guppi/guppi/casecheck.py`, `.claude/settings.json` and `.guppi/guppi/ledger.py`. Those Cases are being built at the same time as this one, after the findings of `/pre-spec`, so their files were not read in this build. No claim of this Case rests on them.

> **problem:**
> A new Case beside a ratified one can take the number of a short-form Case, since nothing stops a case file under a number that only the ledger holds. A Case can also put a reading at a stop of Work Mode before the render of the file it tests, and `/pre-spec` let one through.

> **recommend:**
> - **How does a new Case stop taking the number of a Case with no file?**
>   - Recommended: (a) the guard refuses the first write under a number the ledger already holds, a `defer` included, and names a free number.
>   - Answer: (a), as recommended.
> - **Where is a reading placed before the render it tests caught?**
>   - Recommended: (b) a coded finding in `guppi prespec --check` for a Case with a render line of a file, a `stop:` task, and a `when` or `then` that names that file.
>   - Answer: (b), as recommended.
> - **Does this Case close the Insight?**
>   - Recommended: (a) set `insight-workflow-code-live-before-the-page-it-reads` `actioned` by the sub-case that fixes the second fault.
>   - Answer: (a), as recommended.
> - **What happens to the empty file of the wrong number?**
>   - Recommended: (a) leave it.
>   - Answer: (a), as recommended.

### Case 1053.1 — The guard refuses a new case file under a number the ledger holds

> **given:**
> `rule-spec-reconcile`: the rule of the guard of a case file; its Purpose names when a write of `case-guppi` passes.
> **＋** `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`: the check of the guard of the number; its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that `case-guppi` writes.
> **＋** `.guppi/guppi/ratified.py`: `held_number`, the guard of the number, and its docstrings.
> **＋** `.guppi/guppi/casecheck.py`: `case_number`, `clashes` and `new_number`, the judgments the guard runs.
> **＋** `rule-case-check`: the check of the file of a Case, which runs the same judgments.
> **＋** `estimate-spec-write-exits-2-on-an-error`: the behaviour of the guard on an error.
> **＋** `.guppi/tests/test_ratified.py`: the tests of the guard.

> **when:**
> `case-guppi` calls `Edit`, `Write` or `MultiEdit` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run --project .guppi guppi ratified --guard` on `PreToolUse` reads the path, the agent type and the `agent_id` of the call from the hook input, `<plan>.checked.json` beside the plan file of the session, and the decision lines of the session's `ledger.md`.

> **then:**
> The guard reads the id N from the file name by `case_number` of `.guppi/guppi/casecheck.py`, a plain id such as `785` or an id of a sprint such as `kir-plugin-12` alike.
> **＋** The call is refused when `<plan>.checked.json` holds Case N, or a sub-case of it, under its id alone with an `agent_id` other than the one of the call: exit 2 with the reason on stderr, and the call does not run.
> **＋** The call is refused the same way when the file does not stand or holds no text and a decision line of the session's `ledger.md` of any kind, a `defer` included, names Case N or a sub-case of it.
> **＋** The reason names the file and a free id, and tells `case-guppi` to build its Case under that id.
> **＋** The holder is judged by `clashes` and the free id is counted by `new_number` of `.guppi/guppi/casecheck.py`, the judgments that the check of `rule-case-check` runs.
> **＋** A call that passes while `<plan>.checked.json` holds no entry under N alone writes there, under N, an entry with the `agent_id` of the call and the time, and no text, so the id is held before the agent stops.
> **＋** A refusal writes one line of the refusal to the day's event log.
> **－** A call whose `agent_id` is the one of the entry under N, and an entry with no `agent_id`, are not refused by the store.
> **－** A call on a file that holds text is not refused by the ledger, so a Case built again under its own number is written.
> **－** A call with no `agent_id`, a file whose name gives no id, and a session with no plan file are not judged by this check, and nothing is written into `<plan>.checked.json`.
> **－** An error of the guard while it finds the plan file or reads or writes `<plan>.checked.json` lets the call run: exit 0 with one line on stderr, as `estimate-spec-write-exits-2-on-an-error` sets it for the guard.

```then
update:
- slug: rule-spec-reconcile
  replace:
  - old: unless `case-guppi` makes it and no other agent holds the number of that Case (cases 453, 645.3, 650.1; a comparison with a ratified copy stood here from case 387.3 to case 445.1).
    new: unless `case-guppi` makes it, no other agent holds the number of that Case and, while its file holds no text, no decision line of the session's ledger names that Case or a sub-case of it (cases 453, 645.3, 650.1, 1053.1; a comparison with a ratified copy stood here from case 387.3 to case 445.1).
  change: the guard refuses the first write of case-guppi on the file of a Case whose number has a decision line in the session's ledger, a defer included, with a free number (case 1053.1)
- slug: estimate-spec-reconcile-refuses-a-case-file-another-agent-holds
  set:
    status: pending
    purpose: Whether the first call of case-guppi on the file of a Case, its name in either form of the id, holds its id in the store, and a call on that file is refused with a free id when another case-guppi holds the id or, while the file holds no text, a decision line of the session's ledger names that Case or a sub-case of it
  change: the Criterion replaced whole — the guard also refuses the first write of case-guppi on the file of a Case whose number has a decision line in the session's ledger, a defer included, with a free id
```

```tasks
- [ ] update `rule-spec-reconcile`
- [ ] update `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`
- [x] `.guppi/guppi/ratified.py`: `held_number` refuses a call of `case-guppi` on `case-<N>.md` whose file does not stand or holds no text while a decision line of the session's ledger names Case N or a sub-case of it, by `in_family` of `.guppi/guppi/materialize.py`, imported, the reason naming a free id by `casecheck.new_number`; it holds no number for a refused call and keeps the pair it gives `guard`, so the live guard is not broken between two edits; the docstring of `held_number`, of `guard` and the guard paragraph of the module docstring name it.
- [x] `.guppi/tests/test_ratified.py`: tests `number_held` on the ledger: a `Write` of a missing `case-7.md` with a ledger line `decision[case 7][defer][…]` is refused, names case 8 and `case-8.md`, and writes nothing into the store; a line of `7.1` refuses it too; an `Edit` of a `case-7.md` that holds text passes; a line of another number passes.
- [ ] read `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`
```

### Case 1053.2 — A stop before the render of a file the Criterion names is a finding

> **given:**
> `rule-prespec-hook`: the rule of `guppi prespec --check`, whose findings the new one joins.
> **＋** `estimate-prespec-hook-reports-a-stop-before-the-render-it-tests`: the new check of the finding.
> **＋** `insight-workflow-code-live-before-the-page-it-reads`: the Insight this sub-case sets `actioned`.
> **＋** `.guppi/guppi/prespec.py`: `judge`, which calls the new function, and the list of findings in its module docstring.
> **＋** `.guppi/guppi/casecheck.py`: the check of the file of `case-guppi`, which runs `judge`.
> **＋** `.guppi/guppi/render.py`: `command_line`, the one matcher of a render line.
> **＋** `.guppi/tests/test_prespec.py`: the tests of the check.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan> --session <id>` of `.guppi/guppi/prespec.py`, or the check of the file of `case-guppi` in `.guppi/guppi/casecheck.py`, reads a Case whose `tasks` block holds a line that opens with `stop:` after its box and a render line that `command_line` of `.guppi/guppi/render.py` matches.

> **then:**
> For each file of its render lines that the `when` or `then` of that Case names in a code span, the check gives one finding `case N: stop before the render of <file> — the file changes only at the librarian's run, so a reading at a stop of Work Mode tests its old text`.
> **＋** The judgment is one function of `.guppi/guppi/prespec.py` that `judge` calls, so `--check`, the `ExitPlanMode` hook of `rule-prespec-hook` and the check of the file of `case-guppi` give the same finding.
> **＋** The file of a render line is a code span after the command that `command_line` matches.
> **－** A Case with a `stop:` line and no render line, or whose `when` and `then` name no file of its render lines, gives no such finding.
> **－** A render line and a `stop:` line under two different Case headings give no such finding.

```then
create:
- slug: estimate-prespec-hook-reports-a-stop-before-the-render-it-tests
  ref: rule-prespec-hook
  kind: QA
  purpose: Whether pre-spec reports a Case whose tasks hold a stop line and a render line of a file that its when or then names, by one function of .guppi/guppi/prespec.py, and leaves alone a Case without one of them or whose when and then name no file of its render lines
  method: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k stop_before_render
  tags:
  - harness
  - workflow
update:
- slug: insight-workflow-code-live-before-the-page-it-reads
  set:
    status: actioned
    addressed_by: decision-case-1053.2
  change: 'actioned: a stop task before the render of a file that the Criterion of its Case names is a finding of guppi prespec --check (case 1053.2)'
```

```tasks
- [ ] create `estimate-prespec-hook-reports-a-stop-before-the-render-it-tests`
- [ ] update `insight-workflow-code-live-before-the-page-it-reads`
- [x] `.guppi/guppi/prespec.py`: a new function, called by `judge` after `check_tasks`, gives the finding for a Case whose `tasks` block holds a `stop:` line and a render line, matched by `render.command_line`, imported, of a file that its `when` or `then` names in a code span; `check_tasks` stays as it stands; the list of findings in the module docstring names it.
- [x] `.guppi/tests/test_prespec.py`: tests `stop_before_render`: a Case with a render line of `plugin/skills/install/SKILL.md`, a `stop:` line and a `when` that names that file gives the finding; the same Case with no `stop:` line, or with a `when` and `then` that name no rendered file, gives none; a render line and a `stop:` line under two sub-cases give none.
- [ ] read `estimate-prespec-hook-reports-a-stop-before-the-render-it-tests`
```

## Case 1054 — The level of a dispatch is judged from its item, and a round asks no choice of form

> **context:**
> Two readings of the `/hi` of session 0605 failed, the Frontier items C2 and C3, which the person asked to be one Case. The first is about the level of effort. The main agent passes the parameter `effort` when it dispatches `case-guppi`, and it judges the level from the Frontier item and the person's words, before the Case exists. The Render of `rule-orchestration` says so, but its three levels, and the three lines of the Criterion of `estimate-orchestration-dispatches-case-guppi-at-a-level`, speak of what the Case changes. The reading compared the level with the built Case: Case 1039, dispatched `medium` on the item C6 of session 1353, which asked whether a step should search the ratified Cases and named no code, changed `.guppi/guppi/casecheck.py`, and the Criterion sets `high` for a Case that changes a hook. The person chose that the level is judged once, at the dispatch, from the item and the person's words, and that it stands where the built Case changes more. Case 1054.1 rewords the effort sentence and the hold sentence of the Render, and replaces the Criterion whole, its three level lines now speaking of what the item asks; a Case like 1039 still runs at `medium`, which the person accepted.
>
> The second is about questions. The Render of `rule-case-build` makes the choice between a new Estimate, a replaced Criterion and an Estimate that already checks the change a choice of form, which `case-guppi` settles itself (case 1031.1). The reading of `estimate-case-build-settles-form-by-itself` found two questions of session 1353 that asked it, Case 1042 Q3 and Case 1043 Q5, each recommended on atomicity alone; the case files under `vault/archive/plugin/2026-11-20/1353/raw/cases/` hold them as the items "How the change is checked" and "How the README and the license are checked". The same Render still has a sentence of case 800.1 that describes a question of a round on how a Case is checked as an ordinary question. The person chose to narrow it: Case 1054.2 adds before it a sentence that asks how a Case is checked only where the Case can give no Estimate, or where the options of that question differ in behaviour, in cost or in what they block. The Criterion is replaced whole: each old line stays word for word, and one line is added for the new sentence.
>
> Choices of form. Two sub-cases, since the level of a dispatch and the questions of a round can fail apart and need different fixes. Each one replaces the Criterion of the failed Estimate that checks its behaviour and sets it `pending`, so that it is read again; no new Estimate is created. Both `method` lines are set anew, since their first part names the session that creates the Estimate. The second part of each still waits for a session after the render, in the form `by hand, after …:` that `waits_for_an_event` of `.guppi/guppi/lint.py` accepts. I read `waits_for_an_event`, `waits_for_another_session`, `tied_to_a_one_off_moment`, `waits_for_a_later_moment` and `check_unread` there. The new `method` lines hold neither `first … after the render` nor a later session outside the part that waits for its event. A `pending` Estimate whose `method` waits for a later moment gives no `unread` finding, so the two `unread: failed` findings of these Estimates leave `guppi check`. Both rule pages have `core: true` and stand `draft`, so setting their Estimates `pending` blocks nothing new. Each new pointer stands in a bracket at the end of its sentence.
>
> Frame. Of the `estimates` of `rule-orchestration`, only the level Estimate has a `purpose` that speaks of the level of a dispatch. Its `purpose`, which names the effort of the kind of its Case, is set anew. Of the `estimates` of `rule-case-build`, `estimate-case-build-answers-what-done-means` has a `purpose` that speaks of a round on the promise. I read its Criterion. Its line says that such a question, where one comes, offers the existing Estimate by slug, so it stays true when fewer such questions come. `estimate-case-build-offers-a-page-for-code-no-page-covers` already asks in a round only where the options differ, and it stays true. `.guppi/tests/test_orchestration.py` reads `vault/wiki/orchestration.md` live, but only its blocks tagged `showing` and `defer`, which neither pair touches. A Grep of `case-guppi\.md|orchestration\.md` over `.guppi/tests/` printed `test_casecheck.py`, `test_onward.py` and `test_orchestration.py`. The first two hold the names as strings and read no live text of the files. The check of this file noted five lines of the old Criterion of the level Estimate that the new one does not carry word for word: the effort line, the three level lines and the hold line. Each is changed on purpose, by the person's answer, to judge the level at the dispatch from what the item asks, and to hold it where the built Case changes more. The note of names listed the files that name `rule-orchestration`, `orchestration.md`, `rule-case-build`, `case-guppi.md` and `case-guppi`. I read `estimate-sprint-plugin-case-guppi-level-trial-decided`, which asks at the close of the sprint what the levels saved and whether the person keeps them. It stands, since it measures the levels whatever they are judged from, and the judgment at the dispatch is the one it measures. I read `lesson-case-build-gave-a-sub-case-no-estimate` too. It stands, since a Case still names the Estimate that checks it when no question is asked. By purpose line or path, every other listed file speaks of another step: the showing, the Frontier, the ledger, the batches, the checks of the file, the skills of a sprint, or the past faults of other steps. The Case leaves each of them true.
>
> Searches. A Grep of `effort` over the repository root with the glob `{vault/wiki,.claude}/**` printed 11 files: `brief.md`, `orchestration.md`, `.claude/agents/case-guppi.md`, `log.md`, `estimate-case-build-writes-the-case.md`, `estimate-orchestration-dispatches-case-guppi-at-a-level.md`, `rule-case-build.md`, `rule-orchestration.md`, `lesson-harness-empty-grep-taken-as-absence.md`, `estimate-context-size-agents-counts-each-agent.md` and `rule-permissions.md`. The Render of `rule-orchestration` and its Estimate enter the Case, and `orchestration.md` changes by the render. `case-guppi.md` and `rule-case-build` set the default `effort: medium` of the agent, which stays. `estimate-case-build-writes-the-case` says the agent runs at the level its call passes, which stays true. `estimate-context-size-agents-counts-each-agent` prints the level, and the lesson tells of a past search; both stand. `rule-permissions` stands too, since its one hit is the word best-effort, about how Claude Code applies a `Read` rule to searches. `brief.md` and `log.md` are not read. A Grep of `choice of form|how it is checked|how a Case is checked` over the same root and glob printed 13 files: `brief.md`, `.claude/skills/setup/SKILL.md`, `orchestration.md`, `.claude/agents/case-guppi.md`, `log.md`, `estimate-case-build-settles-form-by-itself.md`, `estimate-case-build-writes-the-case.md`, `rule-case-build.md`, `rule-orchestration.md`, `estimate-morph-sets-up-the-project-at-the-first-hi.md`, `rule-skill-setup.md`, `estimate-orchestration-shows-the-built-case.md` and `estimate-case-build-answers-what-done-means.md`. `/setup` asks no question on how its Case is checked, and the new sentence leaves that true. `orchestration.md`, its rule and `estimate-orchestration-shows-the-built-case` speak of the short text on how a Case is checked in the showing, which stays. `estimate-case-build-writes-the-case` points to the Estimate for a choice of form and stays true. A Grep of both Estimate slugs over the root with the glob `{vault/wiki,.claude,.guppi/guppi}/**` printed `brief.md`, `log.md`, `estimate-case-build-writes-the-case.md`, `rule-case-build.md` and `rule-orchestration.md`. The lines of `estimate-case-build-writes-the-case` point to the two Estimates for what they check, and those lines stay true. Case 1053 of this session leaves the Render of `rule-case-build` as it stands, and its pages are not these, so no line of it rests on this change. The session's ledger holds no `lesson[error]` line and no `{addresses:` mark, by a Grep of each, so no mark is added. The two Estimates belong to session 0605 and carry no lesson. The note of the check also listed `vault/raw/2026-11-25/0816/cases/case-1055.md`, which names `rule-orchestration` and `rule-case-build`, and `vault/raw/2026-11-25/0816/cases/case-1057.md`, which names `rule-case-build`. The main agent named Cases 1055 and 1057 as built at the same time as this one, so I read neither file in this build. This Case rests on no line of them, and a clash between them is left to the check of the file and to `/pre-spec`.

> **problem:**
> The level of a dispatch is judged from the item, but its check judges it against the built Case, so a Case that grows past its item fails the check. A sentence of the agent's text also still invites a question on how a Case is checked, so `case-guppi` asked the person choices of form that it should settle itself.

> **recommend:**
> - **How is the level of a dispatch judged when the built Case changes more than the item asked?**
>   - Recommended: (a) the rule and the check judge the level once, at the dispatch, from the item and the person's words, and the level stands where the built Case changes more.
>   - Answer: (a), as recommended.
> - **What changes so that `case-guppi` stops asking a choice of form?**
>   - Recommended: (a) narrow the sentence of the agent's text: a question on how a Case is checked comes only where the Case can give no check, or where the options differ in behaviour, in cost or in what they block; the check gains that line and is read again.
>   - Answer: (a), as recommended.

### Case 1054.1 — The level of a dispatch is judged once, from its item

> **given:**
> `rule-orchestration`: the rule of the dispatch of `case-guppi`; its Render sets the level of `effort`.
> **＋** `estimate-orchestration-dispatches-case-guppi-at-a-level`: the check of the level; its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`, which `/hi` loads.
> **＋** `.claude/agents/ask-guppi.md`: the agent of the vault query, whose dispatch does not change.

> **when:**
> The main agent, with `vault/wiki/orchestration.md` loaded, dispatches `case-guppi` by the Agent tool for a Case of Plan Mode or Work Mode.

> **then:**
> The call passes the parameter `effort`, judged once at the dispatch by what the Frontier item and the person's words ask the Case to change.
> **＋** The level is `low` for an item that asks to change only the text of pages and no code, and for the setup Case and the opening Case of a sprint.
> **＋** The level is `high` for an item that asks to change a hook, a check or other code that judges a text.
> **＋** The level is `medium` for every other item.
> **＋** The person's word on a Case sets another level up to `high`, and the call passes that level.
> **＋** The level holds to the end of the Case, through each `SendMessage`, also where the built Case changes more than its item asked.
> **－** No new dispatch raises the level of a Case.
> **－** No call passes `xhigh` or `max`.
> **－** No call passes the parameter `model`.
> **－** The dispatch of `.claude/agents/ask-guppi.md` does not change.

```then
update:
- slug: rule-orchestration
  replace:
  - old: 'by what the Frontier item and the person''s words ask the Case to change: `low` for a Case that changes only the text of pages and no code, and for the setup Case and the opening Case of a sprint; `high` for a Case that changes a hook, a check or other code that judges a text; `medium` for every other Case (as set in case 1029.1).'
    new: 'judged once at the dispatch by what the Frontier item and the person''s words ask the Case to change: `low` for an item that asks to change only the text of pages and no code, and for the setup Case and the opening Case of a sprint; `high` for an item that asks to change a hook, a check or other code that judges a text; `medium` for every other item (as set in cases 1029.1 and 1054.1).'
  - old: The level holds to the end of the Case, through each `SendMessage`; no new dispatch raises it, no call passes `xhigh` or `max`, and no call passes the parameter `model` (as set in case 1029.1).
    new: The level holds to the end of the Case, through each `SendMessage`, also where the built Case changes more than its item asked; no new dispatch raises it, no call passes `xhigh` or `max`, and no call passes the parameter `model` (as set in cases 1029.1 and 1054.1).
  change: the level of a dispatch of case-guppi is judged once at the dispatch from the item and the person's words, and stands where the built Case changes more (case 1054.1)
- slug: estimate-orchestration-dispatches-case-guppi-at-a-level
  set:
    status: pending
    purpose: Whether each call that dispatches case-guppi passes the effort that its Frontier item and the person's words ask for, judged once at the dispatch, or the person's word up to high, holds it to the end of the Case, and passes no model
    method: 'by hand, at the Retro of the session that sets this Criterion, the new Render of rule-orchestration in the Spec read against the Criterion; by hand, after a session whose orchestration.md holds that Render: each Agent call of case-guppi in the transcript of that session under ~/.claude/projects/ read against the Criterion, with the Frontier item and the person''s words its prompt holds, the transcript in the estimate line'
  change: the Criterion replaced whole — the level is judged once at the dispatch from the item and the person's words, and stands where the built Case changes more
```

```tasks
- [ ] update `rule-orchestration`
- [ ] update `estimate-orchestration-dispatches-case-guppi-at-a-level`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-dispatches-case-guppi-at-a-level`
```

### Case 1054.2 — A round asks how a Case is checked only where the options differ in what they do

> **given:**
> `rule-case-build`: the rule of `case-guppi`; its Render sets which choices are forks.
> **＋** `estimate-case-build-settles-form-by-itself`: the check of the choices of form; its Criterion is replaced whole.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `/pre-spec`: the check whose finding may ask `case-guppi` to change a Case.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`, meets on an item a choice that the person's words do not give.

> **then:**
> A choice of form is how the work splits into Cases and sub-cases, whether a promise takes a new Estimate, a replaced Criterion or an Estimate that already checks the change, which page holds a thing, and where a fix goes that adds a second behaviour to a ratified Case.
> **＋** It settles a choice of form itself, with no question in a round.
> **＋** The `context` of the Case names the choice, and the person sees it at the showing of the Case.
> **＋** A choice of form whose options differ in behaviour, in cost or in what they block is a fork, and it asks that choice in a round.
> **＋** It asks in a round how a Case is checked only where the Case can give no Estimate, or where the options of that question differ in behaviour, in cost or in what they block.
> **＋** Asked by a message or by a finding of `/pre-spec` to change a Case, it builds the change under the number of that Case.
> **＋** A new Case it builds beside a ratified Case takes the number one above the highest number of the case files and of the decision lines of the session's ledger, or the free number that the guard of its case file names, and carries no `{supersedes:case N}` mark.
> **＋** The file of that ratified Case stays as it is, and a pair of the new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
> **－** A choice of the bound, of a second reasonable `recommend`, of the exceptions or of what is left not done stays a fork.
> **－** A Case that can give no Estimate still asks in a round what its Estimate will check.

```then
update:
- slug: rule-case-build
  replace:
  - old: A question of a round on how a Case is checked gives, beside
    new: You ask in a round how a Case is checked only where the Case can give no Estimate, or where the options of that question differ in behaviour, in cost or in what they block, and never where they differ only in how the work splits or is written down (as set in case 1054.2). A question of a round on how a Case is checked gives, beside
  change: case-guppi asks how a Case is checked only where the Case can give no Estimate or the options differ in behaviour, in cost or in what they block (case 1054.2)
- slug: estimate-case-build-settles-form-by-itself
  set:
    status: pending
    method: 'by hand, at the Retro of the session that sets this Criterion, the new Render of rule-case-build in the Spec read against the Criterion; by hand, after a session whose case-guppi.md holds that Render: each round of case-guppi in the transcript of that session under ~/.claude/projects/ read against the Criterion, the transcript in the estimate line'
  change: the Criterion replaced whole — a round asks how a Case is checked only where the Case can give no Estimate or the options differ in behaviour, in cost or in what they block
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-settles-form-by-itself`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-settles-form-by-itself`
```

## Case 1055 — The install readings are taken at one stop of this Work Mode

> **context:**
> Five readings wait for an install of GUPPI that only the person can make, in a new Claude Code window that the agent cannot open: `estimate-plugin-install-asks-one-approval-in-plan-mode`, `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-git-context-offers-git-init`, `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-plugin-install-sets-aside-the-files-of-the-project`. The brief proposed to put off the first three, since their sessions took no reading. The person chose to take all of them in this session, at one `stop:` task of Work Mode, as Case 1026 of session 0358 did. Before the stop the agent writes the clean copy and the test folders. At the stop the person installs and works in each folder, and then the agent reads the transcripts and the files. Each reading can fail alone and needs its own fix, so the Case has one sub-case per Estimate, as `rule-atomicity` sets it.
>
> The person asked why parts that passed before are read again. A Criterion replaced whole is read whole, against its new text. `estimate-plugin-install-asks-one-approval-in-plan-mode` was created by case 1040 and never read. `estimate-plugin-install-sets-aside-the-files-of-the-project` was created by case 932.1, put off by case 949 the next day, and never read. `estimate-morph-sets-up-the-project-at-the-first-hi` failed on 2026-11-04 on its questions, and case 1031.3 replaced its Criterion. `estimate-git-context-offers-git-init` failed on 2026-11-04, and case 1036 replaced its Criterion. `estimate-plugin-install-writes-guppi-into-an-empty-project` passed on 2026-10-30, and case 1052 replaced its Criterion for the `LICENSE`. The person chose the fewest projects that keep each Criterion as it stands: the `When` lines of three Estimates exclude each other. One wants a `CLAUDE.md` and no other file of the install, one wants no file of the install, and one wants a `CLAUDE.md`, a `.claude/settings.json` and a `.gitattributes`. So there are five projects, three of them install-only for the set-aside Estimate. Each sub-case sets the `method` of its Estimate anew to describe its folder, and changes no Criterion and no status, so each Estimate stays `pending` until its reading, as `case-schema.md` sets it for an `update` that names a part alone. Each new `method` is one part that opens with `by hand, after` and names its event before a colon, so `waits_for_an_event` of `.guppi/guppi/lint.py` accepts it and `check_unread` gives no `unread` line. I read `tied_to_a_one_off_moment`, `waits_for_an_event`, `waits_for_another_session`, `waits_for_a_later_moment` and `check_unread` there. No new `method` holds `first` with `after the render` or `after the change`. No new `method` names a case, since the clean copy ships the Estimates.
>
> By the person's choice, the set-aside reading joins the stop, so Case 1055.5 carries `{supersedes:case 949}` and retires its put-off. By the person's choice, no push to `prod` and no change to `main` happen here. The Frontier item C1 is left out of this Case. `guppi ship` writes nothing without `--allow-draft` while `is_draft_core` of `.guppi/guppi/pages.py` accepts a page. I read it whole with `drafts` and `run` of `.guppi/guppi/ship.py`. `rule-morph` was never set `built`, and `rule-case-build` and `rule-orchestration` each have a `failed` Estimate. So a run of `prod.yml` here would write nothing, as `guppi check` in `## Flags` of `vault/wiki/brief.md` reports: `rules/rule-case-build`, `rules/rule-morph`, `rules/rule-orchestration`: `status: a page with core: true that is draft`. `main` gets the sprint by the pull request after `/sprint-close`, as `rule-skill-merge-main` sets it. By the person's choice, the branch `plugin` is pushed at a second stop at the end of Work Mode, since a push is a stop by `rule-where-to-stop`. That task stands in Case 1055.5, the last sub-case. No Estimate checks a push, and `git status` after it shows the branch up to date with `origin/plugin`.
>
> The copy comes from `run` of `.guppi/guppi/ship.py`. It refuses a folder that is not empty, prints the line of each draft core page and goes on with `--allow-draft`, and stops when `version` finds no tag `prod-x.y.z` in the history of HEAD. The copy task shows whether one stands. No `render` line stands in this Case, so the finding of Case 1053.2 on a stop before a render does not apply. Case 1054 of this session sets Estimates of `rule-orchestration` and `rule-case-build` `pending`, and this Case touches neither page. A Grep of `plugin-install-asks-one-approval|morph-sets-up-the-project|git-context-offers-git-init|plugin-install-writes-guppi-into|plugin-install-sets-aside-the-files` over `.guppi/tests/` printed no file, so no test reads these pages by slug. A Grep of the session's ledger for `lesson\[error\]|\{addresses:` printed nothing, so no lesson is marked.
>
> The check of this file listed the files that name the changed Estimates. `rule-plugin-install` and `rule-git-context` list them in `estimates` and in History, and this Case changes only a `method` and adds a History line to each, so they stand. The `method` of `estimate-clean-branch-writes-the-session-files` lets its reading share the copy and the folder of the reading of `estimate-git-context-offers-git-init`. This Case does not take that reading, and that line stands. `backlog.md` is written by `guppi backlog` from the pages, so it follows the retired put-off at the librarian's run. Some `then` lines of the sub-cases share words, since each sub-case copies the Criterion of its own Estimate word for word, and they stand.

> **problem:**
> The readings of the install, the setup and the git offer wait for installs by hand that no session has made. The person chose to take them in this session at one stop, on the fewest projects that keep each Criterion as it stands.

> **recommend:**
> - **Does the push to `prod` stay in this Case?**
>   - Recommended: (a) leave the push out, since the build writes nothing while core pages block it.
>   - Answer: (a); a push to `prod` may not be needed.
> - **How does the stop run?**
>   - Recommended: (a) one stop; the agent writes the copy and makes the folders before it.
>   - Answer: (a), as recommended.
> - **How does `plugin` reach `main` in this session?**
>   - Recommended: (a) not in this session; the pull request after `/sprint-close` does it.
>   - Answer: (a); the person meant a push of the branch `plugin`, which this Case adds.
> - **Does the put-off reading of the set-aside files join the stop?**
>   - Recommended: (b) leave it put off.
>   - Answer: take it anyway.
> - **How many test projects does the stop use?**
>   - Recommended: (b) three projects, the methods set anew.
>   - Answer: the person asked why parts that passed before are read again, and why not one project; replaced by the next question.
> - **How many projects does the stop use, now that the set-aside reading joins it?**
>   - Recommended: (a) one main project and two small ones.
>   - Answer: (a); replaced by the last question, since that main project breaks three Criteria.
> - **When is `plugin` pushed to GitHub?**
>   - Recommended: (a) a stop at the end of this Work Mode.
>   - Answer: (a), as recommended.
> - **The shared project does not fit three of the checks: how many projects then?**
>   - Recommended: (a) five projects, three of them install-only, no check changed.
>   - Answer: (a), as recommended.

### Case 1055.1 — The install in Plan Mode is read at the install stop

> **given:**
> `estimate-plugin-install-asks-one-approval-in-plan-mode`: its `method` is set anew and its reading is taken.
> **＋** `rule-plugin-install`: the skill `/guppi:install`.
> **＋** `plugin/skills/install/SKILL.md`: the skill the person types.
> **＋** `.guppi/guppi/ship.py`: the command that writes the clean copy.
> **＋** `rule-where-to-stop`: the stop before a task that opens with `stop:`.
> **＋** `guppi-set-aside/`: the folder of the files set aside.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in a project open in Claude Code whose session stands in Plan Mode, and the project holds a `CLAUDE.md` of its own and no other file of the install.

> **then:**
> Before it writes or moves anything, the agent checks the paths of the install and shows a plan that lists each file it will copy and each file of the project it will set aside under `guppi-set-aside/`, `CLAUDE.md` among them.
> **＋** The agent asks the person to approve that plan once, by the plan approval of Claude Code, and names none of its options.
> **＋** Once the person approves it, the agent runs the install as `rule-plugin-install` sets it, with no second plan.
> **＋** Where `uv --version` fails and the person says yes to installing `uv`, the installer of `uv` is the first item of that plan, and the agent runs it only after the approval.
> **－** When the person does not approve the plan, the agent writes and moves nothing in the project and stops.

```then
update:
- slug: estimate-plugin-install-asks-one-approval-in-plan-mode
  set:
    method: 'by hand, after the install stop of the Work Mode that sets this method: the clean version written into C:/tmp/guppi-1055/copy by uv run --project .guppi guppi ship --allow-draft, added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in a folder with no git that holds a CLAUDE.md and a code file of its own, Claude Code started by claude --permission-mode plan from a terminal whose PATH holds no folder of uv, /guppi:install typed, the offer of uv answered yes and the plan not approved, then /guppi:install typed again and the plan approved; the transcript of that session under ~/.claude/projects/ and the files of the folder before, between and after read against the Criterion, recorded in the estimate line'
  change: the method set anew — one project with no uv on its PATH takes the refused plan and then the approved one, at the install stop of Work Mode
```

```tasks
- [ ] update `estimate-plugin-install-asks-one-approval-in-plan-mode`
- [x] by hand: `uv run --project .guppi guppi ship --allow-draft C:/tmp/guppi-1055/copy` into an empty folder outside the repository, the catalogue of the installs; its output shows whether a tag `prod-x.y.z` stands in the history of HEAD.
- [x] by hand: five new folders under `C:/tmp/guppi-1055/`: `p1-code`, no git, with a `CLAUDE.md` and a code file of its own; `p2-license`, `git init -b main` run in it, with only a `LICENSE` of its own; `p3-set-aside`, with a `CLAUDE.md`, a `.claude/settings.json` with a hook and a `.gitattributes` of its own; `p4-offline`, the same files as `p3-set-aside`; `p5-clash`, with a `vault/wiki/glossary.md` of its own, a path the install writes; and an empty folder `C:/tmp/guppi-1055/empty-cache`.
- [x] stop: the person adds the catalogue by `/plugin marketplace add C:/tmp/guppi-1055/copy` and installs the plugin by `/plugin install guppi@guppi-marketplace`, then works through each folder with the commands written out whole in the reply: in `p1-code`, Claude Code started by `claude --permission-mode plan` from a terminal whose PATH holds no folder of uv, `/guppi:install`, yes to uv, the plan not approved, `/guppi:install` again and the plan approved, Claude Code reopened, `/hi`, `! git init -b main`, `/hi` again, and that session taken through the setup Case, its first sprint, Work Mode and its librarian's run; in `p2-license`, `/guppi:install`, Claude Code reopened, `/hi`, and that session taken through the setup Case to its librarian's run; in `p3-set-aside` and `p5-clash`, `/guppi:install`; in `p4-offline`, Claude Code started from a terminal with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to `C:/tmp/guppi-1055/empty-cache`, and `/guppi:install`; the person reports, and the agent reads the transcripts under `~/.claude/projects/`, the ledgers and the files of each folder for the readings of Case 1055.
- [ ] read `estimate-plugin-install-asks-one-approval-in-plan-mode`
```

### Case 1055.2 — The setup at the first /hi is read at the install stop

> **given:**
> `estimate-morph-sets-up-the-project-at-the-first-hi`: its `method` is set anew and its reading is taken.
> **＋** `rule-morph`: the setup Case at the first `/hi`.
> **＋** `rule-skill-setup`: the skill `/setup` that builds the setup Case.
> **＋** `rule-plugin-install`: the skill `/guppi:install`.
> **＋** `rule-ledger-write`: the ledger hook.
> **＋** `guppi.toml`: the settings file that holds `setup_done`, `test` and `style`.
> **＋** `/sprint-open`: the skill that opens the first sprint after the setup Case.
> **＋** `.guppi/`: the code of GUPPI in the project.
> **＋** `vault/`: the vault of the project.
> **＋** `.claude/`: the harness files of the project.
> **＋** `guppi-set-aside/`: the folder of the files set aside.

> **when:**
> In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` holds `setup_done = false`, the person reopens Claude Code and types `/hi`.

> **then:**
> `/hi` opens the session and starts `/setup` of `rule-skill-setup`, which puts the setup Case of `rule-morph` first, before the opening Case of the first sprint and before the Frontier.
> **＋** The setup Case takes the name of the project's folder of saved transcripts from the path of the project.
> **＋** It asks the person only for the values it cannot find: the language of the repository, the language of the chat and the description of the project.
> **＋** Where the file paths of the project show a file of a programming language outside `.guppi/`, `vault/`, `.claude/` and `guppi-set-aside/`, one plain question says that GUPPI's own tests and style check keep running in the project, says why it asks, and asks how the project's own tests and style check run beside them, and the commands the person gives stand after GUPPI's commands in the keys `test` and `style` of `guppi.toml`.
> **＋** Every value stands in that one setup Case, which the person ratifies or corrects, and the ledger hook of `rule-ledger-write` writes its decision lines though no sprint is open.
> **＋** The reply that acknowledges the setup Case shows no Frontier and ends with the open question on what the first sprint is to build, and on the person's answer `/sprint-open` starts in the same session with that answer.
> **＋** The librarian's run of that session writes the settings by the render of the rule pages that hold them, `guppi.toml`, the description of the project in `CLAUDE.md` and the read rules of the saved transcripts, and `guppi.toml` then holds `setup_done = true`.
> **－** `/guppi:install` is no Case, and the person ratifies nothing at it.
> **－** Between `/guppi:install` and that librarian's run, no settings file changes but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs.
> **－** The setup step asks for no category set, no name of the main branch and no git remote, reads no code of the project and creates no page for it.
> **－** Where the file paths show no such file, it asks nothing on tests or style, and the keys `test` and `style` stay as they are.
> **－** The question names no key of `guppi.toml`, GUPPI's commands leave no key, and no key becomes an empty list.
> **－** It asks no question on how the setup Case splits or how it is checked.
> **－** A project whose `guppi.toml` does not hold `setup_done = false` gets no setup Case at `/hi`.

```then
update:
- slug: estimate-morph-sets-up-the-project-at-the-first-hi
  set:
    method: 'by hand, after the install stop of the Work Mode that sets this method: the plugin guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, in a git project made by git init -b main after the install that holds a CLAUDE.md and a code file of its own, and in a git project that holds only a LICENSE of its own, /guppi:install typed, Claude Code reopened, /hi typed and that session taken to its librarian''s run, the transcript of each of those sessions under ~/.claude/projects, its ledger and the files written in it read against the Criterion, recorded in the estimate line'
  change: the method set anew — the project with code is the one of the git init offer, the project with no code the one that holds only a LICENSE, at the install stop of Work Mode
```

```tasks
- [ ] update `estimate-morph-sets-up-the-project-at-the-first-hi`
- [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`
```

### Case 1055.3 — The git init offer is read at the install stop

> **given:**
> `estimate-git-context-offers-git-init`: its `method` is set anew and its reading is taken.
> **＋** `rule-git-context`: the git step of `/hi`.
> **＋** `.claude/skills/hi/SKILL.md`: the skill that opens a session.
> **＋** `rule-skill-hi`: sets `/hi`.
> **＋** `rule-default-mode`: sets the writes allowed before a ratified Case.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of a session.
> **＋** `/sprint-open`: the skill that opens a sprint.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` in a project folder in Plan Mode, and its `Branch:` line, which runs `uv run --project .guppi guppi gitstate` of `rule-git-context`, reads `none: this folder is no git repository`.

> **then:**
> Before `/sprint-open` and before the Frontier, the agent says that GUPPI works only in a git repository, tells the person to type `! git init -b main`, which names the first branch `main`, and then `/hi` again, and ends the reply.
> **＋** The person's `! git init -b main` runs in Plan Mode as the person's own shell command and makes the repository.
> **＋** The next `/hi` prints `main` under `Branch:` and goes on as `rule-skill-hi` sets it.
> **－** That `/hi` asks the person no question, starts no `/sprint-open` and writes no `raw/<date>/<hi HHMM>/frontier.md`.
> **－** The agent runs no `git init -b main` and writes nothing, as `rule-default-mode` sets it, and `allowed-tools` of `.claude/skills/hi/SKILL.md` does not name `git init -b main`.

```then
update:
- slug: estimate-git-context-offers-git-init
  set:
    method: 'by hand, after the install stop of the Work Mode that sets this method, in a repository that holds the module of the command ship: in a folder that is no git repository and holds a CLAUDE.md and a code file of its own, GUPPI installed by /guppi:install from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, Claude Code reopened there, /hi typed, ! git init -b main typed as the reply tells, then /hi typed again, and the replies, the context of each /hi and the session folders in the transcripts of those sessions under ~/.claude/projects/, and git branch --show-current, read against the Criterion, recorded in the estimate line'
  change: the method set anew — the folder with no git is the one of the install in Plan Mode, at the install stop of Work Mode
```

```tasks
- [ ] update `estimate-git-context-offers-git-init`
- [ ] read `estimate-git-context-offers-git-init`
```

### Case 1055.4 — The copy into a project with its own LICENSE is read at the install stop

> **given:**
> `estimate-plugin-install-writes-guppi-into-an-empty-project`: its `method` is set anew and its reading is taken.
> **＋** `rule-plugin-install`: the skill `/guppi:install`.
> **＋** `rule-clean-branch`: the clean version that `guppi ship` builds.
> **＋** `plugin/skills/install/SKILL.md`: the skill the person types.
> **＋** `.guppi/guppi/ship.py`: the command that writes the clean copy.
> **＋** `.guppi/tests/test_ship.py`: the tests of the copy.
> **＋** `/plugin marketplace add <folder>`: the command that adds the copy as a catalogue.
> **＋** `/plugin install guppi@guppi-marketplace`: the command that installs the plugin.
> **＋** `/hi`: the skill the last message of the install names.
> **＋** `vault/`: the vault the copy holds.
> **＋** `vault/wiki/`: the pages the install copies.
> **＋** `.claude-plugin/`: the folder of the plugin's manifest.
> **＋** `.git/`: the git folder of the plugin.
> **＋** `.claude/settings.json`: the settings file the install copies.
> **＋** `.claude/skills/`: the skills the install copies.
> **＋** `.guppi/LICENSE`: the license file of the code.

> **when:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
> **＋** The agent writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`; the person adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` of `plugin/skills/install/SKILL.md`, as `rule-plugin-install` sets it, in a project open in Claude Code that holds a `LICENSE` of its own and none of the files the install writes.

> **then:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
> **＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
> **＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
> **＋** `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/` and the file `LICENSE` at the root of the plugin, such as `CLAUDE.md`, `.claude/settings.json`, `.guppi/LICENSE`, the code under `.guppi/` and the pages under `vault/wiki/`.
> **＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
> **－** The `LICENSE` of the project stays at its path with its text unchanged: the install neither stops on it nor sets it aside.
> **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
> **－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
> **－** Which files a new project needs, what the install does about `uv` and the Python environment under `.guppi/`, and what it does with a file of the project that stands at one of its paths are no part of this promise.

```then
update:
- slug: estimate-plugin-install-writes-guppi-into-an-empty-project
  set:
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, after the install stop of the Work Mode that sets this method: with a tag prod-x.y.z in the history of HEAD, the clean version written by the agent into a local folder by uv run --project .guppi guppi ship --allow-draft, and in a git project that holds only a LICENSE of its own, the person adds that folder as a catalogue by /plugin marketplace add, installs guppi by /plugin install guppi@guppi-marketplace and types /guppi:install; the files of the project, its LICENSE among them, read against those of the plugin and against the Criterion, and the calls of the install read in the transcript of that session under ~/.claude/projects/'
  change: the method set anew — the reading taken at the install stop of Work Mode, in the project that also serves the setup with no code
```

```tasks
- [ ] update `estimate-plugin-install-writes-guppi-into-an-empty-project`
- [ ] read `estimate-plugin-install-writes-guppi-into-an-empty-project`
```

### Case 1055.5 — The set-aside files are read at the install stop

> **given:**
> `estimate-plugin-install-sets-aside-the-files-of-the-project`: its put-off is retired, its `method` is set anew and its reading is taken.
> **＋** `rule-plugin-install`: the skill `/guppi:install`, which sets files aside.
> **＋** `plugin/skills/install/SKILL.md`: the skill the person types.
> **＋** `guppi-set-aside/`: the folder of the files set aside.
> **＋** `rule-where-to-stop`: the stop before a push.
> **＋** `.claude/`: the harness files of the project.
> **＋** `.claude/settings.json`: the settings file of the project and of GUPPI.
> **＋** `.github/workflows/checks.yml`: a workflow file the install writes.
> **＋** `/hi`: the skill at which the set-aside files are kept or dropped.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in a project open in Claude Code, where `uv --version` passes, that holds a `CLAUDE.md`, a `.claude/settings.json` and a `.gitattributes` of its own and no other file of the install.

> **then:**
> Before it copies, the agent moves each file of the project at a path of the install that is `CLAUDE.md`, a file under `.claude/` but `.claude/settings.json`, `.gitattributes` or `.github/workflows/checks.yml` into `guppi-set-aside/`, under its old path with `.set-aside` added to its name.
> **＋** It moves the `.claude/settings.json` of the project into `guppi-set-aside/` the same way only after `uv sync` passes, just before it copies the `.claude/settings.json` of GUPPI.
> **＋** Its last message lists each file it set aside with its path under `guppi-set-aside/`, and says that none of them loads or runs until the person keeps or drops it at the first `/hi`.
> **＋** When `uv sync` fails, it deletes what it copied, moves each file it set aside back to its old path and deletes `guppi-set-aside/`, so that the project holds only what it held before.
> **－** It changes no text of a file it sets aside, and sets aside no file at a path that the install does not write.
> **－** In a project that holds a file of the install at any other path, or that already holds `guppi-set-aside/`, it lists them, writes and moves nothing, and stops.
> **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.

```then
update:
- slug: estimate-plugin-install-sets-aside-the-files-of-the-project
  set:
    method: 'by hand, after the install stop of the Work Mode that sets this method: with a tag prod-x.y.z in the history of HEAD, the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in a project that holds a CLAUDE.md, a .claude/settings.json with a hook and a .gitattributes of its own, /guppi:install typed; in a second such project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, /guppi:install typed; in a third project with a vault/wiki/glossary.md of its own, a path the install writes, /guppi:install typed; the transcripts and the files of the three projects before and after read against the Criterion, recorded in the estimate line'
  change: the put-off retired before it was applied; the reading taken at the install stop of Work Mode
```

```tasks
- [ ] update `estimate-plugin-install-sets-aside-the-files-of-the-project`
- [ ] read `estimate-plugin-install-sets-aside-the-files-of-the-project`
- [x] stop: at the end of Work Mode, the person types `! git push origin plugin`, and `git status` then shows the branch up to date with `origin/plugin`.
```

## Case 1057 — A one-off Estimate is done only when one reading passes

> **context:**
> A one-off Estimate carries `once: true`. It checks one state once and targets the live sprint page. Case 1046 set the Purpose of `entity-sprint-plugin` to say that such an Estimate is done once it is read, and that a failed reading stays as the record. Case 1051 made `guppi sprint` tick a failed one-off Estimate under Done when. The close of a sprint, in `settled` of `.guppi/guppi/sprint_close.py`, already took a failed Estimate of the sprint page to the archive with no choice by name. Only lint disagreed: `check_unread` of `.guppi/guppi/lint.py` reports every `failed` Estimate as `unread: failed`. So `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` stood ticked and red at once. The person reversed Cases 1046 and 1051. A failed reading is not done. A one-off Estimate is worked on until one reading passes, and `once` means that one passed reading is enough. Lint stays as it is, and the Criterion of `estimate-lint-checks-the-statuses` stands, since it already says that a `failed` Estimate earns its `unread` finding whatever its `method` says. Case 1057.1 changes the sprint page and replaces the Criterion of `estimate-sprint-plugin-done-counts-a-one-off-reading`, whose last line kept the frontierguard Estimate `failed`. Case 1057.2 changes the tick in `.guppi/guppi/sprint.py` line 257 and the sentence of `rule-sprint` that states it, and replaces the Criterion of `estimate-sprint-ticks-a-read-one-off-estimate`; its slug stays, since a rename is a choice of form that changes nothing it does. Case 1057.3 makes the close refuse a failed Estimate of the sprint page that is not named by `--archive-unread`, in `settled` and `estimate_lines` of `sprint_close.py`, its docstring and the test `test_settle_failed_sprint_page_estimate_goes_with_the_page_its_status_kept` of `.guppi/tests/test_sprint_close.py`; it replaces the Criterion of `estimate-sprint-close-settles-unread-estimates`, whose purpose stated the old promise and is set anew. The Purpose of `rule-sprint-close` names no settling and stands. The sentences of `entity-sprint` and `rule-sprint` saying that an Estimate that has not passed goes to the archive with its status kept in the record of the close still hold, since an Estimate archived unread moves in the same close and its History keeps its old status. Case 1057.4 replaces the Criterion of the frontierguard Estimate. The old Criterion reads one past build, the build of Case 1012, and that build did not read the root `.gitignore`, so no reading again could pass it. The new Criterion reads a later build of this sprint, and its `method` waits for that build, as `case-schema.md` allows for an Estimate of a sprint page. The docstring of `is_one_off` of `.guppi/guppi/ledger.py` names `sprint.py` as a caller; that changes with 1057.2. `guppi sprint --check`, run by `uv run --project .guppi guppi check`, goes red on `vault/wiki/sprint.md` between the code change and the librarian's `guppi sprint`; that red is a note for the handoff, and `rule-retro` sets it so. The tests that read `sprint.md` or a sprint page all write a copy under a temporary folder, by a Grep of `.guppi/tests/` for `entity-sprint-plugin|wiki/sprint\.md|"sprint\.md"|frontierguard-build`, so no live test changes. The person also said that a one-off Estimate that has passed is not read again when its pages change. This Case does not set that as a general rule, since what a Case names when it changes a page is the rule of `case-schema.md`. The `－` line of 1057.4 holds for that one Estimate alone, and 1057.1 adds the general rule as a line to the `## Backlog` of `entity-sprint-plugin`, by the person's answer to a question of `/pre-spec`. Case 1057.5 changes step 4 of `rule-skill-sprint-close`, rendered to `.claude/skills/sprint-close/SKILL.md`, which named by `--carry` or `--archive-unread` only an Estimate still unread or one read `failed` that the sprint page does not list, so a close line built by it would be refused after 1057.3; it replaces the Criterion of `estimate-sprint-close-takes-the-readings-in-groups`, whose `－` line said the same, and sets its purpose anew. Both findings came from `/pre-spec`. It is a sub-case of its own, since it is the promise of the skill and not of the command. The sentence of step 4 around the pair was read whole and reads whole with the new words. The files that the check listed as naming `rule-skill-sprint-close`, `SKILL.md` or `/sprint-close` speak, by their purpose lines and paths, of other steps and skills and stand; the case files of Cases 1053, 1054 and 1055 are built at the same time as this one and were not read. The check of this file listed the files that name `entity-sprint-plugin`, `rule-sprint`, `sprint.py`, `sprint.md`, `ledger.py`, `generate.py`, `sprint_close.py`, `guppi sprint`, `guppi sprint-close` and `guppi ledger`; judged by their purpose lines and paths, they speak of other behaviour of those pages and stand. Of the ones that speak of the close, the When of `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` already says that each Estimate of the sprint page not `passed` is read or archived unread, and step 3 of `.claude/skills/sprint-close/SKILL.md` sorts the `pending` and `failed` Estimates by the moment their `method` names; both stand with 1057.3. No `error` lesson stands in the ledger of this session, by a Grep for `lesson\[error\]` and for `\{addresses:`, so no mark is added.

> **problem:**
> A failed one-off Estimate counts as done on the sprint page, in `sprint.md` and at the close, but stays red in lint. The person decided that a failed reading is not done.

> **recommend:**
> - **Does lint still flag a failed one-off Estimate of a sprint page?**
>   - Recommended: (a) no flag for a failed one-off reading of a sprint page.
>   - Answer: none of the options; a failed reading is not done, and the earlier decision is reversed; a one-off Estimate is worked on until it passes once, and `once` means one passed reading is enough, so it is not read again when pages change.
> - **How does this one Estimate reach a passed reading?**
>   - Recommended: (a) a new Criterion on a fresh build.
>   - Answer: (a).
> - **What does the close of the sprint do with a failed one-off Estimate?**
>   - Recommended: (a) the close refuses it unless it is named.
>   - Answer: (a).
> - **Change**
>   - Asked: findings of `/pre-spec` — step 4 of `rule-skill-sprint-close` and `estimate-sprint-close-takes-the-readings-in-groups` would be false after 1057.3; the `－` line of 1057.4 and its purpose went past the bound of `context`; the person agreed that the line holds for that Estimate alone and that the general rule goes into the Backlog of `entity-sprint-plugin`.
>   - Taken: Case 1057.5 added; the `－` line of 1057.4 names this Estimate alone; 1057.1 adds the Backlog line.

### Case 1057.1 — The sprint page counts a one-off Estimate done when it passes

> **given:**
> `entity-sprint-plugin`: the sprint page whose Purpose says when an Estimate is done.
> **＋** `estimate-sprint-plugin-done-counts-a-one-off-reading`: its Criterion is replaced whole.

> **when:**
> Someone reads the Purpose of `entity-sprint-plugin` after the librarian's run.

> **then:**
> An Estimate of the page is done when it passes, one with `once: true` too.
> **＋** A one-off Estimate whose reading failed is not done, and it is worked on until one reading passes.
> **－** A failed reading of a one-off Estimate is not called done or kept as its record of done.

```then
update:
- slug: entity-sprint-plugin
  replace:
  - old: 'Done when every Estimate of this page that checks a lasting behaviour passes, and each one-off Estimate, which carries `once: true`, is read, a failed reading kept as the record of what it found:'
    new: 'Done when every Estimate of this page passes, a one-off Estimate, which carries `once: true`, by one reading that passes, a failed one worked on until a reading passes:'
  - old: the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)
    new: |-
      the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)
      - Whether a one-off Estimate that has passed once is never read again, so that a Case that changes its pages gives it no update and sets it `pending` no more, as `case-schema.md` would then set it; the person's view in session 0816 (case 1057)
  change: a one-off Estimate is done when one reading passes, a failed reading not done; the Backlog asks whether a passed one-off Estimate is never read again
- slug: estimate-sprint-plugin-done-counts-a-one-off-reading
  set:
    status: pending
    purpose: Whether the sprint page says that an Estimate, a one-off one too, is done when it passes, and that a failed one-off reading is not done; read once
    method: 'by hand, after the librarian''s run of session 0816: the Purpose of vault/wiki/entities/entity-sprint-plugin.md read against the Criterion, in the estimate line'
  change: the Criterion replaced whole — a one-off Estimate is done when one reading passes
```

```tasks
- [ ] update `entity-sprint-plugin`
- [ ] update `estimate-sprint-plugin-done-counts-a-one-off-reading`
- [ ] read `estimate-sprint-plugin-done-counts-a-one-off-reading`
```

### Case 1057.2 — guppi sprint ticks only a passed Estimate

> **given:**
> `rule-sprint`: the rule of `sprint.md`, whose Purpose states the tick of Done when.
> **＋** `.guppi/guppi/sprint.py`: `render`, which ticks the lines of Done when.
> **＋** `.guppi/tests/test_sprint.py`: the test of the tick of a one-off Estimate.
> **＋** `.guppi/guppi/ledger.py`: the docstring of `is_one_off`, which names its callers.
> **＋** `estimate-sprint-ticks-a-read-one-off-estimate`: its Criterion is replaced whole.
> **＋** `vault/wiki/sprint.md`: the file that `guppi sprint` writes.

> **when:**
> `uv run --project .guppi guppi sprint` of `.guppi/guppi/sprint.py` renders `vault/wiki/sprint.md` from a sprint page whose `estimates` hold a `passed` Estimate, a `pending` one, a `failed` one with `once: true` and a `failed` one with no `once`.

> **then:**
> The line of the `passed` Estimate stands under Done when as `- [x]`.
> **＋** Each line keeps its status after ` · `, `failed` included.
> **－** The line of the `pending` Estimate and the lines of both `failed` ones stay `- [ ]`.

```then
update:
- slug: rule-sprint
  replace:
  - old: 'Under Done when, the line of an Estimate is ticked when it is `passed`, or when it is `failed` and carries `once: true`, since a one-off Estimate is done once it is read; its status stands after ` · ` (as set in case 1051).'
    new: 'Under Done when, the line of an Estimate is ticked only when it is `passed`, one with `once: true` too, since a failed reading is not done; its status stands after ` · ` (as set in case 1057.2).'
  change: Done when ticks only a passed Estimate, a failed one-off one left unticked
- slug: estimate-sprint-ticks-a-read-one-off-estimate
  set:
    status: pending
    purpose: 'Whether guppi sprint ticks under Done when only a passed Estimate, keeps each status, and leaves a pending one and a failed one, with once: true or without, unticked'
  change: the Criterion replaced whole — a failed one-off Estimate stays unticked
```

```tasks
- [ ] update `rule-sprint`
- [x] `.guppi/guppi/sprint.py`: `render` ticks a line of Done when only for a `passed` Estimate, and the module docstring says so.
- [x] `.guppi/tests/test_sprint.py`: `test_a_read_one_off_estimate_is_ticked_and_keeps_its_status` expects `- [ ] read once · failed`, under a name that says a failed one-off Estimate stays unticked.
- [x] `.guppi/guppi/ledger.py`: the docstring of `is_one_off` names `.guppi/guppi/lint.py` alone as its caller.
- [ ] update `estimate-sprint-ticks-a-read-one-off-estimate`
- [ ] read `estimate-sprint-ticks-a-read-one-off-estimate`
```

### Case 1057.3 — The close refuses a failed Estimate of the sprint page not named

> **given:**
> `.guppi/guppi/sprint_close.py`: `settled`, `estimate_lines` and the module docstring.
> **＋** `.guppi/tests/test_sprint_close.py`: the tests of the settling.
> **＋** `estimate-sprint-close-settles-unread-estimates`: its Criterion is replaced whole.
> **＋** `rule-sprint-close`: the rule of the close.
> **＋** `entity-sprint-<id>`: the sprint page that the close closes.
> **＋** `vault/wiki/estimates/`: the live Estimates the close lists.
> **＋** `vault/archive/`: where the moved pages stand.

> **when:**
> `uv run --project .guppi guppi sprint-close --sprint <id>` closes the sprint `entity-sprint-<id>` of the made-up vault of `.guppi/tests/test_sprint_close.py`, its preview first and then its run with `--apply`; someone reads its output, the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.
> **＋** Or the preview `uv run --project .guppi guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/estimates/`.

> **then:**
> Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
> **＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
> **＋** A listed Estimate counts as settled only when the close names it by `--carry` or `--archive-unread`, one that `entity-sprint-<id>` lists and that stands `failed` included.
> **＋** The run with `--apply` refuses, moving nothing, while a listed Estimate is not settled.
> **＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
> **＋** An Estimate archived unread stands under `vault/archive/`, its old status kept in its History, and the page that listed it no longer lists it in `estimates`.
> **－** An Estimate that `entity-sprint-<id>` lists is not carried into the next sprint: the person reads it now or archives it unread.

```then
update:
- slug: estimate-sprint-close-settles-unread-estimates
  set:
    status: pending
    purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves; an Estimate of the sprint page is read or archived unread and never carried, one that stands failed too; no listed Estimate is settled until the close names it
  change: the Criterion replaced whole — a failed Estimate of the sprint page is settled only by --archive-unread
```

```tasks
- [x] `.guppi/guppi/sprint_close.py`: `settled` counts an Estimate of the sprint page as settled only when `--archive-unread` names it, `estimate_lines` drops the way `goes with the sprint page, its status kept`, and the module docstring says that a failed Estimate of the sprint page is settled only by name.
- [x] `.guppi/tests/test_sprint_close.py`: `test_settle_failed_sprint_page_estimate_goes_with_the_page_its_status_kept` asserts that the run refuses an unnamed failed Estimate of the sprint page and moves nothing, and that with `--archive-unread` it stands archived with `status: failed → archived` in its History.
- [ ] update `estimate-sprint-close-settles-unread-estimates`
- [ ] read `estimate-sprint-close-settles-unread-estimates`
```

### Case 1057.4 — The frontierguard Estimate reads a fresh build

> **given:**
> `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`: its Criterion, purpose and method are replaced.
> **＋** `entity-sprint-plugin`: the sprint page it targets.
> **＋** `~/.claude/projects/`: where the agent transcript of the build stands.
> **＋** `vault/wiki/`: the pages, outside which the build adds a file.
> **＋** `.guppi/guppi/`: the code the build searches.
> **＋** `.guppi/tests/`: the tests the build searches.
> **＋** `.claude/`: the harness files the build searches.
> **＋** `vault/wiki/rules/`: the rules the build searches.

> **when:**
> The agent transcript under `~/.claude/projects/` of a `case-guppi` build of the sprint `plugin` whose Case adds a file outside `vault/wiki/`, and its case file, are read against this Criterion.

> **then:**
> That build searched `.guppi/guppi/`, `.claude/` and `vault/wiki/rules/` for the path of each folder that holds the new file, the root left out.
> **＋** It searched `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
> **＋** It read each ignore file of git in each folder from the folder of the new file up to the root of the repository, the root `.gitignore` included.
> **＋** It read each reader that takes every file of such a folder.
> **＋** Each reader that the new file makes wrong entered the Case, or its `context` names it and says why it stands.
> **＋** That `context` names each of those searches, with its pattern, its paths and each file or count it printed, and each ignore file and reader it read, with whether the new file makes it wrong.
> **－** Once one such reading passes, this Estimate is not read again.

```then
update:
- slug: estimate-sprint-plugin-frontierguard-build-read-its-folders-readers
  set:
    status: pending
    purpose: Whether a case-guppi build of the sprint plugin that adds a file outside vault/wiki/ makes and names in context each search and reading for the folders of the new file that rule-case-build sets, the root .gitignore included; passes once
    method: 'by hand, after a case-guppi build of the sprint plugin whose Case adds a file outside vault/wiki/: its agent transcript under ~/.claude/projects/ searched by a Grep with lines of context for each search and reading of the Criterion, and its case file read for the list of them in its context; the transcript, the case file and the result in the estimate line'
  change: the Criterion replaced whole — a fresh build read, since the build of Case 1012 cannot pass
```

```tasks
- [ ] update `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`
- [ ] read `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`
```

### Case 1057.5 — The closing Case names each failed Estimate of the sprint page

> **given:**
> `rule-skill-sprint-close`: the skill of the closing session, whose step 4 builds the close line.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the Render of that rule.
> **＋** `estimate-sprint-close-takes-the-readings-in-groups`: its Criterion is replaced whole.
> **＋** `entity-sprint-<id>`: the sprint page that the session closes.
> **＋** `vault/wiki/estimates/`: the live Estimates that the closing Case sorts.
> **＋** `vault/raw/<date>/<hi HHMM>/spec.md`: the Spec of the closing session.
> **＋** `vault/raw/<date>/<hi HHMM>/ledger.md`: the ledger of the closing session.

> **when:**
> The session that closes `entity-sprint-<id>` runs its Plan Mode and its Work Mode; someone reads its closing Case in `vault/raw/<date>/<hi HHMM>/spec.md` and its `vault/raw/<date>/<hi HHMM>/ledger.md` after its Work Mode.

> **then:**
> The `context` of the closing Case sorts each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed` into groups by the kind of moment its `method` names.
> **＋** The `tasks` of the closing Case hold one `by hand` task per moment that Work Mode sets up, and one `read` line per Estimate of each group.
> **＋** Work Mode sets up each such moment, and the ledger holds a reading of each Estimate whose moment came.
> **＋** The close line names by `--carry` or `--archive-unread` each Estimate read `failed` in Work Mode that `entity-sprint-<id>` does not list.
> **＋** The close line names by `--archive-unread` each Estimate that `entity-sprint-<id>` lists and that stands `failed`.
> **－** The close line names no Estimate that stands `passed`.

```then
update:
- slug: rule-skill-sprint-close
  replace:
  - old: and each one read `failed` in Work Mode that the sprint page does not list; an Estimate of the sprint page is never carried
    new: each one read `failed` in Work Mode that the sprint page does not list, and, by `--archive-unread` alone, each Estimate of the sprint page that stands `failed`; an Estimate of the sprint page is never carried
  change: step 4 names each failed Estimate of the sprint page by --archive-unread
- slug: estimate-sprint-close-takes-the-readings-in-groups
  set:
    status: pending
    purpose: Whether the session that closes a sprint sorts the pending and failed Estimates into groups by the kind of moment their method names, sets up each moment it can in its Work Mode, and names in the close line each one still unread, each one read failed, and each failed Estimate of the sprint page by --archive-unread
  change: the Criterion replaced whole — the close line names each failed Estimate of the sprint page
```

```tasks
- [ ] update `rule-skill-sprint-close`
- [ ] `uv run --project .guppi guppi render`: `.claude/skills/sprint-close/SKILL.md`
- [ ] update `estimate-sprint-close-takes-the-readings-in-groups`
- [ ] read `estimate-sprint-close-takes-the-readings-in-groups`
```
