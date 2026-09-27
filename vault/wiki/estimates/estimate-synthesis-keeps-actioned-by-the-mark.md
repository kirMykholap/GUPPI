---
type: estimate
kind: QA
status: passed
target: "[[rule-synthesis]]"
purpose: An Insight stays or is born actioned by the mark — an existing actioned Insight keeps its status and takes the later of the two addressed_by; a new Insight from a marked lesson is set actioned right after its create
method: one reading by hand of the yaml and the brief after the librarian's run on the first marked lesson clustered under an actioned Insight; no date
checked: 2026-09-27
origin: raw/2026-09-20/2106/ledger.md#case-284.4
sprint: migration
created: 2026-09-20
tags: [harness, workflow, librarian]
---

## Criterion

When:
The librarian, at synthesis, hangs a lesson whose entry carries `addressed_by: decision-case-N` on an existing Insight of the same pattern that stands `actioned` with `addressed_by: decision-case-M`.

Then:
When case N is later than case M — compared number by number, `378.5` after `378.4` — the `update` carries `set: {addressed_by: decision-case-N}`, and `status` stays `actioned`.
**＋** When case N is not later than M, the `update` carries no `addressed_by`: the field stays `decision-case-M`, and `status` stays `actioned`.
**＋** Either way the `update` carries `children` plus the lesson; the lesson is `clustered`, the cascade archives it, and the brief reports the pair beside the synthesis.
**＋** An Insight born from a marked lesson gets, right after its `create`, an `update` with `set: {status: actioned, addressed_by: decision-case-N}` (302.2).
**＋** A lesson with no `addressed_by` sets an `actioned` Insight `open` with `set: {status: open}`, and a new Insight is born `open`.
**－** `addressed_by` never names two decisions.

## Result

2026-09-27, raw/2026-09-27/1819/materialize.yaml, insight-case-show-built-case-retyped-by-hand, the archived lesson and vault/wiki/brief.md read by hand after 049458e; the lesson marked decision-case-458 under an Insight actioned by 452.4 gave an update with the lesson in children and addressed_by decision-case-458, no status, the Insight stays actioned, the lesson clustered and archived, the pair named in the Flags; the not-later, born-Insight and unmarked branches were not exercised

## History

- 2026-09-21 created · [[decision-case-284.4]]
- 2026-09-22 updated: the Criterion replaced whole — the second case of the mark, an Insight born from a marked lesson (case 302.2) · [[decision-case-302.2]]
- 2026-09-22 updated: the exception is named by the schema and the glossary, not by §8 (case 318) · [[decision-case-318]]
- 2026-09-24 updated: the Criterion replaced whole — addressed_by takes the later case (case 385) · [[decision-case-385]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L26
