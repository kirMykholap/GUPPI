---
type: rule
kind: Leaf
purpose: Prevents a Decision page from carrying a field or section outside the shape lint checks, or lacking one it needs
status: built
enforcement: render
governs: vault/wiki/decisions/schema.yaml
render_mode: full
parent: "[[rule-page-schemas]]"
estimates: ["[[estimate-decisions-schema-checked]]"]
origin: raw/2026-09-22/0014/ledger.md#case-304.7
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Purpose

Prevents a Decision page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/decisions/schema.yaml`, the file `guppi lint` reads for every page of `wiki/decisions/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8).

## Render

<!-- rule-decisions-schema -->
type: decision
description: |
  Every page has three blocks: properties (frontmatter), body (per-category sections), history (appended by hook). This is the schema for Decision. One page per Case, however many ledger lines the Case produced.

  Slug. `decision-case-<N>`: `decision-case-18.1`. Mechanical, because the script writes the page and may not name anything; unique, because a Case id is. Nothing searches Decision pages, so the slug needs no meaning beyond the Case it points back at. A Decision is reached by reference only: from a target page's `deferred_by` (a deferred decision, case 52.3), from the `[[decision-case-N]]` wikilink of a History line (case 52.4), or by the case id a `supersedes` carries.

  Fields deliberately absent. `ratification` — a Decision page cannot exist without it. The Case does not close, no ledger line is written, no page is generated. A field with one possible value carries no information; the fact is recorded by the page existing and by `origin`. `recommend` — if the human accepted the proposal it became `Then`; if they changed it, `Then` holds the change. Either way the original is conversation history, recoverable from the archived ledger. `last_updated` — a decision is not edited. Only `status` and `superseded_by` ever change, and both are dated in History; one more History line is allowed, `updated:` of a Case that signs the page's text after the fact (case 358). `authority` — dropped. It overlapped with tags on one reading and with `ref` on the other. If a real need appears later, it comes back as a ratified decision.

  The body is the Case that produced it, minus what belongs to the conversation rather than the decision. `create`, `update`, `delete`, `defer`: one list per kind present among the Case's ledger lines, in that order, each the slugs of those lines in ledger order; a kind with no line is absent, at least one is present. The category is derived from the slug prefix, never written. Lint checks every page slug names a live or archived page, and that neither `kind` nor `target_slug` is present (case 59.4).
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
    one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `create` lines, in ledger order: a page. One list per kind present, in the order create, update, delete, defer; a kind with no line is absent. Lists of quoted wikilinks for page slugs, so Obsidian shows them as links (case 148.2); the kind of every target is its key (case 59.4, replacing the aligned `kind` and `target_slug` of case 52.1). The category is derived from the slug prefix and never written; the parent of a `create` is on the child page as `parent` or `target`.
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
    optional. The Case's `given`, verbatim: the frame of the Case — the pages, modules, files and tests it touches and the rule that constrains — written by `generate` on the page of a Case that has one (case 378.3); a page written between case 201.2 and case 378.3 carries none.
  "## When": |
    optional. Only on pages written before case 72, which keep it: the Case's `when`. A page written after case 72 has no `## When` (case 72.2).
  "## Criterion": |
    optional. Only on pages written before case 201.2, which keep it: one `- [[estimate-x]] § case N` line per block the Case wrote under the shape before case 193. A page written after carries none: the Estimate named in the Case holds the Criterion whole (case 201.2).
  "## Deferred": |
    when the Case has a `defer` line with a `purpose`. The body of the deferred decision: one `### [[slug]]` heading per target of the Case's `defer` lines, in that order, each followed by that target's `purpose` verbatim, however long — written for a defer with a `ref` and for a placeholder alike, so the postponed work is never dropped; a `supersedes` does not edit it, the page is archived whole (case 186.1).
  "## Note": |
    optional. Only when ratification was non-trivial: a reservation, a condition, a rejected alternative worth remembering. Omit when the answer was simply yes.
  "## History": |
    required. Appended by hook, never by an agent. Always the last section, so `tail` reads it without loading the page: `- <date> created · <origin>`, `- <date> superseded by decision-case-N`, and `- <date> updated: <change> · [[decision-case-N]]` of a Case that signs the text after the fact (case 358).
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
    `entity-cart` — the page this Case creates.
    **＋** `entity-checkout` — the page the cart precedes.

    ## History
    - 2026-09-08 created · raw/2026-09-08/ledger.md#case-1
<!-- /rule-decisions-schema -->

## History

- 2026-09-22 created · [[decision-case-304.7]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-22 updated: a Decision target is a page; the Rule-class map is gone (case 320) · [[decision-case-320]]
- 2026-09-23 updated: a Decision's History takes one updated line of a Case that signs its text after the fact (case 358) · [[decision-case-358]]
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 status: draft → built · cascade
- 2026-09-23 updated: the decision page carries the Case's given again (case 378.3) · [[decision-case-378.3]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
