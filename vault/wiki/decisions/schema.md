# Decision — page schema

`wiki/decisions/schema.yaml`

Every page has three blocks: **properties** (frontmatter), **body** (per-category sections), **history** (appended by hook). This is the schema for Decision.

## Properties

One page per Case, however many ledger lines the Case produced.

| Field | Required | Values / format | Purpose |
|---|---|---|---|
| `type` | yes | `decision` | Page category. Fixed for this schema. |
| `case` | yes | case id, e.g. `18.1` | The Case this page records. |
| `status` | yes | `current` \| `superseded` \| `archived` | Lifecycle of this page, not of the work. `superseded` once a later Case names it in `supersedes`, and `archived` the moment the cascade of `generate` meets it so: a superseded Decision no longer describes the present (case 104.1). |
| `create` | one of the four | list of quoted wikilink `"[[slug]]"` | The slugs of the Case's `create` lines, in ledger order: a page, or a Rule-class file by its ledger slug (`case-schema`, `rules-schema-yaml`). One list per kind present, in the order create, update, delete, defer; a kind with no line is absent. Lists of quoted wikilinks for page slugs, a Rule-class slug bare, so Obsidian shows them as links (case 148.2); the kind of every target is its key (case 59.4, replacing the aligned `kind` and `target_slug` of case 52.1). The category is derived from the slug prefix or the Rule-class map and never written; the parent of a `create` is on the child page as `parent` or `target`. |
| `update` | one of the four | list of quoted wikilink `"[[slug]]"` | The slugs of the Case's `update` lines, in ledger order. |
| `delete` | one of the four | list of quoted wikilink `"[[slug]]"` | The slugs of the Case's `delete` lines, in ledger order. |
| `defer` | one of the four | list of quoted wikilink `"[[slug]]"` | The slugs of the Case's `defer` lines, in ledger order; each target carries this page in `deferred_by`. |
| `source` | no | list | External ids the Case's lines carried (`{source:...}`), traceability only. |
| `supersedes` | no | list of decision quoted wikilink `"[[slug]]"` | Earlier Cases this one overrides, from the ledger's `{supersedes:case N}`. |
| `superseded_by` | no | list of decision quoted wikilink `"[[slug]]"` | Back-references, written by the script. |
| `origin` | yes | `raw/YYYY-MM-DD/HHMM/ledger.md#case-N` (the date form, `raw/YYYY-MM-DD/ledger.md#case-N`, on pages born before 2026-09-13; case 103.6) | Where this was ratified. The folder also holds the Spec with the Case. The `raw/` of a session is archived with it once every line of it became a page, and the pointer is not rewritten (cases 100.1, 103.6). |
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
| `## Given` | when a kind other than `defer` is present | The Case's `given`: how things worked before, the pre-task result included — what already existed, what conflicted, what sat in `draft`. The short form of Retro (a defer-only Case) has none (case 56). |
| `## When` | no | Only on pages written before case 72, which keep it: the Case's `when`. A page written after case 72 has no `## When` (case 72.2). |
| `## Criterion` | when the Case shaped an Estimate | One line per Estimate the Case shaped, `- [[estimate-x]] § case N`: the block of the Estimate's Criterion this Case wrote. `when` and `then` live on the Estimate, the `then` block on the target — not here (case 72.2). |
| `## Deferred` | when the Case has a `defer` line with a `purpose` | The body of the deferred decision: one `### [[slug]]` heading per target of the Case's `defer` lines, in that order, each followed by that target's `purpose` verbatim, however long — written for a defer with a `ref` and for a placeholder alike, so the postponed work is never dropped; a `supersedes` does not edit it, the page is archived whole (case 186.1). |
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
Pre-task found no cart page and no overlapping purpose. `entity-checkout` exists and will
be affected. Nothing in `draft` covers this either.

## Criterion
- [[estimate-cart]] § case 1

## History
- 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
```
