---
type: decision
case: "670"
status: archived
children: ["[[decision-case-670.1]]", "[[decision-case-670.2]]", "[[decision-case-670.3]]", "[[decision-case-670.4]]", "[[decision-case-670.5]]", "[[decision-case-670.6]]", "[[decision-case-670.7]]"]
origin: raw/2026-10-05/1831/ledger.md#case-670
sprint: migration
created: 2026-10-05
tags: [harness, workflow, session, hooks, ledger, render]
---

## Problem

Every change of an Estimate leaves it `pending`. Its reading is barred in the session that made the change and waits for a live moment in another session, so each `/hi` pays to read the same Estimates again, and the list never empties.

## Recommend

- **When does the ledger hook let a reading of a changed Estimate through?**
  - Recommended: (a) from the opening of Retro, by the existing `retro` mark; before it the hook still refuses.
  - Answer: agreed, (a).
- **How does Retro read an Estimate of a rule whose text is rendered into a harness file?**
  - Recommended: (a) Retro reads the new text in the Spec against the Criterion; the render and `make lint` check the file, and a problem seen later is a lesson.
  - Answer: agreed, (a).
- **What happens to an Estimate whose method needs your word?**
  - Recommended: (a) the one exception: Retro leaves it under `## Ask the person`, and the next `/hi` asks it once, with no transcript.
  - Answer: agreed, (a).
- **What does `/hi` do with an old open reading whose method waits for a moment in another session?**
  - Recommended: (a) remove the transcript step: `/hi` takes only the readings it can run now, and any other open Estimate becomes one Cases line; the readings of the sprint migration's close stay as they are.
  - Answer: agreed, (a).
- **What makes sure Retro reads, or sets `failed`, each Estimate the session changed?**
  - Recommended: (b) Retro's text alone, with `/hi` as the net for a forgotten reading.
  - Answer: agreed, (b).
- **Does a check report a new method that waits for another session?**
  - Recommended: (a) pre-spec reports it in the Spec, by a predicate in `guppi/lint.py` that `guppi/prespec.py` imports; a method whose reading is the person's answer is the exception, and lint over the live pages stays as it is.
  - Answer: agreed, (a).
- **Change**
  - Asked: from the summary of Case 669, the main agent asked whether this Case should leave alone an Estimate whose `update` in this session sets its status itself and does not change its Criterion, so the fifteen of Case 669 stay `passed`; the person agreed, (a).
  - Taken: 670.2 neither reads nor sets `failed` an Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, nor one whose `update` names one part of the page alone.

## History

- 2026-10-05 created · raw/2026-10-05/1831/ledger.md#case-670
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
