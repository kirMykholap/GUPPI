---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
purpose: Whether the form of a Case and the schema of an Estimate say that an Estimate off a sprint page reads no transcript, that a promise checked in a transcript takes a lasting Estimate that reads a text that ships and a one-off Estimate of the sprint page, for each Estimate a Case creates, gives a new method or gives a new Criterion, and that pre-spec reports a break
method: "by hand, at the Retro of the session that sets this Criterion: the new Render of rule-case-protocol and of rule-estimates-schema and the update of entity-sprint-plugin in the Spec read against the Criterion, recorded in the estimate line"
origin: raw/2026-11-26/1515/ledger.md#case-1071.1
sprint: plugin
created: 2026-11-26
tags: [harness, workflow]
---

## Criterion

When:
`case-guppi` reads `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, to write the `method` of an Estimate, or a reader reads the fields `method` and `once` of `vault/wiki/estimates/schema.yaml`, rendered from `rule-estimates-schema`.
**＋** A reader opens the `## Backlog` of `entity-sprint-plugin`.

Then:
Both texts say that an Estimate whose target is not a sprint page `entity-sprint-<id>` reads no transcript of a session in its `method`.
**＋** Both say that a promise whose check reads what an agent did in a transcript takes two Estimates: a lasting one on the page of the promise, whose `method` reads a text that ships — a test, a command, or the text of a page in the Spec at Retro or in the file rendered from it — and a one-off Estimate of the live sprint page with `once: true`, whose `method` reads the transcript.
**＋** Both say that this binds each Estimate that a Case creates, gives a new `method` or gives a new Criterion, and that `guppi prespec --check` of `.guppi/guppi/prespec.py` reports one that breaks it.
**＋** The field `once` of `vault/wiki/estimates/schema.yaml` names what an agent did in the transcript of a session among the states that a one-off Estimate checks.
**＋** The `## Backlog` of `entity-sprint-plugin` no longer asks whether every Estimate that reads a transcript is split.
**－** An Estimate that stands with a transcript reading keeps it until a Case gives it a new `method` or a new Criterion.
**－** A Criterion written back word for word to set an Estimate `pending` again is no new Criterion.
**－** A test over a made-up transcript reads no transcript of a session.

## Result

2026-11-26, Retro, vault/raw/2026-11-26/1515/spec.md Case 1071.1: the new sentences of rule-case-protocol and rule-estimates-schema say that an Estimate off a sprint page reads no transcript, that such a promise takes a lasting Estimate reading a test, a command or the text of a page in the Spec or its rendered file and a one-off Estimate of the live sprint page with once: true, that this binds each Estimate a Case creates or gives a new method or Criterion, that a Criterion written back word for word is none, and that guppi prespec --check reports a break; the field once names what an agent did in a transcript; the pair of entity-sprint-plugin removes the Backlog question

## History

- 2026-11-26 created · [[decision-case-1071.1]]
- 2026-11-26 status: pending → passed · raw/2026-11-26/1515/ledger.md#L39
