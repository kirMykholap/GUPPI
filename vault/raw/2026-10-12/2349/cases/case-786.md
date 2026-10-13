## Case 786 — A defer writes a stand-in page only for a rule or an entity

> **context:**
> When the person puts an item off, a short Case writes one `defer` line per page, and at the librarian's run `guppi generate` adds the decision to the `deferred_by` of the page. When the page does not exist, the `defer` method of `guppi/generate.py` writes a stand-in page with `status: draft` and the fields the Case gave, for every vault folder but `estimates`, which case 783 closed. That fits a rule or an entity: `is_placeholder` of `guppi/lint.py` knows a stand-in only in those two folders and gives it one `deferred` finding. For an Insight it goes wrong: `rule-insights-schema` allows only `open`, `actioned` and `archived`, and the stand-in has no `pattern` or `children`. A Lesson page allows only `new`, `clustered` and `archived`, and a Decision page is written only by the script, so a stand-in in those folders is wrong too. Case 783 left the Insight out by the person's choice (handoff of session 2252, For the next session). The person chose three things. A defer with no page writes no page and fails alone. This holds for every kind of page but a rule or an entity. `/pre-spec` reports such a defer by the same judgment. Each part replaces the Criterion of one existing Estimate, as case 783 did for an Estimate: Case 786.1 replaces the Criterion of `estimate-generate-writes`, and Case 786.2 that of `estimate-prespec-checks-the-form-of-an-item`. The `purpose` and `method` of both state no promise that changes, so they stand. In `estimate-generate-writes` the `defer` line and the `－` line on an Estimate are rewritten, not dropped. In `estimate-prespec-checks-the-form-of-an-item` the line on an Estimate, the line on the judgment and the `－` line on an Insight are rewritten, not dropped. The check notes each rewritten line as not carried. The `then` lines of Case 786.2 on a defer share words with lines of Case 786.1. That is meant: 786.1 sets what `guppi generate` does with such a defer, and 786.2 sets what `/pre-spec` reports. These are two promises, checked by two Estimates. A Grep for `^status: draft` over `vault/` with the glob `**/{insights,lessons}/*.md` printed no match, so no stand-in Insight or Lesson stands today and nothing needs to move.
>
> Shared code. The functions each side calls today were read whole. `defer` of `guppi/generate.py` asks `has_page` of `guppi/materialize.py` for an Estimate, then `find`, which reaches a page in any category folder. `check_form` of `guppi/prespec.py` asks `category_of` and `has_page` for an Estimate. `is_placeholder` of `guppi/lint.py` judges a stand-in by the folders `rules` and `entities`, written there as a literal. `generate` and `/pre-spec` already share `has_page`, which finds a page only in its own category folder; case 783 set that judgment, and `has_page` is asked before `find`, so the two sides cannot part on a page in a folder of another category. Case 786.1 adds to `guppi/materialize.py` the constant `PLACEHOLDER_CATEGORIES`, the folders `rules` and `entities`, and the predicate `defer_writes_no_page`. `guppi/generate.py` and `guppi/prespec.py` import the predicate, and `is_placeholder` of `guppi/lint.py` imports the constant in place of its literal, so the folders where a stand-in may stand are one judgment. The behaviour of lint does not change, so the Criterion of `estimate-lint-checks-the-statuses` stands. A Grep for `placeholder|has_page` over `guppi/` printed `guppi/generate.py`, `guppi/glossary.py`, `guppi/lint.py`, `guppi/materialize.py`, `guppi/prespec.py` and `guppi/render.py`. In `render.py` the word means a language placeholder, and in `glossary.py` a page with no `parent`. The hits in `generate.py`, `materialize.py` and `prespec.py` are the docstrings and code the tasks change. The fill of a stand-in by a `create` in `generate.py` stays true, since a stand-in now stands only as a rule or an entity.
>
> Pages. A Grep for `placeholder page|a placeholder|draft placeholder|stand-in|has_page` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `glossary.md`, `entity-glossary.md`, `rule-page-generation.md`, `estimate-generate-writes.md`, `estimate-prespec-checks-the-form-of-an-item.md`, `rule-brief.md`, `rule-decisions-schema.md`, `rule-glossary.md`, `rule-lint.md`, `estimate-glossary-renders-the-terms.md`, `estimate-guppi-config-fills-the-languages.md`, `estimate-lint-checks-the-statuses.md`, `estimate-lint-finds-a-broken-link.md` and `lesson-case-build-reused-judgment-not-checked-against-the-other-side.md`. The Purpose of `rule-page-generation` names the exception of case 783 for an Estimate only, so Case 786.1 widens it. The Types row of `entity-glossary`, rendered into `glossary.md`, says a defer writes a stand-in page when there is no `ref`, so Case 786.1 limits it to a rule or an entity. The last `－` line of the Criterion of `estimate-prespec-checks-the-form-of-an-item` says a defer of an Insight with no page is no finding, so Case 786.2 rewrites it. In `rule-brief`, a deferred item lives on as a draft stand-in or as the open Insight itself, and an Insight is deferred only as a page that stands, so the sentence stays true. In `rule-decisions-schema`, `rule-glossary`, `rule-lint`, `estimate-glossary-renders-the-terms`, `estimate-lint-checks-the-statuses` and `estimate-lint-finds-a-broken-link`, a stand-in is a rule or an entity page, which stays true. In `estimate-guppi-config-fills-the-languages` the word means a language placeholder. The lesson is a record. A Grep for `placeholder|defer of an Estimate|has_page` over `.claude/` printed no match. In `rule-orchestration`, read whole, the sentences on what a defer names are the take-back sentence and the sentence of case 783. The take-back defers each rule, entity and insight page that a ratified Case names, and such an Insight stands, so it stays true. The sentence of case 783 stays true, and Case 786.2 adds the route for the new finding after it, since a short Case has no `case-guppi` to send a finding to. The short-form example defers `entity-booking-export`, an entity, which keeps its stand-in. The change to the Purpose of `rule-page-generation` and to the Render of `rule-orchestration` touches no Estimate (case 378.5). The Criteria of the other Estimates of `rule-page-generation` speak of other steps; `estimate-generate-fails-alone` speaks of any entry that fails, which the new failure joins, so it stands. The Criteria of the Estimates of `rule-orchestration` on a defer speak of the reply, the example and the take-back, which stay true. The Criterion of `estimate-glossary-terms-defined` asks that no row contradict its `where` page, and `rule-case-protocol` says nothing of stand-in pages, so it stands. The text of `rule-insights-schema` says a defer postpones an Insight, which stays true, and the Case does not change it.
>
> Tests that read live files. A Grep for `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_generate.py`, `tests/test_orchestration.py` and `tests/test_schemas.py`. `test_case_schema.py` runs the check of `guppi/casecheck.py`, which reaches `check_form` through `prespec.judge`, over `case-example.md`, which holds no `defer` item. `test_orchestration.py` reads the blocks tagged `showing` and `defer` of `orchestration.md`; the new sentence adds no block, and the `defer` example names an entity, which the new finding does not judge. `test_generate.py` and `test_schemas.py` read only the live `schema.yaml` files, which this Case does not change.

> **problem:**
> A defer of an Insight, a Lesson or a Decision page that does not exist makes `guppi generate` write a stand-in page with `status: draft`, which the format of that page does not allow. Nothing in the session reports such a defer.

> **recommend:**
> - **What should a defer of an Insight that has no page do?**
>   - Recommended: (a) write no page and fail that entry alone, as for a defer of a check with no page.
>   - Answer: agreed, (a).
> - **Which kinds of page does the fix cover?**
>   - Recommended: (b) every kind except a rule or an entity: a stand-in page is written only for a rule or an entity, and a defer of any other kind with no page fails alone.
>   - Answer: agreed, (b).
> - **Should `/pre-spec` also report such a defer before the librarian's run?**
>   - Recommended: (a) yes, by the same test of whether a page exists that `guppi generate` uses; the Case becomes two parts, each rewriting one existing check.
>   - Answer: agreed, (a).

### Case 786.1 — Generate writes a stand-in page only for a rule or an entity

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, whose Purpose names the exception to a page always created.
> **＋** `guppi/generate.py`: the `defer` of an entry and the module docstring.
> **＋** `guppi/materialize.py`: its routing table names the defer with no page; `has_page`, and the new `PLACEHOLDER_CATEGORIES` and `defer_writes_no_page`, which `guppi/generate.py` and `guppi/prespec.py` import.
> **＋** `guppi/lint.py`: `is_placeholder`, which judges a stand-in by the folders where it may stand.
> **＋** `tests/test_generate.py`: the tests of `guppi generate`.
> **＋** `estimate-generate-writes`: its Criterion is replaced whole.
> **＋** `estimate-generate-fails-alone`: the Estimate of an entry that fails alone.
> **＋** `entity-glossary`: the terms, rendered into `vault/wiki/glossary.md`, whose Types row names the stand-in page of a defer.
> **＋** `rule-insights-schema`, `rule-lessons-schema` and `rule-decisions-schema`: the formats whose statuses a stand-in page breaks.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/log.md` and `vault/wiki/tags.md`: the files `guppi generate` reads or appends to; the sprint comes from `vault/wiki/sprint.md`, or from `entity-sprint-<id>` when a unit creates it.
> **＋** `vault/wiki/<category>/`, and a folder `<category>` under `vault/archive/` outside its `raw/` folders: where the page of a slug stands.

> **when:**
> `guppi generate` applies one entry of a yaml to a page.

> **then:**
> A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the `sprint` of the yaml, which `guppi materialize` takes from the first `## <id>` of `sprint.md` or, in a unit whose ledger creates `entity-sprint-<id>`, from that `<id>`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
> **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`, and `deferred_by` after `checked` once a `defer` marks it; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
> **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
> **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
> **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
> **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
> **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
> **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight, estimate) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by` for a rule or an entity only.
> **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
> **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
> **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
> **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
> **－** A `defer` of an Estimate, an Insight, a Lesson or a Decision page whose page stands neither under `vault/wiki/<category>/` nor in a folder `<category>` under `vault/archive/` outside a `raw/` folder, by `defer_writes_no_page` of `guppi/materialize.py`, which asks `has_page`, writes no page: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: an Estimate is deferred only with its page — defer the page it would check` on stderr for an Estimate, and `generate: <slug>: a placeholder is written only for a rule or an entity — defer a page that stands` for the other kinds.
> **－** No body section is derived from a ref field; a section the entry does not name under `sections` or reach by `replace` is not touched.
> **－** An `update` of an Estimate whose `set` carries `method` drops no section.
> **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `` An exception is a `defer` of an Estimate with no page: it writes no page and fails as an entry, since a check that was never created has no reading to put off, and the short Case puts off the page it would check instead (case 783). ``
>   - new: `` An exception is a `defer` with no page of anything but a rule or an entity: it writes no page and fails as an entry. A check that was never created has no reading to put off, and the short Case puts off the page it would check instead (case 783); an Insight is made only by the librarian, and the format of an Insight, a Lesson or a Decision page has no status for a stand-in page (case 786). ``
>   - change: `a defer with no page writes a placeholder only for a rule or an entity; any other kind fails as an entry (case 786)`
> - [ ] `guppi/materialize.py`: a constant `PLACEHOLDER_CATEGORIES`, the folders `rules` and `entities`, and a predicate `defer_writes_no_page(project_dir, category, slug)` — true when `category` is a vault folder of `CATEGORIES` outside `PLACEHOLDER_CATEGORIES` and `has_page` is false; its docstring names `guppi/generate.py` and `guppi/prespec.py` as the modules that import it, and the docstring of `has_page` names it; the line `defer none` of the routing table says that a placeholder is written for a rule or an entity only and that the entry of any other kind fails in `generate` (case 786).
> - [ ] `guppi/generate.py`: in `defer`, an entry for which `materialize.defer_writes_no_page` is true fails before any page is read, with the Estimate line for an Estimate and `a placeholder is written only for a rule or an entity — defer a page that stands` for any other kind, and no page is written; the module docstring and the docstring of `defer` say that a placeholder is written for a rule or an entity only (case 786).
> - [ ] `guppi/lint.py`: `is_placeholder` judges the category by `materialize.PLACEHOLDER_CATEGORIES`, imported, in place of its literal (case 786).
> - [ ] `tests/test_generate.py`: a `defer` of an Insight, of a Lesson and of a Decision page with no page each writes no page, prints its line on stderr, exits 1 and lets the other entries apply; so does a `defer` of an Insight whose file stands under `vault/archive/` in a folder other than `insights/`, or under a `raw/` folder; a `defer` of an Insight that stands in a folder `insights/` under `vault/archive/` appends the decision to its `deferred_by` there; `generate.defer_writes_no_page` is `materialize.defer_writes_no_page`, and `lint.PLACEHOLDER_CATEGORIES` is `materialize.PLACEHOLDER_CATEGORIES`.
> - [ ] update `entity-glossary`
>   - old: `` `defer` postpones, a placeholder page when no `ref`, never for an Estimate, which is put off through the page it would check (case 783) ``
>   - new: `` `defer` postpones, a placeholder page when no `ref` for a rule or an entity only; an Estimate is put off through the page it would check (case 783), and a defer of any other kind with no page fails (case 786) ``
>   - change: `Types: a defer writes a placeholder only for a rule or an entity (case 786)`
> - [ ] `uv run guppi glossary`
> - [ ] update `estimate-generate-writes`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a defer with no page of anything but a rule or an entity writes no placeholder and fails alone`
> - [ ] read `estimate-generate-writes`

> **ratification:**
> ```
> - decision[case 786.1][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 786.1][update][entity-glossary]{ref:entity-glossary}
> - decision[case 786.1][update][estimate-generate-writes]{ref:rule-page-generation}
> ```

### Case 786.2 — Pre-spec reports a defer with no page of anything but a rule or an entity

> **given:**
> `rule-prespec`: the rule of `/pre-spec`, the target of the Estimate.
> **＋** `rule-orchestration`: the rule rendered into `vault/wiki/orchestration.md`, which sets the short Case of a deferred decision.
> **＋** `guppi/prespec.py`: `check_form`, the check of the form of an item, and the module docstring.
> **＋** `guppi/materialize.py`: `defer_writes_no_page`, the one judgment whether a defer names a page, which Case 786.1 adds and which asks `has_page`.
> **＋** `guppi/generate.py`: the `defer` that fails such an entry by the same judgment, by Case 786.1.
> **＋** `tests/test_prespec.py`: the tests of the check.
> **＋** `vault/wiki/<category>/`, and a folder `<category>` under `vault/archive/` outside its `raw/` folders: where the page of a slug stands.
> **＋** `vault/wiki/estimates/`, and a folder `estimates/` under `vault/archive/`: where the page of an Estimate stands.
> **＋** `estimate-prespec-checks-the-form-of-an-item`: its Criterion is replaced whole.

> **when:**
> `uv run guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

> **then:**
> A Case whose `then` block holds two or more Estimate items that set a new Criterion — a `create`, or an `update` that names no part of the page by `names_a_part` of `guppi/materialize.py` — is the finding `case N: two promises in one Case — split it`, whether each item writes its Criterion under `sections` or lifts it.
> **＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
> **＋** A `defer` of an Estimate whose page stands neither under `vault/wiki/estimates/` nor in a folder `estimates/` under `vault/archive/` outside a `raw/` folder is the finding `case N: defer <slug>: no such Estimate page — defer the page it would check`, a short Case under `## Deferred` of the plan included.
> **＋** A `defer` of an Insight, a Lesson or a Decision page whose page stands neither under `vault/wiki/<category>/` nor in a folder `<category>` under `vault/archive/` outside a `raw/` folder is the finding `case N: defer <slug>: no such page — a placeholder is written only for a rule or an entity`, a short Case under `## Deferred` of the plan included.
> **＋** The judgment of both is `defer_writes_no_page` of `guppi/materialize.py`, which asks `has_page` and which the `defer` of `guppi/generate.py` imports too.
> **＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
> **＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.
> **＋** A key of an item of any kind that `item_keys` of `guppi/materialize.py` does not give its kind and category — `slug` a key of every kind — is the finding `case N: <kind> <slug>: key <key> is not a key of this item`.
> **－** An `update` of an Estimate that names a part alone — `set` without `status`, a `replace` pair, a section other than `Criterion` — is not counted.
> **－** A `defer` of a rule or an entity with no page is not a finding.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session creates or updates, is not judged by its keys (case 308.2).

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` `/pre-spec` reports a `defer` of an Estimate with no page; the agent fixes that finding with a new short Case with `{supersedes:case N}` whose `defer` names the page the Estimate would check, as for a wording the person corrects (case 783). ``
>   - new: `` `/pre-spec` reports a `defer` of an Estimate with no page; the agent fixes that finding with a new short Case with `{supersedes:case N}` whose `defer` names the page the Estimate would check, as for a wording the person corrects (case 783). A `defer` of an Insight, a Lesson or a Decision page names a page that stands too, since only a rule or an entity gets a placeholder page, and `/pre-spec` reports one with no page; the agent fixes that finding the same way, with a new short Case with `{supersedes:case N}` whose `defer` names a page that stands (case 786). ``
>   - change: `a defer of an Insight, a Lesson or a Decision page names a page that stands; a pre-spec finding on one with no page is fixed by a new short Case that supersedes it (case 786)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] `guppi/prespec.py`: `check_form` judges each `defer` item whose slug has a category by `materialize.defer_writes_no_page`, imported in place of its direct call of `has_page`, and reports an Estimate with the line it gives today and any other kind with `case N: defer <slug>: no such page — a placeholder is written only for a rule or an entity`; the module docstring and the docstring of `check_form` name it (case 786).
> - [ ] `tests/test_prespec.py`: a `defer` of an Insight and of a Lesson with no page, under a Case heading and under `## Deferred`, gives the new finding, and so does one whose file stands under `vault/archive/` in a folder of another category, or under a `raw/` folder; a `defer` of an Insight that stands live or in a folder `insights/` under `vault/archive/`, and a `defer` of a rule or an entity with no page, give none; `prespec.defer_writes_no_page` and `generate.defer_writes_no_page` are `materialize.defer_writes_no_page`.
> - [ ] update `estimate-prespec-checks-the-form-of-an-item`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a defer with no page of anything but a rule or an entity is a finding`
> - [ ] read `estimate-prespec-checks-the-form-of-an-item`

> **ratification:**
> ```
> - decision[case 786.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 786.2][update][estimate-prespec-checks-the-form-of-an-item]{ref:rule-prespec}
> ```
