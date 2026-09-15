---
type: decision
case: "140"
status: current
update: ["[[decision-case-130.1]]", "[[decision-case-130.2]]"]
origin: raw/2026-09-14/1229/ledger.md#case-140
sprint: migration
created: 2026-09-14
tags: [harness, workflow, ledger]
---

## Context

The shared `context` of Case 130 quotes a line of `rule-page-generation`: `"History and log lines end with · [[decision-case-N]] when a decision exists"` — without backticks. The librarian carried it onto `decision-case-130.1` and `decision-case-130.2` verbatim; lint sees `[[decision-case-N]]`, no page has that slug — two `ref` findings. Case 130.1 cured the same thing on the pages 112.1–112.6 by hand, with backticks.

## Problem

Remove the two findings and leave the pages what was signed. Through `generate` (an `update` with `replace`, a History line) or by hand, as 130.1 did.

## Given

`decision-case-130.1` (line 15) and `decision-case-130.2` (line 14): the same Context paragraph, in it `"History and log lines end with · [[decision-case-N]] when a decision exists"`; one occurrence per page.
**＋** `guppi lint`: `ref: body names decision-case-N, which no live or archived page carries` — two of the 74 findings; `CODE_SPAN` (`lint.py:57`) does not count a `[[slug]]` inside backticks as a link.
**＋** `generate.update` (`generate.py:468`): finds a page of any category, applies `replace` in the body, adds a History line with `change`.
**＋** Precedent 130.1: the same literal on `decision-case-112.1`–`112.6` wrapped in backticks by hand, the ledger line on `rule-page-generation` `contract: same`.
**－** `decisions/schema.md`: "a decision is not edited. Only `status` and `superseded_by` ever change" — the edit changes no signed content; the schema is not updated.
**－** The other 72 findings are not touched: 62 — Slice 5, 10 — F1.

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#case-140
- 2026-09-15 updated: the quoted wikilink of the Context in backticks: lint and Obsidian read a quotation, not a link (case 160) · [[decision-case-160]]
