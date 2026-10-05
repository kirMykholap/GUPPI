<!-- approved 17:57:18 · session 6360af9f -->

# Spec — session 1616, 2026-10-05

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

```then
update:
- slug: estimate-prespec-catches-a-superseded-case
  set:
    status: pending
  change: the Criterion replaced whole — a tag on a parent covers its sub-cases, by materialize.in_family (case 660.1)
```

```tasks
- [x] `guppi/prespec.py`: `superseded_in_window` and its callers read each tag by `materialize.in_family`, in `check_lines` and `check_tasks`; the module docstring says that the lines and headings of the sub-cases of a superseded Case are covered.
- [x] `tests/test_prespec.py`: a tag on a parent whose sub-cases hold the decision lines gives no "no heading" finding and asks for no item; a sub-case heading left in the plan is a finding; a tag on N.M leaves the parent and its other sub-cases.
- [x] update `estimate-prespec-catches-a-superseded-case`
- [ ] read `estimate-prespec-catches-a-superseded-case`
```

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

```then
update:
- slug: estimate-materialize-marks-superseded
  set:
    status: pending
  change: the Criterion replaced whole — a tag marks the Case and its sub-cases, by in_family (case 660.2)
- slug: entity-glossary
  replace:
  - old: each of which marks every entry of its Case superseded
    new: each of which marks every entry of its Case and of its sub-cases superseded
  change: 'the row of supersedes: a tag marks the sub-cases too (case 660.2)'
```

```tasks
- [x] `guppi/materialize.py`: `in_family(case, top)`, true when `case` is `top` or a sub-case of it at any depth; `mark_superseded` and the marks of the `decisions` records in `assemble` mark every Case it covers, here and in another unit, and refold the readings of each; the docstring says so.
- [x] `guppi/ratified.py`: `remove_case` judges each section by `materialize.in_family`.
- [x] `guppi/casecheck.py`: `in_family` imported from `guppi/materialize.py`, its own definition removed.
- [x] `tests/test_materialize.py`: a tag on a parent with no lines of its own marks the entries and the records of its sub-cases, in this unit and in another; a tag on N.M leaves the parent and its other sub-cases.
- [x] update `estimate-materialize-marks-superseded`
- [x] update `entity-glossary`
- [x] `uv run guppi glossary`
- [ ] read `estimate-materialize-marks-superseded`
```

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

```then
update:
- slug: estimate-generate-writes-the-decision-page
  set:
    status: pending
  change: the Criterion replaced whole — a superseded page takes the pages of its children with it (case 660.3)
- slug: rule-page-generation
  replace:
  - old: and its status follows the mechanism as for any superseded page (case 299.4);
    new: 'and its status follows the mechanism as for any superseded page (case 299.4); a page that a later Case supersedes takes the pages of its `children` with it, at any depth: each that stands `current` becomes `superseded` and names the later Decision in `superseded_by`, an archived or superseded one is left as it is, and no `deferred_by` is cleared through them (case 660.3);'
  change: a superseded Decision page takes the pages of its sub-cases with it (case 660.3)
- slug: rule-decisions-schema
  replace:
  - old: '`superseded` once a later Case names it in `supersedes`, and `archived`'
    new: '`superseded` once a later Case names it, or the page of a Case it is a sub-case of, in `supersedes`, and `archived`'
  change: the page of a sub-case is superseded with its parent (case 660.3)
- slug: entity-glossary
  replace:
  - old: '`superseded` once a later Case names it in `supersedes`, `archived`'
    new: '`superseded` once a later Case names it, or the page of a Case it is a sub-case of, in `supersedes`, `archived`'
  change: 'the row of the status of a Decision: the page of a sub-case is superseded with its parent (case 660.3)'
```

```tasks
- [x] `guppi/generate.py`: `decision` sets each page of the `children` of a superseded page, at any depth, that stands `current` `superseded`, leaves an archived or superseded one as it is, appends the new page to its `superseded_by` and writes its History line once; `clear_deferred_by` runs only on the pages the record's `supersedes` names; the docstring says so.
- [x] `tests/test_generate.py`: a `supersedes` of a parent page sets its sub-case pages `superseded`, in the same run and on pages of an earlier run; a child page already marked gets no second History line; an archived child page stays archived and gains no `superseded_by`; a child's `defer` targets keep their `deferred_by`.
- [x] update `estimate-generate-writes-the-decision-page`
- [x] update `rule-page-generation`
- [x] update `rule-decisions-schema`
- [x] update `entity-glossary`
- [x] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [x] `uv run guppi glossary`
- [ ] read `estimate-generate-writes-the-decision-page`
```

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

```then
create:
- slug: estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case
  ref: rule-retro
  kind: QA
  purpose: Whether Retro and the handoff leave out the sub-cases of a Case that a supersedes tag names
  method: 'by hand at a /retro whose session ledger holds a {supersedes:case N} on a Case N whose sub-cases have decision lines: the debt Retro sorts and the Cases that handoff.md lists'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-retro
  replace:
  - old: The lines of a Case that a `{supersedes:case N}` line of the Tail names are not counted at all;
    new: The lines of a Case that a `{supersedes:case N}` line of the Tail names, and of its sub-cases, are not counted at all;
  change: a supersedes tag leaves the sub-cases of its Case out of the debt (case 660.4)
- slug: rule-handoff
  replace:
  - old: a Case that a `{supersedes:case N}` line names not counted;
    new: a Case that a `{supersedes:case N}` line names, and each of its sub-cases, not counted;
  change: a supersedes tag leaves the sub-cases of its Case out of what got done (case 660.4)
```

```tasks
- [x] create `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`
- [x] update `rule-retro`
- [x] update `rule-handoff`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
- [ ] read `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`
```

## Case 661 — The tests of the orchestration examples fail when the page holds no example

> **context:**
> `tests/test_orchestration.py` reads two examples from `vault/wiki/orchestration.md`, the block tagged `showing` and the block tagged `defer`, and runs over each the check that the scripts run over a real reply: the `Stop` check of `rule-case-check` over a showing, and the `Stop` hook of `rule-spec-write` over a short-form defer. Case 651 made the tests skip, with a reason that names the file, while the page held no such block, because the examples reached the page only at the librarian's render. The render has put both examples there, and at the `/hi` of this session the readings of `estimate-orchestration-showing-example-passes-the-check` and `estimate-orchestration-defer-example-passes-the-hook` both passed, with none skipped. The skip still stands in the code. A skip leaves `make test` green, so a later render that lost a block or changed its tag would leave that example unchecked with no one told. The person chose that the tests fail, with a message that names the file, when the page holds no such block: the same behaviour Case 652 gave `tests/test_case_schema.py`.
>
> The last `－` line of the Criterion of each of the two Estimates says the test is skipped, so this Case makes it false. Each Estimate is a separate promise, so each is a sub-case that replaces its Criterion whole: the same lines, with that line rewritten to say that the tests that read the block fail and no test of the file is skipped. Both pages go `pending`. The two `passed` readings at lines 1 and 2 of this session's ledger were taken at the `/hi`, before this Case existed. They stand before its decision lines and are the ground of the Case. The `update` lines that follow them set both Estimates `pending`, so the librarian records the reading first and the replaced Criterion after it. `estimate-case-protocol-example-passes-the-check` went through the same order in session 1343: its History holds the `passed` reading from that session's ledger, then the update of case 652, and its `status` is `pending`. No new reading of either Estimate is taken in this session. The readings are taken at the `/hi` of a later session, since `rule-retro` says that an Estimate this session creates or updates has no reading in this session, and the ledger hook refuses one (case 428.1). The `purpose` of neither Estimate speaks of the skip, so both stand. Each `method` reads "passed and not skipped", which stays true once no skip remains, so both stand. The skip lives in one function, `example`, which both pairs of tests call, so the code change is one task on Case 661.1 and covers Case 661.2 too. The test only goes red and loses nothing, so it keeps no old form. The defer Criterion said its Insight stands `actioned`, addressed by this Case; in the new Criterion it names case 651.3, the Case that addressed it, since this Case does not. So three old lines are not carried word for word, by intent: the skip line of each Criterion and the Insight line of the defer Criterion. Some `then` lines of the two sub-cases share most of their words, also by intent: the two Estimates check two examples of one page in the same way, and each line names its own block, check or hook. The `－` line of `estimate-guppi-tests-green` that says a skipped test is not a failure stands: after this Case these tests fail rather than skip, which is the behaviour the person chose. This Case changes neither `rule-orchestration` nor its page.
>
> The search this Case rests on. A Grep of `test_orchestration|estimate-orchestration-showing-example-passes-the-check|estimate-orchestration-defer-example-passes-the-hook` over the repository root, with the glob `!**/decisions/** !**/raw/** !**/log.md !**/brief.md`, printed 4 files: `tests/test_orchestration.py`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-orchestration-defer-example-passes-the-hook.md` and `vault/wiki/estimates/estimate-orchestration-showing-example-passes-the-check.md`. On `rule-orchestration` the hits are its `estimates` field and two History lines, which stand. The other three enter the Case.

> **problem:**
> `tests/test_orchestration.py` still skips when `vault/wiki/orchestration.md` holds no `showing` or `defer` example, though both examples now stand there and both readings passed. A lost example would go unchecked while the tests stay green. The question was what the tests do when the page holds no example.

> **recommend:**
> - **What the test does when the page has no example**
>   - Recommended: (a) fail with a message that names the file.
>   - Answer: agreed, (a).

### Case 661.1 — The showing tests fail when the page holds no showing example

> **given:**
> `tests/test_orchestration.py`: the tests that run the checks over the examples.
> **＋** `estimate-orchestration-showing-example-passes-the-check`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the page that holds the examples, rendered from `rule-orchestration`. Unchanged.
> **＋** `rule-orchestration`: the rule whose Render is that page. Unchanged.
> **＋** `guppi/casecheck.py`: the check of a reply that shows a Case, which the test imports. Unchanged.
> **＋** `rule-case-check`: its `Stop` check runs over a reply that shows a Case. Unchanged.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `showing` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it the functions of `guppi/casecheck.py` that the `Stop` check of `rule-case-check` runs over a reply that shows a Case, with a store whose sub-cases hold the ledger lines the example's `ratification` gives them.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## Showing and signing a Case`, one block tagged `showing`: a reply that shows a Case with two sub-cases, its heading, one list with an item per sub-case, one `ratification` and the agent's own text after one horizontal rule.
> **＋** The `ratification` of the example is a quote block: the line `> **ratification:**`, then the fence and the ledger lines of both sub-cases, each line opening with `> `.
> **＋** The example is in English; the paragraph before the block says that in the chat the heading, the names and the short texts stand in the language of the chat, that the file goes by `SendUserFile` in the same reply, and that the example passes the `Stop` check of `rule-case-check`, which is the source of the limits; it lists no other limit.
> **＋** The check finds no text outside the list and the `ratification`, reads the `ratification` as the showing of each sub-case it names, and finds no difference from the store, and the test passes.
> **＋** The example with the lines of its fence not quoted gives the finding of a text outside the list, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `showing`, both tests of `tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

```then
update:
- slug: estimate-orchestration-showing-example-passes-the-check
  set:
    status: pending
  change: the Criterion replaced whole — the tests fail, not skip, when orchestration.md holds no block tagged showing (case 661.1)
```

```tasks
- [x] update `estimate-orchestration-showing-example-passes-the-check`
- [x] `tests/test_orchestration.py`: `example` calls `pytest.fail` with a message that names the file and the tag, in place of `pytest.skip`, when the page holds no block tagged that tag; the module docstring says the tests fail then and drops the sentences on the skip.
- [ ] read `estimate-orchestration-showing-example-passes-the-check`, at the `/hi` of a later session
```

### Case 661.2 — The defer tests fail when the page holds no defer example

> **given:**
> `tests/test_orchestration.py`: the tests that run the hook over the examples.
> **＋** `estimate-orchestration-defer-example-passes-the-hook`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the page that holds the examples, rendered from `rule-orchestration`. Unchanged.
> **＋** `rule-orchestration`: the rule whose Render is that page. Unchanged.
> **＋** `guppi/ratified.py`: the hook that writes a defer-only Case into the Spec, which the test imports. Unchanged.
> **＋** `rule-spec-write`: its `Stop` hook writes a defer-only Case under `## Deferred`. Unchanged.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept`: the Insight the Criterion names. Unchanged.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `defer` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it, as the text of a reply, the functions of `guppi/ratified.py` that the `Stop` hook of `rule-spec-write` runs over a defer-only Case, in a temporary project that holds the schema files of the vault and a plan file, with one `defer` record for each item of the example.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## The short form — deferred decisions`, one block tagged `defer`: a Case in the short form with its heading, `context`, `problem` and a fence tagged `then` whose `defer:` holds a list, one item per target, each item opening with `- slug:` and carrying `type` and `purpose`.
> **＋** The paragraph before the block says that the reply that shows the Case carries its `LEDGER` block with one `defer` line per item, and that the example passes the `Stop` hook of `rule-spec-write`, which is the source of the limits; it lists no other limit.
> **＋** The hook writes the example under `## Deferred` of the plan file with no error, and the test passes.
> **＋** The example with its `defer:` items written as one mapping gives the error that no fence tagged `then` holds its `defer` items, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the hook from `guppi/ratified.py`, and holds no copy of either.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stands `actioned`, addressed by case 651.3.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `defer`, both tests of `tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

```then
update:
- slug: estimate-orchestration-defer-example-passes-the-hook
  set:
    status: pending
  change: the Criterion replaced whole — the tests fail, not skip, when orchestration.md holds no block tagged defer (case 661.2)
```

```tasks
- [x] update `estimate-orchestration-defer-example-passes-the-hook`
- [ ] read `estimate-orchestration-defer-example-passes-the-hook`, at the `/hi` of a later session
```

## Case 662 — The summary of case-guppi names the Case it built, and the heading of a showing takes that name

> **context:**
> When `case-guppi` has written a Case into its file, it answers the main agent with a summary: the path, then one list item per Case and sub-case with its Estimate and its ledger lines. A top-level Case with sub-cases has no Estimate and no ledger lines of its own, so `case-guppi` gives it no item, and no line of the summary holds its name. The main agent writes the showing from the summary and does not read the file (case 645.6), so it wrote the heading of the showing in its own words. In session 1343 Case 653 was shown under the words of Frontier item C3, and the reading of `estimate-orchestration-shows-the-built-case` failed on it (L36 of that session's ledger; lesson L44). In this session Cases 660 and 661 were shown under headings the main agent composed, not the names their files hold. The person chose three things: the summary carries, after its `**Built:**` line, a line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, and the main agent translates that name for the heading; the `SubagentStop` check of `rule-case-check` sends back a summary whose line is missing or differs from the file; and `insight-case-show-built-case-retyped-by-hand` stays open. The line is a bold label and not a Markdown heading, because `answer_of` of `guppi/casecheck.py` takes an output that holds a `## Case` heading as a Case to check, and would judge the summary as a faulty Case.
>
> Three promises change, so the Case has three sub-cases. Case 662.1 changes the summary in the Render of `rule-case-build` and replaces the Criterion of `estimate-case-build-writes-the-case`, whose summary line the change makes false. Case 662.2 changes the showing in the Render of `rule-orchestration` and replaces the Criterion of `estimate-orchestration-shows-the-built-case`, whose heading line said only that the name stands in Russian. Case 662.3 adds the check to `guppi/casecheck.py` and creates `estimate-case-check-sends-back-a-summary-without-the-case-name`, read by a test. The `purpose` and `method` of both replaced Estimates speak of a summary and of showings in general, not of where the heading takes its name, so they stand. The check is a reader in code that lands in Work Mode, while the new text of `.claude/agents/case-guppi.md` lands at the render; a `case-guppi` that builds a Case again before the render is sent back once with the line it must write, and nothing it wrote is lost, so the check keeps no old form. `guppi/casecheck.py` is changed by Case 660.2 too, in `in_family` of the clash check at the same `SubagentStop` moment; this Case touches the judgment of the summary only, so the two do not clash, and 662.3 names the case file of 660. The lesson of session 1343 gets no `{addresses}` mark, since its fix is ratified in another session (case 284.2). `insight-case-show-built-case-retyped-by-hand` stays open: its pattern is any line of a Case the main agent writes out by hand, and this Case fixes the heading alone.
>
> The check of the file noted lines of the two replaced Criteria that the new ones do not carry word for word: in `estimate-case-build-writes-the-case` the line on findings of the hook, the line of the summary and the line on findings and changes, and in `estimate-orchestration-shows-the-built-case` the line of the showing and the `－` line on what the main agent writes from the summary. Each is rewritten by intent, to add the `**Case:**` line, the finding on a summary, or the heading taken from that line; the rest of each Criterion is carried whole. It noted too that `then` lines of the three sub-cases share most of their words. That is by intent: the three Estimates check one summary from three sides, `case-guppi` that writes it, the main agent that reads it and the hook that checks it, and each line names its own actor.
>
> The searches this Case rests on. A Grep of `\*\*Built:\*\*` over the repository root, with the glob `!**/decisions/** !**/raw/**`, printed 7 files: `vault/wiki/orchestration.md`, `.claude/agents/case-guppi.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md`, `vault/wiki/rules/rule-case-build.md` and `tests/test_casecheck.py`. The two rendered files follow their rules at the render; the other five enter the Case. A Grep of `summary|Built` over `vault/wiki/estimates/` printed 6 files: the two Estimates above, which enter the Case; `estimate-case-build-answers-what-done-means`, whose line that the summary names the Estimate under each item stays true; `estimate-case-check-sends-back-a-faulty-case`, whose line that an output with no Case heading, a summary among them, is not read as a Case stays true, since the new check reads only the `**Case:**` line of a summary; and `estimate-ask-finds` and `estimate-synthesis-clusters`, which speak of other summaries.

> **problem:**
> The summary of `case-guppi` gives no name for a top-level Case with sub-cases, and the main agent may not read the file, so it shows the Case under a heading of its own words. The person ratifies a Case under a name its file does not hold. The question was where the heading takes its name, whether a script checks it, and what happens to the open Insight.

> **recommend:**
> - **Where the main agent gets the name of the heading**
>   - Recommended: (a) a labelled `**Case:**` line in the summary, right after `**Built:**`, with the id and name as the file's heading holds them, not a Markdown heading.
>   - Answer: agreed, (a).
> - **Whether a script checks that the summary names the top-level Case**
>   - Recommended: (a) the check that runs when `case-guppi` stops sends back a summary whose line is missing or differs from the file's heading.
>   - Answer: agreed, (a).
> - **What happens to the open Insight**
>   - Recommended: (a) leave it open; the `context` names it and says this Case fixes the heading part only.
>   - Answer: agreed, (a).

### Case 662.1 — The summary of case-guppi names the top-level Case

> **given:**
> `rule-case-build`: its Render is the instructions of `case-guppi`, which set the summary.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `rule-case-check`: its `SubagentStop` hook checks the file and the summary.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that `case-guppi` writes.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a round.
> **＋** `vault/wiki/case-schema.md`: the form of a Case, read by `case-guppi`.
> **＋** `vault/wiki/ratification.md`: the form of the ledger lines, read by `case-guppi`.
> **＋** `.claude/agents/ask-guppi.md`: the vault query that `case-guppi` runs before a `create` without a `ref`.
> **＋** `.claude/settings.json`: the hooks that `case-guppi` reads for a Case that changes a hook.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
> **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
> **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
> **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: acceptEdits`, so it writes its file with no prompt while the session is in Plan Mode.
> **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
> **－** It does not write the whole Case again to fix a finding or make a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, and no ledger line.

```then
update:
- slug: rule-case-build
  replace:
  - old: 'Then answer with the summary alone: a first line `**Built:**` and the path of the file, then one list item per Case and sub-case'
    new: 'Then answer with the summary alone: a first line `**Built:**` and the path of the file, a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, such as `**Case:** 7 — The cart stands before payment`, for a Case with sub-cases too, since the main agent takes the heading of its showing from it; the line is no Markdown heading, since the hook reads an answer that holds a Case heading as a Case, and the hook sends back a summary whose line is missing or gives another id or name than the heading of the file (case 662.1); then one list item per Case and sub-case'
  - old: when it sends findings back, fix the lines at fault by `Edit` and answer with the summary again, never by writing the whole Case again (case 645.1)
    new: when it sends findings back on the file, fix the lines at fault by `Edit` and answer with the summary again, never by writing the whole Case again (case 645.1); when it sends a finding back on the summary alone, answer with the summary again and leave the file as it stands (case 662.1)
  change: the summary names the top-level Case in a line **Case:** after its Built line (case 662.1)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  change: the Criterion replaced whole — the summary carries a line **Case:** with the id and the name of the top-level Case as the file heads it (case 662.1)
```

```tasks
- [x] update `rule-case-build`
- [x] update `estimate-case-build-writes-the-case`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-the-case`, by hand in a later session after the render
```

### Case 662.2 — The heading of a showing takes the name from the summary

> **given:**
> `rule-orchestration`: its Render sets what the main agent shows of a built Case.
> **＋** `vault/wiki/orchestration.md`: the page rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `rule-case-build`: it sets the summary that the main agent reads.
> **＋** `rule-case-check`: its checks of a built Case and of a showing.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that the main agent sends, under the folder `cases/`.
> **＋** `cases/`: the folder of the files of built Cases, which the main agent does not edit.
> **＋** `/wait-what`: the command by which the person asks for a plain explanation.
> **＋** `.claude/skills/wait-what/SKILL.md`: the skill by which the main agent explains in plain words.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a round that the main agent shows.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**` and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it; a reply that shows a round and that the `Stop` check refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, never to build a Case, and asks a run again only to confirm its own findings.
> **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

```then
update:
- slug: rule-orchestration
  replace:
  - old: '`case-guppi` answers with a summary of it — the path, then for each Case and sub-case its id'
    new: '`case-guppi` answers with a summary of it — the path, a line `**Case:**` with the id and the name of the top-level Case as the heading of its file writes them, then for each Case and sub-case its id'
  - old: in the same reply it writes the heading of the top-level Case, its name in {{chat_lang}}, and under it
    new: in the same reply it writes the heading of the top-level Case, its id and its name in {{chat_lang}} translated from the `**Case:**` line of the summary, never a name of its own or the words of the Frontier item (case 662.2), and under it
  change: the heading of a showing takes the name of the top-level Case from the Case line of the summary (case 662.2)
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — the heading of a showing is the id and the name of the Case line of the summary, translated (case 662.2)
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-shows-the-built-case`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-shows-the-built-case`, by hand at the close of a later session after the render
```

### Case 662.3 — The check of case-guppi sends back a summary that does not name its Case

> **given:**
> `estimate-case-check-sends-back-a-summary-without-the-case-name`: the new check of the line `**Case:**` of a summary.
> **＋** `rule-case-check`: the rule of the hook, whose Purpose names what it prevents.
> **＋** `guppi/casecheck.py`: the `SubagentStop` hook `guppi casecheck --subagent`.
> **＋** `tests/test_casecheck.py`: the tests of the hook.
> **＋** `vault/raw/2026-10-05/1616/cases/case-660.md`: Case 660.2 changes `in_family` of the same module, at the same hook.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case whose heading the check reads.
> **＋** `.claude/settings.json`: it registers the hook on `SubagentStop`.

> **when:**
> `case-guppi` stops after it wrote or edited a file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the `SubagentStop` hook `guppi casecheck --subagent` of `guppi/casecheck.py`, registered in `.claude/settings.json`, reads its newest output: a summary whose first line that is not blank opens with `**Built:**`.

> **then:**
> A summary with no line `**Case:**` for the top-level Case of a file it wrote, or with one whose id and name differ from the heading `## Case N — name` of that file, gets a finding that names the file and the line to write, and the hook exits 2.
> **＋** A summary whose `**Case:**` line gives the same id and the same name as the heading of each such file, trailing spaces aside, gets no finding on its line.
> **＋** A finding on the summary is sent back in the same exit 2 as the findings on the file.
> **＋** A summary sent back once is sent back again when the heading of its file has changed since, even if an earlier output holds its text.
> **－** A summary whose text an earlier output of the subagent already holds, trailing spaces aside, is not sent back again for its line while the heading of its file is the same as when it was sent back.
> **－** A round, a `**Fact:**` answer, and an answer with no file written are not judged for the line.

```then
create:
- slug: estimate-case-check-sends-back-a-summary-without-the-case-name
  ref: rule-case-check
  kind: QA
  purpose: Whether the check of case-guppi sends back a summary that does not name the top-level Case as its file heads it
  method: uv run pytest tests/test_casecheck.py -k summary_names_the_case
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: outside the list under its heading and its `ratification` (case 611); the Case reaches
    new: outside the list under its heading and its `ratification` (case 611), and a summary of `case-guppi` from reaching the main agent without the id and the name of the Case it built (case 662.3); the Case reaches
  set:
    purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi from being shown after a text of the main agent's own, a Case from being shown with a text of the main agent's own outside the list under its heading and its ratification, and a summary of case-guppi from reaching the main agent without the id and the name of the Case it built
  change: the SubagentStop check sends back a summary whose Case line is missing or differs from the heading of the file (case 662.3)
```

```tasks
- [x] create `estimate-case-check-sends-back-a-summary-without-the-case-name`
- [x] update `rule-case-check`
- [x] `guppi/casecheck.py`: in `subagent`, when the subagent wrote a file of `cases/` and its newest output opens with `**Built:**`, one function compares the `**Case:**` lines of that output with the top-level heading of each written file, read by `CASE_HEADING` of `guppi/materialize.py`, compares the id and the name of the line with those of the heading, not the whole line, and gives a finding for each one missing or different; the guard against a loop keys on the text of the summary, trailing spaces aside, and the heading of the file together, so an earlier summary with the same text gives no finding again only while the heading stands as it was; the findings join those of the files in one `send_back`; the module docstring describes the check.
- [x] `tests/test_casecheck.py`: tests named `summary_names_the_case` for each line of the `then`; the helpers that write a summary — the one beside `case_path` and `built` — give it its `**Case:**` line, so the tests of a passing file still pass.
- [ ] read `estimate-case-check-sends-back-a-summary-without-the-case-name`, at the `/hi` of a later session
```

## Case 664 — A hook leaves the Decision pages out of every search

> **context:**
> `rule-search-leaves-out-decisions` keeps the text of Decision pages out of the context of the agents. Today it is only text: `.claude/rules/search-leaves-out-decisions.md` tells the main agent, `ask-guppi` and `case-guppi` to add `!**/decisions/**` at the end of the glob of every Grep over the wiki. Its Estimate `estimate-search-leaves-out-decisions-in-every-agent` failed at the `/hi` of session 1343 (L10 of that session's ledger): the file stood in all seven contexts of session 0311, but 9 Greps over `vault/`, `vault/wiki/` or the root carried no exclusion, and `case-guppi` a1cf96ac9df5edd1c read `decision-case-432` because the `addressed_by` of an Insight named it, which is no reason of `.claude/agents/ask-guppi.md`. The handoff of 1343 adds that `ask-guppi` broke the rule again, once by putting the exclusion first. The order matters: a Grep of `^type: decision` over `vault/wiki/` with the glob `!**/decisions/** *.md` counted 1127 files, pages under `vault/wiki/decisions/` among them, and the same Grep with the glob `*.md !**/decisions/**` printed only `vault/wiki/rules/rule-decisions-schema.md`. Both probes printed counts and paths, no text of a Decision page.
>
> The person chose that a `PreToolUse` hook on Grep adds the exclusion at the end of the glob, like the hook of `rule-page-read` that cuts the History from a read by `updatedInput`, for every agent, the librarian too, since `.claude/agents/librarian-guppi.md` says its job does not need the text of a Decision page. The person kept the two reasons to open a Decision page, so the read through `addressed_by` stays a breach that the check counts. The person chose two checks. Case 664.1 builds the hook and creates `estimate-search-leaves-out-decisions-by-the-grep-hook`. Case 664.2 replaces the Criterion of `estimate-search-leaves-out-decisions-in-every-agent`, so that it reads only the load of the file and the reads of Decision pages, and sets its `purpose` and `method` anew, which named the Greps. The hook stays on `rule-search-leaves-out-decisions`, which keeps `enforcement: render` for its file and takes an `implementation_ref`, as `rule-ledger-tail` does; the rule keeps its Leaf, with two Estimates. The Render loses its two lines on the glob and gains one line on the hook. `.claude/settings.json` registers no hook on `PreToolUse` of Grep today, so the new one runs alone on its event. `estimate-hook-registry-rendered` stands: its Criterion speaks of the file equal to the Render, which a render update keeps (case 378.5). At pre-spec the main agent asked whether an agent may Grep inside `vault/wiki/decisions/`, since the Render of `rule-ask` lets `ask-guppi` open or grep that folder for its two reasons. The person chose that it may: the hook leaves unchanged a Grep whose `path` is that folder or lies in it, and the text of a Decision page reaches an agent by a Read of its path or by such a Grep, for a reason of its frame alone. So the Render of `rule-ask` stands, and 664.2 promises this. A Grep whose `path` is one file is left as it is too: the glob does not filter a file that is named directly. A Grep of `^type:` with the path `vault/wiki/decisions/decision-case-640.md` and the glob `!**/decisions/**` still counted 1 match in that file. Because the hook covers the librarian, 664.1 sets the `purpose` of `rule-search-leaves-out-decisions` anew and says so in its Purpose and Render. The file itself still binds only the three agents. The line of `.claude/agents/librarian-guppi.md` that says no read is forbidden to the librarian stays true: a Read of a Decision page, or a Grep inside its folder, still works, and still takes a line under Flags of the brief. `estimate-documentation-completes` stands for the same reason. Its Criterion line asks for a Flags line for each read of the text of a Decision page, and a Grep the hook filtered reads no such text.
>
> A Grep of `search-leaves-out-decisions` over the repository root, with the glob `!**/decisions/** !vault/raw/** !vault/archive/**`, printed 9 files. `vault/wiki/brief.md` and `vault/wiki/log.md` are not read. `rule-search-leaves-out-decisions` and `estimate-search-leaves-out-decisions-in-every-agent` enter the Case. `vault/wiki/rules/rule-harness.md` lists the rule as a child, which stays true. `vault/wiki/rules/rule-ask.md` and its render `.claude/agents/ask-guppi.md`, and `vault/wiki/estimates/estimate-ask-finds.md`, name a search that breaks a rule of the file; this stays true, since the file keeps its rule on the reads. The last `－` line of the Criterion of `vault/wiki/estimates/estimate-ask-searches-at-prespec.md` says that `estimate-search-leaves-out-decisions-in-every-agent` reads whether a Grep or a Read of the agent reaches `vault/wiki/decisions/`. After the split, that is false for the Grep. So Case 664.3 replaces that Criterion whole, with every other line as it stands. The Estimate is already `pending` from case 655. Its `purpose` names only a count over Decision pages that is not run again, and its `method` names no Decision page. Neither states what the replaced line said, so both stand. Cases 662 and 663 of this session change other pages and other moments, so this Case does not clash with them.
>
> The check of the file noted lines of the two replaced Criteria that the new ones do not carry word for word. In `estimate-search-leaves-out-decisions-in-every-agent`, the line on the Greps leaves for the new Estimate of 664.1, the `When:` line names a Read, or a Grep inside `vault/wiki/decisions/`, in place of Grep, Glob or Read, and the line on the reads names that Grep and the two reasons of the frame. In `estimate-ask-searches-at-prespec`, the last `－` line splits in two: one line for the Greps over a folder that holds the Decision pages, and one for the Reads and the Greps inside it. Each change is made by intent, and the rest of each Criterion is carried whole. The check noted too that the `－` lines of 664.2 and 664.3 that leave the Greps or the Reads to another Estimate share most of their words. That is by intent: each line bounds its own Estimate, and each names the other check. The `－` line of 664.1 on a Grep inside `vault/wiki/decisions/` and the line of 664.2 on how a Decision page may reach an agent also share words. That is by intent too: 664.1 says the hook lets such a Grep pass, and 664.2 says the agent runs it only for a reason of its frame.

> **problem:**
> The rule that keeps the text of Decision pages out of a search is text that loads but is not followed. Agents leave the exclusion out, or put it first, where it does not work. The questions were how the exclusion is enforced, whether a Decision page named by `addressed_by` may be opened, whether an agent may Grep inside the folder of the Decision pages, which agents the hook covers, and how the change is checked.

> **recommend:**
> - **How every search leaves out the Decision pages**
>   - Recommended: (a) a hook adds the exclusion at the end of the glob of each Grep over the wiki, by changing the call, as the hook of `rule-page-read` does for a read; the rule file keeps only the part on reading a Decision page.
>   - Answer: agreed, (a).
> - **When an agent may open a Decision page**
>   - Recommended: (b) keep the two reasons; a read through `addressed_by` stays a breach that the check counts.
>   - Answer: agreed, (b).
> - **Which agents the new hook covers**
>   - Recommended: (a) every agent, the librarian too.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) two checks: a new Estimate of the hook, read by a test and one live search in the main agent and in a subagent; the existing Estimate rewritten to cover only the load of the file and the reads of Decision pages.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, may an agent Grep inside `vault/wiki/decisions/`: (a) only a Read, `rule-ask` changes and the hook covers a Grep inside the folder too; or (b) a Grep is allowed for the two reasons, the hook leaves a Grep whose path is inside `decisions/` unchanged, 664.2 says the text arrives by a Read or such a Grep for one of the two reasons, and the frame of `ask-guppi` stays. The person chose (b).
>   - Taken: 664.1 leaves unchanged a Grep whose `path` is `vault/wiki/decisions/` or lies in it; 664.1 sets the rule's `purpose` and Purpose anew and makes its Render say the hook covers every agent and a Grep inside the folder is allowed for a reason; 664.2 promises that the text arrives by a Read or such a Grep, for a reason of the frame only.

### Case 664.1 — A hook adds the exclusion to every Grep over the wiki

> **given:**
> `estimate-search-leaves-out-decisions-by-the-grep-hook`: the new check of the hook.
> **＋** `rule-search-leaves-out-decisions`: the rule of the hook and of the file it renders.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the file rendered from `rule-search-leaves-out-decisions`.
> **＋** `guppi/grepguard.py`: the new hook `uv run guppi grepguard`.
> **＋** `guppi/cli.py`: the entry point that maps the command to its module.
> **＋** `tests/test_grepguard.py`: the tests of the hook.
> **＋** `rule-hook-registry`: its Render registers the hook in `.claude/settings.json`.
> **＋** `.claude/settings.json`: the file rendered from `rule-settings` and its children.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `!**/decisions/**`: the glob filter that leaves that folder out.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian, whose Greps the hook changes too.

> **when:**
> The main agent or any subagent calls Grep, and `uv run guppi grepguard` of `guppi/grepguard.py`, registered on `PreToolUse` of `Grep` in `.claude/settings.json`, reads the call.

> **then:**
> When the searched folder — the `path` of the call, or the working directory when the call has none — is a folder that holds `vault/wiki/decisions/`, the hook returns the call by `updatedInput` with `!**/decisions/**` at the end of its `glob`, after a space when the `glob` holds another filter, and with no permission decision.
> **＋** A `glob` that already ends with `!**/decisions/**` is not changed; one that holds it elsewhere gets it again at the end.
> **＋** The Grep then prints no line and no path of a file under `vault/wiki/decisions/`.
> **＋** A call of the librarian is changed in the same way as a call of any other agent.
> **－** A Grep whose `path` is `vault/wiki/decisions/` or lies in it passes unchanged: an agent greps there only for a reason of its frame.
> **－** A Grep whose `path` is one file, or a folder that does not hold `vault/wiki/decisions/`, passes unchanged.
> **－** The hook never refuses a call; a payload it cannot read or an error lets the call pass unchanged.

```then
create:
- slug: estimate-search-leaves-out-decisions-by-the-grep-hook
  ref: rule-search-leaves-out-decisions
  kind: QA
  purpose: Whether every Grep over vault/wiki/ or a folder that holds it runs with !**/decisions/** at the end of its glob, added by the PreToolUse hook, and prints nothing under vault/wiki/decisions/
  method: uv run pytest tests/test_grepguard.py, then by hand at the /hi of a later session after the render a Grep over vault/wiki/ with no glob in the main agent and in a subagent, whether it prints a file under vault/wiki/decisions/
  tags:
  - hooks
  - harness
  - session
update:
- slug: rule-search-leaves-out-decisions
  replace:
  - old: '- Every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, carries `!**/decisions/**` in its `glob`: alone, or after another filter with a space between them, as in `*.md !**/decisions/**`. - A glob written from the searched folder, such as `!decisions/**`, does not leave the folder out: the Grep tool reads a glob that holds a slash from the working directory, the repository root, and not from its `path`.'
    new: '- A hook adds `!**/decisions/**` at the end of the `glob` of every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, in every agent, the librarian too, whom the rest of this file does not bind; a Grep over such a folder prints nothing under `vault/wiki/decisions/`, and an exclusion written first, where it does not work, is put last by the hook (case 664.1).'
  - old: '- The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, and only for a reason the frame of the agent names.'
    new: '- The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, or by a Grep whose `path` is that folder or lies in it, which the hook leaves unchanged, and only for a reason the frame of the agent names (case 664.1).'
  - old: The librarian follows its own frame, which flags such a read rather than forbids it.
    new: The librarian follows its own frame, which flags such a read rather than forbids it; the hook filters its Greps over the wiki too, and a read of a Decision page it needs stays open to it (case 664.1).
  - old: and if it does not, a later Case moves the text to `CLAUDE.md`.
    new: 'and if it does not, a later Case moves the text to `CLAUDE.md`. The file loaded in every agent, but the agents did not follow it for Grep: in the reading of session 1343 nine Greps over the wiki carried no exclusion, and one put it first, where it leaves nothing out. So a `PreToolUse` hook on Grep adds the exclusion at the end of the glob, in every agent, the librarian too; a Grep inside `vault/wiki/decisions/` it leaves unchanged, and the file keeps the rule on reading a Decision page (case 664.1).'
  set:
    implementation_ref:
    - guppi/grepguard.py
    - tests/test_grepguard.py
    - .claude/settings.json
    purpose: 'Prevents the text of a Decision page from entering the context of an agent through a search of the vault: a hook leaves the Decision pages out of every Grep over the wiki, and the main agent, ask-guppi and case-guppi read a Decision page only for a reason of their frame'
  change: a PreToolUse hook on Grep adds !**/decisions/** at the end of the glob in every agent, a Grep inside decisions/ left unchanged; the Render keeps the rule on reads; purpose set anew (case 664.1)
- slug: rule-hook-registry
  replace:
  - old: |-
      { "matcher": "Read",
        "hooks": [ { "type": "command", "command": "uv run guppi pageread", "timeout": 30 } ] }
    new: |-
      { "matcher": "Read",
        "hooks": [ { "type": "command", "command": "uv run guppi pageread", "timeout": 30 } ] },
      { "matcher": "Grep",
        "hooks": [ { "type": "command", "command": "uv run guppi grepguard", "timeout": 30 } ] }
  change: the hook grepguard registered on PreToolUse of Grep (case 664.1)
```

```tasks
- [x] create `estimate-search-leaves-out-decisions-by-the-grep-hook`
- [x] update `rule-search-leaves-out-decisions`
- [x] update `rule-hook-registry`
- [x] `guppi/grepguard.py`: the hook reads the payload as UTF-8, judges whether the searched folder holds `vault/wiki/decisions/` and does not lie in it by `inside` of `guppi/pageread.py`, and prints `hookSpecificOutput.updatedInput` with the glob ended by `!**/decisions/**`; it never raises; the module docstring describes the hook and names the rule page.
- [x] `guppi/cli.py`: the command `grepguard` maps to `grepguard.run`, and the docstring lists it among the hook commands.
- [x] `tests/test_grepguard.py`: one test per line of the `then`, among them a Grep with no path, a Grep with the exclusion first, a Grep whose path is `vault/wiki/decisions/`, and a Grep whose path is one file.
- [x] `uv run guppi render`: `.claude/settings.json`
- [x] `uv run guppi render`: `.claude/rules/search-leaves-out-decisions.md`
- [ ] read `estimate-search-leaves-out-decisions-by-the-grep-hook`
```

### Case 664.2 — The rule file loads and a Decision page is read only for a reason of the frame

> **given:**
> `estimate-search-leaves-out-decisions-in-every-agent`: its Criterion, `purpose` and `method` are replaced.
> **＋** `rule-search-leaves-out-decisions`: the rule whose file the agents load.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the file rendered from `rule-search-leaves-out-decisions`.
> **＋** `.claude/agents/ask-guppi.md`: the two reasons to open a Decision page.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian.
> **＋** `estimate-search-leaves-out-decisions-by-the-grep-hook`: the check of the Greps.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.

> **when:**
> A session starts after `uv run guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Read, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it.

> **then:**
> `.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
> **＋** The text of a Decision page reaches one of these agents only by a Read of its path or by a Grep whose `path` is `vault/wiki/decisions/` or lies in it, for a reason of `.claude/agents/ask-guppi.md` in `ask-guppi` and `case-guppi` — a page of its answer carries `deferred_by`, or the question asks why something was decided — and for no reason in the main agent.
> **－** An `addressed_by` that names a Decision page is no reason to read it.
> **－** Whether a Grep over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
> **－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
> **－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.

```then
update:
- slug: estimate-search-leaves-out-decisions-in-every-agent
  set:
    status: pending
    purpose: Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, and the text of a Decision page reaches them only by a Read of its path, or a Grep inside vault/wiki/decisions/, for a reason their frame names
    method: 'by hand at the /hi of a later session: the transcripts of the main agent and of each ask-guppi and case-guppi of a session after the render of .claude/rules/search-leaves-out-decisions.md by case 664.1, whether the file stands in each context and each Read of a page under vault/wiki/decisions/ and each Grep inside that folder, read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the load of the file and the reads of Decision pages only; the Greps move to estimate-search-leaves-out-decisions-by-the-grep-hook; purpose and method set anew (case 664.2)
```

```tasks
- [x] update `estimate-search-leaves-out-decisions-in-every-agent`
- [ ] read `estimate-search-leaves-out-decisions-in-every-agent`
```

### Case 664.3 — The check of the searches of ask-guppi points to both checks of Decision pages

> **given:**
> `estimate-ask-searches-at-prespec`: its Criterion is replaced whole.
> **＋** `rule-ask`: the rule rendered into `.claude/agents/ask-guppi.md`.
> **＋** `.claude/agents/ask-guppi.md`: the frame of `ask-guppi`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the questions the main agent sends at pre-spec.
> **＋** `estimate-search-leaves-out-decisions-by-the-grep-hook`: the check of the Greps over Decision pages.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the check of the reads of Decision pages.
> **＋** `vault/wiki/rules/`: the folder the first Grep of the agent runs over.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
> **＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
> **－** Whether a Grep of the agent over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
> **－** Whether a Read of the agent, or a Grep inside `vault/wiki/decisions/`, reaches a Decision page only for a reason of its frame is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.

```then
update:
- slug: estimate-ask-searches-at-prespec
  set:
    status: pending
  change: the Criterion replaced whole — the Greps over a folder that holds the Decision pages are left to estimate-search-leaves-out-decisions-by-the-grep-hook, the Reads and the Greps inside it to estimate-search-leaves-out-decisions-in-every-agent (case 664.3)
```

```tasks
- [x] update `estimate-ask-searches-at-prespec`
- [ ] read `estimate-ask-searches-at-prespec`
```

## Case 668 — A lesson reopens an Insight that a decision of its own session sets actioned

> **context:**
> This Case replaces Case 663 whole, with the same content the person ratified. The first ratification of 663 left a ledger line that creates the Estimate under its old slug `estimate-synthesis-reads-the-status-the-run-sets`, a ledger line cannot be withdrawn, and only a Case under a new number whose lines carry `{supersedes:case 663}` retires it. At synthesis the librarian hangs each new lesson on an Insight of the same root cause. When that Insight is `actioned`, the lesson reopens it, unless the lesson entry carries `addressed_by`, the mark of a decision of its own session that closed its cause (cases 284.4, 385). The librarian does this on `materialize.yaml` before `guppi generate` runs, so it sees the status on disk, while a decision entry of the same yaml can set the same Insight `actioned`. In the librarian run of session 1343 `insight-workflow-case-schema-silent-on-what-the-scripts-accept` was `open` on disk, and the entry of Case 651.3 set it `actioned`. The lesson `lesson-orchestration-defer-acknowledged-without-its-short-form` (ledger line L43, with no mark) joined it by an `update` with no status. `generate` applied the entries in their order: the History of the Insight holds the line of 651.3 and then the line of the new child. The cascade then archived the lesson, since its Insight stood `actioned`. The lesson neither reopened the Insight nor was marked as closed by a decision. The person chose that the librarian counts an Insight as `actioned` when a decision entry of the same yaml sets it so, and that an unmarked lesson then reopens it. The synthesis entries are appended after the decision entries, so the reopening is applied last, and the cascade finds the Insight `open` and leaves the lesson `clustered`. The addressed_by that the decision entry sets is the one a marked lesson is compared with. At /pre-spec the person bounded the Case to one `materialize.yaml`, the yaml of the lesson's own session: a librarian run takes every yaml that `guppi materialize` names, one per unit, and `estimate-generate-cascades` says that `generate` runs the cascade after all entries of a unit, so a decision in the yaml of another unit is not counted. The person left the Insight and the lesson of session 1343 as they stand: reopening the Insight now would leave it `open` with no live child, which the cascade archives at once. Its fix, Case 651.3, also added to `rule-orchestration` the sentence that the reply that shows a short-form defer carries its `LEDGER` block, which is the step the lesson missed. A Grep of `` when it was `actioned` `` over `vault/wiki/` without `decisions/` printed `vault/wiki/rules/rule-synthesis.md`; the same Grep over `.claude/` printed `.claude/agents/librarian-guppi.md`, its Render, which follows by the render. A Grep of `unless a decision of its own session` over `vault/wiki/` without `decisions/` and `.claude/` printed `vault/wiki/entities/entity-glossary.md` and `vault/wiki/glossary.md`; the row of the status of an Insight changes on `entity-glossary`, and `glossary.md` follows by its command. That row reads as if a decision of the same session were enough without the mark. `rule-insights-schema` already says that only the mark keeps an Insight `actioned`, so it stays true and is not changed. `estimate-glossary-terms-defined` stands: the new row names the mark, as its `where` page `rule-insights-schema` does, and contradicts nothing there. Case 660 of this session changes other rows of `entity-glossary`, the rows of `supersedes` and of the status of a Decision, not this one. `estimate-synthesis-keeps-actioned-by-the-mark` stands with its passed result: its Criterion speaks of an Insight that stands `actioned` before the run, and each of its lines stays true. The new case is checked by a new Estimate of its own. `estimate-synthesis-clusters` stands too: its line on a lesson that joins a live Insight says nothing of the status. A Glob `vault/**/*synthesis-reads*` printed nothing, so the new slug is free.

> **problem:**
> The rule of synthesis does not say whether an Insight that a decision entry of the lesson's own `materialize.yaml` sets `actioned` counts as `actioned` for a lesson that joins it. As a result, a lesson with no mark can join such an Insight with no reopening and go to the archive, as if a decision had closed its cause.

> **recommend:**
> - **Which status the librarian reads when a lesson joins an Insight**
>   - Recommended: (a) the status after the run's decisions: an Insight counts as `actioned` when it stands so on disk or when a decision entry of the same run sets it so; an unmarked lesson reopens it, a marked one keeps it `actioned`, and the brief reports the reopening.
>   - Answer: agreed, (a).
> - **The Insight this already happened to**
>   - Recommended: (a) leave the Insight `actioned` and the lesson archived; the Case says why in its `context`.
>   - Answer: agreed, (a).
> - **The glossary row on the status of an Insight**
>   - Recommended: (a) the row names the mark, and says that an Insight a decision of the same run sets `actioned` counts as `actioned`; the glossary file is rebuilt.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) a new Estimate, `estimate-synthesis-reads-the-status-the-run-sets`, read by hand after the first run in which a lesson joins an Insight a decision of the same run sets `actioned`; `estimate-synthesis-keeps-actioned-by-the-mark` stands with its result.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at /pre-spec, whether the scope is the lesson's own yaml, that is its own session, or every yaml of the librarian run; the person chose the lesson's own yaml.
>   - Taken: every text of the Case says a decision entry of the same `materialize.yaml`, the lesson's own session: the name, `problem`, the glossary row, the new Estimate, renamed `estimate-synthesis-reads-the-status-its-yaml-sets`, and its `purpose`; its `method` names the kind of run, not the first one.

> **given:**
> `estimate-synthesis-reads-the-status-its-yaml-sets`: the new check of the status the synthesis reads.
> **＋** `rule-synthesis`: its Render, the condition on which a lesson reopens an Insight.
> **＋** `.claude/agents/librarian-guppi.md`: the file the Render of `rule-synthesis` is rendered into.
> **＋** `entity-glossary`: the row of the status of an Insight.
> **＋** `vault/raw/<date>/<hi HHMM>/materialize.yaml`: the entries of one session, decisions first and synthesis after.
> **＋** `guppi/generate.py`: applies the entries in their order, and its cascade archives the `clustered` lessons of an `actioned` Insight.
> **＋** `vault/wiki/brief.md`: where the librarian reports the synthesis.

> **when:**
> `librarian-guppi`, at synthesis, hangs a lesson entry on an Insight of the same pattern that stands `open` on disk, while an `update` entry of a decision in the same `materialize.yaml` sets that Insight `actioned` with `addressed_by: decision-case-M`, and `guppi/generate.py` then applies the yaml.

> **then:**
> A lesson entry with no `addressed_by` gives an `update` of the Insight with `children` plus the lesson and `set: {status: open}`.
> **＋** After `guppi/generate.py` runs, the Insight stands `open` and the lesson stands `clustered`, not archived.
> **＋** A lesson entry with `addressed_by: decision-case-N` gives an `update` with no `status`: it carries `set: {addressed_by: decision-case-N}` when case N is later than case M, compared number by number, and no `addressed_by` otherwise; the Insight stays `actioned`.
> **＋** `vault/wiki/brief.md` reports the pair beside the synthesis.
> **－** An Insight that is not `actioned` on disk and that no decision entry of the yaml sets `actioned` takes no `status` from the lesson.

```then
create:
- slug: estimate-synthesis-reads-the-status-its-yaml-sets
  ref: rule-synthesis
  kind: QA
  purpose: Whether a lesson that joins an Insight a decision entry of its own materialize.yaml sets actioned reopens it when it carries no addressed_by, and keeps it actioned when it does
  method: one reading by hand of the yaml, the Insight page and the brief after a librarian run in which a lesson joins an Insight that a decision entry of the same yaml sets actioned; no date
  tags:
  - harness
  - workflow
  - librarian
update:
- slug: rule-synthesis
  replace:
  - old: 'when it was `actioned` — `set: {status: open}`'
    new: 'when it was `actioned`, on disk or by an `update` entry of a decision in this yaml that sets it `actioned`, whose `addressed_by` is then the one the Insight names (case 668) — `set: {status: open}`'
  change: an Insight that a decision entry of the same yaml sets actioned counts as actioned at synthesis (case 668)
- slug: entity-glossary
  replace:
  - old: a new Lesson of the same root cause reopens it unless a decision of its own session closed its cause (case 284.4);
    new: a new Lesson of the same root cause reopens it unless its entry carries `addressed_by`, the mark of a decision of its own session that closed its cause (case 284.4); an Insight that a decision of the Lesson's own session sets `actioned`, in the same `materialize.yaml`, counts as `actioned` for that Lesson (case 668);
  change: the row of the status of an Insight names the mark and the status a decision of the lesson's own session sets (case 668)
```

```tasks
- [x] create `estimate-synthesis-reads-the-status-its-yaml-sets`
- [x] update `rule-synthesis`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] update `entity-glossary`
- [x] `uv run guppi glossary`
- [ ] read `estimate-synthesis-reads-the-status-its-yaml-sets`
```

## Deferred

## Case 665 — the failed reading of the Case form put off

> **context:**
> `estimate-case-protocol-case-form` failed at the Work readings of session 1343 (L38): `given` lines with two things on a line or with a state, and a count in `then`. Session 1616 closed Plan Mode at the person's word with this item still open.

> **problem:**
> No Case of session 1616 decides whether `case-guppi` changes or the Criterion accepts a pair such as a module and its test on one line.

```then
defer:
  - slug: estimate-case-protocol-case-form
    type: estimate
    purpose: "A built Case carries the whole contract in given, when and then, in the file the person is sent; its failed reading of session 1343 put off by session 1616"
```

## Case 666 — the failed reading of the confirmation after pre-spec put off

> **context:**
> `estimate-prespec-confirms-the-findings-once` failed at the Work readings of session 1343 (L41): the confirmation runs of ask-guppi wrote four sentences under one finding. Session 1616 closed Plan Mode at the person's word with this item still open.

> **problem:**
> No Case of session 1616 decides whether the frame of ask-guppi or the Criterion of this Estimate changes.

```then
defer:
  - slug: estimate-prespec-confirms-the-findings-once
    type: estimate
    purpose: "The ask-guppi runs confirm their own findings once on the Cases built again, at most three sentences per finding; its failed reading of session 1343 put off by session 1616"
```

## Case 667 — the failed reading of the case-guppi check of the finished Case put off a third time

> **context:**
> `estimate-case-build-checks-the-finished-case` failed at the Work Mode of session 0109 (L22), was put off by Case 647 of session 0311 and by Case 657 of session 1343. Session 1616 closed Plan Mode at the person's word with this item still open.

> **problem:**
> No Case of session 1616 decides whether the frame of `case-guppi` or the Criterion of this Estimate changes.

```then
defer:
  - slug: estimate-case-build-checks-the-finished-case
    type: estimate
    purpose: "Whether case-guppi checks its finished Case before it answers, counted by what ask-guppi still finds at pre-spec; its failed reading of session 0109 put off by session 1616"
```
