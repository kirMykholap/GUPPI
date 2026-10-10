---
type: decision
case: "690"
status: archived
children: ["[[decision-case-690.1]]", "[[decision-case-690.2]]", "[[decision-case-690.3]]"]
origin: raw/2026-10-06/0104/ledger.md#case-690
sprint: migration
created: 2026-10-06
tags: [session, workflow, harness, ledger, tests]
---

## Problem

A fact the main agent writes into a dispatch prompt enters a Case unchecked, and the reply that acknowledges a ratification can tell the person that a change of a rendered harness file already runs in the session, while it changes only at the librarian's render.

## Recommend

- **A fact in the prompt that sends out a Case build**
  - Recommended: (a) the builder's frame says that a fact the prompt states, apart from the person's words, enters a Case only after the builder reads it at its source, and a fact it cannot read stays out.
  - Answer: agreed, (a).
- **A ratified change claimed to work before the render**
  - Recommended: (a) the paragraph `Changes:` of the acknowledging reply says that a change to a file rendered from a Rule page takes effect at the librarian's render, after the session, and the reply claims no new behaviour for the rest of the session.
  - Answer: agreed, (a).
- **What checks the two fixes**
  - Recommended: (a) two new Estimates, one per fix, each read at the Retro of this session from the new text in the Spec; the two existing Estimates stand.
  - Answer: agreed, (a).
- **What becomes of the backlog item after this Case**
  - Recommended: (a) marked as dealt with by this Case; it leaves the backlog and its two lessons are archived.
  - Answer: agreed, (a).

## History

- 2026-10-06 created · raw/2026-10-06/0104/ledger.md#case-690
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
