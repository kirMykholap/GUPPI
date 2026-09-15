---
type: lesson
kind: knowledge
root_cause: Obsidian reads a property value as a link only in the form `[[slug]]` (quoted in YAML, or it parses as a nested list); a bare slug is text; a property link is seen by the graph, backlinks, unresolved and Bases, and resolves in any folder, the archive included
status: new
source: the owner's Obsidian after the migration of case 148.1 — insight-tests-clock-not-pinned 2 backlinks, rule-harness 15
origin: raw/2026-09-14/1633/ledger.md#L60
sprint: migration
created: 2026-09-14
tags: [harness]
---

## Trigger

before 148.1 the graph showed an Insight linked only through the body sections generate duplicates, never through children, parent or estimates

## Root cause

Obsidian reads a property value as a link only in the form `[[slug]]` (quoted in YAML, or it parses as a nested list); a bare slug is text; a property link is seen by the graph, backlinks, unresolved and Bases, and resolves in any folder, the archive included

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#L60
- 2026-09-15 updated: the quoted wikilink of the root cause in backticks: lint and Obsidian read a quotation, not a link (case 160) · [[decision-case-160]]
