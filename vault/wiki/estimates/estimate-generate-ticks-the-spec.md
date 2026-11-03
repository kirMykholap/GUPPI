---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading, of a deleted Estimate or of an Estimate an update sets passed or failed, across the Specs of raw/ — never a line of a later or a superseded Case
method: uv run --project .guppi pytest .guppi/tests/test_generate.py
checked: 2026-10-05
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi generate` of `rule-page-generation` marks an entry of `materialize.yaml` `applied`. Either it applied the entry, or it found the entry to be a repeat: a `create`, `update`, `delete` or `defer` entry whose `case`, `kind` and `slug` match those of an entry of the same `materialize.yaml` already marked `applied`.

Then:
For a `create`, `update`, `delete` or `defer` entry that was applied, in the `spec.md` of the same unit, the first unticked line `` - [ ] <kind> `<slug>` `` in the section of the entry's Case becomes `- [x]`. Nothing else in the file changes.
**＋** For an `estimate` entry, a `create` entry with `folded`, a `delete` entry and an `update` entry whose `set` gives `status` the value `passed` or `failed`, every unticked line `` - [ ] read `<slug>` `` of every `spec.md` under `vault/raw/` becomes `- [x]`. The Spec beside the yaml comes first, then the Specs of the other session folders, oldest first.
**＋** In the Spec beside the yaml, for an `estimate` entry, a `delete` entry or such an `update` entry, a `read` line in the section of a Case whose first decision entry carries a `line` greater than the entry's `line` is not the entry's line, and the search goes on.
**＋** In any Spec, a `read` line in the section of a Case whose entries are marked `superseded_by` is not the entry's line. For the Spec beside the yaml, the marks come from the run's entries. For another Spec, they come from the `materialize.yaml` beside it. With no yaml beside a Spec, nothing is skipped there.
**＋** A `create` entry with `folded` ticks both its page line and its `read` line. The filter by `line` does not apply to it, and the filter by `superseded_by` does.
**＋** A `delete` entry, and an `update` entry whose `set` gives `status` the value `passed` or `failed`, tick both the page line in their own Case and the `read` lines of their slug.
**－** An `update` entry whose `set` gives no `status`, or the value `pending`, ticks no `read` line.
**－** A repeat ticks no line in any `spec.md`. A second line `` - [ ] <kind> `<slug>` `` in the section of its Case stays unticked, and a repeated `delete` or `update` leaves the `read` lines of its slug as they stand.
**－** A line, a section or a Spec not found raises no error and prints nothing on stderr. The entry is `applied` all the same.
**－** A `lesson` entry and an entry marked `failed` tick no line. A `delete` or an `update` that fails leaves the `read` lines of its slug as they stand.
**－** A `spec.md` under `vault/archive/` is not read.

## Result

2026-10-05, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
