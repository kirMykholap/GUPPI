---
type: decision
case: "597"
status: archived
children: ["[[decision-case-597.1]]", "[[decision-case-597.2]]"]
origin: raw/2026-10-02/2049/ledger.md#case-597
sprint: migration
created: 2026-10-02
tags: [session, workflow, hooks, harness]
---

## Problem

The Plan Mode run of the onward hook stays silent after any refusal in the stretch. When the ledger hook refuses a line of the acknowledging reply, Plan Mode stops before `/pre-spec` or the exit, although nobody is needed. After a re-ratification, the reply that rewrites a refused line carries none of the Case's decision lines, so the run would judge the Case still out. The decision of case 575 on that judgment stands open.

## Recommend

- **What guards the Plan Mode run against a loop**
  - Recommended: (a) the Retro judgment. The run speaks once per stretch and once more after each reply the ledger hook refused. The flag and refusals of other hooks neither silence it nor send it on. It reads the refusals with the function the Retro fix adds to `guppi/ledger.py`. An error of its own exits 2 at most once a stretch.
  - Answer: agreed with the recommendation, (a).
- **How the hook judges that a rebuilt Case is still out**
  - Recommended: (a) read the decisions of the whole stretch. The decision lines of every reply since the person's last message count, each at the time of its record in the transcript. The defer of case 575 is closed by this change.
  - Answer: agreed with the recommendation, (a).
- **The line in the Retro fix that says the Plan Mode run keeps the flag**
  - Recommended: (a) rebuild the Retro fix. Case 596 goes back to its `case-guppi`, and the line says that `--plan` keeps its own judgment, set by `rule-prespec-onward`. This Case does not touch that Estimate.
  - Answer: agreed with the recommendation, (a).
- **How the change is checked: one promise or two**
  - Recommended: (a) two sub-cases. 597.1 replaces the promise of `estimate-prespec-onward-sends-the-agent-on`. 597.2 creates `estimate-prespec-onward-reads-the-decisions-of-the-session`. Each has its own tests and its own check by hand.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-02 created · raw/2026-10-02/2049/ledger.md#case-597
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
