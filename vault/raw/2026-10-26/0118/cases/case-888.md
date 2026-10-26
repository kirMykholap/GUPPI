## Case 888 — A Case replaced before its entries applied is written superseded

> **context:**
> When `guppi generate` applies a session, it skips every entry of `materialize.yaml` that carries `superseded_by`, and writes the Decision page of its Case all the same (`apply` of `.guppi/guppi/generate.py`, case 151). `Vault.decision` writes every new page with `status: current`. The earlier page goes `superseded` only later, when the page of the Case that replaced it walks its `supersedes`. Case 883 stopped that walk for a record that itself carries `superseded_by`, a Case that another Case retired. So in a chain where B replaces A, then C retires B and does not name A, the entries of A and of B are skipped, and the page of A stands `current` with no `superseded_by`, though nothing of A applied. The person holds that the skip is right: B replaced A first, so A must not apply after C retires B, and the tags that `mark_superseded` of `.guppi/guppi/materialize.py` writes stay. By the person's choices, `Vault.decision` writes a new page `superseded` when its record carries `superseded_by`, and names in `superseded_by` the slugs the record holds (B in the chain), each by `take_superseded_by`, which writes one History line and one line of `log.md`. Where B stands, B's walk then finds its name already there and writes no second line, so the end state is as today. A page that already stands is skipped as before, so a Case whose entries already applied stays `current` when the Case that replaced it is retired. The cascade then archives the new `superseded` page, as `estimate-generate-cascades` already checks. I read whole `Vault.decision`, `take_superseded_by`, `supersede_children`, `clear_deferred_by`, `Vault.history`, `apply`, `apply_decision` and `archived_by_cascade` of `generate.py`, and `mark_superseded` of `materialize.py`, which writes `decision-case-<by>` into the record of every Case of the family it marks. The rule that governs the choice of the slug is `rule-page-generation`: the script lays the content of `materialize.yaml` into fields and invents nothing. B is in the record, while naming C would need a walk of the chain that no step of the page names. The new condition reads the same key that `Vault.decision` already reads for the two-line body and for the guard of case 883. A Grep `get\("superseded_by"\)` over `.guppi/guppi/generate.py` printed 5 lines: in `superseded_cases`, in `Vault.decision` twice, in `take_superseded_by` and in `apply`. Each is a test of the same key, so the task adds no second judgment. The Criterion of `estimate-generate-writes-the-decision-page` speaks of `status: current` and of what the record of a retired Case changes, so it is replaced whole: its first line names the new status, one `＋` line is added, and the last `－` line says where the earlier page takes the name from. Each other line stays word for word. It already holds more than seven `＋` lines. Its `purpose` and `method` do not state the old promise and stand. `estimate-generate-fails-alone` says that an entry with `superseded_by` leaves no line, and the Decision page of its Case is still written. That stands, since the line it means is the History line of the entry on its target. The new History line is on the Decision page. `estimate-decisions-schema-checked` and `estimate-glossary-terms-defined` stand: the lists of the schema do not change, and the row and its `where` page get the same clause. A Grep `retired that later Case` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/glossary.md`, `vault/wiki/entities/entity-glossary.md` and `vault/wiki/rules/rule-decisions-schema.md`. Each says that a page stays `current` when another Case retired the Case that names it, which the change makes false for a page whose own entries never applied, so the two sources change and their files render again. I read the `## Terms` of `entity-glossary` whole. The pair changes the row `Decision (status)` alone. The rows `ref`, `slug`, `supersedes`, `Decision page`, `deferred_by` and `archived` stand, since none of them says what status a new Decision page takes, and the row `archived` already says that the cascade archives a superseded Decision. A Grep `` status follows the mechanism|makes no decision `superseded` `` over the same paths printed `vault/wiki/rules/rule-page-generation.md` and `.guppi/guppi/materialize.py`, and the docstring of `generate.py` holds the first sentence across a line break. All three change. A Grep `\["superseded_by"\] = |superseded_by=\[` over `.guppi/tests/` printed four lines of `test_generate.py`. I read each test there against the new code. The two tests of the case where a Case is superseded in its own session expect the earlier page `superseded` or `archived`, naming the later Case. The fixture of `other_session` marks only an entry. The tests of case 883 assert only on pages that already stand and on lines that name the retired Case, and the new page of that Case names the Case that retired it. All of them pass on the new code by that reading. The tests that read the live vault, `test_schemas.py` and `test_generate.py` on the lists of `schema.yaml` and `test_guppi_package.py` and `test_ship.py` through `ship.ship`, are not broken by new prose that carries its pointer in a bracket at the end of its sentence. The brief reports at its last reading `uv run --project .guppi guppi test: 1768 passed, 6 skipped, 1 deselected (exit 0)`. No other Case of this session is ratified or shown, and Case 883 of session 2307 is the Case this one extends.

> **problem:**
> A Case that a later Case replaced before its entries applied keeps a Decision page that stands `current` and names no Case that replaced it, when the Case that replaced it is retired in turn, though nothing of it applied.

> **recommend:**
> - **Which Case does A's page name as the one that replaced it?**
>   - Recommended: (a) B, the Case the mark on A's record names; nothing is invented and no chain is walked.
>   - Answer: agreed, (a).
> - **Does A's page date that change in its history?**
>   - Recommended: (a) one History line, and one line of the log, at once, as for any page that goes superseded.
>   - Answer: agreed, (a).
> - **How do the texts that define the page status read?**
>   - Recommended: (a) add one clause to both texts for a page whose own entries never applied.
>   - Answer: agreed, (a).

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
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, or `superseded` for a record that carries `superseded_by`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
> **＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded`, unless it stands `archived`, and appends to its `superseded_by`, and does the same to each page in the `children` of the earlier page, at any depth, that stands `current`, a page of an earlier session too. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
> **＋** An earlier page that stands `archived`, under `vault/archive/` or under `vault/wiki/decisions/`, keeps `status: archived` and its place; it takes the new page into its `superseded_by` with one History line `superseded by decision-case-<N>`, and it removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, as for a page that stands `current`.
> **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`; neither does a page reached only through `children` clear a `deferred_by`.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **＋** The new page of a record that carries `superseded_by`, a Case that a later Case superseded before its entries applied, is written `superseded`, takes each slug of the record's `superseded_by` into its own `superseded_by` with one History line `superseded by decision-case-<M>` and one line of `vault/wiki/log.md` per slug, and the cascade of the same run archives it; this holds whether or not another Case retired that later Case in turn.
> **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
> **－** The Decision pages already written are not rewritten.
> **－** A page whose `superseded_by` already names the new page gets no second History line and no second line in `vault/wiki/log.md`, whether an earlier run put the name there or an earlier step of the same record did, such as a sub-case page reached through the `children` of its parent and named in `supersedes` too.
> **－** A page in `children` that stands `archived` or `superseded` is left as it is.
> **－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.
> **－** A record that carries `superseded_by`, a Case that a later Case retired, still gets its page with its `supersedes`, but that `supersedes` changes no other page: no earlier page or page in its `children` changes `status` or takes the record into `superseded_by`, no target loses a `deferred_by`, and no History line and no line of `vault/wiki/log.md` names the retired page for such a change; the page of an earlier Case names the retired Case only when its own record carries it in `superseded_by`.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `` naming the superseding Decision, and its status follows the mechanism as for any superseded page (case 299.4); a Case whose record carries `superseded_by`, retired by a later Case before its entries applied, still gets its Decision page with its `supersedes`, but that `supersedes` changes no other page and writes no line of History or of `log.md` (as set in case 883); ``
>   - new: `` naming the superseding Decision (case 299.4); a Case whose record carries `superseded_by`, retired by a later Case before its entries applied, gets its Decision page `superseded` at once, naming in `superseded_by` each Decision its record names, with one History line for each, whether or not another Case retired that later Case in turn (as set in case 888); it still lists its own `supersedes`, but that `supersedes` changes no other page and writes no line of History or of `log.md` (as set in case 883); ``
>   - change: `a Case replaced before its entries applied gets its Decision page superseded at once, naming the Case its record names`
> - [ ] update `estimate-generate-writes-the-decision-page`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the new page of a record with superseded_by is written superseded`
> - [ ] update `rule-decisions-schema`
>   - old: `` in `supersedes`, unless another Case retired that later Case before its entries applied, and `archived` the moment ``
>   - new: `` in `supersedes`, unless another Case retired that later Case before its entries applied; a page whose own entries never applied, since a later Case's mark skipped them, is written `superseded` and names that later Case, whether or not another Case then retired it, and `archived` the moment ``
>   - change: `a Decision page whose own entries never applied is written superseded, naming the Case that replaced it`
> - [ ] update `entity-glossary`
>   - old: `` in `supersedes`, unless another Case retired that later Case before its entries applied, `archived` when ``
>   - new: `` in `supersedes`, unless another Case retired that later Case before its entries applied; a page whose own entries never applied, since a later Case's mark skipped them, is written `superseded` and names that later Case, whether or not another Case then retired it, `archived` when ``
>   - change: `the row Decision (status): a page whose own entries never applied is written superseded, naming the Case that replaced it`
> - [ ] `.guppi/guppi/generate.py`: `Vault.decision` writes a new page `status: superseded` when its record carries `superseded_by`, and takes each slug of it into the page's `superseded_by` by `take_superseded_by` before it saves the page; the module docstring says so where it says that the status of the two-line page follows the mechanism, and in the paragraph of case 883.
> - [ ] `.guppi/guppi/materialize.py`: the module docstring says that the `{supersedes:case N}` of a Case that a later Case retires still makes `superseded` the earlier Case whose entries it marked before they applied, since that Case's record carries the mark and its new page is written `superseded`.
> - [ ] `.guppi/tests/test_generate.py`: in a chain where B supersedes A and C supersedes B alone, with no page of A yet, the entries of A are not applied, the page of A ends `superseded` or `archived` with `superseded_by` B alone, one History line and one line of `log.md` `superseded by decision-case-B`, and no name of C; and where B stands, the page of A gets that line once.
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] `uv run --project .guppi guppi glossary`
> - [ ] read `estimate-generate-writes-the-decision-page`

> **ratification:**
> ```
> - decision[case 888][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 888][update][estimate-generate-writes-the-decision-page]{ref:rule-page-generation}
> - decision[case 888][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 888][update][entity-glossary]{ref:entity-glossary}
> ```
