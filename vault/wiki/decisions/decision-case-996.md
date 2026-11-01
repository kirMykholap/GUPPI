---
type: decision
case: "996"
status: current
children: ["[[decision-case-996.1]]", "[[decision-case-996.2]]", "[[decision-case-996.3]]"]
origin: raw/2026-11-01/2227/ledger.md#case-996
sprint: plugin
created: 2026-11-01
tags: [ci, git, plugin, harness, workflow, sprint]
---

## Problem

A shipped page falls back to `draft` each time a Case adds a check to it, and the build writes nothing while any such page stands, so the tagged run may never write `prod` in this sprint.

## Recommend

- **What lets the tagged run write `prod` while harness pages stand draft**
  - Recommended: (c) block only on pages that were never finished.
  - Answer: the person asked instead to take `core: true` off the blocking pages and leave a backlog entry to fix them and give it back.
- **Which pages lose `core: true` so the tagged run can write `prod`**
  - Recommended: (c) no page loses the mark; block only on pages that were never finished.
  - Answer: (c); `prod` is not stripped.
- **How the build tells a page that was never finished**
  - Recommended: (a) by the History of the page.
  - Answer: agreed, (a).
- **Whether a failed check still blocks a page that was finished before**
  - Recommended: (a) a failed check blocks.
  - Answer: agreed, (a).
- **What lint keeps reporting**
  - Recommended: (a) lint reports only what blocks the build, by the one shared function.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) replace the promise of `estimate-clean-branch-refuses-a-draft-core-page`.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, how the clean version shows a page that ships as `draft`, since lint there would report it `draft while every Estimate is passed`; the person took the recommended answer, that the page stays `draft` and lint where the command `ship` is missing gives no such finding. The findings of `/pre-spec` also asked to fix the sentence of `rule-clean-branch` on a draft page that loses `core`, to give the cascade test a `draft_core` name, and to correct what Case 994 does to `rule-close`.
  - Taken: the new sub-case 996.3 replaces the Criterion of `estimate-lint-checks-the-statuses` and carries the task on `.guppi/guppi/lint.py` for that exemption; 996.1 adds it to the sentence of `rule-lint` and the `purpose` of that Estimate, rewords the sentence of `rule-clean-branch` to a page that blocks the build, names the cascade test, and `context` is corrected.

## History

- 2026-11-02 created · raw/2026-11-01/2227/ledger.md#case-996
