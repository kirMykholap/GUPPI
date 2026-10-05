## Case 637 — Seven checks that wait for a rare live event get readings that can be taken at any time

> **context:**
> Seven Estimates are `pending` because the second half of each method waits for a live event that seldom comes. Five of them check the `SubagentStop` hook `uv run guppi casecheck --subagent` of `rule-case-check`. Four of these five wait for a live answer of `case-guppi` that the hook sends back for that one reason. The fifth, `estimate-case-check-sends-back-a-clash-with-another-case`, also waits for the main agent's question to the person after a clash and its `SendMessage` on a yes. In session 2041 the hook sent `case-guppi` back for other reasons only, so none of these readings came. `estimate-lint-runs-every-step` waits for a Baseline whose backlog step is red. No session has had one, and case 631 put off the question of a method that stages one. `estimate-session-start-context` waits for a session opened without `/hi` whose reply carries a `LEDGER` block, and no such session followed the `/hi` of 2041. While they stay `pending`, the closing Case of the sprint `migration` must read each one or name it by `--carry` or `--archive-unread` (case 628.2).
>
> The test half of each case-check method exists: `tests/test_casecheck.py` holds the tests that `-k lone`, `-k rounds`, `-k subagent_clash`, `-k shape` and `-k session_clash` select. The tests call `casecheck.run` with the payload of `SubagentStop`. The live half adds only the registration in `.claude/settings.json` and a real answer, and `estimate-case-check-sends-back-a-faulty-case` read both live on 2026-10-04. `estimate-case-check-refuses-a-letter-outside-the-script` and `estimate-case-check-refuses-a-problem-in-a-sub-case` are already read by pytest alone. So the four plain case-check Estimates keep their Criteria, with methods of pytest alone (637.1).
>
> The Criterion of the clash Estimate is replaced whole without two lines (637.2). One is the trigger line on the main agent getting the answer that passed. The other is the line on what `case-guppi` and the main agent do when another Case should change instead. The hook sends a note on each of the two lines, and both are dropped on purpose, as chosen in the round. Its `purpose`, which names that step, and its `method` are set anew. The main agent's half of the step stays as text in `vault/wiki/orchestration.md`. The other half, where `case-guppi` changes its own Case and names the other one in `context`, stood in no live page. A Grep of `should change|bounded around` over the repository, leaving out `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/`, printed `vault/wiki/orchestration.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-orchestration-asks-in-the-grill-me-shape.md` and `vault/wiki/estimates/estimate-case-check-sends-back-a-clash-with-another-case.md`. A Grep of `clash` over `.claude/agents/case-guppi.md` printed nothing. So 637.2 adds that half to the Render of `rule-case-build`, after the sentence on findings the hook sends back. As chosen at pre-spec, it has no check of its own, like the main agent's half. The Criterion of the clash Estimate is therefore written under `sections.Criterion`, so the `case-guppi` line of the `then` of 637.2 stays out of it. Of the Estimates of `rule-case-build`, `estimate-case-build-writes-the-case` covers the moment the hook sends findings back, but its Criterion speaks of the form of the answer again, not of what the Case changes, so it stands. Case 636 replaces another sentence of `rule-case-build`, the one on a claim of `context` about a search, and sets the step just before an answer with a Case. The new sentence sits in a later paragraph and covers an answer again after a clash finding, so the two texts do not meet.
>
> A Grep of `clash` over `vault/wiki/estimates/` printed `estimate-case-build-checks-the-finished-case.md`, `estimate-prespec-reconciles.md`, `estimate-orchestration-asks-in-the-grill-me-shape.md`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent.md` and `estimate-case-check-sends-back-a-clash-with-another-case.md`. `estimate-orchestration-asks-in-the-grill-me-shape` checks only the shape of the main agent's question after a clash, so the send on a yes has no check of its own. The first two are about pre-spec and the checks of `case-guppi`, and the fourth names only its own `-k subagent_clash`. All three stand.
>
> No test runs `make lint` now. New tests in `tests/test_lint.py` run the real target of the `Makefile` with a fake `uv` first on the search path, once with a red backlog step and once with every step green (637.3). The Criterion of `estimate-lint-runs-every-step` names who runs `make lint`, and that list has no test. So the Criterion is replaced whole: it gets one trigger line for each test run, and every other line is carried word for word. Its `purpose` stands. The sub-case takes up the defer of case 631. `estimate-harness-pipeline` (`passed`) asks that `make test-harness` be green and that the steps of `make lint` before `guppi lint` exit 0 on the committed tree. The new tests join `make test-harness` and must pass there. They run the steps in a temp folder with a fake `uv`, never on the committed tree, so its Criterion stands.
>
> `rule-session-start` is a MOC, so the method of `estimate-session-start-context` must be a `make` target, and `make test-session-start` alone meets that (637.4). Its refusal path is held in `tests/test_ledger.py`. Both live readings passed on 2026-09-09, but on the old Criterion. Case 485.1 replaced that Criterion whole on 2026-09-28, and the page has stood `pending` since. The new Criterion only moved the ledger into the session folder, and this session's ledger is written to `raw/2026-10-04/2245/ledger.md`, so the make target alone stands as chosen.
>
> A Grep of the seven slugs over `vault/wiki/` printed 29 files. Outside `decisions/` these were `brief.md`, `log.md`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent.md`, `rule-case-check.md`, `rule-lint.md`, `estimate-case-build-records-the-rounds-in-recommend.md`, `rule-session-start.md` and `insight-workflow-contract-change-leaves-its-derived-text-stale.md`. The other 21 files are Decision pages, which state their own moment. Each hit read stays true: the rules list the Estimates, the promise of `estimate-case-check-requires-each-question-of-the-rounds` stands, and the Insight names an old Criterion. The new methods land at the librarian's run, so each Estimate is read at the next session by its new method (case 428.1). 637.1 and 637.4 set no Estimate `pending` and are checked by those readings. 637.2 and 637.3 carry a read line.

> **problem:**
> Seven Estimates cannot close while their methods wait for live events that may not come before the sprint closes. Each needs a reading that can be taken at any time, or a promise cut to what such a reading checks.

> **recommend:**
> - **How should the five checks of the answer hook be read?**
>   - Recommended: (a) pytest alone; the live hook setup counts as proven by the check that passed live; the main agent's part of the clash check is settled in a later round.
>   - Answer: agreed with the recommendation, (a).
> - **How should the check that make lint runs every step be read?**
>   - Recommended: (a) a new pytest runs the real `make lint` with a fake `uv` first on the search path that fails the backlog step, and asserts that all five steps ran in order and that the exit code is non-zero; the put-off question is taken up.
>   - Answer: agreed with the recommendation, (a).
> - **How should the check of a session opened without /hi be read?**
>   - Recommended: (a) the method keeps only `make test-session-start`.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to the part of the clash check that reads the main agent?**
>   - Recommended: (a) the promise of the clash check is rewritten whole without the main agent's part and its trigger line; the main agent's step stays as text in `orchestration.md` with no check of its own.
>   - Answer: agreed with the recommendation, (a).
> - **How should this Case be split?**
>   - Recommended: (a) four sub-cases: the four answer-hook checks whose method becomes pytest alone, the clash check, the `make lint` check with its new test, and the session-start check.
>   - Answer: agreed with the recommendation, (a).
> - **Change**
>   - Asked: at pre-spec, the half of the dropped Criterion line on what `case-guppi` does after a clash stood in no live page, agent file or code; the person chose to add it to `rule-case-build` in 637.2, with no check of its own.
>   - Taken: 637.2 replaces the sentence of `rule-case-build` on findings sent back with that sentence and the new one, and renders `.claude/agents/case-guppi.md` again; the Criterion of the clash Estimate is written under `sections.Criterion`, so the new line stays out of it.

### Case 637.1 — Four checks of the answer hook are read by pytest alone

> **given:**
> `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` — its `method` set anew; its Criterion stands
> **＋** `estimate-case-check-requires-each-question-of-the-rounds` — its `method` set anew; its Criterion stands
> **＋** `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — its `method` set anew; its Criterion stands
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — its `method` set anew; its Criterion stands
> **＋** `tests/test_casecheck.py` — the tests the methods select
> **＋** `rule-case-check` — the rule of the hook these Estimates check
> **＋** `rule-estimates-schema` — the forms of a `method`

> **when:**
> Someone takes the reading of `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent` or `estimate-case-check-sends-back-a-ratified-case-in-another-shape` by its method.

> **then:**
> The method is a run of pytest over `tests/test_casecheck.py` with the selector of that Estimate, and the reading can be taken at any time.
> **－** No live answer of `case-guppi` that the hook sends back is part of the reading.
> **－** The Criterion and the status of each of these Estimates stand.

> **tasks:**
> - [ ] update `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`
>   - set: `{method: "uv run pytest tests/test_casecheck.py -k lone"}`
>   - change: `the method is pytest alone; the live send-back is no longer waited for (case 637.1)`
> - [ ] update `estimate-case-check-requires-each-question-of-the-rounds`
>   - set: `{method: "pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, a round out of form whose titles are not required, an answer with no round, and an answer of sub-cases alone whose titles stand in the recommend of its stored parent"}`
>   - change: `the method is pytest alone; the live send-back is no longer waited for (case 637.1)`
> - [ ] update `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
>   - set: `{method: "uv run pytest tests/test_casecheck.py -k subagent_clash"}`
>   - change: `the method is pytest alone; the live send-back is no longer waited for (case 637.1)`
> - [ ] update `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
>   - set: `{method: "uv run pytest tests/test_casecheck.py -k shape"}`
>   - change: `the method is pytest alone; the live send-back is no longer waited for (case 637.1)`

> **ratification:**
> ```
> - decision[case 637.1][update][estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent]{ref:rule-case-check}
> - decision[case 637.1][update][estimate-case-check-requires-each-question-of-the-rounds]{ref:rule-case-check}
> - decision[case 637.1][update][estimate-case-check-sends-back-a-case-number-held-by-another-agent]{ref:rule-case-check}
> - decision[case 637.1][update][estimate-case-check-sends-back-a-ratified-case-in-another-shape]{ref:rule-case-check}
> ```

### Case 637.2 — The clash check promises only what the hook does

> **given:**
> `estimate-case-check-sends-back-a-clash-with-another-case` — its Criterion replaced whole under `sections.Criterion`, its `purpose` and `method` set anew
> **＋** `guppi/casecheck.py` — the hook `uv run guppi casecheck --subagent`
> **＋** `guppi/prespec.py` — `check_same_target`, the judgment the hook imports
> **＋** `tests/test_casecheck.py` — the tests that `-k session_clash` selects
> **＋** `<plan>.checked.json` — the store of checked Cases beside the plan file
> **＋** `raw/<date>/<hi HHMM>/ledger.md` — the session's ledger the hook reads
> **＋** `rule-case-build` — the Render of `case-guppi`, which gains the step after a clash
> **＋** `.claude/agents/case-guppi.md` — the agent file rendered from `rule-case-build`

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
> **＋** Or `tests/test_casecheck.py` runs it over a made-up plan file, store and ledger.

> **then:**
> The hook judges the Cases of the answer together with the other Cases of the session by `check_same_target` of `guppi/prespec.py`, imported, not copied: each Case of the plan file, and each entry of `<plan>.checked.json` under its number alone whose id the plan file does not hold.
> **＋** A Case of the answer whose `update` of a page sets one field to another value than another Case, writes a section that another Case writes, or replaces whole the Criterion of an Estimate that another Case replaces whole, gets a finding that names both Cases, the page and the field or the section.
> **＋** The finding is stored with the Case, the hook exits 2, and `case-guppi` answers again before the main agent shows the Case.
> **＋** Where the other Case should change rather than its own, `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, still changes its own Case so that no finding stands, and its `context` names the other Case and the change it needs.
> **－** A stored Case that has findings, an entry joined with an agent id, and a Case whose number a `{supersedes:case N}` mark of the session's ledger names are not compared.
> **－** A Case whose id the answer holds is compared only as the answer holds it, and an answer that holds a top-level Case is compared with no part of that Case's family in the plan file or the store.
> **－** Two other Cases that clash with each other give this answer no finding.
> **－** The `Stop` hook `uv run guppi ratified` keeps its check of the Cases it writes, by the same function.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `A hook checks the answer before the main agent sees it; when it sends findings back, fix the Case and answer with it again.`
>   - new: `` A hook checks the answer before the main agent sees it; when it sends findings back, fix the Case and answer with it again. Where a finding is a clash with another Case of the session and that other Case should change rather than yours, still change your own Case so that no finding stands, and name in `context` the other Case and the change it needs; the main agent asks the person whether that Case is built again (case 637.2). ``
>   - change: `after a clash where the other Case should change, case-guppi still changes its own Case and names the other Case and its change in context (case 637.2)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-check-sends-back-a-clash-with-another-case`
>   - set: `{status: pending, purpose: "Whether the check of an answer of case-guppi sends back a Case that sets one field, writes one section or replaces one Criterion that another Case of the session, ratified or only stored, sets, writes or replaces too", method: "uv run pytest tests/test_casecheck.py -k session_clash"}`
>   - sections.Criterion:
>     ```
>     When:
>     `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
>     **＋** Or `tests/test_casecheck.py` runs it over a made-up plan file, store and ledger.
>
>     Then:
>     The hook judges the Cases of the answer together with the other Cases of the session by `check_same_target` of `guppi/prespec.py`, imported, not copied: each Case of the plan file, and each entry of `<plan>.checked.json` under its number alone whose id the plan file does not hold.
>     **＋** A Case of the answer whose `update` of a page sets one field to another value than another Case, writes a section that another Case writes, or replaces whole the Criterion of an Estimate that another Case replaces whole, gets a finding that names both Cases, the page and the field or the section.
>     **＋** The finding is stored with the Case, the hook exits 2, and `case-guppi` answers again before the main agent shows the Case.
>     **－** A stored Case that has findings, an entry joined with an agent id, and a Case whose number a `{supersedes:case N}` mark of the session's ledger names are not compared.
>     **－** A Case whose id the answer holds is compared only as the answer holds it, and an answer that holds a top-level Case is compared with no part of that Case's family in the plan file or the store.
>     **－** Two other Cases that clash with each other give this answer no finding.
>     **－** The `Stop` hook `uv run guppi ratified` keeps its check of the Cases it writes, by the same function.
>     ```
>   - change: `the Criterion replaced whole — the step of case-guppi and of the main agent after a clash is no longer part of the promise; the method is pytest alone (case 637.2)`
> - [ ] read `estimate-case-check-sends-back-a-clash-with-another-case`

> **ratification:**
> ```
> - decision[case 637.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 637.2][update][estimate-case-check-sends-back-a-clash-with-another-case]{ref:rule-case-check}
> ```

### Case 637.3 — A test runs make lint with a failing backlog step

> **given:**
> `estimate-lint-runs-every-step` — its Criterion replaced whole to name the tests, its `method` set anew
> **＋** `Makefile` — the recipe of `make lint`
> **＋** `tests/test_lint.py` — the new tests of the recipe
> **＋** `/work` — the skill whose Baseline runs `make lint`
> **＋** `.claude/agents/librarian-guppi.md` — the librarian's run, which runs `make lint`
> **＋** `rule-lint` — the rule that `make lint` runs every step
> **＋** `decision-case-631` — the defer of this method, taken up
> **＋** `estimate-harness-pipeline` — `make test-harness`, whose run the new tests join; its Criterion stands

> **when:**
> Someone runs `make lint` of the `Makefile`: by hand, in the Baseline of `/work`, or in the librarian's run of `.claude/agents/librarian-guppi.md`.
> **＋** Or `tests/test_lint.py` runs `make lint` of the `Makefile` in a temp folder, with a fake `uv` first on the search path that records each call and fails the step `guppi backlog --check`.
> **＋** Or `tests/test_lint.py` runs it the same way, with a fake `uv` that exits 0 for every step.

> **then:**
> `make lint` runs all five steps in the order `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint`, whether an earlier step exited 0 or not.
> **＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
> **＋** `make lint` exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
> **－** No step reads the stdin of its caller, and `make lint` writes nothing to the tree.

> **tasks:**
> - [ ] `tests/test_lint.py`: tests whose names hold `every_step` run `make lint` of the repository's `Makefile` in a temp folder with a fake `uv` first on the search path; the fake prints one line per call, records its arguments and whether its stdin was empty, and exits 1 for `guppi backlog --check` in one test and 0 for every step in another; they assert the five steps in order, each step's line in the output, a non-zero exit with the red step and 0 with none, an empty stdin for each step, and no new or changed file in the temp folder
> - [ ] update `estimate-lint-runs-every-step`
>   - set: `{status: pending, method: "uv run pytest tests/test_lint.py -k every_step"}`
>   - change: `the Criterion replaced whole — tests run make lint with a fake uv, one whose backlog step is red and one whose steps are all green; the method is those tests, and the defer of case 631 is taken up (case 637.3)`
> - [ ] read `estimate-lint-runs-every-step`

> **ratification:**
> ```
> - decision[case 637.3][update][estimate-lint-runs-every-step]{ref:rule-lint}{supersedes:case 631}
> ```

### Case 637.4 — The session-start check is read by its make target alone

> **given:**
> `estimate-session-start-context` — its `method` set anew; its Criterion stands
> **＋** `Makefile` — the target `make test-session-start`
> **＋** `tests/test_ledger.py` — the tests of the ledger hook, the refusal without `/hi` included
> **＋** `tests/test_event.py` — the tests of the event log
> **＋** `rule-session-start` — a MOC, whose Estimate's method is a `make` target
> **＋** `rule-estimates-schema` — the forms of a `method`

> **when:**
> Someone takes the reading of `estimate-session-start-context` by its method.

> **then:**
> The method is `make test-session-start` alone, which runs `tests/test_event.py` and `tests/test_ledger.py`, and the reading can be taken at any time.
> **－** No session opened without `/hi`, and no ledger of a later working session, is part of the reading.
> **－** The Criterion and the status of `estimate-session-start-context` stand.

> **tasks:**
> - [ ] update `estimate-session-start-context`
>   - set: `{method: "make test-session-start"}`
>   - change: `the method is the make target alone; the live session without /hi is no longer waited for (case 637.4)`

> **ratification:**
> ```
> - decision[case 637.4][update][estimate-session-start-context]{ref:rule-session-start}
> ```
