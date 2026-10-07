---
type: decision
case: "722"
status: current
children: ["[[decision-case-722.1]]", "[[decision-case-722.2]]", "[[decision-case-722.3]]"]
origin: raw/2026-10-07/2114/ledger.md#case-722
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow, session, ledger]
---

## Problem

A part of a Case that a later build or a later Case left behind stays live. The store of the Case-file check keeps a sub-case that a Case built again no longer holds, and it clashes with the Cases that come after it. The Spec hook keeps a parent whose every sub-case is retired, and the schema says that a mark on a sub-case removes that sub-case alone.

## Recommend

- **The two leftover entries of last session**
  - Recommended: (a) leave them; nothing reads that store any more.
  - Answer: agreed, (a).
- **How the check leaves out a sub-case its rebuilt Case no longer holds**
  - Recommended: (a) leave it out when reading: the check leaves out each stored entry whose top-level Case file stands and holds no section under its id; nothing is deleted.
  - Answer: agreed, (a).
- **The pre-spec half of the same pattern**
  - Recommended: (a) this Case covers the store only.
  - Answer: (b), a second sub-case for the pre-spec half too. The frame then showed that `/pre-spec` no longer reports such a parent, and the question "Where the pre-spec half is fixed" replaced this one.
- **What checks that it works**
  - Recommended: (a) replace the Criterion of `estimate-case-check-sends-back-a-clash-with-another-case` with one more exception line.
  - Answer: agreed, (a).
- **Where the pre-spec half is fixed**
  - Recommended: (a) the Spec hook removes a parent whose every sub-case is retired, by `retired_whole`; the second sub-case changes `rule-spec-write`.
  - Answer: agreed, (a).
- **The sentence of the Case schema that the second sub-case makes false**
  - Recommended: (a) leave the sentence to the waiting item on the defers of Case 713.
  - Answer: (b), fix the sentence in this Case, in a third sub-case that carries the mark of the put-off decision.
- **The other fault put off on `rule-case-protocol`**
  - Recommended: (b) put the page off again for that fault, by a new defer line in this Case.
  - Answer: (b).
- **How the new build gets past the check while the first build stands in the plan**
  - Recommended: (a) the main agent first takes back the first build by a short Case, and the new build is shown after it.
  - Answer: neither option as such. The person agreed with the main agent's proposal: this Case stays as first ratified, its put-off line included, and Case 723 does not touch the sentence on a Frontier line closed again by the superseding Case.
- **Change**
  - Asked: the person dropped the change that built this Case again without the put-off line of Case 722.3.
  - Taken: the Case went back to its ratified form; the build under the number 724 was emptied.
- **Change**
  - Asked: the person had Case 722.1 built again, so that its Criterion also leaves out a Case that a supersedes mark on a decision line of the answer's own file names, as Case 725.2 sets it.
  - Taken: the exception line of 722.1 on marks now names a mark of the answer's own file beside a mark of the session's ledger; the number and the ledger lines of Case 722 stay.
- **Change**
  - Asked: at `/pre-spec`, the person agreed that 722.1 names a Case that a mark of the answer's own file names only as a pointer to `estimate-case-check-leaves-out-a-case-the-file-supersedes`, in its Criterion and its `purpose`, and the findings asked that a parent with a decision line of its own is not removed and that `context` names `estimate-prespec-catches-a-superseded-case`.
  - Taken: the exception line and the `purpose` of 722.1 point to that Estimate; 722.2 and 722.3 remove a parent only when no line of its own stays unretired, with a new exception line and test; `context` says why the Criterion of `estimate-prespec-catches-a-superseded-case` stands.

## History

- 2026-10-07 created · raw/2026-10-07/2114/ledger.md#case-722
