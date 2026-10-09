---
type: insight
pattern: A Case is composed from what the agent has in view — the dialogue, the rule page, the code — and the pages it changes or runs beside are not read against it before it is shown, so a contradiction with them is found only by a later check, pre-task or pre-spec.
status: actioned
children: ["[[lesson-plan-mode-contract-change-skips-the-estimates-blocks]]", "[[lesson-case-designed-in-dialogue-not-checked-against-its-rules]]", "[[lesson-case-frame-read-without-the-estimates-of-the-pages-it-edits]]", "[[lesson-orchestration-recommended-a-rebuild-that-signed-a-promise-twice]]", "[[lesson-case-build-finds-the-sentences-it-changes-by-their-words]]", "[[lesson-case-build-task-copies-an-existing-judgment]]"]
severity: 0
addressed_by: "[[decision-case-752]]"
origin: raw/2026-09-23/1859/ledger.md#L30
sprint: migration
created: 2026-09-23
tags: [workflow, harness, session]
---

## Pattern

A Case is composed from what the agent has in view — the dialogue, the rule page, the code — and the pages it changes or runs beside are not read against it before it is shown, so a contradiction with them is found only by a later check. In session 1809 of 2026-09-15 Cases 175 and 164 changed the contract of a rule without reading the Estimate pages that take the new block; ask-guppi at pre-task found the contradicting blocks (`lesson-plan-mode-contract-change-skips-the-estimates-blocks`). In session 1859 of 2026-09-23 Case 387 was written in one pass from the discussion; the rules it touches and the order in which its hooks run were not read against it, and pre-spec found eight contradictions (`lesson-case-designed-in-dialogue-not-checked-against-its-rules`).

## Proposal

A suggestion, not a decision: before a Case that changes a contract or adds a hook is shown, the agent could list the pages its tasks touch or run beside — the Estimates of the rule, the rules it names, the hooks on the same event — and read each against the Case, so the contradiction is found before the showing, not by the check after ratification.

## History

- 2026-09-24 created · raw/2026-09-23/1859/ledger.md#L30
- 2026-09-24 updated: actioned: the frame of a Case is checked by frame-guppi before the showing (case 391.2) · [[decision-case-391.2]]
- 2026-09-24 updated: lesson-case-frame-read-without-the-estimates-of-the-pages-it-edits added to children by the librarian's synthesis; addressed_by decision-case-391.2 stands (the lesson names the same case) · raw/2026-09-24/1303/ledger.md#L25
- 2026-10-07 updated: child lesson-orchestration-recommended-a-rebuild-that-signed-a-promise-twice added; open again, the pattern came back after case 391.2 (synthesis) · raw/2026-10-07/2114/ledger.md#L30
- 2026-10-08 updated: actioned: case-guppi words the change another Case needs as a pointer to its own Estimate when that Estimate already makes the promise (case 730.3) · [[decision-case-730.3]]
- 2026-10-08 updated: child lesson-case-build-finds-the-sentences-it-changes-by-their-words added, reopened from actioned by case 730.3 of this run (synthesis) · raw/2026-10-08/0050/ledger.md#L17
- 2026-10-08 updated: actioned: case-guppi lists by meaning each sentence of a page it changes that states the behaviour the change touches, not by a Grep for the words of the changed sentence (case 734) · [[decision-case-734]]
- 2026-10-09 updated: child lesson-case-build-task-copies-an-existing-judgment added, reopened from actioned (synthesis) · raw/2026-10-09/0200/ledger.md#L23
- 2026-10-09 updated: actioned: case-guppi searches guppi/ for an existing implementation of a judgment before a task adds one (case 752) · [[decision-case-752]]
