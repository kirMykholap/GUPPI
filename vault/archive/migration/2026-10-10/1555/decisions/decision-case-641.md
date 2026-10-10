---
type: decision
case: "641"
status: archived
update: ["[[estimate-session-phases-in-order]]"]
origin: raw/2026-10-05/0109/ledger.md#case-641
sprint: migration
created: 2026-10-05
tags: [session, workflow]
---

## Problem

The `method` of `estimate-session-phases-in-order` is a reading by hand alone. Now that `estimate-session-start-context` is checked by a test target only, `make lint` reports the MOC's Estimate on every run. Something must clear the finding without weakening the rule that stops a reading by hand on a MOC from hiding its children's pipelines.

## Recommend

- **How should the finding on the session's Estimate be cleared?**
  - Recommended: (a) a new `make test-session` target that runs the tests of each phase that has them, named first in the method of `estimate-session-phases-in-order` before the same reading by hand; the rule of lint, its tests and the promise of the Estimate do not change.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/0109/ledger.md#case-641
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
