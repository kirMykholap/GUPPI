---
type: estimate
kind: QA
status: pending
target: "[[rule-orchestration]]"
purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names, acts at the same moment, or sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind, by its id, one sentence on what it sets and the path of its case file, and each other Case of a batch of items the person took up in one answer
method: "by hand, after the first dispatch of case-guppi under the new Render of rule-orchestration in which a Case of the session sets the form of a text a check reads and the Case of the item may write text of that kind: the Agent call of that dispatch in its transcript, read against the Criterion; a related Case left unnamed counted in the reading line"
checked: 2026-10-06
origin: raw/2026-10-01/1441/ledger.md#case-579.1
sprint: migration
created: 2026-10-01
tags: [session, workflow]
---

## Criterion

When:
The main agent dispatches `case-guppi` by an `Agent` call to build the Case of an item of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
**＋** The prompt also names each Case of the session, ratified or already shown, that sets the form of a text a check reads, or how the check reads it, when the Case of the item may write text of that kind, such as the `method` of an Estimate.
**＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
**＋** When the item is one of two or more items that one answer of the person took up, the prompt also names each other Case of that batch by its id and its Frontier item, and by the path of its case file where that file stands.
**＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
**－** A Case of the session that changes no page the item names, acts at another moment, sets no form of a text of a kind the Case of the item may write and is no Case of the same batch need not stand in the prompt.
**－** A Case that only writes a text a check reads, and sets no form of it, is not related by that text alone.
**－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

## Result

2026-10-06, the transcript of session 2249: the Agent call of Case 682 named Case 683 by id and Frontier item C12 and Case 681 with its case file; the call of Case 683 named Case 682 by id and C11, Case 681 with its case file, and Cases 676, 677, 679, 680 with their files

## History

- 2026-10-01 created · [[decision-case-579.1]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1725/ledger.md#L15
- 2026-10-02 renamed from `estimate-case-protocol-names-related-cases-in-the-dispatch` · [[decision-case-595.15]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the dispatch as orchestration.md sets it (case 595.15) · [[decision-case-595.15]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L29
- 2026-10-06 updated: the Criterion replaced whole — the prompt of a builder in a batch names each other Case of the batch; the purpose and the method set anew (case 684.2) · [[decision-case-684.2]]
- 2026-10-06 status: pending → passed · raw/2026-10-05/2249/ledger.md#L24
- 2026-10-15 updated: the pointers of the method stand in a bracket at the end of their sentence · [[decision-case-823.1]]
- 2026-10-30 updated: the Criterion replaced whole — a Case that sets the form of a text a check reads is related to an item whose Case may write text of that kind; purpose and method set anew · [[decision-case-938]]
