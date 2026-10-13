---
type: decision
case: "795"
status: current
children: ["[[decision-case-795.1]]", "[[decision-case-795.2]]"]
origin: raw/2026-10-13/1426/ledger.md#case-795
sprint: plugin
created: 2026-10-13
tags: [github, ci, git, harness, workflow, schema]
---

## Problem

`rule-github-repository` stands with no link from any page, so lint prints it as an orphan. The check before ratification lets a new single rule through with no parent, though the librarian's script marks it incomplete and an Estimate promises the finding.

## Recommend

- **Which page should be the parent of `rule-github-repository`?**
  - Recommended: (a) `rule-harness`, with its Purpose sentence on its members changed.
  - Answer: none of the options fits. The rules of the GUPPI repository and the rules of the repository of someone who uses GUPPI can differ; this is more like an entity, the GUPPI repository, which has its own rules. Replaced by the question **Where should the entity of the GUPPI repository stand?**
- **Should this Case also make the check before ratification report a missing parent?**
  - Recommended: (b) fix the page, and close the gap in a second sub-case.
  - Answer: (b).
- **How is the fix of the page confirmed?**
  - Recommended: (a) the librarian's `make lint`, with no Estimate.
  - Answer: (a).
- **Where should the entity of the GUPPI repository stand?**
  - Recommended: (a) a new entity `entity-guppi-repository` under `entity-guppi`, which `rule-github-repository` names in `applies_to`.
  - Answer: agreed, (a).
- **Does `rule-github-repository` still need a parent rule page?**
  - Recommended: (a) no parent rule; the link to the entity is enough.
  - Answer: agreed, (a).
- **What should the check before ratification report for a new single rule?**
  - Recommended: (a) report a single rule with neither a parent nor an entity link, by one shared function.
  - Answer: agreed, (a).

## History

- 2026-10-13 created · raw/2026-10-13/1426/ledger.md#case-795
