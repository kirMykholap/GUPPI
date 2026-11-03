---
type: estimate
kind: QA
status: passed
target: "[[rule-synthesis]]"
purpose: Whether a lesson that joins an Insight a decision entry of its own materialize.yaml sets actioned reopens it when it carries no addressed_by, and keeps it actioned when it does
method: one reading by hand of the yaml, the Insight page and the brief after a librarian run in which a lesson joins an Insight that a decision entry of the same yaml sets actioned; no date
checked: 2026-10-05
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, librarian]
core: true
---

## Criterion

When:
`librarian-guppi`, at synthesis, hangs a lesson entry on an Insight of the same pattern that stands `open` on disk, while an `update` entry of a decision in the same `materialize.yaml` sets that Insight `actioned` with `addressed_by: decision-case-M`, and `.guppi/guppi/generate.py` then applies the yaml.

Then:
A lesson entry with no `addressed_by` gives an `update` of the Insight with `children` plus the lesson and `set: {status: open}`.
**＋** After `.guppi/guppi/generate.py` runs, the Insight stands `open` and the lesson stands `clustered`, not archived.
**＋** A lesson entry with `addressed_by: decision-case-N` gives an `update` with no `status`: it carries `set: {addressed_by: decision-case-N}` when case N is later than case M, compared number by number, and no `addressed_by` otherwise; the Insight stays `actioned`.
**＋** `vault/wiki/brief.md` reports the pair beside the synthesis.
**－** An Insight that is not `actioned` on disk and that no decision entry of the yaml sets `actioned` takes no `status` from the lesson.

## Result

2026-10-05, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
