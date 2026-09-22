# Case — schema

## The one rule

Nothing in the vault or the codebase changes without a Decision ratified by the human. The agent has full autonomy over *how* to implement something once its contract is ratified, and none over the contract itself. When unsure whether something needs ratification: it does. The vault is the only memory: no note outside the repository — not the harness's memory directory, not a file outside `vault/`; what is worth keeping is a `lesson` line or a Case on a Rule page (case 272.1).

`wiki/case-schema.md` — the Render of `rule-case-protocol`, loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md`, so the structure and the terms are present from the first turn of a working session rather than read as a file; the map of the vault is [[index]]. A session without `/hi` holds no Case: the ledger hook refuses it.

A Case is the unit of dialogue, not a vault page. It lives only inside a session. This schema exists because the Case is where content gets ratified: whatever is not in a Case was never signed by anyone.

**One agent response ≈ one Case.**

## Plan Mode and the Frontier

One reply is one Case, in the eight sections below. That is the form of Plan Mode. The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`; close its line in the reply that ends the item — `· case N` when ratified, `· work` when it needed no decision, `· defer case N` when deferred. Plan Mode does not end while a line is open; `/pre-spec` checks it. Never move to the next Case until this one is ratified or deferred.

## Sections

Eight, in this order. Each is one blockquote: the first line `**name:**`, the text on the following quoted lines.

| Section | Required | Content |
|---|---|---|
| `context` | yes | What this is about, in plain words. In Work Mode this may shrink to a one-line reference back to an earlier Case; it is never omitted. |
| `problem` | yes | What requires a decision. |
| `recommend` | yes | The agent's suggestion. Not carried onto the Decision page. |
| `given` | yes | The conditions of the behaviour: one per line, and only a condition a line of `then` depends on — the rule that constrains, the test that fixes the behaviour. The state of the pages the Case changes, what conflicts, what sits in `draft`, the vault's answer and which Estimates of the rule the Case touches go to `context` (case 188). |
| `when` | yes | The action that triggers the behaviour: a hook fires, a script runs, the person invokes a skill. For a change to a document, the moment someone reads it. |
| `then` | yes | What holds after the action, once the recommendation is accepted. Behaviour only: no Estimate block, no reading, no `supersedes` — those are lines of `tasks` (cases 159, 188). |
| `tasks` | yes | The work the Case leaves: a checklist, one line per page `update`, file, test, command, one-off migration and reading; no `contract` line, no "block N" line (case 188). In the chat a blockquote with the checklist; in the Spec the block tagged `tasks` — the same lines (case 159). |
| `ratification` | yes | The human's sign-off, question, or their own alternative. Ends with a preview of the ledger lines in an untagged fence, and the turn ends with a plain question in the chat, never a picker tool. A Case the person changed is shown again: `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`, and no `recommend` (cases 62, 163). |

## Operands

In `given`, `when` and `then`, the first line stands alone. Every further line starts with a bold operand: **＋** for one more condition or action — "and also", **－** for a limit or an exception — "but not", "does not apply here". One statement per line. `context`, `problem` and `recommend` carry no operand (case 159).

## Language

Short sentences. One idea per sentence. Active voice. A common word over a term. Russian in the chat with the owner: a Case is discussed there in Russian, all its sections. English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the Case enters the Spec translated, its slugs, field names and ledger lines unchanged (case 123). The language of the repository and of the chat as a standing rule is `rule-language`, in `CLAUDE.md`.

The story sections — `context`, `problem`, `recommend` — name the slug of the thing described only; no count of sentences, the shape of each bounds it: `context` opens with the mechanism in plain words — what the thing does today and where it goes wrong — for a reader who has not opened the pages, and closes with one sentence of bookkeeping — the state of the pages the Case changes, the vault's answer, the Estimates of the rule the Case touches and the ones it does not; a case number stands in `context` or `problem` only when the Case is about that case; no line numbers and no quotation unless the Case is about one; `problem` says what is wrong, or the question answered, in one paragraph; `recommend` says the choice and why, the rejected option in one sentence (case 267). `given` holds the conditions of the behaviour, one per line, and only a condition a line of `then` depends on: the rule that constrains, the test that fixes the behaviour; no state of pages, no history, no quotation for its own sake (case 188). `then` holds behaviour only; the bookkeeping is `tasks`. Slugs, file names and field values sit in code spans; bold is for section labels and operands only. In the chat one horizontal rule at most, after the Case or its last sub-case, and only when the agent's own text follows. The Spec keeps its form — the blockquotes in English, the `then` and `tasks` blocks — and the scripts read nothing of the chat form (case 159).

## `given`, `when` and `then` are the Criterion

The Case that creates an Estimate writes its Criterion; the Case that changes a promise names the Estimate by slug and replaces its Criterion whole. The scripts copy the Case's `given`, `when` and `then`, verbatim with their operands, as the Estimate's `Criterion` — `Given:`, `When:`, `Then:` — replacing what stood there and setting the page `pending`, unless the item wrote the Criterion under `sections` itself, which then stands, on an `update` as on a `create` (case 204); no `### case N` block, nothing appended, and nothing removed by a `{supersedes:case N}` — the replaced text stays in the Spec of its session and in History. A Case superseded in its own session, before the Spec is approved, leaves the Spec — no heading, no section, no `then` or `tasks` block — and the superseding Case is written whole; its text is not kept — its ledger lines name its targets, the `context` of the superseding Case says what it replaced — a Frontier line it closed is closed again by the superseding Case, and pre-spec catches a superseded Case still in the plan (case 299.1). Only a replaced Criterion sets `pending`: an `update` of a rule's `Purpose` touches no Estimate, an `update` of its `Render` touches the Estimate of the live reading of that Render (case 187). One promise per Case or sub-case: a Case that touches two promises is two sub-cases, and pre-spec asks for the split. Nothing is signed twice, and nothing is signed in two wordings (cases 72.1, 188). A `when` on a slash command names the path it covers — the person's typed command on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`, or both; the reading of a `then` that covers both takes both (case 173).

## The `then` block lives in the Spec

Ratifying "create entity-x" without seeing what that page will claim is an empty ratification. The human signs content, not the fact that a decision occurred. The content is a YAML block tagged `then` under the Case in the Spec — the plan the human approves at the end of Plan Mode — not in the chat. A list under each decision type present, one entry per target, `slug` first.

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

A `create` holds the fields the target schema needs a judgment for; prose for a body section goes under `sections`, keyed by the section name. A new promise is an explicit `create` of an Estimate: its own item, `ref` naming the target, its slug written in the Case — `estimate-<target minus its prefix>-<promise>` — with `kind`, `purpose`, `method` and `tags`; its Criterion is the Case's `given`, `when` and `then`, lifted by the scripts, or the text the item writes under `sections: Criterion` (cases 188, 194.1). A `create` of a rule or an entity carries no `method`, `estimate_kind` or `estimate_slug`; nothing is derived from it. A rule with several promises is a parent Case that creates the rule and one sub-case per Estimate. An `update` holds `set` (fields), `sections` (the whole new text of a section), `replace` (a list of `{old, new}` pairs, each `old` replaced by its `new` inside the body; one pair is a list of one, and a mapping under `replace` is a shape `generate` rejects), `change` (one line for History) and, when the page changes its slug, `rename` (the new slug, the same category prefix; the page moves and every link to it in the live pages follows, `origin`, History and Result kept — case 258.1); it carries no `contract`. An `update` of an Estimate carries `slug`, `set: {status: pending}` and `change` — and `set.method` when the page has no `method` field, since the recut brings the page to the shape of case 193 and `generate` refuses one without it (case 211); the scripts replace its Criterion with the Case's `given`, `when` and `then`, or keep the text the item wrote under `sections: Criterion` (case 204). An `update` that names a part alone — a field under `set` other than `status`, a `replace` pair, a section other than `Criterion` — carries no `set.status`: the scripts change that part, and the Criterion and the status stand, unless the part is inside the Criterion, which sets `pending` (case 296). One promise per Case or sub-case: two touched promises are two sub-cases, and pre-spec asks for the split. A `delete` holds `impact`, a `defer` a `type` and a `purpose`. A Rule-class file (`index.md`, `glossary.md`, a schema) is an `update` with `file` and `change`, applied by hand in Work Mode; `CLAUDE.md` and this file are not — they are rendered from `rule-claude-md` and `rule-case-protocol` and change by an `update` of one of them (cases 59.8, 273.1). New tags are declared under `new_tags` with a meaning and a Russian alias, under any Case of the Spec (case 61).

**The Spec is written as each Case is ratified**, into the plan file, in the reply that carries the Case's ledger lines: `context`, `problem`, `given`, `when`, `then`, the `then` block and a block tagged `tasks` — one `- [ ] <what>` per file to change, test to write, command to run, one-off migration, and one per reading of an Estimate the Case creates or sets `pending`, by its slug. `recommend` and `ratification` stay in the chat; code is Work Mode. Work Mode ticks the boxes on code, tests, migrations and `by hand` checks in `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73), in the reply that finishes the task; `generate` ticks the page lines and the `read` lines whose reading stands in the ledger, `render`, `sprint` and `glossary` the render, sprint and glossary lines (cases 226, 250, 270, 306); Retro counts the unticked (case 59.3). A render line is `- [ ] `uv run guppi render`: `<file>``, a sprint line `- [ ] `uv run guppi sprint``, a glossary line `- [ ] `uv run guppi glossary`` — the command in the first code span is what the ticker matches (case 235); a line of another form stays debt at Retro (case 279.1).

Derivable fields — `origin`, `status`, `parent` from `ref`, `children`, `code_ref`, `deferred_by` — are filled mechanically and are not written here. `guppi materialize` reads the blocks, and what is not in a block was signed by nobody.

**The slug is written in the Case**, and pre-spec checks it. Meaningful, never an index: `entity-cart`, `lesson-hooks-sessionstart-cannot-block`. The page's category comes from its prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`. Decision pages are the one exception: `decision-case-<N>`, one per Case, written by the script.

## The vault before a `create`

Before a `create` without a `ref`, ask the vault first: does this exist, what conflicts, what sits in `draft`, which tags fit. Dispatch the `ask-guppi` agent with one short question and put the answer in `context`. An `update` carries a `ref` and reads the page itself.

## The short form — deferred decisions

A deferred decision is its own Case in the short form — `## Case N — name`, then `context`, `problem`, and a `then` block with `defer:` carrying `slug`, `type` and `purpose`; no `recommend`, `given`, `when` or `then` section. It has two moments: the close of Plan Mode, when the person defers the items left open, and Retro, which ratifies no other decision. Either way the agent appends it to `raw/<date>/<hi HHMM>/spec.md` under the `## Deferred` heading before writing its ledger line, one line per target, so `materialize` finds it like any other Case; a defer line without its Case is marked `incomplete`. Two or more pages share one Case only when one context and one problem hold for all of them. A page-less Slice task goes to `sprint.md`, not into a defer. Taking a deferred decision up means building its full Case from its page — `context` and `problem` as they stand, then `recommend`, `given` (the vault asked), `when`, `then` — and writing `{supersedes:case N}` on the line. A `create`, `update` or `delete` at Retro waits for the next Plan Mode (cases 52.2, 56, 59.5).

## Splitting

If the human's reply to a Case is a follow-up question, the Case was not atomic. Detect this and propose splitting into sub-cases — recursive dotted ids, `1.1`, `1.1.1`. A sub-case is `### Case N.M — name` under its parent, with its own `when`, `then`, `tasks` and `ratification` (case 159), and its own `given` unless it is the parent's word for word; `context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing one there (case 60). Ratifying a parent does not ratify its children.

A question that only asks you to justify a choice already on the table ("why this approach?") does **not** split the Case. A question whose answer requires a new choice with its own consequences ("how will we handle X?") **does**.

**Never move to another Case until the current one is ratified or deferred.**

## What a Case produces

| Outcome | Ledger line |
|---|---|
| ratified decision | `- decision[case 12][update][rule-x]{ref:rule-x}` or `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` |
| a measurement taken | `- estimate[slug][passed\|failed] <date, command or place; the result>` (case 199) |
| something learned | `- lesson[error\|knowledge][slug]{tags:a,b} trigger: <...> root_cause: <...>` |

The id is `case N` — the word and a space — in the first bracket and in `{supersedes:case N}` alike; `{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1); `{addresses:<lesson slug>}` stands on a decision line whose Case closes the root cause of a lesson of this session — written when the lesson line already stands in the session's ledger, one mark per lesson; a lesson whose fix is ratified in another session gets no mark (case 284.2).

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

The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first; a heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; a heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last. Headings and labels in the language of the chat (case 167, supersedes 157).

## Slug collisions

Pre-spec checks the slug when the Case is formed. If it is nonetheless taken by generation time — a second decision in the same session claimed it, or a page was created by hand — **the generation script errors rather than renaming.**

Silently producing `entity-cart-2` would put a name in the vault that nobody ratified, and break the correspondence between a decision and its page. The librarian runs the script, so the librarian sees the error and judges what to do.

## The harness

The harness — hooks, skills, agents, `settings.json`, `CLAUDE.md`, this file — is rendered from `rules/`. A harness file changes through an `update` of its Rule page, never by hand; a hook refuses the edit.

## Not schema-governed

`brief.md`, `sprint.md`, `tags.md` and `log.md` are not pages and have no schema. Lint must not check them against the page template.
