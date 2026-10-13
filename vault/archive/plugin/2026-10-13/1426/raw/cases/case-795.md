## Case 795 — The GUPPI repository becomes an entity, and a single rule needs a link

> **context:**
> A new rule page that holds one rule (a `Leaf`) gets its `parent` from the `ref` of its decision line. Case 794 created `rule-github-repository` with no `ref`, so the page has no `parent`, no page lists it, and `make lint` prints it as an orphan. The librarian's script marked the entry `incomplete: [parent]` (line 41 of `raw/2026-10-12/2349/materialize.yaml`). The check before ratification never reported it, so Case 787.1 and Case 794 both passed without a parent. That check reports by `create_lacks` of `guppi/materialize.py`, which judges only the fields of `REQUIRED`. The parent of a `Leaf` rule is judged by a second test inside `_lift_item`, which `guppi/prespec.py` does not call. The test that runs both sides leaves `parent` out on purpose. Yet `estimate-prespec-hook-reports-a-create-without-a-required-field`, now `passed`, promises a finding for every field that the lift names under `incomplete`.
>
> The person chose that no grouping rule page fits. The rules of the GUPPI repository can differ from the rules of a repository of someone who uses GUPPI, so the repository is an entity of its own, and the rule guards it. Case 795.1 creates `entity-guppi-repository` as a part of `entity-guppi`, and `rule-github-repository` names it in `applies_to`. The cascade of `guppi/generate.py` then writes the rule into the `rules` of the entity, so a live page names the rule in its frontmatter and the orphan line goes. The rule gets no `parent`, as `rule-sprint-close` has none and links only to `entity-sprint`. `rules/schema.yaml` lists `parent` as optional on a rule, and its description of the field does not make it required, so it stands. The person also chose that the check accept such a rule. In Case 795.2, a `Leaf` rule lacks its parent only when it has neither a `ref` nor an `applies_to`, and `create_lacks` judges this for both sides.
>
> Vault answer for the new slug. A Glob `vault/**/entity-*repo*.md` printed nothing, so `entity-guppi-repository` is free. The index lines of `vault/wiki/entities/` hold no page on a repository, and the tags `github`, `ci` and `git` stand in `tags.md`. `entity-guppi` carries `deferred_by` Case 616: the future shape of GUPPI is put off. Adding a part the person named does not decide that question, so the defer stands, and no line of this session's Frontier puts it up. The purpose of `entity-guppi` names its parts, and so does one sentence of its Purpose. Case 795.1 changes both. `vault/wiki/backlog.md` repeats that purpose in its Deferred line, and the librarian's `uv run guppi backlog` writes it again in the same run. A Grep `entity-guppi[^-]` over `vault/wiki/` printed `backlog.md`, `log.md`, `rules/rule-rules-schema.md`, `rules/schema.yaml`, `rules/rule-harness.md`, `rules/rule-glossary.md`, `entities/entity-sprint.md`, `entities/entity-glossary.md` and `estimates/estimate-guppi-tests-green.md`. `log.md` is not read. The rest name `entity-guppi` as the entity of `rule-harness`, as the parent of the sprint and the glossary, as the target of `estimate-guppi-tests-green`, or in an example of the field `applies_to`, and the change makes none of them false.
>
> What checks each part. `rule-github-repository` has no Estimate, and a link between pages is no promise of the rule. So by the person's answer, the orphan line is left to the `make lint` of the librarian's run, which the brief reports (case 606.1). The Estimate that already checks the change of Case 795.1 is `estimate-lint-finds-a-broken-link` of `rule-lint`. Its Criterion makes lint report a live entity, rule or estimate that no other live page names in its frontmatter as `orphan`. It also makes lint report an entity whose `rules` differs from the live rules whose `applies_to` names it. Case 795.1 changes neither judgment, only the pages lint reads, so that Criterion stands and the Estimate is not set `pending`. Case 795.2 replaces the Criterion of `estimate-prespec-hook-reports-a-create-without-a-required-field` whole and sets it `pending`. Its `purpose` and its `method` (`-k required_field`) do not state the old exception, so they stand, and the new tests carry `required_field` in their names. The Criterion carries over each line of the old one word for word, and adds the two lines on the parent of a `Leaf` rule.
>
> One judgment. A Grep `Leaf` over `guppi/` printed `guppi/casecheck.py`, `guppi/lint.py`, `guppi/materialize.py` and `guppi/prespec.py`. Only `materialize.py` judges the parent of a `Leaf`. The others name a `Leaf` in docstrings on the method of an Estimate, on a nested Estimate and on a Leaf section. A Grep `applies_to` over `guppi/` printed `guppi/generate.py`, `guppi/lint.py` and `guppi/pages.py`. Those judge the `applies_to` of live pages: the backlink `rules`, and whether it names an entity. None judges what a `create` lacks. So `create_lacks` holds the judgment, and both the lift and `check_required` call it. Pre-spec reads the `ref` of a `create` from its item or from its decision line, as the tests of the check do.
>
> Tests. A Grep `entity-guppi|guppi-repository` over `tests/` printed `tests/test_glossary.py`, which writes its pages under a temporary folder, so no test reads a page Case 795.1 changes. A Grep `kind: Leaf|"kind": "Leaf"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_casecheck.py`, `tests/test_render.py`, `tests/test_lint.py`, `tests/test_materialize.py`, `tests/test_glossary.py`, `tests/test_ratified.py`, `tests/test_guard.py`, `tests/test_generate.py`, `tests/test_pages.py` and `tests/test_prespec.py`. Of these, only `tests/test_prespec.py` passes a `Leaf` rule `create` with no `ref` to `check_required`, in the tests of the required field. Its other plans carry a `ref` on the item or on the decision line. The `Leaf` creates of `tests/test_materialize.py` keep their marks, since the lift only stops marking a rule that has an `applies_to`. The other files write live-looking pages, not `create` items.

> **problem:**
> `rule-github-repository` stands with no link from any page, so lint prints it as an orphan. The check before ratification lets a new single rule through with no parent, though the librarian's script marks it incomplete and an Estimate promises the finding.

> **recommend:**
> - **Which page should be the parent of `rule-github-repository`?**
>   - Recommended: (a) `rule-harness`, with its Purpose sentence on its members changed.
>   - Answer: none of the options fits. The rules of the GUPPI repository and the rules of the repository of someone who uses GUPPI can differ; this is more like an entity, the GUPPI repository, which has its own rules. Replaced by the question **Where should the entity of the GUPPI repository stand?**
> - **Should this Case also make the check before ratification report a missing parent?**
>   - Recommended: (b) fix the page, and close the gap in a second sub-case.
>   - Answer: (b).
> - **How is the fix of the page confirmed?**
>   - Recommended: (a) the librarian's `make lint`, with no Estimate.
>   - Answer: (a).
> - **Where should the entity of the GUPPI repository stand?**
>   - Recommended: (a) a new entity `entity-guppi-repository` under `entity-guppi`, which `rule-github-repository` names in `applies_to`.
>   - Answer: agreed, (a).
> - **Does `rule-github-repository` still need a parent rule page?**
>   - Recommended: (a) no parent rule; the link to the entity is enough.
>   - Answer: agreed, (a).
> - **What should the check before ratification report for a new single rule?**
>   - Recommended: (a) report a single rule with neither a parent nor an entity link, by one shared function.
>   - Answer: agreed, (a).

### Case 795.1 — The GUPPI repository is an entity that its rule guards

> **given:**
> `entity-guppi-repository`: the new page of the GUPPI repository on GitHub.
> **＋** `entity-guppi`: the top entity, whose parts gain the repository.
> **＋** `rule-github-repository`: the rule of the repository, which names the new entity in `applies_to`.
> **＋** `guppi/lint.py`: `make lint`, whose `orphan` finding the change clears.

> **when:**
> The librarian's run applies the decisions of this session, and its `make lint` reads `rule-github-repository`, `entity-guppi-repository` and `entity-guppi`.

> **then:**
> `make lint` prints no `orphan` line for `rule-github-repository`.
> **＋** `rule-github-repository` names `entity-guppi-repository` in `applies_to`, and `entity-guppi-repository` lists the rule in `rules`.
> **＋** `entity-guppi` lists `entity-guppi-repository` in `children`, and its `purpose` and its Purpose name the repository as one of its parts.
> **－** `rule-github-repository` gets no `parent`, and no rule page lists it in `children`.

> **tasks:**
> - [ ] create `entity-guppi-repository`
>   - ref: `entity-guppi`
>   - type: `entity`
>   - kind: `Leaf`
>   - purpose: `The repository of GUPPI on GitHub, with rules of its own that a repository of another person who uses GUPPI need not share`
>   - tags: `[github, ci, git]`
>   - sections.Purpose: `` The repository of GUPPI on GitHub, as a thing of its own. Its rules are those of `rule-github-repository`, which names this page in `applies_to`: the rulesets on `main` and `prod`, the workflow of checks, and the approval of the runs of an outside contributor. A person who uses GUPPI keeps a repository of their own, whose rules may differ, so these rules belong to this repository and not to GUPPI as a whole (case 795.1). ``
> - [ ] update `rule-github-repository`
>   - set:
>     ```
>     applies_to: [entity-guppi-repository]
>     ```
>   - change: `the rule guards entity-guppi-repository, so a live page names it (case 795.1)`
> - [ ] update `entity-guppi`
>   - set:
>     ```
>     purpose: "GUPPI as the thing this repository builds — the harness and the vault it keeps; its parts the sprint, the glossary and the repository of GUPPI on GitHub"
>     ```
>   - old: `` Its parts the person named: the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`) — the things of the vault that are content, not rules. ``
>   - new: `` Its parts the person named: the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of the vault that are content, not rules, and the repository of GUPPI on GitHub (`entity-guppi-repository`), whose rules are its own (case 795.1). ``
>   - change: `the repository of GUPPI on GitHub is a part (case 795.1)`

> **ratification:**
> ```
> - decision[case 795.1][create][entity-guppi-repository]{ref:entity-guppi}{tags:github,ci,git}
> - decision[case 795.1][update][rule-github-repository]{ref:rule-github-repository}
> - decision[case 795.1][update][entity-guppi]{ref:entity-guppi}
> ```

### Case 795.2 — Pre-spec reports a single rule created with no link

> **given:**
> `guppi/materialize.py`: `create_lacks`, the one judgment of what a `create` lacks, and `_lift_item`, which marks `incomplete` by it.
> **＋** `guppi/prespec.py`: `check_required`, which reports by `create_lacks`.
> **＋** `tests/test_prespec.py`: the tests of the required field, and the test that runs both sides over the same items.
> **＋** `estimate-prespec-hook-reports-a-create-without-a-required-field`: its Criterion is replaced whole.
> **＋** `rule-prespec-hook`: the rule whose Estimate it is.
> **＋** `rule-case-check`: its check of a case file runs `judge`.
> **＋** `rule-spec-write`: its check after ratification runs `judge`.

> **when:**
> `judge` of `guppi/prespec.py` — run by `uv run guppi prespec --check <plan> --session <id>`, by the check of a case file of `rule-case-check` or by the check after ratification of `rule-spec-write` — reads a `create` item of a page of `rules`, `entities`, `estimates` or `insights` in the `then` blocks.

> **then:**
> A `create` item that lacks a field which `guppi materialize` would name under `incomplete` gives one finding that names the Case, the slug and the missing field.
> **＋** A `create` of a rule of kind `Leaf` with no `ref`, on its item or on its decision line, and no `applies_to` lacks the field `parent`: `judge` gives its finding, and `guppi materialize` names `parent` under `incomplete`.
> **＋** A `create` of a rule of kind `Leaf` with an `applies_to` and no `ref` lacks no `parent`, on either side.
> **＋** The list of required fields and the judgment of what is missing are one function of `guppi/materialize.py`, which the lift and `guppi/prespec.py` both call.
> **＋** A field counts as present when the item writes it as a key or under `sections`, and the tags count as present when the item or its decision line carries them.
> **－** The finding never names `type`, since the lift fills it from the category.
> **－** An Estimate with no `method` gives no second finding beside the one of the form of its method.
> **－** A `defer`, an `update` or a `delete` item gives no such finding.

> **tasks:**
> - [ ] `guppi/materialize.py`: `create_lacks` takes the `ref` of the item or of its decision line, and names `parent` for a rule of kind `Leaf` with neither a `ref` nor an `applies_to`; `_lift_item` drops its own test of the parent and marks by `create_lacks` alone.
> - [ ] `guppi/prespec.py`: `check_required` passes `create_lacks` the `ref` of the item, or of the decision line of its Case and slug.
> - [ ] `tests/test_prespec.py`: the rule items of the tests of the required field that stand for another field carry a `ref`. Two new tests, their names holding `required_field`, cover a `Leaf` rule with neither a `ref` nor an `applies_to`, which gives the finding of `parent`, and one with an `applies_to` alone, which gives none. The test that runs both sides over the same items stops leaving out `parent`, and gains a `Leaf` rule with an `applies_to` and one with a `ref`.
> - [ ] update `estimate-prespec-hook-reports-a-create-without-a-required-field`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the parent of a Leaf rule, or its applies_to, is judged by create_lacks on both sides (case 795.2)`
> - [ ] read `estimate-prespec-hook-reports-a-create-without-a-required-field`

> **ratification:**
> ```
> - decision[case 795.2][update][estimate-prespec-hook-reports-a-create-without-a-required-field]{ref:rule-prespec-hook}
> ```
