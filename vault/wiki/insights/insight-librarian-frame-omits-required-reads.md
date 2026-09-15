---
type: insight
pattern: The frame of the librarian names the reads it allows one by one, and the list is shorter than the judgments the librarian must make; the agent then breaks a clause or judges on an index line alone.
status: open
children: ["[[lesson-librarian-reads-beyond-the-four-inputs]]", "[[lesson-frame-read-clauses-omit-candidate-check-and-brief]]", "[[lesson-brief-next-section-has-no-source]]"]
severity: 1
addressed_by: "[[decision-case-143]]"
origin: raw/2026-09-10/ledger.md#L132
sprint: migration
created: 2026-09-11
tags: [harness, librarian]
---

## Pattern

Two lessons name the same gap in the written frame of the librarian.

Session F (`lesson-librarian-reads-beyond-the-four-inputs`): the prompt described no semantics for the yaml marks, so the librarian read `guppi/generate.py`; and `rule-index-check` allowed opening a page when an index line did not settle the judgment while `rule-synthesis` forbade reading a lesson page, so two rules gave opposite answers for one act.

Session G (`lesson-frame-read-clauses-omit-candidate-check-and-brief`): the frame listed three reads and covered two judgments; deciding whether a lesson joins a cluster, and taking a fact the brief needs, each need a page when an index line is not enough, and neither had a clause.

In both, the reads the work needs were found while the work ran, not when the frame was written.

## Proposal

A suggestion, not a decision. Derive the read clauses from the judgments: list every judgment the librarian makes (duplicate or not, cluster or not, why a script failed, what the brief states as fact), and give each one clause that says which page it may open and for which field. Case 54 added four reasons to the frame this way; the readings of `estimate-documentation-completes` and `estimate-synthesis-clusters` after this run show whether the list is now complete. Every rule that names a read should be changed in one pass, so that two rules never answer one act differently.

## History

- 2026-09-11 created · raw/2026-09-10/ledger.md#L132
- 2026-09-14 updated: actioned: the four reasons of the frame (54, 58, 90.3, 102.4) are one clause per judgment, the children's clauses agree, nine runs without a recurrence; no Rule changed (case 143) · [[decision-case-143]]
- 2026-09-15 updated: synthesis: lesson-brief-next-section-has-no-source added, the frame names no source for the "What the next session does first" section of the brief; reopened from actioned · raw/2026-09-15/1110/ledger.md#L7
