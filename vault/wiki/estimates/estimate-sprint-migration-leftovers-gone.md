---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-migration]]"
purpose: vault/parked/, the 2026-08 documents, the old archive root and the empty raw date folders are gone by decision at the close of the sprint
method: one reading of the tree by hand at the close of the sprint, each path and decision named in the estimate line
origin: raw/2026-09-16/2238/ledger.md#case-209.3
sprint: migration
created: 2026-09-16
tags: [sprint, git]
---

## Criterion

Given:
Slice 4 and Slice 5 today list things outside the vault: `vault/parked/`, `docs/superpowers/`, `docs/HANDOFF.md`, `docs/migration/rule-*.md`, the 2026-08 documents under `docs/`, the old `vault/archive/` of August, the `raw/<date>/` folders holding only an `event_log.md`, decisions 11.1 and 11.2.

When:
Someone reads the tree of the repository at the close of the sprint.

Then:
`vault/parked/` is empty or absent: each of its pages became a live vault page or lies in the archive.
**＋** Under `docs/` no 2026-08 document and no `docs/migration/rule-*.md` remains; each became a page, was archived, or was deleted by a decision named in the reading.
**＋** `vault/archive/` has no root outside `<sprint>/`; `raw/` has no date folder without a session.
**＋** A decision stands on `git pull` without an upstream and on `gh` without a login — keep as is, or repair — and is named in the reading.
**－** What to do with each thing this promise does not decide: those are the Cases of Slices 4 and 5.

## History

- 2026-09-17 created · [[decision-case-209.3]]
