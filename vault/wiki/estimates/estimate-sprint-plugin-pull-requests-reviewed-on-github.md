---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether a pull request from another account, a second account of the owner included, runs the checks of CI on GitHub and can be reviewed and merged into the branch plugin
method: by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close
origin: raw/2026-10-10/1713/ledger.md#case-756.4
sprint: plugin
created: 2026-10-10
tags: [sprint, github, git]
---

## Criterion

When:
In a session of the sprint `plugin` before its close, someone opens a pull request against the branch `plugin` of the repository of the project on GitHub from an account other than the owner's, such as a second account that the owner made for the test.

Then:
The checks of CI run on the pull request and show their result on it.
**＋** The owner reviews the pull request on GitHub and can merge it into `plugin`.
**－** The pull request does not go into the main branch before the close; the main branch takes it with `plugin` as `estimate-skill-sprint-close-leads-the-closing-session` sets.

## History

- 2026-10-10 created · [[decision-case-756.4]]
- 2026-10-10 updated: the Criterion replaced whole — the pull request goes against the branch plugin, and a second account of the owner counts as another account · [[decision-case-766]]
