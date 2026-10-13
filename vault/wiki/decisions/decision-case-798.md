---
type: decision
case: "798"
status: current
children: ["[[decision-case-798.1]]", "[[decision-case-798.2]]"]
origin: raw/2026-10-13/1426/ledger.md#case-798
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness, case-build, ci, github, prespec]
---

## Problem

`case-guppi` can recommend an option that breaks the rule governing what the option changes, or that rests on a check that is red today. It reads the governing rule only on an item that reports a defect, and it never reads the last output of a check. A Case built on such a recommendation has to be replaced.

## Recommend

- **What must `case-guppi` read before it recommends an option?**
  - Recommended: (b) on every item, the rule that governs what each option changes, and, where an option rests on whether a check passes, what that check printed at its last run, as the brief reports it; `context` names both.
  - Answer: agreed, (b).
- **What happens to the group page of the two lessons?**
  - Recommended: (a) this Case sets the group page `actioned`.
  - Answer: agreed, (a).
- **How is the new instruction checked?**
  - Recommended: (a) two parts: widen the Criterion of the existing check to every item, and add a new check for the last output of a check.
  - Answer: agreed, (a).
- **When is each check read?**
  - Recommended: (a) at this session's Retro, on the new instruction text.
  - Answer: agreed, (a).
- **What if the brief shows no output for the check an option rests on?**
  - Recommended: (a) look in the brief and the handoff of the last session; where neither shows it, the `**After:**` line of the option and `context` say so, and the option may still be recommended.
  - Answer: agreed, (a).
- **Change**
  - Asked: by a finding of `/pre-spec`, the person agreed that `case-guppi` reads the last output of a check only in the brief, the `make lint` lines under `## Flags` and `make test` under `## Readings at the close`, since the handoff of the last session is usually moved to the archive; where the brief shows none, the option and `context` say so.
  - Taken: Case 798.2 drops the handoff from its sentence, `given`, `then` and the `purpose` of its Estimate.
- **Change**
  - Asked: by a finding of `/pre-spec`, the sentence of Case 798.2 must not contradict the sentence of Case 797.1 where another Case of the session changes the check or the pages it reads.
  - Taken: the sentence and the `then` of Case 798.2 say that, in that case, the option is judged by the state at the moment the check runs, as Case 797.1 sets it; `context` no longer claims that the last output is that state.

## History

- 2026-10-13 created · raw/2026-10-13/1426/ledger.md#case-798
