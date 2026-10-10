---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data, and fails when one remains
method: by hand, a CI run on GitHub and the clean branch it wrote, read in a session of the sprint plugin before its close
origin: raw/2026-10-10/1713/ledger.md#case-756.5
sprint: plugin
created: 2026-10-10
tags: [sprint, ci, git]
---

## Criterion

When:
In a session of the sprint `plugin` before its close, a commit lands on the branch `plugin` of the repository of the project on GitHub, and CI runs on it.

Then:
CI writes a clean version of the project to a branch of its own.
**＋** No text of the clean version holds a reference to a case or a decision.
**＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
**＋** A check of CI fails the run when a case reference or session data remains in the clean version.

## History

- 2026-10-10 created · [[decision-case-756.5]]
- 2026-10-10 updated: the Criterion replaced whole — CI starts on a commit to the branch plugin, where the sprint commits · [[decision-case-767]]
