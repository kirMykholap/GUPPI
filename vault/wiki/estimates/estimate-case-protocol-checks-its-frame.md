---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: A Case that changes the behaviour of a rule or a hook is checked by frame-guppi before it is shown
method: by hand, the Cases of a session at its close, their context against the Agent calls of the event log
origin: raw/2026-09-24/1303/ledger.md#case-391.2
sprint: migration
created: 2026-09-24
tags: [session, workflow]
---

## Criterion

When:
The agent prepares a Case that changes the behaviour of a rule or of a hook, before its first showing in the chat, and again before a showing after its `given` changed.

Then:
The agent dispatches `frame-guppi` with the lines of the Case's `given` and a few lines on what it changes, in the prompt of the call; nothing of the Case stands in the chat before the answer.
**＋** Each contradiction the answer names is fixed in the Case before it is shown, or the Case says why it stands.
**＋** The `context` of the Case gives what was read and what was found, or that nothing was found.
**＋** Before a showing again, the dispatch carries only the lines of `given` added since the last dispatch and the pages changed since.
**－** A Case that changes no behaviour of a rule or of a hook dispatches nothing.

## History

- 2026-09-24 created · [[decision-case-391.2]]
