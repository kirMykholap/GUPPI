## Case 702 — A Case file declares a new tag on a tag line

> **context:**
> `guppi generate` adds a row to `vault/wiki/tags.md` only for an entry of `new_tags` in the yaml. `guppi materialize` takes those entries from the `then` block of a Case in the Spec. For any tag that a page written in the same run carries and the list does not hold, `generate` prints `generate: tag <tag> is used but not registered in tags.md` on stderr. The Spec hook of `rule-spec-write`, `guppi/ratified.py`, builds that `then` block from the task lines of the Case file. It reads a line as an item only when the line opens with `create`, `update`, `delete` or `defer`, and it refuses a sub-point under any other line. So a Case file has no way to declare a new tag, although `case-schema.md` says that new tags are declared under `new_tags` with a meaning and a Russian alias. The brief of the librarian's run of session 0211 flagged the tag `orchestration`: two lesson lines carried it with no check, the synthesis put it on `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`, and it is not in the list. The person chose to give the Case file a way to declare a tag: a task line `tag` with the sub-points `meaning` and `aliases`. The hook turns that line into an entry of `new_tags` and leaves it out of the `tasks` block, since the row in `tags.md` and the line in `log.md` already record that the tag was added.
>
> This Case does not declare `orchestration`. The hook and the check of the Case file run the code of the working tree, and until Work Mode changes it they refuse a sub-point under a tag line. So the declaration is an item for the next session, after the render puts the form into `case-schema.md`, and the handoff names it. A Case that declares a tag also needs a decision line, since the hook writes a Case only after a reply that carries one. This Case also leaves one thing not done, by the person's choice: no check stops a tag that the list does not hold from getting onto a lesson line or a `create` line. The warning of `generate` in the brief stays the only signal. The reader changes at once in the working tree, and `case-guppi` learns the form only from the render of `case-schema.md`. So no file uses the tag line before the new reader stands, no refusal loses anything, and no old form is kept. The check of the Case file, `guppi/casecheck.py`, builds the Spec section by `case_section` of `guppi/ratified.py`, so it reads the tag line by the same function. The Criterion of `estimate-case-check-sends-back-a-faulty-case` of `rule-case-check` already says that the check reads each Case in the chat form by the functions of `guppi/ratified.py` and builds its section of the Spec in memory as the Spec hook writes it. That covers the tag line as written, so it stands, and the method of the new Estimate also runs the tests of the check in `tests/test_casecheck.py`.
>
> A Grep for `` opening with `create`, `update`, `delete` or `defer`|new_tags `` over `vault/wiki/` printed `vault/wiki/case-schema.md`, `vault/wiki/log.md`, `rule-materialize.md`, `rule-case-protocol.md`, `estimate-generate-writes.md`, `estimate-materialize-assembles.md` and `estimate-spec-write-copies-the-ratified-case.md`, and over `.claude/` printed nothing. The hits in `rule-case-protocol` change here, and `case-schema.md` follows at the render. The hit in `rule-materialize` is a History line, and `log.md` is not read. `estimate-materialize-assembles` and `estimate-generate-writes` stand: `materialize` and `generate` already carry `new_tags` from a `then` block to `tags.md`, and this Case does not change them. `estimate-spec-write-copies-the-ratified-case` stands too. Its Criterion lists the lines that become items, and it says that the `tasks` block holds the task lines without their sub-points. The new texts call the tag line no task, so both sentences stay true, and the tag line is a promise of its own in the new Estimate. The Estimates of `rule-case-protocol` stand. This Case changes its Render, which touches no Estimate of the live reading (case 378.5), and it leaves the example Case of `case-schema.md` as it is. Case 701 of this session changes none of the pages this Case changes.

> **problem:**
> A Case file cannot declare a new tag, so a tag that a ratified page carries, such as `orchestration`, can never enter `tags.md`, and `generate` warns about it.

> **recommend:**
> - **Register the tag or take it off the pages**
>   - Recommended: (a) take the tag off the live lesson and the Insight, and use `workflow` and `session` like the other pages about `rule-orchestration`, with no code change.
>   - Answer: (b) register it: give the Case file a way to declare a tag, then declare `orchestration`.
> - **Whether anything stops an unlisted tag from getting in again**
>   - Recommended: (a) leave it not done; the Case says that no check stops an unlisted tag.
>   - Answer: agreed, (a).
> - **How a Case file declares a new tag**
>   - Recommended: (a) a task line `tag` with the tag in a code span and two sub-points, `meaning` and `aliases`, each one code span, which the Spec hook turns into one entry of `new_tags`; a tag line with a missing or a foreign sub-point is refused.
>   - Answer: agreed, (a).
> - **When `orchestration` itself is declared**
>   - Recommended: (a) a Case of a later session declares it, after the render puts the form into `case-schema.md`; the handoff names it.
>   - Answer: agreed, (a).
> - **What checks that the hook reads the new line**
>   - Recommended: (a) a new Estimate of `rule-spec-write`, `estimate-spec-write-reads-a-new-tag`, checked by tests in `tests/test_ratified.py`; the Criterion of `estimate-spec-write-copies-the-ratified-case` stands.
>   - Answer: agreed, (a).
> - **Whether the tag line leaves a box in the Spec**
>   - Recommended: (b) no box: the hook puts the declaration into `new_tags` of the `then` block and leaves the line out of the `tasks` block; `generate` and Retro do not change.
>   - Answer: agreed, (b).

> **given:**
> `rule-spec-write`: the rule of the Spec hook, whose How it works gains the tag line.
> **＋** `guppi/ratified.py`: `read_tasks` reads the tag line into `new_tags`.
> **＋** `tests/test_ratified.py` and `tests/test_casecheck.py`: the tests of the tag line in the hook and in the check.
> **＋** `rule-case-check`: the rule of the check of the file of a Case, whose Estimate `estimate-case-check-sends-back-a-faulty-case` stands.
> **＋** `guppi/casecheck.py`: the check of the file of a Case, which builds the Spec section by `case_section` of `guppi/ratified.py`.
> **＋** `rule-case-protocol`: its Render, `vault/wiki/case-schema.md`, gains the tag line.
> **＋** `vault/wiki/case-schema.md`: the file rendered from `rule-case-protocol`.
> **＋** `estimate-spec-write-reads-a-new-tag`: the new check of the tag line.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.

> **when:**
> The `Stop` hook `uv run guppi ratified` of `guppi/ratified.py` writes into the plan file a ratified Case whose `tasks` in `raw/<date>/<hi HHMM>/cases/case-<N>.md` hold a line `` - [ ] tag `<tag>` ``.
> **＋** Or the `SubagentStop` hook `uv run guppi casecheck --subagent` of `guppi/casecheck.py` checks that file.

> **then:**
> A task line that opens with `tag` and the tag in its first code span, with the sub-points `meaning` and `aliases`, each one code span, becomes one entry of the key `new_tags` in the block tagged `then`: its `tag`, `meaning` and `aliases`.
> **＋** Each tag line of a Case becomes an entry of its own, in the order of the file.
> **＋** The tag line is no task: the block tagged `tasks` does not hold it.
> **＋** `guppi/casecheck.py` reads the tag line by the same function of `guppi/ratified.py`, and a refusal of the hook is a finding of the check.
> **－** A tag line with `meaning` or `aliases` missing, with another sub-point, or with a value that is not one code span is refused: exit 2 with the reason on stderr, and nothing of the Case is written.
> **－** A sub-point under a line that is neither a tag line nor an item of `create`, `update`, `delete` or `defer` is refused as before.

> **tasks:**
> - [ ] create `estimate-spec-write-reads-a-new-tag`
>   - ref: `rule-spec-write`
>   - kind: `QA`
>   - purpose: `Whether the Spec hook turns a tag line of a Case file into an entry of new_tags in the then block, leaves it out of the tasks block, and refuses a tag line off the form, and whether the check of the Case file reads the line alike`
>   - method: `uv run pytest tests/test_ratified.py tests/test_casecheck.py -k tag`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-spec-write`
>   - old: `nothing of the Case is written (case 436.1).`
>   - new: `` nothing of the Case is written (case 436.1). A task line that opens with `tag` and the tag in its first code span declares a new tag: its sub-points `meaning` and `aliases`, each one code span, make one entry of `new_tags` in the block tagged `then`, which `guppi materialize` carries to `guppi generate`, and the line stands in no block tagged `tasks`, since it is no task; a tag line with either sub-point missing, with another sub-point or with a value that is not one code span is refused, exit 2, and nothing of the Case is written (case 702). ``
>   - change: `a task line tag with the sub-points meaning and aliases declares a new tag into new_tags of the then block and stands in no tasks block (case 702)`
> - [ ] update `rule-case-protocol`
>   - old: `inside it (case 444.3); a Case off this form is not written`
>   - new: `` inside it (case 444.3); a task line that opens with `tag` and the tag in its first code span, with the sub-points `meaning` and `aliases`, each one code span, declares a new tag: the hook makes it an entry of `new_tags` in the `then` block and leaves it out of the `tasks` block, since it is no task (case 702); a Case off this form is not written ``
>   - old: `` New tags are declared under `new_tags` with a meaning and a {{chat_lang}} alias, under any Case of the Spec (case 61). ``
>   - new: `` New tags are declared under `new_tags` with a meaning and a {{chat_lang}} alias, under any Case of the Spec (case 61); in the file of a Case by a task line `tag` with the sub-points `meaning` and `aliases`, which the hook of `rule-spec-write` turns into that entry (case 702). ``
>   - change: `a Case file declares a new tag by a task line tag with the sub-points meaning and aliases (case 702)`
> - [ ] `guppi/ratified.py`: `read_tasks` reads a task line `` tag `<tag>` `` and its sub-points `meaning` and `aliases` into an entry of `new_tags`, keeps the line out of the task lines, and refuses a missing or a foreign sub-point; the docstring says so.
> - [ ] `tests/test_ratified.py`: a Case with two tag lines writes two entries of `new_tags` in the `then` block in their order and no tag line in the `tasks` block; a tag line with `aliases` missing, with a foreign sub-point, or with a value that is not one code span is refused and writes nothing; a sub-point under a plain task line is still refused.
> - [ ] `tests/test_casecheck.py`: the check of a Case file with a tag line passes with no finding, and one with a tag line off the form gives the refusal of the hook as a finding.
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-spec-write-reads-a-new-tag`

> **ratification:**
> ```
> - decision[case 702][create][estimate-spec-write-reads-a-new-tag]{ref:rule-spec-write}{tags:hooks,harness,workflow}
> - decision[case 702][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 702][update][rule-case-protocol]{ref:rule-case-protocol}
> ```
