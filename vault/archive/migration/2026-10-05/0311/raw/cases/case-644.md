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

> **tasks:**
> - [ ] create `estimate-spec-write-answers-a-refusal`
>   - ref: `rule-spec-write`
>   - kind: `QA`
>   - purpose: `Whether the Spec hook writes, removes and checks Cases on a reply with stop_hook_active set as on a reply without it, so a Case repeated after a refusal is written at once`
>   - method: `uv run pytest tests/test_ratified.py -k answers_a_refusal; by hand at the /hi of a later session: a Case refused at the reply that acknowledges it and written into the plan file at the reply that answers the refusal, read in the plan file and the transcript, recorded in the estimate line`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-spec-write`
>   - old: `` exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0. ``
>   - new: `exit 2 with the reason on stderr.`
>   - old: `so the agent sees it at the end of that reply; a Case not yet written`
>   - new: `` so the agent sees it at the end of that reply, unless the same line already stands in a refusal of its own in the stretch, and with `stop_hook_active` set and a transcript it cannot read it exits 0 and prints nothing; a Case not yet written ``
>   - old: `since the hook cannot tell a re-fire then;`
>   - new: `since the hook cannot read its refusals then;`
>   - old: `` the guard of `rule-spec-reconcile` keeps exit 0 on its own error (case 554). ``
>   - new: `` the guard of `rule-spec-reconcile` keeps exit 0 on its own error (case 554). The hook writes, removes and checks whether `stop_hook_active` is set or not: Claude Code keeps the flag set from the first refusal of any `Stop` hook until the person's next message, so a Case whose ledger lines a reply repeats after a refusal would otherwise wait for the person to write again (case 644.1). It guards its own loop by its refusals in the stretch, the transcript after the person's last message, read by `own_refusals` of `guppi/ledger.py`: a reason that already stands in one of them is not printed again, by `untold` of the same module; the hook exits 2 only while a reason not yet given is left, and with the flag set and a transcript it cannot read it prints nothing and exits 0 (case 644.8). ``
>   - change: `the hook writes, removes and checks whether stop_hook_active is set or not, and gives each reason once a stretch, judged by its own refusals in the transcript (cases 644.1, 644.8)`
> - [ ] `guppi/ratified.py`: `stop` no longer returns at `stop_hook_active`; the comment at the call in `main` and the module docstring say the same.
> - [ ] `tests/test_ratified.py`: tests `-k answers_a_refusal` — a flagged reply that repeats the lines of a refused Case writes it into the plan file and into `spec.md`; a flagged reply with a superseding line removes the old Case.
> - [ ] read `estimate-spec-write-answers-a-refusal`

> **ratification:**
> ```
> - decision[case 644.1][create][estimate-spec-write-answers-a-refusal]{ref:rule-spec-write}{tags:hooks,harness,workflow}
> - decision[case 644.1][update][rule-spec-write]{ref:rule-spec-write}
> ```

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

> **tasks:**
> - [ ] update `estimate-spec-write-copies-the-ratified-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the text stored under Case N in place of the answer of case-guppi; with stop_hook_active set the hook writes and refuses as without it, each reason once a stretch (case 644.2)`
> - [ ] `tests/test_ratified.py`: `test_write_nothing_outside_a_working_session_and_nothing_on_the_re_fire` rewritten — nothing outside a working session; a flagged reply writes the Case.
> - [ ] read `estimate-spec-write-copies-the-ratified-case`

> **ratification:**
> ```
> - decision[case 644.2][update][estimate-spec-write-copies-the-ratified-case]{ref:rule-spec-write}
> ```

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

> **tasks:**
> - [ ] update `estimate-spec-write-checks-the-written-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — with stop_hook_active set the hook checks as without it, each finding once a stretch (case 644.3)`
> - [ ] `tests/test_ratified.py`: `test_checks_the_written_case_the_re_fire_checks_nothing` rewritten — a flagged reply checks the written Case.
> - [ ] read `estimate-spec-write-checks-the-written-case`

> **ratification:**
> ```
> - decision[case 644.3][update][estimate-spec-write-checks-the-written-case]{ref:rule-spec-write}
> ```

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

> **tasks:**
> - [ ] update `estimate-spec-write-writes-a-defer`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — with stop_hook_active set the hook writes and refuses a defer as without it, each reason once a stretch (case 644.4)`
> - [ ] `tests/test_ratified.py`: a test `-k defer` — a short-form defer refused, then shown again fixed on a flagged reply, is written under `## Deferred`.
> - [ ] read `estimate-spec-write-writes-a-defer`

> **ratification:**
> ```
> - decision[case 644.4][update][estimate-spec-write-writes-a-defer]{ref:rule-spec-write}
> ```

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

> **tasks:**
> - [ ] update `estimate-spec-write-reaches-the-approved-spec`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the text stored under Case N in place of its stored answer; with stop_hook_active set the hook writes into spec.md as without it (case 644.5)`
> - [ ] `tests/test_ratified.py`: a test `-k approved_spec` — a flagged reply writes the Case into `spec.md`.
> - [ ] read `estimate-spec-write-reaches-the-approved-spec`

> **ratification:**
> ```
> - decision[case 644.5][update][estimate-spec-write-reaches-the-approved-spec]{ref:rule-spec-write}
> ```

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

> **tasks:**
> - [ ] update `estimate-spec-write-removes-a-superseded-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — with stop_hook_active set the hook removes a superseded Case as without it (case 644.6)`
> - [ ] `tests/test_ratified.py`: a test `-k superseded` — a flagged reply removes the superseded Case.
> - [ ] read `estimate-spec-write-removes-a-superseded-case`

> **ratification:**
> ```
> - decision[case 644.6][update][estimate-spec-write-removes-a-superseded-case]{ref:rule-spec-write}
> ```

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

> **tasks:**
> - [ ] update `estimate-spec-write-exits-2-on-an-error`
>   - set:
>     ```
>     status: pending
>     purpose: 'Whether the Spec hook exits 2 with the error on stderr when its Stop run raises after reading the payload, once a stretch for the same error, exits 0 and prints nothing with stop_hook_active set and a transcript it cannot read, and exits 0 on an error while reading the payload and in the guard'
>     ```
>   - change: `the Criterion replaced whole — an error is told once a stretch, judged by the hook's own refusals in the transcript, and with stop_hook_active set and a transcript it cannot read the hook exits 0 silent; the purpose follows (case 644.7)`
> - [ ] `tests/test_ratified.py`: `test_error_the_re_fire_exits_0_and_writes_nothing` rewritten — a new error on a flagged reply exits 2; the same error already in a refusal of the stretch exits 0 silent; an error with the flag set and an unreadable transcript exits 0 silent.
> - [ ] read `estimate-spec-write-exits-2-on-an-error`

> **ratification:**
> ```
> - decision[case 644.7][update][estimate-spec-write-exits-2-on-an-error]{ref:rule-spec-write}
> ```

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

> **tasks:**
> - [ ] create `estimate-spec-write-tells-each-reason-once`
>   - ref: `rule-spec-write`
>   - kind: `QA`
>   - purpose: `Whether the Spec hook gives each of its reasons, a refusal or an error, once a stretch, judged by its own refusals in the transcript, and prints nothing with stop_hook_active set and a transcript it cannot read`
>   - method: `uv run pytest tests/test_ratified.py -k tells_each_reason_once`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/ratified.py`: the reasons of `stop` and the error of `main` pass through `own_refusals` and `untold` of `guppi/ledger.py` with the command `uv run guppi ratified`; the module docstring says the same.
> - [ ] `guppi/ledger.py`: the docstring of `refusals` names `guppi ratified` among the hooks that read their own refusals through it.
> - [ ] `tests/test_ratified.py`: tests `-k tells_each_reason_once` — a reason already in a refusal of the stretch exits 0 silent; a new reason beside it exits 2 with only the new one; the flag set with no readable transcript exits 0 silent; a reason given before the person's last message is given again.
> - [ ] read `estimate-spec-write-tells-each-reason-once`

> **ratification:**
> ```
> - decision[case 644.8][create][estimate-spec-write-tells-each-reason-once]{ref:rule-spec-write}{tags:hooks,harness,workflow}
> ```
