---
type: decision
case: "1043"
status: current
children: ["[[decision-case-1043.1]]", "[[decision-case-1043.2]]"]
origin: raw/2026-11-20/1353/ledger.md#case-1043
sprint: plugin
created: 2026-11-20
tags: [github, git, ci, sprint, readme, workflow]
---

## Problem

A reader who finds GUPPI on GitHub learns neither what it is nor how to install it, and the repository states no license.

## Recommend

- **Which branches hold README.md and LICENSE**
  - Recommended: (a) main only.
  - Answer: agreed, (a).
- **What the install section tells a reader while prod holds no release**
  - Recommended: (a) both paths, with a note that no release is out yet.
  - Answer: agreed, (a).
- **Whose name the MIT license names**
  - Recommended: (a) the GitHub name `kirMykholap`.
  - Answer: agreed, (a).
- **Whether the README gives a figure for the cost**
  - Recommended: (a) no figure now.
  - Answer: agreed, (a).
- **How the README and the license are checked**
  - Recommended: (a) the existing README Estimate, plus a new Estimate for the license.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, the person agreed that the license text of the clean copy goes into the `## Backlog` of `entity-sprint-plugin`, and that no line of `then` promises it.
  - Taken: Case 1043.2 updates `entity-sprint-plugin` with that Backlog line, and its `－` line is dropped; by the other findings, Case 1043.1 replaces the Criterion of the README Estimate, and both Criteria read the files on the branch of the session.

## History

- 2026-11-23 created · raw/2026-11-20/1353/ledger.md#case-1043
