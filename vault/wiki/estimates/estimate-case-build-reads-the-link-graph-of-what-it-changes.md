---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi reads, for each page and file its Case changes, its block in .guppi/links.md, and opens each neighbour whose purpose line bears on the change
method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on .guppi/links.md and whose start wrote that file: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether a Grep of .guppi/links.md names each page and file the Case changes and whether each neighbour that bears on the change is opened or named in context; the count and the transcripts in the estimate line"
checked: 2026-11-01
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

## Result

2026-11-01, Work Mode of session 0141, the case-guppi transcripts of session 2307 under ~/.claude/projects/c--PROJECTS-GUPPI/8d8876d7-f627-4f65-95f7-cb7b7172cd46/subagents/: 2 of 4 Cases found the block of each existing page and file they change; Case 972 (agent-ab08bcaa476ca5d9f.jsonl L142) grepped the blocks of lint.py and prespec.py but not of .guppi/tests/test_lint.py, which has one, nor said that test_prespec.py has none; Case 975 (agent-aa121a9ddfe7235f9.jsonl L82) grepped rule-rules-schema and schema.yaml but not entity-glossary, estimate-rules-schema-checked or vault/wiki/glossary.md; Cases 973 (L158) and 974 (L79, L207) grepped theirs, 974 with -A 40 that printed 40 of the 96 lines of the block of rule-case-build; no context said that a page it creates has no block

## History

- 2026-10-31 created · [[decision-case-967.2]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/0141/ledger.md#L17
