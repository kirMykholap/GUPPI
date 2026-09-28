---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
purpose: Whether a check red in Work Mode because it reads a page or a governed file the same Spec updates ends at Retro as a note for the handoff, not as debt, while a red test is still fixed or reverted
method: one reading by hand at the first /retro after the render in a session whose Spec updates a page or a governed file that make lint reads, recorded in the estimate line
origin: raw/2026-09-28/0000/ledger.md#case-473.1
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
The person invokes `/retro` in a session whose Spec updates a page or a governed file, and in Work Mode `make lint`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

Then:
The red or the refusal is an item of the frontier, and it ends as a note for the handoff that names the check and the page or file it waits for.
**＋** The reading of the check that counts is the `make lint` of the librarian's run, after the page is written and the file rendered.
**－** The red is not debt: the agent does not fix it or revert it into a patch.
**－** A red test is not such a check: it is fixed or reverted into a patch, and the handoff still needs green.

## History

- 2026-09-28 created · [[decision-case-473.1]]
