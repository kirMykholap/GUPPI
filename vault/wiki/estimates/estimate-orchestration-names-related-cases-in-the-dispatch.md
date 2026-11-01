---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names, acts at the same moment, or sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind and the change may alter what the check answers on it, by its id, one sentence on what it sets and which pages it changes, and the path of its case file, and each other Case of a batch of items the person took up in one answer
method: "by hand, after the librarian's render of this Criterion's rule text into vault/wiki/orchestration.md: at the Retro of the first session that runs on that render, each Agent call of that session that dispatched case-guppi for the Case of an item, read in the transcript of the session under ~/.claude/projects/ against the Criterion, only the Cases the Criterion counts as related judged and a Case named beyond them not counted, a related Case left unnamed or named without its sentence, the pages it changes or the path of its case file counted in the reading line and the transcript named (the first session after 2026-11-01/1721)"
checked: 2026-11-01
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
**－** A Case whose change to a check leaves the answer of that check the same on each text the Case of the item may write is not related by that change.
**－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

## Result

2026-11-01, Retro of session 2038, the Agent calls that dispatched case-guppi in the transcript ~/.claude/projects/c--PROJECTS-GUPPI/dbf67938-c4f7-44d4-8502-a6d55d47c17a.jsonl, lines 113 and 237: 2 dispatches; the dispatch of Case 990 named no Case, none of the session standing before it; the dispatch of Case 991 named Case 990 with its id, one sentence on what it sets, its pages and the path of its case file; no related Case left unnamed; Case 992 was built by SendMessage to the case-guppi of Case 990, not by an Agent call

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
- 2026-10-31 updated: the method reads the dispatch of Case 961 in the transcript of session 0431, the Criterion written back unchanged · [[decision-case-961.2]]
- 2026-10-31 status: pending → failed · raw/2026-10-31/0431/ledger.md#L46
- 2026-10-31 deferred · [[decision-case-971]]
- 2026-11-01 deferred · [[decision-case-976]]
- 2026-11-01 defer by decision-case-971 superseded · [[decision-case-980]]
- 2026-11-01 defer by decision-case-976 superseded · [[decision-case-980]]
- 2026-11-01 updated: the method reads the dispatches of session 0141 at its Retro and the purpose names the pages of a related Case, the Criterion written back unchanged; the defers of cases 971 and 976 retired · [[decision-case-980]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/0141/ledger.md#L14
- 2026-11-01 updated: the Criterion replaced whole — a change to a check that keeps its answer on each text the Case of the item may write makes no related Case; purpose and method set anew, the reading after the render · [[decision-case-984]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/2038/ledger.md#L14
