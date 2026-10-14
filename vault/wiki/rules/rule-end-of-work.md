---
type: rule
kind: MOC
purpose: Prevents a session being handed over without a settled account of what happened
status: built
parent: "[[rule-session]]"
children: ["[[rule-retro]]", "[[rule-retro-commit]]", "[[rule-handoff]]", "[[rule-carry-over]]", "[[rule-retro-onward]]", "[[rule-spec-box]]"]
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow]
core: true
---

## Purpose

Prevents a session being handed over without a settled account of what happened. It
also prevents the librarian's writes from being indistinguishable from the
session's own, by forcing a commit between the two. Three steps, which the agent runs in the turn of Work Mode with no stop for the person: Retro, the commit gate on the way to handoff, then handoff itself.

A session has a second end: `/carry` straight after Plan Mode, when the Spec is
ratified and its work is not done — no Work Mode, no Retro, no handoff, no
librarian; the brief is rewritten and the session folder marked, so the next session
picks the Spec up and the librarian does not apply it blind. On leaving Plan Mode the agent asks the person which of the two ends and starts nothing until it is answered. A session that took a conserved Spec at the Frontier is asked nothing there: `/box` runs it the ordinary way on the branch of that Spec, and merges the branch back by a fast-forward after `handoff.md` stands and before the librarian, as `rule-spec-box` sets it.

## History

- 2026-10-14 shipped with GUPPI
