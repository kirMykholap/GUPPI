---
type: estimate
kind: QA
status: pending
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
children and ## Children in order, the target's estimates and ## Estimates; an
update with set, sections, replace and change changes the field, the section, the
text and appends History; a replace absent or not unique fails that entry alone,
exit 1; a delete sets archived with History; a defer without a page writes a
placeholder with only the Case's fields and deferred_by, a defer with a page appends
the decision slug to its deferred_by, and a supersedes removes it; an estimate entry
sets status and overwrites ## Result whatever the page held; a lesson entry writes
the lesson and no Estimate; one decision page per Case with one list per kind present —
create, update, delete, defer, the slugs in ledger order — and the sections Context, Problem, Given, When, written before
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

tests/test_generate.py 21 green with the four folded criteria, no skip, no paired estimate, the decision-page shape, deferred_by and its clearing, the decision written first, History wikilinks, a stale failed dropped; live 2026-09-11, the librarian's run: 13 decision pages, 6 lessons, 2 insights created, 14 rules, 11 estimates, 2 lessons, 2 decisions updated, 21 estimates set archived and moved by cleanup, stderr one line (tag tests unregistered), no entry failed, exit 0; make lint afterwards 146, all on the known-false list plus the 25 decision findings of lint's own archived-target defect; git diff --stat of 10731cb is vault/ only

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L71
- 2026-09-11 updated: the criteria of the four Estimates of Cases 47–48 folded in; no skip, no paired estimate, the decision-page shape and deferred_by of Case 52; pending until the End of Work reading · [[decision-case-53.2]]
- 2026-09-11 updated: criterion: a stale failed mark is dropped on apply (case 53.3) · [[decision-case-53.3]]
- 2026-09-12 status: pending → passed · raw/2026-09-11/ledger.md#L76
- 2026-09-12 updated: the decision page's four lists replace the aligned pair in the criterion (case 59.4) · [[decision-case-59.4]]
