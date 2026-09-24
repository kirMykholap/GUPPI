---
type: rule
kind: Leaf
purpose: Prevents a Rule page from carrying a field or section outside the shape lint checks, or lacking one it needs
status: built
enforcement: render
governs: vault/wiki/rules/schema.yaml
render_mode: full
parent: "[[rule-page-schemas]]"
estimates: ["[[estimate-rules-schema-checked]]"]
origin: raw/2026-09-22/0014/ledger.md#case-305.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Purpose

Prevents a Rule page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/rules/schema.yaml`, the file `guppi lint` reads for every page of `wiki/rules/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8). `applies_to` is the edge Rule → Entity, written in the Case; the Entity's `rules` is its backlink, computed (case 305).

## Render

<!-- rule-rules-schema -->
type: rule
description: |
  Three blocks: properties, body, history. Mirrors Entity, with three differences that matter: how it is enforced, what a MOC means, and that children are ordered.

  A Rule is a standing condition one case can break, with a guard that refuses that case when it occurs. The check: can one case refute it, and is there something to refuse that case? Yes to both → a Rule, and its Estimate is the test that the guard works. A condition no single case can break — a measure of the whole — is not a Rule but an Estimate on an Entity; a condition with no guard is not one either. A Leaf is a condition on each case; a MOC a sequence whose Estimate promises the order — one run out of order breaks it. A Rule is of the harness or of an Entity: on an Entity it is a checkable requirement, and its Estimate promises how the requirement is controlled. That single definition covers both harness hooks and code constraints — see Enforcement below (case 240.2).

  Ordering. `children` on a Rule MOC is an ordered list, and the order is the content. A workflow MOC says `retro → handoff → documentation`; sorting those alphabetically destroys the only thing the page was recording. Scripts that rebuild backlinks must preserve the order given, and lint must not normalize it. This is the one place a Rule MOC differs structurally from an Entity MOC, where children are independent requirements and order is arbitrary.

  MOCs and enforcement. `hook` and `check` are meaningless on a MOC: grouping does not fire on an event and does not run against code. The force there lives in the children. `render` is the exception. A MOC that renders holds the frame of a harness file — its structure and the markers its children splice into — while each child renders one section. The frame is not separable from the grouping: a MOC over three sections plus a separate Leaf holding an empty template with markers would be two pages describing one thing. So a rendering MOC uses `render_mode: full` on the target file, and its children with a Render use `partial` into the same file. Child order is the order of sections in the output, which is the ordinary Rule-MOC rule about order being content, applied literally. A child without a Render — a script the frame calls by name — is a step of the workflow that contributes nothing to the file; the renderer skips it, and a marker line for it is an error. Not every step of a workflow is a child page. The atomicity rule of [[rule-atomicity]] applies as everywhere: split when parts fail independently and are fixed differently. Four `@`-imports from the vault fail the same way (missing file, wrong path) and are fixed the same way — one Leaf, listed in its body. But `git pull` and `gh issue list` fail differently, on conflicts versus authentication, so those are separate Leaves. Intermediate MOCs need justification too. A MOC earns its place when a cross-cutting Estimate can be stated for it; "internal storage" has none of its own — the only meaningful check covers the whole load, and that belongs to the workflow MOC.

  Enforcement. Three ways a rule has force. `hook` — fires during the session lifecycle. Blocks a ledger write, appends to `log.md` on every page change, refuses a commit while tests are red. `implementation_ref` points at the script. `check` — runs against the code. This is where constraints live: "synchronous API only in this module" is not a hook, it is a linter rule that catches `async` there. `implementation_ref` points at the linter config or test. `render` — the rule's own body is the harness text. `governs` names the target file, `render_mode` says whether the body replaces it entirely or is spliced between markers `<!-- rule-slug -->` … `<!-- /rule-slug -->`. `render` is what closes the self-improvement loop. Where `hook` and `check` describe something implemented elsewhere, a `render` rule is the implementation — the page is the source of truth and a script regenerates the harness from it. Change the rule through a ratified decision and the skill changes; there is no second copy to drift. `render` applies to harness rules and to the vault files a rule renders — `case-schema.md` from `rule-case-protocol` (case 273.1), each `schema.yaml` from a child of `rule-page-schemas` (case 304). A constraint on an Entity — async in the pricing module — is a `check`: it has no `render_mode`, because there is nothing in the harness to write it into; a `check` rule whose script writes a file names that file in `governs`, so the guard reads the field alike (`rule-sprint`, case 209.7). A constraint that no hook, check or render can detect is not a Rule at all. It is a sentence in an Entity's `How it works`. The one exception is the agent's own conduct — how it writes, splits and implements — which no script can judge in substance: its `render` rule puts the text into a file the agent reads when it acts — `CLAUDE.md` in every context, `case-schema.md` in a working session —, `render --check` and the governed-files hook refuse its drift, and its Estimate reads the render, and what the agent did by hand where it names that; the text in the context is the guard (case 372). Keeping that line sharp is what stops `rules/` from filling with unenforceable declarations. Every Rule requires an Estimate. A broken hook breaks the workflow as thoroughly as broken product code breaks the product — there is no "documentation-class" exemption. In the harness a thing is a Rule when its code is a guard — it refuses a case: a hook, a check, a render that refuses drift. A thing is an Entity when it is measured and has no guard of its own; its guard is a separate Rule. The sprint is an Entity by this criterion — its Definition of done is read, and `rule-sprint` is its guard — not an exception (case 240.2). A rule of an Entity names it in `applies_to`, the edge Rule → Entity; the Entity's `rules` is the backlink, computed by the cascade of `generate`. A rule constrains a case — a page, a session, a file — never another rule: what a rule reads or guards among the rules follows from `implementation_ref` and `governs` and is never written (case 305).

  No body section is derived from a ref field: `estimates`, `children`, `parent` and `implementation_ref` are the link, seen by Obsidian since case 148.1 (case 166.1). `deferred_by` is written on a defer and cleared on a `supersedes` by `guppi generate`, never by hand (case 52.3).
properties:
  required: [type, kind, purpose, status, estimates, origin, sprint, created, tags]
  optional: [enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to]
  values:
    kind: [MOC, Leaf]
    status: [draft, built, archived]
    enforcement: [hook, check, render]
    render_mode: [full, partial]
  conditional:
    - when: {enforcement: hook}
      required: [implementation_ref]
    - when: {enforcement: check}
      required: [implementation_ref]
    - when: {enforcement: render}
      required: [governs, render_mode]
    - when: {kind: MOC}
      required: [children]
      forbidden_values: {enforcement: [hook, check]}
ordered_children: true
body:
  required: ["## Purpose", "## History"]
  optional: ["## Render", "## How it works"]
  conditional:
    - when: {enforcement: render}
      required: ["## Render"]
fields:
  type: |
    required; `rule`. Page category.
  kind: |
    required; `MOC` | `Leaf`. MOC: a workflow — an ordered sequence of rules. Leaf: one enforceable rule.
  purpose: |
    required; one line. What this prevents, not what it provides. The index line of the category is built from it.
  status: |
    required; `draft` | `built` | `archived`. Set by the cascade of `generate` once every Estimate passes, never by hand.
  enforcement: |
    optional; `hook` | `check` | `render`. How the rule has force, and which of the fields below apply. On a Leaf, any of the three. On a MOC, only `render` — see MOCs and enforcement.
  implementation_ref: |
    required on `hook` and `check`; list of paths. The hook script, or the linter/test that performs the check. The field is the link; no body section repeats it (case 166.1).
  governs: |
    required on `render`, allowed on `check`; path. The file this rule's text is rendered into — a harness file, or a file of the vault such as `case-schema.md` (case 273.1) or a `schema.yaml` (case 304); on a `check` rule, the file its script writes — the governed-files hook refuses a hand edit of either (case 209.7).
  render_mode: |
    required on `render`; `full` | `partial`. Whether the rule's body becomes the whole target file, or is spliced between markers inside it.
  parent: |
    on a Leaf; quoted wikilink `"[[slug]]"`. The workflow MOC above it. The scripts read the slug through the brackets; a slug without a category prefix stays bare (case 148.2). The field is the link; no body section repeats it (case 166.1).
  children: |
    on a MOC; ordered list of quoted wikilinks `"[[slug]]"`. See Ordering. The field is the link; no body section repeats it (case 166.1).
  estimates: |
    required; list of quoted wikilinks `"[[slug]]"`. On a Leaf: that the rule does what it claims. On a MOC: that the sequence itself holds. Empty until the person names a promise. The field is the link; no body section repeats it (case 166.1).
  deferred_by: |
    optional; list of decision quoted wikilinks `"[[slug]]"`. The Decision pages whose `defer` targets this page. Written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; the index line carries it, so `ask-guppi` reaches the deferred decision without opening the page (case 52.3).
  applies_to: |
    optional; list of quoted wikilinks `"[[entity-slug]]"`. The Entities this rule is the guard of (case 240.2): a rule that guards a thing names it here — `rule-sprint` → `entity-sprint`, `rule-harness` → `entity-guppi`; a rule of the process — a phase MOC and its steps — carries none; written in the Case, never computed. The Entity's `rules` is the backlink, written by the cascade of `generate` (case 305). The field is the link; no body section repeats it.
  origin: |
    required; `raw/YYYY-MM-DD/HHMM/ledger.md#case-N` — the date form, `raw/YYYY-MM-DD/ledger.md#case-N`, on pages born before 2026-09-13 (case 103.6).
  sprint: |
    required; the sprint id.
  created: |
    required; date.
  tags: |
    required; list, ratified in the Case.
sections:
  "## Purpose": |
    required. Expands the property: what goes wrong without this rule. State the failure it prevents, not the behaviour it produces.
  "## Render": |
    required on `render`. The text written into `governs`, wrapped in `<!-- slug -->` markers. This section is the implementation. On a rendering MOC it is the frame, containing the children's markers.
  "## How it works": |
    optional. MOC only: why the steps are in this order, and what breaks if they are reordered. On a Leaf the promise lives in its Estimates and the mechanism in the docstring of its code, or in its Render; a Leaf that still carries the section keeps it until its next touch, when the section leaves (cases 193, 200.2).
  "## History": |
    required. Appended by hook, never by an agent. Always the last section.
examples:
  "MOC — a rendering workflow": |
    Holds the frame of the skill file; children splice into its markers, in child order.

    ---
    type: rule
    kind: MOC
    purpose: Prevents a session from being loaded piecemeal by read-tool calls
    status: draft
    enforcement: render
    governs: .claude/skills/hi/SKILL.md
    render_mode: full
    parent: rule-session-start
    children: [rule-internal-context, rule-git-context, rule-github-issues]
    estimates: [estimate-hi-no-read-calls]
    origin: raw/2026-09-08/ledger.md#case-5
    sprint: 2026-Q3-s4
    created: 2026-09-08
    tags: [session, harness]
    ---

    ## Purpose
    Prevents a session from being loaded piecemeal by read-tool calls. Bash substitutions in a
    command body resolve before the agent's first turn, so the context is simply present —
    there is no step the agent can forget or reorder.

    ## How it works
    Rendered in full into the skill file; the three children splice into the markers below, in
    the order they are listed. Editing the skill directly is meaningless — the next render
    overwrites it. Changes belong on these pages, through a ratified decision.

    ## Render
    <!-- rule-skill-hi -->
    <!-- rule-internal-context -->
    <!-- rule-git-context -->
    <!-- rule-github-issues -->

    Assemble the Frontier from the above and present it as a list: tasks, problems, debt
    carried over, and where the sprint stands. Wait for the human to pick the order.
    <!-- /rule-skill-hi -->

    ## History
    - 2026-09-08 created · raw/2026-09-08/ledger.md#case-5
  "Leaf — a partial render": |
    ---
    type: rule
    kind: Leaf
    purpose: Prevents work starting without the current sprint and last session's handover
    status: draft
    enforcement: render
    governs: .claude/skills/hi/SKILL.md
    render_mode: partial
    parent: rule-skill-hi
    estimates: [estimate-internal-context-loaded]
    origin: raw/2026-09-08/ledger.md#case-6
    sprint: 2026-Q3-s4
    created: 2026-09-08
    tags: [session, harness]
    ---

    ## Purpose
    Prevents work starting without the current sprint and the previous session's handover.
    Both are vault files, both fail the same way — missing file or wrong path — so they are
    one rule rather than two.

    ## How it works
    `case-schema.md` is listed here since case 273; the glossary arrives through `@import`
    in `CLAUDE.md`, the category schemas are read when a page of their category is written,
    and re-reading either would duplicate context that is already present.

    ## Render
    <!-- rule-internal-context -->
    @wiki/sprint.md
    @wiki/brief.md
    <!-- /rule-internal-context -->

    ## History
    - 2026-09-08 created · raw/2026-09-08/ledger.md#case-6
  "Leaf — a hook": |
    ---
    type: rule
    kind: Leaf
    purpose: Prevents a ledger line from being written to the wrong branch
    status: built
    enforcement: hook
    implementation_ref: [.claude/hooks/ledger-guard.sh]
    parent: rule-session-start
    estimates: [estimate-ledger-guard]
    origin: raw/2026-09-08/ledger.md#case-6
    sprint: 2026-Q3-s4
    created: 2026-09-08
    tags: [ledger, session]
    ---

    ## Purpose
    Prevents a ledger line from being written to the wrong branch. SessionStart cannot block
    anything — exit 2 is a no-op there — so without this guard a decision ratified before the
    workspace resolves would silently land outside the session.

    ## How it works
    PreToolUse, matched on writes to `ledger.md`. Reads the readiness flag written when the
    workspace was resolved; exits 2 and blocks the write if it is missing.

    ## History
    - 2026-09-08 created · raw/2026-09-08/ledger.md#case-6
    - 2026-09-09 status: draft → built
  "Leaf — a check (constraint)": |
    ---
    type: rule
    kind: Leaf
    purpose: Prevents async calls leaking into the pricing module
    status: built
    enforcement: check
    implementation_ref: [ruff.toml, tests/lint/test_pricing_sync.py]
    estimates: [estimate-pricing-sync-check]
    origin: raw/2026-09-12/ledger.md#case-2
    sprint: 2026-Q3-s4
    created: 2026-09-12
    tags: [pricing, constraints]
    ---

    ## Purpose
    Prevents async calls leaking into the pricing module. Pricing runs inside a synchronous
    transaction; an await there does not fail loudly, it produces a partially applied price.

    ## How it works
    A lint rule flags `async def` and `await` under `src/pricing/`. Runs in CI, so the
    violation surfaces at the change that introduces it rather than at the next incident.

    ## History
    - 2026-09-12 created · raw/2026-09-12/ledger.md#case-2
<!-- /rule-rules-schema -->

## History

- 2026-09-22 created · [[decision-case-305.1]]
- 2026-09-22 updated: the atomicity rule is named by its page (case 317) · [[decision-case-317]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 updated: the guard of a rule on the agent's own conduct is its text in the context (case 372) · [[decision-case-372]]
- 2026-09-24 status: draft → built · cascade
