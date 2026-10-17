---
type: entity
kind: Leaf
purpose: The repository of GUPPI on GitHub, with rules of its own that a repository of another person who uses GUPPI need not share
status: built
parent: "[[entity-guppi]]"
estimates: ["[[estimate-guppi-repository-remote-on-github]]", "[[estimate-guppi-repository-keeps-the-development-project]]", "[[estimate-guppi-repository-stops-in-the-merge-tasks]]"]
rules: ["[[rule-clean-branch]]", "[[rule-github-repository]]"]
origin: raw/2026-10-13/1426/ledger.md#case-795.1
sprint: plugin
created: 2026-10-13
tags: [github, ci, git]
---

## Purpose

The repository of GUPPI on GitHub, as a thing of its own. Its rules are `rule-github-repository` — the rulesets on `main` and `prod`, the workflow of checks and the approval of the runs of an outside contributor — and `rule-clean-branch`, the workflow that writes the clean version of GUPPI to `prod`; each names this page in `applies_to` (case 804). A person who uses GUPPI keeps a repository of their own, whose rules may differ, so these rules belong to this repository and not to GUPPI as a whole (case 795.1).

## History

- 2026-10-13 created · [[decision-case-795.1]]
- 2026-10-13 rules: [rule-github-repository] · cascade
- 2026-10-13 updated: its rules name rule-clean-branch beside rule-github-repository (case 804) · [[decision-case-804.6]]
- 2026-10-13 rules: [rule-clean-branch, rule-github-repository] · cascade
- 2026-10-17 estimate estimate-guppi-repository-remote-on-github added · [[decision-case-880.7]]
- 2026-10-17 estimate estimate-guppi-repository-keeps-the-development-project added · [[decision-case-880.9]]
- 2026-10-17 estimate estimate-guppi-repository-stops-in-the-merge-tasks added · [[decision-case-880.20]]
- 2026-10-17 status: draft → built · cascade
