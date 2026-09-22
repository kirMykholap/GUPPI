<!-- approved 16:36:44 · session cd07081a -->

# Spec — 2026-09-22, session 1121

## Case 308 — the edge `rule-glossary` → `entity-glossary`, and the lift of a `create` on a schema change

> **context:**
> `materialize` lifts the fields of a `create` by the category's `schema.yaml` on disk: a key the schema does not name is marked `unknown` and does not reach the page. The schema is now rendered from `rule-<category>-schema` — by the `render` step, after `generate`. In session 0014 case 304 created `rule-rules-schema` with the field `applies_to`, and case 306.4 created `rule-glossary` with that field; `materialize` walked by the old `schema.yaml`, dropped `applies_to`, and the edge Rule → Entity of the glossary was not made: `rule-glossary` without `applies_to`, `entity-glossary` without `rules`, lint silent — neither side of the edge exists. `rule-harness` and `rule-sprint` got their `applies_to` by an `update` with `set` — a `set` is not checked against the schema. Pages: `rule-glossary` `built`, `entity-glossary` `draft`; `rule-materialize` `built`, its ten Estimates untouched but for one new one.

> **problem:**
> Two defects. The edge of the glossary is absent — an `update` is needed. And the order of the pipeline: a `create` that uses a field the same Spec adds to the schema always loses that field — the schema on disk catches up only after `generate`.

### Case 308.1 — the edge `rule-glossary` → `entity-glossary`

> **given:**
> `rule-glossary` is the guard of `entity-glossary` (case 306.4).
> **＋** The schema of rules: `applies_to` on a Rule is written in the Case, `rules` on an Entity is the backlink computed by the cascade of `generate` (case 305).

> **when:**
> The librarian runs `generate` on the yaml of this session.

> **then:**
> `rule-glossary` carries `applies_to: ["[[entity-glossary]]"]`.
> **＋** `entity-glossary` carries `rules: ["[[rule-glossary]]"]` with a History line `rules: [...] · cascade`.
> **＋** `check_edges` of lint finds no difference on the pair.

```then
update:
  - slug: rule-glossary
    set: {applies_to: ["[[entity-glossary]]"]}
    change: the edge to entity-glossary, dropped by materialize as unknown against the old schema in session 0014 (case 308.1)
```

```tasks
- [x] update `rule-glossary`
- [ ] by hand, after the librarian's run: `entity-glossary` carries `rules: ["[[rule-glossary]]"]`, `make lint` — no `ref` finding on the pair
```

### Case 308.2 — `materialize` lifts a `create` whole on a schema change

> **given:**
> `materialize` lifts a `create` by the category's `schema.yaml` on disk: a key outside the schema is `unknown` and does not reach `fields` (case 214.1).
> **＋** The `schema.yaml` of a category is the Render of `rule-<category>-schema`, written by `render` after `generate` (case 304).

> **when:**
> `materialize` walks a unit whose Spec holds a `create` or `update` with the slug `rule-<category>-schema`.

> **then:**
> A `create` of that category in the same unit is lifted whole: every key into `fields`, no `unknown` — wherever the schema entry stands in the Spec, before or after.
> **＋** The pages the librarian writes carry the field before `render` lands the schema on disk.
> **－** A unit without such an entry is lifted by the schema as before; the other categories of the same unit too.

```then
create:
  - slug: estimate-materialize-lifts-unfiltered-on-a-schema-change
    type: estimate
    ref: rule-materialize
    kind: QA
    purpose: A create of a category whose schema rule the same unit creates or updates is lifted with every key into fields and no unknown; a unit without that entry is lifted by the schema on disk
    method: uv run pytest tests/test_materialize.py -k schema_change — a unit with create rule-rules-schema and create rule-x carrying a key the disk schema lacks, the key in fields and no unknown; the same create without the schema entry, unknown as before
    tags: [harness, librarian]
update:
  - slug: rule-materialize
    replace:
      - old: "defect of the ledger, and it shows here."
        new: "defect of the ledger, and it shows here. The keys of a `create` are lifted by the category's `schema.yaml` on disk (case 214.1) — but for a category whose `rule-<category>-schema` the same unit creates or updates: its `create` items are lifted whole, no `unknown`, since the schema on disk catches up only at the render after `generate` (case 308.2)."
    change: a create of a category whose schema rule the same unit changes is lifted whole (case 308.2)
```

```tasks
- [x] update `rule-materialize`
- [x] create `estimate-materialize-lifts-unfiltered-on-a-schema-change`
- [x] `guppi/materialize.py`: the schema-rule entries of the unit collected before the lift; `_lift_item` gets `known=None` for their categories; the docstring
- [x] `tests/test_materialize.py`: a unit with `create rule-rules-schema` and `create rule-x` carrying a key the disk schema lacks — the key in `fields`, no `unknown`; the same `create` without the schema entry — `unknown` as before
- [x] read `estimate-materialize-lifts-unfiltered-on-a-schema-change`: `uv run pytest tests/test_materialize.py -k schema_change`
```

## Case 309 — a reading folded into a superseded `create` moves

> **context:**
> An `estimate[...]` line of the ledger does not become an entry of its own when the yaml of the unit already holds an unapplied `create` of the same slug: `fold_estimate` writes `status` and `result` into that `create` and keeps the line number in `folded`. The mark `{supersedes:case N}` comes later — on the line of the next Case — and marks every entry of Case N `superseded_by`; `generate` skips them, the folded reading with them. In 0014 the readings L52 and L53 (`estimate-rules-schema-checked`, `estimate-entities-schema-checked`, both `passed`) folded into the creates of 304.2 and 304.3, which 305.1 and 306.1 replaced at once: the pages stand `pending` with no Result, `rule-rules-schema` and `rule-entities-schema` `draft`. The order in `lift_line`: the new `create` is appended to `entries` before `mark_superseded`, so at the moment of the mark the live `create` of the same slug is already there. A yaml is never rewritten — 0014 is not repaired by this; its two readings are taken again by hand (W2) and reach the pages as entries of their own in this session. `rule-materialize` `built`; of its Estimates the Case touches one new one only; `estimate-materialize-marks-superseded` it does not touch.

> **problem:**
> A reading taken between a `create` and its `{supersedes}` is lost in silence — no `failed`, no `incomplete`, no line in the brief; it shows only as an empty Result on the page.

> **given:**
> `materialize` folds an `estimate[...]` line into the unapplied `create` of the same slug in the unit's yaml — `status`, `result`, the line number in `folded` (case 49).
> **＋** `{supersedes:case N}` marks every entry of Case N `superseded_by`; `generate` skips the marked ones (case 175).
> **＋** The live `create` of a line with `{supersedes}` reaches `entries` before the mark.

> **when:**
> `materialize` lifts a line with `{supersedes:case N}`, and a `create` entry of Case N holds `folded`.

> **then:**
> The readings of `folded` move to the live `create` of the same slug in this unit — `status`, `result`, the line numbers; the marked `create` loses `status`, `result` and `folded`.
> **＋** With no live `create`, each reading becomes an `estimate` entry of its own from the ledger line of that number, after the mark.
> **＋** A reading lifted after the mark is not folded into the marked `create`.
> **－** A mark on a Case of another unit (`elsewhere`) moves nothing — no live `create` is there; the readings of that yaml stand as they are.

```then
create:
  - slug: estimate-materialize-refolds-a-reading-on-a-supersede
    type: estimate
    ref: rule-materialize
    kind: QA
    purpose: A reading folded into a create that a later supersedes marks moves to the live create of the same slug in the unit, or becomes an estimate entry of its own; no reading folds into a superseded create
    method: uv run pytest tests/test_materialize.py -k refold — create A, a reading, create B with supersedes A, the reading on B; create A, a reading, supersedes A without a new create, an estimate entry; a reading after the mark, not on A
    tags: [harness, librarian]
update:
  - slug: rule-materialize
    replace:
      - old: "not done (case 190.3). The mechanism"
        new: "not done (case 190.3). A reading — an `estimate` line — folds into the unapplied `create` of its slug in the unit; a `create` a `{supersedes}` marks is never folded into, and the readings already folded into it move to the live `create` of the same slug in the unit, or each becomes an entry of its own from its ledger line (case 309). The mechanism"
    change: a reading folded into a superseded create moves to the live create of the slug or becomes an entry of its own (case 309)
```

```tasks
- [x] update `rule-materialize`
- [x] create `estimate-materialize-refolds-a-reading-on-a-supersede`
- [x] `guppi/materialize.py`: `fold_estimate` skips a `superseded_by` create; `lift_line` after a local mark moves `folded` readings to the live create or appends `estimate` entries; the docstring
- [x] `tests/test_materialize.py`: create A, reading, create B `{supersedes}` A — the reading on B; create A, reading, `{supersedes}` A without a new create — an `estimate` entry; a reading after the mark — not on A
- [x] read `estimate-materialize-refolds-a-reading-on-a-supersede`: `uv run pytest tests/test_materialize.py -k refold`
```

## Case 310 — a sprint item is a page; a note is a task not yet cut into pages

> **context:**
> `guppi sprint` writes `sprint.md` from the page `entity-sprint-migration`: an item `- [[slug]] — …` gets `[x]` by the status of its page, a plain line renders `- [ ] …` and is never ticked, and a milestone holding one never closes. Themes 1–6 of Slice 3f are plain lines: 304–306 did themes 1–3, but the lines stand open and nothing can close them. In the Frontier a sprint item not taken in a session closes only by `[-] · defer case N` — hence 18 defer decisions on Slice 3b that decide nothing; in 0014 themes 4–6 were closed `· work` with a note, which is not true. Pages: `entity-sprint-migration` `draft`; `rule-sprint` `built`, of its three Estimates the Case touches `estimate-sprint-renders-the-backlog`; `rule-skill-hi` `built`, it touches `estimate-hi-writes-frontier`; `rule-prespec` `built`, it touches `estimate-prespec-checks-the-plan`; `rule-page-schemas` `draft`, `rule-glossary` `built`, `estimate-generate-writes-rules-from-applies-to` `passed`. The slugs `estimate-sprint-migration-index-dissolved` and `estimate-sprint-migration-file-route-gone` are free by the Grep over `estimates/`; the nearest is `estimate-sprint-migration-rule-class-files-dissolved`, the Estimate of the whole Slice — themes 4 and 5 are its parts that fail and are fixed apart, the Atomicity Rule.

> **problem:**
> How a sprint item without a page closes; where a task of a milestone goes as prose so that the agent sees it; how the Frontier closes a sprint item not taken this session without a defer decision.

### Case 310.2 — Slice 3f on the sprint page: page items

> **given:**
> Themes 1–3 are done by Cases 304–306: `rule-page-schemas`, the edge `applies_to`/`rules` (`estimate-generate-writes-rules-from-applies-to` `passed`), `rule-glossary`.
> **＋** A note closes by the cut (310.1).

> **when:**
> The librarian applies the `update` and runs `guppi sprint`.

> **then:**
> Slice 3f holds five page items — `[[rule-page-schemas]]`, `[[estimate-generate-writes-rules-from-applies-to]]`, `[[rule-glossary]]`, `[[estimate-sprint-migration-index-dissolved]]`, `[[estimate-sprint-migration-file-route-gone]]` — and the Estimate of the whole Slice as it stood; theme 6 is a sentence of the Slice's description.
> **＋** Each is ticked by the status of its page; the Slice closes by mechanism once every item is `[x]`.
> **＋** The Estimate line says `entity-glossary`; the Purpose says "four Estimates".

```then
update:
  - slug: entity-sprint-migration
    replace:
      - old: "Done when the three"
        new: "Done when the four"
      - old: "from decisions (case 301)."
        new: "from decisions (case 301). The Slice closes by the reading of its Estimate, once \"Rule-class\" is retired in the Case schema and the glossary (theme 6)."
      - old: "the glossary from `terms`, `index.md` gone"
        new: "the glossary from `entity-glossary`, `index.md` gone"
      - old: "- 1. schemas — six Leaves `rule-<category>-schema`, `enforcement: render`, the Render the `schema.yaml` with the description of its fields as yaml data; `schema.md` gone; one rule per category, never two"
        new: "- [[rule-page-schemas]] — 1. schemas: the six category schemas as rule pages, each the Render of its `schema.yaml`; `schema.md` gone (case 304)"
      - old: "- 2. audit of the rules — the parent of every rule: under a category's MOC a rule that holds for that category alone, the MOC made at two or more such rules, else the schemas under `rule-page-schemas`; `applies_to` on a Rule and `rules` on an Entity, the edge Rule → Entity, `rule-sprint` → `entity-sprint` the first (from the Backlog, session 1119)"
        new: "- [[estimate-generate-writes-rules-from-applies-to]] — 2. the edge Rule → Entity: `applies_to` on a Rule, `rules` on an Entity by the cascade; `rule-sprint` → `entity-sprint` the first (case 305)"
      - old: "- 3. glossary — `terms` on the page that defines a term; `guppi glossary` writes `glossary.md`, grouped by the parent MOC, under `rule-glossary` with `governs`, `implementation_ref` and `--check`, the pattern of `rule-sprint`; the rows on `§N` resolved as the index dissolves, \"Retired terms\" into the history of decisions"
        new: "- [[rule-glossary]] — 3. glossary: `glossary.md` rendered from the `## Terms` of `entity-glossary`, under `rule-glossary` with `governs` and `--check` (case 306)"
      - old: "- 4. `index.md` — one Case per §: covered by a rule page, the § leaves; not covered, a rule is made; the last Case removes the file and every `§N` pointer in the vault"
        new: "- [[estimate-sprint-migration-index-dissolved]] — 4. `index.md`: one Case per §: covered by a rule page, the § leaves; not covered, a rule is made; the last Case removes the file and every `§N` pointer in the vault"
      - old: "- 5. scripts — the audit \"script — what it assumes — what changes\"; the `file` route and \"applied by hand\" removed from `materialize`, `generate`, `prespec`, `lint`; the grep of `index.md` out of `rule-ask`; `rule-morph` (Slice 5) kept compatible with six schema rules - 6. close — \"Rule-class\" retired in the Case schema and the glossary; the Estimate read; the Slice moved to Closed"
        new: "- [[estimate-sprint-migration-file-route-gone]] — 5. scripts: the audit \"script — what it assumes — what changes\"; the `file` route and \"applied by hand\" removed from `materialize`, `generate`, `prespec`, `lint`; the grep of `index.md` out of `rule-ask`; `rule-morph` (Slice 5) kept compatible with six schema rules"
    change: Slice 3f as page items — themes 1–3 by the pages of 304–306, themes 4–5 by their Estimates, theme 6 into the description; the Estimate line and the Purpose reworded (case 310.2)
```

```tasks
- [x] update `entity-sprint-migration`
- [x] `uv run guppi sprint`
```

### Case 310.3 — `estimate-sprint-migration-index-dissolved`

> **given:**
> `index.md` is the map of the vault by §; pages, rules and scripts point at `§N` (case 301, theme 4).
> **＋** Each § is either covered by a rule page or gets one.

> **when:**
> The last Case of theme 4 is applied by the librarian.

> **then:**
> `vault/wiki/index.md` does not exist.
> **＋** No live page of `wiki/`, no harness file and no docstring of `guppi/` points at a `§N` or at `index.md` as a source.
> **－** The archive and the ledgers under `raw/` keep their pointers.

```then
create:
  - slug: estimate-sprint-migration-index-dissolved
    type: estimate
    ref: entity-sprint-migration
    kind: QA
    purpose: index.md is gone and no live page, harness file or script docstring points at a §N of it or at the file as a source
    method: at the close of theme 4 — test -e vault/wiki/index.md false; rg over vault/wiki, .claude, guppi and CLAUDE.md for §N and index.md, every hit read by eye, only a live pointer — a page that sends a reader to the file — a failure; the archive and raw/ are not read
    tags: [sprint, workflow, harness]
```

```tasks
- [x] create `estimate-sprint-migration-index-dissolved`
- [ ] read `estimate-sprint-migration-index-dissolved`: at the close of theme 4 — `test -e vault/wiki/index.md` false; `rg '§|index\.md' vault/wiki .claude guppi CLAUDE.md` empty but for the archive
```

### Case 310.5 — the closer `· sprint` in the Frontier

> **given:**
> A Frontier line closes `· case N`, `· work` or `· defer case N` (case 268.2).
> **＋** A `defer` postpones a page; a note of the sprint page has nothing to defer — it is on the page already.

> **when:**
> An item of the current milestone — a page or a note — is not taken this session.

> **then:**
> The line closes `[-] … · sprint`: the item stays on the sprint page; no decision, no `deferred_by`.
> **－** `· defer case N` stays for a page postponed by a decision.

```then
update:
  - slug: rule-skill-hi
    replace:
      - old: "deferred; an item the person adds is a new Cases line;"
        new: "deferred, `[-] … · sprint` when the item is a line of the sprint page left for a later session — no decision, no `deferred_by` (case 310.5); an item the person adds is a new Cases line;"
    change: the closer `· sprint` for a sprint item left for later (case 310.5)
  - slug: estimate-hi-writes-frontier
    replace:
      - old: "`[-] … · defer case N`."
        new: "`[-] … · defer case N`, and `[-] … · sprint` when the item is a line of the sprint page left for a later session — no decision, no `deferred_by` (case 310.5)."
    change: the closer `· sprint` (case 310.5)
```

```tasks
- [x] update `rule-skill-hi`
- [x] update `estimate-hi-writes-frontier`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-writes-frontier`: by hand at the first `/hi` of the next session
```

### Case 310.6 — `pre-spec` accepts `· sprint`

> **given:**
> `prespec.check_frontier`: the closer is the last segment after ` · `; one not of `work`, `case N`, `defer case N` is a finding.
> **＋** `tests/test_prespec.py` fixes `--check`.

> **when:**
> `guppi prespec --check` reads a Frontier with a line `[-] … · sprint`.

> **then:**
> The line is clean: no finding, no Case and no `defer` needed.
> **－** `[x] … · sprint` is a finding: a note is not done, only left.

```then
update:
  - slug: rule-prespec
    replace:
      - old: "still open or closed by a Case the plan does not hold"
        new: "still open, closed by a Case the plan does not hold, or closed `[x]` whose closer — the last segment after ` · ` — is `sprint`; `[-] … · sprint` is clean, a sprint item left for a later session, no Case and no `defer` needed (case 310.6)"
    change: the closer `· sprint` accepted on a `[-]` line, a finding on `[x]` (case 310.6)
  - slug: estimate-prespec-checks-the-plan
    replace:
      - old: "a `defer case N` with no `defer` item under Case N."
        new: "a `defer case N` with no `defer` item under Case N; `[-] … · sprint` is clean, `[x] … · sprint` a finding (case 310.6)."
    change: the closer `· sprint` (case 310.6)
```

```tasks
- [x] update `rule-prespec`
- [x] update `estimate-prespec-checks-the-plan`
- [x] `guppi/prespec.py`: `CLOSERS` with `sprint`; `[x]` with `sprint` a finding; the docstring
- [x] `tests/test_prespec.py`: `[-] · sprint` clean, `[x] · sprint` a finding
- [x] read `estimate-prespec-checks-the-plan`: `uv run pytest tests/test_prespec.py`
```

## Case 311 — `estimate-harness-pipeline`: three file checks, not two

> **context:**
> The Criterion of `estimate-harness-pipeline` describes `make lint` as four steps — `render --check`, `sprint --check`, `glossary --check`, `guppi lint` (306.5 added the third) — but its `then` line still says "exits 0 … by its first two steps": the promise counts the steps by the shape before 306. The sense of the line: the file checks pass clean, and `guppi lint` with its findings is read by its own Estimates. The page is `pending`; the Purpose of `rule-harness` names the four steps in order; W5 reads the Estimate by hand after the librarian's run.

> **problem:**
> One line of the Criterion counts the wrong number of steps; a reading by it either fails by the letter or passes against it.

> **given:**
> `make lint` is `render --check`, `sprint --check`, `glossary --check`, `guppi lint`, in this order (cases 227, 306.5).
> **＋** A `replace` inside the Criterion sets `pending` (case 296).

> **when:**
> Someone reads `estimate-harness-pipeline` after the librarian's run; W5 takes the reading.

> **then:**
> The `then` line says: `make test-harness` is green; `make lint` on the committed tree passes its three file checks clean — `render`, `sprint`, `glossary` `--check` silent; the fourth step, `guppi lint`, is read by its own Estimates.
> **＋** The page is `pending` until the reading of W5.

```then
update:
  - slug: estimate-harness-pipeline
    replace:
      - old: "by its first two steps."
        new: "by its first three steps — the file checks, `render`, `sprint` and `glossary --check` silent; the fourth, `guppi lint`, is read by its own Estimates (case 311)."
    change: the then line counts three file checks, glossary --check the third (case 311)
```

```tasks
- [x] update `estimate-harness-pipeline`
- [ ] read `estimate-harness-pipeline`: `make test-harness`, then `make lint` — the three checks silent, `guppi lint` its own count
```

## Case 312 — one reading ticks every `read` line of its Estimate in the Spec

> **context:**
> `generate`, on an `estimate` entry (or a `create` with a folded reading), ticks the *first* unticked line `- [ ] read `<slug>`` in the first Spec that holds one, skipping the sections of Cases ratified after the reading (280) and superseded (286) — one line per entry. In 0014 two Cases touched `estimate-lint-catches` — 304.8 and 305.5, one `replace` pair each, from different parents — and the Spec holds two `read` lines. The reading after Work Mode was one, the page is `passed`; the line of 304.8 was ticked, the line of 305.5 stands open — a false debt at Retro. A reading is taken of the page, not of a Case: the Criterion is one, and after Work Mode it holds both changes, so one reading answers for both lines. Pages: `rule-page-generation` `built`, of its nine Estimates the Case touches `estimate-generate-ticks-the-spec` (`passed`).

> **problem:**
> Two Cases of one session that touched one Estimate leave one `read` line open for ever; either it is a form `pre-spec` refuses, or a tick `generate` adds.

> **given:**
> `generate` ticks a `read` line in the first Spec that holds one, skipping the sections of Cases after the reading (280) and superseded (286) (case 270.1).
> **＋** `tests/test_generate.py` fixes the tick on the Spec beside the yaml.

> **when:**
> `generate` applies an `estimate` entry or a `create` with a folded reading, and the first Spec with such a line holds two or more unticked `- [ ] read `<slug>``.

> **then:**
> Each of them becomes `- [x]`; nothing else in the file changes.
> **＋** A line in the section of a Case ratified after the reading, or superseded, stays open — as before.
> **－** A second Spec is not opened when the first held at least one line.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: "or a `create` with a folded reading, the first unticked `- [ ] read `<slug>`` line, in the Spec beside the yaml first"
        new: "or a `create` with a folded reading, every unticked `- [ ] read `<slug>`` line of the first Spec that holds one — one reading is of the page, whose Criterion is one, however many Cases of the session touched it (case 312) — in the Spec beside the yaml first"
    change: one reading ticks every read line of its slug in the first Spec that holds one (case 312)
  - slug: estimate-generate-ticks-the-spec
    replace:
      - old: "the first unticked line `- [ ] read `<slug>`` becomes `- [x]` — in the Spec beside the yaml first, then in the `spec.md` of the other session folders of `raw/`, oldest first; one line per entry."
        new: "every unticked line `- [ ] read `<slug>`` of the first Spec that holds one becomes `- [x]` — the Spec beside the yaml first, then the `spec.md` of the other session folders of `raw/`, oldest first; one Spec per entry, every line of the slug in it but those in the section of a Case ratified after the reading or superseded (case 312)."
    change: every read line of the slug in the first Spec, not the first line (case 312)
```

```tasks
- [x] update `rule-page-generation`
- [x] update `estimate-generate-ticks-the-spec`
- [x] `guppi/generate.py`: `tick_read` ticks every matching line of the first Spec that holds one; the docstring
- [x] `tests/test_generate.py`: two `read` lines of one slug in one Spec, one reading — both ticked; one in a later Case's section — left
- [x] read `estimate-generate-ticks-the-spec`: `uv run pytest tests/test_generate.py -k tick`
```

## Case 313 — a sprint item names one or more pages; a note keeps its box and is never ticked

> **context:**
> `guppi sprint` ticks an item by the status of the one page its leading `[[slug]]` names; a further wikilink in the text is text — the item `[[rule-work-mode]]` carries `[[insight-workflow-code-live-before-the-page-it-reads]]` in its sentence and must not wait for it. Case 310.1 of this session took the checkbox off a plain line; the box is the better sign — it shows an open task, and nothing but `guppi sprint` can tick it, since the governed-files hook refuses a hand edit of `sprint.md` and the sprint page has no box at all. What is missing is an item whose work is two pages. Pages: `rule-sprint` `built`, of its three Estimates the Case touches `estimate-sprint-renders-the-backlog` (`passed`); `entity-sprint-migration` `draft`, changed by 310.2 of this Spec, which writes one page per item.

> **problem:**
> An item whose work is finished by two pages has no form; and 310.1 removed the box that shows a note is an open task.

> **given:**
> `guppi sprint` ticks an item `- [[slug]] — <text>` by the status of its page — `built`, `passed` or `archived` — and renders a line without a wikilink as `- [ ] <text>`, never ticked (case 229.2).
> **＋** The governed-files hook refuses a hand edit of `sprint.md`; the sprint page carries no checkbox.
> **＋** `tests/test_sprint.py` fixes the render on a temp vault.

> **when:**
> `guppi sprint` renders an item of a milestone or of the Backlog.

> **then:**
> The pages of an item are every `[[slug]]` before the first ` — `; the item is `[x]` when each of them is `built`, `passed` or `archived`, `[ ]` otherwise, and the statuses follow after ` · `, in the order of the slugs.
> **＋** A wikilink after the ` — ` is text: it names no page of the item and holds no tick back.
> **＋** A line with no wikilink before the ` — ` is a note: `- [ ] <text>`, no status, never ticked; it keeps its milestone open and leaves only by the `update` of the Case that cuts it into items or removes it.
> **－** A slug of an item with no live or archived page is one line on stderr and exit 1, as today.

```then
update:
  - slug: rule-sprint
    replace:
      - old: "an item without a wikilink is a plain line, never ticked (case 229.2)."
        new: "an item names its pages by every `[[slug]]` before the first ` — `, and is ticked when each of them is `built`, `passed` or `archived`, the statuses after ` · ` in the order of the slugs; a wikilink after the ` — ` is text. A line with no wikilink before the ` — ` is a note — a task not yet cut into pages: `- [ ] <text>`, no status, never ticked, keeping its milestone open until the `update` of the Case that cuts it into items or removes it (cases 229.2, 313)."
    change: an item names one or more pages before the ` — `; a note keeps its box and is never ticked (case 313)
  - slug: estimate-sprint-renders-the-backlog
    replace:
      - old: "An item `- [[slug]] — <text>` is ticked by the status of its page, as today; an item `- <text>` without a wikilink renders `- [ ] <text>` and is never ticked."
        new: "An item is ticked by the statuses of every page its `[[slug]]` before the first ` — ` names — `[x]` when each is `built`, `passed` or `archived`, the statuses after ` · ` in the order of the slugs; a wikilink after the ` — ` is text. A line with no wikilink before the ` — ` is a note: `- [ ] <text>`, never ticked, keeping its milestone open (case 313)."
    change: the Criterion names the pages of an item and the note (case 313)
```

```tasks
- [x] update `rule-sprint`
- [x] update `estimate-sprint-renders-the-backlog`
- [x] `guppi/sprint.py`: the pages of an item are the wikilinks before the first ` — `; `[x]` when each is done, the statuses in order; a note keeps `- [ ]`; the docstring
- [x] `tests/test_sprint.py`: an item of two pages, one `draft` — `[ ]` with both statuses, both `built` — `[x]`; a wikilink after the ` — ` holds no tick back; a note renders `- [ ] <text>` and keeps its milestone open
- [x] read `estimate-sprint-renders-the-backlog`: `uv run pytest tests/test_sprint.py`
- [x] `uv run guppi sprint`
```

## Case 314 — a Frontier line of the sprint keeps its source, and its Case changes the sprint page

> **context:**
> A Frontier line carries its source — `- [ ] C2 — <title> · sprint` — and is closed by replacing the tail: `· case N`, `· work`, `· defer case N`. The source is lost at the close, so nothing can tell afterwards that the line came from the sprint page. That is the one place where "an item of the sprint was decided" is written down mechanically: in 0014 the Cases 304–306 finished themes 1–3 and left their lines on the sprint page untouched, and no script could say so — the brief's Flags named it by hand. Pages: `rule-skill-hi` `built`, of its two Estimates the Case touches `estimate-hi-writes-frontier` (`passed`); `rule-prespec` `built`, its five Estimates untouched, one new one added; `estimate-prespec-binds-a-sprint-line` is free by the Grep over `estimates/`, the nearest is `estimate-prespec-checks-the-plan` — the plan against the ledger, another promise.

> **problem:**
> The close of a Frontier line drops its source, so no check can ask the one question that matters: a sprint item was decided this session — did its Case change the sprint page?

### Case 314.1 — the closer is appended, the source stays

> **given:**
> A Frontier line is `- [ ] C<n> — <title> · <source>`, closed `[x] … · case N`, `[x] … · work`, `[-] … · defer case N`, `[-] … · sprint` (cases 268.2, 310.5).
> **＋** `prespec.check_frontier` reads the closer as the last segment after ` · `.

> **when:**
> The agent closes a Frontier line.

> **then:**
> The closer is appended, the source stays: `- [x] C2 — <title> · sprint · case 315`.
> **＋** An item left for a later session is `- [-] C2 — <title> · sprint` — the box changed, no closer appended, since the source says it already.
> **－** The closer is still the last segment; nothing else of the line changes.

```then
update:
  - slug: rule-skill-hi
    replace:
      - old: "Close a line when its item ends: `[x] … · case N`"
        new: "Close a line when its item ends, the closer appended and the source kept — `- [x] C2 — <title> · sprint · case 315` (case 314.1): `[x] … · case N`"
    change: the closer is appended, the source of a line stays (case 314.1)
  - slug: estimate-hi-writes-frontier
    replace:
      - old: "closed as today — `[x] … · case N`"
        new: "closed by appending the closer and keeping the source — `- [x] C2 — <title> · sprint · case 315` (case 314.1) — `[x] … · case N`"
    change: the closer is appended, the source stays (case 314.1)
```

```tasks
- [x] update `rule-skill-hi`
- [x] update `estimate-hi-writes-frontier`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-writes-frontier`: by hand at the first `/hi` of the next session
```

### Case 314.2 — `pre-spec`: a decided sprint item changes the sprint page

> **given:**
> `prespec.check_frontier` reads every line of the session's `frontier.md`, the closer the last segment after ` · `; the `then` blocks of the plan are parsed beside it.
> **＋** The sprint page is the one live Entity whose slug starts with `entity-sprint-` (case 209.1).
> **＋** `tests/test_prespec.py` fixes `--check`.

> **when:**
> `guppi prespec --check` reads a Frontier line whose segments hold `sprint` and whose closer is `case N`.

> **then:**
> An `update` item naming the sprint page under Case N — the parent or any sub-case — is required; without one the finding is `frontier: C<n> closes a sprint item with case N, no update of <sprint slug> under Case N`.
> **＋** A line closed `[-] … · sprint` needs nothing: the item stays on the page as it is.
> **－** A line without `sprint` among its segments is read as today.

```then
create:
  - slug: estimate-prespec-binds-a-sprint-line
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: A Frontier line of the sprint closed by a Case is a finding of prespec --check unless that Case updates the sprint page; a line left [-] with sprint needs nothing
    method: uv run pytest tests/test_prespec.py -k sprint — a line `· sprint · case N` with and without an update of entity-sprint-<id> under Case N, a `[-] … · sprint` line, a line without sprint among its segments
    tags: [harness, workflow, sprint]
update:
  - slug: rule-prespec
    replace:
      - old: "no Case and no `defer` needed (case 310.6)"
        new: "no Case and no `defer` needed (case 310.6), and for every line closed `· case N` while its segments hold `sprint` and no `update` of the sprint page stands under Case N — a decided item of the sprint changes the sprint page (case 314.2)"
    change: a Frontier line of the sprint closed by a Case needs an update of the sprint page under it (case 314.2)
```

```tasks
- [x] update `rule-prespec`
- [x] create `estimate-prespec-binds-a-sprint-line`
- [x] `guppi/prespec.py`: `check_frontier` finds the sprint slug, requires an `update` of it under the closing Case of a `sprint` line; the docstring
- [x] `tests/test_prespec.py`: `· sprint · case N` with and without the `update`; `[-] … · sprint`; a line without `sprint`
- [x] read `estimate-prespec-binds-a-sprint-line`: `uv run pytest tests/test_prespec.py -k sprint`
```

## Case 315 — `rule-vault-layout`: no file of `wiki/` is written by hand

> **context:**
> The layout of the vault lives in §1 of `index.md`: the trees of `raw/`, `archive/` and `wiki/`, "the filename is the slug", the table "System files are Rule-class" and the line "`brief.md`, `sprint.md`, `tags.md` and `log.md` are not pages". Part of it stands on pages already: `raw/` and the archive in `rule-raw-archive`, the shape of a page per category in the six schema rules, History and `log.md` in `rule-page-generation`. The Rule-class table is retired by themes 5 and 6, and the "not pages" line is stale: `sprint.md` and `glossary.md` are Renders of pages, `case-schema.md` too. Nothing holds the layout of `wiki/` itself, the equality of slug and filename, or the rule that no file lands in `wiki/` without a decision — `read_vault` takes `*.md` of a category folder but `schema`, and does not read a file at the root at all. Pages: `rule-harness` a `draft` MOC of eight children; `rule-lint` `built`, the Case touches no Estimate of it — `estimate-lint-catches` keeps its Criterion; the slugs `rule-vault-layout` and `estimate-vault-layout-holds` are free by the Grep over `rules/` and `estimates/`, the nearest are `rule-page-schemas` (the shape of a page, not its place) and `rule-raw-archive` (the layout of `raw/`, not of `wiki/`).

> **problem:**
> Where the layout of `wiki/` lives once `index.md` is gone, and what checks that no file nobody ratified appeared in `wiki/`.

> **given:**
> `read_vault` reads the `*.md` of a category folder but `schema.yaml`; a file at the root of `wiki/` it does not read (`guppi/pages.py`).
> **＋** Every file of `wiki/` is a page, the Render of a page under `governs`, or a record a script keeps by a named rule: `sprint.md` and `glossary.md` under `rule-sprint` and `rule-glossary`, `case-schema.md` under `rule-case-protocol`, `brief.md` by the frame of `rule-brief`, `log.md` from `generate` and `cleanup`, `tags.md` the registry of ratified tags.
> **＋** `tests/test_lint.py` fixes the behaviour on a temp vault.

> **when:**
> `guppi lint` reads the vault.

> **then:**
> A page whose `type` does not match its folder is a `layout` finding.
> **＋** A page whose `slug` is not its filename without the extension is a `layout` finding.
> **＋** A `.md` at the root of `wiki/` whose name no live rule page carries — in `governs` or in its text — is a `layout` finding.
> **－** A category folder without a `schema.yaml` is the finding it is today, not this one.

```then
create:
  - slug: rule-vault-layout
    type: rule
    kind: Leaf
    purpose: Prevents a file from sitting in the vault in a place nobody ratified — under a category it does not belong to, under a name that is not its slug, or at the root of wiki/ with no rule that writes it
    parent: rule-harness
    enforcement: check
    implementation_ref: [guppi/lint.py, tests/test_lint.py]
    estimates: [estimate-vault-layout-holds]
    tags: [harness, workflow]
    sections:
      Purpose: |
        Prevents a file from sitting in the vault in a place nobody ratified. The vault is `vault/wiki/`: one folder per page category — `entities/`, `rules/`, `estimates/`, `lessons/`, `insights/`, `decisions/` — each holding its pages and the `schema.yaml` its rule renders. The filename is the slug: there is no register of identifiers, `ref` and `origin` name filenames, and a page whose `slug` is not its filename is a finding. A page belongs to the folder of its `type`.

        No file of `wiki/` is written by hand. A file is a page, the Render of a page — `sprint.md` from `entity-sprint-migration` under `rule-sprint`, `glossary.md` from `entity-glossary` under `rule-glossary`, `case-schema.md` from `rule-case-protocol` — or a record a script keeps by a named rule: `brief.md` by the frame of `rule-brief`, `log.md` from `generate` and `cleanup`, `tags.md` the registry of tags already ratified in a Case. A `.md` at the root that no live rule page names is a finding: it reached the vault without a decision. `raw/` and `archive/` are the working folders of a session, held by `rule-raw-archive`; the shape of a page is held by its category's schema rule.
  - slug: estimate-vault-layout-holds
    type: estimate
    ref: rule-vault-layout
    kind: QA
    purpose: lint finds a page under the wrong category folder, a page whose slug is not its filename, and a .md at the root of wiki/ that no live rule page names; the live vault has none
    method: uv run pytest tests/test_lint.py -k layout, then make lint — no layout finding on the live vault
    tags: [harness, workflow]
update:
  - slug: rule-harness
    set: {children: [rule-render-harness, rule-settings, rule-lint, rule-page-schemas, rule-vault-layout, rule-governed-files-hook, rule-claude-md, rule-bash-guard, rule-tests-clock-pinned]}
    change: rule-vault-layout, the layout of the vault, after rule-page-schemas (case 315)
```

```tasks
- [x] create `rule-vault-layout` (parent `rule-harness`)
- [x] create `estimate-vault-layout-holds` (ref `rule-vault-layout`)
- [x] update `rule-harness`: `children` with `rule-vault-layout` after `rule-page-schemas`
- [x] `guppi/lint.py`: `check_layout` — `type` against the folder, `slug` against the filename, a root `.md` no live rule names; the docstring
- [x] `tests/test_lint.py`: a page of the wrong `type` in a folder; a page whose slug differs from its filename; an unnamed file at the root; the six live root files clean
- [x] read `estimate-vault-layout-holds`: `uv run pytest tests/test_lint.py -k layout`, then `make lint` — no `layout` finding on the live vault
```

## Case 316 — `rule-session`: the root MOC over the five phases

> **context:**
> The five phases of a session — `rule-session-start`, `rule-plan-mode`, `rule-work-mode`, `rule-end-of-work`, `rule-documentation` — stand as root MOCs with no parent, and their order lives only in the table of §9 of `index.md`. By the rule "a Rule MOC is a workflow" the order of the children is the content, and the MOC's Estimate promises it. Each phase holds its own cross-cutting Estimate inside itself: `estimate-session-start-context` the difference between an ordinary and a working session, `estimate-end-of-work-order` the order Retro → commit → handoff → librarian. Nobody holds the chain whole: that all five left their marks in the session folder, and in that order. Pages: of the five, `rule-session-start`, `rule-plan-mode` and `rule-end-of-work` are `built`, `rule-work-mode` and `rule-documentation` `draft`; the slugs `rule-session` and `estimate-session-phases-in-order` are free by the Grep over `rules/` and `estimates/`, the nearest are `rule-session-start` (the first phase, not the chain) and `rule-harness` (the tools outside the phases). The Estimates of the phases are untouched: a parent is a field, not a promise (case 296).

> **problem:**
> Where the order of the phases lives once `index.md` is gone, and what promises that the chain ran whole.

> **given:**
> A Rule MOC is a workflow: its children are ordered, the order is the content, and the MOC's Estimate promises the order itself (`rule-rules-schema`).
> **＋** A session leaves its marks in `raw/<date>/<hi HHMM>/`: the `hi` line in the day's log, `frontier.md`, `spec.md` with its approved stamp, `handoff.md`; the Retro commit and the librarian's commit in `git log`.
> **＋** A session conserved by `/carry` leaves `carry.md` in place of the last three marks (case 190.3).

> **when:**
> A session has ended, and someone reads its folder and `git log`.

> **then:**
> All five phases left a mark, and the marks ascend in time: `hi` → `frontier.md` → `spec.md` approved → the Retro commit → `handoff.md` → the librarian's commit.
> **＋** `rule-session` is the parent of the five phases, its children in that order.
> **－** A session conserved by `/carry` ends at `carry.md`: the marks of Work Mode, End of Work and Documentation are absent, and that is not a failure.

```then
create:
  - slug: rule-session
    type: rule
    kind: MOC
    purpose: Prevents a phase of the session from running out of its turn, or a session from ending with a phase that left no mark
    children: [rule-session-start, rule-plan-mode, rule-work-mode, rule-end-of-work, rule-documentation]
    estimates: [estimate-session-phases-in-order]
    tags: [session, workflow]
    sections:
      Purpose: |
        Prevents a phase of the session from running out of its turn. A session is five phases in one order: Session Start, Plan Mode, Work Mode, End of Work, Documentation. Each child holds its own mechanism and its own Estimate; this MOC holds what none of them owns — that the chain ran whole, in order. The guards of the order live in the children: the ledger hook refuses a line in a session no `/hi` opened; the pre-spec hook refuses `ExitPlanMode` before `/pre-spec` ran; `guppi gate` refuses `/handoff` on a dirty tree; `rule-close` keeps the librarian's commit out of the session's. The marks each phase leaves stand in the session folder and in `git log`, and they ascend in time. A session conserved by `/carry` stops after Plan Mode and leaves `carry.md`: the last three phases have no mark, and that is the second lawful ending, not a break in the order (case 190.3).
  - slug: estimate-session-phases-in-order
    type: estimate
    ref: rule-session
    kind: QA
    purpose: The five phases of a finished session left their marks in the session folder and in git log, ascending in time; a conserved session ends at carry.md
    method: by hand at the close of a session — the hi line of the day's log, frontier.md, the approved stamp of spec.md, the Retro commit, handoff.md, the librarian's commit, read in that order
    tags: [session, workflow]
update:
  - slug: rule-session-start
    set: {parent: "[[rule-session]]"}
    change: the parent is rule-session, the MOC of the five phases (case 316)
  - slug: rule-plan-mode
    set: {parent: "[[rule-session]]"}
    change: the parent is rule-session, the MOC of the five phases (case 316)
  - slug: rule-work-mode
    set: {parent: "[[rule-session]]"}
    change: the parent is rule-session, the MOC of the five phases (case 316)
  - slug: rule-end-of-work
    set: {parent: "[[rule-session]]"}
    change: the parent is rule-session, the MOC of the five phases (case 316)
  - slug: rule-documentation
    set: {parent: "[[rule-session]]"}
    change: the parent is rule-session, the MOC of the five phases (case 316)
```

```tasks
- [x] create `rule-session` (MOC, root, five children in order)
- [x] create `estimate-session-phases-in-order` (ref `rule-session`)
- [x] update `rule-session-start`, `rule-plan-mode`, `rule-work-mode`, `rule-end-of-work`, `rule-documentation`: `parent: rule-session`
- [ ] read `estimate-session-phases-in-order`: by hand at the close of this session — the six marks in order
```

## Case 317 — `rule-atomicity`: the rule that splits a unit, rendered into the Case schema

> **context:**
> §6 of `index.md` holds the atomicity rule: a unit stays whole while its closing judgment is indivisible; once it breaks into conditions that fail apart and are fixed apart, it splits into children. Only the specializations stand on pages: `rule-entities-schema` the MOC/Leaf cut and the Entity vs Estimate fork, `rule-rules-schema` "a Rule MOC is a workflow", `case-schema.md` the Splitting section for a Case. The statement itself, the pair test and the scope are nowhere, and `rule-entities-schema` points at "§6 of `index.md`", a pointer theme 4 removes. The rule cannot be checked in substance — like `rule-language` and `rule-agent-writing`, whose guard is that their text stands in the file the agent reads and does not drift from the page. Pages: `rule-case-protocol` a `draft` Leaf, `render_mode: full`, four Estimates, none touched — the Case adds a child and a marker line; `rule-entities-schema` `draft`, `rule-rules-schema` `draft`, `rule-prespec` `built` — each changed outside its Criterion. The slugs `rule-atomicity` and `estimate-atomicity-rendered` are free by the Grep over `rules/` and `estimates/`; the nearest are `rule-language` and `rule-agent-writing`, the same pattern on another file.

> **problem:**
> Where the rule that splits a unit lives once `index.md` is gone, and what it refuses when it cannot be checked in substance.

> **given:**
> `rule-render-harness`: a page with `render_mode: partial` writes the body of its `## Render` between the markers `<!-- rule-slug -->` … `<!-- /rule-slug -->` of the file in `governs`; `render --check` catches a drift.
> **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
> **＋** `rule-case-protocol` renders `case-schema.md` whole; `/hi` loads it in every working session.
> **＋** `pre-spec` refuses a Case with two Estimate items and no written `sections: Criterion` — the one mechanical refusal of this rule, signed for `rule-prespec`.

> **when:**
> `guppi render` writes the files, and the agent reads `case-schema.md` at the start of a session.

> **then:**
> `case-schema.md` holds the text of `rule-atomicity` between its markers: the statement, the pair test — list the conditions of "done", and for each pair ask whether one could fail while the other passes and needs a different fix — and the scope: Case, Entity, Rule, Estimate; not a Lesson, a recorded fact does not split; not an Insight, which is born by clustering, the same rule in reverse; depth is not fixed in advance.
> **＋** `render --check` after the render exits 0; a hand edit of the file is refused by the hook.
> **＋** `rule-case-protocol` is a MOC with the child `rule-atomicity` and a marker line in its Render.
> **－** The rule has no refusal of its own in substance: the refusal of two promises in one Case stays with `rule-prespec`.

```then
create:
  - slug: rule-atomicity
    type: rule
    kind: Leaf
    purpose: Prevents a unit from being split or kept whole by taste — one closing judgment, one unit; two conditions that fail apart are two children
    parent: rule-case-protocol
    enforcement: render
    render_mode: partial
    governs: vault/wiki/case-schema.md
    estimates: [estimate-atomicity-rendered]
    tags: [harness, workflow]
    sections:
      Purpose: |
        Prevents a unit from being split or kept whole by taste. The rule cannot be checked in substance, so its guard is the one `rule-language` and `rule-agent-writing` have: the text stands in the file the agent reads — `case-schema.md`, loaded by `/hi` in every working session — and `render --check` keeps it identical to this page, while the governed-files hook refuses a hand edit. The one mechanical refusal of the rule is `pre-spec` on two Estimate items in a Case with no written Criterion, signed for `rule-prespec`.
      Render: |
        ## Atomicity — when a unit splits

        A unit stays whole as long as its closing act — ratification, a reading, `built` — is one indivisible judgment. The moment it breaks into two or more conditions that can fail independently and need different fixes, it splits into children.

        The test is mechanical. List the conditions of "done". For each pair, ask: could one fail while the other passes, and would the fix be a different one? Yes for any pair — split.

        It holds for a Case, an Entity, a Rule and an Estimate alike. Not for a Lesson: a recorded fact does not split. Not for an Insight: it is born by clustering, which is this rule running in reverse. Depth is not fixed in advance — it follows the rule and nothing else. Two conditions that are different behaviours are two children; the same behaviour checked from two angles is one page and two Estimates.
  - slug: estimate-atomicity-rendered
    type: estimate
    ref: rule-atomicity
    kind: QA
    purpose: The text of rule-atomicity stands between its markers in case-schema.md, identical to the page, and a hand edit of the file is refused
    method: make lint — render --check exit 0; the text between the markers of case-schema.md read by hand after the librarian's render
    tags: [harness, workflow]
update:
  - slug: rule-case-protocol
    set: {kind: MOC, children: [rule-atomicity]}
    replace:
      - old: "## Splitting"
        new: "<!-- rule-atomicity -->\n<!-- /rule-atomicity -->\n\n## Splitting"
    change: a MOC with the child rule-atomicity, whose marker line stands above Splitting (case 317)
  - slug: rule-entities-schema
    replace:
      - old: "the atomicity rule of §6 of `index.md`"
        new: "the atomicity rule of [[rule-atomicity]]"
    change: the atomicity rule is named by its page, not by a § of index.md (case 317)
  - slug: rule-rules-schema
    replace:
      - old: "atomicity rule applies as everywhere: split when parts fail independently and are fixed differently."
        new: "atomicity rule of [[rule-atomicity]] applies as everywhere: split when parts fail independently and are fixed differently."
    change: the atomicity rule is named by its page (case 317)
  - slug: rule-prespec
    replace:
      - old: "one promise per Case: split it"
        new: "one promise per Case: split it, by [[rule-atomicity]]"
    change: the one promise per Case check names rule-atomicity (case 317)
  - slug: entity-glossary
    replace:
      - old: "| Atomicity Rule | A unit splits when its closing judgment breaks into parts that fail and are fixed apart | [[rule-entities-schema]] |"
        new: "| Atomicity Rule | A unit splits when its closing judgment breaks into parts that fail and are fixed apart | [[rule-atomicity]] |"
    change: the term Atomicity Rule is defined by rule-atomicity (case 317)
```

```tasks
- [x] create `rule-atomicity` (parent `rule-case-protocol`, `render_mode: partial`, `governs: vault/wiki/case-schema.md`)
- [x] create `estimate-atomicity-rendered` (ref `rule-atomicity`)
- [x] update `rule-case-protocol`: `kind: MOC`, `children: [rule-atomicity]`, the marker line in its Render
- [x] update `rule-entities-schema`: `[[rule-atomicity]]` in place of the `§6 of index.md` pointer
- [x] update `rule-rules-schema`: `[[rule-atomicity]]` beside the order of a Rule MOC's children
- [x] update `rule-prespec`: `[[rule-atomicity]]` beside "one promise per Case"
- [x] update `entity-glossary`: the row "Atomicity Rule" — `where` is `[[rule-atomicity]]`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi glossary`
- [ ] read `estimate-atomicity-rendered`: `make lint` — `render --check` exit 0; the text between the markers of `case-schema.md` read by hand
```

## Case 318 — `index.md` leaves: the map dissolved into pages

> **context:**
> `index.md` is the map of the vault in thirteen §. After 315, 316 and 317 every § is covered by a page: §0, §2, §3 and §12 by `rule-case-protocol`; §1 by `rule-vault-layout` and `rule-raw-archive`; §4 by `rule-ledger-write`; §5 by `rule-materialize`; §6 by `rule-atomicity`; §7 by `rule-estimates-schema`; §8 by `rule-lessons-schema`, `rule-insights-schema` and `rule-synthesis`; §9 by `rule-session`; §10 by `rule-documentation`; §11 by `rule-ask`. What is left is the file and its pointers: a live `§N` or a mention of the file stands on six rule pages (`rule-ask`, `rule-materialize`, `rule-skill-hi`, `rule-case-protocol`, `rule-claude-md`, `rule-prespec`), on `entity-glossary` in two rows, on five Estimates and in `RULE_CLASS` of `guppi/materialize.py`; four harness files — `CLAUDE.md`, `ask-guppi.md`, the `/hi` and `/pre-spec` skills — are repaired by the render of their rules, and `entities/schema.yaml` by the render of `rule-entities-schema`. Estimates: `estimate-sprint-migration-index-dissolved` (created by 310.3) is the promise of this work and is read here; of the five carrying a pointer four are `pending` already (`estimate-glossary-terms-defined`, `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-sprint-migration-merges`, `estimate-sprint-migration-rule-class-files-dissolved`), `estimate-raw-archive` is changed in its `## Context` and keeps its status (case 296), and `estimate-case-protocol-ledger-line-form` is the one `passed` page whose Criterion is touched: it goes `pending` and is read again. The rest of the `file` route in the scripts is theme 5.

> **problem:**
> How the file and its thirty pointers go without leaving a live page that sends a reader to a § that no longer exists.

> **given:**
> Every § is covered by a live page after 315, 316 and 317.
> **＋** `guppi render` rewrites `CLAUDE.md`, `.claude/agents/ask-guppi.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/case-schema.md` and `vault/wiki/entities/schema.yaml` from their rules.
> **＋** A `replace` inside a Criterion sets the Estimate `pending`; in another section it does not (case 296).

> **when:**
> The last `update` of this Case is applied, the file is deleted in Work Mode, and `rg` walks the live tree.

> **then:**
> `vault/wiki/index.md` does not exist.
> **＋** No live page of `wiki/`, no harness file and no docstring of `guppi/` points at a `§N` or at `index.md` as a source; the archive and `raw/` keep their pointers.
> **＋** `RULE_CLASS` of `guppi/materialize.py` does not hold `index`.
> **－** The rest of the `file` route — `RULE_CLASS` whole, "applied by hand", `prose_names` — stands until theme 5.

```then
delete:
  - slug: index
    file: vault/wiki/index.md
    impact: the thirteen § are covered by live pages after 315, 316 and 317; every live pointer is rewritten by this Case, the harness files by the render of their rules; the archive and raw/ keep theirs; the file route of the scripts stands until theme 5
update:
  - slug: rule-ask
    replace:
      - old: "the librarian asks by finished content afterwards, as §11 of the map says."
        new: "the librarian asks by finished content afterwards ([[rule-index-check]])."
      - old: "Grep `vault/wiki/index.md` when the proposal may cross a rule of the vault itself."
        new: "Grep the rules of the vault itself — `vault/wiki/rules/` — when the proposal may cross one."
    change: the index lines and the vault's own rules named by their pages, not by a § of index.md (case 318)
  - slug: rule-materialize
    replace:
      - old: "Its route is computed from `index.md` §5."
        new: "Its route is the Routing Table of this page."
    change: the route is this page, not §5 of index.md (case 318)
  - slug: rule-skill-hi
    replace:
      - old: "(§3 of `vault/wiki/index.md`)."
        new: "([[rule-ask]])."
    change: the vault query is named by rule-ask (case 318)
  - slug: rule-case-protocol
    replace:
      - old: "the map of the vault is [[index]]"
        new: "the layout of the vault is [[rule-vault-layout]] and the phases of a session [[rule-session]]"
      - old: "A Rule-class file (`index.md`, `glossary.md`, a schema)"
        new: "A Rule-class file (a schema)"
    change: the map replaced by rule-vault-layout and rule-session; index.md out of the Rule-class list (case 318)
  - slug: rule-claude-md
    replace:
      - old: "its map is `vault/wiki/index.md`; its terms are"
        new: "its terms are"
    change: CLAUDE.md names the glossary alone; the map is gone (case 318)
  - slug: rule-prespec
    replace:
      - old: "a rule of `index.md`, or each other"
        new: "a rule of the vault, or each other"
    change: the vault's rules named as pages, not as index.md (case 318)
  - slug: entity-glossary
    replace:
      - old: "| Rule-class files | `index.md`, changed by a ratified `update` with `file`, by hand; `glossary.md` left the list with case 306"
        new: "| Rule-class files | `glossary.md` left the list with case 306"
      - old: "| `CLAUDE.md`, `case-schema.md`, `index.md` |"
        new: "| `CLAUDE.md`, `case-schema.md` |"
    change: index.md out of the two rows that named it (case 318)
  - slug: estimate-case-protocol-ledger-line-form
    set: {method: "one reading by hand of case-schema.md after the render, at a session start"}
    replace:
      - old: "the Case schema is the Render of `rule-case-protocol`, and §4 of `index.md` is the second copy of the line's form"
        new: "the Case schema is the Render of `rule-case-protocol`, the one place the line's form is written"
      - old: "`case-schema.md` or `index.md` §4"
        new: "`case-schema.md`"
      - old: "The ledger paragraph of the schema and §4 of the map say"
        new: "The ledger paragraph of the schema says"
    change: the Criterion reads case-schema.md alone; the second copy in index.md is gone (case 318)
  - slug: estimate-glossary-terms-defined
    replace:
      - old: "§N` and `here` on the page whose meaning they name"
        new: "`here` on the page whose meaning they name"
    change: the rows on §N are gone with index.md (case 318)
  - slug: estimate-synthesis-keeps-actioned-by-the-mark
    replace:
      - old: "§8 of the map and the glossary name the exception"
        new: "the schema of Insights and the glossary name the exception"
    change: the exception is named by the schema and the glossary, not by §8 (case 318)
  - slug: estimate-sprint-migration-merges
    replace:
      - old: "(`index.md` §6)"
        new: "([[rule-atomicity]], [[rule-entities-schema]])"
    change: order as the content of a page named by its rules (case 318)
  - slug: estimate-raw-archive
    replace:
      - old: "`rule-cleanup` and `index.md` §1 say \"`raw/` stays\""
        new: "`rule-cleanup` and [[rule-vault-layout]] say \"`raw/` stays\""
    change: the layout named by its rules (case 318)
  - slug: entity-sprint-migration
    replace:
      - old: "- [[estimate-sprint-migration-index-dissolved]] — 4. `index.md`: one Case per §: covered by a rule page, the § leaves; not covered, a rule is made; the last Case removes the file and every `§N` pointer in the vault"
        new: "- [[estimate-sprint-migration-index-dissolved]] — 4. `index.md`: the thirteen § covered by `rule-vault-layout`, `rule-session`, `rule-atomicity` and the pages that held them already; the file and every `§N` pointer gone (cases 315–318)"
    change: theme 4 done — the § covered by pages, the file and its pointers gone (case 318)
```

```tasks
- [x] delete `vault/wiki/index.md` by hand in Work Mode
- [x] update `rule-ask`, `rule-materialize`, `rule-skill-hi`, `rule-case-protocol`, `rule-claude-md`, `rule-prespec`
- [x] update `entity-glossary`: the rows "Rule-class files" and "`CLAUDE.md`, `case-schema.md`, `index.md`"
- [x] update `estimate-case-protocol-ledger-line-form`, `estimate-glossary-terms-defined`, `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-sprint-migration-merges`, `estimate-raw-archive`
- [x] update `entity-sprint-migration`: theme 4 closed
- [x] `guppi/materialize.py`: `RULE_CLASS` without `index`
- [x] `uv run guppi render`: `CLAUDE.md`, `.claude/agents/ask-guppi.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/case-schema.md`, `vault/wiki/entities/schema.yaml`
- [x] `uv run guppi glossary`
- [x] `uv run guppi sprint`
- [ ] read `estimate-sprint-migration-index-dissolved`: `test -e vault/wiki/index.md` false; `rg` over `vault/wiki`, `.claude`, `guppi`, `CLAUDE.md` — empty but for the archive and `raw/`
- [ ] read `estimate-case-protocol-ledger-line-form`: by hand at a session start — `case-schema.md` alone now
```

## Case 319 — reuse in the Backlog: the `uses` edge, the question in `rule-ask`, the hook in lint

> **context:**
> The architecture catches a duplicate three times, and all three are at the moment of the decision: `rule-ask` before a `create` without `ref`, `pre-spec` before the Spec is approved, and the index check of the librarian, who may turn a `create` into an `update`. Two things are missing. The vault query asks "does this exist" but not "what of this already exists that the thing could use"; and the relation "A uses B" is written nowhere: `parent`/`children` is decomposition, `applies_to`/`rules` (case 305) is Rule → Entity only, and an Entity → Entity edge does not exist. So nobody can ask what a change to a module breaks, and the next agent sees no example of reuse. The Backlog line "the product model … `ask-guppi` through Entities" (session 1119) is about the same thing but names neither the edge nor the check. Pages: `entity-sprint-migration` `draft`, changed in this session by 310.2 and 318; the change is in `## Backlog` and touches no Estimate (case 296).

> **problem:**
> The shape of reuse was worked out in this session and is lost by the next one unless the Backlog names its cut.

> **given:**
> A note in a milestone or in the Backlog is a task not yet cut into pages; it leaves only by the `update` of the Case that cuts it (case 313).
> **＋** `applies_to`/`rules` is the pattern of an edge: one side written in the Case, the backlink computed by the cascade of `generate`, the pair checked by lint (case 305).
> **＋** An edge Rule → Rule is refused: a rule constrains a case, never another rule (case 305).

> **when:**
> The `/hi` of a later session takes the Backlog, or the person names the reuse item.

> **then:**
> The Backlog holds three notes: the edge `uses` / `used_by` between Entities — `uses` written in the Case, `used_by` by the cascade, the pair checked by lint, no Rule → Rule; the second required question of the vault query — what of the existing the thing could use, the answer in `context`, and the Case names what it found in `uses` or says why not; a lint finding on two live Entities naming one path in `code_ref` with no edge between them.
> **＋** The product-model line stays: `kind` and the records of a product are its part, not covered by the three notes.
> **－** This Case creates no page: a later session cuts the notes.

```then
update:
  - slug: entity-sprint-migration
    replace:
      - old: "the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)"
        new: "the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)\n- reuse, the edge: `uses` / `used_by` between Entities — `uses` written in the Case on the side that uses, `used_by` computed by the cascade of `generate`, the pair checked by lint, the pattern of `applies_to` / `rules`; no edge Rule → Rule (cases 305, 319)\n- reuse, the question: the vault query before a `create` asks a second question — what of the existing this thing could use, by the index lines of the Entities — and the answer stands in `context`; the Case names what it found in `uses` or says why it is not used (case 319)\n- reuse, the hook: a lint finding on two live Entities naming one path in `code_ref` with no edge between them; a new module written beside an existing one in another file is caught by the question alone, not by a script (case 319)"
    change: three notes of the reuse model in the Backlog — the edge, the question, the hook (case 319)
```

```tasks
- [x] update `entity-sprint-migration`: three notes in `## Backlog`
- [x] `uv run guppi sprint`
```

## Case 320 — the `file` route leaves the scripts

> **context:**
> A Rule-class file changed by a route of its own: `RULE_CLASS` and `rule_class_path` in `materialize.py` give an entry `category: file` with its `path`, `generate` prints "a Rule-class file, applied by hand" and marks it applied, `prespec` matches an item by `file` in `line_has_item` and `item_has_line`, and `check_governed` refuses a `file` on a path a live rule governs. After 304 (the schemas as Renders of rules), 306 (the glossary) and 318 (`index.md` deleted) no file of that class is left; `prose_names` left lint with 304. The route is described on four pages (`rule-case-protocol`, `rule-lint`, `rule-decisions-schema`, `rule-prespec`) and in the Criteria of four Estimates; `estimate-materialize-finds-a-rule-class-item` (`passed`) promises the route itself. Case 310.4 of this session created the Estimate of theme 5 with the line "a ledger line with `file` is `unparsed`" — wrong: `file` is a key of a `then` item, not part of a ledger line, and a slug without a prefix lands `category: unknown`. This Case is written whole in its place. `rule-morph` (defer 239, Slice 5) does not touch the route — it is about the category set of a project, and its compatibility with the six schema rules is already held by 304.

> **problem:**
> The route is dead but alive in four scripts, on four pages and in four promises; and the promise of theme 5 is worded wrong.

> **given:**
> No Rule-class file is left: the schemas are Renders of rules (304), the glossary (306), `index.md` is deleted (318), `case-schema.md` and `CLAUDE.md` are Renders (273, 59.8).
> **＋** `category_of` returns `None` for a slug without a prefix, and the entry lands `category: unknown`.
> **＋** A `replace` inside a Criterion sets the Estimate `pending` (case 296).
> **＋** `tests/test_materialize.py`, `tests/test_generate.py` and `tests/test_prespec.py` fix the behaviour.

> **when:**
> `make test` and `make lint` run after the route is removed.

> **then:**
> `rg 'RULE_CLASS|rule_class|applied by hand|prose_names' guppi/` is empty.
> **＋** An `update` item carrying `file` is a `pre-spec` finding — the file route is gone; `check_governed` refuses any such item, not only one on a governed path.
> **＋** A ledger line whose slug has no category prefix lands `category: unknown`, and `generate` reports an error instead of "applied by hand".
> **＋** `make test` is green and `make lint` has no finding on a schema.
> **－** `rule-morph` is untouched: the category set is its business, not the file route.

```then
create:
  - slug: estimate-sprint-migration-file-route-gone
    type: estimate
    ref: entity-sprint-migration
    kind: QA
    purpose: The file route is out of the scripts — no RULE_CLASS, rule_class, applied by hand or prose_names in guppi/; an update item with file is a pre-spec finding; a slug without a prefix lands category unknown; tests green and lint clean on the schemas
    method: at the close of theme 5 — rg 'RULE_CLASS|rule_class|applied by hand|prose_names' guppi/ empty; make test; make lint
    tags: [sprint, workflow, harness]
delete:
  - slug: estimate-materialize-finds-a-rule-class-item
    impact: the promise ceases to exist with the route; rule-materialize loses it from estimates by the cascade; no other page names it
update:
  - slug: rule-case-protocol
    replace:
      - old: "A Rule-class file (a schema) is an `update` with `file` and `change`, applied by hand in Work Mode; `CLAUDE.md` and this file are not — they are rendered"
        new: "`CLAUDE.md` and this file are rendered"
    change: the Rule-class file route is gone from the Case schema (case 320)
  - slug: rule-lint
    replace:
      - old: "Pages are written by the generator and, for the Rule-class files, by hand;"
        new: "Pages are written by the generator;"
    change: no page is written by hand (case 320)
  - slug: rule-decisions-schema
    replace:
      - old: "each the slugs of those lines in ledger order (a page, or a Rule-class file such as `case-schema`)"
        new: "each the slugs of those lines in ledger order"
      - old: "The category is derived from the slug prefix or the Rule-class map, never written."
        new: "The category is derived from the slug prefix, never written."
      - old: "a page, or a Rule-class file by its ledger slug (`case-schema`, `rules-schema-yaml`)"
        new: "a page"
      - old: "Lists of quoted wikilinks for page slugs, a Rule-class slug bare, so Obsidian shows them as links (case 148.2)"
        new: "Lists of quoted wikilinks for page slugs, so Obsidian shows them as links (case 148.2)"
      - old: "The category is derived from the slug prefix or the Rule-class map and never written"
        new: "The category is derived from the slug prefix and never written"
    change: a Decision target is a page; the Rule-class map is gone (case 320)
  - slug: rule-prespec
    replace:
      - old: "for every `file` item on a path a Rule page governs"
        new: "for every `update` item carrying `file` — the file route is gone (case 320)"
    change: any file item is a finding, not only one on a governed path (case 320)
  - slug: estimate-case-protocol-case-form
    replace:
      - old: "are Rule-class files: an `update` with `file` and `change`, applied by hand in Work Mode;"
        new: "are the Renders of their rule pages (case 304);"
    change: the Criterion names the Renders, not the file route (case 320)
  - slug: estimate-generate-fails-alone
    replace:
      - old: "A Rule-class file entry prints `a Rule-class file, applied by hand` and is marked applied; an `update` with no content prints"
        new: "An `update` with no content prints"
    change: no Rule-class branch in generate (case 320)
  - slug: estimate-generate-ticks-the-spec
    replace:
      - old: "**－** A Rule-class file entry `generate` does not apply — \"applied by hand\"."
        new: "**－** An `update` item carrying `file` is a pre-spec finding and never reaches `generate` (case 320)."
      - old: "`lesson` and Rule-class file entries, and an entry marked `failed`, tick no line"
        new: "`lesson` entries and an entry marked `failed` tick no line"
    change: no Rule-class entry reaches generate (case 320)
  - slug: estimate-prespec-checks-the-plan
    replace:
      - old: "a `defer` line matches a `defer` item, a Rule-class file line an `update` with that `file` or `slug`"
        new: "a `defer` line matches a `defer` item; an `update` item carrying `file` is a finding of its own (case 320)"
    change: the file route is a finding, not a route (case 320)
  - slug: entity-sprint-migration
    replace:
      - old: "5. scripts: the audit"
        new: "5. scripts (case 320): the audit"
    change: theme 5 done — the file route out of the scripts (case 320)
```

```tasks
- [x] create `estimate-sprint-migration-file-route-gone` (ref `entity-sprint-migration`, supersedes 310.4)
- [x] delete `estimate-materialize-finds-a-rule-class-item`
- [x] update `rule-case-protocol`, `rule-lint`, `rule-decisions-schema`, `rule-prespec`
- [x] update `estimate-case-protocol-case-form`, `estimate-generate-fails-alone`, `estimate-generate-ticks-the-spec`, `estimate-prespec-checks-the-plan`
- [x] update `entity-sprint-migration`: theme 5 closed
- [x] `guppi/materialize.py`: `RULE_CLASS`, `rule_class_path`, `category: file` and `path` gone; the docstring
- [x] `guppi/generate.py`: the `category == "file"` branch gone; "an update with no content in the Spec" reworded off "applied by hand"; the docstring
- [x] `guppi/prespec.py`: `rule_class_path` out of `line_has_item` and `item_has_line`; `check_governed` refuses any `update` item with `file`; the docstring
- [x] `tests/test_materialize.py`, `tests/test_generate.py`, `tests/test_prespec.py`: a `file` item is a pre-spec finding; a slug without a prefix lands `category: unknown`; no Rule-class branch remains
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/case-schema.md`, `vault/wiki/decisions/schema.yaml`
- [x] `uv run guppi sprint`
- [x] read `estimate-sprint-migration-file-route-gone`: the `rg`, `make test`, `make lint`
- [ ] read `estimate-case-protocol-case-form`, `estimate-generate-fails-alone`, `estimate-generate-ticks-the-spec` — their Criteria changed
```

## Case 321 — theme 6: "Rule-class" is retired and Slice 3f closes

> **context:**
> "Rule-class" was the name of fourteen files that changed by a decision but by hand. After 304, 306, 318 and 320 no such file and no such route is left; the term outlived its thing. It stands live in two places: the row "Rule-class files" of the `## Terms` of `entity-glossary`, which says of itself "the term is retired with theme 6 of Slice 3f", and the tail of the row on `CLAUDE.md` and `case-schema.md` describing the map read a section at a time — there is no map. Two pointers 318 did not touch: `(§1 of `index.md`)` in the Criterion of `estimate-sprint-migration-rule-class-files-dissolved` and the fragment on the glossary row in `estimate-glossary-terms-defined`; without them the reading of theme 4 would find a live `§N`. Pages: `entity-sprint-migration` `draft`, changed in this session by 310.2, 318, 319 and 320; `entity-glossary` `draft`, changed by 317 and 318; the Estimate of the Slice is `pending` and is read here; `estimate-glossary-terms-defined` is `pending` and read by W3.

> **problem:**
> A term without its thing, two pointers at a deleted file, and a Slice standing finished in Milestones.

> **given:**
> A retired term is a History line, not a row (`entity-glossary`).
> **＋** `guppi sprint` renders `## Milestones` in the order of the page and copies `## Closed` as it stands (case 229.2).
> **＋** A `replace` inside a Criterion sets the Estimate `pending` (case 296).

> **when:**
> The librarian applied the Case and ran `glossary` and `sprint`; the reading of the Slice's Estimate is taken.

> **then:**
> Neither `entity-glossary` nor `glossary.md` holds the term "Rule-class"; the row on `CLAUDE.md` and `case-schema.md` does not describe reading the map.
> **＋** No live Criterion points at a `§N` or at `index.md` as a source.
> **＋** `## Milestones` holds Slice 3b, Slice 4 and Slice 5; Slice 3f is named in `## Closed` as prose, with cases 301, 304–306, 310, 315–321.
> **－** The Slice's Estimate stays in the `estimates` of the sprint page: it is one of the four promises of the sprint's "done", not a milestone item.

```then
update:
  - slug: entity-glossary
    replace:
      - old: "Insight: `severity` (children not archived), `addressed_by` | [[rule-page-schemas]] | | Rule-class files | `glossary.md` left the list with case 306 — rendered from `entity-glossary` — the schemas with case 304 — each the Render of a rule page — and `case-schema.md` with case 273; the term is retired with theme 6 of Slice 3f | [[rule-page-schemas]] |"
        new: "Insight: `severity` (children not archived), `addressed_by` | [[rule-page-schemas]] |"
      - old: "(cases 273, 288); the map is read a section at a time — layout, routing, ledger, splitting, librarian | [[rule-claude-md]] |"
        new: "(cases 273, 288) | [[rule-claude-md]] |"
    change: the term Rule-class files retired with its thing; the map leaves the CLAUDE.md row (case 321)
  - slug: estimate-sprint-migration-rule-class-files-dissolved
    replace:
      - old: "by hand (§1 of `index.md`)"
        new: "by hand"
    change: the pointer at §1 of index.md is gone with the file (case 321)
  - slug: estimate-glossary-terms-defined
    replace:
      - old: "the row Rule-class files rewritten to the fact;"
        new: "the row Rule-class files gone with the term (case 321);"
    change: the Rule-class row is retired, not rewritten (case 321)
  - slug: entity-sprint-migration
    sections:
      Milestones: |
        ### Slice 3b — Work Mode

        - [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; the sentence of [[insight-workflow-code-live-before-the-page-it-reads]] on a check that reads a page the same Spec changes; cases 183, 206, 238
        - [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206

        ### Slice 4 — conversion of the parked pages by group

        - [[estimate-sprint-migration-leftovers-gone]] — every page of `vault/parked/` and every document of 2026-08 under `docs/` converted, archived or deleted by a decision

        ### Slice 5 — closing

        - [[estimate-sprint-migration-lint-clean]] — `make lint` exit 0: the 31 Decision pages of Cases 1–28 decided, `unmigrated` at zero
        - [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`; at the close [[rule-git-context]] and [[rule-github-issues]] — the upstream of the branch and the GitHub remote, decisions 11.1, 11.2, defers 220, 243 — read by [[estimate-sprint-migration-leftovers-gone]]
        - [[rule-spec-box]] — the Spec box, case 207, after Slice 3b
        - [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239
      Closed: |
        Slices 0–2 closed by 2026-09-10: layout; ledger, event log, `/hi`; renderer, lint,
        indexes, `/ask`, pre-spec (then `/pre-task`). Slice 3 (materialize, generate, cleanup, librarian, retro,
        handoff) built 2026-09-10, closed 2026-09-12. Slice 3c (the raw lifecycle: the archive
        of an applied session, the tail, one archive root, the ledger of a session, the status
        cascades, the slug checked against the archive) built 2026-09-13. Slice 3d (the
        Estimate model, case 182) opened and closed 2026-09-16: Cases 187–190 ratified in
        session 1034 and conserved, repaired by 193–198 and built in session 1651, case 191
        taken up by 201–203 and built in session 1955 — `generate`, `lint`, `pre-spec` by the
        model. The recut of each old Estimate at its first touch runs on past the Slice: lint
        counts the remainder as `unmigrated` (42 at the close of 3d) and the old shape is
        removed when it reaches zero. Kept without a page: `/grill-me`; `git pull` in `/hi`
        without an upstream (decision 11.1); `gh` not logged in, no GitHub remote (11.2) —
        both decided again at the close (`estimate-sprint-migration-leftovers-gone`).

        Slice 3f (the Rule-class files into the graph, case 301) opened 2026-09-22 and closed
        the same day: the six schemas as rule pages under `rule-page-schemas` (304), the edge
        Rule → Entity (305), the glossary as `entity-glossary` under `rule-glossary` (306);
        then `rule-vault-layout` (315), `rule-session` over the five phases (316),
        `rule-atomicity` rendered into the Case schema (317), `index.md` and its thirty
        pointers gone (318), the `file` route out of the scripts (320), the term "Rule-class"
        retired (321). A sprint item is a page and a note is a task not yet cut (310, 313).
        No file of `vault/wiki/` is written by hand.
    change: Slice 3f closed — out of Milestones, named in Closed with its cases (case 321)
```

```tasks
- [x] update `entity-glossary`: the row "Rule-class files" gone; the tail of the `CLAUDE.md` row on reading the map gone
- [x] update `estimate-sprint-migration-rule-class-files-dissolved`: the `§1 of index.md` pointer gone
- [x] update `estimate-glossary-terms-defined`: the fragment on the Rule-class row
- [x] update `entity-sprint-migration`: `## Milestones` without Slice 3f, `## Closed` with it
- [x] `uv run guppi glossary`
- [x] `uv run guppi sprint`
- [ ] read `estimate-sprint-migration-rule-class-files-dissolved`: by its `method` — `ls vault/wiki/*/schema.md` empty, `vault/wiki/index.md` absent, the `rg` over `guppi/` empty, `render --check`, `glossary --check`, `make lint` exit 0
```

## Case 323 — the text this Spec leaves stale

> **context:**
> Pre-spec found seven places where a page speaks of a thing this Spec changes and no Case names it. `entity-sprint-migration` names `wiki/index.md` in its `purpose` field and in its Purpose, which 318 deletes, and counts its Estimates — 310.2 writes "four" while 310.3 and 320 create two more, making six. `estimate-lint-catches` enumerates the finding classes of lint, and 315 adds `layout`. `estimate-prespec-checks-the-plan` holds the line "Governed: an `update` item with `file` on a path a live Rule page governs", which 320 revokes. The Purpose of `rule-harness` names three steps of `make lint` without the glossary and "Four more" children — 306.5 added the fourth step, 315 adds the ninth child — while `estimate-harness-pipeline` already demands four steps: the page contradicts its own promise. `estimate-materialize-marks-superseded` describes what the mark does, and 309 adds the move of a folded reading. Two rows of `entity-glossary` — Sprint and Session — describe what 313 and 316 change. Statuses: `estimate-lint-catches` and `estimate-materialize-marks-superseded` are `passed` and go `pending`; `estimate-prespec-checks-the-plan` and `estimate-harness-pipeline` are `pending` already in this Spec.

> **problem:**
> Seven live texts become false the moment the Spec is applied; two of them are Criteria a reading is later taken by.

> **given:**
> A `replace` inside a Criterion sets the Estimate `pending`; a change to a field or to another section does not (case 296).
> **＋** 318 deletes `index.md`, 315 adds the `layout` class and the ninth child of `rule-harness`, 320 revokes the `file` route, 309 changes what the mark does, and 313 and 316 change the things of two glossary rows.

> **when:**
> The librarian applied the Spec, and someone reads these pages.

> **then:**
> None of the seven pages describes its thing as it stood before this Spec.
> **＋** `entity-sprint-migration` names `index.md` neither in its field nor in its Purpose, and counts its Estimates by no number.
> **＋** The Purpose of `rule-harness` names four steps of `make lint` and five rules outside the pipeline, and does not contradict `estimate-harness-pipeline`.
> **－** The Case creates no new promise.

```then
update:
  - slug: entity-sprint-migration
    set: {purpose: The repository works by the model of its rule pages — Phase 1 and Phase 2 of docs/migration/migration-plan.md closed}
    sections:
      Purpose: |
        Open since 2026-09-09. The repository works by the model of its rule pages: Phase 1
        (the harness built by its own rules) and Phase 2 (the surviving pages brought into
        conformance) of `docs/migration/migration-plan.md` are closed. Done when every
        Estimate of this page passes: lint clean, the leftovers gone, the branch merged, the
        Rule-class files dissolved, `index.md` gone, the `file` route out of the scripts.
    change: the Purpose off index.md and off a count of Estimates (case 323)
  - slug: estimate-lint-catches
    replace:
      - old: "`## When` is never required on a Decision page;"
        new: "`## When` is never required on a Decision page; `layout`: a page whose `type` does not match its folder, a page whose slug is not its filename, a `.md` at the root of `wiki/` that no live rule page names (case 315);"
    change: the layout class of lint (case 323)
  - slug: estimate-prespec-checks-the-plan
    replace:
      - old: "Governed: an `update` item with `file` on a path a live Rule page governs"
        new: "Governed: an `update` item carrying `file` — the file route is gone (case 320)"
    change: any file item is a finding (case 323)
  - slug: rule-harness
    replace:
      - old: "in this order: the harness files are checked against their pages, the sprint file against its page, then the pages (case 227). Four more belong here and run in no pipeline:"
        new: "in this order: the harness files are checked against their pages, the sprint file against its page, the glossary file against its page, then the pages (cases 227, 306.5). Five more belong here and run in no pipeline:"
    change: the glossary step of make lint and the fifth rule outside the pipeline (case 323)
  - slug: estimate-harness-pipeline
    replace:
      - old: "The Purpose says: three rules belong to no phase of the session"
        new: "The Purpose says: three rules belong to no phase of the session, and five more stand outside the pipeline"
    change: the Purpose it reads names five rules outside the pipeline (case 323)
  - slug: estimate-materialize-marks-superseded
    replace:
      - old: "the `decisions` record of Case N as today."
        new: "the `decisions` record of Case N as today. A marked `create` loses the readings folded into it: each moves to the live `create` of its slug in the unit, or becomes an `estimate` entry of its own (case 309)."
    change: the mark moves a folded reading (case 323)
  - slug: entity-glossary
    replace:
      - old: "one tick per item by the status of the page it names, the current milestone whole and the others one line"
        new: "one tick per item by the statuses of every page its `[[slug]]` before the first ` — ` names, a line without one a note that never ticks, the current milestone whole and the others one line"
      - old: "| Session | Session Start, Plan Mode, Work Mode, End of Session | [[rule-session-start]] |"
        new: "| Session | Five phases in one order under [[rule-session]]: Session Start, Plan Mode, Work Mode, End of Work, Documentation | [[rule-session]] |"
    change: the rows Sprint and Session by cases 313 and 316 (case 323)
```

```tasks
- [x] update `entity-sprint-migration`: `purpose` and `## Purpose` off `index.md`, no count of Estimates
- [x] update `estimate-lint-catches`: the `layout` class
- [x] update `estimate-prespec-checks-the-plan`: the Governed line
- [x] update `rule-harness`: the glossary step, five rules outside the pipeline
- [x] update `estimate-harness-pipeline`: the Purpose it reads
- [x] update `estimate-materialize-marks-superseded`: the readings moved by the mark
- [x] update `entity-glossary`: the rows Sprint and Session
- [x] `uv run guppi glossary`
- [x] `uv run guppi sprint`
- [x] read `estimate-lint-catches`: `uv run pytest tests/test_lint.py`, then `make lint`
- [x] read `estimate-materialize-marks-superseded`: `uv run pytest tests/test_materialize.py -k supersede`
```

## Deferred

## Case 322 — Slice 3b deferred, the nineteenth time

> **context:**
> Slice 3b — `rule-work-mode` and `rule-subagent-guppi` — has stood on the sprint page since case 29 and was deferred eighteen times (183, 206, 218, 231, 242, 248, 252, 254, 260, 263, 269, 276, 281, 285, 289, 293, 303, 307). Both pages exist as `draft` placeholders; `insight-workflow-code-live-before-the-page-it-reads` (`open`, `severity` 2, defer 238) is named by the `rule-work-mode` item and waits with it.

> **problem:**
> This session ratified twelve Cases that leave work in three scripts, lint, the renderer and twelve readings; Slice 3b is not started and would not be finished.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes in spec.md, the test of each Estimate written first and turned green, with the sentence of insight-workflow-code-live-before-the-page-it-reads on a check that reads a page the same Spec changes
  - slug: rule-subagent-guppi
    type: rule
    purpose: What a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case
```
