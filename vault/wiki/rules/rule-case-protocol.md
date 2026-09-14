---
type: rule
kind: Leaf
purpose: Prevents a decision from being acted on before it is ratified, or ratified without its content in view
status: built
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: "[[rule-claude-md]]"
estimates: ["[[estimate-case-protocol-loaded]]"]
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

## Render

<!-- rule-case-protocol -->
## Case protocol

One reply is one Case, in the seven sections of `case-schema.md`: context, problem,
recommend, given, when, then, ratification. That is the form of Plan Mode. A deferred
decision — an item left open when the person closes Plan Mode, or an item Retro ends
in a defer — is its own Case in the short form: context, problem, a `defer` block with
`purpose`, under the `## Deferred` heading of `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73), before its ledger line (cases 56, 59.5); a page-less Slice task goes to `sprint.md` instead. Taking a
deferred decision up means building its full Case from its page — recommend, given,
when, then added — and writing `{supersedes:case N}` on the line. Never move to the
next Case until this one is ratified or deferred. The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`;
close its line in the reply that ends the item. Plan Mode does not end while a line is
open; `/pre-task` checks it.

A follow-up question that asks you to justify a choice does not split the Case; one
whose answer needs a new choice does — into sub-cases `N.1`, `N.2`. Ratifying a
parent does not ratify its children.

A Case renders as `## Case N — name`, then one blockquote per section: its first
line `**name:**`, its text on the following quoted lines, a blank line between
sections. In `given`, `when` and `then` every line after the first starts with a
bold operand: **＋** for one more condition or action, **－** for a limit or an
exception. `when` and `then` together are the criterion of the Estimate the Case creates or changes: the scripts copy them as its `### case N` block and `problem` as its Context at birth; a Leaf `create` carries `method`, a Leaf `update` `contract: same` or `changed`; one contract per Case or sub-case. Write short sentences, one idea each, in the active voice. A sub-case is
`### Case N.M — name` under its parent, with its own `when`, `then` and
`ratification`, and its own `given` unless it is the parent's word for word; the
sections the children share live on the parent, and `materialize` reads them there. The
`ratification` section ends with a preview of the ledger lines in an untagged
fence, and the turn ends with a plain question in the chat, never a picker tool.
When the person answers with a change, show the Case again: `context` and
`problem` if they changed, always `given`, `when`, `then` and `ratification`, and
no `recommend` — the variant is theirs. The page content itself — fields, prose sections, the `method` of its check — is a YAML
block tagged `then` under the Case in the Spec, not in the chat; `guppi
materialize` reads it, and what is not in that block was signed by nobody.

The Spec is the plan file, written as each Case is ratified, in the reply that
carries its ledger lines: `context`, `problem`, `given`, `when`, `then`, the `then`
block and a block tagged `tasks` — one `- [ ] <what>` per file, test, command and
one-off migration, and one per reading of an Estimate the Case creates or sets
`pending`, by its slug; no `recommend`, no `ratification`, no code. Work Mode ticks the boxes in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task; Retro
counts the unticked.

The harness — hooks, skills, agents, `settings.json`, this section of `CLAUDE.md` —
is rendered from `rules/`. A harness file changes through an `update` of its Rule
page, never by hand; a hook refuses the edit.

Before a `create` without a `ref`, ask the vault first: does this exist, what
conflicts, what sits in `draft`, which tags fit. Put the answer in `given`.
Dispatch the `ask-guppi` agent with one short question.

Ledger lines are written by the `Stop` hook, from the reply, verbatim, each with
the time of writing. A record is a `- decision[case 12][update][rule-x]{ref:rule-x}`, `- estimate[...]` or `- lesson[...]` line inside a fenced block opened with the `LEDGER` tag — the id is `case N`, the word and a space, in `{supersedes:case N}` too; the same
line anywhere else — bare, or in a block with another tag or none — is a preview
and is never written. A `create` line carries the ratified tags: `{tags:a,b}`.
Write the `- decision[...]` lines only in the reply that acknowledges ratification;
`- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson
exists. Without `/hi` the hook refuses and says so: tell the person, do not retry. A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call is never kept, and the hook reads nothing.
<!-- /rule-case-protocol -->

## How it works

Spliced into `CLAUDE.md` between its markers. The six Case sections are not repeated here:
they arrive through `@vault/wiki/case-schema.md`, imported by the same file. What this
section adds is the discipline around them — one Case at a time, when a Case splits, the
vault query before a `create`, the shape of a section, and the LEDGER-block rule the ledger
hook relies on.

`parent: rule-plan-mode` names the Plan Mode MOC of Slice 2, which does not exist yet as a
page; the reference dangles until then, on purpose.

## Estimates

- [[estimate-case-protocol-loaded]]

## Parent

- [[rule-claude-md]]

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-13
- 2026-09-09 updated: records live in a LEDGER block · raw/2026-09-09/ledger.md#case-15.1
- 2026-09-09 updated: a section is `**name:**` + text, closed by a blank line · raw/2026-09-09/ledger.md#case-15.2
- 2026-09-09 updated: a Case is a `## Case N` heading and one blockquote per section; sub-cases are `###` · raw/2026-09-09/ledger.md#case-17, supersedes case 15.2
- 2026-09-09 updated: the search mechanism is the `ask-guppi` agent, not a `/ask` command · raw/2026-09-09/ledger.md#case-26.1
- 2026-09-10 updated: the Render names the then block (superseded by case 34) · raw/2026-09-10/ledger.md#case-30
- 2026-09-10 updated: the Render describes the seven sections, the operands, the then block in the Spec, and {tags} on a create line · raw/2026-09-10/ledger.md#case-34
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: the Frontier is a file, closed line by line (case 59.2) · [[decision-case-59.2]]
- 2026-09-12 updated: the Spec is written as ratified, with a tasks block per Case; boxes ticked in Work Mode, counted at Retro (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: a deferred decision is its own short-form Case under · [[decision-case-59.5]]
- 2026-09-12 updated: the harness changes through Rule pages, never by hand — one sentence always in CLAUDE.md (case 59.6) · [[decision-case-59.6]]
- 2026-09-12 updated: a sub-case's given may be the parent's; when, then and ratification are its own (case 60) · [[decision-case-60]]
- 2026-09-12 updated: the sign-off is asked in plain chat; a changed Case is shown again without recommend (case 62) · [[decision-case-62]]
- 2026-09-12 updated: parent is rule-claude-md, the page CLAUDE.md is rendered from (case 66) · [[decision-case-66]]
- 2026-09-12 deferred · [[decision-case-67]]
- 2026-09-12 updated: the Estimate is derived from the Case: when and then as its Criterion block, method on a create, contract on an update (case 72.1) · [[decision-case-72.1]]
- 2026-09-12 updated: the Spec and the Frontier live in the session's folder (case 73.9) · [[decision-case-73.9]]
- 2026-09-12 defer by decision-case-67 superseded · [[decision-case-75.1]]
- 2026-09-12 updated: the ledger paragraph shows a decision line as written, with the word case (case 75.1, supersedes 67) · [[decision-case-75.1]]
- 2026-09-12 deferred · [[decision-case-81]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-12 defer by decision-case-81 superseded · [[decision-case-86]]
- 2026-09-12 updated: the two keys of the derived Estimate are ratified as estimate_kind and estimate_slug (case 86) · [[decision-case-86]]
- 2026-09-13 status: draft → built · cascade
- 2026-09-14 updated: a reply that carries a LEDGER block ends in that text, no tool call after it (case 122) · [[decision-case-122]]
