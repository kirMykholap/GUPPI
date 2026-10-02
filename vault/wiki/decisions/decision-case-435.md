---
type: decision
case: "435"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-orchestration-shows-the-built-case]]"]
origin: raw/2026-09-26/1337/ledger.md#case-435
sprint: migration
created: 2026-09-26
tags: [session, workflow, ledger]
---

## Context

`case-guppi` builds a Case, and the main agent shows it. `rule-case-protocol` requires the answer shown whole and unchanged. But the main agent does not copy the text; it writes it again. In session 1654 it retyped Case 428 this way and put the ledger line of 428.2 under the ratification of 428.3. The comparison `uv run guppi casecheck` on `Stop` of `rule-case-check` refused that reply. The next reply of the same turn showed 428.3 unchanged, and the person answered the correct Case. The Criterion of `estimate-orchestration-shows-the-built-case` promises that each showing is unchanged, so the reading failed. The other lines of the Criterion held in that reading.

The guard is in place and it worked. The comparison on `Stop` ran in session 1654, and `estimate-case-check-shows-only-the-checked-case` passed on exactly this refusal. There is no stronger guard. `Stop` fires on a reply the person already sees, so the hook can only refuse a showing, not stop it. The retyping stays an error of the agent, and the hook catches it. On the re-fire (`stop_hook_active`) the comparison exits 0. The hook does not refuse a second showing that differs, and only the reading by hand finds it.

The refusal of Case 433 in this session ("not built and checked by case-guppi") was not a showing that differed. Its cause is `SubagentHandback`, and Case 434 closes it. Case 434 does not change the comparison on `Stop`. The new lines of the Criterion speak only of a showing the comparison refused as different from the answer.

What `case-guppi` found in the frame. The section Who builds a Case in `rule-case-protocol` says that the agent shows the answer "whole and unchanged". As an instruction to the agent this sentence stays true. The Case adds to it what follows a refused showing, so that the Render and the Criterion promise the same thing. The Render is `vault/wiki/case-schema.md`, so `tasks` holds a render line. `estimate-case-check-shows-only-the-checked-case` does not change: it promises the comparison itself, and the comparison does not change. The other Estimates of `rule-case-protocol` speak of the loading, the form of a Case, the ledger lines, the acknowledging reply and deferred decisions, not of the showing. `estimate-case-build-writes-the-case` speaks of how `case-guppi` builds a Case. The lesson `lesson-case-show-sub-case-ratification-retyped` was recorded in another session, so the decision line carries no `addresses`, and the lesson stays `new`. The Case has no `create`, so no vault query is needed. The Criterion changes in this session, so its reading waits for the next one.

## Problem

The reading failed, but the guard against this error is in place and it worked: the person answered the correct Case. The decision is what the failure asks for: a new rule or guard, a new Criterion, or a new reading under the old Criterion.

## Given

`rule-case-protocol` — the rule of how a built Case is shown; its Who builds a Case changes
**＋** `vault/wiki/case-schema.md` — the Render of `rule-case-protocol`
**＋** `estimate-orchestration-shows-the-built-case` — the promise that the built Case is shown unchanged
**＋** `rule-case-check` — the `Stop` comparison of `uv run guppi casecheck`, which refuses a showing that differs from the answer
**＋** `rule-case-build` — the agent `case-guppi` that builds a Case
**＋** `rule-ask` — the agent `ask-guppi`, dispatched at pre-spec

## History

- 2026-09-26 created · raw/2026-09-26/1337/ledger.md#case-435
