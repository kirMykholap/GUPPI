---
type: decision
case: "415"
status: archived
update: ["[[estimate-case-protocol-case-form]]"]
supersedes: ["[[decision-case-413]]"]
origin: raw/2026-09-25/0051/ledger.md#case-415
sprint: migration
created: 2026-09-25
tags: [session, workflow]
---

## Context

One promise is signed twice. `estimate-case-protocol-case-form` promises in its line on `given`: "`when` and `then` name only what `given` names". It is read by hand at the close of a session. `estimate-prespec-checks-the-frame` promises the same as a finding of `prespec --check`, and a test reads it. `case-form` stands `pending`, `checks-the-frame` `passed`. The pre-spec of session 1916 found the double, and Case 413 deferred the choice. The rule itself in the Render of `rule-case-protocol` (the Sections table) does not change, so the behaviour of the rule and of the hooks stays as it is and `frame-guppi` is not dispatched. Only the Criterion of one Estimate changes. No vault query: it is an `update` with a `ref`.

## Problem

Which of the two Estimates keeps the line on the frame, so that one promise is signed once?

## Given

`estimate-case-protocol-case-form` — the Estimate whose Criterion is replaced.
**＋** `estimate-prespec-checks-the-frame` — the Estimate that keeps the line on the frame.
**＋** `rule-case-protocol` — the rule whose Case form the first Estimate reads.

## History

- 2026-09-25 created · raw/2026-09-25/0051/ledger.md#case-415
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
