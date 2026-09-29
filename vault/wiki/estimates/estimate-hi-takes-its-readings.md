---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-hi]]"
purpose: Whether /hi takes, in its first reply, each open W reading whose method names /hi or the librarian's run and can be done whole then, closes its W line and writes its line, opens no page but the Estimates it reads, and leaves the readings that name a later moment or a /hi run of their own
method: "by hand at the first /hi after the render: the first reply, its tool calls, its LEDGER block and frontier.md read against the Criterion, recorded in the estimate line"
origin: raw/2026-09-29/1134/ledger.md#case-508.1
sprint: migration
created: 2026-09-29
tags: [session, harness, workflow]
---

## Criterion

When:
The person types `/hi` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md`.

Then:
In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose `method` names the `/hi` of a session or the librarian's run and whose whole method can be done at that moment.
**＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the commands of the method, and reads the librarian's report from the transcript of the previous session.
**＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
**＋** It closes the `W` line of each reading taken as `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
**－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
**－** A reading whose `method` also names a later moment is not taken at `/hi`. It is taken at that moment, and its `/hi` part is read then from the session's first turn.
**－** A reading whose `method` asks for a `/hi` run of its own, such as one outside plan mode, is not taken at `/hi`.
**－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

## History

- 2026-09-29 created · [[decision-case-508.1]]
