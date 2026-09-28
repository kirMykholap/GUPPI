## Case 489 — Slice 3g: the Estimates of `generate` and `materialize` recut to `When:` and `Then:`

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds the five Estimates of `rule-page-generation` and the two of `rule-materialize` that still have `Given:`. Two of them lost their promise by a fault of the tools. Case 211.1 wrote a new Criterion for `estimate-generate-writes`: the text of case 201.1 plus one line on `set.method`. Case 211.3 then set a `method` field on both `estimate-generate-writes` and `estimate-generate-walks-dates`. The scripts of that day replaced the whole Criterion of each page with the `when` and `then` of 211.3, which was a one-time job on five named pages. So the 211.1 text never stood on the page, and the 201.5 text of `estimate-generate-walks-dates` was lost. No decision chose this. Since case 378.4, an `update` that names only a field leaves the Criterion alone.
> The person decided in three rounds. The item goes in seven Cases by area, one group per Case. The pages that record a one-time act get a real promise, and a page with no `purpose` gets one in the same change. This group is the second, after case 488. For the two lost promises the person chose to restore the ratified text, checked against the code of today. The main agent read the text of 211.1 in the archived Spec of session 2238 and the text of 201.5 at the librarian's commit of session 1955. The person also chose to keep `estimate-generate-writes` as one page, although its `Then:` holds 11 `＋` lines, with no split and no backlog item. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. On 489.1 and 489.2 it compares with the 211.3 text on the page, which this Case replaces on purpose. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. A `Given:` line that states behaviour of the step moves into `When:` or `Then:`. 489.1 restores the 211.1 text word for word. It drops only "The Decision page, the failure of an entry and the cascade are three other Estimates", because that is a pointer to other pages. Every other line was read against the docstring and the code of `guppi/generate.py`, and none is contradicted. The drop of `## Context` and `## Method` on `set.method` still runs in `update`. 489.2 restores the 201.5 text word for word. `run` and `generate_date` hold each line. 489.3 moves the `rename` key and the category prefix into `When:` and `Then:`. It drops "`guppi sprint` redraws `sprint.md`", because that is another script, and it drops the collision of a `create`, which 489.1 promises ("any other existing page is a collision"). 489.4 moves the owner and the whole-word boundary into `Then:`. The owner's text now also counts the field `purpose`, as `reword_pairs` compares it. It drops "the Rule-class files", which no longer exist, and the line that a slug goes through `rename`, which is advice and no behaviour of the step. 489.5 keeps its lines and names the `guppi lint` finding in place of "(305.5)". 489.6 turns "as before" into the lift by the `schema.yaml` on disk that the old `Given:` stated. 489.7 keeps its `Then:` word for word and moves the fold of a reading into `When:`.
> The check of the answer also notes that a `then` line of 489.4 shares words with 489.3. This is expected. Both steps walk the live pages and replace a whole word outside History and Result. 489.3 moves a page and follows its slug into links and ref fields, and 489.4 replaces a word that is not a slug, and the owner page must carry the new word. They are two promises, each with its own test.
> The frame. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. `rule-page-generation` carries `deferred_by` for case 469. No open Frontier line of this session names it, and this Case changes only its Estimates, so the backlog item stands. The other Estimates of `rule-page-generation` (`-cascades`, `-fails-alone`, `-ticks-the-spec`, `-writes-the-decision-page`, `-writes-the-given`) and of `rule-materialize` are already in the new layout and speak of other steps, so they are not touched. 489.1 names `estimate-generate-fails-alone` as the promise of an entry that fails, and does not change it. The sentence of `rule-estimates-schema` on `Given:` "until the one pass of its migration" stays true. The Case creates no page, so no vault query was run. Not done: the other five groups (24 pages), and the split of `estimate-generate-writes`, which the person declined.

> **problem:**
> The seven Estimates of `generate` and `materialize` still open with `Given:`. Two of them promise a one-time job in place of the promise the person ratified, which the tools overwrote. So their readings check stale text, or nothing that can happen again.

> **recommend:**
> Replace each Criterion whole with only `When:` and `Then:`: restore the two lost texts as ratified, less the one pointer line, and recut the other five from their own lines, read against the code. Writing the two lost promises new from the code was rejected, because the ratified text still holds line by line.

### Case 489.1 — What `generate` writes for one entry

> **given:**
> `estimate-generate-writes` — the promise, its Criterion restored and replaced whole
> **＋** `rule-page-generation` — the rule it promises for
> **＋** `guppi/generate.py` — `Vault` and its steps per kind of entry
> **＋** `vault/wiki/` — the live pages written
> **＋** `vault/archive/` — where an entry finds a page not under `vault/wiki/`
> **＋** `raw/` — the session folders inside the archive, which the search passes by
> **＋** `estimate-generate-fails-alone` — the promise of an entry that fails, named and not changed
> **＋** `tests/test_generate.py` — the tests the reading runs

> **when:**
> `guppi generate` applies one entry of a yaml to a page.

> **then:**
> A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the first `## <id>` of `sprint.md`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
> **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
> **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
> **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
> **＋** An `update` of an Estimate whose `set` carries `method` writes the field after `purpose` and drops `## Context` and `## Method` where the page carries them — the field replaces the section, the Case is reached by `origin`; an `update` without `set.method` touches no section (case 211.1).
> **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
> **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
> **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
> **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by`.
> **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
> **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
> **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
> **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
> **－** No body section is derived from a ref field; a section a page still carries is not touched, except the two `set.method` drops.
> **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

> **tasks:**
> - [ ] update `estimate-generate-writes`
>   - set: `{status: pending, purpose: "What generate writes to a page for each kind of entry of a materialize.yaml, and nothing an entry does not carry"}`
>   - change: `the Criterion restored whole — the text of case 211.1, which case 211.3 overwrote, less its pointer line; purpose set (case 489.1)`
> - [ ] read `estimate-generate-writes` — `pytest tests/test_generate.py`, then by hand at a later librarian's run

> **ratification:**
> ```
> - decision[case 489.1][update][estimate-generate-writes]{ref:estimate-generate-writes}
> ```

### Case 489.2 — The walk of `generate` over the units, dates ascending

> **given:**
> `estimate-generate-walks-dates` — the promise, its Criterion restored and replaced whole
> **＋** `rule-page-generation` — the rule it promises for
> **＋** `guppi/generate.py` — `run` and `generate_date`, the walk and one unit
> **＋** `guppi/materialize.py` — `units_with`, the units that have a yaml
> **＋** `vault/raw/<date>/materialize.yaml` — the date-level yaml
> **＋** `vault/raw/<date>/<HHMM>/materialize.yaml` — the yaml of a session
> **＋** `tests/test_generate.py` — the tests the reading runs

> **when:**
> `uv run guppi generate` runs, with `--date` or without.

> **then:**
> Without `--date` every unit under `vault/raw/` with a `materialize.yaml` is applied: the date-level yaml `vault/raw/<date>/materialize.yaml` first, then `vault/raw/<date>/<HHMM>/materialize.yaml` in folder order, dates ascending; `--date` walks the units of that date alone.
> **＋** A unit with no unapplied entry changes no page; stdout carries one line per unit, `generate: <unit>: N page(s) written or changed`.
> **＋** A failure on one unit is printed, the walk goes on, the exit code is 1 at the end.
> **＋** A `--date` without a yaml is named on stderr, exit 1; no yaml anywhere — one line on stderr, exit 1.
> **－** A unit `materialize` passed by (`carry.md`) has no yaml and is not walked.

> **tasks:**
> - [ ] update `estimate-generate-walks-dates`
>   - set: `{status: pending, purpose: "generate applies every unit under raw/ that has a yaml, dates ascending, and a failing unit does not stop the walk"}`
>   - change: `the Criterion restored whole — the text of case 201.5, which case 211.3 overwrote; purpose set (case 489.2)`
> - [ ] read `estimate-generate-walks-dates` — `pytest tests/test_generate.py`, then by hand at a later librarian's run

> **ratification:**
> ```
> - decision[case 489.2][update][estimate-generate-walks-dates]{ref:estimate-generate-walks-dates}
> ```

### Case 489.3 — A `rename` moves the page and every link to it

> **given:**
> `estimate-generate-renames` — the promise, its Criterion replaced whole
> **＋** `rule-page-generation` — the rule it promises for
> **＋** `guppi/generate.py` — `rename`, the move and the walk of the links
> **＋** `vault/wiki/` — the live pages whose links follow
> **＋** `vault/archive/` — the archive, left as it is
> **＋** `vault/raw/` — the session folders, left as they are
> **＋** `tests/test_generate.py` — the tests the reading runs

> **when:**
> `guppi generate` applies an `update` entry whose item carries `rename: <new slug>`, beside `set`, `sections`, `replace` or `change`, and the ledger line names the old slug.

> **then:**
> The file of the page moves from `<old>.md` to `<new>.md` in its category folder, and the new slug carries the same category prefix. The page's History gets "renamed from `<old>` · `[[decision-case-N]]`", and the item's `set`, `sections` and `replace` apply to the new file.
> **＋** In every live page of `vault/wiki/`, Decision pages included, every `[[old]]` becomes `[[new]]`, every `REF_FIELDS` value holding the old slug becomes the new one, and the old slug as a whole word in the body outside `## History` and `## Result` becomes the new one. Every page touched, Decision pages excepted, gets the History line "ref `<old>` → `<new>` · `[[decision-case-N]]`".
> **＋** The Decision page of the Case is written by the slug of the ledger line, before the entries, and the walk retargets its link like any other.
> **＋** The order of application is the order of the yaml: an `update` of the same page from an earlier Case lands on the old file, and the `rename` moves it with the page.
> **－** A taken slug, live or archived, or a foreign prefix: the entry is `failed`, and nothing is moved.
> **－** `origin`, `## History` and `## Result` of any page, `vault/archive/`, `vault/raw/`, `log.md` and `brief.md` are untouched.

> **tasks:**
> - [ ] update `estimate-generate-renames`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the line on guppi sprint out (case 489.3)`
> - [ ] read `estimate-generate-renames` — `pytest tests/test_generate.py`, then by hand at the librarian's run that applies a later rename

> **ratification:**
> ```
> - decision[case 489.3][update][estimate-generate-renames]{ref:estimate-generate-renames}
> ```

### Case 489.4 — A `reword` replaces a word on every live page

> **given:**
> `estimate-generate-rewords` — the promise, its Criterion replaced whole
> **＋** `rule-page-generation` — the rule it promises for
> **＋** `guppi/generate.py` — `reword_pairs`, the owner check and the walk
> **＋** `vault/wiki/` — the live pages the pairs reach
> **＋** `vault/archive/` — the archive, left as it is
> **＋** `vault/raw/` — the session folders, left as they are
> **＋** `tests/test_generate.py` — the tests the reading runs

> **when:**
> `guppi generate` applies an `update` entry whose item carries `reword`, a list of `{old, new}` pairs.

> **then:**
> Every pair is replaced as a whole word, with no letter, digit, `_` or `-` right before or after it. The replace runs on every live page of the folders `rules`, `entities` and `estimates` of `vault/wiki/`, in every section but History and Result and in the fields `purpose` and `method`. Each page touched gets one History line `reworded: old → new · [[decision-case-N]]`, and stdout has one line per page with the count.
> **＋** The other keys of the item — `set`, `replace`, `sections`, `change` — apply to the page itself as before; an item that carries `reword` alone is content and applies.
> **－** A pair with no hit on any live page fails the entry with the reason, and so does a pair whose `new` is absent from the text of the page of the item: its `purpose`, `governs`, `implementation_ref`, Purpose and Render, compared without regard to case. Nothing is applied.
> **－** The Decision pages, the lessons and the Insights, `vault/archive/`, `vault/raw/`, `log.md`, `brief.md` and `sprint.md` are not touched; the status of no Estimate changes.

> **tasks:**
> - [ ] update `estimate-generate-rewords`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the Rule-class files out (case 489.4)`
> - [ ] read `estimate-generate-rewords` — `pytest tests/test_generate.py`, then by hand at the librarian's run that applies a later reword

> **ratification:**
> ```
> - decision[case 489.4][update][estimate-generate-rewords]{ref:estimate-generate-rewords}
> ```

### Case 489.5 — The `rules` of an Entity from the `applies_to` of the live rules

> **given:**
> `estimate-generate-writes-rules-from-applies-to` — the promise, its Criterion replaced whole
> **＋** `rule-page-generation` — the rule it promises for
> **＋** `guppi/generate.py` — the cascade after the entries
> **＋** `guppi/lint.py` — the finding on an `applies_to` that names no live Entity
> **＋** `vault/wiki/` — the live pages the cascade reads and writes
> **＋** `tests/test_generate.py` — the tests the reading runs

> **when:**
> `guppi generate` has applied the entries of a yaml and runs the cascade over the live pages of `vault/wiki/`.

> **then:**
> The `rules` of every live Entity is the slugs of the live rules whose `applies_to` names it, in slug order; the field is written when the list is not empty or the field already stands; a change is a History line `rules: [...] · cascade`; an empty list on a page without the field writes no field.
> **＋** A rule with `applies_to` on a slug with no live page: the entry applies and the field stands; the cascade skips it; `guppi lint` names it.
> **－** An archived rule gives no edge; `applies_to` is never computed — it comes from the Case alone.

> **tasks:**
> - [ ] update `estimate-generate-writes-rules-from-applies-to`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out (case 489.5)`
> - [ ] read `estimate-generate-writes-rules-from-applies-to` — `pytest tests/test_generate.py`, then by hand at a later librarian's run

> **ratification:**
> ```
> - decision[case 489.5][update][estimate-generate-writes-rules-from-applies-to]{ref:estimate-generate-writes-rules-from-applies-to}
> ```

### Case 489.6 — A `create` lifted whole when its schema rule changes in the same unit

> **given:**
> `estimate-materialize-lifts-unfiltered-on-a-schema-change` — the promise, its Criterion replaced whole
> **＋** `rule-materialize` — the rule it promises for
> **＋** `rule-<category>-schema` — the schema rule of a category, whose Render is its `schema.yaml`
> **＋** `guppi/materialize.py` — `schema_changed` and the lift of a `create`
> **＋** `vault/wiki/<category>/schema.yaml` — the schema on disk of a category
> **＋** `tests/test_materialize.py` — the tests the reading runs

> **when:**
> `materialize` walks a unit whose ledger holds a decision line, a `create` or an `update`, with the slug `rule-<category>-schema`.

> **then:**
> A `create` of that category in the same unit is lifted whole: every key goes into `fields`, and no key is `unknown`, wherever the schema entry stands in the Spec, before or after.
> **＋** The pages the librarian writes carry the field before `render` lands the schema on disk.
> **－** In a unit without such an entry, and for the other categories of the same unit, a `create` is lifted by `vault/wiki/<category>/schema.yaml` on disk: a key outside the schema is `unknown` and does not reach `fields`.

> **tasks:**
> - [ ] update `estimate-materialize-lifts-unfiltered-on-a-schema-change`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the lift by the schema on disk stated (case 489.6)`
> - [ ] read `estimate-materialize-lifts-unfiltered-on-a-schema-change` — `uv run pytest tests/test_materialize.py -k schema_change`

> **ratification:**
> ```
> - decision[case 489.6][update][estimate-materialize-lifts-unfiltered-on-a-schema-change]{ref:estimate-materialize-lifts-unfiltered-on-a-schema-change}
> ```

### Case 489.7 — A reading moves off a superseded `create`

> **given:**
> `estimate-materialize-refolds-a-reading-on-a-supersede` — the promise, its Criterion replaced whole
> **＋** `rule-materialize` — the rule it promises for
> **＋** `guppi/materialize.py` — `fold_estimate` and `refold`, the fold of a reading and its move
> **＋** `tests/test_materialize.py` — the tests the reading runs

> **when:**
> `materialize` lifts a line with `{supersedes:case N}`, and a `create` entry of Case N in the unit's yaml holds `folded`: the readings of its slug folded into it, with their `status`, `result` and line numbers.

> **then:**
> The readings of `folded` move to the live `create` of the same slug in this unit — `status`, `result`, the line numbers; the marked `create` loses `status`, `result` and `folded`.
> **＋** With no live `create`, each reading becomes an `estimate` entry of its own from the ledger line of that number, after the mark.
> **＋** A reading lifted after the mark is not folded into the marked `create`.
> **－** A mark on a Case of another unit (`elsewhere`) moves nothing — no live `create` is there; the readings of that yaml stand as they are.

> **tasks:**
> - [ ] update `estimate-materialize-refolds-a-reading-on-a-supersede`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the fold of a reading moved into When (case 489.7)`
> - [ ] read `estimate-materialize-refolds-a-reading-on-a-supersede` — `uv run pytest tests/test_materialize.py -k refold`

> **ratification:**
> ```
> - decision[case 489.7][update][estimate-materialize-refolds-a-reading-on-a-supersede]{ref:estimate-materialize-refolds-a-reading-on-a-supersede}
> ```

### Case 489.8 — The sprint page records the group of `generate` and `materialize`

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on every other Estimate
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-page-generation` — a rule whose Estimates this Case recuts
> **＋** `rule-materialize` — a rule whose Estimates this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of `rule-page-generation` and `rule-materialize` are recut.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the Estimates of rule-page-generation and rule-materialize recut to When and Then, the two texts overwritten by case 211.3 restored; the note on every other Estimate stands (case 489)`

> **ratification:**
> ```
> - decision[case 489.8][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
