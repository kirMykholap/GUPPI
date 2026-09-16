---
type: decision
case: "195"
status: archived
update: ["[[rule-case-protocol]]"]
superseded_by: ["[[decision-case-200.1]]"]
origin: raw/2026-09-16/1651/ledger.md#case-195
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
---

## Context

`rule-case-protocol` is a Leaf, `enforcement: render`, `governs: CLAUDE.md`, `render_mode: partial`; its Render is the "Case protocol" section of the system prompt. Case 188 ratified the new form of a Case: `given` holds the conditions of the behaviour, the state of pages goes to `context`, `context` names the Estimates touched, `given` + `when` + `then` are the Criterion replaced whole, the Case names the Estimate by slug, `tasks` without `contract` and "block N", a `create` without `method`, `estimate_kind`, `estimate_slug`. But the block of 188 carries only `sections: Purpose` and `change`; there is no new Render text, and the task of 188 demands `render --check` exit 0, which would splice the old Render into `CLAUDE.md`. Case 187 added a rule the Render must carry too: only a replaced Criterion sets `pending`, an `update` of `Purpose` touches no Estimate, an `update` of the Render touches the Estimate of the live reading. This Case touches `estimate-case-protocol-loaded` — the Estimate of the live reading of the Render, already `pending` by 188 with a replaced Criterion this Case does not change; it does not touch `estimate-case-protocol-case-form`, `-acknowledging-reply`, `-ledger-line-form` or `estimate-claude-md-rendered`.

## Problem

The Render is the one text the agent writes a Case by, and it still says the old model. Without the new text Cases 187 and 188 are ratified but every next session writes Cases the old way, and `guppi render` rewrites `CLAUDE.md` with what contradicts `case-schema.md` after 188.

## Given

`CLAUDE.md` is in the system prompt from the first turn; the Render is spliced between the `rule-case-protocol` markers.
**＋** `case-schema.md` is rewritten by 188 in the same run; the Render does not repeat it, it adds the discipline around it.
**＋** `guppi render --check` compares the file with the page's Render; `estimate-claude-md-rendered` promises the equality.
**－** The live reading of the Render is `estimate-case-protocol-loaded`, `pending` by 188; this Case does not change its Criterion and does not name it in the block.

## History

- 2026-09-16 created · raw/2026-09-16/1651/ledger.md#case-195
- 2026-09-16 superseded by decision-case-200.1 · [[decision-case-200.1]]
- 2026-09-16 archived · superseded
- 2026-09-16 archived · cleanup
