---
type: estimate
kind: QA
status: passed
target: "[[rule-synthesis]]"
purpose: Whether a lesson that joins an Insight a decision entry of its own materialize.yaml sets actioned reopens it when it carries no addressed_by, and keeps it actioned when it does
method: one reading by hand of the yaml, the Insight page and the brief after a librarian run in which a lesson joins an Insight that a decision entry of the same yaml sets actioned; no date
checked: 2026-10-05
origin: raw/2026-10-05/1616/ledger.md#case-668
sprint: migration
created: 2026-10-05
tags: [harness, workflow, librarian]
---

## Criterion

When:
`librarian-guppi`, at synthesis, hangs a lesson entry on an Insight of the same pattern that stands `open` on disk, while an `update` entry of a decision in the same `materialize.yaml` sets that Insight `actioned` with `addressed_by: decision-case-M`, and `guppi/generate.py` then applies the yaml.

Then:
A lesson entry with no `addressed_by` gives an `update` of the Insight with `children` plus the lesson and `set: {status: open}`.
**＋** After `guppi/generate.py` runs, the Insight stands `open` and the lesson stands `clustered`, not archived.
**＋** A lesson entry with `addressed_by: decision-case-N` gives an `update` with no `status`: it carries `set: {addressed_by: decision-case-N}` when case N is later than case M, compared number by number, and no `addressed_by` otherwise; the Insight stays `actioned`.
**＋** `vault/wiki/brief.md` reports the pair beside the synthesis.
**－** An Insight that is not `actioned` on disk and that no decision entry of the yaml sets `actioned` takes no `status` from the lesson.

## Result

2026-10-05, Plan Mode of session 1831, case 669: set passed by the person's decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. No reading was taken before it.

## History

- 2026-10-05 created · [[decision-case-668]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.3]]
