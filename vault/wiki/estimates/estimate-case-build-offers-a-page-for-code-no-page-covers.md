---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on an item that points to code no page covers, reads that code and offers in a round a page only for the thing the Case changes, or the path added to a page that describes it, and puts the chosen page into the same Case
method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-13/1753/ledger.md#case-803
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`, builds a Case on an item whose words point to code, a file, a module or a function, that no live page under `vault/wiki/` names, by its file or by a folder that holds it, in `code_ref`, `implementation_ref` or `governs`.

Then:
It reads that code in parts, the functions the Case changes and the places that call them, and searches the pages under `vault/wiki/` by meaning for the thing that code does.
**＋** Before it writes the Case, a round offers a page only for the thing the Case changes, described from the code it read: where a page already describes that thing, the path added to the field of that page that lists its code; otherwise a new page, its category by the check of the schema of that category, with its slug, its one-line purpose, its parent and its paths.
**＋** Where the person turns down both, it asks in a round which page the Case changes.
**＋** The page the person chose, created or given the path, is a task of the same Case, and the Estimate that checks the change stands on that page.
**－** Code that the Case does not change gets no page offered.
**－** Code that a page names, by its file or by a folder that holds it, gets no page offered.

## Result

2026-10-13, Retro, the new Render of rule-case-build in raw/2026-10-13/1753/spec.md (Case 803) read against the Criterion; the new sentence, for code no live page names by file or folder in code_ref, implementation_ref or governs, reads it as the paragraph sets for a module of code ("the functions the Case changes and the places that call them"), searches the pages by meaning, offers in a round the path on a page that describes the thing or a new page with category, slug, purpose, parent and paths, asks which page the Case changes when both are turned down, puts the page into the same Case with its Estimate, and offers no page for code the Case does not change

## History

- 2026-10-13 created · [[decision-case-803]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1753/ledger.md#L115
