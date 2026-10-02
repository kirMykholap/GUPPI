---
type: decision
case: "605"
status: current
update: ["[[insight-case-form-chat-form-read-by-no-script]]", "[[lesson-case-check-question-line-without-colon-unseen]]"]
origin: raw/2026-10-02/2300/ledger.md#case-605
sprint: migration
created: 2026-10-02
tags: [session, workflow, hooks]
---

## Problem

The Insight still stands `open` in the backlog. Its one live lesson was closed by case 562. A second lesson of its pattern, the question title line without the colon, stands `new` and is part of no Insight. Case 601.1 of this session closes the cause of that second lesson. The question was whether to close the Insight now, and with which lessons and which fix.

## Recommend

- Recommended: close the Insight now, with `addressed_by` naming `decision-case-562`, the decision whose `Stop` check refuses a round shown after the main agent's own text.
  - Answer: ratified as built
- **Change**
  - Asked: pre-spec found that `lesson-case-check-question-line-without-colon-unseen`, recorded after case 562, fits the Insight's pattern, and that Case 601.1 is then the latest fix. The person chose to add that lesson to the Insight's `children`, set it `clustered` with `insight`, have `addressed_by` name `decision-case-601.1`, and let the cascade archive both lessons with the Insight `actioned`.
  - Taken: the Insight's `update` sets `children` with the new lesson, `status: actioned` and `addressed_by: decision-case-601.1`. A second `update` sets the lesson `clustered` with `insight`. The context no longer claims that no lesson of the cause came in after case 562.

## History

- 2026-10-03 created · raw/2026-10-02/2300/ledger.md#case-605
