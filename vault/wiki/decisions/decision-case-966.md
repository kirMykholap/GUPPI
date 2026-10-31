---
type: decision
case: "966"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-reads-the-readers-of-a-changed-step]]"]
origin: raw/2026-10-31/1831/ledger.md#case-966
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Problem

A builder that searches only for the words of a changed step misses the skill that carries the step out under other words, so `/pre-spec` finds the miss after the person has ratified the Case.

## Recommend

- **How the builder finds a text that does the same step**
  - Recommended: (a) follow the step to the agent, skill or hook that carries it out, and to each skill such an agent loads by its `skills` field.
  - Answer: (a), as recommended.
- **How the change is checked**
  - Recommended: (a) keep the Criterion of `estimate-case-build-reads-the-readers-of-a-changed-step` word for word and set it to wait for a new reading, its method waiting for the `/pre-spec` of a session on the new Render.
  - Answer: (a), as recommended.
- **Whether this Case also covers Frontier C6**
  - Recommended: (a) separate Cases; this Case changes only the sentence on the texts that do the same step.
  - Answer: (a), as recommended; a graph of the links becomes a new Frontier item, with no Case yet.

## History

- 2026-10-31 created · raw/2026-10-31/1831/ledger.md#case-966
