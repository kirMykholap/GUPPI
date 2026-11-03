---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi reads the examples only before it writes a Case, reads whole only the pages the Case changes and the case files of the related Cases, reads the purpose line of each Estimate of those pages and the Criterion and the code it names only where that purpose speaks of the change, reads the rest in parts, makes independent calls in one turn, and keeps its cache for an hour
method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the tool calls, the tokens and the cache writes by their time to live of each dispatch of case-guppi in that session, when there was one, in the estimate line
checked: 2026-11-03
origin: raw/2026-10-07/1804/ledger.md#case-717.2
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent dispatches `case-guppi` by `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, or sends it a message by `SendMessage`.

Then:
`case-guppi` reads `vault/wiki/case-example.md` once in a dispatch, just before its first `Write` of the file of a Case.
**＋** It reads whole each page the Case changes; of each Estimate such a page lists it reads the `purpose` line, and the `## Criterion` of each one whose `purpose` speaks of the thing the Case changes, with the code that Criterion or its `method` names, read in parts.
**＋** It reads in parts, by a Grep with lines of context or a Read with `offset` and `limit`, the case file of a Case of an earlier session, the brief and the handoff of the session, a page it reads only for background, and a module of code, of which it reads the functions the Case changes and the places that call them.
**＋** It reads whole the case file of each Case of the session that the prompt of its call names, and of each Case of the session that the check of its file names in a finding or a note.
**＋** It makes the tool calls that do not wait on each other's output in one turn.
**＋** `.claude/agents/case-guppi.md` sets the cache of the agent to live one hour, by `cacheTtl: "1h"` under `experimental`.
**－** An Estimate whose `purpose` speaks of something else it reads no further.
**－** A dispatch that answers only with rounds does not read `vault/wiki/case-example.md`.
**－** The case file of a Case that the prompt or a message names as built at the same time it does not read in that build; it reads that file whole only after a later message says that the build of that Case has ended, as `estimate-case-build-reads-no-sibling-file-mid-send` checks.

## Result

2026-11-03, Retro of session 2155, the new Render of rule-case-build in vault/raw/2026-11-02/2155/spec.md (Case 1011.3) with .claude/agents/case-guppi.md as rendered: the frame reads whole each page the Case changes and the related case files, the purpose line of each Estimate such a page lists and its Criterion and the code it names only where that purpose speaks of the change, the rest in parts by a Grep with context or a Read with offset and limit, case-example.md once before the first Write, the calls that do not wait on each other in one turn, cacheTtl "1h" under experimental; the dispatches of case-guppi this session ran on the old Render: Case 1011 six runs, its last at 280667 tokens and 53 tool calls in 305 s; Case 1012 five runs, its last at 223791 tokens and 11 tool calls in 49 s; Case 1013 three runs, its last at 145614 tokens and 8 tool calls in 38 s; the cache writes by their time to live were not seen

## History

- 2026-10-07 created · [[decision-case-717.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/1804/ledger.md#L25
- 2026-10-17 updated: the Criterion replaced whole — the case file of a Case built at the same time is read only after its build has ended · [[decision-case-872.4]]
- 2026-10-17 status: pending → passed · raw/2026-10-16/2104/ledger.md#L47
- 2026-11-03 updated: the Criterion replaced whole — the Estimates of a changed page are read by their purpose first · [[decision-case-1011.3]]
- 2026-11-03 status: pending → passed · raw/2026-11-02/2155/ledger.md#L20
