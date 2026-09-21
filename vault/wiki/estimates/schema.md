# Estimate — page schema

`wiki/estimates/schema.yaml`

Three blocks: **properties**, **body**, **history**. One schema for both kinds; sections that do not apply are omitted rather than left empty.

An Estimate is the evidence. On a Rule it is a test that the guard works; on an Entity it is a reading of the whole, which no single case can break. Which of the two it is, the prefix of `target` says; the agent does not choose (case 240.3).

An Estimate is one promise, one way to check it and the last result with its date (case 182). It is always a Leaf — never inline on another page, never a MOC. Grouping is what the parent Entity's recursion already does. One action (`when`) — one Estimate; the ＋/－ lines stay in its `then` while one run checks them; a line with a test or a reading of its own is split off, and the axis of the split is the promise, not the method.

## Properties

| Field | Required | Values / format | Purpose |
|---|---|---|---|
| `type` | yes | `estimate` | Page category. |
| `kind` | yes | `QA` \| `Research` | QA: the expected result is known in advance and checked against a stated criterion. Research: the result is not known, and finding it produces new content — on an Entity only, since a Rule has its criterion by definition; `failed` on a Research Estimate means the finding does not serve the purpose the Estimate was made for — no answer, or the answer "not this way" — which of the two, the person says in the estimate line; both are debt, a Case on a changed approach or archival; when a bar grows out of the finding, it becomes a QA Estimate or a Rule (case 240.3); its `then` is a question, its Result the finding. Reading a known criterion by eye is QA by hand, not Research. |
| `status` | yes | `pending` \| `passed` \| `failed` | Short state, from a fixed list. The narrative belongs in the body. |
| `target` | yes | quoted wikilink `"[[slug]]"` of an Entity or Rule | The page with a contract this verifies; the scripts read the slug through the brackets (case 148.2); a Lesson or an Insight has no Estimate (case 53.1). Written by the script from the ledger. Without it the cascade — an Entity is `built` only once all its Estimates pass — cannot be computed. |
| `purpose` | no | one line | The promise, for the list on the target page: the reader of a rule sees its Estimates by `purpose` and opens only the touched ones. Written from the Case on every page born since case 193; absent on the older pages until their recut, counted by lint as `unmigrated` (case 202). |
| `method` | no | one line | How the promise is checked: the test command (`make test-x`, `pytest tests/test_x.py`); or where and when it is read by hand — a live reading of a session start, the brief of a librarian's run; or, for Research, what is measured. Written from the Case since case 193. |
| `checked` | no | date | The date of the last reading: the date the Result opens with, else the date of the reading's unit; written by `generate` on every reading (case 201.1). |
| `origin` | yes | `raw/YYYY-MM-DD/HHMM/ledger.md#case-N` (the date form, `raw/YYYY-MM-DD/ledger.md#case-N`, on pages born before 2026-09-13; case 103.6) | The ratified decision that created it. |
| `sprint` | yes | sprint id | |
| `created` | yes | date | |
| `tags` | yes | list | Chosen at the vault query before the Case, ratified in the Case. |

A `failed` Estimate is debt, not an endpoint: its target stays `draft` and the librarian surfaces it in `brief.md` until a human decides. Absent a decision to fix, the default is archival — something that cannot pass its own criterion should not sit in the vault pretending to be work in progress.

### Fields deliberately absent

- **`verified_at`** — `checked` takes its place (case 182, point 5): the date of the last reading, so lint can one day catch a stale check.
- **`blocking`** — not yet. The distinction between a QA failure (blocks the build) and a Research non-result (may be a fine outcome) is currently carried by `kind` plus human judgment at the brief.
- **`severity`** — Estimates do not accumulate the way Insights do.
- **`retry_count`** — a check that keeps failing is a Lesson, not a counter.

## Body

| Section | Required | Content |
|---|---|---|
| `## Criterion` | yes | The promise, written once: the `given`, `when` and `then` of one Case, verbatim with their operands, as `Given:`, `When:`, `Then:`. The Case that creates the Estimate writes it; an `update` that changes the promise replaces it whole and sets the page `pending`; an `update` that names a part alone — a field, a `replace` pair — keeps it, and a pair inside it sets `pending` (case 296); nothing is appended and no `### case N` block exists (case 193; the blocks of the shape before it stand on the older pages until their recut, counted by lint as `unmigrated`, case 202). The Criterion that was replaced stays in the Spec of the session that wrote it, reached by `origin`, and in History. For Research the `then` may legitimately be broad ("determine whether we stay inside the latency budget"); for QA it should be exact. |
| `## Result` | no | Omitted while `pending`. Its first line is the date of the reading and the command — `make test-x`, `pytest tests/test_x.py` — or the place of a live reading; the result follows (case 199). For QA usually one line more. For Research this is the substance of the page — findings, numbers, the conclusion drawn. |
| `## Context` | no | The shape before case 193: the `problem` of the Case that made the Estimate, written once. Not written to a new page — the Case is reached by `origin`; dropped by the `update` that sets `method` (case 211). |
| `## Method` | no | The shape before case 193: the `method` of the Case as a section. On a new page `method` is a field; the `update` that sets `method` drops the section, and a recut — `sections: Criterion` on a page without the field — is refused by `generate` unless `set` carries `method` (case 211). |

The two kinds sit at opposite ends of the same schema: QA puts its weight on `Criterion` and treats `Result` as a formality, Research often has a loose `Criterion` and carries everything in `Result`. That is why unused sections are omitted rather than filled with placeholder text.

**`Result` is overwritten, not appended.** It is about one run of one check: a test that passed, broke and was fixed leaves one current result; the sequence of changes is what History is for. Same for Research: the page states what we currently believe, and History records that the belief changed. **`Criterion` is replaced, not appended:** a rule changes → the Estimate the Case names goes `pending` → the test or the reading → `passed`.

## History

Appended by hook, never by an agent. Always the last section.

```
## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-2
- 2026-09-08 status: pending → passed
- 2026-09-19 status: passed → failed
- 2026-09-19 status: failed → passed
```

## Examples

### QA

```markdown
---
type: estimate
kind: QA
status: passed
target: "[[entity-discount-new-client]]"
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
```

### Research

```markdown
---
type: estimate
kind: Research
status: passed
target: "[[entity-cart]]"
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
```
