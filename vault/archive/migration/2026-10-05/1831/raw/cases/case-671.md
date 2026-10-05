## Case 671 — A ratified Case built again without a target of its lines goes back for a new number

> **context:**
> When the person ratifies a Case, the ledger gets one decision line per page the Case creates or changes. The ledger only grows, and only a `{supersedes:case N}` mark retires a line. Today the check of the file `case-guppi` writes, `shape_findings` of `guppi/casecheck.py` (case 610.1), sends back a ratified Case only when its layout of sub-cases changed. A Case built again under its number with a target renamed or dropped passes that check, and the Spec hook then refuses the old line, by `check_lines` of `guppi/prespec.py`. In session 1616 the create of Case 663 was renamed under its number, the hook refused "case 663: line [create][estimate-synthesis-reads-the-status-the-run-sets] has no item in the plan", and Case 668 had to supersede 663 (`lesson-case-build-renamed-a-slug-of-a-ratified-case-under-its-old-number`). Session 2300 met the same fault with a dropped create (`lesson-ledger-a-dropped-item-needs-a-superseding-sub-case`). The two lessons are the children of `insight-ledger-ratified-line-never-withdrawn`.
> The person chose that the check sends such a Case back with a new number and the marks, as it does for a change of layout. The person also chose to delete the draft `rule-ledger-line-withdrawn-on-re-ratification`, which case 594 put off, and which proposed that a second ratification withdraws the old lines. Case 671.1 adds the check, under a new Estimate, and closes the Insight. Case 671.2 adds the renamed or dropped target to the Splitting section of `case-schema.md`, and deletes the draft rule. Its delete line carries `{supersedes:case 594}`, so that it retires the defer of the page.
> The new check judges an item by `line_has_item` of `guppi/prespec.py`, which is the judgment the Spec hook runs. It takes the new number from `new_number` of `guppi/casecheck.py`, so its number and its marks agree with the finding of the layout check. It skips a number with no section or with sub-cases in the file, since the layout check already gives that Case its finding. It skips a `defer` line, as the layout check does. The check only sends a Case back before ratification, so no ledger line is lost and no old form is kept. `casecheck --subagent` is the one hook on `SubagentStop` in `.claude/settings.json`.
> The Estimates. `estimate-case-check-sends-back-a-ratified-case-in-another-shape` stands. Its Criterion speaks of the layout, and its last line says that a Case in its layout gets no finding of that check, which stays true. `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-check-sends-back-a-clash-with-another-case` judge other faults and stand. For 671.2, `estimate-case-protocol-loaded` stands. It promises that `case-schema.md` equals the Render of `rule-case-protocol` and holds the form, the sub-cases among it, and a sentence added to that section keeps both true. The send-back that the sentence describes is checked by the Estimate of 671.1. The deleted page carries no promise, and the `make lint` of the librarian's run checks that no live page links to it.
> The frame. Case 670.4 of this session updates `rule-case-protocol` by `replace` pairs in its paragraphs on a `create` of an Estimate and on the boxes of the Spec. A sub-case of Case 669 updates its paragraph on an `update` of an Estimate. The pair of 671.2 is in the Splitting section, so no Case touches another's text. The pair adds a sentence of its own, since the layout check and its Estimate mean the layout alone by "another shape". The finding tells `case-guppi` to change the number by `Edit`, as the frame of `case-guppi` in `rule-case-build` sets for any finding on the file, and `estimate-case-build-writes-the-case` stands. The finding of the layout check (case 610.1) still says to build the Case again under the new number, and a later Case may align its words. This session's Retro still follows its old rendered text until the librarian renders Case 670, so it takes no reading of the Estimate of 671.1. The next `/hi` takes that reading by its pytest `method`. A Grep `rule-ledger-line-withdrawn-on-re-ratification` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 4 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/insights/insight-ledger-ratified-line-never-withdrawn.md`. The librarian writes `backlog.md` and `brief.md` from the pages, and `log.md` is history, so these three stand. The `## Proposal` of the Insight says that the draft stands in the backlog, which the delete makes false, so the update of 671.1 replaces those words. A Grep `new number|another shape` over `{vault/wiki/rules/**,vault/wiki/*.md,.claude/**,guppi/**}` printed 8 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/case-schema.md`, `vault/wiki/log.md`, `guppi/casecheck.py`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-spec-write.md` and `vault/wiki/rules/rule-glossary.md`. The hits in `rule-case-protocol`, its file `case-schema.md` and `guppi/casecheck.py` enter this Case. The hit in `rule-spec-write` is a History line. The hit in `rule-glossary` speaks of a row of the glossary table. `brief.md`, `backlog.md` and `log.md` were not read. These four stand.

> **problem:**
> A Case ratified in the session and built again under its number with a target renamed or dropped passes every check until the Spec hook refuses its old line. A whole new Case then has to supersede it.

> **recommend:**
> - **How the gap is closed**
>   - Recommended: (a) the check of a rebuilt Case also sends it back when a ledger line of one of its numbers has no item under that number, with the new number and the marks, and the draft `rule-ledger-line-withdrawn-on-re-ratification` is deleted.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) a new Estimate under `rule-case-check` with its own tests; the Estimate of the layout check stays as it is.
>   - Answer: agreed, (a).

### Case 671.1 — The check sends back a ratified Case built again without the item of one of its lines

> **given:**
> `estimate-case-check-sends-back-a-ratified-case-without-a-target`: the new check of this promise.
> **＋** `rule-case-check`: the rule of the check of the file `case-guppi` writes.
> **＋** `guppi/casecheck.py`: the check, which holds `shape_findings` and `new_number`.
> **＋** `guppi/prespec.py`: holds `line_has_item`, the judgment of the Spec hook.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that `case-guppi` writes and the check reads.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the session's ledger, whose decision lines the check reads.
> **＋** `insight-ledger-ratified-line-never-withdrawn`: the Insight this Case closes.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` of `guppi/casecheck.py` reads the Cases of that file and the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`.

> **then:**
> For each number of the family of a top-level Case N in the file that has a section in the file and no sub-case under it, the hook reads the decision lines of that number in the session's ledger, of a kind other than `defer`.
> **＋** A line whose kind and slug has no item under that number, in the `then` block that the hook builds from the file, gives Case N a finding. The judgment of an item is `line_has_item` of `guppi/prespec.py`, imported.
> **＋** The finding names the number and the line, and tells `case-guppi` to build the Case under the number that `new_number` of `guppi/casecheck.py` gives. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr. `case-guppi` fixes the file by `Edit`: it puts the item back, or it changes the number in the headings and the ledger lines and adds the marks. It does not write the whole Case again.
> **－** A `defer` line gives no finding of this check.
> **－** A number with no section in the file, or with a sub-case in the file, gets no finding of this check.
> **－** A Case whose items hold each decision line of its numbers gets no finding of this check, whatever items it adds.

> **tasks:**
> - [ ] `guppi/casecheck.py`: a function `target_findings` gives `(top-level case, finding)` for each decision line other than `defer` of the session's ledger on a number of the family that has a section in the answer and no sub-case in it, whose kind and slug `line_has_item` of `guppi/prespec.py`, imported, does not find in that number's `then` block; the finding names the number, the line, the new number by `new_number` and the marks as `shape_findings` writes them, and tells `case-guppi` to put the item back or to change the number in the headings and the ledger lines by `Edit` and add the marks, never writing the whole Case again; `check_answer` adds its findings where `store` is given, beside `shape_findings`; the module docstring and the docstring of `check_answer` name it (case 671.1).
> - [ ] `tests/test_casecheck.py`: tests `-k dropped_target`: a file whose Case renames the slug of a ratified `create` under its number is sent back with the new number and the marks; a file that drops an item of a ratified line is sent back; a file that keeps each item and adds one passes; a dropped `defer` item gives no finding of this check; a number with no section, or with sub-cases, gets only the finding of `shape_findings`.
> - [ ] create `estimate-case-check-sends-back-a-ratified-case-without-a-target`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether a Case that has decision lines in the session and comes back from case-guppi under its number without the item of one of those lines goes back to case-guppi with a new number to build it under`
>   - method: `uv run pytest tests/test_casecheck.py -k dropped_target`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `insight-ledger-ratified-line-never-withdrawn`
>   - set: `{status: actioned, addressed_by: decision-case-671.1}`
>   - old: `(rule-ledger-line-withdrawn-on-re-ratification stands in the backlog)`
>   - new: `(rule-ledger-line-withdrawn-on-re-ratification was deleted by case 671.2)`
>   - change: `actioned: the check of the file case-guppi writes sends back a ratified Case built again without the item of one of its lines, with the new number and the marks (case 671.1)`
> - [ ] read `estimate-case-check-sends-back-a-ratified-case-without-a-target`

> **ratification:**
> ```
> - decision[case 671.1][create][estimate-case-check-sends-back-a-ratified-case-without-a-target]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 671.1][update][insight-ledger-ratified-line-never-withdrawn]{ref:insight-ledger-ratified-line-never-withdrawn}
> ```

### Case 671.2 — The schema names a renamed or dropped target among the Cases built under a new number

> **given:**
> `rule-case-protocol`: the Render of the Case form, whose Splitting section changes.
> **＋** `vault/wiki/case-schema.md`: the file rendered from it, which `case-guppi` reads whole.
> **＋** `rule-ledger-line-withdrawn-on-re-ratification`: the draft rule put off by case 594, which this Case deletes.

> **when:**
> `case-guppi` reads `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, before it builds again a Case that has decision lines in the session's ledger.

> **then:**
> The Splitting section says, in a sentence apart from the Cases built again in another shape, that a Case that comes back in its shape without the item of one of its decision lines, its target renamed or dropped, is built under a new number too.
> **＋** The section says that the check of the file `case-guppi` writes sends such a build back and names the new number, and that `case-guppi` changes the number by `Edit` and does not write the whole Case again.
> **－** `rule-ledger-line-withdrawn-on-re-ratification` no longer stands as a draft for withdrawing the old lines.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `names the new number (case 610.1).`
>   - new: `` names the new number (case 610.1). A Case that has a decision line in the session's ledger and comes back in its shape, but without the item of one of those lines under its number — the target of that line renamed or dropped — is built under a new number too, its decision lines carrying the same marks; the check of the file case-guppi writes sends it back with the new number, and case-guppi changes the number in the headings and the ledger lines by `Edit` and adds the marks, never writing the whole Case again (case 671.1). ``
>   - change: `Splitting: a Case built again under its number without the item of one of its decision lines takes a new number too (case 671.2)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] delete `rule-ledger-line-withdrawn-on-re-ratification`
>   - impact: `the draft rule of the backlog leaves; a ratified Case built again without a target takes a new number that supersedes it, and the check of case 671.1 sends back one that keeps its number; the defer of case 594 is retired by the supersedes mark of this line`

> **ratification:**
> ```
> - decision[case 671.2][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 671.2][delete][rule-ledger-line-withdrawn-on-re-ratification]{ref:rule-ledger-line-withdrawn-on-re-ratification}{supersedes:case 594}
> ```
