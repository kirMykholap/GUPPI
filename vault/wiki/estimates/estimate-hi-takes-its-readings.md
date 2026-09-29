---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
purpose: Whether /hi takes, in its first reply, each open W reading whose method names /hi or the librarian's run and can be done whole then, closes its W line and writes its line, opens no page but the Estimates it reads, and leaves the readings that name a later moment or a /hi run of their own
method: "by hand at the first /hi after the render: the first reply, its tool calls, its LEDGER block and frontier.md read against the Criterion, recorded in the estimate line"
checked: 2026-09-29
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

## Result

2026-09-29, by hand, the first reply of session 1432: before the question on the order it took the five readings whose method names the librarian's run and could be done whole (close-commits, index-check-merges, synthesis-clusters, raw-archive, glossary-terms-defined), from git log, git status, the commands and the report in the transcript of session 1134; it opened each Estimate page and judged it against its Criterion; it closed W9, W20, W27, W33 and W46 [x] · work in frontier.md and then wrote five estimate lines in a LEDGER block of a reply that ends in text; it left git-context-current (a later moment named), event-log-records (a /hi run of its own), brief-carries-the-run-facts (no run with the Render yet) and the two readings of its own reply; no page or repository file changed but frontier.md

## History

- 2026-09-29 created · [[decision-case-508.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L30
