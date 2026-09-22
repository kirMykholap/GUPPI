<!-- approved 23:51:17 · session 13db9cea -->

# Spec — 2026-09-21, session 1853

## Case 299 — a Case superseded in its own session leaves the Spec (takes up 298)

> **context:**
> The Spec is the plan the person approves at the end of Plan Mode. In session 1315 Case 296 superseded 291.1 before the approval, and the Spec of 1315 still holds 291.1 whole: its sections, its `then` block, its five task lines. Nothing ticks or removes them: `generate` neither applies nor ticks the entries of a superseded Case (151, 286), Retro does not count them (282). The lines stay `[ ]` for good and read like debt. The sentence of the schema, "the replaced text stays in the Spec of its session and in History", is right for a supersede from a later session, whose Spec is archived history; inside one session the superseded Case was never the plan. Three scripts lean on the Case being in the Spec: `prespec --check` (`check_lines`) prints "no Case N heading in the plan" for a ledger line whose Case left the plan — so today removing 291.1 from the plan would be a finding; `materialize` without the Case in the Spec marks the entry `incomplete: [then]` and the `decisions` record `incomplete: [context, problem, given, when]`; `generate` writes the body of the Decision page from `case_text` — without it, a page with no `## Context` and no `## Problem`. The defect of the librarian's run of 1315: the `then` block of Case 298 is not YAML (a colon in `no incomplete: [then]`, line 384 of Spec 1315), so the three entries of 298 are `incomplete` and `decision-case-298` has no `## Deferred`; the `deferred_by` on the three pages stand.
> The pages: `rule-case-protocol` `draft`, `rule-prespec` `built`, `rule-materialize` `draft`, `rule-page-generation` `draft`, the last three with `deferred_by: decision-case-298`; `index.md` §7 a Rule-class file, by hand. The Estimates the Case touches: `estimate-case-protocol-loaded` (the live reading of the Render), the new `estimate-prespec-catches-a-superseded-case`, `estimate-materialize-marks-superseded` (in the shape before case 193, no `Given`), `estimate-generate-writes-the-decision-page`; the other Estimates of these rules are not touched. The slug of the new Estimate is free, in `wiki/` and in the archive.

> **problem:**
> Where the rule stands and what the three scripts do, so that the agent removes a superseded Case from the plan, pre-spec catches one left there, and `materialize` and `generate` invent no debt from its absence. And how `decision-case-298` is repaired.

> **given:**
> `{supersedes:case N}` on a decision line marks every entry of Case N `superseded_by` in the yaml of any unit (175, 177); `generate` applies none of them and ticks none of their lines (151, 286); Retro does not count them (282).
> **＋** The Spec of a session is the plan approved at the end of Plan Mode, copied to `raw/<date>/<hi HHMM>/spec.md` (73.1); `## Case N — …` or `### Case N.M — …` is a heading, its section runs to the next such heading.

### Case 299.1 — the schema and `index.md` §7: a Case superseded in its session leaves the Spec

> **given:**
> `{supersedes:case N}` on a decision line marks every entry of Case N `superseded_by` in the yaml of any unit (175, 177); `generate` applies none of them and ticks none of their lines (151, 286); Retro does not count them (282).
> **＋** The Spec of a session is the plan approved at the end of Plan Mode, copied to `raw/<date>/<hi HHMM>/spec.md` (73.1); `## Case N — …` or `### Case N.M — …` is a heading, its section runs to the next such heading.
> **＋** `case-schema.md` is the Render of `rule-case-protocol`; an `update` of the Render touches the Estimate of its live reading (187); `index.md` §7 is a Rule-class file, by hand.

> **when:**
> The agent in Plan Mode supersedes a Case of the same session, before the Spec is approved; the person reads the schema.

> **then:**
> The Spec holds no section of the superseded Case — no heading, no blockquote, no `then` or `tasks` block; the superseding Case is written whole, with its own `tasks`; the text of the superseded Case is not kept — its ledger lines name its targets, and the `context` of the superseding Case says what it replaced.
> **＋** A Frontier line closed by the superseded Case is closed again by the superseding one.
> **＋** The paragraph of the schema on the Criterion and §7 of `index.md` say it in one sentence beside "the replaced text stays in the Spec of its session".
> **－** A supersede from a later session does not change: the earlier Spec keeps the text, as today.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "nothing removed by a `{supersedes:case N}` — the replaced text stays in the Spec of its session and in History."
        new: "nothing removed by a `{supersedes:case N}` — the replaced text stays in the Spec of its session and in History. A Case superseded in its own session, before the Spec is approved, leaves the Spec — no heading, no section, no `then` or `tasks` block — and the superseding Case is written whole; its text is not kept — its ledger lines name its targets, the `context` of the superseding Case says what it replaced — a Frontier line it closed is closed again by the superseding Case, and pre-spec catches a superseded Case still in the plan (case 299.1)."
    change: the Spec paragraph on the Criterion — a Case superseded in its own session leaves the Spec, the superseding Case is written whole (case 299.1)
  - slug: estimate-case-protocol-loaded
    set: {status: pending}
    change: one line of the Criterion — the Spec paragraph says a Case superseded in its own session leaves the Spec (case 299.1)
    sections:
      Criterion: |
        Given:
        `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi`; the hook refuses a hand edit.
        **＋** The one rule stood as the first paragraph of `CLAUDE.md` until this Case (59.8, 272.1).
        **＋** `guppi render --check` keeps the file equal to the page.

        When:
        The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

        Then:
        `case-schema.md` opens with the section "The one rule" right under its title: nothing in the vault or the codebase changes without a Decision ratified by the human; the agent has full autonomy over how to implement something once its contract is ratified, and none over the contract itself; when unsure whether something needs ratification, it does; the vault is the only memory — no note outside the repository, what is worth keeping is a `lesson` line or a Case on a Rule page (272.1).
        **＋** The paragraph after it says, as before, that the schema is the Render loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md`, and that a session without `/hi` holds no Case.
        **＋** The Spec paragraph names the field-only `update` of an Estimate: a part named changes alone, a part inside the Criterion sets `pending` (294, 296).
        **＋** The paragraph on the Criterion says that a Case superseded in its own session, before the Spec is approved, leaves the Spec and the superseding Case is written whole; a supersede from a later session leaves the earlier Spec as it is (299.1).
        **＋** `render --check` after the render exits 0.
        **－** The other sections of the schema do not change; the description of the project is not in the schema.
  - slug: index
    file: vault/wiki/index.md
    change: "§7 — after \"reached by `origin`, and in History\": a Case superseded in its own session, before the Spec is approved, leaves the Spec, the superseding Case written whole; its text is not kept — the ledger lines name its targets, the superseding Case's context what it replaced (case 299.1)"
```

```tasks
- [x] update `rule-case-protocol`: one `replace` pair in the Render — the sentence after "nothing removed by a `{supersedes:case N}`"
- [x] update `estimate-case-protocol-loaded`: the Criterion whole under `sections`, one line added, `pending`
- [x] update `index` (`vault/wiki/index.md`, §7): one sentence after "reached by `origin`, and in History", by hand
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-protocol-loaded`: `render --check` after the render; the `/hi` of the next session, by hand
```

### Case 299.2 — pre-spec catches a superseded Case still in the plan

> **given:**
> `{supersedes:case N}` on a decision line marks every entry of Case N `superseded_by` in the yaml of any unit (175, 177); `generate` applies none of them and ticks none of their lines (151, 286); Retro does not count them (282).
> **＋** The Spec of a session is the plan approved at the end of Plan Mode, copied to `raw/<date>/<hi HHMM>/spec.md` (73.1); `## Case N — …` or `### Case N.M — …` is a heading, its section runs to the next such heading.
> **＋** `prespec --check` runs every record line of the session's window through `materialize.parse_line` (75.2) and prints a finding for a decision line whose Case has no heading in the plan (59.1).
> **＋** `tests/test_prespec.py` fixes the behaviour on a temp plan.

> **when:**
> `/pre-spec` — `guppi prespec --check` on the plan of this Plan Mode.

> **then:**
> A `{supersedes:case N}` in the session's window while `## Case N` or `### Case N` still stands in the plan is a finding `case N: superseded by case M, still in the plan`.
> **＋** A decision line of Case N, N superseded by a line of the window, is no finding "no Case N heading" and needs no item in the plan.
> **＋** A superseded sub-case: the one heading `### Case N.M` leaves; the parent with its other sub-cases stays.
> **－** A `{supersedes:case N}` on a Case of an earlier session — a defer taken up — finds no heading N in the plan and is no finding.
> **－** A Frontier line closed `· case N` with N superseded is a finding as today; the agent closes it with the superseding Case.
> **－** Nothing else in pre-spec changes.

```then
create:
  - slug: estimate-prespec-catches-a-superseded-case
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: A supersedes of the session's window whose Case still stands in the plan is a finding of prespec --check; a line of the superseded Case needs no item
    method: pytest tests/test_prespec.py on a temp plan; the live reading the first /pre-spec of a later session whose window holds a supersedes of a Case of that session — this session's /pre-spec runs on the old check
    tags: [harness, workflow]
update:
  - slug: rule-prespec
    replace:
      - old: "and for every `tasks` line that opens with the bare word `render` or `sprint`"
        new: "for every `{supersedes:case N}` line of the session's window whose `## Case N` or `### Case N` heading still stands in the plan — the superseded Case leaves the Spec, the superseding one is written whole, and a decision line of Case N then needs no item (case 299.2), and for every `tasks` line that opens with the bare word `render` or `sprint`"
    change: a supersedes of the window whose Case still stands in the plan is a finding; a line of the superseded Case needs no item (case 299.2)
```

```tasks
- [x] update `rule-prespec`: one `replace` pair in the Render — the new finding in the list
- [x] create `estimate-prespec-catches-a-superseded-case` (ref `rule-prespec`)
- [x] `guppi/prespec.py`: `check_lines` — the set of superseded Cases from the window's records, the finding on a heading, their lines freed
- [x] `tests/test_prespec.py`: the heading of a superseded Case in the plan — a finding; a line of a superseded Case with no heading — no finding; a sub-case; a supersedes of a Case of an earlier session — nothing
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-catches-a-superseded-case`: pytest now; live — the first `/pre-spec` of a later session whose window holds a `{supersedes:case N}` of a Case of that session; this session's `/pre-spec` ran on the old check (`lesson-pretask-runs-before-the-check-it-adds`)
```

### Case 299.3 — `materialize`: the entry of a superseded Case is complete by the mark alone

> **given:**
> `{supersedes:case N}` on a decision line marks every entry of Case N `superseded_by` in the yaml of any unit (175, 177); `generate` applies none of them and ticks none of their lines (151, 286); Retro does not count them (282).
> **＋** The Spec of a session is the plan approved at the end of Plan Mode, copied to `raw/<date>/<hi HHMM>/spec.md` (73.1); `## Case N — …` or `### Case N.M — …` is a heading, its section runs to the next such heading.
> **＋** `materialize` takes the `then` and the texts of a Case from the Spec of the unit; what is missing it names in `incomplete`, never invents.
> **＋** `tests/test_materialize.py` fixes the behaviour on a temp ledger.

> **when:**
> `guppi materialize` reads a line with `{supersedes:case N}`, and the entries of Case N lie in this yaml or in the yaml of another session under `raw/`.

> **then:**
> Every entry with `case: N` gets `superseded_by` — the lines of Case N and everything derived from them; the `decisions` record of Case N as today.
> **＋** `generate` applies none of them.
> **＋** A foreign yaml is marked by the same rule.
> **＋** An entry of Case N marked `superseded_by` while no heading N stands in the Spec of the unit carries no `incomplete: [then]`; its `decisions` record carries no `case_text` and no `incomplete` for `context`, `problem`, `given`, `when`; the mark alone is its completeness.
> **－** Case N standing in the Spec — the entries are lifted as today; `--show` prints the same.
> **－** An entry without `case` — `estimate`, `lesson` — gets no mark.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "What is missing is named, not\ninvented."
        new: "What is missing is named, not\ninvented — but for a Case superseded in its own session and gone from the Spec: its entries, marked `superseded_by`, carry no `incomplete: [then]`, and its `decisions` record no `case_text` and no missing section; the mark alone is its completeness (case 299.3)."
    change: an entry of a Case superseded in its own session and gone from the Spec is complete by the mark alone (case 299.3)
  - slug: estimate-materialize-marks-superseded
    set: {status: pending}
    change: the Criterion replaced whole — the entries of a superseded Case gone from the Spec carry no incomplete, the record no case_text; Given added, the shape of case 193 (case 299.3)
```

```tasks
- [x] update `rule-materialize`: one `replace` pair in the Purpose — after "What is missing is named, not invented."
- [x] update `estimate-materialize-marks-superseded`: the Criterion from this sub-case, `pending`
- [x] `guppi/materialize.py`: `mark_superseded` drops `then` from the `incomplete` of an entry whose Case is not in the Spec; `decision_record` without `case_text` and without missing sections for such a Case; the docstring
- [x] `tests/test_materialize.py`: a superseded Case with no heading — entries without `incomplete`, the record without `case_text`; with a heading — as before
- [x] read `estimate-materialize-marks-superseded`: pytest now; live — the librarian's run of the first session where a Case is superseded in it and removed from the Spec
```

### Case 299.4 — `generate`: the Decision page of a superseded Case, and the repair of 298

> **given:**
> `{supersedes:case N}` on a decision line marks every entry of Case N `superseded_by` in the yaml of any unit (175, 177); `generate` applies none of them and ticks none of their lines (151, 286); Retro does not count them (282).
> **＋** The Spec of a session is the plan approved at the end of Plan Mode, copied to `raw/<date>/<hi HHMM>/spec.md` (73.1); `## Case N — …` or `### Case N.M — …` is a heading, its section runs to the next such heading.
> **＋** `generate` writes the Decision page before the entries of its Case, the body `## Context` and `## Problem` from `case_text` (201.2); an entry with `superseded_by` is not applied, the page of its Case is written (151).
> **＋** `tests/test_generate.py` fixes the behaviour.

> **when:**
> `guppi generate` reaches the first entry of a Case whose `decisions` record carries `superseded_by` and no `case_text`.

> **then:**
> The page `decision-case-N` is written with a body of two lines: `## Context` — "Superseded by `[[decision-case-M]]` in its own session, before the Spec was approved; the Case left the Spec (case 299)", `## Problem` — "Decided under `[[decision-case-M]]`"; the lists per kind, `origin`, `tags` as on any page.
> **＋** The status by the mechanism, as today: born `current`, set `superseded` when the page of M is written, `archived` by the cascade; `origin` and `deferred_by` resolve as before.
> **－** A record with `case_text` — the body from it, as today; a supersede from a later session does not change.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: "The Decision page of a Case is written before its entries and carries the body of\nevery defer (cases 52.4, 186.1);"
        new: "The Decision page of a Case is written before its entries and carries the body of\nevery defer (cases 52.4, 186.1); the page of a Case superseded in its own session and gone from the Spec — its record carries `superseded_by` and no `case_text` — has a two-line body naming the superseding Decision, and its status follows the mechanism as for any superseded page (case 299.4);"
    change: the Decision page of a Case superseded in its own session has a two-line body naming the superseding Decision (case 299.4)
  - slug: estimate-generate-writes-the-decision-page
    set: {status: pending}
    change: one line of the Criterion — the page of a superseded Case without case_text has a two-line body (case 299.4)
    sections:
      Criterion: |
        Given:
        `guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
        **＋** An `update` entry for an Estimate that replaces the promise carries `sections.Criterion` and `set: {status: pending}`; one that names a part alone carries neither, and a part inside the Criterion sets `pending` (296); a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
        **＋** An `estimate` entry carries `status` and `result`; the `result` opens with the date of the reading and the command (199).
        **＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
        **－** `materialize`, `cleanup` and `lint` do not change here.

        When:
        `guppi generate` reaches the first entry of a Case, or a `decisions` record with no page yet.

        Then:
        One page `decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`, `tags` — the union of the targets' tags; the body `## Context` and `## Problem` from `case_text`; `## Deferred` — one `### [[slug]]` per target of the `defer` lines, with its `purpose` verbatim.
        **＋** The page is written before the first entry of its lines, so their History lines name it.
        **＋** A `supersedes` sets the earlier page `superseded`, appends to its `superseded_by`, removes its slug from the `deferred_by` of every target of its `defer` list; an empty `deferred_by` is dropped.
        **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
        **＋** A record with `superseded_by` and no `case_text` — a Case superseded in its own session and gone from the Spec — gets a two-line body: `## Context` "Superseded by `[[decision-case-M]]` in its own session, before the Spec was approved; the Case left the Spec (case 299)", `## Problem` "Decided under `[[decision-case-M]]`"; its status follows the mechanism as for any superseded page (299.4).
        **－** No `## Given`, no `## When`, no `## Criterion` list: the contract lives on the Estimate; pages written before keep theirs.
```

```tasks
- [x] update `rule-page-generation`: one `replace` pair in the Purpose — after "carries the body of every defer (cases 52.4, 186.1)"
- [x] update `estimate-generate-writes-the-decision-page`: the Criterion whole under `sections`, one line added, `pending`
- [x] `guppi/generate.py`: `decision` — the two-line body for a record with `superseded_by` and no `case_text`; the docstring
- [x] `tests/test_generate.py`: the page of a superseded Case without `case_text` — the two-line body, then `superseded` and `archived`
- [x] by hand, a one-off migration: `## Deferred` of `vault/wiki/decisions/decision-case-298.md` — three `### [[slug]]` with the `purpose` from Spec 1315, lines 379–387
- [x] read `estimate-generate-writes-the-decision-page`: pytest now; live — the librarian's run of this session
```

### Case 299.5 — `estimate-prespec-checks-the-plan` names the exemption

> **given:**
> `{supersedes:case N}` on a decision line marks every entry of Case N `superseded_by` in the yaml of any unit (175, 177); `generate` applies none of them and ticks none of their lines (151, 286); Retro does not count them (282).
> **＋** `prespec --check` prints a finding for a decision line whose Case has no heading in the plan (59.1); by 299.2 a line of a Case superseded by a line of the window needs no item, and the heading of such a Case still in the plan is a finding.
> **＋** A `replace` pair whose `old` stands inside the Criterion changes that line and sets `pending` (296).

> **when:**
> `guppi prespec --check <plan>` runs in a session with a `hi`.

> **then:**
> The `Lines` line of the Criterion of `estimate-prespec-checks-the-plan` says: a decision line of the window with no item of its kind under its own Case heading is a finding, unless a `{supersedes:case N}` of the window names its Case; that Case's heading still in the plan is a finding of its own.
> **－** The other lines of the Criterion do not change; the `given` line on the form of an Estimate item (194.1) is not touched here.

```then
update:
  - slug: estimate-prespec-checks-the-plan
    replace:
      - old: "Lines: a decision line of the window with no item of its kind under its own Case heading; an item with no line;"
        new: "Lines: a decision line of the window with no item of its kind under its own Case heading — unless a `{supersedes:case N}` of the window names its Case, whose heading still in the plan is a finding of its own (299.2); an item with no line;"
    change: one line of the Criterion — the lines of a Case superseded by a line of the window need no item, its heading in the plan is a finding (case 299.5)
```

```tasks
- [x] update `estimate-prespec-checks-the-plan`: one `replace` pair in the `Lines` line (inside the Criterion — `pending`)
- [x] read `estimate-prespec-checks-the-plan`: pytest now; live — with the reading of `estimate-prespec-catches-a-superseded-case`
```

## Case 301 — Slice 3f: the Rule-class files into the graph

> **context:**
> The vault is a tree of pages: one `parent` per page, `children` on a MOC, the other edges wikilinks — `estimates`, `deferred_by`, History. Fourteen files stand outside that tree — `index.md`, `glossary.md`, six `schema.md` and six `schema.yaml`: "Rule-class" by §1 of `index.md`, changed only by a ratified `update` with `file`, by hand in Work Mode. No `purpose`, no History, no Estimates; `ask-guppi` finds them by grep, not by the index lines; pre-spec corrects them with a guard of their own (`check_governed`, `file` against `slug`). The scripts keep a route of their own for them: `RULE_CLASS` and `category: file` in `materialize.py`, "a Rule-class file, applied by hand" in `generate.py`, `rule_class_path` in `prespec.py`, `prose_names` in `lint.py` — the check that the md tables and the yaml agree, a guard on two records of one condition not drifting apart. What the files are: `schema.yaml` is the input of lint, a condition with a guard, a Rule without a page; `schema.md` its prose; `glossary.md` a fast map of the terms, 28 rows pointing at a page and 23 at a `§N` of `index.md` — the count of what has not migrated; `index.md` (438 lines, 13 §) the document the rules migrated from, so every change of a rule is made twice, on the page and in its §; its own §11 says the index of a category is computed by its reader, written by nobody (147.8) — the map file stands outside that rule. The mechanisms of the replacement exist: `render_mode: full` writes any text into `governs`, yaml included (273, `render.py`); `guppi sprint` writes `sprint.md` from the fields of a page under a Rule with `governs`, `implementation_ref` and `--check` (209, 229). The product — a developer's vault on their own codebase — must have no "by hand" route: without it there is no History and no guard; the `file` route is a crutch of the migration. Rejected in the discussion: two rules per category (yaml and md) — one condition signed twice (72.1, 188); a render of `schema.md` — a Leaf has no section for prose, the mechanism lives in the Render or the docstring; a rule per glossary term — a term is no condition with a guard, ~50 pages with a required `estimates`; `replace` pairs written into the file by the script (Case 300 of this session, not ratified) — leaves the files outside the graph; a notes folder under `raw/` — ratification by pointer, a second memory nobody signed; a template engine for the renders — two shapes are not yet a pattern, Backlog. The edge Rule → Entity does not exist in the model: `rule-sprint` names `entity-sprint` in a code span, not a wikilink; it is the Backlog item "`applies_to` on a Rule, `rules` on an Entity" (session 1119) — taken into the Slice. The pages: `entity-sprint-migration` `draft`, an `update` with a `ref`; its three Estimates (lint clean, leftovers gone, merges) the Case does not touch — it creates a fourth; the `purpose` of the entity ("the model in `wiki/index.md`") changes in theme 4, not here. The slug of the new Estimate is free.

> **problem:**
> How these files become vertices of the graph with edges, a `purpose` and Estimates, and whether the "by hand" route leaves the scripts — a programme the size of a Slice, to be fixed as the current milestone of the sprint with a Definition of done, and done from the next session on.

> **given:**
> A Rule-class file — `index.md`, `glossary.md`, `<category>/schema.md` and `schema.yaml` — changes only by a ratified `update` with `file`, by hand (§1 of `index.md`); its route in the scripts is `RULE_CLASS` and `category: file` in `materialize.py`, "applied by hand" in `generate.py`, `rule_class_path` and `check_governed` in `prespec.py`, `prose_names` in `lint.py`.
> **＋** The Render of a rule with `render_mode: full` becomes the file of `governs` whole; `render --check` and the governed-files hook keep them equal (273).
> **＋** `guppi sprint` writes `sprint.md` from the sprint page under `rule-sprint`, which carries `governs`, `implementation_ref` and `--check` under `make lint` (209, 227, 229).
> **＋** A page has one `parent`; the tree of rules is built by mechanism; the schema has no edge Rule → Entity.
> **＋** Lint reads `<category>/schema.yaml`; `materialize.schema_fields` and `generate` read it too.

> **when:**
> The reading at the close of Slice 3f: `ls` of the schemas and `index.md`, a grep of the `file` route over `guppi/`, `uv run guppi render --check`, `uv run guppi glossary --check`, `make lint`.

> **then:**
> No Rule-class file: every `<category>/schema.yaml` is the Render of the Leaf `rule-<category>-schema` (`enforcement: render`, `governs` that yaml), with the description of its fields as yaml data; no `schema.md`; `glossary.md` is written by `guppi glossary` from the `terms` field of the defining pages, a table "term — meaning — `[[page]]`" grouped by the parent MOC, under `rule-glossary` with `governs`, `implementation_ref` and `--check`; no `index.md`, every `§N` pointer in the vault replaced by a slug.
> **＋** The scripts hold no `file` route: no `RULE_CLASS`, no `category: file`, no "applied by hand", no `rule_class_path`, no `prose_names`; the vault changes only by the scripts, from decisions.
> **＋** Every rule has its parent by the criterion of the audit: under a category's MOC a rule that holds for that category alone, the MOC made at two or more such rules, else the schemas under `rule-page-schemas`; `applies_to` on a Rule and `rules` on an Entity carry the edge Rule → Entity, `rule-sprint` → `entity-sprint` the first.
> **＋** "Rule-class" is a retired term in the Case schema and in the glossary.
> **－** `case-schema.md` and `CLAUDE.md` are not brought into the graph by the Slice: they are Renders already and change by an `update` of `rule-case-protocol` or `rule-claude-md`, as theme 6 does.
> **－** No template engine for the renders is built: Backlog.

```then
create:
  - slug: estimate-sprint-migration-rule-class-files-dissolved
    type: estimate
    ref: entity-sprint-migration
    kind: QA
    purpose: No Rule-class file at the close of Slice 3f — the schemas rendered from rule pages, the glossary from terms, index.md gone, the file route out of the scripts
    method: "one reading at the close of Slice 3f: ls vault/wiki/*/schema.md empty and vault/wiki/index.md absent; grep -rn -e RULE_CLASS -e 'applied by hand' -e rule_class_path -e prose_names guppi/ empty; uv run guppi render --check, uv run guppi glossary --check and make lint exit 0"
    tags: [sprint, workflow, harness]
update:
  - slug: entity-sprint-migration
    change: Slice 3f — the Rule-class files into the graph — the current milestone, with its Estimate and six themes; applies_to moved from the Backlog into the Slice, the template engine added to it (case 301)
    sections:
      Milestones: |
        ### Slice 3f — the Rule-class files into the graph

        The vault is a graph of pages; fourteen files stand outside it — `index.md`, `glossary.md`, six `schema.md` and six `schema.yaml` — changed by hand, without `purpose`, History or Estimates, and kept by a route of their own in the scripts. The Slice brings each into the graph by its nature and removes the "by hand" route: a developer's vault changes only by the scripts, from decisions (case 301).

        - [[estimate-sprint-migration-rule-class-files-dissolved]] — no Rule-class file: the schemas rendered from rule pages, the glossary from `terms`, `index.md` gone, the `file` route out of the scripts
        - 1. schemas — six Leaves `rule-<category>-schema`, `enforcement: render`, the Render the `schema.yaml` with the description of its fields as yaml data; `schema.md` gone; one rule per category, never two
        - 2. audit of the rules — the parent of every rule: under a category's MOC a rule that holds for that category alone, the MOC made at two or more such rules, else the schemas under `rule-page-schemas`; `applies_to` on a Rule and `rules` on an Entity, the edge Rule → Entity, `rule-sprint` → `entity-sprint` the first (from the Backlog, session 1119)
        - 3. glossary — `terms` on the page that defines a term; `guppi glossary` writes `glossary.md`, grouped by the parent MOC, under `rule-glossary` with `governs`, `implementation_ref` and `--check`, the pattern of `rule-sprint`; the rows on `§N` resolved as the index dissolves, "Retired terms" into the history of decisions
        - 4. `index.md` — one Case per §: covered by a rule page, the § leaves; not covered, a rule is made; the last Case removes the file and every `§N` pointer in the vault
        - 5. scripts — the audit "script — what it assumes — what changes"; the `file` route and "applied by hand" removed from `materialize`, `generate`, `prespec`, `lint`; the grep of `index.md` out of `rule-ask`; `rule-morph` (Slice 5) kept compatible with six schema rules
        - 6. close — "Rule-class" retired in the Case schema and the glossary; the Estimate read; the Slice moved to Closed

        ### Slice 3b — Work Mode

        - [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; the sentence of [[insight-workflow-code-live-before-the-page-it-reads]] on a check that reads a page the same Spec changes; cases 183, 206, 238
        - [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206

        ### Slice 4 — conversion of the parked pages by group

        - [[estimate-sprint-migration-leftovers-gone]] — every page of `vault/parked/` and every document of 2026-08 under `docs/` converted, archived or deleted by a decision

        ### Slice 5 — closing

        - [[estimate-sprint-migration-lint-clean]] — `make lint` exit 0: the 31 Decision pages of Cases 1–28 decided, `unmigrated` at zero
        - [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`; at the close [[rule-git-context]] and [[rule-github-issues]] — the upstream of the branch and the GitHub remote, decisions 11.1, 11.2, defers 220, 243 — read by [[estimate-sprint-migration-leftovers-gone]]
        - [[rule-spec-box]] — the Spec box, case 207, after Slice 3b
        - [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239
      Backlog: |
        - the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)
        - a template engine for the rendered files — one script with the shape of each file declared, once a third render beside `sprint.md` and `glossary.md` appears (case 301)
```

```tasks
- [x] update `entity-sprint-migration`: `sections` — `Milestones` whole (Slice 3f first: the vision, the Estimate, six themes; 3b, 4, 5 unchanged), `Backlog` whole (`applies_to` moved into theme 2; the template engine added)
- [x] create `estimate-sprint-migration-rule-class-files-dissolved` (ref `entity-sprint-migration`)
- [x] `uv run guppi sprint`
- [ ] read `estimate-sprint-migration-rule-class-files-dissolved`: at the close of Slice 3f, by its `method`
```

## Case 302 — the Insight closed by 296; the synthesis births an Insight from a marked lesson `actioned`

> **context:**
> The lesson L3 of session 1315 was written, and in the same session 296 closed its cause: the line of 296 carries `{addresses:…}`, `materialize` puts `addressed_by: decision-case-296` on the lesson's entry (284.3). The librarian, at synthesis, finds a second lesson with the same cause (0958) and by the rule creates an Insight `open`, severity 2. The synthesis rule knows the mark in one case only — the lesson falls under an Insight that already exists and is `actioned`: it stays `actioned`, `addressed_by` moves to the decision (284.4, `estimate-synthesis-keeps-actioned-by-the-mark`, `pending`, no date). The case "an Insight is born from a marked lesson" is not in the rule — so it is born `open`, goes to the brief's Deferred, to the Frontier and into a Case, although the decision that closed the pattern is named on the lesson's entry. No change of mechanism is needed: `generate` sets every new Insight `open` (`INITIAL_STATUS`), and the librarian already appends the `update` of each lesson — one more `update` of the new Insight in the same yaml, `set: {status: actioned, addressed_by}`, applies right after the `create`; the cascade archives the `clustered` children. The Proposal of the Insight — a check in pre-spec and a flag of the librarian — is read no further: the pattern is closed by 296, the Case schema (294), `estimates/schema.md` and §7 (297) name the form, the readings W1–W4 of this session confirmed it. The pages: the Insight `open`, both lessons `clustered`; `rule-synthesis` `draft` (its Render a partial of `.claude/agents/librarian-guppi.md`); of its two Estimates the Case touches `estimate-synthesis-keeps-actioned-by-the-mark`, not `estimate-synthesis-clusters`; `insights/schema.md` a Rule-class file, by hand, the `status` row; §8 of the index and the glossary do not contradict and are not touched.

> **problem:**
> Close the Insight as solved by 296, and close the gap by which every cause cured in its own session costs a Case of the next one.

### Case 302.1 — the Insight `actioned` by 296

> **given:**
> The `addressed_by` of an Insight is the decision that fixed or rejected the pattern; `actioned` archives the `clustered` children by the cascade; a new lesson with the same cause reopens it unless its entry carries `addressed_by` (104.2, 124, 284.4).

> **when:**
> The librarian applies the `update` of the Insight.

> **then:**
> `insight-materialize-estimate-update-lifts-the-criterion-whole` is `actioned`, `addressed_by: decision-case-296`; both lessons go to the archive by the cascade; a third lesson with the same cause reopens the Insight.
> **－** `rule-prespec` and `rule-materialize` do not change.

```then
update:
  - slug: insight-materialize-estimate-update-lifts-the-criterion-whole
    set: {status: actioned, addressed_by: decision-case-296}
    change: actioned — the pattern was closed by case 296 in the session of the second lesson; the Proposal's further check is not taken (case 302.1)
```

```tasks
- [x] update `insight-materialize-estimate-update-lifts-the-criterion-whole`: `set: {status: actioned, addressed_by: decision-case-296}`
```

### Case 302.2 — synthesis: an Insight born from a marked lesson is `actioned`

> **given:**
> `rule-synthesis`: two live lessons with one cause and no Insight — a `create` of the Insight (`pattern`, `children`, `tags`, `Pattern`, `Proposal`) and an `update` of each lesson to `clustered`; on an existing `actioned` Insight — `set: {addressed_by: decision-case-N}` with the status kept `actioned` when the lesson's entry carries `addressed_by` (284.4); the entries are marked `librarian: synthesis`.
> **＋** `generate` sets a new Insight `open`; the entries of a yaml apply in order; the cascade after all entries archives the `clustered` children of an `actioned` Insight.
> **＋** The lesson's entry carries `addressed_by: decision-case-N` when a decision line of the unit marked it (284.3).

> **when:**
> The librarian, at synthesis, creates an Insight, and the entry of the lesson that triggered it carries `addressed_by`.

> **then:**
> Right after the `create` of the Insight the librarian appends an `update` of the same slug with `set: {status: actioned, addressed_by: decision-case-N}` — the bare slug, `generate` writes the wikilink; the Insight stands `actioned`, both lessons `clustered` go to the archive by the cascade; the brief names the pair beside the synthesis.
> **＋** Without `addressed_by` on the lesson's entry — the Insight is `open`, as today.
> **＋** An existing `actioned` Insight — as in 284.4, unchanged.
> **－** The librarian never sets `actioned` on his own: only by the mark a decision put.

```then
update:
  - slug: rule-synthesis
    replace:
      - old: "- A live lesson has the same cause and no Insight exists: append to the yaml a `create` in `insights` with `slug` (`insight-<area>-<pattern>`), `pattern`, `children` (both lessons), `tags` (the union), and `sections` `Pattern` and `Proposal`; and an `update` for each lesson with `set: {status: clustered, insight: <slug>}`."
        new: "- A live lesson has the same cause and no Insight exists: append to the yaml a `create` in `insights` with `slug` (`insight-<area>-<pattern>`), `pattern`, `children` (both lessons), `tags` (the union), and `sections` `Pattern` and `Proposal`; and an `update` for each lesson with `set: {status: clustered, insight: <slug>}`. When the lesson entry carries `addressed_by: decision-case-N` — the Case of this unit that closed its cause — append right after the `create` an `update` of the new Insight with `set: {status: actioned, addressed_by: decision-case-N}`: the Insight is born closed, its lessons go to the archive by the cascade, and the pair is reported in the brief beside the synthesis (case 302.2)."
    change: an Insight born from a lesson whose entry carries addressed_by is set actioned by an update right after its create (case 302.2)
  - slug: estimate-synthesis-keeps-actioned-by-the-mark
    set:
      status: pending
      purpose: An Insight stays or is born actioned by the mark — an existing actioned Insight keeps its status and takes the new addressed_by; a new Insight from a marked lesson is set actioned right after its create
    change: the Criterion replaced whole — the second case of the mark, an Insight born from a marked lesson (case 302.2)
    sections:
      Criterion: |
        Given:
        `rule-synthesis`: on an Insight of the same pattern the librarian appends an `update` with `children` plus the lesson and `set: {status: open}` when it was `actioned`; on two lessons with one cause and no Insight a `create` of the Insight and an `update` of each lesson; the entries it adds carry `librarian: synthesis`.
        **＋** `insights/schema.md`: `addressed_by` is one decision; `generate` sets a new Insight `open`; the cascade of `generate` archives the children of an `actioned` Insight.
        **＋** The lesson entry carries `addressed_by: decision-case-N` when a decision line of the unit marked it (284.3).
        **－** An `open` Insight stays as today; the librarian sets `actioned` by the mark alone, never on his own.

        When:
        The librarian, at synthesis, finds an Insight of the same pattern that is `actioned`, or creates an Insight, and the lesson entry carries `addressed_by`.

        Then:
        On an existing `actioned` Insight the `update` carries `children` plus the lesson and `set: {addressed_by: decision-case-N}` — the bare slug, `generate` writes the wikilink — with `status` kept `actioned`; the lesson is `clustered` with `insight` set, the cascade archives it; the brief reports the pair beside the synthesis, as it reports a clustering.
        **＋** On a new Insight an `update` of its slug follows the `create` with `set: {status: actioned, addressed_by: decision-case-N}`; the Insight stands `actioned`, both lessons `clustered` go to the archive by the cascade; the brief reports the pair (302.2).
        **＋** Without `addressed_by` — `set: {status: open}` on an existing Insight, a new one `open`, as today.
        **＋** The schema of Insights, §8 of the map and the glossary name the exception: a new Lesson reopens `actioned` unless its entry carries `addressed_by`; the schema names the birth by the mark too.
  - slug: insights-schema
    file: vault/wiki/insights/schema.md
    change: the status row — an Insight made from a lesson whose entry carries addressed_by is set actioned right after its create, by the librarian's update (case 302.2)
```

```tasks
- [x] update `rule-synthesis`: one `replace` pair in the Render — the item "no Insight exists"
- [x] update `estimate-synthesis-keeps-actioned-by-the-mark`: the Criterion whole under `sections`, both cases; `purpose`; `pending`
- [x] update `insights-schema` (`vault/wiki/insights/schema.md`, the `status` row): the birth `actioned` by the mark, by hand
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-synthesis-keeps-actioned-by-the-mark`: the librarian's run on the first marked lesson — under an `actioned` Insight, or the second of a new pattern; no date
```

## Deferred

## Case 303 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b — `rule-work-mode` (Work Mode: the Spec as tasks with code, the ticked boxes, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads`) and `rule-subagent-guppi` (what a subagent may do, the fork that comes back as a Case) — two `draft` placeholders, deferred sixteen times, the last by 293. This session put Slice 3f (the Rule-class files into the graph, case 301) ahead of it as the current milestone, took the readings due at `/hi` (W1–W4), the same-session supersede (299), and closed the Insight of 1315 with the birth of an Insight by the mark (302).

> **problem:**
> The person closes this Plan Mode and goes to pre-spec; Slice 3b waits behind Slice 3f, the seventeenth defer. The lines of 293 still bear on it: a subagent loads `CLAUDE.md` and not the glossary (288.1), and `guppi recall` brings the session's load back after a compaction (287) — the rule of Work Mode is written with both.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes on code, tests, migrations and by-hand checks in spec.md (the readings are generate's since case 270, the render and sprint lines in the form of case 279.1), the test of each Estimate written first and turned green, the sentence of insight-workflow-code-live-before-the-page-it-reads on a check that reads a page the same Spec changes; after Slice 3f
  - slug: rule-subagent-guppi
    type: rule
    purpose: what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; a subagent loads CLAUDE.md and no glossary (case 288.1); with rule-work-mode, after Slice 3f
```
