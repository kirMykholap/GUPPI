---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether Cases out at the same time by a route other than the two batches already set are a batch, so that no Case is shown while a round of another Case stands unanswered
method: "by hand at Retro of the session that replaces this Criterion: the Render of rule-orchestration in vault/wiki/orchestration.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-29
origin: raw/2026-10-08/0050/ledger.md#case-730.1
sprint: migration
created: 2026-10-08
tags: [session, workflow]
---

## Criterion

When:
In Plan Mode before `/pre-spec`, a Case of the session goes back to its `case-guppi` — the person questions or changes it, or the person drops a change to it and its `case-guppi` undoes the change — while the `case-guppi` of another Case has not answered or a round of another Case stands unanswered, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The Cases out at the same time are one batch, and take the steps of a batch that `vault/wiki/orchestration.md` sets until each is ratified or deferred.
**＋** The main agent shows no Case while a round of another Case of the batch stands unanswered: a Case that comes back built waits, and is not shown.
**＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line under the bold label `**Waiting:**`, translated, that names the Cases that have answered and those still out, and nothing else.
**＋** It shows every round that came back in one list, each question numbered `<Case id>.Q<n>`, and sends each answer to the `case-guppi` of its Case, all in one message.
**＋** It shows every Case of the batch in one reply, for one ratification.
**－** A Case that goes back while no other Case of the session is out is shown again alone.
**－** A batch of items that one answer of the person takes up, and a batch of a ratified Case asked to change while another Case is built, are no moment of this promise.
**－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

## Result

2026-10-29, Retro of session 0327: vault/wiki/orchestration.md, ## Showing and signing a Case: Cases out at the same time by any other route before /pre-spec — a Case the person questions or changes, or one whose dropped change its case-guppi undoes, while another case-guppi has not answered or a round stands unanswered — are a batch and take its steps until each is ratified or deferred; a Case that comes back built while a round of another stands unanswered waits and is not shown; the steps set the **Waiting:** line naming the Cases answered and out, one list of rounds numbered <Case id>.Q<n>, the answers in one message and every Case shown in one reply; a sub-case questioned or changed is shown again alone when no other Case is out; the loop after /pre-spec is left to rule-prespec

## History

- 2026-10-08 created · [[decision-case-730.1]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/0050/ledger.md#L13
- 2026-10-29 updated: the Criterion replaced whole — it names no Estimate that the clean version does not hold; the method reads the Render as it stands · [[decision-case-901.2]]
- 2026-10-29 status: pending → passed · raw/2026-10-29/0327/ledger.md#L38
