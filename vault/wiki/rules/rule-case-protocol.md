---
type: rule
kind: MOC
purpose: Prevents a decision from being acted on before it is ratified, or ratified without its content in view
status: draft
enforcement: render
governs: vault/wiki/case-schema.md
render_mode: full
parent: "[[rule-plan-mode]]"
children: ["[[rule-atomicity]]"]
estimates: ["[[estimate-case-protocol-loaded]]", "[[estimate-case-protocol-case-form]]", "[[estimate-case-protocol-acknowledging-reply]]", "[[estimate-case-protocol-ledger-line-form]]", "[[estimate-case-protocol-checks-its-frame]]", "[[estimate-case-protocol-defers-in-one-reply]]"]
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## Purpose

Prevents a decision from being acted on before it is ratified, or ratified without its
content in view. This is instruction, not enforcement — no hook can check "did you
finish the Frontier" or "did you wait for the sign-off" — so it is written where the
agent sees it in every working session: `vault/wiki/case-schema.md`, the Render of this
page, loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md` (cases 273.1, 288.1). A session without
`/hi` holds no Case — the ledger hook refuses — and carries none of this text; `CLAUDE.md`
keeps the description of the project, the language and the writing rules; the one rule opens this Render, and the glossary comes with it (case 288.2). Until case 273 the Render was a section of `CLAUDE.md`
and the schema a file edited by hand; the two said the same thing twice and were signed
twice. `parent: rule-plan-mode` is the rule of the phase in which a Case is held (case 188).

## Render

<!-- rule-case-protocol -->
# Case — schema

## The one rule

Nothing in the vault or the codebase changes without a Decision ratified by the human. The agent has full autonomy over *how* to implement something once its contract is ratified, and none over the contract itself. When unsure whether something needs ratification: it does. The vault is the only memory: no note outside the repository — not the harness's memory directory, not a file outside `vault/`; what is worth keeping is a `lesson` line or a Case on a Rule page (case 272.1).

`wiki/case-schema.md` — the Render of `rule-case-protocol`, loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md`, so the structure and the terms are present from the first turn of a working session rather than read as a file; the layout of the vault is [[rule-vault-layout]] and the phases of a session [[rule-session]]. A session without `/hi` holds no Case: the ledger hook refuses it.

A Case is the unit of dialogue, not a vault page. It lives only inside a session. This schema exists because the Case is where content gets ratified: whatever is not in a Case was never signed by anyone.

**One agent response ≈ one Case.**

## Plan Mode and the Frontier

One reply is one Case, in the eight sections below. That is the form of Plan Mode. The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`; close its line in the reply that ends the item — `· case N` when ratified, `· work` when it needed no decision, `· defer case N` when deferred, `[-] … · sprint` for an item of the sprint left for later — never `· defer case N` (case 356.2). Plan Mode does not end while a line under `## Cases` is open — a `W` line closes when its work is done (case 356.1); `/pre-spec` checks it. Never move to the next Case until this one is ratified or deferred.

## Sections

Eight, in this order, under the heading `## Case N — name` — in the chat at every showing, the name in the language of the chat; in the Spec the same heading in English; a sub-case under `### Case N.M — name` beneath its parent (case 368). Each section is one blockquote: the first line `**name:**`, the text on the following quoted lines.

| Section | Required | Content |
|---|---|---|
| `context` | yes | What this is about, in plain words: prose only — the mechanism, where it goes wrong, the state of the pages, the vault's answer; no list of what the Case touches, that is `given` (case 378.1). In Work Mode this may shrink to a one-line reference back to an earlier Case; it is never omitted. |
| `problem` | yes | What requires a decision. |
| `recommend` | yes | The agent's suggestion. Not carried onto the Decision page. |
| `given` | yes | The frame of the Case, one thing per line: each page the Case creates or changes, each module, file and test its `tasks` touch, and the rule that constrains — its slug or path in a code span and a few words on its role, never its state; `when` and `then` name only what `given` names. It stays in the Case and on the Decision page and never enters an Estimate (case 378.1). |
| `when` | yes | The action that triggers the behaviour: a hook fires, a script runs, the person invokes a skill. For a change to a document, the moment someone reads it. |
| `then` | yes | What holds after the action, once the recommendation is accepted. Behaviour only: no Estimate block, no reading, no `supersedes` — those are lines of `tasks` (cases 159, 188). |
| `tasks` | yes | The work the Case leaves: a checklist, one line per page `update`, file, test, command, one-off migration and reading; no `contract` line, no "block N" line (case 188). In the chat a blockquote with the checklist, and under a line whose item writes content that content as sub-points — `old` and `new` of each `replace` or `reword` pair, the value of a `set`, the text of a `sections`, the fields of a `create` — each on its own sub-point (case 370); in the Spec the block tagged `tasks`, the same lines without the sub-points, whose content is the `then` block (case 159). |
| `ratification` | yes | In the chat, the preview of the ledger lines in an untagged fence and nothing else; the human's sign-off, question or own alternative is their reply. The agent's own text stands after the Case, after one horizontal rule, and the turn ends with a plain question in the chat, never a picker tool (case 355.1). A Case the person changed, or one whose text or scope the agent finds wrong or too narrow after its ratification — in the Spec, at pre-spec or in Work Mode — is shown again. A Case not yet ratified is shown again whole. A ratified Case is, in Plan Mode, changed in the plan file first, and `rule-spec-reconcile` compares it with the ratified copy: when its `given`, `when`, `then`, `then` block or `tasks` changed, it is shown again — `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`, and no `recommend` (cases 62, 163); until it is ratified again, nothing of the change is acted on. When only its name, `context` or `problem` changed, the reply shows the change as a `DIFF` of the edit and asks for no ratification; the translation of the name, `context` and `problem` before the approval is no change and is not shown (cases 373, 387.3). In Work Mode a changed Case is shown again whole. |

## Operands

In `given`, `when` and `then`, the first line stands alone. Every further line starts with a bold operand. **＋** is "and", in any of the three: one more thing in the frame, one more action of the trigger, one more result. **－** is "but", most often in `then`: an effect that must not occur, or an exception — only about what `given` or `when` names; a line that names nothing of them is not written. One statement per line. More than seven **＋** lines in `given` or `then` are a sign the Case is not atomic (`rule-atomicity`). `context`, `problem` and `recommend` carry no operand (case 378.6).

## Language

Short sentences. One idea per sentence. Active voice. A common word over a term. Russian in the chat with the owner for the name of a Case, its `context`, `problem` and `recommend`, and the agent's own text; `given`, `when`, `then` and `tasks` — lines and sub-points — are English in the chat already, the words the vault will hold (case 387.1). English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the name, `context` and `problem` are translated in the Spec before its approval, slugs, field names and ledger lines unchanged (cases 123, 387.1). The language of the repository and of the chat as a standing rule is `rule-language`, in `CLAUDE.md`.

The story sections — `context`, `problem`, `recommend` — name the slug of the thing described only; no count of sentences, the shape of each bounds it: `context` is prose: it opens with the mechanism in plain words — what the thing does today and where it goes wrong — for a reader who has not opened the pages, and closes with the state of the pages the Case changes, the vault's answer, what `frame-guppi` found, and why an Estimate of the rule is not touched; the list of what the Case touches is `given` (case 378.1); a case number stands in `context` or `problem` only when the Case is about that case; no line numbers and no quotation unless the Case is about one; no count of items — lines, pages, Estimates, Cases — unless the Case is about that count: a count goes stale first, and what can be counted a script counts; `problem` says what is wrong, or the question answered, in one paragraph; `recommend` says the choice and why, the rejected option in one sentence (case 267). `given` holds the frame, one thing per line: the pages, modules, files and tests the Case touches and the rule that constrains; no state, no history, no quotation (case 378.1). `then` holds behaviour only; the bookkeeping is `tasks`. Slugs, file names and field values sit in code spans; bold is for section labels and operands only. In the chat one horizontal rule at most, after the Case or its last sub-case, and only when the agent's own text follows. The Spec keeps its form — the blockquotes in English, the `then` and `tasks` blocks — and the hook of `rule-spec-write` reads the chat form: a task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block, its sub-points its keys — `old` and `new` in pairs, `reword old` and `reword new`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, with as many backticks as the value needs — a value that holds a backtick takes its outer span padded by one space on each side, and the hook refuses one unpadded (case 402) — or a fenced block under the sub-point; a Case off this form is not written, and the hook says why (cases 159, 387.2).

## `when` and `then` are the Criterion

The Case that creates an Estimate writes its Criterion; the Case that changes a promise names the Estimate by slug and replaces its Criterion whole. The scripts copy the Case's `when` and `then`, verbatim with their operands, as the Estimate's `Criterion` — `When:`, `Then:`; `given` stays in the Case and on the Decision page, so `when` names the trigger and the input it acts on, each thing by its slug or path, and the Estimate reads without the Case (case 378.2) — replacing what stood there and setting the page `pending`, unless the item wrote the Criterion under `sections` itself, which then stands, on an `update` as on a `create` (case 204); no `### case N` block, nothing appended, and nothing removed by a `{supersedes:case N}` — the replaced text stays in the Spec of its session and in History. A Case superseded in its own session, before the Spec is approved, leaves the Spec — no heading, no section, no `then` or `tasks` block — and the superseding Case is written whole; its text is not kept — its ledger lines name its targets, the `context` of the superseding Case says what it replaced — a Frontier line it closed is closed again by the superseding Case, and pre-spec catches a superseded Case still in the plan (case 299.1). Only a replaced Criterion sets `pending`: an `update` of a rule's `Purpose` touches no Estimate, an `update` of its `Render` touches no Estimate of the live reading — that Estimate promises only that the file equals the Render and is loaded; the behaviour a changed paragraph describes is named in the Estimate of that behaviour (case 378.5). One promise per Case or sub-case: a Case that touches two promises is two sub-cases, and pre-spec asks for the split. Nothing is signed twice, and nothing is signed in two wordings (cases 72.1, 188). A `when` on a slash command names the path it covers — the person's typed command on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`, or both; the reading of a `then` that covers both takes both (case 173).

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

A `create` holds the fields the target schema needs a judgment for; prose for a body section goes under `sections`, keyed by the section name. A new promise is an explicit `create` of an Estimate: its own item, `ref` naming the target, its slug written in the Case — `estimate-<target minus its prefix>-<promise>` — with `kind`, `purpose`, `method` and `tags`; its Criterion is the Case's `when` and `then`, lifted by the scripts, or the text the item writes under `sections: Criterion` (cases 188, 194.1). A `create` of a rule or an entity carries no `method`, `estimate_kind` or `estimate_slug`; nothing is derived from it. A rule with several promises is a parent Case that creates the rule and one sub-case per Estimate. An `update` holds `set` (fields), `sections` (the whole new text of a section), `replace` (a list of `{old, new}` pairs, each `old` replaced by its `new` inside the body; one pair is a list of one, and a mapping under `replace` is a shape `generate` rejects; an `old` matches inside one `##` section of the page — a render block is one section with its headings — never in History, a line break matching any whitespace, and hits the page once: an anchor that crosses a section heading never matches, and one that misses or hits twice fails the entry), `reword` (a list of `{old, new}` pairs replaced as whole words over every live page of `wiki/`, the page of the item being the owner, for a word that changes everywhere — a slug goes through `rename`, case 274.1), `change` (one line for History) and, when the page changes its slug, `rename` (the new slug, the same category prefix; the page moves and every link to it in the live pages follows, `origin`, History and Result kept — case 258.1); it carries no `contract`. An `update` of an Estimate carries `slug`, `set: {status: pending}` and `change` — and `set.method` when the page has no `method` field, since the recut brings the page to the shape of case 193 and `generate` refuses one without it (case 211); the scripts replace its Criterion with the Case's `when` and `then`, or keep the text the item wrote under `sections: Criterion` (case 204). An `update` that names a part alone — a field under `set` other than `status`, a `replace` pair, a section other than `Criterion` — carries no `set.status`: the scripts change that part, and the Criterion and the status stand; a part inside the Criterion is refused — a promise changes only whole, by a Criterion replaced whole (case 378.4). A pair under `replace` or `reword` is signed only after the sentence around every match is read whole and what it names there is said, never from the line a grep printed (case 353). A Case that changes the behaviour of an existing page reads the page's `estimates` and gives an `update` to each one whose Criterion speaks of the change — read as the `then` block is written, not at pre-spec; an Estimate whose Criterion speaks of something else is left alone, since naming a spare one replaces a sound Criterion (cases 53.2, 353). One promise per Case or sub-case: two touched promises are two sub-cases, and pre-spec asks for the split. A `delete` holds `impact`, a `defer` a `type` and a `purpose`. `CLAUDE.md` and this file are rendered from `rule-claude-md` and `rule-case-protocol` and change by an `update` of one of them (cases 59.8, 273.1). New tags are declared under `new_tags` with a meaning and a Russian alias, under any Case of the Spec (case 61).

**The Spec is written as each Case is ratified**, by the `Stop` hook of `rule-spec-write`, after the reply that carries the Case's ledger lines: it copies the Case from the reply that showed it into the plan file and into the ratified copy `<plan>.ratified.md` beside it, outside the repository; the agent creates the plan file with its title line before the first Case of the session (case 387.2). The Case holds `context`, `problem`, `given`, `when`, `then`, the `then` block and a block tagged `tasks` — one `- [ ] <what>` per file to change, test to write, command to run, one-off migration, and one per reading of an Estimate the Case creates or sets `pending`, by its slug. `recommend` and `ratification` stay in the chat; code is Work Mode. Work Mode ticks the boxes on code, tests, migrations and `by hand` checks in `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73), in the reply that finishes the task; `generate` ticks the page lines and the `read` lines whose reading stands in the ledger, `render`, `sprint` and `glossary` the render, sprint and glossary lines (cases 226, 250, 270, 306); Retro counts the unticked (case 59.3). A render line is `- [ ] `uv run guppi render`: `<file>``, a sprint line `- [ ] `uv run guppi sprint``, a glossary line `- [ ] `uv run guppi glossary`` — the command in the first code span is what the ticker matches (case 235); a line of another form stays debt at Retro (case 279.1).

Derivable fields — `origin`, `status`, `parent` from `ref`, `children`, `code_ref`, `deferred_by` — are filled mechanically and are not written here. `guppi materialize` reads the blocks, and what is not in a block was signed by nobody.

**The slug is written in the Case**, and pre-spec checks it. Meaningful, never an index: `entity-cart`, `lesson-hooks-sessionstart-cannot-block`. The page's category comes from its prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`. Decision pages are the one exception: `decision-case-<N>`, one per Case, written by the script.

## The vault before a `create`

Before a `create` without a `ref`, ask the vault first: does this exist, what conflicts, what sits in `draft`, which tags fit. Dispatch the `ask-guppi` agent with one short question and put the answer in `context`. An `update` carries a `ref` and reads the page itself. Before the first showing of a Case that changes the behaviour of a rule or of a hook, the agent dispatches `frame-guppi` ([[rule-frame-check]]) with the lines of the Case's `given` and a few lines on what it changes — in the prompt of the call, not in the chat — and fixes each contradiction it returns before the showing, or says why it stands; before a showing again it sends only the lines of `given` added since and the pages changed since. A Case that changes no behaviour of a rule or a hook dispatches nothing; the pages the agent edits by a `replace` pair it reads itself (case 391.2).

## The short form — deferred decisions

A deferred decision is its own Case in the short form — `## Case N — name`, then `context`, `problem`, and a `then` block with `defer:` carrying `slug`, `type` and `purpose`; no `recommend`, `given`, `when`, `then` or `ratification` section. It has two moments: the close of Plan Mode, when the person defers the items left open, and Retro, which ratifies no other decision. Either way the person's words asking for the defer are its ratification: in the same reply the agent appends it under the `## Deferred` heading of the plan file, or of `raw/<date>/<hi HHMM>/spec.md` at Retro, shows it, and ends the reply with its ledger line — in Plan Mode then the Frontier with the line closed `[-] … · defer case N` — and asks nothing about it; a wording the person corrects is a new short Case with `{supersedes:case N}`, written the same way (case 405). It stands there before its ledger line, one line per target, so `materialize` finds it like any other Case; a defer line without its Case is marked `incomplete`. Two or more pages share one Case only when one context and one problem hold for all of them. A page-less Slice task goes to `sprint.md`, not into a defer. Taking a deferred decision up means building its full Case from its page — `context` and `problem` as they stand, then `recommend`, `given` — the frame — `when`, `then`, the vault's answer in `context` (case 378.1) — and writing `{supersedes:case N}` on the line. A `create`, `update` or `delete` at Retro waits for the next Plan Mode (cases 52.2, 56, 59.5).

<!-- rule-atomicity -->

## Splitting

If the human's reply to a Case is a follow-up question, the Case was not atomic. Detect this and propose splitting into sub-cases — recursive dotted ids, `1.1`, `1.1.1`. A sub-case is `### Case N.M — name` under its parent, with its own `when`, `then`, `tasks` and `ratification` (case 159), and its own `given` unless it is the parent's word for word — `materialize` takes a sub-case's `given` as it stands, so a sub-case with the parent's lines and more writes them all out, never a pointer to the parent's; `context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing one there (case 60). Ratifying a parent does not ratify its children. A Case with sub-cases is shown in one reply — the parent's `context`, `problem`, `recommend`, then every sub-case whole; the person ratifies them all at once or names the ids, and the acknowledging reply carries one `LEDGER` block with the lines of every sub-case ratified, one heading `## Case N — ratified` naming those ids, and one Frontier; a sub-case the person questions or changes is shown again alone (case 355.2).

A question that only asks you to justify a choice already on the table ("why this approach?") does **not** split the Case. A question whose answer requires a new choice with its own consequences ("how will we handle X?") **does**.

**Never move to another Case until the current one is ratified or deferred.**

## What a Case produces

| Outcome | Ledger line |
|---|---|
| ratified decision | `- decision[case 12][update][rule-x]{ref:rule-x}` or `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` |
| a measurement taken | `- estimate[slug][passed\|failed] <date, command or place; the result>` (case 199) |
| something learned | `- lesson[error\|knowledge][slug]{tags:a,b} trigger: <...> root_cause: <...>` |

The id is `case N` — the word and a space — in the first bracket and in `{supersedes:case N}` alike; `{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1); `{addresses:<lesson slug>}` stands on a decision line whose Case closes the root cause of a lesson of this session — written when the lesson line already stands in the session's ledger, one mark per lesson; a lesson line written after the Case of this session that closed its cause carries `{addressed_by:case N}` instead, naming that Case — one of the two marks per pair, by the order of the lines (case 379); a lesson whose fix is ratified in another session gets no mark (case 284.2).

**Decision lines are markup only** — their content already sits ratified in the Spec, so the
line just names what happens to which page, and the tags a `create` was ratified with.

**Estimate and lesson lines carry their text inline.** Their content is born in the moment
and exists nowhere else: a measurement taken after the tests were written, a failure
understood while still fresh. There is nothing in the Spec to point at.

An `estimate[...]` line does not replace the `decision[...]` that created the page — the
decision made it exist, the estimate line fills it.

Only the **main agent** writes ledger lines. A subagent that takes a measurement returns it; the main agent records it. A subagent that hits a fork stops and returns — it never decides.

Ledger lines are written by the `Stop` hook, from the reply, verbatim, each with the time of writing. A record is a `- decision[...]`, `- estimate[...]` or `- lesson[...]` line inside a fenced block opened with the `LEDGER` tag; the same line anywhere else — bare, or in a block with another tag or none — is a preview and is never written. A `create` line carries the ratified tags: `{tags:a,b}`. A `knowledge` lesson line carries `{source:...}`, the url or reference the lesson studied — a file of the harness, a probe, a client version; the schema requires it, and a line without it is `incomplete: [source]` in the yaml and a lint finding on the page. An `error` lesson never carries one. Write the `- decision[...]` lines only in the reply that acknowledges ratification; `- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson exists, an `estimate[...]` line opening with the date of the reading and the command or the place it was read (case 199). Without `/hi` the hook refuses and says so: tell the person, do not retry. A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call waits for the next `Stop` of the session, and the last reply of a session has none. A block a tool call did follow is not lost until that `Stop` has passed: check the ledger then, and only a line missing there is a lesson.

## The acknowledging reply

The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first; a heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; a heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last. Headings and labels in the language of the chat (case 167, supersedes 157). The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification: the ledger hook does not append a line it already holds, and the hook of `rule-spec-write` writes a Case into the Spec only after a reply that carries its lines (case 390).

## Slug collisions

Pre-spec checks the slug when the Case is formed. If it is nonetheless taken by generation time — a second decision in the same session claimed it, or a page was created by hand — **the generation script errors rather than renaming.**

Silently producing `entity-cart-2` would put a name in the vault that nobody ratified, and break the correspondence between a decision and its page. The librarian runs the script, so the librarian sees the error and judges what to do.

## The harness

The harness — hooks, skills, agents, `settings.json`, `CLAUDE.md`, this file — is rendered from `rules/`. A harness file changes through an `update` of its Rule page, never by hand; a hook refuses the edit.

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
