# Case — schema

`wiki/case-schema.md` — imported into `CLAUDE.md`, so the structure is loaded at session start rather than read as a file; the map of the vault is [[index]].

A Case is the unit of dialogue, not a vault page. It lives only inside a session. This schema exists because the Case is where content gets ratified: whatever is not in a Case was never signed by anyone.

**One agent response ≈ one Case.**

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

Short sentences. One idea per sentence. Active voice. A common word over a term. Russian in the chat with the owner: a Case is discussed there in Russian, all its sections. English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the Case enters the Spec translated, its slugs, field names and ledger lines unchanged (case 123).

The story sections — `context`, `problem`, `recommend` — name the slug of the thing described only and run to seven sentences each at most: `context` says what the thing is and how it works today, for a reader who has not opened the pages — the state of the pages the Case changes, the vault's answer, and which Estimates of the rule the Case touches and which it does not — with no line numbers and no quotation unless the Case is about one; `problem` says what is wrong, or the question answered, in one paragraph; `recommend` says the choice and why, the rejected option in one sentence. `given` holds the conditions of the behaviour, one per line, and only a condition a line of `then` depends on: the rule that constrains, the test that fixes the behaviour; no state of pages, no history, no quotation for its own sake (case 188). `then` holds behaviour only; the bookkeeping is `tasks`. Slugs, file names and field values sit in code spans; bold is for section labels and operands only. In the chat one horizontal rule at most, after the Case or its last sub-case, and only when the agent's own text follows. The Spec keeps its form — the blockquotes in English, the `then` and `tasks` blocks — and the scripts read nothing of the chat form (case 159).

## `given`, `when` and `then` are the Criterion

The Case that creates an Estimate writes its Criterion; the Case that changes a promise names the Estimate by slug and replaces its Criterion whole. The scripts copy the Case's `given`, `when` and `then`, verbatim with their operands, as the Estimate's `Criterion` — `Given:`, `When:`, `Then:` — replacing what stood there and setting the page `pending`, unless the item wrote the Criterion under `sections` itself, which then stands, on an `update` as on a `create` (case 204); no `### case N` block, nothing appended, and nothing removed by a `{supersedes:case N}` — the replaced text stays in the Spec of its session and in History. Only a replaced Criterion sets `pending`: an `update` of a rule's `Purpose` touches no Estimate, an `update` of its `Render` touches the Estimate of the live reading of that Render (case 187). One promise per Case or sub-case: a Case that touches two promises is two sub-cases, and pre-task asks for the split. Nothing is signed twice, and nothing is signed in two wordings (cases 72.1, 188). A `when` on a slash command names the path it covers — the person's typed command on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`, or both; the reading of a `then` that covers both takes both (case 173).

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

A `create` holds the fields the target schema needs a judgment for; prose for a body section goes under `sections`, keyed by the section name. A new promise is an explicit `create` of an Estimate: its own item, `ref` naming the target, its slug written in the Case — `estimate-<target minus its prefix>-<promise>` — with `kind`, `purpose`, `method` and `tags`; its Criterion is the Case's `given`, `when` and `then`, lifted by the scripts, or the text the item writes under `sections: Criterion` (cases 188, 194.1). A `create` of a rule or an entity carries no `method`, `estimate_kind` or `estimate_slug`; nothing is derived from it. A rule with several promises is a parent Case that creates the rule and one sub-case per Estimate. An `update` holds `set` (fields), `sections` (the whole new text of a section), `replace` (a list of `{old, new}` pairs, each `old` replaced by its `new` inside the body; one pair is a list of one, and a mapping under `replace` is a shape `generate` rejects) and `change` (one line for History); it carries no `contract`. An `update` of an Estimate carries `slug`, `set: {status: pending}` and `change` — and `set.method` when the page has no `method` field, since the recut brings the page to the shape of case 193 and `generate` refuses one without it (case 211); the scripts replace its Criterion with the Case's `given`, `when` and `then`, or keep the text the item wrote under `sections: Criterion` (case 204). One promise per Case or sub-case: two touched promises are two sub-cases, and pre-task asks for the split. A `delete` holds `impact`, a `defer` a `type` and a `purpose`. A Rule-class file (`index.md`, `glossary.md`, this file, a schema) is an `update` with `file` and `change`, applied by hand in Work Mode; `CLAUDE.md` is not one — it is rendered from `rule-claude-md` and `rule-case-protocol` and changes by an `update` of one of them (case 59.8). New tags are declared under `new_tags` with a meaning and a Russian alias, under any Case of the Spec (case 61).

**The Spec is written as each Case is ratified**, into the plan file, in the reply that carries the Case's ledger lines: `context`, `problem`, `given`, `when`, `then`, the `then` block and a block tagged `tasks` — one `- [ ] <what>` per file to change, test to write, command to run, one-off migration, and one per reading of an Estimate the Case creates or sets `pending`, by its slug. `recommend` and `ratification` stay in the chat; code is Work Mode. Work Mode ticks the boxes in `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73), in the reply that finishes the task; Retro counts the unticked (case 59.3).

Derivable fields — `origin`, `status`, `parent` from `ref`, `children`, `code_ref`, `deferred_by` — are filled mechanically and are not written here. `guppi materialize` reads the blocks, and what is not in a block was signed by nobody.

**The slug is written in the Case**, and pre-task checks it. Meaningful, never an index: `entity-cart`, `lesson-hooks-sessionstart-cannot-block`. The page's category comes from its prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`. Decision pages are the one exception: `decision-case-<N>`, one per Case, written by the script.

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

The id is `case N` — the word and a space — in the first bracket and in `{supersedes:case N}` alike; `{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1).

**Decision lines are markup only** — their content already sits ratified in the Spec, so the
line just names what happens to which page, and the tags a `create` was ratified with.

**Estimate and lesson lines carry their text inline.** Their content is born in the moment
and exists nowhere else: a measurement taken after the tests were written, a failure
understood while still fresh. There is nothing in the Spec to point at.

An `estimate[...]` line does not replace the `decision[...]` that created the page — the
decision made it exist, the estimate line fills it.

Only the **main agent** writes ledger lines. A subagent that takes a measurement returns it; the main agent records it. A subagent that hits a fork stops and returns — it never decides.

## Slug collisions

Pre-task checks the slug when the Case is formed. If it is nonetheless taken by generation time — a second decision in the same session claimed it, or a page was created by hand — **the generation script errors rather than renaming.**

Silently producing `entity-cart-2` would put a name in the vault that nobody ratified, and break the correspondence between a decision and its page. The librarian runs the script, so the librarian sees the error and judges what to do.

## Not schema-governed

`brief.md`, `sprint.md`, `tags.md` and `log.md` are not pages and have no schema. Lint must not check them against the page template.
