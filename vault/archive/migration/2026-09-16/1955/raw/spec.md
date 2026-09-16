<!-- approved 21:45:12 · session 286285bb -->

# Spec — session 1955, 2026-09-16: case 191 taken up — `rule-page-generation`, `rule-lint`, `rule-pretask` by the Estimate model

## Case 201 — `rule-page-generation` by the Estimate model

> **context:**
> `rule-page-generation` is a Leaf, `enforcement: check`, its code `guppi/generate.py`, its tests `tests/test_generate.py`. The page carries `## Purpose` and a long `## How it works`; two Estimates: `estimate-generate-writes` — a head plus ten `### case N` blocks (101.1, 104.1–104.3, 105.3, 142.2, 151, 166.2, 166.3, 172) — and `estimate-generate-walks-dates` — a head plus block 103.3; both `passed`. The replacement of a Criterion whole already works through `sections` (194.1), but the code still applies `criterion_block` and `remove_criterion`, writes no `checked`, and the key order of an Estimate does not know `purpose`, `method`, `checked`; the Decision page still gets `## Given` and a `## Criterion` list of `[[estimate-x]] § case N`, which died with the blocks (point 10 of the model of 182, deferred here by 193). Decision 191 deferred the page with the text: generate without blocks and `remove_criterion`, the Criterion whole, the fields `purpose`, `method`, `checked`, the recut of both Estimates; the change of 186.1 (`## Deferred`) stands ratified. The vault was asked for the slugs: `estimate-generate-writes-the-decision-page`, `estimate-generate-fails-alone`, `estimate-generate-cascades` are free in the vault and in the archive (the archive holds seven other `estimate-generate-*`, among them `-rejects-shape-alone` and `-logs-per-entry`, folded into `-writes` by 53.2). The Case touches both Estimate pages and creates three.

> **problem:**
> `estimate-generate-writes` is ten deltas without a whole: what generate promises now is written nowhere, and lint finds a `[[slug]]` in its body that no page carries. The code keeps two paths of the old model that materialize no longer produces, and writes no `checked`, although the schema (193) and the reading line (199) already carry the date. The Decision page writes a Criterion list that points at nothing after a recut. The question: how to recut the two Estimates into promises that read whole, and take the old model out of the code without losing one signed line.

> **given:**
> `guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
> **＋** An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
> **＋** An `estimate` entry carries `status` and `result`; the `result` opens with the date of the reading and the command (199).
> **＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
> **－** `materialize`, `cleanup` and `lint` do not change here.

### Case 201.1 — the text of the rule and the recut of `estimate-generate-writes`

> **when:**
> `guppi generate` applies one entry of a yaml to a page.

> **then:**
> A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the first `## <id>` of `sprint.md`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
> **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
> **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
> **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
> **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
> **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
> **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
> **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by`.
> **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
> **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
> **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
> **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
> **－** No body section is derived from a ref field; a section a page still carries is not touched.
> **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).
> **－** The Decision page, the failure of an entry and the cascade are three other Estimates.

```then
update:
  - slug: rule-page-generation
    sections:
      Purpose: |
        Prevents a ratified decision from ending the session without a page, or a page from
        carrying a field nobody ratified. The script is the only writer to `wiki/`. It lays
        the content of `materialize.yaml` into schema fields and writes nothing else: no
        section is derived from a ref field, no Estimate from a flag, and the Criterion of an
        Estimate is replaced whole by the text its Case signed (cases 166.2, 194.1, 201.1). A
        page is always created, even incomplete: red lint is an accurate signal of debt, a
        decision with no page is the ledger and the vault disagreeing silently. A slug
        collision is an error, never a rename — with one exception: a `create` whose slug is a
        placeholder page, `status: draft` and no `kind`, fills that page (case 101.1). One bad
        entry never stops the run: it is marked `failed`, reported, and the rest apply (case
        47). The Decision page of a Case is written before its entries and carries the body of
        every defer (cases 52.4, 186.1); the cascade after all entries computes what is
        computed — `built`, the archive of a superseded decision, the severity of an Insight —
        never by hand (case 104). The mechanism — the shape of every entry and every History
        line — lives in the docstring of `guppi/generate.py`.
    change: Purpose carries the text of the model; How it works dropped by hand, the mechanism in the docstring of guppi/generate.py (case 201.1)
  - slug: estimate-generate-writes
    set: {status: pending}
    change: the Criterion replaced whole by case 201.1 — the head recut with 101.1, 105.3, 166.2, 171 and 172; 104.x and 166.3 go to -cascades, 142.2 and 151 to -fails-alone; the ten blocks leave (case 201.1)
```

```tasks
- [x] update `rule-page-generation`: `## Purpose` rewritten with the text of the model; `## How it works` dropped by hand, a one-off; the mechanism in the docstring of `guppi/generate.py`
- [x] update `estimate-generate-writes`: the Criterion replaced whole by this sub-case, `pending`
- [x] `guppi/generate.py`: `KEY_ORDER["estimates"]` with `purpose`, `method`, `checked` after `target`; `estimate()` writes `checked`; `criterion_block`, `remove_criterion`, `drop_case_block`, `CASE_BLOCK` removed; the docstring rewritten
- [x] `tests/test_generate.py`: `checked` from the date of the Result and from the yaml's date; the Estimate fields in order; `criterion_block` and `remove_criterion` fail on stderr; the tests of the old paths removed
- [x] read `estimate-generate-writes`
```

### Case 201.2 — `estimate-generate-writes-the-decision-page`

> **when:**
> `guppi generate` reaches the first entry of a Case, or a `decisions` record with no page yet.

> **then:**
> One page `decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`, `tags` — the union of the targets' tags; the body `## Context` and `## Problem` from `case_text`; `## Deferred` — one `### [[slug]]` per target of the `defer` lines, with its `purpose` verbatim.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded`, appends to its `superseded_by`, removes its slug from the `deferred_by` of every target of its `defer` list; an empty `deferred_by` is dropped.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **－** No `## Given`, no `## When`, no `## Criterion` list: the contract lives on the Estimate; pages written before keep theirs.

```then
create:
  - slug: estimate-generate-writes-the-decision-page
    type: estimate
    ref: rule-page-generation
    kind: QA
    purpose: One Decision page per Case, written before its entries, with its lists, its body and its defers
    method: pytest tests/test_generate.py, the tests of the decision page; the live reading in the librarian's run
    tags: [harness, workflow, ledger]
update:
  - slug: decisions-schema
    file: vault/wiki/decisions/schema.md
    change: "`## Given` and `## Criterion` are the shape before case 201.2: kept on the pages that carry them, not written to a new page (case 201.2)"
  - slug: decisions-schema-yaml
    file: vault/wiki/decisions/schema.yaml
    change: "the comment on `## Given` and `## Criterion`: the shape before case 201.2, optional, never written to a new page (case 201.2)"
```

```tasks
- [x] create `estimate-generate-writes-the-decision-page`
- [x] `vault/wiki/decisions/schema.md` and `schema.yaml`: `## Given` and `## Criterion` — the shape before case 201.2, kept where they stand, not written to a new page (Rule-class, by hand)
- [x] `guppi/generate.py`: `decision()` without `Given` and without the Criterion list
- [x] `tests/test_generate.py`: a new page without `## Given` and `## Criterion`; the rest as it is
- [x] read `estimate-generate-writes-the-decision-page`
```

### Case 201.3 — `estimate-generate-fails-alone`

> **when:**
> `guppi generate` meets an entry it cannot apply, or one already handled.

> **then:**
> An entry that fails — a collision, a `ref` naming no page, a `replace` absent or not unique, a field of an unexpected shape, an unknown `kind`, any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` in the yaml and skipped; the rest apply; the exit code is 1; no entry ends the run.
> **＋** Every applied entry is marked `applied: <time>`; a stale `failed` mark is dropped on apply; a rerun writes nothing.
> **＋** An entry with `failed` and no `kind` is skipped with its mark kept and the line `generate: line N: not lifted by materialize; <message>`, exit 1.
> **＋** An entry with `superseded_by` is not applied and leaves no line; the Decision page of its Case is still written.
> **＋** A Rule-class file entry prints `a Rule-class file, applied by hand` and is marked applied; an `update` with no content prints `an update with no content in the Spec; applied by hand` and is marked applied.
> **－** The failure of one entry changes no other page: `log.md` after it is level with the pages.

```then
create:
  - slug: estimate-generate-fails-alone
    type: estimate
    ref: rule-page-generation
    kind: QA
    purpose: One bad entry never stops the run; every entry carries its mark
    method: pytest tests/test_generate.py, the tests of the failed, skipped and marked entries
    tags: [harness, workflow, ledger, tests]
```

```tasks
- [x] create `estimate-generate-fails-alone`
- [x] `tests/test_generate.py`: the existing tests of failures, marks and skips green; none new beyond 201.1
- [x] read `estimate-generate-fails-alone`
```

### Case 201.4 — `estimate-generate-cascades`

> **when:**
> `guppi generate` runs the cascade after all entries of a unit.

> **then:**
> An entity or rule whose Estimates are all `passed` becomes `built`; a `built` one with an Estimate not `passed` returns to `draft`; History `status: a → b · cascade`.
> **＋** A Decision page with `status: superseded` becomes `archived` with History `archived · superseded`; `superseded_by` and `deferred_by` are not touched.
> **＋** Every `clustered` child of an Insight with `status: actioned` becomes `archived` with History `archived · insight actioned`; the Insight's `children` does not change.
> **＋** The `severity` of every Insight is recounted: a child's status is read under `wiki/lessons/`, else in the archive; a child with no page counts live; an `open` Insight at 0 becomes `archived` with History `archived · no live child`, `children` kept; an `actioned` one at 0 stays.
> **－** A page without Estimates keeps its status; no section of any page is derived or touched by the cascade.

```then
create:
  - slug: estimate-generate-cascades
    type: estimate
    ref: rule-page-generation
    kind: QA
    purpose: The cascade computes built, the archive of a superseded decision and the severity of an Insight, never by hand
    method: pytest tests/test_generate.py, the tests of the cascade
    tags: [harness, workflow, ledger]
```

```tasks
- [x] create `estimate-generate-cascades`
- [x] `tests/test_generate.py`: the existing tests of the cascade green; none new
- [x] read `estimate-generate-cascades`
```

### Case 201.5 — the recut of `estimate-generate-walks-dates`

> **when:**
> `uv run guppi generate` runs, with `--date` or without.

> **then:**
> Without `--date` every unit under `raw/` with a `materialize.yaml` is applied: the date-level yaml first, then `raw/<date>/<HHMM>/materialize.yaml` in folder order, dates ascending; `--date` walks the units of that date alone.
> **＋** A unit with no unapplied entry changes no page; stdout carries one line per unit, `generate: <unit>: N page(s) written or changed`.
> **＋** A failure on one unit is printed, the walk goes on, the exit code is 1 at the end.
> **＋** A `--date` without a yaml is named on stderr, exit 1; no yaml anywhere — one line on stderr, exit 1.
> **－** A unit `materialize` passed by (`carry.md`) has no yaml and is not walked.

```then
update:
  - slug: estimate-generate-walks-dates
    set: {status: pending}
    change: the Criterion replaced whole by case 201.5 — the head and block 103.3 recut into one (case 201.5)
```

```tasks
- [x] update `estimate-generate-walks-dates`: the Criterion replaced whole by this sub-case, `pending`; block 103.3 merged
- [x] `tests/test_generate.py`: the existing tests of the walk green; none new
- [x] read `estimate-generate-walks-dates`
```

## Case 202 — `rule-lint` by the Estimate model

> **context:**
> `rule-lint` is a Leaf, `enforcement: check`, its code `guppi/lint.py`, its tests `tests/test_lint.py`, the target `make lint` after `render --check`. The page carries `## Purpose` and a long `## How it works`; one Estimate — `estimate-lint-catches`: a head plus four blocks (103.5, 112.1, 149.3, 156), `passed`. The Estimate schemas are already in the new shape (193): `purpose`, `method`, `checked` optional fields, `## Context` and `## Method` optional sections. The code does not know it: `check_method` reads the `## Method` section only and says nothing of the `method` field on the thirteen new pages; `check_criterion` accepts `### case N` blocks; a `pending` Estimate is invisible to lint — ten today, known to the brief alone. Decision 191 deferred the page with the text: the finding `unread` on every `pending` and `failed`; the schema without `## Context` and `## Method`; the `unmigrated` counter for the transition and the removal of the old shape at zero; the change of 186.3 (`deferred`) stands. The Case touches the one Estimate of the rule.

> **problem:**
> The model of 182 says: a rule changes → the Estimate `pending` → lint red → the reading → `passed` → lint clean. Today the chain is broken in the middle: lint does not see `pending`, and an Estimate can stand unread for any length of time. Nobody checks the `method` field on the new pages, and the 42 pages of the old shape are not visible as a remainder. The question: how lint sees an unread promise and the remainder of the migration, and what it checks in `method` once it is a line, not a section.

> **given:**
> `guppi lint` reads every live page of `wiki/<category>/` against the category's `schema.yaml` and writes nothing.
> **＋** `estimates/schema.yaml` (193): `purpose`, `method`, `checked` are optional fields; `## Context`, `## Method` optional sections; `## Result` required on `passed` and `failed`.
> **＋** The tests in `tests/test_lint.py` fix the behaviour, one per class; the live reading is `make lint` in the librarian's run of this session.
> **－** `render --check` and the Makefile do not change.

> **when:**
> `uv run guppi lint` reads the live pages of the vault.

> **then:**
> Every live page is checked against the `schema.yaml` of its category; one line per finding, `<category>/<slug>: <class>: <what>`; exit 1 on any finding, 0 and no output on a clean vault; nothing is written.
> **＋** `schema`: a missing required field or section, a value outside the list, a conditional not met; `## When` is never required on a Decision page; `schema-prose`: `schema.md` and `schema.yaml` naming different fields or sections.
> **＋** `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by` or in a History wikilink that no live or archived page carries; a `[[…]]` in a body may name a hub file under `wiki/` by stem or path; a `[[slug]]` under a Decision page's `## Criterion` that is no Estimate; a `### case N` block of an Estimate with no decision page.
> **＋** `origin`: both forms resolve in `raw/` or in `vault/archive/`; in neither, or in both, a finding.
> **＋** `path`: a file of `implementation_ref` or `governs` that does not exist.
> **＋** `orphan`: a live entity, rule or estimate that no live page's frontmatter names; a lesson and an Insight never.
> **＋** `status`: `built` with an Estimate not `passed`, `draft` with every one `passed`; an Estimate `passed` or `failed` without `## Result`; an Estimate whose target is not an entity or a rule, or does not list it in `estimates`.
> **＋** `unread`: every Estimate `pending` or `failed` — one finding each, `unread: <status>`; red between a change of a promise and its reading, by design.
> **＋** `method`: the `method` field, or on a page of the old shape the `## Method` section; for a MOC's Estimate a named `make <target>` of the Makefile passes whatever stands beside it, without one `by hand` passes only when the Estimates of every child are by hand; for a Leaf's Estimate a `tests/` file that exists, the word `pytest`, a `make <target>` of the Makefile or a reading (`by hand`, `reading`); else a finding.
> **＋** `decision`: a decision page with none of the four lists, or with `kind`/`target_slug`; a listed slug with a category prefix and no page.
> **＋** `deferred`: a placeholder earns one finding `deferred: <N> times since case <M>` in place of its `schema` and `orphan` findings; a page with `deferred_by` whose fields are in place earns none.
> **＋** `unmigrated`: one line, `estimates: unmigrated: <N> pages in the shape before case 193` — the live Estimates without a `method` field, or with `## Context`, `## Method` or a `### case N` block; no line at zero.
> **－** `make lint` runs it after `render --check`; neither writes.
> **－** The checks of the old shape — `## Method` as a section, the `### case N` blocks — leave by a separate `update` of this rule once the counter reads zero; not this Case.

```then
update:
  - slug: rule-lint
    sections:
      Purpose: |
        Prevents a page that breaks its schema, points at nothing, claims a status its
        Estimates do not support, or waits for a reading nobody took from sitting in the vault
        unnoticed. Pages are written by the generator and, for the Rule-class files, by hand;
        both drift, and nothing else reads the whole graph at once. Red is a signal, not a
        gate: a `pending` Estimate is red until its reading (case 182, point 13), a
        placeholder is red with the count of its defers (case 186.3), the pages of the shape
        before case 193 are red as one counted line until the last is recut (case 202).
        `make lint` runs it after `render --check`; both only report, so the Makefile's rule
        — no target writes to the tree — holds (case 147.7). `parent: rule-harness` names the
        MOC of the harness tools: lint runs with the renderer, in no phase of the session. The
        classes and their order live in the docstring of `guppi/lint.py`.
    change: Purpose carries unread, deferred and unmigrated; How it works dropped by hand, the classes in the docstring of guppi/lint.py (case 202)
  - slug: estimate-lint-catches
    set: {status: pending}
    change: the Criterion replaced whole by case 202 — the head and the blocks 103.5, 112.1, 149.3, 156 recut into one, with unread, the method field and unmigrated (case 202)
```

```tasks
- [x] update `rule-lint`: `## Purpose` rewritten; `## How it works` dropped by hand, a one-off; the classes and their order in the docstring of `guppi/lint.py`
- [x] update `estimate-lint-catches`: the Criterion replaced whole by this Case, `pending`
- [x] `guppi/lint.py`: `unread`; `check_method` on the `method` field, the section only without the field, the classes of a test and of a reading; `unmigrated` as one line; the docstring
- [x] `tests/test_lint.py`: `pending` and `failed` each one `unread` finding; a `method` field with `tests/`, `pytest`, `make`, `reading` clean, without them a finding; a page of the old shape counted in `unmigrated`, no line at zero
- [x] read `estimate-lint-catches`
```

## Case 203 — `rule-pretask` by the Estimate model

> **context:**
> `rule-pretask` is a Leaf, `enforcement: render`, it governs `.claude/skills/pre-task/SKILL.md`; the code of the check is `guppi/pretask.py` (`--check`), its tests `tests/test_pretask.py`. The page carries `## Purpose` and `## Render`, no `## How it works`; one Estimate — `estimate-pretask-reconciles`: a head plus six blocks (73.4, 74, 75.2, 90.2, 103.4, 128), `passed`, its `## Method` "one reading by hand" although half of the blocks are checked by pytest. The Render still names the findings of the old shape: a Leaf `create` without `method`, an `update` without `contract`, two contracts in one Case, a derived slug without `estimate_slug`; `check_form` in the code prints them — five times on the plan of 1651, as the brief knows. Decision 191 deferred the page with the text: pre-task checks the Estimates of the rule named in `context` and asks `ask-guppi` whether an unnamed one speaks of the same thing; the checks of the old model are removed; the changes of 186.2 (the body of a defer is not read) and 198 stand. The vault was asked: `estimate-pretask-checks-the-plan` is free in the vault and in the archive. The Case touches the one Estimate of the rule and creates one.

> **problem:**
> The model of 182 closes the hole with one question: a Case that changes a rule names the Estimate it touches, and pre-task asks whether an unnamed one was left. Today pre-task asks about `contract: changed`, which no longer exists, and prints findings on keys materialize ignores. The one Estimate mixes two promises with different ways to check — the `--check` command (pytest) and the live run of the skill (a reading by hand) — and its Method speaks of one only. The question: which findings `--check` prints by the new model, what the skill asks `ask-guppi`, and how to cut the Estimate along the axis of the promise.

> **given:**
> `guppi pretask --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `pretask` line with the session's stamp on the Skill call.
> **＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
> **＋** The tests in `tests/test_pretask.py` fix `--check`; the live reading is the `/pre-task` of this session.
> **－** The `PreToolUse ExitPlanMode` hook (`rule-pretask-hook`) does not change.

### Case 203.1 — `estimate-pretask-checks-the-plan`

> **when:**
> `guppi pretask --check <plan>` runs in a session with a `hi`.

> **then:**
> One finding per line on stdout, exit 1 on any, 0 and silent when clean; without a `hi` in the session's window, exit 0 and one line on stderr.
> **＋** Lines: a decision line of the window with no item of its kind under its own Case heading; an item with no line; a `defer` line matches a `defer` item, a Rule-class file line an `update` with that `file` or `slug`; an item under another sub-case's heading is a finding.
> **＋** The frontier `raw/<hi date>/<hi HHMM>/frontier.md`: a missing file, an open line, a `case N` whose heading the plan lacks, a `defer case N` with no `defer` item under Case N.
> **＋** Tasks: a Case with a line of a kind other than `defer` and no `tasks` block; an Estimate a `then` block creates or sets `pending` with no task line naming its slug.
> **＋** Governed: an `update` item with `file` on a path a live Rule page governs.
> **＋** Form: a Case whose `then` block holds two or more Estimate items without a written `sections: Criterion` — one promise per Case, split it; an `update` of an Estimate whose page does not exist; a `create` of an Estimate whose `ref` names no live rule or entity.
> **＋** Grammar: every record line of the window — the session's ledger whole plus the date-level ledgers from the `hi` time on — through `materialize.parse_line`; one that does not parse is a finding with its file and line number.
> **＋** A `then` block that does not parse: the error as a finding of its Case.
> **－** No finding on a Leaf `create` without `method`, an `update` without `contract` or a derived slug: those keys are not read.

```then
create:
  - slug: estimate-pretask-checks-the-plan
    type: estimate
    ref: rule-pretask
    kind: QA
    purpose: The check of the plan against the session's lines, frontier, tasks, governed paths and the form of an Estimate item
    method: pytest tests/test_pretask.py, the tests of --check
    tags: [session, workflow, harness, tests]
```

```tasks
- [x] create `estimate-pretask-checks-the-plan`
- [x] `guppi/pretask.py`: `check_form` rewritten — two Estimate items without a written Criterion, an `update` of an Estimate without a page, a `create` of an Estimate with a `ref` without a page; `leaf_page`, `derived_estimate_slug`, `page_estimates` removed when no longer used; the docstring
- [x] `tests/test_pretask.py`: two items with the Case's Criterion a finding, one plus one with a written Criterion clean; an `update` of an Estimate without a page a finding; a `create` with a `ref` without a page a finding; the tests of the old findings removed
- [x] read `estimate-pretask-checks-the-plan`
```

### Case 203.2 — the Render and the recut of `estimate-pretask-reconciles`

> **when:**
> The person invokes `/pre-task`, or the agent calls the skill, before the Spec is approved.

> **then:**
> The agent runs `guppi pretask --check` on the plan file and fixes the plan, the frontier or the line for every finding until the command prints nothing; `guppi gate` writes the stamped `pretask` line into the event log on the Skill call.
> **＋** The agent lists every decision of this Plan Mode, one line each: slug — kind — `purpose` for a `create`, an `update`, a `delete`; a `defer` by its slug and the word `defer`; for an `update` of a rule or an entity, the page's `estimates` and which of them the Case names by slug.
> **＋** `ask-guppi` is dispatched once with the list, the absolute path of the plan file, the instruction to read every Case outside `## Deferred` — `when`, `then`, the `then` block — and two questions: which decisions contradict a page, `index.md` or each other; whether an Estimate the Case does not name speaks of the thing the Case changes.
> **＋** Every finding returned is raised as a Case or named in one line as already known; then Plan Mode exits again.
> **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

```then
update:
  - slug: rule-pretask
    replace:
      - old: "for every Leaf `create` item without `method`, for every Leaf `update` item without `contract`, for every Case with two or more Leaf items that create or say `contract: changed` (split the Case), for every derived Estimate slug that names an existing page while the item has no `estimate_slug`, and for every `update` with `contract: changed` whose page carries no Estimate or more than one while the item names no `estimate_slug` (case 90.2); an Estimate has no line of its own (case 72.5)."
        new: "for every Case whose `then` block holds two or more Estimate items — a `create`, or an `update` with `set: {status: pending}` — without a written `sections: Criterion` (one promise per Case: split it), for every `update` of an Estimate whose page does not exist, and for every `create` of an Estimate whose `ref` names no live rule or entity (case 203.1); an Estimate has its own line and its own item (case 189)."
      - old: "for an `update` that changes a page's contract, add the page's `estimates` and whether the Case updates their criterion — an Estimate whose criterion quotes the changed wording and has no update line is a finding."
        new: "for an `update` of a rule or an entity, add the page's `estimates` and which of them the Case names by slug — `ask-guppi` is asked whether an Estimate the Case does not name speaks of the thing the Case changes; one that does is a finding (case 203.2)."
    change: the findings of --check by the Estimate model; the list for ask-guppi carries the page's estimates and the ones the Case names; supersedes 191 (case 203.2)
  - slug: estimate-pretask-reconciles
    set: {status: pending}
    change: the Criterion replaced whole by case 203.2 — the live run of the skill; the blocks 73.4, 74, 75.2, 90.2, 103.4 go to -checks-the-plan, 128 stays here (case 203.2)
```

```tasks
- [x] update `rule-pretask`: two `replace` in the Render — the findings of `--check` by the new model; the list for `ask-guppi` with the page's `estimates` and the named Estimates
- [x] update `estimate-pretask-reconciles`: the Criterion replaced whole by this sub-case, `pending`; the blocks 73.4, 74, 75.2, 90.2, 103.4 to `-checks-the-plan`, 128 here
- [x] `uv run guppi render`: `.claude/skills/pre-task/SKILL.md`
- [x] `tests/test_render.py`: the existing tests of the render green
- [x] read `estimate-pretask-reconciles` — at the `/pre-task` of this session
- [x] `{supersedes:case 191}`: `decision-case-191` superseded, the three rules lose `deferred_by`
```

## Case 204 — a written Criterion wins over the Case's text

> **context:**
> `rule-materialize` is a Leaf, `enforcement: check`, its code `guppi/materialize.py`; nine Estimates, among them `estimate-materialize-assembles` — `pending` with the Criterion of 194.1, its reading not yet taken. The Purpose of the rule says: the Criterion of an Estimate is the `given`, `when`, `then` of the Case, lifted verbatim into the entry's `sections`. The Criterion of `-assembles` says the same for an `update` and allows a written text for a `create` only: "from the block's `sections` when one is written, else from the Case". The code (`lift_criterion`) keeps a written `sections.Criterion` in both cases — on a `create` and on an `update` — and sets `pending` unless the item set a status itself. The handoff of 1651 named the divergence: 188 updated `estimate-case-protocol-loaded` with a written Criterion and the text stayed, although the `then` of 194.1 says the entry carries the Case's text. `case-schema.md` already allows both paths for a `create` (194.1), and Case 203.1 of this session leans on a written Criterion as the signature of a separate promise. The Case touches one Estimate — `-assembles`; the other eight it does not touch.

> **problem:**
> Two texts speak of an Estimate `update` differently: the rule and the Criterion say "the Case's text replaces", the code says "the written text stands". Until this is signed, `estimate-case-protocol-loaded` carries a Criterion that by the letter of the rule should not have stayed, and 203.1 treats an item with a written Criterion as a separately signed promise without a rule that says so. The question: which of the two texts is the signature when the item wrote `sections: Criterion` itself.

> **given:**
> A unit `raw/<date>/<HHMM>/` holds `ledger.md` and `spec.md`; a Case in the Spec has a heading, the sections `given`, `when`, `then` and a `then` block.
> **＋** `guppi generate` applies the `sections` of an `update` entry as whole replacements and writes every field of a `create` entry's `fields` into the frontmatter.
> **＋** The tests in `tests/test_materialize.py` fix the behaviour; the live reading is the librarian's run.

> **when:**
> `guppi materialize` lifts a record line of a ledger against its Spec.

> **then:**
> One entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `origin`, `line`, `text`, `decision`; from the `then` block — `fields`, `sections`, `replace`, `change`, `impact`; what the block lacks is `incomplete`, never invented.
> **＋** An Estimate has its own line and its own entry; the `ref` of the line is the Estimate itself.
> **＋** An `update` entry for an Estimate carries `sections.Criterion` — the text the item wrote under `sections: Criterion` itself, else the `given`, `when` and `then` of its Case verbatim with their operands as `Given:`, `When:`, `Then:` — replacing what stood there, and `set: {status: pending}` unless the item set a status itself; the `given` of a sub-case is its parent's when it has none of its own.
> **＋** A `create` entry for an Estimate keeps `kind`, `purpose`, `method`, `tags` as fields; its Criterion the same way: the written text when there is one, else the Case's; `## Context` and `## Method` are not written.
> **＋** One decision entry per Case: `decision`, `case_text`, `targets`; a sub-case inherits `context`, `problem`, `recommend`, `given`, never `when`.
> **＋** An `estimate` line for a page of the same ledger is folded into its `create`; for an earlier page it is an `estimate` entry. The `new_tags` of any Case reach the yaml once. An existing yaml is extended, never rewritten.
> **－** An `update` entry carries no `contract`, and no Estimate is derived from it; a `create` carries no `method`, `estimate_kind` or `estimate_slug`; neither `criterion_block`, `case_removed` nor `remove_criterion` is derived.
> **－** The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule's item are ignored: they reach neither the page nor `incomplete`.
> **－** A line the grammar does not parse goes under `unparsed`; the run goes on.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "is the `given`, `when` and `then` of the Case that names it, lifted verbatim into the entry's `sections` and replacing what stood on the page (cases 189, 194.1)."
        new: "is the `given`, `when` and `then` of the Case that names it, lifted verbatim into the entry's `sections` and replacing what stood on the page (cases 189, 194.1); a Criterion the item writes under `sections` itself stands instead, on a `create` and on an `update` alike — it is signed in the same block, and it is how one Case touches two promises (case 204)."
    change: a written Criterion stands on a create and on an update alike (case 204)
  - slug: estimate-materialize-assembles
    set: {status: pending}
    change: the Criterion replaced whole by case 204 — the text of 194.1 with the written Criterion winning on an update, the given without the state of pages (case 204)
```

```tasks
- [x] update `rule-materialize`: one `replace` in Purpose — a written Criterion stands on a `create` and on an `update`
- [x] update `estimate-materialize-assembles`: the Criterion replaced whole by this Case, `pending`
- [x] `tests/test_materialize.py`: an Estimate `update` with a written `sections: Criterion` keeps it and is set `pending`; with `set: {status: passed}` on the item, the item's status
- [x] read `estimate-materialize-assembles`
```

## Case 208 — the written Criterion in the Rule-class texts, and two pre-task findings

> **context:**
> Case 204 signed: on an `update` of an Estimate a written `sections: Criterion` stands, as on a `create`. Three texts say otherwise: `index.md` §7 — "its `update` replaces the Criterion whole" with the Case's text, and §12 allows the written text on a `create` only (194.1); `case-schema.md` — "the scripts copy the Case's `given`, `when` and `then` … replacing what stood there", and below: "an `update` of an Estimate carries `slug`, `set`, `change`; the scripts replace its Criterion with the Case's `given`, `when` and `then`"; the Render of `rule-case-protocol` — "the scripts copy them whole, replacing what stood there" — which is `CLAUDE.md`, changed only through an `update` of the page. `rule-case-protocol` carries four Estimates; the sentence is read by `estimate-case-protocol-case-form` (a Case in the chat carries the whole contract in `given`, `when`, `then`), `pending`, its reading not taken; the other three are not touched. Two more findings: `estimates/schema.md` and `schema.yaml` point at "case 191" as the one that builds `checked` and the recut — 191 is superseded by 203.2; and the Render of `rule-pretask` after the two `replace` of 203.2 still says "and the question: which of these contradict…", while the `then` of 203.2 speaks of two questions — the second is named only inside the sentence on the list.

> **problem:**
> The next agent reads the behaviour ratified in 204 from `CLAUDE.md`, `index.md` and `case-schema.md` — and reads the old one. The pointers at 191 lead to an archived decision page. The dispatch sentence of the pre-task Render does not match its own Criterion. The question: how 204 reaches the three texts that override it, and how the two small findings close.

> **given:**
> `index.md`, `case-schema.md`, `estimates/schema.md` and `schema.yaml` are Rule-class files: an `update` with `file` and `change`, applied by hand in Work Mode.
> **＋** `CLAUDE.md` is rendered from `rule-case-protocol`; an `update` of the Render touches the Estimate of the live reading of that Render (187).
> **＋** The reading of `estimate-case-protocol-case-form` is the Cases of this session at its close, by hand.

### Case 208.1 — the Rule-class files

> **when:**
> A reader opens `index.md` §7 or §12, `case-schema.md` or `estimates/schema.md`.

> **then:**
> Each says one thing: the Criterion of an Estimate is the `given`, `when`, `then` of the Case, lifted by the scripts, or the text the item wrote under `sections: Criterion` itself; the written one stands on an `update` as on a `create` (204).
> **＋** `estimates/schema.md` and `schema.yaml` point at 201.1 (`checked` written by `generate`) and at 202 (the counter of the recut) instead of 191.
> **－** The rest of these files does not change.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§7 the sentence on an update, §12 the sentence on the written text: a written Criterion stands on a create and on an update alike (case 204)"
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "two sentences — the scripts copy the Case's text replacing what stood there, and an update of an Estimate carries slug, set, change — unless the item wrote the Criterion under sections itself, which stands on an update as on a create (case 204)"
  - slug: estimates-schema
    file: vault/wiki/estimates/schema.md
    change: "the rows purpose, checked and ## Criterion point at 201.1 and 202 instead of 191, which 203.2 supersedes"
  - slug: estimates-schema-yaml
    file: vault/wiki/estimates/schema.yaml
    change: "the comment on the older pages points at 202 instead of 191"
```

```tasks
- [x] `vault/wiki/index.md`: §7 the sentence on an `update`, §12 the sentence on the written text — on a `create` and on an `update` (case 204); by hand
- [x] `vault/wiki/case-schema.md`: two sentences — "the scripts copy … replacing" and "an `update` of an Estimate carries …" — with the written text (case 204); by hand
- [x] `vault/wiki/estimates/schema.md`: the rows `purpose`, `checked`, `## Criterion` — 201.1 and 202 instead of 191; by hand
- [x] `vault/wiki/estimates/schema.yaml`: the comment — 202 instead of 191; by hand
```

### Case 208.2 — the Render of `rule-case-protocol` and `estimate-case-protocol-case-form`

> **when:**
> The agent writes a Case in the chat — at its first showing, when shown again after the owner's change, and with sub-cases.

> **then:**
> `given` holds the conditions of the behaviour; the state of the pages the Case changes goes to `context`.
> **＋** `context` names which Estimates of the rule the Case touches and which it does not.
> **＋** `given`, `when` and `then` together are the Criterion of the Estimate, copied whole and replacing what stood there.
> **＋** An item that writes `sections: Criterion` itself signs that text, on a `create` and on an `update` alike; the Case's `given`, `when`, `then` are the Criterion of the one Estimate that writes none; that is how one Case touches two Estimates.
> **＋** The Case names by slug the Estimate it changes.
> **＋** `tasks` carries no `contract` line and no "block N" line.
> **－** A `create` carries no `method`, `estimate_kind` or `estimate_slug`: a new promise is an explicit `create` of an Estimate with its own slug.
> **－** The eight sections of the chat form do not change.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "`given`, `when` and `then` together are the Criterion of the Estimate the Case creates or changes: the scripts copy them whole, replacing what stood there;"
        new: "`given`, `when` and `then` together are the Criterion of the Estimate the Case creates or changes: the scripts copy them whole, replacing what stood there, unless the item writes `sections: Criterion` itself — that text stands, on an `update` as on a `create`, and it is how one Case touches two promises (case 204);"
    change: a written Criterion stands on an update as on a create; the Case's text is the Criterion of the one item that writes none (case 208.2)
  - slug: estimate-case-protocol-case-form
    set: {status: pending}
    change: the Criterion replaced whole by case 208.2 — the text of 188 with the given recut and the line on a written Criterion (case 208.2)
```

```tasks
- [x] update `rule-case-protocol`: one `replace` in the Render — "copy them whole, replacing", unless the item wrote the Criterion itself (case 204)
- [x] update `estimate-case-protocol-case-form`: the Criterion replaced whole by this sub-case, `pending`
- [x] `uv run guppi render`: `CLAUDE.md`; `render --check` exit 0
- [x] read `estimate-case-protocol-case-form` — the Cases of this session at its close
```

### Case 208.3 — the sentence on two questions in the Render of `rule-pretask`

> **when:**
> The agent reads the Render of pre-task and assembles the dispatch of `ask-guppi`.

> **then:**
> The dispatch sentence names two questions: which decisions contradict a page, `index.md` or each other; whether an Estimate the Case does not name speaks of the thing the Case changes.
> **－** The Criterion of `estimate-pretask-reconciles` (203.2) already says so; no second `update` of it.

```then
update:
  - slug: rule-pretask
    replace:
      - old: "and the question: which of these contradict a page of the vault, a rule of `index.md`, or each other."
        new: "and two questions: which of these contradict a page of the vault, a rule of `index.md`, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes."
    change: the dispatch sentence names the two questions of 203.2 (case 208.3)
```

```tasks
- [x] update `rule-pretask`: a third `replace` in the Render — "and the question: …" → "and two questions: …"
- [x] `uv run guppi render`: `.claude/skills/pre-task/SKILL.md` (with 203.2)
```

## Deferred

## Case 205 — the binding of a hi line to its session by position, deferred again

> **context:**
> `insight-ledger-hi-tied-to-its-session-by-position` is an Insight, `open`, severity 1, four children, `deferred_by: decision-case-192`, in its fourth brief. Its pattern: the event log binds a `hi` line to its session by the position of the `session-start` lines around it, not by an id; any start missing from the window or added to it sends the `hi` to the wrong session, and the ledger writer refuses. Case 111 already writes a stamped `hi` from the `UserPromptSubmit` hook and reads the window by that stamp, with the old rule as a fallback.

> **problem:**
> Retiring the binding by position is code in two readers — `pretask.resolve_session` and the ledger hook's window — with its own Estimate and a live reading across midnight, which this session cannot take. This session ratified four Cases of code (201–204) with none built yet; a fifth waits for a session that can read it.

```then
defer:
  - slug: insight-ledger-hi-tied-to-its-session-by-position
    type: insight
    purpose: |
      Retire the binding by position: `pretask.resolve_session` resolves the session from the
      stamped `hi` and walks back to the date of that `hi`, instead of falling back to the
      last `session-start` of today's event log; the ledger hook's window is checked against
      it so the two readers do not disagree at midnight. Closes all four children of the
      Insight. Needs its own Estimate and one live reading across midnight. Deferred by 192,
      again by 205.
```

## Case 206 — Slice 3b after the build of 201–203

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` are placeholders, `draft`, `deferred_by: decision-case-183`, `deferred: 13 times since case 29`, in their eighteenth brief. `sprint.md` puts Slice 3b after case 191 and before Slice 4; the model of 182 says Work Mode leans on "an Estimate is the red test".

> **problem:**
> Case 191 is ratified in this session (201–203) and not built: `lint` does not yet print `unread`, `pretask --check` does not yet know the form of an Estimate item. Work Mode built on top of promises that are not yet red would be built on text, not on tests. Slice 3b is the Plan Mode of a session of its own, after the build of 201–203.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: |
      Slice 3b — Work Mode: the Spec as tasks with code, the ticked boxes in spec.md, the test
      of each Estimate written first and turned green; the Plan Mode of a session of its own,
      after the build of cases 201–203 and before Slice 4. Deferred by 183, again by 206.
  - slug: rule-subagent-guppi
    type: rule
    purpose: |
      Slice 3b — what a subagent may do in Work Mode, and the fork that comes back to the main
      agent as a Case; with rule-work-mode, after the build of cases 201–203. Deferred by 183,
      again by 206.
```

## Case 207 — a Spec box: a conserved Spec run by a Work Mode session of its own

> **context:**
> `/carry` (`rule-carry-over`, `draft`) conserves a Spec whose work is not done: `carry.md` in `raw/<date>/<HHMM>/`, the brief rewritten, a commit; `materialize` passes the unit by; "the session that finishes the Spec deletes `carry.md`" — where and how that session runs is unsaid. `rule-end-of-work` knows two ends of a session, the ordinary one and `/carry`. `rule-documentation` and `rule-close`: the librarian is the only writer to `wiki/` and ends in its own commit; `guppi gate` refuses `/handoff` on a dirty tree; the ledger hook refuses without a `hi` in the session's window. `rule-work-mode` and `rule-subagent-guppi` are placeholders (case 206). The vault was asked: `rule-spec-box` is free in `wiki/` and in the archive; no page speaks of a worktree or of a session started from a conserved folder; `lesson-subagents-parallel-on-one-tree-red-mid-flight` says two writers on one tree make readings meaningless. The wider question was named in session 1651 and left without a defer.

> **problem:**
> A session ends in a brief that the next session must work off, so the sessions run one after another even when the work of a Spec has no decision left in it. Work Mode is where the time goes and where nothing is decided; it could run in parallel — one conserved Spec per session, each in a git worktree. What keeps it from racing is already the rule: the librarian alone writes `wiki/`, each session writes its own `raw/` folder, `generate` applies only what is unapplied, a superseded Case is skipped. What is missing is the session itself: how it opens a box, where its hook writes, how it ends, and who runs the librarian after the merge. This leans on Work Mode (Slice 3b) and is discussed after it.

```then
defer:
  - slug: rule-spec-box
    type: rule
    tags: [session, workflow, git, harness]
    purpose: |
      A Spec box: a session that opens a conserved Spec — a `raw/<date>/<HHMM>/` folder with
      `carry.md` — in a git worktree on its own branch, and runs its Work Mode. Not `/hi`,
      not Plan Mode: a skill lists the boxes, the person picks one, the agent executes it.
      It writes only into that folder — ticks `spec.md`, readings into its `ledger.md`,
      `handoff.md` — and into the code; it never touches `wiki/` and never runs the
      librarian. It ends with `/retro` and `/handoff`; done is `handoff.md` present and
      `carry.md` removed. At a fork it stops and returns the question, as a subagent does.
      The branch is merged into the main branch; the librarian runs once there, over every
      unapplied unit and every handoff, and writes one brief. Open: the skill and its
      conditions; the ledger hook and `guppi gate` inside a worktree with its own
      `event_log.md`; the cut of a Spec into boxes that share no file and no page; a third
      end of a session in `rule-end-of-work`; whether the box is a subagent of the main
      session with `isolation: worktree` or a session the person starts. After Slice 3b
      (case 206).
```
