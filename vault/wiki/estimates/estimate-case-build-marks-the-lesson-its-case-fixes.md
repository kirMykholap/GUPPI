---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi weighs each error lesson of the session that no mark ties to a Case, and writes the addresses mark on a decision line of the Case or sub-case that fixes its cause
method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
origin: raw/2026-10-29/2341/ledger.md#case-915.2
sprint: plugin
created: 2026-10-29
tags: [session, workflow, harness]
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

2026-10-30, Retro of session 2341: the new Render of rule-case-build in the Spec (case 915.2), its old string standing once on the page, has case-guppi read the ledger by a Grep for lesson\[error\] and one for \{addresses:, judge each error lesson no mark ties to a Case, add {addresses:<slug>} to one decision line of the Case or sub-case that fixes its cause with the lesson named in context, and add no mark for a knowledge lesson; the summary carries its ledger lines as the file holds them, as .claude/agents/case-guppi.md sets it, so the mark reaches the person

## History

- 2026-10-30 created · [[decision-case-915.2]]
- 2026-10-30 status: pending → passed · raw/2026-10-29/2341/ledger.md#L31
