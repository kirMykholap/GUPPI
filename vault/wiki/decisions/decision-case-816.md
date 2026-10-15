---
type: decision
case: "816"
status: current
children: ["[[decision-case-816.1]]", "[[decision-case-816.2]]"]
origin: raw/2026-10-15/0553/ledger.md#case-816
sprint: plugin
created: 2026-10-15
tags: [ci, plugin, git, sprint]
---

## Problem

The branch `prod` holds the clean version, but Claude Code cannot add it as a catalogue or install a plugin from it, and nothing checks in CI that it is a valid plugin.

## Recommend

- **Where the two files come from**
  - Recommended: (c) a template folder `plugin/` on `main` holds both files with no version; `guppi ship` copies them into `.claude-plugin/` and adds the version.
  - Answer: (c).
- **Where the catalogue points**
  - Recommended: (a) both files on `prod`; the source of the plugin entry is the branch itself, `./`.
  - Answer: (a).
- **Whether the plugin has a version**
  - Recommended: (a) no `version`.
  - Answer: set the current version to 0.2 and take the version from the tag, written as x.y or with more levels where needed.
- **The names**
  - Recommended: (a) plugin `guppi`, catalogue `guppi`, owner `kirMykholap`.
  - Answer: (b) plugin `guppi`, catalogue `guppi-marketplace`.
- **How CI checks the files**
  - Recommended: (c) both: `claude plugin validate` on the clean folder in `prod.yml` before the commit, and our own test in `make test`.
  - Answer: (c).
- **What checks that this is done**
  - Recommended: (a) a new Estimate on `rule-clean-branch`: after a tag push the CI plugin check passes and `prod` is written; by hand, in an empty project, adding the catalogue and installing `guppi` end with no error.
  - Answer: agreed, (a).
- **Which page records it**
  - Recommended: (a) update `rule-clean-branch`.
  - Answer: agreed, (a).
- **The form of the version**
  - Recommended: (b) tags `prod-x.y` or deeper; the manifest fills in the missing parts up to three.
  - Answer: take three parts at once: the tag itself is `prod-x.y.z`.
- **The version of a run without a version tag**
  - Recommended: (a) the version is the newest `prod-x.y.z` tag in the history of the built commit; whole-number tags are ignored; with no such tag `guppi ship` stops and nothing reaches `prod`.
  - Answer: (a).
- **The sprint's CI Estimate after the tag change**
  - Recommended: (a) this Case replaces that Criterion with the same promise for a three-part tag and adds that `guppi ship` stops when no such tag stands in the history.
  - Answer: agreed, (a).
- **What the sprint's CI Estimate reads while the build refuses draft pages**
  - Recommended: (a) keep the promise of a written `prod`, and add that the run writes nothing while a draft page with `core: true` stands; the tests check the version now, the run is read after the first run that writes `prod`, and the person decides its status at the close when none comes.
  - Answer: agreed, (a).
- **Change**
  - Asked: build the Case again after Case 821, under which a run of `prod.yml` writes nothing while `rule-skill-hi`, `rule-work-mode` and `entity-sprint` stand `draft` with `core: true`.
  - Taken: the `method` of `estimate-clean-branch-installs-as-a-plugin` waits for the first run that writes `prod`; the push of the tag moves to Case 816.2 as the placing of `prod-0.2.0` after the Work Mode; the Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` says that a sample is no reference and that the run writes nothing while such a page stands, and its `method` reads the tests now and the run after the first one that writes `prod`.
- **Change**
  - Asked: at `/pre-spec`, the person chose that every Estimate that waits for a run that writes `prod` is read from a local copy that `guppi ship --allow-draft <folder>` writes, and that `prod` is built once every page with `core: true` is `built`; the word "first" stands only for an event that has never happened.
  - Taken: `estimate-clean-branch-installs-as-a-plugin` reads `claude plugin validate` and the install on a local copy built with `--allow-draft`, that folder being the catalogue, before the close of `plugin`, and reads the CI step from the text of the workflow; the `method` of `estimate-sprint-plugin-ci-writes-a-clean-branch` waits for a run that writes `prod`, not the first one, as ratified.

## History

- 2026-10-15 created · raw/2026-10-15/0553/ledger.md#case-816
