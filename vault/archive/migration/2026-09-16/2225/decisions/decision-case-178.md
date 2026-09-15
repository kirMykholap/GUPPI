---
type: decision
case: "178"
status: archived
defer: ["[[rule-plan-mode]]"]
superseded_by: ["[[decision-case-182]]"]
origin: raw/2026-09-15/1809/ledger.md#case-178
sprint: migration
created: 2026-09-15
tags: [session, workflow]
---

## Context

The Criterion of an Estimate page is a head text plus one `### case N` block per contract change; the script appends the blocks one after another and removes one only by `{supersedes:case N}` on a decision line. No judgment says whether a new block contradicts an old one: a script writes. The one check that catches a contradiction is pre-task through `ask-guppi`, at the exit of Plan Mode; in sessions R and S it caught 124.2 (Case 171) and 130.2 (Case 177), and both times a Case of its own was added to carry the `supersedes`.

## Problem

Old criteria pile up on the page even when they are no longer needed, and the removal is decided after the signature, not before. Who reads the blocks and names the removal: the Case at its forming — `given` carries the blocks of the Estimate and the `supersedes` of the contradicting one, the plan file checked by `pretask --check` before the ratification question — or the librarian at `generate`, by what it received. A question of the next Plan Mode.

## History

- 2026-09-15 created · raw/2026-09-15/1809/ledger.md#case-178
- 2026-09-16 superseded by decision-case-182 · [[decision-case-182]]
- 2026-09-16 archived · superseded
- 2026-09-16 archived · cleanup
