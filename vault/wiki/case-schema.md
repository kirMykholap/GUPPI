# Case — schema

`wiki/case-schema.md` — imported into `CLAUDE.md`, so the structure is loaded at session start rather than read as a file.

A Case is the unit of dialogue, not a vault page. It lives only inside a session. This schema exists because the Case is where content gets ratified: whatever is not in a Case was never signed by anyone.

**One agent response ≈ one Case.**

## Sections

| Section | Required | Content |
|---|---|---|
| `context` | yes | What this is about. In Work Mode this may shrink to a one-line reference back to an earlier Case — the weight scales with what is genuinely new, but it is never omitted. |
| `now` | yes | How things work today, including the pre-task result: what already exists, what conflicts, what sits in `draft`. This is what determines whether the decision can be a `create` at all. |
| `problem` | yes | What requires a decision. |
| `recommend` | yes | The agent's suggestion. Not carried onto the Decision page — if accepted it becomes `then`, if changed then `then` holds the change. |
| `then` | yes | What happens if the recommendation is accepted. **For a `create`, this holds the page draft itself**, laid out per the target category's schema. |
| `ratification` | yes | The human's sign-off, question, or their own alternative. |

## `then` carries the page

Ratifying "create entity-x" without seeing what that page will claim is an empty ratification. The human signs content, not the fact that a decision occurred. So `then` contains the fields the target schema requires — the ones that need human judgment:

```
then:
  slug: entity-cart
  type: entity
  kind: MOC
  purpose: Lets a buyer review an order before paying
  tags: [cart, checkout]
  estimate:
    kind: Research
    criterion: cart renders within 200ms
    method: measure at 10, 50 and 200 line items
```

Derivable fields — `origin`, `status`, `parent`, `children`, `code_ref` — are filled mechanically later and are not written here.

**The slug is written here too**, and pre-task checks it. Meaningful, never an index: `entity-cart`, `decision-create-cart`, `lesson-hooks-sessionstart-cannot-block`.

## Splitting

If the human's reply to a Case is a follow-up question, the Case was not atomic. Detect this and propose splitting into sub-cases — recursive dotted ids, `1.1`, `1.1.1`. Ratifying a parent does not ratify its children.

A question that only asks you to justify a choice already on the table ("why this approach?") does **not** split the Case. A question whose answer requires a new choice with its own consequences ("how will we handle X?") **does**.

**Never move to another Case until the current one is ratified or deferred.**

## What a Case produces

| Outcome | Ledger line |
|---|---|
| ratified decision | `- decision[case_id][kind][slug]{ref}{source}` |
| a measurement taken | `- estimate[slug][passed\|failed] <result>` |
| something learned | `- lesson[error\|knowledge][slug] trigger: <...> root_cause: <...>` |

**Decision lines are markup only** — their content already sits ratified in the Spec, so the
line just names what happens to which page.

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
