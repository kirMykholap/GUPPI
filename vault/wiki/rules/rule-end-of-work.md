---
type: rule
kind: MOC
purpose: Prevents a session being handed over without a settled account of what happened
status: built
children: ["[[rule-retro]]", "[[rule-retro-commit]]", "[[rule-handoff]]", "[[rule-carry-over]]"]
estimates: ["[[estimate-end-of-work-order]]"]
origin: raw/2026-09-10/ledger.md#case-38
sprint: migration
created: 2026-09-10
tags: [session, workflow]
---

## Purpose

Prevents a session being handed over without a settled account of what happened. It
also prevents the librarian's writes from being indistinguishable from the
session's own, by forcing a commit between the two. Three steps: the Retro
conversation, the commit gate on the way to handoff, then handoff itself.

A session has a second end: `/carry` straight after Plan Mode, when the Spec is
ratified and its work is not done — no Work Mode, no Retro, no handoff, no
librarian; the brief is rewritten and the session folder marked, so the next session
picks the Spec up and the librarian does not apply it blind. On leaving Plan Mode the
agent asks the person which of the two ends and starts nothing until it is answered
(case 190.2).

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
- 2026-09-10 estimate estimate-end-of-work-order added · raw/2026-09-10/ledger.md#case-38
- 2026-09-10 status: draft → built · cascade
- 2026-09-16 child rule-carry-over added · [[decision-case-190.1]]
- 2026-09-16 updated: a session has a second end — /carry straight after Plan Mode, without Work Mode, retro, handoff or the librarian; the agent asks which of the two on leaving Plan Mode (case 190.2) · [[decision-case-190.2]]
- 2026-09-16 status: built → draft · cascade
- 2026-09-16 updated: the second end — /carry straight after Plan Mode — and the question on leaving Plan Mode (case 196.2, the text of 190.2) · [[decision-case-196.2]]
- 2026-09-17 status: draft → built · cascade
