---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names or acts at the same moment, by its id, one sentence on what it sets and the path of its case file
method: by hand at the close of a later session after the render, each Agent call to case-guppi in the transcript read against the Cases ratified or shown before it; a related Case not named, and a named Case without its sentence or its case file, counted in the reading line
checked: 2026-10-02
origin: raw/2026-10-01/1441/ledger.md#case-579.1
sprint: migration
created: 2026-10-01
tags: [session, workflow]
---

## Criterion

When:
The main agent dispatches `case-guppi` by an `Agent` call to build the Case of a Frontier item, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
**＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
**＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
**－** A Case of the session that changes no page the item names and acts at another moment need not stand in the prompt.
**－** When no Case of the session is related, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

## Result

2026-10-02, the close of session 2049, by hand: five Agent calls to case-guppi; 596 named none, no Case before it; 597 named 596; 598 named 596 and 597; 599 named 598; 600 named 598, 599 and 597; each named Case by its id, one sentence on what it sets and which pages it changes, and its case file path; 596 was not named for 599 and 600, which change no page it names and act at another moment; no prompt sent case-guppi to search the Cases of the session; 0 related Cases left unnamed

## History

- 2026-10-01 created · [[decision-case-579.1]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1725/ledger.md#L15
- 2026-10-02 renamed from `estimate-case-protocol-names-related-cases-in-the-dispatch` · [[decision-case-595.15]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the dispatch as orchestration.md sets it (case 595.15) · [[decision-case-595.15]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L29
