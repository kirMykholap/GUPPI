---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
checked: 2026-09-16
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Every page of the vault comes through this script from Slice 3 on. A derived field computed wrong, or a ratified one dropped, is corrupted everywhere at once.

## Criterion

Given:
`guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
**＋** An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
**＋** An `estimate` entry carries `status` and `result`; the `result` opens with the date of the reading and the command (199).
**＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
**－** `materialize`, `cleanup` and `lint` do not change here.

When:
`guppi generate` applies one entry of a yaml to a page.

Then:
A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the first `## <id>` of `sprint.md`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
**＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
**＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
**＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
**＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
**＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
**＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
**＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by`.
**＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
**＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
**＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
**＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
**－** No body section is derived from a ref field; a section a page still carries is not touched.
**－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).
**－** The Decision page, the failure of an entry and the cascade are three other Estimates.

## Method

pytest in tests/test_generate.py against a temp vault; the live reading once by hand

## Result

2026-09-16, `pytest tests/test_generate.py`: 46 green — an Estimate page carries purpose, method and checked after target, its Criterion from sections and no Context or Method; an update with sections.Criterion replaces the section whole and keeps the old sections a page still carries; a reading writes checked from the date the Result opens with, else the yaml's date; criterion_block and remove_criterion fail as shapes the script no longer knows; the live half is the librarian's run of this session

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L71
- 2026-09-11 updated: the criteria of the four Estimates of Cases 47–48 folded in; no skip, no paired estimate, the decision-page shape and deferred_by of Case 52; pending until the End of Work reading · [[decision-case-53.2]]
- 2026-09-11 updated: criterion: a stale failed mark is dropped on apply (case 53.3) · [[decision-case-53.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-11/ledger.md#L76
- 2026-09-12 updated: the decision page's four lists replace the aligned pair in the criterion (case 59.4) · [[decision-case-59.4]]
- 2026-09-12 updated: the derived Estimate page and the decision page's Criterion links join the criterion (case 72.4); pending until the unit reading · [[decision-case-72.4]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L167
- 2026-09-13 criterion: case 101.1 added · [[decision-case-101.1]]
- 2026-09-13 criterion: case 104.1 added · [[decision-case-104.1]]
- 2026-09-13 criterion: case 104.2 added · [[decision-case-104.2]]
- 2026-09-13 criterion: case 104.3 added · [[decision-case-104.3]]
- 2026-09-13 criterion: case 105.3 added · [[decision-case-105.3]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/0747/ledger.md#L1
- 2026-09-14 criterion: case 114 added · [[decision-case-114]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L46
- 2026-09-14 criterion: case 124.2 added · [[decision-case-124.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L33
- 2026-09-14 criterion: case 142.2 added · [[decision-case-142.2]]
- 2026-09-14 criterion: case 148.1 added · [[decision-case-148.1]]
- 2026-09-14 criterion: case 151 added · [[decision-case-151]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1633/ledger.md#L58
- 2026-09-15 criterion: case 124.2 removed · [[decision-case-164]]
- 2026-09-15 criterion: case 166.2 added · [[decision-case-166.2]]
- 2026-09-15 criterion: case 166.3 added · [[decision-case-166.3]]
- 2026-09-15 criterion: case 114 removed · [[decision-case-166.3]]
- 2026-09-15 criterion: case 172 added · [[decision-case-172]]
- 2026-09-15 criterion: case 148.1 removed · [[decision-case-172]]
- 2026-09-15 updated: head Criterion: no ## Children, no ## Estimates — the text of 166.2 (case 174) · [[decision-case-174]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L9
- 2026-09-16 status: passed → passed · raw/2026-09-16/1651/ledger.md#L37
- 2026-09-16 updated: the Criterion replaced whole by case 201.1 — the head recut with 101.1, 105.3, 166.2, 171 and 172; 104.x and 166.3 go to -cascades, 142.2 and 151 to -fails-alone; the ten blocks leave (case 201.1) · [[decision-case-201.1]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L27
