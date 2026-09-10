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
  in the reply and the `Stop` hook writes them into `vault/raw/<date>/ledger.md`, each
  prefixed with the time of writing. The lines of 2026-09-09 written by hand before it
  carry no time; that is how the two are told apart.
- **The rituals of the new model exist since Slice 3.** `/retro` (the person), `/handoff` (the
  agent, refused by `guppi gate` while the tree is dirty), then the `librarian-guppi` agent:
  `materialize`, index check, synthesis, `generate`, `cleanup`, brief, commit. Pages are no
  longer written by hand; `brief.md` is written by the librarian. `docs/migration/` still
  holds the drafts of Work Mode and the plan of the move.
- **Each slice is its own Plan Mode and its own approval.** The approved plan is copied to
  `vault/raw/<date>/spec.md` by the `PostToolUse ExitPlanMode` hook `guppi spec` since
  Slice 2; the Specs of Slices 0–2 were copied by hand.

<!-- rule-case-protocol -->
## Case protocol

One reply is one Case, in the seven sections of `case-schema.md`: context, problem,
recommend, given, when, then, ratification. Never move to the next Case until this
one is ratified or deferred. Plan Mode does not end while a Frontier item is neither
ratified nor deferred.

A follow-up question that asks you to justify a choice does not split the Case; one
whose answer needs a new choice does — into sub-cases `N.1`, `N.2`. Ratifying a
parent does not ratify its children.

A Case renders as `## Case N — name`, then one blockquote per section: its first
line `**name:**`, its text on the following quoted lines, a blank line between
sections. In `given`, `when` and `then` every line after the first starts with a
bold operand: **＋** for one more condition or action, **－** for a limit or an
exception. `when` and `then` together are the criterion of the Estimate the Case
creates. Write short sentences, one idea each, in the active voice. A sub-case is
`### Case N.M — name` under its parent, with its own `given`, `when`, `then` and
`ratification`; the sections the children share live on the parent. The
`ratification` section ends with a preview of the ledger lines in an untagged
fence. The page content itself — fields, prose sections, the Estimate — is a YAML
block tagged `then` under the Case in the Spec, not in the chat; `guppi
materialize` reads it, and what is not in that block was signed by nobody.

Before a `create` without a `ref`, ask the vault first: does this exist, what
conflicts, what sits in `draft`, which tags fit. Put the answer in `given`.
Dispatch the `ask-guppi` agent with one short question.

Ledger lines are written by the `Stop` hook, from the reply, verbatim, each with
the time of writing. A record is a `- decision[...]`, `- estimate[...]` or
`- lesson[...]` line inside a fenced block opened with the `LEDGER` tag; the same
line anywhere else — bare, or in a block with another tag or none — is a preview
and is never written. A `create` line carries the ratified tags: `{tags:a,b}`.
Write the `- decision[...]` lines only in the reply that acknowledges ratification;
`- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson
exists. Without `/hi` the hook refuses and says so: tell the person, do not retry.
<!-- /rule-case-protocol -->

## Language

English for everything written into the repository: code, identifiers, comments, pages,
commit messages, documents. Russian for chat with the owner, and for the plan he reads in
order to approve it. English technical terms are not transliterated into Cyrillic.

## Style

Keep the facts and remove the sales pitch. Name a real source or remove the claim. Short
sentences, active voice, a common word over a term. Give the answer first. Say what is done
and what is not done; never leave the not-done implied.

## Commands

`make help` lists the targets. `make style` must be clean before every commit. Add no new
dependencies, Python or otherwise.
