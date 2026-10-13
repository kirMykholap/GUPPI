---
type: entity
kind: Leaf
purpose: "GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand"
status: draft
parent: "[[entity-sprint]]"
estimates: ["[[estimate-sprint-plugin-close-steps-run-from-the-line]]", "[[estimate-sprint-plugin-readme-describes-the-project]]", "[[estimate-sprint-plugin-pull-requests-reviewed-on-github]]", "[[estimate-sprint-plugin-ci-writes-a-clean-branch]]", "[[estimate-sprint-plugin-installs-as-a-plugin]]"]
deferred_by: ["[[decision-case-805]]"]
origin: raw/2026-10-10/1713/ledger.md#case-756.1
sprint: plugin
created: 2026-10-10
tags: [sprint, workflow]
---

## Purpose

GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand. Done when every Estimate of this page passes: the close steps run from the close line, the README describes the project, a pull request from another account is checked and reviewed on GitHub, CI writes the clean branch, and the clean branch installs as a plugin. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (rule-sprint-close).

## Milestones

### The clean branch

- [[rule-clean-branch]], [[estimate-sprint-plugin-ci-writes-a-clean-branch]] — CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint; what remains: once the librarian's run applies the rewording of the pages (case 809), the owner pushes a tag `prod-*` on a commit of `plugin`, and the CI run it starts is read by its Estimate

### The plugin

- the clean version made into a Claude Code plugin
- [[rule-morph]] — the install step that the first `/hi` of a new install runs
- the README on what the project is and what it is for and on its main parts and its use
- the close of `plugin` — `/sprint-close`, a session of its own

## Backlog

- The category set as data: the person sets the categories of a project, the development set entity, rule, estimate by default, and the harness holds them as data, so a changed set rewrites no rule; taken out of rule-morph (case 802); the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md

## Closed

- The sprint turn and GitHub: the repository on GitHub set up so that a pull request from another person is easy to review (case 794)

## History

- 2026-10-10 created · [[decision-case-756.1]]
- 2026-10-10 estimate estimate-sprint-plugin-close-steps-run-from-the-line added · [[decision-case-756.2]]
- 2026-10-10 estimate estimate-sprint-plugin-readme-describes-the-project added · [[decision-case-756.3]]
- 2026-10-10 estimate estimate-sprint-plugin-pull-requests-reviewed-on-github added · [[decision-case-756.4]]
- 2026-10-10 estimate estimate-sprint-plugin-ci-writes-a-clean-branch added · [[decision-case-756.5]]
- 2026-10-10 estimate estimate-sprint-plugin-installs-as-a-plugin added · [[decision-case-756.6]]
- 2026-10-11 updated: the note on the opening and the close of a sprint leaves the milestone The sprint turn and GitHub; the Purpose names only the close · [[decision-case-774]]
- 2026-10-13 updated: the milestone The sprint turn and GitHub closed — out of Milestones, named in Closed (case 794) · [[decision-case-794]]
- 2026-10-13 updated: the milestone The plugin names rule-morph, the install step; the Backlog takes the category set as data, out of rule-morph (case 802) · [[decision-case-802]]
- 2026-10-13 updated: the item of The clean branch links rule-clean-branch and the Estimate of the live run (case 804) · [[decision-case-804.7]]
- 2026-10-14 deferred · [[decision-case-805]]
- 2026-10-14 updated: the clean branch: guppi ship removes each bracket that holds a pointer; the pages are reworded by a Case of the next session (case 807.1) · [[decision-case-807.1]]
- 2026-10-14 updated: the milestone The clean branch says what remains after the rewording of the pages · [[decision-case-809]]
