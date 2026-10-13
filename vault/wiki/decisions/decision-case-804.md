---
type: decision
case: "804"
status: current
children: ["[[decision-case-804.1]]", "[[decision-case-804.2]]", "[[decision-case-804.3]]", "[[decision-case-804.4]]", "[[decision-case-804.5]]", "[[decision-case-804.6]]", "[[decision-case-804.7]]"]
origin: raw/2026-10-13/1753/ledger.md#case-804
sprint: plugin
created: 2026-10-13
tags: [ci, git, plugin, harness, render, schema, workflow, session, librarian, sprint, hooks, ledger, tests, github]
---

## Problem

Nothing builds the version of GUPPI that other people install. Every text points to this repository's decisions and sessions, nothing marks which pages belong to GUPPI itself, and the schemas and lint have no shape for a page that shipped.

## Recommend

- **What does the clean version hold?**
  - Recommended: (a) code, harness and rule pages, with history fields and links to pages left out removed; no Entity, Estimate, Lesson, Insight or Decision page, and no session records.
  - Answer: agreed, (a). The person asked whether the Entity page of the sprint as a kind should ship too, since it is part of how GUPPI works. A later question took that up.
- **How do the pointers to past decisions leave the text?**
  - Recommended: (a) a script removes them, and a check fails on the rest.
  - Answer: agreed, (a).
- **What starts a run, and from which branch?**
  - Recommended: (a) a push to `main`, plus a run by hand on any branch.
  - Answer: agreed, (a).
- **How does `prod` keep its history?**
  - Recommended: (a) one new commit per run, on top of the last one.
  - Answer: agreed, (a).
- **How does CI get the right to write `prod`?**
  - Recommended: (a) the built-in GitHub Actions account on the bypass list.
  - Answer: agreed, (a).
- **Which page sets the rule of the clean branch?**
  - Recommended: (a) a new rule page, `rule-clean-branch`.
  - Answer: agreed, (a).
- **Which Entity pages go into the clean version?**
  - Recommended: (a) the three pages that describe GUPPI as a tool: `entity-guppi`, `entity-sprint` and `entity-glossary`.
  - Answer: agreed, (a).
- **Do the rules that apply only to this repository ship?**
  - Recommended: (a) a rule that applies only to a page left out stays out.
  - Answer: agreed, (a). The person proposed an explicit page field, `core`, that tells the build which pages ship, so that a page can stay in `main` while it is tried live. The next question took it up.
- **Does each page carry an explicit flag that says it ships?**
  - Recommended: (a) an opt-in `core` field on Entity, Rule and Estimate pages.
  - Answer: agreed, (a).
- **What do shipped pages carry in place of their history fields?**
  - Recommended: (a) the copy writes neutral values, and the schema accepts them.
  - Answer: agreed, (a).
- **Do any Estimate pages ship?**
  - Recommended: (a) none now.
  - Answer: agreed, (a).
- **Which pages get `core` now, and how?**
  - Recommended: (a) all of them in this Case, in a sub-case of their own.
  - Answer: agreed, (a).
- **What happens to text the script cannot clean on the first run?**
  - Recommended: (a) a later Case of this sprint rewords them.
  - Answer: agreed, (a).
- **How does the Case split, and how is each part checked?**
  - Recommended: (a) four sub-cases, each with its own check.
  - Answer: agreed, (a).
- **Does this Case settle the put-off question on GUPPI's future shape?**
  - Recommended: (a) it stands open.
  - Answer: agreed, (a).
- **What else does the check refuse in the copy?**
  - Recommended: (a) both a link in the text to a page left out and a mention of a session fail the run.
  - Answer: agreed, (a).
- **How does the part on the schemas and lint split?**
  - Recommended: (a) four sub-cases, each replacing one existing Criterion, and no new Estimate.
  - Answer: agreed, (a).
- **Does the copy carry this project's `guppi.toml`?**
  - Recommended: (a) the copy leaves out `guppi.toml`.
  - Answer: agreed, (a).
- **Where does the list of leftovers for the pages come from?**
  - Recommended: (a) code and harness from Work Mode, pages from the first run on GitHub.
  - Answer: agreed, (a).
- **Do the Estimates of the shipped rules ship after all?**
  - Recommended: (a) no Estimate ships, and the schema of rules says why.
  - Answer: agreed, (a): let us try it that way.
- **When does the milestone The clean branch count as done?**
  - Recommended: (a) the item links the rule and the sprint's check of the live run.
  - Answer: agreed, (a).
- **How does the workflow get the right to write `prod`?**
  - Recommended: (a) a deploy key on the bypass list.
  - Answer: agreed, (a); the person asked what to do, and the steps stand as `stop:` tasks of 804.7.
- **Change**
  - Asked: at pre-spec, the Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` names that `prod` holds exactly the pages with `core: true`, so that the marks of 804.5 are checked.
  - Taken: 804.7 adds that line to the Criterion, and the `context` names it.
- **Change**
  - Asked: at pre-spec, a push of a tag `prod-*` on a commit of `plugin` starts the run in place of a run by hand; a push to `main` still starts it, and that line is checked by reading the `on:` block of the workflow.
  - Taken: the `when` and `then` of 804.7, the `method` of its Estimate, the workflow task and the Purpose of `rule-clean-branch` say so.

## History

- 2026-10-13 created · raw/2026-10-13/1753/ledger.md#case-804
