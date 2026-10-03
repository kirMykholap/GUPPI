---
type: insight
pattern: A rule of the form of a Case as shown in the chat — the order of its sections, what `ratification` holds, a count in a story section — is read by no script, so it holds only as far as the agent's own reading at the showing, and the fault is found later, by the person or by ask-guppi at pre-spec.
status: open
children: ["[[lesson-case-form-the-spec-free-sections-written-last]]", "[[lesson-case-form-ratification-used-for-the-agents-caveats]]", "[[lesson-case-form-a-count-in-the-sentence-that-opens-a-list]]", "[[lesson-case-form-given-written-before-tasks]]", "[[lesson-case-build-a-list-in-context]]", "[[lesson-case-build-quotes-the-person-in-the-chat-language]]", "[[lesson-case-build-rebuild-quotes-the-relayed-words]]", "[[lesson-case-protocol-own-text-before-a-round]]", "[[lesson-case-check-question-line-without-colon-unseen]]", "[[lesson-orchestration-own-text-before-a-prespec-round]]", "[[lesson-orchestration-own-sentence-between-heading-and-list]]"]
severity: 2
addressed_by: "[[decision-case-601.1]]"
origin: raw/2026-09-25/0051/ledger.md#L20
sprint: migration
created: 2026-09-25
tags: [session, workflow]
---

## Pattern

A rule of the form of a Case as shown in the chat — the order of its sections, what `ratification` holds, a count in a story section — is read by no script, so it holds only as far as the agent's own reading at the showing, and the fault is found later, by the person or by ask-guppi at pre-spec.

## Proposal

Let a check read the chat form of a Case before the person does — for example the check on `SubagentStop` that the scheme deferred by Case 416 proposes — over the order of the sections, the content of `ratification` and a count in a story section.

## History

- 2026-09-25 created · raw/2026-09-25/0051/ledger.md#L20
- 2026-09-25 updated: actioned: the chat form of a Case is checked on SubagentStop before the person sees it; a count in a story section stays unchecked (case 419.3) · [[decision-case-419.3]]
- 2026-09-25 updated: child lesson-case-form-given-written-before-tasks added; addressed_by stands, the lesson is closed by the same case 419.3 · raw/2026-09-25/1228/ledger.md#L15
- 2026-09-27 updated: child lesson-case-build-a-list-in-context added; status actioned reopened · raw/2026-09-26/2300/ledger.md#L32
- 2026-09-27 updated: actioned: the proposal for the story sections rejected — the person judges the text of context, problem and recommend, and no script reads it; the order of the sections and ratification are checked since case 419.3 (case 449) · [[decision-case-449]]
- 2026-09-29 updated: child lesson-case-build-quotes-the-person-in-the-chat-language added, reopened (synthesis) · raw/2026-09-29/1432/ledger.md#L33
- 2026-09-29 updated: child lesson-case-build-rebuild-quotes-the-relayed-words added (synthesis) · raw/2026-09-29/1753/ledger.md#L25
- 2026-09-30 updated: actioned: case-guppi quotes none of the person's words (case 536), and the check of each answer runs the language finding (case 537) · [[decision-case-537]]
- 2026-09-30 updated: child lesson-case-protocol-own-text-before-a-round added, reopened (synthesis) · raw/2026-09-30/1736/ledger.md#L44
- 2026-10-03 updated: child lesson-case-check-question-line-without-colon-unseen added; actioned: the Stop check of rule-case-check refuses a round shown after a text of the main agent's own (case 562), and the SubagentStop check sends back a round with a question out of the grill-me form (case 601.1); a count in a story section stays rejected (case 449) (case 605) · [[decision-case-605]]
- 2026-10-03 updated: children lesson-orchestration-own-text-before-a-prespec-round and lesson-orchestration-own-sentence-between-heading-and-list added, reopened from actioned (synthesis) · raw/2026-10-03/0115/ledger.md#L9
