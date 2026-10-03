## Case 610 — A ratified Case built again in another shape takes a new number

> **context:**
> After each ratification, the `Stop` hook of `rule-spec-write` copies the Case into the plan file. A Case can be ratified whole and then built again with sub-cases, which pre-spec findings often cause. On the second ratification the hook rewrites only the parent's `context`, `problem` and `recommend`. It keeps the parent's old `given`, `when`, `then` and blocks beside the new sub-cases (`write_parent` of `guppi/ratified.py`). The plan then signs the same change twice, and the check after the write refuses it. This happened with Cases 471, 580 and 603. Each time, the way out was a new Case number that supersedes the old one: 474, 581 and 606. `insight-spec-write-parent-body-kept-on-re-ratification` clusters the three lessons, and case 585 put it off. Case 475 put off the matching change on `rule-spec-write`, which was to drop the old body so that the Case keeps its number.
>
> Dropping the body is not enough. The ledger still holds the decision lines of the first ratification. Once their items leave the plan, `check_lines` of `guppi/prespec.py` reports each of them as a line with no item in the plan. A line is retired only by `{supersedes:case N}`, one block per number, since `superseded_in_window` matches the number exactly. So the person chose to make the new number the rule and to guard it. The way to retire old lines without a new Case stays with the put-off `rule-ledger-line-withdrawn-on-re-ratification` (case 594). At pre-spec the person chose to keep that defer, and this Case does not name that page. A dropped sub-case goes by the new number too, and the backlog does not change.
>
> This Case was first ratified whole as Case 608. Pre-spec then found that it needs a second promise, so it is built again with sub-cases. By the rule it sets, it takes a new number. 609 is the highest number in the session's ledger `raw/2026-10-03/0115/ledger.md` and among the keys of the store `curious-petting-pearl.checked.json`, so the new number is 610. Its first decision line carries `{supersedes:case 608}`, and Case 610 closes the Frontier line C4 again.
>
> 610.1 sets the guard. It covers three shapes: a Case ratified whole that comes back with sub-cases; a Case ratified with sub-cases that comes back whole, which keeps its old sub-cases in the plan because `place` replaces only the parent's section; and a Case that comes back without a ratified sub-case. The last one keeps that sub-case and its lines, and no check sees it.
>
> The first build said that `estimate-spec-write-removes-a-superseded-case` already checks that the plan loses the old Case. That holds only for a mark on the top-level number. A parent first ratified with sub-cases has no decision line of its own, and a mark on a sub-case removes that sub-case alone, as that Estimate says, so the old parent would stay in the plan. `lesson-prespec-parent-of-superseded-sub-cases` records this shape. So the finding names a mark for the old top-level number too. `remove_case` then removes it with every sub-case. In `guppi/materialize.py` a mark on a parent with no line of its own marks the parent's Decision record, which exists once its sub-cases have lines (case 544.6). The ledger hook does not judge the marks. With that mark, the Criterion of `estimate-spec-write-removes-a-superseded-case` stands.
>
> 610.2 makes true the claim that a clash of the new number is caught. Two Cases sent back in one batch could be given the same number. So could a new Case the main agent has sent out but that has not answered yet. Each stored Case keeps the `agent_id` of the payload, and an answer under a number that another agent holds is sent back. That answer is stored apart, so the line of `estimate-case-check-sends-back-a-faulty-case` that every Case of an answer is stored stays true. Case 607.1 has just replaced that Criterion, and a second replacement in this session would be refused at pre-spec. Every reader that looks a Case up by its number still finds the first agent's entry, so `estimate-case-check-shows-only-the-checked-case` stands. The notes of `estimate-case-check-notes-a-criterion-line-not-carried` are kept per entry, and an answer that clashes is built again under a new number anyway, so that Criterion stands. A fresh `case-guppi` sent out on a number another one has already answered is sent back too. The rules send every change to the same agent, so that only happens outside them.
>
> The two sub-cases count the new number with one function. 610.2 names that count through the Estimate of 610.1 rather than repeating it, so that the count is promised in one wording.
>
> Both checks run in the existing `SubagentStop` hook `uv run guppi casecheck --subagent`, the only hook on that event in `.claude/settings.json`. Case 607 changes which output that hook takes as the answer. These sub-cases add findings on an answer that holds a Case, and the two do not conflict. The Spec hook does not change. 610.1 retires the two defers with `{supersedes:case 475}` on the line of `rule-spec-write` and `{supersedes:case 585}` on the line of the Insight, and sets the Insight `actioned`. The other Estimates of `rule-case-check` speak of other findings, of the `Stop` comparison or of errors of the run, and stay true. Its Purpose already covers a Case in a form the checks of pre-spec refuse. An update of the Render of `rule-case-protocol` touches no Estimate of the live reading, and the Criterion of `estimate-case-protocol-case-form` says nothing about Case numbers.
>
> Both new Estimates have a `ref`, so the vault query of `ask-guppi` was not run. A Glob for each slug over `vault/wiki/` and `vault/archive/` printed no file. A Grep of `ratified again|built again` over `vault/wiki/rules/*.md`, `.claude/**/*.md` and `vault/wiki/*.md` printed 12 files:
> - `brief.md`
> - `backlog.md`
> - `log.md`
> - `orchestration.md`
> - `.claude/skills/pre-spec/SKILL.md`
> - `.claude/agents/case-guppi.md`
> - `rule-prespec.md`
> - `rule-prespec-onward.md`
> - `rule-orchestration.md`
> - `rule-case-build.md`
> - `rule-spec-box.md`
> - `rule-ledger-line-withdrawn-on-re-ratification.md`
>
> The hits in `brief.md` and `log.md` were not read. The hit in `backlog.md` is the line of the Insight, which leaves the backlog when its defer is retired. `orchestration.md`, the Render of `rule-orchestration`, was read whole. The hits in `rule-prespec.md`, `rule-prespec-onward.md`, `rule-case-build.md`, `rule-spec-box.md` and `.claude/agents/case-guppi.md` were read around the line of each hit. The hit in `.claude/skills/pre-spec/SKILL.md` is the rendered text of `rule-prespec.md`. None of these says which number a Case built again keeps, and each stays true. `case-schema.md` already says that the superseding Case closes again the Frontier line that the superseded Case closed.

> **problem:**
> A Case can be ratified in the session and then built again in another shape under its old number: whole after sub-cases, with sub-cases after whole, or without a ratified sub-case. The Spec hook then keeps the old parts beside the new ones, and the ledger lines of the first ratification stay. Either the plan signs content twice and is refused, or a dropped sub-case stays signed without anyone noticing. Nothing tells the agent to take a new number before the refusal comes, and nothing stops two Cases from being built under one new number.

> **recommend:**
> - **Which way to close the problem**
>   - Recommended: (b) make the new number the rule, with a guard. The check of `case-guppi`'s answer sends back a build that changes the shape of a Case already ratified in the session, the hook stays as it is, the Insight is closed and the put-off change to the hook is retired.
>   - Answer: (b).
> - **Who picks the new number**
>   - Recommended: (a) the check names it: one above the highest Case number in the session's ledger and in the store of checked answers.
>   - Answer: agreed with the recommendation, (a).
> - **Which changes of shape the check sends back**
>   - Recommended: (b) any ratified part missing from a whole answer, and a Case ratified whole that comes back with sub-cases. An answer that holds sub-cases alone is not judged this way.
>   - Answer: agreed with the recommendation, (b).
> - **Whether the form of a Case states the rule too**
>   - Recommended: (a) add one sentence to the splitting part of the form, through `rule-case-protocol`, and keep the check as the guard.
>   - Answer: agreed with the recommendation, (a).
> - **How done is checked**
>   - Recommended: (a) a new Estimate of its own under `rule-case-check`.
>   - Answer: agreed with the recommendation, (a).
> - **How a clash of the new number is caught**
>   - Recommended: (a) the store remembers which agent answered each Case. An answer under a number another agent holds is sent back with a new number and does not replace that entry. This is a sub-case of its own with its own Estimate.
>   - Answer: agreed with (a).
> - **Where the answer that clashes is kept**
>   - Recommended: (c) store it apart, under its number together with its agent's id. Readers by number still find the other agent's entry, and the related Case is not touched.
>   - Answer: (c).
> - **Change**
>   - Asked: at pre-spec, keep the defer of `rule-ledger-line-withdrawn-on-re-ratification`. The context says plainly that a dropped sub-case goes by the new number, while the way without a new Case stays with that rule, and the backlog does not change.
>   - Taken: the context says so. No line names that page, and the defer stands.

### Case 610.1 — The check sends back a ratified Case built again in another shape under its old number

> **given:**
> `guppi/casecheck.py` and `tests/test_casecheck.py` — `check_answer`, `subagent`, the function of the new number, the module docstring, and their tests
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — the new promise of the check
> **＋** `raw/<date>/<hi HHMM>/ledger.md` and `<plan>.checked.json` — the session's decision lines and the store of checked answers, which the check reads
> **＋** `rule-case-protocol` — the rule rendered into `vault/wiki/case-schema.md`; its splitting part gains the rule of the new number
> **＋** `rule-spec-write` and `insight-spec-write-parent-body-kept-on-re-ratification` — the pages whose defers this sub-case retires
> **＋** `estimate-spec-write-removes-a-superseded-case` — the removal from the plan that the marks rely on; unchanged
> **＋** `rule-case-check` — the rule of the check; unchanged
> **＋** `raw/2026-10-03/0115/cases/case-607.md` — Case 607, which sets what the same `SubagentStop` check takes as the answer

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

> **then:**
> For an answer that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
> **＋** Case N gets a finding when a number of its family that has such a line has no section in the answer, or when a number that has such a line has a sub-case in the answer.
> **＋** The finding names each such number and a new number: one above the highest top-level Case number that the decision lines of the session's ledger and the keys of `<plan>.checked.json` hold.
> **＋** The finding tells `case-guppi` to build the Case under the new number. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr, and `case-guppi` answers again.
> **＋** The judgment and the new number come from one function of `guppi/casecheck.py`.
> **－** An answer that holds sub-cases of Case N without Case N gets no finding of this check.
> **－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

> **tasks:**
> - [ ] create `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
>   - type: `estimate`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `A Case that has decision lines in the session and comes back from case-guppi in another shape under its old number goes back to case-guppi with a new number to build it under`
>   - method: `uv run pytest tests/test_casecheck.py -k shape, then by hand the first answer of case-guppi the hook sends back for this reason`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-case-protocol`
>   - old: `then every sub-case whole (case 355.2).`
>   - new: `then every sub-case whole (case 355.2). A Case that has a decision line in the session's ledger and is built again in another shape — whole after sub-cases, with sub-cases after whole, or without a sub-case that has a decision line — is built under a new number, never its old one, and its decision lines carry one {supersedes:case N} for its old top-level number and one for each of its old numbers that has a decision line: the Spec hook keeps the old parts beside the new ones, a mark on a sub-case removes that sub-case alone, and the old lines stay in the ledger until a mark retires them. The check of the answer of case-guppi sends back a build that keeps the old number, and names the new number (case 610.1).`
>   - change: `Splitting: a Case ratified in the session that is built again in another shape takes a new number, its decision lines superseding its old top-level number and each old number with a line (case 610.1)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] update `rule-spec-write`
>   - change: `the put-off change to drop the parent's old body on re-ratification is not taken: a Case ratified in the session that is built again in another shape takes a new number that supersedes it, and the check of rule-case-check sends back one that keeps its number (case 610.1)`
> - [ ] update `insight-spec-write-parent-body-kept-on-re-ratification`
>   - set: `{status: actioned, addressed_by: decision-case-610.1}`
>   - change: `actioned: a Case ratified in the session that is built again in another shape takes a new number that supersedes it, written in the splitting part of case-schema.md and guarded by the SubagentStop check of rule-case-check; the Spec hook is not changed (case 610.1)`
> - [ ] `guppi/casecheck.py`: one function gives the new number, one above the highest top-level number among the decision lines of the ledger and the keys of the store, a key joined with an agent id read by its number. A second function takes the Cases of an answer, the decision lines of the session's ledger and the store. For a top-level Case N of the answer it returns a finding for each number of the family of N that has a decision line other than `defer` and no section in the answer, and for each such number that has a sub-case in the answer. The finding carries the new number, and the marks for N and for each such number. `subagent` passes the store to `check_answer`, and `check_answer` adds the findings to Case N. The module docstring says so.
> - [ ] `tests/test_casecheck.py`, each test named `shape`: a Case ratified whole that comes back with sub-cases is sent back with the new number and the marks; a Case ratified with sub-cases that comes back whole is sent back with a mark for its parent too; a whole answer without a ratified sub-case is sent back; a sub-case answered alone, a Case built again in the same shape, and a Case with only `defer` lines exit 0.
> - [ ] `uv run pytest tests/test_casecheck.py -k shape`
> - [ ] read `estimate-case-check-sends-back-a-ratified-case-in-another-shape`

> **ratification:**
> ```
> - decision[case 610.1][create][estimate-case-check-sends-back-a-ratified-case-in-another-shape]{ref:rule-case-check}{tags:hooks,harness,workflow}{supersedes:case 608}
> - decision[case 610.1][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 610.1][update][rule-spec-write]{ref:rule-spec-write}{supersedes:case 475}
> - decision[case 610.1][update][insight-spec-write-parent-body-kept-on-re-ratification]{ref:insight-spec-write-parent-body-kept-on-re-ratification}{supersedes:case 585}
> ```

### Case 610.2 — The check sends back a Case under a number another agent holds, and stores it apart

> **given:**
> `guppi/casecheck.py` and `tests/test_casecheck.py` — `subagent`, the store's entries and keys, the module docstring, and their tests
> **＋** `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — the new promise of the check
> **＋** `<plan>.checked.json` — the store of checked answers, whose entries keep the agent id
> **＋** `agent_id` of the `SubagentStop` payload — the id of the agent that answered
> **＋** `guppi/ratified.py` — the Spec hook and the `Stop` comparison, which read the store by Case number; unchanged
> **＋** `rule-case-check` and `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — the rule of the check, and the sibling promise whose count of the new number this check uses; unchanged here
> **＋** `raw/2026-10-03/0115/cases/case-607.md` — Case 607, which sets what the same `SubagentStop` check takes as the answer and that each Case of an answer is stored

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, `agent_id` of the payload, and `<plan>.checked.json` beside the plan file.

> **then:**
> The hook stores each Case of an answer in `<plan>.checked.json` with the `agent_id` of the payload beside its text, its findings and the time of the store.
> **＋** A top-level Case N of the answer is sent back when the store holds Case N, or a sub-case of it, under its number from an answer with another `agent_id`.
> **＋** Its message gives `case-guppi` a free number, counted as `estimate-case-check-sends-back-a-ratified-case-in-another-shape` counts it, to build the Case under, and the exit code is 2.
> **＋** Each Case of that answer is stored apart, under its number joined with its `agent_id`, and the entry of the other agent under the number alone stays as it was.
> **＋** The Spec hook, the `Stop` comparison and the writing of the file of a Case read the entry under the number alone.
> **－** An unchanged answer whose text its entry apart already holds with this finding is stored again and exits 0, so it is not sent back twice.
> **－** An entry with no `agent_id`, stored before the change, gives no finding of this check, and neither does an answer whose `agent_id` is the one of the entry under the number.

> **tasks:**
> - [ ] create `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
>   - type: `estimate`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `A Case of case-guppi under a number that the store holds from the answer of another agent goes back to it with a new number, and the other agent's entry is kept`
>   - method: `uv run pytest tests/test_casecheck.py -k clash, then by hand the first answer of case-guppi the hook sends back for this reason`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: `subagent` stores `agent_id` in each entry. Before it stores, it compares the `agent_id` of the entry under the top-level number of each Case of the answer, and of its sub-cases, with the payload's. On another id it adds the finding with the new number from the function of 610.1 and stores the Cases of the answer under their number joined with the `agent_id`, with the loop guard read from that entry. An entry with no `agent_id` is not compared. The module docstring says so.
> - [ ] `tests/test_casecheck.py`, each test named `clash`: an answer under a number that the store holds from another agent exits 2 with the new number and leaves the other entry as it was; the answer stands under its key apart; the same answer again exits 0; an entry with no agent id and an answer of the same agent give no finding; `ratified.find_showing` and the case file still read the entry under the number alone.
> - [ ] `uv run pytest tests/test_casecheck.py -k clash`
> - [ ] read `estimate-case-check-sends-back-a-case-number-held-by-another-agent`

> **ratification:**
> ```
> - decision[case 610.2][create][estimate-case-check-sends-back-a-case-number-held-by-another-agent]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```
