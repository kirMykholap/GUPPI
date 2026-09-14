---
type: insight
pattern: materialize lifts a ledger line or a `then` item into an entry and loses a field the page schema needs; the page is written without it and lint names the page, never the parser.
status: open
children: ["[[lesson-materialize-standalone-estimate-keeps-criterion-as-a-field]]", "[[lesson-materialize-lesson-line-source-dropped]]"]
severity: 2
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

## Children

- [[lesson-materialize-standalone-estimate-keeps-criterion-as-a-field]]
- [[lesson-materialize-lesson-line-source-dropped]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L160
