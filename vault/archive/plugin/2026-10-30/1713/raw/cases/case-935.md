## Case 935 — The lift carries `drop` and guards the Criterion from it

> **context:**
> `guppi materialize` lifts each item of a Case's `then` block into an entry of `materialize.yaml`; for an `update`, `_lift_item` of `.guppi/guppi/materialize.py` copies each key of `ITEM_KEYS["update"]` that the item carries, and `generate` applies the entry. Case 931 adds `drop`, a list of section names, to `ITEM_KEYS`, and `generate` removes each named section and fails the entry when the page lacks the section or the schema of its category requires it, such as `## Criterion` of an Estimate; I read its finished file whole. Once `drop` stands in `ITEM_KEYS`, the loop of `_lift_item` carries it with no other code. Two texts name the keys one by one and miss `drop`: the Criterion of `estimate-materialize-assembles` lists the keys an entry takes from its `then` item, and the Purpose of `rule-materialize` lists the keys lifted from the `then` block; `/pre-spec` reported both on Case 931. In Case 931's round the person chose that a new Case, this one, holds the promise that the lift carries `drop`, on the Estimate of the code that keeps it, and that Case 931 keeps no line of it. The docstring of `.guppi/guppi/materialize.py` lists the fields an entry takes from the `then` block and says that a key the code writes and the list does not name is a finding of the reading of `estimate-materialize-assembles`, so a task adds `drop` there too. In my round the person chose a second part: the lift already marks an Estimate `update` whose `replace` pair stands inside `## Criterion` as `incomplete: [criterion]`, by `touches_criterion` and `lift_criterion`, which I read whole with `names_a_part`, and nothing there reads `drop`. An Estimate `update` whose `drop` names `Criterion` and carries no `set.status` passes `names_a_part` as a named part today and gets no mark; one that carries `set.status` gets a lifted Criterion and `pending`, and `generate` then fails it. `drop` names whole sections only, so the one part of the Criterion it can touch is the whole section; Case 935.2 marks such an item at the lift by a new predicate, `drops_criterion`, so that the librarian sees it in the yaml before `generate` runs. A Grep of `incomplete` over `.guppi/guppi/generate.py` printed nothing, so `generate` does not read the mark, and Case 931's failure stands as the second wall. The judgment of the two sides differs: `generate` asks by `check_schema` of `.guppi/guppi/lint.py` whether the schema requires the section, and the lift asks only whether `drop` names `Criterion` on an Estimate, so no shared function fits both; a Grep of `"drop"|\bdrop\b.*Criterion|Criterion.*\bdrop\b` over `.guppi/guppi` printed nothing, so no code judges `drop` today, and the new predicate is no second copy. A Grep of `touches_criterion|names_a_part` over `.guppi` printed `test_prespec.py`, `materialize.py` and `prespec.py`; `check_criterion_pairs` of `.guppi/guppi/prespec.py`, which I read whole, judges `replace` pairs only, and `/pre-spec` gains no judgment of `drop` here, since the lift and `generate` both catch it. The pair on `rule-materialize` in Case 935.2 adds `drop` to the list of named parts and one sentence on the mark; the sentence on a part inside the Criterion stands, since it names `replace` pairs only. The Criterion of `estimate-materialize-changes-a-named-part-alone` speaks of which `update` items replace a Criterion and which name a part, so Case 935.2 replaces it whole, every line kept but the list of named parts, which gains `drop`, and one `－` line added; its `purpose` and `method` stand. The new Criterion of `estimate-materialize-assembles` keeps every line of the old one and adds `drop` to the list of keys; its `purpose` and `method` do not state the list and stand. A Grep of `estimate-materialize-changes-a-named-part-alone|estimate-materialize-assembles` over `vault/wiki`, `.claude` and `.guppi` printed `log.md`, `materialize.py`, `rule-materialize.md` and `test_materialize.py`; none but the docstring line above states the list, and no test of `.guppi/tests` reads these pages live. The tasks of this Case run after Case 931 adds `drop` to `ITEM_KEYS` in the same Work Mode, since the lift carries no `drop` before it; `test_item_keys_answers_for_each_kind_as_the_lift_does` is changed by Case 931. The check of this file noted that one line of each old Criterion is not carried. Those are the two lines this Case changes on purpose: the first line of the `then` of `estimate-materialize-assembles` gains `drop` in its list of keys, and the line of `estimate-materialize-changes-a-named-part-alone` on a named part gains `drop` in its list of parts. The check also noted that a `then` line of Case 935.2 shares most of its words with one of Case 935.1. The two lines state different promises of two Estimates: the line of Case 935.2 says an item with `change` alone is not `incomplete`, and the line of Case 935.1 lists the keys of an entry, so both stand. The session's ledger holds no `error` lesson.

> **problem:**
> The lift will carry `drop`, but the Estimate and the rule that list its keys do not name it, and an Estimate `update` whose `drop` names its Criterion gets no mark at the lift.

> **recommend:**
> - **Who guards the Criterion against a drop**
>   - Recommended: (a) this Case adds the guard as a second part, judged by the lift.
>   - Answer: (a).

### Case 935.1 — The lift carries `drop` into the entry

> **given:**
> `estimate-materialize-assembles`: its Criterion is replaced whole.
> **＋** `rule-materialize`: its Purpose lists the keys the lift carries.
> **＋** `.guppi/guppi/materialize.py`: `guppi materialize`, which lifts a unit's `ledger.md` and `spec.md` into `materialize.yaml`.
> **＋** `.guppi/tests/test_materialize.py`: the test of the lift.

> **when:**
> `uv run --project .guppi guppi materialize` lifts the record lines of a unit's `ledger.md` against the `then` blocks of its `spec.md`.

> **then:**
> `materialize.yaml` holds one entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `addresses`, `origin`, `line`, `text`, `decision`; from the `then` item found by its slug — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `drop`, `impact`; what the block lacks is `incomplete`, never invented.
> **＋** `reword` is carried as a list of `{old, new}` pairs; a mapping or a scalar under it is `incomplete: [reword]`.
> **＋** An Estimate has its own line and its own entry, the `ref` of the line the Estimate itself; the entry of its `create` keeps `kind`, `purpose`, `method` and `tags` as fields.
> **＋** One decision record per Case: `decision`, `case_text`, `targets`; a sub-case reads a missing `context` and `given` from its parent, never `problem`, `recommend` or `when`, and carries `parent`, the `decision` of its parent.
> **＋** A Case whose sub-cases have decision lines in the unit gets one decision record of its own: its `decision` and its `origin` named by the id of the Case, `case_text` with its `context`, `problem` and `recommend`, and its `given` when it has one, `children` the `decision` of each of its sub-cases in ledger order, and no `targets`.
> **＋** An `estimate` line whose slug has a `create` in the same unit is folded into it; one for a page of an earlier unit is an `estimate` entry of its own.
> **＋** The `new_tags` of any Case reach the yaml once each; an existing `materialize.yaml` is extended with the lines it does not hold, never rewritten.
> **＋** A line the grammar does not parse goes under `unparsed`, and the run goes on.
> **－** No entry of an Estimate is derived from a key of the item of a rule or an entity: an Estimate comes only from its own line.
> **－** A sub-case record without `problem` carries no `incomplete: [problem]`.

> **tasks:**
> - [ ] update `rule-materialize`
>   - old: `` `set`, `sections`, `replace`, `change`, and `rename` or `reword` when the item carries it ``
>   - new: `` `set`, `sections`, `replace`, `change`, and `rename`, `reword` or `drop` when the item carries it ``
>   - change: `the lift carries drop, a list of section names, when the item carries it`
> - [ ] update `estimate-materialize-assembles`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an entry takes drop from its then item`
> - [ ] `.guppi/guppi/materialize.py`: the docstring that lists the fields an entry takes from the `then` block names `drop`, a list of section names carried as written.
> - [ ] `.guppi/tests/test_materialize.py`: a test that an `update` item with `drop: [How it works]` gives its entry `drop` equal to `["How it works"]`, and an item without `drop` gives an entry with no `drop`.
> - [ ] read `estimate-materialize-assembles`

> **ratification:**
> ```
> - decision[case 935.1][update][rule-materialize]{ref:rule-materialize}
> - decision[case 935.1][update][estimate-materialize-assembles]{ref:rule-materialize}
> ```

### Case 935.2 — The lift marks a `drop` of the Criterion

> **given:**
> `estimate-materialize-changes-a-named-part-alone`: its Criterion is replaced whole.
> **＋** `rule-materialize`: its Purpose says which `update` of an Estimate changes a part alone.
> **＋** `.guppi/guppi/materialize.py`: `guppi materialize`, with `names_a_part`, `lift_criterion` and the new `drops_criterion`.
> **＋** `.guppi/guppi/generate.py`: applies the entry and writes its History line.
> **＋** `.guppi/guppi/prespec.py` and `.guppi/guppi/casecheck.py`: import `names_a_part` and its notes.
> **＋** `.guppi/tests/test_materialize.py`: the test of the lift.

> **when:**
> `uv run --project .guppi guppi materialize` lifts the `update` item of an Estimate.

> **then:**
> An item that carries `set.status` gets `sections.Criterion`, the text it writes under `sections: Criterion` or else the `when` and `then` of its Case, and keeps the status it set.
> **＋** An item that writes `sections: Criterion` keeps that text and gets `set: {status: pending}` unless it set a status itself.
> **＋** A written `sections.Criterion` beside any other part stands and sets `pending`.
> **＋** An item that carries `change` alone gets no `sections.Criterion` and no `set`: `.guppi/guppi/generate.py` writes its History line, and the Criterion and the status of the page stand.
> **＋** An item that names a part — `set` without `status`, a `replace` pair, `drop`, a section other than `Criterion` — and writes no Criterion carries that part alone: nothing is lifted and no status is set.
> **＋** `names_a_part` of `.guppi/guppi/materialize.py` is the one judgment of an item that replaces a Criterion: `.guppi/guppi/prespec.py` imports it and `.guppi/guppi/casecheck.py` imports its notes, so an item with `change` alone counts as no promise and gets no note on the lines of the old Criterion.
> **－** An item with `change` alone is not `incomplete`.
> **－** An item whose `drop` names `Criterion` gets `incomplete: [criterion]`, by `drops_criterion` of `.guppi/guppi/materialize.py`, and the lift adds no `sections.Criterion` and no `set.status` to it, whatever else the item carries.

> **tasks:**
> - [ ] update `rule-materialize`
>   - old: `` `set` without `status`, `replace`, a section other than `Criterion` — and writes no Criterion changes ``
>   - new: `` `set` without `status`, `replace`, `drop`, a section other than `Criterion` — and writes no Criterion changes ``
>   - old: `` on an Estimate as on any page (case 588.2). An `update` item's `reword` ``
>   - new: `` on an Estimate as on any page (case 588.2). An `update` of an Estimate whose `drop` names `Criterion` is `incomplete: [criterion]`, and the lift writes no Criterion and sets no status for it, since an Estimate keeps its Criterion (as set in case 935.2). An `update` item's `reword` ``
>   - change: `a drop is a named part, and a drop of the Criterion of an Estimate is incomplete: [criterion]`
> - [ ] update `estimate-materialize-changes-a-named-part-alone`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — drop is a named part, and a drop of the Criterion is incomplete`
> - [ ] `.guppi/guppi/materialize.py`: a function `drops_criterion(drop) -> bool`, True when `drop` is a list that holds the name `Criterion`; `lift_criterion` calls it first for an Estimate `update` and, when it is True, appends `criterion` to the entry's `incomplete` and returns before `names_a_part`. The docstrings of `lift_criterion` and of the module, where they list the named parts, name `drop` and the mark.
> - [ ] `.guppi/tests/test_materialize.py`: tests that an Estimate `update` with `drop: [Criterion]` and `change` gets `incomplete: [criterion]`, no `sections.Criterion` and no `set`; that one with `drop: [Criterion]` and `set: {status: pending}` gets `incomplete: [criterion]` and no `sections.Criterion`; that one with `drop: [Result]` and `change` gets no `incomplete`, no `sections.Criterion` and no `set`.
> - [ ] read `estimate-materialize-changes-a-named-part-alone`

> **ratification:**
> ```
> - decision[case 935.2][update][rule-materialize]{ref:rule-materialize}
> - decision[case 935.2][update][estimate-materialize-changes-a-named-part-alone]{ref:rule-materialize}
> ```
