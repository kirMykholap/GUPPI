---
type: insight
pattern: A Case changes a reader in code and the text it reads in a page or a governed file; the code of the working tree runs at once, the page lands at the librarian's run and the file at the render, so the reader refuses or goes red in between, by construction.
status: open
children: ["[[lesson-reader-changed-before-its-writer-closed-the-live-session]]", "[[lesson-work-mode-check-reads-a-page-the-same-spec-changes]]", "[[lesson-prespec-preview-expected-before-generate-applies-the-readings]]"]
severity: 1
addressed_by: "[[decision-case-473.2]]"
origin: raw/2026-09-17/1119/ledger.md#L43
sprint: migration
created: 2026-09-17
tags: [harness, hooks, ledger, workflow, session]
---

## Pattern

Two lessons, one cause. After case 111.3 the Stop hook of session M refused 13 lines: the reader in the working tree required a stamped hi and the writer of stamped lines reached settings.json only with the next render. After cases 227 and 229.1 `make lint` was red on the sprint step until the librarian's run: `sprint --check` ran at once and the sprint page waited for the run. In both the same Spec changes a reader and what it reads, and the two land at different moments of the session.

## Proposal

One sentence in `rule-work-mode` (Slice 3b, defer 231): a check that reads a page or a file the same Spec updates is read after the librarian's run or the render, and its red in Work Mode is an expectation named in the handoff, not a finding; a reader that drops an old form keeps it as a fallback until its writer is measured live (case 111.6). A suggestion, not a decision.

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#L43
- 2026-09-18 deferred · [[decision-case-238]]
- 2026-09-28 defer by decision-case-238 superseded · [[decision-case-473.2]]
- 2026-09-28 updated: actioned: the red of a check before the librarian's run is a note for the handoff in rule-retro (case 473.1); a reader that loses what it refuses keeps the old form until its writer is measured live, in rule-case-build (case 473.2); the defer of case 238 retired · [[decision-case-473.2]]
- 2026-10-10 updated: child lesson-prespec-preview-expected-before-generate-applies-the-readings added, reopened from actioned (synthesis) · raw/2026-10-10/1555/ledger.md#L6
