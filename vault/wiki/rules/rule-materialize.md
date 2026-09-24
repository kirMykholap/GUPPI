---
type: rule
kind: Leaf
purpose: Prevents the librarian from reading the ledger and the Spec beyond its unticked lines, or from routing a decision by guesswork
status: built
enforcement: check
implementation_ref: [guppi/materialize.py, tests/test_materialize.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-materialize-assembles]]", "[[estimate-materialize-walks-dates]]", "[[estimate-materialize-shows]]", "[[estimate-materialize-lifts-a-lesson]]", "[[estimate-materialize-marks-exists]]", "[[estimate-materialize-fails-alone]]", "[[estimate-materialize-marks-superseded]]", "[[estimate-materialize-skips-a-carried-over-unit]]", "[[estimate-materialize-carries-addresses]]", "[[estimate-materialize-lifts-unfiltered-on-a-schema-change]]", "[[estimate-materialize-refolds-a-reading-on-a-supersede]]", "[[estimate-materialize-lifts-when-and-then]]", "[[estimate-materialize-lifts-a-create-by-the-schema]]", "[[estimate-materialize-changes-a-named-part-alone]]"]
origin: raw/2026-09-10/ledger.md#case-31
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Purpose

Prevents the librarian from reading the ledger and the Spec beyond its unticked lines (case 271), or from routing
a decision by guesswork. The yaml is the one input a clean context needs. Every line
of the ledger is an entry. Its route is the Routing Table in the docstring of `guppi/materialize.py` (case 364.1). Its content is
lifted from the `then` block of its Case in the Spec — `set`, `sections`, `replace`, `change`, and `rename` or `reword` when the item carries it (cases 258.2, 274.3). What is missing is named, not
invented — but for a Case superseded in its own session and gone from the Spec: its entries, marked `superseded_by`, carry no `incomplete: [then]`, and its `decisions` record no `case_text` and no missing section; the mark alone is its completeness (case 299.3). If a route cannot be derived from the ledger and the Spec alone, that is a
defect of the ledger, and it shows here. The keys of a `create` are lifted by the category's `schema.yaml` on disk (case 214.1) — but for a category whose `rule-<category>-schema` the same unit creates or updates: its `create` items are lifted whole, no `unknown`, since the schema on disk catches up only at the render after `generate` (case 308.2).

It also prevents a promise from being written by derivation. No Estimate is derived
from a flag: an Estimate has its own ledger line and its own entry, and its Criterion is the `when` and `then` of the Case that names it (case 378.2), lifted verbatim into the entry's `sections` and replacing what stood on the page (cases 189, 194.1); a Criterion the item writes under `sections` itself stands instead, on a `create` and on an `update` alike — it is signed in the same block, and it is how one Case touches two promises (case 204). An `update` item names the part it changes: one that names a part — `set` without `status`, `replace`, a section other than `Criterion` — and writes no Criterion changes that part alone, nothing lifted; a part inside the Criterion — the `old` of a `replace` pair stands in the page's `## Criterion` — is `incomplete: [criterion]` and sets no status, a Criterion changes only whole (case 378.4); a written `sections.Criterion` beside any other part stands and sets `pending`; one that names no part, or carries `set.status`, replaces the Criterion whole (case 296). An `update` item's `reword` — a list of `{old, new}` pairs — is carried to the entry as written, for `generate` to apply; a mapping or a scalar under it is `incomplete: [reword]` (case 274.3). A decision line's `{addresses:<lesson slug>}` is carried to the entry as `addresses`, a list, and the lesson entry of that slug in the same unit gets `addressed_by: decision-case-N` at the entry's level, never as a page field; a mark whose lesson is not in the unit is `incomplete: [addresses]` on the decision entry (case 284.3). A lesson line's `{addressed_by:case N}` gives its entry the same `addressed_by: decision-case-N` when a decision line of Case N stands earlier in the unit, and `incomplete: [addressed_by]` otherwise (case 377.3). A unit
whose folder holds `carry.md` is passed by with one line on stdout: its Spec was
ratified and its work not done (case 190.3). A reading — an `estimate` line — folds into the unapplied `create` of its slug in the unit; a `create` a `{supersedes}` marks is never folded into, and the readings already folded into it move to the live `create` of the same slug in the unit, or each becomes an entry of its own from its ledger line (case 309). The mechanism and the full list of an
entry's fields, each with its writer, live in the docstring of `guppi/materialize.py`.

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
- 2026-09-15 updated: an entry with librarian and no line is readable: the librarian's synthesis entries are left alone without a stderr line; the text of 142.1 made precise (case 158) · [[decision-case-158]]
- 2026-09-15 updated: the then item of a Rule-class file is found by file as well as by slug; no false incomplete on a file entry (case 161) · [[decision-case-161]]
- 2026-09-15 updated: a supersedes marks every entry of the earlier Case by its case number, the derived block removal included; the filter by kind is gone (case 175) · [[decision-case-175]]
- 2026-09-15 updated: the second statement of the supersedes mark says every entry by case number; block 130.2 with its filter by kind leaves the Estimate (case 177, supersedes 130.2) · [[decision-case-177]]
- 2026-09-15 status: built → draft · cascade
- 2026-09-16 deferred · [[decision-case-182]]
- 2026-09-16 status: draft → built · cascade
- 2026-09-16 updated: materialize derives no Estimate from contract, method or supersedes; an Estimate has its own line and its own entry, its Criterion lifted from the Case; How it works dropped, the mechanism and the full field list moved to the docstring of guppi/materialize.py (case 189) · [[decision-case-189]]
- 2026-09-16 estimate estimate-materialize-shows added · [[decision-case-189]]
- 2026-09-16 estimate estimate-materialize-lifts-a-lesson added · [[decision-case-189]]
- 2026-09-16 estimate estimate-materialize-marks-exists added · [[decision-case-189]]
- 2026-09-16 estimate estimate-materialize-fails-alone added · [[decision-case-189]]
- 2026-09-16 estimate estimate-materialize-finds-a-rule-class-item added · [[decision-case-189]]
- 2026-09-16 estimate estimate-materialize-marks-superseded added · [[decision-case-189]]
- 2026-09-16 updated: a unit whose folder holds carry.md is skipped with one line on stdout; no yaml is written for it (case 190.3) · [[decision-case-190.3]]
- 2026-09-16 estimate estimate-materialize-skips-a-carried-over-unit added · [[decision-case-190.3]]
- 2026-09-16 defer by decision-case-182 superseded · [[decision-case-191]]
- 2026-09-16 status: built → draft · cascade
- 2026-09-16 updated: Purpose carries the text of 189 and 190.3; How it works dropped by hand, the mechanism and the field list in the docstring (case 194.1) · [[decision-case-194.1]]
- 2026-09-16 updated: a written Criterion stands on a create and on an update alike (case 204) · [[decision-case-204]]
- 2026-09-17 status: draft → built · cascade
- 2026-09-20 updated: the rename key of an update item is carried into the entry (case 258.2) · [[decision-case-258.2]]
- 2026-09-20 updated: reword carried from the then block to the entry as a list of pairs (case 274.3) · [[decision-case-274.3]]
- 2026-09-20 updated: the ban on the Spec excepts its unticked lines; reword in the list of the item's keys (case 277.1) · [[decision-case-277.1]]
- 2026-09-21 updated: the mark addresses on a decision line reaches the lesson's entry as addressed_by (case 284.3) · [[decision-case-284.3]]
- 2026-09-21 estimate estimate-materialize-carries-addresses added · [[decision-case-284.3]]
- 2026-09-21 status: built → draft · cascade
- 2026-09-21 updated: an update item of an Estimate that names a part changes that part alone; a part inside the Criterion sets pending; a part not named is the whole Criterion (case 296) · [[decision-case-296]]
- 2026-09-21 deferred · [[decision-case-298]]
- 2026-09-22 defer by decision-case-298 superseded · [[decision-case-299.2]]
- 2026-09-22 updated: an entry of a Case superseded in its own session and gone from the Spec is complete by the mark alone (case 299.3) · [[decision-case-299.3]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-22 updated: a create of a category whose schema rule the same unit changes is lifted whole (case 308.2) · [[decision-case-308.2]]
- 2026-09-22 estimate estimate-materialize-lifts-unfiltered-on-a-schema-change added · [[decision-case-308.2]]
- 2026-09-22 updated: a reading folded into a superseded create moves to the live create of the slug or becomes an entry of its own (case 309) · [[decision-case-309]]
- 2026-09-22 estimate estimate-materialize-refolds-a-reading-on-a-supersede added · [[decision-case-309]]
- 2026-09-22 updated: the route is this page, not §5 of index.md (case 318) · [[decision-case-318]]
- 2026-09-22 status: built → draft · cascade
- 2026-09-22 estimate estimate-materialize-finds-a-rule-class-item archived · cleanup
- 2026-09-23 status: draft → built · cascade
- 2026-09-23 updated: the Routing Table lives in the docstring of guppi/materialize.py (case 364.1) · [[decision-case-364.1]]
- 2026-09-23 updated: the docstring of guppi/materialize.py finds a then item by slug alone, no Rule-class file (case 365) · [[decision-case-365]]
- 2026-09-23 updated: a lesson line's {addressed_by:case N} reaches its entry as addressed_by (case 377.3) · [[decision-case-377.3]]
- 2026-09-23 updated: the Criterion lifted is when and then (case 378.2) · [[decision-case-378.2]]
- 2026-09-23 estimate estimate-materialize-lifts-when-and-then added · [[decision-case-378.2]]
- 2026-09-23 updated: a pair inside a Criterion is incomplete (case 378.4) · [[decision-case-378.4]]
- 2026-09-25 estimate estimate-materialize-lifts-a-create-by-the-schema added · [[decision-case-397.2]]
- 2026-09-25 estimate estimate-materialize-changes-a-named-part-alone added · [[decision-case-397.3]]
- 2026-09-25 status: built → draft · cascade
- 2026-09-25 status: draft → built · cascade
