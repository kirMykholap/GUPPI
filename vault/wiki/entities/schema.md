# Entity — page schema

`wiki/entities/schema.yaml`

Three blocks: **properties**, **body**, **history**. One schema for both kinds; sections that do not apply are omitted.

Entity is the thing that gets built. It is recursive: a MOC holds children, a Leaf holds behaviour. Depth is not fixed in advance — it follows the atomicity rule and nothing else.

## Properties

| Field | Required | Values / format | Purpose |
|---|---|---|---|
| `type` | yes | `entity` | Page category. |
| `kind` | yes | `MOC` \| `Leaf` | MOC: no direct criteria, holds children. Leaf: direct behaviour of its own. |
| `purpose` | yes | one line | Why this exists. Lives in properties, not the body, because `entities.index` is built from it and must stay one line per page. The body expands on it; the property stays short. |
| `status` | yes | `draft` \| `built` \| `archived` | Flat list, like every other category. `built` is set by lint, not by hand: an Entity is built only once all of its Estimates pass — a graph property. |
| `parent` | Leaf | slug | The MOC above it. Written by the script from the ledger's `ref`. |
| `children` | MOC | list of slugs | Functional requirements, each its own page. Written by the script. |
| `estimates` | yes | list of slugs | On a Leaf: checks of its own behaviour. On a MOC: cross-cutting checks that belong to all children and to none individually — non-functional requirements live here. |
| `deferred_by` | no | list of decision slugs | The Decision pages whose `defer` targets this page. Written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; the index line carries it (case 52.3). |
| `code_ref` | no | list of paths | Code, commits or PRs. Allowed on both kinds: a Leaf points at files, a MOC may point at the directory or module it corresponds to. |
| `origin` | yes | `raw/YYYY-MM-DD/HHMM/ledger.md#case-N` (the date form, `raw/YYYY-MM-DD/ledger.md#case-N`, on pages born before 2026-09-13; case 103.6) | The ratified decision that created it. |
| `sprint` | yes | sprint id | |
| `created` | yes | date | |
| `tags` | yes | list | Chosen at pre-task, ratified in the Case. |

### Slug

Meaningful, written by the main agent in the Case and checked by pre-task for collisions. The decision that created it is `decision-case-<N>`, reachable through the page's `origin`; the relationship is readable without opening either page.

### `built` is not a field you set

`status: built` follows from every Estimate having passed. Lint computes it. Writing it by hand would create a second source of truth about whether the work is done.

## Body

| Section | Required | Content |
|---|---|---|
| `## Purpose` | yes | Expands the `purpose` property: what problem this solves, why it exists in this shape. |
| `## How it works` | no | How it is built. For a Leaf, the mechanics. For a MOC, the principle by which it splits into children — why *these* children and not some other cut. Omitted while `draft`. |
| `## Estimates` | yes | Where the script places links to the Estimate pages. |
| `## Children` | MOC | Where the script places links to child Entities. |
| `## Parent` | Leaf | Where the script places the link upward. |
| `## Code` | no | Where the script places `code_ref` links. |

### `How it works` is unratified, and that is fine

Purpose and criteria are ratified in the Case, before anything is built. `How it works` describes what was actually built, so it can only be written afterwards — by the main agent at handoff, which is the only point where someone has watched the tasks close.

The boundary: **it describes structure, it does not introduce claims.** New statements about what the thing is for, or what counts as correct, belong in a Case. If writing this section reveals that what was built differs from what was decided, that is not a wording fix — it is a flag for `brief.md`.

## Constraints

Constraints are not an Entity section. A constraint that can be violated and noticed is a **Rule** with a mandatory QA Estimate — "synchronous API only" becomes a linter that catches `async` in that module. A constraint that cannot be checked by anything is a sentence in `How it works`, not a structure.

This keeps Rule meaning one thing: something that can be broken, where breaking it will be detected.

## History

Appended by hook, never by an agent. Always the last section.

## Examples

### MOC

```markdown
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

## Estimates
- [[estimate-cart-render-time]]

## Children
- [[entity-cart-add]]
- [[entity-cart-quantity]]
- [[entity-cart-remove]]
- [[entity-cart-total]]

## Code
- `src/cart/`

## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
```

### Leaf

```markdown
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

## Estimates
- [[estimate-new-client-discount]]

## Parent
- [[entity-discount-rules]]

## Code
- `src/discounts/new_client.py`

## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-2
- 2026-09-09 status: draft → built
```
