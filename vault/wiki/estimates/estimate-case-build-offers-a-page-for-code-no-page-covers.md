---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on an item that points to code no page covers, reads that code and settles a page only for the thing the Case changes, or the path added to a page that describes it, asks in a round only where the two differ in behaviour, in cost or in what they block, and puts that page into the same Case
method: "by hand, at the Retro of the session whose Render of rule-case-build asks context for why the page was chosen: that Render in the Spec read against the Criterion, recorded in the estimate line; by hand, after a session whose case-guppi.md holds this text in which case-guppi settles a page for code that no page covers: the agent transcript of that case-guppi under ~/.claude/projects/ and its case file read against the Criterion, the transcript in the estimate line"
checked: 2026-11-20
origin: raw/2026-10-13/1753/ledger.md#case-803
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`, builds a Case on an item whose words point to code, a file, a module or a function, that no live page names, by its file or by a folder that holds it, in `code_ref`, `implementation_ref` or `governs`.

Then:
It reads that code in parts, the functions the Case changes and the places that call them, and searches the pages by meaning for the thing that code does.
**＋** It settles a page only for the thing the Case changes, described from the code it read: where a page already describes that thing, the path added to the field of that page that lists its code; otherwise a new page, its category by the check of the schema of that category, with its slug, its one-line purpose, its parent and its paths.
**＋** Its `context` gives the slug of the chosen page and why it was chosen.
**＋** Where the two options differ in behaviour, in cost or in what they block, a round offers them before it writes the Case, and where the person turns down both, it asks in a round which page the Case changes.
**＋** The page, created or given the path, is a task of the same Case, and the Estimate that checks the change stands on that page.
**－** Code that the Case does not change gets no page.
**－** Code that a page names, by its file or by a folder that holds it, gets no page.

## Result

2026-11-20, the new Render of rule-case-build in vault/raw/2026-11-04/0807/spec.md (case 1031.2) read against the Criterion: it settles the page, offers a round only where the two differ, keeps the page a task of the same Case and gives no page to code the Case does not change or a page names; the line "Its `context` gives the slug of the chosen page and why it was chosen" is not set: the Render says "`context` names the page" and sets no reason

## History

- 2026-10-13 created · [[decision-case-803]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1753/ledger.md#L115
- 2026-10-17 updated: the method reads the Render where it lives, with no past moment · [[decision-case-875]]
- 2026-11-20 updated: the Criterion replaced whole — the agent settles the page, and a round comes only where the options differ · [[decision-case-1031.2]]
- 2026-11-20 status: pending → failed · raw/2026-11-04/0807/ledger.md#L57
- 2026-11-23 updated: pending again — the Render now asks for the reason, the Criterion as it stood · [[decision-case-1041]]
