## Case 463 — A delete ticks the read lines of the Estimate it removes

> **context:**
> After `generate` applies an entry, it ticks the matching lines of the Spec. A `delete` entry ticks only its own line, `- [ ] delete `<slug>``, in the section of its Case (`tick_spec`, case 226.1). A `read` line is ticked only by a reading: an `estimate` entry, or a `create` with a folded reading. `tick_read` then ticks the line in every live Spec of `vault/raw/`. It skips the Cases ratified after the reading and the superseded Cases (cases 270.1, 280, 286, 326). When a later Case deletes an Estimate, no reading of it will ever stand in the ledger, so its `read` box stays `[ ]`. The librarian's Next session `Work` list then names that box as work to do until its Spec is archived.
> Case 456 deferred this onto `rule-page-generation`. The box it saw was `- [ ] read `estimate-prespec-checks-the-ratified-copy`` of Case 441.5, which Case 445.4 deleted. That box stands in `vault/archive/migration/2026-09-26/1745/raw/spec.md`. The person chose to leave it as it is. `generate` does not read the archive, and case 326 keeps an archived open line as the record of a task nobody performed.
> The person decided the following. A `delete` entry ticks the `read` lines of its slug by the same ticker as a reading. It uses both skips: superseded Cases in every Spec, and, in the Spec beside the yaml, Cases whose first decision entry has a greater ledger `line` than the delete. The second skip matters because an `update` can bring an archived page back (case 105.3). A Case ratified after the delete may then carry a new `read` line of that slug, and the delete must not close it.
> In the Purpose of `rule-page-generation`, the first pair replaces the list of entries that tick the `read` lines, which is the subject of the sentence on the reading ticks. The second pair replaces the skip of a Case ratified after the reading, in the same sentence. Each anchor stands once in the Purpose.
> Of the Estimates of the rule, only `estimate-generate-ticks-the-spec` speaks of the ticks, so this Case replaces its Criterion whole. `estimate-generate-writes-the-decision-page` names `delete` only as a list of the Decision page, and the change leaves that list alone.
> `rule-retro` stands. Retro counts only the boxes of its own session's Spec. The librarian ticks such a line after Retro, as it does the lines of a reading.
> This Case creates no page, so no vault query was run. The decision line carries `{supersedes:case 456}`, so `generate` clears the defer from `rule-page-generation`.

> **problem:**
> A `read` box of an Estimate that a `delete` removed never closes. No reading of a deleted page will stand in the ledger, so `generate` never ticks the line. The librarian's `Work` list then names work that nobody can do.

> **recommend:**
> When `generate` applies a `delete` entry, it should tick the `read` lines of the deleted slug through `tick_read`. The Spec order and both skips of a reading apply. The ledger's `delete` line is the record of why the box closed, and no second judgment of a closed box is written. Three options were rejected: removing the line rewrites a signed Spec, a skip in each reader copies one judgment into two places, and leaving the box keeps a false item in the brief.

> **given:**
> `estimate-generate-ticks-the-spec` — the promise of the ticks of the Spec, whose Criterion this Case replaces whole
> **＋** `rule-page-generation` — its Purpose, the sentence on the ticks of the Spec
> **＋** `guppi/generate.py` — `tick` and `tick_read`, and the paragraph on the Spec in the docstring of the module
> **＋** `tests/test_generate.py` — the tests of the ticks
> **＋** `materialize.yaml` — the entries `generate` applies, with their `line` and their `superseded_by` marks
> **＋** `vault/raw/<date>/<HHMM>/spec.md` — the live Specs whose lines are ticked
> **＋** `vault/archive/` — the archived Specs, which are not read

> **when:**
> `uv run guppi generate` applied an entry of `materialize.yaml` and marked it `applied`.

> **then:**
> For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit, the first unticked line `` - [ ] <kind> `<slug>` `` in the section of the entry's Case becomes `- [x]`. Nothing else in the file changes. Each further entry of one kind and slug in one Case ticks the next such line, in order.
> **＋** For an `estimate` entry, a `create` entry with `folded` and a `delete` entry, every unticked line `` - [ ] read `<slug>` `` of every `spec.md` under `vault/raw/` becomes `- [x]`. The Spec beside the yaml comes first, then the Specs of the other session folders, oldest first.
> **＋** In the Spec beside the yaml, for an `estimate` or a `delete` entry, a `read` line in the section of a Case whose first decision entry carries a `line` greater than the entry's `line` is not the entry's line, and the search goes on.
> **＋** In any Spec, a `read` line in the section of a Case whose entries are marked `superseded_by` is not the entry's line. For the Spec beside the yaml, the marks come from the run's entries. For another Spec, they come from the `materialize.yaml` beside it. With no yaml beside a Spec, nothing is skipped there.
> **＋** A `create` entry with `folded` ticks both its page line and its `read` line. The filter by `line` does not apply to it, and the filter by `superseded_by` does.
> **＋** A `delete` entry ticks both its page line in its own Case and the `read` lines of its slug.
> **－** A line, a section or a Spec not found raises no error and prints nothing on stderr. The entry is `applied` all the same.
> **－** A `lesson` entry and an entry marked `failed` tick no line. A `delete` that fails leaves the `read` lines of its slug as they stand.
> **－** A `spec.md` under `vault/archive/` is not read.

> **tasks:**
> - [ ] update `rule-page-generation`: two `replace` pairs in the Purpose
>   - old: `` an `estimate` entry, or a `create` with a folded reading, every unticked ``
>   - new: `` an `estimate` entry, a `create` with a folded reading, or a `delete`, whose Estimate no reading will ever reach (case 463), every unticked ``
>   - old: `stands after the reading in the ledger`
>   - new: `` stands after the reading or the `delete` in the ledger ``
>   - change: `a delete ticks the read lines of its slug across the live Specs of raw/, with the skips of a reading (case 463)`
> - [ ] update `estimate-generate-ticks-the-spec`: the Criterion replaced whole
>   - set: `{status: pending, purpose: "generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading or of a deleted Estimate across the Specs of raw/ — never a line of a later or a superseded Case"}`
>   - change: `the Criterion replaced whole — a delete entry ticks the read lines of its slug, with the skips of a reading (case 463)`
> - [ ] `guppi/generate.py`: in `tick`, a `delete` entry also calls `tick_read` over `raw_specs` with the skip of `later_cases` by its `line` and the skip of `superseded_cases`; the docstrings of `tick` and `tick_read` and the paragraph on the Spec in the docstring of the module name case 463
> - [ ] `tests/test_generate.py`: tests that a `delete` of an Estimate ticks its `read` lines in the Spec beside the yaml and in an older Spec of `vault/raw/`; that a `read` line of a Case ratified after the delete stays open; that a `read` line of a superseded Case stays open; that a failed `delete` ticks nothing; and that a Spec under `vault/archive/` stays unchanged
> - [ ] read `estimate-generate-ticks-the-spec`: `uv run pytest tests/test_generate.py` in a later session

> **ratification:**
> ```
> - decision[case 463][update][rule-page-generation]{ref:rule-page-generation}{supersedes:case 456}
> - decision[case 463][update][estimate-generate-ticks-the-spec]{ref:estimate-generate-ticks-the-spec}
> ```
