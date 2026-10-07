---
type: insight
pattern: A check of the Cases of a session leaves a Case id out only when a {supersedes:case N} line of the ledger names it, so an id that no such line names, a parent Case with no lines of its own or a sub-case that a rebuild dropped, stays a finding, and nothing else clears it.
status: open
children: ["[[lesson-prespec-parent-of-superseded-sub-cases]]", "[[lesson-case-check-store-keeps-sub-cases-a-rebuild-dropped]]", "[[lesson-case-check-refuses-a-rebuild-under-a-new-number]]"]
severity: 3
origin: raw/2026-10-07/1804/ledger.md#L27
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness]
---

## Pattern

In session 2214 of 2026-09-24, after Case 412 superseded each of 407.1 to 407.5, check_ratified of guppi/prespec.py still reported the parent Case 407, which had no ledger lines of its own and so was named by no supersedes line. In session 1804 of 2026-10-07 the store of the Case-file check kept 713.1 and 713.2 after case-guppi went back to the ratified Case 713, and the Stop check refused the showing of Case 719 twice on pairs only those stale entries held; the supersedes line that would leave them out comes only with the ratification the refusal blocked.

## Proposal

A suggestion, not a decision. Let the checks leave out a Case id that the current file of its top-level Case no longer holds, or a parent whose every sub-case is superseded, instead of waiting for a supersedes line that names it (cases 720, 721 of session 1804 carry the store side).

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#L27
- 2026-10-07 updated: child lesson-case-check-refuses-a-rebuild-under-a-new-number added (synthesis) · raw/2026-10-07/2114/ledger.md#L28
