---
type: decision
case: "696"
status: archived
children: ["[[decision-case-696.1]]", "[[decision-case-696.2]]"]
origin: raw/2026-10-07/0211/ledger.md#case-696
sprint: migration
created: 2026-10-07
tags: [session, workflow, hooks, harness]
---

## Problem

Plan Mode stops where no person is needed. The hook of `rule-prespec-onward` stays silent for the rest of Plan Mode once a Case replaced under a new number counts as out. It also stays silent after the agent's answer with no `LEDGER` block to a reply that the ledger hook sent back. Before `/pre-spec`, it sends the agent on where the person may still want to speak.

## Recommend

- **A replaced Case keeps the hook silent**
  - Recommended: (a) the replacement mark settles it: a Case that a ratified line marks as replaced by `{supersedes:case N}` no longer counts as waiting, and the Criterion of `estimate-prespec-onward-reads-the-decisions-of-the-session` is replaced.
  - Answer: agreed, (a).
- **The answer to the ledger hook's question ends the run**
  - Recommended: (a) the hook speaks after that answer too: when the ledger hook sent back the reply that held the block, the hook also speaks at the end of the next reply, with or without a block, at most once after each reply sent back; the Criterion of `estimate-prespec-onward-sends-the-agent-on` is replaced.
  - Answer: agreed, (a).
- **The lesson names only the second cause**
  - Recommended: (a) leave the lesson as written; the `context` of this Case records the first cause.
  - Answer: agreed, (a).
- **Change**
  - Asked: a reply on a Frontier with no open line under `## Cases` should ask the person whether to go on, since the person had a question and had to cancel the call of an agent; the hook no longer sends the agent to `/pre-spec`, and the steps after `/pre-spec` stay automatic.
  - Taken: Case 696.2 drops the sending to `/pre-spec` from the hook, from `rule-prespec-onward` and from the Criterion of `estimate-prespec-onward-sends-the-agent-on`; before `/pre-spec` the hook stays silent, and after it the hook sends the agent on as before. What the reply asks is left to Case 697.
- **Change**
  - Asked: the findings of `/pre-spec`, which the person agreed to fix as proposed: reuse the judgment of a mark in `guppi/prespec.py` rather than write a second copy; count a parent as not out when each of its sub-cases is retired; before `/pre-spec`, let an error of the hook not send the reply back; keep Case 696.2 consistent with Case 697.2 on a reply with no `LEDGER` block after `/pre-spec`.
  - Taken: Case 696.1 imports `superseded_in_window` and `retired_by` of `guppi/prespec.py`, writes the judgment of a parent once in that module, and counts a parent whose every sub-case with a decision line is retired as not out. Case 696.2 sends the reply back on an error of its own only after `/pre-spec`, and its rule text says so. The `context` says why the reply with no `LEDGER` block after `/pre-spec` gets no reason.

## History

- 2026-10-07 created · raw/2026-10-07/0211/ledger.md#case-696
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
