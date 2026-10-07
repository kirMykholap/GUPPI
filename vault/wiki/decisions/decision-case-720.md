---
type: decision
case: "720"
status: current
defer: ["[[rule-case-check]]"]
origin: raw/2026-10-07/1804/ledger.md#case-720
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow, session]
---

## Context

At the `/pre-spec` of session 1804 the `case-guppi` of Case 713 first split the ratified Case 713 into 713.1 and 713.2, and the check of `rule-case-check` stored both in `adaptive-gathering-dewdrop.checked.json`; it then went back to the ratified text of 713 and built Case 719 to supersede it. The store kept 713.1 and 713.2, which no file and no plan holds and which have no decision line; `other_blocks` of `guppi/casecheck.py` counts them as other Cases of the session until a `{supersedes:case 713}` mark stands in the ledger, so the check refused the showing of 719 for pairs that only those entries hold. The person put the problem off to the next session.

## Problem

No Case of this session decides how the store of the Case-file check drops the entries of sub-cases that a Case built again no longer holds.

## Deferred

### [[rule-case-check]]

The store of the Case-file check keeps the sub-cases of a Case built again without them, and they clash with the Case that supersedes it; put off at the pre-spec of session 1804

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#case-720
