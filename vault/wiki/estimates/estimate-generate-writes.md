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
children and ## Children in order, the target's estimates and ## Estimates; an
update with set, sections, replace and change changes the field, the section, the
text and appends History; a replace absent or not unique fails that entry alone,
exit 1; a delete sets archived with History; a defer without a page writes a
placeholder with only the Case's fields; an estimate entry sets status and
overwrites ## Result, and one whose page already holds that status with a Result is
skipped; a lesson entry writes the lesson and its paired estimate per kind; one
decision page per Case with targets, and supersedes marks the earlier page
superseded; the cascade sets built; a declared new tag lands in tags.md, an
undeclared one is reported; log.md gains one line per write; applied entries are
marked and a rerun writes nothing; a create colliding with a page not marked exists
fails. Live: the 2026-09-10 yaml and the 2026-09-09 backfill; the reading records
pages created per category, make lint afterwards against the known-false list, and
git diff --stat.

## Method

pytest in tests/test_generate.py against a temp vault; the live reading once by hand

## Result

tests/test_generate.py 11 green; live 2026-09-10: 68 pages written or changed — rules 13 created and 8 updated, estimates 15, lessons 2, decisions 21, placeholders 2, cascade set 14 rules built; live 2026-09-09: 48 pages — decisions 34, lessons 7 with 7 estimates, 34 creates skipped as existing, 11 estimate lines skipped as already recorded, one failure: [delete][old-harness] of case 6 has no page and no category; make lint afterwards 159 findings, all on the known list; git diff --stat 40 tracked files, 126 new pages

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L71
