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

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `` an Insight is made only by the librarian, and the format of an Insight, a Lesson or a Decision page has no status for a stand-in page (case 786). ``
>   - new: `` an Insight is made only by the librarian, and the format of an Insight, a Lesson or a Decision page has no status for a stand-in page (case 786). A `defer` of a Lesson or a Decision page writes nothing and fails as an entry too, whether the page stands or not, since neither format has `deferred_by` and no list would show the item (as set in case 865). ``
>   - change: `a defer of a Lesson or a Decision page fails as an entry, whether the page stands or not (case 865)`
> - [ ] `.guppi/guppi/materialize.py`: `DEFERRABLE`, the folders `rules`, `entities`, `insights` and `estimates`, moved here from `.guppi/guppi/generate.py`; a predicate `defers_a_record(slug)`, true when `category_of(slug)` is a folder of `CATEGORIES` outside `DEFERRABLE`; a constant `DEFER_OF_A_RECORD`, the text `a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it`; the docstring of the predicate names `.guppi/guppi/generate.py`, `.guppi/guppi/prespec.py`, `.guppi/guppi/ratified.py` and `.guppi/guppi/ledger.py` as the modules that import it; the line `defer existing` of the routing table says that a Lesson or a Decision page is refused (case 865).
> - [ ] `.guppi/guppi/generate.py`: imports `DEFERRABLE`, `defers_a_record` and `DEFER_OF_A_RECORD` from `.guppi/guppi/materialize.py` in place of its own constant; in `defer`, an entry for which `defers_a_record` is true fails first, before `defer_writes_no_page` and before any page is read, with `DEFER_OF_A_RECORD`, and no page or `log.md` line is written; the module docstring and the docstring of `defer` say so (case 865).
> - [ ] `.guppi/tests/test_generate.py`: a `defer` of a live Decision page, of a Decision page under `vault/archive/`, of a live Lesson and of a Decision page with no page each changes no page, prints `generate: <slug>: ` and `DEFER_OF_A_RECORD` on stderr, exits 1 and lets the other entries apply; a `defer` of a rule, an entity, an Insight and an Estimate that stand still appends to `deferred_by`; `generate.defers_a_record` is `materialize.defers_a_record` and `generate.DEFERRABLE` is `materialize.DEFERRABLE`; for each folder of `CATEGORIES`, the live `vault/wiki/<folder>/schema.yaml` lists `deferred_by` among its optional properties exactly when the folder is in `DEFERRABLE`.
> - [ ] update `estimate-generate-writes`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a defer of a Lesson or a Decision page fails alone, whether the page stands or not`
> - [ ] read `estimate-generate-writes`

> **ratification:**
> ```
> - decision[case 865.1][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 865.1][update][estimate-generate-writes]{ref:rule-page-generation}
> ```

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

> **tasks:**
> - [ ] `.guppi/guppi/prespec.py`: `check_form` judges each `defer` item whose slug has a category by `materialize.defers_a_record` first, imported, and reports `case N: defer <slug>: ` and `materialize.DEFER_OF_A_RECORD`; only an item it does not report goes on to `defer_writes_no_page`; the module docstring and the docstring of `check_form` say that a `defer` of a Lesson or a Decision page is a finding whether its page stands or not, and that the finding of a page that does not stand covers an Estimate and an Insight (case 865).
> - [ ] `.guppi/tests/test_prespec.py`: a `defer` of a live Decision page, of a Decision page under `vault/archive/` and of a live Lesson, under a Case heading and under `## Deferred`, each gives the new finding; a `defer` of a Lesson with no page gives the new finding alone; a `defer` of an Insight with no page still gives `NO_DEFERRED_PAGE`; a `defer` of a rule, an entity, an Insight and an Estimate that stand gives none; `prespec.defers_a_record` is `materialize.defers_a_record`.
> - [ ] update `estimate-prespec-checks-the-form-of-an-item`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a defer of a Lesson or a Decision page is a finding, whether the page stands or not`
> - [ ] read `estimate-prespec-checks-the-form-of-an-item`

> **ratification:**
> ```
> - decision[case 865.2][update][estimate-prespec-checks-the-form-of-an-item]{ref:rule-prespec}
> ```

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

> **tasks:**
> - [ ] update `rule-spec-write`
>   - old: `` a key of a `defer` item that `item_keys` of `.guppi/guppi/materialize.py` does not give a `defer` of its category is refused, exit 2, and nothing of the Case is written (case 436.3); ``
>   - new: `` a key of a `defer` item that `item_keys` of `.guppi/guppi/materialize.py` does not give a `defer` of its category is refused, exit 2, and nothing of the Case is written (case 436.3); so is a `defer` line of the Case whose slug names a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, since neither page carries `deferred_by` and no list would show the item (as set in case 865); ``
>   - change: `the hook refuses a short defer of a Lesson or a Decision page (case 865)`
> - [ ] update `rule-orchestration`
>   - old: `` A `defer` of an Insight, a Lesson or a Decision page names a page that stands too, since only a rule or an entity gets a placeholder page, and `/pre-spec` reports one with no page; the agent fixes that finding the same way, with a new short Case with `{supersedes:case N}` whose `defer` names a page that stands (case 786). ``
>   - new: `` A `defer` of an Insight names a page that stands too, since only a rule or an entity gets a placeholder page, and `/pre-spec` reports one with no page; the agent fixes that finding the same way, with a new short Case with `{supersedes:case N}` whose `defer` names a page that stands (case 786). A `defer` never names a Lesson or a Decision page, since neither carries `deferred_by` and no list would show the item: the `Stop` hooks of `rule-spec-write` and `rule-ledger-write` refuse such a short Case and its line at the reply that carries them, `/pre-spec` reports it and `guppi generate` fails it, and the agent writes the defer again on the rule or entity page whose change would settle the matter (as set in case 865). ``
>   - change: `a defer never names a Lesson or a Decision page; the hooks refuse it at the reply that carries it (case 865)`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] `.guppi/guppi/ratified.py`: `deferred_section` refuses Case N when a `defer` line of the reply of Case N has a slug for which `materialize.defers_a_record`, imported, is true, before it reads the `then` block, with `case N: defer <slug>: ` and `materialize.DEFER_OF_A_RECORD`, and writes nothing of the Case; the paragraph `The defer` of the module docstring says so (case 865).
> - [ ] `.guppi/tests/test_ratified.py`: a reply with a short defer of a live Decision page, and one of a Lesson with no page, gets the error and leaves the plan file unchanged; a short defer of an entity in the same reply as a refused one is still written; `ratified.defers_a_record` is `materialize.defers_a_record`.
> - [ ] `uv run --project .guppi pytest .guppi/tests/test_orchestration.py`: the short-form example of `vault/wiki/orchestration.md` still passes the hook.
> - [ ] update `estimate-spec-write-writes-a-defer`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a short defer of a Lesson or a Decision page is refused and not written`
> - [ ] read `estimate-spec-write-writes-a-defer`

> **ratification:**
> ```
> - decision[case 865.3][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 865.3][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 865.3][update][estimate-spec-write-writes-a-defer]{ref:rule-spec-write}
> ```

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

> **tasks:**
> - [ ] create `estimate-ledger-write-refuses-a-defer-of-a-record`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook refuses a defer line of a Lesson or a Decision page, so that no defer lands where no list shows it`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ledger.py -k record`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] update `rule-ledger-write`
>   - old: `` so a record with a broken opening is not lost unseen (case 695.1). ``
>   - new: `` so a record with a broken opening is not lost unseen (case 695.1). It refuses a `defer` decision line whose slug names a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, in any text of the transcript, with one stderr line when the line stands in the reply just finished, which asks for a defer of the rule or entity page whose change settles the matter, since neither page carries `deferred_by` and no list would show the item (as set in case 865). ``
>   - change: `the hook refuses a defer line of a Lesson or a Decision page (case 865)`
> - [ ] `.guppi/guppi/ledger.py`: a function `refused_defers(fresh)`, the fresh decision lines of kind `defer`, read by `materialize.parse_line`, whose slug `materialize.defers_a_record` judges true, both imported inside the function; `run` leaves them out of the lines it writes and prints `ledger: line not written — <body>: ` and `materialize.DEFER_OF_A_RECORD` for each that stands in the reply just finished, told once a stretch by `untold`; the module docstring says so (case 865).
> - [ ] `.guppi/tests/test_ledger.py`: a reply whose block holds a `defer` line of a live Decision page, of a Lesson with no page and of a rule writes the line of the rule alone, prints the refusal for the two others and exits 2; the same lines in an earlier text land neither, with no stderr line; one test runs `ledger.refused_defers` and `ratified.write_defers` over the same short defer of a Decision page, and over one of a rule, and asserts that both refuse the first and pass the second.
> - [ ] read `estimate-ledger-write-refuses-a-defer-of-a-record`

> **ratification:**
> ```
> - decision[case 865.4][create][estimate-ledger-write-refuses-a-defer-of-a-record]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> - decision[case 865.4][update][rule-ledger-write]{ref:rule-ledger-write}
> ```
