---
type: decision
case: "552"
status: archived
children: ["[[decision-case-552.1]]", "[[decision-case-552.2]]", "[[decision-case-552.3]]", "[[decision-case-552.4]]"]
origin: raw/2026-09-30/1736/ledger.md#case-552
sprint: migration
created: 2026-09-30
tags: [session, hooks, harness, ledger, workflow]
---

## Problem

An estimate or lesson line with a space between its brackets made `parse_line` raise instead of return. The ledger hook swallowed the error and exited 0, so the line and every later line of the session went unwritten, and nobody was told. The question was how `parse_line` reads such a line, what the hook does with a line it cannot read, how the hook reports its own error, and how these promises are recorded.

## Recommend

- **How the promise of the crash exit is recorded**
  Recommended: (a) a new Estimate of `rule-ledger-write` for the crash exit; `estimate-ledger-write-lifts` keeps its text.
  Answer: (a) a new Estimate.
- **Change**
  Asked: correct the facts of `context`: the full list of Grep hits, and the ledger as it stands after the code of 552.1 was built and the waiting lines were written.
  Taken: `context` names the three missing hits and says that none of them is made false. It tells the failure in the past tense, and it says that the code of 552.1 was built before the Spec, that the hook wrote the 20 waiting lines at 19:47:50 with the line with the space at line 29 and its corrected copy at line 30, and that `guppi/ledger.py` is unchanged.

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#case-552
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
