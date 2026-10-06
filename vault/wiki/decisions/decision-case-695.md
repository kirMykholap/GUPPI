---
type: decision
case: "695"
status: current
children: ["[[decision-case-695.1]]", "[[decision-case-695.2]]"]
origin: raw/2026-10-06/1448/ledger.md#case-695
sprint: migration
created: 2026-10-06
tags: [session, hooks, harness, ledger, workflow, render]
---

## Problem

A line of a `LEDGER` block whose opening is broken is no record, and the hook drops it with no message, so a reading or a lesson can be lost while the agent believes it was written.

## Recommend

- **Which lines in a LEDGER block are refused aloud**
  - Recommended: (b) every non-blank line inside a `LEDGER` block that does not open with `- decision[`, `- estimate[` or `- lesson[`; blank lines and blocks with another tag or none stay as now.
  - Answer: agreed, (b).
- **Which replies the hook tells about**
  - Recommended: (a) as for a line the grammar cannot read: told only when it stands in the reply just finished, a line of an earlier text skipped silently.
  - Answer: agreed, (a).
- **The message and the check that proves it**
  - Recommended: (b) its own stderr line, which names the three openings, and a new Estimate on `rule-ledger-write`; the passed Estimate stays as it is.
  - Answer: agreed, (b).
- **What the reply after Retro does with a refused line that is no record**
  - Recommended: (a) the Retro rule and `estimate-retro-runs-on-to-the-handoff` change: a refused record line is written again, a refused line that is no record is left out, and with nothing left the agent goes on to commit and call `/handoff`.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-06/1448/ledger.md#case-695
