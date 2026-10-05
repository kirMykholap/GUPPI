## Case 660 — One reading of a supersedes tag on a parent Case

> **context:**
> A decision line retires an earlier Case by the tag `{supersedes:case N}`. Today three scripts read the tag in two ways. The Spec hook, `remove_case` of `guppi/ratified.py`, removes Case N with all its sub-cases from the plan. `prespec.superseded_in_window` and `materialize.mark_superseded` retire only the number named. In session 1343 Case 658 put off Case 653 with the one tag `{supersedes:case 653}`. The decision lines of 653 belonged to 653.1 and 653.2. The Spec hook removed all three sections. `uv run guppi prespec --check` printed three findings "no Case 653.x heading in the plan", and `materialize` would have applied the three updates the person put off. Case 659 replaced the defer with a tag for each number (lesson `lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases`, clustered under `insight-harness-one-rule-implemented-twice-drifts`). The person chose the reading of the Spec hook: a tag on N retires N and its sub-cases at any depth. One function `in_family` in `guppi/materialize.py` gives that reading, and the Spec hook, `prespec`, `materialize` and the clash check of `guppi/casecheck.py` import it. `casecheck` already left out the family of a retired Case by its own copy of `in_family`, which gives way to the import. The Decision pages of the sub-cases that stand `current` become `superseded` with their parent. An archived or superseded sub-case page is left as it is. `decision-case-469` put off the round trip of an archived Decision page that a later Case supersedes: today `generate` sets such a page `superseded` again, `guppi cleanup` brings it back from the archive, and the cascade archives it again. Case 660.3 adds no such round trip, and the question of `decision-case-469` stays open for the page a tag names. The Retro and handoff texts say the same. A Grep of `supersedes` over `guppi/` printed `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/prespec.py`, `guppi/materialize.py`, `guppi/generate.py` and `guppi/pages.py`. `pages.py` only lists the field name. `generate` reads the marks through the `superseded_by` that `materialize` writes, and it changes only for the Decision pages (Case 660.3). `prespec.decided_on_its_page` (case 467) keeps its exact reading. It asks for a tag on each Case of a page's `deferred_by` by its own number, and `generate` clears a `deferred_by` only through such a tag, which 660.3 keeps. The two stay stricter than the family reading, and they agree with each other. The person kept the tag per number that the check of case 610.1 asks for, so `estimate-case-check-sends-back-a-ratified-case-in-another-shape` stands. The extra tags retire nothing more. A Grep of `names it in .supersedes.` over `vault/wiki/` without `decisions/` printed `vault/wiki/glossary.md`, `vault/wiki/rules/rule-decisions-schema.md` and `vault/wiki/entities/entity-glossary.md`. The sentence on `superseded` turns false for a sub-case page, so 660.3 changes it on `rule-decisions-schema` and in the glossary row, and `glossary.md` follows by its command. A Grep of `marks every entry of its Case` over the same paths printed `vault/wiki/glossary.md` and `vault/wiki/entities/entity-glossary.md`; 660.2 changes the row. A Grep of `` \{supersedes:case N\}` line `` over `vault/wiki/` and `.claude/` without `decisions/` printed `.claude/skills/retro/SKILL.md`, `.claude/skills/handoff/SKILL.md`, `vault/wiki/rules/rule-handoff.md` and `vault/wiki/rules/rule-retro.md`; 660.4 changes the two Renders. Some Estimates stand:
> `estimate-spec-write-removes-a-superseded-case` already promises the family reading, and only the source of the judgment moves.
> `estimate-materialize-refolds-a-reading-on-a-supersede` follows the marking that 660.2 widens, and its lines stay true.
> `estimate-case-check-sends-back-a-clash-with-another-case` names a Case whose number a mark names, which stays true, and its code already left out the family.
> `estimate-retro-loads` no longer speaks of the tag.
> `estimate-decisions-schema-checked` speaks of the lists and the body of the schema, not of the meaning of `superseded`.
> Each other copy of the test "N or one of its sub-cases" in `guppi/` serves another job and stays, by the person's choice.
> The ask-guppi run at `/pre-spec` named more Estimates whose Criterion speaks of the tag or of its mark, and each stands. The `－` line of `estimate-prespec-requires-a-task-line` stays true for the Case a tag names; for its sub-cases, 660.1 promises the same. The first line of `estimate-prespec-matches-lines-and-items` already gives way to the exception that `estimate-prespec-catches-a-superseded-case` promises, and 660.1 widens that exception there. `estimate-generate-fails-alone`, `estimate-generate-ticks-the-spec`, `estimate-raw-archive`, `estimate-sprint-ticks-the-spec`, `estimate-render-harness-ticks-the-spec` and `estimate-glossary-ticks-the-spec` speak of an entry that carries `superseded_by`, whoever set it; after 660.2 more entries carry it, and their lines stay true. `estimate-generate-cascades` archives a Decision page that stands `superseded`, and it touches neither `superseded_by` nor `deferred_by`; after 660.3 it archives the sub-case pages too. A `defer` target of such a page keeps its `deferred_by` until a tag names that sub-case itself, as case 467 sets. `estimate-handoff-holds-each-fact-once` says that `## What actually got done` holds the ids of the Cases ratified, which stays true; the new Estimate of 660.4 promises which Cases count. `estimate-glossary-terms-defined` asks that no row contradict its `where` page. The row on the status of a Decision changes as `rule-decisions-schema` does, in 660.3. The row of `supersedes` points to `rule-case-protocol`, and its paragraph on a tag on a sub-case agrees with the new row.

> **problem:**
> One tag `{supersedes:case N}` on a parent Case means two different things in three scripts. As a result, a short defer of a parent fails at `/pre-spec`, and the librarian would apply the work the person put off.

> **recommend:**
> - **What a tag on a parent retires**
>   - Recommended: (a) the parent and all its sub-cases, in all three scripts; a tag on N.M retires N.M and its own sub-cases only.
>   - Answer: agreed, (a).
> - **Which code shares the one test of "N or one of its sub-cases"**
>   - Recommended: (a) only the readers of the retire tag call one function of `guppi/materialize.py`: the Spec hook, the pre-spec check, `materialize` and the clash check of `casecheck`; the other copies stay.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) a sub-case for each script that changes, each replacing the Criterion of its Estimate and naming the shared function; the Estimate of the Spec hook stands.
>   - Answer: agreed, (a).
> - **Whether the Decision pages of the sub-cases become `superseded` too**
>   - Recommended: (a) yes: `generate` sets each page of the `children` of a superseded page, at any depth, `superseded`, with its own sub-case and a new Criterion of `estimate-generate-writes-the-decision-page`.
>   - Answer: agreed, (a).
> - **How many tags the check asks for when a Case is rebuilt in another shape**
>   - Recommended: (a) keep one tag per number; the check, its Estimate and the paragraph of `case-schema.md` stay.
>   - Answer: agreed, (a).
> - **Whether the Retro and handoff texts read the tag the same way**
>   - Recommended: (a) yes: both texts say the tag covers the sub-cases, in a fourth sub-case with a new Estimate read by hand at a later Retro.
>   - Answer: agreed, (a).
> - **What happens to a sub-case's Decision page that is already archived**
>   - Recommended: (a) only sub-case pages that stand `current` change; an archived or superseded one stays as it is, and the question `decision-case-469` put off stays open.
>   - Answer: agreed, (a).

### Case 660.1 — The pre-spec check reads a tag on a parent with its sub-cases

> **given:**
> `estimate-prespec-catches-a-superseded-case`: its Criterion is replaced whole.
> **＋** `guppi/prespec.py`: `superseded_in_window`, `check_lines`, `check_tasks` and the module docstring.
> **＋** `tests/test_prespec.py`: the tests of a tag on a parent.
> **＋** `guppi/materialize.py`: `in_family`, the one test of a tag, which Case 660.2 writes.
> **＋** `rule-prespec`: the rule whose check `estimate-prespec-catches-a-superseded-case` reads.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads a plan and the record lines of the session's window, and a decision line of the window carries `{supersedes:case N}`.

> **then:**
> A `{supersedes:case N}` in the session's window while `## Case N` or `### Case N` still stands in the plan is a finding `case N: superseded by case M, still in the plan`.
> **＋** A heading of a sub-case of Case N, at any depth, that still stands in the plan is the same finding under the number of that sub-case.
> **＋** A decision line of Case N or of a sub-case of Case N, N superseded by a line of the window, is no finding "no Case N heading", needs no item in the plan and asks for no `tasks` block.
> **＋** A `{supersedes:case N.M}` covers Case N.M and its own sub-cases; the parent with its other sub-cases stays.
> **＋** Whether a tag covers a Case is judged by `in_family` of `guppi/materialize.py`, the function that the Spec hook and `guppi materialize` read the tag by.
> **－** A `{supersedes:case N}` on a Case of an earlier session — a defer taken up — finds no heading N in the plan and is no finding.

> **tasks:**
> - [ ] `guppi/prespec.py`: `superseded_in_window` and its callers read each tag by `materialize.in_family`, in `check_lines` and `check_tasks`; the module docstring says that the lines and headings of the sub-cases of a superseded Case are covered.
> - [ ] `tests/test_prespec.py`: a tag on a parent whose sub-cases hold the decision lines gives no "no heading" finding and asks for no item; a sub-case heading left in the plan is a finding; a tag on N.M leaves the parent and its other sub-cases.
> - [ ] update `estimate-prespec-catches-a-superseded-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a tag on a parent covers its sub-cases, by materialize.in_family (case 660.1)`
> - [ ] read `estimate-prespec-catches-a-superseded-case`

> **ratification:**
> ```
> - decision[case 660.1][update][estimate-prespec-catches-a-superseded-case]{ref:rule-prespec}
> ```

### Case 660.2 — materialize marks the sub-cases of a superseded Case, by one function

> **given:**
> `estimate-materialize-marks-superseded`: its Criterion is replaced whole.
> **＋** `guppi/materialize.py`: the new `in_family`, `mark_superseded`, the marks of the `decisions` records in `assemble`, and the module docstring.
> **＋** `tests/test_materialize.py`: the tests of the supersedes mark.
> **＋** `guppi/ratified.py`: `remove_case`, which reads the tag by `in_family`.
> **＋** `guppi/casecheck.py`: its own `in_family`, which gives way to the import.
> **＋** `guppi/prespec.py`: the pre-spec check, which imports `in_family` by Case 660.1.
> **＋** `entity-glossary`: the row of `supersedes`.

> **when:**
> `uv run guppi materialize` lifts a decision line that carries one `{supersedes:case N}` block or several, and the entries of each Case N, or of its sub-cases, stand in this unit's `materialize.yaml` or in the `materialize.yaml` of another unit.

> **then:**
> For each Case N that a block of the line names, every entry with `case: N` gets `superseded_by`, whatever its kind, and the `decisions` record of that Case gets it too.
> **＋** So does every entry and every `decisions` record of a sub-case of Case N at any depth. A block that names Case N.M marks N.M and its own sub-cases, and leaves its parent and its other sub-cases.
> **＋** The entry of the line carries `supersedes` as a list with one Case per block, in the order of the blocks. The `decisions` record of its Case lists under `supersedes` every Case that its lines name.
> **＋** The `materialize.yaml` of another unit is written with that mark only.
> **＋** An entry marked while no heading of its own Case stands in the unit's `spec.md` carries no `incomplete: [then]`, and its `decisions` record no `case_text` and no `incomplete` for a section.
> **＋** Whether a block covers a Case is judged by `in_family` of `guppi/materialize.py`; `remove_case` of `guppi/ratified.py`, `guppi/prespec.py` and `guppi/casecheck.py` import it.
> **－** An entry without `case` — an `estimate` or a `lesson` entry — gets no mark.
> **－** An entry of an existing `materialize.yaml` whose `supersedes` is one value, not a list, is read as a list of one.

> **tasks:**
> - [ ] `guppi/materialize.py`: `in_family(case, top)`, true when `case` is `top` or a sub-case of it at any depth; `mark_superseded` and the marks of the `decisions` records in `assemble` mark every Case it covers, here and in another unit, and refold the readings of each; the docstring says so.
> - [ ] `guppi/ratified.py`: `remove_case` judges each section by `materialize.in_family`.
> - [ ] `guppi/casecheck.py`: `in_family` imported from `guppi/materialize.py`, its own definition removed.
> - [ ] `tests/test_materialize.py`: a tag on a parent with no lines of its own marks the entries and the records of its sub-cases, in this unit and in another; a tag on N.M leaves the parent and its other sub-cases.
> - [ ] update `estimate-materialize-marks-superseded`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a tag marks the Case and its sub-cases, by in_family (case 660.2)`
> - [ ] update `entity-glossary`
>   - old: `each of which marks every entry of its Case superseded`
>   - new: `each of which marks every entry of its Case and of its sub-cases superseded`
>   - change: `the row of supersedes: a tag marks the sub-cases too (case 660.2)`
> - [ ] `uv run guppi glossary`
> - [ ] read `estimate-materialize-marks-superseded`

> **ratification:**
> ```
> - decision[case 660.2][update][estimate-materialize-marks-superseded]{ref:rule-materialize}
> - decision[case 660.2][update][entity-glossary]{ref:entity-glossary}
> ```

### Case 660.3 — A superseded Decision page takes the pages of its sub-cases with it

> **given:**
> `estimate-generate-writes-the-decision-page`: its Criterion is replaced whole.
> **＋** `guppi/generate.py`: `decision` and the module docstring.
> **＋** `tests/test_generate.py`: the tests of the Decision page.
> **＋** `rule-page-generation`: the paragraph on the Decision page.
> **＋** `rule-decisions-schema`: the meaning of `superseded`, rendered into `vault/wiki/decisions/schema.yaml`.
> **＋** `entity-glossary`: the row of the status of a Decision.
> **＋** `vault/wiki/decisions/decision-case-<N>.md`: the Decision page of a Case, which `guppi/generate.py` writes.

> **when:**
> `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

> **then:**
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
> **＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded` and appends to its `superseded_by`, and does the same to each page in the `children` of the earlier page, at any depth, that stands `current`, a page of an earlier session too. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
> **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`; neither does a page reached only through `children` clear a `deferred_by`.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
> **－** The Decision pages already written are not rewritten.
> **－** A page whose `superseded_by` already names the new page gets no second History line.
> **－** A page in `children` that stands `archived` or `superseded` is left as it is.
> **－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.

> **tasks:**
> - [ ] `guppi/generate.py`: `decision` sets each page of the `children` of a superseded page, at any depth, that stands `current` `superseded`, leaves an archived or superseded one as it is, appends the new page to its `superseded_by` and writes its History line once; `clear_deferred_by` runs only on the pages the record's `supersedes` names; the docstring says so.
> - [ ] `tests/test_generate.py`: a `supersedes` of a parent page sets its sub-case pages `superseded`, in the same run and on pages of an earlier run; a child page already marked gets no second History line; an archived child page stays archived and gains no `superseded_by`; a child's `defer` targets keep their `deferred_by`.
> - [ ] update `estimate-generate-writes-the-decision-page`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a superseded page takes the pages of its children with it (case 660.3)`
> - [ ] update `rule-page-generation`
>   - old: `and its status follows the mechanism as for any superseded page (case 299.4);`
>   - new: `` and its status follows the mechanism as for any superseded page (case 299.4); a page that a later Case supersedes takes the pages of its `children` with it, at any depth: each that stands `current` becomes `superseded` and names the later Decision in `superseded_by`, an archived or superseded one is left as it is, and no `deferred_by` is cleared through them (case 660.3); ``
>   - change: `a superseded Decision page takes the pages of its sub-cases with it (case 660.3)`
> - [ ] update `rule-decisions-schema`
>   - old: `` `superseded` once a later Case names it in `supersedes`, and `archived` ``
>   - new: `` `superseded` once a later Case names it, or the page of a Case it is a sub-case of, in `supersedes`, and `archived` ``
>   - change: `the page of a sub-case is superseded with its parent (case 660.3)`
> - [ ] update `entity-glossary`
>   - old: `` `superseded` once a later Case names it in `supersedes`, `archived` ``
>   - new: `` `superseded` once a later Case names it, or the page of a Case it is a sub-case of, in `supersedes`, `archived` ``
>   - change: `the row of the status of a Decision: the page of a sub-case is superseded with its parent (case 660.3)`
> - [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] `uv run guppi glossary`
> - [ ] read `estimate-generate-writes-the-decision-page`

> **ratification:**
> ```
> - decision[case 660.3][update][estimate-generate-writes-the-decision-page]{ref:rule-page-generation}
> - decision[case 660.3][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 660.3][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 660.3][update][entity-glossary]{ref:entity-glossary}
> ```

### Case 660.4 — Retro and the handoff leave out the sub-cases of a superseded Case

> **given:**
> `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`: the new check of the two texts.
> **＋** `rule-retro`: its Render, the text of `.claude/skills/retro/SKILL.md`.
> **＋** `rule-handoff`: its Render, the text of `.claude/skills/handoff/SKILL.md`.

> **when:**
> The skill of `rule-retro` sorts the boxes of a session whose ledger holds a decision line carrying `{supersedes:case N}`, Case N having sub-cases with decision lines, and the skill of `rule-handoff` then writes `handoff.md`.

> **then:**
> Retro counts no line of Case N or of any of its sub-cases as debt.
> **＋** The `## What actually got done` section of `handoff.md` lists neither Case N nor any of its sub-cases among the Cases ratified.
> **－** A tag that names Case N.M leaves out N.M and its own sub-cases only; the parent and its other sub-cases are counted.

> **tasks:**
> - [ ] create `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`
>   - ref: `rule-retro`
>   - kind: `QA`
>   - purpose: `Whether Retro and the handoff leave out the sub-cases of a Case that a supersedes tag names`
>   - method: `by hand at a /retro whose session ledger holds a {supersedes:case N} on a Case N whose sub-cases have decision lines: the debt Retro sorts and the Cases that handoff.md lists`
>   - tags: `[session, workflow, harness]`
> - [ ] update `rule-retro`
>   - old: `` The lines of a Case that a `{supersedes:case N}` line of the Tail names are not counted at all; ``
>   - new: `` The lines of a Case that a `{supersedes:case N}` line of the Tail names, and of its sub-cases, are not counted at all; ``
>   - change: `a supersedes tag leaves the sub-cases of its Case out of the debt (case 660.4)`
> - [ ] update `rule-handoff`
>   - old: `` a Case that a `{supersedes:case N}` line names not counted; ``
>   - new: `` a Case that a `{supersedes:case N}` line names, and each of its sub-cases, not counted; ``
>   - change: `a supersedes tag leaves the sub-cases of its Case out of what got done (case 660.4)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] read `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`

> **ratification:**
> ```
> - decision[case 660.4][create][estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case]{ref:rule-retro}{tags:session,workflow,harness}
> - decision[case 660.4][update][rule-retro]{ref:rule-retro}
> - decision[case 660.4][update][rule-handoff]{ref:rule-handoff}
> ```
