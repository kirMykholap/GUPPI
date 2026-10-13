---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether each Case case-guppi builds creates or replaces an Estimate or names the one that already checks the change, offers that Estimate by slug in a round on the promise, names it in context after an answer that no new Estimate is created, and asks in a round when it can do neither
method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-13
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
**＋** A question of a round before the Case on how it is checked gives an option that names by slug the Estimate that already checks the change, where one in the `estimates` of a page the Case changes does.
**＋** After the person answers that no new Estimate is created, the `context` names by slug the Estimate that checks the change, taken from the `estimates` of a page the Case changes.
**＋** When the person's words and the frame give neither, `case-guppi` asks in a round, before it writes the Case, what the Estimate will check, and the `recommend` of the Case holds that question.
**－** A deferred decision in the short form is not written by `case-guppi` and carries no such Estimate.

## Result

2026-10-13, Retro, the new Render of rule-case-build in raw/2026-10-13/1753/spec.md (Case 800.1) read against the Criterion; the sentence of case 561.11 keeps that a Case creates or replaces an Estimate or names the one that checks the change in context; the new sentence of case 800.1 gives a round on the promise an option that names by slug the Estimate from the estimates of each page the Case changes, closes an answer of no new Estimate only with that Estimate named in context, and asks again where none checks the change; the summary sentence of the Render names "the Estimate that checks it" under each item

## History

- 2026-10-01 created · [[decision-case-561.11]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L28
- 2026-10-05 updated: the Criterion replaced whole — the Case is written into its file, and the summary names the Estimate of each Case (case 645.12) · [[decision-case-645.12]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1343/ledger.md#L39
- 2026-10-13 updated: the Criterion replaced whole — the round on the promise names the existing Estimate, and an answer of no new Estimate closes the promise only with it named (case 800.1) · [[decision-case-800.1]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1753/ledger.md#L113
