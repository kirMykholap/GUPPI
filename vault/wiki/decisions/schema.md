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
| `kind` | yes | list of `create` \| `update` \| `delete` \| `defer` | One item per ledger line of the Case, in ledger order; aligned by position with `target_slug`. Two lists of scalars, not a list of objects, so Obsidian shows them as lists and links (case 52.1). |
| `target_slug` | yes | list of slugs | The slug of each ledger line, at the same position as its `kind`: a page, or a Rule-class file by its ledger slug (`case-schema`, `rules-schema-yaml`). The category is derived from the slug prefix or the Rule-class map and never written; the parent of a `create` is on the child page as `parent` or `target`. |
| `source` | no | list | External ids the Case's lines carried (`{source:...}`), traceability only. |
| `supersedes` | no | list of decision slugs | Earlier Cases this one overrides, from the ledger's `{supersedes:case N}`. |
| `superseded_by` | no | list of decision slugs | Back-references, written by the script. |
| `origin` | yes | `raw/YYYY-MM-DD/ledger.md#case-N` | Where this was ratified. The folder also holds the Spec with the Case. `raw/` stays in place; it is not archived with the session. |
| `sprint` | yes | sprint id | Cheap slice of "what did we decide this sprint" without parsing dates. |
| `created` | yes | date | |
| `tags` | yes | list | The union of the targets' tags, as ratified in the Case. |

### Slug

`decision-case-<N>`: `decision-case-18.1`. Mechanical, because the script writes the page
and may not name anything; unique, because a Case id is. Nothing searches Decision pages,
so the slug needs no meaning beyond the Case it points back at. A Decision is reached by
reference only: from a target page's `deferred_by` (a deferred decision, case 52.3), from
the `[[decision-case-N]]` wikilink of a History line (case 52.4), or by the case id a
`supersedes` carries.

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
| `## Problem` | yes | What required a decision. On a defer, what is unresolved. |
| `## Given` | when any `kind` is not `defer` | The Case's `given`: how things worked before, the pre-task result included — what already existed, what conflicted, what sat in `draft`. The short form of Retro (a defer-only Case) has none (case 56). |
| `## When` | when any `kind` is not `defer` | The Case's `when`: the action that triggers the behaviour. What was decided (`then`) lives on the target pages, not here. |
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
kind: [create, create]
target_slug: [entity-cart, estimate-cart-render-time]
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
Pre-task found no cart page and no overlapping purpose. `entity-checkout` exists and will
be affected. Nothing in `draft` covers this either.

## When
A buyer opens the cart.

## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
```
