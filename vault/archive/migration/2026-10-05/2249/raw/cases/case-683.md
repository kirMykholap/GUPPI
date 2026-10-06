## Case 683 — A supersede leaves an archived Decision in the archive

> **context:**
> When a Case carries `{supersedes:case N}`, `guppi generate` sets the page `decision-case-N` to `superseded` and adds the new Decision to its `superseded_by`. The cascade of the same run archives each Decision page under `vault/wiki/decisions/` that stands `superseded`, and `guppi cleanup` moves it to `vault/archive/`. Where `decision-case-N` already stands `archived` in the archive — superseded before, or archived by `guppi sprint-close` — `generate.decision` finds it there and sets it `superseded` again. The cascade does not look in the archive, so `cleanup` sees a page there whose status is no longer `archived` and moves it back to `vault/wiki/decisions/`. The next run archives it again. The page makes a round trip and gains History lines, with no change of meaning. Case 469 put off the fix on `rule-page-generation`, after session 2050 saw it once case 467.3 let one Decision be superseded by two Cases. This session meets it: Case 676 supersedes the Decisions of 19 Cases, from case 183 to case 322, and a Glob `vault/archive/**/decision-case-{183,206,218,231,242,248,252,254,260,263,269,276,281,285,289,293,303,307,322}.md` printed 19 paths, all under `vault/archive/migration/2026-09-28/1318/decisions/`. The code of this Case runs from the working tree as soon as Work Mode writes it, so the librarian's run of this session applies those marks to those 19 pages with the fix.
> The person agreed to take this item up beside Case 682, as a narrow fix of the pipeline: code and a test. The fix is the behaviour the defer of case 469 states: the archived page stays `archived` where it lies and takes the new Decision into `superseded_by`. It gets one History line `superseded by decision-case-M`, since `rule-decisions-schema` dates every change of `superseded_by` in History. The defers that the later Case retires are cleared as for any supersede (case 467.3). The test `test_a_later_case_superseding_the_archived_decision_clears_the_page_it_names` already covers that, and it gains the check that the page stays archived. A page that stands `current` is not changed by this Case: it still becomes `superseded`, and the cascade archives it. The last update in the History of `rule-page-generation` is case 672, which ticks the read lines of an Estimate closed by the person; case 673 updated `rule-orchestration`, by its line in `log.md`. Neither covers this. The step of case 660.3 already leaves an archived sub-case page alone, but `generate.decision` still sets the named page itself `superseded`. The update of `rule-page-generation` carries `{supersedes:case 469}`, which retires its one defer.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The frame. A Grep `once a later Case names it|sets the earlier page` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 4 files: `vault/wiki/glossary.md`, `vault/wiki/estimates/estimate-generate-writes-the-decision-page.md`, `vault/wiki/entities/entity-glossary.md` and `vault/wiki/rules/rule-decisions-schema.md`. The field `status` in the Render of `rule-decisions-schema` says a Decision becomes `superseded` once a later Case names it; that turns false for an archived page, so a pair adds the exception, and `uv run guppi render` writes `vault/wiki/decisions/schema.yaml`. Its Estimate `estimate-decisions-schema-checked` checks the lists and other prose of the file, not this sentence, so it stands. The row `Decision (status)` of `entity-glossary` says the same, so a pair adds the exception there, and `uv run guppi glossary` writes `vault/wiki/glossary.md` from it. `estimate-glossary-terms-defined` checks that no row contradicts its `where` page, which the pair keeps true, so it stands. `estimate-generate-writes-the-decision-page` says what a `supersedes` does to the earlier page, so its Criterion is replaced whole: its line on a `supersedes` gains the words "unless it stands `archived`", and a new line states what an archived page gets, while the other lines stay as they are; its `purpose` and `method` do not state the old promise, and they stand. `estimate-generate-cascades` says the cascade archives a `superseded` Decision page; that stays true, so it stands. The docstring of `guppi/generate.py` states the same sentence across a line break, so the Grep did not print it; the code task rewrites it. `guppi/cleanup.py` does not change: it still brings back a page whose status is no longer `archived`, which an `update` of an archived page needs (case 105.3).

> **problem:**
> A later Case that supersedes a Decision already in the archive sets it `superseded` again, so `cleanup` brings it back to the live vault and the next run archives it again, with History lines that change no meaning.

> **recommend:**
> - Recommended: an archived Decision that a later Case supersedes stays `archived` where it lies and only takes the later Decision into `superseded_by`, with one History line; the code of `generate.decision`, its test, the Criterion of `estimate-generate-writes-the-decision-page`, and the exception written into `rule-decisions-schema` and `entity-glossary`.
>   Answer: ratified as built
> - **Change**
>   - Asked: the person agreed to the fixes of the pre-spec report: the new line of the Criterion narrows the defers it clears to the targets a decision line of the superseding Case names, and `context` counts the archived Decisions of Case 676.
>   - Taken: the new line of the Criterion of `estimate-generate-writes-the-decision-page` names the same condition as the line after it; `context` says that all 19 Decisions that Case 676 supersedes stand in the archive, by a Glob over the 19.

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, whose defer of case 469 this Case takes up.
> **＋** `guppi/generate.py`: `generate.decision`, which applies a `supersedes` to the earlier page.
> **＋** `tests/test_generate.py`: the tests of the Decision page.
> **＋** `estimate-generate-writes-the-decision-page`: its Criterion is replaced whole.
> **＋** `guppi/cleanup.py`: `guppi cleanup`, which moves back from the archive a page that stands other than `archived`.
> **＋** `rule-decisions-schema`: the shape of a Decision page, rendered into `vault/wiki/decisions/schema.yaml`.
> **＋** `entity-glossary`: the terms, rendered into `vault/wiki/glossary.md`.

> **when:**
> `uv run guppi generate` of `guppi/generate.py` applies a Case whose decision line supersedes an earlier Decision page that stands `archived` in the archive; `guppi cleanup` of `guppi/cleanup.py` runs after it.

> **then:**
> The earlier Decision page keeps `status: archived` and stays where it lies in the archive.
> **＋** Its `superseded_by` takes the Decision page of the later Case, with one History line that names that page.
> **＋** Each page that a decision line of the later Case names drops the earlier page from its `deferred_by`, as for a page that stands `current`.
> **＋** `guppi cleanup` does not move the earlier page back among the live Decision pages.
> **－** A Decision page that stands `current` still becomes `superseded`, and the cascade archives it.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `` and no `deferred_by` is cleared through them (case 660.3); ``
>   - new: `` and no `deferred_by` is cleared through them (case 660.3); a page that a later Case supersedes while it stands `archived` stays `archived` where it lies: it takes the later Decision into its `superseded_by`, with one History line, and the `deferred_by` the later Case clears is cleared as for any page (case 467.3), so `cleanup` does not bring it back (case 683); ``
>   - change: `a supersede of a Decision already archived keeps it archived and only appends the superseding Case to its superseded_by, so cleanup does not bring it back (case 683)`
> - [ ] update `estimate-generate-writes-the-decision-page`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.
>
>     Then:
>     One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
>     **＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
>     **＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
>     **＋** The page is written before the first entry of its lines, so their History lines name it.
>     **＋** A `supersedes` sets the earlier page `superseded`, unless it stands `archived`, and appends to its `superseded_by`, and does the same to each page in the `children` of the earlier page, at any depth, that stands `current`, a page of an earlier session too. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
>     **＋** An earlier page that stands `archived`, under `vault/archive/` or under `vault/wiki/decisions/`, keeps `status: archived` and its place; it takes the new page into its `superseded_by` with one History line `superseded by decision-case-<N>`, and it removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, as for a page that stands `current`.
>     **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`; neither does a page reached only through `children` clear a `deferred_by`.
>     **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
>     **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
>     **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
>     **－** The Decision pages already written are not rewritten.
>     **－** A page whose `superseded_by` already names the new page gets no second History line.
>     **－** A page in `children` that stands `archived` or `superseded` is left as it is.
>     **－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.
>     ```
>   - change: `the Criterion replaced whole — a supersedes leaves an earlier page that stands archived archived, and only appends to its superseded_by (case 683)`
> - [ ] update `rule-decisions-schema`
>   - old: `a superseded Decision no longer describes the present (case 104.1);`
>   - new: `` a superseded Decision no longer describes the present (case 104.1); a page that stands `archived` when a later Case names it stays `archived` and only takes that Case into `superseded_by` (case 683); ``
>   - change: `a Decision page already archived stays archived when a later Case supersedes it (case 683)`
> - [ ] update `entity-glossary`
>   - old: `` `archived` when the cascade of `generate` then meets it | ``
>   - new: `` `archived` when the cascade of `generate` then meets it; a page already `archived` stays `archived` when a later Case names it | ``
>   - change: `the row Decision (status): a page already archived stays archived when a later Case supersedes it (case 683)`
> - [ ] `guppi/generate.py`: `generate.decision` sets the earlier page `superseded` only when it does not stand `archived`; it still appends to `superseded_by`, writes the History line, clears the defers and supersedes the children; the module docstring on a `supersedes` says so.
> - [ ] `tests/test_generate.py`: `test_a_later_case_superseding_the_archived_decision_clears_the_page_it_names` asserts the archived page keeps `status: archived`, stays under `vault/archive/`, names `decision-case-4` in `superseded_by` with one History line, and that no page `vault/wiki/decisions/decision-case-2.md` is written; a test that a page standing `current` still becomes `superseded` stands.
> - [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] `uv run guppi glossary`
> - [ ] read `estimate-generate-writes-the-decision-page`

> **ratification:**
> ```
> - decision[case 683][update][rule-page-generation]{ref:rule-page-generation}{supersedes:case 469}
> - decision[case 683][update][estimate-generate-writes-the-decision-page]{ref:rule-page-generation}
> - decision[case 683][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 683][update][entity-glossary]{ref:entity-glossary}
> ```
