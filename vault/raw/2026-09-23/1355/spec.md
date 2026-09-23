<!-- approved 17:47:56 · session 55eeac28 -->

# Spec — 2026-09-23, session 1355

## Case 376 — the report of `/retro` holds each fact once

> **context:**
> The Render of `rule-retro` sets the report of `/retro` in two places. The Retro opens with the frontier: what was ratified by the Tail, the unticked boxes of the Spec and what the agent noticed during Work Mode. It closes with three lists: the ratifications, what got done, what did not. In session 1126 the person found two defects: the ratifications stand twice, and the unticked boxes of the Spec stand apart from what is not done. `rule-retro` stands `built`, deferred by Case 375 and taken up here; `estimate-retro-loads` speaks of the readings, not of the form of the report, and is not touched; the form of the report gets an Estimate of its own, whose Criterion the item writes itself, so that it does not depend on whether Work Mode builds the code of 378.2 before the librarian. Shown again in the model of Case 378.

> **problem:**
> The report of `/retro` names the same ratifications twice and splits what is not done into two places, so the person reads more and finds the open work in two lists.

> **given:**
> `rule-retro` — the Render `.claude/skills/retro/SKILL.md`: the opening message and the close of the report.
> **＋** `/retro` — the skill, the render of `rule-retro`.
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session, with its unticked boxes.
> **＋** `uv run guppi tail` — the Tail with the decision lines of the session.
> **＋** `estimate-retro-report-holds-each-fact-once` — the new promise.

> **when:**
> The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes; the agent writes the opening message and the close.

> **then:**
> The opening message holds one numbered list of what is not done: the unticked boxes of `raw/<date>/<hi HHMM>/spec.md` per Case, each marked as waiting for the librarian or as debt, and what the agent noticed during Work Mode.
> **－** The opening message holds no list of the ratifications.
> **＋** The close holds every ratification of the session, one line per Case, from `uv run guppi tail` grouped by Case, this session's folder first, a Case a `{supersedes:case N}` line names not counted.
> **＋** The close holds what got done.
> **＋** The close holds what is not done: the numbers of the opening list, each with the end it took.
> **－** No ratification and no box is named twice in the report.

```then
update:
  - slug: rule-retro
    replace:
      - old: "what was ratified (the lines of the Tail above grouped by Case, this session's folder first, one line per Case); the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), the unticked boxes per Case"
        new: "the list of what is not done, numbered: the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), per Case"
      - old: "you noticed during Work Mode, as a numbered list"
        new: "you noticed during Work Mode, in the same list"
      - old: "Close with three lists: every ratification of this session, one line each; what"
        new: "Close with three lists: every ratification of this session, one line per Case, by the Tail above grouped by Case, this session's folder first, a Case a `{supersedes:case N}` line names not counted; what"
      - old: "got done; what did not."
        new: "got done; what is not done — the opening list by its numbers, each item with the end it took."
    change: the report of /retro holds each fact once — the ratifications in the closing list only, the unticked boxes inside the numbered list of what is not done (case 376)
create:
  - slug: estimate-retro-report-holds-each-fact-once
    type: estimate
    ref: rule-retro
    kind: QA
    purpose: Whether the report of /retro holds each fact once — the ratifications in the closing list only, the unticked boxes of the Spec inside the list of what is not done
    method: one reading by hand at the first /retro after the render, recorded in the estimate line
    tags: [session, workflow, harness]
    sections:
      Criterion: |
        When:
        The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes; the agent writes the opening message and the close.

        Then:
        The opening message holds one numbered list of what is not done: the unticked boxes of `raw/<date>/<hi HHMM>/spec.md` per Case, each marked as waiting for the librarian or as debt, and what the agent noticed during Work Mode.
        **－** The opening message holds no list of the ratifications.
        **＋** The close holds every ratification of the session, one line per Case, from `uv run guppi tail` grouped by Case, this session's folder first, a Case a `{supersedes:case N}` line names not counted.
        **＋** The close holds what got done.
        **＋** The close holds what is not done: the numbers of the opening list, each with the end it took.
        **－** No ratification and no box is named twice in the report.
```

```tasks
- [x] update `rule-retro` — four `replace` pairs in the Render
- [x] create `estimate-retro-report-holds-each-fact-once`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-report-holds-each-fact-once` — by hand at the first `/retro` after the render
```

## Case 377 — a lesson written after its fix keeps the Insight closed

> **context:**
> The Insight `insight-session-vault-knowledge-not-loaded` holds one pattern: a fact the vault holds does not reach the session that needs it. Each child so far was closed by moving the fact into a text loaded at the phase that needs it. The seventh child is `lesson-plan-mode-frontier-refused-at-hi-again`. In session 1126, Case 363 wrote the leave of plan mode into the Render of `rule-skill-hi`; at the `/hi` of this session plan mode was on, and the agent wrote `frontier.md` with no refusal.
> The Insight opened again all the same, because of the order of the ledger lines. The refusal came at `/hi`; the decision lines of 363 were written at 11:33, the lesson line at 13:26, at Retro, as the last line of the ledger. The mark `{addresses:<lesson slug>}` stands on a decision line only when the lesson line already stands in the ledger (case 284.2), so there was nowhere to put it. Case 284.2 forbade the reverse mark: "no `{addressed_by}` on the lesson line"; it assumed a lesson line always comes before its fix, and that assumption failed. The synthesis sees only `addressed_by` on the lesson entry of the yaml, whichever line set it.
> The mark on the lesson line is written into the Case schema by Case 379, which replaced 377.2 in the model of Case 378; the Insight (377.1) and the carrying of the mark by `materialize` (377.3) stay here. The Insight stands `open`, severity 1, one live child; `rule-materialize` stands `built`; every item an `update` with a `ref`, so no vault query.

> **problem:**
> A lesson can reach the ledger after the decision that already closed its cause. Then the mark has no place, the synthesis opens the Insight again, and a Case is spent on a fact the yaml already holds. Apart from that, the Insight stands `open` now.

### Case 377.1 — the Insight `actioned`

> **given:**
> `insight-session-vault-knowledge-not-loaded` — the Insight the Case sets `actioned`.
> **＋** `lesson-plan-mode-frontier-refused-at-hi-again` — its live child.
> **＋** `rule-skill-hi` — its Render says plan mode does not stop the write of the Frontier (case 363).
> **＋** `/hi` — the skill that assembles the Frontier.

> **when:**
> The librarian applies this Case, and the next session opens with `/hi`.

> **then:**
> `insight-session-vault-knowledge-not-loaded` stands `actioned` with `addressed_by: decision-case-377.1`.
> **＋** `lesson-plan-mode-frontier-refused-at-hi-again` goes to the archive by the cascade.
> **－** `/hi` makes no Frontier item of the Insight.

```then
update:
  - slug: insight-session-vault-knowledge-not-loaded
    set: {status: actioned, addressed_by: decision-case-377.1}
    change: "actioned: the seventh child closed in its own session by case 363, the leave of plan mode in the text of /hi; the /hi of session 1355 wrote frontier.md in plan mode with no refusal (case 377.1)"
```

```tasks
- [x] update `insight-session-vault-knowledge-not-loaded` — `actioned`, `addressed_by`
```

### Case 377.3 — materialize carries `{addressed_by:case N}` to the lesson entry

> **context:**
> The mark `{addresses:<lesson slug>}` on a decision line gives the lesson entry `addressed_by`, and the synthesis keeps an Insight closed by that field. When the lesson is written after the decision, the lesson line carries the mark, `{addressed_by:case N}` (Case 379); `materialize` must carry it to the same field by the same code. The Criterion of `estimate-materialize-carries-addresses` speaks of the decision's mark alone; it is replaced whole by one promise — the lesson entry gets `addressed_by` whichever line set it. `rule-materialize` stands `built`; its other ten Estimates speak of other things. Shown again in the model of Case 378: the first showing appended a line inside the Criterion, which 378.4 refuses.

> **given:**
> `guppi/materialize.py` — builds the yaml of a unit from its ledger: `parse_line`, `mark_addressed`.
> **＋** `tests/test_materialize.py` — fixes the assembly on a temp ledger.
> **＋** `rule-materialize` — states the marks in its Purpose.
> **＋** `estimate-materialize-carries-addresses` — the promise, its Criterion replaced whole.

> **when:**
> `guppi materialize` assembles a unit whose ledger holds a lesson line and a decision line of Case N, the one written second carrying the mark: `{addresses:<lesson slug>}` on the decision line, or `{addressed_by:case N}` on the lesson line.

> **then:**
> The lesson entry carries `addressed_by: decision-case-N` at the entry's level, set by one function for both marks.
> **＋** A decision entry with the mark carries `addresses: [<slug>, …]`.
> **－** The lesson page gets no `addressed_by` field.
> **－** A decision mark naming no lesson of the unit is `incomplete: [addresses]` on the decision entry, and the run does not fail.
> **－** A lesson mark with no decision line of Case N earlier in the unit is `incomplete: [addressed_by]` on the lesson entry, and the run does not fail.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "a mark whose lesson is not in the unit is `incomplete: [addresses]` on the decision entry (case 284.3)."
        new: "a mark whose lesson is not in the unit is `incomplete: [addresses]` on the decision entry (case 284.3). A lesson line's `{addressed_by:case N}` gives its entry the same `addressed_by: decision-case-N` when a decision line of Case N stands earlier in the unit, and `incomplete: [addressed_by]` otherwise (case 377.3)."
    change: a lesson line's {addressed_by:case N} reaches its entry as addressed_by (case 377.3)
  - slug: estimate-materialize-carries-addresses
    set: {status: pending, purpose: "A decision line's {addresses:<lesson slug>} or a lesson line's {addressed_by:case N} lands on the lesson's entry as addressed_by, at the entry's level; a mark without its pair is incomplete"}
    sections:
      Criterion: |
        When:
        `guppi materialize` assembles a unit whose ledger holds a lesson line and a decision line of Case N, the one written second carrying the mark: `{addresses:<lesson slug>}` on the decision line, or `{addressed_by:case N}` on the lesson line.

        Then:
        The lesson entry carries `addressed_by: decision-case-N` at the entry's level, set by one function for both marks.
        **＋** A decision entry with the mark carries `addresses: [<slug>, …]`.
        **－** The lesson page gets no `addressed_by` field.
        **－** A decision mark naming no lesson of the unit is `incomplete: [addresses]` on the decision entry, and the run does not fail.
        **－** A lesson mark with no decision line of Case N earlier in the unit is `incomplete: [addressed_by]` on the lesson entry, and the run does not fail.
    change: the Criterion replaced whole — both marks land on the lesson entry by one function (case 377.3)
```

```tasks
- [x] update `rule-materialize` — one `replace` pair in the body
- [x] update `estimate-materialize-carries-addresses` — `purpose` and the Criterion whole, `pending`
- [x] `guppi/materialize.py`: `parse_line` lifts `addressed_by` from the braces of a lesson line; one function sets `addressed_by` for both marks, `mark_addressed` through it; the docstring names the lesson line's mark
- [x] `tests/test_materialize.py`: the lesson line's mark reaches its entry; a mark with no decision line of its Case is `incomplete: [addressed_by]`
- [x] `uv run pytest tests/test_materialize.py`
- [x] read `estimate-materialize-carries-addresses`
```

## Case 378 — the model of the Criterion: `given` is the frame of the Case, an Estimate is When and Then

> **context:**
> The `given` of a Case serves two readers today. For the person it is "how it is now"; the scripts copy it into the Estimate as `Given:`, where it must stay true after the fix, so a Criterion goes stale the moment `given` holds a state or the defect. The bookkeeping — what the Case touches — lies in the prose of `context`, and nothing binds `when` and `then` to it. The operands are loose: "does not apply here" lets in lines on the bounds of an edit, and a grep of the `－` lines of the Criteria of the 104 Estimates finds 38 lines in 31 pages carrying one of "not change", "as today", "nothing else", "unchanged" or "stays as". Since case 296, `replace` pairs append lines inside another Criterion, and journals grow: the largest, `estimate-case-protocol-loaded`, holds 13 `＋` lines, of which 355.1, 355.2, 368 and 370 are signed a second time in `estimate-case-protocol-case-form`. Case 187 makes every change of a Render touch the Estimate of its live reading — the root of the live child of the Insight of C4.
> Since case 201.2 the decision page does not hold `given`: `generate` writes only Context, Problem and Deferred, so `given` returns to the decision page, or it leaves the vault with this change.
> `rule-case-protocol` and `rule-prespec` stand `draft`, `rule-materialize` and `rule-plan-mode` `built`. This Case changes the rules and the code; the eleven Estimates whose Criterion speaks of the old model are rewritten whole by the one pass over the 104 pages, Slice 3g of the sprint page (Case 381): `estimate-case-protocol-case-form`, `-loaded`, `estimate-materialize-assembles`, `-walks-dates`, `-marks-superseded`, `estimate-generate-writes-the-decision-page`, `-fails-alone`, `-cascades`, `estimate-prespec-reconciles`, `-checks-the-plan`, `estimate-plan-mode-names-its-estimates`. Every item an `update` with a `ref` or a `create` with a `ref`, so no vault query. The Case is written in the new form.

> **problem:**
> One section serves both the history of the Case and the contract of the Estimate, so the contract goes stale at every fix; `when` and `then` are bound by no frame, the operands let in claims on the bounds of an edit, and a Criterion can be appended to part by part — so Cases describe everything and Estimates turn into journals.

### Case 378.1 — `given` is the frame of the Case, `context` is prose

> **given:**
> `rule-case-protocol` — the Render `vault/wiki/case-schema.md`: the `context` and `given` rows of the Sections table, the Language paragraph, the section on the short form.

> **when:**
> The agent writes a Case by `vault/wiki/case-schema.md`, a Case that takes up a deferred decision included.

> **then:**
> `given` lists one thing per line: each page the Case creates or changes, each module, file and test of its `tasks`, and the rule that constrains — its slug or path in a code span and a few words on its role, no state.
> **＋** `context` is prose: the mechanism, where it goes wrong, the state of the pages, the vault's answer, why an Estimate of the rule is not touched; no list of what the Case touches.
> **＋** `when` and `then` name only what `given` names.
> **＋** A Case that takes up a deferred decision builds `given` as the frame and puts the vault's answer in `context`.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "What this is about, in plain words. In Work Mode this may shrink to a one-line reference back to an earlier Case; it is never omitted."
        new: "What this is about, in plain words: prose only — the mechanism, where it goes wrong, the state of the pages, the vault's answer; no list of what the Case touches, that is `given` (case 378.1). In Work Mode this may shrink to a one-line reference back to an earlier Case; it is never omitted."
      - old: "The conditions of the behaviour: one per line, and only a condition a line of `then` depends on — the rule that constrains, the test that fixes the behaviour. The state of the pages the Case changes, what conflicts, what sits in `draft`, the vault's answer and which Estimates of the rule the Case touches go to `context` (case 188)."
        new: "The frame of the Case, one thing per line: each page the Case creates or changes, each module, file and test its `tasks` touch, and the rule that constrains — its slug or path in a code span and a few words on its role, never its state; `when` and `then` name only what `given` names. It stays in the Case and on the Decision page and never enters an Estimate (case 378.1)."
      - old: "`context` opens with the mechanism in plain words — what the thing does today and where it goes wrong — for a reader who has not opened the pages, and closes with one sentence of bookkeeping — the state of the pages the Case changes, the vault's answer, the Estimates of the rule the Case touches and the ones it does not;"
        new: "`context` is prose: it opens with the mechanism in plain words — what the thing does today and where it goes wrong — for a reader who has not opened the pages, and closes with the state of the pages the Case changes, the vault's answer and why an Estimate of the rule is not touched; the list of what the Case touches is `given` (case 378.1);"
      - old: "`given` holds the conditions of the behaviour, one per line, and only a condition a line of `then` depends on: the rule that constrains, the test that fixes the behaviour; no state of pages, no history, no quotation for its own sake (case 188)."
        new: "`given` holds the frame, one thing per line: the pages, modules, files and tests the Case touches and the rule that constrains; no state, no history, no quotation (case 378.1)."
      - old: "then `recommend`, `given` (the vault asked), `when`, `then`"
        new: "then `recommend`, `given` — the frame — `when`, `then`, the vault's answer in `context` (case 378.1)"
    change: given is the frame of the Case, context is prose (case 378.1)
```

```tasks
- [x] update `rule-case-protocol` — five `replace` pairs in the Render
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
```

### Case 378.2 — the Criterion of an Estimate is `When:` and `Then:` only

> **given:**
> `guppi/materialize.py` — lifts the sections of a Case into the Criterion of an Estimate (`CRITERION_SECTIONS`, `criterion_text`).
> **＋** `tests/test_materialize.py` — fixes the lift.
> **＋** `rule-materialize` — states the lift in its Purpose.
> **＋** `rule-case-protocol` — the section on the Criterion and the paragraph on the `then` block of its Render.
> **＋** `rule-estimates-schema` — the Render `vault/wiki/estimates/schema.yaml`: the section `## Criterion` and two examples.
> **＋** `entity-glossary` — the rows Case and Estimate of `## Terms`.
> **＋** `estimate-materialize-lifts-when-and-then` — the new promise.

> **when:**
> `guppi materialize` assembles the `create` or `update` entry of an Estimate whose Case has `given`, `when` and `then` and whose item writes no `sections: Criterion`.

> **then:**
> The entry's `sections.Criterion` is the `When:` and `Then:` of the Case, verbatim with their operands.
> **－** The Criterion holds no `Given:`.
> **＋** The decision record of the Case still carries `given` in its `case_text`; a sub-case without its own `given` carries its parent's.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "## `given`, `when` and `then` are the Criterion"
        new: "## `when` and `then` are the Criterion"
      - old: "The scripts copy the Case's `given`, `when` and `then`, verbatim with their operands, as the Estimate's `Criterion` — `Given:`, `When:`, `Then:` —"
        new: "The scripts copy the Case's `when` and `then`, verbatim with their operands, as the Estimate's `Criterion` — `When:`, `Then:`; `given` stays in the Case and on the Decision page, so `when` names the trigger and the input it acts on, each thing by its slug or path, and the Estimate reads without the Case (case 378.2) —"
      - old: "its Criterion is the Case's `given`, `when` and `then`, lifted by the scripts"
        new: "its Criterion is the Case's `when` and `then`, lifted by the scripts"
      - old: "the scripts replace its Criterion with the Case's `given`, `when` and `then`, or keep"
        new: "the scripts replace its Criterion with the Case's `when` and `then`, or keep"
    change: the Criterion is the when and then of the Case; given stays in the Case (case 378.2)
  - slug: rule-estimates-schema
    replace:
      - old: "the `given`, `when` and `then` of one Case, verbatim with their operands, as `Given:`, `When:`, `Then:`."
        new: "the `when` and `then` of one Case, verbatim with their operands, as `When:`, `Then:` — no `Given:`: the frame of the Case stays on its Decision page (case 378.2); a page written before carries its `Given:` until the one pass of its migration."
      - old: "Given:\n    The discount pipeline runs every rule in order and takes the first that applies.\n\n    When:\n    A client with zero completed orders asks for a discount."
        new: "When:\n    A client with zero completed orders asks for a discount; the discount pipeline runs every rule in order and takes the first that applies."
      - old: "Given:\n    A seeded database with carts of 10, 50 and 200 line items.\n\n    When:\n    A buyer opens the cart."
        new: "When:\n    A buyer opens a cart of 10, 50 or 200 line items against a seeded database."
    change: the Criterion holds When and Then (case 378.2)
  - slug: rule-materialize
    replace:
      - old: "and its Criterion is the `given`, `when` and `then` of the Case that names it,"
        new: "and its Criterion is the `when` and `then` of the Case that names it (case 378.2),"
    change: the Criterion lifted is when and then (case 378.2)
  - slug: entity-glossary
    replace:
      - old: "`given` + `when` + `then` is the Estimate criterion, the Estimate named by slug (case 193)"
        new: "`given` is the frame of the Case; `when` + `then` is the Estimate criterion, the Estimate named by slug (cases 193, 378.2)"
      - old: "its Criterion is the `given`, `when` and `then` of one Case"
        new: "its Criterion is the `when` and `then` of one Case"
    change: the Criterion is when and then (case 378.2)
create:
  - slug: estimate-materialize-lifts-when-and-then
    type: estimate
    ref: rule-materialize
    kind: QA
    purpose: The Criterion materialize lifts from a Case is its when and then, never its given
    method: pytest tests/test_materialize.py on a temp Spec
    tags: [harness, workflow, ledger]
```

```tasks
- [x] update `rule-case-protocol` — four `replace` pairs in the Render
- [x] update `rule-estimates-schema` — three `replace` pairs in the Render
- [x] update `rule-materialize` — one `replace` pair in the Purpose
- [x] update `entity-glossary` — two `replace` pairs in `## Terms`
- [x] create `estimate-materialize-lifts-when-and-then`
- [x] `guppi/materialize.py`: `CRITERION_SECTIONS = ("when", "then")`; the docstring
- [x] `tests/test_materialize.py`: the lifted Criterion holds no `Given:`; a sub-case without `given` carries its parent's in `case_text`
- [x] `uv run pytest tests/test_materialize.py`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] `uv run guppi glossary`
- [x] read `estimate-materialize-lifts-when-and-then`
```

### Case 378.3 — the decision page holds `## Given`

> **given:**
> `guppi/generate.py` — writes the body of a decision page.
> **＋** `tests/test_generate.py` — fixes the body, today without `## Given`.
> **＋** `rule-decisions-schema` — the Render `vault/wiki/decisions/schema.yaml`: the entry `## Given` and the example page.
> **＋** `entity-glossary` — the row Decision page of `## Terms`.
> **＋** `rule-page-generation` — the `ref` of the new promise; its `estimates` gets the new Estimate.
> **＋** `estimate-generate-writes-the-given` — the new promise.

> **when:**
> `guppi generate` writes the decision page of a Case whose `case_text` in the yaml carries `given`.

> **then:**
> The body of the page is `## Context`, `## Problem`, `## Given`, `## Deferred` on a Case with a defer, and `## History`; `## Given` is the Case's `given`, verbatim.
> **－** A Case without `given` (defer-only) has no `## Given`.
> **－** The decision pages already in the vault are not rewritten.

```then
update:
  - slug: rule-decisions-schema
    replace:
      - old: "optional. Only on pages written before case 201.2, which keep it: the Case's `given`. A page written after carries none — the contract lives on the Estimate (case 201.2)."
        new: "optional. The Case's `given`, verbatim: the frame of the Case — the pages, modules, files and tests it touches and the rule that constrains — written by `generate` on the page of a Case that has one (case 378.3); a page written between case 201.2 and case 378.3 carries none."
      - old: "The vault query before the Case found no cart page and no overlapping purpose. `entity-checkout` exists and will\n    be affected. Nothing in `draft` covers this either.\n\n    ## Criterion\n    - estimate-cart § case 1"
        new: "`entity-cart` — the page this Case creates.\n    **＋** `entity-checkout` — the page the cart precedes."
    change: the decision page carries the Case's given again (case 378.3)
  - slug: entity-glossary
    replace:
      - old: "body Context, Problem, Given, When"
        new: "body Context, Problem, Given — the frame of the Case (case 378.3)"
    change: the body of a decision page (case 378.3)
create:
  - slug: estimate-generate-writes-the-given
    type: estimate
    ref: rule-page-generation
    kind: QA
    purpose: A decision page carries the given of its Case, so the frame survives the Criterion that no longer holds it
    method: pytest tests/test_generate.py on a temp vault
    tags: [harness, workflow, librarian]
```

```tasks
- [x] update `rule-decisions-schema` — two `replace` pairs in the Render
- [x] update `entity-glossary` — one `replace` pair in `## Terms`
- [x] create `estimate-generate-writes-the-given`
- [x] `guppi/generate.py`: `## Given` from `case_text` on the decision page; the docstring
- [x] `tests/test_generate.py`: `test_a_decision_page_carries_no_given_and_no_criterion_list` rewritten — `## Given` present, no `## When`, no `## Criterion`; a defer-only Case has no `## Given`
- [x] `uv run pytest tests/test_generate.py`
- [x] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [x] `uv run guppi glossary`
- [x] read `estimate-generate-writes-the-given`
```

### Case 378.4 — a Criterion changes only whole

> **given:**
> `guppi/prespec.py` — checks the plan before the Spec is approved.
> **＋** `guppi/materialize.py` — `touches_criterion`, the one predicate "the `old` of a pair stands inside `## Criterion`".
> **＋** `tests/test_prespec.py` and `tests/test_materialize.py` — fix the check and the assembly.
> **＋** `rule-prespec` — the Render `.claude/skills/pre-spec/SKILL.md`: the list of findings.
> **＋** `rule-case-protocol` — the paragraph on the `then` block (case 296).
> **＋** `rule-estimates-schema` — the section `## Criterion` (case 296).
> **＋** `rule-materialize` — the Purpose (case 296).
> **＋** `estimate-prespec-refuses-a-pair-inside-a-criterion` — the new promise.

> **when:**
> `guppi prespec --check` reads a plan where an `update` of an Estimate carries a `replace` pair whose `old` stands inside the `## Criterion` of that page.

> **then:**
> `guppi prespec --check` prints a finding with the Case, the slug and the opening of the `old`, and exits 1.
> **＋** `guppi materialize` marks such an entry `incomplete: [criterion]` and sets no `pending`.
> **－** A pair outside `## Criterion` still changes its part alone, with no `pending`.

```then
update:
  - slug: rule-prespec
    replace:
      - old: "for every `update` item carrying `file` — the file route is gone (case 320),"
        new: "for every `update` item carrying `file` — the file route is gone (case 320), for every `replace` pair whose `old` stands inside the `## Criterion` of an Estimate page — a Criterion changes only whole (case 378.4),"
    change: a pair inside a Criterion is a finding (case 378.4)
  - slug: rule-case-protocol
    replace:
      - old: "the scripts change that part, and the Criterion and the status stand, unless the part is inside the Criterion, which sets `pending` (case 296)."
        new: "the scripts change that part, and the Criterion and the status stand; a part inside the Criterion is refused — a promise changes only whole, by a Criterion replaced whole (case 378.4)."
    change: a Criterion changes only whole (case 378.4)
  - slug: rule-estimates-schema
    replace:
      - old: "an `update` that names a part alone — a field, a `replace` pair — keeps it, and a pair inside it sets `pending` (case 296);"
        new: "an `update` that names a part alone — a field, a `replace` pair outside it — keeps it; a pair inside it is refused, a changed promise is a Criterion replaced whole (case 378.4);"
    change: a Criterion changes only whole (case 378.4)
  - slug: rule-materialize
    replace:
      - old: "it is set `pending` when the part is inside the Criterion — the `old` of a `replace` pair stands in the page's `## Criterion` — and left as it is otherwise;"
        new: "a part inside the Criterion — the `old` of a `replace` pair stands in the page's `## Criterion` — is `incomplete: [criterion]` and sets no status, a Criterion changes only whole (case 378.4);"
    change: a pair inside a Criterion is incomplete (case 378.4)
create:
  - slug: estimate-prespec-refuses-a-pair-inside-a-criterion
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: A replace pair inside an Estimate's Criterion is refused before the Spec is approved, so a promise changes only whole
    method: pytest tests/test_prespec.py and tests/test_materialize.py on a temp plan and vault
    tags: [harness, workflow]
```

```tasks
- [x] update `rule-prespec` — one `replace` pair in the Render
- [x] update `rule-case-protocol` — one `replace` pair in the Render
- [x] update `rule-estimates-schema` — one `replace` pair in the Render
- [x] update `rule-materialize` — one `replace` pair in the Purpose
- [x] create `estimate-prespec-refuses-a-pair-inside-a-criterion`
- [x] `guppi/prespec.py`: the finding through `materialize.touches_criterion`, no second copy of the predicate
- [x] `guppi/materialize.py`: the branch of 296 sets `incomplete: [criterion]` instead of `pending`; the docstring
- [x] `tests/test_prespec.py`: a pair inside a Criterion is a finding; a pair outside is clean
- [x] `tests/test_materialize.py`: `test_a_pair_inside_the_criterion_sets_pending_and_lifts_nothing` rewritten to `incomplete: [criterion]`
- [x] `uv run pytest tests/test_prespec.py tests/test_materialize.py`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] read `estimate-prespec-refuses-a-pair-inside-a-criterion`
```

### Case 378.5 — the live reading of a Render does not depend on its content

> **given:**
> `rule-case-protocol` — the sentence of case 187 in the Render `vault/wiki/case-schema.md`.
> **＋** `rule-plan-mode` — the same sentence in its Purpose.
> **＋** `insight-workflow-contract-change-leaves-its-derived-text-stale` — the Insight of C4.

> **when:**
> The agent writes a Case that changes the Render of a rule.

> **then:**
> The Case does not touch the Estimate of the live reading of that Render: it promises only that the file equals the Render and is loaded.
> **＋** The behaviour a changed paragraph describes is named by the Case in the Estimate of that behaviour.
> **＋** `insight-workflow-contract-change-leaves-its-derived-text-stale` stands `actioned`, `addressed_by: decision-case-378.5`.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "an `update` of its `Render` touches the Estimate of the live reading of that Render (case 187)."
        new: "an `update` of its `Render` touches no Estimate of the live reading — that Estimate promises only that the file equals the Render and is loaded; the behaviour a changed paragraph describes is named in the Estimate of that behaviour (case 378.5)."
    change: the live reading of a Render does not depend on its content (case 378.5)
  - slug: rule-plan-mode
    replace:
      - old: "an `update` of a `Render` touches the Estimate of the live reading of that Render (case 187)."
        new: "an `update` of a `Render` touches no Estimate of the live reading, which promises only that the file equals the Render and is loaded (case 378.5)."
    change: the live reading of a Render does not depend on its content (case 378.5)
  - slug: insight-workflow-contract-change-leaves-its-derived-text-stale
    set: {status: actioned, addressed_by: decision-case-378.5}
    change: "actioned: the live child's dependency was case 187 — a Render change had to touch the live reading's Criterion; 378.5 removes it, 378.4 stops journals (case 378.5)"
```

```tasks
- [x] update `rule-case-protocol` — one `replace` pair in the Render
- [x] update `rule-plan-mode` — one `replace` pair in the Purpose
- [x] update `insight-workflow-contract-change-leaves-its-derived-text-stale` — `actioned`, `addressed_by`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
```

### Case 378.6 — the operands

> **given:**
> `rule-case-protocol` — the section Operands in the Render `vault/wiki/case-schema.md`.
> **＋** `rule-atomicity` — the rule by which a long chain is a sign.

> **when:**
> The agent writes the `given`, `when` and `then` of a Case.

> **then:**
> `＋` is "and" in any of the three: one more thing in the frame, one more action of the trigger, one more result.
> **＋** `－` is "but", most often in `then`: an effect that must not occur, or an exception — only about what `given` or `when` names.
> **－** A line that names nothing of `given` or `when`, such as "nothing else changes", is not written.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "Every further line starts with a bold operand: **＋** for one more condition or action — \"and also\", **－** for a limit or an exception — \"but not\", \"does not apply here\". One statement per line. `context`, `problem` and `recommend` carry no operand (case 159)."
        new: "Every further line starts with a bold operand. **＋** is \"and\", in any of the three: one more thing in the frame, one more action of the trigger, one more result. **－** is \"but\", most often in `then`: an effect that must not occur, or an exception — only about what `given` or `when` names; a line that names nothing of them is not written. One statement per line. More than seven **＋** lines in `given` or `then` are a sign the Case is not atomic (`rule-atomicity`). `context`, `problem` and `recommend` carry no operand (case 378.6)."
    change: the operands and and but, bounded by the frame (case 378.6)
```

```tasks
- [x] update `rule-case-protocol` — one `replace` pair in the Render
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
```

### Case 378.7 — pre-spec checks the frame, hard

> **given:**
> `guppi/prespec.py` — checks the plan before the Spec is approved.
> **＋** `guppi/materialize.py` — `split_cases`, `case_texts`, `category_of`: the parse of a Case and the one notion of a slug.
> **＋** `guppi/lint.py` — `CODE_SPAN`.
> **＋** `tests/test_prespec.py` — fixes the checks.
> **＋** `rule-prespec` — the Render `.claude/skills/pre-spec/SKILL.md`: the list of findings.
> **＋** `estimate-prespec-checks-the-frame` — the new promise.

> **when:**
> `guppi prespec --check` reads a plan where a Case names in `when` or `then` a slug or path its `given` does not name, or where the slug of an item of its `then` block is not named in its `given`.

> **then:**
> `guppi prespec --check` prints one finding per such slug or path, with the Case number, and exits 1.
> **＋** A slug is the content of a code span with a category prefix by `materialize.category_of`; a path is the content of a code span that holds a `/` and at least one more character; a slash command counts as a path.
> **＋** A sub-case without its own `given` is checked against its parent's.
> **－** A Case without `given` (defer-only) is not checked.

```then
update:
  - slug: rule-prespec
    replace:
      - old: "and a line of another form stays debt (case 279.2);"
        new: "and a line of another form stays debt (case 279.2), for every slug or path in a code span of a Case's `when` or `then` that its `given` — its own or its parent's — does not name, a path being a span that holds a `/` and one more character, and for every slug of its `then` block the `given` does not name (case 378.7);"
    change: when, then and the then block stay inside the frame of given (case 378.7)
create:
  - slug: estimate-prespec-checks-the-frame
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: A Case names in when, then and its then block only what its given names
    method: pytest tests/test_prespec.py on a temp plan
    tags: [harness, workflow]
```

```tasks
- [x] update `rule-prespec` — one `replace` pair in the Render
- [x] create `estimate-prespec-checks-the-frame`
- [x] `guppi/prespec.py`: `check_frame` through `materialize.split_cases`, `case_texts`, `category_of` and `lint.CODE_SPAN`
- [x] `tests/test_prespec.py`: a slug in `then` not in `given` is a finding; a target of the `then` block not in `given` is a finding; `/hi` not in `given` is a finding; a lone `/` span is clean; a sub-case by its parent's `given`; a defer without `given` is clean
- [x] `uv run pytest tests/test_prespec.py`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-checks-the-frame`
```

### Case 378.8 — pre-spec notes a long chain, soft

> **given:**
> `guppi/prespec.py` — checks the plan before the Spec is approved.
> **＋** `tests/test_prespec.py` — fixes the output.
> **＋** `rule-prespec` — the Render `.claude/skills/pre-spec/SKILL.md`: the output and the rule "until it prints".
> **＋** `estimate-prespec-notes-a-long-chain` — the new promise.

> **when:**
> `guppi prespec --check` reads a plan where the `given` or the `then` of a Case holds more than seven `**＋**` lines.

> **then:**
> `guppi prespec --check` prints a line opening with `note:`, with the Case number and the section.
> **－** A `note:` line is not a finding and does not change the exit code.
> **＋** The agent answers a `note:` line in one line in the chat; the run is repeated while findings remain.

```then
update:
  - slug: rule-prespec
    replace:
      - old: "Fix the plan, the frontier or the line for each, then run it again until it prints nothing."
        new: "It also prints a line opening with `note:` for every Case whose `given` or `then` holds more than seven **＋** lines — a sign the Case is not atomic; a `note:` line is not a finding, sets no exit code and is answered in one line in the chat (case 378.8). Fix the plan, the frontier or the line for each finding, then run it again until it prints no finding."
    change: a soft note on a long chain (case 378.8)
create:
  - slug: estimate-prespec-notes-a-long-chain
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: A chain of more than seven ＋ lines is named without blocking the Spec
    method: pytest tests/test_prespec.py on a temp plan
    tags: [harness, workflow]
```

```tasks
- [x] update `rule-prespec` — one `replace` pair in the Render
- [x] create `estimate-prespec-notes-a-long-chain`
- [x] `guppi/prespec.py`: the `note:` lines apart from the findings, the exit code by the findings alone
- [x] `tests/test_prespec.py`: eight `＋` give a `note:` and exit 0; seven give nothing
- [x] `uv run pytest tests/test_prespec.py`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-notes-a-long-chain`
```

## Case 379 — the mark `{addressed_by:case N}` in the Case schema (replaces 377.2)

> **context:**
> The mark `{addresses:<lesson slug>}` stands on a decision line when the lesson line already stands in the ledger; a lesson written after its fix has no place for the mark, and the synthesis opens the Insight again. Case 377.2 fixed this in the old model: it appended lines inside the Criteria of `estimate-case-protocol-ledger-line-form` and `estimate-case-protocol-loaded`. Case 378.4 refuses a pair inside a Criterion, and by Case 378.5 `loaded` is no longer touched by a change of a Render; the ledger line of 377.2 on `loaded` stands already and is undone only by a supersede. So this Case replaces 377.2 whole; 377.2 leaves the Spec. The Criterion of `estimate-case-protocol-ledger-line-form` is replaced whole: the form of a decision line, today in its Given, moves to its Then; its `purpose` and `method` follow the promise — how the agent writes the lines, not what a document says. `rule-case-protocol` stands `draft`; `estimate-case-protocol-loaded` is not touched by 378.5; `-case-form` and `-acknowledging-reply` speak of other things.

> **problem:**
> A lesson written after the decision that closed its cause has no place for the mark, so the synthesis opens its Insight again and a Case is spent on a fact the yaml already holds.

> **given:**
> `rule-case-protocol` — the ledger paragraph of the Render `vault/wiki/case-schema.md`.
> **＋** `estimate-case-protocol-ledger-line-form` — the promise: its Criterion, `purpose` and `method` replaced.

> **when:**
> The agent writes the ledger lines of a session: the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists.

> **then:**
> A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
> **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
> **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
> **－** A lesson whose fix is ratified in another session gets no mark.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "written when the lesson line already stands in the session's ledger, one mark per lesson; a lesson whose fix is ratified in another session gets no mark (case 284.2)."
        new: "written when the lesson line already stands in the session's ledger, one mark per lesson; a lesson line written after the Case of this session that closed its cause carries `{addressed_by:case N}` instead, naming that Case — one of the two marks per pair, by the order of the lines (case 379); a lesson whose fix is ratified in another session gets no mark (case 284.2)."
    change: a lesson line written after the Case that closed its cause carries {addressed_by:case N} (case 379)
  - slug: estimate-case-protocol-ledger-line-form
    set:
      status: pending
      purpose: The written shape of a ledger line and of its marks, as the agent writes them
      method: "by hand: the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together"
    sections:
      Criterion: |
        When:
        The agent writes the ledger lines of a session: the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists.

        Then:
        A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
        **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
        **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
        **－** A lesson whose fix is ratified in another session gets no mark.
    change: the Criterion replaced whole — the shape of a decision line and the two marks, by the order of the lines (case 379)
```

```tasks
- [x] update `rule-case-protocol` — one `replace` pair in the Render
- [x] update `estimate-case-protocol-ledger-line-form` — the Criterion whole, `purpose`, `method`, `pending`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-ledger-line-form`
```

## Case 381 — the one pass over the Estimates becomes a milestone of the sprint

> **context:**
> Case 378 changed the model of the Criterion; the 104 Estimates come to it in one pass: `Given:` out, the input of the scenario into `When:`, the `－` lines on the bounds of an edit out, the journals split, and the eleven Estimates of the old model named by Case 378 rewritten whole. It is the work of a session of its own. A defer does not fit: a defer stands on a Rule or an Insight, and `rule-estimates-schema` is changed by Case 378 already. A task without a page goes to the sprint page; the Frontier takes the first milestone with an open item, so a milestone ahead of Slice 4 is the agenda of the next `/hi`. It is named Slice 3g: the Criterion of `estimate-sprint-migration-lint-clean` reads `## Milestones` as the Slices in order, and 3g follows the closed 3c, 3d and 3f. The item is a plain line with no wikilink — no page closes the pass — so it never ticks and leaves by the `update` of the sprint page that closes the pass. `entity-sprint-migration` stands `draft`; its Estimates speak of the build, lint and the merge and are not touched.

> **problem:**
> The one pass over the Estimates has no place that brings it to the next session as its first item.

> **given:**
> `entity-sprint-migration` — the section `## Milestones`.
> **＋** `vault/wiki/sprint.md` — its render, `uv run guppi sprint`.
> **＋** `/hi` — the skill that assembles the Frontier from `vault/wiki/sprint.md`.

> **when:**
> The `/hi` of the next session assembles the Frontier from `vault/wiki/sprint.md`.

> **then:**
> The first milestone with an open item is "Slice 3g — the model of the Criterion, one pass over the Estimates", ahead of Slice 4; its line is the first Cases item of the Frontier.
> **－** The line names no page and does not tick; it leaves by the `update` of `entity-sprint-migration` that closes the pass.

```then
update:
  - slug: entity-sprint-migration
    replace:
      - old: "### Slice 4 — conversion of the parked pages by group"
        new: "### Slice 3g — the model of the Criterion, one pass over the Estimates\n\n- the one pass of Case 378: `Given:` out of the 104 Estimates, the input of the scenario into `When:`, the `－` lines on the bounds of an edit, the journals split, the eleven Estimates of the old model named by Case 378 rewritten whole\n\n### Slice 4 — conversion of the parked pages by group"
    change: Slice 3g, the one pass over the Estimates, ahead of Slice 4 (case 381)
```

```tasks
- [x] update `entity-sprint-migration` — one `replace` pair in `## Milestones`
- [x] `uv run guppi sprint`
```

## Deferred

## Case 380 — `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`, deferred

> **context:**
> The Insight holds a pattern: a fact is signed — in a Case, in a reading, in a ledger line — on a check narrower than the claim; the command that ran answered one question, the sentence it supports makes a wider one, and the wider check was one command away. Its Proposal: a claim names the command its output rests on and is no wider than that output; a claim about a whole set is checked by a count on both sides. The Insight stands `open`, severity 1, its live child `lesson-case-context-claim-wider-than-its-search`; the section "How the agent writes" of `CLAUDE.md` already holds the rule as text.

> **problem:**
> The session went to the model of the Criterion, and the Insight is not taken up in it.

```then
defer:
  - slug: insight-workflow-fact-signed-from-a-check-that-does-not-cover-it
    type: insight
    purpose: A fact is signed on a check narrower than the claim; whether the text rule of CLAUDE.md is enough or a check is due
```

## Case 382 — the bashguard message says the refusal is legal

> **context:**
> `rule-bash-guard` refuses a heredoc with a backslash and sends the agent to Write. The agent follows it, and at every Retro reports the refusal as a finding. The refusal is the behaviour the hook was made for, so these reports are noise.

> **problem:**
> The message of the hook does not say that the refusal is legal and needs no report, so the agent takes it for an event of the session each time.

```then
defer:
  - slug: rule-bash-guard
    type: rule
    purpose: The refusal message says the refusal is by design — use Write, and do not report it at Retro
```
