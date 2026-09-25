---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: A Case is built by case-guppi and shown by the main agent unchanged
method: by hand, the Cases of a session at its close, their context against the Agent calls of the event log
origin: raw/2026-09-24/1303/ledger.md#case-391.2
sprint: migration
created: 2026-09-24
tags: [session, workflow]
---

## Criterion

When:
The main agent takes up a Frontier item that needs a Case, the person answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

Then:
The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call; nothing of the Case stands in the chat before the answer.
**＋** A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`.
**＋** The main agent shows the Case of the answer whole and unchanged, and its own text stands after one horizontal rule.
**＋** An answer that holds no Case heading is a question the main agent puts to the person, and no Case is shown.
**＋** The plan file stands with its title line before the first dispatch of the session.
**＋** The main agent dispatches `ask-guppi` once, at pre-spec, and neither `ask-guppi` nor `frame-guppi` before a showing.
**－** A deferred decision in the short form is written by the main agent, with no dispatch.

## History

- 2026-09-24 created · [[decision-case-391.2]]
- 2026-09-25 renamed from `estimate-case-protocol-checks-its-frame` · [[decision-case-419.1]]
- 2026-09-25 updated: renamed; the Criterion replaced whole — the Case built by case-guppi and shown unchanged (case 419.1) · [[decision-case-419.1]]
