---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the line of a backlog item that a Case of the session defers again with a new wording closes [-] … · backlog · defer case N, while an item left as it stands or whose Case is taken back closes [-] … · backlog · kept
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration and of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-30/2005/ledger.md#case-937.2
sprint: plugin
created: 2026-10-30
tags: [session, workflow]
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

2026-10-30, Retro of session 2005: the new Render of rule-orchestration and rule-skill-hi in vault/raw/2026-10-30/2005/spec.md (Case 937.2) read against the Criterion: both name [-] … · backlog · defer case N for an item a Case defers again, with a defer line naming the page and {supersedes:case M} for each Case of its deferred_by and /pre-spec reporting the line otherwise; [-] … · backlog · kept stays for an item left as it stands, and vault/wiki/orchestration.md already closes a take-back kept; [x] … · backlog · case N is left to a Case that takes the item off the backlog

## History

- 2026-10-30 created · [[decision-case-937.2]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/2005/ledger.md#L46
