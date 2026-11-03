---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether Cases out at the same time by a route other than the two batches already set are a batch, so that no Case is shown while a round of another Case stands unanswered
method: "by hand at Retro of the session that replaces this Criterion: the Render of rule-orchestration in vault/wiki/orchestration.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
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

2026-10-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
