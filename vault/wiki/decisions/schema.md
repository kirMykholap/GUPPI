# Decision — page schema

`wiki/decisions/schema.yaml`

Every page has three blocks: **properties** (frontmatter), **body** (per-category sections), **history** (appended by hook). This is the schema for Decision.

## Properties

| Field | Required | Values / format | Purpose |
|---|---|---|---|
| `type` | yes | `decision` | Page category. Fixed for this schema. |
| `kind` | yes | `create` \| `update` \| `delete` \| `defer` | The decision itself. Together with `ref` presence, drives routing. |
| `status` | yes | `current` \| `superseded` \| `archived` | Lifecycle of this page. What lint reads, and what archival acts on. Not the state of the work — that lives on the target page. |
| `target_category` | yes | `entities` \| `rules` \| `estimates` \| `lessons` | Where the resulting page belongs. Explicit, so the generation script never infers a folder from a slug prefix. |
| `target_slug` | yes | slug | The page this decision acts on. For `create`, the name of the new page. |
| `ref` | no | slug | Parent MOC, for a `create` that adds a child. Omitted for `update`/`delete` — `target_slug` is already unambiguous. |
| `origin` | yes | `raw/YYYY-MM-DD/ledger.md#case-N` | Where this was ratified. `raw/` is archived with the session; the pointer stays valid into the archive. |
| `sprint` | yes | sprint id | Cheap slice of "what did we decide this sprint" without parsing dates. |
| `created` | yes | date | |
| `source` | no | external id, e.g. `issue-84` | External provenance. Traceability only — never affects routing. |
| `supersedes` | no | decision slug | This decision overrides an earlier one. |
| `superseded_by` | no | decision slug | Back-reference, written by the script. Without it, telling whether a decision still stands would mean scanning everything that came after it. |
| `tags` | yes | list | Chosen during pre-task, ratified in the Case. |

### Slug

The slug carries the meaning — `decision-create-cart`, not `decision-2026-09-08-01`. **The main agent writes it in the Case**, so the human ratifies the name along with everything else, and pre-task checks it for collisions and for near-identical existing decisions.

Because the slug already says what the decision was, there is no `summary` field — it would only restate the slug in prose.

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
| `## Now` | yes | How things worked before, including the pre-task result — what already existed, what conflicted, what sat in `draft`. |
| `## Problem` | yes | What required a decision. |
| `## Then` | yes | What was decided and what follows. If the human reshaped the proposal, this holds the reshaped version. |
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
kind: create
status: current
target_category: entities
target_slug: entity-cart
origin: raw/2026-09-08/ledger.md#case-1
sprint: 2026-Q3-s4
created: 2026-09-08
source: issue-84
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
Create `entity-cart` as a MOC. Four children follow, each ratified separately: add item,
change quantity, remove item, total. Cross-cutting estimate on the parent: the cart
renders within 200ms.

## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
```
