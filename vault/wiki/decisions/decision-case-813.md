---
type: decision
case: "813"
status: current
update: ["[[rule-orchestration]]", "[[estimate-ratification-case-id-carries-the-sprint]]"]
origin: raw/2026-10-14/1536/ledger.md#case-813
sprint: plugin
created: 2026-10-14
tags: [session, workflow, harness, ledger]
---

## Problem

`orchestration.md` does not tell the main agent that each run of `guppi caseid --next` holds a new id, so the agent ran it to check an id and held one that no Case uses.

## Recommend

- **How do we stop a run that only checks from holding an id?**
  - Recommended: (a) a sentence in `orchestration.md` only: the main agent runs the command only to get the id of a new top-level Case, once for each Case, and never to check an id; no code changes.
  - Answer: agreed, (a).
- **Which Estimate checks the fix?**
  - Recommended: (a) replace the Criterion of `estimate-ratification-case-id-carries-the-sprint` with one more line, read at the Retro of this session against the new Render of `orchestration.md`.
  - Answer: agreed, (a).

## History

- 2026-10-14 created · raw/2026-10-14/1536/ledger.md#case-813
