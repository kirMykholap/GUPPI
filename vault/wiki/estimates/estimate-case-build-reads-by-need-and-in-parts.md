---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi reads the examples only before it writes a Case, reads whole only the pages the Case changes, the Criteria of their Estimates and the case files of the related Cases, reads the rest in parts, makes independent calls in one turn, and keeps its cache for an hour
method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the tool calls, the tokens and the cache writes by their time to live of each dispatch of case-guppi in that session, when there was one, in the estimate line
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The main agent dispatches `case-guppi` by `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, or sends it a message by `SendMessage`.

Then:
`case-guppi` reads `vault/wiki/case-example.md` once in a dispatch, just before its first `Write` of the file of a Case.
**＋** It reads whole each page the Case changes and the Criterion of each Estimate such a page lists.
**＋** It reads in parts, by a Grep with lines of context or a Read with `offset` and `limit`, the case file of a Case of an earlier session, the brief and the handoff of the session, a page it reads only for background, and a module of code, of which it reads the functions the Case changes and the places that call them.
**＋** It reads whole the case file of each Case of the session that the prompt of its call names, and of each Case of the session that the check of its file names in a finding or a note.
**＋** It makes the tool calls that do not wait on each other's output in one turn.
**＋** `.claude/agents/case-guppi.md` sets the cache of the agent to live one hour, by `cacheTtl: "1h"` under `experimental`.
**－** A dispatch that answers only with rounds does not read `vault/wiki/case-example.md`.
**－** The case file of a Case that the prompt or a message names as built at the same time it does not read in that build; it reads that file whole only after a later message says that the build of that Case has ended, as `estimate-case-build-reads-no-sibling-file-mid-send` checks.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
