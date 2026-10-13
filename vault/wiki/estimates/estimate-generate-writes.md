---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: What generate writes to a page for each kind of entry of a materialize.yaml, and nothing an entry does not carry
method: pytest in tests/test_generate.py against a temp vault; the live reading once by hand
checked: 2026-10-13
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Criterion

When:
`guppi generate` applies one entry of a yaml to a page.

Then:
A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the `sprint` of the yaml, which `guppi materialize` takes from the first `## <id>` of `sprint.md` or, in a unit whose ledger creates `entity-sprint-<id>`, from that `<id>`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
**＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`, and `deferred_by` after `checked` once a `defer` marks it; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
**＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
**＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
**＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
**＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
**＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
**＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight, estimate) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by` for a rule or an entity only.
**＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
**＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
**＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
**＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
**－** A `defer` of an Estimate, an Insight, a Lesson or a Decision page whose page stands neither under `vault/wiki/<category>/` nor in a folder `<category>` under `vault/archive/` outside a `raw/` folder, by `defer_writes_no_page` of `guppi/materialize.py`, which asks `has_page`, writes no page: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: an Estimate is deferred only with its page — defer the page it would check` on stderr for an Estimate, and `generate: <slug>: a placeholder is written only for a rule or an entity — defer a page that stands` for the other kinds.
**－** No body section is derived from a ref field; a section the entry does not name under `sections` or reach by `replace` is not touched.
**－** An `update` of an Estimate whose `set` carries `method` drops no section.
**－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

## Result

2026-10-13, uv run pytest tests/test_generate.py: 127 passed — a defer of an Insight, a Lesson and a Decision page with no page writes no page and fails alone; an Insight archived in an insights folder is marked there

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
- 2026-09-17 updated: one line in the Criterion — an update of an Estimate with set.method writes the field and drops · [[decision-case-211.1]]
- 2026-09-17 updated: method as a field, the old sections dropped — the recut completed (case 211.3) · [[decision-case-211.3]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L49
- 2026-09-20 ref `estimate-pretask-hook-gates` → `estimate-prespec-hook-gates` · [[decision-case-261]]
- 2026-09-20 updated: the word moved: the module pretask → prespec and the slug -pretask-reconciles → -prespec-reconciles in the Criterion; the promise and the reading unchanged, passed kept (case 265) · [[decision-case-265]]
- 2026-09-29 updated: the Criterion restored whole — the text of case 211.1, which case 211.3 overwrote, less its pointer line; purpose set (case 489.1) · [[decision-case-489.1]]
- 2026-09-29 updated: the Criterion replaced whole — set.method drops no section (case 506.6) · [[decision-case-506.6]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L25
- 2026-10-04 updated: the Criterion replaced whole — a page's sprint is the sprint of the yaml, the new sprint's id in the unit that creates its page (case 628.6) · [[decision-case-628.6]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/2041/ledger.md#L6
- 2026-10-12 updated: the Criterion replaced whole — a defer marks an Estimate deferred_by, written after checked · [[decision-case-781.6]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1604/ledger.md#L26
- 2026-10-12 updated: the Criterion replaced whole — a defer of an Estimate with no page writes no placeholder and fails alone · [[decision-case-783.1]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/2252/ledger.md#L13
- 2026-10-13 updated: the Criterion replaced whole — a defer with no page of anything but a rule or an entity writes no placeholder and fails alone · [[decision-case-786.1]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L45
