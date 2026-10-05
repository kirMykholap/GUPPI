---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether each Case case-guppi builds creates or replaces an Estimate or names the one that already checks the change, and asks in a round when it can do neither
method: by hand at the close of a later session, each Case of the plan and the rounds before it read in the transcript
checked: 2026-10-05
origin: raw/2026-09-30/2356/ledger.md#case-561.11
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
`case-guppi` writes a Case into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`.

Then:
Each Case and sub-case of the file creates an Estimate or replaces the Criterion of one, or its `context`, or its parent's, names by slug the Estimate that already checks the change and says why its Criterion stands.
**＋** The summary that `case-guppi` answers with names that Estimate under the item of each Case and sub-case.
**＋** When the person's words and the frame give neither, `case-guppi` asks in a round, before it writes the Case, what the Estimate will check, and the `recommend` of the Case holds that question.
**－** A deferred decision in the short form is not written by `case-guppi` and carries no such Estimate.

## Result

2026-10-05, by hand at the Work readings of session 1343: each Case and sub-case of 650–656 names in its file and in every summary the Estimate that checks it — created (650.1, 651.2, 651.3), replaced (650.2, 652, 653.1, 653.2, 654, 655, 656) or named in context as already checking it with its Criterion standing (651.1); rounds asked how the change is checked before the Case was written (650 Q3, 651 Q5, 653 Q3), each in its recommend; the short-form defers 657–659 are the main agent's and carry none

## History

- 2026-10-01 created · [[decision-case-561.11]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L28
- 2026-10-05 updated: the Criterion replaced whole — the Case is written into its file, and the summary names the Estimate of each Case (case 645.12) · [[decision-case-645.12]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L39
