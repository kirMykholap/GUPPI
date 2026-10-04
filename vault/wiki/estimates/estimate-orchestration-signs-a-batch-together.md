---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether, when the person's word asks that a ratified Case change while another Case is built, the main agent sends it back and shows the two Cases together for one ratification, with the rounds gathered and the waits marked as after the findings of pre-spec
method: "by hand at a Plan Mode of a later session in which the person's word asks that a ratified Case change: the SendMessage calls and the replies from that word to the acknowledging reply, read in the transcript"
checked: 2026-10-04
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
**＋** The person ratifies the batch at once or names the ids. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or in a new batch with each Case it asks to change.
**－** Outside a batch and the loop after the findings of `/pre-spec`, the main agent does not take up the next item of `raw/<date>/<hi HHMM>/frontier.md` before the shown Case is ratified or deferred.
**－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

## Result

2026-10-04, at the /hi of session 1934, by hand: transcript 8b8ce20f of session 1439: the person's word at 17:45:25 asked a change of the ratified Case 627 while Case 628 was built; the main agent sent 627 back to its case-guppi by SendMessage at 17:46:32 and showed neither Case alone; the six turns while an answer was out (17:46:34, 17:47:21, 17:52:03, 18:04:06, 18:05:56, 18:11:22) each held one line opening with **Waiting:** naming who answered and who was out, and the Stop hooks refused none; the rounds of 628 were shown numbered 628.Q1–Q4, 628.Q5, 628.Q6, 628.Q11, each answer sent to the case-guppi of 628 verbatim; at 18:19:51 both case files went by one SendUserFile and the reply of 18:20:18 showed both Cases under their Russian headings with one ratification fence; the person ratified both with one word; the second batch, 627.1 with 628.1 at 18:28:39–18:31:55, took the same steps; the reply of 18:23:19, after the hook ratified refused 628.1, held text before its Waiting line, a send-back by the hook and not by the person's word, so outside the When; not exercised: a third Case joining a batch, rounds of two Cases out at once, a Case the person questions inside a batch

## History

- 2026-10-02 created · [[decision-case-598.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/1934/ledger.md#L2
