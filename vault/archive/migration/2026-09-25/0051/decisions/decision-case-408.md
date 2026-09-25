---
type: decision
case: "408"
status: archived
defer: ["[[rule-frame-check]]"]
superseded_by: ["[[decision-case-416]]"]
origin: raw/2026-09-24/2214/ledger.md#case-408
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Context

Case 403 deferred the question: whether `frame-guppi` pays, judged by the contradictions it finds against its tokens and time. In session 2214 it was dispatched three times — twice for Case 406, once for Case 407. It found no contradiction for Case 406 and one for Case 407: the circular import between `guppi/prespec.py` and `guppi/ratified.py`, which would have broken the code of Cases 407.2 and 407.4 at the first load. The dispatch for Case 407 cost about 160 thousand tokens and six minutes. The pre-spec of the same session then found in Case 407 contradictions that `frame-guppi` had not reported, with the frame it had read. The person chose to spend the rest of the session on Work Mode.

## Problem

Keep `frame-guppi` or roll it back: decided in a later session, with the data of sessions 1916 and 2214.

## Deferred

### [[rule-frame-check]]

Whether frame-guppi pays — the contradictions it finds against its tokens and time, with the dispatches of sessions 1916 and 2214; rolled back by a Case if it does not

## History

- 2026-09-25 created · raw/2026-09-24/2214/ledger.md#case-408
- 2026-09-25 superseded by decision-case-416 · [[decision-case-416]]
- 2026-09-25 archived · superseded
- 2026-09-25 archived · cleanup
