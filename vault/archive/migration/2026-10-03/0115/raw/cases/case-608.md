## Case 608 — A ratified Case built again in another shape takes a new number

> **context:**
> After each ratification, the `Stop` hook of `rule-spec-write` copies the Case into the plan file. A Case can be ratified whole and then built again with sub-cases, which pre-spec findings often cause. On the second ratification the hook rewrites only the parent's `context`, `problem` and `recommend`. It keeps the parent's old `given`, `when`, `then` and blocks beside the new sub-cases (`write_parent` of `guppi/ratified.py`). The plan then signs the same change twice, and the check after the write refuses it. This happened with Cases 471, 580 and 603. Each time, the way out was a new Case number that supersedes the old one: 474, 581 and 606. `insight-spec-write-parent-body-kept-on-re-ratification` clusters the three lessons, and case 585 put it off. Case 475 put off the matching change on `rule-spec-write`, which was to drop the old body so that the Case keeps its number.
>
> `case-guppi` found that dropping the body is not enough. The ledger still holds the decision lines of the first, whole ratification. Once their items leave the plan, `check_lines` of `guppi/prespec.py` reports each of them as a line with no item in the plan. A line is retired only by `{supersedes:case N}`, one block per Case number, since `superseded_in_window` matches the number exactly. Retiring old lines in some other way is the put-off `rule-ledger-line-withdrawn-on-re-ratification` (case 594). So the person chose to make the new number the rule and to guard it.
>
> The guard covers two other shapes besides the reported one. A Case ratified with sub-cases that comes back whole keeps its old sub-cases in the plan, because `place` replaces only the parent's section. A Case that comes back without a ratified sub-case keeps that sub-case and its ledger lines, and no check sees it. The check runs in the existing `SubagentStop` hook `uv run guppi casecheck --subagent`. That is the only hook on that event in `.claude/settings.json`. Case 607 of this session changes which output that hook takes as the answer of `case-guppi`. This Case adds one finding on an answer that holds a Case, and the two do not conflict. The Spec hook does not change. Taking up the two defers retires them with `{supersedes:case 475}` on the line of `rule-spec-write` and `{supersedes:case 585}` on the line of the Insight. The Insight is set `actioned`.
>
> The new Estimate has a `ref`, so the vault query of `ask-guppi` was not run. A Glob for its slug over `vault/wiki/` and `vault/archive/` printed no file. The other Estimates of `rule-case-check` speak of other findings, of the `Stop` comparison or of errors of the run, and adding one finding to the same exit makes none of them false. The Purpose of `rule-case-check` already covers a Case in a form the checks of pre-spec refuse, so it stands. `estimate-spec-write-removes-a-superseded-case` already checks that the plan loses the old Case once the new one is ratified. The two Estimates of `rule-case-protocol` stand: an update of its Render touches no Estimate of the live reading, and the Criterion of `estimate-case-protocol-case-form` says nothing about Case numbers. A Grep of `ratified again|built again` over `vault/wiki/rules/*.md`, `.claude/**/*.md` and `vault/wiki/*.md` printed 12 files:
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
> A Case can be ratified in the session and then built again in another shape under its old number: whole after sub-cases, with sub-cases after whole, or without a ratified sub-case. The Spec hook then keeps the old parts beside the new ones, and the ledger lines of the first ratification stay. Either the plan signs content twice and is refused, or a dropped sub-case stays signed without anyone noticing. Nothing tells the agent to take a new number before the refusal comes.

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

> **given:**
> `guppi/casecheck.py` and `tests/test_casecheck.py` — `check_answer`, `subagent`, the module docstring, and their tests
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — the new promise of the check
> **＋** `raw/<date>/<hi HHMM>/ledger.md` and `<plan>.checked.json` — the session's decision lines and the store of checked answers, which the check reads
> **＋** `rule-case-check` — the rule of the check; unchanged
> **＋** `rule-case-protocol` — the rule rendered into `vault/wiki/case-schema.md`; its splitting part gains the rule of the new number
> **＋** `rule-spec-write` and `insight-spec-write-parent-body-kept-on-re-ratification` — the pages whose defers this Case retires
> **＋** `raw/2026-10-03/0115/cases/case-607.md` — Case 607, which sets what the same `SubagentStop` check takes as the answer

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

> **then:**
> For an answer that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
> **＋** Case N gets a finding when a number of its family that has such a line has no section in the answer, or when a number that has such a line has a sub-case in the answer.
> **＋** The finding names each such number and a new number for the Case: one above the highest top-level Case number that the decision lines of the session's ledger and the Cases of `<plan>.checked.json` hold. It tells `case-guppi` to build the Case under the new number, with one `{supersedes:case M}` on a decision line for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr, and `case-guppi` answers again.
> **＋** The judgment and the new number come from one function of `guppi/casecheck.py`.
> **－** An answer that holds sub-cases of Case N without Case N gets no finding of this check.
> **－** A Case whose family has no decision line other than `defer` in the session's ledger, and a Case built again with each number of its family that has such a line, and no sub-case under any of them, get no finding of this check.

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
>   - new: `then every sub-case whole (case 355.2). A Case that has a decision line in the session's ledger and is built again in another shape — whole after sub-cases, with sub-cases after whole, or without a sub-case that has a decision line — is built under a new number, never its old one, with one {supersedes:case N} for each of its numbers that has a decision line: the Spec hook keeps the old parts beside the new ones, and the old lines stay in the ledger. The check of the answer of case-guppi sends back a build that keeps the old number, and names the new number (case 608).`
>   - change: `Splitting: a Case ratified in the session that is built again in another shape takes a new number that supersedes it (case 608)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] update `rule-spec-write`
>   - change: `the put-off change to drop the parent's old body on re-ratification is not taken: a Case ratified in the session that is built again in another shape takes a new number that supersedes it, and the check of rule-case-check sends back one that keeps its number (case 608)`
> - [ ] update `insight-spec-write-parent-body-kept-on-re-ratification`
>   - set: `{status: actioned, addressed_by: decision-case-608}`
>   - change: `actioned: a Case ratified in the session that is built again in another shape takes a new number that supersedes it, written in the splitting part of case-schema.md and guarded by the SubagentStop check of rule-case-check; the Spec hook is not changed (case 608)`
> - [ ] `guppi/casecheck.py`: one function takes the Cases of an answer, the decision lines of the session's ledger and the store. For a top-level Case N of the answer it returns a finding for each number of the family of N that has a decision line other than `defer` and no section in the answer, and for each such number that has a sub-case in the answer. The finding carries the new number, one above the highest top-level number of the ledger lines and the store keys, and the `{supersedes:case M}` marks to carry. `subagent` passes the store to `check_answer`, and `check_answer` adds the findings to Case N. The module docstring says so.
> - [ ] `tests/test_casecheck.py`, each test named `shape`: a Case ratified whole that comes back with sub-cases is sent back with the new number and the marks; a Case ratified with sub-cases that comes back whole is sent back; a whole answer without a ratified sub-case is sent back; a sub-case answered alone, a Case built again in the same shape, and a Case with only `defer` lines exit 0.
> - [ ] `uv run pytest tests/test_casecheck.py -k shape`
> - [ ] read `estimate-case-check-sends-back-a-ratified-case-in-another-shape`

> **ratification:**
> ```
> - decision[case 608][create][estimate-case-check-sends-back-a-ratified-case-in-another-shape]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 608][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 608][update][rule-spec-write]{ref:rule-spec-write}{supersedes:case 475}
> - decision[case 608][update][insight-spec-write-parent-body-kept-on-re-ratification]{ref:insight-spec-write-parent-body-kept-on-re-ratification}{supersedes:case 585}
> ```
