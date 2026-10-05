---
type: decision
case: "644"
status: current
children: ["[[decision-case-644.1]]", "[[decision-case-644.2]]", "[[decision-case-644.3]]", "[[decision-case-644.4]]", "[[decision-case-644.5]]", "[[decision-case-644.6]]", "[[decision-case-644.7]]", "[[decision-case-644.8]]"]
origin: raw/2026-10-05/0311/ledger.md#case-644
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow, session]
---

## Problem

The Spec hook does nothing on a reply that carries `stop_hook_active`. Claude Code keeps the flag set on every reply after a refusal until the person writes again. So a Case refused at the reply that acknowledges it, then fixed and repeated in the next reply as the hook's own advice asks, is never written until the person sends one more message and sees the Case once more. The question was whether the rules describe this gap or the hook closes it, how it then avoids a loop, how that is checked, and what else changes.

## Recommend

- **Describe the gap or write on the reply that answers a refusal**
  - Recommended: (b) the hook writes there too: it writes, removes and checks Cases whether or not the flag is set, as the ledger hook already does, and keeps itself from looping by its own refusals in the transcript since the person's last message; the six Estimates of `rule-spec-write` get their Criteria replaced.
  - Answer: agreed, (b).
- **How the hook keeps itself from looping**
  - Recommended: (a) each refusal once until the person writes: a refusal whose text already stands in one of the hook's own refusals since the person's last message is not given again; a new one is given once; with the flag set and a transcript it cannot read, the hook writes and exits 0 without a word; it reads its refusals through the function the ledger hook and `guppi onward` already use.
  - Answer: agreed, (a).
- **How the new behaviour is checked**
  - Recommended: (a) a new Estimate, `estimate-spec-write-answers-a-refusal`, for the write on a flagged reply and the loop guard; in each of the six Criteria the line about the flag points to it; seven sub-cases.
  - Answer: agreed, (a).
- **What else the Case covers**
  - Recommended: (a) the hook alone: `guppi/ratified.py`, its tests, `rule-spec-write` and its Estimates; `orchestration.md` and the comparison check stay as they are.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, the write on a flagged reply and the loop guard were found to be two conditions that fail apart. The main agent asked whether they get two Estimates, and recommended (a): `estimate-spec-write-answers-a-refusal` for the write and `estimate-spec-write-tells-each-reason-once` for the guard, each of the six Criteria pointing to the one it needs. The person chose (a).
  - Taken: 644.1 keeps the write and its Estimate. The new 644.8 creates `estimate-spec-write-tells-each-reason-once` and takes the guard code and tests. 644.2 to 644.7 point to one or both.
- **Change**
  - Asked: at `/pre-spec`, 644.7 was found to lack the exception for a flag set with a transcript the hook cannot read, and `rule-spec-write` was found to keep an error sentence and a reason that disagree with 644.1 and 644.7. The main agent proposed adding the line as `estimate-ledger-write-exits-2-on-an-error` holds it, and pairs on `rule-spec-write`. The person agreed.
  - Taken: 644.7 has the `－` line. 644.1 has pairs on the error sentence and on the reason of the payload error in `rule-spec-write`.
- **Change**
  - Asked: at `/pre-spec`, the Criteria of 644.2 and 644.5 were found to speak of the answer of `case-guppi`, which Case 645 turns into a summary. The main agent proposed that they speak of the text stored under Case N. The person agreed.
  - Taken: 644.2 and 644.5 speak of the text stored under Case N and under the parent.

## History

- 2026-10-05 created · raw/2026-10-05/0311/ledger.md#case-644
