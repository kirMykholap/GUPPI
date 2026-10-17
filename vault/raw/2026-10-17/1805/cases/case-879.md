## Case 879 — A built Case made only of put-offs reaches the Spec from its file

> **context:**
> When the person ratifies a Case, the `Stop` hook of `rule-spec-write` copies it into the Spec. A Case built by `case-guppi` is copied from the text the check of `rule-case-check` stored for its file. A short put-off, which the main agent writes itself, is copied from the reply that shows it: `context`, `problem` and a fence tagged `then` with its `defer` items. Today the hook picks the path by the kinds of the lines alone: `ratified_cases` of `.guppi/guppi/ratified.py` leaves out each Case whose lines in the reply are all `defer`, and `defer_only` sends it to `deferred_section`, which wants the fence tagged `then` in the reply. A Case that `case-guppi` built in full with only `defer` lines holds its items as task lines in its file, and the check of the file refuses a fence there. In session 0027 Case 876 was such a Case: the hook refused its acknowledging reply with "no fence tagged then with its defer items", and the main agent showed it again in the short form, so the Spec of that session holds it without `recommend`, `given`, `when` and `then`, in words that differ from its file (`lesson-ratified-defer-only-case-wants-its-fence-in-the-reply`, handoff of session 0027). The rule that governs the choice is the Purpose of `rule-spec-write`, that a ratified Case enters the Spec in the words `case-guppi` wrote into its file.
>
> The person chose: the Spec hook changes, not the check of the file; the hook tells the two kinds by what the reply shows, by `is_short_form` of `.guppi/guppi/casecheck.py`, read whole, which is true when the lines hold no `given` and no `when` and a fence tagged `then` opens with `defer:`. `shows_sections` of the same module, read whole, already leaves out a showing that `is_short_form` takes for the short form, and its docstring names it the one judgment of the `Stop` check of a showing and of the showing the Spec hook reads, so after the change both hooks judge the short form by one function, imported, and no second copy is written. A reply that shows a built Case, and the acknowledging reply that shows only its heading, are not the short form, so such a Case takes the path of every built Case: `against_store`, `sent`, `changed_file` of `.guppi/guppi/casecheck.py`, then `write_case`, whose `read_tasks` already builds `defer` items from task lines, as for Case 875 of session 0027, whose `defer` line stood beside an `update`. A reply with lines that are all `defer`, no short form and no store entry gets the refusal `against_store` gives, "not built and checked by case-guppi — dispatch it". The store was not chosen as the test, since it keeps the entry of a Case that `case-guppi` dropped — `other_blocks` of `.guppi/guppi/casecheck.py` leaves such an entry out by `dropped`, whose file holds only blank space — so a short put-off written after a drop would take the full path. The ledger hook does not part: `off_store` of `.guppi/guppi/ledger.py` leaves every `defer` line out of its comparison with the store.
>
> The person chose a new Estimate, `estimate-spec-write-copies-a-built-defer-only-case`; a Glob `vault/**/estimate-spec-write-copies-a-built-*.md` printed nothing, so the slug is free. Three Criteria of `rule-spec-write` speak of every Case of put-offs as the short form and are replaced whole by the person's choice, one line each: `estimate-spec-write-writes-a-defer` (879.2), whose refusal of a reply with no showing goes, since such a reply now takes the full path; `estimate-spec-write-refuses-a-changed-case-file` (879.3), whose "A defer-only Case has no file"; and `estimate-spec-write-checks-the-written-case` (879.4), whose "a defer-only Case ... are not checked". Their `purpose` and `method` do not state the old promise and stand. Each replaced Criterion keeps every other line word for word, so the check of the file notes the lines it leaves, which are the one line each changes, and the trigger it widens or narrows. It also notes the lines the sub-cases share, such as the lines on `stop_hook_active` and on a refusal with exit 2; they stand, since each is a line of its own Estimate today and says the same of a different path of the hook. `estimate-spec-write-copies-the-ratified-case` stands: its trigger, lines of a kind other than `defer`, stays true, and the new Estimate covers the rest. A Grep `defer-only` over `vault/wiki/` outside `decisions/`, `log.md` and `brief.md` printed `orchestration.md`, `rule-orchestration.md`, `rule-prespec.md`, `rule-spec-capture.md`, `rule-spec-write.md`, `estimate-materialize-assembles.md`, `estimate-orchestration-defer-example-passes-the-hook.md`, `estimate-prespec-checks-the-frame.md`, `estimate-spec-write-copies-the-ratified-case.md`, `estimate-spec-write-checks-the-written-case.md` and `estimate-spec-write-refuses-a-changed-case-file.md`. The hits in `rule-prespec.md`, `estimate-materialize-assembles.md` and `estimate-spec-write-copies-the-ratified-case.md` are History lines. The hit in `estimate-prespec-checks-the-frame.md` speaks of a Case without `given`, which stays true. The hits in `orchestration.md`, `rule-orchestration.md` and `estimate-orchestration-defer-example-passes-the-hook.md` speak of the short-form example, which takes the short path, and `.guppi/tests/test_orchestration.py` calls `write_defers` with that reply, so it stays green under the Criterion that Case 878.11 sets. `rule-spec-write.md` and `rule-spec-capture.md` change here. A Grep `defer` over `vault/wiki/estimates/estimate-{spec-capture,case-check,ledger-write}*.md` printed nothing for `rule-spec-capture`, and 13 files: `estimate-ledger-write-refuses-a-defer-of-a-record.md`, `estimate-ledger-write-holds-a-decision-line-off-the-stored-case.md`, `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line.md`, `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session.md`, `estimate-case-check-shows-only-the-checked-case.md`, `estimate-case-check-sends-back-a-ratified-case-without-a-target.md`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape.md`, `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line.md`, `estimate-case-check-sends-back-a-faulty-case.md`, `estimate-case-check-refuses-text-outside-the-list.md`, `estimate-case-check-requires-a-backlog-item-decided-on-its-page.md`, `estimate-case-check-refuses-a-changed-case-file.md` and `estimate-case-check-notes-a-page-the-cascade-archives.md`. None of them is made false: the hits on the case check speak of a showing in the short form, of `defer` lines in the ledger or in a Result or History, and the hits on the ledger hook speak of the ledger lines, which this Case does not change. A Grep `rule-spec-write\.md|rule-spec-capture\.md` over `.guppi/tests/` printed `test_spec.py`, whose hit is its docstring, so no test reads either page live. Left not done: the Spec of session 0027 keeps Case 876 in the short form, and the lesson stays as it stands, since its fix is ratified in another session.

> **problem:**
> The Spec hook reads every Case whose lines are all put-offs as the short form, so a Case that `case-guppi` built in full with only put-offs is refused, or reaches the Spec only in the main agent's words.

> **recommend:**
> - **Which side changes so that a full Case made only of put-offs reaches the Spec?**
>   - Recommended: (a) the Spec hook changes.
>   - Answer: agreed, (a).
> - **How does the hook tell a full Case made only of put-offs from a short put-off?**
>   - Recommended: (a) by what the reply shows.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) a new Estimate for the full Case made only of put-offs, and the Criterion of `estimate-spec-write-writes-a-defer` replaced.
>   - Answer: agreed, (a).
> - **What happens to the two other checks that say a Case made only of put-offs has no file?**
>   - Recommended: (a) replace both Criteria too.
>   - Answer: agreed, (a).

### Case 879.1 — A built Case made only of put-offs is copied from its file

> **given:**
> `estimate-spec-write-copies-a-built-defer-only-case`: the new check of the path of such a Case.
> **＋** `rule-spec-write`: the rule of the `Stop` hook that writes the Spec.
> **＋** `rule-spec-capture`: the rule of the Spec file, which names the writers of the file.
> **＋** `.guppi/guppi/ratified.py`: the hook, `uv run --project .guppi guppi ratified`.
> **＋** `.guppi/guppi/casecheck.py`: the store, the reading of a sending and `is_short_form`.
> **＋** `.guppi/tests/test_ratified.py`: the tests of the hook.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ratified` of `.guppi/guppi/ratified.py` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer`, and the same reply does not show Case N in the short form, by `is_short_form` of `.guppi/guppi/casecheck.py`: no `given`, no `when`, and a fence tagged `then` with `defer` items.

> **then:**
> The hook takes Case N for a Case built by `case-guppi`: it reads the text stored for Case N and the sending of the file of Case N, as for a Case with lines of another kind.
> **＋** It writes the stored text into the plan file, and into the approved Spec of the session once it stands, in the place of a ratified Case and not under `## Deferred`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, a block tagged `then` whose `defer` items it builds from the sub-points of `tasks`, and a block tagged `tasks`.
> **＋** A store with no Case N: exit 2 with `case N: not built and checked by case-guppi — dispatch it` on stderr, and nothing of Case N is written.
> **＋** A decision line of Case N that carries `{supersedes:case M}` removes Case M from the plan file and the approved Spec, as for any Case written in the run.
> **－** A reply that shows Case N in the short form makes the hook write Case N under `## Deferred` from that reply, and the hook reads no stored text for it.

> **tasks:**
> - [ ] create `estimate-spec-write-copies-a-built-defer-only-case`
>   - ref: `rule-spec-write`
>   - kind: `QA`
>   - purpose: `Whether the Spec hook copies a Case that case-guppi built with only defer lines from its stored file, and keeps the short path for a Case the reply shows in the short form`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ratified.py -k built_defer`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-spec-write`
>   - old: `` After a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, it reads ``
>   - new: `` After a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, or lines that are all `defer` of a Case N that the same reply does not show in the short form, it reads ``
>   - old: `` A defer-only Case — a Case whose lines in the reply are all `defer`, beside other Cases or alone — is written by the same hook from the reply that carries its lines and shows it in the short form ``
>   - new: `` A short put-off — a Case whose lines in the reply are all `defer`, beside other Cases or alone, and that the reply which carries its lines shows in the short form, with no `given` and no `when`, by `is_short_form` of `.guppi/guppi/casecheck.py` — is written by the same hook from that reply ``
>   - change: `a Case built by case-guppi with only defer lines is copied from its stored file; only a Case the reply shows in the short form goes under ## Deferred`
> - [ ] update `rule-spec-capture`
>   - old: `` and writes a defer-only Case under `## Deferred` ``
>   - new: `` and writes a Case the reply shows in the short form under `## Deferred` ``
>   - change: `the Spec hook writes under ## Deferred only a Case the reply shows in the short form`
> - [ ] `.guppi/guppi/ratified.py`: `defer_only(records, reply)` returns the Cases whose lines are all `defer` and whose lines in the reply, by `split_cases`, pass `is_short_form` of `.guppi/guppi/casecheck.py`, imported inside the function since that module imports this one; `ratified_cases(records, reply)` leaves out only those Cases; `stop` and `write_defers` pass the reply; the module docstring, under the write and under the defer, says so.
> - [ ] `.guppi/tests/test_ratified.py`: tests whose names hold `built_defer`, set up as the tests of a built Case set up its store and its sending: a built Case whose lines are all `defer`, stored and its file sent, after its acknowledging reply stands in the plan outside `## Deferred` with `given`, `when`, `then` and a block tagged `then` of its `defer` items; with no store entry the reply exits 2 with `not built and checked by case-guppi`; its `{supersedes:case M}` removes Case M; a short form shown in the same reply as a built Case of put-offs still goes under `## Deferred`. `test_write_a_defer_not_shown_or_without_its_item_is_refused` asserts for the bare reply the refusal `case 8: not built and checked by case-guppi — dispatch it`.
> - [ ] read `estimate-spec-write-copies-a-built-defer-only-case`

> **ratification:**
> ```
> - decision[case 879.1][create][estimate-spec-write-copies-a-built-defer-only-case]{ref:rule-spec-write}{tags:hooks,harness,workflow}
> - decision[case 879.1][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 879.1][update][rule-spec-capture]{ref:rule-spec-capture}
> ```

### Case 879.2 — A short put-off is the one the reply shows

> **given:**
> `estimate-spec-write-writes-a-defer`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/ratified.py`: the hook, `uv run --project .guppi guppi ratified`.
> **＋** `.guppi/guppi/casecheck.py`: `is_short_form`, the one judgment of the short form.
> **＋** `.guppi/guppi/materialize.py`: `defers_a_record`, `item_keys` and the reading of a YAML comment.
> **＋** `estimate-spec-write-answers-a-refusal`: the hook on a reply with `stop_hook_active` set.
> **＋** `estimate-spec-write-tells-each-reason-once`: each reason once a stretch.
> **＋** `.guppi/tests/test_ratified.py`: the tests of the hook.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form, by `is_short_form` of `.guppi/guppi/casecheck.py`: `context`, `problem` and a fence tagged `then` with its `defer` items, no `given` and no `when`.

> **then:**
> The hook writes that Case under `## Deferred` of the plan file while `spec.md` in the session's folder does not stand, and of that `spec.md` once it stands: the heading, `context`, `problem` and the `then` block as the reply shows them.
> **＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
> **＋** A `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr.
> **＋** A `defer` line of Case N whose slug names a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, whether its page stands or not: exit 2 with `case N: defer <slug>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it` on stderr, and nothing of the Case is written.
> **＋** A key of a `defer` item that `item_keys` of `.guppi/guppi/materialize.py` does not give a `defer` of its category: exit 2 with `` `<key>`: not a key of defer <slug> `` on stderr, and nothing of the Case is written.
> **＋** A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — as the function of `.guppi/guppi/materialize.py` judges it: exit 2 with the line of the comment and the advice to quote the value on stderr, and nothing of the Case is written.
> **＋** With `stop_hook_active` set, the hook writes and refuses as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a reason it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
> **－** A `defer` line of a rule, an entity, an Insight or an Estimate is not refused by `defers_a_record`.
> **－** A `#` inside a quoted value or inside a `|` or `>` block is text, not a comment, and is no refusal.
> **－** A `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
> **－** The check after the write does not run on the Case.

> **tasks:**
> - [ ] update `estimate-spec-write-writes-a-defer`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the short form judged by is_short_form; a reply with no short form is no short put-off`
> - [ ] read `estimate-spec-write-writes-a-defer`

> **ratification:**
> ```
> - decision[case 879.2][update][estimate-spec-write-writes-a-defer]{ref:rule-spec-write}
> ```

### Case 879.3 — A built Case made only of put-offs is compared with its file

> **given:**
> `estimate-spec-write-refuses-a-changed-case-file`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/ratified.py`: the hook, `uv run --project .guppi guppi ratified`.
> **＋** `.guppi/guppi/casecheck.py`: `changed_file` and `is_short_form`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.
> **＋** `<plan>.checked.json`: the store of the texts the check stored.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the approved Spec of the session.
> **＋** `estimate-spec-write-answers-a-refusal`: the hook on a reply with `stop_hook_active` set.
> **＋** `estimate-spec-write-tells-each-reason-once`: each reason once a stretch.
> **＋** `.guppi/tests/test_ratified.py`: the tests of the hook.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, or lines of Case N that are all `defer` while the same reply does not show Case N in the short form by `is_short_form` of `.guppi/guppi/casecheck.py`, and reads `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and `<plan>.checked.json`.

> **then:**
> The hook compares the Cases of that file with the entries of the store under their ids, by the one function of `.guppi/guppi/casecheck.py` that the `Stop` check of a showing runs.
> **＋** A Case of the file that differs from its entry, or that the store does not hold: exit 2 with the reason on stderr, and nothing of Case N is written into the plan file or into `raw/<date>/<hi HHMM>/spec.md`.
> **＋** With `stop_hook_active` set, the hook compares and refuses as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a reason it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
> **－** A Case whose lines are all `defer` and that the same reply shows in the short form has no file and is not compared.

> **tasks:**
> - [ ] update `estimate-spec-write-refuses-a-changed-case-file`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a built Case with only defer lines is compared with its file; only a Case shown in the short form is not`
> - [ ] `.guppi/tests/test_ratified.py`: a test whose name holds `changed_file` and `built_defer`: a built Case whose lines are all `defer`, its file changed after the store, exits 2 at its acknowledging reply and stands neither in the plan nor under `## Deferred`.
> - [ ] read `estimate-spec-write-refuses-a-changed-case-file`

> **ratification:**
> ```
> - decision[case 879.3][update][estimate-spec-write-refuses-a-changed-case-file]{ref:rule-spec-write}
> ```

### Case 879.4 — A built Case made only of put-offs is checked after the write

> **given:**
> `estimate-spec-write-checks-the-written-case`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/ratified.py`: the hook, `uv run --project .guppi guppi ratified`.
> **＋** `.guppi/guppi/prespec.py`: the checks of `prespec --check`.
> **＋** `<plan>.ratified.md`: the ratified copy, which is not written.
> **＋** `estimate-spec-write-answers-a-refusal`: the hook on a reply with `stop_hook_active` set.
> **＋** `estimate-spec-write-tells-each-reason-once`: each reason once a stretch.
> **＋** `.guppi/tests/test_ratified.py`: the tests of the hook.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ratified` has written Case N into the plan file after a reply whose `LEDGER` block holds the decision lines of Case N.

> **then:**
> The hook runs the checks of `prespec --check` on each Case it wrote in this run and its sub-cases, with the decision lines of the reply added to those of the session's ledger, each line once.
> **＋** The `replace` and `reword` pairs of every Case of the plan are applied in entry order, and only an anchor of a Case written in this run that misses or hits more than once is a finding.
> **＋** On a finding: exit 2, the findings on stderr after `ratified:`, each naming its Case; the written Case stays in the plan file.
> **＋** A finding of a Case not written in this run is not reported.
> **＋** With `stop_hook_active` set, the hook checks as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a finding it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
> **－** A Case not written in this run, and a Case whose lines are all `defer` and that the reply shows in the short form, which the hook writes under `## Deferred`, are not checked.
> **－** The Frontier is not read, and a name, `context` or `problem` that holds a Cyrillic letter is no finding.
> **－** A ledger line of the window that does not parse is no finding of this check.
> **－** The plan is compared with no other file, and no ratified copy `<plan>.ratified.md` is written.

> **tasks:**
> - [ ] update `estimate-spec-write-checks-the-written-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a built Case with only defer lines is checked after the write; only a Case shown in the short form is not`
> - [ ] `.guppi/tests/test_ratified.py`: a test whose name holds `checks_the_written` and `built_defer`: a built Case whose lines are all `defer`, written at its acknowledging reply, goes through the checks after the write, and a finding on it exits 2 with the finding naming its Case.
> - [ ] read `estimate-spec-write-checks-the-written-case`

> **ratification:**
> ```
> - decision[case 879.4][update][estimate-spec-write-checks-the-written-case]{ref:rule-spec-write}
> ```
