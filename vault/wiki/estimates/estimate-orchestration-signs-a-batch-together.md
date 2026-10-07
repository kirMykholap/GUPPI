---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether, when the person's word asks that a ratified Case change while another Case is built, the main agent sends it back and shows the two Cases together for one ratification, with the rounds gathered and the waits marked as after the findings of pre-spec
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
checked: 2026-10-08
origin: raw/2026-10-02/2049/ledger.md#case-598.1
sprint: migration
created: 2026-10-02
tags: [session, workflow]
---

## Criterion

When:
In Plan Mode before `/pre-spec`, the person's answer to a round of a `case-guppi`, or the person's word on a shown Case, asks that a Case already ratified in the session change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The main agent sends the ratified Case back to its `case-guppi` by `SendMessage`, and shows neither that Case nor the Case being built alone: the two are one batch.
**＋** A Case that a Case of the batch asks to change in the same way joins the batch.
**＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
**＋** It shows one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
**＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
**＋** The person ratifies the batch at once or names the ids. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone only when no other Case of the session is out, or in a new batch with each Case it asks to change; while another Case is out, it is shown as `estimate-orchestration-batches-cases-out-at-once` sets it.
**－** Outside a batch and the loop after the findings of `/pre-spec`, the main agent does not take up the next item of `raw/<date>/<hi HHMM>/frontier.md` before the shown Case is ratified or deferred.
**－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

## Result

2026-10-08, Retro of session 0050, the new Render of rule-orchestration in spec.md (Case 730.1) against the Criterion of Case 730.2: the ratified Case sent back and the Case being built are one batch, a Case asked to change in the same way joins it, the Waiting line, one list of rounds numbered <Case id>.Q<n>, every Case shown in one reply, the person ratifies at once or names ids; a Case questioned or changed is shown again alone only when no other Case of the session is out, otherwise in a batch per the new route; no next item before the shown Case is ratified or deferred outside a batch; the loop after /pre-spec unchanged

## History

- 2026-10-02 created · [[decision-case-598.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/1934/ledger.md#L2
- 2026-10-08 updated: the Criterion replaced whole — a Case is shown again alone only when no other Case is out, and otherwise as estimate-orchestration-batches-cases-out-at-once sets it; the method reads the new Render at Retro (case 730.2) · [[decision-case-730.2]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/0050/ledger.md#L14
