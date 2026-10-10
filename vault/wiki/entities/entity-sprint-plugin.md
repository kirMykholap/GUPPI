---
type: entity
kind: Leaf
purpose: "GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand"
status: draft
parent: "[[entity-sprint]]"
estimates: ["[[estimate-sprint-plugin-close-steps-run-from-the-line]]", "[[estimate-sprint-plugin-readme-describes-the-project]]", "[[estimate-sprint-plugin-pull-requests-reviewed-on-github]]", "[[estimate-sprint-plugin-ci-writes-a-clean-branch]]", "[[estimate-sprint-plugin-installs-as-a-plugin]]"]
origin: raw/2026-10-10/1713/ledger.md#case-756.1
sprint: plugin
created: 2026-10-10
tags: [sprint, workflow]
---

## Purpose

GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand. Done when every Estimate of this page passes: the close steps run from the close line, the README describes the project, a pull request from another account is checked and reviewed on GitHub, CI writes the clean branch, and the clean branch installs as a plugin. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (rule-sprint-close).

## Milestones

### The sprint turn and GitHub

- the repository on GitHub set up so that a pull request from another person is easy to review

### The clean branch

- CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint

### The plugin

- the clean version made into a Claude Code plugin
- the README on what the project is and what it is for and on its main parts and its use
- the close of `plugin` — `/sprint-close`, a session of its own

## History

- 2026-10-10 created · [[decision-case-756.1]]
- 2026-10-10 estimate estimate-sprint-plugin-close-steps-run-from-the-line added · [[decision-case-756.2]]
- 2026-10-10 estimate estimate-sprint-plugin-readme-describes-the-project added · [[decision-case-756.3]]
- 2026-10-10 estimate estimate-sprint-plugin-pull-requests-reviewed-on-github added · [[decision-case-756.4]]
- 2026-10-10 estimate estimate-sprint-plugin-ci-writes-a-clean-branch added · [[decision-case-756.5]]
- 2026-10-10 estimate estimate-sprint-plugin-installs-as-a-plugin added · [[decision-case-756.6]]
- 2026-10-11 updated: the note on the opening and the close of a sprint leaves the milestone The sprint turn and GitHub; the Purpose names only the close · [[decision-case-774]]
