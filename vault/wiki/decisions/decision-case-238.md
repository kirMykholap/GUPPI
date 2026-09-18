---
type: decision
case: "238"
status: current
defer: ["[[insight-workflow-code-live-before-the-page-it-reads]]"]
origin: raw/2026-09-18/1252/ledger.md#case-238
sprint: migration
created: 2026-09-18
tags: [harness, hooks, ledger, workflow, session]
---

## Context

`insight-workflow-code-live-before-the-page-it-reads` (`open`, severity 2) was made by the librarian of the 1119 run over two lessons: the Stop hook that refused 13 lines after case 111.3, and `make lint` red on the sprint step after cases 227 and 229.1. One Spec changes a reader in code and the text it reads on a page or in a governed file; the code of the working tree runs at once, the page lands at the librarian's run and the file at the render, so the reader is red in between by construction. Its Proposal is one sentence in `rule-work-mode`: such a check is read after the run or the render, its red in Work Mode is an expectation named in the handoff, not a finding, and a reader that drops an old form keeps it as a fallback until its writer is measured live. `rule-work-mode` is a placeholder without a body, Slice 3b, deferred by 183, 206, 218 and 231.

## Problem

The Proposal is right and has no page to land on: the sentence belongs to the rule of Work Mode, and that rule does not exist yet. The person chose to take it up with the whole of Slice 3b, when `rule-work-mode` is built, rather than as a line written ahead of its rule.

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#case-238
