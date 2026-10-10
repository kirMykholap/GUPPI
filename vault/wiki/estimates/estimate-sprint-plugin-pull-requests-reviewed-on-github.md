---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether a pull request from another account runs the checks of CI on GitHub and can be reviewed and merged into main
method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close
origin: raw/2026-10-10/1713/ledger.md#case-756.4
sprint: plugin
created: 2026-10-10
tags: [sprint, github, git]
---

## Criterion

When:
In a session of the sprint `plugin` before its close, someone opens a pull request against `main` of the repository of the project on GitHub from an account other than the owner's.

Then:
The checks of CI run on the pull request and show their result on it.
**＋** The owner reviews the pull request on GitHub and can merge it into `main`.

## History

- 2026-10-10 created · [[decision-case-756.4]]
