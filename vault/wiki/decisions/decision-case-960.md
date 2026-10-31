---
type: decision
case: "960"
status: current
children: ["[[decision-case-960.1]]", "[[decision-case-960.2]]", "[[decision-case-960.3]]"]
origin: raw/2026-10-31/0431/ledger.md#case-960
sprint: plugin
created: 2026-10-31
tags: [schema, workflow, harness, render, session, ledger, case-build]
---

## Problem

A reading by hand may point at a text that stood only in the chat of a session, so it cannot be taken once that chat ends. No rule says where the evidence of a reading must stand.

## Recommend

- **Where the evidence of a reading may stand**
  - Recommended: (a) a saved file, a transcript included: a file of the repository, the output of a command, or the transcript of the session under `~/.claude/projects/`.
  - Answer: agreed, (a).
- **Which texts carry the new rule**
  - Recommended: (c) both texts, the field `method` of `rule-estimates-schema` and one sentence of `case-schema.md`, with no lint check.
  - Answer: agreed, (c).
- **How the two methods change**
  - Recommended: (a) any event of the kind, read in its transcript, read in this session.
  - Answer: agreed, (a).
- **Which methods this Case fixes**
  - Recommended: (a) the two Estimates, and a change asked of the Case of this session.
  - Answer: agreed, (a).
- **How the new rule is checked**
  - Recommended: (a) a new Estimate on `rule-estimates-schema`.
  - Answer: agreed, (a).

## History

- 2026-10-31 created · raw/2026-10-31/0431/ledger.md#case-960
