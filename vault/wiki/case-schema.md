# Case — schema

`wiki/case-schema.md` — imported into `CLAUDE.md`, so the structure is loaded at session start rather than read as a file; the map of the vault is [[index]].

A Case is the unit of dialogue, not a vault page. It lives only inside a session. This schema exists because the Case is where content gets ratified: whatever is not in a Case was never signed by anyone.

**One agent response ≈ one Case.**

## Sections

Seven, in this order. Each is one blockquote: the first line `**name:**`, the text on the following quoted lines.

| Section | Required | Content |
|---|---|---|
| `context` | yes | What this is about, in plain words. In Work Mode this may shrink to a one-line reference back to an earlier Case; it is never omitted. |
| `problem` | yes | What requires a decision. |
| `recommend` | yes | The agent's suggestion. Not carried onto the Decision page. |
| `given` | yes | How things work today: the rules and pages this touches, what conflicts, what sits in `draft`. The pre-task result lives here. This is what determines whether the decision can be a `create` at all. |
| `when` | yes | The action that triggers the behaviour: a hook fires, a script runs, the person invokes a skill. For a change to a document, the moment someone reads it. |
| `then` | yes | What holds after the action, once the recommendation is accepted. |
| `ratification` | yes | The human's sign-off, question, or their own alternative. Ends with a preview of the ledger lines in an untagged fence, and the turn ends with a plain question in the chat, never a picker tool. A Case the person changed is shown again: `context` and `problem` if they changed, always `given`, `when`, `then`, `ratification`, and no `recommend` (case 62). |

## Operands

In `given`, `when` and `then`, the first line stands alone. Every further line starts with a bold operand: **＋** for one more condition or action, **－** for a limit or an exception. One statement per line.

## Language

Short sentences. One idea per sentence. Active voice. A common word over a term. Russian in the chat with the owner: a Case is discussed there in Russian, all its sections. English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the Case enters the Spec translated, its slugs, field names and ledger lines unchanged (case 123).

## `when` and `then` are the criterion

The Case that creates a Leaf also creates its Estimate; the Case that changes the Leaf's contract changes the Estimate. The scripts copy the Case's `when` and `then`, verbatim with their operands, as the `### case N` block of the Estimate's `Criterion`, and its `problem` as the Estimate's `Context` at birth. A later line with `{supersedes:case N}` removes the block of case N. One contract per Case or sub-case: a Case that changes two contracts is split, and pre-task asks for the split. Nothing is signed twice, and nothing is signed in two wordings (case 72.1).

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
    method: measure the render at 10, 50 and 200 line items, against a seeded database
    estimate_kind: Research
update:
  - slug: entity-checkout
    contract: changed
    set: {tags: [cart, checkout, payment]}
    change: the cart precedes payment
```

A `create` holds the fields the target schema needs a judgment for; prose for a body section goes under `sections`, keyed by the section name. A `create` of a Leaf also carries `method` (required): how the check of its `when` and `then` is made. The Estimate is derived from the Case, with no nested `estimate` and no ledger line of its own: its slug is `estimate-<target minus its prefix>` (`entity-cart` → `estimate-cart`), its kind `QA` unless the item says `estimate_kind: Research`; `estimate_slug` names it only when the derived slug collides with a live page. The two keys carry the `estimate_` prefix because `kind` and `slug` on the item are the target page's own fields: an unprefixed `kind` would land in the page's frontmatter and overwrite it (case 86). A MOC gets an Estimate the same way, only when its `create` carries `method` (case 72.1). An `update` holds `set` (fields), `sections` (the whole new text of a section), `replace` (a list of `{old, new}` pairs, each `old` replaced by its `new` inside the body; one pair is a list of one, and a mapping under `replace` is a shape `generate` rejects) and `change` (one line for History). An `update` of a Leaf carries `contract: same` or `contract: changed`. With `contract: changed` the scripts append the Case's `when` and `then` to its Estimate as a `### case N` block and set the Estimate `pending`; `method` is written only when the way of checking changes. One contract per Case or sub-case: two changed contracts in one Case are two sub-cases, and pre-task asks for the split. A new Estimate is made only for a condition that fails and is fixed apart, with its slug named in the Case (case 53.2). A `delete` holds `impact`, a `defer` a `type` and a `purpose`. A Rule-class file (`index.md`, `glossary.md`, this file, a schema) is an `update` with `file` and `change`, applied by hand in Work Mode; `CLAUDE.md` is not one — it is rendered from `rule-claude-md` and `rule-case-protocol` and changes by an `update` of one of them (case 59.8). New tags are declared under `new_tags` with a meaning and a Russian alias, under any Case of the Spec (case 61).

**The Spec is written as each Case is ratified**, into the plan file, in the reply that carries the Case's ledger lines: `context`, `problem`, `given`, `when`, `then`, the `then` block and a block tagged `tasks` — one `- [ ] <what>` per file to change, test to write, command to run, one-off migration, and one per reading of an Estimate the Case creates or sets `pending`, by its slug. `recommend` and `ratification` stay in the chat; code is Work Mode. Work Mode ticks the boxes in `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73), in the reply that finishes the task; Retro counts the unticked (case 59.3).

Derivable fields — `origin`, `status`, `parent` from `ref`, `children`, `code_ref`, `deferred_by` — are filled mechanically and are not written here. `guppi materialize` reads the blocks, and what is not in a block was signed by nobody.

**The slug is written in the Case**, and pre-task checks it. Meaningful, never an index: `entity-cart`, `lesson-hooks-sessionstart-cannot-block`. The page's category comes from its prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`. Decision pages are the one exception: `decision-case-<N>`, one per Case, written by the script.

## The short form — deferred decisions

A deferred decision is its own Case in the short form — `## Case N — name`, then `context`, `problem`, and a `then` block with `defer:` carrying `slug`, `type` and `purpose`; no `recommend`, `given`, `when` or `then` section. It has two moments: the close of Plan Mode, when the person defers the items left open, and Retro, which ratifies no other decision. Either way the agent appends it to `raw/<date>/<hi HHMM>/spec.md` under the `## Deferred` heading before writing its ledger line, one line per target, so `materialize` finds it like any other Case; a defer line without its Case is marked `incomplete`. Two or more pages share one Case only when one context and one problem hold for all of them. A page-less Slice task goes to `sprint.md`, not into a defer. Taking a deferred decision up means building its full Case from its page — `context` and `problem` as they stand, then `recommend`, `given` (the vault asked), `when`, `then` — and writing `{supersedes:case N}` on the line. A `create`, `update` or `delete` at Retro waits for the next Plan Mode (cases 52.2, 56, 59.5).

## Splitting

If the human's reply to a Case is a follow-up question, the Case was not atomic. Detect this and propose splitting into sub-cases — recursive dotted ids, `1.1`, `1.1.1`. A sub-case is `### Case N.M — name` under its parent, with its own `when`, `then` and `ratification`, and its own `given` unless it is the parent's word for word; `context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing one there (case 60). Ratifying a parent does not ratify its children.

A question that only asks you to justify a choice already on the table ("why this approach?") does **not** split the Case. A question whose answer requires a new choice with its own consequences ("how will we handle X?") **does**.

**Never move to another Case until the current one is ratified or deferred.**

## What a Case produces

| Outcome | Ledger line |
|---|---|
| ratified decision | `- decision[case 12][update][rule-x]{ref:rule-x}` or `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` |
| a measurement taken | `- estimate[slug][passed\|failed] <result>` |
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
