---
type: rule
kind: Leaf
purpose: Prevents the librarian from needing the ledger beyond its one read or the Spec beyond its unticked lines, or from routing a decision by guesswork
status: built
enforcement: check
implementation_ref: [guppi/materialize.py, tests/test_materialize.py]
parent: "[[rule-documentation]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, workflow, ledger]
core: true
---

## Purpose

Prevents the librarian from needing the ledger beyond its one read or the Spec beyond its unticked lines, or from routing
a decision by guesswork. The yaml is the one input a clean context needs. Every line
of the ledger is an entry. `parse_line` reads a record line with or without spaces between its brackets, and returns None, never an error, for a line it cannot read. Its route is the Routing Table in the docstring of `guppi/materialize.py`. Its content is
lifted from the `then` block of its Case in the Spec — `set`, `sections`, `replace`, `change`, and `rename` or `reword` when the item carries it. A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — gives each decision entry of its Case `incomplete: [comment]`: after a space YAML drops the rest of the line, so the value may be cut, and after a tab PyYAML, the library the scripts use, refuses the whole block; the judgment is one function, which the `Stop` hook of `rule-spec-write` imports. What is missing is named, not
invented — but for a Case superseded in its own session and gone from the Spec: its entries, marked `superseded_by`, carry no `incomplete: [then]`, and its `decisions` record no `case_text` and no missing section; the mark alone is its completeness. If a route cannot be derived from the ledger and the Spec alone, that is a
defect of the ledger, and it shows here. The keys of a `create` are lifted by the category's `schema.yaml` on disk — but for a category whose `rule-<category>-schema` the same unit creates or updates: its `create` items are lifted whole, no `unknown`, since the schema on disk catches up only at the render after `generate`.

It also prevents a promise from being written by derivation. No Estimate is derived
from a flag: an Estimate has its own ledger line and its own entry, and its Criterion is the `when` and `then` of the Case that names it, lifted verbatim into the entry's `sections` and replacing what stood on the page; a Criterion the item writes under `sections` itself stands instead, on a `create` and on an `update` alike — it is signed in the same block, and it is the one promise of its Case or sub-case. An `update` item names the part it changes: one that names a part — `set` without `status`, `replace`, a section other than `Criterion` — and writes no Criterion changes that part alone, nothing lifted; a part inside the Criterion — the `old` of a `replace` pair stands in the page's `## Criterion` — is `incomplete: [criterion]` and sets no status, a Criterion changes only whole; a written `sections.Criterion` beside any other part stands and sets `pending`; one that carries `set.status` replaces the Criterion whole, and one that carries `change` alone writes its History line and nothing else, on an Estimate as on any page. An `update` item's `reword` — a list of `{old, new}` pairs — is carried to the entry as written, for `generate` to apply; a mapping or a scalar under it is `incomplete: [reword]`. A decision line's `{addresses:<lesson slug>}` is carried to the entry as `addresses`, a list, and the lesson entry of that slug in the same unit gets `addressed_by: decision-case-N` at the entry's level, never as a page field; a mark whose lesson is not in the unit is `incomplete: [addresses]` on the decision entry. A lesson line's `{addressed_by:case N}` gives its entry the same `addressed_by: decision-case-N` when a decision line of Case N stands earlier in the unit, and `incomplete: [addressed_by]` otherwise. A unit
whose folder holds `carry.md` is passed by with one line on stdout: its Spec was
ratified and its work not done. A reading — an `estimate` line — folds into the unapplied `create` of its slug in the unit; a `create` a `{supersedes}` marks is never folded into, and the readings already folded into it move to the live `create` of the same slug in the unit, or each becomes an entry of its own from its ledger line. An `estimate` entry carries no `case`, so no `{supersedes}` reaches it: a reading that must not apply is retired only by a ratified Case, whose one-off migration sets `superseded_by` on the entry to a list that holds the number of that Case and removes its `failed`. The yaml's `sprint` is the first `## <id>` heading of `sprint.md`, but in a unit whose ledger holds a `create` decision line of `entity-sprint-<id>` it is that `<id>`, so that the session that opens a sprint belongs to it, as `rule-sprint-close` sets it. The mechanism and the full list of an entry's fields, each with its writer, live in the docstring of `guppi/materialize.py`.

## History

- 2026-10-14 shipped with GUPPI
