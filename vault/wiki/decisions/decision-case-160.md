---
type: decision
case: "160"
status: current
update: ["[[decision-case-140]]", "[[lesson-obsidian-property-links-need-wikilink-form]]"]
origin: raw/2026-09-15/1110/ledger.md#case-160
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger]
---

## Context

Lint reads every `[[…]]` in the body of a page as a link and requires that page to exist. One exception: inside backticks it is a quotation, not a link; Obsidian reads it the same way. When a page quotes the form of a link in plain quotes — `"[[slug]]"` — lint sees a link to a page `slug`, and Obsidian's graph an unresolved link. This happened twice before: Case 130.1 cured the pages of 112.x, Case 140 the pages of 130.x. Now the same quotation stands in the Context of `decision-case-140` itself (the librarian carried it from the chat as it was) and in the `root_cause` of the lesson on property links (written in the ledger line in quotes, the hook wrote it verbatim).

## Problem

Two `ref` findings, the third time on the same thing; the pages or lint.

## Given

`decision-case-140` Context: `"History and log lines end with · [[decision-case-N]] when a decision exists"` without backticks; its own Given carries the same phrase in backticks, no finding.
**＋** `lesson-obsidian-property-links-need-wikilink-form`: the Root cause section and the `root_cause` field carry `"[[slug]]"`; Obsidian shows `slug` as an unresolved link from the section (checked by the owner), lint raises `ref` from the same place.
**＋** `guppi lint`: `CODE_SPAN` drops a `[[…]]` inside backticks; Obsidian does the same (checked); `generate.update` applies `replace` to the body and `set` to the fields of a page of any category, with a History line — the precedent of 140 and 144.2.
**＋** `decisions/schema.md`: "a decision is not edited" — 140 already decided that backticks change nothing signed.
**－** The ledger line the lesson was born from is not rewritten; the page changes.

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#case-160
