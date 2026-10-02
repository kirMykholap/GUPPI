---
type: decision
case: "598"
status: current
children: ["[[decision-case-598.1]]", "[[decision-case-598.2]]", "[[decision-case-598.3]]"]
origin: raw/2026-10-02/2049/ledger.md#case-598
sprint: migration
created: 2026-10-02
tags: [session, workflow, harness, ledger]
---

## Problem

Only the loop after the findings of `/pre-spec` lets Cases go out together for one ratification. When a new Case shows that a ratified Case must change, the changed Case is ratified again in a reply of its own, and the new Case in the next one. Nothing gathers the Cases handled side by side into one sign-off.

## Recommend

- **Which Cases can be signed together outside the pre-spec loop?**
  - Recommended: (a) one by one, with a batch only when Cases are handled side by side. Frontier items are taken one at a time, and each Case is ratified once discussed. After the findings of `/pre-spec`, and when a new Case shows that a ratified Case must change, the agent waits for the whole batch and shows all of it in one reply for one ratification.
  - Answer: agreed with the recommendation, (a). In the first round the person had chosen (b), to hold every ratification for a batch, and the person's own answer in the second round replaced it.
- **What the reply that shows a Case asks you**
  - Recommended: (a) sign now or move on. The reply asks for the sign-off or lets the Case wait for the batch.
  - Answer: in the person's own words: items of the Frontier are taken one after another and each Case is ratified after it is discussed. When several Cases are considered side by side, the agent always waits for the batch and shows all the Cases together. The cases are after the pre-spec check, or when it becomes clear that an earlier Case needs a change because of new edits. The person asked whether this holds.
- **When the agent asks for the batch sign-off**
  - Recommended: (a) when every open item under the Cases list is a waiting Case, and whenever the person asks; the person may name the Cases they sign.
  - Answer: not answered; replaced by **How a batch runs in the middle of Plan Mode**.
- **What the batch sign-off reply shows**
  - Recommended: (a) a short list with no files and no ledger lines.
  - Answer: not answered; replaced by **How a batch runs in the middle of Plan Mode**.
- **How the Frontier shows a waiting Case**
  - Recommended: (a) the line stays open as it is.
  - Answer: not answered; replaced by **Which Cases can be signed together outside the pre-spec loop?**, under which no Case waits unsigned.
- **How a batch runs in the middle of Plan Mode**
  - Recommended: (a) the same steps as the pre-spec loop. The agent sends the ratified Case back to its `case-guppi`, writes one `**Waiting:**` line while an answer is out, gathers the rounds into one list numbered by Case, and shows all the Cases of the batch in one reply for one ratification.
  - Answer: agreed with the recommendation, (a).
- **If you sign only part of a batch**
  - Recommended: (a) name the Cases you sign, as with sub-cases. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or with any Case it changes in turn.
  - Answer: agreed with the recommendation, (a).
- **How the change is checked, and what else it changes**
  - Recommended: (a) three sub-cases. The first changes `rule-orchestration` and creates an Estimate for the batch. The second replaces the Criterion of `estimate-orchestration-acknowledging-reply`. The third replaces the Criterion of `estimate-prespec-gathers-the-answers-after-findings` without its line on what holds outside the loop.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-02 created · raw/2026-10-02/2049/ledger.md#case-598
