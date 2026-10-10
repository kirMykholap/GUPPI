---
type: decision
case: "773"
status: current
update: ["[[estimate-generate-writes-the-decision-page]]"]
origin: raw/2026-10-10/2350/ledger.md#case-773
sprint: plugin
created: 2026-10-10
tags: [harness, workflow, ledger]
---

## Problem

`guppi generate` writes the History line `superseded by` a second time, and a second line in `vault/wiki/log.md`, when one record supersedes an earlier page that an earlier step of the same record already marked, such as a sub-case whose parent the same line supersedes.

## Recommend

- **How should the doubled line be prevented?**
  - Recommended: (a) write the line only when the name is new; one helper holds the check and both steps call it; a test supersedes a parent and one of its sub-cases in one line.
  - Answer: agreed, (a).
- **What about the two doubled lines already written?**
  - Recommended: (a) leave them as the record of that run.
  - Answer: agreed, (a).
- **Which check confirms the fix?**
  - Recommended: (b) replace the Criterion of `estimate-generate-writes-the-decision-page` whole, its line made explicit for a page marked earlier in the same run, so it goes `pending` and the Retro of this session reads it again.
  - Answer: agreed, (b).

## History

- 2026-10-11 created · raw/2026-10-10/2350/ledger.md#case-773
