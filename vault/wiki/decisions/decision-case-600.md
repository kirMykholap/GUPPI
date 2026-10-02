---
type: decision
case: "600"
status: current
update: ["[[insight-prespec-after-findings-loop-unruled]]"]
origin: raw/2026-10-02/2049/ledger.md#case-600
sprint: migration
created: 2026-10-02
tags: [workflow, session]
---

## Problem

The rules of `/pre-spec` now set the loop after its findings and rule out a costly second run, and the checks of both passed once. The Insight still stands `open` in the backlog only because no decision marked it `actioned`. The questions were whether every part of its cause is closed, which decision to name as the fix, and whether to close it now.

## Recommend

- **Is the cost part closed by removing the costly run?**
  - Recommended: (a) closed. No costly later run remains, since a later step is only the script check. Neither lesson concerned the first run.
  - Answer: agreed with the recommendation, (a).
- **Which decision should the note name as its fix?**
  - Recommended: (a) `decision-case-561.1`, the decision that wrote the loop and the later-run rule and so closed both failures.
  - Answer: agreed with the recommendation, (a).
- **Close the note now, or after the loop's check passes again?**
  - Recommended: (a) close now. The rule stands, its check passed once on real questions, and a recurrence reopens the note.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-02 created · raw/2026-10-02/2049/ledger.md#case-600
