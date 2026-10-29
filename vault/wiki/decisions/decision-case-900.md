---
type: decision
case: "900"
status: current
children: ["[[decision-case-900.1]]", "[[decision-case-900.2]]", "[[decision-case-900.3]]", "[[decision-case-900.4]]", "[[decision-case-900.5]]"]
origin: raw/2026-10-29/0327/ledger.md#case-900
sprint: plugin
created: 2026-10-29
tags: [session, harness, git, plugin, ci]
---

## Problem

Five install checks wait in the backlog, though the events their methods wait for have come. No Case sets when their readings are taken. Two of them would also reach the clean copy with a method that cannot run in an installed project.

## Recommend

- **What the methods of the two Estimates that ship once passed say**
  - Recommended: (a) reword the two methods now, so that each states that it runs in a repository that holds the command `ship`, and the second drops its pointer to the Estimate that is not shipped; the steps, the Criterion and the `pending` status stand.
  - Answer: agreed, (a).
- **How the install readings run in Work Mode**
  - Recommended: (a) one `stop:` task: the agent runs `test_ship.py -k skeleton` in the repository and the three `--check` commands over a fresh clean copy written for them alone, and writes a second fresh copy, in which no command runs, as the catalogue; then the person makes the three installs from that catalogue and reports, and the five readings are recorded.
  - Answer: agreed, (a).
- **Change**
  - Asked: after the findings of `/pre-spec`, the person agreed that the item on how the install readings run should match the tasks of Case 900.2.
  - Taken: the item now says that the skeleton tests run in the repository, that the `--check` commands run over a copy of their own, and that the installs take a second copy as the catalogue; the decision lines stand as they were.

## History

- 2026-10-29 created · raw/2026-10-29/0327/ledger.md#case-900
