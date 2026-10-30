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

> **tasks:**
> - [ ] `.guppi/guppi/prespec.py`: `decided_on_its_page` takes a keyword `by_defer`, false by default. With it, only the `defer` lines of Case N and its sub-cases name the page. Without it, every line but a `defer` names the page, as today. `check_backlog_line` keeps its call as it stands.
> - [ ] `.guppi/guppi/generate.py`: one new function takes the slugs of the title of a Frontier line, from the text after the item id. It reads the code spans by `CODE_SPAN` in the text before the first ` · ` and trims each one of its backticks and of the spaces inside them. `frontier_marks` calls it, and so does `deferred_pages` of `.guppi/guppi/prespec.py`, which no longer reads a code span after the first ` · `.
> - [ ] `.guppi/guppi/prespec.py`: in `check_frontier`, a line closed `[-] … · backlog · defer case N` goes to a new function beside `check_backlog_line`. That function calls `decided_on_its_page` with `by_defer` for each slug that the new function of `generate.py` takes from the title, and for each page of `deferred_pages`, and gives the two findings of the Criterion, each naming the Frontier line, the page and, for a missing mark, `{supersedes:case M}`. The finding that an item is deferred by a Case stays for the source `sprint` alone. The module docstring and the docstring of `check_frontier` say this. Each pointer to a Case in a new docstring or comment stands in a bracket at the end of its sentence, as `test_the_live_code_holds_no_pointer_outside_a_bracket` of `.guppi/tests/test_ship.py` reads the live code.
> - [ ] `.guppi/tests/test_prespec.py`: `test_defer_case_n_after_sprint_or_backlog_is_a_finding` keeps the source `sprint` alone. New tests: a backlog line closed `defer case N` whose Case defers the page with the mark of each Case of its `deferred_by` is clean; one whose Case has no `defer` line that names a slug of the title is a finding; one whose `defer` lacks a mark is a finding that names the mark; and `decided_on_its_page` over one set of lines counts a `defer` line as naming the page only with `by_defer`. One more test runs `frontier_marks` and `deferred_pages` over the same lines, one with a code span after the first ` · ` and one with spaces inside its backticks, and asserts that they take the same slugs.
> - [ ] update `estimate-prespec-checks-the-frontier`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a backlog item that a Case defers again closes defer case N, checked against the defer lines of that Case and the marks of each Case of the page's deferred_by`
> - [ ] read `estimate-prespec-checks-the-frontier`

> **ratification:**
> ```
> - decision[case 937.1][update][estimate-prespec-checks-the-frontier]{ref:rule-prespec}
> ```

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

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` `[-] … · backlog · kept` for an item of `backlog.md` left as it stands, and `[-] … · defer case N` for a decision of any other source put off (case 451.1). ``
>   - new: `` `[-] … · backlog · kept` for an item of `backlog.md` left as it stands, and `[-] … · defer case N` for a decision of any other source put off (case 451.1). An item of `backlog.md` that a Case defers again with a new wording closes `[-] … · backlog · defer case N`: a `defer` line of Case N names its page and carries `{supersedes:case M}` for each Case M of the page's `deferred_by`, so that `generate` drops the old defer from that list, and `/pre-spec` reports the line otherwise (as set in case 937.2). ``
>   - change: `the Frontier closer of a backlog item that a Case defers again with a new wording: [-] … · backlog · defer case N`
> - [ ] update `rule-skill-hi`
>   - old: `` `[-] … · backlog · kept` when an item of `backlog.md` is left as it stands — no Case, no ledger line, but for the short Case of a take-back that `orchestration.md` sets, it stays in the backlog (case 723.3); ``
>   - new: `` `[-] … · backlog · kept` when an item of `backlog.md` is left as it stands — no Case, no ledger line, but for the short Case of a take-back that `orchestration.md` sets, it stays in the backlog (case 723.3); `[-] … · backlog · defer case N` when Case N defers an item of `backlog.md` again with a new wording, its `defer` line naming the page with `{supersedes:case M}` for each Case M of the page's `deferred_by` (as set in case 937.2); ``
>   - change: `the closer [-] … · backlog · defer case N for a backlog item that a Case defers again`
> - [ ] create `estimate-orchestration-closes-a-backlog-item-deferred-again`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the line of a backlog item that a Case of the session defers again with a new wording closes [-] … · backlog · defer case N, while an item left as it stands or whose Case is taken back closes [-] … · backlog · kept`
>   - method: `by hand at Retro of the session that changes it: the new Render of rule-orchestration and of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow]`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-orchestration-closes-a-backlog-item-deferred-again`

> **ratification:**
> ```
> - decision[case 937.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 937.2][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 937.2][create][estimate-orchestration-closes-a-backlog-item-deferred-again]{ref:rule-orchestration}{tags:session,workflow}
> ```

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

> **tasks:**
> - [ ] `.guppi/guppi/casecheck.py`: `check_backlog` judges a top-level Case that names the page only on `defer` lines by `decided_on_its_page` with `by_defer`, and gives the same finding for each missing mark. The docstring of the module and of `check_backlog` say this, each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/tests/test_casecheck.py`: `test_backlog_a_case_naming_the_page_only_in_a_defer_line_is_not_judged` changes. A `defer` of the page without `{supersedes:case M}` gets the finding, and one with the mark of each Case of the page's `deferred_by` gets none.
> - [ ] update `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
>   - set:
>     ```
>     {status: pending, method: "uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k backlog"}
>     ```
>   - change: `the Criterion replaced whole — a Case that names the page of an open backlog line only on defer lines needs the mark of each Case of its deferred_by too; the method is the test alone`
> - [ ] read `estimate-case-check-requires-a-backlog-item-decided-on-its-page`

> **ratification:**
> ```
> - decision[case 937.3][update][estimate-case-check-requires-a-backlog-item-decided-on-its-page]{ref:rule-case-check}
> ```
