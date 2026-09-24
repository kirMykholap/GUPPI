<!-- approved 22:09:34 · session cdbf5dc4 -->

# Spec — session 2026-09-24 1916

## Case 395 — Slice 3g: the one note of the whole pass cut into four

> **context:**
> Today Slice 3g of `entity-sprint-migration` holds one note — a line with no wikilink — for the whole pass of Case 378 over the Estimates. A note never ticks and leaves only by the `update` that removes it, so it keeps the milestone open until the whole pass is done and does not show which part is done. One Frontier line of this size cannot close in one session; for the same reason the brief brings back `estimate-case-protocol-case-form` and `estimate-case-protocol-loaded` again and again as an item of their own: the note names no page. Counted on 2026-09-24 over 117 Estimate pages: `Given:` stands in the Criterion of 71; the eleven pages of the old model named by Case 378 all exist, 8 of them `passed`; three pages outside the eleven hold more than seven `＋` lines; `－` lines on the bounds of an edit stand on 28 pages; `### case N` blocks remain on 16 pages, and lint counts 21 pages `unmigrated`. `entity-sprint-migration` stands `draft`; its six Estimates speak of lint, the leftovers, the merge, the Rule-class files, `index.md` and the `file` route, none of the content of Slice 3g, so the Case does not touch them. An `update` with a `ref`, so no vault query; `frame-guppi` was not dispatched: the Case changes no behaviour of a rule or a hook.

> **problem:**
> One note covers a pass over 117 pages: it cannot close in one session, and it does not show which part is done.

> **given:**
> `entity-sprint-migration` — the section `## Milestones`, Slice 3g.
> **＋** `vault/wiki/sprint.md` — its render, written by `uv run guppi sprint`.
> **＋** `rule-sprint` — renders a line with no wikilink as a note that is never ticked.
> **＋** `/hi` — assembles the Frontier from `vault/wiki/sprint.md`.

> **when:**
> `uv run guppi sprint` writes `vault/wiki/sprint.md` from `entity-sprint-migration`, and `/hi` assembles the Frontier from it.

> **then:**
> Slice 3g, the current milestone, shows four notes in place of one, each `- [ ]`: the eleven Estimates of the old model, the journals, `Given:` out of the rest, the old shape.
> **＋** The Frontier of `/hi` holds one `C` line for each note.
> **＋** A note leaves Slice 3g by the `update` of `entity-sprint-migration` in the Case that finishes its group; Slice 3g stays the current milestone while one note stands.

```then
update:
- slug: entity-sprint-migration
  replace:
  - old: '- the one pass of Case 378: `Given:` out of the 104 Estimates, the input of the scenario into `When:`, the `－` lines on the bounds of an edit, the journals split, the eleven Estimates of the old model named by Case 378 rewritten whole'
    new: |-
      - the eleven Estimates of the old model named by Case 378 rewritten whole, one Case for each target rule: `estimate-case-protocol-case-form`, `estimate-case-protocol-loaded`, `estimate-materialize-assembles`, `estimate-materialize-walks-dates`, `estimate-materialize-marks-superseded`, `estimate-generate-writes-the-decision-page`, `estimate-generate-fails-alone`, `estimate-generate-cascades`, `estimate-prespec-reconciles`, `estimate-prespec-checks-the-plan`, `estimate-plan-mode-names-its-estimates`
      - the journals split, one promise for each Estimate: `estimate-lint-catches`, `estimate-generate-ticks-the-spec`, `estimate-materialize-skips-a-carried-over-unit`
      - every other Estimate: `Given:` out, the input of the scenario into `When:`, the `－` lines on the bounds of an edit out, each Criterion replaced whole
      - the old shape recut: every Estimate whose Criterion still holds `### case N` blocks brought to one Criterion, until lint counts no `unmigrated` page
  change: 'Slice 3g cut into four notes — the eleven, the journals, Given: out of the rest, the old shape (case 395)'
```

```tasks
- [x] update `entity-sprint-migration` — Slice 3g: the one note cut into four
- [x] `uv run guppi sprint`
```

## Case 396 — `rule-case-protocol`: two Estimates of the old model rewritten whole

> **context:**
> Two Estimates of `rule-case-protocol` describe a model of the Criterion that no longer stands. Both open with `Given:`, while Case 378 left `given` in the Case and on the Decision page. `estimate-case-protocol-case-form` also says that `given`, `when` and `then` together are copied into the Criterion; now only `when` and `then` are. `estimate-case-protocol-loaded` has grown into a journal of 13 `＋` lines, each retelling one paragraph of the Render. By Case 378.5 the reading of a Render promises one thing: the file equals the Render and is loaded; the behaviour a paragraph describes is promised by the Estimate of that behaviour. Most lines of the journal already have such a home:
> - the lines of 355.1, 355.2, 368 and 370 repeat `estimate-case-protocol-case-form`;
> - 356.1 and 356.2 stand in `estimate-hi-writes-frontier`;
> - 299.1 stands in `estimate-prespec-catches-a-superseded-case`;
> - 306.6 stands in `estimate-glossary-ticks-the-spec`;
> - 373 stands in `estimate-spec-reconcile-shows-a-changed-case`;
> - "a session without `/hi` holds no Case" stands in `estimate-ledger-write-lifts`;
> - the line of 294 and 296 is out of date: since Case 378.4 a pair inside the Criterion is refused, as `estimate-prespec-refuses-a-pair-inside-a-criterion` promises.
>
> The line of 353 stands only in the journal: a `replace` or `reword` pair is signed after the sentence around each match is read, and a Case that changes a page reads its `estimates`. It moves to `estimate-case-protocol-case-form`. The first paragraph, "The one rule", has no Estimate of its behaviour, and this Case creates none. The language of the sections of a Case in the chat is promised by `estimate-language-followed`, the report of `frame-guppi` in `context` by `estimate-case-protocol-checks-its-frame`, so neither enters the form of a Case. Both Estimates stand `pending`, `rule-case-protocol` `draft`. The three other Estimates of the rule (`-acknowledging-reply`, `-ledger-line-form`, `-checks-its-frame`) are written in the new model already and are not touched. An `update` with a `ref`, no vault query; `frame-guppi` was not dispatched: the behaviour of the rule does not change. The agent read the Render itself; it is loaded by the `/hi` of this session.

> **problem:**
> The Criteria of two Estimates promise a model that no longer stands; one of them is also a journal that repeats the promises of others and breaks at every edit of the Render.

### Case 396.1 — The form of a Case in the chat

> **given:**
> `estimate-case-protocol-case-form` — the Estimate whose Criterion is replaced.
> **＋** `rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the Sections table, the Operands, the Language paragraph, the section Splitting.
> **＋** `frame-guppi` — named in `context` by the Render, promised by `estimate-case-protocol-checks-its-frame`.

> **when:**
> The agent shows a Case in the chat, at its first showing or again.

> **then:**
> The Case opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds its sections in the order of the Sections table, each one blockquote whose first line is `**name:**`.
> **＋** `context` is prose: the mechanism in plain words first, then the state of the pages the Case changes, the vault's answer and why an Estimate of the rule is not touched; a case number stands only when the Case is about that case.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state; `when` and `then` name only what `given` names.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, and `then` holds behaviour only.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; the agent's own text stands after the Case, after one horizontal rule, and the reply ends with a plain question.
> **＋** A Case with sub-cases is shown in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole.

```then
update:
- slug: estimate-case-protocol-case-form
  set:
    status: pending
  change: the Criterion replaced whole — the form of a Case in the chat by the model of case 378, the line of case 353 taken from estimate-case-protocol-loaded (case 396.1)
```

```tasks
- [x] update `estimate-case-protocol-case-form` — the Criterion replaced whole by the `when` and `then` of this Case
- [ ] read `estimate-case-protocol-case-form` — by hand, the Cases of this session at its close
```

### Case 396.2 — The Case schema loaded as the Render

> **given:**
> `estimate-case-protocol-loaded` — the Estimate whose Criterion and `method` are replaced.
> **＋** `rule-case-protocol` — the page whose Render is `vault/wiki/case-schema.md`.
> **＋** `guppi/render.py` — `uv run guppi render` writes the Render, `--check` compares the file with it.
> **＋** `.claude/skills/hi/SKILL.md` — `/hi`, which loads `vault/wiki/case-schema.md` with `sprint.md`, `brief.md` and `glossary.md`.
> **＋** `CLAUDE.md` — the system prompt, which does not carry the schema.

> **when:**
> `/hi` opens a session after `uv run guppi render` wrote `vault/wiki/case-schema.md` from `rule-case-protocol`.

> **then:**
> The context of the session holds `vault/wiki/case-schema.md` from the first turn after `/hi`, loaded with `sprint.md`, `brief.md` and `glossary.md`.
> **＋** `uv run guppi render --check` exits 0: the file equals the Render of `rule-case-protocol`.
> **－** `CLAUDE.md` repeats no paragraph of `vault/wiki/case-schema.md`.

```then
update:
- slug: estimate-case-protocol-loaded
  set:
    status: pending
    method: uv run guppi render --check; by hand at the first /hi of a session, vault/wiki/case-schema.md in the context
  change: the Criterion replaced whole — the Render present from the first turn after /hi and equal to the page, the journal of its paragraphs out (cases 378.5, 396.2)
```

```tasks
- [x] update `estimate-case-protocol-loaded` — the Criterion replaced whole by the `when` and `then` of this Case, and its `method`
- [x] read `estimate-case-protocol-loaded` — `uv run guppi render --check`, and by hand the `/hi` of this session
```

## Case 397 — `rule-materialize`: three Estimates of the old model, the journal `-assembles` split

> **context:**
> Three Estimates of `rule-materialize` stand on the list of Case 378: `estimate-materialize-assembles`, `-walks-dates` and `-marks-superseded`. All three open with `Given:`, all three carry `－` lines on the bounds of an edit ("as today", "not this one"), and all three repeat promises of their neighbours:
> - the lines "`generate` applies none of them" and on the readings of a marked `create` in `-marks-superseded` belong to `generate` and to `estimate-materialize-refolds-a-reading-on-a-supersede`;
> - the error of a line and of a unit in `-walks-dates` belong to `estimate-materialize-fails-alone`.
>
> `-assembles` is a journal of 10 `＋` lines that holds three promises: the assembly of an entry, the filter of keys by `schema.yaml` (cases 214.1, 266), and the choice between a part and the whole in an `update` of an Estimate (cases 296, 378.4). Its fifth `＋` line is also out of date: it says a pair inside the Criterion sets `pending`, while since Case 378.4 the code (`lift_criterion`, `touches_criterion`) gives `incomplete: [criterion]` and sets no status. The filter of keys and the choice of a part become Estimates of their own; their slugs are free in `wiki/` and in the archive. `-walks-dates` has no `purpose` and no `method` field, and holds `## Context` and `## Method` of the old shape; `set.method` removes both sections (`generate`, case 211). `-assembles` has no `purpose`.
>
> All three stand `passed`, `rule-materialize` `built`; after the ratification the rule goes `draft` by the cascade until the readings pass. The readings are `pytest` with no change of code and can be taken in this session. Of the other nine Estimates of the rule, `-skips-a-carried-over-unit` is rewritten by Case 401.7, `-lifts-unfiltered-on-a-schema-change` and `-refolds-a-reading-on-a-supersede` still open with `Given:` and wait for C9, and the rest are in the new model; none of them is touched here. Every item an `update` or a `create` with a `ref`, no vault query; `frame-guppi` was not dispatched: the behaviour of the rule does not change. The agent read the code itself.

> **problem:**
> Three Criteria promise the model with `Given:` and repeat the promises of others, and one holds a line out of date; the journal `-assembles` holds three promises that break and are fixed apart.

### Case 397.1 — The assembly of an entry

> **given:**
> `estimate-materialize-assembles` — the Estimate whose Criterion is replaced and whose `purpose` is set.
> **＋** `guppi/materialize.py` — `assemble`, `lift_line`, `_lift_item`, `decision_record`, `fold_estimate`.
> **＋** `tests/test_materialize.py` — fixes the assembly.
> **＋** `vault/raw/<date>/<HHMM>/` — a unit: `ledger.md`, `spec.md`, `materialize.yaml`.

> **when:**
> `uv run guppi materialize` lifts the record lines of a unit's `ledger.md` against the `then` blocks of its `spec.md`.

> **then:**
> `materialize.yaml` holds one entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `addresses`, `origin`, `line`, `text`, `decision`; from the `then` item found by its slug — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented.
> **＋** `reword` is carried as a list of `{old, new}` pairs; a mapping or a scalar under it is `incomplete: [reword]`.
> **＋** An Estimate has its own line and its own entry, the `ref` of the line the Estimate itself; the entry of its `create` keeps `kind`, `purpose`, `method` and `tags` as fields.
> **＋** One decision record per Case: `decision`, `case_text`, `targets`; a sub-case reads a missing `context`, `problem`, `recommend` and `given` from its parent, never `when`.
> **＋** An `estimate` line whose slug has a `create` in the same unit is folded into it; one for a page of an earlier unit is an `estimate` entry of its own.
> **＋** The `new_tags` of any Case reach the yaml once each; an existing `materialize.yaml` is extended with the lines it does not hold, never rewritten.
> **＋** A line the grammar does not parse goes under `unparsed`, and the run goes on.
> **－** The keys `method`, `contract`, `estimate_slug` and `estimate_kind` on the item of a rule or an entity reach neither the page, nor `incomplete`, nor `unknown`: no Estimate is derived from them.

```then
update:
- slug: estimate-materialize-assembles
  set:
    status: pending
    purpose: One entry per record line of a ledger, its content lifted from the then block of its Case, nothing invented
  change: the Criterion replaced whole — the assembly of an entry by the model of case 378; the filter of keys and the update of an Estimate moved to their own Estimates (case 397.1)
```

```tasks
- [x] update `estimate-materialize-assembles` — the Criterion replaced whole by the `when` and `then` of this Case, and its `purpose`
- [x] read `estimate-materialize-assembles` — `uv run pytest tests/test_materialize.py`
```

### Case 397.2 — The keys of a `create` and a `defer` by `schema.yaml`

> **given:**
> `estimate-materialize-lifts-a-create-by-the-schema` — the new promise.
> **＋** `guppi/materialize.py` — `_lift_item`, `schema_fields`, `STRUCTURAL_KEYS`, `DEFER_KEYS`.
> **＋** `vault/wiki/<category>/schema.yaml` — the fields of a category.
> **＋** `tests/test_materialize.py` — fixes the filter.
> **＋** `estimate-materialize-lifts-unfiltered-on-a-schema-change` — the exception when the unit creates or updates `rule-<category>-schema`, a promise of its own.

> **when:**
> `uv run guppi materialize` lifts a `create` or `defer` item whose category has its `vault/wiki/<category>/schema.yaml` on disk, in a unit that neither creates nor updates `rule-<category>-schema`.

> **then:**
> Only the keys the category's `schema.yaml` names as fields reach `fields` of the entry; `ref` goes to the entry, `sections` to its own key.
> **＋** A key that is no field of the schema and none of the item's own keys — `slug`, `ref`, `sections`, `file`, `estimate`, `parent_create`, `parent_tags`, and on the `create` of a rule or an entity `method`, `contract`, `estimate_slug`, `estimate_kind` — is named under `unknown` on the entry, printed by `--show`, never written to the page, and the entry applies.
> **＋** The `type` and `purpose` of a `defer` are its own keys and reach `fields` whatever the category of its target; a `defer` without `purpose` is `incomplete: [purpose]`.

```then
create:
- slug: estimate-materialize-lifts-a-create-by-the-schema
  ref: rule-materialize
  kind: QA
  purpose: A key of a create or a defer that the category's schema.yaml does not name never reaches the page
  method: uv run pytest tests/test_materialize.py
  tags:
  - harness
  - workflow
  - ledger
```

```tasks
- [x] create `estimate-materialize-lifts-a-create-by-the-schema` — the promise of cases 214.1 and 266, moved out of `estimate-materialize-assembles`
- [x] read `estimate-materialize-lifts-a-create-by-the-schema` — `uv run pytest tests/test_materialize.py`
```

### Case 397.3 — An `update` of an Estimate: a part or the whole

> **given:**
> `estimate-materialize-changes-a-named-part-alone` — the new promise.
> **＋** `guppi/materialize.py` — `lift_criterion`, `names_a_part`, `touches_criterion`.
> **＋** `tests/test_materialize.py` — fixes the choice.
> **＋** `estimate-materialize-lifts-when-and-then` — the text lifted, a promise of its own.
> **＋** `estimate-prespec-refuses-a-pair-inside-a-criterion` — a pair inside a Criterion, at pre-spec and in `materialize`, a promise of its own.

> **when:**
> `uv run guppi materialize` lifts the `update` item of an Estimate.

> **then:**
> An item that names no part of the page — `change` alone — or carries `set.status` gets `sections.Criterion`, the text written under `sections: Criterion` or else the Criterion lifted from its Case, and `set: {status: pending}` unless the item set a status itself.
> **＋** An item that names a part — `set` without `status`, a `replace` pair, a section other than `Criterion` — and writes no Criterion carries that part alone: nothing is lifted and no status is set.
> **＋** A written `sections.Criterion` beside any other part stands and sets `pending`.

```then
create:
- slug: estimate-materialize-changes-a-named-part-alone
  ref: rule-materialize
  kind: QA
  purpose: An update of an Estimate changes the part it names alone, or replaces the Criterion whole
  method: uv run pytest tests/test_materialize.py
  tags:
  - harness
  - workflow
  - ledger
```

```tasks
- [x] create `estimate-materialize-changes-a-named-part-alone` — the promise of cases 296 and 378.4, moved out of `estimate-materialize-assembles`
- [x] read `estimate-materialize-changes-a-named-part-alone` — `uv run pytest tests/test_materialize.py`
```

### Case 397.4 — The walk of the units under `raw/`

> **given:**
> `estimate-materialize-walks-dates` — the Estimate whose Criterion is replaced and whose `purpose` and `method` are set.
> **＋** `guppi/materialize.py` — `units_with`, `spec_files`, `materialize_date`, `run`.
> **＋** `tests/test_materialize.py` — fixes the walk.
> **＋** `raw/<date>/<HHMM>/` — a session unit under `vault/raw/`: `raw/<date>/<HHMM>/ledger.md`, `raw/<date>/<HHMM>/spec.md`, `raw/<date>/<HHMM>/materialize.yaml`, the `origin` `raw/<date>/<HHMM>/ledger.md#case-N`.
> **＋** `raw/<date>/` — a date-level unit of the old shape: `raw/<date>/ledger.md`, `raw/<date>/spec.md`, `raw/<date>/materialize.yaml`.
> **＋** `estimate-materialize-fails-alone` — the error of a line and of a unit, a promise of its own.

> **when:**
> `uv run guppi materialize` runs, with `--date` or without.

> **then:**
> The unit of the walk is a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`: its yaml `raw/<date>/<HHMM>/materialize.yaml`, its Spec `raw/<date>/<HHMM>/spec.md` alone, the `origin` of its entries `raw/<date>/<HHMM>/ledger.md#case-N` and `#L<n>`.
> **＋** A date-level `raw/<date>/ledger.md` is a unit of the old shape: every Spec of the date in folder order and `raw/<date>/spec.md` when it exists, the yaml `raw/<date>/materialize.yaml`, `origin` in the date form; on a date with both shapes the date-level unit goes first; the yaml's `spec` field names the file each Case was found in.
> **＋** Without `--date` the walk covers every unit under `raw/`, dates ascending; `--date` walks the units of that date; stdout carries one line per yaml; a line written after the librarian's commit of its unit is lifted by the next run.

```then
update:
- slug: estimate-materialize-walks-dates
  set:
    status: pending
    purpose: Every unit under raw/ is walked, so a line written after the librarian's commit is lifted by the next run
    method: uv run pytest tests/test_materialize.py; live, the librarian's next run over more than one unit
  change: the Criterion replaced whole — the walk by the model of case 378, the error of a line and of a unit left to estimate-materialize-fails-alone; purpose and method as fields (case 397.4)
```

```tasks
- [x] update `estimate-materialize-walks-dates` — the Criterion replaced whole by the `when` and `then` of this Case, its `purpose` and `method`; `## Context` and `## Method` go with `set.method`
- [x] read `estimate-materialize-walks-dates` — `uv run pytest tests/test_materialize.py`
```

### Case 397.5 — The mark of a `supersedes`

> **given:**
> `estimate-materialize-marks-superseded` — the Estimate whose Criterion is replaced.
> **＋** `guppi/materialize.py` — `mark_superseded`, `mark_superseded_elsewhere`, `decision_record`.
> **＋** `tests/test_materialize.py` — fixes the mark.
> **＋** `vault/raw/` — the units whose `materialize.yaml` hold the entries of Case N.
> **＋** `estimate-materialize-refolds-a-reading-on-a-supersede` — the readings of a marked `create`, a promise of its own.

> **when:**
> `uv run guppi materialize` lifts a line with `{supersedes:case N}`, and the entries of Case N stand in this unit's `materialize.yaml` or in that of another unit under `raw/`.

> **then:**
> Every entry with `case: N` gets `superseded_by`, whatever its kind, and the `decisions` record of Case N gets it too.
> **＋** The `materialize.yaml` of another unit is written with that mark only.
> **＋** An entry of Case N marked while no heading of Case N stands in the unit's `spec.md` carries no `incomplete: [then]`, and its `decisions` record no `case_text` and no `incomplete` for a section.
> **－** An entry without `case` — an `estimate` or a `lesson` entry — gets no mark.

```then
update:
- slug: estimate-materialize-marks-superseded
  set:
    status: pending
  change: the Criterion replaced whole — the mark by the model of case 378; what generate skips and the readings of a marked create left to their own Estimates (case 397.5)
```

```tasks
- [x] update `estimate-materialize-marks-superseded` — the Criterion replaced whole by the `when` and `then` of this Case
- [x] read `estimate-materialize-marks-superseded` — `uv run pytest tests/test_materialize.py`
```

## Case 398 — `rule-page-generation`: three Estimates of the old model

> **context:**
> Three Estimates of `rule-page-generation` on the list of Case 378 open with the same `Given:` of five lines. The block has two faults:
> - it is out of date: it says a part inside the Criterion sets `pending`, while since Case 378.4 that is `incomplete: [criterion]`;
> - it holds a line on the bounds of an edit: "`materialize`, `cleanup` and `lint` do not change here".
>
> Beyond that, `estimate-generate-writes-the-decision-page` is false today: its `－` line says "no `## Given`", while since Case 378.3 `generate` writes `## Given` (`decision` in `guppi/generate.py`); that promise belongs to `estimate-generate-writes-the-given`. `estimate-generate-cascades` repeats the recount of an Entity's `rules`, which belongs to `estimate-generate-writes-rules-from-applies-to`; the line goes and the `purpose` is set. In `estimate-generate-fails-alone` only `Given:` changes: its lines were checked against the code (`error`, `a recut without method`, `not lifted by materialize`, `an update with no content`) and all hold.
>
> All three stand `passed`, `rule-page-generation` `built`; after the ratification the rule goes `draft` by the cascade. The readings are `pytest` with no change of code. The other seven Estimates of the rule are not on the list of eleven: `estimate-generate-writes` and `-walks-dates` are C10, the old shape; `-ticks-the-spec` is C8. Every item an `update` with a `ref`; `frame-guppi` was not dispatched: the behaviour of the rule does not change. The agent read the code itself.

> **problem:**
> Three Criteria carry a `Given:` out of date; one of them promises what the code no longer does, another repeats a promise of another Estimate.

### Case 398.1 — The Decision page

> **given:**
> `estimate-generate-writes-the-decision-page` — the Estimate whose Criterion is replaced.
> **＋** `guppi/generate.py` — `decision`, `clear_deferred_by`.
> **＋** `tests/test_generate.py` — fixes the page.
> **＋** `vault/raw/<date>/<HHMM>/materialize.yaml` — the entries and the `decisions` records `generate` applies.
> **＋** `vault/wiki/decisions/decision-case-<N>.md` — the Decision page it writes.
> **＋** `estimate-generate-writes-the-given` — the section `## Given`, a promise of its own.

> **when:**
> `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

> **then:**
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Context` and `## Problem` from `case_text`, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded`, appends to its `superseded_by`, and removes its slug from the `deferred_by` of every target of its `defer` list; an empty `deferred_by` is dropped.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **－** The page holds no `## When` and no `## Criterion`: the promise lives on the Estimate.

```then
update:
- slug: estimate-generate-writes-the-decision-page
  set:
    status: pending
  change: the Criterion replaced whole — the Decision page by the model of case 378; the false line on no Given out, the Given left to estimate-generate-writes-the-given (case 398.1)
```

```tasks
- [x] update `estimate-generate-writes-the-decision-page` — the Criterion replaced whole by the `when` and `then` of this Case
- [x] read `estimate-generate-writes-the-decision-page` — `uv run pytest tests/test_generate.py`
```

### Case 398.2 — One bad entry does not stop the run

> **given:**
> `estimate-generate-fails-alone` — the Estimate whose Criterion is replaced.
> **＋** `guppi/generate.py` — `error`, the apply of an `update`, the loop over the entries.
> **＋** `tests/test_generate.py` — fixes the failed, skipped and marked entries.
> **＋** `vault/raw/<date>/<HHMM>/materialize.yaml` — the entries and their marks.
> **＋** `vault/wiki/log.md` — the feed of page changes.

> **when:**
> `uv run guppi generate` meets an entry of `materialize.yaml` it cannot apply, or one already handled.

> **then:**
> An entry that fails — a collision, a `ref` naming no page, a `replace` absent or not unique, a field of an unexpected shape, an unknown `kind`, any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` in the yaml and skipped; the rest apply; the exit code is 1; no entry ends the run.
> **＋** An `update` with `sections.Criterion` on an Estimate page without a `method` field, whose `set` carries no `method`, fails the same way: `generate: <slug>: a recut without method (case 211)`.
> **＋** Every applied entry is marked `applied: <time>`; a stale `failed` mark is dropped on apply; a rerun writes nothing.
> **＋** An entry with `failed` and no `kind` is skipped with its mark kept and the line `generate: line N: not lifted by materialize; <message>`, exit 1.
> **＋** An entry with `superseded_by` is not applied and leaves no line; the Decision page of its Case is still written.
> **＋** An `update` with no content prints `generate: <slug>: an update with no content in the Spec; nothing applied` on stdout, changes no page and is marked applied.
> **－** The failure of one entry changes no other page: `vault/wiki/log.md` after it is level with the pages.

```then
update:
- slug: estimate-generate-fails-alone
  set:
    status: pending
  change: the Criterion replaced whole — Given out by the model of case 378, the When and Then as they stood (case 398.2)
```

```tasks
- [x] update `estimate-generate-fails-alone` — the Criterion replaced whole by the `when` and `then` of this Case
- [x] read `estimate-generate-fails-alone` — `uv run pytest tests/test_generate.py`
```

### Case 398.3 — The cascade

> **given:**
> `estimate-generate-cascades` — the Estimate whose Criterion is replaced and whose `purpose` is set.
> **＋** `guppi/generate.py` — the cascade after all entries: the status of Entities and Rules, the archive of a superseded decision, the children and `severity` of an Insight.
> **＋** `tests/test_generate.py` — fixes the cascade.
> **＋** `wiki/estimates/` and `wiki/lessons/` under `vault/`, and the archive — where the cascade reads the statuses.
> **＋** `estimate-generate-writes-rules-from-applies-to` — the `rules` of an Entity, a promise of its own.

> **when:**
> `uv run guppi generate` runs the cascade after all entries of a unit.

> **then:**
> An entity or rule whose live Estimates are all `passed` becomes `built`; a `built` one with a live Estimate not `passed` returns to `draft`; an Estimate standing `archived` with its file still under `wiki/estimates/`, or a slug with no page, is not counted; History `status: a → b · cascade`.
> **＋** A Decision page with `status: superseded` becomes `archived` with History `archived · superseded`; `superseded_by` and `deferred_by` are not touched.
> **＋** Every `clustered` child of an Insight with `status: actioned` becomes `archived` with History `archived · insight actioned`; the Insight's `children` does not change.
> **＋** The `severity` of every Insight is recounted: a child's status is read under `wiki/lessons/`, else in the archive; a child with no page counts live; an `open` Insight at 0 becomes `archived` with History `archived · no live child`, `children` kept; an `actioned` one at 0 stays.
> **－** A page without Estimates keeps its status, and the cascade writes no section of any page.

```then
update:
- slug: estimate-generate-cascades
  set:
    status: pending
    purpose: The cascade computes built, the archive of a superseded decision and the severity of an Insight, never by hand
  change: the Criterion replaced whole — the cascade by the model of case 378; the rules of an Entity left to estimate-generate-writes-rules-from-applies-to (case 398.3)
```

```tasks
- [x] update `estimate-generate-cascades` — the Criterion replaced whole by the `when` and `then` of this Case, and its `purpose`
- [x] read `estimate-generate-cascades` — `uv run pytest tests/test_generate.py`
```

## Case 399 — `rule-prespec`: the journal `-checks-the-plan` split by check

> **context:**
> Of the two Estimates of `rule-prespec` on the list of Case 378, only one needs work. `estimate-prespec-reconciles` was rewritten whole in the new model by Case 388: no `Given:`, no line on the bounds of an edit, its text agrees with the Render `.claude/skills/pre-spec/SKILL.md`; it waits only for its reading, which is W1. `estimate-prespec-checks-the-plan` is a journal: 9 `＋` lines in `then`, a `Given:` of five lines and a `－` line on the bounds of an edit. It repeats three neighbouring Estimates:
> - the mark of a `supersedes` — `estimate-prespec-catches-a-superseded-case`;
> - a Frontier line of the sprint closed by a Case — `estimate-prespec-binds-a-sprint-line`;
> - a `method` without a form — `estimate-prespec-catches-a-method-without-a-form`.
>
> It carries the line on `file` twice, and its `Given:` says the Criterion is `given`, `when` and `then` — the old model.
>
> The cut follows the functions of `guppi/prespec.py`: one function, one check, one promise, as the eleven neighbouring Estimates already stand:
> - the run (`resolve_session`, `check`, `check_grammar`, the parse of `then`) stays in `-checks-the-plan`;
> - `check_lines`, `check_frontier`, `check_tasks`, and `check_form` with `check_governed` become four new Estimates.
>
> Their slugs are free. `estimate-prespec-checks-the-plan` stands `passed`, `rule-prespec` `draft`. The readings are `pytest` with no change of code. Every item an `update` or a `create` with a `ref`; `frame-guppi` was not dispatched: the behaviour of the rule does not change. The agent read the code itself.

> **problem:**
> One Criterion holds six checks, three of them repeat neighbours, and it still describes the old model; a fault in any check turns the whole `failed`.

### Case 399.1 — The run of `prespec --check`

> **given:**
> `estimate-prespec-checks-the-plan` — the Estimate whose Criterion and `purpose` are replaced.
> **＋** `guppi/prespec.py` — `run`, `check`, `resolve_session`, `window_lines`, `check_grammar`.
> **＋** `guppi/materialize.py` — `parse_line`, `then_blocks`.
> **＋** `tests/test_prespec.py` — fixes `--check`.
> **＋** `vault/raw/<date>/<HHMM>/ledger.md` and the event logs — the session's window.
> **＋** `raw/<unit>/ledger.md:<n>: does not parse: <text>` — the finding on a ledger line that does not parse.

> **when:**
> `uv run guppi prespec --check <plan>` runs.

> **then:**
> The stamp is `--session`, else `CLAUDE_SESSION_ID`; with neither, one line on stderr `prespec: no session id; pass --session <stamp> from the hi: line`, exit 2, nothing checked; with no file at `<plan>`, `prespec: no plan file at <plan>`, exit 2.
> **＋** The session's window is found as the ledger hook finds it — by the stamped `hi`, over the event logs back to the date of its `session-start` — so the `hi` of yesterday's session is found after midnight; with no `hi` of the stamp, one line on stderr `prespec: no hi recorded for session <stamp>; nothing checked`, exit 0.
> **＋** Each finding is one line on stdout; exit 1 on any finding, 0 on none.
> **＋** A `then` block that does not parse is a finding of its Case, with the error.
> **＋** Every record line of the window — the session's `ledger.md` whole, plus the date-level ledgers from the `hi` time on — goes through `parse_line`; one that does not parse is the finding `raw/<unit>/ledger.md:<n>: does not parse: <text>`.

```then
update:
- slug: estimate-prespec-checks-the-plan
  set:
    status: pending
    purpose: prespec --check finds the session by its stamp, parses the plan and the ledger lines, and prints one line per finding, exit 1 on any
  change: the Criterion replaced whole — the run of prespec --check by the model of case 378; the lines, the frontier, the tasks and the form of an item moved to their own Estimates (case 399.1)
```

```tasks
- [x] update `estimate-prespec-checks-the-plan` — the Criterion replaced whole by the `when` and `then` of this Case, and its `purpose`
- [x] read `estimate-prespec-checks-the-plan` — `uv run pytest tests/test_prespec.py`
```

### Case 399.2 — The ledger lines and the items of the plan

> **given:**
> `estimate-prespec-matches-lines-and-items` — the new promise.
> **＋** `guppi/prespec.py` — `check_lines`, `items_of`.
> **＋** `tests/test_prespec.py` — fixes the check.
> **＋** `estimate-prespec-catches-a-superseded-case` — the lines of a superseded Case, a promise of its own.

> **when:**
> `uv run guppi prespec --check <plan>` compares the decision lines of the session's window with the items of the plan's `then` blocks.

> **then:**
> A decision line whose Case has no heading in the plan is the finding `case N: line [kind][slug]: no Case N heading in the plan`; one whose Case holds no item of its kind and slug is `case N: line [kind][slug] has no item in the plan`.
> **＋** An item with no decision line of its kind and slug under its own Case heading — a sub-case's heading included — is the finding `case N: item [kind][slug] has no decision line`.
> **＋** A nested `estimate` of a `create` needs no line of its own: the line of its parent covers it.

```then
create:
- slug: estimate-prespec-matches-lines-and-items
  ref: rule-prespec
  kind: QA
  purpose: Every decision line of the session has its item under its own Case in the plan, and every item its line
  method: uv run pytest tests/test_prespec.py
  tags:
  - session
  - workflow
  - harness
```

```tasks
- [x] create `estimate-prespec-matches-lines-and-items` — the check of case 59.1, moved out of `estimate-prespec-checks-the-plan`
- [x] read `estimate-prespec-matches-lines-and-items` — `uv run pytest tests/test_prespec.py`
```

### Case 399.3 — The Frontier of the session

> **given:**
> `estimate-prespec-checks-the-frontier` — the new promise.
> **＋** `guppi/prespec.py` — `check_frontier`.
> **＋** `vault/raw/<date>/<HHMM>/frontier.md` — the Frontier of the session.
> **＋** `tests/test_prespec.py` — fixes the check.
> **＋** `estimate-prespec-binds-a-sprint-line` — a sprint line closed by a Case, a promise of its own.
> **＋** `estimate-hi-writes-frontier` — an open line under `## Cases` and a sprint line closed `defer case N`, promises of its own.

> **when:**
> `uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<HHMM>/frontier.md`.

> **then:**
> A missing file is the finding `frontier: <path> is missing`.
> **＋** A closed line whose last segment after ` · ` is none of `case N`, `work`, `sprint`, `defer case N` is a finding.
> **＋** A line closed `case N` with no heading of Case N in the plan is a finding; one closed `defer case N` with no `defer` item under Case N is a finding.
> **＋** A line closed `[x]` with `sprint` is a finding.

```then
create:
- slug: estimate-prespec-checks-the-frontier
  ref: rule-prespec
  kind: QA
  purpose: The Frontier of the session exists, and every closed line names a closer the plan bears out
  method: uv run pytest tests/test_prespec.py
  tags:
  - session
  - workflow
  - harness
```

```tasks
- [x] create `estimate-prespec-checks-the-frontier` — the check of cases 59.2 and 310.6, moved out of `estimate-prespec-checks-the-plan`
- [x] read `estimate-prespec-checks-the-frontier` — `uv run pytest tests/test_prespec.py`
```

### Case 399.4 — `tasks` and the read line

> **given:**
> `estimate-prespec-requires-a-task-line` — the new promise.
> **＋** `guppi/prespec.py` — `check_tasks`, `estimates_to_read`.
> **＋** `guppi/generate.py` — `READ_LINE`, the pattern the ticker matches.
> **＋** `tests/test_prespec.py` — fixes the check.
> **＋** `estimate-prespec-catches-a-command-line-off-form` — a render or sprint line off form, a promise of its own.

> **when:**
> `uv run guppi prespec --check <plan>` reads the `tasks` block of each Case of the plan.

> **then:**
> A Case with a decision line of a kind other than `defer` in the window and no `tasks` block is the finding `case N: decision lines and no tasks block`.
> **＋** An Estimate the Case's `then` block creates or sets `pending` needs a line `` - [ ] read `<slug>` `` whose first backticked slug is that Estimate, matched by `READ_LINE`; with none, the finding `case N: <slug> has no task line`.
> **＋** A slug named only on another Estimate's read line is the finding `case N: <slug> is named on another read line, not its own`.
> **－** A Case that a `{supersedes:case N}` of the window names needs no `tasks` block.

```then
create:
- slug: estimate-prespec-requires-a-task-line
  ref: rule-prespec
  kind: QA
  purpose: A Case with work has its tasks block, and every Estimate it creates or sets pending has a read line of its own
  method: uv run pytest tests/test_prespec.py
  tags:
  - session
  - workflow
  - harness
```

```tasks
- [x] create `estimate-prespec-requires-a-task-line` — the check of cases 59.3 and 327, moved out of `estimate-prespec-checks-the-plan`
- [x] read `estimate-prespec-requires-a-task-line` — `uv run pytest tests/test_prespec.py`
```

### Case 399.5 — The form of an item

> **given:**
> `estimate-prespec-checks-the-form-of-an-item` — the new promise.
> **＋** `guppi/prespec.py` — `check_form`, `check_governed`.
> **＋** `tests/test_prespec.py` — fixes the check.
> **＋** `estimate-prespec-catches-a-method-without-a-form` — the `method` of an Estimate item, a promise of its own.

> **when:**
> `uv run guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

> **then:**
> A Case whose `then` block holds two or more Estimate items — a `create`, or an `update` with `set: {status: pending}` — without a written `sections: Criterion` is the finding `case N: two promises in one Case — split it`.
> **＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
> **＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
> **＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.

```then
create:
- slug: estimate-prespec-checks-the-form-of-an-item
  ref: rule-prespec
  kind: QA
  purpose: An item of the plan carries one promise per Case, names a page that exists or is created, and no file
  method: uv run pytest tests/test_prespec.py
  tags:
  - session
  - workflow
  - harness
```

```tasks
- [x] create `estimate-prespec-checks-the-form-of-an-item` — the checks of cases 203.1, 221 and 320, moved out of `estimate-prespec-checks-the-plan`
- [x] read `estimate-prespec-checks-the-form-of-an-item` — `uv run pytest tests/test_prespec.py`
```

## Case 400 — `rule-plan-mode`: the last Estimate of the old model; the note of the eleven leaves Slice 3g

> **context:**
> `estimate-plan-mode-names-its-estimates` is the last page on the list of Case 378. Its `Given:` of seven lines is the history of Case 187: `materialize.py:583`, `DERIVED_KEYS`, a free slug, the defer of Case 182; none of it stands in the code any more. Its `then` line on an `update` of a Render says such an `update` touches the Estimate of the live reading; since Case 378.5 the opposite holds — the Purpose of `rule-plan-mode` and the Render of `rule-case-protocol` already say it does not — so the line is false. Three lines repeat the promises of others:
> - "the Case names the Estimate by slug" — `estimate-case-protocol-case-form` (396.1);
> - "only a replaced Criterion sets `pending`" — `estimate-materialize-changes-a-named-part-alone` (397.3);
> - "the `contract` flag decides nothing" — `estimate-materialize-assembles` (397.1).
>
> What stays the page's own is one thing: what a Case does not name — an `update` of a Purpose names no Estimate, an `update` of a Render names no Estimate of the live reading. The Estimate stands `passed`, `rule-plan-mode` `built`. The other Estimate of the rule, `estimate-plan-mode-verified`, speaks of the check of Plan Mode and is not touched. With this, C7 is done, and by Case 395 its note leaves Slice 3g by an `update` of the sprint page: 400.2, a `replace` pair that removes the line of the eleven together with the head of the next line, so no blank line stays. Every item an `update` with a `ref`; `frame-guppi` was not dispatched.

> **problem:**
> The Criterion describes code that is gone, one of its lines contradicts Case 378.5, and three repeat the promises of others; the note of the eleven keeps Slice 3g open though its work is done.

### Case 400.1 — What a Case does not name

> **given:**
> `estimate-plan-mode-names-its-estimates` — the Estimate whose Criterion, `purpose` and `method` are replaced.
> **＋** `rule-plan-mode` — its Purpose states which Estimate a Case touches (case 378.5).
> **＋** `rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the paragraph on the Criterion.
> **＋** `estimate-case-protocol-case-form` — the naming of an Estimate by slug and the `update` of each Estimate whose Criterion speaks of a change, a promise of its own.
> **＋** `estimate-materialize-changes-a-named-part-alone` — the status of an Estimate an `update` names, a promise of its own.

> **when:**
> The person ratifies a Case that updates the `Purpose` or the `Render` of a rule page.

> **then:**
> A Case that updates a rule's `Purpose` names no Estimate for it in its `then` block.
> **＋** A Case that updates a rule's `Render` names no Estimate of the live reading of that Render.

```then
update:
- slug: estimate-plan-mode-names-its-estimates
  set:
    status: pending
    purpose: A Case that updates a Purpose or a Render names no Estimate for it but the Estimate of the behaviour it changes
    method: 'by hand at the close of a session: each Case that updates a Purpose or a Render of a rule, and the Estimates its then block names'
  change: the Criterion replaced whole — what a Case does not name, by case 378.5; the given of case 187 out, the lines other Estimates hold left to them (case 400.1)
```

```tasks
- [x] update `estimate-plan-mode-names-its-estimates` — the Criterion replaced whole by the `when` and `then` of this Case, its `purpose` and `method`
- [x] read `estimate-plan-mode-names-its-estimates` — by hand, the Cases of this session at its close
```

### Case 400.2 — The note of the eleven leaves Slice 3g

> **given:**
> `entity-sprint-migration` — the section `## Milestones`, Slice 3g, as Case 395 leaves it.
> **＋** `vault/wiki/sprint.md` — its render, written by `uv run guppi sprint`.
> **＋** `rule-sprint` — a note keeps its milestone open until an `update` removes it.

> **when:**
> `uv run guppi sprint` writes `vault/wiki/sprint.md` from `entity-sprint-migration`.

> **then:**
> Slice 3g shows three notes — the journals, `Given:` out of the rest, the old shape — and no note of the eleven Estimates.

```then
update:
- slug: entity-sprint-migration
  replace:
  - old: |-
      - the eleven Estimates of the old model named by Case 378 rewritten whole, one Case for each target rule: `estimate-case-protocol-case-form`, `estimate-case-protocol-loaded`, `estimate-materialize-assembles`, `estimate-materialize-walks-dates`, `estimate-materialize-marks-superseded`, `estimate-generate-writes-the-decision-page`, `estimate-generate-fails-alone`, `estimate-generate-cascades`, `estimate-prespec-reconciles`, `estimate-prespec-checks-the-plan`, `estimate-plan-mode-names-its-estimates`
      - the journals split
    new: '- the journals split'
  change: 'Slice 3g: the note of the eleven Estimates done — cases 396 to 400, 388 for estimate-prespec-reconciles (case 400.2)'
```

```tasks
- [x] update `entity-sprint-migration` — the note of the eleven Estimates out of Slice 3g
- [x] `uv run guppi sprint`
```

## Case 401 — The journals: `estimate-lint-catches` split by class, `Given:` out of the other two

> **context:**
> The note of the journals in Slice 3g names three pages; only one of them is a real journal. `estimate-lint-catches`, the one Estimate of `rule-lint`, holds 12 `＋` lines in `then` and 2 in `Given:`, most of them one class of finding each and one line three classes, while `guppi/lint.py` checks 14 classes; a broken class turns the whole of lint `failed`. In the other two the long part is `Given:`, not `then`:
> - `estimate-generate-ticks-the-spec` holds 5 `＋` lines in `then` and 8 lines of the history of cases 130.2–320 in `Given:`;
> - `estimate-materialize-skips-a-carried-over-unit` holds one line in `then` and 10 lines in `Given:` written at Case 190.3 ("the slug is free", "`governs` is one file", "the word parked is not used").
>
> For these two it is enough to remove `Given:` and the lines on the bounds of an edit; the other lines were checked against the code. Lint is cut by the functions of `guppi/lint.py`, by what a finding is about:
> - the run, the schema, the layout, the paths and the markers stay in `estimate-lint-catches`;
> - links: `check_refs`, `check_edges`, `check_criterion`, `check_origin`, `check_decision`, `check_orphans`;
> - statuses: `check_status`, `check_unread`, `check_deferred`;
> - `method`;
> - the `unmigrated` count.
>
> The four new slugs are free. All three pages stand `passed`; `rule-lint`, `rule-page-generation` and `rule-materialize` stand `built` and go `draft` by the cascade until the readings. The readings are `pytest` with no change of code. The note of the journals leaves Slice 3g in 401.8. Every item with a `ref`; `frame-guppi` was not dispatched. The agent read the code itself.

> **problem:**
> One Criterion holds the fourteen classes of lint, which break and are fixed apart; in the two other Criteria `Given:` retells the history of their Case.

### Case 401.1 — The run of lint, the schema, the layout, the paths, the markers

> **given:**
> `estimate-lint-catches` — the Estimate whose Criterion and `purpose` are replaced.
> **＋** `guppi/lint.py` — `lint`, `check_schema`, `check_descriptions`, `check_layout`, `check_paths`, `check_markers`.
> **＋** `vault/wiki/<category>/schema.yaml` — the schema of each category.
> **＋** `vault/archive/` — the archived pages, which lint does not read.
> **＋** `<category>/<slug>: <class>: <what>` — the form of a finding; `<!-- /slug -->` and `<!-- /child -->` — the closing markers a Render is read for.
> **＋** `tests/test_lint.py` — fixes each class.

> **when:**
> `uv run guppi lint` reads the live pages under `vault/wiki/<category>/`.

> **then:**
> Each finding is one line `<category>/<slug>: <class>: <what>`; exit 1 on any finding, 0 and no output on a clean vault; nothing is written.
> **＋** `schema`: a missing required field or section, a value outside the list of `values`, a conditional not met, a field of `properties.single` holding a list; `## When` is never required on a Decision page.
> **＋** `schema-description`: a field or section the lists of `schema.yaml` name without a description under `fields` or `sections`, or a description of a name no list carries.
> **＋** `layout`: a page whose `type` does not match its folder, a page whose `slug` field is not its filename, a `.md` at the root of `vault/wiki/` that no live rule page names.
> **＋** `path`: a file named in `implementation_ref` or `governs` that does not exist.
> **＋** `markers`: a page with `enforcement: render` without `## Render`, or whose Render does not open with `<!-- slug -->` and close with `<!-- /slug -->`; a page with `render_mode: full` whose Render holds a closing line `<!-- /child -->` for one of its `children`.
> **－** A page under `vault/archive/` is not read.

```then
update:
- slug: estimate-lint-catches
  set:
    status: pending
    purpose: lint reads every live page against the schema of its category and prints one line per finding, exit 1 on any
  change: the Criterion replaced whole — the run, schema, layout, paths and markers by the model of case 378; links, statuses, method and the unmigrated count moved to their own Estimates (case 401.1)
```

```tasks
- [x] update `estimate-lint-catches` — the Criterion replaced whole by the `when` and `then` of this Case, and its `purpose`
- [x] read `estimate-lint-catches` — `uv run pytest tests/test_lint.py`
```

### Case 401.2 — Links

> **given:**
> `estimate-lint-finds-a-broken-link` — the new promise.
> **＋** `guppi/lint.py` — `check_refs`, `check_edges`, `check_criterion`, `check_origin`, `check_decision`, `check_orphans`.
> **＋** `vault/wiki/` — the live pages whose links are followed.
> **＋** `vault/raw/` and `vault/archive/` — where the ledger an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` names may stand, and `decision-case-N` the Decision page a `### case N` block names.
> **＋** `tests/test_lint.py` — fixes each class.

> **when:**
> `uv run guppi lint` follows the links of the live pages under `vault/wiki/`.

> **then:**
> `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a body `[[…]]` that no live or archived page carries; a body `[[…]]` may name a file under `vault/wiki/` by stem or path; a `[[…]]` inside a code span is no link.
> **＋** `ref`: an `applies_to` naming a page that is not an Entity; an Entity whose `rules` differs from the live rules whose `applies_to` names it, the difference as `+slug` and `-slug`.
> **＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate; a `### case N` block under an Estimate's `## Criterion` with no live or archived `decision-case-N`.
> **＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
> **＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer`, or with `kind` or `target_slug`; a slug of its lists with a category prefix that no live or archived page carries.
> **＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.

```then
create:
- slug: estimate-lint-finds-a-broken-link
  ref: rule-lint
  kind: QA
  purpose: A link, an origin or a Decision list that names nothing, and a page nothing names, are findings of lint
  method: uv run pytest tests/test_lint.py
  tags:
  - harness
  - workflow
```

```tasks
- [x] create `estimate-lint-finds-a-broken-link` — the classes `ref`, `origin`, `decision` and `orphan`, moved out of `estimate-lint-catches`
- [x] read `estimate-lint-finds-a-broken-link` — `uv run pytest tests/test_lint.py`
```

### Case 401.3 — Statuses

> **given:**
> `estimate-lint-checks-the-statuses` — the new promise.
> **＋** `guppi/lint.py` — `check_status`, `check_unread`, `check_deferred`, `is_placeholder`.
> **＋** `vault/wiki/` — the live pages whose statuses are read.
> **＋** `tests/test_lint.py` — fixes each class.

> **when:**
> `uv run guppi lint` reads the `status` of the live pages under `vault/wiki/`.

> **then:**
> `status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged.
> **＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
> **＋** `unread`: every Estimate `pending` or `failed`, one finding each, `unread: <status>`.
> **＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.

```then
create:
- slug: estimate-lint-checks-the-statuses
  ref: rule-lint
  kind: QA
  purpose: A status its Estimates do not support, an Estimate not read, and a placeholder are findings of lint
  method: uv run pytest tests/test_lint.py
  tags:
  - harness
  - workflow
```

```tasks
- [x] create `estimate-lint-checks-the-statuses` — the classes `status`, `unread` and `deferred`, moved out of `estimate-lint-catches`
- [x] read `estimate-lint-checks-the-statuses` — `uv run pytest tests/test_lint.py`
```

### Case 401.4 — `method`

> **given:**
> `estimate-lint-checks-the-method` — the new promise.
> **＋** `guppi/lint.py` — `check_method`, `method_of`, `names_a_form`; its finding `method: names no tests/ file, pytest or make target and is not a reading`.
> **＋** `Makefile` — the targets a `method` may name.
> **＋** `estimate-prespec-catches-a-method-without-a-form` — the one predicate `names_a_form` shared with pre-spec, a promise of its own.
> **＋** `tests/test_lint.py` — fixes the class.

> **when:**
> `uv run guppi lint` reads the `method` of each live Estimate — the field, or `## Method` on a page of the old shape.

> **then:**
> For an Estimate of a Leaf, a `tests/` file that exists, the word `pytest`, a `make <target>` of the `Makefile`, or `by hand` passes; else the finding `method: names no tests/ file, pytest or make target and is not a reading`.
> **＋** A named `tests/` file that does not exist, or a `make <target>` the `Makefile` does not hold, is a finding.
> **＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it; `by hand` without one passes when every Estimate of the children is a reading or a sibling Estimate names a `make <target>` of the `Makefile`; else a finding.

```then
create:
- slug: estimate-lint-checks-the-method
  ref: rule-lint
  kind: QA
  purpose: An Estimate whose method names no form of reading, or a test file or make target that does not exist, is a finding of lint
  method: uv run pytest tests/test_lint.py
  tags:
  - harness
  - workflow
```

```tasks
- [x] create `estimate-lint-checks-the-method` — the class `method`, moved out of `estimate-lint-catches`
- [x] read `estimate-lint-checks-the-method` — `uv run pytest tests/test_lint.py`
```

### Case 401.5 — The `unmigrated` count

> **given:**
> `estimate-lint-counts-the-unmigrated` — the new promise.
> **＋** `guppi/lint.py` — `check_unmigrated`, `is_old_shape`.
> **＋** `vault/wiki/estimates/` — the live Estimates it counts.
> **＋** `tests/test_lint.py` — fixes the count.

> **when:**
> `uv run guppi lint` reads the live Estimates under `vault/wiki/estimates/`.

> **then:**
> One line `estimates: unmigrated: <N> pages in the shape before case 193` — `page` when N is 1 — N the Estimates without a `method` field, or with `## Context`, `## Method` or a `### case N` block under `## Criterion`.
> **＋** At zero there is no line.

```then
create:
- slug: estimate-lint-counts-the-unmigrated
  ref: rule-lint
  kind: QA
  purpose: lint counts the Estimates still in the shape before case 193 in one line, and prints none at zero
  method: uv run pytest tests/test_lint.py
  tags:
  - harness
  - workflow
```

```tasks
- [x] create `estimate-lint-counts-the-unmigrated` — the class `unmigrated`, moved out of `estimate-lint-catches`
- [x] read `estimate-lint-counts-the-unmigrated` — `uv run pytest tests/test_lint.py`
```

### Case 401.6 — `generate` ticks the lines of a Spec

> **given:**
> `estimate-generate-ticks-the-spec` — the Estimate whose Criterion is replaced.
> **＋** `guppi/generate.py` — the ticker of page lines and `read` lines, `READ_LINE`.
> **＋** `vault/raw/<date>/<HHMM>/` — `spec.md` and `materialize.yaml` of each session.
> **＋** `vault/archive/` — the archived sessions, whose Specs are not read.
> **＋** `tests/test_generate.py` — fixes the ticks.

> **when:**
> `uv run guppi generate` applied an entry of `materialize.yaml` and marked it `applied`.

> **then:**
> For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit the first unticked line `` - [ ] <kind> `<slug>` `` in the section of the entry's Case becomes `- [x]`; nothing else in the file changes; two entries of one kind and slug in one Case tick two lines, in order.
> **＋** For an `estimate` entry, and for a `create` entry with `folded`, every unticked line `` - [ ] read `<slug>` `` of every `spec.md` under `vault/raw/` becomes `- [x]` — the Spec beside the yaml first, then those of the other session folders, oldest first.
> **＋** In the Spec beside the yaml, a `read` line in the section of a Case whose first decision entry carries a `line` greater than the `line` of the `estimate` entry is not the reading's line; the search goes on.
> **＋** In any Spec, a `read` line in the section of a Case whose entries are marked `superseded_by` — among the run's entries for the Spec beside the yaml, in the `materialize.yaml` beside it for another Spec — is not the reading's line; with no yaml beside a Spec nothing is skipped there.
> **＋** A `create` entry with `folded` ticks both its page line and its read line; the filter by `line` does not apply to it, the filter by `superseded_by` does.
> **－** A line, a section or a Spec not found raises no error and prints nothing on stderr; the entry is `applied` all the same.
> **－** A `lesson` entry and an entry marked `failed` tick no line.
> **－** A `spec.md` under `vault/archive/` is not read.

```then
update:
- slug: estimate-generate-ticks-the-spec
  set:
    status: pending
  change: the Criterion replaced whole — Given out by the model of case 378, the When and Then as they stood, the case numbers out of the lines (case 401.6)
```

```tasks
- [x] update `estimate-generate-ticks-the-spec` — the Criterion replaced whole by the `when` and `then` of this Case
- [x] read `estimate-generate-ticks-the-spec` — `uv run pytest tests/test_generate.py`
```

### Case 401.7 — A unit with `carry.md` is skipped

> **given:**
> `estimate-materialize-skips-a-carried-over-unit` — the Estimate whose Criterion is replaced.
> **＋** `guppi/materialize.py` — `is_carried_over`, `materialize_date`.
> **＋** `vault/raw/<date>/<HHMM>/carry.md` — the mark `/carry` leaves on a conserved session.
> **＋** `tests/test_materialize.py` — fixes the skip.

> **when:**
> `uv run guppi materialize` reaches a unit whose folder holds `carry.md`.

> **then:**
> The unit is skipped and one line naming it is printed on stdout; no `materialize.yaml` is written or extended for it.
> **－** The unit is marked neither `applied` nor `failed`.

```then
update:
- slug: estimate-materialize-skips-a-carried-over-unit
  set:
    status: pending
  change: the Criterion replaced whole — the Given of case 190.3 out by the model of case 378 (case 401.7)
```

```tasks
- [x] update `estimate-materialize-skips-a-carried-over-unit` — the Criterion replaced whole by the `when` and `then` of this Case
- [x] read `estimate-materialize-skips-a-carried-over-unit` — `uv run pytest tests/test_materialize.py`
```

### Case 401.8 — The note of the journals leaves Slice 3g

> **given:**
> `entity-sprint-migration` — the section `## Milestones`, Slice 3g, as Cases 395 and 400.2 leave it.
> **＋** `vault/wiki/sprint.md` — its render, written by `uv run guppi sprint`.
> **＋** `rule-sprint` — a note keeps its milestone open until an `update` removes it.

> **when:**
> `uv run guppi sprint` writes `vault/wiki/sprint.md` from `entity-sprint-migration`.

> **then:**
> Slice 3g shows two notes — `Given:` out of the rest, the old shape — and no note of the journals.

```then
update:
- slug: entity-sprint-migration
  replace:
  - old: |-
      - the journals split, one promise for each Estimate: `estimate-lint-catches`, `estimate-generate-ticks-the-spec`, `estimate-materialize-skips-a-carried-over-unit`
      - every other Estimate:
    new: '- every other Estimate:'
  change: 'Slice 3g: the note of the journals done (case 401)'
```

```tasks
- [x] update `entity-sprint-migration` — the note of the journals out of Slice 3g
- [x] `uv run guppi sprint`
```

## Case 402 — `rule-spec-write`: a value holding a backtick only in a padded span

> **context:**
> The hook of `rule-spec-write` reads the value of a sub-point with `code_value` in `guppi/ratified.py`, as CommonMark reads a code span. Case 393 set the rule: a value that opens or closes with a backtick takes its outer span padded by one space on each side, and a value that opens with a code span and ends in text, written without the spaces, is refused. A second shape remains: a value that opens and closes with a code span, written without the spaces — ``` ```a` and `b``` ``` — is read by CommonMark and by `code_value` alike as one span whose edge backticks are eaten, and the hook writes the value without them, silently. The text cannot tell this from a lawful span: CommonMark reads both the same. The one mechanical guard left is to require the padding whenever the value holds a backtick.
>
> `rule-spec-write` stands `built`, deferred by Case 394; this Case takes the defer up. Its one Estimate, `estimate-spec-write-copies-the-ratified-case`, speaks of the form of a value, so its Criterion is replaced whole. The rule of the form also stands in the Render of `rule-case-protocol` (the Language paragraph); by Case 378.5 the edit of the Render does not touch `estimate-case-protocol-loaded`.
>
> `frame-guppi` found one contradiction: the fixture `SHOWING` in `tests/test_ratified.py` carries `` old: ``the `old` text`` `` without the spaces; under the new rule it would be refused and three tests of the writer would fail. A task line for the fixture was added. No other user of `code_value` stands in `guppi/`. In this session the agent itself wrote values holding backticks without the spaces, the `old` of Case 395 among them; after the change such values are refused.

> **problem:**
> A value that opens and closes with a code span, written without the spaces, enters the Spec with its edge backticks lost, and nothing says so. Should the hook refuse a span whose content holds a backtick when the outer span is not padded?

> **given:**
> `rule-spec-write` — the hook that writes a ratified Case into the plan file; its `How it works`.
> **＋** `guppi/ratified.py` — `code_value` and `read_tasks`, the reading of a sub-point value.
> **＋** `guppi/gate.py` — `plan_path`, the plan file of the session.
> **＋** `.claude/settings.json` — the `Stop` hook `uv run guppi ratified`.
> **＋** `tests/test_ratified.py` — fixes the reading of a value and the fixture `SHOWING`.
> **＋** `estimate-spec-write-copies-the-ratified-case` — the promise of the hook; its Criterion names the form of a value.
> **＋** `rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the form of a sub-point value in the Language paragraph.

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads the session's transcript and finds the last earlier reply that shows `## Case N —` whole.

> **then:**
> The hook writes that Case into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `given`, `when` and `then` as they stand in the chat; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points.
> **＋** It writes the same text the same way into the ratified copy `<plan>.ratified.md` beside the plan file.
> **＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
> **＋** A value that holds a backtick in an outer span not padded on both sides is refused: exit 2 with `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
> **＋** `recommend` and `ratification` are not written.
> **＋** When the last showing of Case N is a `DIFF` block, not the Case whole, the hook writes nothing for it.
> **＋** No plan file in the event log, no showing of Case N, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **－** A Case whose lines are all `defer` is not written by the hook: the agent appends it under `## Deferred`.

```then
update:
- slug: rule-spec-write
  replace:
  - old: 'or a sub-point it cannot read: exit 2 with the reason on stderr'
    new: 'or a sub-point it cannot read — a value holding a backtick whose outer span is not padded by one space on each side among them (case 402): exit 2 with the reason on stderr'
  change: a value holding a backtick is refused unless its outer span is padded by one space on each side (case 402, supersedes 394)
- slug: rule-case-protocol
  replace:
  - old: a value that opens or closes with a backtick takes its outer span padded by one space on each side, as CommonMark reads it
    new: a value that holds a backtick takes its outer span padded by one space on each side, and the hook refuses one unpadded (case 402)
  change: a value that holds a backtick takes its outer span padded by one space on each side (case 402)
- slug: estimate-spec-write-copies-the-ratified-case
  set:
    status: pending
  change: the Criterion replaced whole — a value holding a backtick padded by one space, an unpadded one refused (case 402)
```

```tasks
- [x] update `rule-spec-write` — one clause in `How it works`: the refusal of an unpadded value holding a backtick
- [x] update `rule-case-protocol` — the form of a sub-point value in the Language paragraph of the Render
- [x] update `estimate-spec-write-copies-the-ratified-case` — the Criterion replaced whole by the `when` and `then` of this Case
- [x] `guppi/ratified.py` — `code_value` or `read_tasks`: a value holding a backtick in an outer span not padded on both sides returns the refusal with its reason; the one-sided pad trimming goes
- [x] `tests/test_ratified.py` — the padding test: an unpadded value opening and closing with a code span is refused with the reason, a padded one read; the `old` of `SHOWING` padded
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-spec-write-copies-the-ratified-case` — `uv run pytest tests/test_ratified.py`
```

## Case 405 — A defer is written in the reply that asks for it, with no ratification of its own

> **context:**
> Today a deferred decision is shown in the short form and waits for the person's "ratify" like any Case; only then does the acknowledging reply write its `LEDGER` line. The decision to defer, though, is the person's own words ("keep it", "defer it"); the second question checks only the wording of `purpose`. In this session C3 and C4 took one round more for it. `frame-guppi` found three contradictions, all taken in:
> 1. The one rule, "nothing changes without a Decision ratified by the human": it now says outright that the person's words asking for the defer are its ratification.
> 2. The `ratification` row of the Sections table is required of every Case: the short form now names it among the sections it does not hold.
> 3. Retro has no Frontier: the closing of a Frontier line stays with Plan Mode alone.
>
> `estimate-case-protocol-acknowledging-reply` speaks of the reply after a ratification; a defer no longer has one, so it is not touched. The slug of the new Estimate is free. `rule-case-protocol` stands `draft`.

> **problem:**
> Does a defer need a round of ratification of its own when the person asked for it?

> **given:**
> `rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the section on the short form.
> **＋** `estimate-case-protocol-defers-in-one-reply` — the new promise.
> **＋** `rule-retro` — its Render `.claude/skills/retro/SKILL.md`: a short defer at Retro, which closes with three lists and no Frontier.
> **＋** `raw/<date>/<hi HHMM>/spec.md` and the plan file — where the short Case is appended.
> **＋** `rule-ledger-write` — writes the `LEDGER` lines of a reply.
> **＋** `estimate-case-protocol-acknowledging-reply` — the reply after a ratification; a defer has none.

> **when:**
> The person asks in the chat to defer an item, in Plan Mode or at Retro.

> **then:**
> In the same reply the agent appends the Case in the short form — `context`, `problem`, the `defer` block, no `ratification` section — under `## Deferred` of the plan file, or of `raw/<date>/<hi HHMM>/spec.md` at Retro, shows it in the chat, and ends the reply with its `LEDGER` block, one `defer` line per target.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** In Plan Mode the reply ends with the Frontier, the line of the item closed `[-] … · defer case N`; at Retro no Frontier is shown.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, written the same way.

```then
create:
- slug: estimate-case-protocol-defers-in-one-reply
  ref: rule-case-protocol
  kind: QA
  purpose: A defer the person asks for is shown and written in the same reply, with no round of ratification
  method: by hand, the first defer the person asks for after the render
  tags:
  - session
  - workflow
  - ledger
update:
- slug: rule-case-protocol
  replace:
  - old: no `recommend`, `given`, `when` or `then` section
    new: no `recommend`, `given`, `when`, `then` or `ratification` section
  - old: Either way the agent appends it to `raw/<date>/<hi HHMM>/spec.md` under the `## Deferred` heading before writing its ledger line
    new: 'Either way the person''s words asking for the defer are its ratification: in the same reply the agent appends it under the `## Deferred` heading of the plan file, or of `raw/<date>/<hi HHMM>/spec.md` at Retro, shows it, and ends the reply with its ledger line — in Plan Mode then the Frontier with the line closed `[-] … · defer case N` — and asks nothing about it; a wording the person corrects is a new short Case with `{supersedes:case N}`, written the same way (case 405). It stands there before its ledger line'
  change: a defer is written in the reply that asks for it, the person's words its ratification (case 405)
```

```tasks
- [x] update `rule-case-protocol` — the section on the short form in the Render: no `ratification` section, the defer written in the reply that asks for it
- [x] create `estimate-case-protocol-defers-in-one-reply` — the new promise of the short form
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-defers-in-one-reply` — by hand, the first defer the person asks for after the render
```

## Deferred

## Case 403 — Whether frame-guppi pays

> **context:**
> Case 391.2 brought in `frame-guppi`: before the first showing of a Case that changes the behaviour of a rule or a hook, the agent gives the agent the `given` of the Case and gets back the contradictions. The person asked to judge from the numbers of the next session whether it pays, and to roll it back by a Case if it does not. In session 1916 it was dispatched once, in Case 402: it found one real contradiction — the fixture `SHOWING`, without whose fix three tests of the writer would fail; the dispatch cost about 73 thousand tokens and 3 minutes. The seven other Cases changed no behaviour of a rule and dispatched nothing. One dispatch is too few to judge.

> **problem:**
> Keep `frame-guppi` or roll it back: decided once there is more than one dispatch.

```then
defer:
  - slug: rule-frame-check
    type: rule
    purpose: Whether frame-guppi pays — the contradictions it finds against its tokens and time over the sessions after 1303; rolled back by a Case if it does not
```

## Case 404 — The limit of 400 000 tokens

> **context:**
> Case 392.2 set a limit of 400 000 tokens, a constant in `guppi/context.py`: past it the `Stop` hook adds a warning to the size line, and the `UserPromptSubmit` hook orders the session closed with `/retro` and `/handoff`. The person proposed the figure as one to discuss. In session 1916 the limit was never reached; there is no data yet to move it up or down.

> **problem:**
> Which limit is right: decided once a session reaches it and the behaviour of the context near it is seen.

```then
defer:
  - slug: rule-context-size
    type: rule
    purpose: The limit of 400 000 tokens in guppi/context.py, proposed as a figure to discuss; judged once a session reaches it
```
