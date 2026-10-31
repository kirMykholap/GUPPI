---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi reads, for each page and file its Case changes, its block in .guppi/links.md, and opens each neighbour whose purpose line bears on the change
method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on .guppi/links.md and whose start wrote that file: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether a Grep of .guppi/links.md names each page and file the Case changes and whether each neighbour that bears on the change is opened or named in context; the count and the transcripts in the estimate line"
origin: raw/2026-10-31/1831/ledger.md#case-967.2
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case it builds, before it answers with its summary.

Then:
For each page and file the Case changes, it finds the block of that page or file in `.guppi/links.md` by a Grep for its line `## <slug or path>` with lines of context.
**＋** From that block it judges, by what each neighbour is for, which neighbours bear on the change.
**＋** It opens each neighbour whose purpose line bears on the change, whole or in parts as the Render sets for its kind of text.
**＋** Each neighbour that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
**－** Where `.guppi/links.md` is missing or holds no block of that page or file, the `context` of the Case says so.

## History

- 2026-10-31 created · [[decision-case-967.2]]
