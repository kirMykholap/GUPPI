---
type: decision
case: "780"
status: current
create: ["[[estimate-case-build-judges-options-against-the-broken-rule]]"]
update: ["[[rule-case-build]]"]
origin: raw/2026-10-12/1604/ledger.md#case-780
sprint: plugin
created: 2026-10-12
tags: [session, workflow, harness]
---

## Problem

`case-guppi` judges an option for a defect against the item's own words, not against the rule the defect breaks. So it can recommend an option that keeps the same defect in the rest of the text.

## Recommend

- **Where the fix lives**
  - Recommended: (a) one sentence in `rule-case-build`: when an item reports a defect, `case-guppi` finds the rule it breaks and judges each option against that rule over the whole text the option leaves; no check in `/pre-spec`, which item C2 may take up.
  - Answer: agreed, (a).
- **How a round shows an option that fixes only part of the defect**
  - Recommended: (a) the option may stand; its `**After:**` line names the part that still breaks the rule, and the agent does not recommend it.
  - Answer: agreed, (a).
- **How we check that the fix works**
  - Recommended: (a) a new Estimate, `estimate-case-build-judges-options-against-the-broken-rule`, read at the Retro of this session against the new Render in the Spec.
  - Answer: agreed, (a).

## History

- 2026-10-12 created · raw/2026-10-12/1604/ledger.md#case-780
