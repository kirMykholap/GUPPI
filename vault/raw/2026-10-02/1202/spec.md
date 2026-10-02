<!-- approved 18:07:14 · session 1a155152 -->

# Spec — session 1202, 2026-10-02

## Case 587 — make lint runs every step and reports each

> **context:**
> `make lint` runs five steps in a fixed order: `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, then the page check `guppi lint`. Each step is one line of the recipe of the target `lint` in the `Makefile`, and make stops the recipe at the first line that exits non-zero. The backlog step is red in nearly every session that puts an item off: `guppi/backlog.py` counts the `[-]` lines of every `frontier.md`, the session's own included, and only the librarian's run writes `backlog.md` again. So the Baseline that `/work` writes into `work.md` holds only the backlog line, and the findings of the glossary and page steps are not printed. The handoff of session 1725 shows this: the Baseline `make lint` gave exit 2 and stopped at its backlog step, and the agent had to run the page step by hand to get the schema, orphan and fence findings, the deferred lines and the unread lines. The Result of `estimate-retro-red-in-the-baseline-is-not-charged` shows the same stop in session 2356. The librarian's `make lint` at the brief and at the close stops in the same way; the search below printed a line of case 58 that says "`make lint` stopped at its first step". The person chose to fix this in `make lint` itself: the recipe runs every step, each prints its own lines, and the target exits non-zero when any step is red. The backlog red itself stays, as the signal that `backlog.md` waits for the librarian. `/work` and the librarian keep running `make lint` as they do now, and their text does not change. `rule-lint` lists the `Makefile` in `implementation_ref`. Its `## Purpose` says that `make lint` runs `guppi lint` after the four checks and that all five only report. That stays true, and this Case adds one sentence on the new behaviour. No test reads the recipe of `lint`: a Grep of `Makefile` over `tests/` printed only `tests/test_lint.py`, whose hits write fixture Makefiles for the method check. The Case creates `estimate-lint-runs-every-step` with `ref: rule-lint`, so the vault query for a `create` without a `ref` did not run. A Glob `vault/**/estimate-lint-runs-every-step*` found no file, so the slug is free. These Estimates speak of `make lint` and stand. `estimate-harness-pipeline` checks the order of the steps and the Purpose of `rule-harness`, and the order does not change; the person chose to keep the new promise out of it. `estimate-backlog-checks-the-file` and `estimate-sprint-checks-the-file` check the place of their step in that order, and the place does not change. `estimate-harness-make-runs-in-both-shells` wants the same exit code from both shells, no read of stdin and no write to the tree, and the new recipe keeps all three. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` wants each lint finding line as printed in the Baseline, and the Baseline now gets more of them. `estimate-sprint-migration-lint-clean` wants exit 0 at the close of the sprint, which still means every step is clean. The search with pattern `make lint` over `vault/wiki/rules/` printed `rule-close`, `rule-glossary`, `rule-harness`, `rule-lint`, `rule-case-build`, `rule-brief`, `rule-backlog`, `rule-work-mode`, `rule-sprint`, `rule-retro` and `rule-render-harness`. Outside History lines, each hit says that `make lint` runs a step, sets its order, reads its output, or tells Retro not to run it. None says that it stops at the first red, and none is made false. The same pattern over `vault/wiki/estimates/` printed 25 files: the Estimates named above, the schema-check and layout Estimates whose `method` reads `make lint`, `estimate-documentation-completes`, `estimate-glossary-checks-the-file`, `estimate-glossary-terms-defined`, `estimate-lint-checks-the-method`, `estimate-raw-archive`, `estimate-page-schemas-one-file-per-rule`, `estimate-atomicity-rendered`, `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-sprint-migration-file-route-gone` and `estimate-sprint-migration-rule-class-files-dissolved`. Each reads the findings or the exit code, and none relies on the stop. The pattern `make lint|guppi lint|--check` over `.claude/` printed `.claude/skills/work/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/agents/librarian-guppi.md` and `.claude/agents/case-guppi.md`. They run `make lint` and keep its output, or forbid running it at Retro, and the hit in the pre-spec skill is `guppi prespec --check`. All of them stand. The pattern `first (red|step|failing)|stops at|make -k|keep-going` over `vault/wiki/` printed `brief.md` (the source of this item) and the Decision pages of cases 58, 89.1–89.4, 150.1, 326 and 569, which were not opened. No hook changes, and no reader in code reads a text this Case changes, so no old form is kept.

> **problem:**
> `make lint` stops at its first red step. The backlog step is red in nearly every session that puts an item off, so the Baseline of `/work` and the librarian's runs lose the findings of the later steps, the page findings included. The question was where the fix goes.

> **recommend:**
> - **Where the fix for the hidden findings goes**
>   - Recommended: (a) `make lint` runs every step, each prints its own findings, and it exits non-zero when any step is red; only the `Makefile` changes, and the backlog red stays as a signal.
>   - Answer: (a), agreed.
> - **How the change is checked**
>   - Recommended: (a) a new Estimate of its own, `estimate-lint-runs-every-step` on `rule-lint`, read by hand at the next session's Baseline, where the backlog step is expected to be red; `estimate-harness-pipeline` stays as it is.
>   - Answer: (a), agreed.

> **given:**
> `Makefile` — the target `lint`, whose recipe runs the five steps
> **＋** `rule-lint` — the rule that lists the `Makefile` among its code files and says what `make lint` runs
> **＋** `estimate-lint-runs-every-step` — the new promise of `rule-lint`
> **＋** `/work` — the skill whose Baseline runs `make lint` and writes its output into `work.md`
> **＋** `.claude/agents/librarian-guppi.md` — the librarian, whose brief and close run `make lint`

> **when:**
> Someone runs `make lint` of the `Makefile`: by hand, in the Baseline of `/work`, or in the librarian's run of `.claude/agents/librarian-guppi.md`.

> **then:**
> `make lint` runs all five steps in the order `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint`, whether an earlier step exited 0 or not.
> **＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
> **＋** `make lint` exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
> **－** No step reads the stdin of its caller, and `make lint` writes nothing to the tree.

```then
create:
- slug: estimate-lint-runs-every-step
  ref: rule-lint
  kind: QA
  purpose: Whether make lint runs all five steps when an earlier one is red, prints the lines of each, and exits non-zero when any step is red
  method: 'by hand, the make lint of the Baseline of the first /work of a later session whose backlog step is red: the steps that printed, the page findings of guppi lint and the exit code, recorded in the estimate line'
  tags:
  - harness
  - workflow
update:
- slug: rule-lint
  replace:
  - old: holds (cases 147.7, 227).
    new: holds (cases 147.7, 227). It runs all five even when one of them is red, so a red step hides no finding of a later one, and it exits non-zero when any step is red (case 587).
  change: make lint runs every step and exits non-zero when any is red (case 587)
```

```tasks
- [x] `Makefile`: the recipe of `lint` runs each of the five steps with stdin from `/dev/null`, keeps going after a step that exits non-zero, and exits non-zero at the end when any step did
- [x] update `rule-lint`
- [x] create `estimate-lint-runs-every-step`
- [x] by hand: `make lint` on the working tree after the change, from PowerShell and from Git Bash; the steps that printed and the exit code in both shells
- [ ] read `estimate-lint-runs-every-step` — by hand at the Baseline of the first `/work` of a later session whose backlog step is red
```

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

```then
update:
- slug: estimate-estimates-schema-checked
  set:
    status: pending
  change: the Criterion restored whole — the text of case 506.1, which case 583 meant to keep and its update with change alone replaced (case 588.1)
```

```tasks
- [x] update `estimate-estimates-schema-checked`
- [x] read `estimate-estimates-schema-checked` — in a later session: `uv run pytest tests/test_schemas.py -k estimate` on the live schema, and the live reading `make lint`, no schema finding on `wiki/estimates/`
```

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

```then
update:
- slug: rule-materialize
  replace:
  - old: one that names no part, or carries `set.status`, replaces the Criterion whole (case 296).
    new: one that carries `set.status` replaces the Criterion whole (case 296), and one that carries `change` alone writes its History line and nothing else, on an Estimate as on any page (case 588.2).
  change: an update of an Estimate with change alone writes only its History line; set.status or a written Criterion replaces the Criterion (case 588.2)
- slug: estimate-materialize-changes-a-named-part-alone
  set:
    status: pending
  change: the Criterion replaced whole — change alone lifts nothing and sets no status; set.status or a written Criterion replaces it (case 588.2)
```

```tasks
- [x] `guppi/materialize.py`: `names_a_part` counts an Estimate `update` item with `change` alone as naming a part, its History; `lift_criterion` lifts the Criterion only for an item with `set.status` or a written `sections: Criterion`, and sets `pending` only on one that writes its Criterion without a status; the module docstring and the docstrings of both functions say so
- [x] `tests/test_materialize.py`: the Estimate `update` items of the fixtures that expect a lifted Criterion carry `set: {status: pending}`; a test that an Estimate `update` with `change` alone gets no `sections`, no `set` and no `incomplete`
- [x] `tests/test_prespec.py`: `test_two_estimate_items_with_the_cases_criterion_is_a_finding` counts an item with `change` alone as no promise; a test that such an item gets no `note:` line on the old Criterion
- [x] `uv run pytest tests/test_materialize.py tests/test_prespec.py tests/test_casecheck.py`: green
- [x] update `rule-materialize`
- [x] update `estimate-materialize-changes-a-named-part-alone`
- [x] read `estimate-materialize-changes-a-named-part-alone` — in a later session: `uv run pytest tests/test_materialize.py`
```

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

```then
update:
- slug: estimate-materialize-lifts-when-and-then
  set:
    status: pending
  change: the Criterion replaced whole — the lift covers a create and an update that carries set.status, not an update with change alone (case 588.3)
```

```tasks
- [x] update `estimate-materialize-lifts-when-and-then`
- [x] read `estimate-materialize-lifts-when-and-then` — in a later session: `uv run pytest tests/test_materialize.py` on a temp Spec
```

## Case 589 — The language finding accepts Latin letters in a code span

> **context:**
> The language finding of `/pre-spec` reads the name, `context` and `problem` of every Case of the plan. It reports a letter outside the script of `documentation_lang`, which `guppi.toml` sets. The hook of `rule-case-check` runs the same finding on each answer of `case-guppi`. `check_untranslated` of `guppi/prespec.py` calls `ratified.untranslated`, which calls `config.outside`, the one judgment of a letter's script (case 476.3). That judgment reads the whole text, code spans included. A slug, a path or a field name in a code span is always Latin. For `en` this changes nothing. For a documentation language in another script, such as `ru`, every Case that names a page in a code span gets a finding. Work Mode of session 1318 found this, and case 481 put it off on the placeholder `rule-prespec-script-skips-code-spans`. The page holds only its purpose and its defer.
> The person chose to put no rule of its own in the vault. The code-span sentence goes into the description of the finding in the docstring of `guppi/prespec.py`, which `rule-prespec` points to (case 561.1). The Criteria of the two Estimates of the finding are replaced whole. The placeholder is deleted, and its delete line carries the supersede of case 481, which retires the defer. The person also chose what the check does inside a code span: a Latin letter there is accepted, and a letter of any other script is judged as in prose. So for `en` the finding behaves exactly as it does today, and a Russian word between backticks is still a finding. 589.1 changes the judgment and the Estimate of `/pre-spec`. 589.2 replaces the Estimate of the hook and changes `rule-case-check`. These are two promises of two Estimates, because the run at `/pre-spec` and the run on an answer can fail apart.
> The `## How it works` of `rule-case-check`. It states that any such letter is a finding, which would no longer be true. A pre-spec finding showed that `vault/wiki/rules/schema.yaml` asks a Leaf to lose that section at its next touch, with the mechanism in the docstring of its code (cases 193, 200.2). The person chose that the section leaves now. They also chose that 589.2 removes it by hand, as a one-off task of Work Mode, after the docstring of `guppi/casecheck.py` carries each fact of it that still holds. No script can remove a section: an `update` replaces the text of a section or words inside it, and `body` of `guppi/generate.py` writes a section given empty text as a bare heading. The section left `rule-materialize`, `rule-spec-capture` and `rule-lint` the same way (cases 189, 200.4, 202). The removal is an exception to the sentence of `rule-page-generation` that the script is the only writer to `wiki/`, and that sentence stands. So the update of `rule-case-check` carries only its History line, and no `replace` pair, which would miss the removed section at the librarian's run. Its Purpose says the hook judges the script of the name, `context` and `problem`, and that stays true. Case 590.1 changes the turn sentence of the same section and the paragraphs on how a round opens in the docstring of `guppi/casecheck.py`. With the person's answer, 590.1 makes no change of its own in the section and names this Case. The docstring task of 589.2 carries the turn sentence as 590.1 sets it, so the `given` of 589.2 names its case file.
> What `case-guppi` found in the frame. `config.outside` stays the one judgment of a letter's script. The code span is read by `CODE_SPAN` of `guppi/lint.py`, the pattern that `guppi/prespec.py` and `guppi/generate.py` already import, so no second pattern of a code span is written. A Grep of `CODE_SPAN|code_spans|def spans|SPAN =|outside\(` over `guppi/` printed `guppi/config.py`, `guppi/generate.py`, `guppi/prespec.py`, `guppi/ratified.py` and `guppi/lint.py`. `guppi/config.py` imports no module of `guppi`, and `guppi/lint.py` imports neither `guppi/config.py` nor `guppi/ratified.py`, so the import makes no cycle. A Grep of ``outside the script|config\.outside|letter outside|ratified\.untranslated`` over the repository outside `vault/raw/` and `vault/archive/` printed 25 files: `backlog.md`, `log.md`, `rule-case-check.md`, `rule-prespec.md`, `rule-prespec-script-skips-code-spans.md`, `estimate-case-check-refuses-a-letter-outside-the-script.md`, `estimate-language-spec-prose-in-english.md`, `guppi/casecheck.py`, `guppi/prespec.py`, `guppi/ratified.py`, `guppi/config.py`, `tests/test_casecheck.py`, `tests/test_prespec.py`, `tests/test_config.py`, and the Decision pages of cases 445.1, 445.2, 445.3, 445.4, 445.6, 445.7, 476.1, 476.2, 476.3, 476.4 and 481. The log, the backlog and the Decision pages are not read. The hit in `rule-prespec.md` is a History line. The two Criteria, the docstrings of the three modules and the tests enter the sub-cases. The `purpose` of each Estimate states the old promise without the exception, so it is set anew. The `method` of each names its test run, so it stands. `estimate-language-followed`, the other Estimate of `rule-language`, says that slugs and paths stay as they are in either language. The change makes that easier to keep, so it stands. A Grep of ``How it works of `?rule-case-check|rule-case-check`?'s How it works|rule-case-check#How`` over the same paths printed no file, so no page points to the section that leaves. A Grep of `rule-prespec-script-skips-code-spans` over the same paths printed 4 files: `brief.md`, `backlog.md`, `log.md` and `decision-case-481.md`. None of them is a live page that the delete makes false. A Grep of `outside the script|letter outside|language finding` over `.claude/` printed no file. The only hook on `SubagentStop` in `.claude/settings.json` is `uv run guppi casecheck --subagent`, and this Case changes what it judges, not its registration. The judgment only accepts more text than before, so no reader refuses an old form, and no old form is kept. Case 588 changes the notes of `/pre-spec` on an Estimate `update` and other tests of `tests/test_prespec.py`. It does not touch the language finding, so the two Cases do not meet. The Grep of `^(purpose|deferred_by):` over `vault/wiki/rules/` printed the placeholder and no other rule on code spans in the language finding. No `create` is made, so no slug is checked. Not done: a code span of two or more backticks, which `CODE_SPAN` does not match, is still read as prose, and a `[[slug]]` outside a code span is still judged letter by letter.
> The notes of the check, and why each change is kept. In each sub-case the first line of the old Criterion, that any such letter is a finding, is not carried word for word. It is replaced by a line that adds the exception for a Latin letter in a code span, and that exception is the behaviour this Case changes. The other old lines are carried word for word. 589.2 names `/pre-spec` in its `given`, so its line on the function the hook runs stands as it was. The line of 589.1 on where the judgment lives stands as it was, and the code span has a line of its own. Some `then` lines of 589.2 share most of their words with lines of 589.1, among them the line on an answer with no such letter and the two lines on a Latin slug in a code span. They are the same behaviour checked from two angles, the run of `/pre-spec` on the plan and the run of the hook on an answer. Each Estimate must read without the other, so both stand. The `given` of 589.2 holds more than seven `**＋**` lines. The frame of the hook, the removal of the section and the Case it shares the docstring with all need a line, and the promise is still one, the finding on an answer.

> **problem:**
> The language finding cannot tell a word written in the wrong language from a slug or a path in a code span. So for a documentation language not written in Latin script, it reports almost every Case. The question was where the fix is recorded, and what the check does with the letters inside a code span.

> **recommend:**
> - **Where is the change recorded in the vault?**
>   - Recommended: (b) no new rule. One sentence goes into the description of `/pre-spec` next to the language check, the promises of the two existing Estimates are rewritten whole, and the empty page `rule-prespec-script-skips-code-spans` is deleted, which closes the put-off item. The behaviour is one sentence about a check that already has its description and two Estimates.
>   - Answer: Agreed: (b).
> - **What does the check do with the letters inside a code span?**
>   - Recommended: (b) inside a code span, accept Latin letters and judge all other letters as in prose. It solves the problem, a Russian word between backticks is still caught, and for English nothing changes.
>   - Answer: Agreed: (b).

### Case 589.1 — The pre-spec language finding accepts a Latin letter in a code span

> **given:**
> `estimate-language-spec-prose-in-english` — the promise of the finding at `/pre-spec`, its Criterion replaced whole
> **＋** `rule-prespec-script-skips-code-spans` — the placeholder of the defer of case 481, deleted
> **＋** `guppi/config.py` — `outside`, the one judgment of a letter's script
> **＋** `guppi/lint.py` — `CODE_SPAN`, the one pattern of a code span, unchanged
> **＋** `guppi/ratified.py` — `untranslated`, which reads the name, `context` and `problem` of each Case
> **＋** `guppi/prespec.py` — `check_untranslated` and the description of the finding in the module docstring
> **＋** `tests/test_prespec.py` — the tests of the finding
> **＋** `tests/test_config.py` — the test of `outside`

> **when:**
> `guppi prespec --check <plan>` runs at `/pre-spec`, and reads the plan file and `guppi.toml`.

> **then:**
> A name, `context` or `problem` of a Case of the plan that holds, outside a code span, a letter outside the script of the language `guppi.toml` sets as `documentation_lang`, or, inside a code span, a letter that is neither Latin nor of that script, gives one finding naming the Case, the part and the language.
> **＋** A Latin slug, path or field name in a code span gives no finding, whatever the documentation language.
> **＋** A short-form Case under `## Deferred` is read the same way.
> **＋** A plan whose names, contexts and problems hold no letter outside that script gives no finding of this check.
> **＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`, and no Case is read by this check.
> **＋** The judgment of a letter's script lives in `guppi/config.py`, and `guppi/ratified.py` imports it.
> **＋** `guppi/config.py` reads a code span by `CODE_SPAN` of `guppi/lint.py`, and holds no pattern of its own.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.
> **－** The plan is compared with no other file: no ratified copy is read.

```then
update:
- slug: estimate-language-spec-prose-in-english
  set:
    status: pending
    purpose: Pre-spec finds a name, context or problem of a Case of the plan that holds a letter outside the script of the documentation language of guppi.toml, a Latin letter in a code span excepted, a short form under Deferred included
  change: the Criterion replaced whole — a Latin letter in a code span gives no finding, any other letter there is judged as in prose (case 589.1)
delete:
- slug: rule-prespec-script-skips-code-spans
  impact: its one sentence stands in the Criterion of estimate-language-spec-prose-in-english and the description of the finding in guppi/prespec.py; in vault/wiki/ only brief.md, backlog.md, log.md and decision-case-481 name it, and the supersede of case 481 retires that defer
```

```tasks
- [x] `guppi/config.py`: `outside` reads the code spans of the text by `CODE_SPAN` of `guppi/lint.py`, and a letter inside a span counts as outside only when it is neither Latin nor of the script of the language; the module docstring and the docstring of `outside` say so
- [x] `guppi/ratified.py`: the module docstring and the docstring of `untranslated` say that a Latin letter in a code span gives no finding
- [x] `guppi/prespec.py`: the language item of the module docstring and the docstring of `check_untranslated` say that a Latin letter in a code span gives no finding (case 589.1)
- [x] `tests/test_config.py`: `test_outside_finds_a_letter_of_another_script` asserts that a Latin slug in a code span is not outside for `ru`, that a Cyrillic word in a code span is outside for `en`, and that a Greek letter in a code span is outside for `ru`
- [x] `tests/test_prespec.py`: a test `test_script_a_latin_code_span_passes_under_russian`, a plan in Russian whose `context` names a slug in a code span gives no finding under `documentation_lang = "ru"`; a test `test_script_a_cyrillic_code_span_is_found_under_english`, a Russian word in a code span of a `context` gives the finding under `en`
- [x] `uv run pytest tests/test_config.py tests/test_prespec.py`: green
- [x] update `estimate-language-spec-prose-in-english`
- [x] delete `rule-prespec-script-skips-code-spans`
- [x] read `estimate-language-spec-prose-in-english` — in a later session: `uv run pytest tests/test_prespec.py -k script`
```

### Case 589.2 — The check of each answer of `case-guppi` accepts a Latin letter in a code span

> **recommend:**
> - **Change**
>   - Asked: a pre-spec finding showed that `vault/wiki/rules/schema.yaml` asks a Leaf to lose its `## How it works` at its next touch, and this sub-case added a sentence to that section of `rule-case-check`. The person agreed that the section leaves at this touch, and that what still holds of it moves into the docstring of `guppi/casecheck.py`.
>   - Taken: the `replace` pair on the section is dropped, the docstring of `guppi/casecheck.py` takes the facts of the section, and the update of `rule-case-check` carries only its History line.
> - **How does the `## How it works` section leave `rule-case-check`, when no script can remove a section?**
>   - Recommended: (a) remove it by hand, as a one-off task of Work Mode. This Case takes the removal, and Case 590 makes no change of its own in that section and names this Case. It is how the section left three rule pages before, it keeps both Cases small, and the content only moves.
>   - Answer: (a).

> **given:**
> `estimate-case-check-refuses-a-letter-outside-the-script` — the promise of the finding on an answer, its Criterion replaced whole
> **＋** `rule-case-check` — the rule; its `## How it works` leaves the page by hand
> **＋** `vault/wiki/rules/schema.yaml` — a Leaf loses its `## How it works` at its next touch, its mechanism in the docstring of its code
> **＋** `guppi/casecheck.py` — runs `check_untranslated` on `SubagentStop`; its module docstring takes the facts of the section
> **＋** `guppi/prespec.py` — `check_untranslated`, imported, unchanged by this sub-case
> **＋** `/pre-spec` — the skill whose check runs the same function
> **＋** `guppi/config.py` — the judgment of a letter's script, as 589.1 sets it
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of the Case the hook writes
> **＋** `tests/test_casecheck.py` — the tests of the finding on an answer
> **＋** `raw/2026-10-02/1202/cases/case-590.md` — 590.1 sets the turn sentence of the docstring of `guppi/casecheck.py` and leaves the removal of the section to this Case

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the answer and `guppi.toml`.

> **then:**
> A name, `context` or `problem` of a Case of the answer that holds, outside a code span, a letter outside the script of the language `guppi.toml` sets as `documentation_lang`, or, inside a code span, a letter that is neither Latin nor of that script, is a finding of that Case, stored with the Case in `<plan>.checked.json`: the hook exits 2 with it on stderr, and `case-guppi` answers again.
> **＋** While such a finding stands, no `raw/<date>/<hi HHMM>/cases/case-<N>.md` is written for the answer.
> **＋** An answer whose names, contexts and problems hold no such letter gets no finding from this check.
> **＋** A Latin slug or path in a code span of an answer is no finding, whatever the documentation language.
> **＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`.
> **＋** The hook runs `check_untranslated` of `guppi/prespec.py`, the function `/pre-spec` runs, and holds no second copy of its judgment.
> **－** An answer whose text `<plan>.checked.json` already holds with findings is stored again with this finding and exits 0, so an unchanged answer is not sent back twice, and no file is written for it.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.

```then
update:
- slug: rule-case-check
  change: How it works removed by hand, a one-off, its facts in the docstring of guppi/casecheck.py; the language finding on an answer accepts a Latin letter in a code span (case 589.2)
- slug: estimate-case-check-refuses-a-letter-outside-the-script
  set:
    status: pending
    purpose: An answer of case-guppi whose name, context or problem holds a letter outside the script of the documentation language, a Latin letter in a code span excepted, is a finding of the check, and no file of the Case is written while it stands
  change: the Criterion replaced whole — a Latin letter in a code span is no finding, any other letter there is judged as in prose (case 589.2)
```

```tasks
- [x] `guppi/casecheck.py`: the module docstring carries each fact of the `## How it works` of `rule-case-check` that it does not yet hold, the sentence on the turn of the reply as case 590.1 sets it, and says that a Latin letter in a code span of a name, `context` or `problem` is no finding (case 589.2)
- [x] one-off: remove the `## How it works` section from `vault/wiki/rules/rule-case-check.md` by hand, once the docstring of `guppi/casecheck.py` carries each fact of it that still holds, as `vault/wiki/rules/schema.yaml` asks of a Leaf at its next touch; nothing else of the page changes by hand
- [x] `tests/test_casecheck.py`: a test `test_subagent_script_a_latin_code_span_passes_under_russian`, an answer whose name, `context` and `problem` are in Russian and name a slug in a code span gets no finding under `documentation_lang = "ru"`, and its file is written; a test `test_subagent_script_a_cyrillic_code_span_is_a_finding`, a Russian word in a code span of the `context` is a finding under `en`, and no file is written
- [x] `uv run pytest tests/test_casecheck.py -k script`: green
- [x] update `rule-case-check`
- [x] update `estimate-case-check-refuses-a-letter-outside-the-script`
- [x] read `estimate-case-check-refuses-a-letter-outside-the-script` — in a later session: `uv run pytest tests/test_casecheck.py -k script`
```

## Case 590 — Make the turn and the stretch share one test of the person's message

> **context:**
> Three hooks read the transcript of the session, and each one needs to know where the person last spoke. The `Stop` check of `rule-case-check` reads the turn of the reply. It looks there for the sending of a Case file and for a round of `case-guppi`. `turn_of_reply` in `guppi/casecheck.py` starts that turn after the last `user` record that is not `isMeta` and holds more than tool results. The ledger hook of `rule-ledger-write`, and `guppi/onward.py` through it, read the stretch since the person's last message, to see whether they have already refused once. `own_refusals` in `guppi/ledger.py` starts the stretch after the last `user` record whose `origin.kind` is `human`. `is_prompt` in `guppi/context.py` holds a third copy: it needs a text block and no tool result. Part of the difference between the hooks is on purpose. A subagent's answer to a `SendMessage` comes back as a `user` record with `origin.kind` `task-notification`. The turn must start there, because `given_back` reads the round from that record. The stretch must not start there, because the person has not written. The weak part is the shared core, the test of the person's message, which each module writes in its own way. They already differ. In the transcript `d08a5ca5-…` of this project, the record of the local command `/clear` has string content, no `origin` and no `isMeta`. `turn_of_reply` takes it as the start of a turn, and the stretch does not. Case 586 (session 2026-10-01/1725) put this question off on the placeholder `rule-turn-start-one-judgment`. The page holds only its purpose and its defer.
> The person chose the recommendations of the first two rounds. There is one function in `guppi/ledger.py` that names the kind of a `user` record. A record is the person's message when its `origin.kind` is `human`, and a returned answer when its `origin.kind` is `task-notification`. The turn starts at either kind. The stretch starts at the person's message alone. `guppi/context.py` joins the function and counts from the start of the turn. The placeholder is deleted. One new Estimate checks the shared function, and the Criterion of `estimate-context-size-shown-after-each-reply` is replaced, since its sentence on the person's last prompt would no longer be true. Two findings of `/pre-spec` changed the Case after that. The first found that `estimate-case-check-refuses-text-before-a-round` defines the turn as the records after the person's last prompt. The person chose to replace its Criterion whole in a sub-case of its own. The second found that the Case added sentences to the `## How it works` of three Leaf pages. `vault/wiki/rules/schema.yaml` says that on a Leaf this section leaves at its next touch, and that the mechanism lives in the docstring of the code. The person chose that the section leaves now. No script removes a section, so Work Mode removes it by hand as a one-off task, as earlier sessions did, and moves what still holds into the docstring of the module. The `update` of each page then carries only its History line. This replaces the How-it-works sentences of the answer to the question on where the decision is recorded. The facts now go into the docstrings alone. Case 589.2 takes the removal of the section of `rule-case-check`, so this Case makes no change on that page. This Case takes `rule-ledger-write` and `rule-context-size`.
> The split. 590.1 is the shared function, the hooks and the new Estimate. 590.2 is the token counter and its Estimate. 590.3 is the round check of the Case check and its Estimate. These are three promises: the boundary of the turn and the stretch, the number the person sees after a reply, and the judgment of how a round is shown can each fail apart.
> What `case-guppi` found in the frame. Several searches ran over the transcripts of this project in `C:\Users\kir\.claude\projects\c--PROJECTS-GUPPI`. A Grep for a record that holds both `"isMeta":true` and `"origin":{"kind":"human"` printed no match, and neither did a Grep for a record that holds both a `tool_result` and that label. So keying on `human` alone keeps the stretch exactly as it is today. The main transcripts outside `subagents/` give different counts: 1431 records of string content not opening with `<`, against 1373 such records carrying `human`. The older transcript `71cd373f-…` holds typed messages of the person with no `origin`, and messages with `origin.kind` `peer`, which come from another Claude session. Under the chosen test, neither kind opens a turn. For a transcript with no labelled record, the Case check then reads the whole transcript as the turn, and finds an earlier sending too, so it is looser there and not stricter. The ledger hook already reads such a transcript that way. The readers judge a transcript that Claude Code writes, not a text of the vault, so no old form needs to be kept beside the new one.
> Other searches were over the vault and the code. A Grep of `turn_of_reply|own_refusals|given_back` over the repository outside `vault/raw/` and `vault/archive/` printed 9 files: `backlog.md`, `guppi/casecheck.py`, `guppi/ledger.py`, `guppi/onward.py`, `estimate-case-build-checks-the-finished-case.md`, `rule-case-check.md`, `rule-turn-start-one-judgment.md`, `decision-case-586.md` and `decision-case-584.md`. The hit in `estimate-case-build-checks-the-finished-case.md` is in its Result and stands, and the Decision pages and the backlog are not read. The hit in `rule-case-check.md` is in its `## How it works`, which Case 589.2 removes. A Grep of `person's last (prompt|message)|turn of the reply|last prompt|origin\.kind` over `vault/wiki/rules/`, `vault/wiki/entities/`, the pages at the root of `vault/wiki/`, `.claude/` and `guppi/` printed 11 files: `backlog.md`, `log.md`, `rule-turn-start-one-judgment.md`, `rule-case-check.md`, `rule-retro-onward.md`, `rule-ledger-write.md`, `rule-context-size.md`, `guppi/casecheck.py`, `guppi/ledger.py`, `guppi/onward.py` and `guppi/context.py`. `rule-retro-onward` speaks of the refusal after the person's last message, and its stretch does not change, so it stands. The hits in `rule-ledger-write.md` and `rule-context-size.md` are in the `## How it works` that leaves.
> The Estimates. The Criteria of `estimate-ledger-write-lifts` and `estimate-retro-onward-sends-the-agent-to-the-handoff` define the stretch by `human` and stand. `estimate-case-check-shows-only-the-checked-case` requires a sending in the turn of the reply without saying where the turn starts, and the new Estimate states the start, so it stands. The purpose and the method of `estimate-context-size-shown-after-each-reply` speak of the change since the last reply and of its test run. The purpose and the method of `estimate-case-check-refuses-text-before-a-round` speak of the round and of its tests. None of them states the old line, so they stand.
> Other checks. The `Stop` hooks in `.claude/settings.json` are `guppi ledger`, `guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward` and `guppi onward --plan`, and no registration changes. `guppi/ratified.py` reads a sending by time and not by the turn, so it is not touched. Case 589.2 moves what still holds of the `## How it works` of `rule-case-check` into the module docstring of `guppi/casecheck.py`. 590.1 writes the start of the turn into the same docstring, so 590.1 names the case file of 589 in its `given`, and the turn sentence of 590.1 is the one that docstring keeps. A Glob of `vault/{wiki,archive}/**/estimate-ledger-write-names-the-kind-of-a-user-record.md` printed no file, so the slug is free. A Grep of `rule-turn-start-one-judgment` over the repository outside `vault/raw/` and `vault/archive/` printed 4 files: `brief.md`, `backlog.md`, `log.md` and `decision-case-586.md`. None of them is a live page that the delete makes false.
> The notes of the check, and why each change is kept. In 590.2, the old line of the Criterion on N and D is not carried word for word. Its sentence on N is kept, and its sentence on D is replaced with the start of the turn, which is the behaviour this sub-case changes. In 590.3, the old first line is not carried word for word. Its definition of the turn is replaced, and the rest of the line is kept. The other old lines of both are carried word for word. The `－` line of 590.2 on the records that do not move the start of the count shares most of its words with the `－` line of 590.1 on the records that open no turn. The first line of 590.3 shares words with the turn line of 590.1. Each is the same boundary checked from the side of one reader, and each Estimate must read without the Estimate of the shared function, so both stand.
> Not done: a `peer` message from another Claude session opens no turn.

> **problem:**
> The person's message in a transcript is tested in three places in three ways. That breaks `rule-one-judgment-one-implementation`, and it already gives two answers on one record. The question was whether the turn and the stretch are one judgment, how they come to agree, whether the token counter joins, how the record is classified, where the decision is recorded and how it is checked.

> **recommend:**
> - **How should the two hooks agree on the person's message?**
>   - Recommended: (a) one shared function in `guppi/ledger.py` that names the kind of a user record. The Case check starts its turn at the person's message or a returned answer, and the ledger hook and `guppi/onward.py` start at the person's message only.
>   - Answer: Agreed with the recommendations: (a).
> - **Does the token counter join the shared function?**
>   - Recommended: (a) yes. `guppi/context.py` uses the shared function with the turn boundary, and `is_prompt` is removed.
>   - Answer: Agreed with the recommendations: (a).
> - **Where is the decision recorded?**
>   - Recommended: (a) delete the placeholder, which retires its defer, and record the decision in the docstrings and the How it works of the existing rule pages.
>   - Answer: Agreed with the recommendations: (a).
> - **Which test says that a line is the person's message?**
>   - Recommended: (a) the source label: `origin.kind` `human` is the person's message, and `task-notification` is a returned answer.
>   - Answer: Agreed with the recommendations: (a).
> - **How is it checked that the fix is done?**
>   - Recommended: (a) a new Estimate for the shared test under `rule-ledger-write`, and the Criterion of `estimate-context-size-shown-after-each-reply` rewritten, in two sub-cases.
>   - Answer: Agreed with the recommendations: (a).
> - **Is the Criterion of the round check rewritten too?**
>   - Recommended: (a) a third sub-case replaces the Criterion of `estimate-case-check-refuses-text-before-a-round` whole. Its first line names the turn by the shared function, and every other line is carried word for word.
>   - Answer: (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person chose that `## How it works` leaves the Leaf pages this Case touches, as the schema of rule pages asks. What still holds moves into the docstrings of the modules, and Work Mode removes the section by hand as a one-off task. Case 589 takes the section of `rule-case-check`.
>   - Taken: the How-it-works sentences of `rule-ledger-write` and `rule-context-size` are dropped. Each `update` carries only its History line, and a one-off task removes the section and moves what holds into `guppi/ledger.py` and `guppi/context.py`. The `update` of `rule-case-check` is dropped, and 590.1 names the case file of 589.

### Case 590.2 — The token counter counts the change from the start of the turn

> **given:**
> `estimate-context-size-shown-after-each-reply` — the promise of the size line, its Criterion replaced whole
> **＋** `rule-context-size` — its `## How it works` leaves, by hand
> **＋** `guppi/context.py` — `sizes`, `is_prompt` and the module docstring
> **＋** `guppi/ledger.py` — the function that names the kind of a `user` record, as 590.1 sets it
> **＋** `tests/test_context.py` — the tests of the count
> **＋** `vault/wiki/rules/schema.yaml` — a Leaf drops `## How it works` at its next touch

> **when:**
> The `Stop` hook `uv run guppi context` runs after a reply of the main agent and reads the transcript at `transcript_path`.

> **then:**
> With no error of its own, the hook prints JSON with a `systemMessage` of one line that opens with `context: <N> tokens (<+D> since the last reply)`.
> **＋** N is the sum of the input, cache read, cache creation and output tokens of the last main-agent API call the transcript holds; D is N less the same sum at the last main-agent call before the start of the turn, the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer.
> **＋** The records of a subagent (`isSidechain`) are not counted.
> **＋** On the re-fire (`stop_hook_active`), with a transcript it cannot read, or with no call that carries `usage`, the hook prints nothing.
> **－** A record with no `origin.kind`, a record marked `isMeta` and a tool result do not move the call that D is counted from.
> **－** The hook never blocks: it exits 0 in every case.

```then
update:
- slug: rule-context-size
  change: '## How it works left the Leaf, its mechanism in the docstring of guppi/context.py; D counts from the start of the turn, named by the function of guppi/ledger.py (case 590.2)'
- slug: estimate-context-size-shown-after-each-reply
  set:
    status: pending
  change: the Criterion replaced whole — D counts from the last call before the start of the turn, the person's message or a returned answer (case 590.2)
```

```tasks
- [x] `guppi/context.py`: `is_prompt` is removed; `sizes` takes the start of the turn by the function of `guppi/ledger.py`; the module docstring says that D counts from the last call before the start of the turn (case 590.2)
- [x] `tests/test_context.py`: the prompt records carry `origin.kind` `human`; a test `test_d_counts_from_the_start_of_the_turn`: a returned answer starts the count, and a record with no `origin` does not
- [x] `uv run pytest tests/test_context.py`: green
- [x] one-off, by hand: the `## How it works` section of `vault/wiki/rules/rule-context-size.md` is removed, heading and text; what of it still holds and the module docstring of `guppi/context.py` does not yet say moves into that docstring first, D counted from the start of the turn
- [x] update `rule-context-size`
- [x] update `estimate-context-size-shown-after-each-reply`
- [x] read `estimate-context-size-shown-after-each-reply` — in a later session: `uv run pytest tests/test_context.py`
```

### Case 590.3 — The round check reads the turn by the shared function

> **given:**
> `estimate-case-check-refuses-text-before-a-round` — the promise of the round check, its Criterion replaced whole
> **＋** `guppi/casecheck.py` — `round_opening` and `turn_of_reply`
> **＋** `guppi/ledger.py` — the function that names the kind of a `user` record, as 590.1 sets it
> **＋** `tests/test_casecheck.py` — the tests of the round check
> **＋** `.claude/skills/grill-me/SKILL.md` — the question line of a round
> **＋** `.claude/skills/wait-what/SKILL.md` — a re-pitch, not judged
> **＋** `/pre-spec` — the skill after which only the first line is judged
> **＋** `/hi` — the skill whose own questions are not judged
> **＋** `rule-prespec` — sets the text of the loop after the findings of `/pre-spec`

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that holds a question line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, no Case heading and no first line `**Fact:**`.
> **＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn before its last tool call.
> **＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
> **＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
> **＋** Text after the last question and one horizontal rule is not judged.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
> **－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
> **－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
> **－** On the re-fire (`stop_hook_active`) it exits 0, so the round shown again after a refusal is not judged again.
> **－** It stores nothing and writes no file.

```then
update:
- slug: estimate-case-check-refuses-text-before-a-round
  set:
    status: pending
  change: the Criterion replaced whole — the turn of the reply starts at the person's message or a returned answer, by the function of guppi/ledger.py (case 590.3)
```

```tasks
- [x] `tests/test_casecheck.py`: a test `test_round_a_record_with_no_origin_opens_no_turn`: a round given back to an `Agent` call before the record of a local command with no `origin` is still judged in the turn of the reply (case 590.3)
- [x] `uv run pytest tests/test_casecheck.py -k round`: green
- [x] update `estimate-case-check-refuses-text-before-a-round`
- [ ] read `estimate-case-check-refuses-text-before-a-round` — in a later session: `uv run pytest tests/test_casecheck.py -k round`
```

## Case 591 — The Spec box: a conserved Spec runs on its own branch, first part

> **context:**
> `rule-spec-box` held one idea, put off in five sessions: a session that runs a conserved Spec on a branch of its own. A defer copied `tags` onto the page. Lint therefore does not judge it a placeholder, and it prints three findings on it: missing `kind`, missing `estimates`, and orphan. These findings keep `estimate-sprint-migration-lint-clean` red. The defer of case 532 also names the missing parent. In the rounds the person chose to build the box now (Q1), and to build it in a first part (Q10).
>
> Today `/carry` conserves a Spec: it writes `carry.md`, rewrites the brief, runs `guppi backlog` and commits. The librarian passes the folder by while `carry.md` stands, and `/hi` lists each conserved Spec first under `## Cases`. But no skill runs a conserved Spec, and no branch holds one. The defer of case 540 on `rule-work-mode` names the same gap: `/work` does not say which `spec.md` it runs, where it ticks the boxes, or when it deletes `carry.md`.
>
> After this Case, `/carry` makes the branch `spec/<date>-<HHMM>` at its commit (Q3). A later session takes the conserved Spec at the Frontier, but only while it has ratified no Case of its own (Q11). The title line of its plan file names the conserved `spec.md`, and the hook of `rule-spec-capture` then prints a line that leads to `/box` in place of the fork. `/box` does these steps:
> - it checks the Spec and commits;
> - it switches to the Spec's branch and brings it up to the shared branch by a fast-forward;
> - it calls `/work` with the folder (Q8);
> - after `/handoff`, it fast-forwards the shared branch to the Spec's branch and deletes that branch;
> - it runs `make test` and dispatches the librarian there (Q7).
>
> Nothing under `vault/wiki/` is written on the branch (Q4). One session runs at a time (Q6), so both merges are fast-forwards. They refuse only when the other branch holds a commit of its own, and that refusal is a stop. `/box` loads `vault/wiki/where-to-stop.md` as `/work` does. Its check refuses `main` as the shared branch.
>
> The check also refuses a Spec when a page it changes has a History line that names a decision of a later Case, or when a page it creates now stands. Two things are the second part, a line of the Backlog of `entity-sprint-migration` (Q10, Q11): checking such a Case again and building it again (Q4, Q9), and taking a conserved Spec after other Cases of the session (Q5).
>
> Q8 put the baseline of `/work` into the Spec's folder. Q11 then put every record of the session into the session's own folder: the baseline, the readings, the lessons and the handoff. The Case follows Q11. `/work` ticks the conserved `spec.md`, deletes its `carry.md`, and names the folder under `## Conserved Spec` of `work.md`. That section is the one signal of a box session for `/work`, `/retro` and `/handoff`.
>
> `/work` and `/retro` count the decision lines of the conserved Spec as this session's: for the boxes, for the scope of an edit and for the readings, since this session builds that Spec. The ledger hook sees only this session's lines, so the text is the guard. `/handoff` dispatches nothing in a box session, and `vault/wiki/where-to-stop.md` gets the stops of `/box`. Sub-case 591.7 carries `{supersedes:case 540}`, since it answers that defer. Sub-case 591.11 closes the code fence of `decision-case-13`, which the defer of case 565 tied to this item (Q2).
>
> `rule-spec-box` becomes a child of `rule-end-of-work`, after `rule-retro-onward`, which answers the missing parent of case 532. `generate` writes a parent's `children` only on a `create`, so 591.4 sets the list on `rule-end-of-work` beside the `parent` that 591.5 sets.
>
> In the frame, the guard of `guppi/ratified.py` lets the agent create the plan file only with one line that opens with `# `. So the conserved Spec is named in that title line. `guppi gate` refuses `/retro` in a session with no `spec.md` and no record line. The hook of `rule-spec-capture` copies the title line into the session's `spec.md`, so that file stands. `.gitignore` keeps `vault/raw/*/event_log.md` out of git, and `/box` commits the tree before each switch, so the writes of the hooks do not block a switch. No hook registration in `.claude/settings.json` changes. `guppi spec` prints and refuses nothing, and no reader refuses a text it reads, so no old form is kept.
>
> After the librarian's run, `rule-spec-box` carries `kind`, `estimates`, `tags` and `parent`, and its Estimates name it in `target`. Its three findings go, and its new Estimates print `unread` lines by design. The pre-spec finding on this Spec says that 589.1 and 590.1 delete two of the seven placeholders that print `deferred` lines. The other five still keep `estimate-sprint-migration-lint-clean` red, so its Criterion stands. Every `create` carries a `ref`, so the vault query for a `create` without a `ref` did not run. A Glob of `vault/**/estimate-{spec-box,hi-takes}*` printed only `estimate-hi-takes-its-readings`, so the three new slugs are free.
>
> These searches were run:
> - The pattern `/carry` over `vault/wiki/rules/` printed `rule-brief`, `rule-case-protocol`, `rule-session`, `rule-permissions`, `rule-spec-capture`, `rule-carry-over` and `rule-end-of-work`. Over `.claude/` it printed `.claude/settings.json` (its `carry.md` allow line) and `.claude/skills/carry/SKILL.md`. Over `vault/wiki/estimates/` it printed `estimate-brief-written`, `estimate-case-protocol-asks-in-the-grill-me-shape`, `estimate-case-protocol-puts-the-harness-before-plan-mode`, `estimate-session-phases-in-order`, `estimate-carry-over-writes`, `estimate-end-of-work-order` and `estimate-spec-capture-offers-the-fork`.
> - The pattern `ExitPlanMode` over `vault/wiki/rules/` printed `rule-ledger-write`, `rule-case-protocol`, `rule-session`, `rule-prespec-hook`, `rule-hook-registry`, `rule-spec-capture`, `rule-carry-over` and `rule-work-mode`. Over `.claude/` it printed `.claude/skills/work/SKILL.md`, `.claude/settings.json` and `.claude/skills/carry/SKILL.md`.
> - The pattern `librarian-guppi` over `vault/wiki/rules/` printed `rule-documentation`, `rule-brief`, `rule-synthesis`, `rule-carry-over`, `rule-handoff`, `rule-index-check` and `rule-close`. The pattern `librarian-guppi|Materialize` over `.claude/` printed `.claude/skills/handoff/SKILL.md`, `.claude/agents/librarian-guppi.md` and `.claude/skills/carry/SKILL.md`.
> - The pattern `work\.md` over `guppi/` printed nothing.
> - The pattern `spec-box` over `vault/wiki/` printed `entity-sprint-migration`, `brief.md`, `backlog.md`, `log.md`, the Decision pages of cases 207, 219, 232, 244, 305.1–305.5, 367, 428.1–428.4, 465, 478.1, 478.2, 479.1–479.5, 532 and 565, and the Result sections of `estimate-rules-schema-checked` and `estimate-retro-red-in-the-baseline-is-not-charged`.
>
> Outside History, `log.md` and `brief.md`, the sentences made false are these: the pair in `rule-end-of-work` on the question asked when leaving Plan Mode; the Purpose of `rule-spec-capture`; the import sentence of `rule-where-to-stop`; and the Backlog line of `entity-sprint-migration`. Each enters a sub-case. The choice between `/work` and `/carry` in `rule-case-protocol` and its two Estimates holds wherever that choice is asked; a box session asks none.
>
> These Estimates stand:
> - `estimate-session-phases-in-order`: the marks still rise in time, and the commit of `/box` sits between `spec.md` and the Retro commit.
> - `estimate-hi-writes-frontier`: the line of a conserved Spec and the closers do not change.
> - `estimate-spec-capture-appends`: the copy of the plan does not change.
> - `estimate-retro-runs-on-to-the-handoff`: the hook of `rule-retro-onward` does not change.
> - `estimate-lint-checks-the-statuses`: the placeholder judgment does not change.
> - `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`: it speaks of the Spec of the session and the pages that Spec updates. 591.8 makes the conserved Spec that Spec in a box session, and each line of its Criterion stays true of it.

> **problem:**
> The placeholder `rule-spec-box` keeps `make lint` red, and the person chose to build the Spec box rather than archive it. The questions were: how a conserved Spec runs on a branch of its own without the vault conflicting at the merge, how a session takes it up, and how much of that is built now.

> **recommend:**
> - **What happens to the page `rule-spec-box`**
>   - Recommended: (a) archive the page and keep the idea as a note in the sprint page's backlog list.
>   - Answer: (c), build it now. The person described a branch made at once for each saved Spec, which they enter to build it, or leave while work goes on in the shared branch. They said the documentation must be settled first, since merging branches brings conflicts, and asked for a proposal.
> - **Is the broken code fence of `decision-case-13` fixed in this Case**
>   - Recommended: (a) fix it here, as a sub-case.
>   - Answer: (a), agreed.
> - **When the branch of a saved plan is made, and what it is**
>   - Recommended: (a) a plain branch made by `/carry` from the commit that saves the plan; the session stays on the shared branch.
>   - Answer: (a), with one correction: the branch is made from the commit after the whole of `/carry` is done, the brief written and the rest.
> - **How the documentation stays free of merge conflicts**
>   - Recommended: (a) only the shared branch writes the vault. Before the work, the plan's branch takes in the shared branch, pre-spec checks the plan against today's pages, and only a Case on a page whose History has a line after the save is built again and ratified again.
>   - Answer: (a). The person first wrote "4) b", then said the numbers were mixed up and confirmed (a).
> - **Where taking up a saved plan starts**
>   - Recommended: (b) from Plan Mode at any point; the session's own Cases are saved by `/carry` with their branch, then the box runs the saved plan.
>   - Answer: (b), after the person asked whether this is all one session — `/carry`, then the box.
> - **Ordinary work and a saved plan at the same time**
>   - Recommended: (a) take turns: one session at a time, on one branch at a time.
>   - Answer: (a).
> - **Who merges the plan's branch back, and when**
>   - Recommended: (a) the box skill merges at its end, after `/handoff`, runs `make test`, and the librarian runs on the shared branch; on a conflict in code it stops and asks.
>   - Answer: (a). The person asked whether the box is in essence ordinary Work Mode with git branches.
> - **Is the box a new skill around `/work`, or `/work` itself**
>   - Recommended: (a) a new skill that does the branch steps and calls `/work` with the saved plan's folder.
>   - Answer: (a), agreed.
> - **Where a Case of the saved plan built again is written**
>   - Recommended: (a) into the saved plan's folder, its file and its ledger, by the two hooks taught to write there.
>   - Answer: (a), agreed.
> - **How much of this is built in this session**
>   - Recommended: (b) a first part now — the branch made by `/carry`, the box skill, the merge back and the fence fix. The check against changed pages (Q4, Q9) is put off as a backlog item, and until then the box refuses a saved plan whose pages changed after the save.
>   - Answer: (b), agreed.
> - **Where the box writes its records when this session's own Cases were saved**
>   - Recommended: (b) for now, the box runs only in a session with no Cases of its own. Its records go into the session's own folder, and Q5 (b) comes with the later part.
>   - Answer: (b), agreed.

### Case 591.1 — /carry makes the branch of the Spec after its commit

> **given:**
> `rule-carry-over` — the rule of `/carry`; its Render is the skill
> **＋** `.claude/skills/carry/SKILL.md` — the skill, rendered in full from `rule-carry-over`
> **＋** `raw/<hi date>/<hi HHMM>/frontier.md` — the open lines that Next session takes
> **＋** `vault/wiki/brief.md` — the brief that `/carry` rewrites
> **＋** `vault/wiki/backlog.md` — the backlog that `guppi backlog` writes
> **＋** `vault/wiki/sprint.md` — the sprint file, through which a sprint item reaches `/hi`
> **＋** `/hi` — the start of the next session, which reads the brief
> **＋** `vault/raw/` — the session folders that `/carry` commits
> **＋** `git branch spec/<hi date>-<hi HHMM>` — the command that makes the branch of the Spec
> **＋** `/retro` and `/handoff` — the end skills that `/carry` does not run
> **＋** `vault/wiki/` — the pages, which `/carry` does not write
> **＋** `rule-spec-box` — the box that runs the Spec from its branch
> **＋** `estimate-carry-over-writes` — its Criterion replaced whole

> **when:**
> The agent calls the skill `/carry` on `PreToolUse Skill`, after the person answered "conserve" at the fork `ExitPlanMode` prints. The person never types it.

> **then:**
> The skill reads the tree. When the tree holds changes outside the session folder and `vault/wiki/brief.md`, the skill stops and says that work was done and the ordinary exit applies.
> **＋** Otherwise it rewrites `vault/wiki/brief.md` in the short shape, with no Deferred list.
> **＋** The short shape holds Where things stand, Flags and Next session, with no Readings due and no Readings at the close.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, a list with no item the line "none": `Cases` is always the line "none", since a deferred decision reaches `/hi` through `vault/wiki/backlog.md` and a sprint item through `vault/wiki/sprint.md`; `Work` holds each open `W` line of `raw/<hi date>/<hi HHMM>/frontier.md`, and `Ask the person` each open `A` line with its Estimate by slug, the mark `needs the person` and its question.
> **＋** It puts `carry.md` into the session folder: one line, a flag for `materialize` and `guppi backlog`, not a document. The session that finishes the work deletes it.
> **＋** It runs `uv run guppi backlog`, and `vault/wiki/backlog.md` then shows the conserved Spec with its targets.
> **＋** It runs `make style` and commits `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`.
> **＋** After that commit it runs `git branch spec/<hi date>-<hi HHMM>`, so the branch of the Spec points at the commit that holds the whole of `/carry`.
> **－** No open `W` or `A` line of `frontier.md` is left out of Next session, so the next `/hi` takes each one into its Frontier.
> **－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`, and it writes no decision. It writes no page of `vault/wiki/`.
> **－** It switches to no branch: the session stays on the branch it ran on.
> **－** The work stays sequential, session after session: one conserved Spec, no parallel work.
> **－** `.claude/skills/carry/SKILL.md` equals the Render of the page and is not edited by hand.

```then
update:
- slug: rule-carry-over
  replace:
  - old: 'description: Conserve a ratified Spec whose work is not done — rewrite the brief, mark the session folder, run `guppi backlog`, commit; run nothing else.'
    new: 'description: Conserve a ratified Spec whose work is not done — rewrite the brief, mark the session folder, run `guppi backlog`, commit, make the branch of the Spec; run nothing else.'
  - old: '`docs(vault): Spec of session <HHMM> conserved, Cases <N>–<M>`.'
    new: |-
      `docs(vault): Spec of session <HHMM> conserved, Cases <N>–<M>`.
      4. Make the branch of the Spec at that commit: `git branch spec/<hi date>-<hi HHMM>`. Stay on the current branch: the Spec waits on its branch until a later session takes it at the Frontier and `/box` runs it (`rule-spec-box`, case 591).
  change: /carry makes the branch spec/<hi date>-<hi HHMM> at its commit and stays on the current branch (case 591.1)
- slug: estimate-carry-over-writes
  set:
    status: pending
    purpose: /carry writes the brief and the mark, runs guppi backlog, commits, makes the branch of the Spec at that commit, and runs nothing else
    method: uv run guppi render --check; by hand, the first /carry after the fork of ExitPlanMode — the tree, vault/wiki/brief.md, carry.md, vault/wiki/backlog.md, the commit and git branch read
  change: the Criterion replaced whole — /carry makes the branch of the Spec after its commit (case 591.1)
```

```tasks
- [x] update `rule-carry-over`
- [x] update `estimate-carry-over-writes`
- [x] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
- [ ] read `estimate-carry-over-writes` — by hand, at the first `/carry` of a later session
```

### Case 591.3 — After ExitPlanMode the hook leads a box session to /box

> **given:**
> `rule-spec-capture` — the rule of the hook `guppi spec` on `PostToolUse ExitPlanMode`; its Purpose, on the fork
> **＋** `guppi/spec.py` — the hook that copies the plan and prints the line
> **＋** `raw/<hi date>/<hi HHMM>/spec.md` — the Spec of the session, which the hook writes
> **＋** `vault/raw/` — the session folders, among them the folders of conserved Specs
> **＋** `/hi` — opens the session; without its `hi` line the hook writes no Spec
> **＋** `vault/wiki/case-schema.md` — a Case is ratified by the person's reply, never by a picker tool
> **＋** `guppi/box.py` — the module of `/box`; it holds the judgment whether a plan names a conserved Spec
> **＋** `guppi/materialize.py` — `is_carried_over`, the one judgment of a folder marked by `carry.md`
> **＋** `tests/test_spec.py` — the tests of the printed line
> **＋** `.claude/skills/box/SKILL.md`, `.claude/skills/work/SKILL.md` and `.claude/skills/carry/SKILL.md` — the skills the line names
> **＋** `estimate-spec-capture-appends` — the copy of the plan, which stands
> **＋** `estimate-spec-capture-offers-the-fork` — its Criterion replaced whole

> **when:**
> `guppi spec` has run on `PostToolUse` of `ExitPlanMode` and written the Spec, or found it already there.

> **then:**
> The stdout of the hook is one JSON object, `hookSpecificOutput` with `hookEventName: PostToolUse` and `additionalContext`, that holds one line with the session folder and the Spec file `raw/<hi date>/<hi HHMM>/spec.md`.
> **＋** For `PostToolUse` Claude Code adds to the agent's context only `hookSpecificOutput.additionalContext` from a JSON object on stdout; plain stdout with exit 0 goes to the debug log.
> **＋** The agent sees this line in the `ExitPlanMode` result.
> **＋** When the approved plan names the `spec.md` of a folder under `vault/raw/` that `is_carried_over` of `guppi/materialize.py` judges marked by `carry.md`, the line names that folder and tells the agent to call `.claude/skills/box/SKILL.md` with it, and to ask the person nothing.
> **＋** For any other plan the line is the fork. The fork line tells the agent to ask the person by `AskUserQuestion` with two options, `/work` (Work Mode on the Spec now) and `/carry` (the Spec conserved for a later session), and to start nothing until the person answers.
> **＋** On the answer, the agent calls `.claude/skills/work/SKILL.md` or `.claude/skills/carry/SKILL.md`, the skill of the option picked.
> **－** A `PostToolUse` hook blocks nothing: the tool has run.
> **－** Without a Spec, nothing, as before.
> **－** The path "no `/hi` for this session" — stderr, exit 2 — does not change.
> **－** A Case is still ratified by the person's reply in the chat, never by a picker tool, as `vault/wiki/case-schema.md` says: the picker is for the end of the session only.
> **－** The writing of the Spec does not change: that is the promise of `estimate-spec-capture-appends`.

```then
update:
- slug: rule-spec-capture
  replace:
  - old: the person picks, and the agent calls the skill picked (cases 190.5, 479.1).
    new: 'the person picks, and the agent calls the skill picked (cases 190.5, 479.1). When the approved plan names the `spec.md` of a conserved Spec — a folder under `vault/raw/` that holds `carry.md` — the hook prints in place of the fork a line that names that folder and tells the agent to call `/box` with it and to ask the person nothing: the person took that Spec at the Frontier (`rule-spec-box`, case 591).'
  change: a plan that names a conserved Spec gets a line that leads to /box in place of the fork (case 591.3)
- slug: estimate-spec-capture-offers-the-fork
  set:
    status: pending
    purpose: 'The hook prints one line after the Spec is written: for a plan that names a conserved Spec, the call of /box with its folder and no question; otherwise the fork, asked by AskUserQuestion with /work and /carry, and the skill picked called'
    method: uv run pytest tests/test_spec.py -k 'fork or box'; by hand, the first ExitPlanMode of a session after the render, and the first ExitPlanMode of a session that took a conserved Spec
  change: the Criterion replaced whole — a plan that names a conserved Spec leads to /box, any other gets the fork (case 591.3)
```

```tasks
- [x] update `rule-spec-capture`
- [x] update `estimate-spec-capture-offers-the-fork`
- [x] `guppi/box.py` — `conserved_spec_named(plan, project_dir)`: the folder `vault/raw/<date>/<HHMM>/` whose `spec.md` the plan names and that `is_carried_over` of `guppi/materialize.py` judges marked, or `None`; the module docstring names `rule-spec-box`
- [x] `guppi/spec.py` — when `conserved_spec_named` returns a folder, the line names it and tells the agent to call `/box` with it and to ask nothing; otherwise `fork_line` as before; the module docstring says so
- [x] `tests/test_spec.py` — `-k box`: a plan whose title line names the `spec.md` of a folder with `carry.md` gets the line of `/box` with that folder and no `AskUserQuestion`; a folder without `carry.md`, or no such path, gets the fork
- [ ] read `estimate-spec-capture-offers-the-fork` — `uv run pytest tests/test_spec.py -k 'fork or box'`, and by hand at the first `ExitPlanMode` of a session that took a conserved Spec
```

### Case 591.4 — A box session is asked nothing on leaving Plan Mode and ends the ordinary way

> **given:**
> `rule-end-of-work` — the MOC of the ends of a session; its Purpose, on the question when leaving Plan Mode, and its `children`
> **＋** `rule-retro`, `rule-retro-commit`, `rule-handoff`, `rule-carry-over` and `rule-retro-onward` — the children of `rule-end-of-work`, in their order
> **＋** `rule-spec-box` — the box that runs a conserved Spec and merges its branch back, the new last child
> **＋** `/box`, `/handoff` and `/carry` — the skills of the ends
> **＋** `vault/raw/<date>/<hi HHMM>/` and `vault/raw/<date>/event_log.md` — the session folder and the day's event log
> **＋** `git log` — the commits of the session
> **＋** `estimate-end-of-work-order` — its Criterion replaced whole

> **when:**
> A session ends, and someone reads its folder `vault/raw/<date>/<hi HHMM>/`, the day's event log `vault/raw/<date>/event_log.md` and `git log`.

> **then:**
> The session ended one of two ways: Work Mode, Retro, the commit, the handoff and the librarian; or `/carry` straight after Plan Mode.
> **＋** In the ordinary way the order holds: `/handoff` is refused while the tree is dirty; `handoff.md` exists before the librarian is dispatched; no other commit stands between the handoff and the librarian's commit.
> **＋** On leaving Plan Mode the agent asks the person which of the two ends, and starts nothing until it is answered.
> **＋** A session that took a conserved Spec at the Frontier is asked nothing on leaving Plan Mode: `/box` runs the ordinary way on the branch of that Spec, and the shared branch takes that branch by a fast-forward after `handoff.md` exists and before the librarian is dispatched.
> **＋** `rule-carry-over` is a child of `rule-end-of-work`, after `rule-handoff`.
> **＋** `rule-spec-box` is a child of `rule-end-of-work`, after `rule-retro-onward`.

```then
update:
- slug: rule-end-of-work
  set:
    children:
    - '[[rule-retro]]'
    - '[[rule-retro-commit]]'
    - '[[rule-handoff]]'
    - '[[rule-carry-over]]'
    - '[[rule-retro-onward]]'
    - '[[rule-spec-box]]'
  replace:
  - old: On leaving Plan Mode the agent asks the person which of the two ends and starts nothing until it is answered (case 190.2).
    new: 'On leaving Plan Mode the agent asks the person which of the two ends and starts nothing until it is answered (case 190.2). A session that took a conserved Spec at the Frontier is asked nothing there: `/box` runs it the ordinary way on the branch of that Spec, and merges the branch back by a fast-forward after `handoff.md` stands and before the librarian (`rule-spec-box`, case 591).'
  change: a session that took a conserved Spec is asked nothing on leaving Plan Mode and ends the ordinary way through /box; rule-spec-box a child after rule-retro-onward (case 591.4)
- slug: estimate-end-of-work-order
  set:
    status: pending
  change: the Criterion replaced whole — a box session is asked nothing on leaving Plan Mode, its branch merged back by a fast-forward before the librarian; rule-spec-box the last child (case 591.4)
```

```tasks
- [x] update `rule-end-of-work`
- [x] update `estimate-end-of-work-order`
- [ ] read `estimate-end-of-work-order` — `make test-end-of-work`, and by hand at the close of the first session that `/box` runs
```

### Case 591.7 — /work runs the Spec of the folder /box gives it

> **given:**
> `rule-work-mode` — the rule of Work Mode, taken up from the defer of case 540; its Render is the skill
> **＋** `.claude/skills/work/SKILL.md` — the skill, rendered in full from `rule-work-mode`
> **＋** `raw/<date>/<hi HHMM>/work.md` — the baseline, the marks of an expected red and the section `## Conserved Spec`
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec of the session
> **＋** `vault/raw/<date>/<HHMM>/` — the folder of a conserved Spec, with its `spec.md` and `carry.md`
> **＋** `/box` — the skill that calls `/work` with the folder
> **＋** `vault/wiki/` — the pages, which only the librarian's run writes
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — its Criterion replaced whole

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
> **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task.
> **＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.

```then
update:
- slug: rule-work-mode
  replace:
  - old: Work Mode runs the approved Spec of the session.
    new: Work Mode runs the approved Spec of the session, or the conserved Spec whose folder `/box` gives it (case 591).
  - old: the person types it to resume.
    new: the person types it to resume; /box calls it with the folder of a conserved Spec.
  - old: Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder.
    new: Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder. When `/box` calls it with the folder of a conserved Spec, `vault/raw/<date>/<HHMM>/`, the Spec below is that folder's `spec.md`, and `work.md` still stands in the session's folder (case 591).
  - old: write `vault/raw/<date>/<hi HHMM>/work.md` with two sections.
    new: write `vault/raw/<date>/<hi HHMM>/work.md` with two sections, or three with a folder from `/box`.
  - old: '`## Expected red`: empty for now.'
    new: '`## Expected red`: empty for now. With a folder from `/box`, the third, `## Conserved Spec`: the folder, on one line.'
  - old: 'When the last task is done, take the Work readings before `/retro`:'
    new: 'When the last task is done, delete the `carry.md` of a folder from `/box`, then take the Work readings before `/retro`:'
  change: /work runs the Spec of the folder /box gives it, names that folder under Conserved Spec of work.md and deletes its carry.md after the last task (case 591.7)
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    status: pending
    purpose: Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks, names that folder under Conserved Spec and deletes its carry.md, and marks an expected red under Expected red
    method: 'uv run guppi render --check; by hand, in a session after the render, the first /work the agent calls at the fork, the first /work the person types and the first /work that /box calls: the branch, work.md, the ticks of the Spec, the carry.md of the folder and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent''s own run of its command, recorded in the estimate line'
  change: the Criterion replaced whole — /work runs the Spec of the folder /box gives it (case 591.7)
```

```tasks
- [x] update `rule-work-mode`
- [x] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [x] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — by hand, in a later session, the first `/work` that `/box` calls among them
```

### Case 591.8 — /retro reviews the conserved Spec that /box ran as this session's work

> **given:**
> `rule-retro` — the rule of Retro; its Purpose holds the scope rule, its Render is the skill
> **＋** `.claude/skills/retro/SKILL.md` — the skill, rendered in full from `rule-retro`
> **＋** `raw/<date>/<hi HHMM>/work.md` — its section `## Conserved Spec`, written by `/work`
> **＋** `vault/raw/<date>/<HHMM>/spec.md` and `ledger.md` — the conserved Spec and its decision lines
> **＋** `/box` — the skill that runs the conserved Spec
> **＋** `guppi/ledger.py` — the ledger hook, which judges only this session's lines
> **＋** `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — the expected red of the Spec's pages, which stands
> **＋** `estimate-retro-loads` — its Criterion replaced whole

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built — rendered, written, run.
> **＋** An Estimate that this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — gets no reading in this session, built or not; the handoff names it as a reading of a later session.
> **＋** The `read` line of its old Criterion in an earlier Spec is not read; the reading of the new Criterion closes it in a later session, at the moment its `method` names.
> **＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec of this session is the `spec.md` of the folder that section names: Retro sorts its boxes, and the decision lines of that folder's `ledger.md` count as this session's for those boxes, for the scope of an edit and for the readings above.
> **－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

```then
update:
- slug: rule-retro
  replace:
  - old: an edit is allowed when it finishes work a line of this session's ledger ratified, and is new scope otherwise.
    new: an edit is allowed when it finishes work a line of this session's ledger ratified, and is new scope otherwise; in a session that `/box` runs, the lines of the conserved Spec's ledger count as this session's (case 591).
  - old: otherwise open it with the Read tool (case 569.2). Sort the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73).
    new: 'otherwise open it with the Read tool (case 569.2). When `work.md` holds `## Conserved Spec`, this session runs that conserved Spec by `/box`, and builds it: below, the Spec of this session is the `spec.md` of the folder that section names, and the decision lines of that folder''s `ledger.md` count as lines of this session''s ledger — for the boxes, for the scope of an edit and for the readings this session does not take; the ledger hook sees only this session''s own lines, so this text is the guard (case 591). Sort the unticked boxes of the `tasks` of the Spec — `raw/<date>/<hi HHMM>/spec.md` (the session''s folder, case 73), or the `spec.md` of the folder of `## Conserved Spec`.'
  change: in a session that /box runs, the conserved Spec is the Spec Retro reviews, and its decision lines count as this session's (case 591.8)
- slug: estimate-retro-loads
  set:
    status: pending
    method: one reading by hand at the first /retro, and one at the first /retro of a session that /box runs, recorded in the estimate line
  change: the Criterion replaced whole — in a session that /box runs, the conserved Spec counts as this session's work (case 591.8)
```

```tasks
- [x] update `rule-retro`
- [x] update `estimate-retro-loads`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-loads` — by hand, at the first `/retro` of a session that `/box` runs
```

### Case 591.9 — /handoff in a box session hands back to /box

> **given:**
> `rule-handoff` — the rule of `/handoff`; its Render is the skill
> **＋** `.claude/skills/handoff/SKILL.md` — the skill, rendered in full from `rule-handoff`
> **＋** `guppi/gate.py` — the gate that reads the tree before `/handoff`
> **＋** `vault/raw/<date>/event_log.md` and `vault/raw/<date>/<hi HHMM>/` — the day's event log and the session folder
> **＋** `raw/<date>/<hi HHMM>/work.md` — its section `## Conserved Spec`, the signal of a box session
> **＋** `librarian-guppi` — the librarian the skill dispatches
> **＋** `/box` — the skill that dispatches the librarian after its merge
> **＋** `estimate-handoff-dispatches` — its Criterion replaced whole

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, the gate of `guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

> **then:**
> The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
> **＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
> **＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the sections that `rule-handoff` names, with no Read call on the artifacts.
> **＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written, and shows the librarian's report to the person unchanged.
> **－** In a session whose `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec` — one that `/box` runs — the agent dispatches nothing after `handoff.md` and goes back to the step of `/box` that follows `/handoff`.
> **－** No commit follows the handoff except the librarian's own, and no reply between the call and the librarian's report carries a `LEDGER` block.

```then
update:
- slug: rule-handoff
  replace:
  - old: 'Then dispatch the `librarian-guppi` agent with one line:'
    new: 'Then, in a session whose `work.md` holds `## Conserved Spec` — one that `/box` runs, as you wrote it in this turn — dispatch nothing: go back to the step of `/box` that follows `/handoff`, which merges the branch and dispatches the librarian (case 591). In any other session, dispatch the `librarian-guppi` agent with one line:'
  change: in a session that /box runs, /handoff dispatches nothing and hands back to /box (case 591.9)
- slug: estimate-handoff-dispatches
  set:
    status: pending
    purpose: /handoff stops on a dirty tree, writes handoff.md from memory into the session's folder and dispatches the librarian with its path, or, in a session that /box runs, hands back to /box, with no commit after
    method: 'by hand at the /handoff of a later session and at the /handoff of the first session that /box runs: the event log, handoff.md, the dispatch line and git log'
  change: the Criterion replaced whole — in a session that /box runs, /handoff hands back to /box (case 591.9)
```

```tasks
- [x] update `rule-handoff`
- [x] update `estimate-handoff-dispatches`
- [x] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
- [ ] read `estimate-handoff-dispatches` — by hand, at the `/handoff` of the first session that `/box` runs
```

### Case 591.10 — /box stops where its check or a merge refuses

> **given:**
> `rule-where-to-stop` — the rule of the stops; its Purpose names who imports the file, its Render is the file
> **＋** `vault/wiki/where-to-stop.md` — the file, rendered in full from `rule-where-to-stop`
> **＋** `vault/wiki/case-schema.md` — the schema that names a task opening with `stop:`
> **＋** `.claude/skills/box/SKILL.md` — the skill of `/box`, which imports the file as `/work` does
> **＋** `/box`, `/work` and `/retro` — the skills of the run
> **＋** `uv run guppi box --check` and `git merge --ff-only` — the check and the merges of `/box` that can refuse
> **＋** `raw/<date>/<hi HHMM>/spec.md` and `raw/<date>/<hi HHMM>/handoff.md` — the Spec of the run and its report
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions` — its Criterion replaced whole

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
> **＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

> **then:**
> The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
> **＋** The context of `/box`, from `.claude/skills/box/SKILL.md`, holds the same text.
> **＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
> **＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
> **＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
> **＋** In a run of `/box`, the agent stops and asks when `uv run guppi box --check` prints a line, or when a `git merge --ff-only` of `/box` refuses.
> **＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
> **＋** After the person's answer the run goes on from where it stopped.
> **＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
> **－** No other point stops the run: a red test, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

```then
update:
- slug: rule-where-to-stop
  replace:
  - old: '`/work` loads its text by an import of `vault/wiki/where-to-stop.md`,'
    new: '`/work` and `/box` load its text by an import of `vault/wiki/where-to-stop.md` (case 591),'
  - old: '`/work`, the Work readings, `/retro` and `/handoff` run in one turn.'
    new: '`/box`, `/work`, the Work readings, `/retro` and `/handoff` run in one turn.'
  - old: '5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch.'
    new: |-
      5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch.
      6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; show what stopped it, and go on after the person's word.
  change: /box imports the file, and its stops — a reason of its check, a fast-forward merge that refuses — are condition 6 (case 591.10)
- slug: estimate-where-to-stop-stops-only-on-its-conditions
  set:
    status: pending
    method: 'by hand at the first run from /work to the librarian after the render, and at the first run of /box: the context of /work and of /box, the replies of the turn and the Spec read against the Criterion, recorded in the estimate line; a condition that does not arise is named as not exercised'
  change: the Criterion replaced whole — /box imports the file, and its stops (case 591.10)
```

```tasks
- [x] update `rule-where-to-stop`
- [x] update `estimate-where-to-stop-stops-only-on-its-conditions`
- [x] `uv run guppi render`: `vault/wiki/where-to-stop.md`
- [ ] read `estimate-where-to-stop-stops-only-on-its-conditions` — by hand, at the first run of `/box`
```

### Case 591.11 — The code fence of decision-case-13 is closed

> **context:**
> `make lint` prints a `fence` finding on `decision-case-13`. A code fence opens in `## When` and is still open at the end of that section, because the text was cut off when the page was written. The defer of case 565 tied this fix to the item. The fix closes the fence with one line at the end of the section, by an `update` with a `replace` pair, as earlier Cases did on Decision pages. `estimate-lint-catches-a-broken-fence` checks that lint finds such a fence, and its Criterion stands. `estimate-sprint-migration-lint-clean` checks that lint is clean at the close of the sprint; its Criterion stands, and this sub-case removes one of the lines that keep it red. Case 587 sets how `make lint` runs its steps; this sub-case changes no step.

> **given:**
> `decision-case-13` — the Decision page whose `## When` holds the open fence
> **＋** `guppi lint` — the check whose `fence` class reads the page
> **＋** `make lint` — the target that runs `guppi lint`
> **＋** `raw/2026-10-02/1202/cases/case-587.md` — the Case of this session that sets how `make lint` runs
> **＋** `estimate-lint-catches-a-broken-fence` — the check of the `fence` class, which stands
> **＋** `estimate-sprint-migration-lint-clean` — the clean lint at the close of the sprint, which stands

> **when:**
> Someone runs `make lint` after the librarian's run of this session has applied its Spec.

> **then:**
> `guppi lint` prints no `fence` line on `decision-case-13`.
> **＋** The `## When` section of `decision-case-13` ends with a closing fence line after `<!-- rule-case-protocol -->`.
> **－** The rest of the text of `decision-case-13` stays as it was; only its History gains a line.

````then
update:
- slug: decision-case-13
  replace:
  - old: |-
      ```markdown
      <!-- rule-case-protocol -->
    new: |-
      ```markdown
      <!-- rule-case-protocol -->
      ```
  change: 'the code fence of When closed: the text was cut off when the page was written; no content change (case 591.11)'
````

```tasks
- [x] update `decision-case-13`
- [x] by hand: `make lint` after the librarian's run of this session prints no `fence` line on `decision-case-13`
```

### Case 591.12 — The Work readings of /box leave the Estimates the conserved Spec changes

> **context:**
> The Work readings of `/work` leave a reading of an Estimate that this session creates or updates. In a box session, the Estimates that the conserved Spec creates or updates are built in this session but decided in the session that conserved the Spec, and the ledger hook sees only this session's lines. Without this sub-case `/work` could take such a reading, while `/retro` (591.8) holds it back. This sub-case extends the Work readings in the same way as 591.8. 591.7 changes other sentences of the same Render, and no pair of the two touches the same sentence.

> **given:**
> `rule-work-mode` — the rule of Work Mode; its Render holds the Work readings
> **＋** `.claude/skills/work/SKILL.md` — the skill, rendered in full from `rule-work-mode`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the `W` lines of the readings
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec of the session
> **＋** `vault/raw/<date>/<HHMM>/` — the folder of a conserved Spec, with its `spec.md` and `ledger.md`
> **＋** `/box` and `/retro` — the skill that calls `/work`, and the skill whose reply carries the readings
> **＋** `vault/wiki/where-to-stop.md` — the stops of the run
> **＋** `estimate-work-mode-takes-the-work-readings` — its Criterion replaced whole

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.
> **＋** Or `/box` called `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, and the last task of that folder's `spec.md` is done.

> **then:**
> Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
> **＋** A moment of an earlier session, such as the librarian's run, has come.
> **＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and its `estimate[...]` line stands in the `LEDGER` block of the one reply that ends Retro.
> **＋** The tasks, the readings and `/retro` run in one turn, and no reply ends before the reply that ends Retro, except at a stop of `vault/wiki/where-to-stop.md`.
> **－** A reading of an Estimate this session creates or updates is not taken, and its `W` line stays open.
> **－** With a folder from `/box`, a reading of an Estimate that a decision line of that folder's `ledger.md` creates or updates is not taken either, and its `W` line stays open.
> **－** A reading whose moment has not come is not taken, and its `W` line stays open.
> **－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

```then
update:
- slug: rule-work-mode
  replace:
  - old: 'Leave a reading of an Estimate this session creates or updates, and one whose moment has not come:'
    new: 'Leave a reading of an Estimate this session creates or updates — with a folder from `/box`, one that a decision line of that folder''s `ledger.md` creates or updates too — and one whose moment has not come:'
  change: the Work readings of /box leave the Estimates that the conserved Spec creates or updates (case 591.12)
- slug: estimate-work-mode-takes-the-work-readings
  set:
    status: pending
    purpose: Whether /work, after the last task and in the same turn, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line, leaves its line to the reply that ends Retro, and leaves open the readings this session changes, or the conserved Spec that /box gives it changes, or whose moment has not come
    method: 'by hand at the first /work after the render and at the first /work that /box calls: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the Work readings of /box leave the Estimates the conserved Spec changes (case 591.12)
```

```tasks
- [x] update `rule-work-mode`
- [x] update `estimate-work-mode-takes-the-work-readings`
- [ ] read `estimate-work-mode-takes-the-work-readings` — by hand, at the first `/work` that `/box` calls
```

## Case 592 — One function of the ledger module names the person's message and a returned answer

> **context:**
> This Case re-issues Case 590.1 under a new id, with the content the person ratified last, and carries `{supersedes:case 590.1}` on each of its decision lines. The first ratification of 590.1 wrote the line `decision[case 590.1][update][rule-case-check]{ref:rule-case-check}` to the session's ledger at 13:45:27. The Case built again after the findings of `/pre-spec` no longer carries that line, since Case 589.2 takes `rule-case-check`. The ledger hook only appends, so `guppi prespec --check` reports that line with no item in the plan and refuses the exit from Plan Mode. A line is retired only by a `{supersedes:case N}`, which retires every line of Case N and takes Case N out of the plan. The person refused a hand edit of the ledger and chose this re-issue. 590.1 leaves the plan, and 590.2 and 590.3 stay as they were ratified.
> What this Case does. Three hooks read the transcript of the session, and each one needs to know where the person last spoke. The `Stop` check of `rule-case-check` reads the turn of the reply. `turn_of_reply` in `guppi/casecheck.py` starts that turn after the last `user` record that is not `isMeta` and holds more than tool results. The ledger hook of `rule-ledger-write`, and `guppi/onward.py` through it, read the stretch since the person's last message. `own_refusals` in `guppi/ledger.py` starts the stretch after the last `user` record whose `origin.kind` is `human`. `is_prompt` in `guppi/context.py` holds a third copy. A subagent's answer to a `SendMessage` comes back as a `user` record with `origin.kind` `task-notification`. The turn must start there, and the stretch must not. The three tests of the person's message already differ. In the transcript `d08a5ca5-…` of this project, the record of the local command `/clear` has string content, no `origin` and no `isMeta`. `turn_of_reply` takes it as the start of a turn, and the stretch does not. One function of `guppi/ledger.py` now names the kind of a record: the person's message by `human`, a returned answer by `task-notification`. The turn starts at either kind, and the stretch at the person's message alone. The placeholder `rule-turn-start-one-judgment` of the defer of case 586 is deleted, and the delete line keeps `{supersedes:case 586}`. The `## How it works` of `rule-ledger-write` leaves by hand as a one-off task, its mechanism moved into the docstring of `guppi/ledger.py`.
> What `case-guppi` found in the frame, as for 590.1. Over the transcripts of this project in `C:\Users\kir\.claude\projects\c--PROJECTS-GUPPI`, a Grep for a record that holds both `"isMeta":true` and `"origin":{"kind":"human"` printed no match, and neither did a Grep for one that holds both a `tool_result` and that label. So keying on `human` keeps the stretch exactly as it is. The main transcripts outside `subagents/` give different counts: 1431 records of string content not opening with `<`, against 1373 such records carrying `human`. The older transcript `71cd373f-…` holds typed messages with no `origin`, and messages with `origin.kind` `peer`. Neither kind opens a turn under this test, and a transcript with no labelled record is read whole, which makes the check looser and not stricter. A Grep of `turn_of_reply|own_refusals|given_back` over the repository outside `vault/raw/` and `vault/archive/` printed 9 files: `backlog.md`, `guppi/casecheck.py`, `guppi/ledger.py`, `guppi/onward.py`, `estimate-case-build-checks-the-finished-case.md`, `rule-case-check.md`, `rule-turn-start-one-judgment.md`, `decision-case-586.md` and `decision-case-584.md`. The Criteria of `estimate-ledger-write-lifts` and `estimate-retro-onward-sends-the-agent-to-the-handoff` define the stretch by `human` and stand. A Glob of `vault/{wiki,archive}/**/estimate-ledger-write-names-the-kind-of-a-user-record.md` printed no file, so the slug is free. A Grep of `rule-turn-start-one-judgment` over the repository outside `vault/raw/` and `vault/archive/` printed 4 files: `brief.md`, `backlog.md`, `log.md` and `decision-case-586.md`.
> Who names 590.1. The `given` of 590.2 and of 590.3 names the function of `guppi/ledger.py` "as 590.1 sets it". With 590.1 out of the plan, that pointer names a Case that is no longer in the Spec, so both need to name 592 instead. That is a change of their `given` alone. Their `when`, `then`, `tasks` and Criteria do not name 590.1. The person sees the change when the two are shown again, and it is not made by this Case. The parent context of 590 also names 590.1. Case 589.2 names 590.1 in its `given` and tasks, and it should name 592 too. The task lines and the History lines of this Case cite case 592. The content is otherwise that of 590.1 as last ratified.

> **problem:**
> A ledger line of the first ratification of 590.1 has no item in the plan, so the exit from Plan Mode is refused, and only a supersede retires it. The question answered is how 590.1 stays in force without that line: re-issued whole under a new id that supersedes it.

> **recommend:**
> - **How should the two hooks agree on the person's message?**
>   - Recommended: (a) one shared function in `guppi/ledger.py` that names the kind of a user record. The Case check starts its turn at the person's message or a returned answer, and the ledger hook and `guppi/onward.py` start at the person's message only.
>   - Answer: Agreed with the recommendations: (a).
> - **Does the token counter join the shared function?**
>   - Recommended: (a) yes. `guppi/context.py` uses the shared function with the turn boundary, and `is_prompt` is removed.
>   - Answer: Agreed with the recommendations: (a).
> - **Where is the decision recorded?**
>   - Recommended: (a) delete the placeholder, which retires its defer, and record the decision in the docstrings and the How it works of the existing rule pages.
>   - Answer: Agreed with the recommendations: (a).
> - **Which test says that a line is the person's message?**
>   - Recommended: (a) the source label: `origin.kind` `human` is the person's message, and `task-notification` is a returned answer.
>   - Answer: Agreed with the recommendations: (a).
> - **How is it checked that the fix is done?**
>   - Recommended: (a) a new Estimate for the shared test under `rule-ledger-write`, and the Criterion of `estimate-context-size-shown-after-each-reply` rewritten, in two sub-cases.
>   - Answer: Agreed with the recommendations: (a).
> - **Is the Criterion of the round check rewritten too?**
>   - Recommended: (a) a third sub-case replaces the Criterion of `estimate-case-check-refuses-text-before-a-round` whole. Its first line names the turn by the shared function, and every other line is carried word for word.
>   - Answer: (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person chose that `## How it works` leaves the Leaf pages this Case touches. What still holds moves into the docstrings of the modules, and Work Mode removes the section by hand as a one-off task. Case 589 takes the section of `rule-case-check`.
>   - Taken: the update of `rule-ledger-write` carries only its History line, a one-off task removes the section, and the update of `rule-case-check` is dropped.
> - **Change**
>   - Asked: the person refused a hand edit of the ledger, and chose to re-issue 590.1 as Case 592 with `{supersedes:case 590.1}`, with the same content.
>   - Taken: this Case holds the `given`, `when`, `then` and `tasks` of 590.1 as last ratified, each decision line carries `{supersedes:case 590.1}`, and the delete line keeps `{supersedes:case 586}`.

> **given:**
> `estimate-ledger-write-names-the-kind-of-a-user-record` — the new promise of the shared function
> **＋** `rule-ledger-write` — its `## How it works` leaves, by hand
> **＋** `rule-turn-start-one-judgment` — the placeholder of the defer of case 586, deleted
> **＋** `guppi/ledger.py` — the shared function, `own_refusals` and the module docstring
> **＋** `guppi/casecheck.py` — `turn_of_reply`, `given_back` and the module docstring
> **＋** `guppi/onward.py` — reads the stretch by `own_refusals`, unchanged
> **＋** `guppi/context.py` — the token counter, which imports the function as 590.2 sets it
> **＋** `tests/test_ledger.py` — the test over one transcript for every reader
> **＋** `tests/test_casecheck.py` — its `prompt` record
> **＋** `raw/2026-10-02/1202/cases/case-589.md` — removes the `## How it works` of `rule-case-check` into the docstring of `guppi/casecheck.py`
> **＋** `vault/wiki/rules/schema.yaml` — a Leaf drops `## How it works` at its next touch
> **＋** `rule-one-judgment-one-implementation` — the rule the change serves

> **when:**
> The `Stop` hooks `uv run guppi casecheck`, `uv run guppi ledger`, `uv run guppi onward` and `uv run guppi context` run after a reply and read the transcript at `transcript_path`.

> **then:**
> One function of `guppi/ledger.py` names the kind of a `user` record of the transcript: the person's message when its `origin.kind` is `human`, a returned answer when its `origin.kind` is `task-notification`, and neither for any other record.
> **＋** The turn of the reply, which `guppi/casecheck.py` reads for a sending and for a round, is the records after the last record that is the person's message or a returned answer.
> **＋** The stretch, which `guppi/ledger.py` and `guppi/onward.py` read for their own refusals, is the records after the last person's message, and a returned answer does not end it.
> **＋** `guppi/casecheck.py` and `guppi/context.py` import that function, `guppi/onward.py` reaches it through `own_refusals`, and no other module of `guppi/` judges `origin.kind` of a `user` record.
> **＋** One test runs `turn_of_reply`, `own_refusals` and the count of `guppi/context.py` over one transcript that holds a person's message, a returned answer, a local command with no `origin`, a `peer` message, a refusal marked `isMeta` and a tool result, and asserts where each one starts.
> **－** A record with no `origin.kind`, such as that of the local command that clears the session, a record of another kind, a record marked `isMeta` and a tool result open no turn and end no stretch.
> **－** A transcript that holds neither kind of record gives the whole transcript as the turn and as the stretch.

```then
create:
- slug: estimate-ledger-write-names-the-kind-of-a-user-record
  type: estimate
  ref: rule-ledger-write
  kind: QA
  purpose: One function of guppi/ledger.py says whether a user record of a transcript is the person's message or a returned answer, and the case check, the ledger hook, the onward hook and the token counter judge by it, so the turn and the stretch cannot drift apart
  method: uv run pytest tests/test_ledger.py -k kind; by hand, a Grep of task-notification|"human" over guppi/ that prints guppi/ledger.py alone
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  change: '## How it works left the Leaf, its mechanism in the docstring of guppi/ledger.py; the person''s message and a returned answer are named by one function of guppi/ledger.py, which the case check and the token counter import (case 592)'
delete:
- slug: rule-turn-start-one-judgment
  impact: its question is answered by the function of guppi/ledger.py, its docstring and estimate-ledger-write-names-the-kind-of-a-user-record; in vault/wiki/ only brief.md, backlog.md, log.md and decision-case-586 name it, and the supersede of case 586 retires that defer
```

```tasks
- [x] `guppi/ledger.py`: one function names the kind of a `user` record by its `origin.kind` (`human`, `task-notification`); `own_refusals` starts the stretch by it; the module docstring and the docstrings say that `guppi/casecheck.py` and `guppi/context.py` import it (case 592)
- [x] `guppi/casecheck.py`: `turn_of_reply` starts the turn after the last record that the function of `guppi/ledger.py` names the person's message or a returned answer; `given_back` judges the opener by the same function, and `NOTIFICATION` is imported from `guppi/ledger.py`; the paragraphs "How a round opens" and "A sending" of the module docstring and the docstrings of `turn_of_reply`, `opening_record` and `given_back` say so
- [x] `tests/test_casecheck.py`: `prompt` carries `origin.kind` `human`
- [x] `tests/test_ledger.py`: a test `test_kind_of_a_user_record_sets_the_turn_and_the_stretch` runs `casecheck.turn_of_reply`, `ledger.own_refusals` and `context.sizes` over one transcript with a person's message, a returned answer, the record of a local command with no `origin`, a `peer` message, a refusal marked `isMeta` and a tool result, and asserts where each one starts; a transcript with neither kind gives the whole of it
- [x] `uv run pytest tests/test_ledger.py tests/test_casecheck.py tests/test_onward.py`: green
- [x] one-off, by hand: the `## How it works` section of `vault/wiki/rules/rule-ledger-write.md` is removed, heading and text; what of it still holds and the module docstring of `guppi/ledger.py` does not yet say moves into that docstring first, with the shared function of case 592
- [x] update `rule-ledger-write`
- [x] create `estimate-ledger-write-names-the-kind-of-a-user-record`
- [x] delete `rule-turn-start-one-judgment`
- [x] read `estimate-ledger-write-names-the-kind-of-a-user-record` — in a later session: `uv run pytest tests/test_ledger.py -k kind`
```

## Case 593 — The Spec box: three sub-cases of case 591 re-issued under new ids

> **context:**
> Case 591 was ratified, then built again on the findings of `/pre-spec` and ratified again. When it was built again, three Estimates of its sub-cases got new slugs: `estimate-hi-takes-a-saved-plan` became `estimate-hi-takes-a-conserved-spec` (591.2), `estimate-spec-box-runs-a-saved-plan` became `estimate-spec-box-runs-a-conserved-spec` (591.5), and `estimate-spec-box-refuses-a-stale-plan` became `estimate-spec-box-refuses-a-stale-spec` (591.6). The ledger hook only appends, so the session's ledger still holds the three `create` lines of the first ratification under the old slugs. `guppi prespec --check` reports each of them as a line with no item in the plan, and it refuses the exit from Plan Mode. A ledger line is retired only by a `{supersedes:case N}` block, which retires every line of Case N and needs Case N out of the plan (`check_lines` and `superseded_in_window` of `guppi/prespec.py`). The person refused a hand edit of the ledger, and chose to re-issue the three sub-cases as this Case.
>
> 593.1, 593.2 and 593.3 hold the content of 591.2, 591.5 and 591.6 as last ratified, whole. Two things change. Each decision line carries `{supersedes:case 591.x}` of the sub-case it replaces. The `change` line of each `update` and `create` names `case 593.x`, since History will point to the Decision page of 593.x. The line on `rule-spec-box` keeps its `{supersedes:case 207}` … `{supersedes:case 565}` blocks, so the five defers of `rule-spec-box` are still retired. The new texts of the pages keep "case 591" where they cite the design, because 591 stays as the parent of the other sub-cases. The frame, the searches and the Estimates that stand are those of the `context` of 591, in `raw/2026-10-02/1202/cases/case-591.md`.
>
> No body of another sub-case of 591 names 591.2, 591.5 or 591.6:
> - 591.4 names `rule-spec-box` as the last child of `rule-end-of-work`, a page that 593.2 now gives its `parent`.
> - 591.3, 591.7, 591.8, 591.9, 591.10 and 591.12 name `/box`, `.claude/skills/box/SKILL.md`, `guppi/box.py` or `uv run guppi box --check`, which 593.2 and 593.3 now build.
>
> They name pages, files and skills, never a Case id, so none of them changes. Only the `context` of 591 names 591.5 as the sub-case that sets the `parent`. It is a story section, the Spec keeps it as ratified, and 593.2 now sets that field.
>
> 593.1 and 593.3 share one condition, a session with no decision line of its own but a `defer`. They state it from two sides: the agent's text at the Frontier, and the refusal of the check.

> **problem:**
> Three `create` lines of the first ratification of 591 stand in the ledger under slugs that the Case built again no longer carries, and they block the exit from Plan Mode. The ratified content of 591.2, 591.5 and 591.6 must stand under Case ids whose lines retire the old ones.

> **recommend:**
> - **What happens to the page `rule-spec-box`**
>   - Recommended: (a) archive the page and keep the idea as a note in the sprint page's backlog list.
>   - Answer: (c), build it now. The person described a branch made at once for each saved Spec, which they enter to build it, or leave while work goes on in the shared branch. They said the documentation must be settled first, since merging branches brings conflicts, and asked for a proposal.
> - **Is the broken code fence of `decision-case-13` fixed in this Case**
>   - Recommended: (a) fix it here, as a sub-case.
>   - Answer: (a), agreed.
> - **When the branch of a saved plan is made, and what it is**
>   - Recommended: (a) a plain branch made by `/carry` from the commit that saves the plan; the session stays on the shared branch.
>   - Answer: (a), with one correction: the branch is made from the commit after the whole of `/carry` is done, the brief written and the rest.
> - **How the documentation stays free of merge conflicts**
>   - Recommended: (a) only the shared branch writes the vault. Before the work, the plan's branch takes in the shared branch, pre-spec checks the plan against today's pages, and only a Case on a page whose History has a line after the save is built again and ratified again.
>   - Answer: (a). The person first wrote "4) b", then said the numbers were mixed up and confirmed (a).
> - **Where taking up a saved plan starts**
>   - Recommended: (b) from Plan Mode at any point; the session's own Cases are saved by `/carry` with their branch, then the box runs the saved plan.
>   - Answer: (b), after the person asked whether this is all one session — `/carry`, then the box.
> - **Ordinary work and a saved plan at the same time**
>   - Recommended: (a) take turns: one session at a time, on one branch at a time.
>   - Answer: (a).
> - **Who merges the plan's branch back, and when**
>   - Recommended: (a) the box skill merges at its end, after `/handoff`, runs `make test`, and the librarian runs on the shared branch; on a conflict in code it stops and asks.
>   - Answer: (a). The person asked whether the box is in essence ordinary Work Mode with git branches.
> - **Is the box a new skill around `/work`, or `/work` itself**
>   - Recommended: (a) a new skill that does the branch steps and calls `/work` with the saved plan's folder.
>   - Answer: (a), agreed.
> - **Where a Case of the saved plan built again is written**
>   - Recommended: (a) into the saved plan's folder, its file and its ledger, by the two hooks taught to write there.
>   - Answer: (a), agreed.
> - **How much of this is built in this session**
>   - Recommended: (b) a first part now — the branch made by `/carry`, the box skill, the merge back and the fence fix. The check against changed pages (Q4, Q9) is put off as a backlog item, and until then the box refuses a saved plan whose pages changed after the save.
>   - Answer: (b), agreed.
> - **Where the box writes its records when this session's own Cases were saved**
>   - Recommended: (b) for now, the box runs only in a session with no Cases of its own. Its records go into the session's own folder, and Q5 (b) comes with the later part.
>   - Answer: (b), agreed.
> - **Change**
>   - Asked: the person refused a hand edit of the ledger and agreed to re-issue 591.2, 591.5 and 591.6 as a new Case. Each of its decision lines supersedes the sub-case it replaces, with the same content; the line of `rule-spec-box` keeps its five blocks of the defers; the other sub-cases of 591 stay.
>   - Taken: Case 593 with 593.1, 593.2 and 593.3, the content of 591.2, 591.5 and 591.6 whole. Each decision line carries `{supersedes:case 591.x}`, and the `change` lines name `case 593.x`.

### Case 593.1 — A conserved Spec is taken whole at the Frontier

> **given:**
> `rule-skill-hi` — the rule of `/hi`; its Render is the skill that assembles the Frontier
> **＋** `.claude/skills/hi/SKILL.md` — the skill, rendered in full from `rule-skill-hi`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier and its closers
> **＋** `vault/wiki/backlog.md` — the list that names each conserved Spec and its `spec.md`
> **＋** `guppi/ratified.py` — the guard that lets the plan file be created with one title line only
> **＋** `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md` — the title line of the plan file of a box session
> **＋** `/box` — the skill that runs the conserved Spec
> **＋** `/pre-spec` — the check that closes Plan Mode
> **＋** `estimate-hi-takes-a-conserved-spec` — the new promise

> **when:**
> In a session that `/hi` opened from `.claude/skills/hi/SKILL.md` as rendered from `rule-skill-hi`, the person takes a conserved Spec of `## Cases` of `raw/<date>/<hi HHMM>/frontier.md`.

> **then:**
> The agent takes the Spec whole, to be run by `/box`, only while the session's ledger holds no decision line other than a `defer`, and after it ratifies no Case but a short-form defer.
> **＋** It closes the line of that Spec `[x] … · work`.
> **＋** It creates the plan file with one title line, `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, the path that `vault/wiki/backlog.md` names for that Spec.
> **＋** It closes each other open line under `## Cases` as left — `[-] … · backlog · kept`, `[-] … · sprint · defer` or `[-] … · defer case N` — and goes on to `/pre-spec`.
> **－** No Case of the conserved Spec is built again or ratified again in this session.
> **－** `.claude/skills/hi/SKILL.md` equals the Render of `rule-skill-hi` and is not edited by hand.

```then
create:
- slug: estimate-hi-takes-a-conserved-spec
  ref: rule-skill-hi
  kind: QA
  purpose: Whether a session takes a conserved Spec of the Frontier whole — only with no decision line of its own but a defer, its line closed, the plan file created with a title line that names the conserved spec.md, the other lines closed as left
  method: 'uv run guppi render --check; by hand, at the first session whose person takes a conserved Spec at the Frontier: frontier.md, the title line of the plan file and the session''s ledger read against the Criterion'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-skill-hi
  replace:
  - old: Wait for the human to pick the order or defer items. Every Case is built by `case-guppi` (`rule-case-build`).
    new: 'Wait for the human to pick the order or defer items. Every Case is built by `case-guppi` (`rule-case-build`). A conserved Spec on `## Cases` is taken whole and run by `/box` (`rule-spec-box`, case 591): take it only while the session''s ledger holds no decision line other than a `defer`, and ratify no Case after it but a short-form defer; close its line `[x] … · work`; create the plan file with one title line, `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, the path `backlog.md` names; close the other open lines under `## Cases` as left, and go on to `/pre-spec`.'
  change: a conserved Spec is taken whole at the Frontier, named in the title line of the plan file, and run by /box (case 593.1)
```

```tasks
- [x] update `rule-skill-hi`
- [x] create `estimate-hi-takes-a-conserved-spec`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-takes-a-conserved-spec` — by hand, at the first session that takes a conserved Spec at the Frontier
```

### Case 593.2 — /box runs a conserved Spec on its branch and merges it back

> **given:**
> `rule-spec-box` — the placeholder, built as the rule of `/box`; its Render is the skill
> **＋** `.claude/skills/box/SKILL.md` — the skill, rendered in full from `rule-spec-box`
> **＋** `rule-end-of-work` — the parent of `rule-spec-box`
> **＋** `vault/raw/<date>/<HHMM>/` — the folder of the conserved Spec, the argument of the skill
> **＋** `spec/<date>-<HHMM>` — the branch of the conserved Spec, made by `/carry`
> **＋** `rule-spec-capture` — the hook whose line after `ExitPlanMode` calls the skill
> **＋** `git switch`, `git merge --ff-only` and `git branch -d` — the branch steps of the skill
> **＋** `uv run guppi box --check` — the check the skill runs first
> **＋** `/work`, `/retro` and `/handoff` — the skills of the run the box calls
> **＋** `librarian-guppi` — the librarian, dispatched by the skill on the shared branch
> **＋** `vault/wiki/` — the pages, which the branch of the Spec does not write
> **＋** `entity-sprint-migration` — its Backlog line on `rule-spec-box`
> **＋** `estimate-spec-box-runs-a-conserved-spec` — the new promise

> **when:**
> The agent calls `/box` on `PreToolUse Skill` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, on the line that the hook of `rule-spec-capture` printed after `ExitPlanMode`, and runs `.claude/skills/box/SKILL.md` as rendered from `rule-spec-box`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/box/SKILL.md` equals the Render of `rule-spec-box`.
> **＋** The agent first runs `uv run guppi box --check` on the folder; when it prints a line, the agent changes nothing, shows the lines and asks the person.
> **＋** Otherwise the agent commits the tree, runs `git switch` to `spec/<date>-<HHMM>`, and brings that branch up to the branch it came from by `git merge --ff-only`; when the merge refuses, it switches back, shows the refusal and asks the person.
> **＋** It calls `/work` with the folder, and Work Mode, the Work readings, `/retro` and `/handoff` run in one turn.
> **＋** After `handoff.md` stands, it switches back, brings the branch it came from up to `spec/<date>-<HHMM>` by `git merge --ff-only`, deletes `spec/<date>-<HHMM>` by `git branch -d` and runs `make test`; a merge that refuses is a stop.
> **＋** Then it dispatches `librarian-guppi` with the path of the session's `handoff.md`, and shows the librarian's report unchanged with the exit code of `make test`.
> **－** Nothing under `vault/wiki/` is written on `spec/<date>-<HHMM>`, and the librarian runs once, on the branch the session came from.
> **－** No commit follows the handoff but the librarian's own.

```then
create:
- slug: estimate-spec-box-runs-a-conserved-spec
  ref: rule-spec-box
  kind: QA
  purpose: Whether /box checks a conserved Spec, runs it on its own branch brought up to the shared branch by a fast-forward, merges the branch back by a fast-forward after the handoff, and has the librarian write the pages on the shared branch, stopping when the check or a merge refuses
  method: 'uv run guppi render --check; by hand, the first session that takes a conserved Spec at the Frontier and runs it by /box: git log, the branches, the folders of the session and of the conserved Spec, the dispatch line and the librarian''s commit, recorded in the estimate line'
  tags:
  - session
  - workflow
  - git
  - harness
update:
- slug: rule-spec-box
  set:
    kind: Leaf
    enforcement: render
    governs: .claude/skills/box/SKILL.md
    render_mode: full
    implementation_ref:
    - guppi/box.py
    - tests/test_box.py
    parent: '[[rule-end-of-work]]'
    tags:
    - session
    - workflow
    - git
    - harness
    - render
    purpose: Prevents a conserved Spec from being built on a branch that lacks the current vault, or its pages from being written anywhere but on the shared branch
  sections:
    Purpose: 'Prevents a conserved Spec from being built on a branch that lacks the current vault, and its pages from being written anywhere but on the shared branch. `/carry` conserves a Spec whose work is not done and makes its branch `spec/<date>-<HHMM>` at the commit that conserves it. A later session takes the Spec at the Frontier, and `/box` runs it: it checks the Spec, switches to its branch, brings that branch up to the shared branch by a fast-forward, runs `/work` on the Spec, and after `/handoff` brings the shared branch up to the Spec''s branch by a fast-forward and hands the session to the librarian there. One session runs at a time, in one folder of the repository, so both merges are fast-forwards and the vault has one writer; the shared branch is never `main`. The check refuses a Spec whose pages changed after it was conserved, and a session that ratified a Case of its own: in this first part a Case of the Spec is not checked again or built again, and the readings, lessons and handoff of the session go into the session''s own folder, which the librarian applies. Both wait for a second part, a line of the Backlog of `entity-sprint-migration` (case 591).'
    Render: |-
      <!-- rule-spec-box -->
      ---
      name: box
      description: Run a conserved Spec on its own branch — check it, switch to the branch and bring it up to date, run /work on it, merge the branch back and hand the session to the librarian. The agent calls it on the line that the hook of rule-spec-capture prints after ExitPlanMode.
      ---


      @vault/wiki/where-to-stop.md

      Branch: !`git branch --show-current`

      The argument is the folder of a conserved Spec, `vault/raw/<date>/<HHMM>/`, which the line printed after `ExitPlanMode` names. The branch above is the shared branch: the session leaves it here and comes back to it at the end. The branch of the Spec is `spec/<date>-<HHMM>`, the date and time of that folder, made by `/carry`. Nothing under `vault/wiki/` is written on the branch of the Spec: the librarian writes the pages once, on the shared branch.

      1. Run `uv run guppi box --check <folder> --session <id>`, the id being the eight characters of the `hi:` line of this session. Each line it prints is a reason the Spec cannot run now. When it prints one, change nothing: show the lines and ask the person.
      2. Commit the tree: `chore(session): session <hi HHMM> takes the conserved Spec of <folder>`.
      3. Run `git switch spec/<date>-<HHMM>`, then `git merge --ff-only <shared branch>`. When the merge refuses, run `git switch <shared branch>`, show the refusal and ask the person.
      4. Call `/work` with the folder as its argument. Work Mode, the Work readings, `/retro` and `/handoff` run as their skills say, in one turn; `/handoff` dispatches nothing and comes back here.
      5. Run `git switch <shared branch>`, then `git merge --ff-only spec/<date>-<HHMM>`. When the merge refuses, show the refusal and ask the person. Then run `git branch -d spec/<date>-<HHMM>` and `make test`.
      6. Dispatch the `librarian-guppi` agent with one line: `Materialize <hi date> from vault/raw/<hi date>/<hi HHMM>/handoff.md.`. Wait for its report and show it to the person unchanged, then one line with the exit code of `make test`. Do not commit after this, and write no `LEDGER` block.

      The stops of steps 1, 3 and 5 are condition 6 of `vault/wiki/where-to-stop.md`.
      <!-- /rule-spec-box -->
  change: 'built from the placeholder: /box runs a conserved Spec on its branch and merges it back before the librarian, first part; a child of rule-end-of-work (case 593.2)'
- slug: entity-sprint-migration
  replace:
  - old: '- [[rule-spec-box]] — the Spec box, case 207, after Slice 3b'
    new: '- [[rule-spec-box]] — the Spec box, its second part: a conserved Spec checked against the pages changed after it was conserved, a Case on such a page built again, ratified again and written into the folder of the conserved Spec, and a conserved Spec taken after other Cases of its session (case 591)'
  change: the Backlog line of rule-spec-box names its second part (case 593.2)
```

```tasks
- [x] update `rule-spec-box`
- [x] update `entity-sprint-migration`
- [x] create `estimate-spec-box-runs-a-conserved-spec`
- [x] `uv run guppi render`: `.claude/skills/box/SKILL.md`
- [ ] read `estimate-spec-box-runs-a-conserved-spec` — by hand, at the first session that runs a conserved Spec by `/box`
```

### Case 593.3 — guppi box --check refuses a conserved Spec that cannot run now

> **given:**
> `guppi/box.py` — the check of a conserved Spec
> **＋** `guppi/cli.py` — the table of the `guppi` commands
> **＋** `guppi/materialize.py` — `is_carried_over`, the one judgment of a folder marked by `carry.md`
> **＋** `tests/test_box.py` — the tests of the check
> **＋** `vault/raw/<date>/<HHMM>/spec.md` — the conserved Spec, its `then` blocks and its Case headings
> **＋** `vault/raw/<hi date>/<hi HHMM>/ledger.md` — the ledger of the session that runs the check
> **＋** `spec/<date>-<HHMM>` — the branch of the conserved Spec, made by `/carry`
> **＋** `main` — the branch that is never the shared branch
> **＋** `estimate-spec-box-refuses-a-stale-spec` — the new promise

> **when:**
> Someone runs `uv run guppi box --check <folder> --session <id>`, where `<folder>` is a folder `vault/raw/<date>/<HHMM>/` and `<id>` is the session id of a `hi` line.

> **then:**
> It prints one line for each reason the Spec cannot run now, and exits 1 when it prints any; with no reason it prints nothing and exits 0.
> **＋** A folder that `is_carried_over` of `guppi/materialize.py` does not judge marked is one reason, and so is a folder for which no branch `spec/<date>-<HHMM>` exists.
> **＋** A current branch `main` is one reason: the shared branch is never `main`.
> **＋** A decision line other than a `defer` in the ledger of the session's folder is one reason, naming its Case.
> **＋** A live page named by an `update`, `delete` or `defer` item of the folder's `spec.md` is one reason when a line of its History names the Decision page of a Case whose number, in its whole part, is higher than that of every Case of that Spec; the line names the page and that Decision page.
> **＋** A slug that a `create` item of that Spec names and a live page carries is one reason, naming the slug.
> **－** The check writes nothing, switches no branch, and opens no page beyond those the Spec names.

```then
create:
- slug: estimate-spec-box-refuses-a-stale-spec
  ref: rule-spec-box
  kind: QA
  purpose: Whether guppi box --check refuses a conserved Spec whose folder lacks carry.md or its branch, a run from main, a session that ratified a Case of its own, a page of the Spec changed by a later Case, and a page the Spec creates that now stands — and passes any other
  method: uv run pytest tests/test_box.py
  tags:
  - session
  - workflow
  - git
  - harness
```

```tasks
- [x] `guppi/box.py` — `check(project_dir, folder, session)` and `run`, by the `then` above; the folder judged by `is_carried_over` of `guppi/materialize.py`, the branches by `git branch --show-current` and `git branch --list`, the ledger window of the session the way `guppi prespec --check` finds it, the items by the parser of the `then` blocks that `guppi materialize` uses; the module docstring names `rule-spec-box`
- [x] `guppi/cli.py` — the command `box`
- [x] `tests/test_box.py` — each reason alone and its line; a clean folder, exit 0 and no output; a `defer` line of the session not counted; a History line of a Case of the Spec itself, and a `cascade` line, not counted
- [x] create `estimate-spec-box-refuses-a-stale-spec`
- [x] read `estimate-spec-box-refuses-a-stale-spec` — `uv run pytest tests/test_box.py`, in a later session
```

## Deferred

## Case 594 — How to retire a ledger line of a Case ratified again waits for a later session

> **context:**
> At `/pre-spec` of session 1202, Cases 590 and 591 were built again on its findings and ratified again. Case 590.1 no longer carried its `update` of `rule-case-check`, and three Estimates of 591.2, 591.5 and 591.6 got new slugs. The ledger hook only appends, so the lines of the first ratification stayed in `raw/2026-10-02/1202/ledger.md`, and `guppi prespec --check` refused the exit from Plan Mode. A line is retired only by `{supersedes:case N}`, which retires every line of Case N and takes Case N out of the plan (`check_lines` of `guppi/prespec.py`). So the four sub-cases were re-issued as Cases 592 and 593. The person asked to think later about a better mechanism.

> **problem:**
> The decision on how a Case ratified again with fewer or renamed items retires the lines of its first ratification, without a new Case that supersedes it whole, is put off.

```then
defer:
  - slug: rule-ledger-line-withdrawn-on-re-ratification
    type: rule
    purpose: "Prevents a decision line of the first ratification of a Case from standing in the ledger after the Case is ratified again without its item, so that a rename or a dropped item does not need a new Case that supersedes the whole one"
```
