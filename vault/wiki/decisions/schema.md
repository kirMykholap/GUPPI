# Decision — page schema

`wiki/decisions/schema.yaml`

Every page has three blocks: **properties** (frontmatter), **body** (per-category sections), **history** (appended by hook). This is the schema for Decision.

## Properties

One page per Case, however many ledger lines the Case produced.

| Field | Required | Values / format | Purpose |
|---|---|---|---|
| `type` | yes | `decision` | Page category. Fixed for this schema. |
| `case` | yes | case id, e.g. `18.1` | The Case this page records. |
| `status` | yes | `current` \| `superseded` \| `archived` | Lifecycle of this page, not of the work. `superseded` once a later Case names it in `supersedes`. |
| `targets` | yes | list of `{kind, category, slug, ref?, source?, path?}` | One item per ledger line of the Case. `kind`: `create` \| `update` \| `delete` \| `defer`. `category`: the folder the effect lands in (`entities`, `rules`, `estimates`, `lessons`, `insights`), or `file` with `path` for a Rule-class file. `ref`: the parent for a `create` that adds a child. `source`: an external id, traceability only. The category is explicit on the page; the script derives it from the slug prefix, which pre-task guards. |
| `supersedes` | no | list of decision slugs | Earlier Cases this one overrides, from the ledger's `{supersedes:case N}`. |
| `superseded_by` | no | list of decision slugs | Back-references, written by the script. |
| `origin` | yes | `raw/YYYY-MM-DD/ledger.md#case-N` | Where this was ratified. The folder also holds the Spec with the Case. `raw/` stays in place; it is not archived with the session. |
| `sprint` | yes | sprint id | Cheap slice of "what did we decide this sprint" without parsing dates. |
| `created` | yes | date | |
| `tags` | yes | list | The union of the targets' tags, as ratified in the Case. |

### Slug

`decision-case-<N>`: `decision-case-18.1`. Mechanical, because the script writes the page
and may not name anything; unique, because a Case id is. Nothing searches Decision pages,
so the slug needs no meaning beyond the Case it points back at. The one lookup that
happens — which decision a new one supersedes — goes by the case id the ledger line
already carries.

### Fields deliberately absent

- **`ratification`** — a Decision page cannot exist without it. The Case does not close, no ledger line is written, no page is generated. A field with one possible value carries no information; the fact is recorded by the page existing and by `origin`.
- **`recommend`** — if the human accepted the proposal it became `Then`; if they changed it, `Then` holds the change. Either way the original is conversation history, recoverable from the archived ledger.
- **`last_updated`** — a decision is not edited. Only `status` and `superseded_by` ever change, and both are dated in History.
- **`authority`** — dropped. It overlapped with tags on one reading and with `ref` on the other. If a real need appears later, it comes back as a ratified decision.

## Body

The Case that produced it, minus what belongs to the conversation rather than the decision.

| Section | Required | Content |
|---|---|---|
| `## Context` | yes | What this is about. |
| `## Now` | yes | The Case's `given`: how things worked before, the pre-task result included — what already existed, what conflicted, what sat in `draft`. |
| `## Problem` | yes | What required a decision. |
| `## Then` | yes | The Case's `when` and `then`: what was decided and what follows. If the human reshaped the proposal, this holds the reshaped version. |
| `## Note` | no | Only when ratification was non-trivial: a reservation, a condition, a rejected alternative worth remembering. Omit when the answer was simply yes. |

## History

Appended by hook, never by an agent. Always the last section, so `tail` reads it without loading the page.

```
## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
- 2026-09-15 superseded by decision-split-cart-total
```

## Example

```markdown
---
type: decision
case: "1"
status: current
targets:
  - {kind: create, category: entities, slug: entity-cart}
  - {kind: create, category: estimates, slug: estimate-cart-render-time, ref: entity-cart}
origin: raw/2026-09-08/ledger.md#case-1
sprint: 2026-Q3-s4
created: 2026-09-08
tags: [cart, checkout]
---

## Context
The site has checkout but no cart — items go straight from the catalogue to payment.

## Now
Pre-task found no cart page and no overlapping purpose. `entity-checkout` exists and will
be affected. Nothing in `draft` covers this either.

## Problem
Buyers cannot review an order before paying.

## Then
A buyer opens the cart.

The cart lists the order and renders within 200ms.
**＋** Four children follow, each ratified separately: add item, change quantity, remove
item, total.

## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
```
