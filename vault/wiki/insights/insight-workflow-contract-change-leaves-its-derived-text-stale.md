---
type: insight
pattern: A ratified change lands on one text and leaves the text derived from it behind, because no step of the pipeline names the dependents of a change.
status: open
children: [lesson-estimates-criterion-stale-after-contract-change, lesson-render-governed-file-updated-as-rule-class-file]
severity: 2
origin: raw/2026-09-12/ledger.md#L12
sprint: migration
created: 2026-09-12
tags: [harness, render, workflow]
---

## Pattern

Two lessons where one contract lived in two places and only one was changed.

`lesson-estimates-criterion-stale-after-contract-change` (session A): Case 15.1 redefined
a ledger record as a line in a LEDGER block; the criteria of `estimate-session-start-context`
and `estimate-case-protocol-loaded` still described the bare-line contract, and the first
stopped discriminating a session with `/hi` from one without. Nothing listed the Estimates
whose criterion quotes the changed wording.

`lesson-render-governed-file-updated-as-rule-class-file` (session I): Case 56 changed the
Case protocol paragraph of `CLAUDE.md` by hand, as a file item; `rule-case-protocol`, whose
Render that paragraph is, was not updated, so `render --check` names the file and a render
would drop the ratified sentence.

In both, the derived text has no pointer back to its source, and nothing checks the pair.

## Proposal

A suggestion, not a decision. Resolve the dependents of a change in one pass at pre-task:
for each changed slug, the Estimates whose criterion quotes it; for each `file` path, the
Rule whose `governs` names it. A change without its pair is a finding. Case 59.6 covers
the path half at write time with the `guard` hook, and Case 59.8 removes the dual nature
of `CLAUDE.md`; the Estimate-criterion half is still done by hand, by grep, in the
acknowledging reply.

## Children

- [[lesson-estimates-criterion-stale-after-contract-change]]
- [[lesson-render-governed-file-updated-as-rule-class-file]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L12
