---
type: insight
pattern: case_out of the hook of rule-prespec-onward takes a Case file written after the last decision line it reads as a Case still out, and a Case can end with no decision line after its file, ratified again with unchanged lines or built and dropped, so the hook stays silent for the rest of Plan Mode
status: archived
children: ["[[lesson-prespec-onward-re-ratification-out-after-its-stretch]]", "[[lesson-prespec-onward-an-empty-case-file-keeps-it-silent]]"]
severity: 0
addressed_by: "[[decision-case-701.1]]"
origin: raw/2026-10-07/0211/ledger.md#L48
sprint: migration
created: 2026-10-07
tags: [hooks, workflow, orchestration]
---

## Pattern

Two lessons, one cause. In session 2049 Case 596 was ratified again with the decision lines the ledger already held, so case-596.md stood newer than its last decision line and uv run guppi onward --plan stayed silent once the stretch of the re-ratification had passed. In session 0211 case-guppi wrote cases/case-700.md for a Case 700 that was then dropped and never ratified; the file has no decision line, so case_out printed True and the hook stayed silent after /pre-spec. In both, the hook learns that a Case is no longer out only from a decision line written after its file, and these two ends of a Case write none.

## Proposal

A suggestion: let the end of a Case that writes no new decision line, a re-ratification with unchanged lines or a dropped Case, leave a mark the hook reads, or let case_out leave out a Case file that no ledger line and no reply names, as the For the next session of handoff 0211 asks to decide.

## History

- 2026-10-07 created · raw/2026-10-07/0211/ledger.md#L48
- 2026-10-07 updated: actioned: case 604 counts a re-ratification with unchanged lines for the rest of the session, and case 701 makes the emptied file of a dropped Case count as no Case · [[decision-case-701.1]]
- 2026-10-07 updated: its tag orchestration is registered in tags.md (case 704) · [[decision-case-704]]
- 2026-10-07 updated: addressed_by: decision-case-701.1, the decision that set it actioned (case 706) · [[decision-case-706]]
- 2026-10-10 status: actioned → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
