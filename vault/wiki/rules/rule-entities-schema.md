---
type: rule
kind: Leaf
purpose: Prevents an Entity page from carrying a field or section outside the shape lint checks, or lacking one it needs
status: built
enforcement: render
governs: vault/wiki/entities/schema.yaml
render_mode: full
parent: "[[rule-page-schemas]]"
estimates: ["[[estimate-entities-schema-checked]]"]
origin: raw/2026-09-22/0014/ledger.md#case-306.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Purpose

Prevents an Entity page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/entities/schema.yaml`, the file `guppi lint` reads for every page of `wiki/entities/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8). `rules` is the backlink of the edge Rule → Entity, computed by the cascade of `generate` from the `applies_to` of the live rules (case 305); `## Terms` is the section of the glossary page, `entity-glossary` (case 306).

## Render

<!-- rule-entities-schema -->
type: entity
description: |
  Three blocks: properties, body, history. One schema for both kinds; sections that do not apply are omitted.

  An Entity is a thing the developer builds: a noun the person named as part of what is built. The check before a `create`: who makes this thing? The developer → an Entity. The product's user, or the running product — a post, an account, a record → data, which lives in the product and is never a page. A developer who uses GUPPI is still the developer; "user" in this check is always the user of the developer's product (case 240.1).

  A MOC is a thing whose parts the person named as things that are built; a Leaf is a thing for which the person has not done that yet. A part comes only from the person's words, through a Case; the agent proposes a cut — in Retro, by the atomicity rule of [[rule-atomicity]] — and never makes it. A part is itself an Entity: its own code, its own conditions. What is not a part — a field, a button, a function inside a Leaf — is the Leaf's inner working and goes to `## How it works`, not to a page. The Estimates of a MOC measure what no child owns; a Leaf's measure its own scope; a Leaf with empty `estimates` is legal — the person said nothing yet. Depth is not fixed in advance — it follows the atomicity rule and nothing else.

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

## History

- 2026-09-22 created · [[decision-case-306.1]]
- 2026-09-22 updated: the atomicity rule is named by its page, not by a § of index.md (case 317) · [[decision-case-317]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
