---
type: estimate
kind: QA
status: passed
target: "[[rule-synthesis]]"
purpose: An Insight stays or is born actioned by the mark — an existing actioned Insight keeps its status and takes the later of the two addressed_by; a new Insight from a marked lesson is set actioned right after its create
method: "by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`: the yaml and the brief read against the Criterion"
checked: 2026-11-27
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [harness, workflow, librarian]
core: true
---

## Criterion

When:
The librarian, at synthesis, hangs a lesson whose entry carries `addressed_by: decision-case-N` on an existing Insight of the same pattern that stands `actioned` with `addressed_by: decision-case-M`.

Then:
When case N is later than case M — compared number by number, `378.5` after `378.4` — the `update` carries `set: {addressed_by: decision-case-N}`, and `status` stays `actioned`.
**＋** When case N is not later than M, the `update` carries no `addressed_by`: the field stays `decision-case-M`, and `status` stays `actioned`.
**＋** Either way the `update` carries `children` plus the lesson; the lesson is `clustered`, the cascade archives it, and the brief reports the pair beside the synthesis.
**＋** An Insight born from a marked lesson gets, right after its `create`, an `update` with `set: {status: actioned, addressed_by: decision-case-N}`.
**＋** A lesson with no `addressed_by` sets an `actioned` Insight `open` with `set: {status: open}`, and a new Insight is born `open`.
**－** `addressed_by` never names two decisions.

## Result

2026-11-27, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
