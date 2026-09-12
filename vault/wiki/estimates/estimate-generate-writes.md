---
type: estimate
kind: QA
status: passed
target: rule-page-generation
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

Every page of the vault comes through this script from Slice 3 on. A derived field computed wrong, or a ratified one dropped, is corrupted everywhere at once.

## Criterion

Against a temp vault from one yaml: a MOC rule create, a Leaf child create with ref
and its nested estimate yield three pages that pass their schema.yaml, the parent's
children and ## Children in order, the target's estimates and ## Estimates; a derived Estimate create yields a pending page with Context, Criterion as a ### case N block and Method, listed on its target; an update carrying a criterion block appends it to ## Criterion and sets pending, a removal deletes the block, each with its History line; an update with set, sections, replace and change changes the field, the section, the
text and appends History; a replace absent or not unique fails that entry alone,
exit 1; a delete sets archived with History; a defer without a page writes a
placeholder with only the Case's fields and deferred_by, a defer with a page appends
the decision slug to its deferred_by, and a supersedes removes it; an estimate entry
sets status and overwrites ## Result whatever the page held; a lesson entry writes
the lesson and no Estimate; one decision page per Case with one list per kind present —
create, update, delete, defer, the slugs in ledger order — and the sections Context, Problem, Given, and Criterion links when the Case shaped an Estimate, no When, written before
the entries of its lines, and supersedes marks the earlier page superseded; History
and log lines of a Case's entries end with the decision wikilink, a reading's or a
lesson's with the ledger pointer; the cascade sets built; a declared new tag lands
in tags.md, an undeclared one is reported; log.md gains one line per write.
**＋** An entry whose field has a shape the script does not expect, or in which any
exception is raised, is marked failed, reported on stderr and skipped; the rest
apply; exit 1.
**＋** After each applied entry its lines are in log.md; a run that stops at entry N
leaves the feed level with the pages up to N.
**＋** History lines and log.md lines carry the date of the run; created carries the
yaml's date.
**＋** A delete whose slug is neither a category prefix nor a Rule-class file is
printed on stdout as outside the vault and marked applied; a delete of a missing
page with a category fails.
Applied entries are marked, a stale failed mark left by an earlier run is dropped on apply, and a rerun writes nothing; a create colliding with a
page not marked exists fails. Live: the yaml of the session's librarian run; the
reading records pages created per category, make lint afterwards against the
known-false list, and git diff --stat.

## Method

pytest in tests/test_generate.py against a temp vault; the live reading once by hand

## Result

unit: tests/test_generate.py green in the same 47, with the derived Estimate page and the decision page's Criterion links of case 72.4; live 2026-09-12, the librarian's run of session J on raw/2026-09-12/materialize.yaml: 76 pages for the date and 0 for the three earlier dates, exit 0, stderr empty, every entry of every yaml applied and none failed — 30 decision pages created and 6 set superseded, 17 rules updated, 2 estimates created and 11 updated, 5 lessons created and 5 set clustered, 1 insight created and 3 updated, 21 derived criterion blocks appended with their Estimate set pending, 8 remove_criterion entries applied, 11 file entries skipped as Rule-class; guppi lint afterwards 133 findings in the known-false classes only (128 schema, 3 orphan, 1 ref, 1 method) against 129 before the run; git show --stat 8836953 touches vault/ only

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L71
- 2026-09-11 updated: the criteria of the four Estimates of Cases 47–48 folded in; no skip, no paired estimate, the decision-page shape and deferred_by of Case 52; pending until the End of Work reading · [[decision-case-53.2]]
- 2026-09-11 updated: criterion: a stale failed mark is dropped on apply (case 53.3) · [[decision-case-53.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-11/ledger.md#L76
- 2026-09-12 updated: the decision page's four lists replace the aligned pair in the criterion (case 59.4) · [[decision-case-59.4]]
- 2026-09-12 updated: the derived Estimate page and the decision page's Criterion links join the criterion (case 72.4); pending until the unit reading · [[decision-case-72.4]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L167
