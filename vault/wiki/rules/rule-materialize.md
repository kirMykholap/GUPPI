---
type: rule
kind: Leaf
purpose: Prevents the librarian from reading the ledger and the Spec itself, or from routing a decision by guesswork
status: draft
enforcement: check
implementation_ref: [guppi/materialize.py, tests/test_materialize.py]
parent: rule-documentation
estimates: [estimate-materialize-assembles, estimate-materialize-walks-dates]
origin: raw/2026-09-10/ledger.md#case-31
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Purpose

Prevents the librarian from reading the ledger and the Spec itself, or from routing
a decision by guesswork. The yaml is the one input a clean context needs. Every line
of the ledger is an entry. Its route is computed from `index.md` §5. Its content is
lifted from the `then` block of its Case in the Spec. What is missing is named, not
invented. If a route cannot be derived from the ledger and the Spec alone, that is a
defect of the ledger, and it shows here.

## How it works

`uv run guppi materialize [--date YYYY-MM-DD]` reads `raw/<date>/ledger.md` and
`raw/<date>/spec.md` and writes `raw/<date>/materialize.yaml`. Without `--date` it
walks every `raw/<date>/` that holds a `ledger.md`, in date order, and prints one
line per date; a line written after the librarian's commit of its date is picked up
by the next run, whatever the date of that run. An error on one date stops the walk
with exit 1.

One entry per record line, in ledger order. Fields: `case`, `kind` (`create`,
`update`, `delete`, `defer`, `estimate`, `lesson`), `category` (from the slug
prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`; a Rule-class file
is `file` with its path), `slug`, `ref`, `source`, `supersedes`, `superseded_by`,
`origin` (`raw/<date>/ledger.md#case-N`; a lesson `#L<n>`), `line`, `text` (the
ledger line), `tags` (from `{tags:...}`), `fields`, `sections`, `replace`, `change`
(from the `then` block), `incomplete` (required fields the block lacks), `exists`
(a create whose page is on disk), `applied` (set by `guppi generate`).

The Spec is read by headings `## Case N` and `### Case N.M`. Under a heading, every
fenced block tagged `then` up to the next heading is YAML; a leading `> ` is
removed. The entry for a slug is the item with that `slug` under the key of its
kind. A Leaf's nested `estimate` becomes its own `create` entry. An `estimate` line
for a page created in the same ledger is folded into that create (`status`,
`result`); for an earlier page it is an `estimate` entry, an update. A `lesson` line
is a `create` in `lessons`: `kind`, `root_cause` and the sections `Trigger` and
`Root cause` from the line. A line with `{supersedes:case N}` marks the entries of
case N `superseded_by`. One decision entry per Case: `decision: decision-case-<N>`,
`case_text` (the seven quoted sections of the Case, verbatim, in the language of
the Spec), `targets` (one item per line of the Case). A line the grammar does not
parse goes under `unparsed`; the script continues.

An existing yaml is extended, never rewritten (case 41): entries whose `line` is
present stay as they are, with the librarian's edits and the `applied` marks; new
ledger lines become new entries at the end; an entry whose stored `text` differs
from the ledger line at that number is reported on stderr and left alone; a later
`supersedes` adds `superseded_by` to the earlier entry and changes nothing else; an
`estimate` line for a create already `applied` becomes its own `estimate` entry.
The count of entries added goes to stdout, one line per date. Exit 0; exit 1 when a
date fails.

## Estimates

- [[estimate-materialize-assembles]]
- [[estimate-materialize-walks-dates]]

## Parent

- [[rule-documentation]]

## Implementation

- `guppi/materialize.py`
- `tests/test_materialize.py`

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-31
- 2026-09-10 estimate estimate-materialize-assembles added · raw/2026-09-10/ledger.md#case-31
- 2026-09-10 updated: an existing yaml is extended with the ledger lines it does not hold, never rewritten (the How it works of case 31 already carries it) · raw/2026-09-10/ledger.md#case-41
- 2026-09-10 status: draft → built · cascade
- 2026-09-10 updated: without --date the script walks every raw/<date> with a ledger, so lines written after a date's librarian commit are materialized by the next run; exit 1 when a date fails · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 estimate estimate-materialize-walks-dates added · raw/2026-09-10/ledger.md#case-43
- 2026-09-09 status: built → draft · cascade
