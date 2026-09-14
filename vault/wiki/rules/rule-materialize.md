---
type: rule
kind: Leaf
purpose: Prevents the librarian from reading the ledger and the Spec itself, or from routing a decision by guesswork
status: built
enforcement: check
implementation_ref: [guppi/materialize.py, tests/test_materialize.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-materialize-assembles]]", "[[estimate-materialize-walks-dates]]"]
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

`uv run guppi materialize [--date YYYY-MM-DD]` reads one unit at a time. A session folder `raw/<date>/<HHMM>/` holding a `ledger.md` is a unit (case 103.2): it reads that ledger and `raw/<date>/<HHMM>/spec.md` alone, and writes `raw/<date>/<HHMM>/materialize.yaml`, the `origin` of every entry `raw/<date>/<HHMM>/ledger.md#…`. A date-level `raw/<date>/ledger.md` (the shape before case 103) is a unit read as before: the ledger and every Spec of the date — `raw/<date>/<HHMM>/spec.md` in folder order, and `raw/<date>/spec.md` when the date has one (dates before case 73) — written to `raw/<date>/materialize.yaml` with the date form of `origin`; on a date with both shapes the date-level unit goes first; the yaml's `spec` field names the file each Case was found in, and a Case heading found in two files stops the walk with exit 1. Without `--date` it
walks every unit under `raw/` — dates ascending, the date-level ledger of a date first, then its sessions in folder order — and prints one
line per unit; a line written after the librarian's commit of its date is picked up
by the next run, whatever the date of that run. An error of a unit — no `ledger.md`, a Case heading in two files — stops the walk with exit 1; a line whose lift failed marks its entry, the unit exits 1 and the walk goes on (case 142.4). With `--show` (case 76) the same walk prints to stdout the yaml each date would be written with — entries, `unparsed`, `incomplete` marks, decision groups, one document per date — and writes nothing under `raw/`; the agent and pre-task look before the librarian runs.

One entry per record line, in ledger order. The fields of an entry, each with its writer (case 142.1) — from the ledger line: `case`, `kind` (`create`, `update`, `delete`, `defer`, `estimate`, `lesson`), `category` (from the slug prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`; a Rule-class file is `file` with its `path`), `slug`, `ref`, `source`, `supersedes`, `tags` (from `{tags:...}`), `origin` (`raw/<date>/<HHMM>/ledger.md#case-N`; a lesson `#L<n>`), `line`, `text` (the ledger line), `decision` (`decision-case-<N>`); from the `then` block: `fields`, `sections`, `replace`, `change`, `impact`, `incomplete` (required fields the block lacks), `exists` (a create whose page is on disk with an `origin` carrying this line's `#case-N`; a page of another Case, live or archived, leaves the entry a create for `generate` to refuse as a collision, case 105.2); derived by this script: `derived`, `criterion_block`, `set`, `case_removed`, and `status`, `result`, `folded` of a reading folded into a create; `superseded_by` from a later `{supersedes}` in any unit; `failed` from a lift that raised; set by `guppi generate`: `applied` (the time applied) and `failed` (the error); set by the librarian: `near`, and `librarian` with the value `merged` or `synthesis` (`rule-documentation`). A key the code writes and this list does not name is a finding.

The Spec is read by headings `## Case N` and `### Case N.M`. Under a heading, every
fenced block tagged `then` up to the next heading is YAML; a leading `> ` is
removed. The entry for a slug is the item with that `slug` under the key of its
kind. A Leaf `create` whose item carries `method` yields a second entry for its Estimate, with no line of its own (case 72.3): category `estimates`, slug `estimate-<target minus its prefix>` or the item's `estimate_slug`, `ref` the target, `tags` the target's, `origin` and `decision` the line's, sections Context (the Case's `problem`), Criterion (`### case N`, then the Case's `when` and `then` verbatim with their operands) and Method. An `update` of a Leaf whose item carries `contract: changed` yields an `update` entry of the Estimate the item's `estimate_slug` names, or of the page's one Estimate when it carries exactly one; when it carries none or more than one and the item names none, the entry goes without a slug and is marked `incomplete: [estimate]` rather than guessing (case 90.1): `criterion_block` (`### case N` with `when` and `then`), `set: {status: pending}`, `sections: {Method}` when the item carries `method`; `contract: same` yields nothing. A line with `{supersedes:case N}` also yields a `remove_criterion` entry for the Estimate case N shaped. The decision entry carries `criterion`, one `{estimate, case}` per Estimate the Case shaped. A nested `estimate` in an older Spec becomes its own `create` entry as before, for a line with its slug; a standalone estimate `create` with `ref` maps `context`, `criterion` and `method` into `sections` the same way, so the page gets its Criterion and Method sections whichever way it was born. An `estimate` line
for a page created in the same ledger is folded into that create (`status`,
`result`); for an earlier page it is an `estimate` entry, an update. A `lesson` line
is a `create` in `lessons`: `kind`, `root_cause`, `source` when the braces of the line carry one, and the sections `Trigger` and
`Root cause` from the line; a `knowledge` lesson whose line carries no `source` is marked `incomplete: [source]`, an `error` lesson never (case 87). A line with `{supersedes:case N}` marks the entries of
case N `superseded_by`. One decision entry per Case: `decision: decision-case-<N>`, `case_text` (the quoted sections of the Case, verbatim, in the language of the Spec), `targets` (one item per line of the Case); a sub-case's `context`, `problem`, `recommend` and `given` are its own when present and its parent's otherwise, `when` never; a Case whose text lacks `given` or `when`, its parent's included, is marked `incomplete` only when a kind other than `defer` is among its lines, since the short form has neither. A line the grammar does not
parse goes under `unparsed`; the script continues. A line whose lift raises — a `then` item of an unexpected shape, any error while the entry is built — becomes an entry `{line, text, failed: "<Type>: <message>"}` without `kind`, reported on stderr as `materialize: line N: <message>`; the other lines are lifted, the yaml is written, the unit exits 1 and the walk goes on to the next unit; on the next run such an entry is lifted again from its line and replaced when the lift succeeds. An existing entry the script cannot read — not a mapping, or a mapping without `line` and without `derived` — is left as it is, named on stderr, and does not end the run (case 142.1). `new_tags` declared in the `then`
block of any Case of the Spec, with decision lines or without, go to the yaml's
`new_tags` once each, so a tag a lesson brought can be declared at the next Plan Mode.

An existing yaml is extended, never rewritten (case 41): entries whose `line` is
present stay as they are, with the librarian's edits and the `applied` marks; new
ledger lines become new entries at the end; an entry whose stored `text` differs
from the ledger line at that number is reported on stderr and left alone; a later `supersedes` adds `superseded_by` to the entries of the earlier Case in whichever unit's yaml holds them — this one or any other under `raw/` — and to that unit's `decisions` list, and changes nothing else; a foreign yaml is written with that mark only (case 130.2); an
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
- 2026-09-10 updated: the field list names folded, applied and failed · raw/2026-09-10/ledger.md#case-49
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: a standalone estimate create maps context, criterion and method into sections, as the nested one does · [[decision-case-53.3]]
- 2026-09-11 updated: a decision entry lacks given or when: incomplete only when a kind other than defer is among its lines · [[decision-case-56]]
- 2026-09-11 status: built → draft · cascade
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 updated: a sub-case inherits a missing given from its parent, as context, problem and recommend; when stays its own (case 60) · [[decision-case-60]]
- 2026-09-12 updated: new_tags are collected from every Case block, lines or none (case 61) · [[decision-case-61]]
- 2026-09-12 deferred · [[decision-case-69]]
- 2026-09-12 updated: a Leaf create with method and an update with contract: changed yield the Estimate's entries; supersedes removes a criterion block; the decision entry names the Estimates shaped (case 72.3) · [[decision-case-72.3]]
- 2026-09-12 updated: one Spec per session folder; all of a date's Specs are read (case 73.5) · [[decision-case-73.5]]
- 2026-09-12 defer by decision-case-69 superseded · [[decision-case-76]]
- 2026-09-12 updated: a --show mode prints the yaml and writes nothing (case 76, supersedes 69) · [[decision-case-76]]
- 2026-09-12 deferred · [[decision-case-82]]
- 2026-09-12 defer by decision-case-82 superseded · [[decision-case-87]]
- 2026-09-12 updated: the lesson entry carries source from the braces of its line (case 87) · [[decision-case-87]]
- 2026-09-12 updated: the derived update names its Estimate instead of taking the first of the page's list (case 90.1) · [[decision-case-90.1]]
- 2026-09-12 updated: the item's key is named estimate_slug, as case 86 ratified (case 99) · [[decision-case-99]]
- 2026-09-13 updated: the unit of the walk is the session folder with its own ledger, yaml, Spec and origin; a date-level ledger is walked in the old shape (case 103.2) · [[decision-case-103.2]]
- 2026-09-13 updated: exists only when the page on disk was born of the same Case; another Case's page is a collision (case 105.2) · [[decision-case-105.2]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: a supersedes marks the earlier Case's entries in the yaml of any unit under raw/, so a failed entry superseded from a later session no longer keeps its unit out of the archive (case 130.2) · [[decision-case-130.2]]
- 2026-09-14 updated: an entry fails alone in materialize, the walk goes on; an unreadable existing entry is left alone; the field list names every field and its writer (case 142.1) · [[decision-case-142.1]]
- 2026-09-14 updated: a failed line does not stop the walk; a unit error still does (case 142.4) · [[decision-case-142.4]]
