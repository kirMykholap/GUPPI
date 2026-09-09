---
title: "The remaining `target_kind:` value is `none`, so no value of it collides with a value of `binding:`"
type: decision
status: archived
authority: target-kind-value-set
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: date-scope-the-decision-fields
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "wiki/decisions/_schema.yaml"]
tags: [vault, record-schema, process]
---

# Context

**The session proposed `deferral` as the fifth value of `target_kind:`.** `binding:` already has a
value spelled `deferral` ([[a-decision-declares-whether-it-binds]]), so one page would have carried
the same word twice under two mechanisms.

**One word over two mechanisms is a shape this store has paid for.** It cost three days on
*retrospective* ([[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]]) and it held a live
three-way collision on *frontier* — closed the same day, in the same session
([[the-frontier-is-one-concept-with-three-carriers]]).

# The question

**What is the fifth value, given that a deferral has to be expressible?**

# How it works after

**`none`.** It covers a deferral, a ratification of something already being practised, and any
decision whose product is nothing.

**It is not a new coinage.** The feedback channel already writes `[none]` for an absent destination,
so the word arrives with its meaning attached.

**And the constraint is written into the schema rather than left to be rediscovered**: no value of
`target_kind:` may ever equal a value of `binding:`. A later reader adding a sixth value meets the
rule instead of the collision.

# Recommendation

**Rename before anything is written**, against dropping the value and leaving the field unset for
those decisions. A conditional requirement — *required unless the decision produces nothing* — cannot
live in a per-folder schema, which states keys and values and no conditions.

# Ratification

**The owner selected it**, against dropping the value: «Case 6 : принимаю твою рекомендацию,
ратифицирую».

**He ruled it before either field was written**, so no page ever carried the collision. That is the
first time in this store a word collision was caught in front of the write rather than behind it.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
