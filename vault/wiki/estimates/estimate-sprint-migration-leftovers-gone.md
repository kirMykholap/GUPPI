---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-migration]]"
purpose: vault/parked/, the 2026-08 documents and the old archive root are gone, git tracks no raw date folder without a session, and the repository has no remote, each by a decision named at the close of the sprint
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
**＋** `vault/archive/` has no root outside the folders of its sprints, and the decision that deleted the old root is named in the reading.
**＋** Every file under `vault/raw/` that git tracks lies in a session folder `vault/raw/<date>/<HHMM>/`.
**＋** The repository has no remote, and `.claude/skills/hi/SKILL.md` runs neither `git pull` nor `gh`; the decision is named in the reading.
**－** `docs/migration/migration-plan.md` is outside this promise: the Case that closes the sprint deletes it.
**－** The `event_log.md` of a past date stays in `vault/raw/<date>/`, as `rule-raw-archive` keeps it, and does not fail this promise.

## History

- 2026-09-17 created · [[decision-case-209.3]]
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out (case 494.2) · [[decision-case-494.2]]
- 2026-09-29 updated: the Criterion replaced whole — the parked pages deleted, not archived; the migration plan left to the closing Case (case 510) · [[decision-case-510]]
- 2026-09-30 updated: the Criterion replaced whole — the raw date folders read by what git tracks, the remote removed and git pull and gh out of /hi, the old archive root deleted by case 102.1 (case 528.5) · [[decision-case-528.5]]
