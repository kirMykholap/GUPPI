# Estimate — page schema

`wiki/estimates/schema.yaml`

Three blocks: **properties**, **body**, **history**. One schema for both kinds; sections that do not apply are omitted rather than left empty.

An Estimate is always a Leaf — never inline on another page, never a MOC. Grouping is what the parent Entity's recursion already does.

## Properties

| Field | Required | Values / format | Purpose |
|---|---|---|---|
| `type` | yes | `estimate` | Page category. |
| `kind` | yes | `QA` \| `Research` | QA: the expected result is known in advance and checked against a stated criterion. Research: the result is not known, and finding it produces new content. |
| `status` | yes | `pending` \| `passed` \| `failed` | Short state, from a fixed list. The narrative belongs in the body. |
| `target` | yes | slug | The Entity or Rule this verifies. Written by the script from the ledger. Without it the cascade — an Entity is `built` only once all its Estimates pass — cannot be computed. |
| `origin` | yes | `raw/YYYY-MM-DD/ledger.md#case-N` | The ratified decision that created it. |
| `sprint` | yes | sprint id | |
| `created` | yes | date | |
| `tags` | yes | list | Chosen at pre-task, ratified in the Case. |

A `failed` Estimate is debt, not an endpoint: its target stays `draft` and the librarian surfaces it in `brief.md` until a human decides. Absent a decision to fix, the default is archival — something that cannot pass its own criterion should not sit in the vault pretending to be work in progress.

### Fields deliberately absent

- **`verified_at`** — not yet. It would let lint catch a stale check (`code_ref` newer than the last verification), but that is a refinement to add when the need is real.
- **`blocking`** — not yet. The distinction between a QA failure (blocks the build) and a Research non-result (may be a fine outcome) is currently carried by `kind` plus human judgment at the brief.
- **`severity`** — Estimates do not accumulate the way Insights do.
- **`retry_count`** — a check that keeps failing is a Lesson, not a counter.

## Body

| Section | Required | Content |
|---|---|---|
| `## Context` | yes | What is being checked and why this check matters. Not a restatement of the target's `purpose` — that is on the target page. |
| `## Criterion` | yes | What counts as passing, as ratified in the Case. For Research this may legitimately be broad ("determine whether we stay inside the latency budget"); for QA it should be exact. |
| `## Method` | yes | How it is checked. QA: which test, where it lives. Research: what is being measured or investigated, and how. |
| `## Result` | no | Omitted while `pending`. For QA usually one line. For Research this is the substance of the page — findings, numbers, the conclusion drawn. |

The two kinds sit at opposite ends of the same schema: QA puts its weight on `Criterion` and treats `Result` as a formality, Research often has a loose `Criterion` and carries everything in `Result`. That is why unused sections are omitted rather than filled with placeholder text.

**`Result` is overwritten, not appended.** A test that passed, broke and was fixed leaves one current result; the sequence of changes is what History is for. Same for Research: the page states what we currently believe, and History records that the belief changed.

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
target: entity-discount-new-client
origin: raw/2026-09-08/ledger.md#case-2
sprint: 2026-Q3-s4
created: 2026-09-08
tags: [discounts, pricing]
---

## Context
New-client discount is the only rule that returns zero rather than a positive percentage,
so it is the one most likely to be broken by a change to the discount pipeline.

## Criterion
A client with zero completed orders receives a 0% discount.

## Method
Unit test `test_new_client_discount` in `tests/discounts/test_new_client.py`.

## Result
Passing.

## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-2
- 2026-09-08 status: pending → passed
```

### Research

```markdown
---
type: estimate
kind: Research
status: passed
target: entity-cart
origin: raw/2026-09-08/ledger.md#case-1
sprint: 2026-Q3-s4
created: 2026-09-08
tags: [cart, performance]
---

## Context
The cart is a MOC with four children; render time is cross-cutting and belongs to the
parent, not to any single child.

## Criterion
Determine whether the cart can render within 200ms, and what dominates the time if not.

## Method
Measure render time under 10, 50 and 200 line items, against a seeded database.

## Result
Renders in 140ms at 50 items. At 200 items it reaches 380ms, dominated by per-item
price recalculation rather than by rendering. The 200ms target holds for realistic
cart sizes; above roughly 120 items it does not.

## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
- 2026-09-11 status: pending → passed
```
