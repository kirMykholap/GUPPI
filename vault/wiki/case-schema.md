# Case — schema

`wiki/case-schema.md` — imported into `CLAUDE.md`, so the structure is loaded at session start rather than read as a file.

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
| `ratification` | yes | The human's sign-off, question, or their own alternative. Ends with a preview of the ledger lines in an untagged fence. |

## Operands

In `given`, `when` and `then`, the first line stands alone. Every further line starts with a bold operand: **＋** for one more condition or action, **－** for a limit or an exception. One statement per line.

## Language

Short sentences. One idea per sentence. Active voice. A common word over a term. Russian in the chat with the owner; English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault.

## `when` and `then` are the criterion

The Case that creates a page also creates its Estimate. The Estimate's criterion is the `when` and `then` of the Case, copied without change. Nothing is signed twice, and nothing is signed in two wordings.

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
    estimate:
      slug: estimate-cart-render-time
      kind: Research
      criterion: cart renders within 200ms
      method: measure at 10, 50 and 200 line items
update:
  - slug: entity-checkout
    set: {tags: [cart, checkout, payment]}
    change: the cart precedes payment
```

A `create` holds the fields the target schema needs a judgment for and, for a Leaf, its `estimate`; prose for a body section goes under `sections`, keyed by the section name. An `update` holds `set` (fields), `sections` (the whole new text of a section), `replace` (`old` → `new` inside the body) and `change` (one line for History). A `delete` holds `impact`, a `defer` a `type` and a `purpose`. A Rule-class file (`index.md`, `glossary.md`, this file, a schema, `CLAUDE.md`) is an `update` with `file` and `change`, applied by hand in Work Mode. New tags are declared under `new_tags` with a meaning and a Russian alias.

Derivable fields — `origin`, `status`, `parent` from `ref`, `children`, `code_ref` — are filled mechanically and are not written here. `guppi materialize` reads the blocks, and what is not in a block was signed by nobody.

**The slug is written in the Case**, and pre-task checks it. Meaningful, never an index: `entity-cart`, `lesson-hooks-sessionstart-cannot-block`. The page's category comes from its prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`. Decision pages are the one exception: `decision-case-<N>`, one per Case, written by the script.

## Splitting

If the human's reply to a Case is a follow-up question, the Case was not atomic. Detect this and propose splitting into sub-cases — recursive dotted ids, `1.1`, `1.1.1`. A sub-case is `### Case N.M — name` under its parent, with its own `given`, `when`, `then` and `ratification`; the sections the children share live on the parent. Ratifying a parent does not ratify its children.

A question that only asks you to justify a choice already on the table ("why this approach?") does **not** split the Case. A question whose answer requires a new choice with its own consequences ("how will we handle X?") **does**.

**Never move to another Case until the current one is ratified or deferred.**

## What a Case produces

| Outcome | Ledger line |
|---|---|
| ratified decision | `- decision[case_id][kind][slug]{ref}{source}{supersedes}{tags:a,b}` |
| a measurement taken | `- estimate[slug][passed\|failed] <result>` |
| something learned | `- lesson[error\|knowledge][slug]{tags:a,b} trigger: <...> root_cause: <...>` |

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
