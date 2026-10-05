<!-- approved 05:20:53 · session 6d53e05d -->

# Spec — session 0311, 2026-10-05

## Case 644 — The Spec hook writes a Case at the reply that answers a refusal

> **context:**
> The `Stop` hook `guppi ratified` copies a ratified Case into the plan file, and into `spec.md` once that file exists, after a reply whose `LEDGER` block carries the Case's decision lines. When an end-of-reply hook refuses a reply, the agent answers the refusal at once in a new reply. Claude Code sets `stop_hook_active` on that reply and keeps it set until the person writes again (measured for case 577.3). `stop` in `guppi/ratified.py` returns 0 at its first line when the flag is set (line 821). So it writes, removes and checks nothing on any reply after a refusal until the person's next message. The hook's own refusals still tell the agent to fix the cause and then repeat the ledger lines. `rule-spec-write` says a Case not yet written is written at the reply that repeats its lines. Both hold only when the repeat comes after a new message from the person. In session 0109 the short-form defer of Case 642 was refused for the shape of its `then` block. The agent fixed it and showed it again with its ledger line in the next reply, and nothing was written. The Case reached the plan file only on its third showing, after the person wrote again (`lesson-spec-write-skips-the-reply-that-answers-a-refusal`, ledger line 24 of session 0109).
>
> The ledger hook had the same gap and closed it in case 577.3. It writes whether or not the flag is set. It guards its own loop by its refusals in the stretch, the transcript after the person's last message. `own_refusals` of `guppi/ledger.py` reads them, and `untold` holds back a line already told. The person chose that `guppi ratified` writes on a flagged reply too, with the same guard. A reason already given since the person's last message is not given again. A new reason is given once. The guard reuses the functions of `guppi/ledger.py`, so the judgment stays in one module (`CLAUDE.md`, One judgment, one implementation). The person chose to keep the change to this hook alone. `orchestration.md` says the agent's answer to a refusal is a reply of its own, and that the Spec hook writes a Case only after a reply that carries its lines. Both stay true. The `Stop` check of `rule-case-check` also skips flagged replies and stays as it is: it loses nothing, since this hook runs the same comparison with the stored text before it writes.
>
> The `/pre-spec` run of `ask-guppi` found three faults in the ratified Case, and this build fixes them.
> - The write on a flagged reply and the loop guard can fail apart, and they need different fixes (`rule-atomicity`). The person chose two Estimates. `estimate-spec-write-answers-a-refusal` (644.1) checks the write. `estimate-spec-write-tells-each-reason-once` (644.8) checks the guard. Each of the six Estimates of `rule-spec-write` says today that nothing happens when the flag is set. In each, that line is replaced by a line that points to the Estimate or Estimates it needs, so each Criterion is replaced whole, one sub-case per Estimate.
> - 644.7 now carries the exception that `estimate-ledger-write-exits-2-on-an-error` states. With the flag set and a transcript the hook cannot read, it cannot tell whether a refusal of its own stands, so it exits 0 and prints nothing. `rule-spec-write` gets pairs on its error sentence and on its reason for an error while the hook reads the payload, so the page agrees with 644.1, 644.7 and 644.8.
> - Case 645 of this session makes `case-guppi` write its Case into its file and hand back a summary. The check copies the file into the store, and the Spec hook keeps reading the store. So the Criteria that 644.2 and 644.5 set anew speak of the text stored under Case N, not of the answer of `case-guppi`.
>
> Case 645.5 changes the sentence of `rule-spec-write` on the time of the store, which none of the pairs here touches. Its `then` line on the flag points to `estimate-spec-write-answers-a-refusal` both for writing on a flagged reply and for a reason not given twice. After the split, the second half belongs to `estimate-spec-write-tells-each-reason-once`. 645.5 needs that line to point to the new Estimate for the guard.
>
> The frame I read, by these searches:
> - A Grep of `stop_hook_active|re-fire` over `vault/wiki/`, with `!**/decisions/**`, printed 34 files. They are placed as follows:
>   - `rule-spec-write` and its six Estimates enter the Case.
>   - `lesson-spec-write-skips-the-reply-that-answers-a-refusal` is the source. It is a lesson of another session, so it gets no mark.
>   - `brief.md` and `log.md` were not read.
>   - `rule-case-check`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-refuses-text-outside-the-list`, `estimate-case-check-refuses-text-before-a-round`, `estimate-case-check-shows-only-the-checked-case` and `estimate-case-check-exits-2-on-an-error` set the behaviour of the comparison check, which stays as it is. Its hit on `rule-case-check` is a History line.
>   - `rule-ledger-write` (a History line), `estimate-ledger-write-lifts`, `estimate-ledger-write-refuses-a-line-it-cannot-read`, `estimate-ledger-write-refuses-a-mark-with-no-decision-line`, `estimate-ledger-write-refuses-a-lesson-without-its-prefix`, `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` and `estimate-ledger-write-exits-2-on-an-error` set the ledger hook, the model this Case follows.
>   - `rule-retro-onward`, `rule-prespec-onward`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-onward-exits-2-on-an-error` and `estimate-prespec-onward-sends-the-agent-on` set `guppi onward`. `estimate-context-size-shown-after-each-reply` and `estimate-context-size-shows-its-error` set `guppi context`. Each speaks of its own hook only.
>   - `insight-case-show-built-case-retyped-by-hand` says the comparison on `Stop` lets the re-fire through. That is the comparison check, which stays as it is.
>   - `lesson-hooks-stop-payload`, `lesson-hooks-subagentstop-exit-2-sends-the-subagent-back` and `lesson-hooks-subagentstop-fires-before-and-after-the-handback` record what the payload carries, and that stays true.
> - A Grep of `answers a refusal|answer to the refusal|answers the refusal|re-fire|repeats? (its|the) ledger lines` over `vault/wiki/rules/` printed `rule-orchestration.md`, `rule-retro.md` and `rule-spec-write.md`. Over `.claude/` it printed nothing.
>   - `rule-orchestration` says the agent's answer to a refusal is a reply of its own and may call tools, which stays true.
>   - The hit in `rule-retro` is a History line.
> - A Grep of ``` `refusals`|ledger\.refusals|own_refusals ``` over `vault/wiki/`, with `!**/decisions/**`, printed `estimate-prespec-onward-reads-the-decisions-of-the-session.md` and `estimate-ledger-write-names-the-kind-of-a-user-record.md`. Both stand.
>   - The second names the hooks that read the stretch for their own refusals. It says no module but `guppi/ledger.py` judges the kind of a `user` record. The hook reaches the stretch through `own_refusals` and judges no kind itself, so each line stays true.
>   - The first speaks of `guppi onward` alone.
> - A Grep of `stop_hook_active` over `guppi/` printed `guppi/ledger.py`, `guppi/casecheck.py`, `guppi/onward.py`, `guppi/context.py` and `guppi/ratified.py`. The return at line 821 and the docstring of `guppi/ratified.py` enter the Case. The other modules set their own hooks.
>
> The `Stop` event in `.claude/settings.json` also runs `guppi ledger`, `guppi casecheck`, `guppi context`, `guppi onward` and `guppi onward --plan`. `guppi onward --plan` judges open Cases by the ledger lines, not by the plan file, so writing on a flagged reply does not change what it sees. Both new Estimates carry a `ref`, so the vault query of `ask-guppi` was not run. A Glob `vault/**/*spec-write-{answers,tells}*` printed nothing, so both slugs are free.
>
> The check sent back two kinds of notes, and both stand:
> - Notes on Criterion lines that 644.2 and 644.5 do not carry. Each change is on purpose: the line about the flag, and the text stored under Case N in place of the answer of `case-guppi`.
> - Notes on `then` lines of sibling sub-cases that share many words. The six Criteria keep the shared wording they had, and their lines about the flag share the words of the two Estimates they point to. Each sub-case still sets its own promise: the write on a flagged reply (644.1), the copy (644.2), the check after the write (644.3), a defer (644.4), the approved Spec (644.5), the removal of a superseded Case (644.6), an error (644.7) and the loop guard (644.8). 644.7 and 644.8 both say what happens with the flag set and an unreadable transcript, one for an error and one for every reason.
>
> Not done:
> - The comparison check of `rule-case-check` still skips flagged replies.
> - `orchestration.md` gains no sentence.

> **problem:**
> The Spec hook does nothing on a reply that carries `stop_hook_active`. Claude Code keeps the flag set on every reply after a refusal until the person writes again. So a Case refused at the reply that acknowledges it, then fixed and repeated in the next reply as the hook's own advice asks, is never written until the person sends one more message and sees the Case once more. The question was whether the rules describe this gap or the hook closes it, how it then avoids a loop, how that is checked, and what else changes.

> **recommend:**
> - **Describe the gap or write on the reply that answers a refusal**
>   - Recommended: (b) the hook writes there too: it writes, removes and checks Cases whether or not the flag is set, as the ledger hook already does, and keeps itself from looping by its own refusals in the transcript since the person's last message; the six Estimates of `rule-spec-write` get their Criteria replaced.
>   - Answer: agreed, (b).
> - **How the hook keeps itself from looping**
>   - Recommended: (a) each refusal once until the person writes: a refusal whose text already stands in one of the hook's own refusals since the person's last message is not given again; a new one is given once; with the flag set and a transcript it cannot read, the hook writes and exits 0 without a word; it reads its refusals through the function the ledger hook and `guppi onward` already use.
>   - Answer: agreed, (a).
> - **How the new behaviour is checked**
>   - Recommended: (a) a new Estimate, `estimate-spec-write-answers-a-refusal`, for the write on a flagged reply and the loop guard; in each of the six Criteria the line about the flag points to it; seven sub-cases.
>   - Answer: agreed, (a).
> - **What else the Case covers**
>   - Recommended: (a) the hook alone: `guppi/ratified.py`, its tests, `rule-spec-write` and its Estimates; `orchestration.md` and the comparison check stay as they are.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the write on a flagged reply and the loop guard were found to be two conditions that fail apart. The main agent asked whether they get two Estimates, and recommended (a): `estimate-spec-write-answers-a-refusal` for the write and `estimate-spec-write-tells-each-reason-once` for the guard, each of the six Criteria pointing to the one it needs. The person chose (a).
>   - Taken: 644.1 keeps the write and its Estimate. The new 644.8 creates `estimate-spec-write-tells-each-reason-once` and takes the guard code and tests. 644.2 to 644.7 point to one or both.
> - **Change**
>   - Asked: at `/pre-spec`, 644.7 was found to lack the exception for a flag set with a transcript the hook cannot read, and `rule-spec-write` was found to keep an error sentence and a reason that disagree with 644.1 and 644.7. The main agent proposed adding the line as `estimate-ledger-write-exits-2-on-an-error` holds it, and pairs on `rule-spec-write`. The person agreed.
>   - Taken: 644.7 has the `－` line. 644.1 has pairs on the error sentence and on the reason of the payload error in `rule-spec-write`.
> - **Change**
>   - Asked: at `/pre-spec`, the Criteria of 644.2 and 644.5 were found to speak of the answer of `case-guppi`, which Case 645 turns into a summary. The main agent proposed that they speak of the text stored under Case N. The person agreed.
>   - Taken: 644.2 and 644.5 speak of the text stored under Case N and under the parent.

### Case 644.1 — The hook writes on a reply that answers a refusal

> **given:**
> `rule-spec-write`: the rule of the Spec hook. Its How it works says the hook exits 0 on the re-fire, and states its error and its reason.
> **＋** `estimate-spec-write-answers-a-refusal`: the new check of the write on a flagged reply.
> **＋** `estimate-spec-write-tells-each-reason-once`: the check of the loop guard, created by 644.8.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.
> **＋** `raw/<hi date>/<hi HHMM>/spec.md`: the approved Spec the hook writes into.
> **＋** `rule-ledger-write`, `rule-orchestration` and `rule-case-check`: the ledger hook, which already writes on a flagged reply; the agent's answer to a refusal; the `Stop` check, which skips flagged replies. Unchanged.
> **＋** `raw/2026-10-05/0311/cases/case-645.md`: Case 645, which changes another sentence of `rule-spec-write`.

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply with `stop_hook_active` set: a reply that answers a refusal of a `Stop` hook, before the person's next message.

> **then:**
> The hook writes, removes and checks Cases as on a reply without `stop_hook_active`.
> **＋** A Case N whose decision lines the reply repeats after a refusal, with the cause fixed, is written at that reply into the plan file, and into `raw/<hi date>/<hi HHMM>/spec.md` once it stands.
> **＋** A reason to refuse that reply exits 2 as without the flag, unless `estimate-spec-write-tells-each-reason-once` holds it back.
> **－** A Case refused at the reply that acknowledges it does not wait for the person's next message to be written.

```then
create:
- slug: estimate-spec-write-answers-a-refusal
  ref: rule-spec-write
  kind: QA
  purpose: Whether the Spec hook writes, removes and checks Cases on a reply with stop_hook_active set as on a reply without it, so a Case repeated after a refusal is written at once
  method: 'uv run pytest tests/test_ratified.py -k answers_a_refusal; by hand at the /hi of a later session: a Case refused at the reply that acknowledges it and written into the plan file at the reply that answers the refusal, read in the plan file and the transcript, recorded in the estimate line'
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-spec-write
  replace:
  - old: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
    new: exit 2 with the reason on stderr.
  - old: so the agent sees it at the end of that reply; a Case not yet written
    new: so the agent sees it at the end of that reply, unless the same line already stands in a refusal of its own in the stretch, and with `stop_hook_active` set and a transcript it cannot read it exits 0 and prints nothing; a Case not yet written
  - old: since the hook cannot tell a re-fire then;
    new: since the hook cannot read its refusals then;
  - old: the guard of `rule-spec-reconcile` keeps exit 0 on its own error (case 554).
    new: 'the guard of `rule-spec-reconcile` keeps exit 0 on its own error (case 554). The hook writes, removes and checks whether `stop_hook_active` is set or not: Claude Code keeps the flag set from the first refusal of any `Stop` hook until the person''s next message, so a Case whose ledger lines a reply repeats after a refusal would otherwise wait for the person to write again (case 644.1). It guards its own loop by its refusals in the stretch, the transcript after the person''s last message, read by `own_refusals` of `guppi/ledger.py`: a reason that already stands in one of them is not printed again, by `untold` of the same module; the hook exits 2 only while a reason not yet given is left, and with the flag set and a transcript it cannot read it prints nothing and exits 0 (case 644.8).'
  change: the hook writes, removes and checks whether stop_hook_active is set or not, and gives each reason once a stretch, judged by its own refusals in the transcript (cases 644.1, 644.8)
```

```tasks
- [x] create `estimate-spec-write-answers-a-refusal`
- [x] update `rule-spec-write`
- [x] `guppi/ratified.py`: `stop` no longer returns at `stop_hook_active`; the comment at the call in `main` and the module docstring say the same.
- [x] `tests/test_ratified.py`: tests `-k answers_a_refusal` — a flagged reply that repeats the lines of a refused Case writes it into the plan file and into `spec.md`; a flagged reply with a superseding line removes the old Case.
- [x] read `estimate-spec-write-answers-a-refusal`
```

### Case 644.2 — The copy of a ratified Case holds with the flag set

> **given:**
> `estimate-spec-write-copies-the-ratified-case`: its Criterion is replaced whole.
> **＋** `estimate-spec-write-answers-a-refusal` and `estimate-spec-write-tells-each-reason-once`: the write on a flagged reply and the loop guard.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.
> **＋** `guppi/casecheck.py`: the comparison of a showing with the stored text, and the reading of a sending.
> **＋** `guppi/materialize.py`: `item_keys` and `tagged_blocks`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of the Case whose sending the hook looks for.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the approved Spec, whose blocks follow the same fence rule.

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads `<plan>.checked.json` beside the plan file for the text stored under Case N, and the session's transcript for the `SendUserFile` calls on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and for the last earlier reply that shows Case N with at least one of its sections.

> **then:**
> The hook writes the text stored under Case N into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then` as the store holds them; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points; `ratification` is not written.
> **＋** A sub-case's own `recommend` is written under its heading, and the `context`, `problem` and `recommend` of its parent come from the text stored under the parent.
> **＋** Each of the two blocks opens and closes with a fence of backticks one longer than the longest run of backticks that opens a line inside it, three at the least, which `tagged_blocks` of `guppi/materialize.py` reads back whole; the same fence rule holds for the blocks it writes into `raw/<date>/<hi HHMM>/spec.md` once it stands, and for the `then` block of a short-form defer under `## Deferred`.
> **＋** No `SendUserFile` call on the file of Case N made after the time the store holds for Case N: exit 2 with the reason on stderr, and nothing of Case N is written.
> **＋** A last showing of Case N that differs from the stored text in a section it shows — by the one comparison `uv run guppi casecheck` makes on `Stop`, imported from `guppi/casecheck.py` — a store with no Case N, or a Case N stored with findings: exit 2 with the reason on stderr, and nothing of Case N is written.
> **＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
> **＋** A sub-point that reads into no key `item_keys` of `guppi/materialize.py` gives the kind and the category of its item, or a value that holds a backtick in an outer span not padded on both sides, is refused: exit 2 with `` `<key>`: not a key of <kind> <slug> `` or `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
> **＋** No plan file in the event log, or a sub-point it cannot read: exit 2 with the reason on stderr. With `stop_hook_active` set, the hook writes and refuses as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a reason it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys.
> **－** A reply with no showing of Case N is no refusal when the file of Case N was sent after the store.

```then
update:
- slug: estimate-spec-write-copies-the-ratified-case
  set:
    status: pending
  change: the Criterion replaced whole — the text stored under Case N in place of the answer of case-guppi; with stop_hook_active set the hook writes and refuses as without it, each reason once a stretch (case 644.2)
```

```tasks
- [x] update `estimate-spec-write-copies-the-ratified-case`
- [x] `tests/test_ratified.py`: `test_write_nothing_outside_a_working_session_and_nothing_on_the_re_fire` rewritten — nothing outside a working session; a flagged reply writes the Case.
- [x] read `estimate-spec-write-copies-the-ratified-case`
```

### Case 644.3 — The check after the write runs with the flag set

> **given:**
> `estimate-spec-write-checks-the-written-case`: its Criterion is replaced whole.
> **＋** `estimate-spec-write-answers-a-refusal` and `estimate-spec-write-tells-each-reason-once`: the write on a flagged reply and the loop guard.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.
> **＋** `guppi/prespec.py`: the checks of `prespec --check` the hook runs.

> **when:**
> The `Stop` hook `uv run guppi ratified` has written Case N into the plan file after a reply whose `LEDGER` block holds the decision lines of Case N.

> **then:**
> The hook runs the checks of `prespec --check` on each Case it wrote in this run and its sub-cases, with the decision lines of the reply added to those of the session's ledger, each line once.
> **＋** The `replace` and `reword` pairs of every Case of the plan are applied in entry order, and only an anchor of a Case written in this run that misses or hits more than once is a finding.
> **＋** On a finding: exit 2, the findings on stderr after `ratified:`, each naming its Case; the written Case stays in the plan file.
> **＋** A finding of a Case not written in this run is not reported.
> **＋** With `stop_hook_active` set, the hook checks as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a finding it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
> **－** A Case not written in this run, and a defer-only Case, which the hook writes under `## Deferred`, are not checked.
> **－** The Frontier is not read, and a name, `context` or `problem` that holds a Cyrillic letter is no finding.
> **－** A ledger line of the window that does not parse is no finding of this check.
> **－** The plan is compared with no other file, and no ratified copy `<plan>.ratified.md` is written.

```then
update:
- slug: estimate-spec-write-checks-the-written-case
  set:
    status: pending
  change: the Criterion replaced whole — with stop_hook_active set the hook checks as without it, each finding once a stretch (case 644.3)
```

```tasks
- [x] update `estimate-spec-write-checks-the-written-case`
- [x] `tests/test_ratified.py`: `test_checks_the_written_case_the_re_fire_checks_nothing` rewritten — a flagged reply checks the written Case.
- [x] read `estimate-spec-write-checks-the-written-case`
```

### Case 644.4 — A defer is written with the flag set

> **given:**
> `estimate-spec-write-writes-a-defer`: its Criterion is replaced whole.
> **＋** `estimate-spec-write-answers-a-refusal` and `estimate-spec-write-tells-each-reason-once`: the write on a flagged reply and the loop guard.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.
> **＋** `guppi/materialize.py`: `item_keys` and the judgment of a YAML comment.

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

> **then:**
> The hook writes that Case under `## Deferred` of the plan file while `spec.md` in the session's folder does not stand, and of that `spec.md` once it stands: the heading, `context`, `problem` and the `then` block as the reply shows them.
> **＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
> **＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr.
> **＋** A key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category: exit 2 with `` `<key>`: not a key of defer <slug> `` on stderr, and nothing of the Case is written.
> **＋** A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — as the function of `guppi/materialize.py` judges it: exit 2 with the line of the comment and the advice to quote the value on stderr, and nothing of the Case is written.
> **＋** With `stop_hook_active` set, the hook writes and refuses as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a reason it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
> **－** A `#` inside a quoted value or inside a `|` or `>` block is text, not a comment, and is no refusal.
> **－** A `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
> **－** The check after the write does not run on the Case.

```then
update:
- slug: estimate-spec-write-writes-a-defer
  set:
    status: pending
  change: the Criterion replaced whole — with stop_hook_active set the hook writes and refuses a defer as without it, each reason once a stretch (case 644.4)
```

```tasks
- [x] update `estimate-spec-write-writes-a-defer`
- [x] `tests/test_ratified.py`: a test `-k defer` — a short-form defer refused, then shown again fixed on a flagged reply, is written under `## Deferred`.
- [x] read `estimate-spec-write-writes-a-defer`
```

### Case 644.5 — The approved Spec takes a Case with the flag set

> **given:**
> `estimate-spec-write-reaches-the-approved-spec`: its Criterion is replaced whole.
> **＋** `estimate-spec-write-answers-a-refusal`: the write on a flagged reply.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.
> **＋** `raw/<hi date>/<hi HHMM>/spec.md`: the approved Spec the hook writes into.

> **when:**
> The `Stop` hook `uv run guppi ratified` has written a ratified Case N from the text stored under it into the plan file, after a reply whose `LEDGER` block holds the decision lines of Case N, and `raw/<hi date>/<hi HHMM>/spec.md` stands.

> **then:**
> The hook writes the same stored text of Case N into `spec.md`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, the block tagged `then` and the block tagged `tasks`.
> **＋** Every section of Case N that stands in `spec.md` is replaced; a Case with no section there is placed after the last section of its family, or before the `## Deferred` of the last approved document, or at the end.
> **＋** A task line whose text stood in a replaced section keeps the box it had there.
> **＋** The `context`, `problem` and `recommend` of a sub-case's parent, written into `spec.md` and into the plan file, come from the text stored under the parent, never from the reply.
> **＋** With `stop_hook_active` set, the hook writes into `spec.md` as without it, as `estimate-spec-write-answers-a-refusal` sets it.
> **－** Nothing written into `spec.md` is translated or refused for its language.
> **－** A refusal that writes nothing of Case N into the plan file writes nothing of it into `spec.md`.

```then
update:
- slug: estimate-spec-write-reaches-the-approved-spec
  set:
    status: pending
  change: the Criterion replaced whole — the text stored under Case N in place of its stored answer; with stop_hook_active set the hook writes into spec.md as without it (case 644.5)
```

```tasks
- [x] update `estimate-spec-write-reaches-the-approved-spec`
- [x] `tests/test_ratified.py`: a test `-k approved_spec` — a flagged reply writes the Case into `spec.md`.
- [x] read `estimate-spec-write-reaches-the-approved-spec`
```

### Case 644.6 — A superseded Case leaves the Spec with the flag set

> **given:**
> `estimate-spec-write-removes-a-superseded-case`: its Criterion is replaced whole.
> **＋** `estimate-spec-write-answers-a-refusal`: the write on a flagged reply.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.
> **＋** `raw/<hi date>/<hi HHMM>/spec.md`: the approved Spec the hook removes from.

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds a decision line carrying `{supersedes:case N}`, and it has written the Case of that line in the same run.

> **then:**
> The hook removes the section of Case N — its heading, its sections, its `then` and `tasks` blocks, and the sections of its sub-cases — from the plan file.
> **＋** Once `raw/<hi date>/<hi HHMM>/spec.md` stands, it removes every section of Case N and of its sub-cases from it too.
> **＋** A `{supersedes:case N.M}` removes the section of that sub-case alone; its parent and its other sub-cases stay.
> **＋** A section of Case N under `## Deferred` is removed the same way.
> **＋** With `stop_hook_active` set, the hook removes as without it, as `estimate-spec-write-answers-a-refusal` sets it.
> **－** A Case N that neither file holds — a Case of an earlier session, a defer taken up — is no refusal, and nothing is removed.
> **－** A line whose own Case the hook refused or did not write removes nothing.

```then
update:
- slug: estimate-spec-write-removes-a-superseded-case
  set:
    status: pending
  change: the Criterion replaced whole — with stop_hook_active set the hook removes a superseded Case as without it (case 644.6)
```

```tasks
- [x] update `estimate-spec-write-removes-a-superseded-case`
- [x] `tests/test_ratified.py`: a test `-k superseded` — a flagged reply removes the superseded Case.
- [x] read `estimate-spec-write-removes-a-superseded-case`
```

### Case 644.7 — An error of the hook is told once a stretch, with the flag set or not

> **given:**
> `estimate-spec-write-exits-2-on-an-error`: its Criterion and its `purpose` are set anew.
> **＋** `estimate-spec-write-tells-each-reason-once`: the loop guard.
> **＋** `estimate-ledger-write-exits-2-on-an-error`: the ledger Estimate whose exception for an unreadable transcript this one follows. Unchanged.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.

> **when:**
> The `Stop` hook `uv run guppi ratified` fires, and an exception rises in `guppi/ratified.py` after the hook has read the payload: while it reads the transcript, the store, the plan file or `spec.md`, or while it writes, removes or checks a Case.

> **then:**
> The hook exits 2. Its stderr holds `ratified: not done: <error>` and the advice to repeat the ledger lines once the cause is fixed, so the agent sees the error at the end of that reply.
> **＋** The reply that repeats the ledger lines writes a Case that the error left unwritten.
> **＋** A Case written before the error stays written, and the repeat replaces its section.
> **＋** The error line is told once a stretch, as `estimate-spec-write-tells-each-reason-once` sets it for every reason of the hook.
> **－** When `stop_hook_active` is set and the hook cannot read the transcript, so it cannot tell whether a refusal of its own stands, it exits 0 and prints nothing, so it cannot loop.
> **－** An error while the hook reads the payload exits 0 with the error on stderr. The hook cannot read its refusals at that point, and exit 2 could loop.
> **－** The guard `uv run guppi ratified --guard` keeps exit 0 with its line on stderr on its own error.
> **－** A refusal of the hook with no error keeps its own reason on stderr and its own exit.

```then
update:
- slug: estimate-spec-write-exits-2-on-an-error
  set:
    status: pending
    purpose: Whether the Spec hook exits 2 with the error on stderr when its Stop run raises after reading the payload, once a stretch for the same error, exits 0 and prints nothing with stop_hook_active set and a transcript it cannot read, and exits 0 on an error while reading the payload and in the guard
  change: the Criterion replaced whole — an error is told once a stretch, judged by the hook's own refusals in the transcript, and with stop_hook_active set and a transcript it cannot read the hook exits 0 silent; the purpose follows (case 644.7)
```

```tasks
- [x] update `estimate-spec-write-exits-2-on-an-error`
- [x] `tests/test_ratified.py`: `test_error_the_re_fire_exits_0_and_writes_nothing` rewritten — a new error on a flagged reply exits 2; the same error already in a refusal of the stretch exits 0 silent; an error with the flag set and an unreadable transcript exits 0 silent.
- [x] read `estimate-spec-write-exits-2-on-an-error`
```

### Case 644.8 — The hook gives each reason once a stretch

> **given:**
> `estimate-spec-write-tells-each-reason-once`: the new check of the loop guard.
> **＋** `rule-spec-write`: the rule of the Spec hook, whose text 644.1 changes.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.
> **＋** `guppi/ledger.py`: holds `own_refusals` and `untold`, which the hook imports.
> **＋** `rule-ledger-write`: the ledger hook, whose guard this one follows. Unchanged.

> **when:**
> The `Stop` hook `uv run guppi ratified` has a reason to refuse a reply — a refusal of a Case or an error of its own after it read the payload — with `stop_hook_active` set or not, and reads the transcript at `transcript_path`.

> **then:**
> The hook reads its own refusals in the stretch, the records of the transcript after the person's last message, by `own_refusals` of `guppi/ledger.py`.
> **＋** A reason that already stands in one of them is not printed again, by `untold` of `guppi/ledger.py`, the function that judges the lines of the ledger hook.
> **＋** The hook exits 2 when a reason not yet given is left, and prints only those reasons on stderr. When none is left, it exits 0 and prints nothing.
> **＋** With `stop_hook_active` set and a transcript it cannot read, it prints nothing and exits 0.
> **－** What the hook writes, removes or checks does not depend on whether a reason is printed.

```then
create:
- slug: estimate-spec-write-tells-each-reason-once
  ref: rule-spec-write
  kind: QA
  purpose: Whether the Spec hook gives each of its reasons, a refusal or an error, once a stretch, judged by its own refusals in the transcript, and prints nothing with stop_hook_active set and a transcript it cannot read
  method: uv run pytest tests/test_ratified.py -k tells_each_reason_once
  tags:
  - hooks
  - harness
  - workflow
```

```tasks
- [x] create `estimate-spec-write-tells-each-reason-once`
- [x] `guppi/ratified.py`: the reasons of `stop` and the error of `main` pass through `own_refusals` and `untold` of `guppi/ledger.py` with the command `uv run guppi ratified`; the module docstring says the same.
- [x] `guppi/ledger.py`: the docstring of `refusals` names `guppi ratified` among the hooks that read their own refusals through it.
- [x] `tests/test_ratified.py`: tests `-k tells_each_reason_once` — a reason already in a refusal of the stretch exits 0 silent; a new reason beside it exits 2 with only the new one; the flag set with no readable transcript exits 0 silent; a reason given before the person's last message is given again.
- [x] read `estimate-spec-write-tells-each-reason-once`
```

## Case 645 — case-guppi writes its own Case file, and the hooks check it

> **context:**
> Today `case-guppi` hands back the whole Case as text. When the agent stops, the `SubagentStop` hook `guppi casecheck --subagent` reads that text from the agent's transcript and checks it. It stores the text in `<plan>.checked.json`, and when no finding stands it writes the text into `raw/<date>/<hi HHMM>/cases/case-<N>.md`. The `Stop` comparison of a showing and the Spec hook of `rule-spec-write` read the store. The guard `guppi ratified --guard` refuses every edit under `cases/`. When the check finds a fault, the agent must write the whole Case again. Case 644 shows the cost. It had seven sub-cases and about 30,000 characters. It was sent back for faults in 644.1, 644.2, 644.5 and 644.6, and it was generated again whole, though 644.3, 644.4 and 644.7 came back the same, character for character. The whole text also enters the main agent's context at every answer.
>
> The person chose these changes:
> - `case-guppi` writes its Case into its file by Write. It fixes findings, or makes a change the person asks for, by Edit of the lines at fault.
> - The same `SubagentStop` hook checks the file when the agent stops, and copies its text into the store, which stays the source that the Spec hook and the `Stop` comparison read.
> - A file changed after its check is refused, both at the showing and at the write into the Spec. Each of these two refusals gets a new Estimate.
> - The agent hands back a short summary: the path, then each Case's id and name, the Estimate that checks it, its ledger lines, and a line `**Other Case:**` when its `context` says another Case of the session should change instead (case 629.1). The main agent shows the Case from the summary and does not read the file.
> - The guard lets a Write or Edit under `cases/` through only for `case-guppi`, and refuses that agent anywhere else. The main agent stays the orchestrator and writes no Case.
> - The check reads the whole file every time, so `stored_parents` (case 629.3) and its Estimate go.
>
> This build answers the findings of pre-spec, with the person's answers:
> - The probe. The `case-guppi` of this session cannot run it. The render of `rule-render-harness` is the librarian's step, and the client reads `.claude/agents/` only at the start of a session (`lesson-agents-read-at-session-start-in-claude-code-2-1-228`). So the new form is live from the next session. The probe of 645.3 is made in Work Mode by a subagent this session can dispatch. It measures only whether the `PreToolUse` input names the agent type. The hooks reference says it does: `agent_type` is "Present when the session uses `--agent` or the hook fires inside a subagent" (https://code.claude.com/docs/en/hooks.md, read by the main agent at pre-spec).
> - Permission in Plan Mode. The person said no allow rule is needed when a subagent runs in Plan Mode, and asked that the documentation be checked. The subagents page says that a subagent with no `permissionMode` inherits the main conversation's mode, and that in `plan` mode the subagent "runs in the permission mode you set, except `bypassPermissions`". `acceptEdits` auto-accepts file edits in the working directory (https://code.claude.com/docs/en/sub-agents.md). So 645.1 sets `permissionMode: acceptEdits` in the agent file, and the guard of 645.3 keeps the agent inside `cases/`. A Grep of `asks before every edit|asks all the same` over `vault/wiki/`, with `!**/decisions/**`, printed 4 files: `log.md`, `lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt.md`, `rule-permissions.md` and `estimate-permissions.md`. I did not read `log.md`. `rule-permissions` and `estimate-permissions` say that in Plan Mode the client asks before every edit outside the plan file, which 645.16 bounds to the main agent. The lesson stands as the record of what the main conversation does. Its claim that the allow list does not lift the prompt stays true, and the allow list gains no path.
> - The old form. `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` speaks of this Case. The check changes in Work Mode, but the new frame of `case-guppi` is live only from the next session. A Case built again in this session's Work Mode would otherwise be stored by nobody, and its showing and its Spec write would be refused. So 645.2 keeps the old path: when the subagent wrote no case file and its newest output holds a Case heading, the check reads that output, stores it and writes the file as today, until a reading of `estimate-case-build-writes-the-case` passes live. A Case of a later session removes that path. On that path, an answer of sub-cases alone is judged without its parent's `given`, since `stored_parents` goes now. Its sections are still placed in the file beside the others.
> - The sentences that 645 makes false on `rule-case-build`, `rule-spec-reconcile`, `rule-spec-write` and `rule-case-check` get replace pairs in 645.1, 645.3, 645.5 and 645.2.
> - The Criterion of `estimate-case-check-shows-only-the-checked-case` is replaced in 645.11, because its pass condition for a showing of `ratification` alone holds no comparison of the file.
> - `estimate-case-build-answers-what-done-means`, `estimate-case-build-records-the-rounds-in-recommend`, `estimate-case-check-requires-a-backlog-item-decided-on-its-page` and `estimate-case-check-sends-back-a-ratified-case-in-another-shape` speak of the answer as the Case. They are replaced in 645.12 to 645.15, their moment the Case written into its file.
> - `estimate-case-build-checks-the-finished-case` is deferred by Case 647 of this plan. Its Criterion stays for the session that takes 647 up, though 645.1 changes the render sentences on the moment before the agent answers.
>
> What the frame showed, by these searches:
> - A Grep of `writes no file|file of the Case is written|is written for the answer|writing of the file|wrote from the answer|writes it into a file|writes from the answer|writes a Case that` over `vault/wiki/`, with `!**/decisions/**`, printed 18 files. They are placed as follows:
>   - These enter the Case: `rule-case-check`, `rule-case-build`, `rule-orchestration` and its render `orchestration.md`, `estimate-case-build-writes-the-case`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, `estimate-orchestration-shows-the-built-case`, `estimate-case-protocol-case-form`, `estimate-case-check-refuses-a-letter-outside-the-script` and `estimate-case-check-notes-a-criterion-line-not-carried`.
>   - These stand: `estimate-case-check-sends-back-a-faulty-round`, `estimate-case-check-refuses-text-outside-the-list` and `estimate-case-check-refuses-text-before-a-round` say that their own check writes no file, and it still writes none. `estimate-compact-recall-reloads`, `estimate-glossary-checks-the-file`, `estimate-prespec-onward-sends-the-agent-on` and `estimate-retro-onward-sends-the-agent-to-the-handoff` speak of other hooks.
> - A Grep of `SubagentStop` over `vault/wiki/rules/` printed `rule-case-check.md`, `rule-orchestration.md`, `rule-hook-registry.md` and `rule-spec-reconcile.md`. Over `.claude/` it printed `.claude/settings.json`. The registration in `rule-hook-registry` and `.claude/settings.json` stays as it is.
> - A Grep of `write_case_files|is_case_file|stored_parents|stored_family` over the `*.py` files of the repository printed `guppi/casecheck.py`, `guppi/ratified.py` and `tests/test_casecheck.py`. `stored_parents` goes. `write_case_files` stays for the old path until the later Case. `is_case_file` stays, the one judgment of the guard and the check. `stored_family` (case 629.4) stays: when the file holds the whole family it finds nothing to add, and the line of `estimate-case-check-requires-each-question-of-the-rounds` that describes it stays true.
>
> The other Estimates of `rule-case-check` (clash, problem in a sub-case, rounds, `then` line shared by siblings) speak of the Cases the check reads. They stay true when those Cases are read from the file. Case 644 is built again now. Its 644.1 takes a pair on the error sentence of `rule-spec-write`, and the pairs of 645.5 stand on other sentences of that page. Case 646 replaces the sentences of `rule-case-protocol` that call the reply of `case-guppi` its answer. The new Estimates carry a `ref`, so the vault query of `ask-guppi` was not run. A Glob `vault/**/*changed-case-file*` printed nothing, so both slugs are free.
>
> The check sent back two kinds of notes, and both kinds stand:
> - Notes on lines of the old Criteria that the new Criteria do not carry. Each of those lines was changed on purpose, for one of these reasons:
>   - It spoke of the answer as the Case, of a file the hook writes, of the tools Read, Grep and Glob alone, or of a sub-case answered alone.
>   - In 645.11, the pass condition and the list of refusals add the comparison of the file.
>   - In 645.16, the moment adds the write of `case-guppi`, the prompt in Plan Mode is bound to the main agent, and the line on `deny` and `ask` adds that no path under `cases/` is allowed.
> - Notes on `then` lines of sibling sub-cases that share many words. They share the words of files, the store, refusals and the rounds, but each sub-case sets its own promise.
>
> Not done:
> - When a second agent builds a Case under a number another agent holds, it overwrites that Case's file before the check sends it back. The comparison of 645.4 then refuses the showing of that Case until its own agent writes the file again. No guard stops the overwrite.
> - `orchestration.md` still calls the agent's reply "the answer". The summary is that answer now.
> - The old path of 645.2 stays until a later session removes it.

> **problem:**
> The check reads the text the agent hands back and writes the file from it. So every fix after a finding means generating the whole Case again, and the whole Case enters the main agent's context at every answer. The question was where the check runs, which copy reaches the Spec, what the agent hands back, how the guard tells `case-guppi` from the main agent, how a file changed after its check is caught, and what happens to the handling of an answer of sub-cases alone.

> **recommend:**
> - **When the check reads the file the agent wrote**
>   - Recommended: (a) when the agent stops, from the file: the same stop hook finds the file by the agent's own Write and Edit calls and checks it whole; findings are fixed by Edit; rounds and Fact answers stay plain text.
>   - Answer: agreed, (a). The person added that `case-guppi` must be allowed to write into `cases/`; as the person recalls, a subagent is not asked for permission to write in Plan Mode, so this stays convenient; the main agent still writes no Case and stays the orchestrator.
> - **Which copy reaches the Spec**
>   - Recommended: (a) keep the store: the check copies the passed file into it, and the Spec hook and the `Stop` check keep reading it; the sent file must still equal the stored text at the showing and at the Spec write.
>   - Answer: agreed, (a).
> - **What the agent hands back for a built Case**
>   - Recommended: (a) a short summary: the path, then for each Case and sub-case its id and name, the Estimate that checks it with one line on what it checks, and its ledger lines; a ledger line that differs from the file is caught at the showing.
>   - Answer: agreed, (a).
> - **How the guard tells `case-guppi` from the main agent**
>   - Recommended: (a) by the agent's type in the hook input, measured first: a Write or Edit under `cases/` passes only for `case-guppi`, which is refused anywhere else; a probe that waits for the person's word comes first in Work Mode, and work stops if the field is missing.
>   - Answer: agreed, (a).
> - **How the check of a changed file is itself checked**
>   - Recommended: (a) two new Estimates, one for the `Stop` check of a showing and one for the Spec hook; the existing Criteria stand, and nothing clashes with the other Case of the session.
>   - Answer: agreed, (a).
> - **What happens to the check of a lone sub-case**
>   - Recommended: (a) the whole file is judged every time; the lone-part handling and its Estimate are deleted, and the Estimates that say the agent writes no file or hands back the whole Case are replaced.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, a probe that this session can run, and a context that says the new form is live from the next session.
>   - Taken: the probe of 645.3 is made by a subagent this session can dispatch, and measures only whether the `PreToolUse` input names the agent type; the context says the render lands at the librarian's step and is read at the next session.
> - **Change**
>   - Asked: at pre-spec, check the documentation of Claude Code; when a subagent is dispatched in Plan Mode, no allow rule is needed.
>   - Taken: `permissionMode: acceptEdits` in the agent file of `case-guppi` (645.1), no allow rule, and `rule-permissions` and `estimate-permissions` bound the prompt in Plan Mode to the main agent (645.16).
> - **Change**
>   - Asked: at pre-spec, keep the old form until the writer is live.
>   - Taken: 645.2 still reads the answer text and writes the file when the subagent wrote no case file, until a reading of `estimate-case-build-writes-the-case` passes live; a later Case removes that path.
> - **Change**
>   - Asked: at pre-spec, replace the sentences of `rule-case-build`, `rule-spec-reconcile`, `rule-spec-write` and `rule-case-check` that the Case makes false.
>   - Taken: replace pairs in 645.1, 645.3, 645.5 and 645.2, and a `set` of the `purpose` of `rule-spec-write`.
> - **Change**
>   - Asked: at pre-spec, the summary carries a line when the Case's `context` says another Case should change instead, and the showing shows it.
>   - Taken: a line `**Other Case:**` in the summary (645.1), and the main agent asks about that Case from it (645.6).
> - **Change**
>   - Asked: at pre-spec, the Not done no longer names `case-schema.md`.
>   - Taken: removed; Case 646 replaces those sentences.
> - **Change**
>   - Asked: at pre-spec, replace the Criterion of `estimate-case-check-shows-only-the-checked-case`.
>   - Taken: 645.11, its pass condition joined with the comparison of the file.
> - **Change**
>   - Asked: at pre-spec, replace the four Estimates that speak of the answer as the Case, their moment the Case written into its file, and leave `estimate-case-build-checks-the-finished-case` for the session that takes Case 647 up.
>   - Taken: 645.12 to 645.15, and the context says the deferred Estimate stays.

### Case 645.1 — case-guppi writes its Case into its file and hands back a summary

> **given:**
> `rule-case-build`: the rule whose Render is the agent file of `case-guppi`.
> **＋** `estimate-case-build-writes-the-case`: its Criterion, `purpose` and `method` are set anew.
> **＋** `estimate-case-build-checks-the-finished-case`: deferred by Case 647. Unchanged.
> **＋** `.claude/agents/case-guppi.md`: the agent file the render writes.
> **＋** `.claude/skills/grill-me/SKILL.md`: the template of a round.
> **＋** `.claude/agents/ask-guppi.md`: the vault query the agent runs before a `create` without a `ref`.
> **＋** `vault/wiki/case-schema.md` and `vault/wiki/ratification.md`: the form of a Case and of its ledger lines.
> **＋** `.claude/settings.json`: the hooks registered on the event a changed hook runs on.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `rule-case-check`: its `SubagentStop` hook checks the file.
> **＋** `rule-spec-reconcile`: its guard lets `case-guppi` write that file, as 645.3 sets it.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
> **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file, then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
> **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
> **＋** Sent findings by the hook, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; asked by a message that opens a fork, it answers with a round.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: acceptEdits`, so it writes its file with no prompt while the session is in Plan Mode.
> **－** It does not write the whole Case again to fix a finding or make a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, and no ledger line.

```then
update:
- slug: rule-case-build
  replace:
  - old: and with the Case alone when none is; the hook of `rule-case-check` checks it and writes it into a file of the session, which the main agent sends the person
    new: and, when none is, writes the Case into its file of the session by `Write` and answers with a short summary of it; the hook of `rule-case-check` checks the file, which the main agent sends the person
  - old: and the `Stop` hook compares what the chat shows of it with the answer (cases 441, 452.4)
    new: and the `Stop` hook compares what the chat shows of it, and the file, with the text the check stored (cases 441, 452.4, 645.1)
  - old: 'tools: Read, Grep, Glob'
    new: |-
      tools: Read, Grep, Glob, Write, Edit
      permissionMode: acceptEdits
  - old: and answer with a round of questions while a fork is open, or with the Case alone.
    new: and answer with a round of questions while a fork is open, or write the Case into its file and answer with a summary.
  - old: since the Spec is written from your answer; a hook writes your answer into a file that the main agent sends the person, who reads it in {{documentation_lang}}, and the person ratifies it.
    new: into its file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, since the Spec is written from the text of that file that a hook checks and stores; the main agent sends the file to the person, who reads it in {{documentation_lang}}, and the person ratifies it.
  - old: answer with the next round, or with the Case when no fork is left.
    new: answer with the next round, or, when no fork is left, write the Case into its file and answer with the summary.
  - old: Before you answer with the Case, check it whole, its sub-cases with it.
    new: Before you answer with the summary of a Case, check the Case in its file whole, its sub-cases with it.
  - old: Just before you answer with the Case, run again each search
    new: Just before you answer with the summary, run again each search
  - old: 'When no fork is open, answer with the Case in the chat form of the schema, from its heading to the fence of `ratification`, and nothing else: no line before it, no note after it. A hook checks the answer before the main agent sees it; when it sends findings back, fix the Case and answer with it again.'
    new: 'When no fork is open, write the Case in the chat form of the schema, from its heading to the fence of `ratification` and nothing else, into its file by `Write`. Claude Code may tell you in Plan Mode that you may edit only your own plan file: the file of your Case is the one file this harness lets you write, in the permission mode your agent file sets, and its guard refuses any other. Then answer with the summary alone: a first line `**Built:**` and the path of the file, then one list item per Case and sub-case — its id and name, the Estimate that checks it and one line on what that Estimate checks — and under the item its ledger lines in an untagged fence, as the file holds them. A hook checks the file when you stop, before the main agent sees your answer; when it sends findings back, fix the lines at fault by `Edit` and answer with the summary again, never by writing the whole Case again (case 645.1).'
  - old: and name in `context` the other Case and the change it needs; the main agent asks the person whether that Case is built again (case 637.2).
    new: and name in `context` the other Case and the change it needs, and again on a line `**Other Case:**` under the item of your Case in the summary; the main agent asks the person whether that Case is built again (cases 637.2, 645.1).
  - old: Asked again by a message, answer with the Case again, changed as asked, or with a round when the message opens a fork. An answer again holds the Case whole, or, where the parent's `context`, `problem` and `recommend` stand as they were, the changed sub-cases alone, each from its heading to the fence of its `ratification`, an item of `recommend` whose answer changed only that sub-case under its heading; the hook writes them into the file of the Case beside the parts that did not change (case 629.2).
    new: Asked again by a message, change the file as asked, by `Edit` of the lines that change, and answer with the summary again, or answer with a round when the message opens a fork (case 645.1).
  - old: Write no file and no ledger line.
    new: Write no file but the file of your Case, and no ledger line.
  change: case-guppi writes its Case into its file by Write in permissionMode acceptEdits, fixes it by Edit and answers with a summary that names another Case to change; its tools gain Write and Edit (case 645.1)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
    purpose: case-guppi asks about the forks of an item in rounds by the skill grill-me, then builds the Case against the vault and its frame, writes it into its file and answers with a short summary
    method: 'by hand: live dispatches in a session after the render — one item with a fork, answered by a round and then the Case written into its file and a summary, one Case with a create without a ref, one that changes a hook, a Case the hook sent back and fixed by Edit, and a change the person asked for on one sub-case, made by Edit of that sub-case, the file written in Plan Mode with no prompt; the tokens and seconds of each dispatch in the estimate line'
  change: the Criterion replaced whole — case-guppi writes its Case into its file in permissionMode acceptEdits, fixes it by Edit and answers with a summary; the purpose and the method follow (case 645.1)
```

```tasks
- [x] update `rule-case-build`
- [x] update `estimate-case-build-writes-the-case`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-writes-the-case`
```

### Case 645.2 — The check reads the file case-guppi wrote

> **given:**
> `rule-case-check`: the rule of the check of a built Case.
> **＋** `estimate-case-check-sends-back-a-faulty-case`: its Criterion and `method` are set anew.
> **＋** `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`: deleted.
> **＋** `estimate-case-check-sends-back-a-faulty-round`: the promise of the form of a round. Unchanged.
> **＋** `estimate-case-build-writes-the-case`: its live reading ends the old path.
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`: the rule of the old path. Unchanged.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/ratified.py`: the reading of the chat form the check builds the Spec section by.
> **＋** `guppi/prespec.py`: `judge`, the checks of pre-spec.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.
> **＋** `.claude/settings.json`: the `SubagentStop` registration. Unchanged.

> **when:**
> `SubagentStop` fires when `case-guppi` stops; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

> **then:**
> `uv run guppi casecheck --subagent` takes each file under the `cases/` folder of a session folder, judged by `is_case_file` of `guppi/casecheck.py`, that a `Write` or `Edit` call of the subagent in `agent_transcript_path` names, and reads its Cases as the file stands now.
> **＋** A file whose Cases `<plan>.checked.json` already holds with the same text, line ends and trailing spaces aside, and with no findings is not checked or stored again, so the time of its store stands.
> **＋** Any other such file is checked whole: each Case is read in the chat form by the functions of `guppi/ratified.py`, its section of the Spec is built in memory as the Spec hook writes it, and `judge` of `guppi/prespec.py` runs over them, the decision lines of the `ratification` fences standing for the ledger and, with the session's window, giving the categories whose schema rule the session changes.
> **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
> **＋** Each Case of the file is stored, its text as the file holds it, with its findings and the time of the store, in `<plan>.checked.json`; the hook does not write that file.
> **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` fixes the file and stops again, whatever `stop_hook_active` says.
> **＋** Until a reading of `estimate-case-build-writes-the-case` passes live, a transcript that names no such file and whose newest output holds a Case heading is read the old way: that output is checked and stored as the Cases of a file are, and with no finding the hook writes it into `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the whole file when it holds the top-level Case, the section of each sub-case otherwise. A Case of a later session removes this path.
> **－** A finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged file is not sent back twice.
> **－** An output of the subagent with no Case heading — a summary, a round or a `**Fact:**` answer — is not read as a Case; the form of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`.
> **－** A subagent of another type, and a transcript the hook cannot read, get none of these checks, and nothing is stored. A session with no plan file is not sent back for a fault of a Case.

```then
update:
- slug: rule-case-check
  replace:
  - old: the Case reaches the person in a file the hook writes from the answer that passed them (case 452.1).
    new: the Case reaches the person in the file `case-guppi` writes, which the hook checks whole when the agent stops and stores, and a file that differs from its stored text is not shown or written into the Spec (cases 452.1, 645.2).
  - old: The check of an answer compares its Cases with the other Cases of the session
    new: The check of the file of a Case compares its Cases with the other Cases of the session
  change: the check reads the file case-guppi wrote, whole, when the agent stops, and keeps the old path of the answer text until the writer is live (case 645.2)
- slug: estimate-case-check-sends-back-a-faulty-case
  set:
    status: pending
    method: uv run pytest tests/test_casecheck.py -k subagent, then by hand in a session after the render a file of case-guppi the hook sends back, fixed by Edit and passed, and a live round after a built Case, which leaves the stored entry of that Case as it stood
  change: the Criterion replaced whole — the check reads the file case-guppi wrote, whole, and keeps the old path until the writer is live; the method follows (case 645.2)
delete:
- slug: estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent
  impact: the check reads the whole file of a Case; stored_parents of guppi/casecheck.py and its tests -k lone go, and on the old path an answer of sub-cases alone is judged without the given of its parent
```

```tasks
- [x] update `rule-case-check`
- [x] update `estimate-case-check-sends-back-a-faulty-case`
- [x] delete `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`
- [x] `guppi/casecheck.py`: `subagent` takes the files of `cases/` that the Write and Edit calls of the subagent name, skips one the store holds unchanged with no findings, and checks and stores each other one whole; with no such file and a newest output that holds a Case heading, the old path as today; `stored_parents` removed; the module docstring says the same and names the old path as kept until the writer is live.
- [x] `tests/test_casecheck.py`: tests `-k subagent` over a temp transcript with Write and Edit calls and temp case files — a file with a fault sent back and stored; the file fixed by Edit passes and is stored and not written; an unchanged passed file is not stored again; a round after a built Case leaves its entry as it stood; an answer text with no case file still stored and written; the tests `-k lone` removed.
- [x] read `estimate-case-check-sends-back-a-faulty-case`
```

### Case 645.3 — The guard lets case-guppi alone write under cases/

> **given:**
> `rule-spec-reconcile`: the rule of the guard.
> **＋** `estimate-spec-reconcile-refuses-an-edit-of-the-plan`: its Criterion, `purpose` and `method` are set anew.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the guard and its tests.
> **＋** `guppi/casecheck.py`: `is_case_file`, the judgment of a file under `cases/`.
> **＋** `guppi/ledger.py`: `is_plan_file` and `plan_path`.
> **＋** `.claude/plans/`: the folder of the plan files.
> **＋** `<plan>.checked.json`: the store beside the plan file.
> **＋** `vault/raw/<date>/<HHMM>/`: a session folder, which holds `cases/`.
> **＋** `.claude/settings.json`: the `PreToolUse` registration of the guard. Unchanged.

> **when:**
> An agent calls `Edit`, `Write` or `MultiEdit` on a file, and `uv run guppi ratified --guard` on `PreToolUse` reads the path, the content and the agent type of the call from the hook input.

> **then:**
> The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
> **＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
> **＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way.
> **＋** An `Edit`, `Write` or `MultiEdit` of a file under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`, whatever its name and whether it exists or not, is let through when the hook input names `case-guppi` as the agent type, and refused the same way otherwise; the reason names the file and says that `case-guppi` alone writes it.
> **＋** An `Edit`, `Write` or `MultiEdit` whose hook input names `case-guppi` on a file outside such a `cases/` folder is refused the same way.
> **＋** A file under that folder is judged by `is_case_file` of `guppi/casecheck.py`, which the check of the file uses too; a plan file is a `.md` file under `.claude/plans/`, judged by `is_plan_file` of `guppi/ledger.py`, which `plan_path` uses too.
> **＋** A refusal writes one line of the refusal to the day's event log and no `tool` line, so `plan_path` of `guppi/ledger.py` still names the plan file.
> **－** An edit of a file outside `.claude/plans/` and outside such a `cases/` folder by any agent but `case-guppi` is not judged by this hook.
> **－** A payload the hook cannot read: exit 0 with one line on stderr.
> **－** No `PostToolUse` hook compares an edit of the plan.

```then
update:
- slug: rule-spec-reconcile
  replace:
  - old: the `Stop` hook of `rule-spec-write` writes the stored answer of `case-guppi`,
    new: the `Stop` hook of `rule-spec-write` writes the text of the file of `case-guppi` that `rule-case-check` stored,
  - old: and any edit of the file of a built Case that the person is sent, before it lands (case 453);
    new: and any edit of the file of a built Case that the person is sent, before it lands, unless `case-guppi` makes it (cases 453, 645.3);
  - old: 'and every `Edit`, `Write` and `MultiEdit` of a file under the `cases/` folder of a session folder under `vault/raw/` — the file of a built Case that the `SubagentStop` hook of `rule-case-check` writes from the stored answer, judged by one function of `guppi/casecheck.py` that its writer uses too (case 453): exit 2'
    new: 'and every `Edit`, `Write` and `MultiEdit` of a file under the `cases/` folder of a session folder under `vault/raw/` whose hook input does not name `case-guppi` as the agent type — the file of a built Case that `case-guppi` writes and the `SubagentStop` hook of `rule-case-check` checks, judged by one function of `guppi/casecheck.py` that the check uses too (cases 453, 645.3) — and every `Edit`, `Write` and `MultiEdit` that names `case-guppi` on a file outside such a folder: exit 2'
  - old: The one exception is a `Write` of a plan file that does not exist whose content, trimmed, is one line that opens with `# `
    new: The exceptions are an `Edit`, `Write` or `MultiEdit` of `case-guppi` under `cases/`, and a `Write` of a plan file that does not exist whose content, trimmed, is one line that opens with `# `
  - old: The hooks of `rule-spec-write` and `rule-case-check` write the plan, the store and the files of `cases/` with no tool call, and this hook does not judge them;
    new: The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, and the old path of `rule-case-check` writes a file of `cases/` the same way until the writer is live; this hook does not judge them;
  change: the guard lets case-guppi alone write under cases/, and refuses case-guppi anywhere else (case 645.3)
- slug: estimate-spec-reconcile-refuses-an-edit-of-the-plan
  set:
    status: pending
    purpose: An edit of the plan file or its store is refused, the one Write that creates the plan with its title line excepted, and so is an edit of a file of a built Case under cases/ by any agent but case-guppi, and any edit of case-guppi outside cases/
    method: uv run pytest tests/test_ratified.py -k guard; by hand in a later session, one probe Write of the main agent under cases/, refused and in the event log, and one file under cases/ written by case-guppi
  change: the Criterion replaced whole — case-guppi alone writes under cases/ and is refused anywhere else; the purpose and the method follow (case 645.3)
```

```tasks
- [x] stop: before the guard code, a probe: a temporary dump of the keys of the `PreToolUse` input in `guppi ratified --guard` to the scratchpad, and a subagent this session can dispatch, its type named in the result, that calls Write on a probe file in the scratchpad; the dumped keys shown to the person; with no agent type in the input, the work stops and the person decides; the dump and the probe file removed after.
- [x] update `rule-spec-reconcile`
- [x] update `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
- [x] `guppi/ratified.py`: `guard_refusal` reads the agent type of the hook input; a file under `cases/` passes for `case-guppi` alone; an edit of `case-guppi` outside `cases/` is refused; the reason and the module docstring say the same.
- [x] `tests/test_ratified.py`: tests `-k guard` — a Write and an Edit of `case-guppi` under `cases/` pass; the same calls with no agent type or another one are refused; a Write of `case-guppi` outside `cases/` is refused.
- [x] read `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
```

### Case 645.4 — The Stop check refuses a showing whose file changed after its check

> **given:**
> `estimate-case-check-refuses-a-changed-case-file`: the new check of a showing whose file differs from the store.
> **＋** `rule-case-check`: the rule of the `Stop` check of a showing.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/materialize.py`: `split_cases`, the reading of the Cases of a text.
> **＋** `guppi/ratified.py`: the Spec hook, which imports the comparison.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, and `uv run guppi casecheck` reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

> **then:**
> The hook reads the Cases of that file by `split_cases` of `guppi/materialize.py` and compares each with the entry of the store under its id alone, line ends and trailing spaces aside.
> **＋** A Case of the file whose text differs from its entry, or that the store does not hold, exits 2 with a reason that names the Case and the file, joined with the other reasons of the hook.
> **＋** The comparison is one function of `guppi/casecheck.py`, which the Spec hook `guppi/ratified.py` imports.
> **－** A heading with no section, a fence tagged `DIFF` and a deferred decision in the short form are not compared, and no file is read for them.
> **－** On the re-fire (`stop_hook_active`) it exits 0, as the other checks of the same run do.

```then
create:
- slug: estimate-case-check-refuses-a-changed-case-file
  ref: rule-case-check
  kind: QA
  purpose: Whether the Stop check refuses a showing of a Case whose file under cases/ differs from the text the store holds for it
  method: uv run pytest tests/test_casecheck.py -k changed_file
  tags:
  - hooks
  - harness
  - workflow
```

```tasks
- [x] create `estimate-case-check-refuses-a-changed-case-file`
- [x] `guppi/casecheck.py`: one function compares the Cases of a case file with the store; `stop` refuses a showing whose file differs; the module docstring says the same.
- [x] `tests/test_casecheck.py`: tests `-k changed_file` — a file equal to the store passes; a line changed after the store is refused with the Case and the file named; a Case of the file the store lacks is refused.
- [x] read `estimate-case-check-refuses-a-changed-case-file`
```

### Case 645.5 — The Spec hook writes nothing from a file changed after its check

> **given:**
> `estimate-spec-write-refuses-a-changed-case-file`: the new check of the Spec hook on a file that differs from the store.
> **＋** `rule-spec-write`: the rule of the Spec hook.
> **＋** `guppi/ratified.py` and `tests/test_ratified.py`: the hook and its tests.
> **＋** `guppi/casecheck.py`: the comparison of a case file with the store.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the approved Spec the hook writes into.
> **＋** `estimate-spec-write-answers-a-refusal`: the write on a reply with `stop_hook_active` set, created by Case 644.
> **＋** `estimate-spec-write-tells-each-reason-once`: the guard that gives each reason once a stretch, created by Case 644.
> **＋** `raw/2026-10-05/0311/cases/case-644.md`: the ratified Case that changes the same hook and other sentences of the same rule page.

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, and reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

> **then:**
> The hook compares the Cases of that file with the entries of the store under their ids, by the one function of `guppi/casecheck.py` that the `Stop` check of a showing runs.
> **＋** A Case of the file that differs from its entry, or that the store does not hold: exit 2 with the reason on stderr, and nothing of Case N is written into the plan file or into `raw/<date>/<hi HHMM>/spec.md`.
> **＋** With `stop_hook_active` set, the hook compares and refuses as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a reason it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
> **－** A defer-only Case has no file and is not compared.

```then
create:
- slug: estimate-spec-write-refuses-a-changed-case-file
  ref: rule-spec-write
  kind: QA
  purpose: Whether the Spec hook writes nothing of a ratified Case whose file under cases/ differs from the text the store holds for it
  method: uv run pytest tests/test_ratified.py -k changed_file
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-spec-write
  set:
    purpose: Prevents a ratified Case from entering the Spec in other words than the Case case-guppi wrote into its file, whose given, when, then, tasks and ratification the person signed and the check of rule-case-check stored
  replace:
  - old: Prevents a ratified Case from entering the Spec in other words than the answer of `case-guppi` whose `given`, `when`, `then`, `tasks` and `ratification` the person signed.
    new: Prevents a ratified Case from entering the Spec in other words than the Case `case-guppi` wrote into its file, whose `given`, `when`, `then`, `tasks` and `ratification` the person signed and the check of `rule-case-check` stored (case 645.5).
  - old: it reads `<plan>.checked.json` for the answer of `case-guppi` stored under Case N by `rule-case-check`,
    new: it reads `<plan>.checked.json` for the text of the file of `case-guppi` stored under Case N by `rule-case-check` (case 645.5),
  - old: no such call made after the time of the store (case 452.3),
    new: no such call made after the time of the store (case 452.3), a file of Case N whose Cases differ from the text the store holds under their ids or that the store does not hold, by the one comparison of `guppi/casecheck.py` that the `Stop` check of a showing runs (case 645.5),
  - old: a showing that differs from that answer in a section it shows
    new: a showing that differs from that stored text in a section it shows
  change: the hook copies the text of the file case-guppi wrote, as the check stored it, and writes nothing of a Case whose file differs from it; the purpose follows (case 645.5)
```

```tasks
- [x] create `estimate-spec-write-refuses-a-changed-case-file`
- [x] update `rule-spec-write`
- [x] `guppi/ratified.py`: before it writes Case N, the hook compares its case file with the store by the function of `guppi/casecheck.py`; the module docstring says the same.
- [x] `tests/test_ratified.py`: tests `-k changed_file` — a ratified Case whose file equals the store is written; a file changed after the store writes nothing and exits 2.
- [x] read `estimate-spec-write-refuses-a-changed-case-file`
```

### Case 645.6 — The main agent shows a Case from the summary

> **given:**
> `rule-orchestration`: the rule whose Render is `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file the render writes.
> **＋** `rule-case-check`: its hook checks the file and refuses a showing.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `.claude/skills/grill-me/SKILL.md`: the template of a round.
> **＋** `.claude/skills/wait-what/SKILL.md`: the skill of a plain explanation.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**` and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case with its name in Russian and, under it, one list with an item per Case and sub-case of the summary `case-guppi` answered with: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it; a reply that shows a round and that the `Stop` check refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, never to build a Case, and asks a run again only to confirm its own findings.
> **－** The main agent writes the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

```then
update:
- slug: rule-orchestration
  replace:
  - old: the file the `SubagentStop` hook of `rule-case-check` writes from the answer;
    new: the file `case-guppi` writes and the `SubagentStop` hook of `rule-case-check` checks; `case-guppi` answers with a summary of it — the path, then for each Case and sub-case its id, its name, the Estimate that checks it, its ledger lines and, when its `context` says another Case of the session should change instead, a line `**Other Case:**` — and the main agent writes the reply from the summary without reading the file (case 645.6);
  - old: a Case whose `context` says that another Case of the session, which it was bounded around after a clash, should change instead
    new: a Case whose item in the summary carries a line `**Other Case:**`, since its `context` says that another Case of the session, which it was bounded around after a clash, should change instead,
  - old: an answer with no Case heading and no first line `**Fact:**` is a round of questions
    new: an answer with no first line `**Built:**` and no first line `**Fact:**` is a round of questions
  change: the main agent shows a built Case from the summary of case-guppi, its Other Case line included, and a round is an answer with neither a Built nor a Fact first line (case 645.6)
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — the Case is shown from the summary of case-guppi, the file written by case-guppi, another Case asked about from the Other Case line, and a round known by no Built and no Fact first line (case 645.6)
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-shows-the-built-case`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] read `estimate-orchestration-shows-the-built-case`
```

### Case 645.7 — A letter outside the script holds a Case back from the showing and the Spec

> **given:**
> `estimate-case-check-refuses-a-letter-outside-the-script`: its Criterion and `purpose` are set anew.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/prespec.py`: `check_untranslated`, the language finding of pre-spec.
> **＋** `/pre-spec`: the skill whose check runs the same function.
> **＋** `guppi/config.py`: the table of languages.
> **＋** `guppi.toml`: sets `documentation_lang`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file and `guppi.toml`.

> **then:**
> A name, `context` or `problem` of a Case of the file that holds, outside a code span, a letter outside the script of the language `guppi.toml` sets as `documentation_lang`, or, inside a code span, a letter that is neither Latin nor of that script, is a finding of that Case, stored with the Case in `<plan>.checked.json`: the hook exits 2 with it on stderr, and `case-guppi` fixes the file.
> **＋** While such a finding stands, the store holds the Case with it, so the `Stop` check refuses its showing and the Spec hook writes nothing of it.
> **＋** A file whose names, contexts and problems hold no such letter gets no finding from this check.
> **＋** A Latin slug or path in a code span is no finding, whatever the documentation language.
> **＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`.
> **＋** The hook runs `check_untranslated` of `guppi/prespec.py`, the function `/pre-spec` runs, and holds no second copy of its judgment.
> **－** A file whose text `<plan>.checked.json` already holds with findings is stored again with this finding and exits 0, so an unchanged file is not sent back twice.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.

```then
update:
- slug: estimate-case-check-refuses-a-letter-outside-the-script
  set:
    status: pending
    purpose: A Case of case-guppi whose name, context or problem holds a letter outside the script of the documentation language, a Latin letter in a code span excepted, is a finding of the check, and the Case is not shown or written into the Spec while it stands
  change: the Criterion replaced whole — the check reads the file case-guppi wrote, and a finding holds the Case back from the showing and the Spec instead of keeping a file unwritten; the purpose follows (case 645.7)
```

```tasks
- [x] update `estimate-case-check-refuses-a-letter-outside-the-script`
- [x] `tests/test_casecheck.py`: tests `-k script` read a temp case file in place of an answer text.
- [x] read `estimate-case-check-refuses-a-letter-outside-the-script`
```

### Case 645.8 — A note on a Criterion line goes back on the file

> **given:**
> `estimate-case-check-notes-a-criterion-line-not-carried`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/prespec.py` and `tests/test_prespec.py`: the notes and their tests.
> **＋** `guppi/materialize.py`: `names_a_part`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `uv run guppi casecheck --subagent` checks on `SubagentStop` the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that `case-guppi` wrote, or `uv run guppi prespec --check <plan>` checks the plan, and a Case of it holds an `update` of an Estimate that names no part of the page by `names_a_part` of `guppi/materialize.py`, and so replaces its `## Criterion` whole.

> **then:**
> The old Criterion is the `## Criterion` of the Estimate page as it stands. The new one is the Criterion the item writes under `sections`, or else the `when` and `then` of the Case that holds the item.
> **＋** Each line of the old Criterion that no line of the new one equals is a note that names the Case, the Estimate and the line. The operand at the head of a line, the labels `When:`, `Then:` and `Given:`, and whitespace are set aside.
> **＋** The notes of a Case are judged by functions of `guppi/prespec.py`, and `guppi/casecheck.py` imports them, not copies.
> **＋** `uv run guppi prespec --check <plan>` prints each note as a line opening with `note:`, which sets no exit code.
> **＋** `uv run guppi casecheck --subagent` exits 2 with the notes on stderr, beside any findings, and `case-guppi` changes the file: it restores the line, or it keeps the change and says why in `context`.
> **＋** It stores the notes it sent for each Case id in `<plan>.checked.json`, apart from the findings, and a later check of the same id keeps them.
> **－** A note that the store already holds for the same Case id is not sent again, and a check whose only notes are held exits 0.
> **－** A note is not a finding: the Case is stored with no finding for it, and the `Stop` check of `guppi casecheck` does not refuse a showing for a note.
> **－** An Estimate that a Case creates has no old Criterion and gets no note.

```then
update:
- slug: estimate-case-check-notes-a-criterion-line-not-carried
  set:
    status: pending
  change: the Criterion replaced whole — the note goes back on the file case-guppi wrote, and a note writes no file since the hook writes none (case 645.8)
```

```tasks
- [x] update `estimate-case-check-notes-a-criterion-line-not-carried`
- [x] `tests/test_casecheck.py`: tests `-k note` read a temp case file in place of an answer text.
- [x] read `estimate-case-check-notes-a-criterion-line-not-carried`
```

### Case 645.9 — A number held by another agent is judged on the file

> **given:**
> `estimate-case-check-sends-back-a-case-number-held-by-another-agent`: its Criterion is replaced whole.
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape`: the count of a free number.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, `agent_id` of the payload, and `<plan>.checked.json`.

> **then:**
> The hook stores each Case of the file in `<plan>.checked.json` with the `agent_id` of the payload beside its text, its findings and the time of the store.
> **＋** A top-level Case N of the file is sent back when the store holds Case N, or a sub-case of it, under its number from an answer with another `agent_id`.
> **＋** Its message gives `case-guppi` a free number, counted as `estimate-case-check-sends-back-a-ratified-case-in-another-shape` counts it, to build the Case under, and the exit code is 2.
> **＋** Each Case of that file is stored apart, under its number joined with its `agent_id`, and the entry of the other agent under the number alone stays as it was.
> **＋** The Spec hook, the `Stop` comparison and the comparison of a case file with the store read the entry under the number alone.
> **－** An unchanged file whose text its entry apart already holds with this finding is stored again and exits 0, so it is not sent back twice.
> **－** An entry with no `agent_id`, stored before the change, gives no finding of this check, and neither does a file whose `agent_id` is the one of the entry under the number.

```then
update:
- slug: estimate-case-check-sends-back-a-case-number-held-by-another-agent
  set:
    status: pending
  change: the Criterion replaced whole — the Cases are read from the file case-guppi wrote, and no hook writes the file from the entry (case 645.9)
```

```tasks
- [x] update `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- [x] `tests/test_casecheck.py`: tests `-k subagent_clash` read a temp case file in place of an answer text.
- [x] read `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
```

### Case 645.10 — The form of a Case stands in the file case-guppi writes

> **given:**
> `estimate-case-protocol-case-form`: its Criterion is replaced whole.
> **＋** `rule-case-protocol`: the rule whose Render is `vault/wiki/case-schema.md`.
> **＋** `vault/wiki/case-schema.md`: the form of a Case.
> **＋** `rule-case-check`: its hook checks the file.
> **＋** `estimate-orchestration-shows-the-built-case`: the showing in the chat.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `make lint`: the check of the librarian's run.

> **when:**
> `case-guppi` writes a Case it built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the hook of `rule-case-check` checks it, and the main agent sends that file to the person, at its first showing or again.

> **then:**
> The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
> **＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** `tasks` holds no `by hand` box whose moment comes after Work Mode of the Case's own session — the librarian's run of that session or a later session; such a check stands as the reading of an Estimate or is left to the `make lint` of the librarian's run.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification` of `estimate-orchestration-shows-the-built-case`, and the reply ends with a plain question.
> **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
> **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.

```then
update:
- slug: estimate-case-protocol-case-form
  set:
    status: pending
  change: the Criterion replaced whole — case-guppi writes the file of the Case and the hook checks it (case 645.10)
```

```tasks
- [x] update `estimate-case-protocol-case-form`
- [x] read `estimate-case-protocol-case-form`
```

### Case 645.11 — A showing passes only when its file equals the store

> **given:**
> `estimate-case-check-shows-only-the-checked-case`: its Criterion is replaced whole.
> **＋** `estimate-case-check-refuses-a-changed-case-file`: the refusal of a showing whose file differs from the store, created in 645.4.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/ratified.py`: the Spec hook, which imports the comparison and the reading of a sending.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

> **then:**
> `uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line once line ends and trailing spaces are the same.
> **＋** Under the heading of a top-level Case, one `ratification` whose fence holds the ledger lines of its sub-cases, as the list of a showing holds them, is read as the showing of each sub-case whose id a line names: the lines that name that id are compared with the `ratification` of that sub-case in the store, and a stored line that is missing or a line the store lacks is a difference.
> **＋** A section the reply does not show is not compared: a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the stored text and `raw/<date>/<hi HHMM>/cases/case-<N>.md` equals the store, as `estimate-case-check-refuses-a-changed-case-file` sets it.
> **＋** The name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared.
> **＋** A Case the store does not hold, a Case that differs in a compared section, a Case stored with findings, a Case whose file differs from the store, or a Case with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2, the reason and the findings on stderr.
> **＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
> **＋** The Spec hook `guppi/ratified.py` judges a showing by the same comparison, and a sending by the same reading of the transcript, both imported from `guppi/casecheck.py`.
> **－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared and need no sending.
> **－** On the re-fire (`stop_hook_active`) it exits 0.

```then
update:
- slug: estimate-case-check-shows-only-the-checked-case
  set:
    status: pending
  change: the Criterion replaced whole — a showing passes only when the file of the Case equals the store too (case 645.11)
```

```tasks
- [x] update `estimate-case-check-shows-only-the-checked-case`
- [x] `tests/test_casecheck.py`: tests `-k stop` — a showing of `ratification` alone with a file changed after the store is refused.
- [x] read `estimate-case-check-shows-only-the-checked-case`
```

### Case 645.12 — Each Case written into its file names what done means

> **given:**
> `estimate-case-build-answers-what-done-means`: its Criterion is replaced whole.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `rule-case-build`: the rule of the agent.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.

> **when:**
> `case-guppi` writes a Case into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`.

> **then:**
> Each Case and sub-case of the file creates an Estimate or replaces the Criterion of one, or its `context`, or its parent's, names by slug the Estimate that already checks the change and says why its Criterion stands.
> **＋** The summary that `case-guppi` answers with names that Estimate under the item of each Case and sub-case.
> **＋** When the person's words and the frame give neither, `case-guppi` asks in a round, before it writes the Case, what the Estimate will check, and the `recommend` of the Case holds that question.
> **－** A deferred decision in the short form is not written by `case-guppi` and carries no such Estimate.

```then
update:
- slug: estimate-case-build-answers-what-done-means
  set:
    status: pending
  change: the Criterion replaced whole — the Case is written into its file, and the summary names the Estimate of each Case (case 645.12)
```

```tasks
- [x] update `estimate-case-build-answers-what-done-means`
- [x] read `estimate-case-build-answers-what-done-means`
```

### Case 645.13 — The recommend of a Case written into its file records the rounds

> **given:**
> `estimate-case-build-records-the-rounds-in-recommend`: its Criterion is replaced whole.
> **＋** `estimate-case-check-requires-each-question-of-the-rounds`: the check of each title. Unchanged.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `rule-case-build`: the rule of the agent.
> **＋** `vault/wiki/case-schema.md`: the form of a Case, rendered from `rule-case-protocol`.
> **＋** `rule-case-protocol`: the rule of the form.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.

> **when:**
> `case-guppi` writes a Case into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, with a sub-item `Recommended:` with what the agent recommended and a sub-item `Answer:` with the person's answer in English, both as they stood when the person answered that question.
> **＋** A later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer.
> **＋** A question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it.
> **＋** A question the person left unanswered is asked again in the next round under the same title; a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did.
> **＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
> **＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
> **＋** An item whose answer changed only one sub-case stands in the parent's `recommend` or in a `recommend` under that sub-case's heading; every other item stands in the parent's `recommend`.
> **＋** A Case with sub-cases carries `problem` on the parent only.
> **－** No item quotes the person's words word for word.
> **－** The promise of `estimate-case-check-requires-each-question-of-the-rounds` stands: each question title of the rounds has an item.

```then
update:
- slug: estimate-case-build-records-the-rounds-in-recommend
  set:
    status: pending
  change: the Criterion replaced whole — its moment is the Case written into its file (case 645.13)
```

```tasks
- [x] update `estimate-case-build-records-the-rounds-in-recommend`
- [x] read `estimate-case-build-records-the-rounds-in-recommend`
```

### Case 645.14 — A backlog item is judged on the file

> **given:**
> `estimate-case-check-requires-a-backlog-item-decided-on-its-page`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `guppi/prespec.py`: `decided_on_its_page`, the judgment of pre-spec.
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, and the pages of the vault.

> **then:**
> For each open line of the Frontier whose source is `backlog`, each page that its title names in a code span and that carries `deferred_by` is checked against each top-level Case N of the file that, itself or through a sub-case, names that page on a decision line other than a `defer`.
> **＋** Case N gets a finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases in the file both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and the missing mark. The hook exits 2, and `case-guppi` fixes the file.
> **＋** The judgment is the function of `guppi/prespec.py` that the pre-spec check runs, imported, not copied.
> **－** A Case of the file that names no such page, a file while no open line of the source `backlog` stands, and a page without `deferred_by` get no finding of this check.

```then
update:
- slug: estimate-case-check-requires-a-backlog-item-decided-on-its-page
  set:
    status: pending
  change: the Criterion replaced whole — the Cases are read from the file case-guppi wrote (case 645.14)
```

```tasks
- [x] update `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
- [x] `tests/test_casecheck.py`: tests `-k backlog` read a temp case file in place of an answer text.
- [x] read `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
```

### Case 645.15 — A ratified Case in another shape is judged on the file

> **given:**
> `estimate-case-check-sends-back-a-ratified-case-in-another-shape`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py`: the hook and its tests.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

> **then:**
> For a file that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
> **＋** Case N gets a finding when a number of its family that has such a line has no section in the file, or when a number that has such a line has a sub-case in the file.
> **＋** The finding names each such number and a new number: one above the highest top-level Case number that the decision lines of the session's ledger and the keys of `<plan>.checked.json` hold.
> **＋** The finding tells `case-guppi` to build the Case under the new number. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr, and `case-guppi` fixes the file or writes the Case under the new number.
> **＋** The judgment and the new number come from one function of `guppi/casecheck.py`.
> **－** An answer on the old path that holds sub-cases of Case N without Case N gets no finding of this check.
> **－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

```then
update:
- slug: estimate-case-check-sends-back-a-ratified-case-in-another-shape
  set:
    status: pending
  change: the Criterion replaced whole — the Cases are read from the file case-guppi wrote (case 645.15)
```

```tasks
- [x] update `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- [x] `tests/test_casecheck.py`: tests `-k shape` read a temp case file in place of an answer text.
- [x] read `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
```

### Case 645.16 — The prompt in Plan Mode binds the main agent, not case-guppi

> **given:**
> `rule-permissions`: the rule of the allow list of `.claude/settings.json`.
> **＋** `estimate-permissions`: its Criterion is replaced whole.
> **＋** `.claude/settings.json`: its allow list. Unchanged.
> **＋** `.claude/agents/case-guppi.md`: sets `permissionMode: acceptEdits`, as 645.1 sets it.
> **＋** `tests/test_render.py`: fixes the shape of the block.
> **＋** `rule-spec-reconcile`: its guard keeps `case-guppi` inside `cases/`.
> **＋** `vault/raw/**`: the folder of the working files of a session.
> **＋** `vault/wiki/brief.md`: the brief of the session.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, and Edit and Write for `vault/wiki/brief.md`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** `case-guppi` writes the file of its Case in the mode `permissionMode: acceptEdits` of `.claude/agents/case-guppi.md`, with no prompt in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/`.
> **＋** A prompt in Plan Mode, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed, and no path under `cases/` is on the allow list.

```then
update:
- slug: rule-permissions
  replace:
  - old: in Plan Mode the client asks before every edit outside the plan file all the same, the person approves, and whether it asked is the person's word, never the agent's, which cannot see the prompt (case 237).
    new: 'in Plan Mode the client asks before every edit of the main agent outside the plan file all the same, the person approves, and whether it asked is the person''s word, never the agent''s, which cannot see the prompt (case 237). The file of a built Case under `cases/` is not on the list: `case-guppi` writes it in the mode `permissionMode: acceptEdits` of its agent file, which Claude Code keeps for a subagent while the session is in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/` (case 645.16).'
  change: the prompt in Plan Mode binds the main agent; case-guppi writes its Case file in permissionMode acceptEdits, with no allow rule (case 645.16)
- slug: estimate-permissions
  set:
    status: pending
  change: the Criterion replaced whole — the prompt in Plan Mode binds the main agent, and case-guppi writes its Case file with no prompt and no allow rule (case 645.16)
```

```tasks
- [x] update `rule-permissions`
- [x] update `estimate-permissions`
- [x] read `estimate-permissions`
```

## Case 646 — The Case schema shows the form case-guppi writes, by an example a test checks

> **context:**
> `case-guppi` reads `vault/wiki/case-schema.md` before it writes a Case. The page describes the chat form in prose. Its one example is the `then` block of the Spec, a form `case-guppi` never writes. When the agent writes a form the scripts do not accept, the `SubagentStop` check sends the Case back. Earlier in this session the first build of Case 644 was sent back for an `old` value that held a backtick in an unpadded span, for a `new` that then had no `old` before it, and for paths in `then` that `given` did not name. The whole Case was then written again, though the page already stated both rules. Case 432 chose not to copy the limits of the scripts into the schema, because a second copy of a judgment is a defect from its first day. The person chose a way that keeps that reason: one example Case in the chat form under its own heading after `## Language`, and a test that runs the check of the `SubagentStop` hook over it and fails on any finding or note. This is the second form that `CLAUDE.md` allows under "One judgment, one implementation". The new Estimate `estimate-case-protocol-example-passes-the-check` stands on that test. The paragraph before the example lists no limit. It says that the check is the source of the limits and that the example passes it. The prose limits the page already states, and the Spec example, stay as they are. The example is the cart decision of the Spec example in the chat form. Like the Spec example, it updates `estimate-checkout-orders-the-steps` and creates `estimate-cart-renders-in-time`. It adds a `replace` pair whose values hold a backtick in padded spans, and its `context` says what the sentence around that match names, as `estimate-case-protocol-case-form` asks.
>
> The test reads the rendered `vault/wiki/case-schema.md`, and the example lands there only at the librarian's generate and render. `rule-retro` lets no red test pass to the commit, and `rule-work-mode` allows an expected red only for `make lint`, one of its steps or a hook. So, as the person chose, the test is skipped with a reason while the file holds no block tagged `case`. This follows `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`. A Case of a later session removes the skip after the reading of the new Estimate passes.
>
> The person also chose to fix, on this page alone, the sentences that call the reply of `case-guppi` its answer. A Grep of `answer` over `vault/wiki/case-schema.md` printed 10 lines. Lines 28, 68, 76, 80 and 84 speak of the reply of `case-guppi` or of a check of it, and they enter the Case as five `replace` pairs. The other five speak of the person's answer, the vault's answer, a question answered, or the moment the agent answers, and they stand. The pair on line 68 says that a file that differs from its stored text is refused, as 645.5 sets it, so the case file of 645 is named in `given`. Each behaviour these pairs describe has an Estimate that another Case of this session replaces. This Case leaves those Estimates to those Cases, so that no promise is signed in two wordings:
> - Line 80 describes the backlog check, whose Estimate is `estimate-case-check-requires-a-backlog-item-decided-on-its-page`.
> - Line 84 describes the check of a Case built again in another shape, whose Estimate is `estimate-case-check-sends-back-a-ratified-case-in-another-shape`.
> - Line 68 describes the copy into the Spec, whose Estimate is `estimate-spec-write-copies-the-ratified-case`.
>
> As the main agent reports, Case 645, now built again, replaces the first two Criteria so that their moment is the file `case-guppi` writes. 644.2 replaces the third, so that it speaks of the text stored under Case N. `estimate-spec-write-refuses-a-changed-case-file` (645.5) and `estimate-case-check-sends-back-a-faulty-case` (645.2) check the rest. Case 645 does not change `rule-case-protocol`. Its 645.10 replaces the Criterion of `estimate-case-protocol-case-form`, which speaks of the form of a file, and the example now follows it, so this Case does not touch that Estimate. `estimate-case-protocol-loaded` stands: its Criterion lists what the file holds without saying that nothing else stands there, and the new paragraph repeats no paragraph of `orchestration.md` or `ratification.md`.
>
> A Grep of `case-schema|rule-case-protocol` over `vault/wiki/**/*.md`, `.claude/**` and `guppi/**`, with `!**/decisions/**`, printed 60 files. I did not read the hits in `brief.md` or `log.md`. In each other file I read the lines around each hit. None says what the schema holds in a way that this Case makes false. The new Estimate carries a `ref`, so the vault query of `ask-guppi` was not run. A Glob `vault/**/*example*` printed only `vault/wiki/lessons/lesson-wait-what-invents-an-example.md`, so the slug is free.
>
> Not done:
> - The Insight `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stays open and is not touched. Two of its lessons are about forms the main agent writes, which `orchestration.md` sets.
> - `orchestration.md` still calls the reply of `case-guppi` the answer.
> - The test keeps its skip until a Case of a later session removes it.

> **problem:**
> The Case schema describes the chat form in prose and shows no example of it. The agent writes forms that the check sends back, even where the prose states the rule. The question was how the schema shows the form without an untested second copy of the checks, whether this Case also fixes the page's wording about the agent's answer, and what happens to the Insight.

> **recommend:**
> - **How the page describes the form**
>   - Recommended: (a) a worked example, kept true by a test: one example Case in the form `case-guppi` writes, with a sub-case, `old` and `new` pairs, a padded value with a backtick, a fenced `set`, a `create` with its fields, a `given` that names each path its `when` and `then` use, and a `ratification` fence. A test runs the stop check over it and fails on any finding, and a new Estimate stands on that test. The prose limits stay.
>   - Answer: agreed, (a).
> - **The word "answer" on the page**
>   - Recommended: (a) fix them in this Case, on `case-schema.md` alone: its sentences speak of the file `case-guppi` writes and the text the check stored, and `orchestration.md` waits for a later Case.
>   - Answer: agreed, (a).
> - **What happens to the Insight**
>   - Recommended: (b) leave the Insight open and untouched until a later Case covers the main agent's forms too.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: the pre-spec check found that a test red in Work Mode cannot pass Retro. The person chose that the test is skipped, with a reason, while `case-schema.md` holds no `case` block, runs and passes after the librarian's render, and that a later Case removes the skip.
>   - Taken: a `－` line of `then` sets the skip, and the test task and `context` follow.
> - **Change**
>   - Asked: the pre-spec check found that the example did not say what the sentence around its `replace` match names, and gave no update of `estimate-checkout-orders-the-steps` where the Spec example gives one. The person agreed to the recommended fix.
>   - Taken: the example's `context` says what that sentence names, and Case 1.1 of the example updates and reads `estimate-checkout-orders-the-steps`.
> - **Change**
>   - Asked: the pre-spec check found that the paragraph before the example restated limits of the check, one of them wrongly, with no test behind it. The person agreed that the paragraph lists no limit.
>   - Taken: the paragraph says only that the example passes the check of the `SubagentStop` hook and that the check is the source of the limits. The `then` line on a paragraph naming each limit is gone.
> - **Change**
>   - Asked: the pre-spec check found that the pairs on lines 68, 80 and 84 describe behaviours whose Estimates this Case did not name. The person agreed to name them and to leave them to the Cases that replace them.
>   - Taken: `context` names `estimate-case-check-requires-a-backlog-item-decided-on-its-page` and `estimate-case-check-sends-back-a-ratified-case-in-another-shape`, left to Case 645, and `estimate-spec-write-copies-the-ratified-case`, left to 644.2.

> **given:**
> `rule-case-protocol`: the rule whose Render is `vault/wiki/case-schema.md`.
> **＋** `vault/wiki/case-schema.md`: the form of a Case, which `case-guppi` reads before it writes one.
> **＋** `estimate-case-protocol-example-passes-the-check`: the new check of the example.
> **＋** `tests/test_case_schema.py`: the test that runs the check over the example.
> **＋** `guppi/casecheck.py`: the check of the Cases of a file, which the test imports.
> **＋** `rule-case-check`: its `SubagentStop` hook runs that check over the file of a Case.
> **＋** `rule-one-judgment-one-implementation`: one test runs the example and the check over the same input.
> **＋** `raw/2026-10-05/0311/cases/case-645.md`: the ratified Case whose file and store the new wording names.

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
> **－** While `vault/wiki/case-schema.md` holds no block tagged `case`, the test is skipped with a reason that names the file; a Case of a later session removes the skip after the reading of `estimate-case-protocol-example-passes-the-check` passes.
> **－** The Spec example and the limits that the prose of `vault/wiki/case-schema.md` already states stay as they are.

`````then
create:
- slug: estimate-case-protocol-example-passes-the-check
  ref: rule-case-protocol
  kind: QA
  purpose: Whether the example Case of case-schema.md, in the chat form case-guppi writes, passes the check the SubagentStop hook runs over the file of a Case, so the form it shows stays a form the scripts accept
  method: uv run pytest tests/test_case_schema.py, passed and not skipped
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-protocol
  replace:
  - old: a Case off this form is not written, and the hook says why (cases 159, 387.2).
    new: |-
      a Case off this form is not written, and the hook says why (cases 159, 387.2).

      ## The chat form, by example

      The Case below is written in the chat form that `case-guppi` writes into its file. A test runs over it the check that the `SubagentStop` hook of `rule-case-check` runs over that file, and fails on any finding or note, so the example passes that check as the check stands (case 646). The limits a form must keep are those of the check, not of this paragraph: copy the form of the example, and read a finding of the check as the limit it names.

      ````case
      ## Case 1 — The cart stands before payment

      > **context:**
      > Until now items went straight from the catalogue to payment, and a buyer could not review an order. The person chose a cart between the two. The pair on `entity-checkout` changes the one sentence of its Purpose that names where the buyer pays; there it names the payment step, which now follows the cart. The Criterion of `estimate-checkout-orders-the-steps` speaks of the order of the steps, so Case 1.1 replaces it. A Glob `vault/**/*cart*` printed nothing, so both new slugs are free.

      > **problem:**
      > A buyer pays for an order without seeing it whole.

      > **recommend:**
      > - **Where the cart stands**
      >   - Recommended: (a) between the catalogue and payment.
      >   - Answer: agreed, (a).

      ### Case 1.1 — The cart stands before payment

      > **given:**
      > `entity-cart`: the new page of the cart.
      > **＋** `entity-checkout`: the page of payment, which names the cart.
      > **＋** `estimate-checkout-orders-the-steps`: its Criterion is replaced whole.

      > **when:**
      > A buyer with items in `entity-cart` opens `entity-checkout`.

      > **then:**
      > The buyer sees each item of the order and its price.
      > **＋** The buyer pays only after the cart is shown.
      > **－** An empty cart does not open `entity-checkout`.

      > **tasks:**
      > - [ ] create `entity-cart`
      >   - type: `entity`
      >   - kind: `MOC`
      >   - purpose: `Lets a buyer review an order before paying`
      >   - tags: `[cart, checkout]`
      >   - sections.Purpose: `Until now items went straight from the catalogue to payment.`
      > - [ ] update `entity-checkout`
      >   - old: `` the buyer pays at `/checkout/pay` ``
      >   - new: `` the buyer reviews the cart, then pays at `/checkout/pay` ``
      >   - set:
      >     ```
      >     tags: [cart, checkout, payment]
      >     ```
      >   - change: `the cart precedes payment`
      > - [ ] update `estimate-checkout-orders-the-steps`
      >   - set: `{status: pending}`
      >   - change: `the Criterion replaced whole — the cart precedes payment`
      > - [ ] read `estimate-checkout-orders-the-steps`

      > **ratification:**
      > ```
      > - decision[case 1.1][create][entity-cart]{tags:cart,checkout}
      > - decision[case 1.1][update][entity-checkout]{ref:entity-checkout}
      > - decision[case 1.1][update][estimate-checkout-orders-the-steps]{ref:entity-checkout}
      > ```

      ### Case 1.2 — The cart renders in time

      > **given:**
      > `estimate-cart-renders-in-time`: the new check of the time the cart takes to show.
      > **＋** `entity-cart`: the page of the cart.
      > **＋** `src/cart/view.py`: the view of the cart.

      > **when:**
      > A buyer opens the cart of `src/cart/view.py` with 10, 50 or 200 items.

      > **then:**
      > The cart shows all its items within 200 ms.
      > **－** A cart of more than 200 items is not bound by this time.

      > **tasks:**
      > - [ ] create `estimate-cart-renders-in-time`
      >   - ref: `entity-cart`
      >   - kind: `QA`
      >   - purpose: `Whether the cart shows its items within 200 ms`
      >   - method: `uv run pytest tests/test_cart_view.py -k render_time`
      >   - tags: `[cart, performance]`
      > - [ ] `src/cart/view.py`: the cart reads its items in one query.
      > - [ ] read `estimate-cart-renders-in-time`

      > **ratification:**
      > ```
      > - decision[case 1.2][create][estimate-cart-renders-in-time]{ref:entity-cart}{tags:cart,performance}
      > ```
      ````
  - old: the Spec is written from the {{documentation_lang}} answer and the {{documentation_lang}} short form
    new: the Spec is written from the {{documentation_lang}} text of the Case file that the check stored and the {{documentation_lang}} short form
  - old: it copies the Case as `case-guppi` answered it — the answer the check of `rule-case-check` stored, never a showing that differs from it, which is refused (case 437)
    new: it copies the Case as `case-guppi` wrote it into its file — the text the check of `rule-case-check` stored, never a showing or a file that differs from it, which is refused (cases 437, 645.5)
  - old: passes on the person's words and shows its answer is
    new: passes on the person's words and shows the Case it built is
  - old: the check of the answer of `case-guppi` sends back a Case that names the page of an open `backlog` line when no Case among it and its sub-cases in the answer both names
    new: the check of the file `case-guppi` writes sends back a Case that names the page of an open `backlog` line when no Case among it and its sub-cases in the file both names
  - old: The check of the answer of case-guppi sends back a build
    new: The check of the file case-guppi writes sends back a build
  change: the schema shows the chat form by an example that a test runs the check over, and names the file case-guppi writes, not its answer, as what the check reads and the Spec copies (case 646)
`````

```tasks
- [x] update `rule-case-protocol`
- [x] create `estimate-case-protocol-example-passes-the-check`
- [x] `tests/test_case_schema.py`: reads the block tagged `case` from `vault/wiki/case-schema.md`, and skips with a reason that names the file while it holds none. It seeds a temporary project with the `schema.yaml` files of `vault/wiki/`, an `entity-checkout` page that holds the anchor of the example's pair, and an `estimate-checkout-orders-the-steps` page whose Criterion holds only lines that the example's `when` and `then` carry. It runs the function of `guppi/casecheck.py` that the `SubagentStop` check runs over the Cases of a file (today `check_answer`) and asserts no finding and no note, printing them when any stands. A second test makes one padded span of the example unpadded and asserts the finding.
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-protocol-example-passes-the-check`
```

## Deferred

## Case 647 — the failed reading of the case-guppi check of the finished Case put off

> **context:**
> `estimate-case-build-checks-the-finished-case` failed at the Work Mode of session 0109 (L22): the four case-guppi of that session missed 1 page made false, 4 rules and 1 lesson of the same moment, 1 clash with a Case of the prompt and 4 claims of context. The brief of 0109 asks to decide what the frame of `case-guppi` changes, or whether the Criterion asks too much of one build. Session 0311 changed how `case-guppi` writes its Case (case 645) and left this item open.

> **problem:**
> No Case of session 0311 decides whether the frame of `case-guppi` or the Criterion of this Estimate changes.

```then
defer:
  - slug: estimate-case-build-checks-the-finished-case
    type: estimate
    purpose: "Whether case-guppi checks its finished Case before it answers, counted by what ask-guppi still finds at pre-spec; failed at L22 of session 0109, put off by session 0311, which took cases 644-646"
```

## Case 648 — the early send-on of guppi onward --plan put off

> **context:**
> At the `/pre-spec` of session 0109 the hook `guppi onward --plan` said that the Cases built again on the findings were ratified, after the reply of the defer 643 and before any Case had been sent back to its `case-guppi`: it judged the loop after the findings ended while it had not started (handoff of 0109, For the next session).

> **problem:**
> No Case of session 0311 decides whether this is a bug of the hook of `rule-prespec-onward`.

```then
defer:
  - slug: rule-prespec-onward
    type: rule
    purpose: "Prevents Plan Mode from stopping where no person is needed; its hook guppi onward --plan judged the loop after the findings of /pre-spec ended before it started in session 0109, put off by session 0311"
```

## Case 649 — the failed reading of the ask-guppi searches at pre-spec put off

> **context:**
> `estimate-ask-searches-at-prespec` failed at the `/hi` of session 0109 (L9): call 16 of an ask-guppi of session 2245 ran a Grep over `vault/wiki` with the glob `!decisions/**` and printed 29 lines of Decision pages. Case 640 put `.claude/rules/search-leaves-out-decisions.md` in place and set the method of the Estimate anew; its next reading waits for a `/pre-spec` after that render.

> **problem:**
> The Estimate stands `failed`, and no Case of session 0311 takes it up before its reading again.

```then
defer:
  - slug: estimate-ask-searches-at-prespec
    type: estimate
    purpose: "Whether ask-guppi at /pre-spec greps the rules first and leaves vault/wiki/decisions/ out of every search but the two reasons its frame names; failed at L9 of session 0109, read again at a /pre-spec after the render by case 640; put off by session 0311"
```
