---
type: insight
pattern: A ratified change lands on one text and leaves the text derived from it behind, because no step of the pipeline names the dependents of a change.
status: actioned
children: [lesson-estimates-criterion-stale-after-contract-change, lesson-render-governed-file-updated-as-rule-class-file, lesson-estimates-live-clause-stale-at-first-render]
severity: 0
addressed_by: decision-case-138
origin: raw/2026-09-12/ledger.md#L12
sprint: migration
created: 2026-09-12
tags: [harness, render, workflow]
---

## Pattern

Three lessons where one contract lived in two places and only one was changed.

`lesson-estimates-criterion-stale-after-contract-change` (session A): Case 15.1 redefined
a ledger record as a line in a LEDGER block; the criteria of `estimate-session-start-context`
and `estimate-case-protocol-loaded` still described the bare-line contract, and the first
stopped discriminating a session with `/hi` from one without. Nothing listed the Estimates
whose criterion quotes the changed wording.

`lesson-render-governed-file-updated-as-rule-class-file` (session I): Case 56 changed the
Case protocol paragraph of `CLAUDE.md` by hand, as a file item; `rule-case-protocol`, whose
Render that paragraph is, was not updated, so `render --check` names the file and a render
would drop the ratified sentence.

`lesson-estimates-live-clause-stale-at-first-render` (session J): the live clauses of
`estimate-claude-md-rendered` and `estimate-render-harness-reproduces` were written in Plan
Mode of session I against the files as they stood; the librarian of the same session then
wrote the ratified Cases into the Rule pages, and the first render of session J moved six
files instead of the marker lines the clauses name. Both readings failed on the clause, not
on the renderer.

In all three, the derived text has no pointer back to its source, and nothing checks the pair.

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
- [[lesson-estimates-live-clause-stale-at-first-render]]

## Addressed by

- [[decision-case-138]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L12
- 2026-09-12 updated: clustered by librarian: a third lesson on a change that leaves its derived text stale · raw/2026-09-12/ledger.md#L155
- 2026-09-14 updated: actioned: the path half by 59.6, 59.8 and pre-task's governed check; the criterion half by the derived criterion blocks of 72.1 and 88.2; no pre-task pass over quoting Estimates (case 138) · [[decision-case-138]]
