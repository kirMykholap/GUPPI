---
type: decision
case: "717"
status: archived
children: ["[[decision-case-717.1]]", "[[decision-case-717.2]]", "[[decision-case-717.3]]"]
origin: raw/2026-10-07/1804/ledger.md#case-717
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness, ledger, hooks]
---

## Problem

A dispatch of `case-guppi` costs more than its work needs. It reads examples it does not use, it reads background sources whole when it needs only a few lines, and it writes its whole context into the cache again after each pause longer than five minutes.

## Recommend

- **Where do the examples of the Case form go?**
  - Recommended: (a) both examples go to a new file, made from a new rule page; `case-schema.md` keeps all its rules and points to the new file, and the test of the sample Case reads it from there.
  - Answer: agreed, (a).
- **When does the agent read the examples file?**
  - Recommended: (a) once in a dispatch, just before it first writes a Case file; a dispatch that only asks questions never reads it.
  - Answer: agreed, (a).
- **What does the agent read whole, and what in parts?**
  - Recommended: (a) whole: `case-schema.md`, `ratification.md`, each page the Case changes and the promise text of each Estimate of such a page; in parts: case files of other Cases (searched first, read whole on a hit), the brief, the handoff, background pages and code (the functions the Case changes and the places that use them); independent reads in one turn.
  - Answer: agreed, (a).
- **Does the cache of `case-guppi` last longer than 5 minutes?**
  - Recommended: (a) one hour for `case-guppi` only, set in its agent file.
  - Answer: agreed, (a).
- **How do we check that the change works?**
  - Recommended: (a) rewrite the promise of the agent's work and the promise of the sample Case; no limit on tokens; the tokens of each run are recorded as before.
  - Answer: agreed, (a).
- **How does the agent read the case files of the related Cases the main agent names?**
  - Recommended: (a) whole for the Cases the prompt names and the Cases a finding of the check names; a search first, then the whole file on a hit, for other case files.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#case-717
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
