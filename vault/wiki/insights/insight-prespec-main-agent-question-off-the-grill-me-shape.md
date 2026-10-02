---
type: insight
pattern: no rule gives the question shape of the skill grill-me to a question the main agent asks the person itself, so at /pre-spec the main agent writes such a question in its own shape
status: actioned
children: ["[[lesson-prespec-report-decisions-off-the-question-shape]]", "[[lesson-prespec-report-questions-still-off-the-shape]]"]
severity: 0
addressed_by: "[[decision-case-561.13]]"
origin: raw/2026-09-30/1306/ledger.md#L48
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Pattern

Two lessons of one cause. At /pre-spec of session 0248 (`lesson-prespec-report-decisions-off-the-question-shape`) the main agent put the two decisions it needed from the person as bold labels with bare option lines, with no question line, no Now block and no recommendation line. At /pre-spec of session 1306 (`lesson-prespec-report-questions-still-off-the-shape`) it put three decisions as numbered bold questions with (a) and (b) lines, in the same shape. In both, the question shape of grill-me governs a round of case-guppi only, and no rule names it for a question the main agent asks the person itself; the item was deferred to `rule-orchestration` by case 546.

## Proposal

A suggestion, not a decision. The rule that governs the main agent's own questions to the person names the question shape of grill-me for them, and the lesson of the first session stands where the next /pre-spec reads it.

## History

- 2026-09-30 created · raw/2026-09-30/1306/ledger.md#L48
- 2026-10-02 updated: actioned: orchestration.md and the pre-spec skill give the grill-me shape to each question the main agent puts to the person itself (case 561.13); no lesson of the cause since (case 599) · [[decision-case-599]]
