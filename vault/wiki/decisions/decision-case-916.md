---
type: decision
case: "916"
status: current
children: ["[[decision-case-916.1]]", "[[decision-case-916.2]]"]
origin: raw/2026-10-29/2341/ledger.md#case-916
sprint: plugin
created: 2026-10-29
tags: [session, workflow, harness]
---

## Problem

No rule says what the main agent does with an `**Other Case:**` line that names a Frontier item not yet built as a Case, so the change it names can be lost, and two Estimates do not say whether such a line is the event they wait for.

## Recommend

- **What should the main agent do with an Other Case line that names a Frontier item not yet built as a Case?**
  - Recommended: (a) keep the change for that item's Case: show the Case as it stands, and put the change into the prompt that dispatches the item's `case-guppi` when the person takes it up; `case-guppi` may name the item by its Frontier id.
  - Answer: agreed, (a).
- **What happens to the change when the named item ends with no Case?**
  - Recommended: (a) send the change back, with no question, to the `case-guppi` of the Case that wrote the line; that Case is shown again, and the person agrees or not at that showing.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) two parts, each with a new check read at the Retro of this session against the new text in the Spec; the old checks stay as they are.
  - Answer: agreed, (a).
- **Should this Case also say what the two waiting checks wait for?**
  - Recommended: (a) the `method` of `estimate-orchestration-shows-the-built-case` and of `estimate-orchestration-signs-items-taken-together` says that the line names a Case of the session.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed to the fixes `/pre-spec` proposed: the change for a named item taken up in the same batch goes to that item's `case-guppi` by `SendMessage`; the description of the summary and the batch sentence of `rule-orchestration` cover a line that names such an item; `context` says why `estimate-orchestration-names-related-cases-in-the-dispatch` stands.
  - Taken: 916.1 gains a `then` line and two `replace` pairs, its clause and the `purpose` of its new Estimate cover the batch, and `context` names the findings and why each Criterion stands.

## History

- 2026-10-30 created · raw/2026-10-29/2341/ledger.md#case-916
