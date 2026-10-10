## Case 749 — A rebuilt Case that changes the parent or tags of a new page goes back with a new number

> **context:**
> Each time the person signs a Case, its decision lines are added to the session's ledger, and no line is ever removed; only a `{supersedes:case N}` mark retires one. When the librarian builds the pages, `guppi/generate.py` applies the first line of a Case for a page, and takes a later line of the same Case, kind and slug for a repeat that changes nothing (case 514). A new page takes its `ref`, its parent, and its tags from that line, not from the signed item (`_lift_item` of `guppi/materialize.py`), so when a rebuilt Case keeps a page and changes its parent or tags, the first line wins. In session 2352 Case 743 was ratified, built again at `/pre-spec` and ratified again: ledger lines 15 and 19 create `rule-skill-sprint-open` and `rule-skill-sprint-close` with `{ref:rule-session}`, and lines 27 and 28 create them with `{ref:rule-session-start}` and `{ref:rule-plan-mode}`. Both pages were built under `rule-session`, and Case 746 of this session moves them under their phases by `update` items that `generate` applies at the librarian's run. The check of the file `case-guppi` writes already sends back a rebuilt Case that drops or renames a page, with a new number and the marks (`target_findings` of `guppi/casecheck.py`, case 671.1), but it judges only the kind and the slug of a line, so a changed `ref` or tag list passes.
>
> The person chose to extend that check and not the librarian's scripts: a rebuilt Case whose `create` line keeps its slug and changes its `ref`, or adds or removes a tag, goes back with a new number and the marks, and `case-guppi` either writes the line back as the ledger holds it or moves the Case to the new number. Only a `create` line is judged, since `guppi/generate.py` reads the `ref` of an entry only when it creates a page, and a decision line carries tags only on a `create` (`ratification.md`). The order of the tags does not count. The new promise gets an Estimate of its own. The Criterion of `estimate-case-check-sends-back-a-ratified-case-without-a-target` stands, since each of its lines speaks of its own check of a line with no item, and the two checks can fail apart. The Criterion of `estimate-case-check-sends-back-a-ratified-case-in-another-shape` (case 610.1) stands too. Its lines speak of a Case built again in another shape, and each of its exceptions is scoped to its own check. Its line that the judgment and the new number come from one function of `guppi/casecheck.py` stays true, since the new finding takes its number from the same `new_number`. The Splitting paragraph of `rule-case-protocol` gains one sentence beside the sentence of case 671.1, which stays true. The Purpose of `rule-case-check` names neither the check of case 610.1 nor that of case 671.1, so it stands. `estimate-case-protocol-loaded` and `estimate-case-protocol-case-form` speak of the render and the form of a Case, not of a rebuilt Case, so they stand. `insight-ledger-ratified-line-never-withdrawn` is set `actioned` again, `addressed_by` this Case, so the cascade archives its `clustered` lesson `lesson-ledger-rebuilt-create-keeps-the-stale-ref`.
>
> The Grep `renamed or dropped|dropped or renamed|671\.1` over the repository, with the glob `!vault/{raw,archive}/**`, printed `guppi/casecheck.py`, `tests/test_casecheck.py`, `vault/wiki/case-schema.md`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-case-check.md`, `vault/wiki/insights/insight-ledger-ratified-line-never-withdrawn.md`, `vault/wiki/estimates/estimate-case-check-sends-back-a-ratified-case-without-a-target.md`, `vault/wiki/backlog.md` and `vault/wiki/log.md`. The module and the test change in `tasks`. `case-schema.md` changes through the render. The hit in `rule-case-check` is a History line. The Pattern of the Insight stays as the record of what the lessons share. The hit in the Estimate is its own check, which stands. `backlog.md` is rendered from the live pages, and `log.md` is not read. The Grep `Path\(__file__\)|parents\[1\]|REPO|ROOT =` over `tests/` printed `tests/test_lint.py`, `tests/test_case_schema.py`, `tests/test_generate.py`, `tests/test_orchestration.py`, `tests/test_materialize.py` and `tests/test_schemas.py`. The Grep `casecheck` over `tests/` printed `tests/test_casecheck.py`, `tests/test_ratified.py`, `tests/test_case_schema.py`, `tests/test_ledger.py`, `tests/test_onward.py`, `tests/test_orchestration.py` and `tests/test_materialize.py`, so of the six only `test_case_schema.py`, `test_orchestration.py` and `test_materialize.py` reach `guppi/casecheck.py`. `test_case_schema.py` runs `check_answer` with no store, and the check of a rebuilt Case runs only with a store. `test_orchestration.py` and `test_materialize.py` call other functions. So no test reads a live file through the new check. Case 748 of this session, which adds a check of the fields of a `create` item, was not written when this Case was built. Where it changes `guppi/casecheck.py` or the Splitting paragraph, the two texts are read side by side at `/pre-spec`.
>
> Not done: the ledger and `materialize.yaml` of session 2352 stay as they are. `guppi/generate.py` keeps its rule that a later line of the same Case, kind and slug is a repeat.

> **problem:**
> A Case that is ratified, built again and ratified again with a new parent or new tags for a page it creates leaves two `create` lines in the ledger. The librarian builds the page from the first, stale line, and no check before the Spec says so.

> **recommend:**
> - **Where the fix lives**
>   - Recommended: (a) the check of the case file sends the rebuilt Case back with a new number and the marks that retire the old lines, as it does for a dropped page.
>   - Answer: agreed, (a).
> - **Which parts of a line count as a change**
>   - Recommended: (b) the parent page and the tags.
>   - Answer: agreed, (b).
> - **Whether the pattern page closes**
>   - Recommended: (a) this Case marks `insight-ledger-ratified-line-never-withdrawn` handled, and the librarian archives the lesson of this item with it.
>   - Answer: agreed, (a).
> - **How the new check is checked**
>   - Recommended: (a) a new Estimate of its own on `rule-case-check`; `estimate-case-check-sends-back-a-ratified-case-without-a-target` stands unchanged.
>   - Answer: agreed, (a).
> - **Whether the order of the tags counts**
>   - Recommended: (a) order does not count; only a tag added or removed is a change.
>   - Answer: agreed, (a).
> - **What the send-back offers**
>   - Recommended: (a) the same two ways as for a dropped page: write the line back as the ledger holds it, or move the Case to the new number with the marks, by `Edit` alone.
>   - Answer: agreed, (a).

> **given:**
> `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line`: the new check of the send-back.
> **＋** `rule-case-check`: the rule of the check of the file of a Case.
> **＋** `guppi/casecheck.py`: the check that `SubagentStop` runs on the file, beside `target_findings`.
> **＋** `tests/test_casecheck.py`: the tests of the new finding.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case, whose `ratification` holds its new lines.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the session's ledger, which holds the lines already signed.
> **＋** `rule-case-protocol`: the rule whose Render `vault/wiki/case-schema.md` says how a rebuilt Case takes a new number.
> **＋** `insight-ledger-ratified-line-never-withdrawn`: the pattern page of this problem, set handled.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` of `guppi/casecheck.py` reads the Cases of that file, the decision lines of their `ratification`, and the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`.

> **then:**
> For each number of the family of a top-level Case N in the file that has a section in the file and no sub-case under it, the hook reads the `create` lines of that number in the session's ledger.
> **＋** A `create` line of the ledger gives Case N a finding when the `ratification` of that number in the file holds a `create` line of the same slug whose `ref` differs, or whose tags differ by a tag added or removed.
> **＋** The finding names the number, the slug and both lines, and the number that `new_number` of `guppi/casecheck.py` gives. It also names the marks: one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr. `case-guppi` fixes the file by `Edit`: it writes the line back as the ledger holds it, or it changes the number in the headings and the ledger lines and adds the marks. It does not write the whole Case again.
> **－** The same tags in another order, and a line that differs only by a `{supersedes}` or `{addresses}` mark, give no finding of this check.
> **－** A `create` line of the ledger whose slug has no `create` line under that number in the file gives no finding of this check.
> **－** An `update`, `delete` or `defer` line gives no finding of this check.
> **－** A number with no section in the file, or with a sub-case in the file, gets no finding of this check.

> **tasks:**
> - [ ] create `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether a Case that has a create line in the session and comes back from case-guppi under its number with another ref or another set of tags on that line goes back to case-guppi with a new number to build it under`
>   - method: `uv run pytest tests/test_casecheck.py -k changed_create_line`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: a finding beside `target_findings`, run where it runs, that compares each `create` line of the ledger on a number of the file with the `create` line of the same slug in the file's `ratification`, by `ref` and by the set of tags, with the new number by `new_number` and the marks by `supersede_marks`; the module docstring names it.
> - [ ] `tests/test_casecheck.py`: under `changed_create_line`, a changed `ref` and a tag added are sent back with the new number and the marks; the same tags in another order, a line with an added `{supersedes}` mark, an `update` line with another `ref`, and a number with sub-cases give no finding of this check.
> - [ ] update `rule-case-protocol`
>   - old: `` never writing the whole Case again (case 671.1). ``
>   - new: `` never writing the whole Case again (case 671.1). A Case that has a `create` line in the session's ledger and comes back in its shape with a `create` line of the same slug under the same number whose `ref` differs, or whose tags differ by a tag added or removed, is built under a new number too, its decision lines carrying the same marks, since the librarian builds the page from the first line and takes the later one for a repeat; the check of the file case-guppi writes sends it back with the new number, and case-guppi writes the line back as the ledger holds it, or changes the number in the headings and the ledger lines by `Edit` and adds the marks, never writing the whole Case again (case 749). ``
>   - change: `a rebuilt Case whose create line changes its ref or its tags takes a new number, and the check sends it back (case 749)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] update `insight-ledger-ratified-line-never-withdrawn`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-749
>     ```
>   - change: `actioned: the check of the file case-guppi writes sends back a ratified Case built again whose create line changes its ref or its tags, with the new number and the marks (case 749)`
> - [ ] read `estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line`

> **ratification:**
> ```
> - decision[case 749][create][estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 749][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 749][update][insight-ledger-ratified-line-never-withdrawn]{ref:insight-ledger-ratified-line-never-withdrawn}
> ```
