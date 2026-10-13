---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi judges the forms, the moments of readings and what they will find by the state of the code and the pages at the moment the check or the reading runs, and asks the person when a Case needs a form another Case of the same session adds
method: "by hand, after case-guppi builds a Case whose form or reading depends on another Case of the same session: the Case file, or the round before it, read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-13/1426/ledger.md#case-797.1
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case whose task writes a form of an update or whose Estimate sets the moment of a reading, while another Case of the same session changes the code that judges that form or the page or file that reading reads.

Then:
`case-guppi` judges the form, the moment of the reading and what the reading will find by the state of the code and the pages at the moment the check or the reading runs, not by the state at the end of the session.
**＋** A task of the Case writes only a form of an update that the code accepts when the check of `rule-case-check` runs.
**＋** Where the Case needs a form of an update that another Case of the same session adds, `case-guppi` asks the person in a round whether the Case uses a form the code accepts now or leaves that change to a Case of a later session.

## History

- 2026-10-13 created · [[decision-case-797.1]]
