---
type: decision
case: "737"
status: archived
update: ["[[lesson-case-build-misses-the-example-a-changed-check-runs-over]]"]
origin: raw/2026-10-08/1547/ledger.md#case-737
sprint: migration
created: 2026-10-08
tags: [workflow, tests]
---

## Problem

The tags the agent needs to mark lessons on how `case-guppi` builds a Case and on the `/pre-spec` check do not exist, so the ledger hook refuses them and the lesson that asked for them carries only broad tags.

## Recommend

- **Should the two tags be added, and on which pages?**
  - Recommended: (a) add both, and tag only `lesson-case-build-misses-the-example-a-changed-check-runs-over`, the lesson that asked for them.
  - Answer: agreed, (a).
- **Change**
  - Asked: after the pre-spec findings, keep the target as it is, name `estimate-spec-write-reads-a-new-tag`, and say in `context` and `then` that the cascade of Case 736.1 archives the lesson in the same run and that the point of the Case is the declaration of the tags for later lessons and pages; no tags on rule pages.
  - Taken: `context` names that Estimate and the archiving, and the `then` line on the lesson says that the cascade archives it and `rule-cleanup` moves it.

## History

- 2026-10-08 created · raw/2026-10-08/1547/ledger.md#case-737
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
