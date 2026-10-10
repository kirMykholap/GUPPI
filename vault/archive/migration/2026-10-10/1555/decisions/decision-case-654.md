---
type: decision
case: "654"
status: archived
update: ["[[estimate-synthesis-clusters]]"]
origin: raw/2026-10-05/1343/ledger.md#case-654
sprint: migration
created: 2026-10-05
tags: [harness, workflow, librarian]
---

## Problem

The Criterion of `estimate-synthesis-clusters` asks the librarian to name in its report every lesson page it reads at synthesis. The frame of the librarian and `estimate-documentation-completes` say a page read for anything but a judgment is not named. The check fails a run that kept its frame.

## Recommend

- **How the clash between the check and the librarian's instructions is settled**
  - Recommended: (a) narrow the check: name only a page whose text is read to judge a shared cause, a lesson's Trigger and Root cause or an Insight's Pattern; a read of frontmatter fields alone is not named; only the Criterion of `estimate-synthesis-clusters` changes.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/1343/ledger.md#case-654
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
