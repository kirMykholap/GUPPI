## Case 883 — A retired Case replaces no earlier decision

> **context:**
> `guppi generate` writes a Decision page for every Case of `materialize.yaml`, and for a Case that a later Case retired before its entries applied it writes that page alone: `apply` of `.guppi/guppi/generate.py` skips each entry that carries `superseded_by` and calls `apply_decision` for its Case (case 151). But `Vault.decision`, which writes the page, then walks the record's `supersedes` with no look at the record's own `superseded_by`: it sets each earlier page `superseded` unless it stands `archived`, adds the record to its `superseded_by` by `take_superseded_by`, clears the earlier slug from the `deferred_by` of each target the record names by `clear_deferred_by`, and supersedes the earlier page's `children` by `supersede_children`, each step with a History line and a line of `vault/wiki/log.md`. In session 1805, Case 880 retired Case 878 whole, and `raw/2026-10-17/1805/materialize.yaml` holds the record of 878.22 with `supersedes: [decision-case-875]` and `superseded_by: [decision-case-880.21]`; the run put `decision-case-878.22` into the `superseded_by` of `decision-case-875`, whose `superseded` status `archived_by_cascade` of `generate.py` then turned into `archived` at the cascade of the same run, and wrote on `rule-clean-branch` the History line `defer by decision-case-875 superseded · [[decision-case-878.22]]`, as the brief of that run reports and the pages show. Since 880.21 named Case 875 too, the pages ended in the right state and only the names are wrong; had it not, a put-off would have been cleared by a Case that never applied. This breaks the sentence of the docstring of `generate.py` that an entry with `superseded_by` is not applied and leaves no line. I read whole `Vault.decision`, `take_superseded_by`, `supersede_children`, `clear_deferred_by`, `apply` and `apply_decision` of `generate.py`, and `mark_superseded` of `.guppi/guppi/materialize.py`. By the person's choices the fix stays in `generate.py`: a record that carries `superseded_by` carries out none of its `supersedes`, and its page still lists them. The tags that `mark_superseded` writes in `materialize.yaml` stay: a Grep `pop\("superseded_by|del .*superseded_by|\["superseded_by"\] =` over `.guppi/guppi/` printed `generate.py` and `materialize.py`, both lines that add a name, so no step takes a tag back, and an earlier Case whose entries are not yet applied when a retired Case tagged them is still skipped; that gap is left for a later Case. The lines already written stay as a true record of that run: the History of `rule-clean-branch`, two lines of `log.md` and the `superseded_by` of the archived `decision-case-875`. A Case that retires another and keeps its effect names the earlier decision itself, as 880.21 did, so a rebuilt Case loses nothing. The new condition reads the key that the same function already reads for the two-line body of a Case superseded in its own session, and a Grep `superseded_by|supersedes` over `.guppi/guppi/` printed `casecheck.py`, `archive.py`, `generate.py`, `onward.py`, `materialize.py`, `prespec.py`, `pages.py`, `render.py` and `ratified.py`; in `generate.py` a Grep `get\("superseded_by"\)` printed the reads of the mark by `superseded_cases`, `Vault.decision`, `take_superseded_by` and `apply`, each of them a test of the same key, so the task adds no second judgment. The Criterion of `estimate-generate-writes-the-decision-page` speaks of what a `supersedes` does, so it is replaced whole: each old line stays word for word and one `－` line is added; it already holds more than seven `＋` lines, and the new line adds none. Its `purpose` and `method` do not state the old promise and stand. Its reading at the Retro of this session runs the tests of `test_generate.py`, so `rule-page-generation`, which goes `draft` when the update sets the Estimate `pending`, comes back to `built` once the reading applies in the same run of the librarian. A Grep `once a later Case names it` over `vault/wiki/` printed `glossary.md`, `rules/rule-decisions-schema.md` and `entities/entity-glossary.md`: the status of a Decision page said there would be false for a retired later Case, so the two sources change and their files render again. A Grep `supersedes:case N\}` makes|makes the earlier decision` over the repository outside `vault/raw/` and `vault/archive/` printed `.guppi/guppi/materialize.py`, whose docstring changes too. The row `deferred_by` of the glossary and the sentence of `case-schema.md` that `generate` clears a defer only from the pages the superseding Case names stand, since both state a condition that still holds. A Grep `rule-page-generation|estimate-generate-writes-the-decision-page|generate\.py` over `.guppi/tests/` printed `test_guppi_package.py`, whose docstring names the module for the `reword` it imports, and `test_generate.py`, which runs on a temporary vault; `test_schemas.py` reads the lists and keys of the live `schema.yaml`, which the new text of a field leaves as they are. Case 881.5 changes another sentence of the Purpose of `rule-page-generation`, 881.8 other sentences of `rule-decisions-schema` and 881.24 the Purpose and the rows `origin` and `Librarian` of the table of `entity-glossary`, whose `## Terms` I read whole; the pair here changes the row `Decision (status)` alone, the pairs match none of their `old` texts, and read side by side the new rows say nothing of a supersede and agree with the new row here. Case 882.3 supersedes `decision-case-880.21` at the librarian's run of this session; its record carries no `superseded_by`, so this Case leaves it as it acts today. Case 884 of this session takes up `decision-case-876` by `{supersedes:case 876}` on its `update` of `rule-ledger-write`, and carries over the put-off of that Decision on `rule-orchestration` by a `defer` and an `update` with only a `change`. A Grep `supersedes` over `raw/2026-10-17/2307/ledger.md` printed the lines of 882.3 and 884 alone, and no line retires either Case, so their records carry no `superseded_by` and both marks act as they do today. Case 886 changes `rule-raw-archive`, `.guppi/guppi/sprint_close.py` and an Estimate of `rule-sprint-close`, none of which this Case touches. I read the finished files of Cases 881, 882, 884 and 886 after their builds ended. The pairs of 881.5, 881.8 and 881.24 hit other sentences than the pairs here, and the context of 882 names this Case on the reading of `estimate-generate-writes-the-decision-page` in the words of the `－` line here.

> **problem:**
> `guppi generate` carries out the `supersedes` of a Case that a later Case retired, so a Case that never applied sets an earlier decision superseded, clears a put-off and writes its name into History and `log.md`.

> **recommend:**
> - **How far does the fix go?**
>   - Recommended: (a) page writing only; the tags in `materialize.yaml` stay, and the case where they skip a Case not yet applied is left for a later Case.
>   - Answer: agreed, (a).
> - **What happens to the lines already written?**
>   - Recommended: (a) leave them as a true record of that run.
>   - Answer: agreed, (a).
> - **Does the page of a retired Case still list what it meant to replace?**
>   - Recommended: (a) keep the list; its status shows that nothing of it applied.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, make the field `status` of `rule-decisions-schema` and the row `Decision (status)` of `entity-glossary` carry the same condition as the rule, a later Case retired before its entries applied, and say that the earlier Decision page ends `archived` after the cascade.
>   - Taken: both new texts say that a page does not go `superseded` when another Case retired the naming Case before its entries applied, and `context` says that the cascade archived `decision-case-875`.

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, whose Purpose changes.
> **＋** `.guppi/guppi/generate.py`: `Vault.decision` and the module docstring.
> **＋** `.guppi/tests/test_generate.py`: the tests of the Decision page.
> **＋** `estimate-generate-writes-the-decision-page`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/materialize.py`: the module docstring on what a `supersedes` mark makes.
> **＋** `rule-decisions-schema`: the field `status` of its Render changes.
> **＋** `vault/wiki/decisions/schema.yaml`: the file rendered from it.
> **＋** `entity-glossary`: the row `Decision (status)` changes.
> **＋** `vault/wiki/glossary.md`: the file rendered from it.
> **＋** `vault/wiki/decisions/decision-case-<N>.md`: the Decision pages that `guppi generate` writes and supersedes.
> **＋** `vault/archive/`: the folder where an archived earlier Decision page may stand.
> **＋** `vault/wiki/log.md`: the feed of page changes that `guppi generate` appends to.

> **when:**
> `uv run --project .guppi guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

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
> **－** A record that carries `superseded_by`, a Case that a later Case retired, still gets its page with its `supersedes`, but that `supersedes` changes no other page: no earlier page or page in its `children` changes `status` or takes the record into `superseded_by`, no target loses a `deferred_by`, and no History line and no line of `vault/wiki/log.md` names the retired page for such a change.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `` has a two-line body naming the superseding Decision, and its status follows the mechanism as for any superseded page (case 299.4); ``
>   - new: `` has a two-line body naming the superseding Decision, and its status follows the mechanism as for any superseded page (case 299.4); a Case whose record carries `superseded_by`, retired by a later Case before its entries applied, still gets its Decision page with its `supersedes`, but that `supersedes` changes no other page and writes no line of History or of `log.md` (as set in case 883); ``
>   - change: `a Case that a later Case retired carries out none of its supersedes`
> - [ ] update `estimate-generate-writes-the-decision-page`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the supersedes of a retired Case changes no other page`
> - [ ] update `rule-decisions-schema`
>   - old: `` `superseded` once a later Case names it, or the page of a Case it is a sub-case of, in `supersedes`, and `archived` the moment ``
>   - new: `` `superseded` once a later Case names it, or the page of a Case it is a sub-case of, in `supersedes`, unless another Case retired that later Case before its entries applied, and `archived` the moment ``
>   - change: `a Decision page does not go superseded by a later Case that another Case retired before its entries applied`
> - [ ] update `entity-glossary`
>   - old: `` `superseded` once a later Case names it, or the page of a Case it is a sub-case of, in `supersedes`, `archived` when ``
>   - new: `` `superseded` once a later Case names it, or the page of a Case it is a sub-case of, in `supersedes`, unless another Case retired that later Case before its entries applied, `archived` when ``
>   - change: `a Decision page does not go superseded by a later Case that another Case retired before its entries applied`
> - [ ] `.guppi/guppi/generate.py`: `Vault.decision` walks the record's `supersedes` only when the record carries no `superseded_by`; the module docstring says so in the paragraph on `supersedes` and beside the sentence of case 151.
> - [ ] `.guppi/guppi/materialize.py`: the module docstring says that the `{supersedes:case N}` of a Case that a later Case retires makes no decision `superseded` in `generate`.
> - [ ] `.guppi/tests/test_generate.py`: a record with `superseded_by` and `supersedes` leaves the earlier page, its `children` and the `deferred_by` of the target its Case names as they stood, with no History line and no line of `log.md` naming it, while its own page lists `supersedes`; and where the retiring record names the same earlier decision, the earlier page and the target name the retiring page alone.
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] `uv run --project .guppi guppi glossary`
> - [ ] read `estimate-generate-writes-the-decision-page`

> **ratification:**
> ```
> - decision[case 883][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 883][update][estimate-generate-writes-the-decision-page]{ref:rule-page-generation}
> - decision[case 883][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 883][update][entity-glossary]{ref:entity-glossary}
> ```
