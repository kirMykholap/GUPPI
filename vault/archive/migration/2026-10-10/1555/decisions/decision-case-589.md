---
type: decision
case: "589"
status: archived
children: ["[[decision-case-589.1]]", "[[decision-case-589.2]]"]
origin: raw/2026-10-02/1202/ledger.md#case-589
sprint: migration
created: 2026-10-02
tags: [harness, workflow, hooks, session]
---

## Problem

The language finding cannot tell a word written in the wrong language from a slug or a path in a code span. So for a documentation language not written in Latin script, it reports almost every Case. The question was where the fix is recorded, and what the check does with the letters inside a code span.

## Recommend

- **Where is the change recorded in the vault?**
  - Recommended: (b) no new rule. One sentence goes into the description of `/pre-spec` next to the language check, the promises of the two existing Estimates are rewritten whole, and the empty page `rule-prespec-script-skips-code-spans` is deleted, which closes the put-off item. The behaviour is one sentence about a check that already has its description and two Estimates.
  - Answer: Agreed: (b).
- **What does the check do with the letters inside a code span?**
  - Recommended: (b) inside a code span, accept Latin letters and judge all other letters as in prose. It solves the problem, a Russian word between backticks is still caught, and for English nothing changes.
  - Answer: Agreed: (b).

## History

- 2026-10-02 created · raw/2026-10-02/1202/ledger.md#case-589
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
