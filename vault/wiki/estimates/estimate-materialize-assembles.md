---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
checked: 2026-09-16
origin: raw/2026-09-10/ledger.md#case-31
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

The yaml is the librarian's whole view of the session. An entry routed wrong, or a line dropped, is a decision that never becomes a page.

## Criterion

Given:
A unit `raw/<date>/<HHMM>/` holds `ledger.md` and `spec.md`; a Case in the Spec has a heading, the sections `given`, `when`, `then` and a `then` block.
**＋** `guppi generate` applies the `sections` of an `update` entry as whole replacements and writes every field of a `create` entry's `fields` into the frontmatter.
**＋** The tests in `tests/test_materialize.py` fix the behaviour; the live reading is the librarian's run.

When:
`guppi materialize` lifts a record line of a ledger against its Spec.

Then:
One entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `origin`, `line`, `text`, `decision`; from the `then` block — `fields`, `sections`, `replace`, `change`, `impact`; what the block lacks is `incomplete`, never invented.
**＋** An Estimate has its own line and its own entry; the `ref` of the line is the Estimate itself.
**＋** An `update` entry for an Estimate carries `sections.Criterion` — the text the item wrote under `sections: Criterion` itself, else the `given`, `when` and `then` of its Case verbatim with their operands as `Given:`, `When:`, `Then:` — replacing what stood there, and `set: {status: pending}` unless the item set a status itself; the `given` of a sub-case is its parent's when it has none of its own.
**＋** A `create` entry for an Estimate keeps `kind`, `purpose`, `method`, `tags` as fields; its Criterion the same way: the written text when there is one, else the Case's; `## Context` and `## Method` are not written.
**＋** One decision entry per Case: `decision`, `case_text`, `targets`; a sub-case inherits `context`, `problem`, `recommend`, `given`, never `when`.
**＋** An `estimate` line for a page of the same ledger is folded into its `create`; for an earlier page it is an `estimate` entry. The `new_tags` of any Case reach the yaml once. An existing yaml is extended, never rewritten.
**－** An `update` entry carries no `contract`, and no Estimate is derived from it; a `create` carries no `method`, `estimate_kind` or `estimate_slug`; neither `criterion_block`, `case_removed` nor `remove_criterion` is derived.
**－** The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule's item are ignored: they reach neither the page nor `incomplete`.
**－** A line the grammar does not parse goes under `unparsed`; the run goes on.

## Method

pytest in tests/test_materialize.py against a temp vault; the live reading once by hand

## Result

2026-09-16, `pytest tests/test_materialize.py`: 52 green — an update with a written sections.Criterion keeps it and goes pending, a written status is kept, a create's ref is the entry's and no page field; live, `materialize --show --date 2026-09-16` over 1955: 26 entries lifted, no incomplete, the Criterion of every update from its Case's given, when and then, the four creates with purpose, method and tags as fields

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-31
- 2026-09-10 updated: criterion: an existing yaml gains only the entries of ledger lines it does not hold (the Criterion of case 31 already carries it) · raw/2026-09-10/ledger.md#case-41
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L70
- 2026-09-11 updated: criterion: the standalone estimate create maps to sections; the incomplete rule for a defer-only Case (case 56) · [[decision-case-53.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-11/ledger.md#L77
- 2026-09-12 updated: the parent's given is inherited by a sub-case; pending for the unit reading (case 60) · [[decision-case-60]]
- 2026-09-12 updated: new_tags of a line-less Case join the criterion (case 61) · [[decision-case-61]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L99
- 2026-09-12 updated: the derived Estimate entries of case 72.3 join the criterion; pending until the unit reading · [[decision-case-72.3]]
- 2026-09-12 criterion: case 73.5 added · [[decision-case-73.5]]
- 2026-09-12 criterion: case 76 added · [[decision-case-76]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L157
- 2026-09-12 criterion: case 87 added · [[decision-case-87]]
- 2026-09-12 criterion: case 90.1 added · [[decision-case-90.1]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L207
- 2026-09-13 criterion: case 105.2 added · [[decision-case-105.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L44
- 2026-09-14 criterion: case 130.2 added · [[decision-case-130.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L36
- 2026-09-14 criterion: case 142.1 added · [[decision-case-142.1]]
- 2026-09-14 updated: the bare #L<n> of the Criterion prose in a code span, no Obsidian tag (case 148.3) · [[decision-case-148.3]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1633/ledger.md#L55
- 2026-09-15 criterion: case 158 added · [[decision-case-158]]
- 2026-09-15 criterion: case 161 added · [[decision-case-161]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L25
- 2026-09-15 criterion: case 175 added · [[decision-case-175]]
- 2026-09-15 criterion: case 130.2 removed · [[decision-case-177]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L2
- 2026-09-16 updated: the Criterion replaced whole by this Case; the nine blocks leave — 73.5 to walks-dates, six to their own pages, 90.1 dies with the derivation (case 189) · [[decision-case-189]]
- 2026-09-16 updated: the Criterion replaced whole by case 194.1 — the head recut, the lines of 189 and the shape of the entry; the nine blocks leave (case 194.1) · [[decision-case-194.1]]
- 2026-09-16 updated: the Criterion replaced whole by case 204 — the text of 194.1 with the written Criterion winning on an update, the given without the state of pages (case 204) · [[decision-case-204]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L35
