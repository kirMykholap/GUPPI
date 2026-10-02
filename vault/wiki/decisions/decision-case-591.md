---
type: decision
case: "591"
status: current
children: ["[[decision-case-591.1]]", "[[decision-case-591.3]]", "[[decision-case-591.4]]", "[[decision-case-591.7]]", "[[decision-case-591.8]]", "[[decision-case-591.9]]", "[[decision-case-591.10]]", "[[decision-case-591.11]]", "[[decision-case-591.12]]"]
origin: raw/2026-10-02/1202/ledger.md#case-591
sprint: migration
created: 2026-10-02
tags: [session, workflow, harness, git, render, hooks, sprint, ledger]
---

## Problem

The placeholder `rule-spec-box` keeps `make lint` red, and the person chose to build the Spec box rather than archive it. The questions were: how a conserved Spec runs on a branch of its own without the vault conflicting at the merge, how a session takes it up, and how much of that is built now.

## Recommend

- **What happens to the page `rule-spec-box`**
  - Recommended: (a) archive the page and keep the idea as a note in the sprint page's backlog list.
  - Answer: (c), build it now. The person described a branch made at once for each saved Spec, which they enter to build it, or leave while work goes on in the shared branch. They said the documentation must be settled first, since merging branches brings conflicts, and asked for a proposal.
- **Is the broken code fence of `decision-case-13` fixed in this Case**
  - Recommended: (a) fix it here, as a sub-case.
  - Answer: (a), agreed.
- **When the branch of a saved plan is made, and what it is**
  - Recommended: (a) a plain branch made by `/carry` from the commit that saves the plan; the session stays on the shared branch.
  - Answer: (a), with one correction: the branch is made from the commit after the whole of `/carry` is done, the brief written and the rest.
- **How the documentation stays free of merge conflicts**
  - Recommended: (a) only the shared branch writes the vault. Before the work, the plan's branch takes in the shared branch, pre-spec checks the plan against today's pages, and only a Case on a page whose History has a line after the save is built again and ratified again.
  - Answer: (a). The person first wrote "4) b", then said the numbers were mixed up and confirmed (a).
- **Where taking up a saved plan starts**
  - Recommended: (b) from Plan Mode at any point; the session's own Cases are saved by `/carry` with their branch, then the box runs the saved plan.
  - Answer: (b), after the person asked whether this is all one session — `/carry`, then the box.
- **Ordinary work and a saved plan at the same time**
  - Recommended: (a) take turns: one session at a time, on one branch at a time.
  - Answer: (a).
- **Who merges the plan's branch back, and when**
  - Recommended: (a) the box skill merges at its end, after `/handoff`, runs `make test`, and the librarian runs on the shared branch; on a conflict in code it stops and asks.
  - Answer: (a). The person asked whether the box is in essence ordinary Work Mode with git branches.
- **Is the box a new skill around `/work`, or `/work` itself**
  - Recommended: (a) a new skill that does the branch steps and calls `/work` with the saved plan's folder.
  - Answer: (a), agreed.
- **Where a Case of the saved plan built again is written**
  - Recommended: (a) into the saved plan's folder, its file and its ledger, by the two hooks taught to write there.
  - Answer: (a), agreed.
- **How much of this is built in this session**
  - Recommended: (b) a first part now — the branch made by `/carry`, the box skill, the merge back and the fence fix. The check against changed pages (Q4, Q9) is put off as a backlog item, and until then the box refuses a saved plan whose pages changed after the save.
  - Answer: (b), agreed.
- **Where the box writes its records when this session's own Cases were saved**
  - Recommended: (b) for now, the box runs only in a session with no Cases of its own. Its records go into the session's own folder, and Q5 (b) comes with the later part.
  - Answer: (b), agreed.

## History

- 2026-10-02 created · raw/2026-10-02/1202/ledger.md#case-591
- 2026-10-02 child decision-case-591.2 archived · cleanup
- 2026-10-02 child decision-case-591.5 archived · cleanup
- 2026-10-02 child decision-case-591.6 archived · cleanup
