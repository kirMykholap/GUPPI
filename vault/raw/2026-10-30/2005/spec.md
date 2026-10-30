<!-- approved 21:45:35 · session b66fdf86 -->

# Session 2005 — the items of the brief of 1713

## Case 937 — A backlog item that a Case defers again closes as put off by that Case

> **context:**
> When a session ends an item of its Frontier, the agent closes the item's line with a closer. `orchestration.md` and the `/hi` skill give a backlog item two closers: `[x] … · backlog · case N` for a Case that takes the item off the backlog, and `[-] … · backlog · kept` for an item left as it stands, with no Case and no ledger line. They name none for a Case whose only decision puts the item off again with a new wording. In session 1713, Case 934 deferred `rule-spec-capture` again with `{supersedes:case 909}`. The agent closed its line `[x] … · backlog · case 934`, and `guppi prespec --check` printed two findings, as `lesson-frontier-closed-a-backlog-item-deferred-again-as-a-case` records. The line was then closed `kept`, although a Case stood. The person chose a third closer, `[-] … · backlog · defer case N`. The check accepts it when a `defer` line of Case N names a page of the title and carries `{supersedes:case M}` for each Case M of that page's `deferred_by`. A take-back keeps `kept`.
>
> The check is `check_frontier` of `.guppi/guppi/prespec.py`, which I read whole with `check_backlog_line`, `deferred_pages`, `decided_on_its_page`, `has_defer_item` and the closer constants `CLOSERS`, `PUT_OFF_SOURCE` and `PUT_OFF_CLOSER`. Today it refuses `defer case N` after `backlog` through `PUT_OFF_CLOSER`. It accepts `kept` after `backlog` and checks nothing more. It sends a line closed `[x] … · backlog · case N` to `check_backlog_line`, which calls `decided_on_its_page`. That function counts only lines other than a `defer` as naming the page. `generate.clear_deferred_by` of `.guppi/guppi/generate.py` drops Case M from a page's `deferred_by` when the superseding Case names the page on any of its decision lines, a `defer` included; its caller passes the slugs of every target of the record. So a `defer` that carries the mark removes the old wording, and the new judgment counts `defer` lines in the same way. `backlog.py` counts an item by every `[-]` line that names its slug (`put_off_count`, through `generate.frontier_marks`), so the new closer adds to the count as `kept` does.
>
> One judgment: a Grep for `decided_on_its_page` over `.guppi` printed `.guppi/guppi/casecheck.py` and `.guppi/guppi/prespec.py`. The check of the answer of `case-guppi` in `casecheck.py` imports it and counts lines other than a `defer`. So Case 937.1 adds a keyword to that one function and adds no second copy, as `rule-one-judgment-one-implementation` sets it. The keyword is false by default, so `check_backlog_line` keeps its answer. No test reads that function over a live file. The finding of `/pre-spec` on `estimate-case-check-requires-a-backlog-item-decided-on-its-page` showed that `check_backlog` of `casecheck.py`, which I read whole with `open_backlog_lines`, judges only a Case that names the page on a line other than a `defer` (`missing if named else []`). So a Case that only defers the page again without the mark would get no finding when `case-guppi` stops, only at `/pre-spec` after ratification, which is the shape of the failure of session 1713. The person agreed that `check_backlog` calls the same mode, so Case 937.3 replaces the Criterion of that Estimate. Its test `test_backlog_a_case_naming_the_page_only_in_a_defer_line_is_not_judged` of `.guppi/tests/test_casecheck.py` asserts the old answer, so 937.3 changes it. The `method` of that Estimate also asked for a reading by hand of the first answer of `case-guppi` on an item taken from the backlog, an event this session may not see. So 937.3 sets the `method` to the test alone, as the fix the person agreed to says. Its `purpose` still holds. The finding of `/pre-spec` on the slugs of a title showed two functions that read them. `deferred_pages` of `prespec.py` reads every code span after the item id and trims spaces inside the backticks. `frontier_marks` of `.guppi/guppi/generate.py` reads only the text before the first ` · ` and keeps such spaces. They part on a code span after the first ` · ` and on one with spaces inside its backticks. The person chose that one function in `generate.py` takes the title before the first ` · ` with spaces trimmed, and that each site imports it. A third finding of `/pre-spec` was left with no change to this Case: a backlog line closed `defer case N` by a Case of a conserved Spec in a session of `/box` is a finding before this Case and after it, and it goes to the handoff as a line. A Grep for `orchestration\.md|skills/hi/SKILL|skills" / "hi` over `.guppi/tests` printed `test_lint.py`, `test_ratified.py`, `test_onward.py`, `test_ship.py`, `test_guard.py`, `test_prespec.py`, `test_recall.py` and `test_orchestration.py`. `test_orchestration.py` reads the live `orchestration.md`, but only its blocks tagged `showing` and `defer`, which this Case leaves as they are. `test_recall.py` writes its skill under a temporary folder. `test_ship.py` runs `test_the_live_code_holds_no_pointer_outside_a_bracket` over the live code of `.guppi/`. So the new docstrings and comments of 937.1 keep each pointer to a Case in a bracket at the end of its sentence.
>
> A Grep for `backlog · kept|· defer case N|defer case N`` over `.claude/` and `vault/wiki/` printed 17 files. These are `.claude/skills/sprint-close/SKILL.md`, `.claude/skills/hi/SKILL.md`, `vault/wiki/orchestration.md`, `vault/wiki/log.md`, the lesson above, `rule-case-protocol`, `rule-orchestration`, `rule-skill-hi`, `rule-skill-sprint-close`, `estimate-orchestration-shows-the-built-case`, `estimate-prespec-checks-the-frontier`, `estimate-hi-writes-frontier`, `estimate-orchestration-takes-back-a-ratified-case`, `estimate-hi-takes-a-conserved-spec`, `estimate-orchestration-shows-the-frontier-after-a-closed-line`, `estimate-orchestration-defers-in-one-reply` and `estimate-orchestration-acknowledging-reply`. The Criterion of `estimate-prespec-checks-the-frontier` says that `defer case N` after `backlog` is a finding, so Case 937.1 replaces it. Its `purpose` and `method` still hold. `orchestration.md` and the skill of `rule-skill-hi` list the closers, so Case 937.2 adds the new closer to each. The other hits stand. The sprint-close skill closes a backlog item left at the close of a sprint as `kept`, which stays true. In `rule-case-protocol` the hit is a History line. The Estimates of the acknowledging reply, the built Case, the Frontier after a closed line and the conserved Spec list `[-] … · defer case N`, a form that the new closer keeps. `estimate-orchestration-takes-back-a-ratified-case` keeps `kept` for a take-back, as the person chose. `estimate-orchestration-defers-in-one-reply` covers sources other than the sprint and the backlog by its `When`. `estimate-hi-writes-frontier` stays as it is: each of its lines stays true. It already waits, unread, for the session that opens a sprint, and a replaced Criterion with a `method` that waits for a later session is a finding of `/pre-spec`. `estimate-prespec-requires-a-backlog-item-decided-on-its-page` stands: its Criterion speaks only of lines closed `[x] … · backlog · case N`, and its two findings do not fire on a `[-]` line. The `/pre-spec` sentence of `case-schema.md` on a Case that takes up a backlog item stands, since it speaks of that Case alone. The row `Plan Mode` of `glossary.md` names a backlog item kept as it stands, which stays true.
>
> The brief reports `uv run --project .guppi guppi test` at the close of session 1713 as "1814 passed, 6 skipped, 1 deselected, exit 0". It reports no output of `guppi prespec --check`. The options of the rounds rest on the code I read, not on a run. The check runs at `/pre-spec` of this session with the code as it stands then. No line of this session's Frontier closes `· backlog · defer case N`, so the old code finds nothing new. The session's ledger holds no `lesson[error]` line, and the lesson above is of session 1713, so no line carries `{addresses:...}`.

> **problem:**
> No closer fits a backlog item that a Case of the session defers again with a new wording. The agent takes `[x] … · backlog · case N`, which the check reads as a Case that takes the item off the backlog, or `kept`, which says that no Case stands.

> **recommend:**
> - **Which closer a backlog item takes when a Case defers it again**
>   - Recommended: (a) `[-] … · backlog · defer case N`, with the check changed to accept it.
>   - Answer: agreed, (a).
> - **What the check asks of the Case that the closer names**
>   - Recommended: (a) a `defer` of a page that the title names, and the mark `{supersedes:case M}` for each Case M of that page's `deferred_by`.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) two sub-cases. One replaces the Criterion of `estimate-prespec-checks-the-frontier`, which a test run reads. The other creates an Estimate on `rule-orchestration`, read at Retro against the new text in the Spec. `estimate-hi-writes-frontier` stays as it is.
>   - Answer: agreed, (a).
> - **Which closer a backlog item takes after a take-back**
>   - Recommended: (a) the take-back keeps `kept`.
>   - Answer: (a).
> - **Which slugs of a Frontier line the shared function takes**
>   - Recommended: (a) the title only, the text before the first ` · `, with spaces trimmed inside the backticks.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec`: the new check of 937.1 reads the slugs of a title by no shared function, while `deferred_pages` and `frontier_marks` already read them.
>   - Taken: 937.1 adds one function in `.guppi/guppi/generate.py` that takes the slugs of a title, and `frontier_marks`, `deferred_pages` and the new check import it.
> - **Change**
>   - Asked: a finding of `/pre-spec`, which the person agreed to fix: `check_backlog` of `.guppi/guppi/casecheck.py` calls the same `defer` mode, and the Criterion of `estimate-case-check-requires-a-backlog-item-decided-on-its-page` is replaced and read by a test.
>   - Taken: the new sub-case 937.3.

### Case 937.1 — The pre-Spec check accepts a backlog item that a Case defers again

> **given:**
> `.guppi/guppi/prespec.py`: the Frontier check `check_frontier` and the shared judgment `decided_on_its_page`.
> **＋** `.guppi/guppi/generate.py`: the one function that takes the slugs of the title of a Frontier line, which `frontier_marks` calls.
> **＋** `.guppi/tests/test_prespec.py`: the tests of the Frontier check and of the slugs of a title.
> **＋** `.guppi/tests/test_ship.py`: its test of pointers in the live code reads the new docstrings.
> **＋** `estimate-prespec-checks-the-frontier`: its Criterion is replaced whole.
> **＋** `vault/raw/<date>/<HHMM>/frontier.md`: the Frontier the check reads.
> **＋** `vault/raw/<date>/<HHMM>/spec.md`: the conserved Spec that the title line of the plan may name.
> **＋** `rule-one-judgment-one-implementation`: the two checks share one judgment of a page decided by a Case.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<HHMM>/frontier.md`, and the title line of `<plan>` may name the `vault/raw/<date>/<HHMM>/spec.md` of a folder that holds `carry.md`.
> **＋** The check reads the decision lines of the session's window and the pages of the vault.

> **then:**
> A missing file is the finding `frontier: <path> is missing`.
> **＋** An open line under `## Cases` is a finding. An open line under `## Work` or `## Ask` is not.
> **＋** A closed line whose last segment after ` · ` is none of `case N`, `work`, `defer`, `kept` and `defer case N` is a finding.
> **＋** These pairings of box and closer are findings: `[x]` with `defer`, `kept` or `defer case N`, and `[-]` with `case N` or `work`.
> **＋** `defer` is clean only after the source segment `sprint`, the segment before the closer. `kept` is clean only after the source `backlog`. After any other source, each one is a finding.
> **＋** `defer case N` after the source `sprint` is a finding. After the source `backlog`, it is a finding when no `defer` line of Case N or of its sub-cases names a slug that the title, the text before the first ` · `, names in a code span. It is also a finding for each Case M of the `deferred_by` of such a page when no Case among Case N and its sub-cases both names the page on a `defer` line and carries `{supersedes:case M}`.
> **＋** After another source, `defer case N` is a finding when there is no `defer` item under Case N in the plan, and none under Case N of the `spec.md` that the title line of the plan names.
> **＋** A line closed `case N` is a finding when the plan has no heading of Case N.
> **－** A title line that names no folder holding `carry.md` adds no Case: `defer case N` after a source other than `sprint` or `backlog` is then judged against the plan alone.
> **－** A line that is not a box line, such as `Backlog: N items` or an indented `- near` line, is not read. No line of another session's Frontier file is read.

```then
update:
- slug: estimate-prespec-checks-the-frontier
  set:
    status: pending
  change: the Criterion replaced whole — a backlog item that a Case defers again closes defer case N, checked against the defer lines of that Case and the marks of each Case of the page's deferred_by
```

```tasks
- [x] `.guppi/guppi/prespec.py`: `decided_on_its_page` takes a keyword `by_defer`, false by default. With it, only the `defer` lines of Case N and its sub-cases name the page. Without it, every line but a `defer` names the page, as today. `check_backlog_line` keeps its call as it stands.
- [x] `.guppi/guppi/generate.py`: one new function takes the slugs of the title of a Frontier line, from the text after the item id. It reads the code spans by `CODE_SPAN` in the text before the first ` · ` and trims each one of its backticks and of the spaces inside them. `frontier_marks` calls it, and so does `deferred_pages` of `.guppi/guppi/prespec.py`, which no longer reads a code span after the first ` · `.
- [x] `.guppi/guppi/prespec.py`: in `check_frontier`, a line closed `[-] … · backlog · defer case N` goes to a new function beside `check_backlog_line`. That function calls `decided_on_its_page` with `by_defer` for each slug that the new function of `generate.py` takes from the title, and for each page of `deferred_pages`, and gives the two findings of the Criterion, each naming the Frontier line, the page and, for a missing mark, `{supersedes:case M}`. The finding that an item is deferred by a Case stays for the source `sprint` alone. The module docstring and the docstring of `check_frontier` say this. Each pointer to a Case in a new docstring or comment stands in a bracket at the end of its sentence, as `test_the_live_code_holds_no_pointer_outside_a_bracket` of `.guppi/tests/test_ship.py` reads the live code.
- [x] `.guppi/tests/test_prespec.py`: `test_defer_case_n_after_sprint_or_backlog_is_a_finding` keeps the source `sprint` alone. New tests: a backlog line closed `defer case N` whose Case defers the page with the mark of each Case of its `deferred_by` is clean; one whose Case has no `defer` line that names a slug of the title is a finding; one whose `defer` lacks a mark is a finding that names the mark; and `decided_on_its_page` over one set of lines counts a `defer` line as naming the page only with `by_defer`. One more test runs `frontier_marks` and `deferred_pages` over the same lines, one with a code span after the first ` · ` and one with spaces inside its backticks, and asserts that they take the same slugs.
- [ ] update `estimate-prespec-checks-the-frontier`
- [ ] read `estimate-prespec-checks-the-frontier`
```

### Case 937.2 — The main agent closes a backlog item deferred again by that Case

> **given:**
> `rule-orchestration`: its Render names the new closer under `## Plan Mode and the Frontier`.
> **＋** `rule-skill-hi`: its Render names the new closer in the list of closers.
> **＋** `vault/wiki/orchestration.md`: rendered from `rule-orchestration`.
> **＋** `.claude/skills/hi/SKILL.md`: rendered from `rule-skill-hi`.
> **＋** `vault/wiki/backlog.md`: the backlog whose item a Case defers again.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose line closes.
> **＋** `estimate-orchestration-closes-a-backlog-item-deferred-again`: the new check of the closer.
> **＋** `estimate-prespec-checks-the-frontier`: the check of 937.1, which sets what the Case named in the closer must hold.

> **when:**
> In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and `.claude/skills/hi/SKILL.md` from `rule-skill-hi`, a Case of the session defers again, with a new wording, an item of `vault/wiki/backlog.md` that stands on a line of `raw/<date>/<hi HHMM>/frontier.md` with the source `backlog`.

> **then:**
> The agent closes the line of the item `[-] … · backlog · defer case N`, N the id of that Case, in the reply that carries the decision lines of the Case.
> **＋** The agent takes this closer only for a Case whose decision lines meet the backlog rule of `estimate-prespec-checks-the-frontier`, so that the check that Estimate reads finds nothing on the line.
> **＋** An item of `vault/wiki/backlog.md` left as it stands, with no Case, closes `[-] … · backlog · kept`, and so does one whose ratified Case the person takes back in Plan Mode.
> **－** The line of an item that a Case defers again does not close `[x] … · backlog · case N`, which stays for a Case that takes the item off the backlog.

```then
create:
- slug: estimate-orchestration-closes-a-backlog-item-deferred-again
  ref: rule-orchestration
  kind: QA
  purpose: Whether the line of a backlog item that a Case of the session defers again with a new wording closes [-] … · backlog · defer case N, while an item left as it stands or whose Case is taken back closes [-] … · backlog · kept
  method: 'by hand at Retro of the session that changes it: the new Render of rule-orchestration and of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
update:
- slug: rule-orchestration
  replace:
  - old: '`[-] … · backlog · kept` for an item of `backlog.md` left as it stands, and `[-] … · defer case N` for a decision of any other source put off (case 451.1).'
    new: '`[-] … · backlog · kept` for an item of `backlog.md` left as it stands, and `[-] … · defer case N` for a decision of any other source put off (case 451.1). An item of `backlog.md` that a Case defers again with a new wording closes `[-] … · backlog · defer case N`: a `defer` line of Case N names its page and carries `{supersedes:case M}` for each Case M of the page''s `deferred_by`, so that `generate` drops the old defer from that list, and `/pre-spec` reports the line otherwise (as set in case 937.2).'
  change: 'the Frontier closer of a backlog item that a Case defers again with a new wording: [-] … · backlog · defer case N'
- slug: rule-skill-hi
  replace:
  - old: '`[-] … · backlog · kept` when an item of `backlog.md` is left as it stands — no Case, no ledger line, but for the short Case of a take-back that `orchestration.md` sets, it stays in the backlog (case 723.3);'
    new: '`[-] … · backlog · kept` when an item of `backlog.md` is left as it stands — no Case, no ledger line, but for the short Case of a take-back that `orchestration.md` sets, it stays in the backlog (case 723.3); `[-] … · backlog · defer case N` when Case N defers an item of `backlog.md` again with a new wording, its `defer` line naming the page with `{supersedes:case M}` for each Case M of the page''s `deferred_by` (as set in case 937.2);'
  change: the closer [-] … · backlog · defer case N for a backlog item that a Case defers again
```

```tasks
- [ ] update `rule-orchestration`
- [ ] update `rule-skill-hi`
- [ ] create `estimate-orchestration-closes-a-backlog-item-deferred-again`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [ ] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-orchestration-closes-a-backlog-item-deferred-again`
```

### Case 937.3 — The check of a case file asks the same of a Case that defers a backlog item again

> **given:**
> `.guppi/guppi/casecheck.py`: `check_backlog`, the check of the file of `case-guppi` against the open backlog lines.
> **＋** `.guppi/guppi/prespec.py`: `decided_on_its_page`, the judgment that `check_backlog` imports.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of that check.
> **＋** `estimate-case-check-requires-a-backlog-item-decided-on-its-page`: its Criterion is replaced whole.
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose open lines the check reads.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of `case-guppi` that the check reads.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of that file, the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, and the pages of the vault.

> **then:**
> For each open line of the Frontier whose source is `backlog`, each page that its title names in a code span and that carries `deferred_by` is checked against each top-level Case N of the file that, itself or through a sub-case, names that page on a decision line other than a `defer`.
> **＋** Case N gets a finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases in the file both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and the missing mark. The hook exits 2, and `case-guppi` fixes the file.
> **＋** A top-level Case of the file that puts the item off again, naming that page only on `defer` lines, is checked too: it gets the same finding for each Decision M of the `deferred_by` that none of those lines marks with `{supersedes:case M}`.
> **＋** The judgment is the function of `.guppi/guppi/prespec.py` that the pre-spec check runs, imported, not copied.
> **－** A Case of the file that names no such page, a file while no open line of the source `backlog` stands, and a page without `deferred_by` get no finding of this check.

```then
update:
- slug: estimate-case-check-requires-a-backlog-item-decided-on-its-page
  set:
    status: pending
    method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k backlog
  change: the Criterion replaced whole — a Case that names the page of an open backlog line only on defer lines needs the mark of each Case of its deferred_by too; the method is the test alone
```

```tasks
- [x] `.guppi/guppi/casecheck.py`: `check_backlog` judges a top-level Case that names the page only on `defer` lines by `decided_on_its_page` with `by_defer`, and gives the same finding for each missing mark. The docstring of the module and of `check_backlog` say this, each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/tests/test_casecheck.py`: `test_backlog_a_case_naming_the_page_only_in_a_defer_line_is_not_judged` changes. A `defer` of the page without `{supersedes:case M}` gets the finding, and one with the mark of each Case of the page's `deferred_by` gets none.
- [ ] update `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
- [ ] read `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
```

## Case 938 — The dispatch names a Case that set the form of a text a check reads

> **context:**
> When the main agent dispatches `case-guppi` for an item, it names the related Cases of the session, and `case-guppi` reads no other Case of the session. Today `## Who builds a Case` of `rule-orchestration` counts a Case as related when it changes a page the item names or sets what happens at the same moment, such as a reply, a hook event or a command. A Case of another subject that sets the form of a text one check reads falls outside that test. In session 1713, Case 927 reworded the `method` of `estimate-harness-make-runs-in-both-shells` so that `guppi check` no longer read a word as a target of the `Makefile`. Case 929 was then dispatched with Case 927 named as not related, and wrote the same kind of wording into the `method` of another Estimate. `/pre-spec` found it, as `lesson-orchestration-dispatch-named-a-case-of-the-same-wording-not-related` records. The person chose to add one kind of related Case: a Case that sets the form of a text a check reads, or how the check reads it, when the Case of the item may write text of that kind.
>
> The Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch` speaks of this test, and its first `－` line says that a Case outside the old test need not stand in the prompt, which the change makes false. So this Case replaces its Criterion whole. That line is not carried word for word: in the new Criterion it also leaves out a Case that sets no form of a text of a kind the Case of the item may write. Every other line of the old Criterion is carried as it stands. Its `purpose` states the old test and its `method` names a reading of session 2249, so both are set anew. The new `method` waits for the first dispatch under the new Render in which such a Case stands. `insight-case-build-sibling-texts-unchecked-before-the-showing` is about sibling Cases on one subject built apart, which the main agent had named related, so it stands. Case 937.2 also updates `rule-orchestration`, but under `## Plan Mode and the Frontier`. This Case changes one clause under `## Who builds a Case`, and the two texts do not speak of the same thing.
>
> A Grep for `related` over `vault/wiki/` with `log.md` left out printed 13 files: `brief.md`, `orchestration.md`, `lessons/schema.yaml`, the lesson above, `rule-case-protocol`, `rule-synthesis`, `rule-case-build`, `rule-orchestration`, `estimate-orchestration-passes-a-change-to-an-item-not-built`, `rule-lessons-schema`, `estimate-case-build-checks-the-finished-case`, `estimate-case-build-reads-by-need-and-in-parts` and `estimate-orchestration-names-related-cases-in-the-dispatch`. The same Grep over `.claude/` printed `.claude/agents/case-guppi.md`. `rule-case-build` and its render `case-guppi.md` say only that the main agent judges which Cases are related, which stays true. `estimate-orchestration-passes-a-change-to-an-item-not-built` names a Case that wrote a line `**Other Case:**` as a related Case, which stays true. The hits in `rule-case-protocol` and `estimate-case-build-checks-the-finished-case` are History lines. `estimate-case-build-reads-by-need-and-in-parts` speaks of reading the case files of related Cases, which stays true. In `rule-synthesis`, `rule-lessons-schema` and `lessons/schema.yaml` the word is `unrelated` or `related lessons`, which this Case does not touch. A Grep for `orchestration\.md|rule-orchestration` over `.guppi/tests` printed `test_onward.py` and `test_orchestration.py`. `test_orchestration.py` reads only the blocks tagged `showing` and `defer` of the live `orchestration.md`, which this Case leaves as they are. `test_onward.py` only names `orchestration.md` in the text of a hook. The new text carries no pointer to a Case, since `rule-orchestration` has `core: true` and the clause stands inside a long sentence. The session's ledger holds no `lesson[error]` line. The lesson above is of session 1713, so no line carries `{addresses:...}`.

> **problem:**
> The test of related Cases leaves out a Case that set the form of a text a check reads. So a later Case that writes text of that kind is built without it, and it can bring back the form that the earlier Case fixed.

> **recommend:**
> - **Which Cases the test of related Cases adds**
>   - Recommended: (b) a Case that sets the form of a text a check reads, or how the check reads it, when the item's Case may write text of that kind.
>   - Answer: agreed, (b).
> - **How the change is checked**
>   - Recommended: (a) replace the Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch`, with its `purpose` and `method` set anew.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: its Render sets the test of related Cases under `## Who builds a Case`.
> **＋** `vault/wiki/orchestration.md`: rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-names-related-cases-in-the-dispatch`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose item the dispatch names.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the case file of a related Case.

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of an item of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** The prompt also names each Case of the session, ratified or already shown, that sets the form of a text a check reads, or how the check reads it, when the Case of the item may write text of that kind, such as the `method` of an Estimate.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** When the item is one of two or more items that one answer of the person took up, the prompt also names each other Case of that batch by its id and its Frontier item, and by the path of its case file where that file stands.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names, acts at another moment, sets no form of a text of a kind the Case of the item may write and is no Case of the same batch need not stand in the prompt.
> **－** A Case that only writes a text a check reads, and sets no form of it, is not related by that text alone.
> **－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

```then
update:
- slug: rule-orchestration
  replace:
  - old: that changes a page the item names or sets what happens at the same moment, such as a reply, a hook event or a command, by its id,
    new: that changes a page the item names, sets what happens at the same moment, such as a reply, a hook event or a command, or sets the form of a text that a check reads, or how the check reads it, where the Case of the item may write text of that kind, such as the `method` of an Estimate that `uv run --project .guppi guppi check` reads, by its id,
  change: a Case that sets the form of a text a check reads, or how the check reads it, is related to an item whose Case may write text of that kind
- slug: estimate-orchestration-names-related-cases-in-the-dispatch
  set:
    status: pending
    purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names, acts at the same moment, or sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind, by its id, one sentence on what it sets and the path of its case file, and each other Case of a batch of items the person took up in one answer
    method: 'by hand, after the first dispatch of case-guppi under the new Render of rule-orchestration in which a Case of the session sets the form of a text a check reads and the Case of the item may write text of that kind: the Agent call of that dispatch in its transcript, read against the Criterion; a related Case left unnamed counted in the reading line'
  change: the Criterion replaced whole — a Case that sets the form of a text a check reads is related to an item whose Case may write text of that kind; purpose and method set anew
```

```tasks
- [ ] update `rule-orchestration`
- [ ] update `estimate-orchestration-names-related-cases-in-the-dispatch`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-names-related-cases-in-the-dispatch`
```

## Case 939 — The reading of the clean pages passes --allow-draft

> **context:**
> `estimate-clean-branch-pages-hold-pointers-only-in-brackets` checks that the pages with `core: true`, the `schema.yaml` of each category and the files of `.claude/` that such pages render hold each pointer to a case in a bracket of its own. Its `method` and the `When` of its Criterion build the clean copy by `uv run --project .guppi guppi ship --review` into an empty folder. In `run` of `.guppi/guppi/ship.py`, a build into a folder first calls `drafts`, which lists each page that `is_draft_core` accepts. When that list is not empty and `--allow-draft` is not passed, `run` prints the list and returns 1 before it calls `version` or `ship`. With `--allow-draft` it prints the list, which sets no exit code, then calls `version`, which returns 1 with nothing written when no tag `prod-x.y.z` stands in the history of HEAD, and then `ship`, which writes the copy and gives the lines. I read `run`, `drafts`, `version`, `ship`, `settled`, `judged` and `check` of `.guppi/guppi/ship.py` whole for these claims. The brief reports the last `guppi check` (`## Flags` of `vault/wiki/brief.md`): "13 lines, exit 1 — 13 pages with `core: true` stand `draft`". It also reports that `git tag --merged HEAD` prints `prod-0.2.0`. So the reading as written gives the draft list and no line on the brackets. Case 928 fixed the same gap in the Estimate of the code by `--check`, which judges no file under `vault/`, and left this Estimate as it stood; the handoff of session 1713 carried it on.
>
> The person chose to pass `--allow-draft` in the `When` and the `method`, and to read at Retro of this session. The rule that governs the change is the form of a promise in `case-schema.md`: a part inside a Criterion is refused, and a promise changes only by a Criterion replaced whole. So the Case replaces the Criterion whole and sets the Estimate `pending`. The new `When` names the flag, the tag and Retro. The old `When` line is not carried, since the command it names writes nothing while a draft page with `core: true` stands. The `Then` lines stand as they were, and one new `－` line says that the lines on draft pages set no exit code and are no part of this promise. The new `method` names the flag and holds no pointer, since the copy takes this Estimate once it is `passed`. The `purpose` speaks of what `guppi ship --review` prints and of the brackets it removes, which the new command still does, so it stands.
>
> `rule-clean-branch` gives `--allow-draft` one purpose: it writes the copy for an install by hand from that folder, which is where a check that needs an install reads it. A finding of `/pre-spec` named that sentence, and the person chose that this Case replaces it so that it names both uses: the install by hand and the reading of the pages by `--review`. The pair adds no behaviour of the code. `estimate-clean-branch-refuses-a-draft-core-page`, an Estimate of `rule-clean-branch`, already checks what the flag does: its Criterion says that with `--allow-draft` the build writes the copy and prints the draft lines, which set no exit code. Its Criterion names no purpose of the flag, so it stands. A Grep of `allow-draft` over `vault/wiki/estimates/` with the glob `estimate-clean-branch-*.md` printed `estimate-clean-branch-ships-neutral-texts.md`, `estimate-clean-branch-installs-as-a-plugin.md`, `estimate-clean-branch-writes-the-session-files.md`, `estimate-clean-branch-refuses-a-draft-core-page.md` and `estimate-clean-branch-ships-the-tests.md`. The methods of `estimate-clean-branch-ships-neutral-texts` and `estimate-clean-branch-ships-the-tests` also pass the flag for a reading with no install. By the person's answer, the new sentence names the two uses the finding named, so these other readings are not named in it. A Grep of `install by hand` over `.guppi/`, `.claude/`, `.github/` and `plugin/` printed `.guppi/guppi/ship.py`: line 26 of its module docstring and line 631, the help of `--allow-draft`. Both name the install, and neither says that the flag serves only that. This Case changes no code, so both stand. A Grep of `ship --review` over `vault/wiki/` printed `vault/wiki/brief.md`, `vault/wiki/rules/rule-clean-branch.md`, `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`, `vault/wiki/estimates/estimate-clean-branch-refuses-a-draft-core-page.md` and `vault/wiki/estimates/estimate-clean-branch-pages-hold-pointers-only-in-brackets.md`; over `.claude/` it printed nothing. The two other Estimates set what the folder build does, and this Case changes no code, so they stand; the rule's hits say what `--review` lists, which stays true; the `brief.md` hit is not read. A Grep of `pages-hold-pointers-only-in-brackets` over `.guppi/tests/` printed nothing, so no test reads this page live. I read the finished files of Cases 937, 942 and 943 of this session whole. Case 943 writes a clean copy by `guppi ship --allow-draft` in Work Mode for the install by hand, which is the first use of the new sentence, into a folder of its own, so it shares no folder with this reading. Case 942 changes docstrings under `.guppi/guppi/`, which are outside this promise. It drops a section from core pages, and Case 937 changes core pages, but both changes land at the librarian's run, after Retro, so this reading at Retro judges the pages before those changes. None of them changes `rule-clean-branch` or this Estimate, so this Case needs no change against them. The ledger of this session holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> The reading of the pages that ship, as its `method` and its Criterion write it, exits 1 and writes nothing while any page with `core: true` stands `draft`.

> **recommend:**
> - **How the reading of the pages runs while a core page stands draft**
>   - Recommended: (a) add `--allow-draft` and replace the Criterion whole.
>   - Answer: agreed, (a).
> - **When the new reading is taken**
>   - Recommended: (a) at Retro of this session.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec`, which the person agreed to: the sentence of `rule-clean-branch` that gives `--allow-draft` the install by hand as its one use should name both uses, the install by hand and the reading of the pages by `--review`.
>   - Taken: an `update` of `rule-clean-branch` replaces that sentence, and `estimate-clean-branch-refuses-a-draft-core-page` is named as the check of the flag.

> **given:**
> `estimate-clean-branch-pages-hold-pointers-only-in-brackets`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/ship.py`: the command `guppi ship`, whose `--allow-draft` and `--review` the reading runs.
> **＋** `vault/wiki/` and `.claude/`: the pages and the harness files the reading judges.
> **＋** `rule-clean-branch`: sets the clean version and the option `--allow-draft`; its sentence on the uses of that option is replaced.
> **＋** `estimate-clean-branch-refuses-a-draft-core-page`: checks what `--allow-draft` does.
> **＋** `rule-retro`: sets Retro.

> **when:**
> At Retro of the session, `uv run --project .guppi guppi ship --allow-draft --review <folder>` of `.guppi/guppi/ship.py`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder, with a tag `prod-x.y.z` in the history of HEAD.

> **then:**
> It prints no line on a pointer outside a bracket of its own in a page under `vault/wiki/` with `core: true`, in the `schema.yaml` of a category or in a file of `.claude/` that such a page renders.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as the history of this repository that a pointer names, when a thing was measured or which session a pointer names.
> **＋** No bracket that `--review` lists on those files holds the definition of a term that its sentence needs, or the slug of a page with `core: true` by which its sentence names the rule that sets what it says.
> **－** Each page under `vault/wiki/` keeps every pointer it held, with the words that go with it, in a bracket, and each sentence keeps its meaning in this repository.
> **－** A line on a page with `core: true` that stands `draft` sets no exit code and is no part of this promise.
> **－** A line on a file under `.guppi/guppi/` is no part of this promise.

```then
update:
- slug: estimate-clean-branch-pages-hold-pointers-only-in-brackets
  set:
    status: pending
    method: 'by hand, at Retro: the lines of uv run --project .guppi guppi ship --allow-draft --review into an empty temporary folder on vault/wiki/ and .claude/, read against the Criterion'
  change: 'the Criterion replaced whole — the reading passes --allow-draft, so no draft page with core: true stops it'
- slug: rule-clean-branch
  replace:
  - old: for an install by hand from that folder, which is where a check that needs an install reads it, and the workflow never passes that option
    new: for an install by hand from that folder, which is where a check that needs an install reads it, and for the reading of the pages that the clean version holds by `--review`, and the workflow never passes that option
  change: --allow-draft also serves the reading of the pages by --review
```

```tasks
- [ ] update `estimate-clean-branch-pages-hold-pointers-only-in-brackets`
- [ ] update `rule-clean-branch`
- [ ] read `estimate-clean-branch-pages-hold-pointers-only-in-brackets`
```

## Case 942 — The Leaf rules lose How it works, its facts in their code

> **context:**
> A Rule page of one rule, a Leaf, still carries the section `## How it works` on eleven pages. The schema of Rule pages keeps that section for a MOC, a workflow page, and puts the mechanism of a Leaf in the docstring of its code or in its Render; it lets a Leaf keep the section until its next touch. The section can drift from the code it describes: the one of `rule-retro-commit` restates when `guppi gate` blocks the `handoff` skill, which `.guppi/guppi/gate.py` decides. Earlier Cases moved such facts into the docstring and removed the section by hand, such as cases 589.2, 632.1 and 904.1. Session 1713 added `drop`, the key of an `update` that removes a section with its heading (cases 931, 935). The person chose to remove the section from all eleven Leaf pages now. Each fact it holds moves first into the docstring of the code that the page's `implementation_ref` names, and for `rule-internal-context`, which has no code, into its `## Purpose`, written as the failure each line of its list prevents, as the schema defines a Purpose. A remark on what stood before some Case leaves with the section, since the History of each page and its Decision pages keep it. Case 942 replaces Case 940, which has decision lines in the session's ledger and is built again in two parts after `/pre-spec`. The change of the schema can fail alone while every docstring holds its facts, and its fix is another, so the person chose two sub-cases. Case 942.1 removes the sections, checked by a new Estimate. Case 942.2 rewords the schema, checked by `estimate-rules-schema-checked`, whose Criterion it replaces.
>
> A Grep `^## How it works` over `vault/wiki/rules/` printed 15 files: `rule-skill-hi`, `rule-git-context`, `rule-documentation`, `rule-spec-write`, `rule-raw-archive`, `rule-event-log`, `rule-page-read`, `rule-tests-clock-pinned`, `rule-claude-md`, `rule-retro-commit`, `rule-ledger-tail`, `rule-governed-files-hook`, `rule-compact-recall`, `rule-internal-context` and `rule-session-start`. A Grep `^kind: MOC` over those 15 files printed 4: `rule-skill-hi`, `rule-documentation`, `rule-claude-md` and `rule-session-start`. These keep the section, as the schema allows. The other eleven are Leaves, and each carries `core: true`, so each pointer to a Case in new text stands in a bracket at the end of its sentence. `estimate-clean-branch-code-holds-pointers-only-in-brackets` and `estimate-clean-branch-tests-judge-the-live-code`, both `passed`, already promise that for the comments and docstrings under `.guppi/guppi/` and `.guppi/tests/`, the new docstrings among them, so this Case adds no promise of its own on pointers. Case 937 of this session updates `rule-skill-hi`, a MOC, and no page of this Case. I read `drop` of `.guppi/guppi/generate.py` whole. It removes each named section with its heading. It fails the item when the page lacks the section, or when the removal adds a schema finding, and `## How it works` is optional on a Rule page. I also read `replace_hits` of the same module, which joins the words of an `old` by any whitespace. So the pairs of `rule-rules-schema` below match across the line breaks and the indent of its examples. Its Render holds the examples as one section.
>
> A Grep `How it works` over `vault/wiki/`, without `log.md` and `brief.md`, printed 39 files. Besides the 15 pages above, the hits that are no History line are these. In `rule-rules-schema` and `vault/wiki/rules/schema.yaml`, the description of the section and the three examples of a Leaf that still carry it enter Case 942.2 by four pairs. `rule-entities-schema`, `vault/wiki/entities/schema.yaml`, `glossary.md`, `entity-glossary.md` and `estimate-entities-schema-checked` speak of the section of an Entity, which this Case does not touch. The Criterion of `estimate-rules-schema-checked` lists `## How it works` as optional, which stays true; Case 942.2 replaces it whole with that line kept and one line added. Its `purpose` and `method` stand: the purpose speaks of findings on a page, and the method reads the live file against the Criterion after a librarian's run. `estimate-generate-writes` and `estimate-materialize-assembles` hold it in a Result line, a record. A Grep `How it works` over `.claude/` printed nothing, so no harness file changes. A Grep `How it works|docstring` over the Estimates of the eleven pages printed nothing. Their Criteria speak of behaviour that this Case leaves as it is, so none of them changes.
>
> A Grep `schema\.yaml` over `.guppi/tests/` printed 10 files: `test_generate.py`, `test_materialize.py`, `test_ratified.py`, `test_ship.py`, `test_case_schema.py`, `test_casecheck.py`, `test_prespec.py`, `test_lint.py`, `test_schemas.py` and `test_orchestration.py`. `test_schemas.py` reads the live `vault/wiki/rules/schema.yaml` for its lists and conditions alone. `test_generate.py`, `test_materialize.py`, `test_case_schema.py` and `test_orchestration.py` copy the live schema files into a temporary folder, and their tests rest on the lists, which this Case leaves as they are. The rest write their schema under a temporary folder. `test_the_live_code_holds_no_pointer_outside_a_bracket` of `test_ship.py` reads the live code of `.guppi/`, the new docstrings among it. The brief reports `uv run --project .guppi guppi check` at the close of session 1713 as 13 lines, exit 1, each a page with `core: true` that stands `draft`, none a schema finding; this Case sets no status of a Rule page. The session's ledger holds no `lesson[error]` line, so no line carries `{addresses:...}`.

> **problem:**
> Eleven Leaf rules describe their mechanism in a section that the schema keeps for a MOC, beside the code that decides it, so the two texts can part.

> **recommend:**
> - **Which Leaf rules lose the section, and where its facts go**
>   - Recommended: (a) all eleven now, each fact the docstring of the page's code lacks moved into it first, a rendered Leaf with no code taking it into its Purpose or its Render, then a `drop`.
>   - Answer: (a).
> - **How the removal is checked**
>   - Recommended: (a) a new Estimate on `rule-rules-schema`, read by hand at Retro against the Spec and after the librarian's run by a search, and the schema sentence reworded.
>   - Answer: agreed, (a).
> - **Where the facts of `rule-internal-context` go**
>   - Recommended: (a) into its `## Purpose`.
>   - Answer: agreed, (a).
> - **Whether remarks on what stood before a Case move too**
>   - Recommended: (b) they are left out; the History of each page and its Decision pages keep them.
>   - Answer: agreed, (b).
> - **One Case for all eleven pages, or one part per page**
>   - Recommended: (a) one Case, one Estimate.
>   - Answer: (a).
> - **Change**
>   - Asked: `/pre-spec` found that the change of the schema can fail alone while every docstring holds its facts, and the person agreed to two sub-cases: one for the eleven pages, checked by the new Estimate, and one for the schema, checked by `estimate-rules-schema-checked` with its Criterion replaced.
>   - Taken: the Case is built again as Case 942 in two sub-cases, under a new number, since Case 940 has decision lines.
> - **Change**
>   - Asked: `/pre-spec` found that the new Purpose of `rule-internal-context` describes what the page does, not the failure the rule prevents.
>   - Taken: the same facts stand in the Purpose, each written as the failure that a line of the list prevents.
> - **Change**
>   - Asked: `/pre-spec` found that the line of `then` on pointers in brackets repeats the promise of two Estimates of `rule-clean-branch`.
>   - Taken: the line is left out, and `context` names those two Estimates.

### Case 942.1 — The Leaf pages lose How it works, its facts in their code

> **given:**
> `vault/wiki/rules/`: the Rule pages, MOC and Leaf.
> **＋** `rule-rules-schema`: the target of the new check.
> **＋** `estimate-rules-schema-leaf-carries-no-how-it-works`: the new check.
> **＋** `rule-tests-clock-pinned`: a Leaf whose section leaves.
> **＋** `.guppi/tests/conftest.py`: the code of `rule-tests-clock-pinned`.
> **＋** `rule-spec-write`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/ratified.py`: the code of `rule-spec-write`.
> **＋** `rule-compact-recall`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/recall.py`: the code of `rule-compact-recall`.
> **＋** `rule-event-log`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/event.py`: the code of `rule-event-log`.
> **＋** `rule-retro-commit`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/gate.py`: the code of `rule-retro-commit`, and of the marks of `rule-event-log`.
> **＋** `rule-raw-archive`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/archive.py`: the code of `rule-raw-archive`.
> **＋** `rule-git-context`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/gitstate.py`: the code of `rule-git-context`.
> **＋** `rule-ledger-tail`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/tail.py`: the code of `rule-ledger-tail`.
> **＋** `rule-page-read`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/pageread.py`: the code of `rule-page-read`.
> **＋** `rule-governed-files-hook`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/guard.py`: the code of `rule-governed-files-hook`.
> **＋** `rule-internal-context`: a Leaf with no code, whose section leaves for its Purpose.
> **＋** `.guppi/tests/test_ship.py`: its test of pointers reads the live code.

> **when:**
> After Work Mode writes the new docstrings and the librarian's run applies the updates of the session, an agent reads a Leaf page of `vault/wiki/rules/` and the docstring of its code.

> **then:**
> No Leaf page of `vault/wiki/rules/` carries a section `## How it works`.
> **＋** Each fact that such a section held stands in the docstring of the code that the page's `implementation_ref` names, and for `rule-internal-context` in its `## Purpose`, as the failure that a line of its list prevents.
> **－** A remark on what stood before some Case does not move into the docstrings or the Purpose.
> **－** A MOC page of `vault/wiki/rules/` keeps its `## How it works`.

```then
create:
- slug: estimate-rules-schema-leaf-carries-no-how-it-works
  ref: rule-rules-schema
  kind: QA
  purpose: Whether no Leaf page of vault/wiki/rules/ carries How it works, each fact it held standing in the docstring of its code or, for rule-internal-context, in its Purpose
  method: 'by hand at Retro of the session that changes it: each new docstring and the new Purpose of rule-internal-context read against the How it works it takes, recorded in the estimate line; by hand, after the librarian''s run of that session: a Grep for ^## How it works over vault/wiki/rules/ and the kind of each page it prints, no Leaf among them'
  tags:
  - harness
  - schema
update:
- slug: rule-tests-clock-pinned
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstring of .guppi/tests/conftest.py'
- slug: rule-spec-write
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/ratified.py'
- slug: rule-compact-recall
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/recall.py'
- slug: rule-event-log
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstrings of .guppi/guppi/event.py and .guppi/guppi/gate.py'
- slug: rule-retro-commit
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/gate.py'
- slug: rule-raw-archive
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/archive.py'
- slug: rule-git-context
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/gitstate.py'
- slug: rule-ledger-tail
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/tail.py'
- slug: rule-page-read
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/pageread.py'
- slug: rule-governed-files-hook
  drop:
  - How it works
  change: '## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/guard.py'
- slug: rule-internal-context
  sections:
    Purpose: Prevents work starting without the current sprint and the previous session's handover. Both are vault files, both fail the same way — missing file or wrong path — so they are one rule rather than two. Were `orchestration.md` and `ratification.md` imported by `CLAUDE.md` rather than listed here, a session without `/hi` would carry their text too (as set in case 595). Were `case-schema.md` listed, every working session would carry the form of a Case that only `case-guppi` needs, and that agent reads it itself (as set in case 595). Were `glossary.md` in the `@` import of `CLAUDE.md` rather than here, every subagent would load it, and none of them needs it (as set in case 288.1). A category schema on this list would load text that a session needs only when it writes a page of that category, and it is read then. A file left off this list is missing after a compaction too, since `guppi recall` prints back the paths of these lines (as set in case 287). Without `where-to-stop.md` after `orchestration.md`, Plan Mode, which plans with the person the run from the approved Spec to the librarian, would not hold the conditions on which that run stops for the person, and the main agent could promise the person a turn inside it (as set in case 689.1).
  drop:
  - How it works
  change: '## How it works left the Leaf, its reasons in the Purpose as the failures each line of the list prevents'
```

```tasks
- [x] `.guppi/tests/conftest.py`: its module docstring takes each fact of the `## How it works` of `rule-tests-clock-pinned` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/guppi/ratified.py`: its module docstring takes each fact of the `## How it works` of `rule-spec-write` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/guppi/recall.py`: its module docstring takes each fact of the `## How it works` of `rule-compact-recall` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/guppi/event.py`: its module docstring takes each fact of the `## How it works` of `rule-event-log` that it does not hold, but for a remark on what stood before some Case and for the marks that `guppi gate` writes; each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/guppi/gate.py`: its module docstring takes each fact of the `## How it works` of `rule-retro-commit`, and the facts of the `## How it works` of `rule-event-log` on the marks `prespec`, `retro` and `handoff`, that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/guppi/archive.py`: its module docstring takes each fact of the `## How it works` of `rule-raw-archive` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/guppi/gitstate.py`: its module docstring takes each fact of the `## How it works` of `rule-git-context` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/guppi/tail.py`: its module docstring takes each fact of the `## How it works` of `rule-ledger-tail` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/guppi/pageread.py`: its module docstring takes each fact of the `## How it works` of `rule-page-read` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
- [x] `.guppi/guppi/guard.py`: its module docstring takes each fact of the `## How it works` of `rule-governed-files-hook` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
- [x] `uv run --project .guppi guppi test`: exit 0, `test_the_live_code_holds_no_pointer_outside_a_bracket` of `.guppi/tests/test_ship.py` among the passed.
- [ ] update `rule-tests-clock-pinned`
- [ ] update `rule-spec-write`
- [ ] update `rule-compact-recall`
- [ ] update `rule-event-log`
- [ ] update `rule-retro-commit`
- [ ] update `rule-raw-archive`
- [ ] update `rule-git-context`
- [ ] update `rule-ledger-tail`
- [ ] update `rule-page-read`
- [ ] update `rule-governed-files-hook`
- [ ] update `rule-internal-context`
- [ ] create `estimate-rules-schema-leaf-carries-no-how-it-works`
- [ ] read `estimate-rules-schema-leaf-carries-no-how-it-works`
```

### Case 942.2 — The rule schema says a Leaf carries no How it works

> **given:**
> `rule-rules-schema`: its Render describes the section and holds the examples.
> **＋** `vault/wiki/rules/schema.yaml`: rendered from `rule-rules-schema`.
> **＋** `vault/wiki/rules/`: the Rule pages that lint reads.
> **＋** `.guppi/guppi/render.py`: `guppi render`, which writes the file.
> **＋** `.guppi/guppi/lint.py`: `guppi lint`, which reads it.
> **＋** `estimate-rules-schema-checked`: its Criterion is replaced whole.

> **when:**
> `guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`, and `guppi lint` reads a page of `vault/wiki/rules/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`, `core: true`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional.
> **＋** The file also holds `ordered_children: true`, which lint does not read.
> **＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
> **＋** A Rule page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, Ordering, MOCs and enforcement, Enforcement, the sentence on the edge Rule → Entity, the one on the guard of the agent's own conduct and the one on the Estimates that a shipped page brings along; `examples` holds the example pages.
> **＋** That last sentence says that a shipped page arrives with each of its Estimates that passed in the repository it came from and whose `method` names no target of the `Makefile`, and that the receiving project writes its other Estimates through its own Cases.
> **＋** The description of `## How it works` under `sections` says that the section is for a MOC alone and that a Leaf carries none, and no example of a Leaf under `examples` carries the section.

```then
update:
- slug: rule-rules-schema
  replace:
  - old: 'optional. MOC only: why the steps are in this order, and what breaks if they are reordered. On a Leaf the promise lives in its Estimates and the mechanism in the docstring of its code, or in its Render; a Leaf that still carries the section keeps it until its next touch, when the section leaves (cases 193, 200.2).'
    new: 'optional. MOC only: why the steps are in this order, and what breaks if they are reordered. A Leaf carries none: its promise lives in its Estimates and its mechanism in the docstring of its code, or in its Render (as set in cases 193, 200.2 and 942.2).'
  - old: 'one rule rather than two. ## How it works `case-schema.md` is listed here (since case 273); the glossary arrives through `@import` in `CLAUDE.md`, the category schemas are read when a page of their category is written, and re-reading either would duplicate context that is already present.'
    new: one rule rather than two.
  - old: 'workspace resolves would silently land outside the session. ## How it works PreToolUse, matched on writes to `ledger.md`. Reads the readiness flag written when the workspace was resolved; exits 2 and blocks the write if it is missing.'
    new: workspace resolves would silently land outside the session.
  - old: 'it produces a partially applied price. ## How it works A lint rule flags `async def` and `await` under `src/pricing/`. Runs in CI, so the violation surfaces at the change that introduces it rather than at the next incident.'
    new: it produces a partially applied price.
  change: a Leaf carries no How it works; the section leaves the three examples of a Leaf
- slug: estimate-rules-schema-checked
  set:
    status: pending
  change: the Criterion replaced whole — the description of How it works says a Leaf carries none, and no example of a Leaf carries it
```

```tasks
- [ ] update `rule-rules-schema`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/rules/schema.yaml`
- [ ] update `estimate-rules-schema-checked`
- [ ] read `estimate-rules-schema-checked`
```

## Case 943 — Work Mode stops for the install by hand into five projects, and the agent writes the copy in two checks

> **context:**
> Four Estimates wait on an install by hand from a clean copy: `estimate-plugin-install-sets-aside-the-files-of-the-project`, `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-plugin-install-runs-no-hook-before-uv-sync`, of `rule-plugin-install`, and `estimate-guppi-package-is-ready-after-the-install`, of `rule-guppi-package`. Each `method` writes the clean version by `uv run --project .guppi guppi ship --allow-draft`, adds it as a catalogue by `/plugin marketplace add`, installs it by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in a test project. The method of `estimate-guppi-package-is-ready-after-the-install` says that the person does this at a stop of Work Mode and that its copy and project may be those of `estimate-plugin-install-runs-no-hook-before-uv-sync`. Their event has come: the brief reports the librarian's run of session 1713 and that `git tag --merged HEAD` prints `prod-0.2.0`. The methods name five projects. The first is an empty project, for the copy, the hooks before `uv sync`, and the reopen and `/hi`. The second is an empty project with Claude Code started with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to an empty folder. The third holds a `CLAUDE.md`, a `.claude/settings.json` with a hook and a `.gitattributes` of its own. The fourth is such a project, offline. The fifth holds a file of its own under `vault/`. `where-to-stop.md` lets Work Mode stop for the person only on its conditions, and the fourth condition is a task of the Spec whose text opens with `stop:`.
>
> I read `run`, `drafts` and `version` of `.guppi/guppi/ship.py` whole. A build into a folder that is not empty writes nothing. With `--allow-draft`, the lines on the draft pages with `core: true` are printed and set no exit code, and the copy is written when a tag `prod-x.y.z` stands in the history of HEAD. The person chose to take all four readings in this session, with the copy written by the agent, one stop, and the readings after the person's word. The Claude Code page https://code.claude.com/docs/en/plugin-marketplaces says that one user cannot have two marketplaces with the same name, and that `claude plugin marketplace remove <name>` removes the marketplace and uninstalls its plugins. So the steps first remove a `guppi-marketplace` left by an earlier install.
>
> This Case replaces Case 941, which was ratified with the stop alone and the four Criteria kept. A finding of `/pre-spec` showed that two Criteria say that the person writes the copy, while the agent writes it. In `estimate-plugin-install-writes-guppi-into-an-empty-project` this is a `＋` line of its When, and in `estimate-guppi-package-is-ready-after-the-install` it is its When; the `method` of the second already says that the agent writes it. The person chose to replace both Criteria whole, with the agent as the one who writes the copy and the rest as it stands, and to build Case 941 again under a new number with sub-cases. The rule that governs this is the form of a promise in `case-schema.md`: a promise changes only by a Criterion replaced whole. So Cases 943.2 and 943.3 replace each Criterion whole and set each Estimate `pending`. Each `method` waited for the librarian's run of the session that sets its Criterion; once this session sets it, that wait would move past this session. So each `method` is set anew, with the reading at Retro of this session, as the person chose. Each `purpose` speaks of what the install does, not of who writes the copy, so it stands. `.claude/skills/work/SKILL.md` leaves to Retro the reading of an Estimate that this session creates or updates. So these two are read at Retro, against the Spec that holds their new Criteria. The two other Estimates are still read in Work Mode after the last task. Case 943.1 names the two rules by an `update` with only `change`. I read `names_a_part` and `lift_criterion` of `.guppi/guppi/materialize.py`: an `update` of a rule is no Estimate entry, so nothing is lifted and no status is set.
>
> `estimate-where-to-stop-stops-only-on-its-conditions` stands `passed`. It already promises that the agent stops before a task that opens with `stop:` and runs it after the person's word, so its Criterion stands. The Criteria of `estimate-plugin-install-sets-aside-the-files-of-the-project` and `estimate-plugin-install-runs-no-hook-before-uv-sync` do not say who writes the copy, so they stand. `estimate-sprint-plugin-installs-as-a-plugin` also reads an install into an empty project with `/hi`. Its target is the live sprint page, and `.claude/skills/hi/SKILL.md` makes such an Estimate wait for the Retro of the session that finishes the work of the sprint. Item C1 of the clean branch is still open, so that Estimate stays out. I read the finished file of Case 939 whole. It runs `guppi ship --allow-draft --review` at Retro into an empty temporary folder of its own, so the two builds share no folder. It also replaces the sentence of `rule-clean-branch` on the uses of `--allow-draft`, and its new sentence still names the install by hand from that folder, which is what this Case does. This Case names `rule-clean-branch` only as the rule of the clean version and changes none of its text, so the two Cases need no change against each other. The ledger of this session holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> Four install readings are due, and each needs the person to install by hand. No task of the Spec makes Work Mode stop for that, so without one the run goes on to Retro and the readings go to the handoff unread. Two of their Criteria also say that the person writes the clean copy, while the agent writes it.

> **recommend:**
> - **Which pages does the Case name?**
>   - Recommended: (a) the two rules the checks belong to, by an `update` with only `change`.
>   - Answer: agreed, (a).
> - **Who makes the five test projects?**
>   - Recommended: (a) the agent, before the stop.
>   - Answer: agreed, (a).
> - **Which check closes the Case?**
>   - Recommended: (a) the four install checks, their wording kept.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec` — two Criteria say that the person writes the clean copy; the person agreed that the Case replaces both whole, with the agent as the one who writes it, and that Retro reads both against the Spec.
>   - Taken: Cases 943.2 and 943.3 replace those Criteria whole and set each `method` anew for Retro.
> - **Where do the two rewritten checks go?**
>   - Recommended: (a) Case 941 built again under a new number, with sub-cases.
>   - Answer: agreed, (a).

### Case 943.1 — Work Mode stops for the install by hand into five projects

> **given:**
> `rule-plugin-install`: the install the readings check; an `update` with only `change`.
> **＋** `rule-guppi-package`: the rule of the Python environment after the install; an `update` with only `change`.
> **＋** `.guppi/guppi/ship.py`: `guppi ship --allow-draft`, which writes the clean version.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install` that the person types.
> **＋** `rule-where-to-stop`: sets the stop before a task that opens with `stop:`.
> **＋** `.claude/skills/work/SKILL.md`: takes the readings after the last task.
> **＋** `estimate-guppi-package-is-ready-after-the-install`: the reading by the person's answer.

> **when:**
> In Work Mode of the session, the agent writes the clean version by `uv run --project .guppi guppi ship --allow-draft <folder>` of `.guppi/guppi/ship.py` into a new empty folder outside the repository, makes the five test projects outside the repository, and reaches the `stop:` task of this Case.

> **then:**
> Before the stop, each test project holds only the files that its method names, and the agent records what each holds.
> **＋** The agent stops as `rule-where-to-stop` sets it, and its reply gives the person the steps for each project: the folder, how to start Claude Code there, offline where the method says so, the commands of the catalogue, the install and `/guppi:install`, and what to run after.
> **＋** Where a catalogue `guppi-marketplace` already stands from an earlier install, the first step removes it by `claude plugin marketplace remove guppi-marketplace`.
> **＋** The reply puts the question of `estimate-guppi-package-is-ready-after-the-install` on the first empty project, after the person reopens Claude Code there and opens a working session.
> **＋** After the person's word, the run goes on, and the readings that `.claude/skills/work/SKILL.md` sets read the transcripts and the files of the projects against the Criteria of the Estimates of `rule-plugin-install` and `rule-guppi-package`.
> **－** The agent adds no catalogue, installs no plugin and types no `/guppi:install` itself, and deletes no folder outside the repository.
> **－** No text of `rule-plugin-install` or `rule-guppi-package` changes.

```then
update:
- slug: rule-plugin-install
  change: the install by hand of its readings taken at a stop of Work Mode of session 2005
- slug: rule-guppi-package
  change: the install by hand of its reading taken at a stop of Work Mode of session 2005
```

```tasks
- [ ] update `rule-plugin-install`
- [ ] update `rule-guppi-package`
- [x] `uv run --project .guppi guppi ship --allow-draft <folder>` into a new empty folder outside the repository.
- [x] The five test projects made outside the repository, the files of each as its method names them, and what each holds recorded.
- [x] stop: in Work Mode, the person installs the clean copy into the five projects by the steps the agent gives, and answers the question of `estimate-guppi-package-is-ready-after-the-install`.
```

### Case 943.2 — The check of the copy into an empty project names the agent as the one who writes the copy

> **given:**
> `estimate-plugin-install-writes-guppi-into-an-empty-project`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/ship.py`: `uv run --project .guppi guppi ship --allow-draft <folder>` and `uv run --project .guppi guppi ship --check`.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install`, which `guppi ship` writes to `skills/install/SKILL.md` of the clean version.
> **＋** `rule-plugin-install`: sets the install, which leaves out the files of the plugin under `.claude-plugin/`, `skills/` and `.git/`.
> **＋** `vault/`: the vault of the project, whose pages under `vault/wiki/` the install copies.
> **＋** `.claude/settings.json` and `.claude/skills/`: the settings and the skills of the harness that the install copies.
> **＋** `rule-clean-branch`: sets the clean version.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands of Claude Code that add the catalogue and install the plugin.
> **＋** `/hi`: the command that the last message of the install names.

> **when:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
> **＋** The agent writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`; the person adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in the project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
> **＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
> **＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
> **＋** In a project that holds none of the files it would write, `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/`, such as `CLAUDE.md`, `.claude/settings.json`, the code under `.guppi/` and the pages under `vault/wiki/`.
> **＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
> **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
> **－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
> **－** Which files a new project needs, what the install does about `uv` and the Python environment under `.guppi/`, and what it does with a file of the project that stands at one of its paths are no part of this promise.

```then
update:
- slug: estimate-plugin-install-writes-guppi-into-an-empty-project
  set:
    status: pending
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, at Retro of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written by the agent in Work Mode into a local folder by uv run --project .guppi guppi ship --allow-draft; at a stop of Work Mode, in an empty project, the person adds that folder as a catalogue by /plugin marketplace add, installs guppi by /plugin install guppi@guppi-marketplace and types /guppi:install; the files of the project read against those of the plugin and against the Criterion'
  change: the Criterion replaced whole — the agent writes the clean copy; the reading at Retro of the session that sets it
```

```tasks
- [ ] update `estimate-plugin-install-writes-guppi-into-an-empty-project`
- [ ] read `estimate-plugin-install-writes-guppi-into-an-empty-project`
```

### Case 943.3 — The check of the package after the install names the agent as the one who writes the copy

> **given:**
> `estimate-guppi-package-is-ready-after-the-install`: its Criterion is replaced whole and its `method` set anew.
> **＋** `rule-guppi-package`: the rule of the Python environment `.guppi/.venv/`.
> **＋** `.guppi/guppi/ship.py`: `uv run --project .guppi guppi ship --allow-draft <folder>`, which writes the clean version.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install`, which runs `uv --version` and `uv sync --project .guppi`.
> **＋** `rule-plugin-install`: sets the install.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands of Claude Code that add the catalogue and install the plugin.
> **＋** `.claude/settings.json`: the file that holds the hooks of the project.
> **＋** `/hi`: the command that the install sends the person to.

> **when:**
> In the repository of GUPPI, the agent writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`; the person adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> Before it writes anything, `/guppi:install` runs `uv --version`.
> **＋** It copies each file of the install but `.claude/settings.json`, and then runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/`.
> **＋** Once `uv sync` passes, it copies `.claude/settings.json`, and then tells the person to reopen Claude Code and type `/hi`.
> **＋** The hooks of the project find that environment built at the first `/hi`.
> **－** Where `uv --version` passes, it asks nothing about `uv`.

```then
update:
- slug: estimate-guppi-package-is-ready-after-the-install
  set:
    status: pending
    method: 'by hand, at Retro of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: in the repository of GUPPI, the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft in Work Mode; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person''s answer on the output of the install, the order of its steps, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of the reading of estimate-plugin-install-runs-no-hook-before-uv-sync'
  change: the Criterion replaced whole — the agent writes the clean copy; the reading at Retro of the session that sets it
```

```tasks
- [ ] update `estimate-guppi-package-is-ready-after-the-install`
- [ ] read `estimate-guppi-package-is-ready-after-the-install`
```

## Deferred

## Case 936 — The reading of the refusal of ask-guppi put off

> **context:**
> At the /hi of session 2005 the person put off the reading of `estimate-search-leaves-out-decisions-refuses-ask-guppi`. At the `/pre-spec` of session 1713, `ask-guppi` made no Read and no Grep on `vault/wiki/decisions/`, so no refusal of the hook could be read. The frame of `ask-guppi` names no reason to make such a call, so this session may not see one either.

> **problem:**
> No session has yet seen a call of `ask-guppi` on `vault/wiki/decisions/` that the hook could refuse, so no Case of this session can take the reading.

```then
defer:
  - slug: estimate-search-leaves-out-decisions-refuses-ask-guppi
    type: estimate
    purpose: "Whether the PreToolUse hook grepguard refuses a Read of a Decision page and a Grep inside vault/wiki/decisions/ made by ask-guppi; its reading waits for such a call, which no /pre-spec has made yet"
```
