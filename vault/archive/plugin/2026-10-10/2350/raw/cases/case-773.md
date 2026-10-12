## Case 773 — A superseded page takes its History line once

> **context:**
> When a later Case supersedes an earlier one, `guppi generate` marks the earlier Decision page `superseded`, adds the new page to its `superseded_by` and writes one History line `superseded by decision-case-<N>`; each History line is copied into `vault/wiki/log.md`. The same step marks the pages of the earlier Case's sub-cases. In `guppi/generate.py` the step for a page named in `supersedes` adds the slug to `superseded_by` only when it is not there, but writes the History line either way; the step for a sub-case writes it only when it adds the slug. Last session one decision line of the ledger `raw/2026-10-10/1913/ledger.md` superseded case 764 and case 764.1 together: the parent step marked `decision-case-764.1` first, then the named step wrote its line again. A Grep `decision-case-764.1 superseded` over `vault/wiki/log.md` printed two lines, and the archived page `vault/archive/plugin/2026-10-10/1913/decisions/decision-case-764.1.md` holds the line twice in its History. The person chose to leave those two lines as the record of that run; only later runs change. The code breaks a promise that already stands: the Criterion of `estimate-generate-writes-the-decision-page` says a page whose `superseded_by` already names the new page gets no second History line, and the Purpose of `rule-page-generation` says an archived page takes one History line. The person chose to replace that Criterion whole, the line made explicit for a page marked earlier in the same record, so that the Estimate goes `pending` and the Retro of this session reads it again; the old line on a page whose `superseded_by` already names the new page is not carried as it stood, since its new form in `then` says the same and adds the `log.md` line and the earlier step of the same record. Its `method` ends with a live reading in the librarian's run, which the check of `/pre-spec` refuses on a Criterion replaced whole as a method that waits for another session, so the update sets the method to the test run alone; its `purpose` names no supersede and stands. A Grep `superseded by` over `guppi/` printed `guppi/generate.py` and `guppi/prespec.py`; the hits in `guppi/prespec.py` are the text of a finding on a Case still in the plan, not this judgment, so the check of `superseded_by` before the History line lives in `guppi/generate.py` alone and the task moves both its copies there into one helper. A Grep `estimate-generate-writes-the-decision-page` over `tests/` printed `tests/test_generate.py`, a comment line, so no test reads that page live. A Grep `one History line|superseded_by` over `vault/wiki/rules/` printed `rule-raw-archive.md`, `rule-page-generation.md`, `rule-materialize.md` and `rule-decisions-schema.md`, and over `.claude/` printed nothing; the hits in `rule-page-generation.md` and `rule-decisions-schema.md` already state one mark per page, the other two speak of the marks of the yaml, and none is made false.

> **problem:**
> `guppi generate` writes the History line `superseded by` a second time, and a second line in `vault/wiki/log.md`, when one record supersedes an earlier page that an earlier step of the same record already marked, such as a sub-case whose parent the same line supersedes.

> **recommend:**
> - **How should the doubled line be prevented?**
>   - Recommended: (a) write the line only when the name is new; one helper holds the check and both steps call it; a test supersedes a parent and one of its sub-cases in one line.
>   - Answer: agreed, (a).
> - **What about the two doubled lines already written?**
>   - Recommended: (a) leave them as the record of that run.
>   - Answer: agreed, (a).
> - **Which check confirms the fix?**
>   - Recommended: (b) replace the Criterion of `estimate-generate-writes-the-decision-page` whole, its line made explicit for a page marked earlier in the same run, so it goes `pending` and the Retro of this session reads it again.
>   - Answer: agreed, (b).

> **given:**
> `estimate-generate-writes-the-decision-page`: its Criterion is replaced whole and its method set anew.
> **＋** `rule-page-generation`: the rule the Estimate checks.
> **＋** `rule-one-judgment-one-implementation`: one check of `superseded_by` in one place.
> **＋** `guppi/generate.py`: writes the Decision pages and the `superseded by` History lines.
> **＋** `tests/test_generate.py`: the tests of the Decision page.
> **＋** `materialize.yaml`: the yaml whose entries and `decisions` records `generate` applies.
> **＋** `vault/wiki/decisions/decision-case-<N>.md`: a Decision page, live in `vault/wiki/decisions/` or archived under `vault/archive/`.
> **＋** `vault/wiki/log.md`: the feed that takes a copy of each History line.

> **when:**
> `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

> **then:**
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
> **＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded`, unless it stands `archived`, and appends to its `superseded_by`, and does the same to each page in the `children` of the earlier page, at any depth, that stands `current`, a page of an earlier session too. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
> **＋** An earlier page that stands `archived`, under `vault/archive/` or under `vault/wiki/decisions/`, keeps `status: archived` and its place; it takes the new page into its `superseded_by` with one History line `superseded by decision-case-<N>`, and it removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, as for a page that stands `current`.
> **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`; neither does a page reached only through `children` clear a `deferred_by`.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
> **－** The Decision pages already written are not rewritten.
> **－** A page whose `superseded_by` already names the new page gets no second History line and no second line in `vault/wiki/log.md`, whether an earlier run put the name there or an earlier step of the same record did, such as a sub-case page reached through the `children` of its parent and named in `supersedes` too.
> **－** A page in `children` that stands `archived` or `superseded` is left as it is.
> **－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.

> **tasks:**
> - [ ] `guppi/generate.py`: one helper adds the superseding page to `superseded_by` and writes the History line only when it adds it; the step for a page named in `supersedes` and the step for a sub-case both call it.
> - [ ] `tests/test_generate.py`: a record supersedes a parent and one of its sub-cases; the sub-case page holds one `superseded by` History line and `vault/wiki/log.md` one line for it; the test fails without the change of `guppi/generate.py`.
> - [ ] update `estimate-generate-writes-the-decision-page`
>   - set:
>     ```
>     status: pending
>     method: uv run pytest tests/test_generate.py, the tests of the Decision page
>     ```
>   - change: `the Criterion replaced whole — a page whose superseded_by already names the new page, by an earlier step of the same record too, gets no second History line and no second log line; the method is the test run alone`
> - [ ] read `estimate-generate-writes-the-decision-page`

> **ratification:**
> ```
> - decision[case 773][update][estimate-generate-writes-the-decision-page]{ref:rule-page-generation}
> ```
