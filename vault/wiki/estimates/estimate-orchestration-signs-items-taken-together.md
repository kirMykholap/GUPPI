---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether, when the person's one answer takes up two or more Frontier items, the main agent shows their rounds in one list and their Cases in one reply for one ratification, with the waits marked
method: "by hand at the Retro of the session that took up the Cases of a batch together with a Case built again: the replies in its transcript from the dispatch of those Cases to the reply that acknowledged that batch, read against the Criterion (session 2249, Cases 682 and 683 with Case 681 built again)"
origin: raw/2026-10-05/2249/ledger.md#case-684.1
sprint: migration
created: 2026-10-05
tags: [session, workflow]
---

## Criterion

When:
In Plan Mode before `/pre-spec`, one answer of the person takes up two or more items of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The main agent dispatches a `case-guppi` for each item, and shows no round and no Case of them alone: they are one batch.
**＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
**＋** It shows one list of every round that came back, each question numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
**＋** A question whether another Case is built again, which a line `**Other Case:**` in a summary of the batch raises, stands in that list, numbered under the Case that raised it, before any Case of the batch is shown. On the person's yes, that other Case goes back to its `case-guppi` and joins the batch.
**＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification. The person ratifies the batch at once or names the ids.
**－** An item the person takes up alone is shown alone, and the next item waits until its Case is ratified or deferred.
**－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

## Result

2026-10-06, the transcript of session 2249, the batch of Cases 682 and 683 with 681 built again: no answer shown alone, a Waiting line at each answer while another was out, the round of 682 shown as one list numbered 682.Q1–Q3, the three Cases shown in one reply and ratified at once

## History

- 2026-10-06 created · [[decision-case-684.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-05/2249/ledger.md#L23
- 2026-10-15 updated: the pointers of the method stand in a bracket at its end · [[decision-case-823.1]]
