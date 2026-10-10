---
type: insight
pattern: materialize lifts a ledger line or a `then` item into an entry and loses a field the page schema needs; the page is written without it and lint names the page, never the parser.
status: archived
children: ["[[lesson-materialize-standalone-estimate-keeps-criterion-as-a-field]]", "[[lesson-materialize-lesson-line-source-dropped]]", "[[lesson-materialize-item-ref-lifted-as-a-page-field]]"]
severity: 0
addressed_by: "[[decision-case-214.1]]"
origin: raw/2026-09-12/ledger.md#L160
sprint: migration
created: 2026-09-12
tags: [harness, ledger]
---

## Pattern

Two lessons where the lift from a ledger line, or from a `then` item, to a page dropped what
the schema asks for.

`lesson-materialize-standalone-estimate-keeps-criterion-as-a-field` (session G): a standalone
Estimate create has every key lifted into `fields`, while only the `estimate` nested under a
Leaf create maps `criterion` and `method` into sections; six pages carry the two keys as
frontmatter and have no Criterion or Method section.

`lesson-materialize-lesson-line-source-dropped` (session J): `materialize.parse_line` reads
the braces of a lesson line into options and returns `tags` only, never `source`; every
knowledge lesson is then marked `incomplete: [source]` and its page is written without the
one field its line carried.

In both, the parser decides what a page gets, the page is written without it, and the miss
is named by lint on the page - one step and one session away from the line that held it.

## Proposal

A suggestion, not a decision. Name, in one place, the fields each category's page needs and
where each comes from - a brace of the ledger line, a key of the `then` item - and have
`materialize` lift by that table rather than by a per-kind branch. A field the table names
and the source does not hold is what `incomplete` is for; a field the source holds and the
table does not know is a fault of the parser, not of the page.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L160
- 2026-09-14 updated: actioned: the children fixed by 53.3 and 87; the protocol names {source:...} on a knowledge line (144.1); the three lessons of O sourced (144.2); no table in code (case 144.3) · [[decision-case-144.3]]
- 2026-09-16 updated: reopened by librarian: a third lesson of the same pattern — _lift_item copies every key of a then item into fields except a fixed list, and case 194.1 added ref to the Estimate item without extending the list, so the page carries a field the schema does not know; the parser decides what a page gets by a fixed list, not by the schema (lesson-materialize-item-ref-lifted-as-a-page-field)
- 2026-09-17 updated: the lift by the schema — a key the schema does not name never reaches a page (case 214) · [[decision-case-214.2]]
- 2026-10-10 status: actioned → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
