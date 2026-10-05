---
type: rule
kind: Leaf
purpose: Prevents an Estimate page from carrying a field or section outside the shape lint checks, or lacking one it needs
status: built
enforcement: render
governs: vault/wiki/estimates/schema.yaml
render_mode: full
parent: "[[rule-page-schemas]]"
estimates: ["[[estimate-estimates-schema-checked]]"]
origin: raw/2026-09-22/0014/ledger.md#case-304.4
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Purpose

Prevents an Estimate page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/estimates/schema.yaml`, the file `guppi lint` reads for every page of `wiki/estimates/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8).

## Render

<!-- rule-estimates-schema -->
type: estimate
description: |
  Three blocks: properties, body, history. One schema for both kinds; sections that do not apply are omitted rather than left empty.

  An Estimate is the evidence. On a Rule it is a test that the guard works; on an Entity it is a reading of the whole, which no single case can break. Which of the two it is, the prefix of `target` says; the agent does not choose (case 240.3).

  An Estimate is one promise, one way to check it and the last result with its date (case 182). It is always a Leaf — never inline on another page, never a MOC. Grouping is what the parent Entity's recursion already does. One action (`when`) — one Estimate; the ＋/－ lines stay in its `then` while one run checks them; a line with a test or a reading of its own is split off, and the axis of the split is the promise, not the method.

  `purpose`, `method` and `checked` are the fields of the model of case 182: one line each. `method` is required on every page (case 506.1); `purpose` is written from the Case and stays optional, since some older pages carry none; `checked` is written by `generate` on every reading (case 201.1). `target` names an Entity or a Rule; lint reports any other category (case 53.1).

  A `failed` Estimate is debt, not an endpoint: its target stays `draft` and the librarian surfaces it in `brief.md` until a human decides. The person may decide to close it: a Case then sets it `passed` or `failed` by that decision, its Criterion written back unchanged (case 669.16). Absent a decision to fix, the default is archival — something that cannot pass its own criterion should not sit in the vault pretending to be work in progress.

  Fields deliberately absent. `verified_at` — `checked` takes its place (case 182, point 5): the date of the last reading, so lint can one day catch a stale check. `blocking` — not yet. The distinction between a QA failure (blocks the build) and a Research non-result (may be a fine outcome) is currently carried by `kind` plus human judgment at the brief. `severity` — Estimates do not accumulate the way Insights do. `retry_count` — a check that keeps failing is a Lesson, not a counter, unless the person closes it by decision (case 669.16).

  The two kinds sit at opposite ends of the same schema: QA puts its weight on `Criterion` and treats `Result` as a formality, Research often has a loose `Criterion` and carries everything in `Result`. That is why unused sections are omitted rather than filled with placeholder text.

  `Result` is overwritten, not appended. It is about one run of one check: a test that passed, broke and was fixed leaves one current result; the sequence of changes is what History is for. Same for Research: the page states what we currently believe, and History records that the belief changed. `Criterion` is replaced, not appended: a rule changes → the Estimate the Case names goes `pending` → the test or the reading → `passed`.
properties:
  required: [type, kind, status, target, method, origin, sprint, created, tags]
  optional: [purpose, checked]
  values:
    kind: [QA, Research]
    status: [pending, passed, failed]
body:
  required: ["## Criterion", "## History"]
  optional: ["## Result"]
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
    optional; one line. The promise, for the list on the target page: the reader of a rule sees its Estimates by `purpose` and opens only the touched ones. Written from the Case; some older pages carry none, and lint does not ask for it (case 506.1).
  method: |
    required; one line. How the promise is checked, in one of the four forms lint classifies: a `make <target>` of the Makefile; the word `pytest`; a path under `tests/`; or the words `by hand` — the one spelling of a reading — with where and when it is taken, a session start, the brief of a librarian's run. A reading names its moment by its kind — a `/handoff`, a run of `/box`, a compaction — and any such moment after the render counts, in this session or in an earlier one; the word "first" stands only for an event that has never happened. A reading by hand tied to the first of something after the render or after the change is a finding of the class `moment` of lint and a finding of pre-spec, judged by one predicate of `guppi/lint.py` (case 613.1). Naming a form is not enough by itself: a path under `tests/` must exist and a `make <target>` must stand in the Makefile. On the Estimate of a MOC the form is a `make <target>` of the Makefile alone — there `pytest` or a path by itself earns a finding, and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a target; on a MOC with `render_mode: full` the Estimate of a child with `enforcement: render` is not counted, since that child's Render is part of the parent's file and its Estimate promises the child's own behaviour (cases 378.5, 459). A `method` that names none of the forms earns a finding of the class `method`. A page without the field earns the `schema` finding `missing field method` (case 506.1). For `Research` what is measured stands beside one of the forms, never instead of one. Written from the Case since case 193 (case 350).
  checked: |
    optional; date. The date of the last reading, or of the person's decision that set the status, which the Case writes (case 669.16): the date the Result opens with, else the date of the reading's unit; written by `generate` on every reading (case 201.1).
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
    required. The promise, written once: the `when` and `then` of one Case, verbatim with their operands, as `When:`, `Then:` — no `Given:`: the frame of the Case stays in its Case file and in the Spec (cases 378.2, 513). The Case that creates the Estimate writes it; an `update` that changes the promise replaces it whole and sets the page `pending`; an `update` that names a part alone — a field, a `replace` pair outside it — keeps it; a pair inside it is refused, a changed promise is a Criterion replaced whole (case 378.4); nothing is appended and no `### case N` block exists (case 193). The Criterion that was replaced stays in the Spec of the session that wrote it, reached by `origin`, and in History. For Research the `then` may legitimately be broad ("determine whether we stay inside the latency budget"); for QA it should be exact.
  "## Result": |
    optional; required on `passed` and `failed`. Omitted while `pending`. Its first line is the date of the reading and the command — `make test-x`, `pytest tests/test_x.py` — or the place of a live reading; the result follows (case 199). On a status set by the person's decision, the first line is the date and the place of the decision — `the person's decision, case N` — and the last reading the page held follows (case 669.16). For QA usually one line more. For Research this is the substance of the page — findings, numbers, the conclusion drawn.
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

    When:
    A client with zero completed orders asks for a discount; the discount pipeline runs every rule in order and takes the first that applies.

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

    When:
    A buyer opens a cart of 10, 50 or 200 line items against a seeded database.

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

## History

- 2026-09-22 created · [[decision-case-304.4]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-23 updated: the description of method names the four forms, what lint checks besides naming one, and the four triggers of the old shape (case 350, supersedes 330.2, 336 and 343) · [[decision-case-350]]
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 status: draft → built · cascade
- 2026-09-23 updated: the Criterion holds When and Then (case 378.2) · [[decision-case-378.2]]
- 2026-09-23 updated: a Criterion changes only whole (case 378.4) · [[decision-case-378.4]]
- 2026-09-27 updated: the method of a MOC's Estimate: the Estimates of a render child of a full MOC are not counted (case 459) · [[decision-case-459]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 updated: method required, purpose optional; the old shape, the unmigrated count, the recut and the Given: of older pages gone from the schema (case 506.1) · [[decision-case-506.1]]
- 2026-09-29 deferred · [[decision-case-519]]
- 2026-09-29 status: draft → built · cascade
- 2026-09-29 defer by decision-case-519 superseded · [[decision-case-521.3]]
- 2026-09-29 updated: the description of ## Criterion says the frame of a Case stays in its Case file and the Spec; the defer of case 519 retired (case 521.3) · [[decision-case-521.3]]
- 2026-09-30 status: built → draft · cascade
- 2026-10-02 status: draft → built · cascade
- 2026-10-03 updated: a reading names its moment by its kind; a reading by hand tied to the first moment after the render or the change is a finding of lint and pre-spec (case 613.1) · [[decision-case-613.1]]
- 2026-10-05 updated: the person may close an Estimate by decision: its Result opens with the date and the place of the decision, and checked is that date (case 669.16) · [[decision-case-669.16]]
