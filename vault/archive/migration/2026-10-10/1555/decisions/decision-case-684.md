---
type: decision
case: "684"
status: archived
children: ["[[decision-case-684.1]]", "[[decision-case-684.2]]"]
origin: raw/2026-10-05/2249/ledger.md#case-684
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness]
---

## Problem

When the person takes up several Frontier items in one answer, nothing tells the main agent to wait for every builder and show the questions and the Cases together. So it shows each answer alone as it arrives, and the prompt of each builder names none of the other Cases of the batch.

## Recommend

- **When does the batch form apply?**
  - Recommended: (a) when the person's one answer takes up two or more Frontier items; an item taken up alone is still shown alone.
  - Answer: agreed, (a).
- **Where does the main agent's question about changing another Case go in a batch?**
  - Recommended: (a) it joins the shared list of questions, numbered under the Case that raised it, before any Case is shown; on a yes the other Case joins the batch.
  - Answer: agreed, (a).
- **Does only the page enforce the batch form, or does a hook also enforce it?**
  - Recommended: (a) only the page; no code changes.
  - Answer: agreed, (a).
- **Which check says the change is done?**
  - Recommended: (a) a new Estimate, `estimate-orchestration-signs-items-taken-together`, beside the existing check, which stands.
  - Answer: agreed, (a).
- **How is the check read?**
  - Recommended: (a) at Retro of this session, this session's own batch read in the transcript against the check.
  - Answer: agreed, (a).
- **Change**
  - Asked: after the ratification of Case 681, the person asked that the reading try the next two items taken up side by side, and agreed to the items for Cases 682 and 683.
  - Taken: the `method` of `estimate-orchestration-signs-items-taken-together` now reads, at Retro of this session, the batch of Cases 682 and 683 with Case 681 built again, not the batch of Cases 676 to 680; `context` says why.
- **Change**
  - Asked: at `/pre-spec`, a finding showed that the prompt of each builder of a batch names no other Case of the batch, and the person chose to widen the Case so that it does.
  - Taken: Case 684.2 changes the sentence of `## Who builds a Case` on the dispatch, and replaces the Criterion, `purpose` and `method` of `estimate-orchestration-names-related-cases-in-the-dispatch`, read at Retro of this session over the same batch; the Case is built again as Case 684 with two sub-cases.

## History

- 2026-10-06 created · raw/2026-10-05/2249/ledger.md#case-684
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
