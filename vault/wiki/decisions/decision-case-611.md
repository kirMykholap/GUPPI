---
type: decision
case: "611"
status: current
create: ["[[estimate-case-check-refuses-text-outside-the-list]]"]
update: ["[[rule-case-check]]", "[[insight-case-form-chat-form-read-by-no-script]]"]
origin: raw/2026-10-03/0317/ledger.md#case-611
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow, session]
---

## Problem

The rule of how a built Case is shown puts every text of the agent's own after the horizontal rule, but no script reads that part of a showing. In session 0115 a note under the heading of a Case went through, and the reading of `estimate-orchestration-shows-the-built-case` failed. The question was whether such a note is allowed, or whether the `Stop` check of `rule-case-check` refuses it, and how much of the showing the check reads.

## Recommend

- **A note between the Case heading and its list**
  - Recommended: (a) the check refuses it; a note goes after the horizontal rule.
  - Answer: agreed, (a).
- **How much of the showing the check reads**
  - Recommended: (b) the whole showing up to the horizontal rule: nothing before the first Case heading, and under each heading only the list, the `ratification` blockquote and blank lines.
  - Answer: accepted the recommendation, (b).
- **What checks the new refusal**
  - Recommended: (a) a new promise of its own on `rule-case-check`; the promise on rounds and the comparison promise stand.
  - Answer: accepted the recommendation, (a).
- **The failed reading and the open insight**
  - Recommended: (a) the promise of `estimate-orchestration-shows-the-built-case` stays word for word and is read again in a later session; the insight is marked as acted on; `insight-workflow-case-schema-silent-on-what-the-scripts-accept` is not touched.
  - Answer: accepted the recommendation, (a).

## History

- 2026-10-03 created · raw/2026-10-03/0317/ledger.md#case-611
