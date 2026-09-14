---
type: decision
case: "144.3"
status: current
update: ["[[insight-materialize-lift-loses-a-schema-field]]"]
origin: raw/2026-09-14/1633/ledger.md#case-144.3
sprint: migration
created: 2026-09-14
tags: [harness, ledger]
---

## Context

An Insight of severity 2, `open`, two children (G, J): a standalone Estimate `create` put `criterion` and `method` into the frontmatter instead of sections; `parse_line` read only `tags` from the braces of a lesson line and lost `source`. Pattern: the parser decides what a page gets; the page is written without the field, and lint names the miss on the page — one step and one session after the line. Proposal: one table "field — category — where it comes from", `materialize` lifts by it; a field the source lacks is `incomplete`; a field the source holds and the table does not know is the parser's fault.

## Problem

Both children are fixed: 53.3 — a standalone Estimate maps `context`, `criterion`, `method` into sections; 87 — `parse_line` returns `source` from the braces, a `knowledge` lesson without it is marked `incomplete: [source]`. The table of sources exists in code as `REQUIRED` (rules, entities, estimates, insights — the fields of a `then` item) plus the rule of 87 for a lesson; `rule-page-generation`: "A missing `source` is not invented; lint names it". The recurrence in O — three `knowledge` lessons without `source` — is not a loss by the parser: the lines carried no `{source:…}`. The cause is upstream: neither `rule-case-protocol` (the Render in `CLAUDE.md`) nor `rule-retro` tells the agent to write `{source:…}` on a `knowledge` line; only `case-schema.md` ("present only when they apply", 75.1) and the glossary say so. Decide: (1) the protocol names `source` as required on a `knowledge` line; (2) the three lessons of O get a `source`; (3) the Insight `actioned`.

## Given

`insight-materialize-lift-loses-a-schema-field`: `open`, severity 2, children `lesson-materialize-standalone-estimate-keeps-criterion-as-a-field`, `lesson-materialize-lesson-line-source-dropped`, both `clustered`; the cascade of 104.2.
**＋** `lessons/schema.yaml`: `source` under `optional` and `conditional: when kind: knowledge → required: [source]`; `schema.md`: "`knowledge`: external material studied once so the source never has to be supplied again", "`source` | `knowledge` | url or reference | Where the material came from". `rule-lint` checks by the schema — three `schema` findings on the lessons of O.
**＋** `rule-materialize` `built` (87): "`source` when the braces of the line carry one … a `knowledge` lesson whose line carries no `source` is marked `incomplete: [source]`"; `parse_line` returns `source` for a lesson and a decision.
**＋** `rule-page-generation` `built`: "A missing `source` is not invented; lint names it".
**＋** `rule-case-protocol` `built`, `enforcement: render`, `governs: CLAUDE.md`, `render_mode: partial`, `estimates: [estimate-case-protocol-loaded]`; its Render in `CLAUDE.md` names the form `- lesson[...]` and `{tags:a,b}` for a `create`, not `source`. `rule-ledger-write`: writes verbatim, refuses only without `/hi`. `rule-retro`: `- lesson[...]` without `source`.
**＋** `case-schema.md`: "`{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1)"; the glossary: `source` "in a ledger line, the external origin".
**＋** Three lessons of O, `kind: knowledge`, `status: new`, no `source`, `raw/2026-09-14/1229/materialize.yaml` `incomplete: [source]`: `lesson-gate-plan-path-cut-by-the-event-log-detail-limit` (L20), `lesson-agents-read-at-session-start-in-claude-code-2-1-228` (L29), `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate` (L31).
**－** No other live Lesson or Insight is about a field lost between the line and the page (`ask-guppi`).
**－** An Insight is not a Leaf; a Lesson is not a Leaf: an `update` without `contract`. `case-schema.md` and `lessons/schema.*` do not change.

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-144.3
