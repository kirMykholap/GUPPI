## Case 783 — A defer of a check with no page is refused, not written as a stand-in page

> **context:**
> When the person puts an item off, the main agent writes a short Case with one `defer` line per page, and at the librarian's run `guppi generate` adds the decision to the page's `deferred_by`, through which the page enters `backlog.md`. When the page does not exist, `guppi generate` writes a stand-in page with `status: draft` and the fields the Case gave (the `defer` method of `guppi/generate.py`). That fits a rule or an entity page: lint gives such a page one `deferred` finding (case 186.3). For an Estimate it goes wrong. The format of an Estimate page allows only `pending`, `passed` and `failed`, and the stand-in has no `kind`, `target`, `method` or `## Criterion`, so lint would report it several times. No test covers this path (handoff of session 1604, For the next session). Case 781 made Estimates deferrable. A take-back already avoids the problem: it defers the page that each Estimate it creates would check (case 723.1). The person chose that a defer of an Estimate with no page writes no page. The short Case puts off the page the check would test instead. `/pre-spec` reports such a defer, and `guppi generate` fails the entry alone as a backstop. Each part replaces the Criterion of one existing Estimate. A Grep for `^status: draft` over the files `vault/**/estimates/*.md` printed no match, so no stand-in check page stands today and nothing needs to move.
>
> The person left the stand-in Insight page out. `guppi generate` gives it `status: draft` too, a value the Insight format does not allow (`open`, `actioned`, `archived`). Only the librarian creates Insights, so a defer of a missing Insight does not come up in practice. This Case does not fix it, and it stays open for a later Case.
>
> A Grep for ``placeholder page|draft placeholder|a placeholder `draft`|writes a placeholder|a placeholder —`` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `rule-brief.md`, `glossary.md`, `entity-glossary.md`, `rule-page-generation.md`, `estimate-generate-writes.md` and `estimate-lint-checks-the-statuses.md`. The sentence of `rule-brief` says that every deferred item lives on as a page, a draft stand-in or an open Insight. It stays true, because a check with no page is now put off through a page that stands. Its other hit is a History line. In `estimate-lint-checks-the-statuses` a stand-in is a rule or an entity, which stays true. The Types row of `entity-glossary`, rendered into `glossary.md`, says a defer writes a stand-in page when there is no `ref`, so Case 783.1 adds that an Estimate never gets one. The hit in `rule-page-generation` is the exception for a `create` over a stand-in page, which stays true for a rule or an entity. The line of `estimate-generate-writes` is rewritten by Case 783.1. A Grep for `always created|page is always` over `vault/wiki/`, `.claude/`, `guppi/` and `CLAUDE.md` printed `rule-page-generation.md` and `estimate-materialize-marks-a-comment.md`. The Purpose of `rule-page-generation` says a page is always created, even incomplete, which a refused defer makes false, so Case 783.1 adds the exception. In `estimate-materialize-marks-a-comment` the words say why `generate` applies an entry marked for a comment, which this Case does not touch. A Grep for `placeholder` over `guppi/` printed `guppi/render.py`, `guppi/glossary.py`, `guppi/generate.py`, `guppi/lint.py` and `guppi/materialize.py`. In `render.py` the word means a language placeholder, and in `glossary.py` a page with no `parent`. `is_placeholder` of `lint.py` judges only a rule or an entity, which stays true. The docstrings of `generate.py` and of the routing table of `materialize.py` say a defer with no page writes a stand-in, so both name the Estimate.
>
> In `rule-orchestration`, which Case 783.2 changes and which was read whole, the sentences on what a defer names are the take-back sentence and the sentence that the target of a short Case enters `backlog.md` through its `deferred_by`. The take-back sentence already defers the page an Estimate would check, so it stays true. The new sentence stands after the second one. The Criterion of `estimate-orchestration-defers-in-one-reply` asks for one `defer` item per target. The Criterion of `estimate-orchestration-defer-example-passes-the-hook` speaks of the example block, and the Criterion of `estimate-orchestration-takes-back-a-ratified-case` speaks of the take-back. All three stay true, so they stand. The Estimate that checks the new sentence is the `/pre-spec` finding of Case 783.2. In `entity-glossary`, read whole, the `deferred_by` row, the Estimate row and the Insight row stay true. The Criterion of `estimate-glossary-terms-defined` asks that no row contradict its `where` page, and `rule-case-protocol` says nothing of stand-in pages, so it stands. The `purpose` of `estimate-prespec-checks-the-form-of-an-item` already says an item names a page that exists or is created, so it stands, and so does its `method`. The change to the Purpose of `rule-page-generation` touches no Estimate (case 378.5). The `then` of Case 783.1 is the Criterion of `estimate-generate-writes` as it stands, with one line changed and one `－` line added. It keeps its eleven `＋` lines and one promise. Its `defer` line is rewritten, not dropped, so the check notes it as not carried. The `then` lines of Case 783.2 that speak of a defer share words with lines of Case 783.1. That is meant: 783.1 sets what `guppi generate` does with such a defer, and 783.2 sets what `/pre-spec` reports. These are two promises, checked by two Estimates.
>
> Shared code: a Grep for `def (page_exists|page_paths|archived_paths|live_page)\b` over `guppi/` printed `guppi/generate.py`, `guppi/materialize.py` and `guppi/prespec.py`. `page_exists` of `materialize.py` finds a page under `vault/archive/` at any depth outside `raw/`, whatever folder holds it. `find` of `generate.py`, through `archived_paths`, finds it only in a category folder. So the two answer differently for an Estimate archived outside a folder `estimates/`. Neither is taken as it stands. Case 783.1 adds `has_page` to `materialize.py`, which finds a page only in its own category folder, live or archived outside `raw/`. `guppi generate` and `/pre-spec` both import it, and `generate` asks it before `find`. A page that `has_page` finds is in a category folder, so `find` reaches it too. The tests of both sides put an Estimate in a folder other than `estimates/` under `vault/archive/`, where the two old functions part. A Grep for `has_page` over `guppi/` printed no match, so the name is free. The person was asked about the test of whether a page exists as the one `materialize` uses for a defer. It is now a new shared predicate, because `/pre-spec` found that the two existing functions disagree.
>
> The new finding also falls on a short Case under `## Deferred`. The Render of `rule-prespec` sends a finding in a Case to the `case-guppi` of that Case. A short Case has no `case-guppi`: `rule-orchestration` makes it the agent's own, written with no dispatch, and a wording the person corrects becomes a new short Case with `{supersedes:case N}` (case 405). The new sentence of `rule-orchestration` names that route for this finding, so the sentence of `rule-prespec` stands. It covers a Case that a `case-guppi` built. The rewritten `defer` line of `estimate-generate-writes` promises a stand-in page for a rule or an entity only and promises nothing for an Insight. The code still writes the Insight stand-in, and the docstring of `generate.py` says so only for a rule or an entity. That leaves the Insight defect to a later Case without a promise to replace. Tests that read live files: a Grep for `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_schemas.py`, `tests/test_orchestration.py` and `tests/test_generate.py`. `test_orchestration.py` reads the blocks tagged `showing` and `defer` of `orchestration.md`. The new sentence adds no block, and the `defer` example names `entity-booking-export`, not an Estimate. `test_case_schema.py` runs the check of `guppi/casecheck.py`, which calls `prespec.judge`, over `case-example.md`. That file holds no `defer` item, so the new finding refuses none of it. `test_schemas.py` and `test_generate.py` read only the live `schema.yaml` files, which this Case does not change.

> **problem:**
> A defer of an Estimate with no page makes `guppi generate` write a stand-in check page whose status the check page format does not allow. Nothing in the session reports such a defer.

> **recommend:**
> - **What should a defer of a check that has no page do?**
>   - Recommended: (a) defer the page the check would test: a defer never makes a stand-in check page, and a defer of a check with no page that reaches `guppi generate` fails there alone.
>   - Answer: agreed, (a).
> - **Should this Case also fix the stand-in Insight page?**
>   - Recommended: (a) leave the Insight out; `context` notes the defect as found and not fixed.
>   - Answer: agreed, (a).
> - **What catches a defer of a check with no page before the librarian's run?**
>   - Recommended: (a) `/pre-spec` reports it, by the same test of whether a page exists that the step before `guppi generate` uses for a defer, and `guppi generate` refuses it as a backstop.
>   - Answer: agreed, (a).
> - **Which existing checks should cover the two changes?**
>   - Recommended: (a) two parts, each rewriting one existing check: `guppi generate` fails the defer and `estimate-generate-writes` is rewritten; `/pre-spec` reports it, the rule for short Cases gains one sentence, and `estimate-prespec-checks-the-form-of-an-item` is rewritten.
>   - Answer: agreed, (a).

### Case 783.1 — Generate writes no stand-in page for a check

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, whose Purpose says a page is always created.
> **＋** `guppi/generate.py`: the `defer` of an entry and the module docstring.
> **＋** `guppi/materialize.py`: writes the yaml that `guppi generate` applies; its routing table names the defer with no page, and the new `has_page` is the one judgment whether a page stands, which `guppi/generate.py` and `guppi/prespec.py` import.
> **＋** `tests/test_generate.py`: the tests of `guppi generate`.
> **＋** `estimate-generate-writes`: its Criterion is replaced whole.
> **＋** `estimate-generate-fails-alone`: the Estimate of an entry that fails alone.
> **＋** `entity-glossary`: the terms, rendered into `vault/wiki/glossary.md`, whose Types row names the stand-in page of a defer.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/log.md` and `vault/wiki/tags.md`: the files `guppi generate` reads or appends to; the sprint comes from `vault/wiki/sprint.md`, or from `entity-sprint-<id>` when a unit creates it.
> **＋** `vault/archive/`, outside its `raw/` folders: where an entry finds a page that is not under `vault/wiki/`.
> **＋** `vault/wiki/estimates/`, and a folder `estimates/` under `vault/archive/`: where the page of an Estimate stands.

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
> **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight, estimate) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by` for a rule or an entity.
> **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
> **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
> **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
> **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
> **－** A `defer` of an Estimate whose page stands neither under `vault/wiki/estimates/` nor in a folder `estimates/` under `vault/archive/` outside a `raw/` folder, by `has_page` of `guppi/materialize.py`, writes no page: the entry fails alone with `generate: <slug>: an Estimate is deferred only with its page — defer the page it would check` on stderr (`estimate-generate-fails-alone`).
> **－** No body section is derived from a ref field; a section the entry does not name under `sections` or reach by `replace` is not touched.
> **－** An `update` of an Estimate whose `set` carries `method` drops no section.
> **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `A page is always created, even incomplete: red lint is an accurate signal of debt, a decision with no page is the ledger and the vault disagreeing silently.`
>   - new: `` A page is always created, even incomplete: red lint is an accurate signal of debt, a decision with no page is the ledger and the vault disagreeing silently. An exception is a `defer` of an Estimate with no page: it writes no page and fails as an entry, since a check that was never created has no reading to put off, and the short Case puts off the page it would check instead (case 783). ``
>   - change: `a defer of an Estimate with no page writes no placeholder and fails as an entry (case 783)`
> - [ ] `guppi/materialize.py`: a new predicate `has_page(project_dir, category, slug)` — true when the page stands under `vault/wiki/<category>/`, or in a folder `<category>` under `vault/archive/` outside a `raw/` folder; its docstring names `guppi/generate.py` and `guppi/prespec.py` as the modules that import it; the line `defer none` of the routing table in the module docstring says that an Estimate gets no placeholder and its entry fails in `generate` (case 783).
> - [ ] `guppi/generate.py`: in `defer`, an entry of the category `estimates` for which `materialize.has_page` is false fails with `an Estimate is deferred only with its page — defer the page it would check`, before any page is read, and no page is written; the module docstring and the docstring of `defer` say that a placeholder is written for a rule or an entity, never for an Estimate (case 783).
> - [ ] `tests/test_generate.py`: a `defer` of an Estimate with no page writes no page, prints the line on stderr, exits 1 and lets the other entries apply; so does a `defer` of an Estimate whose file stands under `vault/archive/` in a folder other than `estimates/`, or under a `raw/` folder; a `defer` of an Estimate that stands in a folder `estimates/` under `vault/archive/` appends the decision to its `deferred_by` there.
> - [ ] update `entity-glossary`
>   - old: `` `defer` postpones, a placeholder page when no `ref` ``
>   - new: `` `defer` postpones, a placeholder page when no `ref`, never for an Estimate, which is put off through the page it would check (case 783) ``
>   - change: `Types: a defer writes no placeholder for an Estimate (case 783)`
> - [ ] `uv run guppi glossary`
> - [ ] update `estimate-generate-writes`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a defer of an Estimate with no page writes no placeholder and fails alone`
> - [ ] read `estimate-generate-writes`

> **ratification:**
> ```
> - decision[case 783.1][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 783.1][update][entity-glossary]{ref:entity-glossary}
> - decision[case 783.1][update][estimate-generate-writes]{ref:rule-page-generation}
> ```

### Case 783.2 — Pre-spec reports a defer of a check with no page

> **given:**
> `rule-prespec`: the rule of `/pre-spec`, the target of the Estimate.
> **＋** `rule-orchestration`: the rule rendered into `vault/wiki/orchestration.md`, which sets the short Case of a deferred decision.
> **＋** `guppi/prespec.py`: `check_form`, the check of the form of an item, and the module docstring.
> **＋** `guppi/materialize.py`: `has_page`, the one judgment whether a page stands, which Case 783.1 adds.
> **＋** `guppi/generate.py`: the `defer` that fails an entry of an Estimate with no page by the same judgment, by Case 783.1.
> **＋** `tests/test_prespec.py`: the tests of the check.
> **＋** `vault/wiki/estimates/`, and `vault/archive/` outside its `raw/` folders: where the page of an Estimate stands.
> **＋** `estimate-prespec-checks-the-form-of-an-item`: its Criterion is replaced whole.

> **when:**
> `uv run guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

> **then:**
> A Case whose `then` block holds two or more Estimate items that set a new Criterion — a `create`, or an `update` that names no part of the page by `names_a_part` of `guppi/materialize.py` — is the finding `case N: two promises in one Case — split it`, whether each item writes its Criterion under `sections` or lifts it.
> **＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
> **＋** A `defer` of an Estimate whose page stands neither under `vault/wiki/estimates/` nor in a folder `estimates/` under `vault/archive/` outside a `raw/` folder, by `has_page` of `guppi/materialize.py`, is the finding `case N: defer <slug>: no such Estimate page — defer the page it would check`, a short Case under `## Deferred` of the plan included.
> **＋** The judgment is `has_page` of `guppi/materialize.py`, which the `defer` of `guppi/generate.py` imports too.
> **＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
> **＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.
> **＋** A key of an item of any kind that `item_keys` of `guppi/materialize.py` does not give its kind and category — `slug` a key of every kind — is the finding `case N: <kind> <slug>: key <key> is not a key of this item`.
> **－** An `update` of an Estimate that names a part alone — `set` without `status`, a `replace` pair, a section other than `Criterion` — is not counted.
> **－** A `defer` of a rule, an entity or an Insight with no page is not this finding.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session creates or updates, is not judged by its keys (case 308.2).

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` The target of a short Case enters `backlog.md` through the `deferred_by` that `generate` writes. ``
>   - new: `` The target of a short Case enters `backlog.md` through the `deferred_by` that `generate` writes. A `defer` of an Estimate names a page that stands: a check not yet created is put off through the rule or entity page it would check, as a take-back does, and `/pre-spec` reports a `defer` of an Estimate with no page; the agent fixes that finding with a new short Case with `{supersedes:case N}` whose `defer` names the page the Estimate would check, as for a wording the person corrects (case 783). ``
>   - change: `a defer of an Estimate names a page that stands; a check not yet created is put off through the page it would check, and a pre-spec finding on such a defer is fixed by a new short Case that supersedes it (case 783)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] `guppi/prespec.py`: `check_form` reports a `defer` item of an Estimate for which `materialize.has_page` is false, with the line `case N: defer <slug>: no such Estimate page — defer the page it would check`; the module docstring and the docstring of `check_form` name it (case 783).
> - [ ] `tests/test_prespec.py`: a `defer` of an Estimate with no page, under a Case heading and under `## Deferred`, gives the finding, and so does one whose file stands under `vault/archive/` in a folder other than `estimates/`, or under a `raw/` folder; a `defer` of an Estimate that stands live or in a folder `estimates/` under `vault/archive/`, and a `defer` of a rule with no page, give none.
> - [ ] update `estimate-prespec-checks-the-form-of-an-item`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a defer of an Estimate with no page is a finding`
> - [ ] read `estimate-prespec-checks-the-form-of-an-item`

> **ratification:**
> ```
> - decision[case 783.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 783.2][update][estimate-prespec-checks-the-form-of-an-item]{ref:rule-prespec}
> ```
