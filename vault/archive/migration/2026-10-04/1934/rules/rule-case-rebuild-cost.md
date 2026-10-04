---
type: rule
purpose: Prevents a Case from being rewritten whole and returned whole into the main agent's context when only a sub-case changed, and its context from listing searches that change nothing; options from session 2356 - the SubagentStop hook merges a changed sub-case into the stored answer, case-guppi writes the Case file itself and returns a short answer, the context keeps only what changes the decision, a large item split into several Cases
status: archived
origin: raw/2026-09-30/2356/ledger.md#case-566
sprint: migration
created: 2026-09-30
---

## Purpose

Prevents a Case from being rewritten whole and returned whole into the main agent's context when only a sub-case changed, and its context from listing searches that change nothing; options from session 2356 - the SubagentStop hook merges a changed sub-case into the stored answer, case-guppi writes the Case file itself and returns a short answer, the context keeps only what changes the decision, a large item split into several Cases

## History

- 2026-10-01 deferred, placeholder · [[decision-case-566]]
- 2026-10-01 deferred · [[decision-case-570]]
- 2026-10-04 defer by decision-case-566 superseded · [[decision-case-629.2]]
- 2026-10-04 defer by decision-case-570 superseded · [[decision-case-629.2]]
- 2026-10-04 deleted · [[decision-case-629.2]]
- 2026-10-04 archived · cleanup
