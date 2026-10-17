<!-- approved 20:46:03 · session 164ba6d1 -->

# Session 1805 — the sprint plugin: the Criterion sentences of shipped Estimates true only in the repository of GUPPI

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

```then
create:
- slug: estimate-spec-write-copies-a-built-defer-only-case
  ref: rule-spec-write
  kind: QA
  purpose: Whether the Spec hook copies a Case that case-guppi built with only defer lines from its stored file, and keeps the short path for a Case the reply shows in the short form
  method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k built_defer
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-spec-write
  replace:
  - old: After a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, it reads
    new: After a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, or lines that are all `defer` of a Case N that the same reply does not show in the short form, it reads
  - old: A defer-only Case — a Case whose lines in the reply are all `defer`, beside other Cases or alone — is written by the same hook from the reply that carries its lines and shows it in the short form
    new: A short put-off — a Case whose lines in the reply are all `defer`, beside other Cases or alone, and that the reply which carries its lines shows in the short form, with no `given` and no `when`, by `is_short_form` of `.guppi/guppi/casecheck.py` — is written by the same hook from that reply
  change: 'a Case built by case-guppi with only defer lines is copied from its stored file; only a Case the reply shows in the short form goes under ## Deferred'
- slug: rule-spec-capture
  replace:
  - old: and writes a defer-only Case under `## Deferred`
    new: and writes a Case the reply shows in the short form under `## Deferred`
  change: 'the Spec hook writes under ## Deferred only a Case the reply shows in the short form'
```

```tasks
- [ ] create `estimate-spec-write-copies-a-built-defer-only-case`
- [ ] update `rule-spec-write`
- [ ] update `rule-spec-capture`
- [x] `.guppi/guppi/ratified.py`: `defer_only(records, reply)` returns the Cases whose lines are all `defer` and whose lines in the reply, by `split_cases`, pass `is_short_form` of `.guppi/guppi/casecheck.py`, imported inside the function since that module imports this one; `ratified_cases(records, reply)` leaves out only those Cases; `stop` and `write_defers` pass the reply; the module docstring, under the write and under the defer, says so.
- [x] `.guppi/tests/test_ratified.py`: tests whose names hold `built_defer`, set up as the tests of a built Case set up its store and its sending: a built Case whose lines are all `defer`, stored and its file sent, after its acknowledging reply stands in the plan outside `## Deferred` with `given`, `when`, `then` and a block tagged `then` of its `defer` items; with no store entry the reply exits 2 with `not built and checked by case-guppi`; its `{supersedes:case M}` removes Case M; a short form shown in the same reply as a built Case of put-offs still goes under `## Deferred`. `test_write_a_defer_not_shown_or_without_its_item_is_refused` asserts for the bare reply the refusal `case 8: not built and checked by case-guppi — dispatch it`.
- [ ] read `estimate-spec-write-copies-a-built-defer-only-case`
```

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

```then
update:
- slug: estimate-spec-write-writes-a-defer
  set:
    status: pending
  change: the Criterion replaced whole — the short form judged by is_short_form; a reply with no short form is no short put-off
```

```tasks
- [ ] update `estimate-spec-write-writes-a-defer`
- [ ] read `estimate-spec-write-writes-a-defer`
```

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

```then
update:
- slug: estimate-spec-write-refuses-a-changed-case-file
  set:
    status: pending
  change: the Criterion replaced whole — a built Case with only defer lines is compared with its file; only a Case shown in the short form is not
```

```tasks
- [ ] update `estimate-spec-write-refuses-a-changed-case-file`
- [x] `.guppi/tests/test_ratified.py`: a test whose name holds `changed_file` and `built_defer`: a built Case whose lines are all `defer`, its file changed after the store, exits 2 at its acknowledging reply and stands neither in the plan nor under `## Deferred`.
- [ ] read `estimate-spec-write-refuses-a-changed-case-file`
```

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

```then
update:
- slug: estimate-spec-write-checks-the-written-case
  set:
    status: pending
  change: the Criterion replaced whole — a built Case with only defer lines is checked after the write; only a Case shown in the short form is not
```

```tasks
- [ ] update `estimate-spec-write-checks-the-written-case`
- [x] `.guppi/tests/test_ratified.py`: a test whose name holds `checks_the_written` and `built_defer`: a built Case whose lines are all `defer`, written at its acknowledging reply, goes through the checks after the write, and a finding on it exits 2 with the finding naming its Case.
- [ ] read `estimate-spec-write-checks-the-written-case`
```

## Case 880 — The Criteria of shipped Estimates hold in any project

> **context:**
> Case 880 builds Case 878 again after the findings of `/pre-spec`, without its sub-case 878.10 on `estimate-orchestration-asks-in-the-grill-me-shape`, whose reading this session cannot take; its decision lines retire Case 878 and each of its sub-cases, and the file of Case 878 stays as it was ratified. `guppi ship` copies each `passed` Estimate of a shipped rule into the clean version of GUPPI, its `## Criterion` with it, by `ships` of `.guppi/guppi/ship.py`. The reading of `estimate-clean-branch-ships-neutral-texts` at the `/hi` of session 1805 listed the Estimates whose Criterion holds a sentence true only in the repository of GUPPI: a description of GUPPI in `CLAUDE.md`, a past Insight, a bare case number, the `Makefile`, the GitHub address of GUPPI, its sprints `migration` and `plugin`, skills that do not ship, the word Russian. Case 875 put that rewrite off on `rule-clean-branch`, since a Criterion changes only whole, a replaced Criterion sets its Estimate `pending`, and at the librarian's run `cascade` of `.guppi/guppi/generate.py` sets a rule with an Estimate not `passed` to `draft`; a `draft` rule with `core: true` stops a build of `prod`, by `is_draft_core` of `.guppi/guppi/pages.py`, and a `pending` Estimate leaves the clean version until it passes. This Case takes the listed Estimates whose reading this session can take, so a reading that passes at Retro keeps its rule `built`. Each sub-case replaces one Criterion whole; the purpose and the method of an Estimate are set anew where they state the old promise (`estimate-guppi-package-runs-from-its-own-folder`, `estimate-git-context-current`, `estimate-ratification-case-id-carries-the-sprint`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-orchestration-defer-example-passes-the-hook`). Case 879 of this session, ratified, names the path of the Spec hook for a Case of `defer` lines that the reply shows in the short form a short put-off, by `is_short_form` of `.guppi/guppi/casecheck.py`; 880.10 takes that term for the example in `orchestration.md`, which takes that path. A pointer to a case stands in a bracket of its own at the end of its sentence and stays, as `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets` sets it for a shipped Estimate (880.4, 880.5, 880.12, 880.13, 880.15); a Criterion line dropped whole takes its pointer with it, such as the line of 880.10 on an Insight, and that Estimate stands, since such a line holds nothing true in a new project. 880.19 leaves room in its closing line for the stops of a skill the project holds, so the stops that 880.20 sets for `/pr-review` and `/merge-main` in the repository of GUPPI do not contradict it. A fact true in GUPPI on purpose moves into a new Estimate on `entity-guppi-repository`, which carries no `core: true`, so `ships` never copies it: the GitHub address (880.7), the development layout around `.guppi/` (880.9) and the stops in the merge tasks of `/pr-review` and `/merge-main`, two skills whose rules carry no `core: true` (880.20). History goes into a bracket with the word case, which `guppi ship` removes; a fact is said by its role; a pointer to a page the clean version does not hold is dropped. Left out, by the person's choices: six Estimates whose only such sentence points to an Estimate still `pending` that will ship once it passes (`estimate-case-build-checks-the-finished-case`, `estimate-case-build-reads-by-need-and-in-parts`, `estimate-case-protocol-case-form`, `estimate-orchestration-batches-cases-out-at-once`, `estimate-orchestration-signs-a-batch-together`, `estimate-sprint-close-next-session-opens-the-sprint`); `estimate-event-log-records` and `estimate-sprint-close-moves-old-event-logs`, which promise a `.gitignore` that the clean version does not hold — `ROOT_FILES` of `.guppi/guppi/ship.py` is `CLAUDE.md` and `.gitattributes` — a gap for `rule-clean-branch`; `estimate-case-check-sends-back-a-faulty-case`, whose temporary old path still stands in `subagent` of `.guppi/guppi/casecheck.py` though `estimate-case-build-writes-the-case` is `passed`, so its sentence goes when a Case removes that path; and five whose method waits for a later moment (`estimate-compact-recall-reloads`, `estimate-glossary-checks-the-file`, `estimate-orchestration-forwards-a-discussion-question`, `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-synthesis-clusters`) and `estimate-permissions`, whose method needs the person's word on probes this session may not make; `estimate-orchestration-asks-in-the-grill-me-shape`, whose method reads the new Render of `rule-orchestration` at the Retro of a session that changes it, and no Case of this session changes it; and `estimate-ask-query-before-a-create`, whose Criterion names Russian and English, which the reading of 2104 listed and that of 1805 did not. 880.21 takes up the put-off of Case 875 and puts `rule-clean-branch` off again with that rest named; `decision-case-875` then stands `superseded`, as `generate` does for a taken-up put-off, and the pages it changed stay as they are. Of the target rules, `rule-case-build`, `rule-orchestration`, `rule-git-context`, `rule-guppi-package` and `rule-ratification` are `draft` already; the other ten are `built` and go `draft` only if a reading fails. The frame read: `STEPS` of `.guppi/guppi/check.py` runs `guppi render --check`, then `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check`, then `guppi lint` and `guppi ship --check`, which 880.17 states in place of the `Makefile`; `PLAIN_SPRINTS = ("migration", "plugin")` and `is_plain` of `.guppi/guppi/caseid.py` give a plain id to a sprint of that list or none (880.15); the `generate` docstring fills a placeholder `create` with no `kind` (880.12); `callers` and `live_pages` of `.guppi/tests/test_guppi_package.py` read the `Makefile` when it stands, each file under `.claude/` and `.github/workflows/`, and every live rule, entity and Estimate, and fail on `uv run guppi`, `uv run pytest` or a bare `guppi/` or `tests/` path, which no new text holds; `test_live_build_of_this_repository_prints_no_line_on_a_shipped_page_of_the_checks` of `.guppi/tests/test_ship.py` builds this repository live and fails on a `ship:` line on an Estimate, and each new pointer stands in a bracket of its own. A Grep `gitignore` over `plugin/**`, `.claude/**`, `rule-morph.md`, `rule-plugin-install.md`, `rule-event-log.md`, `rule-sprint-close.md` and `.guppi/guppi/*.py` printed `vault/wiki/rules/rule-event-log.md`, `.guppi/guppi/archive.py`, `.guppi/guppi/event.py`, `.guppi/guppi/sprint_close.py` and `.guppi/guppi/ship.py`, none a writer of a root `.gitignore` for a new project. A Grep for the slugs `estimate-git-context-current`, `estimate-guppi-package-runs-from-its-own-folder`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-ratification-case-id-carries-the-sprint`, `estimate-sprint-checks-the-file` and `estimate-tests-clock-pinned` over `vault/wiki/`, `brief.md`, `log.md` and `backlog.md` left out, printed `rule-guppi-package.md`, `rule-git-context.md`, `rule-where-to-stop.md`, `rule-tests-clock-pinned.md`, `rule-sprint.md`, `rule-skill-sprint-close.md`, `rule-ratification.md` (the `estimates` field and History), `estimate-clean-branch-ships-neutral-texts.md` (its Result) and `estimate-sprint-plugin-close-steps-run-from-the-line.md`, whose line that `estimate-skill-sprint-close-leads-the-closing-session` holds the steps of the skill stays true; none enters the Case. A Glob `vault/**/estimate-guppi-repository-*.md` printed nothing, so the three new slugs are free. The Render of a shipped rule that names a skill that does not ship, such as `vault/wiki/where-to-stop.md` and `.claude/skills/sprint-close/SKILL.md`, is the item `rule-clean-branch` of the sprint, not this Case. Each sub-case is checked by the Estimate whose Criterion it replaces or creates; 880.21 by the `uv run --project .guppi guppi check` of the librarian's run, which the brief reports, its step `guppi backlog --check` promised by `estimate-backlog-checks-the-file`, and by the check of each `deferred_by` on a live page that the brief reports; `estimate-generate-writes-the-decision-page` already promises that a `supersedes` clears the put-off on each page the superseding Case names and that `## Deferred` holds the `purpose` of a `defer` verbatim, so both Criteria stand.

> **problem:**
> The clean version of GUPPI ships Criteria of `passed` Estimates with sentences that hold only in the repository of GUPPI, so a new project reads promises that are false there or point to pages it does not hold; each fix replaces a Criterion whole and sets its Estimate `pending`.

> **recommend:**
> - **How does a Criterion sentence that holds only in GUPPI change?**
>   - Recommended: (a) replace each Criterion whole.
>   - Answer: agreed, (a).
> - **How much does this Case take?**
>   - Recommended: (b) only the Estimates whose reading this session can take.
>   - Answer: agreed, (b).
> - **What happens to a check that is meant to hold only in GUPPI?**
>   - Recommended: (b) move the GUPPI part into a new Estimate on `entity-guppi-repository`.
>   - Answer: agreed, (b).
> - **How is a sentence reworded?**
>   - Recommended: (a) the same way as the last session.
>   - Answer: agreed, (a).
> - **Is a pointer to an Estimate that is still `pending` reworded?**
>   - Recommended: (b) keep these pointers, and leave the six out of this Case.
>   - Answer: agreed, (b).
> - **What happens to the promise that git ignores the event log?**
>   - Recommended: (b) leave both Estimates out of this Case, and name the gap for `rule-clean-branch`.
>   - Answer: agreed, (b).
> - **What happens to the temporary old path in the Case check?**
>   - Recommended: (b) leave this Estimate out of this Case.
>   - Answer: agreed, (b).
> - **What happens to the other facts that hold only in GUPPI?**
>   - Recommended: (b) say the first by role, drop the second, move the third.
>   - Answer: agreed, (b).
> - **What happens to the put-off on `rule-clean-branch`?**
>   - Recommended: (b) take it up and put it off again, naming only what is left.
>   - Answer: agreed, (b).

### Case 880.1 — The description of the project in CLAUDE.md is said by its role

> **given:**
> `estimate-claude-md-rendered`: its Criterion is replaced whole.
> **＋** `rule-claude-md`: its target, the rule whose Render is `CLAUDE.md`.
> **＋** `CLAUDE.md`: the file it checks.
> **＋** `<!-- project-description -->` and `<!-- /project-description -->`: the marker lines around the description of the project.
> **＋** `vault/`, `vault/wiki/glossary.md` and `/hi`: the folder, the path and the skill of the paragraph after the description.
> **＋** `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation`: the children of `rule-claude-md`.
> **＋** `rule-governed-files-hook`: the hook that refuses a hand edit.
> **＋** `vault/wiki/ratification.md`: the file of the one rule.

> **when:**
> `guppi render` writes `CLAUDE.md` from `rule-claude-md` and its children, and a session or a subagent starts and loads the file.

> **then:**
> `CLAUDE.md` is: the line `<!-- project-description -->`; the heading and the description of the project; the line `<!-- /project-description -->`; the paragraph "The vault is vault/; its terms are vault/wiki/glossary.md. A working session opens with /hi.", whose words the file holds with the folder, the path and the skill in code spans; then the text of `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers.
> **＋** `render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
> **＋** Every session and every subagent loads this text.
> **－** No `@` import, no "What is loaded here", no paragraph on `index.md`, no "Migration mode", no "Commands", no one rule and no sentence on memory — the one rule is in `vault/wiki/ratification.md`; the `children` of `rule-claude-md` are `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation`.

```then
update:
- slug: estimate-claude-md-rendered
  set:
    status: pending
  change: the Criterion replaced whole — the heading and the description of the project said by their role, not as those of GUPPI
```

```tasks
- [ ] update `estimate-claude-md-rendered`
- [ ] read `estimate-claude-md-rendered`
```

### Case 880.2 — The test-code reading of case-guppi names no Insight

> **given:**
> `estimate-case-build-reads-the-test-code-over-a-changed-text`: its Criterion is replaced whole.
> **＋** `rule-case-build`: its target, the rule of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from it.
> **＋** `vault/` and `.claude/`: the folders whose live files a Case changes.
> **＋** `.guppi/tests/` and `.guppi/guppi/`: the tests and the code that `case-guppi` reads.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case that changes a live file of `vault/` or `.claude/`, by a page `update` or by the render of its rule.

> **then:**
> It searches `.guppi/tests/` for the tests that read that file live, not a copy under a temporary folder.
> **＋** For each such test, it reads the new text against the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `.guppi/guppi/` they call.
> **＋** Each place where the new text would fail the test enters the Case as a task that changes the test or the text, or its `context` says why it stands.

```then
update:
- slug: estimate-case-build-reads-the-test-code-over-a-changed-text
  set:
    status: pending
  change: the Criterion replaced whole — the line on an Insight of the repository of GUPPI dropped
```

```tasks
- [ ] update `estimate-case-build-reads-the-test-code-over-a-changed-text`
- [ ] read `estimate-case-build-reads-the-test-code-over-a-changed-text`
```

### Case 880.3 — The changed-check reading of case-guppi names no Insight

> **given:**
> `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`: its Criterion is replaced whole.
> **＋** `rule-case-build`: its target, the rule of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from it.
> **＋** `vault/` and `.claude/`: the folders of the live files a test reads.
> **＋** `.guppi/tests/`: the tests that `case-guppi` searches.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case that changes the code of a check.

> **then:**
> It searches `.guppi/tests/` for the tests that read a live file of `vault/` or `.claude/`, not a copy under a temporary folder.
> **＋** For each such test whose code reaches the changed code, directly or through a module that imports it, it reads that file against the new check.
> **＋** Each text of that file that the new check would refuse enters the Case, or its `context` says why it stands.

```then
update:
- slug: estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check
  set:
    status: pending
  change: the Criterion replaced whole — the line on an Insight of the repository of GUPPI dropped
```

```tasks
- [ ] update `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`
- [ ] read `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`
```

### Case 880.4 — The check of round titles names its function by its role

> **given:**
> `estimate-case-check-requires-each-question-of-the-rounds`: its Criterion is replaced whole.
> **＋** `rule-case-check`: its target, the rule of the check of `case-guppi`.
> **＋** `.guppi/guppi/casecheck.py`: the code of the check.
> **＋** `.claude/skills/grill-me/SKILL.md`: the template of a round.

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `agent_transcript_path` holds the agent's earlier outputs with no Case heading, which are its rounds of questions on that Case.

> **then:**
> `uv run --project .guppi guppi casecheck --subagent` takes the title of each question of those rounds from its line `❓ **Q<n>** - **<title>**:`, the title line of the template of `.claude/skills/grill-me/SKILL.md`.
> **＋** It takes titles only from a round that the function of `.guppi/guppi/casecheck.py` that judges the form of a round finds in form, the function by which the check sends a round out of form back; a round out of form gives no title (as set in case 601.1).
> **＋** A title that no item of a `recommend` opens with, in bold, among the Cases of the answer and the entries of `<plan>.checked.json` under the number alone of each Case of their family that the answer does not hold, is a finding of the top-level Case — of the first Case of the answer when it holds sub-cases alone — that names the title, sent back and stored as any other finding.
> **－** An answer with no earlier round gives no such finding.
> **－** A title asked in more than one round is looked for once.
> **－** The words of an item after its title are not judged.
> **－** A round out of form that came back unchanged, passed the check of its form and was shown gives no title either.

```then
update:
- slug: estimate-case-check-requires-each-question-of-the-rounds
  set:
    status: pending
  change: the Criterion replaced whole — the function that judges the form of a round named by its role, its case number in a bracket
```

```tasks
- [ ] update `estimate-case-check-requires-each-question-of-the-rounds`
- [ ] read `estimate-case-check-requires-each-question-of-the-rounds`
```

### Case 880.5 — An entry with no agent id is named by what holds it

> **given:**
> `estimate-case-check-sends-back-a-case-number-held-by-another-agent`: its Criterion is replaced whole.
> **＋** `rule-case-check`: its target, the rule of the check of `case-guppi`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape`: the Estimate that counts a free id.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of that file, `agent_id` of the payload, and `<plan>.checked.json`.

> **then:**
> The hook stores each Case of the file in `<plan>.checked.json` with the `agent_id` of the payload beside its text, its findings and the time of the store.
> **＋** A top-level Case N of the file, N a plain id or an id of a sprint, is sent back when the store holds Case N, or a sub-case of it, under its id from an answer with another `agent_id`.
> **＋** Its message gives `case-guppi` a free id, counted as `estimate-case-check-sends-back-a-ratified-case-in-another-shape` counts it, to build the Case under, and the exit code is 2.
> **＋** Each Case of that file is stored apart, under its id joined with its `agent_id`, and the entry of the other agent under the id alone stays as it was.
> **＋** The Spec hook, the `Stop` comparison and the comparison of a case file with the store read the entry under the id alone.
> **－** An unchanged file whose text its entry apart already holds with this finding is stored again and exits 0, so it is not sent back twice.
> **－** An entry with no `agent_id`, such as one held by `uv run --project .guppi guppi caseid --next`, gives no finding of this check, and neither does a file whose `agent_id` is the one of the entry under the id (an entry stored before case 610.2 holds none either).

```then
update:
- slug: estimate-case-check-sends-back-a-case-number-held-by-another-agent
  set:
    status: pending
  change: the Criterion replaced whole — an entry with no agent_id named by what holds it, the entries from before the change in a bracket at the end of the sentence
```

```tasks
- [ ] update `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- [ ] read `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
```

### Case 880.6 — The context of /hi promises no remote of GUPPI

> **given:**
> `estimate-git-context-current`: its Criterion is replaced whole, and its method set anew.
> **＋** `rule-git-context`: its target, the rule of the git commands of `/hi`.
> **＋** `.claude/skills/hi/SKILL.md`: the skill that runs them.

> **when:**
> The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the commands of `rule-git-context`.

> **then:**
> The context holds `Render:` with the output of `uv run --project .guppi guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
> **－** The skill runs no `git pull`, and the context holds no `Pull:` line.

```then
update:
- slug: estimate-git-context-current
  set:
    status: pending
    method: 'by hand, after a /hi: the first turn''s context and .claude/skills/hi/SKILL.md read against the Criterion, written into the estimate line'
  change: the Criterion replaced whole — the line on the remote of the repository of GUPPI moved to estimate-guppi-repository-remote-on-github; the method reads no git remote
```

```tasks
- [ ] update `estimate-git-context-current`
- [ ] read `estimate-git-context-current`
```

### Case 880.7 — The repository of GUPPI has its remote on GitHub

> **given:**
> `estimate-guppi-repository-remote-on-github`: the new check of the remote of the repository.
> **＋** `entity-guppi-repository`: its target, the repository of GUPPI on GitHub.

> **when:**
> Someone runs `git remote -v` in the repository of GUPPI.

> **then:**
> It prints `origin` with the URL of the repository `GUPPI` on GitHub, once for fetch and once for push.

```then
create:
- slug: estimate-guppi-repository-remote-on-github
  ref: entity-guppi-repository
  kind: QA
  purpose: Whether the repository of GUPPI has its remote origin on GitHub
  method: 'by hand: git remote -v in the repository, its output written into the estimate line'
  tags:
  - git
  - github
```

```tasks
- [ ] create `estimate-guppi-repository-remote-on-github`
- [ ] read `estimate-guppi-repository-remote-on-github`
```

### Case 880.8 — The package of GUPPI runs from its own folder in any project

> **given:**
> `estimate-guppi-package-runs-from-its-own-folder`: its Criterion is replaced whole, and its purpose set anew.
> **＋** `rule-guppi-package`: its target, the rule of the package under `.guppi/`.
> **＋** `.guppi/pyproject.toml`: the settings of the package.
> **＋** `.venv/`: the Python environment that the `.gitignore` under `.guppi/` leaves out.
> **＋** `.claude/settings.json`: the hooks that run the code.
> **＋** `.claude/`: the skills and the agents that run the code.
> **＋** `.github/workflows/`: the workflows that run the code.
> **＋** `.guppi/tests/test_guppi_package.py`: the test of the commands and the paths.
> **＋** `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema`: the pages whose examples keep a path of a project of the person's own.

> **when:**
> In the project, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.

> **then:**
> The package `guppi`, its `pyproject.toml`, its lock file `uv.lock`, its tests and a `.gitignore` that holds `.venv/` stand under `.guppi/`, and `.guppi/pyproject.toml` declares pytest and ruff for the tests.
> **＋** Each hook of `.claude/settings.json`, and each command of a skill, an agent or a workflow of `.github/workflows/` that runs the code of GUPPI or its tests, runs it through `uv run --project .guppi`, and no hook prints an error.
> **＋** No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` without `--project .guppi` outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
> **＋** `.guppi/tests/test_guppi_package.py` fails on such a command in a file of `.claude/`, `.github/workflows/` or a live rule, entity or Estimate, and on such a path in such a page, found by the matching of `reword` of `guppi generate`.
> **＋** Each module that finds its own refusals in the transcript by the command of its hook finds them under the command with `--project .guppi` and under the command without it.
> **＋** The Bash and PowerShell guards judge `uv run --project .guppi python` as they judge `uv run python`, and `guppi lint` takes a test path under `.guppi/tests/` in a `method` as it takes one in the folder of tests of the project's own code.
> **－** The examples of a project of the person's own in `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` keep a path of tests of that project, with no `.guppi/`.

```then
update:
- slug: estimate-guppi-package-runs-from-its-own-folder
  set:
    status: pending
    purpose: Whether the code, the settings, the lock and the tests of GUPPI stand under .guppi/, every hook, skill, agent, workflow and page runs them through uv run --project .guppi, and the modules and the guards take that form
  change: the Criterion replaced whole — the Makefile, prod.yml, the root pyproject.toml, the clean version and the records of the repository of GUPPI moved to estimate-guppi-repository-keeps-the-development-project
```

```tasks
- [ ] update `estimate-guppi-package-runs-from-its-own-folder`
- [ ] read `estimate-guppi-package-runs-from-its-own-folder`
```

### Case 880.9 — The repository of GUPPI keeps its development project

> **given:**
> `estimate-guppi-repository-keeps-the-development-project`: the new check of the layout that only the repository of GUPPI holds.
> **＋** `entity-guppi-repository`: its target, the repository of GUPPI on GitHub.
> **＋** `Makefile`: the targets of the repository.
> **＋** `.github/workflows/prod.yml`: the workflow that writes `prod`.
> **＋** `.guppi/tests/test_guppi_package.py`: the test of the commands.
> **＋** `rule-clean-branch`: the rule of the clean version.

> **when:**
> In the repository of GUPPI, the `Makefile` and `.github/workflows/prod.yml` run the code of GUPPI or its tests, `uv run --project .guppi pytest` runs `.guppi/tests/test_guppi_package.py`, and `uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it.

> **then:**
> Each command of the `Makefile` and of `.github/workflows/prod.yml` that runs the code of GUPPI or its tests runs it through `uv run --project .guppi`.
> **＋** `.guppi/tests/test_guppi_package.py` fails on a command of the `Makefile` that runs that code or those tests through `uv run` without `--project .guppi`.
> **＋** The repository keeps at its root, until a Case of a later session removes them, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so a command without `--project .guppi` still runs at its root and no hook of a running session fails.
> **＋** The clean version holds no `pyproject.toml` and no `uv.lock` at its root.
> **－** The Decision pages, the lessons and the Insights keep the commands and the paths from before the code moved under `.guppi/`, since they are records.

```then
create:
- slug: estimate-guppi-repository-keeps-the-development-project
  ref: entity-guppi-repository
  kind: QA
  purpose: Whether the repository of GUPPI keeps the files of a development project around the package in .guppi/, its Makefile and its workflow prod.yml run the code through uv run --project .guppi, and the clean version holds no pyproject.toml at its root
  method: 'uv run --project .guppi pytest .guppi/tests/test_guppi_package.py; by hand: the Makefile, .github/workflows/prod.yml and the root of the repository read against the Criterion, written into the estimate line'
  tags:
  - harness
  - plugin
```

```tasks
- [ ] create `estimate-guppi-repository-keeps-the-development-project`
- [ ] read `estimate-guppi-repository-keeps-the-development-project`
```

### Case 880.10 — The defer example names no Insight

> **given:**
> `estimate-orchestration-defer-example-passes-the-hook`: its Criterion is replaced whole, and its purpose set anew.
> **＋** `rule-orchestration`: its target, the rule of the main agent.
> **＋** `vault/wiki/orchestration.md`: the file that holds the example.
> **＋** `.guppi/tests/test_orchestration.py`: the test over the example.
> **＋** `.guppi/guppi/ratified.py`: the functions of the hook.
> **＋** `rule-spec-write`: the rule of the `Stop` hook that writes the Spec.
> **＋** `vault/raw/2026-10-17/1805/cases/case-879.md`: Case 879, whose 879.1 names a short put-off and its path.

> **when:**
> `.guppi/tests/test_orchestration.py` runs under `uv run --project .guppi pytest`. It reads the block tagged `defer` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it, as the text of a reply, the functions of `.guppi/guppi/ratified.py` that the `Stop` hook of `rule-spec-write` runs over a short put-off, a Case of `defer` lines that the reply shows in the short form, in a temporary project that holds the schema files of the vault and a plan file, with one `defer` record for each item of the example.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## The short form — deferred decisions`, one block tagged `defer`: a Case in the short form with its heading, `context`, `problem` and a fence tagged `then` whose `defer:` holds a list, one item per target, each item opening with `- slug:` and carrying `type` and `purpose`.
> **＋** The paragraph before the block says that the reply that shows the Case carries its `LEDGER` block with one `defer` line per item, and that the example passes the `Stop` hook of `rule-spec-write`, which is the source of the limits; it lists no other limit.
> **＋** The hook writes the example under `## Deferred` of the plan file with no error, and the test passes.
> **＋** The example with its `defer:` items written as one mapping gives the error that no fence tagged `then` holds its `defer` items, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the hook from `.guppi/guppi/ratified.py`, and holds no copy of either.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `defer`, both tests of `.guppi/tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

```then
update:
- slug: estimate-orchestration-defer-example-passes-the-hook
  set:
    status: pending
    purpose: Whether the example of a short-form defer in orchestration.md passes the Stop hook that writes a short put-off into the Spec, so the form the main agent copies stays a form the hook accepts
  change: the Criterion replaced whole — the line on an Insight of the repository of GUPPI dropped; the hook runs over a short put-off, the term of case 879.1
```

```tasks
- [ ] update `estimate-orchestration-defer-example-passes-the-hook`
- [ ] read `estimate-orchestration-defer-example-passes-the-hook`
```

### Case 880.11 — The pointer check of the plan names no command that does not ship

> **given:**
> `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`: its Criterion is replaced whole.
> **＋** `rule-prespec-hook`: its target, the rule of the check of the plan at `ExitPlanMode`.
> **＋** `.guppi/guppi/prespec.py`: the check of the plan.
> **＋** `.guppi/guppi/pointers.py`: the judgment of a pointer.
> **＋** `decision-case-N`: the form of the id of a Decision page, one form of a pointer.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan>` checks the plan of a session, or the hook of `rule-prespec-hook` runs the same judgment when the agent calls `ExitPlanMode`.

> **then:**
> It prints a finding for each pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — that stands outside a bracket of its own in the `new` of a `replace` pair, the text of a `sections` value or the `purpose` of an item for a page that carries `core: true`, on the live page or as the plan leaves it.
> **＋** It prints the same finding for an item of an Estimate whose target, the `ref` of a `create` or the `target` of the live page, carries `core: true` on the live page or as the plan leaves it: in its `purpose`, its `method`, each `sections` value it writes and its new `## Criterion`.
> **＋** The new `## Criterion` of such an Estimate is the one the item writes under `sections`, else the `when` and `then` of its Case, for a `create` and for an `update` that names no part of the page, read by the one function of `.guppi/guppi/prespec.py` by which the note on a Criterion line not carried reads it.
> **＋** The finding names the Case, the page and the pointer.
> **＋** It judges each text by `outside` of `.guppi/guppi/pointers.py`, imported.
> **－** A pointer inside such a bracket, a code span or a fenced block is no finding.
> **－** An item for a page without `core: true` that is no such Estimate, the `change` line of an item, and the `context`, `problem` and `recommend` of a Case are not judged.

```then
update:
- slug: estimate-prespec-hook-reports-a-pointer-outside-a-bracket
  set:
    status: pending
  change: the Criterion replaced whole — the clause on guppi ship, which the clean version does not hold, dropped
```

```tasks
- [ ] update `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
- [ ] read `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
```

### Case 880.12 — A placeholder is filled by generate, named by its command

> **given:**
> `estimate-materialize-marks-exists`: its Criterion is replaced whole.
> **＋** `rule-materialize`: its target, the rule of `guppi materialize`.

> **when:**
> `uv run --project .guppi guppi materialize` reads a `create` line whose slug is already on disk — live or archived.

> **then:**
> The entry is marked `exists` only when the `origin` of the page carries the `#case-N` of this line.
> **＋** Otherwise the entry stays an ordinary `create`.
> **－** A placeholder, a page with no `kind`, is not a collision: `uv run --project .guppi guppi generate` fills it (as set in case 101.1).

```then
update:
- slug: estimate-materialize-marks-exists
  set:
    status: pending
  change: the Criterion replaced whole — the writer that fills a placeholder named by its command, its case number in a bracket
```

```tasks
- [ ] update `estimate-materialize-marks-exists`
- [ ] read `estimate-materialize-marks-exists`
```

### Case 880.13 — The command-line check of the plan keeps its case number in a bracket

> **given:**
> `estimate-prespec-catches-a-command-line-off-form`: its Criterion is replaced whole.
> **＋** `rule-prespec`: its target, the rule of `/pre-spec`.
> **＋** `/pre-spec`: the skill that runs the check.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the `tasks` block of every Case of a plan, as `/pre-spec` runs it on the plan of this Plan Mode.

> **then:**
> A `tasks` line whose text after the box opens with the word `render` or `sprint`, or with `guppi render`, `guppi sprint`, `uv run --project .guppi guppi render` or `uv run --project .guppi guppi sprint` outside a code span, is a finding `case N: render line off form: <line>`.
> **＋** The form the tickers of `render` and `sprint` match is `` - [ ] `uv run --project .guppi guppi render`: … `` and `` - [ ] `uv run --project .guppi guppi sprint` ``, the command in the first code span.
> **－** A line that opens with a code span holding the command is no finding; a `read` line that names the command in a later span is no finding (as set in case 235).

```then
update:
- slug: estimate-prespec-catches-a-command-line-off-form
  set:
    status: pending
  change: the Criterion replaced whole — the bare case number written in a bracket with the word case
```

```tasks
- [ ] update `estimate-prespec-catches-a-command-line-off-form`
- [ ] read `estimate-prespec-catches-a-command-line-off-form`
```

### Case 880.14 — One judgment, one implementation holds for any code

> **given:**
> `estimate-one-judgment-one-implementation-followed`: its Criterion is replaced whole.
> **＋** `rule-one-judgment-one-implementation`: its target, the rule in `CLAUDE.md`.
> **＋** `CLAUDE.md`: the file every context loads.
> **＋** `rule-governed-files-hook`: the hook that refuses a hand edit.

> **when:**
> The agent writes code that judges a text another part of the pipeline already judges, such as a check beside a writer, a ticker or another check.

> **then:**
> The pattern or the predicate lives in one module, and both sides import it.
> **＋** Where the two sides cannot share the code, one test runs both over the same input and asserts they answer alike.
> **＋** `CLAUDE.md`, which every session and every subagent loads, holds this text between the markers of `rule-one-judgment-one-implementation`; `render --check` keeps it equal to the page, and the hook of `rule-governed-files-hook` refuses a hand edit.
> **－** No script refuses a second copy: the guard is the text in the file every context reads, and the reading of the session's diff.

```then
update:
- slug: estimate-one-judgment-one-implementation-followed
  set:
    status: pending
  change: the Criterion replaced whole — the code that judges a text is any code, not only that of the package of GUPPI
```

```tasks
- [ ] update `estimate-one-judgment-one-implementation-followed`
- [ ] read `estimate-one-judgment-one-implementation-followed`
```

### Case 880.15 — The sprints with plain ids are those of the fixed list

> **given:**
> `estimate-ratification-case-id-carries-the-sprint`: its Criterion is replaced whole, and its purpose set anew.
> **＋** `rule-ratification`: its target, the rule of the ledger and the Case id.
> **＋** `.guppi/guppi/caseid.py`: the reader of a Case id and its fixed list `PLAIN_SPRINTS`.
> **＋** `.guppi/guppi/casecheck.py`, `.guppi/guppi/ratified.py`, `.guppi/guppi/lint.py`, `.guppi/guppi/gate.py` and `.guppi/guppi/materialize.py`: the readers of a Case id.
> **＋** `vault/wiki/orchestration.md` and `rule-orchestration`: the steps of the main agent.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `vault/wiki/sprint.md`: the file of the open sprint.
> **＋** `/sprint-open`: the skill that sets the id of the opening Case.

> **when:**
> `.guppi/guppi/casecheck.py`, `.guppi/guppi/ratified.py`, `.guppi/guppi/lint.py`, `.guppi/guppi/gate.py` or `.guppi/guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
> **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run --project .guppi guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
> **＋** Or `uv run --project .guppi guppi caseid --next` runs without `--session`, or with a stamp whose session has no plan file.

> **then:**
> A Case id of a sprint that `PLAIN_SPRINTS` of `.guppi/guppi/caseid.py` does not list is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case (sprint ids came in with case 788.2).
> **＋** The readers read a Case id through `.guppi/guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
> **＋** The sprints that `PLAIN_SPRINTS`, a fixed list in `.guppi/guppi/caseid.py`, names keep plain ids to their close (the sprints of that list opened before case 788.2).
> **＋** The main agent creates the plan file of its session with its title line before its first run of the command.
> **＋** `uv run --project .guppi guppi caseid --next --session <stamp>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
> **＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
> **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
> **－** The main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id or what the store holds, since each run holds a new id.
> **－** Without `--session` the command prints no id: it prints its usage error and exits 2.
> **－** With a stamp whose session has no plan file, the command prints no id, holds nothing, prints one line on stderr and exits 1.
> **－** An id with no sprint part, such as `785.1`, stays as it is, and no page, file or citation is renamed.

```then
update:
- slug: estimate-ratification-case-id-carries-the-sprint
  set:
    status: pending
    purpose: Whether every reader of a Case id takes an id that carries its sprint and a plain id alike, and guppi caseid --next --session <stamp> prints and holds the next id of the open sprint, which the main agent runs only for the id of a new top-level Case and never to check an id, and prints no id without --session or without the plan file of the session
  change: the Criterion replaced whole — the sprints with plain ids named by the fixed list PLAIN_SPRINTS, not as migration and plugin, the pointers kept in brackets
```

```tasks
- [ ] update `estimate-ratification-case-id-carries-the-sprint`
- [ ] read `estimate-ratification-case-id-carries-the-sprint`
```

### Case 880.16 — The closing skill names no closed sprint and no skill that does not ship

> **given:**
> `estimate-skill-sprint-close-leads-the-closing-session`: its Criterion is replaced whole, and its method set anew.
> **＋** `rule-skill-sprint-close`: its target, the rule of `/sprint-close`.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the skill rendered from it.
> **＋** `gh api repos/{owner}/{repo}/commits/main --jq .sha`: the command that reads the commit of `main`.
> **＋** `vault/wiki/orchestration.md`: the file of the main agent.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian, who runs the close line.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the skill whose opening Case holds the merge.

> **when:**
> The person takes up on the Frontier the line of the sprint that names `/sprint-close`, and the main agent starts the skill `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, rendered from `rule-skill-sprint-close`, on `PreToolUse Skill`, or the person types `/sprint-close` on `UserPromptSubmit`.

> **then:**
> Writing nothing into `.git`, the main agent first runs `gh api repos/{owner}/{repo}/commits/main --jq .sha`, which prints `<hash>`, and `git merge-base --is-ancestor <hash> HEAD`. When the second exits other than 0, it closes the close line `[-] … · sprint · defer`, tells the person to bring the branch up to `main` first, in a session of its own, and the skill stops. When `gh api` fails, it shows the output and the skill stops the same way.
> **＋** When the session's ledger holds a decision line other than a `defer`, the main agent closes the close line `[-] … · sprint · defer`, tells the person that the close needs a session of its own, and the skill stops.
> **＋** Otherwise the main agent closes each other open line under `## Cases` of `frontier.md` by the closer of its source put off, the person's pick of the close line standing as the words that ratify each short-form defer, leaves the lines under `## Work` and `## Ask` open, and shows the Frontier.
> **＋** It sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names and dispatches `case-guppi` for the closing Case with the groups in the prompt, and the closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run --project .guppi guppi sprint-close --sprint <id> --apply` with the person's choice for each Estimate still unread.
> **＋** Work Mode takes each reading whose moment came and neither runs nor ticks the close line; the librarian runs it, as `.claude/agents/librarian-guppi.md` sets it.
> **＋** `vault/wiki/orchestration.md` holds no paragraph on the closing session, names the two skills in one sentence, and counts the start of `/sprint-close` among the moments of a short-form defer.
> **－** Besides the closing Case, the session ratifies only the Cases that prepare its readings.
> **－** The closing Case holds no task line for the merge of the sprint's branch into `main`: the opening Case of the next sprint holds the merge, as `.claude/skills/sprint-open/SKILL.md` sets it.

```then
update:
- slug: estimate-skill-sprint-close-leads-the-closing-session
  set:
    status: pending
    method: 'by hand: the Render of rule-skill-sprint-close in .claude/skills/sprint-close/SKILL.md and vault/wiki/orchestration.md read against the Criterion'
  change: the Criterion replaced whole — the step before the close said without the skill merge-main, and no line on the close line of a closed sprint of the repository of GUPPI; the method reads no archived sprint page
```

```tasks
- [ ] update `estimate-skill-sprint-close-leads-the-closing-session`
- [ ] read `estimate-skill-sprint-close-leads-the-closing-session`
```

### Case 880.17 — The sprint check runs within guppi check

> **given:**
> `estimate-sprint-checks-the-file`: its Criterion is replaced whole.
> **＋** `rule-sprint`: its target, the rule of `vault/wiki/sprint.md`.
> **＋** `vault/wiki/sprint.md`: the file it checks.
> **＋** `estimate-sprint-marks-a-closed-sprint`: the Estimate that sets the closed form.

> **when:**
> Someone runs `uv run --project .guppi guppi sprint --check`, by hand or through `uv run --project .guppi guppi check`, and it renders the file from the sprint page in memory.

> **then:**
> When `vault/wiki/sprint.md` differs from the render of the page, stdout holds one line `sprint: <file> differs from entity-sprint-<id>`, the file named by its path from the project root, and the check exits 1. When the file equals the render, the check exits 0 with no output. The file is written in neither case.
> **＋** `uv run --project .guppi guppi check` runs it after `guppi render --check` and before `guppi lint`.
> **＋** With no live sprint page, the check compares the file with the closed form that `estimate-sprint-marks-a-closed-sprint` sets, and the line on stdout reads `sprint: <file> differs from the closed form of <id>`.
> **－** A render error, such as two sprint pages, a slug with no page, or no sprint page and no file, is one line on stderr and exit 1, as with `guppi sprint`.

```then
update:
- slug: estimate-sprint-checks-the-file
  set:
    status: pending
  change: the Criterion replaced whole — the check runs within guppi check, not by a target of the Makefile
```

```tasks
- [ ] update `estimate-sprint-checks-the-file`
- [ ] read `estimate-sprint-checks-the-file`
```

### Case 880.18 — The pinned clock holds for every run of the tests

> **given:**
> `estimate-tests-clock-pinned`: its Criterion is replaced whole.
> **＋** `rule-tests-clock-pinned`: its target, the rule of the pinned clock.
> **＋** `.guppi/tests/conftest.py`: the file of the fixture.
> **＋** `.guppi/tests/test_conftest.py`: the test of the fixture.
> **＋** `.guppi/tests/` and `.guppi/guppi/`: the tests and the modules.

> **when:**
> `pytest` collects `.guppi/tests/`, and a test calls the `run()` of a module of `.guppi/guppi/` without `now`, or the code reads the clock outside `run()`.

> **then:**
> Before every test, an autouse fixture in `.guppi/tests/conftest.py` sets into every module of `.guppi/guppi/` that carries a `datetime` attribute a subclass whose `now(tz=None)` returns `2001-01-01 00:00:00 UTC`, and `astimezone` gives the same second. A test that leaves the code on the real clock sees the year 2001 and fails on the day it is written.
> **＋** The list of modules comes from a walk over `.guppi/guppi/`, never from a hand list: a new module with a clock is covered with no change to the fixture.
> **＋** `.guppi/tests/test_conftest.py` shows it: a `run()` without `now` writes a time dated 2001, and `datetime.strptime`, `fromisoformat` and the constructor of the subclass work as before.
> **＋** Each run of the tests of `.guppi/tests/` under pytest runs under the same fixture, whatever command starts it.
> **－** A test that passes `now` does not notice the fixture: `run()` reads no clock.

```then
update:
- slug: estimate-tests-clock-pinned
  set:
    status: pending
  change: the Criterion replaced whole — every run of the tests is under the fixture, not the targets of the Makefile
```

```tasks
- [ ] update `estimate-tests-clock-pinned`
- [ ] read `estimate-tests-clock-pinned`
```

### Case 880.19 — Where to stop names only the merges that ship

> **given:**
> `estimate-where-to-stop-stops-only-on-its-conditions`: its Criterion is replaced whole.
> **＋** `rule-where-to-stop`: its target, the rule of the stops of the run.
> **＋** `vault/wiki/where-to-stop.md`: the file rendered from it.
> **＋** `/work`, `/box` and `/retro`: the skills of the run.
> **＋** `.claude/skills/box/SKILL.md`: the skill file of `/box`.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the skill whose opening Case holds merge tasks.
> **＋** `raw/<date>/<hi HHMM>/spec.md`, `raw/<date>/<hi HHMM>/work.md` and `raw/<date>/<hi HHMM>/handoff.md`: the files of the session.
> **＋** `vault/wiki/case-schema.md`: the schema that names a `stop:` task.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
> **＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

> **then:**
> The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
> **＋** The context of `/box`, from `.claude/skills/box/SKILL.md`, holds the same text.
> **＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
> **＋** A fork that changes a contract is a choice that no ratified Case makes, or a ratified Case that turns out wrong: by a text the agent finds wrong or too narrow, or by a finding of `uv run --project .guppi guppi prespec --check` on the plan after a Case ratified in Work Mode.
> **＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
> **＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
> **＋** In a run of `/box`, the agent stops and asks when `uv run --project .guppi guppi box --check` prints a line, or when a `git merge --ff-only` of `/box` refuses.
> **＋** In the merge tasks that the opening Case of a sprint holds by `.claude/skills/sprint-open/SKILL.md`, the agent stops, shows what stopped it and asks when a `git` or `gh` command refuses.
> **＋** When the full `uv run --project .guppi guppi test` run of `/work` after its last task finds a failing test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold, and its fix needs a choice that no ratified Case makes, the agent ends a reply with a question to the person that names the test and its failure.
> **＋** When the auto mode classifier of Claude Code refuses a tool call that the run needs, the agent ends a reply with a question to the person that gives the shell command doing what the refused call would do, for the person to type after `!` in the prompt.
> **＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
> **＋** After the person's answer the run goes on from where it stopped.
> **＋** After the person has run the command that a refusal of the auto mode classifier gave, the run goes on from where it stopped.
> **＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
> **－** No other point stops the run, but a stop that a skill the project holds sets in the tasks of its own Case: any other red test, at `/retro` too, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

```then
update:
- slug: estimate-where-to-stop-stops-only-on-its-conditions
  set:
    status: pending
  change: the Criterion replaced whole — the stops in the merge tasks of the skills pr-review and merge-main, which the clean version does not hold, moved to estimate-guppi-repository-stops-in-the-merge-tasks; a stop that a skill of the project sets for its own tasks is left room
```

```tasks
- [ ] update `estimate-where-to-stop-stops-only-on-its-conditions`
- [ ] read `estimate-where-to-stop-stops-only-on-its-conditions`
```

### Case 880.20 — The repository of GUPPI stops in its merge tasks

> **given:**
> `estimate-guppi-repository-stops-in-the-merge-tasks`: the new check of the stops in the merge tasks that only the repository of GUPPI holds.
> **＋** `entity-guppi-repository`: its target, the repository of GUPPI on GitHub.
> **＋** `.claude/skills/pr-review/SKILL.md`: the skill whose review Case holds a merge task.
> **＋** `.claude/skills/merge-main/SKILL.md`: the skill whose merge Case holds the merge tasks.
> **＋** `vault/wiki/where-to-stop.md` and `rule-where-to-stop`: the stops of the run.

> **when:**
> In the repository of GUPPI, with `vault/wiki/where-to-stop.md` rendered from `rule-where-to-stop`, the agent runs the merge task that a review Case holds by `.claude/skills/pr-review/SKILL.md`, or the tasks that a merge Case holds by `.claude/skills/merge-main/SKILL.md`.

> **then:**
> The agent stops, shows what stopped it and asks when a `git` or `gh` command refuses, or when the merge of a merge Case leaves in conflict a file that the merge Case does not settle.
> **－** `git merge --no-ff --no-commit` of a merge Case of `.claude/skills/merge-main/SKILL.md` that exits non-zero only on files that the merge Case settles is no refusal, and the run goes on to the tasks that settle them.

```then
create:
- slug: estimate-guppi-repository-stops-in-the-merge-tasks
  ref: entity-guppi-repository
  kind: QA
  purpose: Whether the run stops for the person when a git or gh command of the merge tasks of pr-review or merge-main refuses, or when a merge leaves in conflict a file that its merge Case does not settle, and on no refusal of a merge whose conflicts the merge Case settles
  method: 'by hand: vault/wiki/where-to-stop.md as rendered and the merge tasks that .claude/skills/pr-review/SKILL.md and .claude/skills/merge-main/SKILL.md set, read against the Criterion, written into the estimate line'
  tags:
  - session
  - workflow
  - git
```

```tasks
- [ ] create `estimate-guppi-repository-stops-in-the-merge-tasks`
- [ ] read `estimate-guppi-repository-stops-in-the-merge-tasks`
```

### Case 880.21 — The rest of the rewrite stays put off by name

> **given:**
> `rule-clean-branch`: the rule of the clean version, whose put-off is taken up and put off again.
> **＋** `vault/wiki/backlog.md`: the list of the pages put off.

> **when:**
> The librarian's run of this session applies the decision lines of this sub-case to `rule-clean-branch`, and `uv run --project .guppi guppi check` runs at the end of that run.

> **then:**
> `rule-clean-branch` is put off by the Decision page of this sub-case alone, whose `## Deferred` gives the put-off of this sub-case word for word: each listed Estimate that this Case leaves and why it is left.
> **＋** `vault/wiki/backlog.md` keeps its line for `rule-clean-branch`, and the step `guppi backlog --check` of `uv run --project .guppi guppi check` prints no line.
> **－** The changes that the earlier put-off made to the other pages stay as they are.

```then
update:
- slug: rule-clean-branch
  change: the put-off of case 875 taken up and put off again with the rest of the Criterion sentences named
defer:
- slug: rule-clean-branch
  type: rule
  purpose: 'The rest of the rewrite of the sentences inside the Criterion of shipped Estimates that hold only in the repository of GUPPI, which Case 880 left: estimate-compact-recall-reloads, estimate-glossary-checks-the-file, estimate-orchestration-forwards-a-discussion-question, estimate-synthesis-keeps-actioned-by-the-mark, estimate-synthesis-clusters, estimate-permissions and estimate-orchestration-asks-in-the-grill-me-shape, whose readings wait for a later moment; estimate-ask-query-before-a-create, which names Russian and English, and which Case 880 did not take; estimate-case-check-sends-back-a-faulty-case, whose sentence goes when a Case removes the old path of the check from .guppi/guppi/casecheck.py; estimate-event-log-records and estimate-sprint-close-moves-old-event-logs, which promise a .gitignore that the clean version does not hold, so that git tracks the event logs of a project that installs GUPPI, and a Case first decides whether the clean version gets one; and the pointers in estimate-case-build-checks-the-finished-case, estimate-case-build-reads-by-need-and-in-parts, estimate-case-protocol-case-form, estimate-orchestration-batches-cases-out-at-once, estimate-orchestration-signs-a-batch-together and estimate-sprint-close-next-session-opens-the-sprint, which hold once the pending Estimate each names passes and ships; put off by the person in session 1805'
```

```tasks
- [ ] update `rule-clean-branch`
- [ ] defer `rule-clean-branch`
```
