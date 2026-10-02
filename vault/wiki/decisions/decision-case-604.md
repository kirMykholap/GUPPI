---
type: decision
case: "604"
status: current
update: ["[[rule-prespec-onward]]", "[[estimate-prespec-onward-reads-the-decisions-of-the-session]]"]
origin: raw/2026-10-02/2300/ledger.md#case-604
sprint: migration
created: 2026-10-02
tags: [session, workflow, hooks, harness]
---

## Problem

When a Case is ratified again with the decision lines the ledger already holds, `guppi onward --plan` sees that re-ratification only until the person's next message. After that, the Case counts as out for the rest of the session. The hook then stays silent at the last ratification, and the person has to send the agent on by hand.

## Recommend

- **How far back the hook reads the replies for decision lines**
  - Recommended: (a) every reply of the main agent in the transcript, each counted at the time of its record, the way the ledger hook reads it.
  - Answer: agreed with the recommendation, (a).
- **What happens to the Estimate that checks the reading of the decision lines**
  - Recommended: (a) replace the Criterion, set anew the `purpose` and `method`, and rename it `estimate-prespec-onward-reads-the-decisions-of-the-session`.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-03 created · raw/2026-10-02/2300/ledger.md#case-604
