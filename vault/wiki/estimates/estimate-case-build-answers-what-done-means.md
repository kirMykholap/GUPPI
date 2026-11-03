---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether each Case case-guppi builds creates or replaces an Estimate or names the one that already checks the change, offers that Estimate by slug in a round on the promise, names it in context after an answer that no new Estimate is created, and asks in a round when it can do neither
method: "by hand: the Render of rule-case-build in .claude/agents/case-guppi.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-13
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
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

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
