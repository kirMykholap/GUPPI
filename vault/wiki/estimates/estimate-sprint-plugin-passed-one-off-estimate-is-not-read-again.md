---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether the form of a Case, case-guppi, pre-spec and the schema of an Estimate say that a passed one-off Estimate gets no update from a later Case and is no missed Estimate, while a pending or failed one is updated as before; read once
method: "by hand, after the librarian's run of session 2003: vault/wiki/case-schema.md, .claude/agents/case-guppi.md, .claude/skills/pre-spec/SKILL.md and vault/wiki/estimates/schema.yaml read against the Criterion, the sentences found in the estimate line"
origin: raw/2026-11-25/2003/ledger.md#case-1063.1
sprint: plugin
created: 2026-11-25
tags: [sprint, workflow]
once: true
---

## Criterion

When:
The agent reads `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md` and `vault/wiki/estimates/schema.yaml` after the render of `rule-case-protocol`, `rule-case-build`, `rule-prespec` and `rule-estimates-schema`.

Then:
`vault/wiki/case-schema.md` says that a later Case gives a passed Estimate with `once: true` no `update` and does not set it `pending`.
**＋** `vault/wiki/case-schema.md` says that an Estimate with `once: true` that is `pending` or `failed` is updated as any other, and that a Case that needs the same state checked again creates a new one-off Estimate.
**＋** `.claude/agents/case-guppi.md` says that a passed Estimate with `once: true` that the Case does not name is no contradiction.
**＋** `.claude/skills/pre-spec/SKILL.md` says that a passed Estimate with `once: true` that the Case does not name is no finding.
**＋** `vault/wiki/estimates/schema.yaml` says, in the description of the field `once`, that a passed one-off Estimate is not read again.
**＋** The `## Backlog` of `entity-sprint-plugin` no longer asks whether a passed one-off Estimate is read again.
**－** In `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md` and `.claude/skills/pre-spec/SKILL.md`, an Estimate without `once` whose Criterion speaks of what a Case changes still gets an `update` from that Case.

## History

- 2026-11-26 created · [[decision-case-1063.1]]
