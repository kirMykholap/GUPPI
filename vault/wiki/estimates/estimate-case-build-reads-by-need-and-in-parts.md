---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi reads the examples only before it writes a Case, reads whole only the pages the Case changes, the Criteria of their Estimates and the case files of the related Cases, reads the rest in parts, makes independent calls in one turn, and keeps its cache for an hour
method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the tool calls, the tokens and the cache writes by their time to live of each dispatch of case-guppi in that session, when there was one, in the estimate line
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
**＋** It reads whole each page the Case changes and the Criterion of each Estimate such a page lists.
**＋** It reads in parts, by a Grep with lines of context or a Read with `offset` and `limit`, the case file of a Case of an earlier session, the brief and the handoff of the session, a page it reads only for background, and a module of code, of which it reads the functions the Case changes and the places that call them.
**＋** It reads whole the case file of each Case of the session that the prompt of its call names, and of each Case of the session that the check of its file names in a finding or a note.
**＋** It makes the tool calls that do not wait on each other's output in one turn.
**＋** `.claude/agents/case-guppi.md` sets the cache of the agent to live one hour, by `cacheTtl: "1h"` under `experimental`.
**－** A dispatch that answers only with rounds does not read `vault/wiki/case-example.md`.

## Result

2026-10-07, Retro, by hand: the new Render of rule-case-build in the Spec (Case 717.2) read against the Criterion — case-example.md read once just before the first Write and not by a dispatch of rounds alone, whole reads of the pages the Case changes and their Criteria, reads in parts of earlier case files, brief, handoff, background pages and code, whole reads of the case files the prompt or a finding names (the paragraph below it in .claude/agents/case-guppi.md), independent calls in one turn, cacheTtl "1h" under experimental after skills: each set. Dispatches of the session, all under the 5-minute cache as the render has not run: 712 — 35 tool calls, cache read 1510266, write 5m 86324, write 1h 0, output 14778; 713/719 — 120, 11939159, 605268, 0, 98037; 714 — 40, 1781295, 96712, 0, 18967; 715 — 48, 2319587, 184698, 0, 22271; 716 — 50, 3601380, 348523, 0, 37293; 717 — 125, 8129211, 365734, 0, 77167

## History

- 2026-10-07 created · [[decision-case-717.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/1804/ledger.md#L25
