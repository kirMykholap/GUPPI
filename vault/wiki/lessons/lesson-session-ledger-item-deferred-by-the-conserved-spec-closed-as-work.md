---
type: lesson
kind: error
root_cause: rule-skill-hi gives the three closers of a line left — backlog kept, sprint defer, defer case N — but none for a Frontier item of the ledger whose defer stands in the conserved Spec being taken, and the check judges `defer case N` only against the Cases of the session's own plan, so the agent picked a closer by its own judgment and did not name the gap as a stop
status: clustered
insight: "[[insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan]]"
origin: raw/2026-10-03/1416/ledger.md#L10
sprint: migration
created: 2026-10-03
tags: [session, workflow]
---

## Trigger

at the Frontier of session 1416 the person took the conserved Spec of 1341, and the line C4, the failed reading of estimate-handoff-holds-each-fact-once from the ledger Tail, which Case 618 of that Spec defers, had to close as left; the agent wrote `[-] … · ledger · defer case 618`, the pre-spec check refused it since the plan of this session holds no Case 618, and the agent closed the line `[x] … · ledger · work`, a closer the Criterion of estimate-hi-takes-a-conserved-spec does not list, instead of a short-form defer of its own

## Root cause

rule-skill-hi gives the three closers of a line left — backlog kept, sprint defer, defer case N — but none for a Frontier item of the ledger whose defer stands in the conserved Spec being taken, and the check judges `defer case N` only against the Cases of the session's own plan, so the agent picked a closer by its own judgment and did not name the gap as a stop

## History

- 2026-10-03 created · raw/2026-10-03/1416/ledger.md#L10
- 2026-10-03 updated: clustered under insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan (synthesis) · raw/2026-10-03/1416/ledger.md#L10
