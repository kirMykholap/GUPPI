---
type: estimate
kind: QA
status: pending
target: "[[rule-handoff]]"
purpose: /handoff stops on a dirty tree, writes handoff.md from memory into the session's folder and dispatches the librarian with its path, with no commit after
method: "by hand at the /handoff of a later session: the event log, handoff.md, the dispatch line and git log"
origin: raw/2026-09-10/ledger.md#case-38.3
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Criterion

When:
The person invokes `/handoff` after the Retro, the gate of `guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

Then:
The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
**＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
**＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the three sections `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done`, with no Read call on the artifacts.
**＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written, and shows the librarian's report to the person unchanged.
**－** No commit follows the handoff except the librarian's own.

## Result

live 2026-09-14 session N, block 73.7: handoff.md written to raw/2026-09-14/1029/ (the hi folder), one document, no `---`; event_log `12:10:50 handoff`; librarian-guppi dispatched (Agent line 12:19:19) and its report shown; the only commit that followed is the librarian's own fc3d439

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.3
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L87
- 2026-09-12 criterion: case 73.7 added · [[decision-case-73.7]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L4
- 2026-09-29 updated: the Criterion replaced whole — the head and the block 73.7 into one When and Then, the dispatch by the path; purpose and method set, Context and Method out (case 499.2) · [[decision-case-499.2]]
