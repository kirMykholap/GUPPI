---
type: rule
kind: Leaf
purpose: Prevents a decision from being acted on before it is ratified, or ratified without its content in view
status: draft
enforcement: render
governs: CLAUDE.md
render_mode: partial
parent: "[[rule-claude-md]]"
estimates: ["[[estimate-case-protocol-loaded]]", "[[estimate-case-protocol-case-form]]", "[[estimate-case-protocol-acknowledging-reply]]", "[[estimate-case-protocol-ledger-line-form]]"]
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## Purpose

Prevents a decision from being acted on before it is ratified, or ratified without its
content in view. This is instruction, not enforcement — no hook can check "did you
finish the Frontier" or "did you wait for the sign-off" — so it is written where the
agent always sees it: `CLAUDE.md`, which is in the system prompt from the first turn.

The eight Case sections are not repeated in the Render: they arrive through
`@vault/wiki/case-schema.md`, imported by the same file. `parent: rule-claude-md`
names the file the Render is spliced into; `rule-plan-mode` is the rule of the phase
in which a Case is held (case 188).

## Render

<!-- rule-case-protocol -->
## Case protocol

One reply is one Case, in the eight sections of `case-schema.md`: context, problem,
recommend, given, when, then, tasks, ratification. That is the form of Plan Mode. A deferred
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
sections. `context`, `problem` and `recommend` carry no operand, name the slug of the thing described only, and run to seven sentences each at most: `context` says what the thing is and how it works today, for a reader who has not opened the pages — the state of the pages the Case changes lives here — and names which Estimates of the rule the Case touches and which it does not, with no line numbers and no quotation unless the Case is about one; `problem` says what is wrong, or the question answered, in one paragraph; `recommend` says the choice and why, the rejected option in one sentence. `given` holds the conditions of the behaviour, one per line, and only a condition a line of `then` depends on — the rule that constrains, the test that fixes the behaviour; no state of pages, no history, no quotation for its own sake (case 188). In `given`, `when` and `then` every line after the first starts with a
bold operand: **＋** for one more condition or action — "and also", **－** for a limit or an
exception — "but not", "does not apply here". `then` holds behaviour only: no Estimate block, no reading, no `supersedes`; those are lines of `tasks`, a section between `then` and `ratification`, a checklist in its blockquote — one line per page `update`, file, test, command, one-off migration and reading, without `contract` and without "block N" — the same lines that go into the Spec's `tasks` block. Slugs, file names and field values sit in code spans; bold is for section labels and operands only. One horizontal rule at most, after the Case or its last sub-case, and only when the agent's own text follows (case 159). `given`, `when` and `then` together are the Criterion of the Estimate the Case creates or changes: the scripts copy them whole, replacing what stood there, unless the item writes `sections: Criterion` itself — that text stands, on an `update` as on a `create`, and it is how one Case touches two promises (case 204); the Case names that Estimate by slug in its `then` block, and only a replaced Criterion sets it `pending` — an `update` of a rule's `Purpose` touches no Estimate, an `update` of its `Render` touches the Estimate of the live reading of that Render (case 187). A new promise is an explicit `create` of an Estimate with `ref` naming its target and its slug in the Case; a `create` of a rule or an entity carries no `method`, `estimate_kind` or `estimate_slug`, an `update` no `contract`; one promise per Case or sub-case — two touched promises are two sub-cases (case 188). Write short sentences, one idea each, in the active voice. A sub-case is
`### Case N.M — name` under its parent, with its own `when`, `then`, `tasks` and
`ratification`, and its own `given` unless it is the parent's word for word; the
sections the children share live on the parent, and `materialize` reads them there. The
`ratification` section ends with a preview of the ledger lines in an untagged
fence, and the turn ends with a plain question in the chat, never a picker tool.
When the person answers with a change, show the Case again: `context` and
`problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`, and
no `recommend` — the variant is theirs. The page content itself — fields, prose sections, and for an Estimate its `purpose` and `method` — is a YAML
block tagged `then` under the Case in the Spec, not in the chat; `guppi
materialize` reads it, and what is not in that block was signed by nobody.

The Spec is the plan file, written as each Case is ratified, in the reply that
carries its ledger lines: `context`, `problem`, `given`, `when`, `then`, the `then`
block and a block tagged `tasks` — one `- [ ] <what>` per file, test, command and
one-off migration, and one per reading of an Estimate the Case creates or sets
`pending`, by its slug; no `recommend`, no `ratification`, no code. Work Mode ticks the boxes on code, tests, migrations and readings in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task; `generate`, `render` and `sprint` tick the page, render and sprint lines (cases 226, 250); Retro counts the unticked.

The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first; a heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; a heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last. Headings and labels in the language of the chat (case 167, supersedes 157).

The harness — hooks, skills, agents, `settings.json`, this section of `CLAUDE.md` —
is rendered from `rules/`. A harness file changes through an `update` of its Rule
page, never by hand; a hook refuses the edit.

Before a `create` without a `ref`, ask the vault first: does this exist, what
conflicts, what sits in `draft`, which tags fit. Put the answer in `context`.
Dispatch the `ask-guppi` agent with one short question.

Ledger lines are written by the `Stop` hook, from the reply, verbatim, each with
the time of writing. A record is a `- decision[case 12][update][rule-x]{ref:rule-x}`, `- estimate[...]` or `- lesson[...]` line inside a fenced block opened with the `LEDGER` tag — the id is `case N`, the word and a space, in `{supersedes:case N}` too; the same
line anywhere else — bare, or in a block with another tag or none — is a preview
and is never written. A `create` line carries the ratified tags: `{tags:a,b}`. A `knowledge` lesson line carries `{source:...}`, the url or reference the lesson studied — a file of the harness, a probe, a client version; the schema requires it, and a line without it is `incomplete: [source]` in the yaml and a lint finding on the page. An `error` lesson never carries one.
Write the `- decision[...]` lines only in the reply that acknowledges ratification;
`- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson
exists, an `estimate[...]` line opening with the date of the reading and the command or the place it was read (case 199). Without `/hi` the hook refuses and says so: tell the person, do not retry. A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call waits for the next `Stop` of the session, and the last reply of a session has none. A block a tool call did follow is not lost until that `Stop` has passed: check the ledger then, and only a line missing there is a lesson.
<!-- /rule-case-protocol -->

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
- 2026-09-14 updated: a knowledge lesson line carries {source:...}, the reference the lesson studied (case 144.1) · [[decision-case-144.1]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-15 updated: the reply that acknowledges a ratification has four parts: the Case heading with Changes, Notes when any, the Frontier as a checklist, the LEDGER block last (case 157) · [[decision-case-157]]
- 2026-09-15 updated: the shape of a Case in the chat: the story sections by explicit rules, given as the facts then depends on, then as behaviour only, a tasks section as the checklist of the Spec, code spans, one rule after the Case (case 159) · [[decision-case-159]]
- 2026-09-15 updated: the LEDGER block opens the acknowledging reply, the question closes it; supersedes 157 (case 167) · [[decision-case-167]]
- 2026-09-15 deferred · [[decision-case-179]]
- 2026-09-15 status: draft → built · cascade
- 2026-09-16 defer by decision-case-179 superseded · [[decision-case-181]]
- 2026-09-16 updated: How it works says eight sections, not six, and names the real parent; supersedes the defer of 179 (case 181) · [[decision-case-181]]
- 2026-09-16 deferred · [[decision-case-185]]
- 2026-09-16 defer by decision-case-185 superseded · [[decision-case-188]]
- 2026-09-16 updated: the Render rewritten by points 6, 7 and 9 of the model of 182; How it works dropped, its two facts moved into Purpose (case 188) · [[decision-case-188]]
- 2026-09-16 estimate estimate-case-protocol-case-form added · [[decision-case-188]]
- 2026-09-16 estimate estimate-case-protocol-acknowledging-reply added · [[decision-case-188]]
- 2026-09-16 estimate estimate-case-protocol-ledger-line-form added · [[decision-case-188]]
- 2026-09-16 status: built → draft · cascade
- 2026-09-16 updated: the Render of 195 corrected — the then sentence without the self-contradiction, the vault's answer in context, the create clause on rules and entities only, the reading line opens with its date and command; supersedes 195 (case 200.1) · [[decision-case-200.1]]
- 2026-09-16 updated: a written Criterion stands on an update as on a create; the Case's text is the Criterion of the one item that writes none (case 208.2) · [[decision-case-208.2]]
- 2026-09-16 status: draft → built · cascade
- 2026-09-18 updated: the text before a tool call waits for the next Stop, not "never kept"; a block is not called lost before that Stop; the page and render lines are ticked by generate and render (cases 224.2, 233) · [[decision-case-224.2]]
- 2026-09-18 status: built → draft · cascade
- 2026-09-18 status: draft → built · cascade
- 2026-09-18 updated: sprint is the third ticker of the Spec — the sprint lines (case 253.1) · [[decision-case-253.1]]
- 2026-09-18 status: built → draft · cascade
