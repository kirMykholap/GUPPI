---
type: rule
kind: Leaf
purpose: Prevents the librarian from reading the ledger and the Spec itself, or from routing a decision by guesswork
status: draft
enforcement: check
implementation_ref: [guppi/materialize.py, tests/test_materialize.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-materialize-assembles]]", "[[estimate-materialize-walks-dates]]", "[[estimate-materialize-shows]]", "[[estimate-materialize-lifts-a-lesson]]", "[[estimate-materialize-marks-exists]]", "[[estimate-materialize-fails-alone]]", "[[estimate-materialize-finds-a-rule-class-item]]", "[[estimate-materialize-marks-superseded]]", "[[estimate-materialize-skips-a-carried-over-unit]]"]
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

It also prevents a promise from being written by derivation. No Estimate is derived
from a flag: an Estimate has its own ledger line and its own entry, and its Criterion
is the `given`, `when` and `then` of the Case that names it, lifted verbatim into the entry's `sections` and replacing what stood on the page (cases 189, 194.1); a Criterion the item writes under `sections` itself stands instead, on a `create` and on an `update` alike — it is signed in the same block, and it is how one Case touches two promises (case 204). A unit
whose folder holds `carry.md` is passed by with one line on stdout: its Spec was
ratified and its work not done (case 190.3). The mechanism and the full list of an
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
