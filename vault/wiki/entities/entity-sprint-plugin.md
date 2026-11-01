---
type: entity
kind: Leaf
purpose: "GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand"
status: draft
parent: "[[entity-sprint]]"
estimates: ["[[estimate-sprint-plugin-close-steps-run-from-the-line]]", "[[estimate-sprint-plugin-readme-describes-the-project]]", "[[estimate-sprint-plugin-pull-requests-reviewed-on-github]]", "[[estimate-sprint-plugin-ci-writes-a-clean-branch]]", "[[estimate-sprint-plugin-installs-as-a-plugin]]", "[[estimate-sprint-plugin-check-finds-no-bare-slug-link]]", "[[estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link]]"]
origin: raw/2026-10-10/1713/ledger.md#case-756.1
sprint: plugin
created: 2026-10-10
tags: [sprint, workflow]
---

## Purpose

GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand. Done when every Estimate of this page passes: the close steps run from the close line, the README describes the project, a pull request from another account is checked and reviewed on GitHub, CI writes the clean branch, and the clean branch installs as a plugin. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (rule-sprint-close).

## Milestones

### The clean branch

- [[rule-clean-branch]], [[estimate-sprint-plugin-ci-writes-a-clean-branch]] — CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint; what remains: the owner pushes `plugin` and a tag of the form `prod-x.y.z` on its last commit, and the CI run it starts is read by its Estimate; while a page with `core: true` that blocks the build stands — a `draft` one never `built`, or one with an Estimate `failed` — that run writes nothing to `prod`

### The plugin

- the clean version made into a Claude Code plugin
- [[rule-morph]] — the setup Case that the first `/hi` after `/guppi:install` puts before the opening of the first sprint; what remains: the setup skill, its step in `/hi` and in `/sprint-open`, the key of `guppi.toml` that marks the setup as done, the pass of the ledger hook for the setup Case while no sprint is open, and the clean version that ships that key unset
- the README on what the project is and what it is for and on its main parts and its use
- the close of `plugin` — `/sprint-close`, a session of its own

## Backlog

- The category set as data: the person sets the categories of a project, the development set entity, rule, estimate by default, and the harness holds them as data, so a changed set rewrites no rule; taken out of rule-morph (case 802); the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md
- The rest of Work Mode past the skill /work: the test of each Estimate written first and turned green, and the full model the person plans; taken out of rule-work-mode (case 962)
- The Spec box, its second part: a conserved Spec checked against the pages changed after it was conserved, a Case on such a page built again, ratified again and written into the folder of the conserved Spec, and a conserved Spec taken after other Cases of its session; taken out of rule-spec-box (case 962)

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
- 2026-10-14 updated: the milestone The clean branch says what remains after the fix of guppi ship for the example Case · [[decision-case-815]]
- 2026-10-15 defer by decision-case-805 superseded · [[decision-case-822.1]]
- 2026-10-15 updated: the question put off by decision-case-805 is decided by case 822: the passed Estimates of the shipped pages ship, and the tests ship · [[decision-case-822.1]]
- 2026-10-15 updated: the milestone line of rule-morph names what remains of the install step · [[decision-case-817]]
- 2026-10-15 updated: the milestone line of rule-morph names the setup Case, its order before the first sprint and what remains of it · [[decision-case-825]]
- 2026-10-15 deferred · [[decision-case-830]]
- 2026-10-16 defer by decision-case-830 superseded · [[decision-case-847]]
- 2026-10-16 updated: the milestone The clean branch names the tag form prod-x.y.z and the draft core pages that stop the run; the defer of decision-case-830 taken up · [[decision-case-847]]
- 2026-10-31 updated: the Backlog takes the open work of rule-work-mode and rule-spec-box as notes · [[decision-case-962]]
- 2026-11-01 estimate estimate-sprint-plugin-check-finds-no-bare-slug-link added · [[decision-case-973]]
- 2026-11-01 estimate estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link added · [[decision-case-978]]
- 2026-11-02 updated: the milestone The clean branch names the pages that block the build · [[decision-case-996.2]]
