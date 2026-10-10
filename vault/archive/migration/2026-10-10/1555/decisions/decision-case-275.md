---
type: decision
case: "275"
status: archived
update: ["[[lesson-spec-change-text-quotes-a-wikilink-bare]]"]
origin: raw/2026-09-20/1308/ledger.md#case-275
sprint: migration
created: 2026-09-20
tags: [workflow, harness, librarian]
---

## Context

The lesson `lesson-spec-change-text-quotes-a-wikilink-bare` was born from a ledger line of session 0958; its Trigger quotes the `change` of Case 262 — "the two placeholders `[[decision-case-N]]` of the Criterion in code spans" — in quotes, the placeholder bare, without a code span. The page took the text as it was, lint reads the body of a lesson like any other and raises `ref: body names decision-case-N, which no live or archived page carries` — the class the lesson is about, the fifth time. The librarian does not repair it: a lesson page changes by an `update` only.
State of the pages: the lesson `new`, tags `workflow, harness, librarian`; no Estimate touched — a lesson has none; `rule-lint` untouched — the finding is right.

## Problem

The lesson on bare placeholders carries a bare placeholder itself and stands as a lint finding. Repair the page, or keep the finding.

## History

- 2026-09-20 created · raw/2026-09-20/1308/ledger.md#case-275
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
