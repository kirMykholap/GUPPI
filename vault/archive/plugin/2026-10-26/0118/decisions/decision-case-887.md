---
type: decision
case: "887"
status: archived
defer: ["[[rule-case-check]]", "[[rule-orchestration]]"]
superseded_by: ["[[decision-case-890.1]]", "[[decision-case-890.3]]"]
origin: raw/2026-10-17/2307/ledger.md#case-887
sprint: plugin
created: 2026-10-17
tags: [hooks, harness, workflow, session]
---

## Context

At /pre-spec of session 2307 the Stop check of rule-case-check refused the showing of Case 881 three times on 881.24. `other_blocks` of .guppi/guppi/casecheck.py takes the part Case 883 wrote into `entity-glossary` from the plan, where 883 stood as ratified before /pre-spec, and `unread_sentences` looks for that part in a Read of the current file of Case 883, which /pre-spec had changed. Since orchestration.md shows every Case of a batch together for one ratification, the one refusal held back the four other Cases, which had no finding. The person put both off to the next session, and asked that it weigh ratifying the Cases with no finding first and taking up the one with a finding after.

## Problem

No Case of this session decides how the check reads a sibling built again, or whether a batch may be ratified in parts when the check refuses one of its Cases.

## Deferred

### [[rule-case-check]]

The check of the pairs of the session takes the part another Case wrote from the plan as last ratified and looks for it in a read of that Case's current file, so a sibling built again at /pre-spec makes a showing fail until it is ratified again; put off in session 2307

### [[rule-orchestration]]

A batch is shown and ratified whole, so one Case the check refuses holds back the Cases with no finding; the person asks whether those are ratified first and the Case with a finding taken up after; put off in session 2307

## History

- 2026-10-26 created · raw/2026-10-17/2307/ledger.md#case-887
- 2026-10-26 superseded by decision-case-890.1 · [[decision-case-890.1]]
- 2026-10-26 superseded by decision-case-890.3 · [[decision-case-890.3]]
- 2026-10-26 archived · superseded
- 2026-10-26 archived · cleanup
