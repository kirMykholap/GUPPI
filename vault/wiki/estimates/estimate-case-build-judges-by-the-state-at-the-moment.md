---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi judges the forms, the moments of readings and what they will find by the state of the code and the pages at the moment the check or the reading runs, and asks the person when a Case needs a form another Case of the same session adds
method: "by hand, after case-guppi builds a Case whose form or reading depends on another Case of the same session: the Case file, or the round before it, read against the Criterion, recorded in the estimate line"
checked: 2026-10-13
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

## Result

2026-10-13, /hi of session 2118, vault/raw/2026-10-13/1753/cases/case-804.md read against the Criterion: Case 804.5 writes set: {core: true} while Cases 804.1–804.3 add core to the schemas; the code accepts that form when the check of rule-case-check runs, since schema_changed of guppi/materialize.py frees the categories whose schema rule the session changes (case 308.2), and the librarian's run applied all 119 entries; the context of 804 judges the moments by the state then — the pages get core at the librarian's run, so the Work Mode run of guppi ship lists only the leftovers of the code and the harness and the page leftovers come from the first CI run; ledger lines 116–118 of 1753 put the live schema.yaml at the librarian's render; the round "Which pages get core now, and how?" put the choice to the person

## History

- 2026-10-13 created · [[decision-case-797.1]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L1
