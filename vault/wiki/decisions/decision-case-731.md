---
type: decision
case: "731"
status: current
update: ["[[estimate-hi-writes-frontier]]"]
origin: raw/2026-10-08/0050/ledger.md#case-731
sprint: migration
created: 2026-10-08
tags: [session, harness, workflow]
---

## Problem

The `method` of `estimate-hi-writes-frontier` names a reading by the person without the words `by hand`, so `make lint` reports that the Estimate of a MOC names no `make <target>`.

## Recommend

- **How is the lint finding removed?**
  - Recommended: (a) put "by hand" back into the method; only the `method` field changes.
  - Answer: agreed, (a).
- **Which check proves the fix?**
  - Recommended: (a) no new check: `estimate-lint-checks-the-method` stands, and the `make lint` of the librarian's run shows the finding gone.
  - Answer: agreed, (a).
- **Is the gap that let the wording through closed too?**
  - Recommended: (a) leave it: this Case fixes only the one method.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/0050/ledger.md#case-731
