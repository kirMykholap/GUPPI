## Case 588 — An update that carries only a History note no longer replaces an Estimate's Criterion, and the lost Criterion is restored

> **context:**
> `materialize` turns each ratified Case into entries that `generate` writes onto pages. Today it reads an `update` of an Estimate that carries only `change`, the one-line History note, as an order to replace the whole Criterion. It lifts the Case's `when` and `then` into `sections.Criterion` and adds `set: {status: pending}`. `names_a_part` and `lift_criterion` in `guppi/materialize.py` do this, as `rule-materialize` and the Criterion of `estimate-materialize-changes-a-named-part-alone` state (case 296). The case schema says nothing about such an item. It tells a Case that takes up a put-off question to name the page that carries it with "an `update` with only `change` when nothing on the page changes", and on an Estimate that same item replaces the Criterion. Case 583 named `estimate-estimates-schema-checked` in exactly this way, to close the question case 576 had put off on it. Its `context` said the scripts keep the whole Criterion. The yaml entry of ledger line 4 of `raw/2026-10-01/1725/ledger.md` carries the lifted Criterion and `set: {status: pending}`, and `generate` applied it. The page now holds the `then` of 583 as its Criterion. The old Criterion was the `when` and `then` of case 506.1: the schema file equals its Render, lint reads its lists, and a missing `method` is a finding. It is gone from the page. Its `purpose` and `method` still describe that old promise, and its History line of 583 says the Criterion stands. The hook of `rule-case-check` did warn. The store of the session's plan holds six notes for case 583, one per line of the old Criterion that the new one does not carry, and the Case was kept as built.
> The page is restored by 588.1, which lifts the `when` and `then` of 506.1 word for word from the archived case file of session 1134. Those lines still hold against the live `vault/wiki/estimates/schema.yaml`: its lists, values and conditions are the ones they name. Its `purpose` and `method` state that promise, so they stand. Its status is `pending` before and after. Its History line of 583 stays, since History is never edited, and the new line records the restore. The reading of the page, Work line W2 and an unticked `read` box of `raw/2026-10-01/1725/spec.md`, waits for a later session, because the ledger hook refuses a reading of an Estimate that a decision line of the same session names (case 428.1). 588.2 changes the scripts. An `update` item with `change` alone counts as naming a part, its History, so it lifts nothing and sets no status. `set.status` or a Criterion written under `sections` still replaces the Criterion. `guppi/prespec.py` imports `names_a_part`, and `guppi/casecheck.py` imports the notes of `guppi/prespec.py`, so all three keep one judgment.
> What `case-guppi` found in the frame. A Grep of ``names no part|change` alone|`change` alone|change alone|only `change`|with only change`` over `vault/wiki/rules/*.md`, `vault/wiki/case-schema.md`, `guppi/*.py`, `tests/*.py` and `vault/wiki/estimates/*.md` printed 11 files: `guppi/materialize.py`, `guppi/prespec.py`, `tests/test_prespec.py`, `rule-case-protocol.md`, `case-schema.md`, `rule-case-check.md`, `rule-materialize.md`, `estimate-case-check-notes-a-criterion-line-not-carried.md`, `estimate-materialize-changes-a-named-part-alone.md`, `estimate-prespec-catches-two-cases-on-one-target.md` and `estimate-prespec-checks-the-form-of-an-item.md`. The Criteria of the three Estimates of pre-spec and of the hook, the How it works of `rule-case-check` and the docstrings of `guppi/prespec.py` describe a whole replacement as an update "that names no part, by `names_a_part`". They name the function, so they stay true. In `rule-case-protocol` and its Render the sentence on taking up a put-off question becomes true on an Estimate too, and its sentence that an `update` of an Estimate carries `set: {status: pending}` stands. So neither page changes. `estimate-case-protocol-case-form` does not speak of the form of an Estimate `update`. `tests/test_prespec.py` counts an item with `change` alone as a promise, and 588.2 changes that test. The same pattern over `vault/wiki/insights/` printed 1 file, `insight-materialize-estimate-update-lifts-the-criterion-whole.md`, and over `vault/wiki/lessons/` printed nothing. The Insight stands `actioned`, and its record is not changed. Its Proposal says what case 296 built in session 1315, an update with `change` alone as the whole replacement among the rest. That stays true as a record of that Case. Its History line of case 529 already marks it fixed. 588.2 changes the behaviour, not that record, and the History of `rule-materialize` and of `estimate-materialize-changes-a-named-part-alone` will say so. A Grep of `estimate-materialize-changes-a-named-part-alone|estimate-materialize-lifts-when-and-then` over the repository outside `vault/raw/` and `vault/archive/` printed 6 files: `vault/wiki/log.md`, `rule-materialize.md` and the Decision pages of cases 378.2, 397.3, 400.1 and 400.2. The log and the Decision pages are not read. The Criterion of `estimate-materialize-lifts-when-and-then` promises a lifted Criterion for any `update` entry that writes none. That becomes false for an item with `change` alone, so 588.3 narrows its `when`. Its `purpose` and `method` do not state that part and stand. The `purpose` of `estimate-materialize-changes-a-named-part-alone` promises that an update changes the part it names alone or replaces the Criterion whole, and its `method` names the test file. Both stand. In `rule-materialize` the sentence that an Estimate's Criterion is the `when` and `then` of the Case that names it is limited by the next sentence, on what an `update` item names, so it stands. `generate` writes the History line of an item with `change` alone, as it does on a Rule page (case 584), so it does not change. `materialize` reads the Specs from the working tree at the librarian's run and refuses nothing. Case 587 of this session creates an Estimate and updates a rule, and its case file holds no Estimate `update` with `change` alone. By the main agent's word, Cases 589, 590 and 591 of this session update Estimates, each with `set.status`; I did not read their case files. So no item in this session's plan changes its meaning under the new rule, and no old form is kept. A Grep of `Criterion whole|replaces? the Criterion|lifts? the Criterion` over `.claude/` printed only `.claude/agents/case-guppi.md`, whose lines set how a Case is built, not what the scripts lift. No `create` without a `ref` is made, so no vault query ran. Not done: the case schema gets no new sentence on an `update` with `change` alone, and the History line of 583 on the page stays as written.
> The notes of the check, and why each change is kept. 588.1 does not carry the six lines that 583 lifted onto the page by mistake. The person chose to restore the old Criterion and nothing else, and its line on a conditional not met already promises what those lines promised. 588.2 carries the `when` and the line on a written Criterion beside another part word for word. It drops the line that made `change` alone a whole replacement, because that is the behaviour this sub-case changes. 588.3 narrows its `when` to the entries that still get a lifted Criterion; the old `when` named every `update` entry, and that is no longer true. Its `－` line on `Given:` and the `＋` line of 588.1 on `fields` and `sections` share words, but they are two promises of two Estimates, the lift of a Case's text and the schema of a page, so both stand.

> **problem:**
> An `update` meant only for the History of an Estimate replaced its Criterion, because `materialize` reads `change` alone as a whole replacement. The case schema asks for such an update when a put-off question is closed. The promise of `estimate-estimates-schema-checked` was lost without a decision. The question was how to repair the page, and whether the scripts change so that it cannot happen again.

> **recommend:**
> - **How is the page of `estimate-estimates-schema-checked` repaired?**
>   - Recommended: (a) restore the old Criterion word for word. The person ratified that it stands, it already covers the new test, and it is the only promise of `rule-estimates-schema`.
>   - Answer: (a).
> - **Do the scripts change, so that an update meant only for History can no longer replace a promise?**
>   - Recommended: (a) the scripts change: an update with `change` alone writes only the History line, on an Estimate too. The case schema's own instruction then means the same thing on every page, and the judgment stays one function that all three scripts use.
>   - Answer: (a). The person first found it strange that the scripts replace the page when only a History line was asked for, and asked what had to be written into the History of that page and why, since the script writes History. The answer: the Case gives the text of the line in `change`, and that line was to close the question put off on the Estimate, as the case schema asks. The person then agreed.

### Case 588.1 — The Criterion of `estimate-estimates-schema-checked` is restored

> **given:**
> `estimate-estimates-schema-checked` — the promise, its Criterion restored whole
> **＋** `rule-estimates-schema` — the rule; its Render is the schema of an Estimate page, unchanged
> **＋** `vault/wiki/estimates/schema.yaml` — the file rendered from it
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `guppi/lint.py` — reads the lists of the file for every page of `vault/wiki/estimates/`
> **＋** `vault/wiki/estimates/` — the live Estimate pages
> **＋** `tests/test_schemas.py` — the tests the reading runs

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
> **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds, among its paragraphs, the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
> **－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.

> **tasks:**
> - [ ] update `estimate-estimates-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion restored whole — the text of case 506.1, which case 583 meant to keep and its update with change alone replaced (case 588.1)`
> - [ ] read `estimate-estimates-schema-checked` — in a later session: `uv run pytest tests/test_schemas.py -k estimate` on the live schema, and the live reading `make lint`, no schema finding on `wiki/estimates/`

> **ratification:**
> ```
> - decision[case 588.1][update][estimate-estimates-schema-checked]{ref:rule-estimates-schema}
> ```

### Case 588.2 — An Estimate `update` with `change` alone writes only its History line

> **given:**
> `guppi/materialize.py` — `names_a_part`, `lift_criterion` and the module docstring
> **＋** `tests/test_materialize.py` — the tests of the lift
> **＋** `guppi/prespec.py` — imports `names_a_part` for the promise count, the clash of two Cases and the notes, unchanged
> **＋** `tests/test_prespec.py` — the test that counts an item with `change` alone as a promise
> **＋** `guppi/casecheck.py` — imports the notes of `guppi/prespec.py`, unchanged
> **＋** `guppi/generate.py` — writes the History line of an `update`, unchanged
> **＋** `rule-materialize` — the rule; its Purpose says which `update` item replaces a Criterion
> **＋** `estimate-materialize-changes-a-named-part-alone` — the promise, its Criterion replaced whole

> **when:**
> `uv run guppi materialize` lifts the `update` item of an Estimate.

> **then:**
> An item that carries `set.status` gets `sections.Criterion`, the text it writes under `sections: Criterion` or else the `when` and `then` of its Case, and keeps the status it set.
> **＋** An item that writes `sections: Criterion` keeps that text and gets `set: {status: pending}` unless it set a status itself.
> **＋** A written `sections.Criterion` beside any other part stands and sets `pending`.
> **＋** An item that carries `change` alone gets no `sections.Criterion` and no `set`: `guppi/generate.py` writes its History line, and the Criterion and the status of the page stand.
> **＋** An item that names a part — `set` without `status`, a `replace` pair, a section other than `Criterion` — and writes no Criterion carries that part alone: nothing is lifted and no status is set.
> **＋** `names_a_part` of `guppi/materialize.py` is the one judgment of an item that replaces a Criterion: `guppi/prespec.py` imports it and `guppi/casecheck.py` imports its notes, so an item with `change` alone counts as no promise and gets no note on the lines of the old Criterion.
> **－** An item with `change` alone is not `incomplete`.

> **tasks:**
> - [ ] `guppi/materialize.py`: `names_a_part` counts an Estimate `update` item with `change` alone as naming a part, its History; `lift_criterion` lifts the Criterion only for an item with `set.status` or a written `sections: Criterion`, and sets `pending` only on one that writes its Criterion without a status; the module docstring and the docstrings of both functions say so
> - [ ] `tests/test_materialize.py`: the Estimate `update` items of the fixtures that expect a lifted Criterion carry `set: {status: pending}`; a test that an Estimate `update` with `change` alone gets no `sections`, no `set` and no `incomplete`
> - [ ] `tests/test_prespec.py`: `test_two_estimate_items_with_the_cases_criterion_is_a_finding` counts an item with `change` alone as no promise; a test that such an item gets no `note:` line on the old Criterion
> - [ ] `uv run pytest tests/test_materialize.py tests/test_prespec.py tests/test_casecheck.py`: green
> - [ ] update `rule-materialize`
>   - old: `` one that names no part, or carries `set.status`, replaces the Criterion whole (case 296). ``
>   - new: `` one that carries `set.status` replaces the Criterion whole (case 296), and one that carries `change` alone writes its History line and nothing else, on an Estimate as on any page (case 588.2). ``
>   - change: `an update of an Estimate with change alone writes only its History line; set.status or a written Criterion replaces the Criterion (case 588.2)`
> - [ ] update `estimate-materialize-changes-a-named-part-alone`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — change alone lifts nothing and sets no status; set.status or a written Criterion replaces it (case 588.2)`
> - [ ] read `estimate-materialize-changes-a-named-part-alone` — in a later session: `uv run pytest tests/test_materialize.py`

> **ratification:**
> ```
> - decision[case 588.2][update][rule-materialize]{ref:rule-materialize}
> - decision[case 588.2][update][estimate-materialize-changes-a-named-part-alone]{ref:rule-materialize}
> ```

### Case 588.3 — The promise of the lifted When and Then covers only an item that replaces the Criterion

> **given:**
> `estimate-materialize-lifts-when-and-then` — the promise, its Criterion replaced whole
> **＋** `guppi/materialize.py` — `lift_criterion` and `case_texts`
> **＋** `tests/test_materialize.py` — the tests of the lift on a temp Spec

> **when:**
> `guppi materialize` assembles the `create` entry of an Estimate, or an `update` entry whose item carries `set.status`, whose Case has `given`, `when` and `then` and whose item writes no `sections: Criterion`.

> **then:**
> The entry's `sections.Criterion` is the `When:` and `Then:` of the Case, verbatim with their operands.
> **－** The Criterion holds no `Given:`.
> **＋** The decision record of the Case still carries `given` in its `case_text`; a sub-case without its own `given` carries its parent's.

> **tasks:**
> - [ ] update `estimate-materialize-lifts-when-and-then`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the lift covers a create and an update that carries set.status, not an update with change alone (case 588.3)`
> - [ ] read `estimate-materialize-lifts-when-and-then` — in a later session: `uv run pytest tests/test_materialize.py` on a temp Spec

> **ratification:**
> ```
> - decision[case 588.3][update][estimate-materialize-lifts-when-and-then]{ref:rule-materialize}
> ```
