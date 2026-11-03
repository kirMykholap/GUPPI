---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi weighs each error lesson of the session that no mark ties to a Case, and writes the addresses mark on a decision line of the Case or sub-case that fixes its cause
method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`case-guppi`, by `.claude/agents/case-guppi.md`, writes the `ratification` of a Case into its file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the session's ledger `raw/<date>/<hi HHMM>/ledger.md` holds a `lesson[error][<slug>]` line that no mark ties to a Case.

Then:
`case-guppi` judges whether the Case, or one of its sub-cases, fixes the root cause of that lesson.
**＋** Where one does, one decision line of that Case or sub-case carries `{addresses:<slug>}`, in the form of `vault/wiki/ratification.md`, and `context` names the lesson and why the Case closes it.
**＋** The summary of `case-guppi` holds the line with the mark as the file holds it, so the person ratifies the mark with the Case.
**－** A `lesson[knowledge]` line of the ledger gets no mark from this judgment.
**－** A lesson with `{addressed_by:...}` on a line of its slug, or that a decision line of the ledger already marks with `{addresses:<slug>}`, is not judged again.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
