---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names or acts at the same moment, by its id, one sentence on what it sets and the path of its case file
method: by hand at the close of a later session after the render, each Agent call to case-guppi in the transcript read against the Cases ratified or shown before it; a related Case not named, and a named Case without its sentence or its case file, counted in the reading line
checked: 2026-10-01
origin: raw/2026-10-01/1441/ledger.md#case-579.1
sprint: migration
created: 2026-10-01
tags: [session, workflow]
---

## Criterion

When:
The main agent dispatches `case-guppi` by an `Agent` call to build the Case of a Frontier item, with `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

Then:
The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
**＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
**＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
**－** A Case of the session that changes no page the item names and acts at another moment need not stand in the prompt.
**－** When no Case of the session is related, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

## Result

2026-10-01, by hand, session 1725, the three Agent calls to case-guppi (cases 582, 583, 584) read against the Cases ratified before each: no Case of the session changed a page of the item or acted at its moment, so 0 related Cases not named; each prompt held the Case id, the Frontier item with its source and the person's words; the prompt of 583 named 582 as unrelated with a sentence and its case file, the prompt of 584 named 582 and 583 as unrelated with a sentence each and no case file, which the Criterion asks only of a related Case

## History

- 2026-10-01 created · [[decision-case-579.1]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1725/ledger.md#L15
