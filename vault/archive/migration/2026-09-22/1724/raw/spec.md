<!-- approved 20:42:54 · session 4d9fe4e8 -->

# Spec — 2026-09-22, session 1724

## Case 324 — the hand fix of commit 94277ea ratified after the fact

> **context:**
> `rule-atomicity` is a page with `render_mode: partial`: its `## Render` is spliced into `case-schema.md`, and `own_text` in `guppi/render.py` takes the text between the page's own markers `<!-- rule-atomicity -->` … `<!-- /rule-atomicity -->`, while the parent `full` page carries one marker line per child, which the renderer replaces with the child's text and its markers. Case 317 wrote `sections.Render` from the heading, with no marker pair, and put both lines into the Render of the parent `rule-case-protocol`. `plan()` raised before the first write, so `guppi render` in the librarian's run of session 1121 wrote no governed file: `CLAUDE.md`, `case-schema.md`, three `schema.yaml` and the three harness files stayed at the text of the previous session. Commit `94277ea` fixed this by hand, outside the librarian's run: the markers added to `rule-atomicity`, the extra closing line removed from `rule-case-protocol`.
> Both pages stand `draft`; `render --check`, `sprint --check` and `glossary --check` exit 0. `estimate-atomicity-rendered` stands `pending`, and its Criterion already states this state — "`rule-case-protocol` is a MOC with the child `rule-atomicity` and a marker line in its Render"; the Case touches neither it nor the four Estimates of `rule-case-protocol`.

> **problem:**
> The text on disk is right, but nothing is signed under it. The fix went past `materialize` and `generate`, so neither page carries a History line and no Decision page exists for `origin` and History to reach. The gap closes either by signing the text as it stands, or by a change that makes `render` place a partial's markers itself.

> **given:**
> `rule-render-harness`: a page with `enforcement: render` carries the text of its file in `## Render` between `<!-- slug -->` and `<!-- /slug -->`; in a `full` page a lone `<!-- child -->` line is replaced by the child's text, the markers kept.
> **＋** `generate` accepts an `update` carrying one `change`: it writes the History line and saves the page, leaving the body untouched.
> **＋** `replace` needs exactly one occurrence of `old`, and the text before the fix is no longer on disk.
> **＋** `estimate-atomicity-rendered` already holds the promise of this render and stands `pending`.

> **when:**
> `guppi generate` applies the entries of this session.

> **then:**
> `rule-atomicity` carries its `## Render` wrapped in `<!-- rule-atomicity -->` … `<!-- /rule-atomicity -->`, the text as it stands on disk, and a History line leading to this decision.
> **＋** `rule-case-protocol` carries a History line for the removed closing marker; its body does not change.
> **＋** `decision-case-324` binds both pages to the decision.
> **－** The Criterion of `estimate-atomicity-rendered` is not replaced and its status is not touched: the promise is the same.
> **－** `guppi/render.py` does not change.

```then
update:
  - slug: rule-atomicity
    sections:
      Render: |
        <!-- rule-atomicity -->
        ## Atomicity — when a unit splits

        A unit stays whole as long as its closing act — ratification, a reading, `built` — is one indivisible judgment. The moment it breaks into two or more conditions that can fail independently and need different fixes, it splits into children.

        The test is mechanical. List the conditions of "done". For each pair, ask: could one fail while the other passes, and would the fix be a different one? Yes for any pair — split.

        It holds for a Case, an Entity, a Rule and an Estimate alike. Not for a Lesson: a recorded fact does not split. Not for an Insight: it is born by clustering, which is this rule running in reverse. Depth is not fixed in advance — it follows the rule and nothing else. Two conditions that are different behaviours are two children; the same behaviour checked from two angles is one page and two Estimates.
        <!-- /rule-atomicity -->
    change: the Render carries its own markers, so the page renders into case-schema.md — the hand fix of commit 94277ea signed after the fact (case 324)
  - slug: rule-case-protocol
    change: the extra closing marker of rule-atomicity removed from the Render, a parent carrying one marker line per child — the hand fix of commit 94277ea signed after the fact (case 324)
```

```tasks
- [x] update `rule-atomicity` — `sections: Render`, the text as it stands on disk, with its markers
- [x] update `rule-case-protocol` — one `change`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Case 325 — a rendering page without its own markers is refused

> **context:**
> `own_text` in `guppi/render.py` asks the same of each of the 32 pages with `enforcement: render`: its `## Render` opens with `<!-- slug -->` and closes with `<!-- /slug -->`. A parent `full` page carries one line per child — the opening marker — which `render_full` replaces with the child's text and its markers. Neither `pre-spec` nor `materialize`, `generate` or `lint` looks inside `sections.Render`: to a schema it is free prose. Case 317 wrote the child without markers and the parent with a pair; only `render` refused, at the end of the session, and it refused whole — `plan()` raises before the first write, so every governed file went stale at once. The other half of the same error is never caught: `render_full` sends an unmatched closing line to its `else` branch and copies it into the governed file.
> `rule-prespec` stands `built` with six Estimates, one per finding; `rule-lint` stands `built` with the single `estimate-lint-catches` (`passed`, read 2026-09-22), whose Criterion enumerates the classes while the order lives in the docstring of `guppi/lint.py`; the body of `rule-lint` names no class. Case 324 signed the text of both damaged pages but set no guard.

> **problem:**
> An error in the markers survives to the last step of the pipeline, and one kind of it is never caught at all. Two guards are needed in two places: one reads the plan before the Spec is approved, the other reads the pages on disk, by any route, a hand edit included.

### Case 325.1 — `pre-spec` refuses a Render written without its markers

> **given:**
> `check_form` already reads the items of the plan's `then` blocks and knows `live_page` and `read_category`: it can read the target page.
> **＋** In a `create` the fields `enforcement` and `render_mode` stand in the item itself; in an `update` they are read from the page.
> **＋** The check judges only the text the item itself writes, and does not simulate the Spec in entry order.
> **＋** `rule-prespec` carries `enforcement: render` and renders `.claude/skills/pre-spec/SKILL.md`; the new finding belongs in its Render.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the plan before the Spec is approved.

> **then:**
> An item of a `then` block carrying `sections: Render`, whose target is a page with `enforcement: render`, whose text does not open with `<!-- slug -->` and close with `<!-- /slug -->`, gives one line: `case N: <create|update> <slug>: Render is not wrapped in <!-- slug --> … <!-- /slug -->`.
> **＋** A target without `enforcement: render` gives no finding.
> **＋** A wrapped text is silent; exit 0 on a clean plan stands.
> **－** The child's marker line in the parent is not checked here: its true value is known only after every item of the Spec is applied.

```then
create:
  - slug: estimate-prespec-catches-an-unwrapped-render
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: Whether pre-spec refuses an item that writes a Render without the page's own markers
    method: pytest in tests/test_prespec.py — a create and an update with an unwrapped Render, a wrapped one clean
    tags: [harness, workflow]
update:
  - slug: rule-prespec
    replace:
      - old: "for every `update` item carrying `file` — the file route is gone (case 320),"
        new: "for every `update` item carrying `file` — the file route is gone (case 320), for every item of a `then` block carrying `sections: Render` whose target is a page with `enforcement: render` and whose text does not open with `<!-- slug -->` and close with `<!-- /slug -->` (case 325.1),"
    change: a finding for a Render written without the page's own markers (case 325.1)
```

```tasks
- [x] update `rule-prespec` — the replace pair in the Render, the finding after the `file` item
- [x] create `estimate-prespec-catches-an-unwrapped-render`, `ref: rule-prespec`
- [x] `guppi/prespec.py` — the check on the pattern of `check_form`, wired into `check()`
- [x] `tests/test_prespec.py` — a create with an unwrapped Render, an update writing `sections: Render` unwrapped, a wrapped one clean
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-catches-an-unwrapped-render`
```

### Case 325.2 — `lint` finds an unwrapped Render and a stray closing marker

> **given:**
> `lint` reads every live page of `wiki/<category>/` and writes nothing; a finding is one line, `<category>/<slug>: <class>: <what>`.
> **＋** The classes and their order live in the docstring of `guppi/lint.py`; the body of `rule-lint` does not enumerate them.
> **＋** The Criterion of `estimate-lint-catches` enumerates the classes as `＋` lines; by case 296 a `replace` pair inside the Criterion changes a part and sets the page `pending`.
> **＋** `render_full` raises only on a missing marker line for a child.

> **when:**
> `uv run guppi lint` reads the live pages of the vault.

> **then:**
> A page with `enforcement: render` with no `## Render` section, or whose text does not open and close with its own marker pair, gives a finding of the class `markers`.
> **＋** A page with `render_mode: full` whose Render carries a closing marker line `<!-- /child -->` for one of its `children` gives a finding of the same class: a parent carries one opening line per child.
> **＋** Exit 1 on any finding, 0 and silent on a clean vault; nothing is written.
> **－** `render.py` does not change, and `make lint` does not change the order of its steps.

```then
update:
  - slug: rule-lint
    change: the class `markers` — a Render not wrapped in the page's own markers, and a closing marker line for a child in a full page (case 325.2)
  - slug: estimate-lint-catches
    replace:
      - old: "**＋** `path`: a file of `implementation_ref` or `governs` that does not exist."
        new: |-
          **＋** `path`: a file of `implementation_ref` or `governs` that does not exist.
          **＋** `markers`: a page with `enforcement: render` whose `## Render` is absent, or whose text does not open with `<!-- slug -->` and close with `<!-- /slug -->`; a page with `render_mode: full` whose Render carries a closing marker line `<!-- /child -->` for one of its `children` — a parent carries one opening line per child (case 325.2).
    change: the class `markers` added to the Criterion (case 325.2)
```

```tasks
- [x] update `rule-lint` — one `change`
- [x] update `estimate-lint-catches` — the replace pair inside the Criterion, the new class
- [x] `guppi/lint.py` — the check of the class `markers`, the class named in the docstring
- [x] `tests/test_lint.py` — an unwrapped Render, a stray closing marker in a full page
- [ ] read `estimate-lint-catches`
```

## Case 326 — a reading closes the lines of its slug in every live Spec

> **context:**
> `tick_read` walks the Specs of `raw/`: the Spec beside the yaml first, then the folders of the other sessions, oldest first — and stops at the first that holds a line of the slug; inside it every line of that slug is ticked, because "one reading is of the page, whose Criterion is one, however many Cases of the session touched it" (case 312). The archive is not read. When a promise is changed twice in two sessions, the line of the older Spec no longer belongs to its Case and no new reading reaches it: session 0014 left two such lines, 1105 and 1544, and today's reading of `estimate-harness-pipeline` would leave the second of them open.
> `rule-page-generation` stands `draft` with nine Estimates; the promise of the ticker is `estimate-generate-ticks-the-spec`, `passed`, read 2026-09-22; its Criterion covers the page lines as well as the reading lines, so the Case changes a part of it with a `replace` pair, as case 296 allows. The other eight Estimates of `rule-page-generation` are not touched.

> **problem:**
> The `read` line of the older Spec never closes: its Criterion is gone, and a new reading never reaches it. Refusing the form is no answer — the second Case is at no fault, the promise honestly changed twice, and the older line could only be resolved by editing another session's Spec, which its own rule does not allow.

> **given:**
> `tick_read` reads the Specs of `raw/` in order: the Spec beside the yaml, then the folders of the other sessions, oldest first; the archive is not read (cases 270.1, 312).
> **＋** `guppi archive` takes only units dated before the day of the run, so a Spec of the same day stays live.
> **＋** A reading is of the page: its Criterion is one, whichever Case replaced it last.
> **＋** The skips stand: in the Spec beside the yaml, the section of a Case ratified after the reading (case 280); in any Spec, the section of a Case marked `superseded_by` (case 286).

> **when:**
> `guppi generate` applies an `estimate` entry, or a `create` with a folded reading.

> **then:**
> Every unticked `- [ ] read `<slug>`` line of that slug becomes `- [x]` in every live Spec of `raw/`, not only in the first that holds one.
> **＋** The order of the walk stands: the Spec beside the yaml, then the folders of the other sessions, oldest first.
> **＋** Both skips stand.
> **－** The archive is not read: an archived Spec keeps its open line as the record of a task nobody performed.
> **－** A line naming several slugs still matches the first alone: not this Case.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: "every unticked `- [ ] read `<slug>`` line of the first Spec that holds one"
        new: "every unticked `- [ ] read `<slug>`` line of every live Spec of `raw/`"
      - old: "however many Cases of the session touched it (case 312)"
        new: "however many Cases and however many sessions touched it (cases 312, 326)"
    change: a reading ticks the lines of its slug in every live Spec of raw/, not in the first that holds one (case 326)
  - slug: estimate-generate-ticks-the-spec
    replace:
      - old: "every unticked line `- [ ] read `<slug>`` of the first Spec that holds one becomes `- [x]`"
        new: "every unticked line `- [ ] read `<slug>`` of every live Spec of `raw/` becomes `- [x]`"
      - old: "one Spec per entry, every line of the slug in it but those in the section of a Case ratified after the reading or superseded (case 312)."
        new: "every line of the slug in each, but those in the section of a Case ratified after the reading or superseded; the archive is not read (cases 312, 326)."
    change: the walk of the Specs in the Criterion — every live Spec, not the first that holds one (case 326)
```

```tasks
- [x] update `rule-page-generation` — the replace pair in the sentence on the ticker
- [x] update `estimate-generate-ticks-the-spec` — the replace pair inside the Criterion
- [x] `guppi/generate.py` — `tick_read` walks every Spec; the docstring
- [x] `tests/test_generate.py -k tick` — two Specs with a line of one slug, both tick
- [ ] read `estimate-generate-ticks-the-spec`
```

## Case 327 — `pre-spec` knows a reading's task line as `generate` ticks it

> **context:**
> `check_tasks` finds the task line of an Estimate by substring: `slug in line` over every line of the `tasks` block. `generate` matches otherwise — `READ_LINE` takes the first backticked slug of a `- [ ] read …` line and compares it for equality. The gap passes two things: a `read` line naming several Estimates (line 959 of the 1121 Spec names three), and an Estimate the block names by an `update` line alone, with no reading line at all. In the first the reading of the first slug closes the box for all three, while the other readings tick nothing and say nothing; in the second there is no reading line and pre-spec is content. The form — one line per reading, by its slug — is written in the Case schema; nothing guards it.
> `rule-prespec` stands `built` with six Estimates, one per finding; the promise of the `tasks` block is `estimate-prespec-checks-the-plan`, `passed`, whose Criterion also covers the finding for a missing `tasks` block, so the Case changes a part of it with a `replace` pair (case 296). Case 325.1 of this session writes its own pair into the same Render, at the clause that follows this one; the anchors do not overlap.

> **problem:**
> Two scripts disagree on what the task line of a reading is, and both forms fall through the gap: a line of three slugs, and an Estimate with no line of its own. The check must judge as the ticker ticks.

> **given:**
> `check_tasks` finds a task line by substring over every line of the `tasks` block (case 59.3).
> **＋** `generate` ticks by `READ_LINE`: the first backticked slug of a `- [ ] read …` line, compared for equality (cases 226.1, 270.1).
> **＋** The Case schema asks one task line per reading of an Estimate, by its slug.
> **＋** `rule-prespec` carries `enforcement: render` and renders `.claude/skills/pre-spec/SKILL.md`.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the plan before the Spec is approved.

> **then:**
> An Estimate a `then` block creates or sets `pending`, with no line `- [ ] read `<slug>`` in its `tasks` block whose first backticked slug is that Estimate, gives the finding `case N: <slug> has no task line`.
> **＋** A slug named on the read line of another Estimate gives the finding in its own words: `case N: <slug> is named on another read line, not its own`.
> **＋** A mention of the slug on an `update` line, or on any line that is not a read line, is no task line.
> **－** `generate` does not change: the check catches up with the ticker, not the other way round.
> **－** Line 959 of the 1121 Spec is not rewritten: a Spec is written by the hook, by Work Mode's ticks and by the agent under `## Deferred`, and by nobody else.

```then
update:
  - slug: rule-prespec
    replace:
      - old: "for every Estimate a `then` block creates or sets `pending` that no task names,"
        new: "for every Estimate a `then` block creates or sets `pending` with no task line of its own — a line `- [ ] read `<slug>`` whose first backticked slug is that Estimate, as `generate` matches it when it ticks; a slug named on another Estimate's read line, or on a line that is not a read line, has no task line of its own (case 327),"
    change: a reading's task line is matched as generate ticks it — one line per slug (case 327)
  - slug: estimate-prespec-checks-the-plan
    replace:
      - old: "an Estimate a `then` block creates or sets `pending` with no task line naming its slug."
        new: "an Estimate a `then` block creates or sets `pending` with no line `- [ ] read `<slug>`` whose first backticked slug is that Estimate, as `generate` matches it when it ticks; a slug named on another Estimate's read line gives the finding in its own words (case 327)."
    change: the task line of a reading in the Criterion — matched as generate ticks it (case 327)
```

```tasks
- [x] update `rule-prespec` — the replace pair in the Render, the clause on the task line
- [x] update `estimate-prespec-checks-the-plan` — the replace pair inside the Criterion
- [x] `guppi/prespec.py` — `check_tasks` matches a read line as `generate` does, with the second wording
- [x] `tests/test_prespec.py` — a read line of three slugs; an Estimate named by an `update` line alone; a proper read line clean
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-checks-the-plan`
```

## Case 328 — the cascade counts the live Estimates alone

> **context:**
> The cascade of `generate` builds its map of Estimates from the live files of `wiki/estimates/` and already passes over a slug with no page. An Estimate a `delete` of the same run marked `archived` is still a file in that folder, and still a slug in the target's list — and it spoils the count: `all_passed` is false and the page falls back to `draft`. The slug is taken out of the list by `cleanup`, which runs after `generate`, so until the next run the rule stands `draft` while every live promise is `passed`. This is the lint finding on `rule-materialize`: its eleven live Estimates are all `passed`, and the twelfth, retired by case 320, dragged the page down with it.
> `rule-page-generation` stands `draft` with nine Estimates; the promise of the cascade is `estimate-generate-cascades`, `passed`. Case 326 of this session changes the sentence on the ticker of the same page — another place, no overlap. The mechanism of the cascade is not spelled out on the page, which points at the docstring of `guppi/generate.py`, so the Criterion is what changes and the page takes a History line.

> **problem:**
> Deleting an Estimate drops its target to `draft` for a whole session, though every live promise of the target holds. The symptom heals itself — tonight's run sees eleven `passed` and returns `built` — but it returns with every later `delete` of an Estimate, and each time it costs a lint finding, a flag in the brief and an item of the Frontier.

> **given:**
> The cascade builds its map from the live files of `wiki/estimates/` and already passes over a slug with no page.
> **＋** A `delete` sets the Estimate `archived`; `guppi cleanup` moves the file and takes the slug out of the target's list, and it runs after `generate`.
> **＋** The cascade gives `built` when every Estimate of the list is `passed`, and `draft` otherwise.

> **when:**
> `guppi generate` runs its cascade after all entries.

> **then:**
> An Estimate standing `archived` is not counted.
> **＋** A page whose live Estimates are all `passed` becomes `built` in the same run that retired another of its Estimates.
> **＋** A page left with no live Estimate keeps its status, as it does today.
> **－** The order of the librarian's frame does not change: `cleanup` still runs after `generate`.

```then
update:
  - slug: rule-page-generation
    change: the cascade counts the live Estimates alone — one standing archived is not counted (case 328)
  - slug: estimate-generate-cascades
    replace:
      - old: "An entity or rule whose Estimates are all `passed` becomes `built`; a `built` one with an Estimate not `passed` returns to `draft`; History `status: a → b · cascade`."
        new: "An entity or rule whose live Estimates are all `passed` becomes `built`; a `built` one with a live Estimate not `passed` returns to `draft`; an Estimate standing `archived` — one a `delete` of the same run retired, its file still under `wiki/estimates/` until `cleanup` — is not counted, as a slug with no page is not counted (case 328); History `status: a → b · cascade`."
    change: the archived Estimate out of the count in the Criterion (case 328)
```

```tasks
- [x] update `rule-page-generation` — one `change`
- [x] update `estimate-generate-cascades` — the replace pair inside the Criterion
- [x] `guppi/generate.py` — the cascade passes over an `archived` Estimate; the docstring
- [x] `tests/test_generate.py` — a rule with one archived Estimate and the rest passed becomes `built`
- [ ] by hand, after the librarian's run: `rule-materialize` stands `built`, with no lint finding on it
- [ ] read `estimate-generate-cascades`
```

## Case 329 — the `method` of this Estimate names its reading

> **context:**
> `check_method` in lint takes one of four things for the Estimate of a Leaf: a file under `tests/`, the word `pytest`, a `make <target>` of the Makefile, or a reading — and a reading is recognised literally, by the words `by hand` or `reading` in the text of `method`. `estimate-sprint-migration-index-dissolved` describes exactly a reading by hand: `test -e vault/wiki/index.md` false, then `rg` over `vault/wiki`, `.claude`, `guppi` and `CLAUDE.md`, every hit read by eye. But the text opens with "at the close of theme 4" and calls the act "read by eye" — neither of the two words lint looks for stands there, and the finding of the class `method` holds. The sibling `estimate-sprint-migration-rule-class-files-dissolved` describes the same kind of work and passes, because it opens with "one reading at the close of Slice 3f".
> The page stands `pending` and its reading is due this session; the Case touches neither the Criterion nor the status — by case 296 a `set` without `status` changes the named field alone.

> **problem:**
> The text of `method` describes a reading without calling it one, so lint cannot classify it. Either the wording is fixed, or lint learns to read a shell command as a reading.

> **given:**
> `is_reading` in lint recognises a reading by the words `by hand` or `reading` in `method`; it has no other sign.
> **＋** For the Estimate of a Leaf a file under `tests/`, the word `pytest`, a `make <target>` or a reading will do.
> **＋** A `set` with a field other than `status` changes that field; the Criterion and the status stand (case 296).

> **when:**
> `uv run guppi lint` reads the live pages of the vault.

> **then:**
> The `method` of the page names its own act — every hit of the `rg` is read by hand — and drops the moment of theme 4, which has passed.
> **＋** The page earns no finding of the class `method`.
> **－** The Criterion does not change and the status stays `pending` until this session's reading.
> **－** `guppi/lint.py` does not change.

```then
update:
  - slug: estimate-sprint-migration-index-dissolved
    set: {method: "test -e vault/wiki/index.md false; rg over vault/wiki, .claude, guppi and CLAUDE.md for §N and index.md, every hit read by hand — only a live pointer, a page that sends a reader to the file, is a failure; the archive and raw/ are not read"}
    change: the method names its reading — read by hand — and drops the moment of theme 4 (case 329)
```

```tasks
- [x] update `estimate-sprint-migration-index-dissolved` — `set: {method: …}`
- [ ] by hand, after the librarian's run: no finding of the class `method` on the page
```

## Case 330 — one spelling of a reading in `method`, and the forms named

> **context:**
> `is_reading` in lint is `"by hand" in method or "reading" in method`: two spellings of one thing, by substring. An agent writing a `create` guesses which word to put there, because neither the schema of an Estimate nor the rule page names the set of forms: the description of the field `method` in `rule-estimates-schema` says "the test command; or where and when it is read by hand; or, for Research, what is measured" — an example, not a list, and with no obligation in it. The field is marked `optional`, and not by accident: the pages before case 193 carry none. Of the 75 live Estimates with a `method`, the word `reading` stands in 51 but carries the classification in exactly one — `estimate-plan-mode-names-its-estimates`; in the others `pytest` stands beside it and the classification goes by that.
> `rule-lint` stands `built`, its single Estimate `estimate-lint-catches` enumerates the classes in its Criterion and is already changed in this session by case 325.2 — in another place, the anchors do not overlap. `rule-estimates-schema` renders `vault/wiki/estimates/schema.yaml`, the file the agent reads before a `create`.

> **problem:**
> Two spellings of one notion force a guess, and the guess is needed because the set of forms is nowhere written as a set. The guard meanwhile stands at the end of the pipeline: lint speaks of an unhappy `method` in the librarian's run, a session later.

### Case 330.1 — `by hand` becomes the one spelling

> **given:**
> `is_reading` takes `by hand` or `reading`, by substring; it has no other sign of a reading.
> **＋** One live page rests on the word `reading` and on nothing else — `estimate-plan-mode-names-its-estimates`, `passed`.
> **＋** The classes of lint and their order live in the docstring of `guppi/lint.py`; the body of `rule-lint` does not enumerate them.
> **＋** A `set` with a field other than `status` changes the field; the Criterion and the status stand (case 296).

> **when:**
> `uv run guppi lint` reads the live pages of the vault.

> **then:**
> `is_reading` is true when `by hand` stands in `method`, and then only; the constant `READING` goes.
> **＋** The `method` of `estimate-plan-mode-names-its-estimates` names its reading with the words `by hand` and earns no finding.
> **＋** A `method` carrying the word `reading` alone, with no `pytest`, no file under `tests/` and no `make <target>`, earns a finding of the class `method`.
> **－** The branch of a MOC and the other three forms do not change.

```then
update:
  - slug: estimate-lint-catches
    replace:
      - old: "a reading (`by hand`, `reading`)"
        new: "a reading (`by hand`, the one spelling since case 330.1)"
    change: one spelling of a reading in the Criterion — `by hand` (case 330.1)
  - slug: rule-lint
    change: a reading in `method` has one spelling, `by hand`; the constant READING is gone (case 330.1)
  - slug: estimate-plan-mode-names-its-estimates
    set: {method: "read by hand at the close of this session's Spec — every Case that changes a rule names the Estimate it changes by slug, and a Case that changes only the Purpose section names none"}
    change: the method names its reading with the one spelling, by hand (case 330.1)
```

```tasks
- [x] update `estimate-lint-catches` — the replace pair in the line of the class `method`
- [x] update `rule-lint` — one `change`
- [x] update `estimate-plan-mode-names-its-estimates` — `set: {method: …}` with the words `by hand`
- [x] `guppi/lint.py` — `READING` removed, `is_reading` by `by hand`; the docstring of `check_method`
- [x] `tests/test_lint.py` — a `method` with the word `reading` alone earns a finding; `by hand` is clean
- [ ] read `estimate-lint-catches`
```

## Case 336 — the schema of an Estimate names the forms of `method` (supersedes 330.2)

> **context:**
> The description of the field `method` in the Render of `rule-estimates-schema` gives an example, not a list, and does not say that one of the forms must stand; the agent writing a `create` guesses. Case 330.2 set out to repair that, but its text carried two errors: it counted the forms as three where lint and case 331 of the same Spec count four, and it promised a finding of the class `method` to a page that names none — while a page with no `method` field at all is counted `unmigrated`, not `method`. Both came from `/pre-spec`.
> `rule-estimates-schema` renders `vault/wiki/estimates/schema.yaml`. Its live reading is `estimate-estimates-schema-checked`, `passed`, whose Criterion opens "The file equals the Render": a change to the Render asks for it to be read again (case 187), and 330.2 named it nowhere — the third finding.

> **problem:**
> The set of forms is written as a set nowhere, and the attempt to write it parted company with the code on the count and overpromised in its consequence. The Estimate of the live reading of that same Render is not named.

> **given:**
> `vault/wiki/estimates/schema.yaml` is the Render of `rule-estimates-schema`; the agent reads it before a `create` of an Estimate.
> **＋** lint classifies a `method` by four forms: a `make <target>`, the word `pytest`, a path under `tests/`, the words `by hand`.
> **＋** A page of the shape before case 193 carries no `method` field at all and is counted in the line `unmigrated`, not as a finding of the class `method`.
> **＋** An `update` of an Estimate with `sections: Criterion` keeps the written text and does not take the Criterion from the Case (case 204); the page carries a `method` field, so case 211.2 does not refuse it.

> **when:**
> The agent reads `vault/wiki/estimates/schema.yaml` before writing a `create` of an Estimate.

> **then:**
> The description of `method` names four forms as a list: a `make <target>` of the Makefile; the word `pytest`; a path under `tests/`; or the words `by hand` — the one spelling of a reading — with where and when it is taken.
> **＋** A `method` that names none of the four earns a finding of the class `method`; a page with no `method` field at all is counted `unmigrated`.
> **＋** For `Research` what is measured stands beside one of the forms, never instead of one.
> **＋** `estimate-estimates-schema-checked` goes to `pending` with its Criterion unchanged, and is read again after the render.
> **－** The field stays `optional`.

```then
update:
  - slug: rule-estimates-schema
    replace:
      - old: "optional; one line. How the promise is checked: the test command (`make test-x`, `pytest tests/test_x.py`); or where and when it is read by hand — a live reading of a session start, the brief of a librarian's run; or, for Research, what is measured. Written from the Case since case 193."
        new: "optional; one line. How the promise is checked, in one of the four forms lint classifies: a `make <target>` of the Makefile; the word `pytest`; a path under `tests/`; or the words `by hand` — the one spelling of a reading — with where and when it is taken, a session start, the brief of a librarian's run. A `method` that names none of the four earns a finding of the class `method`; a page of the shape before case 193, which carries no `method` at all, is counted `unmigrated` instead. For `Research` what is measured stands beside one of the forms, never instead of one. Written from the Case since case 193 (case 336)."
    change: the description of method names the four forms as a list, with by hand as the one spelling of a reading (case 336, supersedes 330.2)
  - slug: estimate-estimates-schema-checked
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
        **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
        **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
        **＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/estimates/schema.yaml`: a page in the shape, then one defect at a time.

        When:
        `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`; `guppi lint` reads a page of `wiki/estimates/`.

        Then:
        The file equals the Render. Lint reads from it: required `type, kind, status, target, origin, sprint, created, tags`; optional `purpose, method, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Context`, `## Method`, `## Result` optional, `## Result` required on `passed` and on `failed`.
        **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
        **＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, the Result and Criterion paragraph, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the two example pages.
        **－** `vault/wiki/estimates/schema.md` does not exist.
    change: the live reading is due again — the description of method in the Render changed; the Criterion stands (case 336)
```

```tasks
- [ ] update `rule-estimates-schema` — the replace pair in the description of `method` inside the Render
- [ ] update `estimate-estimates-schema-checked` — `set: {status: pending}` and `sections: Criterion` verbatim
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [ ] read `estimate-estimates-schema-checked`
```

## Case 331 — `pre-spec` refuses a `method` that names no form

> **context:**
> `check_method` takes four things for the Estimate of a Leaf: the words `by hand`; a path under `tests/` that exists; the word `pytest`; a `make <target>` the Makefile holds. That check stands at the end alone: lint runs in the librarian's run, when the page is already written, and an unhappy `method` lives on until the next session — which is what happened to `estimate-sprint-migration-index-dissolved`, repaired by case 329. At plan time nobody looks: `pre-spec` touches the word `method` only in the list of the keys of the old shape, which it does not read, and the field is `optional` in the schema because of the pages before case 193.
> `rule-prespec` stands `built` with six Estimates, one per finding; cases 325.1 and 327 of this session change its Render in two other places, and this anchor is a third that meets neither. Case 330 has just fixed the contract this Case checks.

> **problem:**
> The form of `method` is a contract for a machine, and the refusal on it comes a session late. It must be checked in the plan by the predicate lint itself judges by: a copy of the classification is exactly the gap that gave C12.

> **given:**
> `check_method` takes, for the Estimate of a Leaf, `by hand`, a path under `tests/`, the word `pytest` or a `make <target>`; the existence of the file and of the target is checked separately, after the match.
> **＋** At the moment of `pre-spec` the test file does not exist: it is written in Work Mode.
> **＋** `materialize` lifts `kind`, `purpose` and `method` for a `create` of an Estimate; a missing one is `incomplete`.
> **＋** The branch of a MOC depends on the Estimates of its children and of its siblings.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the plan before the Spec is approved.

> **then:**
> A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the four forms, gives one line: `case N: <create|update> <slug>: method names no form — a make target, pytest, a tests/ file or "by hand"`.
> **＋** A `create` of an Estimate with no `method` at all gives the same finding.
> **＋** The predicate is one, lifted out of `guppi/lint.py`; `pre-spec` writes no second one.
> **－** Existence is not checked in the plan: the file under `tests/` is written in Work Mode and lint checks it later.
> **－** The branch of a MOC stays with lint: `pre-spec` does not judge whether the Estimate of a MOC needs a `make` target.
> **－** The behaviour of lint does not change — lifting the predicate is a refactor, and `estimate-lint-catches` is not touched.

```then
create:
  - slug: estimate-prespec-catches-a-method-without-a-form
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: Whether pre-spec refuses an Estimate whose method names none of the forms lint classifies
    method: pytest tests/test_prespec.py on a temp plan — a create with a prose method, a create with no method, and each of the four forms clean
    tags: [harness, workflow]
update:
  - slug: rule-prespec
    replace:
      - old: "and for every `create` of an Estimate whose `ref` names no live rule or entity (case 203.1),"
        new: "and for every `create` of an Estimate whose `ref` names no live rule or entity (case 203.1), and for every `create` of an Estimate, or `update` carrying `set: {method: …}`, whose `method` names none of the four forms lint classifies — a `make <target>`, the word `pytest`, a path under `tests/`, or the words `by hand` — by lint's own predicate, the existence of the file and of the target left to lint (case 331),"
    change: a finding for a method that names none of the forms lint classifies (case 331)
```

```tasks
- [x] create `estimate-prespec-catches-a-method-without-a-form`, `ref: rule-prespec`
- [x] update `rule-prespec` — the replace pair in the Render, after the clause on `ref` (case 203.1)
- [x] `guppi/lint.py` — the predicate that names a form lifted out, `check_method` calling it; the behaviour unchanged
- [x] `guppi/prespec.py` — the check over the `create` and `update` items of Estimates, calling lint's predicate
- [x] `tests/test_prespec.py` — a create with a prose method; a create with no method; each of the four forms clean
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-catches-a-method-without-a-form`
```

## Case 332 — a pair is signed after its place is read

> **context:**
> A Case that changes an existing page names the text with a pair — `replace` or `reword`. The pair is composed from the output of a grep: the matched words are copied out of the line and signed as the anchor. Two things stay unknown to the Case: what the words mean where they stand — case 274.2 signed `pre-task → pre-spec` by a count of grep hits, and in five places the word meant the vault query, not the check of the set — and what the page will hold when the pair lands, since the pairs of one Spec are applied in entry order and an earlier Case rewrites the span a later anchor names (case 314.2). Today this is caught by eye alone: at `/pre-spec` the `ask-guppi` agent reads the `then` blocks, but against the page as it stands, not as the Spec leaves it, and the librarian of session 1121 simulated 71 anchors by hand.
> The Insight stands `open`, severity 2, with `lesson-reword-pairs-signed-before-the-places-were-read` and `lesson-replace-anchors-overlap-in-one-spec` as its `clustered` children. `rule-case-protocol` stands `draft` and renders `case-schema.md`, where `replace` is described; `rule-prespec` stands `built`, and three Cases of this session already change its Render in three places that meet nowhere. This Spec carries eight pairs over six pages, three of them on one.

> **problem:**
> A pair is signed blind twice over: without the meaning of the words in their place, and without what the Spec itself leaves of that place. It is caught late — by eye at pre-spec at best, by a refusal of `generate` at worst, after ratification either way.


### Case 332.2 — the machine: `pre-spec` simulates the pairs of the Spec in entry order

> **given:**
> `prespec --check` reads the plan and the live pages of the vault; it has no check of an anchor at all.
> **＋** `generate` applies the pairs in entry order and matches with whitespace collapsed, exactly one occurrence.
> **＋** The pairs of one Spec can touch one span: 314.2 against 310.6.
> **＋** An Insight is the target of the `update` that closes or rejects it; `actioned` sends its `clustered` children to the archive by the cascade.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the plan before the Spec is approved.

> **then:**
> The `replace` and `reword` pairs of every Case of the plan are applied in entry order to copies of the pages in memory, whitespace collapsed as `generate` collapses it; nothing is written to disk.
> **＋** An anchor that misses, or hits more than once, gives one line with its Case, the page's slug and the opening of its `old`.
> **＋** The anchor is judged against the page as the Spec leaves it, not as it stands today.
> **＋** The Insight moves to `actioned`, its `addressed_by` naming both Decisions of this Case.
> **－** The meaning of the words in their place is not judged by a machine: that half is 332.1.

```then
create:
  - slug: estimate-prespec-simulates-the-pairs
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: Whether pre-spec catches an anchor that misses or is not unique once the pairs of the Spec are applied in entry order
    method: pytest tests/test_prespec.py on a temp plan over temp pages — an anchor that misses, one that hits twice, and a pair whose old is produced by an earlier Case
    tags: [harness, workflow]
update:
  - slug: rule-prespec
    replace:
      - old: "an Estimate has its own line and its own item (case 189)."
        new: "an Estimate has its own line and its own item (case 189). It then applies the `replace` and `reword` pairs of every Case of the plan to copies of the pages in memory, in entry order, whitespace collapsed as `generate` collapses it, writing nothing, and prints one line for every anchor that misses or hits more than once, with its Case, the page's slug and the opening of its `old` — the anchor judged against the page as the Spec leaves it, not as it stands today (case 332.2)."
    change: the pairs of the Spec simulated in entry order, an anchor that misses or is not unique reported with its Case (case 332.2)
  - slug: insight-workflow-edit-pair-signed-from-a-grep-fragment
    set: {status: actioned, addressed_by: decision-case-332.2}
    change: actioned by the two halves of its Proposal — the procedure in case-schema.md and the simulation in pre-spec (case 332.2)
```

```tasks
- [ ] create `estimate-prespec-simulates-the-pairs`, `ref: rule-prespec`
- [ ] update `rule-prespec` — the replace pair in the Render, after the clause on an Estimate's line (case 189)
- [ ] update `insight-workflow-edit-pair-signed-from-a-grep-fragment` — `set: {status: actioned, addressed_by: […]}`
- [ ] `guppi/prespec.py` — the simulation of the pairs in entry order, whitespace collapsed as in `generate`
- [ ] `tests/test_prespec.py` — an anchor that misses; an anchor that hits twice; a pair whose `old` an earlier Case produces is clean
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-simulates-the-pairs`
```

## Case 337 — `reword` in the schema of a Case, and one procedure for both forms of a pair (supersedes 332.1)

> **context:**
> Case 332.1 wrote the procedure of signing a pair into the description of `replace` in `case-schema.md` and carried it in words to `reword`. `/pre-spec` showed that `reword` is not described in that file at all: the keys of an `update` there are `set`, `sections`, `replace`, `change` and `rename`. The cause is older than a slip — the key was introduced by cases 274.1 and 274.3, written into `guppi/generate.py`, `guppi/materialize.py` and the page `rule-materialize`, and the schema of a Case was never brought along. So an agent writing a `then` block does not learn from its own file that `reword` exists.
> `rule-case-protocol` stands `draft` and renders `case-schema.md`; case 324 of this session carries only a History line onto it, so nothing meets. The page's four Estimates are not named: `estimate-case-protocol-case-form` and `-ledger-line-form` already stand `pending` and are due in W2 to be read after the render.

> **problem:**
> A key a Case may use is not described in the schema of a Case, and the procedure of signing a pair has nowhere to stand that covers both forms in one place.

> **given:**
> `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi` in every working session; of the keys of an `update` it describes `set`, `sections`, `replace`, `change` and `rename`.
> **＋** `reword` is a key of a `then` block: `materialize` carries it into the entry (274.3), `generate` replaces the pairs as whole words over every live page, checks the owner and refuses the entry on a pair with no hit (274.1).
> **＋** A slug changes through `rename`, never through `reword` (274.1).
> **＋** No rule page carries a procedure for the author of a pair: the greps over `vault/wiki/rules/` and `.claude/skills/` are empty.

> **when:**
> The agent writes the `then` block of a Case that changes an existing page.

> **then:**
> In the list of the keys of an `update` in `case-schema.md`, `reword` stands beside `replace`: a list of `{old, new}` pairs replaced as whole words over every live page of `wiki/`, the page of the item being the owner, for a word that changes everywhere — a slug goes through `rename`.
> **＋** In the same place, one requirement for both forms: a pair is signed only after the sentence around every match is read whole and what it names there is said, never from the line a grep printed.
> **－** `rule-page-generation` does not change: the mechanics of applying a `reword` are described there and stay.
> **－** The Case has no Estimate of its own; the refusal for the procedure is 332.2.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "`replace` (a list of `{old, new}` pairs, each `old` replaced by its `new` inside the body; one pair is a list of one, and a mapping under `replace` is a shape `generate` rejects)"
        new: "`replace` (a list of `{old, new}` pairs, each `old` replaced by its `new` inside the body; one pair is a list of one, and a mapping under `replace` is a shape `generate` rejects), `reword` (a list of `{old, new}` pairs replaced as whole words over every live page of `wiki/`, the page of the item being the owner, for a word that changes everywhere — a slug goes through `rename`, case 274.1); a pair of either kind is signed only after the sentence around every match is read whole and what it names there is said, never from the line a grep printed (case 337)"
    change: reword among the keys of an update, and one procedure for both forms of a pair (case 337, supersedes 332.1)
```

```tasks
- [ ] update `rule-case-protocol` — the replace pair in the list of the keys of an `update` inside the Render
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Case 335 — `check_frontier` judges by the source segment, not by the whole line

> **context:**
> A Frontier line is `- [x] C<n> — <title> · <source> · <closer>`. Case 314.2 asks that a line closed `· case N` whose segments hold `sprint` carry an `update` of the sprint page under that Case. The code tests it as `any("sprint" in s for s in segments[:-1])` — a substring over every segment but the closer. Today that gave a false finding on C6: its source is `brief`, but its title holds the slug `estimate-sprint-migration-index-dissolved`, and the word was found inside the slug. Six live Estimates carry `sprint` in their slug, so it returns.
> `rule-prespec` stands `built`, and its Render carries the same wording in prose — the fifth place of this session's changes on that page, meeting none of the other four. The findings of the Frontier belong to `estimate-prespec-checks-the-plan`, which case 327 already changes in the neighbouring line of the Criterion.

> **problem:**
> The check judges by a substring over the whole line instead of the field meant for it — the class of C12. An item that came from the brief is declared an item of the sprint because of the name of the page it speaks about.

> **given:**
> The segments of a Frontier line are split by ` · `; the source is the segment that stands immediately before the closer.
> **＋** The slug of a page may hold the word `sprint` without the item being one of the sprint.
> **＋** The sense of case 314.2 is that a decided item **of the sprint** changes the sprint page.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the `frontier.md` of the session.

> **then:**
> `sprint` is looked for in the source segment — the one before the closer — and there alone.
> **＋** A title naming a page whose slug holds `sprint` gives no finding.
> **＋** A line whose source is `sprint`, closed `· case N` with no `update` of the sprint page, gives the finding as before.
> **－** The other checks of the Frontier do not change.

```then
update:
  - slug: rule-prespec
    replace:
      - old: "for every line closed `· case N` while its segments hold `sprint`"
        new: "for every line closed `· case N` whose source segment — the one before the closer — is `sprint`"
    change: the sprint test reads the source segment of a Frontier line, not every segment (case 335)
  - slug: estimate-prespec-checks-the-plan
    replace:
      - old: "`[-] … · sprint` is clean, `[x] … · sprint` a finding (case 310.6)."
        new: "`[-] … · sprint` is clean, `[x] … · sprint` a finding (case 310.6). A line closed `· case N` whose source segment — the one before the closer — is `sprint` needs an `update` of the sprint page under Case N; the word inside the slug of a title is not the source (cases 314.2, 335)."
    change: the source segment of a Frontier line in the Criterion (case 335)
```

```tasks
- [x] update `rule-prespec` — the replace pair in the Render, the clause on the segments
- [x] update `estimate-prespec-checks-the-plan` — the replace pair in the line of the Criterion on the Frontier
- [x] `guppi/prespec.py` — `check_frontier` takes the source segment
- [x] `tests/test_prespec.py` — a title holding an `estimate-sprint-*` slug is clean; a source `sprint` with no `update` gives the finding
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-checks-the-plan`
```

## Case 338 — two Criteria this Spec makes false

> **context:**
> Two Cases of this session change behaviour promised by pages they do not name. Case 335 narrows the `sprint` test to the source segment, while `estimate-prespec-binds-a-sprint-line` (`passed`) promises it "by the segments" twice — in its `When` and in a `－` line. Case 331 makes a `create` of an Estimate with no `method` a finding, while `estimate-prespec-checks-the-plan` carries a `－` line saying in so many words that no such finding exists. Both came from `/pre-spec`.
> `estimate-prespec-checks-the-plan` is already changed in this Spec by 327 and 335, in lines 33 and 34 of its Criterion; the line changed here is 39, and the places do not meet. A pair inside `## Criterion` sends the page to `pending` by itself (case 296); the Criterion is not replaced whole.

> **problem:**
> The promise stays written in the old shape while the code moves to the new. lint is silent on it; the cost falls on the next session, which reads the Criterion and measures by the wrong thing.

### Case 338.1 — `estimate-prespec-binds-a-sprint-line` speaks of the source segment

> **given:**
> Its `When` reads "a Frontier line whose segments hold `sprint`", its `－` line "A line without `sprint` among its segments is read as today".
> **＋** Case 335 narrows the test to the segment standing before the closer.
> **＋** A `replace` pair whose `old` stands in `## Criterion` changes a part and sets the page `pending` (case 296).

> **when:**
> `uv run guppi prespec --check` reads a Frontier line closed `· case N`.

> **then:**
> The `When` of the Criterion speaks of the source segment — the one before the closer — and not of every segment.
> **＋** The `－` line says: a line whose source segment is not `sprint` is read as today; the word inside the slug of a title is not the source.
> **－** The rest of the Criterion does not change; the page goes to `pending` and is read again.

```then
update:
  - slug: estimate-prespec-binds-a-sprint-line
    replace:
      - old: "reads a Frontier line whose segments hold `sprint` and whose closer is `case N`."
        new: "reads a Frontier line whose source segment — the one before the closer — is `sprint` and whose closer is `case N`."
      - old: "**－** A line without `sprint` among its segments is read as today."
        new: "**－** A line whose source segment is not `sprint` is read as today; the word inside the slug of a title is not the source (case 335)."
    change: the Criterion speaks of the source segment of a Frontier line (case 338.1)
```

```tasks
- [ ] update `estimate-prespec-binds-a-sprint-line` — two replace pairs inside the Criterion
- [ ] read `estimate-prespec-binds-a-sprint-line`
```

### Case 338.2 — `estimate-prespec-checks-the-plan` stops denying the finding of 331

> **given:**
> Line 39 of its Criterion: "No finding on a Leaf `create` without `method`, an `update` without `contract` or a derived slug: those keys are not read".
> **＋** Case 331 makes a finding of a `create` of an Estimate with no `method`, and of one whose `method` names none of the four forms.
> **＋** A `create` of a rule or an entity carries no `method` at all and gives no finding.

> **when:**
> `uv run guppi prespec --check` reads the `then` blocks of the plan.

> **then:**
> The `－` line says: no finding on a `create` of a rule or an entity without `method`, on an `update` without `contract`, or on a derived slug — those keys are not read.
> **＋** The same line says: a `create` of an Estimate with no `method`, or with a `method` naming none of the four forms, is a finding.
> **－** Lines 33 and 34, which 327 and 335 change, are not touched.

```then
update:
  - slug: estimate-prespec-checks-the-plan
    replace:
      - old: "**－** No finding on a Leaf `create` without `method`, an `update` without `contract` or a derived slug: those keys are not read."
        new: "**－** No finding on a `create` of a rule or an entity without `method`, an `update` without `contract` or a derived slug: those keys are not read. A `create` of an Estimate with no `method`, or with a `method` naming none of the four forms lint classifies, is a finding (case 331)."
    change: the line on a create without method makes room for the finding of case 331 (case 338.2)
```

```tasks
- [x] update `estimate-prespec-checks-the-plan` — the replace pair in line 39 of the Criterion
- [ ] read `estimate-prespec-checks-the-plan`
```

## Case 340 — a Case reads the `estimates` of the page it changes

> **context:**
> The rule is old: a Case that changes the contract of a page names the page's Estimates, and a stale Criterion is a finding (case 53.2). It is carried out in one place — the dispatch of `ask-guppi` at `/pre-spec`, where the agent is given the `estimates` of every page a Case changes and asked whether one the Case does not name speaks of what the Case changes (case 203.2). Before that moment nobody asks: an `update` carries a `ref`, so the author reads the page itself, but its `estimates` pass as a field of the frontmatter, not as a task. The vault query is required only before a `create` without a `ref` — that is, when the page does not exist yet. This session it cost three supersedes, 336, 337 and 338, on findings that came after everything was ratified.
> `rule-case-protocol` stands `draft` and renders `case-schema.md`; case 324 carries a History line onto it and case 337 changes the list of the keys of an `update`, while this Case takes the end of the same paragraph. The places do not meet.

> **problem:**
> The step that catches a stale Criterion stands at the close of Plan Mode, where a finding costs a supersede. The author of a Case has no step at all.

> **given:**
> `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi` in every working session; the description of an `update` ends with the words "it carries no `contract`".
> **＋** The rule that a Case changing a contract names the page's Estimates was ratified by case 53.2; the question is put to `ask-guppi` at `/pre-spec` (case 203.2).
> **＋** Whether a Criterion speaks of what the Case changes is a question of meaning: no script settles it.
> **＋** To name an Estimate is to give an `update` of its slug, not to mention it in prose.

> **when:**
> The agent writes the `then` block of a Case that changes an existing page.

> **then:**
> At the end of the description of an `update` in `case-schema.md` it stands: a Case that changes the behaviour of an existing page reads the page's `estimates` and gives an `update` to each one whose Criterion speaks of the change.
> **＋** The reading happens as the `then` block is written, not at `/pre-spec`.
> **－** An Estimate whose Criterion speaks of something else is not named: a Case that names a spare one replaces a sound Criterion with its own.
> **－** The refusal stays where it is — the question to `ask-guppi` at `/pre-spec`; the Case has no Estimate of its own.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "it carries no `contract`."
        new: "it carries no `contract`. A Case that changes the behaviour of an existing page reads the page's `estimates` and gives an `update` to each one whose Criterion speaks of the change — read as the `then` block is written, not at pre-spec; an Estimate whose Criterion speaks of something else is left alone, since naming a spare one replaces a sound Criterion (cases 53.2, 340)."
    change: a Case reads the estimates of the page it changes as the then block is written (case 340)
```

```tasks
- [ ] update `rule-case-protocol` — the replace pair at the end of the description of an `update` inside the Render
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Deferred

## Case 333 — `estimate-documentation-completes` stands `failed`

> **context:**
> `estimate-documentation-completes` is a promise of `rule-documentation`, the frame of the librarian. The reading of 2026-09-22 failed on one clause: the librarian of session 0014 read lines 52–64 of `ledger.md` while counting the entries, and the Criterion says the frame reads no ledger. Step 6, the commit and `make test-documentation` were green. The page stands `draft`, the Estimate `failed`, and lint holds a line `unread: failed` on it.

> **problem:**
> One of two things is wrong: the wording of the Criterion that forbids the frame a ledger, or the run itself. Deciding it means reading the frame again and understanding what sent the librarian there — a Case of its own, and this session already carries nine.

```then
defer:
  - slug: rule-documentation
    type: rule
    purpose: Whether the Criterion forbids the librarian a reading it in fact needs, or the run of 0014 stepped outside the frame
```

## Case 339 — the defer of `rule-skill-hi` widened: how many closers a Frontier line needs (supersedes 334)

> **context:**
> Case 334 deferred `rule-skill-hi` with one question: a `## Work` line closes `· work` in advance, because `/pre-spec` refuses an open line while the readings come after it. The talk of this session added a second question of the same subject. The Frontier lives one session and goes to the archive with its folder; the sprint page carries no marks at all — the ticks of `sprint.md` are computed by `guppi sprint` from the statuses of the pages each item names. So the closers of a Frontier line exist for `/pre-spec` alone, to let it see that every item went somewhere. Hence the question whether `· sprint` and `· defer case N` must stay two closers, or one mark for "not taken" is enough and the difference — whether `deferred_by` is written on the page — belongs to the Case itself.

> **problem:**
> Both questions are one: what a Frontier closer must tell apart, when the file lives one session and the state lives on the pages. Deciding them apart means touching `rule-skill-hi` and `rule-prespec` twice.

```then
defer:
  - slug: rule-skill-hi
    type: rule
    purpose: What a Frontier closer must tell apart — whether a Work line closes in a second moment of its own, whether pre-spec requires closed lines under Cases alone, and whether sprint and defer case N stay two closers or become one, the file living one session while the state lives on the pages
```
