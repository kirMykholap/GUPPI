---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on an item that points to code no page covers, reads that code and offers in a round a page only for the thing the Case changes, or the path added to a page that describes it, and puts the chosen page into the same Case
method: "by hand: the Render of rule-case-build in .claude/agents/case-guppi.md read against the Criterion, recorded in the estimate line"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
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

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
