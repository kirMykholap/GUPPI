<!-- approved 03:39:40 · session 4d991442 -->

# Spec — 2026-09-22, session 0014

## Case 304 — Slice 3f, theme 1: the six schemas as rule pages

> **context:**
> The shape of a page category lives in two files outside the graph: `schema.yaml`, which lint reads, and `schema.md`, the same schema as prose with tables and examples; lint checks that the names of the two agree (`schema-prose`). Both change by hand by an `update` with `file`; neither has a `purpose`, a History or an Estimate. The mechanism of the replacement exists: `render_mode: full` writes the text of a `## Render` section whole into `governs` — `case-schema.md` is born that way from `rule-case-protocol`; `guppi/guard.py` refuses a hand edit of any file a live rule governs; `split_sections` in `guppi/pages.py` keeps everything between the markers inside the section, so yaml in `## Render` does not break the page. Lint reads from the yaml only `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; other keys it ignores — room for the descriptions as data.
> Out of this theme: `index.md` §1 and its Rule-class map stay stale until theme 4; the sentence "A Rule-class file (`index.md`, `glossary.md`, a schema)" of `case-schema.md` until theme 6; `rule_class_path` and `RULE_CLASS` in `materialize.py` and `prespec.py` until theme 5 (the slug `rule-rules-schema` does not match their pattern, no collision). `rule-morph` (Slice 5, defer 239) wants the category set as data — six pages fix it; theme 5 keeps the two compatible. No `applies_to` on a schema rule: a schema applies to a category of pages, not to a page; `applies_to` is the edge Rule → Entity alone, theme 2 (the person's decision of this session).
> Vault: the slugs `rule-page-schemas`, `rule-rules-schema`, `rule-entities-schema`, `rule-estimates-schema`, `rule-lessons-schema`, `rule-insights-schema`, `rule-decisions-schema` and the seven Estimates are free, live and archived; the nearest pages are `rule-render-harness` (built), `rule-governed-files-hook` (built), `rule-lint` (built), `rule-case-protocol` (draft, the one precedent of a vault file rendered from a page). A MOC under a MOC exists three times (`rule-harness` → `rule-settings`, `rule-claude-md`; `rule-session-start` → `rule-skill-hi`); an intermediate MOC earns its place by a cross-cutting Estimate. The tags `harness` and `render` exist; `schema` is new. The Estimates touched: `estimate-lint-catches` (its Criterion names `schema-prose`), one `replace` pair; `estimate-case-protocol-loaded` is not touched — the sentence of the Case schema waits for theme 6. `rule-harness` gets `rule-page-schemas` in `children`, a field alone, no Estimate touched (296). Cases 304.2 and 304.3 of this session were superseded by 305.1 and 305.2 before the approval and left the Spec (299.1).

> **problem:**
> How the six schemas enter the graph: one rule page per category whose Render is `schema.yaml`; where the prose of `schema.md` goes; what the parent of the six is, so that six Leaves are no orphans; what each Leaf promises and what the MOC promises, so that one promise is not signed six times; and what lint does once `schema.md` is gone.

> **given:**
> `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
> **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
> **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.

### Case 304.1 — `rule-page-schemas` under `rule-harness`, and its Estimate

> **given:**
> `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
> **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
> **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.

> **when:**
> `guppi render` writes the files, then `guppi lint` reads the vault.

> **then:**
> The six `vault/wiki/<category>/schema.yaml` are written, each from the one Leaf that governs it; `render --check` after it exits 0; there is no seventh file and no `schema.md` in any category.
> **＋** Lint reads each file and gives no `path` and no `schema-description` finding on `<category>/schema`.
> **＋** A hand edit of any of the six is refused by the hook.
> **－** A second `full` page on one of the files fails the render with the two slugs.

```then
create:
  - slug: rule-page-schemas
    type: rule
    kind: MOC
    purpose: Prevents the shape of a page category from living in a file nobody ratified — each schema is a rule page and its yaml the Render
    parent: rule-harness
    children: [rule-entities-schema, rule-rules-schema, rule-estimates-schema, rule-lessons-schema, rule-insights-schema, rule-decisions-schema]
    estimates: [estimate-page-schemas-one-file-per-rule]
    tags: [harness, render, schema]
    sections:
      Purpose: |
        Prevents the shape of a page category from living in a file nobody ratified. Until case 304 the six `schema.yaml` and their `schema.md` stood outside the graph — no `purpose`, no History, no Estimate, changed by hand by an `update` with `file`. Each child renders one `vault/wiki/<category>/schema.yaml`: the lists lint reads, the prose of the former `schema.md` as data under `description`, `fields`, `sections` and `examples`. Lint reads the file, the governed-files hook refuses a hand edit of it. The schemas are read in every phase — the agent's `then` block in Plan Mode, `materialize` and `generate` in Documentation, lint with the renderer — so the MOC sits under `rule-harness`, as `rule-lint` does. The order of the children is the order of `CATEGORIES` in `materialize.py`. No `applies_to` on a schema rule: a schema applies to a category of pages, not to a page (case 304).
  - slug: estimate-page-schemas-one-file-per-rule
    type: estimate
    ref: rule-page-schemas
    kind: QA
    purpose: Each vault/wiki/<category>/schema.yaml is written by guppi render from exactly one rule page, no schema.md remains, lint reads every file and a hand edit is refused
    method: make lint — render --check exit 0 and no path or schema-description finding on a <category>/schema; tests/test_render.py for two full pages on one file; the live reading by hand after the librarian's first render
    tags: [harness, render, schema]
update:
  - slug: rule-harness
    set: {children: [rule-render-harness, rule-settings, rule-lint, rule-page-schemas, rule-governed-files-hook, rule-claude-md, rule-bash-guard, rule-tests-clock-pinned]}
    change: rule-page-schemas, the MOC of the six category schemas, after rule-lint (case 304.1)
new_tags:
  - tag: schema
    meaning: the shape of a page category — its fields, their values and its sections
    aliases: схема, схема страницы
```

```tasks
- [x] create `rule-page-schemas` (parent `rule-harness`, six children)
- [x] create `estimate-page-schemas-one-file-per-rule` (ref `rule-page-schemas`)
- [x] update `rule-harness`: `children` with `rule-page-schemas` after `rule-lint`
- [ ] read `estimate-page-schemas-one-file-per-rule`: by hand after the librarian's first render — `make lint`, no `path` or `schema-description` finding on a `<category>/schema`, `render --check` exit 0
```

### Case 304.4 — `rule-estimates-schema` and `estimate-estimates-schema-checked`

> **given:**
> `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
> **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
> **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
> **＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/estimates/schema.yaml`: a page in the shape, then one defect at a time.

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`; `guppi lint` reads a page of `wiki/estimates/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, status, target, origin, sprint, created, tags`; optional `purpose, method, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Context`, `## Method`, `## Result` optional, `## Result` required on `passed` and on `failed`.
> **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, the Result and Criterion paragraph, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the two example pages.
> **－** `vault/wiki/estimates/schema.md` does not exist.

```then
create:
  - slug: rule-estimates-schema
    type: rule
    kind: Leaf
    purpose: Prevents an Estimate page from carrying a field or section outside the shape lint checks, or lacking one it needs
    enforcement: render
    governs: vault/wiki/estimates/schema.yaml
    render_mode: full
    parent: rule-page-schemas
    estimates: [estimate-estimates-schema-checked]
    tags: [harness, render, schema]
    sections:
      Purpose: |
        Prevents an Estimate page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/estimates/schema.yaml`, the file `guppi lint` reads for every page of `wiki/estimates/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8).
      Render: |
        <!-- rule-estimates-schema -->
        type: estimate
        description: |
          Three blocks: properties, body, history. One schema for both kinds; sections that do not apply are omitted rather than left empty.

          An Estimate is the evidence. On a Rule it is a test that the guard works; on an Entity it is a reading of the whole, which no single case can break. Which of the two it is, the prefix of `target` says; the agent does not choose (case 240.3).

          An Estimate is one promise, one way to check it and the last result with its date (case 182). It is always a Leaf — never inline on another page, never a MOC. Grouping is what the parent Entity's recursion already does. One action (`when`) — one Estimate; the ＋/－ lines stay in its `then` while one run checks them; a line with a test or a reading of its own is split off, and the axis of the split is the promise, not the method.

          `purpose`, `method` and `checked` are the fields of the model of case 182: one line each, written on a page born since case 193; the older pages carry none until their recut at their first touch — the update that sets `method` (case 211) — counted by lint as `unmigrated` (case 202), so none is required yet (case 193). `target` names an Entity or a Rule; lint reports any other category (case 53.1).

          A `failed` Estimate is debt, not an endpoint: its target stays `draft` and the librarian surfaces it in `brief.md` until a human decides. Absent a decision to fix, the default is archival — something that cannot pass its own criterion should not sit in the vault pretending to be work in progress.

          Fields deliberately absent. `verified_at` — `checked` takes its place (case 182, point 5): the date of the last reading, so lint can one day catch a stale check. `blocking` — not yet. The distinction between a QA failure (blocks the build) and a Research non-result (may be a fine outcome) is currently carried by `kind` plus human judgment at the brief. `severity` — Estimates do not accumulate the way Insights do. `retry_count` — a check that keeps failing is a Lesson, not a counter.

          The two kinds sit at opposite ends of the same schema: QA puts its weight on `Criterion` and treats `Result` as a formality, Research often has a loose `Criterion` and carries everything in `Result`. That is why unused sections are omitted rather than filled with placeholder text.

          `Result` is overwritten, not appended. It is about one run of one check: a test that passed, broke and was fixed leaves one current result; the sequence of changes is what History is for. Same for Research: the page states what we currently believe, and History records that the belief changed. `Criterion` is replaced, not appended: a rule changes → the Estimate the Case names goes `pending` → the test or the reading → `passed`.
        properties:
          required: [type, kind, status, target, origin, sprint, created, tags]
          optional: [purpose, method, checked]
          values:
            kind: [QA, Research]
            status: [pending, passed, failed]
        body:
          required: ["## Criterion", "## History"]
          optional: ["## Context", "## Method", "## Result"]
          conditional:
            - when: {status: passed}
              required: ["## Result"]
            - when: {status: failed}
              required: ["## Result"]
        fields:
          type: |
            required; `estimate`. Page category.
          kind: |
            required; `QA` | `Research`. QA: the expected result is known in advance and checked against a stated criterion. Research: the result is not known, and finding it produces new content — on an Entity only, since a Rule has its criterion by definition; `failed` on a Research Estimate means the finding does not serve the purpose the Estimate was made for — no answer, or the answer "not this way" — which of the two, the person says in the estimate line; both are debt, a Case on a changed approach or archival; when a bar grows out of the finding, it becomes a QA Estimate or a Rule (case 240.3); its `then` is a question, its Result the finding. Reading a known criterion by eye is QA by hand, not Research.
          status: |
            required; `pending` | `passed` | `failed`. Short state, from a fixed list. The narrative belongs in the body.
          target: |
            required; quoted wikilink `"[[slug]]"` of an Entity or Rule. The page with a contract this verifies; the scripts read the slug through the brackets (case 148.2); a Lesson or an Insight has no Estimate (case 53.1). Written by the script from the ledger. Without it the cascade — an Entity is `built` only once all its Estimates pass — cannot be computed.
          purpose: |
            optional; one line. The promise, for the list on the target page: the reader of a rule sees its Estimates by `purpose` and opens only the touched ones. Written from the Case on every page born since case 193; absent on the older pages until their recut, counted by lint as `unmigrated` (case 202).
          method: |
            optional; one line. How the promise is checked: the test command (`make test-x`, `pytest tests/test_x.py`); or where and when it is read by hand — a live reading of a session start, the brief of a librarian's run; or, for Research, what is measured. Written from the Case since case 193.
          checked: |
            optional; date. The date of the last reading: the date the Result opens with, else the date of the reading's unit; written by `generate` on every reading (case 201.1).
          origin: |
            required; `raw/YYYY-MM-DD/HHMM/ledger.md#case-N` — the date form, `raw/YYYY-MM-DD/ledger.md#case-N`, on pages born before 2026-09-13 (case 103.6). The ratified decision that created it.
          sprint: |
            required; the sprint id.
          created: |
            required; date.
          tags: |
            required; list. Chosen at the vault query before the Case, ratified in the Case.
        sections:
          "## Criterion": |
            required. The promise, written once: the `given`, `when` and `then` of one Case, verbatim with their operands, as `Given:`, `When:`, `Then:`. The Case that creates the Estimate writes it; an `update` that changes the promise replaces it whole and sets the page `pending`; an `update` that names a part alone — a field, a `replace` pair — keeps it, and a pair inside it sets `pending` (case 296); nothing is appended and no `### case N` block exists (case 193; the blocks of the shape before it stand on the older pages until their recut, counted by lint as `unmigrated`, case 202). The Criterion that was replaced stays in the Spec of the session that wrote it, reached by `origin`, and in History. For Research the `then` may legitimately be broad ("determine whether we stay inside the latency budget"); for QA it should be exact.
          "## Result": |
            optional; required on `passed` and `failed`. Omitted while `pending`. Its first line is the date of the reading and the command — `make test-x`, `pytest tests/test_x.py` — or the place of a live reading; the result follows (case 199). For QA usually one line more. For Research this is the substance of the page — findings, numbers, the conclusion drawn.
          "## Context": |
            optional. The shape before case 193: the `problem` of the Case that made the Estimate, written once. Not written to a new page — the Case is reached by `origin`; dropped by the `update` that sets `method` (case 211).
          "## Method": |
            optional. The shape before case 193: the `method` of the Case as a section. On a new page `method` is a field; the `update` that sets `method` drops the section, and a recut — `sections: Criterion` on a page without the field — is refused by `generate` unless `set` carries `method` (case 211).
          "## History": |
            required. Appended by hook, never by an agent. Always the last section: `- <date> created · <origin>`, `- <date> status: pending → passed`.
        examples:
          "QA": |
            ---
            type: estimate
            kind: QA
            status: passed
            target: entity-discount-new-client
            purpose: A client with no completed order gets a 0% discount
            method: pytest tests/discounts/test_new_client.py
            checked: 2026-09-08
            origin: raw/2026-09-08/0900/ledger.md#case-2
            sprint: 2026-Q3-s4
            created: 2026-09-08
            tags: [discounts, pricing]
            ---

            ## Criterion

            Given:
            The discount pipeline runs every rule in order and takes the first that applies.

            When:
            A client with zero completed orders asks for a discount.

            Then:
            The discount is 0%.
            **－** A client with one completed order is not a new client.

            ## Result

            2026-09-08, `pytest tests/discounts/test_new_client.py`: 3 passed.

            ## History
            - 2026-09-08 created · raw/2026-09-08/0900/ledger.md#case-2
            - 2026-09-08 status: pending → passed
          "Research": |
            ---
            type: estimate
            kind: Research
            status: passed
            target: entity-cart
            purpose: Whether the cart renders within 200ms, and what dominates the time if not
            method: measure the render at 10, 50 and 200 line items, against a seeded database
            checked: 2026-09-11
            origin: raw/2026-09-08/0900/ledger.md#case-1
            sprint: 2026-Q3-s4
            created: 2026-09-08
            tags: [cart, performance]
            ---

            ## Criterion

            Given:
            A seeded database with carts of 10, 50 and 200 line items.

            When:
            A buyer opens the cart.

            Then:
            Determine whether the cart renders within 200ms, and what dominates the time if not.

            ## Result

            2026-09-11, the measurement of the method against the seeded database: renders in 140ms at
            50 items. At 200 items it reaches 380ms, dominated by per-item price recalculation rather
            than by rendering. The 200ms target holds for realistic cart sizes; above roughly 120 items
            it does not.

            ## History
            - 2026-09-08 created · raw/2026-09-08/0900/ledger.md#case-1
            - 2026-09-11 status: pending → passed
        <!-- /rule-estimates-schema -->
  - slug: estimate-estimates-schema-checked
    type: estimate
    ref: rule-estimates-schema
    kind: QA
    purpose: An Estimate page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
    method: pytest tests/test_schemas.py -k estimates on the live vault/wiki/estimates/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/estimates/
    tags: [harness, render, schema]
```

```tasks
- [x] create `rule-estimates-schema` (parent `rule-page-schemas`), the Render above
- [x] create `estimate-estimates-schema-checked` (ref `rule-estimates-schema`)
- [x] `git rm vault/wiki/estimates/schema.md`
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] read `estimate-estimates-schema-checked`: `uv run pytest tests/test_schemas.py -k estimates`, then `make lint` in the librarian's run
```

### Case 304.5 — `rule-lessons-schema` and `estimate-lessons-schema-checked`

> **given:**
> `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
> **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
> **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
> **＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/lessons/schema.yaml`: a page in the shape, then one defect at a time.

> **when:**
> `guppi render` writes `vault/wiki/lessons/schema.yaml` from `rule-lessons-schema`; `guppi lint` reads a page of `wiki/lessons/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, root_cause, status, origin, sprint, created, tags`; optional `source, insight`; values `kind: error | knowledge`, `status: new | clustered | archived`; conditional — `knowledge` requires `source`, `clustered` requires `insight`; the sections `## Trigger`, `## Root cause` and `## History` required.
> **＋** A Lesson page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the Slug, no Estimate, no `reviewed` status, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the two example pages.
> **－** `vault/wiki/lessons/schema.md` does not exist.

```then
create:
  - slug: rule-lessons-schema
    type: rule
    kind: Leaf
    purpose: Prevents a Lesson page from carrying a field or section outside the shape lint checks, or lacking one it needs
    enforcement: render
    governs: vault/wiki/lessons/schema.yaml
    render_mode: full
    parent: rule-page-schemas
    estimates: [estimate-lessons-schema-checked]
    tags: [harness, render, schema]
    sections:
      Purpose: |
        Prevents a Lesson page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/lessons/schema.yaml`, the file `guppi lint` reads for every page of `wiki/lessons/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8).
      Render: |
        <!-- rule-lessons-schema -->
        type: lesson
        description: |
          Three blocks: properties, body, history. Always flat — grouping is what Insight is for.

          A Lesson is a recorded fact, not a ratified decision. It does not go through a Case and requires no ratification; the ledger hook writes it directly.

          Slug. Area + cause: `lesson-hooks-sessionstart-cannot-block`, `lesson-pricing-async-in-sync-tx`. The area groups related lessons together in a plain file listing, and the cause makes near-duplicates visible before anyone opens the index. Naming by symptom was rejected: two unrelated failures often share one symptom, and the symptom is not what clustering compares.

          There is no Estimate. A lesson is a recorded fact: the trigger is the observation, and nothing about it is checked again. An Estimate exists only for a page with a contract — an Entity or a Rule. A `knowledge` claim is checked where it is leaned on: by the Estimate of the Rule built on it (case 53.1).

          There is no `reviewed` status. An intermediate "the librarian looked at it" state records nothing useful — a lesson with no pair is simply still `new`, and will be reconsidered next session anyway. Only membership in an Insight is a real change of state.

          No `## Insight` section: the `insight` field is the link (case 166.1).
        properties:
          required: [type, kind, root_cause, status, origin, sprint, created, tags]
          optional: [source, insight]
          values:
            kind: [error, knowledge]
            status: [new, clustered, archived]
          conditional:
            - when: {kind: knowledge}
              required: [source]
            - when: {status: clustered}
              required: [insight]
        body:
          required: ["## Trigger", "## Root cause", "## History"]
        fields:
          type: |
            required; `lesson`. Page category.
          kind: |
            required; `error` | `knowledge`. `error`: something went wrong. `knowledge`: external material studied once so the source never has to be supplied again.
          root_cause: |
            required; one line. Why it happened (`error`), or the mechanism the source claims (`knowledge`). Lives in properties because the index line of the category is built from it, and clustering into an Insight compares exactly this.
          status: |
            required; `new` | `clustered` | `archived`. `clustered` once it belongs to an Insight. Archived when its Insight is `actioned`.
          source: |
            required on `knowledge`; url or reference. Where the material came from.
          insight: |
            required on `clustered`; quoted wikilink `"[[slug]]"`. The Insight this belongs to, once clustered. Written by the script. The scripts read the slug through the brackets; a slug without a category prefix stays bare (case 148.2). The field is the link; no body section repeats it (case 166.1).
          origin: |
            required; `raw/YYYY-MM-DD/HHMM/ledger.md#L<n>` — the date form, `raw/YYYY-MM-DD/ledger.md#L<n>`, on pages born before 2026-09-13 (case 103.6). The ledger line. Unlike Entity and Rule, this points at a `lesson[...]` line rather than a `decision[...]` one.
          sprint: |
            required; the sprint id.
          created: |
            required; date.
          tags: |
            required; list. Includes what the material applies to, for `knowledge`.
        sections:
          "## Trigger": |
            required. What happened (`error`), or what was read (`knowledge`). The full account — the one-line version is `root_cause` in properties.
          "## Root cause": |
            required. Expands the property: why this happened, or what the source actually claims and on what grounds.
          "## History": |
            required. Appended by hook, never by an agent. Always the last section.
        examples:
          "error": |
            ---
            type: lesson
            kind: error
            root_cause: SessionStart cannot block, so nothing gated the first ledger write
            status: clustered
            insight: insight-hook-gating-assumptions
            origin: raw/2026-09-08/ledger.md#L14
            sprint: 2026-Q3-s4
            created: 2026-09-08
            tags: [hooks, ledger, session]
            ---

            ## Trigger
            The first ratified decision of the session was written to `main` instead of the session
            branch. Noticed only at handoff, when the librarian found a ledger line outside the
            session folder.

            ## Root cause
            SessionStart cannot block — exit code 2 is a no-op there. The guard had been placed on
            SessionStart on the assumption that it behaved like PreToolUse. Nothing actually gated
            the write.

            ## History
            - 2026-09-08 created · raw/2026-09-08/ledger.md#L14
            - 2026-09-15 status: new → clustered
          "knowledge": |
            ---
            type: lesson
            kind: knowledge
            root_cause: Per-finding fix subagents each rebuild context and rerun the suite
            status: new
            source: https://github.com/obra/superpowers
            origin: raw/2026-09-12/ledger.md#L07
            sprint: 2026-Q3-s4
            created: 2026-09-12
            tags: [subagents, review, cost]
            ---

            ## Trigger
            Read the subagent-driven-development skill while deciding how to structure our own
            review step.

            ## Root cause
            It dispatches a single fix subagent with the complete findings list rather than one per
            finding. The stated reason is that per-finding fixers each rebuild context and rerun the
            test suite, and in a real session that wave cost more than all the implementation tasks
            combined.

            ## History
            - 2026-09-12 created · raw/2026-09-12/ledger.md#L07
        <!-- /rule-lessons-schema -->
  - slug: estimate-lessons-schema-checked
    type: estimate
    ref: rule-lessons-schema
    kind: QA
    purpose: A Lesson page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
    method: pytest tests/test_schemas.py -k lessons on the live vault/wiki/lessons/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/lessons/
    tags: [harness, render, schema]
```

```tasks
- [x] create `rule-lessons-schema` (parent `rule-page-schemas`), the Render above
- [x] create `estimate-lessons-schema-checked` (ref `rule-lessons-schema`)
- [x] `git rm vault/wiki/lessons/schema.md`
- [x] `uv run guppi render`: `vault/wiki/lessons/schema.yaml`
- [x] read `estimate-lessons-schema-checked`: `uv run pytest tests/test_schemas.py -k lessons`, then `make lint` in the librarian's run
```

### Case 304.6 — `rule-insights-schema` and `estimate-insights-schema-checked`

> **given:**
> `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
> **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
> **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
> **＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/insights/schema.yaml`: a page in the shape, then one defect at a time.

> **when:**
> `guppi render` writes `vault/wiki/insights/schema.yaml` from `rule-insights-schema`; `guppi lint` reads a page of `wiki/insights/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, pattern, status, children, severity, origin, sprint, created, tags`; optional `addressed_by, deferred_by`; values `status: open | actioned | archived`; conditional — `actioned` requires `addressed_by`; `computed: [severity]`; the sections `## Pattern` and `## History` required, `## Proposal` optional.
> **＋** An Insight page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the Threshold, Reopening, the Slug, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the example page.
> **－** `vault/wiki/insights/schema.md` does not exist.

```then
create:
  - slug: rule-insights-schema
    type: rule
    kind: Leaf
    purpose: Prevents an Insight page from carrying a field or section outside the shape lint checks, or lacking one it needs
    enforcement: render
    governs: vault/wiki/insights/schema.yaml
    render_mode: full
    parent: rule-page-schemas
    estimates: [estimate-insights-schema-checked]
    tags: [harness, render, schema]
    sections:
      Purpose: |
        Prevents an Insight page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/insights/schema.yaml`, the file `guppi lint` reads for every page of `wiki/insights/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8).
      Render: |
        <!-- rule-insights-schema -->
        type: insight
        description: |
          Three blocks: properties, body, history. Always a MOC — a single unclustered lesson is just a Lesson.

          Insight is its own type, not a kind of Lesson. It shares no fields with one: no `trigger`, no `root_cause`, no `source`, no Estimate. It has `children`, `severity` and `addressed_by`, which a Lesson does not. Two schemas under one name would have meant a page where most fields are inapplicable whichever kind it is.

          Created by the librarian, never by a decision; an `update` actions or rejects it, a `defer` postpones it (case 124). It reaches the human through the Deferred list of `brief.md` and becomes an ordinary ratified Case there.

          Threshold. An Insight is created on the second Lesson sharing a root cause. One occurrence is an incident; two is a pattern. The archive is not searched. A Lesson is archived only when its Insight was actioned — its `clustered` children are archived by the cascade of `generate` (case 104.2) — and that Insight stays live with its `pattern` in its index line; a recurrence after the pattern was supposedly fixed is caught there, at the cost of one index line, and reopens the Insight.

          Reopening. `actioned` is not an end state. When a new Lesson matches the root cause of an `actioned` Insight, the Insight returns to `open` and the new Lesson becomes a child. Previously archived children stay archived, so `severity` counts only the current run. No separate recurrence counter — the fact is legible from History plus the retained `addressed_by`. One exception: a Lesson whose entry carries `addressed_by` — a decision line of its own session marked it with `{addresses:<its slug>}`, the Case that closed its cause. Then the Insight stays `actioned`, `addressed_by` moves to that decision, the Lesson becomes a child and is archived with the other children by the cascade (case 284.4).

          Slug. Area + pattern, as for Lessons: `insight-hooks-lifecycle-assumptions`.

          No `## Children` or `## Addressed by` section: the fields are the links (case 166.1). `severity` is `count(children where status != archived)`, recomputed by the cascade of `generate`.
        properties:
          required: [type, pattern, status, children, severity, origin, sprint, created, tags]
          optional: [addressed_by, deferred_by]
          values:
            status: [open, actioned, archived]
          conditional:
            - when: {status: actioned}
              required: [addressed_by]
        computed: [severity]
        body:
          required: ["## Pattern", "## History"]
          optional: ["## Proposal"]
        fields:
          type: |
            required; `insight`. Page category.
          pattern: |
            required; one line. The shared root cause, stated once. The index line of the category is built from it.
          status: |
            required; `open` | `actioned` | `archived`. `actioned` when a ratified decision has addressed it. Not terminal — a new Lesson with the same root cause reopens it, unless its entry carries `addressed_by`: a decision of its own session closed its cause, and the Insight stays `actioned` (case 284.4); an Insight made from a lesson whose entry carries `addressed_by` is set `actioned` right after its `create`, by the librarian's `update` (case 302.2). `archived` when the cascade of `generate` finds an `open` Insight with no live child (case 104.3); an `actioned` Insight is never archived by the cascade, it is kept for the recurrence.
          children: |
            required; list of quoted wikilinks `"[[slug]]"`. The Lessons clustered here. Unordered. The scripts read the slug through the brackets; a slug without a category prefix stays bare (case 148.2). The field is the link; no body section repeats it (case 166.1).
          severity: |
            required; integer. `count(children where status != archived)`. Recomputed by the cascade of `generate` (case 104.3), a child read in `wiki/lessons/` or in the archive (case 110), never written by hand (case 110.1).
          addressed_by: |
            required on `actioned`; decision quoted wikilink `"[[slug]]"`. The ratified decision that fixed the pattern, or rejected it (case 124). The field is the link; no body section repeats it (case 166.1).
          deferred_by: |
            optional; list of decision quoted wikilinks `"[[slug]]"`. The `defer` decisions that postponed it; set by `generate`, cleared by a `supersedes` (case 124.2).
          origin: |
            required; date + session. When the librarian first clustered it. Unlike every other category this does not point at a ledger line — no decision created it.
          sprint: |
            required; the sprint id.
          created: |
            required; date.
          tags: |
            required; list.
        sections:
          "## Pattern": |
            required. Expands the property: what the clustered lessons have in common, stated as a mechanism rather than a list of symptoms.
          "## Proposal": |
            optional. What the librarian suggests doing about it. A suggestion, not a decision — it is ratified, rejected or reshaped in a later Case.
          "## History": |
            required. Appended by hook, never by an agent. Always the last section. Reopening is visible here.
        examples:
          "actioned": |
            ---
            type: insight
            pattern: Hooks were assumed to gate execution without checking which events can block
            status: actioned
            children: [lesson-hooks-sessionstart-cannot-block, lesson-hooks-subagentstart-no-gate]
            severity: 2
            addressed_by: decision-hook-capability-table
            origin: 2026-09-15 · session-2026-09-15
            sprint: 2026-Q3-s4
            created: 2026-09-15
            tags: [hooks, session]
            ---

            ## Pattern
            Both failures came from placing a guard on an event that cannot block. The events were
            chosen by when they fire, without checking whether a non-zero exit there actually stops
            anything. The shape recurs because the two properties are independent and only one is
            obvious from the event name.

            ## Proposal
            A capability table in the session-start rule: for each hook event, whether exit 2 blocks.
            Consult it before placing any guard.

            ## History
            - 2026-09-15 created · clustered from 2 lessons
            - 2026-09-19 status: open → actioned · decision-hook-capability-table
        <!-- /rule-insights-schema -->
  - slug: estimate-insights-schema-checked
    type: estimate
    ref: rule-insights-schema
    kind: QA
    purpose: An Insight page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
    method: pytest tests/test_schemas.py -k insights on the live vault/wiki/insights/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/insights/
    tags: [harness, render, schema]
```

```tasks
- [x] create `rule-insights-schema` (parent `rule-page-schemas`), the Render above
- [x] create `estimate-insights-schema-checked` (ref `rule-insights-schema`)
- [x] `git rm vault/wiki/insights/schema.md`
- [x] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
- [x] read `estimate-insights-schema-checked`: `uv run pytest tests/test_schemas.py -k insights`, then `make lint` in the librarian's run
```

### Case 304.7 — `rule-decisions-schema` and `estimate-decisions-schema-checked`

> **given:**
> `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
> **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
> **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
> **＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/decisions/schema.yaml`: a page in the shape, then one defect at a time.

> **when:**
> `guppi render` writes `vault/wiki/decisions/schema.yaml` from `rule-decisions-schema`; `guppi lint` reads a page of `wiki/decisions/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, case, status, origin, sprint, created, tags`; optional `create, update, delete, defer, source, supersedes, superseded_by`; values `status: current | superseded | archived`; the sections `## Context`, `## Problem` and `## History` required, `## Given`, `## When`, `## Criterion`, `## Deferred`, `## Note` optional.
> **＋** A Decision page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list or lacking a required section has one finding per defect.
> **＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the Slug, the fields deliberately absent, the body paragraph, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the example page.
> **－** `vault/wiki/decisions/schema.md` does not exist.

```then
create:
  - slug: rule-decisions-schema
    type: rule
    kind: Leaf
    purpose: Prevents a Decision page from carrying a field or section outside the shape lint checks, or lacking one it needs
    enforcement: render
    governs: vault/wiki/decisions/schema.yaml
    render_mode: full
    parent: rule-page-schemas
    estimates: [estimate-decisions-schema-checked]
    tags: [harness, render, schema]
    sections:
      Purpose: |
        Prevents a Decision page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/decisions/schema.yaml`, the file `guppi lint` reads for every page of `wiki/decisions/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8).
      Render: |
        <!-- rule-decisions-schema -->
        type: decision
        description: |
          Every page has three blocks: properties (frontmatter), body (per-category sections), history (appended by hook). This is the schema for Decision. One page per Case, however many ledger lines the Case produced.

          Slug. `decision-case-<N>`: `decision-case-18.1`. Mechanical, because the script writes the page and may not name anything; unique, because a Case id is. Nothing searches Decision pages, so the slug needs no meaning beyond the Case it points back at. A Decision is reached by reference only: from a target page's `deferred_by` (a deferred decision, case 52.3), from the `[[decision-case-N]]` wikilink of a History line (case 52.4), or by the case id a `supersedes` carries.

          Fields deliberately absent. `ratification` — a Decision page cannot exist without it. The Case does not close, no ledger line is written, no page is generated. A field with one possible value carries no information; the fact is recorded by the page existing and by `origin`. `recommend` — if the human accepted the proposal it became `Then`; if they changed it, `Then` holds the change. Either way the original is conversation history, recoverable from the archived ledger. `last_updated` — a decision is not edited. Only `status` and `superseded_by` ever change, and both are dated in History. `authority` — dropped. It overlapped with tags on one reading and with `ref` on the other. If a real need appears later, it comes back as a ratified decision.

          The body is the Case that produced it, minus what belongs to the conversation rather than the decision. `create`, `update`, `delete`, `defer`: one list per kind present among the Case's ledger lines, in that order, each the slugs of those lines in ledger order (a page, or a Rule-class file such as `case-schema`); a kind with no line is absent, at least one is present. The category is derived from the slug prefix or the Rule-class map, never written. Lint checks every page slug names a live or archived page, and that neither `kind` nor `target_slug` is present (case 59.4).
        properties:
          required: [type, case, status, origin, sprint, created, tags]
          optional: [create, update, delete, defer, source, supersedes, superseded_by]
          values:
            status: [current, superseded, archived]
        body:
          required: ["## Context", "## Problem", "## History"]
          optional: ["## Given", "## When", "## Criterion", "## Deferred", "## Note"]
        fields:
          type: |
            required; `decision`. Page category. Fixed for this schema.
          case: |
            required; case id, e.g. `18.1`. The Case this page records.
          status: |
            required; `current` | `superseded` | `archived`. Lifecycle of this page, not of the work. `superseded` once a later Case names it in `supersedes`, and `archived` the moment the cascade of `generate` meets it so: a superseded Decision no longer describes the present (case 104.1).
          create: |
            one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `create` lines, in ledger order: a page, or a Rule-class file by its ledger slug (`case-schema`, `rules-schema-yaml`). One list per kind present, in the order create, update, delete, defer; a kind with no line is absent. Lists of quoted wikilinks for page slugs, a Rule-class slug bare, so Obsidian shows them as links (case 148.2); the kind of every target is its key (case 59.4, replacing the aligned `kind` and `target_slug` of case 52.1). The category is derived from the slug prefix or the Rule-class map and never written; the parent of a `create` is on the child page as `parent` or `target`.
          update: |
            one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `update` lines, in ledger order; a later `rename` retargets the link like any link (case 258.1).
          delete: |
            one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `delete` lines, in ledger order.
          defer: |
            one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `defer` lines, in ledger order; each target carries this page in `deferred_by`.
          source: |
            optional; list. External ids the Case's lines carried (`{source:...}`), traceability only.
          supersedes: |
            optional; list of decision quoted wikilinks `"[[slug]]"`. Earlier Cases this one overrides, from the ledger's `{supersedes:case N}`.
          superseded_by: |
            optional; list of decision quoted wikilinks `"[[slug]]"`. Back-references, written by the script.
          origin: |
            required; `raw/YYYY-MM-DD/HHMM/ledger.md#case-N` — the date form, `raw/YYYY-MM-DD/ledger.md#case-N`, on pages born before 2026-09-13 (case 103.6). Where this was ratified. The folder also holds the Spec with the Case. The `raw/` of a session is archived with it once every line of it became a page, and the pointer is not rewritten (cases 100.1, 103.6).
          sprint: |
            required; the sprint id. Cheap slice of "what did we decide this sprint" without parsing dates.
          created: |
            required; date.
          tags: |
            required; list. The union of the targets' tags, as ratified in the Case.
        sections:
          "## Context": |
            required. What this is about.
          "## Problem": |
            required. What required a decision. On a defer, what is unresolved.
          "## Given": |
            optional. Only on pages written before case 201.2, which keep it: the Case's `given`. A page written after carries none — the contract lives on the Estimate (case 201.2).
          "## When": |
            optional. Only on pages written before case 72, which keep it: the Case's `when`. A page written after case 72 has no `## When` (case 72.2).
          "## Criterion": |
            optional. Only on pages written before case 201.2, which keep it: one `- [[estimate-x]] § case N` line per block the Case wrote under the shape before case 193. A page written after carries none: the Estimate named in the Case holds the Criterion whole (case 201.2).
          "## Deferred": |
            when the Case has a `defer` line with a `purpose`. The body of the deferred decision: one `### [[slug]]` heading per target of the Case's `defer` lines, in that order, each followed by that target's `purpose` verbatim, however long — written for a defer with a `ref` and for a placeholder alike, so the postponed work is never dropped; a `supersedes` does not edit it, the page is archived whole (case 186.1).
          "## Note": |
            optional. Only when ratification was non-trivial: a reservation, a condition, a rejected alternative worth remembering. Omit when the answer was simply yes.
          "## History": |
            required. Appended by hook, never by an agent. Always the last section, so `tail` reads it without loading the page: `- <date> created · <origin>`, `- <date> superseded by decision-case-N`.
        examples:
          "a create": |
            ---
            type: decision
            case: "1"
            status: current
            create: [entity-cart]
            origin: raw/2026-09-08/ledger.md#case-1
            sprint: 2026-Q3-s4
            created: 2026-09-08
            tags: [cart, checkout]
            ---

            ## Context
            The site has checkout but no cart — items go straight from the catalogue to payment.

            ## Problem
            Buyers cannot review an order before paying.

            ## Given
            The vault query before the Case found no cart page and no overlapping purpose. `entity-checkout` exists and will
            be affected. Nothing in `draft` covers this either.

            ## Criterion
            - estimate-cart § case 1

            ## History
            - 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
        <!-- /rule-decisions-schema -->
  - slug: estimate-decisions-schema-checked
    type: estimate
    ref: rule-decisions-schema
    kind: QA
    purpose: A Decision page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
    method: pytest tests/test_schemas.py -k decisions on the live vault/wiki/decisions/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/decisions/ but the pages of Cases 1–28 without Context and Problem (Slice 5)
    tags: [harness, render, schema]
```

```tasks
- [x] create `rule-decisions-schema` (parent `rule-page-schemas`), the Render above
- [x] create `estimate-decisions-schema-checked` (ref `rule-decisions-schema`)
- [x] `git rm vault/wiki/decisions/schema.md`
- [x] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [x] read `estimate-decisions-schema-checked`: `uv run pytest tests/test_schemas.py -k decisions`, then `make lint` in the librarian's run
```

### Case 304.8 — lint: `schema-description` for `schema-prose`

> **given:**
> `guppi lint` reads the `schema.yaml` of a category; `check_prose` compares the names of the tables of `schema.md` with the lists of the yaml (`schema-prose`); `tests/test_lint.py` fixes the classes, one test each.
> **＋** `estimate-lint-catches` names `schema-prose` in one line of its Criterion.

> **when:**
> `uv run guppi lint` reads `vault/wiki/<category>/schema.yaml`.

> **then:**
> Every name of `properties.required`, `properties.optional` and the `required` of a conditional has a key under `fields`; every key of `fields` is one of those names; the same for `body` and `sections`; otherwise one line `<category>/schema: schema-description: field <name> has no description` or `fields describes <name>, which no list names`, and the same for a section.
> **＋** `schema.md` is not read; `prose_names` and `check_prose` leave; the class `schema-prose` leaves the docstring, `schema-description` takes its place.
> **－** The other classes do not change; `render --check` and the Makefile do not change.

```then
update:
  - slug: estimate-lint-catches
    replace:
      - old: "`schema-prose`: `schema.md` and `schema.yaml` naming different fields or sections"
        new: "`schema-description`: a field or section the lists of `schema.yaml` name without a description under `fields` or `sections`, or a description of a name no list carries (case 304.8)"
    change: schema-description for schema-prose — the descriptions live in the yaml, schema.md is gone (case 304.8)
```

```tasks
- [x] update `estimate-lint-catches`: one `replace` pair inside the Criterion, `pending` by 296
- [x] `guppi/lint.py`: `check_descriptions` for `check_prose`, `prose_names` removed, the docstring — `schema-description` for `schema-prose`
- [x] `tests/test_lint.py`: the fixtures without `schema.md`, `fields` and `sections` in the yaml fixtures, one test per direction of the finding; `tests/test_generate.py`: the fixture without `schema.md`
- [x] read `estimate-lint-catches`: `uv run pytest tests/test_lint.py`, then `make lint` in the librarian's run
```

## Case 305 — Slice 3f, theme 2: the audit of the parents and the edge Rule → Entity

> **context:**
> The audit over the 47 pages of `wiki/rules/` — kind, parent, purpose, taken by grep, no page opened. 38 rules carry a parent: each is a step of the sequence of its phase (`rule-session-start`, `rule-plan-mode`, `rule-end-of-work`, `rule-documentation`; the order of `children` is content) or a tool under `rule-harness` (`rule-lint`, `rule-render-harness`, `rule-governed-files-hook`, `rule-bash-guard`, `rule-tests-clock-pinned`, the MOCs `rule-settings` and `rule-claude-md`). All stand: none is a condition on the pages of one category — `rule-synthesis` is about Insights, but it is a step of Documentation, and a page has one `parent`. The rules that hold for one category alone are the six schemas, one per category; no category has two, no category MOC is made, the schemas stay under `rule-page-schemas`. The five roots are the four phases and the harness: no root MOC over them — it would hold no cross-cutting promise of its own (the order of the phases is held by the hooks of each: the ledger hook without `/hi`, the prespec hook, the retro commit), and a MOC without an Estimate is against the rule. The four placeholders (`rule-work-mode`, `rule-subagent-guppi`, `rule-spec-box`, `rule-morph`) get a parent when they are taken up.
> The edge Rule → Entity. By case 240.2 an Entity is what is measured and has no guard of its own; its guard is a separate Rule. Today `rule-sprint` names `entity-sprint` in a code span; there is no edge. The precedents of the mechanism: `children` on an Entity is written by the script from the `parent` of the child; `severity` of an Insight is `computed`, recomputed by the cascade of `generate`. Two hand-written fields for one edge are two records of one fact, and they drift; so one side is written — `applies_to` on the Rule, in the Case — and `rules` on the Entity is the backlink the cascade of `generate` recomputes, as `severity`; lint checks the slugs and the agreement of the pair. `applies_to` names an Entity only: a rule constrains a case — a page, a session, a file — not another rule, and what a rule reads or guards among the rules is derived from `implementation_ref` and `governs`, never written (the person's decision of this session).
> The pages: `rule-rules-schema` and `rule-entities-schema` were ratified in this session (304.2, 304.3) and do not exist yet — the field goes into their Render, so 305.1 supersedes 304.2 and 305.2 supersedes 304.3 (299.1): the pages are born in the right shape, and the live legs of `estimate-prespec-catches-a-superseded-case` and `estimate-materialize-marks-superseded` are taken by it. `rule-page-generation` `draft`, `rule-sprint` `built`, `entity-sprint` `draft` (MOC, `estimates: []`), `rule-lint` `built`. The Estimates: `estimate-rules-schema-checked` and `estimate-entities-schema-checked` are created anew by the superseding Cases with the field in their Criterion; `estimate-lint-catches` gets a second `replace` pair of the session, on its `ref` line; `estimate-generate-writes-rules-from-applies-to` is new, on `rule-page-generation`; `estimate-generate-rewords` and the other Estimates of `rule-page-generation` are not touched; `rule-sprint` gets a field alone, its Estimates are not touched (296). In `materialize` the filter by the schema stands on a `create` and a `defer`, not on the `set` of an `update`, so `set: {applies_to: …}` passes; in the librarian's run `render` comes after `generate`, so lint reads the new yaml. The slugs are free. Case 305.2 was superseded by 306.1 before the approval and left the Spec (299.1).

> **problem:**
> Where every rule stands and whether a category MOC or a root is needed; how the edge Rule → Entity enters the schemas, who writes which side of it and who checks it; and how the field reaches the two Renders ratified an hour before.

> **given:**
> `children` on an Entity is written by the script from the `parent` of the child; `severity` of an Insight is `computed`, recomputed by the cascade of `generate`.
> **＋** Case 240.2: an Entity is what is measured and has no guard of its own; its guard is a separate Rule.
> **＋** Case 299.1: a Case superseded in its own session leaves the Spec, the superseding Case is written whole; a Frontier line it closed is closed again by the superseding one.
> **＋** `rule-lint`: the class `ref` — a slug in a link field that no live or archived page carries; `tests/test_lint.py` and `tests/test_generate.py` fix the behaviour.

### Case 305.1 — `rule-rules-schema` with `applies_to` (supersedes 304.2)

> **given:**
> `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
> **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
> **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
> **＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/rules/schema.yaml`: a page in the shape, then one defect at a time.

> **when:**
> `guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`; `guppi lint` reads a page of `wiki/rules/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional; `ordered_children: true`.
> **＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
> **＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, Ordering, MOCs and enforcement, Enforcement, verbatim, and one sentence on the edge Rule → Entity after the paragraph of case 240.2; `fields` and `sections` — the rows of the tables whole, `applies_to` among them; `examples` — the four example pages.
> **－** `vault/wiki/rules/schema.md` does not exist.

```then
create:
  - slug: rule-rules-schema
    type: rule
    kind: Leaf
    purpose: Prevents a Rule page from carrying a field or section outside the shape lint checks, or lacking one it needs
    enforcement: render
    governs: vault/wiki/rules/schema.yaml
    render_mode: full
    parent: rule-page-schemas
    estimates: [estimate-rules-schema-checked]
    tags: [harness, render, schema]
    sections:
      Purpose: |
        Prevents a Rule page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/rules/schema.yaml`, the file `guppi lint` reads for every page of `wiki/rules/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8). `applies_to` is the edge Rule → Entity, written in the Case; the Entity's `rules` is its backlink, computed (case 305).
      Render: |
        <!-- rule-rules-schema -->
        type: rule
        description: |
          Three blocks: properties, body, history. Mirrors Entity, with three differences that matter: how it is enforced, what a MOC means, and that children are ordered.

          A Rule is a standing condition one case can break, with a guard that refuses that case when it occurs. The check: can one case refute it, and is there something to refuse that case? Yes to both → a Rule, and its Estimate is the test that the guard works. A condition no single case can break — a measure of the whole — is not a Rule but an Estimate on an Entity; a condition with no guard is not one either. A Leaf is a condition on each case; a MOC a sequence whose Estimate promises the order — one run out of order breaks it. A Rule is of the harness or of an Entity: on an Entity it is a checkable requirement, and its Estimate promises how the requirement is controlled. That single definition covers both harness hooks and code constraints — see Enforcement below (case 240.2).

          Ordering. `children` on a Rule MOC is an ordered list, and the order is the content. A workflow MOC says `retro → handoff → documentation`; sorting those alphabetically destroys the only thing the page was recording. Scripts that rebuild backlinks must preserve the order given, and lint must not normalize it. This is the one place a Rule MOC differs structurally from an Entity MOC, where children are independent requirements and order is arbitrary.

          MOCs and enforcement. `hook` and `check` are meaningless on a MOC: grouping does not fire on an event and does not run against code. The force there lives in the children. `render` is the exception. A MOC that renders holds the frame of a harness file — its structure and the markers its children splice into — while each child renders one section. The frame is not separable from the grouping: a MOC over three sections plus a separate Leaf holding an empty template with markers would be two pages describing one thing. So a rendering MOC uses `render_mode: full` on the target file, and its children with a Render use `partial` into the same file. Child order is the order of sections in the output, which is the ordinary Rule-MOC rule about order being content, applied literally. A child without a Render — a script the frame calls by name — is a step of the workflow that contributes nothing to the file; the renderer skips it, and a marker line for it is an error. Not every step of a workflow is a child page. The atomicity rule applies as everywhere: split when parts fail independently and are fixed differently. Four `@`-imports from the vault fail the same way (missing file, wrong path) and are fixed the same way — one Leaf, listed in its body. But `git pull` and `gh issue list` fail differently, on conflicts versus authentication, so those are separate Leaves. Intermediate MOCs need justification too. A MOC earns its place when a cross-cutting Estimate can be stated for it; "internal storage" has none of its own — the only meaningful check covers the whole load, and that belongs to the workflow MOC.

          Enforcement. Three ways a rule has force. `hook` — fires during the session lifecycle. Blocks a ledger write, appends to `log.md` on every page change, refuses a commit while tests are red. `implementation_ref` points at the script. `check` — runs against the code. This is where constraints live: "synchronous API only in this module" is not a hook, it is a linter rule that catches `async` there. `implementation_ref` points at the linter config or test. `render` — the rule's own body is the harness text. `governs` names the target file, `render_mode` says whether the body replaces it entirely or is spliced between markers `<!-- rule-slug -->` … `<!-- /rule-slug -->`. `render` is what closes the self-improvement loop. Where `hook` and `check` describe something implemented elsewhere, a `render` rule is the implementation — the page is the source of truth and a script regenerates the harness from it. Change the rule through a ratified decision and the skill changes; there is no second copy to drift. `render` applies to harness rules and to the vault files a rule renders — `case-schema.md` from `rule-case-protocol` (case 273.1), each `schema.yaml` from a child of `rule-page-schemas` (case 304). A constraint on an Entity — async in the pricing module — is a `check`: it has no `render_mode`, because there is nothing in the harness to write it into; a `check` rule whose script writes a file names that file in `governs`, so the guard reads the field alike (`rule-sprint`, case 209.7). A constraint that no hook, check or render can detect is not a Rule at all. It is a sentence in an Entity's `How it works`. Keeping that line sharp is what stops `rules/` from filling with unenforceable declarations. Every Rule requires an Estimate. A broken hook breaks the workflow as thoroughly as broken product code breaks the product — there is no "documentation-class" exemption. In the harness a thing is a Rule when its code is a guard — it refuses a case: a hook, a check, a render that refuses drift. A thing is an Entity when it is measured and has no guard of its own; its guard is a separate Rule. The sprint is an Entity by this criterion — its Definition of done is read, and `rule-sprint` is its guard — not an exception (case 240.2). A rule of an Entity names it in `applies_to`, the edge Rule → Entity; the Entity's `rules` is the backlink, computed by the cascade of `generate`. A rule constrains a case — a page, a session, a file — never another rule: what a rule reads or guards among the rules follows from `implementation_ref` and `governs` and is never written (case 305).

          No body section is derived from a ref field: `estimates`, `children`, `parent` and `implementation_ref` are the link, seen by Obsidian since case 148.1 (case 166.1). `deferred_by` is written on a defer and cleared on a `supersedes` by `guppi generate`, never by hand (case 52.3).
        properties:
          required: [type, kind, purpose, status, estimates, origin, sprint, created, tags]
          optional: [enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to]
          values:
            kind: [MOC, Leaf]
            status: [draft, built, archived]
            enforcement: [hook, check, render]
            render_mode: [full, partial]
          conditional:
            - when: {enforcement: hook}
              required: [implementation_ref]
            - when: {enforcement: check}
              required: [implementation_ref]
            - when: {enforcement: render}
              required: [governs, render_mode]
            - when: {kind: MOC}
              required: [children]
              forbidden_values: {enforcement: [hook, check]}
        ordered_children: true
        body:
          required: ["## Purpose", "## History"]
          optional: ["## Render", "## How it works"]
          conditional:
            - when: {enforcement: render}
              required: ["## Render"]
        fields:
          type: |
            required; `rule`. Page category.
          kind: |
            required; `MOC` | `Leaf`. MOC: a workflow — an ordered sequence of rules. Leaf: one enforceable rule.
          purpose: |
            required; one line. What this prevents, not what it provides. The index line of the category is built from it.
          status: |
            required; `draft` | `built` | `archived`. Set by the cascade of `generate` once every Estimate passes, never by hand.
          enforcement: |
            optional; `hook` | `check` | `render`. How the rule has force, and which of the fields below apply. On a Leaf, any of the three. On a MOC, only `render` — see MOCs and enforcement.
          implementation_ref: |
            required on `hook` and `check`; list of paths. The hook script, or the linter/test that performs the check. The field is the link; no body section repeats it (case 166.1).
          governs: |
            required on `render`, allowed on `check`; path. The file this rule's text is rendered into — a harness file, or a file of the vault such as `case-schema.md` (case 273.1) or a `schema.yaml` (case 304); on a `check` rule, the file its script writes — the governed-files hook refuses a hand edit of either (case 209.7).
          render_mode: |
            required on `render`; `full` | `partial`. Whether the rule's body becomes the whole target file, or is spliced between markers inside it.
          parent: |
            on a Leaf; quoted wikilink `"[[slug]]"`. The workflow MOC above it. The scripts read the slug through the brackets; a slug without a category prefix stays bare (case 148.2). The field is the link; no body section repeats it (case 166.1).
          children: |
            on a MOC; ordered list of quoted wikilinks `"[[slug]]"`. See Ordering. The field is the link; no body section repeats it (case 166.1).
          estimates: |
            required; list of quoted wikilinks `"[[slug]]"`. On a Leaf: that the rule does what it claims. On a MOC: that the sequence itself holds. Empty until the person names a promise. The field is the link; no body section repeats it (case 166.1).
          deferred_by: |
            optional; list of decision quoted wikilinks `"[[slug]]"`. The Decision pages whose `defer` targets this page. Written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; the index line carries it, so `ask-guppi` reaches the deferred decision without opening the page (case 52.3).
          applies_to: |
            optional; list of quoted wikilinks `"[[entity-slug]]"`. The Entities this rule is the guard of (case 240.2): a rule that guards a thing names it here — `rule-sprint` → `entity-sprint`, `rule-harness` → `entity-guppi`; a rule of the process — a phase MOC and its steps — carries none; written in the Case, never computed. The Entity's `rules` is the backlink, written by the cascade of `generate` (case 305). The field is the link; no body section repeats it.
          origin: |
            required; `raw/YYYY-MM-DD/HHMM/ledger.md#case-N` — the date form, `raw/YYYY-MM-DD/ledger.md#case-N`, on pages born before 2026-09-13 (case 103.6).
          sprint: |
            required; the sprint id.
          created: |
            required; date.
          tags: |
            required; list, ratified in the Case.
        sections:
          "## Purpose": |
            required. Expands the property: what goes wrong without this rule. State the failure it prevents, not the behaviour it produces.
          "## Render": |
            required on `render`. The text written into `governs`, wrapped in `<!-- slug -->` markers. This section is the implementation. On a rendering MOC it is the frame, containing the children's markers.
          "## How it works": |
            optional. MOC only: why the steps are in this order, and what breaks if they are reordered. On a Leaf the promise lives in its Estimates and the mechanism in the docstring of its code, or in its Render; a Leaf that still carries the section keeps it until its next touch, when the section leaves (cases 193, 200.2).
          "## History": |
            required. Appended by hook, never by an agent. Always the last section.
        examples:
          "MOC — a rendering workflow": |
            Holds the frame of the skill file; children splice into its markers, in child order.

            ---
            type: rule
            kind: MOC
            purpose: Prevents a session from being loaded piecemeal by read-tool calls
            status: draft
            enforcement: render
            governs: .claude/skills/hi/SKILL.md
            render_mode: full
            parent: rule-session-start
            children: [rule-internal-context, rule-git-context, rule-github-issues]
            estimates: [estimate-hi-no-read-calls]
            origin: raw/2026-09-08/ledger.md#case-5
            sprint: 2026-Q3-s4
            created: 2026-09-08
            tags: [session, harness]
            ---

            ## Purpose
            Prevents a session from being loaded piecemeal by read-tool calls. Bash substitutions in a
            command body resolve before the agent's first turn, so the context is simply present —
            there is no step the agent can forget or reorder.

            ## How it works
            Rendered in full into the skill file; the three children splice into the markers below, in
            the order they are listed. Editing the skill directly is meaningless — the next render
            overwrites it. Changes belong on these pages, through a ratified decision.

            ## Render
            <!-- rule-skill-hi -->
            <!-- rule-internal-context -->
            <!-- rule-git-context -->
            <!-- rule-github-issues -->

            Assemble the Frontier from the above and present it as a list: tasks, problems, debt
            carried over, and where the sprint stands. Wait for the human to pick the order.
            <!-- /rule-skill-hi -->

            ## History
            - 2026-09-08 created · raw/2026-09-08/ledger.md#case-5
          "Leaf — a partial render": |
            ---
            type: rule
            kind: Leaf
            purpose: Prevents work starting without the current sprint and last session's handover
            status: draft
            enforcement: render
            governs: .claude/skills/hi/SKILL.md
            render_mode: partial
            parent: rule-skill-hi
            estimates: [estimate-internal-context-loaded]
            origin: raw/2026-09-08/ledger.md#case-6
            sprint: 2026-Q3-s4
            created: 2026-09-08
            tags: [session, harness]
            ---

            ## Purpose
            Prevents work starting without the current sprint and the previous session's handover.
            Both are vault files, both fail the same way — missing file or wrong path — so they are
            one rule rather than two.

            ## How it works
            `case-schema.md` is listed here since case 273; the glossary arrives through `@import`
            in `CLAUDE.md`, the category schemas are read when a page of their category is written,
            and re-reading either would duplicate context that is already present.

            ## Render
            <!-- rule-internal-context -->
            @wiki/sprint.md
            @wiki/brief.md
            <!-- /rule-internal-context -->

            ## History
            - 2026-09-08 created · raw/2026-09-08/ledger.md#case-6
          "Leaf — a hook": |
            ---
            type: rule
            kind: Leaf
            purpose: Prevents a ledger line from being written to the wrong branch
            status: built
            enforcement: hook
            implementation_ref: [.claude/hooks/ledger-guard.sh]
            parent: rule-session-start
            estimates: [estimate-ledger-guard]
            origin: raw/2026-09-08/ledger.md#case-6
            sprint: 2026-Q3-s4
            created: 2026-09-08
            tags: [ledger, session]
            ---

            ## Purpose
            Prevents a ledger line from being written to the wrong branch. SessionStart cannot block
            anything — exit 2 is a no-op there — so without this guard a decision ratified before the
            workspace resolves would silently land outside the session.

            ## How it works
            PreToolUse, matched on writes to `ledger.md`. Reads the readiness flag written when the
            workspace was resolved; exits 2 and blocks the write if it is missing.

            ## History
            - 2026-09-08 created · raw/2026-09-08/ledger.md#case-6
            - 2026-09-09 status: draft → built
          "Leaf — a check (constraint)": |
            ---
            type: rule
            kind: Leaf
            purpose: Prevents async calls leaking into the pricing module
            status: built
            enforcement: check
            implementation_ref: [ruff.toml, tests/lint/test_pricing_sync.py]
            estimates: [estimate-pricing-sync-check]
            origin: raw/2026-09-12/ledger.md#case-2
            sprint: 2026-Q3-s4
            created: 2026-09-12
            tags: [pricing, constraints]
            ---

            ## Purpose
            Prevents async calls leaking into the pricing module. Pricing runs inside a synchronous
            transaction; an await there does not fail loudly, it produces a partially applied price.

            ## How it works
            A lint rule flags `async def` and `await` under `src/pricing/`. Runs in CI, so the
            violation surfaces at the change that introduces it rather than at the next incident.

            ## History
            - 2026-09-12 created · raw/2026-09-12/ledger.md#case-2
        <!-- /rule-rules-schema -->
  - slug: estimate-rules-schema-checked
    type: estimate
    ref: rule-rules-schema
    kind: QA
    purpose: A Rule page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
    method: pytest tests/test_schemas.py -k rules on the live vault/wiki/rules/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/rules/ but the placeholders
    tags: [harness, render, schema]
```

```tasks
- [x] create `rule-rules-schema` (parent `rule-page-schemas`), the Render above
- [x] create `estimate-rules-schema-checked` (ref `rule-rules-schema`)
- [x] `tests/test_schemas.py`: one parametrized case per category on the live `vault/wiki/<category>/schema.yaml` — a page in the shape has no `schema` finding; a required field missing, a value outside the list, a conditional not met, a required section missing — one finding each
- [x] `git rm vault/wiki/rules/schema.md`
- [x] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
- [ ] read `estimate-rules-schema-checked`: `uv run pytest tests/test_schemas.py -k rules`, then `make lint` in the librarian's run
```

### Case 305.3 — `generate` writes `rules` from `applies_to`

> **given:**
> The cascade of `generate`, after the entries are applied, recomputes on the live pages the status of every Entity and Rule and the `severity` of every Insight.
> **＋** `tests/test_generate.py` fixes the behaviour on a temp vault.

> **when:**
> `guppi generate` reaches the cascade.

> **then:**
> The `rules` of every live Entity is the slugs of the live rules whose `applies_to` names it, in slug order; the field is written when the list is not empty or the field already stands; a change is a History line `rules: [...] · cascade`; an empty list on a page without the field writes no field.
> **＋** A rule with `applies_to` on a slug with no live page: the entry applies and the field stands; the cascade skips it; lint names it (305.5).
> **－** An archived rule gives no edge; `applies_to` is never computed — it comes from the Case alone.

```then
create:
  - slug: estimate-generate-writes-rules-from-applies-to
    type: estimate
    ref: rule-page-generation
    kind: QA
    purpose: The rules of every live Entity are the live rules whose applies_to names it, recomputed by the cascade of generate on every run
    method: pytest tests/test_generate.py on a temp vault; the live reading the librarian's run of this session — entity-sprint carries rules [rule-sprint]
    tags: [harness, workflow, librarian]
update:
  - slug: rule-page-generation
    replace:
      - old: "the cascade after all entries computes what is computed — `built`, the archive of a superseded decision, the severity of an Insight — never by hand (case 104)"
        new: "the cascade after all entries computes what is computed — `built`, the archive of a superseded decision, the severity of an Insight, the `rules` of an Entity from the `applies_to` of the live rules (case 305.3) — never by hand (case 104)"
    change: the cascade writes rules on an Entity from the applies_to of the live rules (case 305.3)
  - slug: estimate-generate-cascades
    set: {purpose: "The cascade computes built, the archive of a superseded decision, the severity of an Insight and the rules of an Entity, never by hand"}
    replace:
      - old: "**－** A page without Estimates keeps its status; no section of any page is derived or touched by the cascade."
        new: "**＋** The `rules` of every live Entity is recounted from the `applies_to` of the live rules (305.3).\n**－** A page without Estimates keeps its status; no section of any page is derived or touched by the cascade."
    change: one line of the Criterion — the cascade recounts rules (case 305.3; pre-spec)
```

```tasks
- [x] create `estimate-generate-writes-rules-from-applies-to` (ref `rule-page-generation`)
- [x] update `rule-page-generation`: one `replace` pair in the Purpose — the cascade sentence
- [x] update `estimate-generate-cascades`: `purpose` and one `replace` pair inside the Criterion, `pending`
- [x] read `estimate-generate-cascades`: `uv run pytest tests/test_generate.py`; live — the librarian's run of this session
- [x] `guppi/generate.py`: `rules` in the cascade, the History line
- [x] `tests/test_generate.py`: the edge appears, leaves when `applies_to` leaves, an archived rule does not count
- [x] read `estimate-generate-writes-rules-from-applies-to`: `uv run pytest tests/test_generate.py`; live — the librarian's run of this session, `entity-sprint` with `rules: [rule-sprint]`
```

### Case 305.4 — the first edge: `rule-sprint` → `entity-sprint`

> **when:**
> The librarian applies the `update` of `rule-sprint`; the cascade runs.

> **then:**
> `rule-sprint` carries `applies_to: ["[[entity-sprint]]"]`; `entity-sprint` carries `rules: ["[[rule-sprint]]"]`; Obsidian shows the edge.
> **－** The Estimates of `rule-sprint` are not touched — a field alone (296).

```then
update:
  - slug: rule-sprint
    set: {applies_to: [entity-sprint]}
    change: the first edge Rule → Entity — rule-sprint is the guard of entity-sprint (cases 240.2, 305.4)
```

```tasks
- [x] update `rule-sprint`: `set: {applies_to: [entity-sprint]}`
```

### Case 305.5 — lint: `applies_to` and `rules` under `ref`

> **given:**
> `rule-lint`: the class `ref` — a slug in a link field that no live or archived page carries; `links_of` names the link fields; `tests/test_lint.py` fixes the behaviour.

> **when:**
> `uv run guppi lint` reads the live pages.

> **then:**
> A slug in `applies_to` that no live or archived page carries, or that is not an Entity, is a `ref` finding; an Entity's `rules` that differs from the live rules whose `applies_to` names it is a `ref` finding: `rules differs from the applies_to of the live rules: +a, -b`.
> **－** The other classes do not change.

```then
update:
  - slug: estimate-lint-catches
    replace:
      - old: "`ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by` or in a History wikilink"
        new: "`ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a History wikilink"
      - old: "a `### case N` block of an Estimate with no decision page."
        new: "a `### case N` block of an Estimate with no decision page; an `applies_to` that names no Entity, and an Entity's `rules` that differs from the live rules whose `applies_to` names it (case 305.5)."
    change: applies_to and rules under ref — the slugs and the agreement of the pair (case 305.5)
```

```tasks
- [x] update `estimate-lint-catches`: two `replace` pairs inside the Criterion, `pending` by 296
- [x] `guppi/lint.py`: `applies_to` and `rules` in `links_of` and `check_refs`, the check of the pair; the docstring
- [x] `tests/test_lint.py`: an `applies_to` on no Entity; a `rules` that disagrees
- [ ] read `estimate-lint-catches`: with 304.8 — `uv run pytest tests/test_lint.py`, then `make lint` in the librarian's run
```

## Case 306 — Slice 3f, theme 3: the glossary as an Entity under `entity-guppi`

> **context:**
> `glossary.md` — 50 rows in eight groups and a table of retired terms: `where` names a page on 28 rows, a `§N` of `index.md` on 19, `here` on 3. The file is changed by hand; `/hi` loads it through `rule-internal-context`. The pattern is the sprint: `entity-sprint-migration` holds its content in `## Milestones`, `rule-sprint` is its guard, writes `sprint.md`, `--check` in `make lint`, ticks its Spec lines through `render.tick_command_lines`. The librarian runs `sprint` as step 5 of the frame of `rule-documentation`; `estimate-documentation-completes` names the step in its Criterion. The Case schema names three tickers of the Spec. By the Entity schema a Leaf carries `parent`; a MOC is a thing whose parts the person named as built (240.1) — a term is a row, not a part, so the glossary is a Leaf. No root stands over the Entities: `entity-sprint` is a MOC without a parent (241). `rule-harness` keeps the code of the harness equal to the pages that describe it; `make test` is the Makefile target over the whole suite, `estimate-harness-pipeline` covers `make test-harness` (render and lint). Vault: `entity-guppi`, `entity-glossary`, `rule-glossary` and the five Estimate slugs are free; `entity-sprint` `draft`, `rule-harness` `built`, `rule-documentation` `built`, `rule-lint` `built`, `rule-case-protocol` `draft`. The Render of `rule-entities-schema` was ratified in 305.2 and the page does not exist — 306.1 supersedes 305.2 (the section `## Terms`); `rule-rules-schema` is not touched. The Estimates touched: `estimate-documentation-completes` (step 6), `estimate-case-protocol-loaded` (the fourth ticker), `estimate-sprint-migration-rule-class-files-dissolved` ("the glossary from `terms`") — one `replace` pair each, `pending`; `estimate-harness-pipeline`, the Estimates of `rule-lint`, `rule-sprint` and `entity-sprint-migration` but the one named — not. The decisions of this session: the glossary is an Entity, not a `terms` field on the pages; the glossary carries no tick — the tick of 306.6 marks a Spec line, never a term; `rule-work-mode`, a placeholder, is a live page and the `where` of Work Mode.
> The rows on `§N` and `here` go to the page whose meaning they name — after 304 the defining pages exist: the six schemas and `rule-page-schemas` take Entity, Rule, Estimate, Lesson, Insight, MOC, Leaf, Vault and the fields; `rule-page-generation` takes `origin`, `deferred_by` and the statuses; `rule-case-protocol` Ratification, Contract, Case, the ledger grammar and the agents. C4 model and Delegate — rejected ideas — and the four retired terms — retired — are not rows; the History of `entity-glossary` names them, their decisions stand in the archived ledgers of 2026-09-08 and 2026-09-09.

> **problem:**
> How the glossary enters the graph as a thing: who its parent is and how the root earns its place; what its section and Estimate are; which rule guards it, how a term is added and how the file is rendered; who runs and checks the script; and where the 19 rows on `§N` and the 3 on `here` go, so that no row is lost.

> **given:**
> `rule-sprint`: a `check` rule with `governs`; the script writes the file from a page, `--check` compares in memory, writes nothing, exit 1 on a difference; once it wrote the file it ticks its Spec lines (250.2).
> **＋** `rule-governed-files-hook` refuses a hand edit of `governs`.
> **＋** Case 240.1: a MOC is a thing whose parts the person named as built; a Leaf is not, and a Leaf carries `parent`. Case 240.2: the guard of an Entity is a separate Rule — the edge `applies_to` (305).
> **＋** Case 299.1: a Case superseded in its own session leaves the Spec, the superseding Case is written whole.
> **＋** `tests/test_glossary.py` fixes the behaviour on a temp vault.

### Case 306.1 — `rule-entities-schema` with `## Terms` (supersedes 305.2)

> **given:**
> `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
> **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
> **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
> **＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/entities/schema.yaml`: a page in the shape, then one defect at a time.

> **when:**
> `guppi render` writes `vault/wiki/entities/schema.yaml` from `rule-entities-schema`; `guppi lint` reads a page of `wiki/entities/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `parent, children, code_ref, deferred_by, rules`; values `kind: MOC | Leaf`, `status: draft | built | archived`; conditional — `Leaf` requires `parent`, `MOC` requires `children`; `computed: [rules]`; the sections `## Purpose` and `## History` required, `## How it works`, `## Milestones`, `## Backlog`, `## Closed`, `## Terms` optional.
> **＋** An Entity page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; an Entity with `rules` on live Rules has none; the glossary page with `## Terms` has none.
> **＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the Slug, `built`, `How it works` and Constraints notes, verbatim, one sentence on the edge after Constraints and one on the glossary page; `fields` and `sections` — the rows of the tables whole, `rules` and `## Terms` among them; `examples` — the two example pages.
> **－** `vault/wiki/entities/schema.md` does not exist.

```then
create:
  - slug: rule-entities-schema
    type: rule
    kind: Leaf
    purpose: Prevents an Entity page from carrying a field or section outside the shape lint checks, or lacking one it needs
    enforcement: render
    governs: vault/wiki/entities/schema.yaml
    render_mode: full
    parent: rule-page-schemas
    estimates: [estimate-entities-schema-checked]
    tags: [harness, render, schema]
    sections:
      Purpose: |
        Prevents an Entity page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/entities/schema.yaml`, the file `guppi lint` reads for every page of `wiki/entities/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8). `rules` is the backlink of the edge Rule → Entity, computed by the cascade of `generate` from the `applies_to` of the live rules (case 305); `## Terms` is the section of the glossary page, `entity-glossary` (case 306).
      Render: |
        <!-- rule-entities-schema -->
        type: entity
        description: |
          Three blocks: properties, body, history. One schema for both kinds; sections that do not apply are omitted.

          An Entity is a thing the developer builds: a noun the person named as part of what is built. The check before a `create`: who makes this thing? The developer → an Entity. The product's user, or the running product — a post, an account, a record → data, which lives in the product and is never a page. A developer who uses GUPPI is still the developer; "user" in this check is always the user of the developer's product (case 240.1).

          A MOC is a thing whose parts the person named as things that are built; a Leaf is a thing for which the person has not done that yet. A part comes only from the person's words, through a Case; the agent proposes a cut — in Retro, by the atomicity rule of §6 of `index.md` — and never makes it. A part is itself an Entity: its own code, its own conditions. What is not a part — a field, a button, a function inside a Leaf — is the Leaf's inner working and goes to `## How it works`, not to a page. The Estimates of a MOC measure what no child owns; a Leaf's measure its own scope; a Leaf with empty `estimates` is legal — the person said nothing yet. Depth is not fixed in advance — it follows the atomicity rule and nothing else.

          No Entity for a "why": the reason behind a rule lives in the Decision that made it, in the rule's `## Purpose` and in the lessons behind it through an Insight; an Entity per why would be a fourth copy (case 240.1).

          Slug. Meaningful, written by the main agent in the Case and checked by pre-spec for collisions. The decision that created it is `decision-case-<N>`, reachable through the page's `origin`; the relationship is readable without opening either page.

          `built` is not a field you set. `status: built` follows from every Estimate having passed. The cascade of `generate` computes it. Writing it by hand would create a second source of truth about whether the work is done.

          `How it works` is unratified, and that is fine. Purpose and criteria are ratified in the Case, before anything is built. `How it works` describes what was actually built, so it can only be written afterwards — by the main agent at handoff, which is the only point where someone has watched the tasks close. The boundary: it describes structure, it does not introduce claims. New statements about what the thing is for, or what counts as correct, belong in a Case. If writing this section reveals that what was built differs from what was decided, that is not a wording fix — it is a flag for `brief.md`.

          Constraints are not an Entity section. A constraint that can be violated and noticed is a Rule with a mandatory QA Estimate — "synchronous API only" becomes a linter that catches `async` in that module. A constraint that cannot be checked by anything is a sentence in `How it works`, not a structure. This keeps Rule meaning one thing: something that can be broken, where breaking it will be detected. The guard of an Entity is a Rule that names it in `applies_to`; the Entity's `rules` lists those Rules — the backlink, computed by the cascade of `generate`, never written by hand (case 305).

          Two Entities of GUPPI hold content in a section of their own: the sprint page, `entity-sprint-<id>`, in `## Milestones`, `## Backlog` and `## Closed` (case 234), and the glossary page, `entity-glossary`, in `## Terms` — a flat table of the terms; `guppi sprint` and `guppi glossary` render `sprint.md` and `glossary.md` from them, and `rule-sprint` and `rule-glossary` are their guards (case 306).

          No body section is derived from a ref field: `estimates`, `children`, `parent`, `rules` and `code_ref` are the link, seen by Obsidian since case 148.1 (case 166.1). `deferred_by` is written on a defer and cleared on a `supersedes` by `guppi generate`, never by hand (case 52.3).
        properties:
          required: [type, kind, purpose, status, estimates, origin, sprint, created, tags]
          optional: [parent, children, code_ref, deferred_by, rules]
          values:
            kind: [MOC, Leaf]
            status: [draft, built, archived]
          conditional:
            - when: {kind: Leaf}
              required: [parent]
            - when: {kind: MOC}
              required: [children]
        computed: [rules]
        body:
          required: ["## Purpose", "## History"]
          optional: ["## How it works", "## Milestones", "## Backlog", "## Closed", "## Terms"]
        fields:
          type: |
            required; `entity`. Page category.
          kind: |
            required; `MOC` | `Leaf`. MOC: no direct criteria, holds children. Leaf: direct behaviour of its own.
          purpose: |
            required; one line. Why this exists. Lives in properties, not the body, because the index line of the category is built from it and must stay one line per page. The body expands on it; the property stays short.
          status: |
            required; `draft` | `built` | `archived`. Flat list, like every other category. `built` is set by the cascade of `generate`, not by hand: an Entity is built only once all of its Estimates pass — a graph property.
          parent: |
            required on a Leaf; quoted wikilink `"[[slug]]"`. The MOC above it. Written by the script from the ledger's `ref`. The scripts read the slug through the brackets; a slug without a category prefix stays bare (case 148.2). The field is the link; no body section repeats it (case 166.1).
          children: |
            required on a MOC; list of quoted wikilinks `"[[slug]]"`. Functional requirements, each its own page. Written by the script. The field is the link; no body section repeats it (case 166.1).
          estimates: |
            required; list of quoted wikilinks `"[[slug]]"`. On a Leaf: checks of its own behaviour. On a MOC: cross-cutting checks that belong to all children and to none individually — non-functional requirements live here. The field is the link; no body section repeats it (case 166.1).
          deferred_by: |
            optional; list of decision quoted wikilinks `"[[slug]]"`. The Decision pages whose `defer` targets this page. Written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; the index line carries it (case 52.3).
          rules: |
            optional, computed; list of quoted wikilinks `"[[rule-slug]]"`. The Rules that are the guard of this Entity — the backlink of their `applies_to`, recomputed by the cascade of `generate` on every run, never written by hand (case 305). The field is the link; no body section repeats it.
          code_ref: |
            optional; list of paths. Code, commits or PRs. Allowed on both kinds: a Leaf points at files, a MOC may point at the directory or module it corresponds to. The field is the link; no body section repeats it (case 166.1).
          origin: |
            required; `raw/YYYY-MM-DD/HHMM/ledger.md#case-N` — the date form, `raw/YYYY-MM-DD/ledger.md#case-N`, on pages born before 2026-09-13 (case 103.6). The ratified decision that created it.
          sprint: |
            required; the sprint id.
          created: |
            required; date.
          tags: |
            required; list. Chosen at the vault query before the Case, ratified in the Case.
        sections:
          "## Purpose": |
            required. Expands the `purpose` property: what problem this solves, why it exists in this shape.
          "## How it works": |
            optional. How it is built. For a Leaf, the mechanics. For a MOC, the principle by which it splits into children — why these children and not some other cut. Omitted while `draft`.
          "## Milestones": |
            the sprint page only (`entity-sprint-<id>`): the Slices in order under `### <name>` headings; the first with an item not done, or with none, is current. An item is a line `- [[slug]] — <text>` or a plain line `- <text>`; `guppi sprint` renders the file from them (cases 209, 229.1).
          "## Backlog": |
            the sprint page only: the items without a turn, the same lines; after Milestones.
          "## Closed": |
            the sprint page only: the closed Slices as prose, copied into the render as they are; after Backlog.
          "## Terms": |
            the glossary page only (`entity-glossary`): a table `| term | meaning | where |`, one row per term in the order the person keeps, `where` a wikilink to the live page that defines the term; `guppi glossary` renders `vault/wiki/glossary.md` from it, grouped by the parent MOC of `where`; a term enters, changes or leaves by an `update` of the page (case 306).
          "## History": |
            required. Appended by hook, never by an agent. Always the last section.
        examples:
          "MOC": |
            ---
            type: entity
            kind: MOC
            purpose: Lets a buyer review an order before paying
            status: draft
            children: [entity-cart-add, entity-cart-quantity, entity-cart-remove, entity-cart-total]
            estimates: [estimate-cart-render-time]
            code_ref: [src/cart/]
            origin: raw/2026-09-08/ledger.md#case-1
            sprint: 2026-Q3-s4
            created: 2026-09-08
            tags: [cart, checkout]
            ---

            ## Purpose
            Lets a buyer review an order before paying. Until now items went straight from the
            catalogue to payment, with no point at which the order could be corrected.

            ## How it works
            Split by operation rather than by screen: adding, changing quantity, removing and
            totalling fail independently and are fixed in different places, so each is its own child.
            Render time is cross-cutting — it belongs to the cart as a whole — so it sits on this
            page rather than on any child.

            ## History
            - 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
          "Leaf": |
            ---
            type: entity
            kind: Leaf
            purpose: New clients receive a 0% discount
            status: built
            parent: entity-discount-rules
            estimates: [estimate-new-client-discount]
            code_ref: [src/discounts/new_client.py]
            origin: raw/2026-09-08/ledger.md#case-2
            sprint: 2026-Q3-s4
            created: 2026-09-08
            tags: [discounts, pricing]
            ---

            ## Purpose
            New clients receive a 0% discount. This is the deliberate baseline the other discount
            tiers are measured against, not an absence of a rule.

            ## How it works
            Order count is read at checkout; zero completed orders returns 0% before any other tier
            is evaluated, so no later rule can raise it accidentally.

            ## History
            - 2026-09-08 created · raw/2026-09-08/ledger.md#case-2
            - 2026-09-09 status: draft → built
        <!-- /rule-entities-schema -->
  - slug: estimate-entities-schema-checked
    type: estimate
    ref: rule-entities-schema
    kind: QA
    purpose: An Entity page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
    method: pytest tests/test_schemas.py -k entities on the live vault/wiki/entities/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/entities/
    tags: [harness, render, schema]
```

```tasks
- [x] create `rule-entities-schema` (parent `rule-page-schemas`), the Render above
- [x] create `estimate-entities-schema-checked` (ref `rule-entities-schema`)
- [x] `git rm vault/wiki/entities/schema.md`
- [x] `uv run guppi render`: `vault/wiki/entities/schema.yaml`
- [ ] read `estimate-entities-schema-checked`: `uv run pytest tests/test_schemas.py -k entities`, then `make lint` in the librarian's run
```

### Case 306.2 — `entity-guppi`, the root

> **when:**
> The librarian applies the entries; a reader opens the graph.

> **then:**
> `entity-guppi` is a MOC without a parent, `children: [entity-sprint, entity-glossary]`, `code_ref: [guppi/, .claude/]`; `entity-sprint` carries `parent: entity-guppi`; `rule-harness` carries `applies_to: [entity-guppi]`, and the cascade writes `rules: [rule-harness]` on `entity-guppi`.
> **＋** `estimate-guppi-tests-green`: `make test` — 0 failed on the branch.
> **－** The four phase MOCs carry no `applies_to` — rules of the process.

```then
create:
  - slug: entity-guppi
    type: entity
    kind: MOC
    purpose: GUPPI as the thing this repository builds — the harness and the vault it keeps; its parts the sprint and the glossary
    children: [entity-sprint, entity-glossary]
    estimates: [estimate-guppi-tests-green]
    code_ref: [guppi/, .claude/]
    tags: [harness, workflow]
    sections:
      Purpose: |
        GUPPI as the thing this repository builds: a Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. Its parts the person named: the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`) — the things of the vault that are content, not rules. `rule-harness` is its guard: the tools of the harness kept equal to the pages that describe them. In a developer's vault this page stands beside the root of the product and keeps GUPPI's own machinery apart from it (case 306.2).
  - slug: estimate-guppi-tests-green
    type: estimate
    ref: entity-guppi
    kind: QA
    purpose: make test is green on the branch — the whole suite of the harness
    method: make test, 0 failed; read after each Work Mode
    tags: [harness, tests]
update:
  - slug: entity-sprint
    set: {parent: entity-guppi}
    change: the sprint as a kind is a part of entity-guppi (case 306.2)
  - slug: rule-harness
    set: {applies_to: [entity-guppi]}
    change: rule-harness is the guard of entity-guppi — the edge Rule → Entity (case 306.2)
```

```tasks
- [x] create `entity-guppi` (MOC, root; children `entity-sprint`, `entity-glossary`)
- [x] create `estimate-guppi-tests-green` (ref `entity-guppi`)
- [x] update `entity-sprint`: `set: {parent: entity-guppi}`
- [x] update `rule-harness`: `set: {applies_to: [entity-guppi]}`
- [x] read `estimate-guppi-tests-green`: `make test` after Work Mode
```

### Case 306.3 — `entity-glossary` and `estimate-glossary-terms-defined`

> **when:**
> The librarian creates the page; a person or an agent reads a term.

> **then:**
> `entity-glossary` is a Leaf under `entity-guppi`; its `## Terms` is a table of 49 rows: the rows of today's `glossary.md` with their meaning verbatim and `where` a `[[slug]]`; the rows Sprint / `brief.md` and Harness / Hook split in two; the row Rule-class files rewritten to the fact; the rows on `§N` and `here` on the page whose meaning they name.
> **＋** A term enters, changes or leaves by an `update` of this page in a Case — a `replace` pair or the section whole; the `change` line is its History; a retired term is a History line, not a row.
> **＋** `estimate-glossary-terms-defined`: every `where` is a live page that defines the term; no term stands twice.
> **－** C4 model, Delegate and the four Retired terms are not rows; one History line of the page names them.

```then
create:
  - slug: entity-glossary
    type: entity
    kind: Leaf
    purpose: The terms of GUPPI, one row each with its meaning and the page that defines it; the source of glossary.md
    parent: entity-guppi
    estimates: [estimate-glossary-terms-defined]
    tags: [session, harness]
    sections:
      Purpose: |
        The terms of GUPPI: one row per term — the term, its meaning in one line, and `where`, the live page that defines it. The table is the content of this page; `rule-glossary` is its guard and renders `vault/wiki/glossary.md` from it, grouped by the parent MOC of `where`, for `/hi` to load. A term enters, changes or leaves by an `update` of this page in a Case — a `replace` pair or the section whole — and the `change` line is its History; a retired term is a History line, not a row. Not rows, by the decision of case 306.3: C4 model (not adopted), Delegate (the agent deciding without ratification; rejected), and the retired terms Proposal, Verify / Accept / Revoke, `deployment_unit` / `authority`, Librarian Report / Session Digest — their decisions stand in the archived ledgers of 2026-09-08 and 2026-09-09.
      Terms: |
        | term | meaning | where |
        |---|---|---|
        | Ratification | Human sign-off on a Decision; nothing in vault or code changes without one | [[rule-case-protocol]] |
        | Contract vs implementation | A Decision fixes what "done" means, never how; a contract change is a new Case | [[rule-case-protocol]] |
        | `ref`, `slug`, `supersedes` | A pointer to an existing page (absent: query the vault before a `create`; present: `update`); the page id = filename; the earlier case a ledger line corrects, written `{supersedes:case N}`, which marks every entry of that Case superseded and clears its `deferred_by` (case 200.2) | [[rule-case-protocol]] |
        | Decision | The atomic unit of work: `create`, `update`, `delete`, `defer`; Read is never one | [[rule-case-protocol]] |
        | Types | `create` a page (an Estimate is its own `create`, with `ref` on its target, case 193); `update` fields, `result`/`status` included, or `rename` — the page moves to the new slug and every link follows (case 258.1); `delete` sets `status: deleted` after an impact analysis, the librarian archives; `defer` postpones, a placeholder page when no `ref` | [[rule-case-protocol]] |
        | Case | The unit of dialogue, not a page: `context`, `problem`, `recommend`, `given`, `when`, `then`, `tasks`, `ratification` (case 163); `given` + `when` + `then` is the Estimate criterion, the Estimate named by slug (case 193); the page content is a `then` block in the Spec; splits into dotted sub-cases the parent's sign-off never covers | [[rule-case-protocol]] |
        | Main agent, Subagent | Runs Cases and writes ledger lines, until the Retro commit; executes plan tasks, never decides, a fork returns | [[rule-case-protocol]] |
        | Plan Mode | Frontier items discussed as Cases until each is ratified or deferred | [[rule-plan-mode]] |
        | the vault query | The vault query before a `create` without `ref`, `draft` pages included (case 277.3) | [[rule-ask]] |
        | Index line, `ask-guppi` | The Grep of a category's frontmatter — `purpose`, `root_cause` or `pattern`, and `deferred_by` — one line per live page, never compared across categories; no index file (case 147.8); the search agent over these lines, one entry point; Estimates through the target, Decisions through `deferred_by`; the archive answered by slug alone — `free`, `live` or `archived at <path>` — never by meaning (case 105.1) | [[rule-ask]] |
        | `/pre-spec` | The check of the ratified set against each other and the vault before the Spec is approved (case 261) | [[rule-prespec]] |
        | Spec | The ratified Cases as one document, approved as Claude Code's plan, copied to `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73.1) | [[rule-spec-capture]] |
        | Vault | The folder of Markdown pages, one per category | [[rule-page-schemas]] |
        | Page fields | `type` the kind; `purpose` one line the index is built from; `children` MOC only, ordered on a Rule; `estimates` cross-cutting on a MOC; `code_ref` (Entity Leaf), `implementation_ref` (`hook`, `check` rules) | [[rule-page-schemas]] |
        | Category fields | Estimate: `purpose`, `method`, `checked`, the sections `Criterion` and `Result` (case 193). Lesson: `trigger`, `root_cause`, `source` (in a ledger line, the external origin). Insight: `severity` (children not archived), `addressed_by` | [[rule-page-schemas]] |
        | Rule-class files | `index.md`, changed by a ratified `update` with `file`, by hand; `glossary.md` left the list with case 306 — rendered from `entity-glossary` — the schemas with case 304 — each the Render of a rule page — and `case-schema.md` with case 273; the term is retired with theme 6 of Slice 3f | [[rule-page-schemas]] |
        | Atomicity Rule | A unit splits when its closing judgment breaks into parts that fail and are fixed apart | [[rule-entities-schema]] |
        | MOC | A thing whose parts the person named as things that are built; `children` lists them; its Estimates measure what no child owns; a part comes from the person's words through a Case — the agent proposes a cut, never makes it (case 240.1) | [[rule-entities-schema]] |
        | Leaf | A thing whose parts the person has not named; holds `estimates` — empty is legal, the person said nothing yet — and a code pointer; its inner workings are `## How it works`, not pages (case 240.1) | [[rule-entities-schema]] |
        | Entity | A thing the developer builds, a noun the person named as part of what is built; the check before a `create`: who makes it — the developer → an Entity; the product's user or the running product → data, outside the vault; MOC or Leaf; never a page for a "why", that is a Decision (case 240.1) | [[rule-entities-schema]] |
        | Rule | A standing condition one case can break, with a guard that refuses that case when it occurs; the check: can one case refute it, and is there something to refuse it; a Leaf a condition on each case, a MOC a sequence whose Estimate promises the order; of the harness or of an Entity; force by `hook`, `check` or `render`; in the harness a thing is a Rule when its code is a guard, an Entity when it is measured and its guard is a separate Rule (case 240.2) | [[rule-rules-schema]] |
        | Estimate | The evidence: on a Rule a test that the guard works, on an Entity a reading of the whole no single case can break — the target's prefix says which; `QA` the answer is known, `Research` the reading finds it, on an Entity only, `failed` when the finding does not serve the purpose (case 240.3); one promise, one way to check it, the last result with its date (case 182); its own Leaf page under an Entity or Rule only, an explicit `create` with its slug in the Case, `estimate-<target minus its prefix>-<promise>`; fields `purpose`, `method`, `checked`; `QA` checks a known criterion, `Research` finds out; its Criterion is the `given`, `when` and `then` of one Case, replaced whole by the `update` that names it, which alone sets `pending`; no index, reached through the target's `estimates` (case 193) | [[rule-estimates-schema]] |
        | Estimate (status) | `pending` / `passed` / `failed`; `failed` is debt, archival the default outcome | [[rule-estimates-schema]] |
        | Lesson | Something learned; a fact the hook writes, no Case, no Estimate; slug = area + cause; a `knowledge` claim is checked by the Rule that leans on it | [[rule-lessons-schema]] |
        | Insight | Over Lessons sharing a root cause, made by the librarian on the second; surfaces in the brief's Deferred list and is the target of the `update` that actions or rejects it, or of a `defer`; never created or deleted by a Decision; `actioned` reopens (case 124) | [[rule-insights-schema]] |
        | Decision page | One page per Case in `wiki/decisions/`, slug `decision-case-<N>`, one list per kind present: `create`, `update`, `delete`, `defer`, body Context, Problem, Given, When; never indexed, reached through `deferred_by`, a History wikilink or `origin` | [[rule-decisions-schema]] |
        | Scripts | Page generation (fills `origin`, `slug`, `status`); cleanup (moves `archived` pages); lint (refs, schema, statuses, orphans); renderer (Rule body into the file it governs) | [[rule-harness]] |
        | Harness | Hooks, agents, skills rendered from `rules/` pages | [[rule-harness]] |
        | Hook | An event-triggered script behind a Rule page, the ledger writer on `Stop`, which reads the session's transcript back, keeps its `hi` window across midnight, and can block | [[rule-hook-registry]] |
        | `CLAUDE.md`, `case-schema.md`, `index.md` | The system prompt, the Render of `rule-claude-md`, whole — the description of the project, `rule-language` and `rule-agent-writing` in their markers (cases 59.8, 272, 288.3); the Case schema is the Render of `rule-case-protocol`, opened by the one rule, and it arrives with `/hi` together with the glossary (cases 273, 288); the map is read a section at a time — layout, routing, ledger, splitting, librarian | [[rule-claude-md]] |
        | `deferred_by` | On an Entity, Rule or Insight, the Decision pages whose `defer` targets it; set by `generate`, cleared by a `supersedes`, shown in the index line, followed by `ask-guppi` | [[rule-page-generation]] |
        | `origin` | The Decision that created or deleted the page, as `raw/<date>/<HHMM>/ledger.md#case-N` — the date form on older pages; kept when archived, never rewritten; `#case-N` is a grep target lint checks in `raw/` or in the archive (case 103.6) | [[rule-page-generation]] |
        | Entity / Rule (status) | `draft` / `built` / `archived`; `built` is computed once every Estimate passes, never by hand | [[rule-page-generation]] |
        | Decision, Lesson, Insight (status) | `current`/`superseded`/`archived`; `new`/`clustered`/`archived`; `open`/`actioned`/`archived`, a new Lesson reopens `actioned` unless a decision of its own session closed its cause (case 284.4) | [[rule-page-generation]] |
        | `archived` | Set by `delete`, or by the cascade of `guppi generate` — a superseded Decision, the lessons of an actioned Insight, an open Insight with no live child (case 104); `guppi cleanup` moves the file to `vault/archive/<sprint>/<date>/<HHMM>/<category>/` and brings it back on an `update` of `status`; `guppi archive` moves an applied session of `raw/` whole (case 100.1); never physical deletion | [[rule-cleanup]] |
        | Routing Table | (type × `ref` × category) to vault action, mechanical | [[rule-materialize]] |
        | Sprint | An Entity Leaf `entity-sprint-<id>` under the MOC `entity-sprint`, the sprint as a kind (case 241), whose Estimates are the Definition of done, whose `## Milestones` holds the Slices in order — the first with an open item is current — and whose `## Backlog` the items without a turn, each a wikilink or a plain line; `sprint.md` is its render, written by `guppi sprint` with one tick per item by the status of the page it names, the current milestone whole and the others one line (cases 209, 229); `/hi` takes the Frontier from the current milestone only | [[rule-sprint]] |
        | `brief.md` | The handover between sessions, written by the librarian — deferred items capped at 7, ranked by Insight severity then postponements, leaving out what the sprint page names — or by `/carry`, which conserves a Spec and keeps the previous list whole (case 200.2) | [[rule-brief]] |
        | Working files | `log.md` and page `History`, the feed of page changes by hook; `raw/`: `event_log.md` of the day and one folder per session, named by its `hi` time (case 73.1), with its ledger, yaml, Spec, Frontier and handoff, moved whole into the archive once applied (cases 100.1, 103.6); `tags.md`, ratified tags with Russian aliases | [[rule-raw-archive]] |
        | Documentation | The librarian's phase, the agent `librarian-guppi`: materialize, index check, synthesis, generate, cleanup, brief, close | [[rule-documentation]] |
        | Librarian | Clean context; the only writer to `wiki/`; reads handoff, yaml, indexes; one judgment, `create` to `update` on a duplicate; flags the rest | [[rule-documentation]] |
        | Session | Session Start, Plan Mode, Work Mode, End of Session | [[rule-session-start]] |
        | `/hi`, Frontier | Opens a working session and records `hi`; the open items it assembles (brief, sprint, issues, an unfinished plan, the ledger tail) in two lists, the kind of each by its source — Cases, the Plan Mode agenda, and Work, what needs no decision (case 268.2) | [[rule-skill-hi]] |
        | Ledger | The record of decisions (routing only), estimates and lessons (with text), written by the `Stop` hook into `raw/<date>/<HHMM>/ledger.md`, the session's folder (case 103.1) | [[rule-ledger-write]] |
        | Event log | The gitignored log of tool calls and commits of the day, written by hooks | [[rule-event-log]] |
        | Issue | Tracked on GitHub; never a page, a `ref` only | [[rule-github-issues]] |
        | Executable plan, Work Mode | The Spec as tasks with code, paths, checkboxes; subagents transcribe, a fork comes back as a Case | [[rule-work-mode]] |
        | Retro | `/retro`: an analysis of this session only — the frontier first, then every item ends as a lesson, a reading, a short defer (a Case of `context`, `problem`, `purpose` under `## Retro` in the Spec) or a handoff note; edits only finish ratified work; red tests are fixed or reverted into a patch in `raw/`; ends with a commit | [[rule-retro]] |
        | Handoff | `/handoff`, gated by `guppi gate` on a dirty tree: `handoff.md` from memory, then the librarian | [[rule-handoff]] |
  - slug: estimate-glossary-terms-defined
    type: estimate
    ref: entity-glossary
    kind: QA
    purpose: Every term names in where a live page that defines it, and no term stands twice
    method: one reading of the table by hand after the librarian's run, plus make lint — no ref finding on entity-glossary
    tags: [session, harness]
```

```tasks
- [x] create `entity-glossary` (Leaf, parent `entity-guppi`), the 49 rows above
- [x] create `estimate-glossary-terms-defined` (ref `entity-glossary`)
- [ ] read `estimate-glossary-terms-defined`: by hand after the librarian's run; `make lint` — no `ref` finding on `entity-glossary`
```

### Case 306.4 — `rule-glossary` and `estimate-glossary-renders-the-terms`

> **when:**
> The librarian, step 6 of the frame: `uv run guppi glossary`.

> **then:**
> `vault/wiki/glossary.md` is written: `# Glossary`, the line "Written by `guppi glossary` from the `## Terms` of `entity-glossary`; a term changes by an `update` of that page", then for each parent MOC of the pages in `where` a group `## [[<moc>]]` in the order of first appearance in the table (a page without a parent — a root MOC, or a placeholder not yet placed — under itself), in it `| term | meaning | where |` in the order of the table.
> **＋** A `where` with no live page, a row not of three columns, a term twice: one line on stderr, exit 1, the file is not written.
> **＋** The frame of the librarian has step 6: "Run `uv run guppi glossary`. It writes `vault/wiki/glossary.md` from the `## Terms` of `entity-glossary`. Every line on its stderr is a flag."
> **－** `index.md` is not read; no row that is not derived from the table.

```then
create:
  - slug: rule-glossary
    type: rule
    kind: Leaf
    purpose: Prevents glossary.md from drifting from the terms of entity-glossary, and a term from pointing at no page
    enforcement: check
    implementation_ref: [guppi/glossary.py, tests/test_glossary.py]
    governs: vault/wiki/glossary.md
    parent: rule-documentation
    applies_to: [entity-glossary]
    estimates: [estimate-glossary-renders-the-terms, estimate-glossary-checks-the-file, estimate-glossary-ticks-the-spec]
    tags: [harness, workflow, librarian, session]
    sections:
      Purpose: |
        Prevents `vault/wiki/glossary.md` from drifting from the terms of `entity-glossary`, and a term from pointing at no page. The glossary is a page — `entity-glossary`, a Leaf under `entity-guppi`, whose `## Terms` is a flat table `| term | meaning | where |`; `glossary.md` is not a document: `guppi glossary` writes it from that table, one group per parent MOC of the pages in `where` — a page without a parent, a root MOC or a placeholder not yet placed, under itself — in the order of first appearance, the rows in the order of the table; a `where` with no live page, a row of another shape or a term twice stops the write with a line on stderr. `governs` names the file, so the governed-files hook refuses a hand edit; a term changes by an `update` of `entity-glossary`. The librarian runs the script after `sprint`, before the brief. `guppi glossary --check` renders in memory and names the file when it differs, exit 1, writing nothing; `make lint` runs it after `sprint --check`. Once the plain `guppi glossary` wrote the file and exits 0, it ticks every unticked task line of an applied Spec that opens with a code span holding `guppi glossary` — the Spec's bookkeeping, no tick in the glossary itself (case 306).
  - slug: estimate-glossary-renders-the-terms
    type: estimate
    ref: rule-glossary
    kind: QA
    purpose: guppi glossary writes glossary.md from the Terms of entity-glossary, one group per parent MOC of where, and refuses a term with no page
    method: pytest tests/test_glossary.py, plus one reading of the rendered glossary.md after the librarian's run
    tags: [harness, workflow, librarian, session]
update:
  - slug: rule-documentation
    set: {children: [rule-materialize, rule-index-check, rule-synthesis, rule-page-generation, rule-cleanup, rule-raw-archive, rule-brief, rule-close, rule-sprint, rule-glossary]}
    replace:
      - old: "5. Run `uv run guppi sprint`. It writes `vault/wiki/sprint.md` from the sprint page by the statuses of this run. Every line on its stderr is a flag."
        new: "5. Run `uv run guppi sprint`. It writes `vault/wiki/sprint.md` from the sprint page by the statuses of this run. Every line on its stderr is a flag.\n\n6. Run `uv run guppi glossary`. It writes `vault/wiki/glossary.md` from the `## Terms` of `entity-glossary`. Every line on its stderr is a flag."
    change: step 6 of the frame — guppi glossary after sprint, before the brief; rule-glossary the tenth child (case 306.4)
  - slug: estimate-documentation-completes
    replace:
      - old: "it runs `uv run guppi render`, then `uv run guppi sprint`; every line"
        new: "it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi glossary`; every line"
    change: the frame's step 6, guppi glossary (case 306.4)
```

```tasks
- [x] create `rule-glossary` (parent `rule-documentation`, `applies_to` `entity-glossary`)
- [x] create `estimate-glossary-renders-the-terms` (ref `rule-glossary`)
- [x] update `rule-documentation`: `children` with `rule-glossary` last; one `replace` pair in the Render — step 6 after step 5
- [x] update `estimate-documentation-completes`: one `replace` pair inside the Criterion, `pending`
- [x] `guppi/glossary.py`: the render from `entity-glossary`, the groups by parent MOC, the refusals; `guppi/cli.py`: the command
- [x] `tests/test_glossary.py`: the render, the grouping, a `where` with no page, a row of another shape, a term twice
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] read `estimate-glossary-renders-the-terms`: `uv run pytest tests/test_glossary.py`; live — the librarian's run of this session, `glossary.md` read
- [ ] read `estimate-documentation-completes`: live — the librarian's run of this session, step 6 in `event_log.md`
```

### Case 306.5 — `estimate-glossary-checks-the-file`

> **when:**
> `uv run guppi glossary --check`, in `make lint` after `sprint --check`.

> **then:**
> The render in memory; a difference is one line `glossary: vault/wiki/glossary.md differs from entity-glossary`, exit 1, nothing written; equal — exit 0 and no output.
> **－** `--check` ticks nothing.

```then
create:
  - slug: estimate-glossary-checks-the-file
    type: estimate
    ref: rule-glossary
    kind: QA
    purpose: glossary --check names glossary.md when it differs from the render of entity-glossary, exit 1, and writes nothing
    method: pytest tests/test_glossary.py, plus make lint after the librarian's run — no glossary line
    tags: [harness, workflow, librarian, session]
update:
  - slug: rule-lint
    replace:
      - old: "`make lint` runs it after `render --check` and `sprint --check`; all three only report"
        new: "`make lint` runs it after `render --check`, `sprint --check` and `glossary --check`; all four only report"
    change: make lint runs glossary --check too (case 306.5)
  - slug: estimate-harness-pipeline
    replace:
      - old: "`make lint` is `render --check`, `sprint --check`, `guppi lint` (case 227); `rule-sprint` is a child of `rule-documentation`, not of `rule-harness`."
        new: "`make lint` is `render --check`, `sprint --check`, `glossary --check`, `guppi lint` (cases 227, 306.5); `rule-sprint` and `rule-glossary` are children of `rule-documentation`, not of `rule-harness`."
      - old: "in this order: the harness files against their pages, the sprint file against its page, then the pages."
        new: "in this order: the harness files against their pages, the sprint file against its page, the glossary file against its page, then the pages."
    change: two lines of the Criterion — glossary --check the third step of make lint (case 306.5; pre-spec)
```

```tasks
- [x] create `estimate-glossary-checks-the-file` (ref `rule-glossary`)
- [x] update `rule-lint`: one `replace` pair in the Purpose — `glossary --check` in `make lint`
- [x] update `estimate-harness-pipeline`: two `replace` pairs inside the Criterion, `pending`
- [ ] read `estimate-harness-pipeline`: `make test-harness`, then `make lint` by hand after the librarian's run — the four steps in order
- [x] `Makefile`: `lint` — `glossary --check` after `sprint --check`
- [x] `guppi/glossary.py`: `--check`; `tests/test_glossary.py`: differs, equal
- [x] read `estimate-glossary-checks-the-file`: `uv run pytest tests/test_glossary.py`, then `make lint` after the librarian's run
```

### Case 306.6 — `estimate-glossary-ticks-the-spec`

> **when:**
> `uv run guppi glossary` wrote the file and exits 0.

> **then:**
> In the `spec.md` of every unit under `raw/` whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi glossary` becomes `- [x]`; `--check` and an exit 1 tick nothing.
> **＋** The Case schema names the fourth ticker and the form of the line `- [ ] `uv run guppi glossary``.

```then
create:
  - slug: estimate-glossary-ticks-the-spec
    type: estimate
    ref: rule-glossary
    kind: QA
    purpose: glossary, once it wrote glossary.md and exits 0, ticks the guppi glossary lines of every Spec under raw/ whose yaml is applied whole
    method: pytest tests/test_glossary.py, plus one reading of this session's spec.md after the librarian's run
    tags: [harness, workflow, librarian, session]
update:
  - slug: rule-case-protocol
    replace:
      - old: "`render` and `sprint` the render and sprint lines (cases 226, 250, 270)"
        new: "`render`, `sprint` and `glossary` the render, sprint and glossary lines (cases 226, 250, 270, 306)"
      - old: "a sprint line `- [ ] `uv run guppi sprint`` — the command in the first code span"
        new: "a sprint line `- [ ] `uv run guppi sprint``, a glossary line `- [ ] `uv run guppi glossary`` — the command in the first code span"
    change: glossary is the fourth ticker of the Spec — the glossary lines (case 306.6)
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "a supersede from a later session leaves the earlier Spec as it is (299.1)."
        new: "a supersede from a later session leaves the earlier Spec as it is (299.1); the Spec paragraph names `glossary` as the fourth ticker, the glossary lines (306.6)."
    change: one line of the Criterion — glossary the fourth ticker (case 306.6)
```

```tasks
- [x] create `estimate-glossary-ticks-the-spec` (ref `rule-glossary`)
- [x] update `rule-case-protocol`: two `replace` pairs in the Render — the tickers and the line form
- [x] update `estimate-case-protocol-loaded`: one `replace` pair inside the Criterion, `pending`
- [x] `guppi/glossary.py`: `tick_command_lines(project_dir, "guppi glossary")` after the write; `tests/test_glossary.py`: the tick, none on `--check`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi glossary`: `vault/wiki/glossary.md`
- [x] read `estimate-glossary-ticks-the-spec`: `uv run pytest tests/test_glossary.py`; live — this Spec after the librarian's run
- [ ] read `estimate-case-protocol-loaded`: the `/hi` of the next session, by hand
```

### Case 306.7 — the Definition of done of Slice 3f: the glossary from `entity-glossary`

> **when:**
> The reading of `estimate-sprint-migration-rule-class-files-dissolved` at the close of Slice 3f.

> **then:**
> Its Criterion and `purpose` say "the glossary from `entity-glossary`" for "the glossary from `terms`"; the method — `glossary --check` exit 0 — stands.

```then
update:
  - slug: estimate-sprint-migration-rule-class-files-dissolved
    set: {purpose: "No Rule-class file at the close of Slice 3f — the schemas rendered from rule pages, the glossary from entity-glossary, index.md gone, the file route out of the scripts"}
    replace:
      - old: "`glossary.md` is written by `guppi glossary` from the `terms` field of the defining pages"
        new: "`glossary.md` is written by `guppi glossary` from the `## Terms` of `entity-glossary`"
    change: the glossary is rendered from entity-glossary, not from a terms field (case 306.7)
```

```tasks
- [x] update `estimate-sprint-migration-rule-class-files-dissolved`: `purpose` and one `replace` pair inside the Criterion, `pending`
```

## Deferred

## Case 307 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b — `rule-work-mode` (Work Mode: the Spec as tasks with code, the ticked boxes, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads`) and `rule-subagent-guppi` (what a subagent may do, the fork that comes back as a Case) — two `draft` placeholders, deferred seventeen times, the last by 303. This session took themes 1–3 of Slice 3f (304, 305, 306): the six schemas as rule pages, the edge Rule → Entity, the glossary as an Entity under `entity-guppi`; `rule-work-mode` is now the `where` of the term Work Mode in `entity-glossary`. Themes 4–6 of the Slice stay on the sprint page for the next session; they have no page and take no defer.

> **problem:**
> The person closes this Plan Mode and goes to pre-spec; Slice 3b waits behind Slice 3f, the eighteenth defer. The lines of 293 still bear on it: a subagent loads `CLAUDE.md` and not the glossary (288.1), and `guppi recall` brings the session's load back after a compaction (287) — the rule of Work Mode is written with both.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes on code, tests, migrations and by-hand checks in spec.md (the readings are generate's since case 270, the render and sprint lines in the form of case 279.1, the glossary lines since case 306.6), the test of each Estimate written first and turned green, the sentence of insight-workflow-code-live-before-the-page-it-reads on a check that reads a page the same Spec changes; after Slice 3f
  - slug: rule-subagent-guppi
    type: rule
    purpose: what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; a subagent loads CLAUDE.md and no glossary (case 288.1); with rule-work-mode, after Slice 3f
```
