---
type: decision
case: "463"
status: current
update: ["[[rule-page-generation]]", "[[estimate-generate-ticks-the-spec]]"]
supersedes: ["[[decision-case-456]]"]
origin: raw/2026-09-27/1819/ledger.md#case-463
sprint: migration
created: 2026-09-27
tags: [harness, workflow, ledger]
---

## Context

After `generate` applies an entry, it ticks the matching lines of the Spec. A `delete` entry ticks only its own line, `- [ ] delete `<slug>``, in the section of its Case (`tick_spec`, case 226.1). A `read` line is ticked only by a reading: an `estimate` entry, or a `create` with a folded reading. `tick_read` then ticks the line in every live Spec of `vault/raw/`. It skips the Cases ratified after the reading and the superseded Cases (cases 270.1, 280, 286, 326). When a later Case deletes an Estimate, no reading of it will ever stand in the ledger, so its `read` box stays `[ ]`. The librarian's Next session `Work` list then names that box as work to do until its Spec is archived.
Case 456 deferred this onto `rule-page-generation`. The box it saw was `- [ ] read `estimate-prespec-checks-the-ratified-copy`` of Case 441.5, which Case 445.4 deleted. That box stands in `vault/archive/migration/2026-09-26/1745/raw/spec.md`. The person chose to leave it as it is. `generate` does not read the archive, and case 326 keeps an archived open line as the record of a task nobody performed.
The person decided the following. A `delete` entry ticks the `read` lines of its slug by the same ticker as a reading. It uses both skips: superseded Cases in every Spec, and, in the Spec beside the yaml, Cases whose first decision entry has a greater ledger `line` than the delete. The second skip matters because an `update` can bring an archived page back (case 105.3). A Case ratified after the delete may then carry a new `read` line of that slug, and the delete must not close it.
In the Purpose of `rule-page-generation`, the first pair replaces the list of entries that tick the `read` lines, which is the subject of the sentence on the reading ticks. The second pair replaces the skip of a Case ratified after the reading, in the same sentence. Each anchor stands once in the Purpose.
Of the Estimates of the rule, only `estimate-generate-ticks-the-spec` speaks of the ticks, so this Case replaces its Criterion whole. `estimate-generate-writes-the-decision-page` names `delete` only as a list of the Decision page, and the change leaves that list alone.
`rule-retro` stands. Retro counts only the boxes of its own session's Spec. The librarian ticks such a line after Retro, as it does the lines of a reading.
This Case creates no page, so no vault query was run. The decision line carries `{supersedes:case 456}`, so `generate` clears the defer from `rule-page-generation`.

## Problem

A `read` box of an Estimate that a `delete` removed never closes. No reading of a deleted page will stand in the ledger, so `generate` never ticks the line. The librarian's `Work` list then names work that nobody can do.

## Given

`estimate-generate-ticks-the-spec` — the promise of the ticks of the Spec, whose Criterion this Case replaces whole
**＋** `rule-page-generation` — its Purpose, the sentence on the ticks of the Spec
**＋** `guppi/generate.py` — `tick` and `tick_read`, and the paragraph on the Spec in the docstring of the module
**＋** `tests/test_generate.py` — the tests of the ticks
**＋** `materialize.yaml` — the entries `generate` applies, with their `line` and their `superseded_by` marks
**＋** `vault/raw/<date>/<HHMM>/spec.md` — the live Specs whose lines are ticked
**＋** `vault/archive/` — the archived Specs, which are not read

## History

- 2026-09-27 created · raw/2026-09-27/1819/ledger.md#case-463
