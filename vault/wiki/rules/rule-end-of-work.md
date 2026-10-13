---
type: rule
kind: MOC
purpose: Prevents a session being handed over without a settled account of what happened
status: built
parent: "[[rule-session]]"
children: ["[[rule-retro]]", "[[rule-retro-commit]]", "[[rule-handoff]]", "[[rule-carry-over]]", "[[rule-retro-onward]]", "[[rule-spec-box]]"]
estimates: ["[[estimate-end-of-work-order]]"]
origin: raw/2026-09-10/ledger.md#case-38
sprint: migration
created: 2026-09-10
tags: [session, workflow]
core: true
---

## Purpose

Prevents a session being handed over without a settled account of what happened. It
also prevents the librarian's writes from being indistinguishable from the
session's own, by forcing a commit between the two. Three steps, which the agent runs in the turn of Work Mode with no stop for the person: Retro, the commit gate on the way to handoff, then handoff itself (case 531.1).

A session has a second end: `/carry` straight after Plan Mode, when the Spec is
ratified and its work is not done — no Work Mode, no Retro, no handoff, no
librarian; the brief is rewritten and the session folder marked, so the next session
picks the Spec up and the librarian does not apply it blind. On leaving Plan Mode the agent asks the person which of the two ends and starts nothing until it is answered (case 190.2). A session that took a conserved Spec at the Frontier is asked nothing there: `/box` runs it the ordinary way on the branch of that Spec, and merges the branch back by a fast-forward after `handoff.md` stands and before the librarian, as `rule-spec-box` sets it (case 591).

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
- 2026-09-10 estimate estimate-end-of-work-order added · raw/2026-09-10/ledger.md#case-38
- 2026-09-10 status: draft → built · cascade
- 2026-09-16 child rule-carry-over added · [[decision-case-190.1]]
- 2026-09-16 updated: a session has a second end — /carry straight after Plan Mode, without Work Mode, retro, handoff or the librarian; the agent asks which of the two on leaving Plan Mode (case 190.2) · [[decision-case-190.2]]
- 2026-09-16 status: built → draft · cascade
- 2026-09-16 updated: the second end — /carry straight after Plan Mode — and the question on leaving Plan Mode (case 196.2, the text of 190.2) · [[decision-case-196.2]]
- 2026-09-17 status: draft → built · cascade
- 2026-09-22 updated: the parent is rule-session, the MOC of the five phases (case 316) · [[decision-case-316]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-30 updated: the steps of the end of a session run in the turn of Work Mode with no stop for the person (case 531.1) · [[decision-case-531.1]]
- 2026-09-30 child rule-retro-onward added · [[decision-case-531.9]]
- 2026-10-02 updated: a session that took a conserved Spec is asked nothing on leaving Plan Mode and ends the ordinary way through /box; rule-spec-box a child after rule-retro-onward (case 591.4) · [[decision-case-591.4]]
- 2026-10-03 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the slug of rule-spec-box stands outside the bracket of its pointer · [[decision-case-809]]
