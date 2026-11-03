---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the line of a backlog item that a Case of the session defers again with a new wording closes [-] … · backlog · defer case N, while an item left as it stands or whose Case is taken back closes [-] … · backlog · kept
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration and of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and `.claude/skills/hi/SKILL.md` from `rule-skill-hi`, a Case of the session defers again, with a new wording, an item of `vault/wiki/backlog.md` that stands on a line of `raw/<date>/<hi HHMM>/frontier.md` with the source `backlog`.

Then:
The agent closes the line of the item `[-] … · backlog · defer case N`, N the id of that Case, in the reply that carries the decision lines of the Case.
**＋** The agent takes this closer only for a Case whose decision lines meet the backlog rule of `estimate-prespec-checks-the-frontier`, so that the check that Estimate reads finds nothing on the line.
**＋** An item of `vault/wiki/backlog.md` left as it stands, with no Case, closes `[-] … · backlog · kept`, and so does one whose ratified Case the person takes back in Plan Mode.
**－** The line of an item that a Case defers again does not close `[x] … · backlog · case N`, which stays for a Case that takes the item off the backlog.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
