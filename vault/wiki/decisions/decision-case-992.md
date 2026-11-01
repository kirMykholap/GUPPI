---
type: decision
case: "992"
status: current
children: ["[[decision-case-992.1]]", "[[decision-case-992.2]]"]
origin: raw/2026-11-01/2038/ledger.md#case-992
sprint: plugin
created: 2026-11-01
tags: [session, workflow, hooks, harness, ledger]
---

## Problem

After `/pre-spec`, the hook of `rule-prespec-onward` tells the agent to open with `STOP:` any reply in which a Case waits for the person's word, while the check of `rule-case-check` notes any line before a shown Case, and `rule-orchestration` puts the `LEDGER` block first in the acknowledging reply. No text says which one holds, so the agent broke the layout of a showing.

## Recommend

- **Which side gives way when a reply shows a Case and waits for the person**
  - Recommended: (a) narrow the hook's message: `STOP:` opens only a reply the hook would send back, one with a `LEDGER` block; a reply that shows a Case or a round keeps the layout of `orchestration.md` with no `STOP:` line; the hook's judgment is unchanged.
  - Answer: (a).
- **Change**
  - Asked: at the check of `/pre-spec`, the person agreed that an acknowledging reply after `/pre-spec` that waits for the person opens with the `STOP:` line and puts the `LEDGER` block right after it, with an update of `rule-orchestration` and the Criterion of `estimate-orchestration-acknowledging-reply` replaced whole, the hook unchanged; and the Purpose of `rule-prespec-onward` was to cover each reason of the hook.
  - Taken: Case 992.2 sets the order of that reply; the new Purpose text of Case 992.1 names each of the three reasons.
- **Where the change to the acknowledging reply goes**
  - Recommended: (a) Case 990 built again under a new number, with two parts, `{supersedes:case 990}` on its decision lines.
  - Answer: agreed, (a).

## History

- 2026-11-01 created · raw/2026-11-01/2038/ledger.md#case-992
