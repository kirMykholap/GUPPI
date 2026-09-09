---
type: rule
kind: Leaf
purpose: Prevents a decision from being acted on before it is ratified, or ratified without its content in view
status: draft
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: rule-plan-mode
estimates: [estimate-case-protocol-loaded]
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## Purpose

Prevents a decision from being acted on before it is ratified, or ratified without its
content in view. This is instruction, not enforcement — no hook can check "did you finish
the Frontier" or "did you wait for the sign-off" — so it is written where the agent always
sees it: `CLAUDE.md`, which is in the system prompt from the first turn.

## How it works

Spliced into `CLAUDE.md` between its markers. The six Case sections are not repeated here:
they arrive through `@vault/wiki/case-schema.md`, imported by the same file. What this
section adds is the discipline around them — one Case at a time, when a Case splits, the
vault query before a `create`, and the fence/bare-line rule the ledger hook relies on.

`parent: rule-plan-mode` names the Plan Mode MOC of Slice 2, which does not exist yet as a
page; the reference dangles until then, on purpose.

## Render

<!-- rule-case-protocol -->
## Case protocol

One reply is one Case, in the six sections of `case-schema.md`. Never move to the next
Case until this one is ratified or deferred. Plan Mode does not end while a Frontier item
is neither ratified nor deferred.

A follow-up question that asks you to justify a choice does not split the Case; one whose
answer needs a new choice does — into sub-cases `N.1`, `N.2`. Ratifying a parent does not
ratify its children.

Before a `create` without a `ref`, ask the vault first: does this exist, what conflicts,
what sits in `draft`, which tags fit. Put the answer in `now`. Use `/ask` once it exists;
until then read the category folders.

Ledger lines are written by the `Stop` hook, from the reply, verbatim. A line inside a
fenced block is a preview and is never written; a bare line at column zero is a record.
Write the bare `- decision[...]` lines only in the reply that acknowledges ratification;
`- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson
exists. Without `/hi` the hook refuses and says so: tell the person, do not retry.
<!-- /rule-case-protocol -->

## Estimates

- [[estimate-case-protocol-loaded]]

## Parent

- [[rule-plan-mode]]

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-13
