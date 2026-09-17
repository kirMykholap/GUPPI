# GUPPI

A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into.
The vault is `vault/`; its map is `vault/wiki/index.md`. Nothing in the vault or the codebase
changes without a Decision ratified by the human. You have full autonomy over *how* to
implement something once its contract is ratified, and none over the contract itself. When you
are unsure whether something needs ratification: it does.

## What is loaded here

The glossary and the Case schema arrive through the imports below, so the terms and the shape
of a Case are present from the first turn without a read.

@vault/wiki/glossary.md

@vault/wiki/case-schema.md

`vault/wiki/index.md` is not imported: it is the map of the vault and the rules that hold in
every phase, read section by section when a section is needed (§0 the one rule, §1 layout,
§2 Case protocol, §3 decisions, §4 ledger, §5 routing, §6 splitting, §7 estimates, §8 lessons
and insights, §10 librarian, §11 indexes, §12 where content comes from).

## Migration mode, since 2026-09-09

This repository is being moved from its earlier model onto the one in `index.md`. Until the
move closes:

- **The state a session starts from is `vault/wiki/brief.md`.** Read it first; nothing prints
  it yet. `vault/wiki/sprint.md` names the slices and what closes the sprint.
- **The ledger hook exists since Slice 1.** Lines are emitted in a ```` ```LEDGER ```` block
  in the reply and the `Stop` hook writes them into `vault/raw/<date>/<hi HHMM>/ledger.md`, the session's folder (case 103.1), each
  prefixed with the time of writing. The lines of 2026-09-09 written by hand before it
  carry no time; that is how the two are told apart.
- **The rituals of the new model exist since Slice 3.** `/retro` (the person, or the agent once the Spec's tasks are ticked), `/handoff` (the
  agent, refused by `guppi gate` while the tree is dirty), then the `librarian-guppi` agent:
  `materialize`, index check, synthesis, `generate`, `cleanup`, brief, commit. Pages are no
  longer written by hand; `brief.md` is written by the librarian. `docs/migration/` still
  holds the drafts of Work Mode and the plan of the move.
- **Each slice is its own Plan Mode and its own approval.** The approved plan is copied to `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder, by the `PostToolUse ExitPlanMode` hook `guppi spec` since Slice 2 (the folder since case 73); the Specs of Slices 0–2 were copied by hand.

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
`pending`, by its slug; no `recommend`, no `ratification`, no code. Work Mode ticks the boxes on code, tests, migrations and readings in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task; `generate` and `render` tick the page and render lines (case 226); Retro counts the unticked.

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

## Language

English for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. Russian for chat with the owner: a Case is discussed in the chat in Russian, all its sections, and enters the Spec translated into English. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. English technical terms are not transliterated into Cyrillic.

## Style

Keep the facts and remove the sales pitch. Name a real source or remove the claim. Short
sentences, active voice, a common word over a term. Give the answer first. Say what is done
and what is not done; never leave the not-done implied.

## Commands

`make help` lists the targets. `make style` must be clean before every commit. Add no new
dependencies, Python or otherwise.
