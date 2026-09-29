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

When:
Someone reads the tree of the repository at the close of the sprint.

Then:
`vault/parked/` is absent: its pages were deleted by a decision named in the reading, and git history keeps them.
**＋** Under `docs/` no 2026-08 document remains, and no rule document of `docs/migration/`; each became a page, was archived, or was deleted by a decision named in the reading.
**＋** `vault/archive/` has no root outside the folders of its sprints; `vault/raw/` has no date folder without a session.
**＋** A decision stands on `git pull` without an upstream and on `gh` without a login — keep as is, or repair — and is named in the reading.
**－** `docs/migration/migration-plan.md` is outside this promise: the Case that closes the sprint deletes it.
**－** What to do with the old archive root, the date folders of `vault/raw/`, `git pull` and `gh`: those are the Cases of Slice 5.

## History

- 2026-09-17 created · [[decision-case-209.3]]
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out (case 494.2) · [[decision-case-494.2]]
- 2026-09-29 updated: the Criterion replaced whole — the parked pages deleted, not archived; the migration plan left to the closing Case (case 510) · [[decision-case-510]]
