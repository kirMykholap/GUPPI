---
type: decision
case: "427"
status: current
update: ["[[rule-materialize]]"]
origin: raw/2026-09-25/1654/ledger.md#case-427
sprint: migration
created: 2026-09-25
tags: [harness, workflow, ledger]
---

## Context

In the ledger of session 1228, line 40 is the reading of `estimate-frame-check-finds-a-contradiction`, taken on the old Criterion, on dispatches of `frame-guppi`. In the same Spec Case 419.2 replaced that Criterion whole and renamed the page to `estimate-case-build-writes-the-case`. So `generate` does not find the page, sets `failed` on the entry and repeats that error at each run. The handoff of session 1228 asked not to apply this reading: by case 283 a reading of an Estimate is not taken while its new Criterion is not built.
While the entry carries `failed`, the yaml of session 1228 is not applied whole. The function `applied_whole` in `guppi/render.py` asks every entry for `applied` or `superseded_by`, and none with `failed`. So `render` does not tick the render lines in the Spec of session 1228, and `kept_reason` in `guppi/archive.py` keeps the unit in `raw/`. All other entries and decisions of this yaml carry `applied`.
There is no mark that retires a reading entry by a decision. Only `materialize` sets `superseded_by`, from a `{supersedes:case N}`, and only on an entry with `case`. A reading entry has no field `case`. The mark cannot be derived automatically: by case 280 a reading that stands in the ledger after the decision line of its own Case counts as a reading of the new Criterion. Such a rule would also retire legitimate readings of Work Mode. The person chose a one-off migration signed by this Case.
The value of the mark is `427`, not `419.2`. Case 419.2 replaced the Criterion and renamed the page, but it signed nothing about the reading entry. This Case signs the retirement of the entry. The code already accepts such an entry without a change. `generate` skips an entry with `superseded_by` without a line on stderr. It writes a decision page only for an entry with `case`, so nothing is written for this entry. `superseded_cases` reads only entries with `case`, so no section of the Spec is skipped. `materialize` does not touch the entry again: it appends only lines that are not in the yaml, and lifts again only an entry with `failed` and no `kind`. Only words change: the docstring of `guppi/materialize.py` lists the writer of each field of an entry and gets a second writer of `superseded_by`, and the Purpose of `rule-materialize` says the same.
What the frame check showed. `rule-permissions` says that a script writes `materialize.yaml` and that this write is not allowed to the agent. That stays true: the list of permissions does not change, the client asks the person before this edit, and this Case signs the edit itself. The list of yaml marks in `rule-documentation` says nothing of `superseded_by`, so it also stays true. The Criterion of `estimate-materialize-marks-superseded` promises that an entry without `case` gets no mark from `materialize`. `materialize` does not change, so that also stays true. The Criteria of `estimate-render-harness-ticks-the-spec`, `estimate-raw-archive` and `estimate-generate-fails-alone` speak of an entry with `superseded_by` in general. Their behaviour does not change, so none of them gets an `update`. The edit of the Purpose touches no Estimate.
What the Case does not do. The `read` line in the Spec of session 1228 for the reading of the new Criterion stays unticked: that reading is still to be taken, and the line names the old slug `estimate-frame-check-finds-a-contradiction` until the migration of Case 432 writes the new one. The unit 1228 is dated by the day of the run, so `archive` takes it only at a run on a later day. The open Insight `insight-retro-reading-taken-on-a-criterion-the-session-replaces` asks for the check that keeps such a reading from being written; Case 428.1 brings it in, not this Case.

## Problem

The entry of ledger line 40 of session 1228 never applies, and there is no mark that retires it by a decision. So the unit 1228 is not applied whole, its render lines are not ticked, and `archive` keeps it. It must be decided by which mark and by which writer to retire the entry.

## Given

`raw/2026-09-25/1228/materialize.yaml` — the yaml of session 1228; its entry of ledger line 40, the reading of `estimate-frame-check-finds-a-contradiction`
**＋** `rule-materialize` — the rule of `materialize`; its Purpose says who marks an entry `superseded_by`
**＋** `guppi/materialize.py` — its docstring lists each field of an entry with its writer
**＋** `guppi/generate.py` — `apply`, which skips an entry with `superseded_by`
**＋** `guppi/render.py` — `applied_whole`, the test before the render lines of a Spec are ticked
**＋** `guppi/archive.py` — `kept_reason`, the test before a unit moves to the archive
**＋** `raw/2026-09-25/1228/spec.md` — the Spec of session 1228, which holds its render lines

## History

- 2026-09-25 created · raw/2026-09-25/1654/ledger.md#case-427
