---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: A Case is built by case-guppi and shown by the main agent unchanged
method: by hand, the Cases of a session at its close, their context against the Agent calls of the event log
checked: 2026-09-25
origin: raw/2026-09-24/1303/ledger.md#case-391.2
sprint: migration
created: 2026-09-24
tags: [session, workflow]
---

## Criterion

When:
The main agent takes up a Frontier item, the person answers a round of questions or answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

Then:
The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
**＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case.
**＋** An answer with no Case heading is a round of questions: the main agent shows it translated into Russian, slugs, paths and quotations unchanged, and no Case is shown.
**＋** No step of confirmation follows the last round: the next showing is the Case.
**＋** The main agent shows the Case of the answer whole at every showing — its name, `context`, `problem` and `recommend` translated into Russian, its `given`, `when`, `then`, `tasks` and `ratification` as the answer holds them — and its own text after one horizontal rule; a showing that the `Stop` comparison of `rule-case-check` refuses is followed, before the person answers, by a reply that shows the answer whole, translated the same way.
**＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is shown and ratified again; the main agent edits no Case in the plan file.
**＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
**－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch.

## Result

2026-09-25, by hand, the Cases of session 1654 against its Agent calls: each of Cases 425–432 was built by a case-guppi dispatch that carried the Case id, the Frontier item, its source and the person's words; the person's questions and changes went to the same agent by SendMessage (427, 428, 429, 430); the answers without a Case heading (427, the first answer of C5+C9) were put to the person as questions and no Case was shown; the plan file stood with its title line before the first dispatch; ask-guppi was dispatched once, at pre-spec. Failed on one showing: the first showing of sub-case 428.3 carried the ledger line of 428.2 under its ratification, retyped by the agent; the Stop comparison of casecheck refused it and 428.3 was shown again unchanged (lesson-case-show-sub-case-ratification-retyped)

## History

- 2026-09-24 created · [[decision-case-391.2]]
- 2026-09-25 renamed from `estimate-case-protocol-checks-its-frame` · [[decision-case-419.1]]
- 2026-09-25 updated: renamed; the Criterion replaced whole — the Case built by case-guppi and shown unchanged (case 419.1) · [[decision-case-419.1]]
- 2026-09-25 status: pending → failed · raw/2026-09-25/1654/ledger.md#L25
- 2026-09-26 updated: the Criterion replaced whole — the Case the person answers is the answer unchanged; a showing the Stop comparison refuses is followed by the answer shown unchanged (case 435) · [[decision-case-435]]
- 2026-09-26 updated: the Criterion replaced whole — the prose translated for the chat, every showing whole, a changed Case through its case-guppi, the short form in English (case 441.2) · [[decision-case-441.2]]
- 2026-09-27 updated: the Criterion replaced whole — a round shown translated, the answers passed verbatim, no step of confirmation (case 443.3) · [[decision-case-443.3]]
