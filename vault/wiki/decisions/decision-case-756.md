---
type: decision
case: "756"
status: current
children: ["[[decision-case-756.1]]", "[[decision-case-756.2]]", "[[decision-case-756.3]]", "[[decision-case-756.4]]", "[[decision-case-756.5]]", "[[decision-case-756.6]]"]
origin: raw/2026-10-10/1713/ledger.md#case-756
sprint: plugin
created: 2026-10-10
tags: [sprint, workflow, readme, github, git, ci, plugin]
---

## Problem

No sprint is open, and the session can ratify no other Case until a sprint page stands. The next sprint needs its id, its goal, its Definition of done, its milestones and an answer on the backlog.

## Recommend

- **What is the goal of the sprint?**
  - Recommended: (a) your own goal; failing one, (b) settle what `migration` left.
  - Answer: (a), the sprint's own goals: make sure the opening and the close of a sprint work correctly and fix every flaw; write the final README on the main parts of the project, why it is needed and how to use it; connect GitHub and set it up so that pull requests from other people are easy to review; set up CI/CD so that a branch of its own holds a clean version of the project, with no case references in its texts and a clean Frontier, sprint and the like; that clean version becomes the Claude plugin. The rest comes as the work goes.
- **Do you take any backlog item into the sprint?**
  - Recommended: (a) take none now.
  - Answer: (a), nothing now; to be thought about later.
- **What is the id of the sprint?**
  - Recommended: (a) `plugin`.
  - Answer: agreed, (a).
- **How is the goal written in one sentence?**
  - Recommended: (a) the whole list in one sentence.
  - Answer: agreed, (a).
- **Which conditions make the Definition of done?**
  - Recommended: (a) five conditions, one per line of the list.
  - Answer: agreed, (a).
- **How are the milestones cut?**
  - Recommended: (b) three milestones in the order of the work.
  - Answer: agreed, (b).
- **When is the condition on the sprint turn read?**
  - Recommended: (a) read the steps up to Work Mode; the archive run stays with the check of the close rule.
  - Answer: agreed, (a).
- **Change**
  - Asked: pre-spec found that the methods of Case 756.2 to Case 756.6 wait for a later session against case 670.4; the person agreed to name in `context` where the exception for a sprint page stands and its precedent.
  - Taken: `context` names `rule-sprint`, `entity-sprint` and the reading of `estimate-sprint-migration-merges` in session 1555.
- **Change**
  - Asked: pre-spec found that the `then` of Case 756.2 signs again the steps that `estimate-skill-sprint-close-leads-the-closing-session` and `estimate-sprint-close-takes-the-readings-in-groups` hold; the person agreed to keep only what is new.
  - Taken: the `then` of Case 756.2 holds only that no step is done or fixed by hand, and names the two Estimates for the rest.
- **Change**
  - Asked: pre-spec found that the alias of the new tag `ci` would also point at the tag `case-build`; the person agreed to another alias.
  - Taken: the aliases of `ci` are CI, CI/CD and continuous integration in Russian.
- **Change**
  - Asked: pre-spec found that `context` and Case 756.2 say a reading of `estimate-sprint-close-runs-in-the-librarian-run` comes at the close of `plugin`, and none is due; the person chose (a), keep that Estimate as it stands and correct the text.
  - Taken: `context` and the `－` line of Case 756.2 say that the run was read `passed` at the close of `migration` and that `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` holds the move of the pages.

## History

- 2026-10-10 created · raw/2026-10-10/1713/ledger.md#case-756
