## Case 931 — A page update drops a section

> **context:**
> `guppi generate` applies a page `update` by its keys `set`, `sections`, `replace`, `reword`, `change` and `rename`. None of them removes a section: `Generator.update` of `.guppi/guppi/generate.py` sets a named section's text, and `body` of the same module writes a section with no text as a bare heading. The schema of rules says a Leaf that still carries `## How it works` keeps it until its next touch, when the section leaves, but no form of an `update` makes it leave. Case 792 asked for such a form and was put off by case 793 when Case 787.2 could only change one sentence of that section on `rule-git-context`; case 897.3 took the put-off up and put it off again, and `rule-page-generation` holds it in `deferred_by`. A Grep of `^## How it works` over `vault/wiki` printed 15 rule pages; 11 of them are Leafs. The person chose a new `update` key, `drop`, with a list of section names, joined to `ITEM_KEYS` of `.guppi/guppi/materialize.py`, the one list of update keys: `_lift_item` copies each key of it into the entry, `item_keys` gives it for an `update`, and `put` of `.guppi/guppi/ratified.py` reads a sub-point whose value opens with `[` as a YAML list, so a sub-point `drop` reaches the entry with no other change to the reader. A name the page does not carry fails the entry, as a `replace` that misses does. A section that the schema of the page's category requires fails the entry too. That judgment already stands in `check_schema` of `.guppi/guppi/lint.py`, with `unmet_conditions`, `holds` and `load_schema`, which I read whole: it reports each section of `body.required` the page lacks, and each `required` section of a `conditional` of `body` whose `when` holds on the page's fields, such as `## Render` on a rule with `enforcement: render`. `generate.py` already imports from `lint.py`, so the task runs `check_schema` over the page with the section and without it, and adds no second copy of the judgment; `lint.py` does not change, which keeps Case 927 true, whose `then` says `lint.py` does not change. The key cannot be used in this session, since the check of a Case file runs the code that stands before Work Mode; the 11 Leafs keep the section until a later Case drops it, so the schema sentence on the next touch stands, now with a form behind it. A Grep of `next touch` over the repository outside `vault/raw` and `vault/archive` printed `vault/wiki/rules/rule-rules-schema.md` and `vault/wiki/rules/schema.yaml`; both say the section leaves at the next touch, which this Case makes possible, so both stand. The change is checked by `estimate-generate-writes`, which states what an `update` writes; its last line says a section the entry does not name under `sections` or reach by `replace` is not touched, which `drop` makes false, so its Criterion is replaced whole under `sections.Criterion`, with the lines of this Case's `then` in it; its `purpose` and `method` stand. The other Estimates of `rule-page-generation` speak of reword, rename, ticks, the cascade, the Decision page, dates, the leading indent and the failure of an entry in general, and stand. A Grep of `` `rename` `` over `vault/wiki` printed 11 files: `glossary.md`, `case-schema.md`, `entity-glossary.md`, `rule-page-generation.md`, `rule-case-protocol.md`, `rule-decisions-schema.md`, `rule-materialize.md`, `estimate-generate-renames.md`, `estimate-materialize-assembles.md`, `estimate-prespec-requires-a-task-line.md` and `estimate-spec-write-copies-the-ratified-case.md`. The pair on `rule-case-protocol` stands in one sentence of its Render, which I read whole: it names each key an `update` holds, `set`, `sections`, `replace`, `reword`, `change` and `rename`, each with its rule, and the pair adds `drop` with its rule between `change` and `rename`. The second pair, asked by a finding of `/pre-spec`, stands in the sentence of the same Render that I read whole: the Spec keeps its form, and the hook of `rule-spec-write` reads the chat form, a task line of a kind and a slug being an item and its sub-points its keys, each value one code span or a fenced block; the pair adds `drop` to that list of sub-point keys, which `put` reads as a YAML list. Cases 927 and 928 write into neither page this Case changes. The later sentence of that paragraph, that an `update` naming a part alone, such as a `replace` pair or a section other than `Criterion`, carries no `set.status`, stands: a `drop` is such a part, and a `drop` of `Criterion` fails, since the schema of Estimates requires it. The new Criterion of `estimate-generate-writes` carries each line of the old one word for word but two: the line that a section the entry does not name under `sections` or reach by `replace` is not touched now names `drop` beside `sections`, since a `drop` touches a section it names; and the line that an `update` of an Estimate whose `set` carries `method` drops no section now says that such a `set` removes no section by itself, as a finding of `/pre-spec` asked, since an item that carries both `set.method` and `drop` removes the sections `drop` names, and the old word "drops" would clash with the key; it adds the lines of this Case's `then` on `drop`, after the line on what an `update` applies and among the `－` lines. Of the other files the Grep of `` `rename` `` printed, each stands: the glossary row and `entity-glossary.md` name the kinds of decision, not every key; `rule-materialize.md` and `estimate-materialize-assembles.md` list keys the lift carries, and Case 935, whose finished file I read whole, adds `drop` to both in Case 935.1; its Case 935.2 makes `drop` a named part of an Estimate `update` and marks one whose `drop` names `Criterion` as `incomplete: [criterion]` at the lift, which agrees with this Case, where `generate` fails such a `drop` since the schema of Estimates requires `## Criterion`, and its tasks run after this Case adds `drop` to `ITEM_KEYS`, as its `context` says: by the person's choice the promise that the lift carries `drop` stands on `estimate-materialize-assembles` alone, so this Case keeps no line of it in its `then` or in the Criterion of `estimate-generate-writes`, and keeps the change of `ITEM_KEYS` in its tasks, since `Generator.update` reads that list; `estimate-spec-write-copies-the-ratified-case.md` refuses only a sub-point outside `item_keys`, which will hold `drop`; `rule-decisions-schema.md`, `estimate-generate-renames.md` and `estimate-prespec-requires-a-task-line.md` speak of `rename` alone. A Grep of `rule-page-generation|estimate-generate-writes|ITEM_KEYS|item_keys` over `.guppi/tests` printed `test_materialize.py`, `test_generate.py` and `test_prespec.py`; none reads a live page, and `test_item_keys_answers_for_each_kind_as_the_lift_does` of `test_materialize.py` asserts the set of update keys, which a task changes. The update of `rule-page-generation` carries `{supersedes:case 897.3}`, which clears the put-off and closes the backlog line; as with cases 793 and 839, which case 897.3 superseded, the Decision page of case 897.3 becomes `superseded`. The session's ledger holds no `error` lesson. By the sentence of the prompt, Case 929 changes `rule-guppi-config`, the defers of `rule-guppi-package` and `estimate-guppi-config-runs-the-test-and-style-commands`, no page this Case changes; Cases 929 and 932 are built at the same time as this one, and I read no file of them.

> **problem:**
> No form of a page `update` removes a section, so a Leaf rule cannot lose `## How it works` at its next touch without an edit by hand, and `rule-page-generation` carries the put-off of that form.

> **recommend:**
> - **What does this Case do with the put-off?**
>   - Recommended: (a) a new update key that names the sections to remove.
>   - Answer: (a).
> - **Which sections may the new key remove?**
>   - Recommended: (a) any section except the ones the page's schema requires.
>   - Answer: agreed, (a).
> - **What happens when a named section is not on the page?**
>   - Recommended: (a) the entry fails.
>   - Answer: agreed, (a).
> - **How is the new key checked?**
>   - Recommended: (b) the Criterion of `estimate-generate-writes` replaced as a whole.
>   - Answer: agreed, (b).
> - **What is the key called?**
>   - Recommended: (a) `drop`.
>   - Answer: agreed, (a).
> - **Where does the promise that the lift carries `drop` stand?**
>   - Recommended: (b) a new Case beside Case 931 carries the lift.
>   - Answer: agreed, (b).

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, which carries the put-off.
> **＋** `estimate-generate-writes`: the Estimate of what an `update` writes; its Criterion is replaced whole.
> **＋** `rule-case-protocol`: its Render, `vault/wiki/case-schema.md`, lists what an `update` holds.
> **＋** `.guppi/guppi/generate.py`: `Generator.update` applies the new key.
> **＋** `.guppi/guppi/materialize.py`: `ITEM_KEYS`, the one list of update keys.
> **＋** `.guppi/guppi/lint.py`: `check_schema`, the judgment of the sections a schema requires.
> **＋** `.guppi/guppi/ratified.py`: the `Stop` hook of `rule-spec-write`, which reads the sub-points of a task line.
> **＋** `.guppi/tests/test_generate.py`, `.guppi/tests/test_materialize.py` and `.guppi/tests/test_ratified.py`: the tests of the new key.

> **when:**
> `guppi generate` applies an `update` entry whose item carries `drop`, a list of section names, to a page.

> **then:**
> Each section that `drop` names leaves the page, its heading and its text, and the page gets the History line `updated: <change>`; an item that carries `drop` alone applies.
> **－** A name of a section the page does not carry fails the entry alone, with the name on stderr, and nothing of `set`, `sections`, `replace` or `drop` of the item is written to the page.
> **－** A name of a section that the schema of the page's category requires of the page fails the entry the same way: `check_schema` of `.guppi/guppi/lint.py`, run over the page with the section and without it, gives a finding without it that it does not give with it.
> **－** A section that `drop` does not name is not touched.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `too (as set in case 819). One bad`
>   - new: `` too (as set in case 819). An `update` whose item carries `drop`, a list of section names, removes each named section, its heading and its text; a name the page does not carry, or a section that the schema of the page's category requires of the page, fails the entry, and nothing of the item is written to the page (as set in case 931). One bad ``
>   - change: `an update drops a named section, heading and text; a section the page lacks or its schema requires fails the entry; the put-off of case 897.3 taken up`
> - [ ] update `estimate-generate-writes`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     `guppi generate` applies one entry of a yaml to a page.
>
>     Then:
>     A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the `sprint` of the yaml, which `guppi materialize` takes from the first `## <id>` of `sprint.md` or, in a unit whose ledger creates `entity-sprint-<id>`, from that `<id>`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
>     **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`, and `deferred_by` after `checked` once a `defer` marks it; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
>     **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
>     **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
>     **＋** An `update` whose item carries `drop`, a list of section names, removes each section it names from the page, its heading and its text; an item that carries `drop` alone applies.
>     **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
>     **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
>     **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
>     **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight, estimate) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by` for a rule or an entity only.
>     **＋** The folders whose page takes `deferred_by` are `DEFERRABLE` of `.guppi/guppi/materialize.py`, which `.guppi/guppi/generate.py` imports; they are the folders whose `schema.yaml` under `vault/wiki/` lists `deferred_by`.
>     **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
>     **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
>     **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
>     **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
>     **－** A name under `drop` of a section the page does not carry fails the entry alone (`estimate-generate-fails-alone`), with the name on stderr, and nothing of `set`, `sections`, `replace` or `drop` of the item is written to the page.
>     **－** A name under `drop` of a section that the schema of the page's category requires of the page fails the entry the same way: `check_schema` of `.guppi/guppi/lint.py`, run over the page with the section and without it, gives a finding without it that it does not give with it.
>     **－** A `defer` of a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, whether its page stands or not, changes no page and appends nothing to `vault/wiki/log.md`: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it` on stderr.
>     **－** A `defer` of an Estimate or an Insight whose page stands neither under `vault/wiki/<category>/` nor in a folder `<category>` under `vault/archive/` outside a `raw/` folder, by `defer_writes_no_page` of `.guppi/guppi/materialize.py`, which asks `has_page`, writes no page: the entry fails alone (`estimate-generate-fails-alone`), with `generate: <slug>: an Estimate is deferred only with its page — defer the page it would check` on stderr for an Estimate, and `generate: <slug>: a placeholder is written only for a rule or an entity — defer a page that stands` for an Insight.
>     **－** No body section is derived from a ref field; a section the entry does not name under `sections` or `drop`, or reach by `replace`, is not touched.
>     **－** The `set` of an `update` of an Estimate that carries `method` removes no section by itself.
>     **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).
>     ```
>   - change: `the Criterion replaced whole — an update drops a named section, and a section the page lacks or its schema requires fails the entry`
> - [ ] update `rule-case-protocol`
>   - old: `` `change` (one line for History) and, when the page changes its slug, `rename` ``
>   - new: `` `change` (one line for History), `drop` (a list of section names, each removed with its heading and its text; a name the page does not carry, or a section that the schema of the page's category requires of the page, fails the entry) and, when the page changes its slug, `rename` ``
>   - old: `` `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` ``
>   - new: `` `set`, `change`, `rename`, `drop`, `sections.<Name>`, the fields of a `create` ``
>   - change: `an update holds drop, a list of sections to remove, and the hook of rule-spec-write reads it as a sub-point`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
> - [ ] `.guppi/guppi/materialize.py`: `drop` joins `ITEM_KEYS["update"]`, and the comment above it names it.
> - [ ] `.guppi/guppi/generate.py`: `Generator.update` applies `drop` after `set`, `sections` and `replace` of the item and before `save`; for each name it fails the entry with `generate: <slug>: drop: <name> is not on the page`, or with `generate: <slug>: drop: <name> is required by the schema`, when `check_schema` of `.guppi/guppi/lint.py`, imported with `load_schema`, gives over a copy of the page without the section a finding it does not give over the page; a failure returns before `save`. The module docstring names `drop` beside `replace`.
> - [ ] `.guppi/guppi/ratified.py`: the docstring that lists the sub-points of an item names `drop`.
> - [ ] `.guppi/tests/test_generate.py`: tests that a `drop` of `How it works` on a Leaf removes the heading and the text and writes History `updated: <change>`; that an item with `drop` alone applies; that a name the page lacks fails the entry and leaves the page as it was; that `drop` of `Purpose` on a rule, of `Render` on a rule with `enforcement: render`, and of `Criterion` on an Estimate each fail the entry; that `drop` of `Render` on a rule with `enforcement: check` applies.
> - [ ] `.guppi/tests/test_materialize.py`: `test_item_keys_answers_for_each_kind_as_the_lift_does` holds `drop` among the update keys.
> - [ ] `.guppi/tests/test_ratified.py`: a test that `read_tasks` reads a sub-point `drop` with the value `[How it works]` of an update item into the list `["How it works"]`, with no error.
> - [ ] read `estimate-generate-writes`

> **ratification:**
> ```
> - decision[case 931][update][rule-page-generation]{ref:rule-page-generation}{supersedes:case 897.3}
> - decision[case 931][update][estimate-generate-writes]{ref:rule-page-generation}
> - decision[case 931][update][rule-case-protocol]{ref:rule-case-protocol}
> ```
