<!-- approved 23:55:16 · session 563a8403 -->

# Session 2104 — the sprint plugin: the Decision pages and the defers the librarian's run of 1712 left behind

## Case 865 — A defer never names a Lesson or a Decision page

> **context:**
> When a Case puts an item off, `guppi generate` adds the Decision page of that Case to the `deferred_by` field of the page that the `defer` line names, and `guppi backlog` lists each live page that has `deferred_by`, so the next session sees the item. The `defer` method of `.guppi/guppi/generate.py` writes `deferred_by` only on a page whose folder is in its constant `DEFERRABLE`: rules, entities, insights and estimates. On a Lesson or a Decision page it writes only a History line `deferred`, since neither page format lists `deferred_by`, so the item drops out of sight. Session 1712 shows it. Case 863 deferred `decision-case-855`, the run wrote the line `2026-10-16 deferred · [[decision-case-863]]` on that page, the same run archived the page, and `backlog.md` has no line for it (brief of the librarian of session 1712, Flags). `/pre-spec` and `generate` refuse a defer of a Lesson or a Decision page only when the page does not exist (case 786). The rule that governs the choice is `rule-backlog`, whose Purpose prevents a deferred item from dropping out of sight. The person chose to refuse such a defer at every step: at the reply that ratifies it, in both `Stop` hooks that act on it, at `/pre-spec` and at `generate`. The person then defers the rule or entity page whose change would settle the matter. So the Case has four parts, and each part rewrites or creates one check.
>
> Shared code. The functions each side calls today were read. `defer` of `.guppi/guppi/generate.py` asks `defer_writes_no_page` of `.guppi/guppi/materialize.py`, then `find`, then `DEFERRABLE`. `check_form` of `.guppi/guppi/prespec.py` asks `defer_writes_no_page` alone. `deferred_section` of `.guppi/guppi/ratified.py` judges a defer item by its keys and by the YAML of its block, not by the category of its target. `run` of `.guppi/guppi/ledger.py` passes every `defer` line by the kind of the line: `off_store` and `refused_without_sprint` leave a `defer` out. So no side judges a defer of a Lesson or a Decision page today, and no two sides answer differently on it, because none refuses it. Case 865.1 moves `DEFERRABLE` into `.guppi/guppi/materialize.py`. It adds there the predicate `defers_a_record`, which is true when the category of a slug, by `category_of`, is a vault folder of `CATEGORIES` outside `DEFERRABLE`. It also adds the message `DEFER_OF_A_RECORD`. `generate`, `prespec`, `ratified` and `ledger` import the three, so the judgment lives in one module, as `rule-one-judgment-one-implementation` sets it. A Grep for `DEFERRABLE` over `.guppi/` printed `.guppi/guppi/generate.py` alone. The data in the page formats is a second holder of the same fact: `deferred_by` stands in the `optional` list of `vault/wiki/{rules,entities,insights,estimates}/schema.yaml` and not in those of `lessons` and `decisions`. So Case 865.1 adds one test that compares `DEFERRABLE` with the live schema files.
>
> Pages. A Grep for `a Lesson or a Decision page` over the repository, with `vault/raw/` and `vault/archive/` left out, printed `.guppi/guppi/prespec.py`, `vault/wiki/orchestration.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-page-generation.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-prespec-checks-the-form-of-an-item.md` and `vault/wiki/estimates/estimate-generate-writes.md`. The hits in `rule-page-generation`, `rule-orchestration` and the two Estimates are the sentences of case 786, which speak of a page that does not stand; each part keeps them for an Insight and adds the refusal of a Lesson or a Decision page. The hits in `.guppi/guppi/prespec.py` are docstrings that Case 865.2 changes. `orchestration.md` changes at the render of `rule-orchestration`. `log.md` is a record. The `defer` field of `rule-decisions-schema` says that each target carries the page in `deferred_by`, and it becomes true for each new defer. Older pages stand: the defer of Case 863 on `decision-case-855` stays as the person left it when Case 864 was dropped. A Grep for `^- \S+ deferred` over `vault/wiki/lessons/` printed `lesson-case-build-agent-context-grows-on-every-resume.md` and `lesson-ledger-window-stops-at-a-resume-on-the-next-day.md`, both deferred by Case 836. This Case does not move them into the backlog, and this is left not done. In `rule-orchestration`, read whole, the take-back defers each rule, entity and insight page and each Estimate, and never a Lesson or a Decision page, so it stays true. The sentence of `## Writing the ledger lines` names the decision line that the ledger hook holds and none of its other refusals, such as a line with no sprint open, so it stands. The Criteria of `estimate-orchestration-defers-in-one-reply` and `estimate-orchestration-takes-back-a-ratified-case` speak of the reply and of rule, entity, insight and Estimate pages, so they stand. The Criterion of `estimate-ledger-write-lifts` already says that a line a refusal of `rule-ledger-write` refuses does not land, and `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` does not compare a `defer` line, so both stand. `estimate-generate-fails-alone` speaks of any entry that fails, so it stands. The Types row and the `deferred_by` row of `entity-glossary` say nothing of a defer of a Lesson or a Decision page, so they stand. The `purpose` and `method` of the three Estimates whose Criterion is replaced state no promise that changes, so they stand. Some lines of the old Criteria are rewritten, not dropped, and the check notes them as not carried: in `estimate-generate-writes` the `－` line of a defer with no page now names an Estimate and an Insight. In `estimate-prespec-checks-the-form-of-an-item` the line of an Insight, a Lesson or a Decision page with no page now names an Insight. The line on the judgment of both now names `defers_a_record` beside `defer_writes_no_page`. The `then` lines of the four parts share words on purpose. Each part sets what one piece of code does with the same defer: `guppi generate`, `/pre-spec`, the hook of `rule-spec-write` and the hook of `rule-ledger-write`. These are four promises, checked by four Estimates. A full Case that `case-guppi` builds is checked by `prespec.judge` through the check of its file and at its ratification by the check after the write of `rule-spec-write`, so the finding of Case 865.2 reaches it at both moments once the code lands.
>
> Tests that read live files. A Grep for `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `.guppi/tests/` printed `test_case_schema.py`, `test_guppi_package.py`, `test_orchestration.py`, `test_generate.py` and `test_schemas.py`. `test_orchestration.py` runs `ratified.write_defers` over the short-form example of `orchestration.md`, which defers `entity-booking-export`, an entity, which the new judgment passes. The new sentence of Case 865.3 adds no block. `test_case_schema.py` runs the check of `.guppi/guppi/casecheck.py` over `case-example.md`, which holds no `defer` item. `test_generate.py` and `test_schemas.py` read the live `schema.yaml` files, which no part changes. `test_guppi_package.py` reads `.claude/settings.json`, which no part changes.

> **problem:**
> A `defer` of a Lesson or a Decision page writes no `deferred_by`, so `backlog.md` never lists the item, and nothing in the session refuses such a defer.

> **recommend:**
> - **What should a defer of a Decision page or a Lesson do?**
>   - Recommended: (a) refuse it: `/pre-spec` reports it and `generate` fails the entry alone, whether the page exists or not, and the person defers the rule or entity page whose change would settle the matter.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) one part per piece of code, each with its own check text rewritten, both reading one shared function.
>   - Answer: agreed, (a).
> - **At which moments is such a defer refused?**
>   - Recommended: (a) also at ratification, in both hooks: the hook of `rule-spec-write` does not write the short defer, and the hook of `rule-ledger-write` does not write its line; `/pre-spec` and `generate` keep the check; four parts.
>   - Answer: (a).

### Case 865.1 — Generate refuses a defer of a Lesson or a Decision page

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, whose Purpose names the defers that fail as an entry.
> **＋** `.guppi/guppi/materialize.py`: `DEFERRABLE`, moved here, and the new `defers_a_record` and `DEFER_OF_A_RECORD`; its routing table names the defer.
> **＋** `.guppi/guppi/generate.py`: the `defer` of an entry and the module docstring.
> **＋** `.guppi/tests/test_generate.py`: the tests of `guppi generate`.
> **＋** `vault/wiki/<category>/schema.yaml`: the page formats whose `optional` list holds `deferred_by` or not.
> **＋** `vault/archive/`, outside its `raw/` folders: where an archived page stands.
> **＋** `estimate-generate-writes`: its Criterion is replaced whole.
> **＋** `estimate-generate-fails-alone`: the Estimate of an entry that fails alone.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/log.md` and `vault/wiki/tags.md`: the files `guppi generate` reads or appends to; the sprint comes from `vault/wiki/sprint.md`, or from `entity-sprint-<id>` when a unit creates it.

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
> **＋** The folders whose page takes `deferred_by` are `DEFERRABLE` of `.guppi/guppi/materialize.py`, which `.guppi/guppi/generate.py` imports; they are the folders whose `schema.yaml` under `vault/wiki/` lists `deferred_by`.
> **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
> **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
> **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
> **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
> **－** A `defer` of a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, whether its page stands or not, changes no page and appends nothing to `vault/wiki/log.md`: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it` on stderr.
> **－** A `defer` of an Estimate or an Insight whose page stands neither under `vault/wiki/<category>/` nor in a folder `<category>` under `vault/archive/` outside a `raw/` folder, by `defer_writes_no_page` of `.guppi/guppi/materialize.py`, which asks `has_page`, writes no page: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: an Estimate is deferred only with its page — defer the page it would check` on stderr for an Estimate, and `generate: <slug>: a placeholder is written only for a rule or an entity — defer a page that stands` for an Insight.
> **－** No body section is derived from a ref field; a section the entry does not name under `sections` or reach by `replace` is not touched.
> **－** An `update` of an Estimate whose `set` carries `method` drops no section.
> **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

```then
update:
- slug: rule-page-generation
  replace:
  - old: an Insight is made only by the librarian, and the format of an Insight, a Lesson or a Decision page has no status for a stand-in page (case 786).
    new: an Insight is made only by the librarian, and the format of an Insight, a Lesson or a Decision page has no status for a stand-in page (case 786). A `defer` of a Lesson or a Decision page writes nothing and fails as an entry too, whether the page stands or not, since neither format has `deferred_by` and no list would show the item (as set in case 865).
  change: a defer of a Lesson or a Decision page fails as an entry, whether the page stands or not (case 865)
- slug: estimate-generate-writes
  set:
    status: pending
  change: the Criterion replaced whole — a defer of a Lesson or a Decision page fails alone, whether the page stands or not
```

```tasks
- [x] update `rule-page-generation`
- [x] `.guppi/guppi/materialize.py`: `DEFERRABLE`, the folders `rules`, `entities`, `insights` and `estimates`, moved here from `.guppi/guppi/generate.py`; a predicate `defers_a_record(slug)`, true when `category_of(slug)` is a folder of `CATEGORIES` outside `DEFERRABLE`; a constant `DEFER_OF_A_RECORD`, the text `a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it`; the docstring of the predicate names `.guppi/guppi/generate.py`, `.guppi/guppi/prespec.py`, `.guppi/guppi/ratified.py` and `.guppi/guppi/ledger.py` as the modules that import it; the line `defer existing` of the routing table says that a Lesson or a Decision page is refused (case 865).
- [x] `.guppi/guppi/generate.py`: imports `DEFERRABLE`, `defers_a_record` and `DEFER_OF_A_RECORD` from `.guppi/guppi/materialize.py` in place of its own constant; in `defer`, an entry for which `defers_a_record` is true fails first, before `defer_writes_no_page` and before any page is read, with `DEFER_OF_A_RECORD`, and no page or `log.md` line is written; the module docstring and the docstring of `defer` say so (case 865).
- [x] `.guppi/tests/test_generate.py`: a `defer` of a live Decision page, of a Decision page under `vault/archive/`, of a live Lesson and of a Decision page with no page each changes no page, prints `generate: <slug>: ` and `DEFER_OF_A_RECORD` on stderr, exits 1 and lets the other entries apply; a `defer` of a rule, an entity, an Insight and an Estimate that stand still appends to `deferred_by`; `generate.defers_a_record` is `materialize.defers_a_record` and `generate.DEFERRABLE` is `materialize.DEFERRABLE`; for each folder of `CATEGORIES`, the live `vault/wiki/<folder>/schema.yaml` lists `deferred_by` among its optional properties exactly when the folder is in `DEFERRABLE`.
- [x] update `estimate-generate-writes`
- [x] read `estimate-generate-writes`
```

### Case 865.2 — Pre-spec reports a defer of a Lesson or a Decision page

> **given:**
> `rule-prespec`: the rule of `/pre-spec`, the target of the Estimate.
> **＋** `.guppi/guppi/prespec.py`: `check_form`, the check of the form of an item, and the module docstring.
> **＋** `.guppi/guppi/materialize.py`: `defers_a_record`, `DEFER_OF_A_RECORD` and `defer_writes_no_page`, the shared judgments.
> **＋** `.guppi/guppi/generate.py`: the `defer` that fails such an entry by the same judgment, by Case 865.1.
> **＋** `.guppi/tests/test_prespec.py`: the tests of the check.
> **＋** `vault/wiki/<category>/`, and a folder `<category>` under `vault/archive/` outside its `raw/` folders: where the page of a slug stands.
> **＋** `vault/wiki/estimates/`, and a folder `estimates/` under `vault/archive/`: where the page of an Estimate stands.
> **＋** `vault/wiki/insights/`, and a folder `insights/` under `vault/archive/`: where the page of an Insight stands.
> **＋** `estimate-prespec-checks-the-form-of-an-item`: its Criterion is replaced whole.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

> **then:**
> A Case whose `then` block holds two or more Estimate items that set a new Criterion — a `create`, or an `update` that names no part of the page by `names_a_part` of `.guppi/guppi/materialize.py` — is the finding `case N: two promises in one Case — split it`, whether each item writes its Criterion under `sections` or lifts it.
> **＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
> **＋** A `defer` of a Lesson or a Decision page, whether its page stands or not, is the finding `case N: defer <slug>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it`, a short Case under `## Deferred` of the plan included.
> **＋** A `defer` of an Estimate whose page stands neither under `vault/wiki/estimates/` nor in a folder `estimates/` under `vault/archive/` outside a `raw/` folder is the finding `case N: defer <slug>: no such Estimate page — defer the page it would check`, a short Case under `## Deferred` of the plan included.
> **＋** A `defer` of an Insight whose page stands neither under `vault/wiki/insights/` nor in a folder `insights/` under `vault/archive/` outside a `raw/` folder is the finding `case N: defer <slug>: no such page — a placeholder is written only for a rule or an entity`, a short Case under `## Deferred` of the plan included.
> **＋** The judgment of a Lesson or a Decision page is `defers_a_record` of `.guppi/guppi/materialize.py`, and the judgment of a page that does not stand is `defer_writes_no_page` of the same module, which asks `has_page`; the `defer` of `.guppi/guppi/generate.py` imports both.
> **＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
> **＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.
> **＋** A key of an item of any kind that `item_keys` of `.guppi/guppi/materialize.py` does not give its kind and category — `slug` a key of every kind — is the finding `case N: <kind> <slug>: key <key> is not a key of this item`.
> **－** An `update` of an Estimate that names a part alone — `set` without `status`, a `replace` pair, a section other than `Criterion` — is not counted.
> **－** A `defer` of a Lesson or a Decision page with no page gives the finding of a Lesson or a Decision page alone, not the finding of a page that does not stand.
> **－** A `defer` of a rule or an entity with no page is not a finding.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session creates or updates, is not judged by its keys (case 308.2).

```then
update:
- slug: estimate-prespec-checks-the-form-of-an-item
  set:
    status: pending
  change: the Criterion replaced whole — a defer of a Lesson or a Decision page is a finding, whether the page stands or not
```

```tasks
- [x] `.guppi/guppi/prespec.py`: `check_form` judges each `defer` item whose slug has a category by `materialize.defers_a_record` first, imported, and reports `case N: defer <slug>: ` and `materialize.DEFER_OF_A_RECORD`; only an item it does not report goes on to `defer_writes_no_page`; the module docstring and the docstring of `check_form` say that a `defer` of a Lesson or a Decision page is a finding whether its page stands or not, and that the finding of a page that does not stand covers an Estimate and an Insight (case 865).
- [x] `.guppi/tests/test_prespec.py`: a `defer` of a live Decision page, of a Decision page under `vault/archive/` and of a live Lesson, under a Case heading and under `## Deferred`, each gives the new finding; a `defer` of a Lesson with no page gives the new finding alone; a `defer` of an Insight with no page still gives `NO_DEFERRED_PAGE`; a `defer` of a rule, an entity, an Insight and an Estimate that stand gives none; `prespec.defers_a_record` is `materialize.defers_a_record`.
- [x] update `estimate-prespec-checks-the-form-of-an-item`
- [x] read `estimate-prespec-checks-the-form-of-an-item`
```

### Case 865.3 — The plan hook refuses a short defer of a Lesson or a Decision page

> **given:**
> `rule-spec-write`: the rule of the `Stop` hook that writes a short defer under `## Deferred`.
> **＋** `rule-orchestration`: the rule rendered into `vault/wiki/orchestration.md`, which sets the short Case of a deferred decision.
> **＋** `.guppi/guppi/ratified.py`: `deferred_section`, the check of a short defer, and the module docstring.
> **＋** `.guppi/guppi/materialize.py`: `defers_a_record` and `DEFER_OF_A_RECORD`, the shared judgment, by Case 865.1.
> **＋** `.guppi/tests/test_ratified.py`: the tests of the hook.
> **＋** `.guppi/tests/test_orchestration.py`: the test that runs the hook over the short-form example of `vault/wiki/orchestration.md`.
> **＋** `estimate-spec-write-writes-a-defer`: its Criterion is replaced whole.
> **＋** `estimate-spec-write-answers-a-refusal` and `estimate-spec-write-tells-each-reason-once`: the Estimates of a reply after a refusal and of a reason told once.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

> **then:**
> The hook writes that Case under `## Deferred` of the plan file while `spec.md` in the session's folder does not stand, and of that `spec.md` once it stands: the heading, `context`, `problem` and the `then` block as the reply shows them.
> **＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
> **＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr.
> **＋** A `defer` line of Case N whose slug names a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, whether its page stands or not: exit 2 with `case N: defer <slug>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it` on stderr, and nothing of the Case is written.
> **＋** A key of a `defer` item that `item_keys` of `.guppi/guppi/materialize.py` does not give a `defer` of its category: exit 2 with `` `<key>`: not a key of defer <slug> `` on stderr, and nothing of the Case is written.
> **＋** A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — as the function of `.guppi/guppi/materialize.py` judges it: exit 2 with the line of the comment and the advice to quote the value on stderr, and nothing of the Case is written.
> **＋** With `stop_hook_active` set, the hook writes and refuses as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a reason it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
> **－** A `defer` line of a rule, an entity, an Insight or an Estimate is not refused by `defers_a_record`.
> **－** A `#` inside a quoted value or inside a `|` or `>` block is text, not a comment, and is no refusal.
> **－** A `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
> **－** The check after the write does not run on the Case.

```then
update:
- slug: rule-spec-write
  replace:
  - old: a key of a `defer` item that `item_keys` of `.guppi/guppi/materialize.py` does not give a `defer` of its category is refused, exit 2, and nothing of the Case is written (case 436.3);
    new: a key of a `defer` item that `item_keys` of `.guppi/guppi/materialize.py` does not give a `defer` of its category is refused, exit 2, and nothing of the Case is written (case 436.3); so is a `defer` line of the Case whose slug names a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, since neither page carries `deferred_by` and no list would show the item (as set in case 865);
  change: the hook refuses a short defer of a Lesson or a Decision page (case 865)
- slug: rule-orchestration
  replace:
  - old: A `defer` of an Insight, a Lesson or a Decision page names a page that stands too, since only a rule or an entity gets a placeholder page, and `/pre-spec` reports one with no page; the agent fixes that finding the same way, with a new short Case with `{supersedes:case N}` whose `defer` names a page that stands (case 786).
    new: 'A `defer` of an Insight names a page that stands too, since only a rule or an entity gets a placeholder page, and `/pre-spec` reports one with no page; the agent fixes that finding the same way, with a new short Case with `{supersedes:case N}` whose `defer` names a page that stands (case 786). A `defer` never names a Lesson or a Decision page, since neither carries `deferred_by` and no list would show the item: the `Stop` hooks of `rule-spec-write` and `rule-ledger-write` refuse such a short Case and its line at the reply that carries them, `/pre-spec` reports it and `guppi generate` fails it, and the agent writes the defer again on the rule or entity page whose change would settle the matter (as set in case 865).'
  change: a defer never names a Lesson or a Decision page; the hooks refuse it at the reply that carries it (case 865)
- slug: estimate-spec-write-writes-a-defer
  set:
    status: pending
  change: the Criterion replaced whole — a short defer of a Lesson or a Decision page is refused and not written
```

```tasks
- [x] update `rule-spec-write`
- [x] update `rule-orchestration`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [x] `.guppi/guppi/ratified.py`: `deferred_section` refuses Case N when a `defer` line of the reply of Case N has a slug for which `materialize.defers_a_record`, imported, is true, before it reads the `then` block, with `case N: defer <slug>: ` and `materialize.DEFER_OF_A_RECORD`, and writes nothing of the Case; the paragraph `The defer` of the module docstring says so (case 865).
- [x] `.guppi/tests/test_ratified.py`: a reply with a short defer of a live Decision page, and one of a Lesson with no page, gets the error and leaves the plan file unchanged; a short defer of an entity in the same reply as a refused one is still written; `ratified.defers_a_record` is `materialize.defers_a_record`.
- [x] `uv run --project .guppi pytest .guppi/tests/test_orchestration.py`: the short-form example of `vault/wiki/orchestration.md` still passes the hook.
- [x] update `estimate-spec-write-writes-a-defer`
- [x] read `estimate-spec-write-writes-a-defer`
```

### Case 865.4 — The ledger hook refuses a defer line of a Lesson or a Decision page

> **given:**
> `rule-ledger-write`: the rule of the `Stop` hook that writes the ledger lines.
> **＋** `estimate-ledger-write-refuses-a-defer-of-a-record`: the new check of the refusal.
> **＋** `.guppi/guppi/ledger.py`: `run`, the new `refused_defers`, and the module docstring.
> **＋** `.guppi/guppi/materialize.py`: `defers_a_record`, `DEFER_OF_A_RECORD` and `parse_line`, the shared judgment and the one parse of a ledger line.
> **＋** `.guppi/guppi/ratified.py`: `write_defers`, which refuses the same short defer by Case 865.3.
> **＋** `rule-spec-write`: the rule of the `Stop` hook that writes the short Case of the same line.
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the hook.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds, in a `LEDGER` block of a session with a `hi`, a `defer` decision line that no ledger holds yet.

> **then:**
> A `defer` line whose slug names a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, whether its page stands or not, does not land in `raw/<hi date>/<hi HHMM>/ledger.md`, whatever text of the transcript holds it.
> **＋** When the line stands in the reply just finished, the hook prints `ledger: line not written — <line>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it` on stderr, once a stretch, and exits 2.
> **＋** The other lines of the same block land as without it.
> **＋** The hook of `rule-spec-write` refuses the short Case of the same line by the same judgment, so neither the plan nor the ledger holds it.
> **－** A `defer` line of a rule, an entity, an Insight or an Estimate is not refused by `defers_a_record`.
> **－** A refused line of an earlier text of the transcript prints no stderr line.

```then
create:
- slug: estimate-ledger-write-refuses-a-defer-of-a-record
  ref: rule-ledger-write
  kind: QA
  purpose: Whether the ledger hook refuses a defer line of a Lesson or a Decision page, so that no defer lands where no list shows it
  method: uv run --project .guppi pytest .guppi/tests/test_ledger.py -k record
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: so a record with a broken opening is not lost unseen (case 695.1).
    new: so a record with a broken opening is not lost unseen (case 695.1). It refuses a `defer` decision line whose slug names a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, in any text of the transcript, with one stderr line when the line stands in the reply just finished, which asks for a defer of the rule or entity page whose change settles the matter, since neither page carries `deferred_by` and no list would show the item (as set in case 865).
  change: the hook refuses a defer line of a Lesson or a Decision page (case 865)
```

```tasks
- [x] create `estimate-ledger-write-refuses-a-defer-of-a-record`
- [x] update `rule-ledger-write`
- [x] `.guppi/guppi/ledger.py`: a function `refused_defers(fresh)`, the fresh decision lines of kind `defer`, read by `materialize.parse_line`, whose slug `materialize.defers_a_record` judges true, both imported inside the function; `run` leaves them out of the lines it writes and prints `ledger: line not written — <body>: ` and `materialize.DEFER_OF_A_RECORD` for each that stands in the reply just finished, told once a stretch by `untold`; the module docstring says so (case 865).
- [x] `.guppi/tests/test_ledger.py`: a reply whose block holds a `defer` line of a live Decision page, of a Lesson with no page and of a rule writes the line of the rule alone, prints the refusal for the two others and exits 2; the same lines in an earlier text land neither, with no stderr line; one test runs `ledger.refused_defers` and `ratified.write_defers` over the same short defer of a Decision page, and over one of a rule, and asserts that both refuse the first and pass the second.
- [x] read `estimate-ledger-write-refuses-a-defer-of-a-record`
```

## Case 866 — The close command names the Bash tool

> **context:**
> At the end of its run the librarian commits by the command that the Render of `rule-close` writes into `.claude/agents/librarian-guppi.md`: `git add vault $(uv run --project .guppi guppi render --paths) && git commit -m "docs(vault): librarian, <date>"` (case 857). The handoff of session 1712 reports, and the brief carries as a defect, that Windows PowerShell 5.1 does not parse the `&&` of that command. The Render of `rule-documentation` gives the librarian the tools `Read, Grep, Glob, Bash, Edit, Write`, so the librarian has no PowerShell tool and runs the command with the Bash tool, where `&&` and `$(...)` parse; the brief of session 1712 says its close commit was run with the Bash tool. The Render of `rule-spec-box` tells the main agent not to commit after the librarian's run, so no other agent runs this command. The defect does not reach the librarian as it stands; the Render does not say which shell the command is written for. The person chose to name the Bash tool in the Render and to leave the command as it is. Splitting the command in two was turned down: the claim that its `$(...)` runs alike in Windows PowerShell 5.1 was never checked.
>
> The new words hold in any project that installs GUPPI, since every Claude Code project has the Bash tool; `rule-close` has `core: true`, and the new text holds no pointer to a case, so it needs no bracket for `guppi ship`. The Purpose of `rule-close` speaks of a separate commit and names no shell, so it stands. `estimate-close-commits` checks the change, and its Criterion stands, as the person chose: its `When` reads that the librarian commits as `.claude/agents/librarian-guppi.md` says, and its `Then` lines read the commit in `git log`, so a command that does not parse shows as no commit; its `purpose` and `method` name no shell. Its reading is already due after this session's librarian run; that run loads its agent file before it renders, so it commits by the Render of Case 857, and the new words change nothing the librarian does. A Grep for `rule-close` over the repository outside `vault/raw/` and `vault/archive/` printed nine files: `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-close.md`, `vault/wiki/rules/rule-documentation.md`, `vault/wiki/rules/rule-session.md`, `vault/wiki/estimates/estimate-close-commits.md`, `vault/wiki/estimates/estimate-brief-carries-the-run-facts.md`, `.claude/agents/librarian-guppi.md` and `.guppi/guppi/render.py`. The hits in `rule-session`, `rule-documentation` (the place of the splice), `estimate-brief-carries-the-run-facts` and `render.py` name the close commit and no shell, so they stand; the agent file follows the render. A Grep for `librarian-guppi|rule-close|git add vault` over `.guppi/tests/` printed `test_grepguard.py`, which uses the name as an agent type and does not read the file.

> **problem:**
> The close command of the librarian is written for a POSIX shell, and its Render does not say so, so a reader may take it for a command that runs in Windows PowerShell 5.1, which does not parse its `&&`.

> **recommend:**
> - **What should this Case do with the close command?**
>   - Recommended: (a) name the Bash tool in the Render and keep the command as it is.
>   - Answer: agreed, (a).
> - **How is this change checked?**
>   - Recommended: (a) use `estimate-close-commits` as it stands; no Estimate is created or changed.
>   - Answer: agreed, (a).

> **given:**
> `rule-close`: its Render sets the close command of the librarian.
> **＋** `.claude/agents/librarian-guppi.md`: the agent file that the render writes from that Render.
> **＋** `rule-documentation`: its Render gives the librarian its tools.
> **＋** `estimate-close-commits`: checks the close commit; its Criterion stands.

> **when:**
> The librarian reaches the close step of `.claude/agents/librarian-guppi.md`.

> **then:**
> The librarian runs the close command with the Bash tool.
> **＋** The close command stays one line, `git add` and `git commit` joined by `&&`.
> **－** The librarian does not run the close command in PowerShell.

```then
update:
- slug: rule-close
  replace:
  - old: 'Commit the vault with the files the render wrote:'
    new: 'Commit the vault with the files the render wrote, by the Bash tool, since the command is written for a POSIX shell:'
  change: the close command is run by the Bash tool
```

```tasks
- [x] update `rule-close`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
```

## Case 867 — The check of the page schemas names its test files

> **context:**
> `estimate-page-schemas-one-file-per-rule` checks `rule-page-schemas`, a MOC over the six rules of the page formats. For the Estimate of a MOC, `check_method` of `.guppi/guppi/lint.py` passes a `make <target>` of the Makefile, or the word `pytest` with test files that each exist; `by hand` alone passes only when every counted Estimate of the children is a reading or a sibling Estimate names such a form. The `method` of this Estimate names `guppi check`, a test path without `pytest`, and a reading by hand after the librarian's first render. Five of the six child Estimates name `.guppi/tests/test_schemas.py` and no `by hand`, so lint gives a finding. The brief of the librarian of session 1712 reports it under `## Readings at the close`: "`estimate-page-schemas-one-file-per-rule` (says by hand while `estimate-entities-schema-checked` names a test file)", and the same run printed 11 lines of `guppi check` at exit 1. Case 829 deferred the Estimate for this finding. Case 861 superseded Case 829 but named only `estimate-guppi-tests-green`, so `guppi generate` kept `decision-case-829` in the `deferred_by` of this page, and the librarian's run of 1712 archived `decision-case-829`. `backlog.md` still lists the item.
>
> The rule that governs the choice is the `method` field of `rule-estimates-schema`. It says that the form of a MOC's Estimate is "a `make <target>` of the Makefile, or the word `pytest` with the test files of its pipeline, each of which must exist". The new `method` names `pytest` with four test files: `.guppi/tests/test_schemas.py` for the six children, `.guppi/tests/test_render.py` for two `full` pages on one file, `.guppi/tests/test_lint.py` for the findings of the classes `path` and `schema-description`, and `.guppi/tests/test_guard.py` for the refused hand edit. All four files exist. The `guppi check` part stays, and the reading by hand goes, since the reading after the first render passed on 2026-09-29. A `make` target was not chosen. `rule-rules-schema` brings a page with `core: true` into a new project with each of its Estimates "whose `method` names no target of the `Makefile`", and `rule-page-schemas` has `core: true`. `/pre-spec` judges the new `method` by `names_a_moc_form`, `tied_to_a_one_off_moment` and `waits_for_another_session` of `.guppi/guppi/lint.py`. It passes all three: it names `pytest` with test paths, holds no `by hand`, and names no later session, librarian or `/hi`. The Case adds no code, so no second copy of a judgment is written.
>
> The decision line carries `{supersedes:case 829}`. `decision` of `.guppi/guppi/generate.py` finds `decision-case-829` under `vault/archive/` by `find`, keeps it `archived`, adds this Case to its `superseded_by`, and `clear_deferred_by` drops it from the `deferred_by` of each target that a decision line of this Case names. This Case names only this page, so `estimate-guppi-tests-green`, which Case 861 already cleared, is not touched.
>
> Frontier item C2 asks whether a MOC with no parent may name `guppi test` alone. `rule-page-schemas` has the parent `rule-harness`, and the finding here comes from the branch of `check_method` for `by hand`, not from `names_a_moc_form`, so C2 does not reach this Case. The promise, `status` and Result of the Estimate do not change. `estimate-lint-checks-the-method` already checks the judgment of lint on this form: "For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it, and so does the word `pytest` with one or more test files, each of which exists." Its Criterion stands, because the Case changes no code of lint. A Grep for `estimate-page-schemas-one-file-per-rule` over the repository, with `vault/raw/` and `vault/archive/` left out, printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-page-schemas.md`. The brief and the log are records. `backlog.md` is written by `guppi backlog`. `rule-page-schemas` lists the slug only in `estimates`. A Grep for `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `.guppi/tests/` printed `test_case_schema.py`, `test_generate.py`, `test_schemas.py`, `test_orchestration.py` and `test_guppi_package.py`. None of them reads an Estimate page.

> **problem:**
> The `method` of `estimate-page-schemas-one-file-per-rule` has no form that lint accepts on the Estimate of a MOC. Its defer points at an archived Decision page, so the item stays in the backlog.

> **recommend:**
> - **What should the `method` of `estimate-page-schemas-one-file-per-rule` say?**
>   - Recommended: (a) `pytest` over the four test files that cover the promise, then `guppi check`.
>   - Answer: agreed, (a).
> - **How is the fix checked?**
>   - Recommended: (a) the existing check covers it: `estimate-lint-checks-the-method`, whose Criterion stands.
>   - Answer: agreed, (a).

> **given:**
> `estimate-page-schemas-one-file-per-rule`: the Estimate whose `method` changes.
> **＋** `rule-page-schemas`: the MOC it checks.
> **＋** `rule-estimates-schema`: the rule of the `method` of a MOC's Estimate.
> **＋** `.guppi/guppi/lint.py`: `check_method`, which judges the `method`.
> **＋** `.guppi/tests/test_schemas.py`, `.guppi/tests/test_render.py`, `.guppi/tests/test_lint.py` and `.guppi/tests/test_guard.py`: the test files the new `method` names.
> **＋** `decision-case-829`: the archived Decision page whose defer the Case retires.
> **＋** `vault/wiki/backlog.md`: the list of deferred items.

> **when:**
> `uv run --project .guppi guppi lint` reads the `method` of `estimate-page-schemas-one-file-per-rule`.
> **＋** `guppi backlog` writes `vault/wiki/backlog.md` after `guppi generate` applies the decision line of this Case.

> **then:**
> Lint gives no finding of the class `method` on `estimate-page-schemas-one-file-per-rule`.
> **＋** Its `method` names `pytest` with `.guppi/tests/test_schemas.py`, `.guppi/tests/test_render.py`, `.guppi/tests/test_lint.py` and `.guppi/tests/test_guard.py`, then `guppi check`.
> **＋** Its `deferred_by` no longer names `decision-case-829`, and `vault/wiki/backlog.md` does not list it.
> **－** Its `method` holds no reading by hand.
> **－** Its Criterion, `status` and Result do not change.

```then
update:
- slug: estimate-page-schemas-one-file-per-rule
  set:
    method: uv run --project .guppi pytest .guppi/tests/test_schemas.py .guppi/tests/test_render.py .guppi/tests/test_lint.py .guppi/tests/test_guard.py; uv run --project .guppi guppi check — render --check exit 0 and no path or schema-description finding on a <category>/schema
  change: the method names pytest with the test files of the MOC; the reading by hand after the first render is gone
```

```tasks
- [x] update `estimate-page-schemas-one-file-per-rule`
- [x] `uv run --project .guppi pytest .guppi/tests/test_schemas.py .guppi/tests/test_render.py .guppi/tests/test_lint.py .guppi/tests/test_guard.py`: the four files of the new `method` pass.
```

## Case 868 — A test over a live file passes on the old text and the new

> **context:**
> A Case can change code that reads a text and, in the same session, the text itself: a page, or a file rendered from a page. The code runs from the working tree as soon as Work Mode edits it. The page changes at the librarian's run, and the rendered file at the render after it. So the new code reads the old text in between. `insight-workflow-code-live-before-the-page-it-reads` collects the lessons of this pattern. Most of its forms are now covered. `rule-retro` and `rule-work-mode` turn the red of a check such as `uv run --project .guppi guppi check`, listed under `## Expected red` of `work.md`, into a note for the handoff (cases 473.1, 479.3). `rule-case-build` makes a reader that would lose what it refuses keep the old form (case 473.2), and makes `case-guppi` judge each task by the state of the code and the pages when it runs (case 797.1). That covers the lessons of the reading moment, of the preview and of the key another Case adds. One form stays open: `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian`. In session 1739 Case 819.1 changed `.guppi/tests/test_guppi_package.py`, which reads the files of `.claude/` and the live pages. Its tests were red at Retro, waiting for the render, and the commit went in with them red. Two texts disagree on such a test. `rule-case-build` says that a reader that only goes red keeps no old form and that its red is a note for the handoff. `rule-retro` says that a red test is never an expected red and is fixed or reverted, and that the commit needs green. The workflow `.github/workflows/checks.yml` also runs `uv run --project .guppi guppi test`. The person chose to action the Insight: such a test passes on the old text and on the new one until the text lands, and a Case of a later session removes the old text.
>
> The rule that governs the choice is `rule-retro`, whose sentence on red tests stands: under this Case no task leaves a test red until the librarian's run. The option of an expected red test would have broken it. The last test run was read in the brief, under Readings at the close: `uv run --project .guppi guppi test`: 1722 passed, 6 skipped, 1 deselected (exit 0).
>
> In `rule-case-build`, read whole, three sentences state the behaviour. The sentence of case 754 puts each place where the new text would fail a test into the Case as a task that changes the test or the text. It stays true, and the new sentence sets how that task writes the test. The sentence of case 473.2 on a reader that loses what it refuses stays true. The sentence on a reader that only goes red would cover a test, and so it gains the sentence that excludes a test. The sentence of case 797.1 on the moment of a check stays true. The Criterion of `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` holds that `－` line, so this Case replaces the Criterion whole and sets its `purpose` and `method` anew, since both name only the reader. The Criterion of `estimate-case-build-reads-the-test-code-over-a-changed-text` promises the reading of the test code and that each failing place enters the Case as a task. How that task writes the test is the replaced Criterion, so that Criterion stands. The Criterion of `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check` (case 736.1) promises that each text of a live file that a changed check would refuse enters the Case. When the Case changes that text, a test that runs the new check over the live file is red on the old text until the text lands. So the new sentence and the replaced Criterion also cover a test that fails because the Case changes the code of a check it runs. That Criterion says nothing of how the test is written, so it stands (/pre-spec, ask-guppi). Two lines of the old Criterion are rewritten, not dropped, and the check notes them as not carried. The `When` line now also names a test and the live file it reads. The line on the removal of the old form now also names the old text in the test. The new `method` waits for the first Case built under the new Render, so the Retro of this session leaves the Estimate `pending`.
>
> A Grep for `only goes red|red test is never|note for the handoff` over `vault/wiki/`, `.claude/` and `.guppi/` printed these files:
> `.claude/skills/work/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/agents/case-guppi.md`, `vault/wiki/log.md`, `vault/wiki/lessons/lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/insights/insight-workflow-code-live-before-the-page-it-reads.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/rules/rule-handoff.md`, `vault/wiki/estimates/estimate-clean-branch-code-holds-pointers-only-in-brackets.md`, `vault/wiki/rules/rule-work-mode.md`, `vault/wiki/estimates/estimate-retro-red-check-of-an-updated-page-is-a-handoff-note.md`, `vault/wiki/estimates/estimate-case-build-keeps-the-old-form-until-the-writer-is-live.md` and `.guppi/tests/test_guppi_package.py`.
> The two skills, `rule-retro`, `rule-work-mode` and `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` speak of the red of a check, and `rule-retro`, its skill and that Estimate add that a red test is never an expected red. The new rule agrees with both, so they stand. `estimate-clean-branch-code-holds-pointers-only-in-brackets` speaks of the red of `uv run --project .guppi guppi check`, so it stands. The hit in `rule-handoff` is a History line, and `log.md` is a record. The lesson and the Insight are records that this Case closes. The docstring of `.guppi/tests/test_guppi_package.py` says that the red of its tests before the render is a note for the handoff, which the new rule makes false, so a task rewords it.
>
> Tests that read live files. A Grep for `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `.guppi/tests/` printed `test_case_schema.py`, `test_guppi_package.py`, `test_generate.py`, `test_orchestration.py` and `test_schemas.py`. Only `test_guppi_package.py` reads a file this Case changes. It reads every file under `.claude/`, `.claude/agents/case-guppi.md` included, and the live rule and Estimate pages, and fails on `uv run guppi`, `uv run pytest`, or `guppi/` and `tests/` where a `reword` would change them. The new texts name only `.guppi/tests/`, the form the live pages already hold while that test passes, so they stand.
>
> The Insight leaves the backlog by an `update` to `actioned` with `addressed_by: decision-case-868`, as its schema sets it (case 712). It has no `deferred_by`, so no `{supersedes:...}` mark is needed. Its `clustered` children go to the archive by the cascade of `generate`. Case 865 of this session changes hooks and the text they read. It is not exposed to this pattern: its hooks refuse only a new kind of `defer`, so nothing they accept today is lost, and its context says that `test_orchestration.py` still passes on the rendered `orchestration.md`. It does not change `rule-case-build`. When this Case was built, no case file of Cases 869 to 872 of the same batch stood.

> **problem:**
> A Case may change a test that reads a live file which the same session changes. The test is red from Work Mode until the librarian's run, while `rule-retro` lets no red test stand. `rule-case-build` still calls that red a note for the handoff.

> **recommend:**
> - **What should happen to this Insight?**
>   - Recommended: (a) action it: a test that reads a live file which the same session changes accepts both the old and the new text until the text lands, and a Case of a later session removes the old form.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`: its Criterion, `purpose` and `method` are replaced.
> **＋** `.guppi/tests/`: the tests, some of which read a live file of `vault/` or `.claude/`.
> **＋** `.guppi/tests/test_guppi_package.py`: a test over live files, whose docstring names its red before the render.
> **＋** `rule-retro`: the rule that lets no red test stand and makes the red of a check a note for the handoff.
> **＋** `estimate-case-build-reads-the-test-code-over-a-changed-text`: the Estimate of the reading of a test over a changed text, which stands.
> **＋** `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`: the Estimate of the reading of a live file that a test runs through a changed check, which stands.
> **＋** `insight-workflow-code-live-before-the-page-it-reads`: the Insight this Case actions.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes a reader in code and the text or the writer that reader reads, or a test of `.guppi/tests/` or the code of a check that test runs, and a live file of `vault/` or `.claude/` that the test reads, where the code and the test run from the working tree at once and the text lands at the librarian's run or the render.

> **then:**
> Where the reader refuses in between and what it refuses is lost, such as a hook that refuses a ledger line, the `then` of the Case says that the reader accepts the old form beside the new one until a reading of the writer passes live.
> **＋** Where the test would fail on the text of the file before the change or after it, whether the Case changes the test, the code of a check the test runs or the file, a task of the Case makes the test pass on the text before the change and on the text after it, until the text lands.
> **＋** The removal of the old form from the reader, after that reading, and of the old text from the test, after the text lands, is left to a Case of a later session.
> **－** A reader that only goes red, such as `uv run --project .guppi guppi check`, keeps no old form: its red is a note for the handoff by `rule-retro`.
> **－** A test of `.guppi/tests/` is no such reader: by `rule-retro` a red test is never an expected red, so no task leaves the test red until the librarian's run.

```then
update:
- slug: rule-case-build
  replace:
  - old: 'A reader that only goes red, such as `uv run --project .guppi guppi check`, keeps no old form: its red is a note for the handoff by `rule-retro`.'
    new: 'A reader that only goes red, such as `uv run --project .guppi guppi check`, keeps no old form: its red is a note for the handoff by `rule-retro`. A test of `.guppi/tests/` that reads a live file of `vault/` or `.claude/` is no such reader, since `rule-retro` lets no red test stand: where the Case changes that test, the code of a check that test runs, or the file by a page `update` or by the render of its rule, and the test would fail on the text of the file before the change or after it, a task of the Case makes the test pass on the text before the change and on the text after it until the text lands, and a Case of a later session removes the old text from the test (as set in case 868).'
  change: a test over a live file that the same session changes passes on the old text and the new until the text lands; its red is no note for the handoff (case 868)
- slug: estimate-case-build-keeps-the-old-form-until-the-writer-is-live
  set:
    status: pending
    purpose: Whether a Case that changes a reader and the text it reads, where the reader loses what it refuses before the text lands, keeps the old form in its then until the writer is measured live, and whether a Case that changes a test over a live file, or the code of a check it runs, while the same session changes that file, makes the test pass on the old text and the new until the text lands
    method: 'by hand, after the first Case case-guppi builds under the Render of rule-case-build that names a test over a live file, which changes a reader in code and the text or the writer it reads, or a test of .guppi/tests/ or the code of a check it runs, and a live file the test reads: the then and tasks of that Case read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — a test over a live file that the same session changes passes on the old text and the new until the text lands
- slug: insight-workflow-code-live-before-the-page-it-reads
  set:
    status: actioned
    addressed_by: decision-case-868
  change: 'actioned: a test over a live file that the same session changes passes on the old text and the new until the text lands, in rule-case-build (case 868)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] update `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
- [ ] read `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
- [x] `.guppi/tests/test_guppi_package.py`: the paragraph of the module docstring that says the tests over `.claude/` and the pages are red until the librarian's run and that this red is a note for the handoff now says that these tests were red then (case 819.1), and that a test like these now passes on the text before the change and on the text after it until the text lands, as `rule-case-build` sets it (case 868).
- [x] update `insight-workflow-code-live-before-the-page-it-reads`
```

## Case 869 — case-guppi reads the function that decides a claim it states about code

> **context:**
> `case-guppi` sometimes says what a function or a script of the repository does, prints or leaves out without reading the function that decides it, and a Case or a recommendation rests on that claim. The claim then proves false after the person signed it, and the Case is built again. `insight-case-build-claims-what-code-does-without-reading-it` clusters three lessons of this cause, and they record these slips. In Case 807 the agent said that the run of `guppi ship` shows every page line that holds a pointer, but `clean_parenthesis` of `.guppi/guppi/ship.py` cuts a pointer out of a longer bracket without printing a line, and a later round withdrew the answer. In Case 856 the agent cited the predicate `ships` of `.guppi/guppi/ship.py` by one line and gave its first condition only. In Case 783 it named a shared judgment without reading the function of the other side; the sentence of case 785 in `rule-case-build` already covers that form, so it stays as it is. Today the Render of `rule-case-build` asks the agent to read code for set tasks only. A fact the prompt states is read at its source (case 690.1). Before a task adds a judgment, `.guppi/guppi/` is searched and `context` names that search (case 752). Over a changed live text, the agent reads the test functions, the functions of the test file they call and the functions of `.guppi/guppi/` they call (case 754). A function named as the judgment two sides share is read whole on each side (case 785). A page offered for code no page covers is described from the code read (case 803). No sentence asks the agent to read the deciding function before every claim it makes itself about what code does, prints or leaves out, in a round, in `context`, in `then` or in a page text. The person chose to action the Insight. Case 869 adds one sentence after the sentence of case 785: before such a claim the agent reads the deciding function whole, each condition and not one line, and `context` names the file and the function. The governing rules are `rule-agent-writing`, whose passage says "Name a real source or remove the claim", and `rule-insights-schema`, by which an `update` actions an Insight and `addressed_by` takes the bare slug `decision-case-869`. The Insight was put off by Case 835, so its decision line carries `{supersedes:case 835}`. Its three lessons are archived by the cascade of `generate` once it is `actioned`. The new sentence names the Case in a bracket at the end of the sentence, since `rule-case-build` has `core: true`. The Criterion of each Estimate of `rule-case-build` was read. `estimate-case-build-reads-by-need-and-in-parts` stands: it reads a module of code in parts, and the new sentence names the deciding function as one of those parts. `estimate-case-build-offers-a-page-for-code-no-page-covers` stands, and its Criterion does not clash with the new sentence. Its Criterion reads that code in parts, the functions the Case changes and the places that call them, and the round offers a page described from the code read. Where that description says what a function does, the new sentence adds that the deciding function is read whole, and a whole function is one of the parts that Criterion reads. Nothing in that Criterion allows a claim about code from a function read at one line. `estimate-case-build-finds-an-existing-judgment` stands: its promise on a shared judgment is not changed. `estimate-case-build-reads-a-prompt-fact-at-its-source` stands: it covers a fact of the prompt, not a claim of the agent. A claim about an outside tool is the item of Case 871, and what a check printed at its last run stays with the sentence of case 798.2. A Grep `case-guppi\.md|rule-case-build` over `.guppi/tests/` printed nothing, so no test reads the live agent file. A Grep `insight-case-build-claims-what-code-does-without-reading-it` over `vault/wiki/` printed `brief.md`, `backlog.md`, `log.md` and the three lessons `lesson-case-build-reused-judgment-not-checked-against-the-other-side`, `lesson-case-build-recommended-on-a-claim-about-code-it-did-not-read` and `lesson-case-build-states-a-predicate-wider-than-the-code`. In the lessons the `insight` field stays true. `backlog.md` is written again by `guppi backlog`, and `brief.md` and `log.md` are not read. A Grep `estimate-case-build-reads-the-code-it-states` over `vault/` printed `raw/2026-10-16/event_log.md`, `raw/2026-10-16/2104/ledger.md` and this case file and no page, so the slug is free. No option rests on a check passing. Each Case of this session was built by `case-guppi` under the old Render, so the `/pre-spec` of this session cannot show the new sentence at work. The `method` of the new Estimate therefore reads the new Render at Retro, and it waits for the first `/pre-spec` of a session whose Cases were built under that Render before it counts the findings. This rebuild did not read the case files of Cases 868, 870, 871 and 872, which are rebuilt at the same time. Their decision lines in the ledger of this session show that Cases 870, 871, 872.1 and 872.3 change `rule-case-build`, and that Case 872.4 changes `estimate-case-build-reads-by-need-and-in-parts`. Where one of them takes the sentence of case 785 as its anchor, the two pairs must be read side by side.

> **problem:**
> `case-guppi` can state what a function or a script of the repository does without reading the function that decides it. A Case the person signed then rests on a false claim and is built again.

> **recommend:**
> - **What happens to this pattern**
>   - Recommended: (a) fix it: add a duty to `rule-case-build`, set the Insight `actioned` and retire its defer.
>   - Answer: agreed, (a).
> - **How wide the duty to read the code is**
>   - Recommended: (a) every claim about code in a round, `context`, `then` or a page text, the whole deciding function read, the file and the function named in `context`.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) a new Estimate `estimate-case-build-reads-the-code-it-states` on `rule-case-build`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by findings of `/pre-spec`: the `context` overstated what the Render lacks, it did not name `estimate-case-build-offers-a-page-for-code-no-page-covers`, and the `method` of the new Estimate counted findings at the `/pre-spec` of this session, whose Cases were built under the old Render.
>   - Taken: the `context` names the sentences of cases 752, 754 and 803 that already read code for set tasks, and says why the Criterion of `estimate-case-build-offers-a-page-for-code-no-page-covers` does not clash with the new sentence. The count of findings in the `method` waits for the first `/pre-spec` of a session whose Cases were built under the new Render.

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, gains the sentence on a claim about code.
> **＋** `estimate-case-build-reads-the-code-it-states`: the new Estimate of that sentence.
> **＋** `insight-case-build-claims-what-code-does-without-reading-it`: set `actioned`, its defer retired.
> **＋** `rule-agent-writing`: the rule that a claim names a real source.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and states in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out.

> **then:**
> Before it states the claim, `case-guppi` reads whole the function that decides it, each of its conditions and not only the line it cites.
> **＋** The `context` of the Case names the file and the function that `case-guppi` read for the claim.
> **＋** A claim about code that `case-guppi` did not read stays out of the Case.
> **－** `case-guppi` still reads a module of code in parts: the deciding function is one of those parts.

```then
create:
- slug: estimate-case-build-reads-the-code-it-states
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi, before it states what a function or a script of the repository does, prints or leaves out, reads whole the function that decides it, names its file and the function in context, and keeps out a claim about code it did not read
  method: 'by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion; by hand, after the first /pre-spec of a session whose Cases case-guppi built with .claude/agents/case-guppi.md rendered from that Render: the findings of ask-guppi at that /pre-spec read for a claim of a Case about what code of the repository does that its context does not back by the function it read, the count in the estimate line'
  tags:
  - session
  - workflow
  - harness
  - case-build
update:
- slug: rule-case-build
  replace:
  - old: and the task adds one test that runs both sides over that input and asserts they answer alike (case 785).
    new: and the task adds one test that runs both sides over that input and asserts they answer alike (case 785). Before you state in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out, read whole the function that decides it, each of its conditions and not only the line you cite, and name its file and the function in `context`; that function is one of the parts of its module that you read, and a claim about code you did not read stays out of the Case (case 869).
  change: case-guppi reads whole the function that decides a claim it states about code, and names it in context (case 869)
- slug: insight-case-build-claims-what-code-does-without-reading-it
  set:
    status: actioned
    addressed_by: decision-case-869
  change: 'actioned: case-guppi reads whole the function that decides a claim it states about code, and names it in context (case 869)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] create `estimate-case-build-reads-the-code-it-states`
- [x] update `insight-case-build-claims-what-code-does-without-reading-it`
- [ ] read `estimate-case-build-reads-the-code-it-states`
```

## Case 870 — case-guppi asks before it puts a change into a new Case

> **context:**
> When the main agent asks `case-guppi` to change a Case by name, the agent sometimes writes a new top-level Case under a new number, and the named Case stays as it was. `insight-case-build-opens-a-new-case-where-one-was-named` clusters two lessons of this cause. In session 0104, at `/pre-spec`, the agent of Case 847 was asked to take the task that pushes the release tag into Case 847. It built Case 850 beside it, and Cases 841, 843 and 846, built again in the same message, named Case 847 as the holder of the push and went back a second time (`lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own`). The case file of Case 850 says why: Case 847 already had a decision line. That follows the sentence of case 725.1 in the Render of `rule-case-build`, which has the agent build a fix that adds a second behaviour to a ratified Case with no sub-cases as a new Case beside it, under a number it picks itself. In session 0342 the agent of Case 851, ratified in Plan Mode, got the `/pre-spec` findings and wrote `case-856.md` with `{supersedes:case 851}` marks, the step that the sentence of case 806.2 sets for Work Mode only, and the main agent sent it back to rebuild under 851 (`lesson-case-build-rebuilds-a-ratified-case-under-a-new-number-in-plan-mode`). In both events the agent alone chose where a change goes. The rule that governs this is `rule-case-build` itself, whose Render says that the agent decides nothing the person has not decided.
>
> The person chose to action the Insight by a round before a new Case. Where a message names a Case, the agent builds the change under that number. Outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one, as it does for a Case built again in another shape. Where a fix would add a second behaviour to a ratified Case with no sub-cases, the agent writes no new file. It asks the person in a round whether the behaviour goes into that Case or into a new Case beside it. The Insight's own proposal, that only the main agent gives out new numbers, was not taken. It conflicts with `vault/wiki/case-schema.md`, where the check of the file names the new number of a Case built again in another shape, and with the guard of `rule-spec-reconcile`, which holds a number the agent takes. That guard and `next_id` of `.guppi/guppi/caseid.py` already keep two Cases from one number, since `next_id` counts the keys of the store and the case files. Other Cases being rebuilt in parallel may still name the old Case before the person answers. That part is the item of Case 872.
>
> The behaviour is checked by `estimate-case-build-writes-the-case`, whose Criterion holds the old line on a new Case beside a ratified one. This Case replaces that Criterion whole. The old line becomes three, and a fourth line is new: a `－` line that says it does not put a change asked on a named Case into a new top-level Case without the person's answer to a round. The line on the tools names WebFetch, since Case 871, ratified in this session, adds `WebFetch` to the tools of the Render, and the reading of this Criterion at Retro comes after that render. Every other line stands as it was. The check of the file notes two old lines as not carried: the line on a new Case beside a ratified one and the line on the model and the tools. Both are rewritten, not dropped. Its `purpose` and `method` do not state the old promise, so they stand. In `rule-case-build`, read whole, these sentences state the behaviour. The sentence of case 645.1, which says that a message is answered by `Edit` of the file, or by a round when it opens a fork, stays true. The sentence of case 725.1 changes by the `replace` pair below, and its end, from the number onward, stays. The sentences of case 806.2 on Work Mode stay true. The list of files the agent may write, which names the file of a new Case built beside a ratified Case, stays true, since that Case is still built when the person chooses it. In `vault/wiki/orchestration.md`, the sentence that the guard holds a number `case-guppi` takes for a Case built again stays true. A round sent back at `/pre-spec` is shown to the person by step 4 of `rule-prespec`, so this Case does not set that moment.
>
> A Grep for `case-guppi\.md|rule-case-build|estimate-case-build-writes-the-case` over `.guppi/tests/` printed no file, so no test reads the live agent file or these pages. A Grep for `estimate-case-build-writes-the-case|insight-case-build-opens-a-new-case-where-one-was-named` over `vault/wiki/` printed `backlog.md`, `log.md`, `lessons/lesson-case-build-rebuilds-a-ratified-case-under-a-new-number-in-plan-mode.md`, `lessons/lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own.md`, `rules/rule-case-build.md`, `estimates/estimate-case-check-sends-back-a-faulty-case.md` and `estimates/estimate-skill-grill-me-asks-in-rounds.md`. `backlog.md` is written again by `guppi backlog`, and `log.md` is not read. The `insight` field of the two lessons stays true. The hit in `estimate-skill-grill-me-asks-in-rounds` is a History line. The Criterion of `estimate-case-check-sends-back-a-faulty-case` waits for a reading of `estimate-case-build-writes-the-case` that passes live, for an old way of reading a transcript. This Case does not change that path, and the Result of that Estimate already records a passing reading on 2026-10-14, so the line stands.
>
> The Insight leaves the backlog by an `update` to `actioned` with `addressed_by: decision-case-870`, as `rule-insights-schema` sets it (case 712). It has no `deferred_by`, so no `{supersedes:...}` mark is needed. Its two lessons belong to other sessions, so they get no mark. Cases 868 and 869 of this batch change `rule-case-build` by pairs on the sentence on a reader that only goes red and on the sentence of case 785. This Case's pair stands on the sentence of case 725.1, so the anchors do not overlap. Cases 871 and 872 also change `rule-case-build`, and their files were not read. If one of them takes the sentence of case 725.1 as its anchor, the two pairs must be read side by side. No option rests on a check passing.

> **problem:**
> Asked to change a named Case, `case-guppi` may put the change into a new top-level Case under a number it picks. The named Case then stays as it was, and the Cases that name it are built again. The person never chose where the change goes.

> **recommend:**
> - **What should be done with this insight?**
>   - Recommended: (a) ask before opening a new Case: a change goes under the number of the Case a message names; where a fix would add a second behaviour to a ratified Case with no sub-cases, `case-guppi` writes no new file and asks in a round whether it goes into that Case or into a new Case beside it; during planning a named Case keeps its number unless the schema sets a new one.
>   - Answer: agreed, (a).
> - **Which check page proves the change?**
>   - Recommended: (a) replace the Criterion of `estimate-case-build-writes-the-case` whole, its old line on a new Case beside a ratified one made three.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `insight-case-build-opens-a-new-case-where-one-was-named`: the Insight this Case actions.
> **＋** `vault/wiki/case-schema.md`: the form that sets a new number for a Case built again.
> **＋** `rule-prespec`: the rule that shows the person a round sent back at `/pre-spec`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of a round.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of the case files of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `.guppi/guppi/ratified.py`: the guard that names a free number for a case file.
> **＋** `rule-case-check`: the check of a case file and of a summary.
> **＋** `vault/wiki/ratification.md`: the form of the ledger lines.
> **＋** `.claude/agents/ask-guppi.md`: the vault query run before a `create` without a `ref`.
> **＋** `.claude/settings.json`: the hooks registered on each event.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
> **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.
> **＋** Or, in Work Mode, the main agent dispatches it with the id of a new top-level Case, the path of the file of a ratified Case of the approved Spec, the sub-case of it that must change and the reason.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
> **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
> **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
> **＋** Where an Estimate that the Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate, never that promise written again.
> **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
> **＋** Asked, by a message or by a finding of `/pre-spec`, to change a Case, it builds the change under the number of that Case; outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one for it.
> **＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it writes no new file and answers with a round that asks whether the behaviour goes into that Case, built again under a new number as `vault/wiki/case-schema.md` sets it, or into a new top-level Case beside it.
> **＋** Where the person chooses a new Case beside it, it builds that behaviour as a new top-level Case in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `.guppi/guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
> **＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
> **＋** Dispatched in Work Mode with a ratified Case and the sub-case of it that must change, it reads the file of that Case whole and builds under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand: each page change, task and Estimate of that sub-case that still holds, with the change.
> **＋** Each decision line of that new Case carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases, and the file of the ratified Case stays as it is.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** In Work Mode a round may also come when it builds a new Case that replaces a sub-case of a ratified Case.
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write, Edit and WebFetch, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
> **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
> **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
> **－** It does not put a change asked on a named Case into a new top-level Case without the person's answer to a round.
> **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
> **－** In Work Mode it never builds a Case of the approved Spec again under its own number; a Case ratified in that Work Mode that comes back to it before any of its tasks has run it changes under its own number, as in Plan Mode.
> **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
> **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, and the file of a new Case it builds beside a ratified Case, and no ledger line.
> **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.

```then
update:
- slug: rule-case-build
  replace:
  - old: A fix, asked by a message or by a finding of `/pre-spec`, that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, you build as a new top-level Case beside it, in its own file and with no `{supersedes:case N}` mark, under a number
    new: 'A change that a message or a finding of `/pre-spec` asks on a Case you build under the number of that Case: outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one for it (as set in case 870). A fix, asked by a message or by a finding of `/pre-spec`, that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, you do not place yourself: you write no new file and answer with a round that asks whether the behaviour goes into that Case, built again under a new number as `vault/wiki/case-schema.md` sets it, or into a new top-level Case beside it (as set in case 870). Where the person chooses a new Case beside it, you build it in its own file and with no `{supersedes:case N}` mark, under a number'
  change: case-guppi builds a change under the number of the Case a message names, and asks in a round before it puts a second behaviour of a ratified Case into a new Case beside it (case 870)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  change: the Criterion replaced whole — a change goes under the number of the named Case, and a round comes before a new Case beside a ratified one
- slug: insight-case-build-opens-a-new-case-where-one-was-named
  set:
    status: actioned
    addressed_by: decision-case-870
  change: 'actioned: case-guppi builds a change under the number of the Case a message names, and asks in a round before a new Case beside a ratified one, in rule-case-build (case 870)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] update `estimate-case-build-writes-the-case`
- [x] read `estimate-case-build-writes-the-case`
- [x] update `insight-case-build-opens-a-new-case-where-one-was-named`
```

## Case 871 — case-guppi reads the documentation of an outside tool before it recommends on it

> **context:**
> `case-guppi` sometimes recommends an option that rests on how a tool outside the repository behaves: what GitHub accepts, which file of settings pytest reads from the root of the repository. The agent has only the tools Read, Grep, Glob, Write and Edit, so it cannot read the documentation of such a tool, and no sentence of `rule-case-build` says what it does with such a fact. The fact is taken as given, the person ratifies the Case, and the fact proves false in Work Mode. `insight-case-build-rests-on-an-unchecked-fact-of-a-tool` clusters two lessons of this cause. In `lesson-case-build-recommended-an-unchecked-github-fact` the agent said in its round that it could not read whether GitHub accepts the built-in Actions account on the bypass list of a ruleset, recommended the option all the same, GitHub refused it with HTTP 422 in Work Mode, and Case 804 was built and ratified again. In `lesson-case-build-names-a-pytest-config-the-root-run-does-not-read` Case 823.1 put the pytest settings in the package's own settings file, while a run from the root reads the root `pyproject.toml`, and Work Mode added the same lines there. The person chose to action the Insight: `WebFetch` joins the tools of the agent, the agent reads the documentation of the tool before it recommends such an option and names the page in `context`, and where the documentation does not settle the fact the option says so and is not recommended. `/pre-spec` does not change, since `ask-guppi` has no tool to read the web either.
>
> The rule that governs the choice is `rule-agent-writing`, whose passage says "Name a real source or remove the claim"; an option recommended on a fact nobody read breaks it, and the new sentence keeps it. `rule-insights-schema` sets that an `update` actions an Insight and that `addressed_by` takes the bare slug `decision-case-871` (case 712). The Insight has no `deferred_by`, so no `{supersedes:...}` mark is needed, and its two `clustered` lessons go to the archive by the cascade of `generate`. No option of the rounds rests on whether a check passes, so no output of a check was read. Whether a call of `WebFetch` by the agent under `permissionMode: auto` runs with no prompt was not read; the reading at Retro reads the text of the rule only.
>
> In `rule-case-build`, read whole, three sentences speak of the behaviour. The sentence of case 690.1 keeps a fact of the prompt that the agent cannot read at its source out of the Case; it stays true. The sentence of cases 798.2 and 801 lets an option that rests on whether a check passes be recommended when its last output was not read; the new sentence follows it and leaves that case to it, and the `－` line of `then` says so. The `tools` line of the Render gains `WebFetch`. The `Purpose` of the page names no tools, so it stands. The new sentence speaks of tools outside the repository; Case 869 of this session adds a sentence on a claim about code of the repository, anchored on the sentence of case 785, and Case 868 a sentence anchored on the sentence of a reader that only goes red; their texts were read beside this one, and the anchors and the subjects differ. Cases 870 and 872 of this session also change `rule-case-build` and their files were not read; where one of them anchors a pair on the sentence of cases 798.2 and 801 or on the `tools` line, the two pairs must be read side by side.
>
> A Grep for `tools|WebFetch|documentation|outside` over `vault/wiki/estimates/estimate-case-build-*.md` printed `estimate-case-build-checks-the-finished-case.md` and `estimate-case-build-writes-the-case.md`. The first speaks of the person's answers outside the options, not of this change. The Criterion of `estimate-case-build-writes-the-case` says that the agent runs with the tools Read, Grep, Glob, Write and Edit and `permissionMode: auto`, so that it writes its file with no prompt in Plan Mode. That line stays true: those tools stand, and it promises the write of the file, not the whole list. The new Estimate `estimate-case-build-checks-a-fact-of-an-outside-tool` promises `WebFetch` among the tools, so the promise is not signed twice. `/pre-spec` found that a Criterion lifted from the `when` and `then` of this Case would ask, at the Retro of this session, for the rendered agent file and for the tool calls of an agent rendered from the new rule, which only the render after Retro and a later session produce. The person chose a reading at this Retro, so the Estimate writes its own Criterion under `sections`, bound to the Render of `rule-case-build` in the Spec, which that reading reads; the `when` and `then` of this Case stay the behaviour of the agent. A Grep for `Read, Grep, Glob, Write, Edit|WebFetch|outside tool` over `vault/wiki/`, `.claude/` and `.guppi/` printed `vault/wiki/backlog.md`, `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/insights/insight-case-build-rests-on-an-unchecked-fact-of-a-tool.md`. The agent file changes by the render, `backlog.md` is written again by `guppi backlog`, and the Insight is set `actioned` by this Case. `.guppi/tests/test_guppi_package.py` reads each file under `.claude/` and the live pages, and fails on the old commands and paths its `OLD_COMMANDS` and `OLD_PATHS` hold; the new texts hold none of them. A Glob `vault/**/*outside-tool*` printed nothing, so the slug of the new Estimate is free.

> **problem:**
> `case-guppi` recommends options that rest on how a tool outside the repository behaves, with no means and no duty to check that behaviour. The fact proves false only in Work Mode, after the person ratified the Case, and the Case is built and ratified again.

> **recommend:**
> - **What do we do with this Insight?**
>   - Recommended: (a) act on it: `WebFetch` joins the tools of `case-guppi`, which reads the documentation of the tool before it recommends an option that rests on it and gives the address of the page in `context`.
>   - Answer: agreed, (a).
> - **What if the documentation does not settle the fact?**
>   - Recommended: (a) the option's `**After:**` line and `context` say that the fact is not checked, and the option is not recommended; where each option rests on the fact, the round says so and the person decides.
>   - Answer: agreed, (a).
> - **Does `/pre-spec` check it too?**
>   - Recommended: (a) no, only `rule-case-build` changes.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) a new Estimate `estimate-case-build-checks-a-fact-of-an-outside-tool`, read at the Retro of this session.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`, which gains `WebFetch` and the sentence on a fact of an outside tool.
> **＋** `estimate-case-build-checks-a-fact-of-an-outside-tool`: the new Estimate of that sentence.
> **＋** `insight-case-build-rests-on-an-unchecked-fact-of-a-tool`: the Insight this Case actions.
> **＋** `rule-agent-writing`: the rule that a claim names a real source.
> **＋** `estimate-case-build-writes-the-case`: its Criterion names the tools of the agent, and stands.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, writes a round with an option that rests on how a tool outside the repository behaves, such as what a service accepts or which file of settings a test runner reads.

> **then:**
> Before it recommends that option, `case-guppi` reads that behaviour in the documentation of the tool by `WebFetch`, and the `context` of the Case gives the address of the page it read and what the page says of the fact.
> **＋** `WebFetch` stands among the tools of `.claude/agents/case-guppi.md`.
> **＋** Where the documentation it read does not settle the fact, the `**After:**` line of the option and the `context` say that the fact is not checked, and `case-guppi` does not recommend that option.
> **＋** Where each option of the question rests on that fact, the `➡️` line says that the fact is not checked and leaves the choice to the person.
> **－** An option that rests on whether a check passes stays with the reading of the last output of that check, as `rule-case-build` sets it.

```then
create:
- slug: estimate-case-build-checks-a-fact-of-an-outside-tool
  ref: rule-case-build
  kind: QA
  purpose: Whether the Render of rule-case-build gives case-guppi WebFetch among its tools and tells it to read in the documentation of a tool outside the repository the behaviour an option rests on before it recommends that option, to give the address of the page in context, and not to recommend an option whose fact the documentation does not settle
  method: 'by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
  - case-build
  sections:
    Criterion: |-
      When:
      The Render of `rule-case-build` in `raw/<date>/<hi HHMM>/spec.md`, the text that `.claude/agents/case-guppi.md` is rendered from, is read at the Retro of the session that changes it.

      Then:
      Its `tools` line holds `WebFetch`.
      **＋** It tells `case-guppi`, before it recommends an option that rests on how a tool outside the repository behaves, to read that behaviour in the documentation of the tool by `WebFetch` and to give in `context` the address of the page it read and what the page says of the fact.
      **＋** It tells `case-guppi` that, where the documentation it read does not settle the fact, the `**After:**` line of the option and `context` say that the fact is not checked, and the option is not recommended.
      **＋** It tells `case-guppi` that, where each option of the question rests on that fact, the `➡️` line says that the fact is not checked and leaves the choice to the person.
      **－** It leaves an option that rests on whether a check passes to the reading of the last output of that check.
update:
- slug: rule-case-build
  replace:
  - old: 'tools: Read, Grep, Glob, Write, Edit'
    new: 'tools: Read, Grep, Glob, Write, Edit, WebFetch'
  - old: and the option may still be recommended (cases 798.2, 801).
    new: and the option may still be recommended (cases 798.2, 801). Where an option rests instead on how a tool outside the repository behaves, such as what a service like GitHub accepts or which file of settings a test runner reads, read that behaviour in the documentation of the tool by `WebFetch` before you recommend the option, and give in `context` the address of the page you read and what it says of the fact; where the documentation you read does not settle the fact, the `**After:**` line of the option and `context` say that the fact is not checked, and you do not recommend that option, and where each option of the question rests on that fact, the `➡️` line says that the fact is not checked and leaves the choice to the person (as set in case 871).
  change: case-guppi gains WebFetch and reads the documentation of an outside tool before it recommends an option that rests on how that tool behaves; an unsettled fact is said and its option not recommended (case 871)
- slug: insight-case-build-rests-on-an-unchecked-fact-of-a-tool
  set:
    status: actioned
    addressed_by: decision-case-871
  change: 'actioned: case-guppi gains WebFetch and reads the documentation of an outside tool before it recommends on it, in rule-case-build (case 871)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] create `estimate-case-build-checks-a-fact-of-an-outside-tool`
- [x] read `estimate-case-build-checks-a-fact-of-an-outside-tool`
- [x] update `insight-case-build-rests-on-an-unchecked-fact-of-a-tool`
```

## Case 872 — Cases built at the same time read no sibling mid-build

> **context:**
> The main agent often sends two or more Cases to their `case-guppi` at once: the first build of a batch, the answers of a batch, and the loop after the findings of `/pre-spec`. Each `case-guppi` reads the case files of the related Cases whenever it gets to them. If a sibling Case is still being built, it reads the half-done text and takes it for the result. `insight-subagents-read-a-sibling-mid-flight` clusters two lessons of this cause. In session 0104 the `case-guppi` of Case 843 read `case-846.md` before the rebuild of Case 846 ended. Case 843 then kept an `**Other Case:**` line that asked for a reading the finished `case-846.md` already held (`lesson-case-build-reads-a-sibling-case-file-mid-rebuild`). In session I of 2026-09-12 four agents edited one working tree at once, and each saw the tests red mid-run on files it had not touched (`lesson-subagents-parallel-on-one-tree-red-mid-flight`). The person chose to action the Insight. During a joint send, a `case-guppi` reads no file of a Case built at the same time. Its summary names the siblings its Case rests on on a `**Sibling:**` line. Once every `case-guppi` has answered, each Case with such a line goes back alone, one after another, to read the finished files. That pass runs once. By the person's words in this session, the main agent also asks the person no question on an `**Other Case:**` line in Plan Mode: it sends the other Case back by itself, and the person agrees or not at its showing. The Insight's own proposal had the main agent check the cross-references itself. It was not taken, since `rule-orchestration` has the main agent write from the summary without reading a case file (case 645.6). The second lesson stays out of the Case: `rule-work-mode` already runs `uv run --project .guppi guppi test` in full once after the last task, against the baseline, and its `Purpose` leaves subagents in Work Mode undecided (case 479.2).
>
> The rules that govern the choice are `rule-ratification`, whose atomicity rule splits the three parts, since each can fail alone and needs its own fix, and `rule-orchestration`, by which the main agent reads no case file, so the second pass is found from the summary. The `**Sibling:**` line is judged by no code. `summary_names` and `summary_findings` of `.guppi/guppi/casecheck.py`, read whole, read only the `**Built:**` and `**Case:**` lines of a summary, so a new line passes the check. A Grep `Other Case|whether that other Case|whether another Case` over `.guppi/guppi/` printed nothing, so no code judges the `**Other Case:**` line either. `rule-case-check` compares a case file with the other Cases of the session from the plan file and the store, the texts its check stored, so this Case does not change it. No option rests on a check passing.
>
> In `rule-case-build`, read whole, these sentences state the behaviour. The sentence of case 579.2 has the agent read the case file of each Case the prompt names. It stays, and the new sentence of Case 872.1 follows it and sets the exception for a Case built at the same time. The sentence of cases 637.2 and 645.1 says that the main agent asks the person whether the other Case is built again. Case 872.3 changes it. In `rule-orchestration`, read whole, three passages set the question on an `**Other Case:**` line: the showing of a summary, the list of questions the main agent puts itself, and the batch paragraph. Case 872.3 changes the first two, and Case 872.5 the third. The description of the summary gains the `**Sibling:**` line in Case 872.2, and the joint send and the second pass join the end of the batch paragraph. The dispatch sentence of case 684.2, which names each other Case of a batch by the path of its case file where it stands, stays true. In `rule-prespec`, step 2 sends the findings in one message and step 6 starts the confirmation of `ask-guppi`. Case 872.2 changes both.
>
> A Grep `Other Case` over `vault/wiki/` printed `orchestration.md`, `log.md`, `lessons/lesson-case-build-reads-a-sibling-case-file-mid-rebuild.md`, `insights/insight-subagents-read-a-sibling-mid-flight.md`, `rules/rule-case-build.md`, `estimates/estimate-orchestration-signs-items-taken-together.md`, `estimates/estimate-case-build-writes-the-case.md`, `estimates/estimate-orchestration-shows-the-built-case.md` and `rules/rule-orchestration.md`. `orchestration.md` changes by the render. `log.md` is not read. The lesson and the Insight are records this Case closes. The line of `estimate-case-build-writes-the-case` says that `case-guppi` writes the `**Other Case:**` line, which stays true, and Case 870 replaces that Criterion. The Criteria of `estimate-orchestration-shows-the-built-case` and `estimate-orchestration-signs-items-taken-together` promise the question. Case 872.3 replaces the first and Case 872.5 the second, each whole under `sections`, and each sets the `method` anew to wait for the next such line, since both methods read only the old promise. The check of this file notes the line of each Criterion on the question, and the line of the first on what the main agent writes from the summary, as not carried: each is rewritten, not dropped. The check found two promises in Case 872.3 when both Estimates stood under it, so the batch side is Case 872.5. The check notes `then` lines of Case 872.5 that share most of their words with Case 872.3. Case 872.3 sets the send of the other Case at the showing of any summary, and Case 872.5 sets it in the list of the rounds of a batch, each under its own Estimate. The check also notes `then` lines of Cases 872.2, 872.4 and 872.7 that share most of their words with Case 872.1. They state the hold-off from four sides — what `case-guppi` does, what the main agent sends, the reading by need and the check of the finished Case — and do not sign one promise twice: Cases 872.4 and 872.7 point at the Estimate of Case 872.1. A Grep `whether (that|another|the) (other )?Case is built again|another Case is built again` over `vault/wiki/` also printed `estimates/estimate-orchestration-asks-in-the-grill-me-shape.md`, besides `orchestration.md`, `rules/rule-case-build.md`, `rules/rule-orchestration.md` and the two Estimates above. Its Criterion lists that question, and its `purpose` names it, with no bound to Work Mode, while the new Render holds it in Work Mode only (a finding of `ask-guppi` at `/pre-spec`). Case 872.6 replaces that Criterion whole and sets its `purpose` anew. It also sets its `method`, which waited for a later session, to read the new Render at the Retro of this session. The check notes that Criterion's line on the question as not carried: it is rewritten, bound to Work Mode, not dropped. A Grep `Other Case` over `.claude/` printed `.claude/agents/case-guppi.md`, which changes by the render.
>
> A Grep `case file of each Case|caller's prompt names|related to the item` over `vault/wiki/estimates/` printed `estimate-case-build-reads-by-need-and-in-parts.md`. Its Criterion says that `case-guppi` reads whole the case file of each Case the prompt names, which Case 872.1 makes false for a Case built at the same time. So Case 872.4 replaces it whole, with one `－` line added that points at the new Estimate of Case 872.1. The person chose three parts; the check of this file found the update of that Estimate a second promise inside Case 872.1, so it stands as a sub-case of its own, which sets no new behaviour. Its `purpose` and `method` stand, since they speak of the related Cases in general and of a reading of the Render. `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-orchestration-batches-cases-out-at-once`, `estimate-prespec-gathers-the-answers-after-findings` and `estimate-prespec-confirms-the-findings-once` speak of joint sends. Their Criteria stay true: the prompt still names the Cases, the Cases still go out together, and the confirmation still waits until every `case-guppi` has answered. So they stand, and the new Estimates of Cases 872.1 and 872.2 check the change.
>
> A Grep `orchestration\.md|case-guppi\.md|pre-spec/SKILL|rule-orchestration|rule-prespec\b|rule-case-build` over `.guppi/tests/` printed `test_prespec.py`, `test_orchestration.py` and `test_config.py`. `test_orchestration.py` reads the two examples of `orchestration.md`, which this Case leaves as they are. The other two only name a rule in a docstring or a string. `.guppi/tests/test_guppi_package.py` reads every file under `.claude/` and the live pages, and fails on the strings of `OLD_COMMANDS` and `OLD_PATHS` (a Grep `OLD_COMMANDS|OLD_PATHS` over it). The new texts hold none of them. A Glob `vault/**/*{sibling,joint-send}*` printed `estimates/estimate-case-check-notes-a-then-line-shared-by-siblings.md`, the Insight and the lesson, so both new slugs are free.
>
> The findings of `ask-guppi` at `/pre-spec` shaped this build too. A sibling's case file never stands in `given`, since the frame paragraph of `rule-case-build` reads each file `given` names; it is named in `context` and on the `**Sibling:**` line only. Case 870 rests on the same frame paragraph, since its new Criterion of `estimate-case-build-writes-the-case` keeps the line that `case-guppi` reads each page and file `given` names. That line stays true with this Case, as no sibling's file stands in `given`; the main agent passed that point on to Case 870. Where the other Case that an `**Other Case:**` line names answers with a round, as Case 870 lets a `case-guppi` do, the round goes into the list of the batch. Step 5 of `rule-prespec` is a joint send too, so it names the siblings as step 2 does. `estimate-case-build-checks-the-finished-case` holds the new text against each Case the prompt names, and `estimate-orchestration-signs-a-batch-together` shows a batch once every answer is in. Cases 872.7 and 872.8 replace those Criteria, and each adds one `－` or `＋` line that points at the Estimate of Case 872.1 or Case 872.2. Their `purpose` and `method` speak of the Cases of the session in general and of a reading of the Render, so they stand. Each replaced Criterion is a promise of its own, so it stands in a sub-case of its own.
>
> Cases 868, 869, 870 and 871 of this batch change `rule-case-build`. Their files were read after their first builds ended. In this rebuild they are built at the same time, so their files were not read again, and the summary names them on a `**Sibling:**` line. Their anchors are the sentence on a reader that only goes red, the sentence of case 785, the sentence of case 725.1, and the `tools` line with the sentence of cases 798.2 and 801. The anchors of this Case are the sentence of case 579.2 and the sentence of cases 637.2 and 645.1, so no pair overlaps. The Insight leaves the backlog by an `update` to `actioned` with `addressed_by: decision-case-872.1`, as `rule-insights-schema` sets it (case 712). It has no `deferred_by`, so no `{supersedes:...}` mark is needed. Its `clustered` lessons go to the archive by the cascade of `generate`.

> **problem:**
> Agents that run at the same time read files that a sibling agent is still writing. A Case then rests on a sibling's half-done text. And the person gets a separate question just to pass a change from one Case to another.

> **recommend:**
> - **What to do with the Insight**
>   - Recommended: (a) during a joint send, `case-guppi` reads no file of a Case built at the same time; once all have answered, each Case that points at a sibling goes back once to read the finished file.
>   - Answer: agreed, (a).
> - **One promise or two parts**
>   - Recommended: (a) two sub-cases, one on `rule-case-build` and one on `rule-orchestration` and `rule-prespec`.
>   - Answer: not answered; replaced by the question One promise or several parts, after the person's words on the question round for another Case.
> - **One promise or several parts**
>   - Recommended: (a) three sub-cases: the build during a joint send, the second pass of the main agent, and the send of another Case with no question.
>   - Answer: agreed, (a).
> - **Which joint sends it covers**
>   - Recommended: (a) every time Cases are out together, the first build of a batch included.
>   - Answer: agreed, (a).
> - **Agents that edit one working tree in Work Mode**
>   - Recommended: (a) leave Work Mode out; `context` says that the full test run after the last task covers that lesson.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) a new Estimate for the hold-off and one for the second pass, read after the next joint send; the two Estimates that promise the question have their Criteria replaced whole.
>   - Answer: agreed, (a).
> - **Where the question about another Case goes away**
>   - Recommended: (a) everywhere in Plan Mode: the main agent sends the other Case back by itself, and the person agrees or not at its showing; Work Mode stays as it is.
>   - Answer: agreed, (a). The person had said that a separate round only to pass information between Cases is bad, and that the agent should handle it.
> - **How the main agent knows which Case points at a sibling**
>   - Recommended: (a) a new summary line `**Sibling:**` from `case-guppi`, naming each Case of the send whose file it did not read and on which its Case rests.
>   - Answer: agreed, (a).
> - **How the second pass runs**
>   - Recommended: (a) one Case after another, once, with no further loop; then an `**Other Case:**` line that still stands sends its Case back with no question.
>   - Answer: agreed, (a).

### Case 872.1 — case-guppi reads no file of a Case built at the same time

> **given:**
> `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.
> **＋** `estimate-case-build-reads-no-sibling-file-mid-send`: the new Estimate of the hold-off.
> **＋** `insight-subagents-read-a-sibling-mid-flight`: the Insight this Case actions.
> **＋** `rule-case-check`: the check of the file of a Case, whose findings may name another Case.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case from a prompt or a message that names another Case of the session as built at the same time.

> **then:**
> `case-guppi` reads no case file of that other Case in that build, though the prompt or a finding of the check of `rule-case-check` names it.
> **＋** It names no case file of that other Case in `given`, so the frame it reads holds none.
> **＋** It bounds its Case by the sentence the prompt gives on that other Case.
> **＋** Where its Case rests on that other Case — a claim of `context` or a line `**Other Case:**` — its `context` names that Case, and the item of its Case in the summary carries a line `**Sibling:**` that names it.
> **＋** Sent a later message that says that the build of that Case has ended, it reads the finished case file whole and fixes its Case against it.
> **－** A Case of the session that no prompt or message names as built at the same time it reads as before.

```then
create:
- slug: estimate-case-build-reads-no-sibling-file-mid-send
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi reads no case file of a Case that its prompt or a message names as built at the same time and names none in given, names in context and in a Sibling line of its summary each such Case its Case rests on, and reads the finished file whole once a message says that build has ended
  method: 'by hand, after the first send of two or more Cases to case-guppi at the same time under the new Render of rule-case-build: the tool calls and the summary of each case-guppi of that send read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
  - case-build
update:
- slug: rule-case-build
  replace:
  - old: and read your new text of that page beside its text and fix a contradiction between them (case 579.2).
    new: 'and read your new text of that page beside its text and fix a contradiction between them (case 579.2). Where the prompt or a message names a Case as built at the same time as yours, read no file of that Case in this build, though this paragraph or a finding of the check names it, and name no file of it in `given`, so that the frame you read holds none: bound your Case by the sentence the prompt gives on that Case, and where your Case rests on it — a claim of `context` or a line `**Other Case:**` — name that Case in `context` and write under the item of your Case in the summary a line `**Sibling:**` that names each such Case; when a later message says that the build of that Case has ended, read its finished file whole and fix your Case against it, as this paragraph sets it for a Case of the session (as set in case 872.1).'
  change: case-guppi reads no file of a Case built at the same time, names the Cases its Case rests on in a Sibling line, and reads their finished files when their build has ended (case 872.1)
- slug: insight-subagents-read-a-sibling-mid-flight
  set:
    status: actioned
    addressed_by: decision-case-872.1
  change: 'actioned: Cases built at the same time read no sibling file mid-build, and a second pass reads the finished files, in rule-case-build, rule-orchestration and rule-prespec (case 872)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] create `estimate-case-build-reads-no-sibling-file-mid-send`
- [ ] read `estimate-case-build-reads-no-sibling-file-mid-send`
- [x] update `insight-subagents-read-a-sibling-mid-flight`
```

### Case 872.4 — The reading by need leaves out a Case built at the same time

> **given:**
> `estimate-case-build-reads-by-need-and-in-parts`: its Criterion is replaced whole.
> **＋** `estimate-case-build-reads-no-sibling-file-mid-send`: the Estimate of the hold-off, which the replaced Criterion points to.
> **＋** `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.

> **when:**
> The main agent dispatches `case-guppi` by `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, or sends it a message by `SendMessage`.

> **then:**
> `case-guppi` reads whole the case file of each Case of the session that the prompt of its call names, and of each Case of the session that the check of its file names in a finding or a note.
> **－** The case file of a Case that the prompt or a message names as built at the same time it does not read in that build, as `estimate-case-build-reads-no-sibling-file-mid-send` checks.

```then
update:
- slug: estimate-case-build-reads-by-need-and-in-parts
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The main agent dispatches `case-guppi` by `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, or sends it a message by `SendMessage`.

      Then:
      `case-guppi` reads `vault/wiki/case-example.md` once in a dispatch, just before its first `Write` of the file of a Case.
      **＋** It reads whole each page the Case changes and the Criterion of each Estimate such a page lists.
      **＋** It reads in parts, by a Grep with lines of context or a Read with `offset` and `limit`, the case file of a Case of an earlier session, the brief and the handoff of the session, a page it reads only for background, and a module of code, of which it reads the functions the Case changes and the places that call them.
      **＋** It reads whole the case file of each Case of the session that the prompt of its call names, and of each Case of the session that the check of its file names in a finding or a note.
      **＋** It makes the tool calls that do not wait on each other's output in one turn.
      **＋** `.claude/agents/case-guppi.md` sets the cache of the agent to live one hour, by `cacheTtl: "1h"` under `experimental`.
      **－** A dispatch that answers only with rounds does not read `vault/wiki/case-example.md`.
      **－** The case file of a Case that the prompt or a message names as built at the same time it does not read in that build; it reads that file whole only after a later message says that the build of that Case has ended, as `estimate-case-build-reads-no-sibling-file-mid-send` checks.
  change: the Criterion replaced whole — the case file of a Case built at the same time is read only after its build has ended
```

```tasks
- [x] update `estimate-case-build-reads-by-need-and-in-parts`
- [x] read `estimate-case-build-reads-by-need-and-in-parts`
```

### Case 872.2 — The main agent re-sends a Case that rests on a sibling, once, one at a time

> **given:**
> `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `rule-prespec`: the rule of `/pre-spec`, rendered into `.claude/skills/pre-spec/SKILL.md`.
> **＋** `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`: the new Estimate of the second pass.
> **＋** `rule-case-build`: the rule that has `case-guppi` write the `**Sibling:**` line.
> **＋** `rule-case-check`: the check of the file of a Case.

> **when:**
> The main agent sends two or more Cases of the session to their `case-guppi` at the same time — the dispatch of a batch, the answers of a batch sent back, or the loop after the findings of `/pre-spec` — with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The prompt or message to each `case-guppi` names each other Case of that send as built at the same time.
> **＋** Once every `case-guppi` of the send has answered with its Case, the main agent sends back each Case whose item in the summary carries a line `**Sibling:**`, one at a time, each after the one before has answered, with a message that the build of each Case that line names has ended.
> **＋** The second pass runs once, and the Cases of the send are shown after it, together, for one ratification.
> **＋** In the loop after the findings of `/pre-spec`, the second pass comes before the `ask-guppi` runs confirm their findings.
> **－** A Case whose summary carries no line `**Sibling:**` does not go back in the second pass.
> **－** The main agent reads no case file to find the Cases of the second pass.

```then
create:
- slug: estimate-orchestration-rechecks-a-sibling-after-a-joint-send
  ref: rule-orchestration
  kind: QA
  purpose: Whether the main agent names the Cases it sends to case-guppi at the same time as built at the same time, and, once all have answered, sends back each Case whose summary carries a Sibling line, one at a time and once, before the Cases are shown together
  method: 'by hand, after the first send of two or more Cases to case-guppi at the same time under the new Render of rule-orchestration: the prompts and messages of the main agent from that send to the showing of its Cases read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
update:
- slug: rule-orchestration
  replace:
  - old: should change instead, a line `**Other Case:**` — and the main agent writes the reply
    new: should change instead, a line `**Other Case:**`, and, when its Case rests on a Case built at the same time whose file it did not read, a line `**Sibling:**` that names that Case — and the main agent writes the reply
  - old: and every Case of the batch is shown in one reply (case 730.1).
    new: 'and every Case of the batch is shown in one reply (case 730.1). When the main agent sends two or more Cases to their `case-guppi` at the same time — the dispatch of a batch, the answers of a batch sent back, or the loop after the findings of `/pre-spec` — its prompt or message to each names each other Case of that send as built at the same time, so that `case-guppi` reads no file of it in that build (as set in case 872.2). Once every `case-guppi` of the send has answered with its Case, the main agent takes one second pass: it sends back each Case whose item in the summary carries a line `**Sibling:**`, one at a time, each after the one before has answered, with a message that the build of each Case that line names has ended, so that its `case-guppi` reads the finished files and fixes its Case against them (as set in case 872.2). The second pass runs once, a clash it leaves is left to the check of the file of `rule-case-check` and to `/pre-spec`, and the Cases of the send are shown after it, together, for one ratification (as set in case 872.2).'
  change: Cases sent at the same time name each other as built at the same time, and a second pass, one Case at a time, sends back each Case whose summary carries a Sibling line (case 872.2)
- slug: rule-prespec
  replace:
  - old: to the `case-guppi` of that Case by `SendMessage`, all of them in one message.
    new: to the `case-guppi` of that Case by `SendMessage`, all of them in one message, and name in each `SendMessage` the other Cases you send in that message as built at the same time, as `vault/wiki/orchestration.md` sets it (as set in case 872.2).
  - old: 5. Send each answer to the `case-guppi` of its Case, all in one message,
    new: 5. Send each answer to the `case-guppi` of its Case, all in one message, naming in each `SendMessage` the other Cases you send in that message as built at the same time,
  - old: 6. Send each `ask-guppi` run whose findings sent a Case back the Cases built again on them,
    new: 6. Once every `case-guppi` you sent has answered with its Case, first take the second pass that `vault/wiki/orchestration.md` sets for Cases sent at the same time, one Case at a time (as set in case 872.2). Then send each `ask-guppi` run whose findings sent a Case back the Cases built again on them,
  change: the Cases sent back after the findings and with the answers name each other as built at the same time, and the second pass of orchestration.md comes before the confirmation of ask-guppi (case 872.2)
```

```tasks
- [x] update `rule-orchestration`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [x] update `rule-prespec`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] create `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`
- [ ] read `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`
```

### Case 872.3 — The main agent sends another Case back with no question

> **given:**
> `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `rule-case-build`: the rule of `case-guppi`, which says what follows an `**Other Case:**` line.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of a round, which goes into the list of a batch.

> **when:**
> In Plan Mode, a summary of `case-guppi` carries a line `**Other Case:**` under the item of a Case, with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The main agent asks the person no question whether the other Case is built again.
> **＋** It sends the other Case to its `case-guppi` by `SendMessage` with the change the line names, and the two Cases are shown together in a batch.
> **＋** In a send of Cases built at the same time it does so after the second pass, so that a line the finished file of a sibling already answers is dropped first.
> **＋** The person agrees or not at the showing of the other Case built again.
> **＋** Where the `case-guppi` of the other Case answers with a round instead of its Case, the round stands in the list of the rounds of the batch, as any round does, and the other Case is shown once it is built.
> **－** In Work Mode the main agent still asks the person whether the other Case changes, and the change takes the way of Work Mode.

```then
update:
- slug: rule-orchestration
  replace:
  - old: is shown as it stands, and the main agent asks the person, in the shape of a question it puts itself, whether that other Case is built again, and on the person's yes sends it to its `case-guppi` by `SendMessage`, in a batch when it is ratified, as `## Showing and signing a Case` sets it (case 629.1); in a batch of items the person took up together, the question stands in the list of the batch before any Case of it is shown (case 684.1);
    new: is shown as it stands; in Plan Mode the main agent asks the person no question on it and sends that other Case to its `case-guppi` by `SendMessage` with the change the line names, in a batch, as `## Showing and signing a Case` sets it, after the second pass of a send of Cases built at the same time where one runs, so that a line the finished file of a sibling answers is dropped first, and the showing of the other Case built again is where the person agrees or not, and where its `case-guppi` answers with a round instead, the round stands in the list of the rounds of the batch, as any round does; in Work Mode it asks the person, in the shape of a question it puts itself, whether that other Case changes, and on the person's yes the change takes the way of Work Mode that `## Showing and signing a Case` sets (cases 629.1, 684.1, 872.3);
  - old: the question whether another Case is built again after a clash (case 629.1),
    new: the question in Work Mode whether another Case changes after a clash (cases 629.1, 872.3),
  change: 'in Plan Mode an Other Case line raises no question: the main agent sends the other Case back by itself, and the person agrees or not at its showing (case 872.3)'
- slug: rule-case-build
  replace:
  - old: and again on a line `**Other Case:**` under the item of your Case in the summary; the main agent asks the person whether that Case is built again (cases 637.2, 645.1).
    new: and again on a line `**Other Case:**` under the item of your Case in the summary; in Plan Mode the main agent sends that Case back to its `case-guppi` with that change, with no question to the person, and in Work Mode it asks the person first (cases 637.2, 645.1, 872.3).
  change: in Plan Mode the main agent sends the Case an Other Case line names back with no question to the person (case 872.3)
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
    method: 'by hand at the Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion; after the first summary of case-guppi in Plan Mode that carries a line Other Case under that Render: the replies of the main agent from that summary to the showing of the other Case read against the Criterion, recorded in the estimate line'
  sections:
    Criterion: |-
      When:
      The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
      **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
      **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
      **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.

      Then:
      The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
      **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
      **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
      **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
      **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
      **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands. In Plan Mode the main agent asks the person no question on it: it sends the other Case to its `case-guppi` by `SendMessage` with the change the line names, and the two Cases are shown together in a batch; in a send of Cases built at the same time it does so after the second pass that `vault/wiki/orchestration.md` sets. Where the `case-guppi` of the other Case answers with a round instead, the round stands in the list of the rounds of the batch, as any round does. In Work Mode it asks the person whether that other Case changes.
      **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
      **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
      **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
      **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
      **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
      **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
      **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
      **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
      **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
      **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
      **－** The main agent writes the heading, the list, the `ratification` and the send of another Case from the summary, and does not read the file of the Case.
      **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
      **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
      **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
      **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
      **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.
  change: the Criterion replaced whole — in Plan Mode an Other Case line raises no question, and the main agent sends the other Case back by itself
```

```tasks
- [x] update `rule-orchestration`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] update `estimate-orchestration-shows-the-built-case`
- [ ] read `estimate-orchestration-shows-the-built-case`
```

### Case 872.5 — An Other Case line of a batch raises no question

> **given:**
> `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-signs-items-taken-together`: its Criterion is replaced whole.
> **＋** `/pre-spec`: the skill of `rule-prespec`, before which a batch of items taken up together runs.

> **when:**
> In Plan Mode before `/pre-spec`, a summary of a `case-guppi` of a batch carries a line `**Other Case:**`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The line raises no question to the person in the list of the rounds of the batch.
> **＋** The other Case it names goes back to its `case-guppi` with the change the line names and joins the batch, before any Case of the batch is shown.
> **＋** In a send of Cases built at the same time, this comes after the second pass.

```then
update:
- slug: rule-orchestration
  replace:
  - old: A question whether another Case is built again, which the line `**Other Case:**` of a summary of that batch raises, stands in the list of its rounds, numbered `<Case id>.Q<n>` under the Case that raised it, before any Case of the batch is shown, and on the person's yes that other Case goes back to its `case-guppi` and joins the batch (case 684.1).
    new: 'A line `**Other Case:**` of a summary of that batch raises no question to the person: the other Case it names goes back to its `case-guppi` with the change the line names and joins the batch, before any Case of the batch is shown, after the second pass of Cases sent at the same time where one runs (as set in case 872.5).'
  change: 'an Other Case line of a batch raises no question: the other Case joins the batch by itself (case 872.5)'
- slug: estimate-orchestration-signs-items-taken-together
  set:
    status: pending
    method: 'by hand, after the first batch of items taken up together in Plan Mode under the new Render of rule-orchestration in which a summary carries a line Other Case: the replies of the main agent from the dispatch of the batch to the reply that acknowledged it read against the Criterion, recorded in the estimate line'
  sections:
    Criterion: |-
      When:
      In Plan Mode before `/pre-spec`, one answer of the person takes up two or more items of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

      Then:
      The main agent dispatches a `case-guppi` for each item, and shows no round and no Case of them alone: they are one batch.
      **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
      **＋** It shows one list of every round that came back, each question numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
      **＋** A line `**Other Case:**` in a summary of the batch raises no question to the person: the other Case it names goes back to its `case-guppi` with the change the line names and joins the batch, before any Case of the batch is shown.
      **＋** Before it shows the Cases of the batch, it takes the second pass that `vault/wiki/orchestration.md` sets for Cases sent at the same time, as `estimate-orchestration-rechecks-a-sibling-after-a-joint-send` checks.
      **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification. The person ratifies the batch at once or names the ids.
      **－** An item the person takes up alone is shown alone, and the next item waits until its Case is ratified or deferred.
      **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.
  change: the Criterion replaced whole — an Other Case line of a batch raises no question, and the other Case joins the batch by itself
```

```tasks
- [x] update `rule-orchestration`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [x] update `estimate-orchestration-signs-items-taken-together`
- [ ] read `estimate-orchestration-signs-items-taken-together`
```

### Case 872.6 — The question on another Case keeps the grill-me shape in Work Mode only

> **given:**
> `estimate-orchestration-asks-in-the-grill-me-shape`: its Criterion and `purpose` are replaced.
> **＋** `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the question shape.

> **when:**
> The main agent puts a question to the person itself in Work Mode, after a Case was bounded around a clash with another Case of the session, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The question asks whether that other Case changes, and takes the question shape of `.claude/skills/grill-me/SKILL.md`.
> **－** In Plan Mode no such question is put.

```then
update:
- slug: estimate-orchestration-asks-in-the-grill-me-shape
  set:
    status: pending
    purpose: Whether each question the main agent puts to the person itself, at pre-spec, at /hi, at a stop of Work Mode, in Work Mode after a clash on whether another Case changes, or at pre-spec on whether a finding of ask-guppi not closed is fixed or left, takes the question shape of grill-me, the exceptions kept in their own form
    method: 'by hand at the Retro of the session that changes it: the new Render of rule-orchestration in the Spec read against the Criterion, recorded in the estimate line'
  sections:
    Criterion: |-
      When:
      The main agent puts a question to the person itself, outside a round of `case-guppi`. The question is one of these:
      - a decision it needs in the report of `/pre-spec`;
      - a question at `/hi`;
      - a question at a stop of Work Mode;
      - in Work Mode, the question whether another Case of the session changes after a Case was bounded around a clash with it;
      - at `/pre-spec`, after the `ask-guppi` runs confirm their findings, the question whether each finding not closed is fixed or left.

      This is with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

      Then:
      Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
      **＋** It stands in Russian, and its labels may stand translated.
      **－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, the question whether to go on to `/pre-spec` when no line under `## Cases` is open, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.
      **－** In Plan Mode the main agent puts no question whether another Case is built again after a clash.
  change: the Criterion replaced whole — the question on another Case after a clash stands in Work Mode only
```

```tasks
- [x] update `estimate-orchestration-asks-in-the-grill-me-shape`
- [x] read `estimate-orchestration-asks-in-the-grill-me-shape`
```

### Case 872.7 — The finished Case is held against a sibling only after its build

> **given:**
> `estimate-case-build-checks-the-finished-case`: its Criterion is replaced whole.
> **＋** `estimate-case-build-reads-no-sibling-file-mid-send`: the Estimate of the hold-off, which the replaced Criterion points to.
> **＋** `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it, while its prompt or a message names another Case of the session as built at the same time.

> **then:**
> It holds its new text against the case file of that other Case only after a later message says that the build of that Case has ended.
> **－** Until then it does not name that case file in `given`.

```then
update:
- slug: estimate-case-build-checks-the-finished-case
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

      Then:
      It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
      **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
      **＋** For each field, term or command whose behaviour the Case changes, it searches the live pages of the vault, leaving out the Decision pages, and `.claude/`, for its name, and reads each hit around its line, a row of `vault/wiki/glossary.md` and the Criterion of an Estimate included; each hit that the change makes false enters the Case, or its `context` says why it stands.
      **＋** In each page the Case changes, which it has read whole, it lists each sentence that states the behaviour the change touches, judged by what the sentence says and not found by a search for the words of the sentence it changes, so that a sentence that states the same rule in other words is on the list; each sentence on that list that the change makes false enters the Case, or its `context` says why it stands.
      **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
      **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and of each Case of the session that the check of `rule-case-check` names in a finding or a note on its file, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
      **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
      **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
      **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
      **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
      **＋** In a Case with sub-cases, it lists each behaviour, field and term that a sub-case sets, reads side by side every sentence of the new texts of all its sub-cases that speaks of it, whatever page each sub-case changes, and the Case holds no contradiction between them.
      **－** A hit in a History line, in `log.md` or in `brief.md` is not read.
      **－** The case file of a Case that the prompt or a message names as built at the same time it does not read in that build and does not name in `given`; it holds its new text against that file only after a later message says that the build of that Case has ended, as `estimate-case-build-reads-no-sibling-file-mid-send` checks.
  change: the Criterion replaced whole — the finished Case is held against a Case built at the same time only after its build has ended
```

```tasks
- [x] update `estimate-case-build-checks-the-finished-case`
- [x] read `estimate-case-build-checks-the-finished-case`
```

### Case 872.8 — A batch of a ratified Case asked to change takes the second pass

> **given:**
> `estimate-orchestration-signs-a-batch-together`: its Criterion is replaced whole.
> **＋** `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`: the Estimate of the second pass, which the replaced Criterion points to.
> **＋** `rule-orchestration`: the rule of what the main agent does, rendered into `vault/wiki/orchestration.md`.
> **＋** `/pre-spec`: the skill of `rule-prespec`, before which such a batch runs.

> **when:**
> In Plan Mode before `/pre-spec`, the person's answer to a round of a `case-guppi`, or the person's word on a shown Case, asks that a Case already ratified in the session change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> Before it shows the Cases of the batch, the main agent takes the second pass that `vault/wiki/orchestration.md` sets for Cases sent at the same time.

```then
update:
- slug: estimate-orchestration-signs-a-batch-together
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      In Plan Mode before `/pre-spec`, the person's answer to a round of a `case-guppi`, or the person's word on a shown Case, asks that a Case already ratified in the session change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

      Then:
      The main agent sends the ratified Case back to its `case-guppi` by `SendMessage`, and shows neither that Case nor the Case being built alone: the two are one batch.
      **＋** A Case that a Case of the batch asks to change in the same way joins the batch.
      **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
      **＋** It shows one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
      **＋** Before it shows the Cases of the batch, it takes the second pass that `vault/wiki/orchestration.md` sets for Cases sent at the same time, as `estimate-orchestration-rechecks-a-sibling-after-a-joint-send` checks.
      **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
      **＋** The person ratifies the batch at once or names the ids. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone only when no other Case of the session is out, or in a new batch with each Case it asks to change; while another Case is out, it is shown as `estimate-orchestration-batches-cases-out-at-once` sets it.
      **－** Outside a batch and the loop after the findings of `/pre-spec`, the main agent does not take up the next item of `raw/<date>/<hi HHMM>/frontier.md` before the shown Case is ratified or deferred.
      **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.
  change: the Criterion replaced whole — the batch takes the second pass before its Cases are shown
```

```tasks
- [x] update `estimate-orchestration-signs-a-batch-together`
- [x] read `estimate-orchestration-signs-a-batch-together`
```

## Deferred

## Case 873 — The MOC form of the method of rule-estimates-schema put off

> **context:**
> The brief of the librarian of session 1712 carried the person's doubt on Case 861: whether `rule-estimates-schema` and `names_a_moc_form` of `.guppi/guppi/lint.py` let the Estimate of a MOC with no parent name `guppi test` alone. The person put it off at the close of Plan Mode of session 2104. No Case of this session sets the forms of a `method` that lint accepts on the Estimate of a MOC.

> **problem:**
> No Case of this session decides whether the Estimate of a MOC with no parent may name `guppi test` alone as its method.

```then
defer:
  - slug: rule-estimates-schema
    type: rule
    purpose: "Whether the Estimate of a MOC with no parent may name guppi test alone as its method, as names_a_moc_form of lint.py judges it; put off at the close of Plan Mode of session 2104"
```

## Case 874 — The rewrite of the sentences true only in the repository of GUPPI put off

> **context:**
> The reading of `estimate-clean-branch-ships-neutral-texts` at the /hi of session 2104 failed. Its reading line holds the sentences of eight shipped rules that hold only in the repository of GUPPI: `rule-spec-box`, `rule-vault-layout`, `rule-morph`, `rule-guppi-config`, `rule-documentation`, `rule-bash-guard`, `rule-claude-md` and `rule-permissions`. It also holds about forty shipped Estimates with such sentences. The person put the rewrite off at the close of Plan Mode of session 2104. No Case of this session rewrites them.

> **problem:**
> No Case of this session rewrites the sentences of the clean version that hold only in the repository of GUPPI.

```then
defer:
  - slug: estimate-clean-branch-ships-neutral-texts
    type: estimate
    purpose: "The rewrite of the sentences of eight shipped rules and about forty shipped Estimates that hold only in the repository of GUPPI, listed in the reading of session 2104; put off at the close of Plan Mode of session 2104"
```
