---
type: rule
kind: Leaf
purpose: Prevents a Lesson page from carrying a field or section outside the shape lint checks, or lacking one it needs
status: draft
enforcement: render
governs: vault/wiki/lessons/schema.yaml
render_mode: full
parent: "[[rule-page-schemas]]"
estimates: ["[[estimate-lessons-schema-checked]]"]
origin: raw/2026-09-22/0014/ledger.md#case-304.5
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Purpose

Prevents a Lesson page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/lessons/schema.yaml`, the file `guppi lint` reads for every page of `wiki/lessons/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8).

## Render

<!-- rule-lessons-schema -->
type: lesson
description: |
  Three blocks: properties, body, history. Always flat — grouping is what Insight is for.

  A Lesson is a recorded fact, not a ratified decision. It does not go through a Case and requires no ratification; the ledger hook writes it directly.

  Slug. Area + cause: `lesson-hooks-sessionstart-cannot-block`, `lesson-pricing-async-in-sync-tx`. The area groups related lessons together in a plain file listing, and the cause makes near-duplicates visible before anyone opens the index. Naming by symptom was rejected: two unrelated failures often share one symptom, and the symptom is not what clustering compares.

  There is no Estimate. A lesson is a recorded fact: the trigger is the observation, and nothing about it is checked again. An Estimate exists only for a page with a contract — an Entity or a Rule. A `knowledge` claim is checked where it is leaned on: by the Estimate of the Rule built on it (case 53.1).

  There is no `reviewed` status. An intermediate "the librarian looked at it" state records nothing useful — a lesson with no pair is simply still `new`, and will be reconsidered next session anyway. Only membership in an Insight is a real change of state.

  No `## Insight` section: the `insight` field is the link (case 166.1).
properties:
  required: [type, kind, root_cause, status, origin, sprint, created, tags]
  optional: [source, insight]
  values:
    kind: [error, knowledge]
    status: [new, clustered, archived]
  conditional:
    - when: {kind: knowledge}
      required: [source]
    - when: {status: clustered}
      required: [insight]
body:
  required: ["## Trigger", "## Root cause", "## History"]
fields:
  type: |
    required; `lesson`. Page category.
  kind: |
    required; `error` | `knowledge`. `error`: something went wrong. `knowledge`: external material studied once so the source never has to be supplied again.
  root_cause: |
    required; one line. Why it happened (`error`), or the mechanism the source claims (`knowledge`). Lives in properties because the index line of the category is built from it, and clustering into an Insight compares exactly this.
  status: |
    required; `new` | `clustered` | `archived`. `clustered` once it belongs to an Insight. Archived when its Insight is `actioned`.
  source: |
    required on `knowledge`; url or reference. Where the material came from.
  insight: |
    required on `clustered`; quoted wikilink `"[[slug]]"`. The Insight this belongs to, once clustered. Written by the script. The scripts read the slug through the brackets; a slug without a category prefix stays bare (case 148.2). The field is the link; no body section repeats it (case 166.1).
  origin: |
    required; `raw/YYYY-MM-DD/HHMM/ledger.md#L<n>` — the date form, `raw/YYYY-MM-DD/ledger.md#L<n>`, on pages born before 2026-09-13 (case 103.6). The ledger line. Unlike Entity and Rule, this points at a `lesson[...]` line rather than a `decision[...]` one.
  sprint: |
    required; the sprint id.
  created: |
    required; date.
  tags: |
    required; list. Includes what the material applies to, for `knowledge`.
sections:
  "## Trigger": |
    required. What happened (`error`), or what was read (`knowledge`). The full account — the one-line version is `root_cause` in properties.
  "## Root cause": |
    required. Expands the property: why this happened, or what the source actually claims and on what grounds.
  "## History": |
    required. Appended by hook, never by an agent. Always the last section.
examples:
  "error": |
    ---
    type: lesson
    kind: error
    root_cause: SessionStart cannot block, so nothing gated the first ledger write
    status: clustered
    insight: insight-hook-gating-assumptions
    origin: raw/2026-09-08/ledger.md#L14
    sprint: 2026-Q3-s4
    created: 2026-09-08
    tags: [hooks, ledger, session]
    ---

    ## Trigger
    The first ratified decision of the session was written to `main` instead of the session
    branch. Noticed only at handoff, when the librarian found a ledger line outside the
    session folder.

    ## Root cause
    SessionStart cannot block — exit code 2 is a no-op there. The guard had been placed on
    SessionStart on the assumption that it behaved like PreToolUse. Nothing actually gated
    the write.

    ## History
    - 2026-09-08 created · raw/2026-09-08/ledger.md#L14
    - 2026-09-15 status: new → clustered
  "knowledge": |
    ---
    type: lesson
    kind: knowledge
    root_cause: Per-finding fix subagents each rebuild context and rerun the suite
    status: new
    source: https://github.com/obra/superpowers
    origin: raw/2026-09-12/ledger.md#L07
    sprint: 2026-Q3-s4
    created: 2026-09-12
    tags: [subagents, review, cost]
    ---

    ## Trigger
    Read the subagent-driven-development skill while deciding how to structure our own
    review step.

    ## Root cause
    It dispatches a single fix subagent with the complete findings list rather than one per
    finding. The stated reason is that per-finding fixers each rebuild context and rerun the
    test suite, and in a real session that wave cost more than all the implementation tasks
    combined.

    ## History
    - 2026-09-12 created · raw/2026-09-12/ledger.md#L07
<!-- /rule-lessons-schema -->

## History

- 2026-09-22 created · [[decision-case-304.5]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
