---
type: rule
kind: Leaf
purpose: Prevents a Case from being built in a form the scripts cannot read, or shown for ratification without its content in view
status: built
enforcement: render
governs: vault/wiki/case-schema.md
render_mode: full
parent: "[[rule-plan-mode]]"
children: []
estimates: ["[[estimate-case-protocol-loaded]]", "[[estimate-case-protocol-case-form]]"]
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## Purpose

Prevents a Case from being built in a form the scripts cannot read, or shown for ratification without its content in view. This is instruction, not enforcement — no hook can judge a whole Case in substance — so it is written where the agent that builds a Case reads it: `vault/wiki/case-schema.md`, the Render of this page, which `case-guppi` reads whole with `ratification.md` before it answers. Until case 595 `/hi` loaded the file into the main agent's context with what the main agent does and the one rule; those moved to `rule-orchestration` and `rule-ratification`, with the child `rule-atomicity` and the Estimates of the behaviours that moved, so the main agent no longer carries the form of a Case it does not build. Until case 273 the Render was a section of `CLAUDE.md` and the schema a file edited by hand; the two said the same thing twice and were signed twice. `parent: rule-plan-mode` is the rule of the phase in which a Case is held (case 188).

## Render

<!-- rule-case-protocol -->
# Case — schema

`wiki/case-schema.md` — the Render of `rule-case-protocol`: the form of a Case, read whole by `case-guppi` with `ratification.md` before it answers. The main agent does not load it; what the main agent does with a Case — the dispatch, the showing, the acknowledging reply, the Frontier and the defers — is `orchestration.md`, the Render of `rule-orchestration` (case 595). The layout of the vault is [[rule-vault-layout]] and the phases of a session [[rule-session]].

A Case is the unit of dialogue, not a vault page. It lives only inside a session. This schema exists because the Case is where content gets ratified: whatever is not in a Case was never signed by anyone.

## Sections

Eight, in this order, under the heading `## Case N — name` — in the file of the Case at every showing and in the Spec, in {{documentation_lang}} (case 452.4); in the file and in the Spec a sub-case under `### Case N.M — name` beneath its parent (case 368). Each section is one blockquote: the first line `**name:**`, the text on the following quoted lines.

| Section | Required | Content |
|---|---|---|
| `context` | yes | What this is about, in plain words: prose only — the mechanism, where it goes wrong, the state of the pages, the vault's answer; no list of what the Case touches, that is `given` (case 378.1). In Work Mode this may shrink to a one-line reference back to an earlier Case; it is never omitted. |
| `problem` | yes | What requires a decision. |
| `recommend` | yes | The record of the choices: one item per question of the rounds of `case-guppi` — the question, what it recommended, the person's answer in English, both as they stood when the person answered it, or a note that it was not answered (case 557.2) — one per change the person asked for on the shown Case, and, with no round, one item of the recommendation ratified as built; an item may stand on the parent whatever it changed, and a sub-case carries only items whose answer changed it alone (cases 544.2, 568). Carried onto the Decision page as `## Recommend` (case 544.7). |
| `given` | yes | The frame of the Case, one thing per line: each page the Case creates or changes, each module, file and test its `tasks` touch, and the rule that constrains — its slug or path in a code span and a few words on its role, never its state; `when` and `then` name only what `given` names. It stays in the Case, in its Case file and in the Spec, and never enters an Estimate or a Decision page (cases 378.1, 513). |
| `when` | yes | The action that triggers the behaviour: a hook fires, a script runs, the person invokes a skill. For a change to a document, the moment someone reads it. |
| `then` | yes | What holds after the action, once the recommendation is accepted. Behaviour only: no Estimate block, no reading, no `supersedes` — those are lines of `tasks` (cases 159, 188). |
| `tasks` | yes | The work the Case leaves: a checklist, one line per page `update`, file, test, command, one-off migration and reading, a task that waits for the person's word before it runs opening its text with `stop:` (`rule-where-to-stop`, case 531.7); no `contract` line, no "block N" line (case 188). In the file of the Case a blockquote with the checklist, and under a line whose item writes content that content as sub-points — `old` and `new` of each `replace` or `reword` pair, the value of a `set`, the text of a `sections`, the fields of a `create` — each on its own sub-point (case 370); in the Spec the block tagged `tasks`, the same lines without the sub-points, whose content is the `then` block (case 159). |
| `ratification` | yes | In the chat, the preview of the ledger lines in an untagged fence and nothing else, each line in the form of the table of `ratification.md`; how a Case is shown, signed and shown again is `orchestration.md` (cases 355.1, 452.4). |

## Operands

In `given`, `when` and `then`, the first line stands alone. Every further line starts with a bold operand. **＋** is "and", in any of the three: one more thing in the frame, one more action of the trigger, one more result. **－** is "but", most often in `then`: an effect that must not occur, or an exception — only about what `given` or `when` names; a line that names nothing of them is not written. One statement per line. More than seven **＋** lines in `given` or `then` are a sign the Case is not atomic (`rule-atomicity`). `context`, `problem` and `recommend` carry no operand (case 378.6).

## Language

Short sentences. One idea per sentence. Active voice. A common word over a term. `case-guppi` writes the whole Case in {{documentation_lang}} (case 441). A Case it built reaches the person whole in {{documentation_lang}}, in the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that the agent sends (case 452.4); what the chat shows of it, and in which language, is `orchestration.md`. {{documentation_lang}} in everything that lands in the vault, in the manner of ASD-STE100 Simplified Technical English when that language is English: the Spec is written from the {{documentation_lang}} answer and the {{documentation_lang}} short form, slugs, field names and ledger lines unchanged (cases 123, 387.1, 441, 476.2). The language of the repository and of the chat as a standing rule is `rule-language`, in `CLAUDE.md`; the two are set in `rule-guppi-config`, rendered into `guppi.toml`.

The story sections — `context`, `problem`, `recommend` — name the slug of the thing described only; no count of sentences, the shape of each bounds it: `context` is prose: it opens with the mechanism in plain words — what the thing does today and where it goes wrong — for a reader who has not opened the pages, and closes with the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame, and why an Estimate of the rule is not touched; the list of what the Case touches is `given` (case 378.1); `context`, `problem` and `recommend` explain briefly — a sentence per part where one is enough, a part with nothing to say left out — and may name a case number as the source of a claim; no script judges their text but for the titles of the items of `recommend`, which the hook of `rule-case-check` compares with the questions of the rounds (case 544.3): the person does, and a complaint of their length or clarity is what changes them (case 449); `problem` says what is wrong, or the question answered, in one paragraph; `recommend` is a list, one item per question of the rounds: its first line the title of the question in bold as the round wrote it, then a sub-item `Recommended:` and a sub-item `Answer:`, the person's answer in English, both as they stood when the person answered that question; a later question that replaced an earlier one is an item of its own, a question asked in more than one round is one item, of the last round in which the person answered it, and a question never answered says so in its `Answer:` sub-item (case 557.2); a change the person asked for on the shown Case is an item `**Change**` with the lines `Asked:` and `Taken:`; a Case with no round has one item, a line `Recommended:` and the line `Answer: ratified as built` (case 544.2). `given` holds the frame, one thing per line: the pages, modules, files and tests the Case touches and the rule that constrains; no state, no history, no quotation (case 378.1). `then` holds behaviour only; the bookkeeping is `tasks`. `given`, `when` and `then` hold no count of items — pages, lines, Estimates, Cases, tests — since `when` and `then` become the Criterion of an Estimate and a count goes stale there first; a number that states a condition or a limit, such as more than 400 000 tokens, stands (case 449). Slugs, file names and field values sit in code spans; bold is for section labels and operands only, and for the title of a question of a round and the title of an item of `recommend`, as the grill-me template sets it (case 544.2). The Spec keeps its form — the blockquotes in {{documentation_lang}}, the `then` and `tasks` blocks — and the hook of `rule-spec-write` reads the chat form: a task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block, its sub-points its keys — `old` and `new` in pairs, `reword old` and `reword new`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, with as many backticks as the value needs — a value that holds a backtick takes its outer span padded by one space on each side, and the hook refuses one unpadded (case 402) — or a fenced block under the sub-point, its opening fence longer than any fence of the same character inside it (case 444.3); a Case off this form is not written, and the hook says why (cases 159, 387.2).

## `when` and `then` are the Criterion

The Case that creates an Estimate writes its Criterion; the Case that changes a promise names the Estimate by slug and replaces its Criterion whole. The scripts copy the Case's `when` and `then`, verbatim with their operands, as the Estimate's `Criterion` — `When:`, `Then:`; `given` stays in the Case file and in the Spec, so `when` names the trigger and the input it acts on, each thing by its slug or path, and the Estimate reads without the Case (case 378.2) — replacing what stood there and setting the page `pending`, unless the item wrote the Criterion under `sections` itself, which then stands, on an `update` as on a `create` (case 204); no `### case N` block, nothing appended, and nothing removed by a `{supersedes:case N}` — the replaced text stays in the Spec of its session and in History. A Case superseded in its own session leaves the Spec — no heading, no section, no `then` or `tasks` block: the `Stop` hook of `rule-spec-write` removes it from the plan file and, once it stands, `raw/<date>/<hi HHMM>/spec.md` (case 441) — and the superseding Case is written whole; its text is not kept — its ledger lines name its targets, the `context` of the superseding Case says what it replaced — a Frontier line it closed is closed again by the superseding Case, and pre-spec catches a superseded Case still in the plan (case 299.1). Only a replaced Criterion sets `pending`: an `update` of a rule's `Purpose` touches no Estimate, an `update` of its `Render` touches no Estimate of the live reading — that Estimate promises only that the file equals the Render and is loaded; the behaviour a changed paragraph describes is named in the Estimate of that behaviour (case 378.5). One promise per Case or sub-case: a Case that touches two promises is two sub-cases, and pre-spec asks for the split. Nothing is signed twice, and nothing is signed in two wordings (cases 72.1, 188). A `when` on a slash command names the path it covers — the person's typed command on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`, or both; the reading of a `then` that covers both takes both (case 173).

## The `then` block lives in the Spec

Ratifying "create entity-x" without seeing what that page will claim is an empty ratification. The human signs content, not the fact that a decision occurred. The content is a YAML block tagged `then` under the Case in the Spec — the plan the human approves at the end of Plan Mode — not in the chat, where its content stands as sub-points of `tasks` (case 370). A list under each decision type present, one entry per target, `slug` first.

```then
create:
  - slug: entity-cart
    type: entity
    kind: MOC
    purpose: Lets a buyer review an order before paying
    tags: [cart, checkout]
    sections:
      Purpose: |
        Until now items went straight from the catalogue to payment.
  - slug: estimate-cart-renders-in-time
    type: estimate
    ref: entity-cart
    kind: Research
    purpose: Whether the cart renders within 200ms, and what dominates the time if not
    method: measure the render at 10, 50 and 200 line items, against a seeded database
    tags: [cart, performance]
update:
  - slug: entity-checkout
    set: {tags: [cart, checkout, payment]}
    change: the cart precedes payment
  - slug: estimate-checkout-orders-the-steps
    set: {status: pending}
    change: the Criterion replaced whole — the cart precedes payment
```

A `create` holds the fields the target schema needs a judgment for; prose for a body section goes under `sections`, keyed by the section name. A new promise is an explicit `create` of an Estimate: its own item, `ref` naming the target, its slug written in the Case — `estimate-<target minus its prefix>-<promise>` — with `kind`, `purpose`, `method` and `tags`; its Criterion is the Case's `when` and `then`, lifted by the scripts, or the text the item writes under `sections: Criterion` (cases 188, 194.1). A rule with several promises is a parent Case that creates the rule and one sub-case per Estimate. An `update` holds `set` (fields), `sections` (the whole new text of a section), `replace` (a list of `{old, new}` pairs, each `old` replaced by its `new` inside the body; one pair is a list of one, and a mapping under `replace` is a shape `generate` rejects; an `old` matches inside one `##` section of the page — a render block is one section with its headings — never in History, a line break matching any whitespace, and hits the page once: an anchor that crosses a section heading never matches, and one that misses or hits twice fails the entry; an `old` that opens with spaces or tabs takes the spaces and tabs before its first word on the page too, so the indent of `new` replaces them, and a `new` that opens with spaces or tabs takes an `old` that opens with them, or pre-spec reports the pair — case 543), `reword` (a list of `{old, new}` pairs replaced as whole words over every live page of `wiki/`, the page of the item being the owner, for a word that changes everywhere — a slug goes through `rename`, case 274.1), `change` (one line for History) and, when the page changes its slug, `rename` (the new slug, the same category prefix; the page moves and every link to it in the live pages follows, `origin`, History and Result kept — case 258.1). An `update` of an Estimate carries `slug`, `set: {status: pending}` and `change`; the scripts replace its Criterion with the Case's `when` and `then`, or keep the text the item wrote under `sections: Criterion` (case 204). An `update` that names a part alone — a field under `set` other than `status`, a `replace` pair, a section other than `Criterion` — carries no `set.status`: the scripts change that part, and the Criterion and the status stand; a part inside the Criterion is refused — a promise changes only whole, by a Criterion replaced whole (case 378.4). A pair under `replace` or `reword` is signed only after the sentence around every match is read whole and what it names there is said, never from the line a grep printed (case 353). A Case that changes the behaviour of an existing page reads the page's `estimates` and gives an `update` to each one whose Criterion speaks of the change — read as the `then` block is written, not at pre-spec; an Estimate whose Criterion speaks of something else is left alone, since naming a spare one replaces a sound Criterion (cases 53.2, 353). One promise per Case or sub-case: two touched promises are two sub-cases, and pre-spec asks for the split. A `delete` holds `impact`, a `defer` a `type` and a `purpose`. `CLAUDE.md`, this file, `orchestration.md` and `ratification.md` are rendered from `rule-claude-md`, `rule-case-protocol`, `rule-orchestration` and `rule-ratification` and change by an `update` of one of them (cases 59.8, 273.1, 595). New tags are declared under `new_tags` with a meaning and a {{chat_lang}} alias, under any Case of the Spec (case 61).

**The Spec is written as each Case is ratified**, by the `Stop` hook of `rule-spec-write`, after the reply that carries the Case's ledger lines: it copies the Case as `case-guppi` answered it — the answer the check of `rule-case-check` stored, never a showing that differs from it, which is refused (case 437) — into the plan file, outside the repository, and, once `raw/<date>/<hi HHMM>/spec.md` stands, into it too, the ticks of its unchanged task lines kept (case 441). The Case holds `context`, `problem`, `recommend`, `given`, `when`, `then`, the `then` block and a block tagged `tasks` — one `- [ ] <what>` per file to change, test to write, command to run, one-off migration, and one per reading of an Estimate the Case creates or sets `pending`, by its slug. A `by hand` box is a check that Work Mode of the Case's own session takes; a check whose moment comes after that Work Mode — the librarian's run of the session or a later session — is no box: it is the reading of an Estimate, through the `read` line of one the Case creates or sets `pending` or through one its `context` names, or it is left to the `make lint` of the librarian's run, which the brief reports (case 606.1). `ratification` stays in the chat (case 544.5); code is Work Mode. Who ticks which line is `orchestration.md`. A render line is `- [ ] `uv run guppi render`: `<file>``, a sprint line `- [ ] `uv run guppi sprint``, a glossary line `- [ ] `uv run guppi glossary``, a close line `- [ ] `uv run guppi sprint-close --sprint <id> --apply …``, which the librarian runs and the command ticks (`rule-sprint-close`, case 628.1) — the command in the first code span is what the ticker matches (case 235); a line of another form stays debt at Retro (case 279.1).

Derivable fields — `origin`, `status`, `parent` from `ref`, `children`, `code_ref`, `deferred_by` — are filled mechanically and are not written here. `guppi materialize` reads the blocks, and what is not in a block was signed by nobody.

**The slug is written in the Case**, and pre-spec checks it. Meaningful, never an index: `entity-cart`, `lesson-hooks-sessionstart-cannot-block`. The page's category comes from its prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`. Decision pages are the one exception: `decision-case-<N>`, one per Case, written by the script.

## Who builds a Case

Every Case, in Plan Mode and in Work Mode, at its first showing and at every showing again, is built by the agent `case-guppi` (`rule-case-build`); how the main agent dispatches it, passes on the person's words and shows its answer is `orchestration.md`.

## Taking up a deferred decision

A deferred decision is written by the main agent in the short form that `orchestration.md` sets. Taking a deferred decision up means building its full Case from its page — `context` and `problem` as they stand, then `recommend`, `given` — the frame — `when`, `then`, the vault's answer in `context` (case 378.1) — and writing on one of its decision lines one `{supersedes:case N}` block for each Case in the page's `deferred_by`, so that every defer of the page is retired (case 429); the Case, or the sub-case, that carries the blocks also names the page on a decision line other than a `defer` — an `update` with only `change` when nothing on the page changes — since `generate` clears a defer only from the pages the superseding Case names. `/pre-spec` reports a Case that closes a Frontier line of the source `backlog` when no Case among it and its sub-cases both names the page and carries each block; the check of the answer of `case-guppi` sends back a Case that names the page of an open `backlog` line when no Case among it and its sub-cases in the answer both names the page and carries each block (case 467).

## Splitting

If the human's reply to a Case is a follow-up question, the Case was not atomic. Detect this and propose splitting into sub-cases — recursive dotted ids, `1.1`, `1.1.1`; whether a unit splits is the rule of atomicity in `ratification.md`. A sub-case is `### Case N.M — name` under its parent, with its own `when`, `then`, `tasks` and `ratification` (case 159), and its own `given` unless it is the parent's word for word — `materialize` takes a sub-case's `given` as it stands, so a sub-case with the parent's lines and more writes them all out, never a pointer to the parent's; `context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing `context` or `given` there (case 60); `problem` stands on the parent only, and the parent's `recommend` may carry every item, and a sub-case may carry its own `recommend` with items whose answer changed that sub-case alone (cases 544.2, 568). A Case with sub-cases stands in one file: the parent's `context`, `problem`, `recommend`, then every sub-case whole (case 355.2). A Case that has a decision line in the session's ledger and is built again in another shape — whole after sub-cases, with sub-cases after whole, or without a sub-case that has a decision line — is built under a new number, never its old one, and its decision lines carry one {supersedes:case N} for its old top-level number and one for each of its old numbers that has a decision line: the Spec hook keeps the old parts beside the new ones, a mark on a sub-case removes that sub-case alone, and the old lines stay in the ledger until a mark retires them. The check of the answer of case-guppi sends back a build that keeps the old number, and names the new number (case 610.1).

A question that only asks you to justify a choice already on the table ("why this approach?") does **not** split the Case. A question whose answer requires a new choice with its own consequences ("how will we handle X?") **does**.

## Slug collisions

Pre-spec checks the slug when the Case is formed. If it is nonetheless taken by generation time — a second decision in the same session claimed it, or a page was created by hand — **the generation script errors rather than renaming.**

Silently producing `entity-cart-2` would put a name in the vault that nobody ratified, and break the correspondence between a decision and its page. The librarian runs the script, so the librarian sees the error and judges what to do.

## Not schema-governed

`brief.md`, `sprint.md`, `tags.md` and `log.md` are not pages and have no schema. Lint must not check them against the page template.
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
- 2026-09-20 status: draft → built · cascade
- 2026-09-20 updated: the sentence on the story sections of the Render: context opens with the mechanism and closes with one sentence of bookkeeping, a case number only when the Case is about it, the cap of seven sentences dropped for the shape of each section (case 267) · [[decision-case-267]]
- 2026-09-20 updated: the tick sentence of the Render — readings ticked by generate, not by Work Mode (case 270.2) · [[decision-case-270.2]]
- 2026-09-20 updated: the page renders vault/wiki/case-schema.md in full, the five paragraphs of the old CLAUDE.md Render folded into the schema, the duplicates gone; parent rule-plan-mode (case 273.1) · [[decision-case-273.1]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 updated: the Spec paragraph names the form of the render and sprint lines the scripts tick (case 279.1) · [[decision-case-279.1]]
- 2026-09-21 updated: the mark {addresses:<lesson slug>} on a decision line whose Case closes the root cause of a lesson of this session (case 284.2) · [[decision-case-284.2]]
- 2026-09-21 updated: the one rule opens the schema, moved from CLAUDE.md; the opening line names the glossary among the files /hi loads (case 288.2) · [[decision-case-288.2]]
- 2026-09-21 updated: the Purpose names the glossary among the files /hi loads (case 290.3) · [[decision-case-290.3]]
- 2026-09-21 updated: the Spec paragraph names the field-only update of an Estimate — a part named changes alone, a part inside the Criterion sets pending (case 294) · [[decision-case-294]]
- 2026-09-22 updated: the Spec paragraph on the Criterion — a Case superseded in its own session leaves the Spec, the superseding Case is written whole (case 299.1) · [[decision-case-299.1]]
- 2026-09-22 updated: glossary is the fourth ticker of the Spec — the glossary lines (case 306.6) · [[decision-case-306.6]]
- 2026-09-22 child rule-atomicity added · [[decision-case-317]]
- 2026-09-22 updated: a MOC with the child rule-atomicity, whose marker line stands above Splitting (case 317) · [[decision-case-317]]
- 2026-09-22 updated: the map replaced by rule-vault-layout and rule-session; index.md out of the Rule-class list (case 318) · [[decision-case-318]]
- 2026-09-22 updated: the Rule-class file route is gone from the Case schema (case 320) · [[decision-case-320]]
- 2026-09-23 updated: the extra closing marker of rule-atomicity removed from the Render, a parent carrying one marker line per child — the hand fix of commit 94277ea signed after the fact (case 324) · [[decision-case-324]]
- 2026-09-23 updated: reword among the keys of an update, and the two steps of the author at the end of the description of an update (case 353, supersedes 332.1, 337, 340, 341 and 342) · [[decision-case-353]]
- 2026-09-23 updated: ratification in the chat is the ledger preview alone, the agent's text after one horizontal rule (case 355.1) · [[decision-case-355.1]]
- 2026-09-23 updated: a Case with sub-cases is shown in one reply, ratified at once or by ids (case 355.2) · [[decision-case-355.2]]
- 2026-09-23 updated: Plan Mode ends with no open line under Cases (case 356.1) · [[decision-case-356.1]]
- 2026-09-23 updated: the Plan Mode paragraph names the closer sprint (case 356.2) · [[decision-case-356.2]]
- 2026-09-23 updated: a Case opens with the heading `## Case N — name` in the chat and in the Spec (case 368) · [[decision-case-368]]
- 2026-09-23 updated: in the chat the content of an item stands as sub-points under its task line (case 370) · [[decision-case-370]]
- 2026-09-23 updated: a Case the agent finds changed after ratification is shown again before anything of the change is written (case 373) · [[decision-case-373]]
- 2026-09-23 updated: given is the frame of the Case, context is prose (case 378.1) · [[decision-case-378.1]]
- 2026-09-23 updated: the Criterion is the when and then of the Case; given stays in the Case (case 378.2) · [[decision-case-378.2]]
- 2026-09-23 updated: a Criterion changes only whole (case 378.4) · [[decision-case-378.4]]
- 2026-09-23 updated: the live reading of a Render does not depend on its content (case 378.5) · [[decision-case-378.5]]
- 2026-09-23 updated: the operands and and but, bounded by the frame (case 378.6) · [[decision-case-378.6]]
- 2026-09-23 updated: a lesson line written after the Case that closed its cause carries {addressed_by:case N} (case 379) · [[decision-case-379]]
- 2026-09-24 updated: the Case schema names the limit of a replace pair and of a sub-case's given (case 383) · [[decision-case-383]]
- 2026-09-24 updated: the language of the Case sections in the chat (case 387.1) · [[decision-case-387.1]]
- 2026-09-24 updated: the Spec is written by the hook of rule-spec-write, which reads the chat form (case 387.2) · [[decision-case-387.2]]
- 2026-09-24 updated: a ratified Case is shown whole again when what the scripts apply changed, as a DIFF when only its prose changed (case 387.3) · [[decision-case-387.3]]
- 2026-09-24 deferred · [[decision-case-389]]
- 2026-09-24 defer by decision-case-389 superseded · [[decision-case-390]]
- 2026-09-24 updated: the acknowledging reply of a re-ratification carries the LEDGER block again (case 390, supersedes 389) · [[decision-case-390]]
- 2026-09-24 updated: the frame of a Case checked by frame-guppi before the showing (case 391.2) · [[decision-case-391.2]]
- 2026-09-24 estimate estimate-case-protocol-checks-its-frame added · [[decision-case-391.2]]
- 2026-09-24 updated: the outer span of a value that opens or closes with a backtick is padded by one space (case 393) · [[decision-case-393]]
- 2026-09-25 updated: a value that holds a backtick takes its outer span padded by one space on each side (case 402) · [[decision-case-402]]
- 2026-09-25 updated: a defer is written in the reply that asks for it, the person's words its ratification (case 405) · [[decision-case-405]]
- 2026-09-25 estimate estimate-case-protocol-defers-in-one-reply added · [[decision-case-405]]
- 2026-09-25 updated: the story sections name no count of items unless the Case is about that count (case 406) · [[decision-case-406]]
- 2026-09-25 updated: the answer to a Stop hook's refusal after a LEDGER block is a reply of its own (case 414.2) · [[decision-case-414.2]]
- 2026-09-25 deferred · [[decision-case-416]]
- 2026-09-25 updated: every Case is built by case-guppi and shown unchanged; ask-guppi at pre-spec only (case 419.1) · [[decision-case-419.1]]
- 2026-09-25 ref `estimate-case-protocol-checks-its-frame` → `estimate-case-protocol-shows-the-built-case` · [[decision-case-419.1]]
- 2026-09-25 defer by decision-case-416 superseded · [[decision-case-419.2]]
- 2026-09-25 updated: the deferred Case is shown by the agent and written by the hook of rule-spec-write (case 421.2) · [[decision-case-421.2]]
- 2026-09-25 updated: an item left deferred as it stands is no decision, closed kept (case 421.4) · [[decision-case-421.4]]
- 2026-09-25 updated: a reading of an Estimate the session creates or updates waits for a later session (case 428.1) · [[decision-case-428.1]]
- 2026-09-25 updated: a decision line carries one {supersedes:case N} block per Case it supersedes; a deferred decision taken up names every Case of its deferred_by (case 429) · [[decision-case-429]]
- 2026-09-26 updated: Who builds a Case says that a showing the Stop comparison refuses is followed by the answer shown unchanged (case 435) · [[decision-case-435]]
- 2026-09-26 updated: the Spec hook copies the stored answer of case-guppi, not the showing (case 437) · [[decision-case-437]]
- 2026-09-26 updated: the Render names no key of the shape before case 189 (case 440.3) · [[decision-case-440.3]]
- 2026-09-26 updated: the main agent translates the prose of the English answer for the chat and writes a short-form Case in English; a ratified Case changes only through its case-guppi and is shown again whole; the prose DIFF and the translation before the approval go (case 441.2) · [[decision-case-441.2]]
- 2026-09-26 updated: the Spec hook writes into spec.md once it stands (case 441.6) · [[decision-case-441.6]]
- 2026-09-26 updated: the Stop hook removes a superseded Case from the Spec (case 441.7) · [[decision-case-441.7]]
- 2026-09-27 updated: the main agent shows a round of case-guppi translated and passes the person's answers verbatim (case 443.3) · [[decision-case-443.3]]
- 2026-09-27 updated: a fenced value opens with a fence longer than any fence inside it (case 444.3) · [[decision-case-444.3]]
- 2026-09-27 updated: the plan has no ratified copy, and the agent's edit of the plan is refused (cases 445.1, 445.2) · [[decision-case-445.2]]
- 2026-09-27 updated: the story sections explain briefly, may name a case number as a source, and are judged by the person; the rules on counts, line numbers and quotations in them removed; no count of items in given, when and then (case 449) · [[decision-case-449]]
- 2026-09-27 updated: the closers of a Frontier line — [x] an item ended, [-] put off as sprint · defer, backlog · kept or defer case N; an item of backlog.md left as it stands keeps its source (case 451.1) · [[decision-case-451.1]]
- 2026-09-27 updated: the acknowledging reply shows every line put off by its closer (case 451.10) · [[decision-case-451.10]]
- 2026-09-27 updated: a built Case is shown by the file the hook writes, sent by SendUserFile, with a short Russian text and its ratification in the chat; the headings, the tasks, a showing again and a Case with sub-cases follow (case 452.4) · [[decision-case-452.4]]
- 2026-09-27 updated: the chat holds a short Russian text and the ledger lines of a built Case; the Case is English whole in its file (case 452.5) · [[decision-case-452.5]]
- 2026-09-27 updated: a round of questions of case-guppi is shown in Russian line by line, each question keeping its ❓ **Qn** and ➡️ lines (case 458) · [[decision-case-458]]
- 2026-09-27 updated: the defer reply in Plan Mode ends with the Frontier and a question of what comes next, the open item or /pre-spec (case 461) · [[decision-case-461]]
- 2026-09-27 updated: the main agent shows the context of a first round translated in place before its first question (case 466.2) · [[decision-case-466.2]]
- 2026-09-27 updated: a Case that takes up a deferred decision names its page on a decision line; what pre-spec and the check of case-guppi's answer each report (case 467) · [[decision-case-467.1]]
- 2026-09-28 updated: the languages of the Case, the chat and the vault named by the placeholders set in rule-guppi-config; ASD-STE100 only for English (case 476.2) · [[decision-case-476.2]]
- 2026-09-28 updated: a request for a plain explanation is answered by the main agent with the skill wait-what; case-guppi is asked only for a fact of its Case and answers under a Fact line, which is not a round (case 477.3) · [[decision-case-477.3]]
- 2026-09-29 updated: a lesson's addressed_by mark names the sub-case whose decision line closes the cause (case 497.4) · [[decision-case-497.4]]
- 2026-09-29 updated: an update of an Estimate needs no set.method; generate refuses no recut without it (case 506.5) · [[decision-case-506.5]]
- 2026-09-29 updated: given stays in the Case file and the Spec, not on a Decision page (case 513.3) · [[decision-case-513.3]]
- 2026-09-29 deferred · [[decision-case-518]]
- 2026-09-29 updated: the short form quotes a value that holds a # after a space or a tab (case 521.4) · [[decision-case-521.4]]
- 2026-09-29 defer by decision-case-518 superseded · [[decision-case-523]]
- 2026-09-29 updated: the defer taken up: the question after a defer stands as written, the failure of session 1134 a slip whose cause case 508 removed (case 523, supersedes 518) · [[decision-case-523]]
- 2026-09-29 updated: the main agent shows a round with each quotation in its blockquote (case 524.3) · [[decision-case-524.3]]
- 2026-09-30 updated: the short form says YAML cuts a value at a # after a space and PyYAML refuses the block at a # after a tab (case 526) · [[decision-case-526]]
- 2026-09-30 updated: a task line that opens with stop: waits for the person's word (case 531.7) · [[decision-case-531.7]]
- 2026-09-30 updated: the reading and lesson lines of the run from /work to the end of Retro stand in the reply that ends Retro (case 531.8) · [[decision-case-531.8]]
- 2026-09-30 updated: a short defer has one moment, the close of Plan Mode; Retro puts nothing off (case 531.14) · [[decision-case-531.14]]
- 2026-09-30 updated: how the leading spaces and tabs of a replace pair match (case 543.3) · [[decision-case-543.3]]
- 2026-09-30 updated: recommend is the record of the rounds and stands in the Spec, its item titles in bold; a sub-case carries its own items and no problem (cases 544.2, 544.5) · [[decision-case-544.2]]
- 2026-09-30 updated: a script reads the titles of the items of recommend (case 544.3) · [[decision-case-544.3]]
- 2026-09-30 updated: a reply after the first reply of /hi that closes a Frontier line in Plan Mode with no ratification and no defer shows the Frontier and the question which item is next · [[decision-case-547]]
- 2026-09-30 estimate estimate-case-protocol-shows-the-frontier-after-a-closed-line added · [[decision-case-547]]
- 2026-09-30 updated: recommend holds one item per question, its recommendation and answer as they stood when the person answered it, as sub-items; a question never answered says so (case 557.2) · [[decision-case-557.2]]
- 2026-10-01 updated: one Case at a time holds outside the loop after the findings of pre-spec (case 561.2) · [[decision-case-561.2]]
- 2026-10-01 updated: the Frontier after a closed line asks nothing when no line under Cases is open (case 561.6) · [[decision-case-561.6]]
- 2026-10-01 updated: the defer reply asks nothing when no line under Cases is open (case 561.7) · [[decision-case-561.7]]
- 2026-10-01 updated: the acknowledging reply asks nothing when no line under Cases is open (case 561.8) · [[decision-case-561.8]]
- 2026-10-01 updated: the showing is one list under the heading of the top-level Case, what done means on each item, and one ratification; a refused reply that shows a round is followed by the round shown again with nothing before it (case 561.9) · [[decision-case-561.9]]
- 2026-10-01 updated: a question to discuss an item goes to its case-guppi and comes back under Fact (case 561.12) · [[decision-case-561.12]]
- 2026-10-01 estimate estimate-case-protocol-forwards-a-discussion-question added · [[decision-case-561.12]]
- 2026-10-01 updated: the main agent's own questions take the grill-me shape, but for the question of the next item, of an open A line, of a sign-off and of work or carry (case 561.13, supersedes the defer of case 546) · [[decision-case-561.13]]
- 2026-10-01 estimate estimate-case-protocol-asks-in-the-grill-me-shape added · [[decision-case-561.13]]
- 2026-10-01 updated: the harness comes before the Plan Mode instructions of Claude Code (case 561.14) · [[decision-case-561.14]]
- 2026-10-01 estimate estimate-case-protocol-puts-the-harness-before-plan-mode added · [[decision-case-561.14]]
- 2026-10-01 updated: an item of recommend may stand on the parent; a sub-case holds only items whose answer changed it alone (case 568) · [[decision-case-568]]
- 2026-10-01 updated: a later Frontier folds the open W lines into one line that lists their ids; the other open lines stand one per line (case 578.2) · [[decision-case-578.2]]
- 2026-10-01 updated: the main agent names in its prompt to case-guppi each Case of the session that changes a page the item names or acts at the same moment, with its id, a sentence and its case file (case 579.1) · [[decision-case-579.1]]
- 2026-10-01 estimate estimate-case-protocol-names-related-cases-in-the-dispatch added · [[decision-case-579.1]]
- 2026-10-02 updated: the Render keeps the form of a Case alone; the main agent's part moves to rule-orchestration, the one rule, the ledger lines, atomicity and the harness to rule-ratification; the file is read by case-guppi and no longer loaded by /hi; the purpose names what this rule alone prevents (case 595.6) · [[decision-case-595.6]]
- 2026-10-02 status: draft → built · cascade
- 2026-10-03 updated: a Case writes no by hand box whose moment comes after Work Mode of its session; such a check is the reading of an Estimate or the make lint of the librarian's run (case 606.1) · [[decision-case-606.1]]
- 2026-10-03 status: built → draft · cascade
- 2026-10-03 updated: Splitting: a Case ratified in the session that is built again in another shape takes a new number, its decision lines superseding its old top-level number and each old number with a line (case 610.1) · [[decision-case-610.1]]
- 2026-10-03 status: draft → built · cascade
- 2026-10-04 updated: the close line of a sprint is a task line form (case 628.1) · [[decision-case-628.1]]
