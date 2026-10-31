---
type: decision
case: "967"
status: current
children: ["[[decision-case-967.1]]", "[[decision-case-967.2]]", "[[decision-case-967.3]]"]
origin: raw/2026-10-31/1831/ledger.md#case-967
sprint: plugin
created: 2026-10-31
tags: [harness, workflow, session, case-build, hooks, render]
---

## Problem

A builder that searches only for words misses a text that is linked to the change but holds none of its words, because no command shows the links of a page or a file in one place, out and in.

## Recommend

- **How much this Case covers**
  - Recommended: (a) one Case with a sub-case for each part.
  - Answer: (a), as recommended.
- **Where a hand-off link comes from**
  - Recommended: (b) derived from the names in the rendered files, with no new field.
  - Answer: (b), as recommended.
- **Which page describes the command**
  - Recommended: (a) a new entity, `entity-link-graph`, under `entity-guppi`.
  - Answer: (a), as recommended.
- **How far the command looks**
  - Recommended: (a) one step in both directions.
  - Answer: (a), as recommended.
- **What becomes of the check of prose names**
  - Recommended: (a) no check in this Case; it is reported as not done.
  - Answer: (a), as recommended.
- **Which texts give a link by a name**
  - Recommended: (b) the rendered harness files and the body of each page outside its History.
  - Answer: (b), as recommended.
- **Where the step of `case-guppi` stands**
  - Recommended: (a) in the paragraph on the frame, for each page and file the Case changes.
  - Answer: (a), as recommended.
- **How the command is checked**
  - Recommended: (a) a new Estimate on `entity-link-graph`, with a test and a live run.
  - Answer: (a), as recommended.
- **How the step of `case-guppi` is checked**
  - Recommended: (a) a new Estimate on `rule-case-build`.
  - Answer: (a), as recommended.
- **How `case-guppi` gets the output of the command**
  - Recommended: (b) a hook at the start of each session writes the whole graph into a file, and the builder reads that file; (a), Bash with a hook in the header, was not recommended, since the documentation does not confirm that its call runs in Plan Mode without a prompt.
  - Answer: (b); the person first chose (a), then (b) when asked again, asked why the graph covers all pages, and kept (b) after the answer that the builder reads only the blocks of what its Case changes.
- **Which page describes the hook that writes the graph**
  - Recommended: (a) a new rule, `rule-link-graph-at-session-start`, under `rule-harness`.
  - Answer: (a), as recommended.

## History

- 2026-10-31 created · raw/2026-10-31/1831/ledger.md#case-967
